
# Pystats results

- benchmark: pylint
- fork: python
- ref: 49918f5b0ceb1950c3222fd4fd6be872d2e15c6f
- commit hash: 49918f5
- commit date: 2026-05-07T23:02:04+00:00

## Execution counts

<details>
<summary> Execution counts for Tier 1 instructions. </summary>


The "miss ratio" column shows the percentage of times the instruction
executed that it deoptimized. When this happens, the base unspecialized
instruction is not counted.

<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="right">Count</th>
<th align="right">Self</th>
<th align="right">Cumulative</th>
<th align="right">Miss ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">274,962,496</td>
<td align="right">17.8%</td>
<td align="right">17.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">67,274,893</td>
<td align="right">4.4%</td>
<td align="right">22.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">64,605,759</td>
<td align="right">4.2%</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">59,523,479</td>
<td align="right">3.9%</td>
<td align="right">30.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">56,555,613</td>
<td align="right">3.7%</td>
<td align="right">33.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">55,429,659</td>
<td align="right">3.6%</td>
<td align="right">37.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">50,186,070</td>
<td align="right">3.2%</td>
<td align="right">40.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">47,471,710</td>
<td align="right">3.1%</td>
<td align="right">43.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">47,133,806</td>
<td align="right">3.0%</td>
<td align="right">46.8%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">41,118,603</td>
<td align="right">2.7%</td>
<td align="right">49.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">34,390,133</td>
<td align="right">2.2%</td>
<td align="right">51.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">33,572,193</td>
<td align="right">2.2%</td>
<td align="right">53.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">33,019,639</td>
<td align="right">2.1%</td>
<td align="right">56.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">30,067,680</td>
<td align="right">1.9%</td>
<td align="right">57.9%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">27,554,320</td>
<td align="right">1.8%</td>
<td align="right">59.7%</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">27,357,013</td>
<td align="right">1.8%</td>
<td align="right">61.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">25,508,037</td>
<td align="right">1.6%</td>
<td align="right">63.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">24,835,553</td>
<td align="right">1.6%</td>
<td align="right">64.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">23,941,333</td>
<td align="right">1.5%</td>
<td align="right">66.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">23,651,780</td>
<td align="right">1.5%</td>
<td align="right">67.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">21,499,553</td>
<td align="right">1.4%</td>
<td align="right">69.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">20,833,840</td>
<td align="right">1.3%</td>
<td align="right">70.5%</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">20,824,980</td>
<td align="right">1.3%</td>
<td align="right">71.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">20,251,120</td>
<td align="right">1.3%</td>
<td align="right">73.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">19,515,350</td>
<td align="right">1.3%</td>
<td align="right">74.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">19,354,713</td>
<td align="right">1.3%</td>
<td align="right">75.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">19,045,266</td>
<td align="right">1.2%</td>
<td align="right">76.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">18,145,170</td>
<td align="right">1.2%</td>
<td align="right">78.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">17,951,280</td>
<td align="right">1.2%</td>
<td align="right">79.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">17,287,060</td>
<td align="right">1.1%</td>
<td align="right">80.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,465,120</td>
<td align="right">1.1%</td>
<td align="right">81.5%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">11,232,520</td>
<td align="right">0.7%</td>
<td align="right">82.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">10,698,610</td>
<td align="right">0.7%</td>
<td align="right">82.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">9,886,700</td>
<td align="right">0.6%</td>
<td align="right">83.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">9,301,020</td>
<td align="right">0.6%</td>
<td align="right">84.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">8,679,230</td>
<td align="right">0.6%</td>
<td align="right">84.7%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">8,661,540</td>
<td align="right">0.6%</td>
<td align="right">85.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,541,303</td>
<td align="right">0.6%</td>
<td align="right">85.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">8,314,760</td>
<td align="right">0.5%</td>
<td align="right">86.3%</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,239,614</td>
<td align="right">0.5%</td>
<td align="right">86.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">8,115,323</td>
<td align="right">0.5%</td>
<td align="right">87.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,246,273</td>
<td align="right">0.4%</td>
<td align="right">87.8%</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,091,780</td>
<td align="right">0.4%</td>
<td align="right">88.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,068,000</td>
<td align="right">0.4%</td>
<td align="right">88.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,669,380</td>
<td align="right">0.4%</td>
<td align="right">88.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">5,636,180</td>
<td align="right">0.4%</td>
<td align="right">89.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">5,528,320</td>
<td align="right">0.4%</td>
<td align="right">89.7%</td>
<td align="right">68.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">5,397,880</td>
<td align="right">0.3%</td>
<td align="right">90.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">5,101,360</td>
<td align="right">0.3%</td>
<td align="right">90.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,961,297</td>
<td align="right">0.3%</td>
<td align="right">90.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,592,520</td>
<td align="right">0.3%</td>
<td align="right">91.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">4,448,620</td>
<td align="right">0.3%</td>
<td align="right">91.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">4,407,140</td>
<td align="right">0.3%</td>
<td align="right">91.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,236,360</td>
<td align="right">0.3%</td>
<td align="right">91.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,780,883</td>
<td align="right">0.2%</td>
<td align="right">92.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,765,680</td>
<td align="right">0.2%</td>
<td align="right">92.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,755,747</td>
<td align="right">0.2%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,578,246</td>
<td align="right">0.2%</td>
<td align="right">92.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,293,480</td>
<td align="right">0.2%</td>
<td align="right">93.0%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,280,840</td>
<td align="right">0.2%</td>
<td align="right">93.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,196,240</td>
<td align="right">0.2%</td>
<td align="right">93.4%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,157,360</td>
<td align="right">0.2%</td>
<td align="right">93.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,148,660</td>
<td align="right">0.2%</td>
<td align="right">93.8%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,097,340</td>
<td align="right">0.2%</td>
<td align="right">94.0%</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">2,942,460</td>
<td align="right">0.2%</td>
<td align="right">94.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,802,620</td>
<td align="right">0.2%</td>
<td align="right">94.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,794,480</td>
<td align="right">0.2%</td>
<td align="right">94.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,688,840</td>
<td align="right">0.2%</td>
<td align="right">94.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,684,953</td>
<td align="right">0.2%</td>
<td align="right">94.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,658,057</td>
<td align="right">0.2%</td>
<td align="right">95.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,650,760</td>
<td align="right">0.2%</td>
<td align="right">95.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,625,440</td>
<td align="right">0.2%</td>
<td align="right">95.4%</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">2,541,400</td>
<td align="right">0.2%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,526,960</td>
<td align="right">0.2%</td>
<td align="right">95.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,492,960</td>
<td align="right">0.2%</td>
<td align="right">95.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,354,700</td>
<td align="right">0.2%</td>
<td align="right">96.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,304,860</td>
<td align="right">0.1%</td>
<td align="right">96.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">2,203,360</td>
<td align="right">0.1%</td>
<td align="right">96.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,166,360</td>
<td align="right">0.1%</td>
<td align="right">96.5%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,025,640</td>
<td align="right">0.1%</td>
<td align="right">96.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,978,980</td>
<td align="right">0.1%</td>
<td align="right">96.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,906,040</td>
<td align="right">0.1%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,869,380</td>
<td align="right">0.1%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,824,620</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,817,180</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,741,723</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,716,480</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,680,490</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,499,000</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,492,400</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">1,380,100</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,334,980</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,321,600</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">SEND_VIRTUAL</td>
<td align="right">1,303,320</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,282,620</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,239,400</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,230,380</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,198,600</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,167,800</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,154,880</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,141,680</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,107,580</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,106,720</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,066,200</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">982,780</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">944,840</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">860,240</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">776,220</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">721,534</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">710,120</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">688,254</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">688,254</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">640,660</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">619,053</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">617,000</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">613,920</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">610,800</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">588,463</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">476,020</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">456,940</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">435,720</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">432,740</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">401,180</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right">302,740</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">281,940</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_VIRTUAL</td>
<td align="right">261,680</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">257,500</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">255,900</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">254,640</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">227,740</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">226,140</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">216,760</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">197,360</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_EX_PY</td>
<td align="right">177,560</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">174,887</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">166,080</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">163,200</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">154,320</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">150,260</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">139,480</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">133,320</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">126,360</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">125,260</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">112,040</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">111,140</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">110,300</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">97,940</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">87,680</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">79,560</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">77,613</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">71,160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">68,980</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">68,700</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">62,800</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">60,640</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">37,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">31,160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">26,580</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">23,500</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">19,880</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">19,700</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">18,180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">16,440</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MATCH_CLASS</td>
<td align="right">14,340</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">13,320</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">12,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">11,740</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">11,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">10,520</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">9,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">8,480</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">6,620</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,560</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,460</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">4,180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">4,100</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">4,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,660</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,800</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">580</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">520</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 opcode pairs </summary>


Pairs of specialized operations that deoptimize and are then followed by
the corresponding unspecialized instruction are not counted as pairs.

<table>
<thead>
<tr>
<th align="left">Pair</th>
<th align="right">Count</th>
<th align="right">Self</th>
<th align="right">Cumulative</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">40,965,966</td>
<td align="right">2.6%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_BORROW</td>
<td align="right">36,588,300</td>
<td align="right">2.4%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">33,516,026</td>
<td align="right">2.2%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_BORROW</td>
<td align="right">25,452,059</td>
<td align="right">1.6%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_BORROW</td>
<td align="right">22,827,596</td>
<td align="right">1.5%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">21,877,760</td>
<td align="right">1.4%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">21,271,773</td>
<td align="right">1.4%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE JUMP_BACKWARD_NO_JIT</td>
<td align="right">21,105,243</td>
<td align="right">1.4%</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_LIST</td>
<td align="right">21,099,053</td>
<td align="right">1.4%</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">20,764,240</td>
<td align="right">1.3%</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">20,611,653</td>
<td align="right">1.3%</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST_BORROW</td>
<td align="right">20,389,453</td>
<td align="right">1.3%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW</td>
<td align="right">20,233,910</td>
<td align="right">1.3%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT RETURN_VALUE</td>
<td align="right">18,648,933</td>
<td align="right">1.2%</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW PUSH_NULL</td>
<td align="right">18,106,420</td>
<td align="right">1.2%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST_BORROW</td>
<td align="right">17,778,653</td>
<td align="right">1.1%</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">17,763,786</td>
<td align="right">1.1%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">17,401,193</td>
<td align="right">1.1%</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW POP_JUMP_IF_NONE</td>
<td align="right">17,329,140</td>
<td align="right">1.1%</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_PY_EXACT_ARGS</td>
<td align="right">17,328,900</td>
<td align="right">1.1%</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST</td>
<td align="right">17,312,490</td>
<td align="right">1.1%</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE LOAD_FAST_BORROW</td>
<td align="right">16,941,840</td>
<td align="right">1.1%</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR</td>
<td align="right">16,777,440</td>
<td align="right">1.1%</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST LOAD_FAST_BORROW</td>
<td align="right">16,347,230</td>
<td align="right">1.1%</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">16,161,946</td>
<td align="right">1.0%</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE NOP</td>
<td align="right">16,061,620</td>
<td align="right">1.0%</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">15,347,820</td>
<td align="right">1.0%</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_NON_PY_GENERAL</td>
<td align="right">13,571,740</td>
<td align="right">0.9%</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">COPY TO_BOOL_BOOL</td>
<td align="right">13,447,780</td>
<td align="right">0.9%</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_GLOBAL_MODULE</td>
<td align="right">13,290,890</td>
<td align="right">0.9%</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW COMPARE_OP_STR</td>
<td align="right">12,581,900</td>
<td align="right">0.8%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE RETURN_VALUE</td>
<td align="right">11,811,680</td>
<td align="right">0.8%</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,700,340</td>
<td align="right">0.8%</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR COPY</td>
<td align="right">11,669,440</td>
<td align="right">0.8%</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_BORROW</td>
<td align="right">11,302,740</td>
<td align="right">0.7%</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,259,960</td>
<td align="right">0.7%</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL TO_BOOL_BOOL</td>
<td align="right">11,079,880</td>
<td align="right">0.7%</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,463,020</td>
<td align="right">0.7%</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_CONST</td>
<td align="right">10,388,926</td>
<td align="right">0.7%</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_FAST_BORROW</td>
<td align="right">10,195,420</td>
<td align="right">0.7%</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW RETURN_VALUE</td>
<td align="right">9,848,400</td>
<td align="right">0.6%</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<td align="right">9,413,220</td>
<td align="right">0.6%</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_FAST_BORROW</td>
<td align="right">9,274,600</td>
<td align="right">0.6%</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">8,654,260</td>
<td align="right">0.6%</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE CALL_ISINSTANCE</td>
<td align="right">8,296,020</td>
<td align="right">0.5%</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,803,626</td>
<td align="right">0.5%</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,695,430</td>
<td align="right">0.5%</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,489,773</td>
<td align="right">0.5%</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE</td>
<td align="right">7,308,493</td>
<td align="right">0.5%</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,926,820</td>
<td align="right">0.4%</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_WITH_HINT</td>
<td align="right">6,873,560</td>
<td align="right">0.4%</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,737,880</td>
<td align="right">0.4%</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">6,724,530</td>
<td align="right">0.4%</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">6,667,600</td>
<td align="right">0.4%</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_COMMON_CONSTANT</td>
<td align="right">6,614,133</td>
<td align="right">0.4%</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,537,380</td>
<td align="right">0.4%</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST_BORROW</td>
<td align="right">6,046,009</td>
<td align="right">0.4%</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW POP_JUMP_IF_NOT_NONE</td>
<td align="right">6,044,763</td>
<td align="right">0.4%</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST COMPARE_OP_STR</td>
<td align="right">6,020,980</td>
<td align="right">0.4%</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR POP_JUMP_IF_FALSE</td>
<td align="right">5,818,260</td>
<td align="right">0.4%</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,781,450</td>
<td align="right">0.4%</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE</td>
<td align="right">5,692,740</td>
<td align="right">0.4%</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_SLOT</td>
<td align="right">5,567,020</td>
<td align="right">0.4%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST_BORROW</td>
<td align="right">5,545,260</td>
<td align="right">0.4%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">5,306,233</td>
<td align="right">0.3%</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST</td>
<td align="right">5,304,773</td>
<td align="right">0.3%</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">5,015,920</td>
<td align="right">0.3%</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST POP_ITER</td>
<td align="right">4,863,040</td>
<td align="right">0.3%</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_COMMON_CONSTANT</td>
<td align="right">4,826,680</td>
<td align="right">0.3%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE TO_BOOL_BOOL</td>
<td align="right">4,771,480</td>
<td align="right">0.3%</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL FOR_ITER_LIST</td>
<td align="right">4,694,500</td>
<td align="right">0.3%</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE LOAD_FAST_BORROW</td>
<td align="right">4,510,023</td>
<td align="right">0.3%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS RESUME_CHECK</td>
<td align="right">4,509,880</td>
<td align="right">0.3%</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT LOAD_FAST_BORROW</td>
<td align="right">4,448,040</td>
<td align="right">0.3%</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL RESUME_CHECK</td>
<td align="right">4,255,880</td>
<td align="right">0.3%</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST_BORROW</td>
<td align="right">4,211,740</td>
<td align="right">0.3%</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">4,158,500</td>
<td align="right">0.3%</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW CALL_PY_EXACT_ARGS</td>
<td align="right">4,060,640</td>
<td align="right">0.3%</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_COMMON_CONSTANT</td>
<td align="right">4,049,660</td>
<td align="right">0.3%</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_BORROW</td>
<td align="right">4,036,860</td>
<td align="right">0.3%</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE COMPARE_OP_INT</td>
<td align="right">3,931,680</td>
<td align="right">0.3%</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS</td>
<td align="right">3,908,600</td>
<td align="right">0.3%</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">3,898,433</td>
<td align="right">0.3%</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_SMALL_INT</td>
<td align="right">3,843,853</td>
<td align="right">0.2%</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS MAKE_CELL</td>
<td align="right">3,823,780</td>
<td align="right">0.2%</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BINARY_OP_SUBSCR_DICT</td>
<td align="right">3,815,480</td>
<td align="right">0.2%</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,632,740</td>
<td align="right">0.2%</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">POP_TOP JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,518,430</td>
<td align="right">0.2%</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">NOP LOAD_COMMON_CONSTANT</td>
<td align="right">3,509,060</td>
<td align="right">0.2%</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">POP_ITER LOAD_FAST_BORROW</td>
<td align="right">3,494,320</td>
<td align="right">0.2%</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE</td>
<td align="right">3,445,060</td>
<td align="right">0.2%</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT STORE_FAST</td>
<td align="right">3,368,133</td>
<td align="right">0.2%</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF LOAD_FAST_BORROW</td>
<td align="right">3,305,460</td>
<td align="right">0.2%</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_DEREF</td>
<td align="right">3,297,640</td>
<td align="right">0.2%</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE</td>
<td align="right">3,292,680</td>
<td align="right">0.2%</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST CALL_KW_PY</td>
<td align="right">3,286,340</td>
<td align="right">0.2%</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_TUPLE</td>
<td align="right">3,259,280</td>
<td align="right">0.2%</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW LOAD_FAST_BORROW</td>
<td align="right">3,226,840</td>
<td align="right">0.2%</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,217,700</td>
<td align="right">0.2%</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">POP_TOP RESUME_CHECK</td>
<td align="right">3,152,020</td>
<td align="right">0.2%</td>
<td align="right">66.7%</td>
</tr>
</tbody>
</table>


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each Tier 1 opcode. </summary>


This does not include the unspecialized instructions that occur after a
specialized instruction deoptimizes.

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">588,500</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">217,120</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">75,860</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">16,920</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">16,920</td>
<td align="right">1.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">279,040</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">173,360</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">145,060</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">100,860</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">63,420</td>
<td align="right">6.7%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">580</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">580</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">333,400</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">108,340</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">96,320</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">18,840</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">16,740</td>
<td align="right">2.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">380,940</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">123,100</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">68,480</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,620</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">9,200</td>
<td align="right">1.5%</td>
</tr>
</tbody>
</table>


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">16,161,946</td>
<td align="right">84.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,309,400</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">502,020</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">73,160</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">66,060</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">50,580</td>
<td align="right">83.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">4,720</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,920</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">460</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">440</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60,640</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,240</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">440</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">80</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">40</td>
<td align="right">2.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right">620</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">380</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">CALL_EX_PY</td>
<td align="right">220</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">120</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">80</td>
<td align="right">4.5%</td>
</tr>
</tbody>
</table>


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">531,020</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">152,560</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">33,467</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,300</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,880</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">721,514</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CLEANUP_THROW

<details>
<summary> Successors and predecessors for CLEANUP_THROW </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CACHE</td>
<td align="right">18,180</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">16,760</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,420</td>
<td align="right">7.8%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">51,680</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">13,680</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,740</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">60</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">51,640</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">13,680</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,600</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,920</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">280</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,380,100</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,380,100</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SEND_VIRTUAL</td>
<td align="right">799,620</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">692,360</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,492,400</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">432,740</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">432,740</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">427,940</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">297,140</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">153,600</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">111,140</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">54,780</td>
<td align="right">4.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">606,740</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">482,600</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">13,920</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,460</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### FORMAT_WITH_SPEC

<details>
<summary> Successors and predecessors for FORMAT_WITH_SPEC </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">180</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">180</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">17,763,786</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,148,720</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">132,760</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">8,340</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">440</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">420</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">200</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">120</td>
<td align="right">1.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">9,920</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_LOCALS

<details>
<summary> Successors and predecessors for LOAD_LOCALS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">4,180</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">4,180</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,239,400</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">980,320</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">171,340</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">46,520</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">21,580</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">7,640</td>
<td align="right">0.6%</td>
</tr>
</tbody>
</table>


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">16,061,620</td>
<td align="right">67.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,034,900</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,457,720</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,149,540</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">986,700</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,259,960</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">3,509,060</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,080,120</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,981,940</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,847,860</td>
<td align="right">7.8%</td>
</tr>
</tbody>
</table>


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">284,947</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">181,960</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">99,547</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">90,600</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">23,660</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">243,320</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">179,840</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">90,600</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">87,667</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">32,347</td>
<td align="right">4.7%</td>
</tr>
</tbody>
</table>


</details>

### POP_ITER

<details>
<summary> Successors and predecessors for POP_ITER </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,863,040</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,347,940</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">1,380,100</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">687,760</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">455,020</td>
<td align="right">4.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,494,320</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">2,592,520</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,128,640</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">628,500</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">360,940</td>
<td align="right">3.7%</td>
</tr>
</tbody>
</table>


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">9,413,220</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,744,554</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,705,240</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">2,004,540</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,680,490</td>
<td align="right">6.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">6,614,133</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,545,260</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,518,430</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,152,020</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,580,840</td>
<td align="right">6.2%</td>
</tr>
</tbody>
</table>


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">152,620</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">130,820</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">120,520</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">115,760</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">73,160</td>
<td align="right">10.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">539,407</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">138,520</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,460</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,780</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">967</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">18,106,420</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,898,433</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,080,740</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">885,700</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">546,780</td>
<td align="right">2.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">20,389,453</td>
<td align="right">82.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,304,000</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">883,700</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">407,260</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">326,880</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,291,360</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">855,260</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">231,980</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">169,240</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">161,440</td>
<td align="right">5.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">1,618,220</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">885,700</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">133,520</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">132,760</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">108,760</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">18,648,933</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,811,680</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,848,400</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,667,600</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,307,580</td>
<td align="right">2.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">17,763,786</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,413,220</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,654,260</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,667,600</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,771,480</td>
<td align="right">8.0%</td>
</tr>
</tbody>
</table>


</details>

### SETUP_ANNOTATIONS

<details>
<summary> Successors and predecessors for SETUP_ANNOTATIONS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,100</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20</td>
<td align="right">1.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">980</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">140</td>
<td align="right">12.5%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">79,820</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">56,340</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10,480</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">7,880</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">5,740</td>
<td align="right">3.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">107,140</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">20,520</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">10,220</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">7,480</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">7,020</td>
<td align="right">4.3%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">226,240</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">215,223</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">61,660</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">16,780</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,660</td>
<td align="right">2.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">304,840</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">234,323</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">30,640</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,900</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,400</td>
<td align="right">0.6%</td>
</tr>
</tbody>
</table>


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,760</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">900</td>
<td align="right">24.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">3,660</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">18,980</td>
<td align="right">96.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">700</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">16,920</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,420</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">680</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">640</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">40</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">239,160</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">12,300</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,800</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,500</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">960</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">175,900</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">73,240</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,100</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,800</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">720</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">4,460</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,920</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,300</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">240</td>
<td align="right">5.4%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">847,800</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">403,580</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">328,660</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">195,920</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">98,200</td>
<td align="right">4.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">784,980</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">451,560</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">218,940</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">151,600</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">96,140</td>
<td align="right">4.7%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">2,748,880</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">739,820</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">673,920</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">326,660</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">322,820</td>
<td align="right">5.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">2,749,100</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,474,760</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">714,580</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">670,420</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">98,180</td>
<td align="right">1.6%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">NOP</td>
<td align="right">675,040</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">326,320</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">215,860</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">169,960</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">138,720</td>
<td align="right">7.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,349,400</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">282,040</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">98,200</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">69,660</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">35,640</td>
<td align="right">1.9%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">87,540</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">67,820</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,340</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,380</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,180</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">90,280</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">69,000</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,340</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">760</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">420</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">23,400</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">80</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">20</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">12,360</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,040</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">100</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">482,600</td>
<td align="right">78.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">134,400</td>
<td align="right">21.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">441,580</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">99,740</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,280</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">11,240</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">10,900</td>
<td align="right">1.8%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,173,740</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">986,180</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">683,340</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">545,340</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">388,970</td>
<td align="right">7.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,306,720</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">943,860</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">911,340</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">467,200</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">221,240</td>
<td align="right">4.5%</td>
</tr>
</tbody>
</table>


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">56,160</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">34,080</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">19,240</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">12,260</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,820</td>
<td align="right">4.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">33,480</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">22,360</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">19,800</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">16,780</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">16,600</td>
<td align="right">7.3%</td>
</tr>
</tbody>
</table>


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_ITER</td>
<td align="right">98,800</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">79,800</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">16,760</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">13,820</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">2,800</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RERAISE</td>
<td align="right">103,460</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">96,400</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,180</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,440</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,200</td>
<td align="right">1.5%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">19,880</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">5,180</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">3,560</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,900</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,800</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,640</td>
<td align="right">8.2%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,115,740</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">1,369,820</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">139,883</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">34,280</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">25,540</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,262,983</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,475,460</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">17,780</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">6,520</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,040</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,306,720</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">919,140</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">537,900</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">316,646</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">196,420</td>
<td align="right">5.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,266,326</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,035,040</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">201,700</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">40,080</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">12,400</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">109,320</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,720</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">111,140</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">11,669,440</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,190,380</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">953,020</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">884,320</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">447,960</td>
<td align="right">2.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">13,447,780</td>
<td align="right">77.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">885,640</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">577,440</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">534,120</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">516,680</td>
<td align="right">3.0%</td>
</tr>
</tbody>
</table>


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CACHE</td>
<td align="right">2,309,400</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,501,060</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">492,980</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">115,160</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">75,020</td>
<td align="right">1.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,509,880</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">76,400</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5,500</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">740</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">112,020</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">74,680</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">37,340</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">11,000</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RERAISE</td>
<td align="right">4,460</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">4,260</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,060</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">120</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">40</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_NAME

<details>
<summary> Successors and predecessors for DELETE_NAME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">140</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">100</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">20</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">20</td>
<td align="right">7.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">140</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">60</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">60</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">20</td>
<td align="right">7.1%</td>
</tr>
</tbody>
</table>


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">452,060</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,580</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,320</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,000</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">460</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right">279,360</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">CALL_EX_PY</td>
<td align="right">175,020</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,320</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,240</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">280</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">120</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">40</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">40</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">20</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">300</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">100</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">80</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">20</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,186,400</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,778,400</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">409,540</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">402,580</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">279,400</td>
<td align="right">4.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,947,100</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,032,180</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">970,000</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">916,520</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">105,060</td>
<td align="right">1.7%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,010,320</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">916,520</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">380,940</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">369,020</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">73,120</td>
<td align="right">1.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,335,680</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">687,760</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">687,660</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">26,440</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">8,680</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">138,980</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,040</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">240</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">120,220</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">26,080</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">3,960</td>
<td align="right">2.6%</td>
</tr>
</tbody>
</table>


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">138,800</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">15,260</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">260</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">138,980</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">8,140</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,120</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">992,517</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">909,500</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">472,000</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">148,060</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">35,760</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,150,777</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">372,600</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">79,860</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">29,040</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">11,380</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,700</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,900</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,160</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,360</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,340</td>
<td align="right">8.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">16,440</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,009,240</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">243,320</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">28,920</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,120</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SEND_VIRTUAL</td>
<td align="right">491,820</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">442,120</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">144,820</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">97,820</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">76,420</td>
<td align="right">6.0%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,312,220</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">414,500</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">300,200</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">166,360</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">120,660</td>
<td align="right">3.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,279,020</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">271,927</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">225,560</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">209,800</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">204,380</td>
<td align="right">5.4%</td>
</tr>
</tbody>
</table>


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,834,560</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">281,720</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">179,980</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">100,860</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">85,100</td>
<td align="right">3.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,764,140</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">11,720</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10,480</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">5,000</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,160</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">33,260</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">23,180</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,380</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">3,220</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,780</td>
<td align="right">4.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">33,340</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">13,820</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">12,940</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,160</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,220</td>
<td align="right">3.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,777,440</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">890,420</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">552,300</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">399,880</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">286,580</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,274,600</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,168,500</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,161,040</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,136,000</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">857,060</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_COMMON_CONSTANT

<details>
<summary> Successors and predecessors for LOAD_COMMON_CONSTANT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">6,614,133</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,826,680</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,049,660</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,509,060</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,592,520</td>
<td align="right">7.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">18,648,933</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,448,040</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,744,220</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,730,560</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">909,500</td>
<td align="right">2.7%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">10,388,926</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,271,780</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,562,540</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,020,160</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">943,860</td>
<td align="right">3.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">6,020,980</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,286,340</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">2,537,840</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,895,640</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,239,400</td>
<td align="right">5.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,297,640</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,106,900</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,847,860</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,014,640</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,012,080</td>
<td align="right">9.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,305,460</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,855,640</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,080,740</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">703,660</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">457,480</td>
<td align="right">4.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,983,013</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,460,160</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,146,060</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">848,207</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">593,580</td>
<td align="right">7.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">1,505,060</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,363,380</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,225,380</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,190,380</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,002,280</td>
<td align="right">12.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,363,380</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,136,000</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">164,460</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">44,720</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">38,280</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">2,757,900</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">44,720</td>
<td align="right">1.6%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_BORROW

<details>
<summary> Successors and predecessors for LOAD_FAST_BORROW </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">36,588,300</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">25,452,059</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">22,827,596</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">20,389,453</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">20,233,910</td>
<td align="right">7.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">40,965,966</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18,106,420</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">17,329,140</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,328,900</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">16,777,440</td>
<td align="right">6.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_BORROW_LOAD_FAST_BORROW

<details>
<summary> Successors and predecessors for LOAD_FAST_BORROW_LOAD_FAST_BORROW </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">NOP</td>
<td align="right">11,259,960</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,926,820</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,737,880</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,015,920</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,632,740</td>
<td align="right">7.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">20,764,240</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,060,640</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,226,840</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,630,380</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,115,740</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">120,480</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">119,460</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">78,560</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">77,880</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">36,440</td>
<td align="right">7.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">121,940</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">119,440</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">75,620</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">75,620</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">36,600</td>
<td align="right">7.7%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">121,300</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">32,240</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">28,720</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,620</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,580</td>
<td align="right">5.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">76,700</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">35,360</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">28,740</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">21,700</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">12,360</td>
<td align="right">5.4%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FROM_DICT_OR_GLOBALS

<details>
<summary> Successors and predecessors for LOAD_FROM_DICT_OR_GLOBALS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">4,020</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">3,680</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">300</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">20</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">28,820</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">26,460</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">25,100</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">11,440</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">11,260</td>
<td align="right">6.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">49,527</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">36,000</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">31,540</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">29,920</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,560</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">31,360</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">15,500</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">10,000</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,620</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,280</td>
<td align="right">7.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">16,100</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">14,040</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,760</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">11,600</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,620</td>
<td align="right">11.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SMALL_INT

<details>
<summary> Successors and predecessors for LOAD_SMALL_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,843,853</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">548,940</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">525,820</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">514,750</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">419,300</td>
<td align="right">4.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,815,940</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,015,630</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">868,840</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">847,800</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">774,960</td>
<td align="right">9.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SPECIAL

<details>
<summary> Successors and predecessors for LOAD_SPECIAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">577,440</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">577,440</td>
<td align="right">50.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">577,440</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">559,780</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">16,420</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,240</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,100</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,780</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,360</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">260</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">260</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">220</td>
<td align="right">5.4%</td>
</tr>
</tbody>
</table>


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,823,780</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,312,140</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">454,920</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">16,320</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">15,180</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,255,880</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,312,140</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">60,580</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">7,580</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,320</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,740</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,600</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,380</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">620</td>
<td align="right">5.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,720</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,680</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">160</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">60</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### MATCH_CLASS

<details>
<summary> Successors and predecessors for MATCH_CLASS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">14,340</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">14,340</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">33,516,026</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,724,530</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,818,260</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,445,060</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,947,100</td>
<td align="right">4.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">25,452,059</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">11,811,680</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,463,020</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">4,049,660</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,292,680</td>
<td align="right">4.9%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">17,329,140</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">231,600</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">219,400</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">81,160</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">52,640</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,941,840</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">550,960</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">165,540</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">120,480</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">63,940</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,044,763</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,371,860</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">458,680</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">157,980</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,740</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,510,023</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">986,700</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">918,880</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">476,520</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">459,080</td>
<td align="right">5.7%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">21,271,773</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,262,983</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,008,680</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,683,120</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,297,060</td>
<td align="right">3.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">21,105,243</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,046,009</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,275,420</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,096,240</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">972,020</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">111,160</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">5,860</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,320</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,620</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,080</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">115,760</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">4,460</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,620</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,120</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">103,460</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">90,600</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">78,060</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">4,460</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,260</td>
<td align="right">1.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">88,080</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">79,800</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">14,640</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">100</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">76,420</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">3,020</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">120</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">76,200</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">940</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">940</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">SEND_VIRTUAL</td>
<td align="right">900</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">420</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>


</details>

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">21,120</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,380</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,820</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,100</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">340</td>
<td align="right">1.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">29,860</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,060</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">180</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">20</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">980,320</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">85,880</td>
<td align="right">8.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">695,180</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">99,340</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">85,880</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">74,660</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">51,840</td>
<td align="right">4.9%</td>
</tr>
</tbody>
</table>


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">68,680</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">67,860</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">420</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">260</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">160</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,502,760</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">481,960</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">236,360</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">70,140</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,580</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">998,320</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">779,660</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">232,620</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">132,140</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">71,720</td>
<td align="right">3.1%</td>
</tr>
</tbody>
</table>


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">77,720</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">58,940</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">25,460</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">15,640</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">8,780</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">91,380</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">80,680</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">19,120</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">18,020</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">10,220</td>
<td align="right">4.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,654,260</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">5,304,773</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,368,133</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,750,040</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,637,120</td>
<td align="right">4.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">20,233,910</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,695,430</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,926,820</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,306,233</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,863,820</td>
<td align="right">5.1%</td>
</tr>
</tbody>
</table>


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,453,100</td>
<td align="right">77.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">356,960</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">26,440</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">18,600</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">13,580</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">918,740</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">220,520</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">193,760</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">135,960</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">119,240</td>
<td align="right">6.4%</td>
</tr>
</tbody>
</table>


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">17,312,490</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,162,900</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">787,580</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">123,880</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">80,960</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,347,230</td>
<td align="right">83.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,226,280</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">787,580</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">720,460</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">236,380</td>
<td align="right">1.2%</td>
</tr>
</tbody>
</table>


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">240</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">40</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">20</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">20</td>
<td align="right">6.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">200</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">60</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">20</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">20</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">20</td>
<td align="right">6.2%</td>
</tr>
</tbody>
</table>


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">39,540</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">30,020</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">26,080</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">21,580</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">19,800</td>
<td align="right">10.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">82,400</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">31,360</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">17,300</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">15,040</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">13,140</td>
<td align="right">6.7%</td>
</tr>
</tbody>
</table>


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,757,900</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,749,100</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,128,640</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">598,340</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">577,440</td>
<td align="right">6.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,748,880</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">2,704,360</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,128,920</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">598,340</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">577,440</td>
<td align="right">6.2%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">773,080</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">387,480</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,400</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,100</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">520</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,162,900</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,360</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,064,620</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">723,320</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">SEND_VIRTUAL</td>
<td align="right">503,700</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">448,640</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">243,260</td>
<td align="right">5.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,493,420</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,148,720</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,101,860</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">448,640</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">179,980</td>
<td align="right">4.0%</td>
</tr>
</tbody>
</table>


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL</td>
<td align="right">16,600</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">13,700</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">7,580</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">5,500</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,140</td>
<td align="right">8.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,620</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">11,260</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,000</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,380</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,020</td>
<td align="right">6.4%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">20</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">20</td>
<td align="right">50.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">40</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">868,840</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">755,720</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">755,720</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">140,820</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">78,160</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,818,680</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">279,440</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">97,680</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">92,940</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">91,740</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">327,800</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">260,200</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">58,460</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">48,920</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,960</td>
<td align="right">1.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">249,480</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">222,760</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">82,020</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">50,580</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">29,100</td>
<td align="right">4.1%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_EXTEND

<details>
<summary> Successors and predecessors for BINARY_OP_EXTEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">92,100</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,720</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,740</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">7,140</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,660</td>
<td align="right">2.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">94,580</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">11,180</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,340</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,680</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,880</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">101,760</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">8,680</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">8,080</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,040</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,040</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">72,460</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">16,740</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">14,620</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,600</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">7,940</td>
<td align="right">6.3%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,815,480</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,193,940</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">132,680</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">113,140</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">42,700</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,612,620</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">1,510,620</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,057,300</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">752,520</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">130,820</td>
<td align="right">2.4%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_GETITEM </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">47,800</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">27,653</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,240</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">440</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">240</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">72,613</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,720</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,540</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,020</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">700</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_LIST_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">891,560</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">774,960</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">552,893</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">386,060</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">56,440</td>
<td align="right">2.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,239,800</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">419,300</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">381,273</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">178,080</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">147,920</td>
<td align="right">5.5%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_LIST_SLICE

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_LIST_SLICE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">239,040</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">12,360</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,740</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">360</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">133,240</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">90,020</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,480</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,680</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">5,740</td>
<td align="right">2.2%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_STR_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,045,780</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">239,480</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">212,280</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">460</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">755,720</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">315,300</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">111,840</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">85,100</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">74,860</td>
<td align="right">5.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_TUPLE_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,815,940</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,240</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">485,300</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">471,740</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">403,060</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">88,600</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">80,520</td>
<td align="right">4.4%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">20</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">20</td>
<td align="right">50.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">20</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">20</td>
<td align="right">50.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">674,200</td>
<td align="right">86.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">36,640</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">35,120</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,560</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">8,960</td>
<td align="right">1.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">247,440</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">210,220</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">135,400</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">35,720</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">33,240</td>
<td align="right">4.3%</td>
</tr>
</tbody>
</table>


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">271,020</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">102,500</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">35,240</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">13,280</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">5,740</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">389,460</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">43,880</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,220</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,287,920</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">935,820</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">209,880</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">102,860</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">41,580</td>
<td align="right">1.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,939,680</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">492,980</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">169,240</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,780</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,040</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BOUND_METHOD_GENERAL

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_GENERAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,800</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,100</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,080</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">200</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">100</td>
<td align="right">1.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">8,300</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">80</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">80</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">20</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">312,220</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">145,760</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right">132,640</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">95,780</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">45,620</td>
<td align="right">4.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">342,240</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">266,880</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">115,380</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">108,340</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">73,320</td>
<td align="right">7.5%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,630,380</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">457,800</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">436,600</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">370,260</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">207,420</td>
<td align="right">4.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,637,120</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">658,200</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">316,080</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">239,900</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">152,620</td>
<td align="right">3.5%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,018,600</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">445,120</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">82,260</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">30,720</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">21,400</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,459,240</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">755,720</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">183,193</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">159,320</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">33,294</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">486,533</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">29,040</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">25,560</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">24,660</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">10,160</td>
<td align="right">1.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">245,913</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">168,040</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">98,180</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">45,620</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">29,500</td>
<td align="right">4.8%</td>
</tr>
</tbody>
</table>


</details>

### CALL_EX_NON_PY_GENERAL

<details>
<summary> Successors and predecessors for CALL_EX_NON_PY_GENERAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">279,360</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">14,840</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">7,900</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">620</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_EX_PY</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">132,640</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">82,340</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">47,320</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">35,560</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">2,840</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>


</details>

### CALL_EX_PY

<details>
<summary> Successors and predecessors for CALL_EX_PY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">175,020</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,300</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">220</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">113,800</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">61,320</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">820</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">360</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">8,296,020</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,308,493</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,153,980</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">911,340</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">658,060</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">17,401,193</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">953,020</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">852,980</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">116,100</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,800</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW_BOUND_METHOD

<details>
<summary> Successors and predecessors for CALL_KW_BOUND_METHOD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">613,560</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">580,780</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">28,260</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">4,460</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW_NON_PY

<details>
<summary> Successors and predecessors for CALL_KW_NON_PY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,537,840</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">3,560</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,871,240</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">231,340</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">166,360</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">111,160</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">84,520</td>
<td align="right">3.3%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW_PY

<details>
<summary> Successors and predecessors for CALL_KW_PY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,286,340</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">5,180</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,840</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,927,400</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">231,980</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">115,160</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">16,320</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,840</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,441,110</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">154,953</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">45,780</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,720</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">16,880</td>
<td align="right">1.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">570,380</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">514,750</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">123,900</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">95,780</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">68,900</td>
<td align="right">4.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,246,840</td>
<td align="right">74.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">82,020</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">57,880</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">53,970</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">44,760</td>
<td align="right">2.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,680,490</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,124,320</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">732,180</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">670,420</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">669,540</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">556,780</td>
<td align="right">10.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,593,080</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,307,580</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">986,740</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">591,920</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">265,040</td>
<td align="right">5.2%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">116,340</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">109,000</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">90,080</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">73,660</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,820</td>
<td align="right">1.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">140,100</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">83,600</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">73,400</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">45,460</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">16,880</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,497,220</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">16,420</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">9,360</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,620</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">680</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">977,740</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">696,680</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">333,400</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">230,280</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">117,240</td>
<td align="right">4.6%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">361,540</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">74,380</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">63,460</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">52,000</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">41,600</td>
<td align="right">6.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">304,600</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">120,520</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">70,460</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">52,420</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">50,000</td>
<td align="right">7.8%</td>
</tr>
</tbody>
</table>


</details>

### CALL_NON_PY_GENERAL

<details>
<summary> Successors and predecessors for CALL_NON_PY_GENERAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">13,571,740</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">863,020</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">756,660</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">425,600</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">326,880</td>
<td align="right">2.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,079,880</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,716,240</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,281,960</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">773,580</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">554,980</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">17,328,900</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,060,640</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,908,600</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">755,720</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">608,680</td>
<td align="right">2.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">21,877,760</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,823,780</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,501,060</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,491,440</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">1,291,360</td>
<td align="right">4.3%</td>
</tr>
</tbody>
</table>


</details>

### CALL_PY_GENERAL

<details>
<summary> Successors and predecessors for CALL_PY_GENERAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,336,900</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">604,740</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">490,880</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">461,960</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">169,800</td>
<td align="right">5.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,384,500</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">454,920</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">161,440</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">114,180</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">75,020</td>
<td align="right">2.3%</td>
</tr>
</tbody>
</table>


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">21,820</td>
<td align="right">82.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,660</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,400</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,180</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">320</td>
<td align="right">1.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">10,780</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,060</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,120</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,100</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,700</td>
<td align="right">6.4%</td>
</tr>
</tbody>
</table>


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">109,560</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">340</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">300</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">100</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">107,100</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,580</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">820</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">460</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">340</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">775,020</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">327,020</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,160</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,580</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">744,060</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">125,980</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">120,340</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">42,700</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">37,120</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,700</td>
<td align="right">86.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">880</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">40</td>
<td align="right">0.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,700</td>
<td align="right">86.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">900</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">20</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,931,680</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,109,500</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,015,630</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">703,660</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">471,920</td>
<td align="right">5.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">6,724,530</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,683,120</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">151,560</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">76,840</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">16,740</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">12,581,900</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,020,980</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,001,780</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">696,680</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">111,840</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">11,669,440</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,818,260</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,186,400</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">849,740</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">278,280</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP_DICT

<details>
<summary> Successors and predecessors for CONTAINS_OP_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,564,960</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">259,360</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">234,120</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">151,600</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">108,300</td>
<td align="right">4.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,344,600</td>
<td align="right">94.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">76,280</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">51,900</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">10,560</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,560</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP_SET

<details>
<summary> Successors and predecessors for CONTAINS_OP_SET </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">848,160</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">319,160</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">277,980</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">259,700</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">114,980</td>
<td align="right">5.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">858,920</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">791,940</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">195,140</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">70,000</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">34,800</td>
<td align="right">1.8%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,173,460</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">1,021,640</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">883,700</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">105,060</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">47,680</td>
<td align="right">1.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,226,580</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,004,540</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,840</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">21,099,053</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">4,694,500</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">970,000</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">585,880</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,860</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">15,347,820</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,304,773</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">4,863,040</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,453,100</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">387,480</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,065,740</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">123,100</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">9,400</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,089,580</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">109,020</td>
<td align="right">9.1%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,259,280</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">2,149,040</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">256,560</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,620</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,750,040</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,347,940</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">356,960</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">213,160</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">620</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_VIRTUAL

<details>
<summary> Successors and predecessors for FOR_ITER_VIRTUAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">249,400</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">12,080</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">246,180</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">12,280</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">3,220</td>
<td align="right">1.2%</td>
</tr>
</tbody>
</table>


</details>

### GET_ITER_SELF

<details>
<summary> Successors and predecessors for GET_ITER_SELF </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">1,618,220</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">266,880</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">163,860</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">97,560</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">34,700</td>
<td align="right">1.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,021,640</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">699,280</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">369,020</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">58,400</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">53,800</td>
<td align="right">2.4%</td>
</tr>
</tbody>
</table>


</details>

### GET_ITER_VIRTUAL

<details>
<summary> Successors and predecessors for GET_ITER_VIRTUAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">2,704,360</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,563,180</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,510,620</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,505,060</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">457,340</td>
<td align="right">5.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,694,500</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,149,040</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">855,260</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">811,020</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">147,540</td>
<td align="right">1.7%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD_NO_JIT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_JIT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">21,105,243</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,518,430</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,863,820</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,764,140</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,271,860</td>
<td align="right">6.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">21,099,053</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">3,259,280</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,420,680</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">2,173,460</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,010,320</td>
<td align="right">5.8%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,633,300</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">36,780</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">20,920</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,640</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,580</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,020,160</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">546,780</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">67,560</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">45,160</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,820</td>
<td align="right">0.6%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_CLASS_WITH_METACLASS_CHECK

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS_WITH_METACLASS_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,217,700</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">37,120</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">13,800</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,660</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,440</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,369,820</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">732,180</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">551,440</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">545,340</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">37,140</td>
<td align="right">1.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN

<details>
<summary> Successors and predecessors for LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">11,880</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">160</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,320</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,560</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">160</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">40,965,966</td>
<td align="right">86.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,388,940</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,102,880</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">939,380</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">364,440</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">17,778,653</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,692,740</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,417,260</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,388,940</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,288,260</td>
<td align="right">4.9%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">11,700</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,080</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">380</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">80</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">80</td>
<td align="right">0.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">9,360</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,180</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">260</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">220</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">180</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,781,450</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,352,840</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">857,060</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">591,920</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">573,140</td>
<td align="right">5.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,036,860</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,497,220</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,562,540</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">757,940</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">477,270</td>
<td align="right">4.5%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">11,700,340</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,855,640</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,205,700</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,002,280</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">918,740</td>
<td align="right">4.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">11,302,740</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,908,600</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,870,400</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,336,900</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">593,580</td>
<td align="right">2.8%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">20,611,653</td>
<td align="right">95.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">622,260</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">170,920</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">46,020</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">28,160</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">8,296,020</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,931,680</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,898,433</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,583,720</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">986,180</td>
<td align="right">4.6%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">137,480</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">980</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">480</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">400</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">140</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">133,800</td>
<td align="right">95.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">980</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">940</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">940</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">720</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,796,600</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">242,160</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">41,180</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">6,440</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,340</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">1,563,180</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">887,600</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">231,600</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">196,420</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">45,900</td>
<td align="right">1.5%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">876,020</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">371,180</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">252,860</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">229,160</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">69,820</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,816,980</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">7,380</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,567,020</td>
<td align="right">89.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">316,380</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">183,193</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">53,080</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">41,840</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,368,133</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">969,440</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">573,140</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">279,340</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">225,600</td>
<td align="right">3.6%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,873,560</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">646,740</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">434,960</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">156,960</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">99,140</td>
<td align="right">1.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,137,100</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">939,380</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">889,780</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">851,680</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">803,660</td>
<td align="right">9.7%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,463,020</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,803,626</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,695,430</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">7,489,773</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,981,940</td>
<td align="right">4.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">22,827,596</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">7,308,493</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">5,015,920</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,297,640</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">884,320</td>
<td align="right">2.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">13,290,890</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,692,740</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,306,233</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,158,500</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,292,680</td>
<td align="right">6.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">20,611,653</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,211,740</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,217,700</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,066,000</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,989,280</td>
<td align="right">6.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">37,660</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">260</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">34,100</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,220</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,380</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">220</td>
<td align="right">0.6%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,940,680</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">1,780</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,798,960</td>
<td align="right">95.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">98,380</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">32,600</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">7,980</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,180</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">21,877,760</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">16,161,946</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,509,880</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,255,880</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,152,020</td>
<td align="right">4.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">36,588,300</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,803,626</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,737,880</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,158,500</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,705,240</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">698,620</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">442,120</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">940</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">649,660</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">491,420</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">600</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### SEND_VIRTUAL

<details>
<summary> Successors and predecessors for SEND_VIRTUAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">810,600</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">491,820</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">900</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">END_SEND</td>
<td align="right">799,620</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">503,700</td>
<td align="right">38.6%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">20,764,240</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,537,380</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">231,560</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">11,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,020</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">NOP</td>
<td align="right">16,061,620</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">4,826,680</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,632,740</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,329,480</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">856,960</td>
<td align="right">3.1%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,072,660</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">271,380</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,120</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,660</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">880</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">NOP</td>
<td align="right">1,149,540</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">607,460</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">290,420</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">141,660</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">91,800</td>
<td align="right">3.9%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">4,360</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,180</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,120</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">400</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">320</td>
<td align="right">3.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">4,000</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,280</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,000</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">620</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">260</td>
<td align="right">2.5%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">504,660</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">404,180</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">181,020</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">88,180</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">33,400</td>
<td align="right">2.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">470,880</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">235,580</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">190,160</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">184,360</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">54,620</td>
<td align="right">4.4%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">764,400</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">69,860</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">18,640</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,040</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">3,160</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">755,740</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">73,420</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">19,920</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">9,860</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,288,260</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,729,560</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">803,660</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">476,460</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">91,540</td>
<td align="right">1.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,445,060</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,008,680</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">60,600</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">9,960</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,560</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">17,401,193</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">13,447,780</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">11,079,880</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,771,480</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,793,333</td>
<td align="right">3.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">33,516,026</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">21,271,773</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">402,580</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">239,160</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">658,880</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">361,340</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">100,540</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">94,580</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">76,700</td>
<td align="right">5.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">843,500</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">270,600</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">208,500</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">12,300</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">525,220</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">296,240</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">178,320</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">119,560</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">119,240</td>
<td align="right">9.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">796,380</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">517,580</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">5,280</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">1,800</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">460</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,482,240</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">534,120</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">404,380</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">398,320</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">176,880</td>
<td align="right">5.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,193,140</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">940,980</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">10,060</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,740</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">970,900</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">516,680</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">193,760</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">174,820</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">173,360</td>
<td align="right">8.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,297,060</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">862,760</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,760</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,160</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">3,200</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,040</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">180</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">80</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">60</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,480</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,080</td>
<td align="right">23.7%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">73,100</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">7,080</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,960</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,960</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,360</td>
<td align="right">2.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">80,960</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">10,060</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,660</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,580</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">820</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">15,347,820</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,335,680</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">213,160</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">186,650</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">38,180</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">17,312,490</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">826,620</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">2,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>


</details>

## Specialization stats

<details>
<summary> Specialization stats by family </summary>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,004,760</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,202,766</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">25,840</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">13,840</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,420</td>
<td align="right">34.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">out of range</td>
<td align="right">1,980</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">1,300</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">1,240</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,060</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">320</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">240</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">220</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">180</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">160</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">140</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">120</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">80</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">60</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">60</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">40</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">40</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">40</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">40</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">20</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">20</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">20</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">subscr re match</td>
<td align="right">20</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">20</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">944,840</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,049,740</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">72,000,539</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,048,860</td>
<td align="right">8.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">225,260</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">init not simple</td>
<td align="right">400</td>
<td align="right">400 / 0 !!</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">20</td>
<td align="right">20 / 0 !!</td>
</tr>
</tbody>
</table>


</details>

### CALL_FUNCTION_EX

<details>
<summary> specialization stats for CALL_FUNCTION_EX family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,120</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,200</td>
<td align="right">55.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">880</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW

<details>
<summary> specialization stats for CALL_KW family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">121,840</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">113,020</td>
<td align="right">85.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">11,060</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,763,363</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,410,930</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">99,900</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">12,600</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,780</td>
<td align="right">35.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">baseobject</td>
<td align="right">2,160</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,840</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">1,540</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">400</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">320</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">260</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">100</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">80</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">60</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">20</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP

<details>
<summary> specialization stats for CONTAINS_OP family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,567,246</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,469,220</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,720</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">3,520</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,520</td>
<td align="right">68.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">tuple</td>
<td align="right">3,180</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,900</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,280</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,160</td>
<td align="right">15.4%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,744,500</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,441,013</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">20,340</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">12,820</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,700</td>
<td align="right">40.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dict items</td>
<td align="right">2,560</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">2,080</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,200</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">600</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">480</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">440</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">420</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">340</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">280</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">180</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">100</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">20</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### GET_ITER

<details>
<summary> specialization stats for GET_ITER family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">593,260</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,860,920</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,980</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">13,200</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,360</td>
<td align="right">24.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">other</td>
<td align="right">4,360</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">19,913,080</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">105,749,290</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">19,061,672</td>
<td align="right">13.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">469,060</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">76,720</td>
<td align="right">14.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">class attr simple</td>
<td align="right">11,500</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">9,760</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">5,240</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,720</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,760</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">920</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">500</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">400</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">340</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">340</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">340</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">180</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">140</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">audited slot</td>
<td align="right">140</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">40</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">89,360</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">88,546,173</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">44,140</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">86,107</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,060</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,980,380</td>
<td align="right">99.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">2,040</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### RESUME

<details>
<summary> specialization stats for RESUME family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,060</td>
<td align="right">4.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">62,800</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,060</td>
<td align="right">4.6%</td>
</tr>
</tbody>
</table>


</details>

### SEND

<details>
<summary> specialization stats for SEND family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">77,600</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,141,680</td>
<td align="right">93.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">1,840</td>
<td align="right">93.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">120</td>
<td align="right">6.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,282,480</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,621,580</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,297,960</td>
<td align="right">38.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">245,400</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,600</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">other</td>
<td align="right">40,840</td>
<td align="right">474.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,240</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,820</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">940</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">680</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">520</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">400</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">320</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">220</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">100</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">20</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">20</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">580</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">160,000</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,090,620</td>
<td align="right">92.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">2,680</td>
<td align="right">83.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">520</td>
<td align="right">16.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">bytearray int</td>
<td align="right">260</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">120</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">60</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">20</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">bytearray slice</td>
<td align="right">20</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">542,663</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">62,623,379</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,566,380</td>
<td align="right">6.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">127,100</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,920</td>
<td align="right">3.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">set</td>
<td align="right">1,160</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">760</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">720</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">540</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">460</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">120</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">80</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">80</td>
<td align="right">2.0%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,163,480</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,247,670</td>
<td align="right">94.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">3,820</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">500</td>
<td align="right">11.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sequence</td>
<td align="right">480</td>
<td align="right">96.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">20</td>
<td align="right">4.0%</td>
</tr>
</tbody>
</table>


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>


All entries are execution counts. Should add up to the total number of
Tier 1 instructions executed.

<table>
<thead>
<tr>
<th align="left">Instructions</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">868,417,445</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">39,751,279</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">594,598,252</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">43,290,072</td>
<td align="right">2.8%</td>
</tr>
</tbody>
</table>

### Deferred by instruction

<details>
<summary> Breakdown of deferred (not specialized) instruction counts by family </summary>

<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">19,913,080</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">7,049,740</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,763,363</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,744,500</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,567,246</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,282,480</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,004,760</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,163,480</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">944,840</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">593,260</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>


</details>

### Misses by instruction

<details>
<summary> Breakdown of misses (specialized deopts) instruction counts by family </summary>

<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">12,296,860</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,665,200</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,088,260</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,837,880</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,788,500</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">3,369,700</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,651,480</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,217,300</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,770,360</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">956,280</td>
<td align="right">2.2%</td>
</tr>
</tbody>
</table>


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>


This shows what fraction of calls to Python functions are inlined (i.e.
not having a call at the C level) and for those that are not, where the
call comes from.  The various categories overlap.

Also includes the count of frame objects created.

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">19,163,346</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">47,780,073</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">19,163,346</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">17,568,386</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">1,594,960</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">3,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">17,554,626</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">9,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">218,293</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">1,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">382,240</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">1,373</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">854,714</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">60,404,899</td>
<td align="right">90.2%</td>
</tr>
</tbody>
</table>


</details>

## Object stats

<details>
<summary> Allocations, frees and dict materializatons </summary>


Below, "allocations" means "allocations that are not from a freelist".
Total allocations = "Allocations from freelist" + "Allocations".

"Inline values" is the number of values arrays inlined into objects.

The cache hit/miss numbers are for the MRO cache, split into dunder and
other names.

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">38,770,432</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">38,867,092</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">63,080,425</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">62,578,298</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">285,360</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">216,767</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">53,480,559</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,087,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">368,333,591</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">436,379,057</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">263,730,428</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">259,198,783</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">35,571,739</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">13,533,043</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">297,112,087</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">241,569,400</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">264,620</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">31,300</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (str subclass)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">63,597,798</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,918,859</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">2,436,011</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">28,483,928</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">545,338</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>


Collected/visits gives some measure of efficiency.

<table>
<thead>
<tr>
<th align="right">Generation</th>
<th align="right">Collections</th>
<th align="right">Objects collected</th>
<th align="right">Object visits</th>
<th align="right">Reachable from roots</th>
<th align="right">Not reachable from roots</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right">0</td>
<td align="right">3,860</td>
<td align="right">32,880</td>
<td align="right">98,938,920</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">360</td>
<td align="right">178,320</td>
<td align="right">81,021,580</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">20</td>
<td align="right">920</td>
<td align="right">41,481,994</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
</tbody>
</table>


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>


</details>

## Rare events

<details>
<summary> Counts of rare/unlikely events </summary>

<table>
<thead>
<tr>
<th align="left">Event</th>
<th align="right">Count</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">40</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">240</td>
</tr>
<tr>
<td align="left">
set eval frame func
<details>
<summary>ⓘ</summary>

Setting the PEP 523 frame eval function `_PyInterpreterState_SetFrameEvalFunc()`
</details>
</td>
<td align="right">0</td>
</tr>
<tr>
<td align="left">
builtin dict
<details>
<summary>ⓘ</summary>

Modifying the builtins, `__builtins__.__dict__[var] = ...`
</details>
</td>
<td align="right">0</td>
</tr>
<tr>
<td align="left">
func modification
<details>
<summary>ⓘ</summary>

Modifying a function, e.g. `func.__defaults__ = ...`, etc.
</details>
</td>
<td align="right">5,660</td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">392,500</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">0</td>
</tr>
</tbody>
</table>


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Count</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Number of data files</td>
<td align="right">20</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2026-05-08
