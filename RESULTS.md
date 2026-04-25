# Benchmark results

<!-- START table -->
- [Most recent  pystats on main (95559d2)](results/bm-20260424-3.15.0a8%2B-95559d2/bm-20260424-unknown-aarch64-python-95559d2a7e0071342dff-3.15.0a8%2B-95559d2-pystats.md)
- [Most recent PYTHON_UOPS pystats on main (95559d2)](results/bm-20260424-3.15.0a8%2B-95559d2-PYTHON_UOPS/bm-20260424-unknown-aarch64-python-95559d2a7e0071342dff-3.15.0a8%2B-95559d2-pystats.md)

## linux aarch64 (sulaco)
| date | fork/ref | hash/flags | vs. 3.11.0: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2026-04-24](results/bm-20260424-3.15.0a8%2B-95559d2-JIT) | python/95559d2a7e0071342dff | 95559d2 (JIT) |  |  |  | 1.075x ↑<br>[📄](results/bm-20260424-3.15.0a8%2B-95559d2-JIT/bm-20260424-sulaco-aarch64-python-95559d2a7e0071342dff-3.15.0a8%2B-95559d2-vs-base.md)[📈](results/bm-20260424-3.15.0a8%2B-95559d2-JIT/bm-20260424-sulaco-aarch64-python-95559d2a7e0071342dff-3.15.0a8%2B-95559d2-vs-base.svg)[🧠](results/bm-20260424-3.15.0a8%2B-95559d2-JIT/bm-20260424-sulaco-aarch64-python-95559d2a7e0071342dff-3.15.0a8%2B-95559d2-vs-base-mem.svg) |
| [2026-04-24](results/bm-20260424-3.15.0a8%2B-95559d2) | python/95559d2a7e0071342dff | 95559d2 |  |  |  |  |
| [2026-04-23](results/bm-20260423-3.15.0a8%2B-448d7b9-JIT) | python/448d7b96c181d13ca7f8 | 448d7b9 (JIT) |  |  |  | 1.073x ↑<br>[📄](results/bm-20260423-3.15.0a8%2B-448d7b9-JIT/bm-20260423-sulaco-aarch64-python-448d7b96c181d13ca7f8-3.15.0a8%2B-448d7b9-vs-base.md)[📈](results/bm-20260423-3.15.0a8%2B-448d7b9-JIT/bm-20260423-sulaco-aarch64-python-448d7b96c181d13ca7f8-3.15.0a8%2B-448d7b9-vs-base.svg)[🧠](results/bm-20260423-3.15.0a8%2B-448d7b9-JIT/bm-20260423-sulaco-aarch64-python-448d7b96c181d13ca7f8-3.15.0a8%2B-448d7b9-vs-base-mem.svg) |
| [2026-04-23](results/bm-20260423-3.15.0a8%2B-448d7b9) | python/448d7b96c181d13ca7f8 | 448d7b9 |  |  |  |  |
| [2026-04-22](results/bm-20260422-3.15.0a8%2B-79321fd-JIT) | python/79321fdce3227cf09bb8 | 79321fd (JIT) |  |  |  | 1.085x ↑<br>[📄](results/bm-20260422-3.15.0a8%2B-79321fd-JIT/bm-20260422-sulaco-aarch64-python-79321fdce3227cf09bb8-3.15.0a8%2B-79321fd-vs-base.md)[📈](results/bm-20260422-3.15.0a8%2B-79321fd-JIT/bm-20260422-sulaco-aarch64-python-79321fdce3227cf09bb8-3.15.0a8%2B-79321fd-vs-base.svg)[🧠](results/bm-20260422-3.15.0a8%2B-79321fd-JIT/bm-20260422-sulaco-aarch64-python-79321fdce3227cf09bb8-3.15.0a8%2B-79321fd-vs-base-mem.svg) |
| [2026-04-22](results/bm-20260422-3.15.0a8%2B-79321fd) | python/79321fdce3227cf09bb8 | 79321fd |  |  |  |  |
| [2026-04-21](results/bm-20260421-3.15.0a8%2B-09233bd-JIT) | python/09233bd19879284395af | 09233bd (JIT) |  |  |  | 1.073x ↑<br>[📄](results/bm-20260421-3.15.0a8%2B-09233bd-JIT/bm-20260421-sulaco-aarch64-python-09233bd19879284395af-3.15.0a8%2B-09233bd-vs-base.md)[📈](results/bm-20260421-3.15.0a8%2B-09233bd-JIT/bm-20260421-sulaco-aarch64-python-09233bd19879284395af-3.15.0a8%2B-09233bd-vs-base.svg)[🧠](results/bm-20260421-3.15.0a8%2B-09233bd-JIT/bm-20260421-sulaco-aarch64-python-09233bd19879284395af-3.15.0a8%2B-09233bd-vs-base-mem.svg) |
| [2026-04-21](results/bm-20260421-3.15.0a8%2B-09233bd) | python/09233bd19879284395af | 09233bd |  |  |  |  |
| [2026-04-21](results/bm-20260421-3.15.0a8%2B-d206d42-JIT) | python/d206d42834b2a34aee11 | d206d42 (JIT) |  |  |  | 1.081x ↑<br>[📄](results/bm-20260421-3.15.0a8%2B-d206d42-JIT/bm-20260421-sulaco-aarch64-python-d206d42834b2a34aee11-3.15.0a8%2B-d206d42-vs-base.md)[📈](results/bm-20260421-3.15.0a8%2B-d206d42-JIT/bm-20260421-sulaco-aarch64-python-d206d42834b2a34aee11-3.15.0a8%2B-d206d42-vs-base.svg)[🧠](results/bm-20260421-3.15.0a8%2B-d206d42-JIT/bm-20260421-sulaco-aarch64-python-d206d42834b2a34aee11-3.15.0a8%2B-d206d42-vs-base-mem.svg) |
| [2026-04-21](results/bm-20260421-3.15.0a8%2B-d206d42) | python/d206d42834b2a34aee11 | d206d42 |  |  |  |  |


<!-- END table -->

`*` indicates that the exact same versions of pyperformance was not used.
