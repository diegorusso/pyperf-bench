# Results vs. base

- fork: diegorusso
- ref: add_gdb_support
- machine: linux-aarch64
- commit hash: 6357698
- commit date: 2026-04-16
- overall geometric mean: 1.005x faster
- HPT reliability: 61.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20260330-sulaco-aarch64-python-76c554bcdf53e84c79a5-3.15.0a7+-76c554b | bm-20260416-sulaco-aarch64-diegorusso-add_gdb_support-3.15.0a7+-6357698 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 802 ms                                                                   | 787 ms: 1.02x faster                                                    |
| chameleon      | 49.9 ms                                                                  | 49.3 ms: 1.01x faster                                                   |
| docutils       | 7.47 sec                                                                 | 7.63 sec: 1.02x slower                                                  |
| sphinx         | 3.08 sec                                                                 | 3.11 sec: 1.01x slower                                                  |
| tornado_http   | 278 ms                                                                   | 289 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20260330-sulaco-aarch64-python-76c554bcdf53e84c79a5-3.15.0a7+-76c554b | bm-20260416-sulaco-aarch64-diegorusso-add_gdb_support-3.15.0a7+-6357698 |
|----------------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_eager_tg              | 703 ms                                                                   | 680 ms: 1.03x faster                                                    |
| async_tree_memoization           | 1.04 sec                                                                 | 1.01 sec: 1.03x faster                                                  |
| async_tree_none                  | 845 ms                                                                   | 823 ms: 1.03x faster                                                    |
| async_tree_eager_cpu_io_mixed_tg | 1.61 sec                                                                 | 1.57 sec: 1.02x faster                                                  |
| async_generators                 | 1.36 sec                                                                 | 1.33 sec: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 1.75 sec                                                                 | 1.71 sec: 1.02x faster                                                  |
| async_tree_eager_io              | 1.87 sec                                                                 | 1.83 sec: 1.02x faster                                                  |
| async_tree_io                    | 1.96 sec                                                                 | 1.93 sec: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 1.76 sec                                                                 | 1.73 sec: 1.02x faster                                                  |
| async_tree_memoization_tg        | 1.01 sec                                                                 | 994 ms: 1.01x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 1.31 sec                                                                 | 1.29 sec: 1.01x faster                                                  |
| asyncio_websockets               | 2.22 sec                                                                 | 2.23 sec: 1.00x slower                                                  |
| coroutines                       | 85.6 ms                                                                  | 86.1 ms: 1.01x slower                                                   |
| async_tree_eager                 | 357 ms                                                                   | 360 ms: 1.01x slower                                                    |
| Geometric mean                   | (ref)                                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_io_tg, async_tree_eager_memoization, async_tree_eager_io_tg, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20260330-sulaco-aarch64-python-76c554bcdf53e84c79a5-3.15.0a7+-76c554b | bm-20260416-sulaco-aarch64-diegorusso-add_gdb_support-3.15.0a7+-6357698 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 276 ms                                                                   | 274 ms: 1.01x faster                                                    |
| pidigits       | 736 ms                                                                   | 741 ms: 1.01x slower                                                    |
| float          | 225 ms                                                                   | 228 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20260330-sulaco-aarch64-python-76c554bcdf53e84c79a5-3.15.0a7+-76c554b | bm-20260416-sulaco-aarch64-diegorusso-add_gdb_support-3.15.0a7+-6357698 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 574 ms                                                                   | 558 ms: 1.03x faster                                                    |
| regex_v8       | 91.3 ms                                                                  | 90.2 ms: 1.01x faster                                                   |
| regex_effbot   | 11.6 ms                                                                  | 11.5 ms: 1.01x faster                                                   |
| regex_compile  | 349 ms                                                                   | 350 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20260330-sulaco-aarch64-python-76c554bcdf53e84c79a5-3.15.0a7+-76c554b | bm-20260416-sulaco-aarch64-diegorusso-add_gdb_support-3.15.0a7+-6357698 |
|----------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| base16_small         | 1.28 ms                                                                  | 1.13 ms: 1.13x faster                                                   |
| base85_large         | 27.0 ms                                                                  | 26.9 ms: 1.00x faster                                                   |
| ascii85_large        | 43.7 ms                                                                  | 43.8 ms: 1.00x slower                                                   |
| base32_large         | 9.65 ms                                                                  | 9.67 ms: 1.00x slower                                                   |
| base64_large         | 8.55 ms                                                                  | 8.57 ms: 1.00x slower                                                   |
| xml_etree_generate   | 312 ms                                                                   | 312 ms: 1.00x slower                                                    |
| base16_large         | 27.1 ms                                                                  | 27.2 ms: 1.00x slower                                                   |
| base32_small         | 580 us                                                                   | 584 us: 1.01x slower                                                    |
| tomli_loads          | 5.23 sec                                                                 | 5.27 sec: 1.01x slower                                                  |
| unpickle_pure_python | 723 us                                                                   | 730 us: 1.01x slower                                                    |
| xml_etree_parse      | 506 ms                                                                   | 514 ms: 1.02x slower                                                    |
| xml_etree_process    | 215 ms                                                                   | 219 ms: 1.02x slower                                                    |
| base64_small         | 806 us                                                                   | 821 us: 1.02x slower                                                    |
| urlsafe_base64_small | 988 us                                                                   | 1.02 ms: 1.03x slower                                                   |
| xml_etree_iterparse  | 325 ms                                                                   | 340 ms: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (5): json_loads, pickle_pure_python, json_dumps, ascii85_small, base85_small

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20260330-sulaco-aarch64-python-76c554bcdf53e84c79a5-3.15.0a7+-76c554b | bm-20260416-sulaco-aarch64-diegorusso-add_gdb_support-3.15.0a7+-6357698 |
|------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 35.4 ms                                                                  | 34.7 ms: 1.02x faster                                                   |
| python_startup_no_site | 20.9 ms                                                                  | 21.1 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                    | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20260330-sulaco-aarch64-python-76c554bcdf53e84c79a5-3.15.0a7+-76c554b | bm-20260416-sulaco-aarch64-diegorusso-add_gdb_support-3.15.0a7+-6357698 |
|-----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 39.7 ms                                                                  | 38.9 ms: 1.02x faster                                                   |
| genshi_text     | 82.7 ms                                                                  | 83.1 ms: 1.00x slower                                                   |
| django_template | 118 ms                                                                   | 119 ms: 1.00x slower                                                    |
| Geometric mean  | (ref)                                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20260330-sulaco-aarch64-python-76c554bcdf53e84c79a5-3.15.0a7+-76c554b | bm-20260416-sulaco-aarch64-diegorusso-add_gdb_support-3.15.0a7+-6357698 |
|----------------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| connected_components             | 1.25 sec                                                                 | 1.06 sec: 1.18x faster                                                  |
| k_core                           | 6.21 sec                                                                 | 5.32 sec: 1.17x faster                                                  |
| base16_small                     | 1.28 ms                                                                  | 1.13 ms: 1.13x faster                                                   |
| shortest_path                    | 1.29 sec                                                                 | 1.17 sec: 1.11x faster                                                  |
| gc_traversal                     | 23.8 ms                                                                  | 22.6 ms: 1.05x faster                                                   |
| create_gc_cycles                 | 8.83 ms                                                                  | 8.48 ms: 1.04x faster                                                   |
| async_tree_eager_tg              | 703 ms                                                                   | 680 ms: 1.03x faster                                                    |
| async_tree_memoization           | 1.04 sec                                                                 | 1.01 sec: 1.03x faster                                                  |
| regex_dna                        | 574 ms                                                                   | 558 ms: 1.03x faster                                                    |
| coverage                         | 298 ms                                                                   | 290 ms: 1.03x faster                                                    |
| async_tree_none                  | 845 ms                                                                   | 823 ms: 1.03x faster                                                    |
| typing_runtime_protocols         | 607 us                                                                   | 592 us: 1.02x faster                                                    |
| async_tree_eager_cpu_io_mixed_tg | 1.61 sec                                                                 | 1.57 sec: 1.02x faster                                                  |
| async_generators                 | 1.36 sec                                                                 | 1.33 sec: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 1.75 sec                                                                 | 1.71 sec: 1.02x faster                                                  |
| mako                             | 39.7 ms                                                                  | 38.9 ms: 1.02x faster                                                   |
| async_tree_eager_io              | 1.87 sec                                                                 | 1.83 sec: 1.02x faster                                                  |
| python_startup                   | 35.4 ms                                                                  | 34.7 ms: 1.02x faster                                                   |
| async_tree_io                    | 1.96 sec                                                                 | 1.93 sec: 1.02x faster                                                  |
| pathlib                          | 54.9 ms                                                                  | 53.9 ms: 1.02x faster                                                   |
| 2to3                             | 802 ms                                                                   | 787 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg       | 1.76 sec                                                                 | 1.73 sec: 1.02x faster                                                  |
| pyflate                          | 1.24 sec                                                                 | 1.22 sec: 1.02x faster                                                  |
| scimark_monte_carlo              | 190 ms                                                                   | 187 ms: 1.02x faster                                                    |
| async_tree_memoization_tg        | 1.01 sec                                                                 | 994 ms: 1.01x faster                                                    |
| chameleon                        | 49.9 ms                                                                  | 49.3 ms: 1.01x faster                                                   |
| regex_v8                         | 91.3 ms                                                                  | 90.2 ms: 1.01x faster                                                   |
| chaos                            | 183 ms                                                                   | 180 ms: 1.01x faster                                                    |
| nqueens                          | 262 ms                                                                   | 259 ms: 1.01x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 1.31 sec                                                                 | 1.29 sec: 1.01x faster                                                  |
| meteor_contest                   | 299 ms                                                                   | 296 ms: 1.01x faster                                                    |
| spectral_norm                    | 278 ms                                                                   | 276 ms: 1.01x faster                                                    |
| pprint_safe_repr                 | 2.28 sec                                                                 | 2.26 sec: 1.01x faster                                                  |
| regex_effbot                     | 11.6 ms                                                                  | 11.5 ms: 1.01x faster                                                   |
| json                             | 15.6 ms                                                                  | 15.5 ms: 1.01x faster                                                   |
| nbody                            | 276 ms                                                                   | 274 ms: 1.01x faster                                                    |
| base85_large                     | 27.0 ms                                                                  | 26.9 ms: 1.00x faster                                                   |
| ascii85_large                    | 43.7 ms                                                                  | 43.8 ms: 1.00x slower                                                   |
| base32_large                     | 9.65 ms                                                                  | 9.67 ms: 1.00x slower                                                   |
| base64_large                     | 8.55 ms                                                                  | 8.57 ms: 1.00x slower                                                   |
| xml_etree_generate               | 312 ms                                                                   | 312 ms: 1.00x slower                                                    |
| regex_compile                    | 349 ms                                                                   | 350 ms: 1.00x slower                                                    |
| base16_large                     | 27.1 ms                                                                  | 27.2 ms: 1.00x slower                                                   |
| asyncio_websockets               | 2.22 sec                                                                 | 2.23 sec: 1.00x slower                                                  |
| genshi_text                      | 82.7 ms                                                                  | 83.1 ms: 1.00x slower                                                   |
| django_template                  | 118 ms                                                                   | 119 ms: 1.00x slower                                                    |
| pidigits                         | 736 ms                                                                   | 741 ms: 1.01x slower                                                    |
| base32_small                     | 580 us                                                                   | 584 us: 1.01x slower                                                    |
| sympy_expand                     | 1.36 sec                                                                 | 1.37 sec: 1.01x slower                                                  |
| coroutines                       | 85.6 ms                                                                  | 86.1 ms: 1.01x slower                                                   |
| telco                            | 22.7 ms                                                                  | 22.9 ms: 1.01x slower                                                   |
| mdp                              | 4.34 sec                                                                 | 4.37 sec: 1.01x slower                                                  |
| tomli_loads                      | 5.23 sec                                                                 | 5.27 sec: 1.01x slower                                                  |
| async_tree_eager                 | 357 ms                                                                   | 360 ms: 1.01x slower                                                    |
| unpickle_pure_python             | 723 us                                                                   | 730 us: 1.01x slower                                                    |
| sqlite_synth                     | 9.12 us                                                                  | 9.20 us: 1.01x slower                                                   |
| python_startup_no_site           | 20.9 ms                                                                  | 21.1 ms: 1.01x slower                                                   |
| sphinx                           | 3.08 sec                                                                 | 3.11 sec: 1.01x slower                                                  |
| richards                         | 71.9 ms                                                                  | 72.6 ms: 1.01x slower                                                   |
| deepcopy                         | 823 us                                                                   | 832 us: 1.01x slower                                                    |
| float                            | 225 ms                                                                   | 228 ms: 1.01x slower                                                    |
| richards_super                   | 86.0 ms                                                                  | 87.0 ms: 1.01x slower                                                   |
| scimark_fft                      | 912 ms                                                                   | 923 ms: 1.01x slower                                                    |
| sympy_str                        | 778 ms                                                                   | 789 ms: 1.01x slower                                                    |
| logging_simple                   | 17.8 us                                                                  | 18.1 us: 1.02x slower                                                   |
| bpe_tokeniser                    | 14.3 sec                                                                 | 14.5 sec: 1.02x slower                                                  |
| xml_etree_parse                  | 506 ms                                                                   | 514 ms: 1.02x slower                                                    |
| sympy_integrate                  | 53.4 ms                                                                  | 54.4 ms: 1.02x slower                                                   |
| xml_etree_process                | 215 ms                                                                   | 219 ms: 1.02x slower                                                    |
| base64_small                     | 806 us                                                                   | 821 us: 1.02x slower                                                    |
| sympy_sum                        | 388 ms                                                                   | 396 ms: 1.02x slower                                                    |
| docutils                         | 7.47 sec                                                                 | 7.63 sec: 1.02x slower                                                  |
| go                               | 313 ms                                                                   | 321 ms: 1.03x slower                                                    |
| dask                             | 1.68 sec                                                                 | 1.73 sec: 1.03x slower                                                  |
| fannkuch                         | 1.15 sec                                                                 | 1.18 sec: 1.03x slower                                                  |
| urlsafe_base64_small             | 988 us                                                                   | 1.02 ms: 1.03x slower                                                   |
| logging_silent                   | 275 ns                                                                   | 284 ns: 1.03x slower                                                    |
| tornado_http                     | 278 ms                                                                   | 289 ms: 1.04x slower                                                    |
| scimark_sparse_mat_mult          | 15.4 ms                                                                  | 16.0 ms: 1.04x slower                                                   |
| generators                       | 105 ms                                                                   | 110 ms: 1.04x slower                                                    |
| xml_etree_iterparse              | 325 ms                                                                   | 340 ms: 1.05x slower                                                    |
| scimark_lu                       | 280 ms                                                                   | 295 ms: 1.06x slower                                                    |
| Geometric mean                   | (ref)                                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (35): async_tree_none_tg, async_tree_io_tg, many_optionals, pycparser, crypto_pyaes, async_tree_eager_memoization, deepcopy_reduce, subparsers, logging_format, json_loads, thrift, sqlalchemy_imperative, html5lib, pprint_pformat, pickle_pure_python, json_dumps, scimark_sor, raytrace, deepcopy_memo, ascii85_small, sqlglot_v2_optimize, genshi_xml, dulwich_log, sqlglot_v2_normalize, sqlalchemy_declarative, base85_small, hexiom, pylint, comprehensions, deltablue, async_tree_eager_io_tg, sqlglot_v2_parse, sqlglot_v2_transpile, async_tree_eager_memoization_tg, xdsl_constant_fold

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 61.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x