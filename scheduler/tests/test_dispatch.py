import datetime as dt
import importlib.util
from pathlib import Path
import tempfile
import unittest
import urllib.error

SPEC = importlib.util.spec_from_file_location("dispatch", Path(__file__).parents[1] / "dispatch.py")
dispatch = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dispatch)


class FakeGitHub:
    def __init__(self):
        self.existing = None
        self.error = None
        self.posts = 0

    def find_run(self, *args):
        return self.existing

    def dispatch(self, *args):
        self.posts += 1
        if self.error:
            raise self.error
        return {"workflow_run_id": 123, "html_url": "https://example.invalid/runs/123"}


class SlotTests(unittest.TestCase):
    def check_slot(self, workflow, now, expected):
        actual = dispatch.scheduled_slot(workflow, dispatch.parse_time(now))
        self.assertEqual(dispatch.timestamp(actual), expected)

    def test_pin_after_midnight_uses_previous_date(self):
        self.check_slot("pin", "2026-09-17T01:00:00Z", "2026-09-16T23:00:00Z")

    def test_exact_scheduled_instant_is_current_slot(self):
        self.check_slot("nightly", "2026-09-17T01:45:00Z", "2026-09-17T01:45:00Z")

    def test_sunday_before_profiling_uses_previous_week(self):
        self.check_slot("profiling", "2026-09-20T03:59:59Z", "2026-09-13T04:00:00Z")

    def test_profiling_on_monday_catches_up_sunday(self):
        self.check_slot("profiling", "2026-09-21T00:00:00Z", "2026-09-20T04:00:00Z")

    def test_local_timezone_does_not_change_utc_schedule(self):
        self.check_slot("nightly", "2026-09-17T02:44:59+01:00", "2026-09-16T01:45:00Z")

    def test_cutover_requires_explicit_timezone(self):
        with self.assertRaises(ValueError):
            dispatch.parse_time("2026-09-17T01:45:00")


class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.github = FakeGitHub()
        self.slot = dispatch.parse_time("2026-09-17T01:45:00Z")

    def run_slot(self):
        return dispatch.dispatch_once(self.github, "nightly", self.slot, self.root)

    def test_repeated_timer_does_not_dispatch_twice(self):
        first = self.run_slot()
        self.assertEqual(self.run_slot(), first)
        self.assertEqual(self.github.posts, 1)

    def test_existing_run_recovers_missing_local_state(self):
        self.github.existing = {"workflow_run_id": 456}
        self.assertEqual(self.run_slot()["status"], "confirmed")
        self.assertEqual(self.github.posts, 0)

    def test_timeout_is_reconciled_without_resubmission(self):
        self.github.error = urllib.error.URLError("timed out")
        with self.assertRaises(urllib.error.URLError):
            self.run_slot()
        self.github.error = None
        with self.assertRaisesRegex(RuntimeError, "unknown outcome"):
            self.run_slot()
        self.assertEqual(self.github.posts, 1)
        self.github.existing = {"workflow_run_id": 789}
        self.assertEqual(self.run_slot()["status"], "confirmed")
        self.assertEqual(self.github.posts, 1)

    def test_explicit_refusal_can_be_retried(self):
        self.github.error = urllib.error.HTTPError("https://example.invalid", 429, "rate limit", {}, None)
        with self.assertRaises(urllib.error.HTTPError):
            self.run_slot()
        self.github.error = None
        self.assertEqual(self.run_slot()["status"], "accepted")
        self.assertEqual(self.github.posts, 2)

    def test_server_error_does_not_blindly_repeat_post(self):
        self.github.error = urllib.error.HTTPError("https://example.invalid", 502, "gateway", {}, None)
        with self.assertRaises(urllib.error.HTTPError):
            self.run_slot()
        self.github.error = None
        with self.assertRaisesRegex(RuntimeError, "unknown outcome"):
            self.run_slot()
        self.assertEqual(self.github.posts, 1)

    def test_new_slot_can_dispatch_after_previous_success(self):
        self.run_slot()
        self.slot += dt.timedelta(days=1)
        self.run_slot()
        self.assertEqual(self.github.posts, 2)
        self.assertEqual(len(list(self.root.glob("*.json"))), 2)


if __name__ == "__main__":
    unittest.main()
