# Benchmark results

<!-- START table -->
- [Most recent  pystats on main (4b33308)](results/bm-20260418-3.15.0a8%2B-4b33308/bm-20260418-unknown-aarch64-python-4b3330813760a3e3c75c-3.15.0a8%2B-4b33308-pystats.md)
- [Most recent PYTHON_UOPS pystats on main (4b33308)](results/bm-20260418-3.15.0a8%2B-4b33308-PYTHON_UOPS/bm-20260418-unknown-aarch64-python-4b3330813760a3e3c75c-3.15.0a8%2B-4b33308-pystats.md)

## linux aarch64 (sulaco)
| date | fork/ref | hash/flags | vs. 3.11.0: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2026-04-18](results/bm-20260418-3.15.0a8%2B-4b33308) | python/4b3330813760a3e3c75c | 4b33308 |  |  |  |  |
| [2026-04-17](results/bm-20260417-3.15.0a8%2B-db3e990-JIT) | python/db3e990b98fd12fee1bf | db3e990 (JIT) |  |  |  | 1.067x ↑<br>[📄](results/bm-20260417-3.15.0a8%2B-db3e990-JIT/bm-20260417-sulaco-aarch64-python-db3e990b98fd12fee1bf-3.15.0a8%2B-db3e990-vs-base.md)[📈](results/bm-20260417-3.15.0a8%2B-db3e990-JIT/bm-20260417-sulaco-aarch64-python-db3e990b98fd12fee1bf-3.15.0a8%2B-db3e990-vs-base.svg)[🧠](results/bm-20260417-3.15.0a8%2B-db3e990-JIT/bm-20260417-sulaco-aarch64-python-db3e990b98fd12fee1bf-3.15.0a8%2B-db3e990-vs-base-mem.svg) |
| [2026-04-17](results/bm-20260417-3.15.0a8%2B-db3e990) | python/db3e990b98fd12fee1bf | db3e990 |  |  |  |  |
| [2026-04-16](results/bm-20260416-3.15.0a8%2B-2faceee-JIT) | python/2faceeec5c0fb06498a9 | 2faceee (JIT) |  |  |  | 3.237x ↑<br>[📄](results/bm-20260416-3.15.0a8%2B-2faceee-JIT/bm-20260416-sulaco-aarch64-python-2faceeec5c0fb06498a9-3.15.0a8%2B-2faceee-vs-base.md)[📈](results/bm-20260416-3.15.0a8%2B-2faceee-JIT/bm-20260416-sulaco-aarch64-python-2faceeec5c0fb06498a9-3.15.0a8%2B-2faceee-vs-base.svg)[🧠](results/bm-20260416-3.15.0a8%2B-2faceee-JIT/bm-20260416-sulaco-aarch64-python-2faceeec5c0fb06498a9-3.15.0a8%2B-2faceee-vs-base-mem.svg) |
| [2026-04-16](results/bm-20260416-3.15.0a8%2B-2faceee) | python/2faceeec5c0fb06498a9 | 2faceee |  |  |  |  |
| [2026-04-16](results/bm-20260416-3.15.0a7%2B-6357698-JIT) | diegorusso/add_gdb_support | 6357698 (JIT) |  |  |  | 1.005x ↑<br>[📄](results/bm-20260416-3.15.0a7%2B-6357698-JIT/bm-20260416-sulaco-aarch64-diegorusso-add_gdb_support-3.15.0a7%2B-6357698-vs-base.md)[📈](results/bm-20260416-3.15.0a7%2B-6357698-JIT/bm-20260416-sulaco-aarch64-diegorusso-add_gdb_support-3.15.0a7%2B-6357698-vs-base.svg)[🧠](results/bm-20260416-3.15.0a7%2B-6357698-JIT/bm-20260416-sulaco-aarch64-diegorusso-add_gdb_support-3.15.0a7%2B-6357698-vs-base-mem.svg) |
| [2026-03-30](results/bm-20260330-3.15.0a7%2B-76c554b-JIT) | python/76c554bcdf53e84c79a5 | 76c554b (JIT) |  |  |  |  |


<!-- END table -->

`*` indicates that the exact same versions of pyperformance was not used.
