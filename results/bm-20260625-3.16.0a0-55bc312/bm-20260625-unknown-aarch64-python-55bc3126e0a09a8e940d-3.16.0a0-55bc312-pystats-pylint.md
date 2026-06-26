
# Pystats results

- benchmark: pylint
- fork: python
- ref: 55bc3126e0a09a8e940da73e51ab1ffeecaf02d4
- commit hash: 55bc312
- commit date: 2026-06-25T18:06:07+00:00

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
<td align="right">273,582,586</td>
<td align="right">17.8%</td>
<td align="right">17.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">66,934,377</td>
<td align="right">4.3%</td>
<td align="right">22.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">64,328,023</td>
<td align="right">4.2%</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">59,244,983</td>
<td align="right">3.8%</td>
<td align="right">30.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">56,403,225</td>
<td align="right">3.7%</td>
<td align="right">33.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">55,049,951</td>
<td align="right">3.6%</td>
<td align="right">37.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">50,043,619</td>
<td align="right">3.3%</td>
<td align="right">40.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">47,347,699</td>
<td align="right">3.1%</td>
<td align="right">43.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">46,577,090</td>
<td align="right">3.0%</td>
<td align="right">46.7%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">40,938,368</td>
<td align="right">2.7%</td>
<td align="right">49.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">34,412,233</td>
<td align="right">2.2%</td>
<td align="right">51.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">34,186,425</td>
<td align="right">2.2%</td>
<td align="right">53.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">32,857,065</td>
<td align="right">2.1%</td>
<td align="right">56.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">29,949,240</td>
<td align="right">1.9%</td>
<td align="right">57.9%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">27,457,140</td>
<td align="right">1.8%</td>
<td align="right">59.7%</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">27,170,945</td>
<td align="right">1.8%</td>
<td align="right">61.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">25,481,526</td>
<td align="right">1.7%</td>
<td align="right">63.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">24,649,593</td>
<td align="right">1.6%</td>
<td align="right">64.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">23,564,700</td>
<td align="right">1.5%</td>
<td align="right">66.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">23,025,347</td>
<td align="right">1.5%</td>
<td align="right">67.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">21,445,513</td>
<td align="right">1.4%</td>
<td align="right">69.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">20,740,700</td>
<td align="right">1.3%</td>
<td align="right">70.5%</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">20,670,100</td>
<td align="right">1.3%</td>
<td align="right">71.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">20,361,380</td>
<td align="right">1.3%</td>
<td align="right">73.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">19,372,339</td>
<td align="right">1.3%</td>
<td align="right">74.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">19,245,045</td>
<td align="right">1.3%</td>
<td align="right">75.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">18,906,138</td>
<td align="right">1.2%</td>
<td align="right">76.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">18,001,739</td>
<td align="right">1.2%</td>
<td align="right">78.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">17,824,980</td>
<td align="right">1.2%</td>
<td align="right">79.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">17,156,960</td>
<td align="right">1.1%</td>
<td align="right">80.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,325,460</td>
<td align="right">1.1%</td>
<td align="right">81.4%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">11,201,860</td>
<td align="right">0.7%</td>
<td align="right">82.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">10,690,359</td>
<td align="right">0.7%</td>
<td align="right">82.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">9,839,420</td>
<td align="right">0.6%</td>
<td align="right">83.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">9,255,660</td>
<td align="right">0.6%</td>
<td align="right">84.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">8,682,639</td>
<td align="right">0.6%</td>
<td align="right">84.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">8,615,200</td>
<td align="right">0.6%</td>
<td align="right">85.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,546,344</td>
<td align="right">0.6%</td>
<td align="right">85.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">8,344,440</td>
<td align="right">0.5%</td>
<td align="right">86.3%</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,229,534</td>
<td align="right">0.5%</td>
<td align="right">86.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">8,105,486</td>
<td align="right">0.5%</td>
<td align="right">87.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,214,773</td>
<td align="right">0.4%</td>
<td align="right">87.8%</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,079,460</td>
<td align="right">0.4%</td>
<td align="right">88.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,027,700</td>
<td align="right">0.4%</td>
<td align="right">88.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,626,700</td>
<td align="right">0.4%</td>
<td align="right">88.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">5,613,520</td>
<td align="right">0.4%</td>
<td align="right">89.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">5,475,600</td>
<td align="right">0.4%</td>
<td align="right">89.6%</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">5,371,680</td>
<td align="right">0.3%</td>
<td align="right">90.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">5,092,220</td>
<td align="right">0.3%</td>
<td align="right">90.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,955,266</td>
<td align="right">0.3%</td>
<td align="right">90.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,583,600</td>
<td align="right">0.3%</td>
<td align="right">90.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">4,448,720</td>
<td align="right">0.3%</td>
<td align="right">91.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">4,393,400</td>
<td align="right">0.3%</td>
<td align="right">91.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,235,660</td>
<td align="right">0.3%</td>
<td align="right">91.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,764,680</td>
<td align="right">0.2%</td>
<td align="right">92.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,755,126</td>
<td align="right">0.2%</td>
<td align="right">92.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,741,127</td>
<td align="right">0.2%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,573,760</td>
<td align="right">0.2%</td>
<td align="right">92.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,284,840</td>
<td align="right">0.2%</td>
<td align="right">93.0%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,246,160</td>
<td align="right">0.2%</td>
<td align="right">93.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,187,780</td>
<td align="right">0.2%</td>
<td align="right">93.4%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,157,400</td>
<td align="right">0.2%</td>
<td align="right">93.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,149,600</td>
<td align="right">0.2%</td>
<td align="right">93.8%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,082,640</td>
<td align="right">0.2%</td>
<td align="right">94.0%</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">2,934,120</td>
<td align="right">0.2%</td>
<td align="right">94.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,786,400</td>
<td align="right">0.2%</td>
<td align="right">94.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,780,600</td>
<td align="right">0.2%</td>
<td align="right">94.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,690,265</td>
<td align="right">0.2%</td>
<td align="right">94.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,687,400</td>
<td align="right">0.2%</td>
<td align="right">94.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,654,827</td>
<td align="right">0.2%</td>
<td align="right">95.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,650,840</td>
<td align="right">0.2%</td>
<td align="right">95.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,623,520</td>
<td align="right">0.2%</td>
<td align="right">95.4%</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">2,532,120</td>
<td align="right">0.2%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,526,760</td>
<td align="right">0.2%</td>
<td align="right">95.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,479,520</td>
<td align="right">0.2%</td>
<td align="right">95.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,354,440</td>
<td align="right">0.2%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,304,320</td>
<td align="right">0.1%</td>
<td align="right">96.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">2,203,040</td>
<td align="right">0.1%</td>
<td align="right">96.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,164,440</td>
<td align="right">0.1%</td>
<td align="right">96.5%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,028,280</td>
<td align="right">0.1%</td>
<td align="right">96.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,980,239</td>
<td align="right">0.1%</td>
<td align="right">96.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,906,200</td>
<td align="right">0.1%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,864,740</td>
<td align="right">0.1%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,825,640</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,813,220</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,743,564</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,717,820</td>
<td align="right">0.1%</td>
<td align="right">97.4%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,679,379</td>
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
<td align="right">1,492,480</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">1,379,980</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,334,480</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,321,960</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">SEND_VIRTUAL</td>
<td align="right">1,303,460</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,282,740</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,238,740</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,230,240</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,198,660</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,167,760</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,155,400</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,141,680</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,112,500</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,098,800</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,065,160</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">983,160</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">944,860</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">859,760</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">775,540</td>
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
<td align="right">710,200</td>
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
<td align="right">640,840</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">620,900</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">617,673</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">613,420</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">610,760</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">586,806</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">476,200</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">457,180</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">435,940</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">431,680</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">401,200</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right">300,560</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">281,720</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_VIRTUAL</td>
<td align="right">261,720</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">258,500</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">255,300</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">254,700</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">227,700</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">225,560</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">216,420</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">198,300</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_EX_PY</td>
<td align="right">177,580</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">174,127</td>
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
<td align="right">162,600</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">154,380</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">150,340</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">139,660</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">133,460</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.1%</td>
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
<td align="right">111,160</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">110,460</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">97,960</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">88,020</td>
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
<td align="right">77,625</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">71,180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">69,020</td>
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
<td align="right">62,780</td>
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
<td align="right">31,180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">26,620</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">11.9%</td>
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
<td align="right">19,920</td>
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
<td align="right">16,380</td>
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
<td align="right">13,340</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">12,400</td>
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
<td align="left">DELETE_FAST</td>
<td align="right">11,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">10,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">9,440</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">9,380</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">6,640</td>
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
<td align="right">4,220</td>
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
<td align="left">UNARY_INVERT</td>
<td align="right">3,660</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">3,400</td>
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
<td align="right">40,439,790</td>
<td align="right">2.6%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_BORROW</td>
<td align="right">36,373,260</td>
<td align="right">2.4%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">33,287,658</td>
<td align="right">2.2%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_BORROW</td>
<td align="right">25,340,503</td>
<td align="right">1.6%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_BORROW</td>
<td align="right">22,722,669</td>
<td align="right">1.5%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">21,787,120</td>
<td align="right">1.4%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">21,122,933</td>
<td align="right">1.4%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE JUMP_BACKWARD_NO_JIT</td>
<td align="right">20,942,186</td>
<td align="right">1.4%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_LIST</td>
<td align="right">20,941,585</td>
<td align="right">1.4%</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">20,676,460</td>
<td align="right">1.3%</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">20,557,433</td>
<td align="right">1.3%</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST_BORROW</td>
<td align="right">20,228,213</td>
<td align="right">1.3%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW</td>
<td align="right">20,189,273</td>
<td align="right">1.3%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT RETURN_VALUE</td>
<td align="right">18,603,293</td>
<td align="right">1.2%</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW PUSH_NULL</td>
<td align="right">17,933,980</td>
<td align="right">1.2%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">17,623,798</td>
<td align="right">1.1%</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST_BORROW</td>
<td align="right">17,616,605</td>
<td align="right">1.1%</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">17,295,605</td>
<td align="right">1.1%</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_PY_EXACT_ARGS</td>
<td align="right">17,234,200</td>
<td align="right">1.1%</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW POP_JUMP_IF_NONE</td>
<td align="right">17,205,940</td>
<td align="right">1.1%</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST</td>
<td align="right">17,169,539</td>
<td align="right">1.1%</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR</td>
<td align="right">16,896,460</td>
<td align="right">1.1%</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE LOAD_FAST_BORROW</td>
<td align="right">16,814,960</td>
<td align="right">1.1%</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST LOAD_FAST_BORROW</td>
<td align="right">16,204,079</td>
<td align="right">1.1%</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">16,029,358</td>
<td align="right">1.0%</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE NOP</td>
<td align="right">15,987,820</td>
<td align="right">1.0%</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">15,199,720</td>
<td align="right">1.0%</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_NON_PY_GENERAL</td>
<td align="right">13,432,620</td>
<td align="right">0.9%</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">COPY TO_BOOL_BOOL</td>
<td align="right">13,319,800</td>
<td align="right">0.9%</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_GLOBAL_MODULE</td>
<td align="right">13,255,959</td>
<td align="right">0.9%</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW COMPARE_OP_STR</td>
<td align="right">12,449,720</td>
<td align="right">0.8%</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE RETURN_VALUE</td>
<td align="right">11,688,880</td>
<td align="right">0.8%</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,650,760</td>
<td align="right">0.8%</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR COPY</td>
<td align="right">11,547,320</td>
<td align="right">0.8%</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_BORROW</td>
<td align="right">11,227,120</td>
<td align="right">0.7%</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,208,160</td>
<td align="right">0.7%</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL TO_BOOL_BOOL</td>
<td align="right">10,959,260</td>
<td align="right">0.7%</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,395,420</td>
<td align="right">0.7%</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_CONST</td>
<td align="right">10,286,740</td>
<td align="right">0.7%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_FAST_BORROW</td>
<td align="right">10,159,240</td>
<td align="right">0.7%</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW RETURN_VALUE</td>
<td align="right">9,805,700</td>
<td align="right">0.6%</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<td align="right">9,392,140</td>
<td align="right">0.6%</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_FAST_BORROW</td>
<td align="right">9,201,280</td>
<td align="right">0.6%</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">8,612,820</td>
<td align="right">0.6%</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE CALL_ISINSTANCE</td>
<td align="right">8,253,820</td>
<td align="right">0.5%</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,775,130</td>
<td align="right">0.5%</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,682,299</td>
<td align="right">0.5%</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,441,065</td>
<td align="right">0.5%</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE</td>
<td align="right">7,255,365</td>
<td align="right">0.5%</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,903,820</td>
<td align="right">0.4%</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_WITH_HINT</td>
<td align="right">6,902,420</td>
<td align="right">0.4%</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_COMMON_CONSTANT</td>
<td align="right">6,793,993</td>
<td align="right">0.4%</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">6,727,639</td>
<td align="right">0.4%</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,709,900</td>
<td align="right">0.4%</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">6,617,380</td>
<td align="right">0.4%</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,525,280</td>
<td align="right">0.4%</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST_BORROW</td>
<td align="right">6,045,372</td>
<td align="right">0.4%</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW POP_JUMP_IF_NOT_NONE</td>
<td align="right">6,034,626</td>
<td align="right">0.4%</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST COMPARE_OP_STR</td>
<td align="right">5,998,300</td>
<td align="right">0.4%</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR POP_JUMP_IF_FALSE</td>
<td align="right">5,817,420</td>
<td align="right">0.4%</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,782,779</td>
<td align="right">0.4%</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE</td>
<td align="right">5,661,060</td>
<td align="right">0.4%</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_SLOT</td>
<td align="right">5,539,480</td>
<td align="right">0.4%</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST_BORROW</td>
<td align="right">5,535,460</td>
<td align="right">0.4%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST</td>
<td align="right">5,298,925</td>
<td align="right">0.3%</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">5,293,673</td>
<td align="right">0.3%</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,995,520</td>
<td align="right">0.3%</td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST POP_ITER</td>
<td align="right">4,835,380</td>
<td align="right">0.3%</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_COMMON_CONSTANT</td>
<td align="right">4,808,440</td>
<td align="right">0.3%</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE TO_BOOL_BOOL</td>
<td align="right">4,756,580</td>
<td align="right">0.3%</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL FOR_ITER_LIST</td>
<td align="right">4,667,980</td>
<td align="right">0.3%</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS RESUME_CHECK</td>
<td align="right">4,500,860</td>
<td align="right">0.3%</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE LOAD_FAST_BORROW</td>
<td align="right">4,499,106</td>
<td align="right">0.3%</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT LOAD_FAST_BORROW</td>
<td align="right">4,438,720</td>
<td align="right">0.3%</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL RESUME_CHECK</td>
<td align="right">4,233,280</td>
<td align="right">0.3%</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST_BORROW</td>
<td align="right">4,192,400</td>
<td align="right">0.3%</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">4,150,120</td>
<td align="right">0.3%</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW CALL_PY_EXACT_ARGS</td>
<td align="right">4,046,200</td>
<td align="right">0.3%</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_BORROW</td>
<td align="right">4,035,460</td>
<td align="right">0.3%</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_COMMON_CONSTANT</td>
<td align="right">4,030,740</td>
<td align="right">0.3%</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE COMPARE_OP_INT</td>
<td align="right">3,931,620</td>
<td align="right">0.3%</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS</td>
<td align="right">3,902,780</td>
<td align="right">0.3%</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">3,887,853</td>
<td align="right">0.3%</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_SMALL_INT</td>
<td align="right">3,845,465</td>
<td align="right">0.2%</td>
<td align="right">63.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS MAKE_CELL</td>
<td align="right">3,801,040</td>
<td align="right">0.2%</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BINARY_OP_SUBSCR_DICT</td>
<td align="right">3,789,920</td>
<td align="right">0.2%</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,623,980</td>
<td align="right">0.2%</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">POP_TOP JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,522,639</td>
<td align="right">0.2%</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">NOP LOAD_COMMON_CONSTANT</td>
<td align="right">3,496,220</td>
<td align="right">0.2%</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">POP_ITER LOAD_FAST_BORROW</td>
<td align="right">3,463,960</td>
<td align="right">0.2%</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE</td>
<td align="right">3,407,980</td>
<td align="right">0.2%</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT STORE_FAST</td>
<td align="right">3,340,493</td>
<td align="right">0.2%</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE</td>
<td align="right">3,300,580</td>
<td align="right">0.2%</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF LOAD_FAST_BORROW</td>
<td align="right">3,297,260</td>
<td align="right">0.2%</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_DEREF</td>
<td align="right">3,289,440</td>
<td align="right">0.2%</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST CALL_KW_PY</td>
<td align="right">3,277,680</td>
<td align="right">0.2%</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_TUPLE</td>
<td align="right">3,235,440</td>
<td align="right">0.2%</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW LOAD_FAST_BORROW</td>
<td align="right">3,231,980</td>
<td align="right">0.2%</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,183,040</td>
<td align="right">0.2%</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">POP_TOP RESUME_CHECK</td>
<td align="right">3,152,120</td>
<td align="right">0.2%</td>
<td align="right">66.6%</td>
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
<td align="right">588,520</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">217,080</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">75,900</td>
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
<td align="right">96,280</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">18,860</td>
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
<td align="right">380,920</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">123,120</td>
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
<td align="right">9,180</td>
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
<td align="right">16,029,358</td>
<td align="right">84.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,302,240</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">502,340</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">73,100</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">66,240</td>
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
<td align="right">531,040</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">152,580</td>
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
<td align="right">1,840</td>
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
<td align="right">5,760</td>
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
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">13,680</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,620</td>
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
<td align="right">1,379,980</td>
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
<td align="right">1,379,980</td>
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
<td align="right">799,700</td>
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
<td align="right">1,492,480</td>
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
<td align="right">431,680</td>
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
<td align="right">431,680</td>
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
<td align="right">427,820</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">297,700</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">152,920</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">111,160</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">56,780</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">608,640</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">486,480</td>
<td align="right">43.7%</td>
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
<td align="right">17,623,798</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,149,400</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">132,940</td>
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
<td align="right">8,480</td>
<td align="right">84.5%</td>
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
<td align="right">10,040</td>
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
<td align="right">4,220</td>
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
<td align="right">4,220</td>
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
<td align="right">1,238,740</td>
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
<td align="right">979,820</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">171,040</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">46,660</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">21,620</td>
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
<td align="right">15,987,820</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,024,880</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,453,300</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,149,540</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">986,860</td>
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
<td align="right">11,208,160</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">3,496,220</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,079,600</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,973,380</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,833,360</td>
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
<td align="right">181,980</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">99,567</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">90,520</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">23,700</td>
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
<td align="right">243,400</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">179,860</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">90,520</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">87,667</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">32,327</td>
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
<td align="right">4,835,380</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,329,100</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">1,379,980</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">687,160</td>
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
<td align="right">3,463,960</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">2,690,020</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,113,700</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">627,880</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">361,300</td>
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
<td align="right">9,392,140</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,739,554</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,705,280</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">2,004,260</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,679,379</td>
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
<td align="right">6,793,993</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,535,460</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,522,639</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,152,120</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,579,800</td>
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
<td align="right">152,640</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">130,860</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">120,540</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">115,760</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">73,100</td>
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
<td align="right">539,427</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">138,540</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,460</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,740</td>
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
<td align="right">17,933,980</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,887,853</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,080,500</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">885,240</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">547,000</td>
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
<td align="right">20,228,213</td>
<td align="right">82.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,290,760</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">883,240</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">326,920</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">260,180</td>
<td align="right">1.1%</td>
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
<td align="right">1,291,420</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">854,880</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">231,920</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">169,240</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">161,680</td>
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
<td align="right">1,618,460</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">885,240</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">133,580</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">132,940</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">108,780</td>
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
<td align="right">18,603,293</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,688,880</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,805,700</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,617,380</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,299,820</td>
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
<td align="right">17,623,798</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,392,140</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,612,820</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,617,380</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,756,580</td>
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
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">56,340</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,880</td>
<td align="right">6.1%</td>
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
<td align="right">65.9%</td>
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
<td align="right">7,280</td>
<td align="right">4.5%</td>
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
<td align="right">226,220</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">213,846</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">61,660</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">16,620</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,680</td>
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
<td align="right">303,380</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">234,206</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">30,560</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,940</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,380</td>
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
<td align="right">238,560</td>
<td align="right">93.4%</td>
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
<td align="right">175,300</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">73,240</td>
<td align="right">28.7%</td>
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
<td align="right">847,760</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">404,480</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">330,660</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">194,460</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">98,220</td>
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
<td align="right">785,940</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">451,580</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">221,460</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">150,480</td>
<td align="right">7.4%</td>
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
<td align="right">2,733,320</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">738,740</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">673,820</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">326,180</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">322,420</td>
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
<td align="right">2,733,540</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,474,940</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">714,160</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">669,260</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">98,300</td>
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
<td align="right">674,960</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">326,560</td>
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
<td align="right">138,700</td>
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
<td align="right">1,349,600</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">282,000</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">98,220</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">69,660</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">35,580</td>
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
<td align="right">486,480</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">134,420</td>
<td align="right">21.6%</td>
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
<td align="right">441,460</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">101,760</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">18,280</td>
<td align="right">2.9%</td>
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
<td align="right">1,173,240</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">984,640</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">683,540</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">538,720</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">386,579</td>
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
<td align="right">1,300,060</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">943,260</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">911,540</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">467,400</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">221,280</td>
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
<td align="right">55,860</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">34,140</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">18,880</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">12,220</td>
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
<td align="right">33,440</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">22,340</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">19,840</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">16,620</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">16,520</td>
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
<td align="right">98,420</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">79,740</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">16,760</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">13,840</td>
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
<td align="right">103,400</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">96,020</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,180</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,460</td>
<td align="right">2.1%</td>
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
<td align="right">19,920</td>
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
<td align="right">5,200</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">3,580</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,880</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,780</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,660</td>
<td align="right">8.3%</td>
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
<td align="right">2,100,260</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">1,356,180</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">143,686</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">34,240</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">25,060</td>
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
<td align="right">2,249,266</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,463,400</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">17,780</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">6,500</td>
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
<td align="right">1,300,060</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">919,060</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">537,900</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">318,840</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">196,460</td>
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
<td align="right">2,261,840</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,035,000</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">201,740</td>
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
<td align="right">109,340</td>
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
<td align="right">111,160</td>
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
<td align="right">11,547,320</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,190,800</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">948,940</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">883,860</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">448,780</td>
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
<td align="right">13,319,800</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">885,220</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">577,700</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">534,560</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">516,820</td>
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
<td align="right">2,302,240</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,502,060</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">492,840</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">115,180</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">74,760</td>
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
<td align="right">4,500,860</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">76,400</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5,600</td>
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
<td align="right">452,300</td>
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
<td align="right">279,580</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">CALL_EX_PY</td>
<td align="right">175,040</td>
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
<td align="right">80</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">100</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">100</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
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
<td align="right">2,158,900</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,777,420</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">409,540</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">400,680</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">275,360</td>
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
<td align="right">2,918,140</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,027,240</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">968,020</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">916,520</td>
<td align="right">15.2%</td>
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
<td align="right">2,009,840</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">916,520</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">380,920</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">368,520</td>
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
<td align="right">2,335,460</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">687,500</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">687,160</td>
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
<td align="right">139,000</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,100</td>
<td align="right">7.4%</td>
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
<td align="right">26,160</td>
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
<td align="right">138,820</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">15,300</td>
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
<td align="right">139,000</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">8,180</td>
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
<td align="right">986,567</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">909,080</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">474,400</td>
<td align="right">17.9%</td>
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
<td align="right">2,145,627</td>
<td align="right">80.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">374,520</td>
<td align="right">14.1%</td>
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
<td align="right">4,680</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,900</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,140</td>
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
<td align="right">16,380</td>
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
<td align="right">1,009,300</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">243,400</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">28,900</td>
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
<td align="right">491,880</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">442,120</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">144,880</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">97,840</td>
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
<td align="right">2,302,960</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">414,200</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">300,120</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">166,320</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">120,680</td>
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
<td align="right">2,268,860</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">271,927</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">225,480</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">209,780</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">199,860</td>
<td align="right">5.3%</td>
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
<td align="right">1,822,860</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">281,740</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">179,220</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">100,860</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">85,120</td>
<td align="right">3.1%</td>
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
<td align="right">2,747,720</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">11,720</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">11,500</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">5,000</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,140</td>
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
<td align="right">23,200</td>
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
<td align="right">13,840</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">12,940</td>
<td align="right">18.7%</td>
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
<td align="right">16,896,460</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">880,960</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">554,100</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">399,840</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">286,420</td>
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
<td align="right">9,201,280</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,180,760</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,171,460</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,130,200</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">849,380</td>
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
<td align="right">6,793,993</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,808,440</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,030,740</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,496,220</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,690,020</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">18,603,293</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,438,720</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,744,020</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,743,340</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">909,080</td>
<td align="right">2.6%</td>
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
<td align="right">10,286,740</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,264,660</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,562,680</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,021,240</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">943,260</td>
<td align="right">4.1%</td>
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
<td align="right">5,998,300</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,277,680</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">2,528,540</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,895,860</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,238,740</td>
<td align="right">5.4%</td>
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
<td align="right">3,289,440</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,099,800</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,833,360</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,014,640</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,011,680</td>
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
<td align="right">3,297,260</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,834,160</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,080,500</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">703,520</td>
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
<td align="right">1,975,973</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,455,280</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,145,660</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">848,487</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">593,840</td>
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
<td align="right">1,503,220</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,356,620</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,227,440</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,190,800</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">998,420</td>
<td align="right">12.1%</td>
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
<td align="right">1,356,620</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,130,200</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">164,440</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">44,060</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">35,220</td>
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
<td align="left">SWAP</td>
<td align="right">2,742,340</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">44,060</td>
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
<td align="right">36,373,260</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">25,340,503</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">22,722,669</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">20,228,213</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">20,189,273</td>
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
<td align="right">40,439,790</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">17,933,980</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,234,200</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">17,205,940</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">16,896,460</td>
<td align="right">6.2%</td>
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
<td align="right">11,208,160</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,903,820</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,709,900</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,995,520</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,623,980</td>
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
<td align="right">20,676,460</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,046,200</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,231,980</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,615,080</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,100,260</td>
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
<td align="right">120,500</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">119,480</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">78,580</td>
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
<td align="right">121,960</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">119,460</td>
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
<td align="right">14,600</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,560</td>
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
<td align="right">3,400</td>
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
<td align="right">3,100</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">300</td>
<td align="right">8.8%</td>
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
<td align="right">28,660</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">26,440</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">25,060</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">11,420</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">11,180</td>
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
<td align="right">49,507</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">35,720</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">31,320</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">29,900</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,440</td>
<td align="right">3.7%</td>
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
<td align="right">31,440</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">15,600</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">10,120</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,660</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,280</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">16,260</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">13,980</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,880</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">11,580</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,660</td>
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
<td align="right">3,845,465</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">549,060</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">525,820</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">518,659</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">419,960</td>
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
<td align="right">1,811,940</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,019,179</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">869,040</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">847,760</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">780,260</td>
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
<td align="right">577,700</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">577,700</td>
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
<td align="right">577,700</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">559,980</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">16,480</td>
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
<td align="right">3,801,040</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,312,100</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">454,960</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">16,320</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">15,220</td>
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
<td align="right">4,233,280</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,312,100</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">60,580</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">7,560</td>
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
<td align="right">6,000</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,740</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,600</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,380</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">620</td>
<td align="right">5.0%</td>
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
<td align="right">7,320</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,680</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">160</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">80</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">60</td>
<td align="right">0.5%</td>
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
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">10,380</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,960</td>
<td align="right">27.6%</td>
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
<td align="right">33,287,658</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,727,639</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,817,420</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,407,980</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,918,140</td>
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
<td align="right">25,340,503</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">11,688,880</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,395,420</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">4,030,740</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,300,580</td>
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
<td align="right">17,205,940</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">231,840</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">219,460</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">81,120</td>
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
<td align="right">16,814,960</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">551,180</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">165,560</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">120,500</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">68,140</td>
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
<td align="right">6,034,626</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,380,280</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">450,400</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">157,940</td>
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
<td align="right">4,499,106</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">986,860</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">919,140</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">476,860</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">459,440</td>
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
<td align="right">21,122,933</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,249,266</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,993,340</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,683,380</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,296,240</td>
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
<td align="right">20,942,186</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,045,372</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,274,520</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,098,620</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">971,820</td>
<td align="right">3.0%</td>
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
<td align="right">111,180</td>
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
<td align="right">103,400</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">90,520</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">77,980</td>
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
<td align="right">88,000</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">79,740</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">14,620</td>
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
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,380</td>
<td align="right">14.0%</td>
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
<td align="right">40</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
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
<td align="right">979,820</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">85,340</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">694,740</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">99,360</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">85,340</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">74,420</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">51,900</td>
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
<td align="right">1,502,720</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">482,040</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">235,760</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">70,160</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,560</td>
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
<td align="right">998,360</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">779,520</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">232,620</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">132,160</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">71,740</td>
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
<td align="right">15,660</td>
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
<td align="right">8,612,820</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">5,298,925</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,340,493</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,725,840</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,621,680</td>
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
<td align="right">20,189,273</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,682,299</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,903,820</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,293,673</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,843,160</td>
<td align="right">5.0%</td>
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
<td align="right">1,448,640</td>
<td align="right">77.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">357,280</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">26,440</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">18,100</td>
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
<td align="right">914,120</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">220,560</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">194,020</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">135,980</td>
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
<td align="right">17,169,539</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,162,880</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">787,580</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">123,820</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">80,980</td>
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
<td align="right">16,204,079</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,226,300</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">787,580</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">720,620</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">236,880</td>
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
<td align="right">32,480</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">30,060</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">26,160</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">21,620</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">19,840</td>
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
<td align="right">75,660</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">31,440</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">20,300</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">17,460</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">15,060</td>
<td align="right">7.6%</td>
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
<td align="right">2,742,340</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,733,540</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,113,700</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">598,640</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">577,700</td>
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
<td align="right">2,733,320</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">2,689,440</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,113,980</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">598,640</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">577,700</td>
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
<td align="right">2,060</td>
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
<td align="right">1,162,880</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,340</td>
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
<td align="right">1,063,600</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">723,520</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">SEND_VIRTUAL</td>
<td align="right">503,760</td>
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
<td align="right">1,493,520</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,149,400</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,101,940</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">448,640</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">179,220</td>
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
<td align="right">16,520</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">13,760</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">7,560</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">5,600</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,080</td>
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
<td align="right">16,600</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">11,180</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,120</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,360</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,860</td>
<td align="right">6.1%</td>
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
<td align="right">869,040</td>
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
<td align="right">78,040</td>
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
<td align="right">1,817,280</td>
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
<td align="right">92,820</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">91,760</td>
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
<td align="right">328,000</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">260,220</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">58,440</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">48,780</td>
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
<td align="right">222,720</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">82,020</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">50,580</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">29,200</td>
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
<td align="right">91,320</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,720</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,000</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,780</td>
<td align="right">5.8%</td>
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
<td align="right">93,820</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">11,180</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,360</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,700</td>
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
<td align="right">6,380</td>
<td align="right">5.1%</td>
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
<td align="right">3,789,920</td>
<td align="right">70.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,195,080</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">132,680</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">112,140</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">41,720</td>
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
<td align="right">1,601,960</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">1,496,180</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,056,380</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">752,700</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">130,860</td>
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
<td align="right">27,665</td>
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
<td align="right">74,445</td>
<td align="right">95.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,980</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">700</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">360</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">60</td>
<td align="right">0.1%</td>
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
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">780,260</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">552,905</td>
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
<td align="right">1,243,240</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">419,960</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">381,625</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">177,960</td>
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
<td align="right">240,040</td>
<td align="right">92.9%</td>
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
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">90,020</td>
<td align="right">34.8%</td>
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
<td align="right">1,811,940</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,280</td>
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
<td align="right">485,360</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">471,680</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">403,060</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">88,500</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">80,540</td>
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
<td align="right">674,020</td>
<td align="right">86.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">36,140</td>
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
<td align="right">210,040</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">135,400</td>
<td align="right">17.5%</td>
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
<td align="right">271,200</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">102,540</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">35,220</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">13,320</td>
<td align="right">3.1%</td>
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
<td align="right">389,480</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">42,780</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,020</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">540</td>
<td align="right">0.1%</td>
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
<td align="right">1,295,360</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">929,460</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">219,240</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">99,680</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">37,160</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">1,938,200</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">492,840</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">169,240</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,440</td>
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
<td align="right">5,700</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,100</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,120</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">200</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">100</td>
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
<td align="right">9,240</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">100</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">80</td>
<td align="right">0.8%</td>
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
<td align="right">145,780</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right">132,820</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">95,800</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">45,680</td>
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
<td align="right">342,320</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">267,080</td>
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
<td align="right">73,380</td>
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
<td align="right">2,615,080</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">460,300</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">436,600</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">368,980</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">207,560</td>
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
<td align="right">2,621,680</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">658,420</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">316,120</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">240,040</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">152,640</td>
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
<td align="right">2,018,460</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">445,260</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">82,220</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">30,720</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">21,420</td>
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
<td align="right">1,459,220</td>
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
<td align="right">159,400</td>
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
<td align="right">487,093</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">28,040</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">25,560</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">24,160</td>
<td align="right">3.9%</td>
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
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">166,540</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">98,200</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">45,680</td>
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
<td align="right">279,580</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">12,440</td>
<td align="right">4.1%</td>
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
<td align="right">132,820</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">79,980</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">47,320</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">35,560</td>
<td align="right">11.8%</td>
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
<td align="right">175,040</td>
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
<td align="right">61,340</td>
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
<td align="right">8,253,820</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,255,365</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,144,460</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">911,540</td>
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
<td align="right">17,295,605</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">948,940</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">853,040</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">116,140</td>
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
<td align="right">613,060</td>
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
<td align="right">580,600</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">27,960</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">4,460</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">280</td>
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
<td align="right">2,528,540</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">3,580</td>
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
<td align="right">1,860,200</td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">230,980</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">166,320</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">111,180</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">84,540</td>
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
<td align="right">3,277,680</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">5,200</td>
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
<td align="right">2,918,880</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">231,920</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">115,180</td>
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
<td align="right">1,443,499</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">153,445</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">45,980</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,740</td>
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
<td align="right">570,240</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">518,659</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">123,400</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">95,800</td>
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
<td align="right">1,246,140</td>
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
<td align="right">53,439</td>
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
<td align="right">1,679,379</td>
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
<td align="right">1,053,120</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">740,880</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">724,400</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">669,260</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">556,500</td>
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
<td align="right">1,593,240</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,299,820</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">986,840</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">590,780</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">264,220</td>
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
<td align="right">109,020</td>
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
<td align="right">45,480</td>
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
<td align="right">2,496,960</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">16,480</td>
<td align="right">0.7%</td>
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
<td align="right">230,300</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">117,260</td>
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
<td align="right">361,500</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">74,440</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">63,460</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">51,980</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">41,720</td>
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
<td align="right">304,580</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">120,540</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">70,500</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">52,380</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">50,120</td>
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
<td align="right">13,432,620</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">863,060</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">756,920</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">425,980</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">326,920</td>
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
<td align="right">10,959,260</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,705,700</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,282,420</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">773,640</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">555,240</td>
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
<td align="right">17,234,200</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,046,200</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,902,780</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">755,720</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">613,400</td>
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
<td align="right">21,787,120</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,801,040</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,502,060</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,485,480</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">1,291,420</td>
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
<td align="right">1,335,480</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">604,760</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">491,000</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">454,680</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">169,840</td>
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
<td align="right">2,382,400</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">454,960</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">161,680</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">107,880</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">74,760</td>
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
<td align="right">21,860</td>
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
<td align="right">10,800</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,060</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,120</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,120</td>
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
<td align="right">109,720</td>
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
<td align="right">107,260</td>
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
<td align="right">766,260</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">327,040</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,180</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,580</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">736,280</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">128,380</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">120,360</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">41,720</td>
<td align="right">3.8%</td>
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
<td align="right">5,720</td>
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
<td align="right">5,720</td>
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
<td align="right">3,931,620</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,109,680</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,019,179</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">703,520</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">472,100</td>
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
<td align="right">6,727,639</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,683,380</td>
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
<td align="right">12,449,720</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,998,300</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,001,780</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">696,680</td>
<td align="right">3.4%</td>
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
<td align="right">11,547,320</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,817,420</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,158,900</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">845,380</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">278,220</td>
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
<td align="right">1,551,420</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">259,400</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">234,360</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">150,480</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">108,800</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,330,640</td>
<td align="right">94.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">76,780</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">51,900</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">10,580</td>
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
<td align="right">848,919</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">318,540</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">277,980</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">260,720</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">115,080</td>
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
<td align="right">861,979</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">792,040</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">193,840</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">69,400</td>
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
<td align="right">2,173,040</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">1,021,820</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">883,240</td>
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
<td align="right">2,226,160</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,004,260</td>
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
<td align="right">20,941,585</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">4,667,980</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">968,020</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">585,760</td>
<td align="right">2.2%</td>
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
<td align="right">15,199,720</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,298,925</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">4,835,380</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,448,640</td>
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
<td align="right">1,065,780</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">123,120</td>
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
<td align="right">1,089,620</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">109,040</td>
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
<td align="right">3,235,440</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">2,130,520</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">256,300</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,600</td>
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
<td align="right">2,725,840</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,329,100</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">357,280</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">213,200</td>
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
<td align="right">249,420</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">12,100</td>
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
<td align="right">246,200</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">12,300</td>
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
<td align="right">1,618,460</td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">267,080</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">163,800</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">97,500</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">34,040</td>
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
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,021,820</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">699,280</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">368,520</td>
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
<td align="right">2,689,440</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,548,700</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,503,220</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,496,180</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">456,700</td>
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
<td align="right">4,667,980</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,130,520</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">854,880</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">811,100</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">146,540</td>
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
<td align="right">20,942,186</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,522,639</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,843,160</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,747,720</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,272,020</td>
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
<td align="right">20,941,585</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">3,235,440</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,400,100</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">2,173,040</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,009,840</td>
<td align="right">5.9%</td>
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
<td align="right">1,634,600</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">36,800</td>
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
<td align="right">1,021,240</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">547,000</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">67,560</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">45,180</td>
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
<td align="right">3,183,040</td>
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
<td align="right">1,356,180</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">724,400</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">544,820</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">538,720</td>
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
<td align="right">40,439,790</td>
<td align="right">86.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,365,180</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,089,260</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">943,780</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">362,700</td>
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
<td align="right">17,616,605</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,661,060</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,383,500</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,365,180</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,264,660</td>
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
<td align="right">11,720</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,080</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">380</td>
<td align="right">2.8%</td>
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
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,200</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">260</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">220</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">180</td>
<td align="right">1.3%</td>
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
<td align="right">5,782,779</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,351,780</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">849,380</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">590,780</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">573,380</td>
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
<td align="right">4,035,460</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,496,960</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,562,680</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">750,160</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">478,959</td>
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
<td align="right">11,650,760</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,834,160</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,981,460</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">998,420</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">914,120</td>
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
<td align="right">11,227,120</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,902,780</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,858,220</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,335,480</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">593,840</td>
<td align="right">2.9%</td>
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
<td align="right">20,557,433</td>
<td align="right">95.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">622,380</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">170,920</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">46,100</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">28,140</td>
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
<td align="right">8,253,820</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,931,620</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,887,853</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,580,500</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">984,640</td>
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
<td align="right">137,660</td>
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
<td align="right">133,980</td>
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
<td align="right">2,782,000</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">242,260</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">40,980</td>
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
<td align="right">1,548,700</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">887,240</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">231,840</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">196,460</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">45,960</td>
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
<td align="right">876,480</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">371,220</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">253,060</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">229,400</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">69,840</td>
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
<td align="right">1,814,460</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">7,440</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,080</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,040</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">200</td>
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
<td align="right">5,539,480</td>
<td align="right">89.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">313,280</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">183,193</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">52,540</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">42,020</td>
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
<td align="right">3,340,493</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">969,840</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">573,380</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">279,580</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">225,840</td>
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
<td align="right">6,902,420</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">647,080</td>
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
<td align="right">99,560</td>
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
<td align="right">1,134,740</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">943,780</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">884,480</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">869,320</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">822,840</td>
<td align="right">9.9%</td>
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
<td align="right">10,395,420</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,775,130</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,682,299</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">7,441,065</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,973,380</td>
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
<td align="right">22,722,669</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">7,255,365</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,995,520</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,289,440</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">883,860</td>
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
<td align="right">13,255,959</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,661,060</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,293,673</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,150,120</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,300,580</td>
<td align="right">7.0%</td>
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
<td align="right">20,557,433</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,192,400</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,183,040</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,050,620</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,003,140</td>
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
<td align="right">2,932,340</td>
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
<td align="right">2,790,560</td>
<td align="right">95.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">98,400</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">32,640</td>
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
<td align="right">21,787,120</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">16,029,358</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,500,860</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,233,280</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,152,120</td>
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
<td align="right">36,373,260</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,775,130</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,709,900</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,150,120</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,705,280</td>
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
<td align="right">810,680</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">491,880</td>
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
<td align="right">799,700</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">503,760</td>
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
<td align="right">20,676,460</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,525,280</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">234,260</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">11,760</td>
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
<td align="right">15,987,820</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">4,808,440</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,623,980</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,329,720</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">857,620</td>
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
<td align="right">271,400</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,120</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,380</td>
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
<td align="right">607,480</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">290,320</td>
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
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,060</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,120</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">400</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">320</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,280</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">2,880</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,000</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">620</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">260</td>
<td align="right">2.8%</td>
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
<td align="right">504,860</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">404,420</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">181,020</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">88,200</td>
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
<td align="right">471,020</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">235,820</td>
<td align="right">19.2%</td>
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
<td align="right">54,660</td>
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
<td align="right">69,880</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">18,140</td>
<td align="right">2.1%</td>
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
<td align="right">73,440</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">19,920</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">9,360</td>
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
<td align="right">2,249,060</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,710,300</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">822,840</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">474,560</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">80,300</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,407,980</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,993,340</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">60,380</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">9,920</td>
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
<td align="right">17,295,605</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">13,319,800</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">10,959,260</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,756,580</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,796,233</td>
<td align="right">3.3%</td>
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
<td align="right">33,287,658</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">21,122,933</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">400,680</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">238,560</td>
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
<td align="right">361,400</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">100,700</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">93,820</td>
<td align="right">7.0%</td>
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
<td align="right">842,800</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">270,800</td>
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
<td align="right">524,840</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">298,200</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">178,080</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">119,240</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">118,640</td>
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
<td align="right">782,300</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">532,020</td>
<td align="right">40.2%</td>
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
<td align="right">1,489,060</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">534,560</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">398,540</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">394,200</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">180,460</td>
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
<td align="right">2,194,660</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">940,400</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">10,040</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,740</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,120</td>
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
<td align="right">969,840</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">516,820</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">194,020</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">173,600</td>
<td align="right">8.0%</td>
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
<td align="right">1,296,240</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">861,680</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,760</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,200</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">380</td>
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
<td align="right">3,980</td>
<td align="right">4.1%</td>
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
<td align="right">80,980</td>
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
<td align="right">15,199,720</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,335,460</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">213,200</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">191,699</td>
<td align="right">1.1%</td>
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
<td align="right">17,169,539</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">826,140</td>
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
<td align="right">2,007,200</td>
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
<td align="right">16,179,510</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">23,360</td>
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
<td align="right">13,900</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,560</td>
<td align="right">35.2%</td>
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
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">1,300</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">1,240</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,100</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">320</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">240</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">220</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">180</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">160</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">160</td>
<td align="right">2.1%</td>
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
<td align="left">subscr mappingproxy</td>
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
<td align="right">944,860</td>
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
<td align="right">7,006,800</td>
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
<td align="right">71,766,501</td>
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
<td align="right">7,005,580</td>
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
<td align="right">224,340</td>
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
<td align="right">11,100</td>
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
<td align="right">3,737,546</td>
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
<td align="right">29,259,479</td>
<td align="right">88.4%</td>
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
<td align="right">12,580</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,860</td>
<td align="right">35.3%</td>
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
<td align="right">2,100</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,820</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">1,520</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">440</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">380</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">340</td>
<td align="right">5.0%</td>
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
<td align="right">3,562,760</td>
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
<td align="right">4,457,039</td>
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
<td align="right">3,540</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,500</td>
<td align="right">67.9%</td>
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
<td align="right">3,160</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,880</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,300</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,160</td>
<td align="right">15.5%</td>
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
<td align="right">3,743,520</td>
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
<td align="right">38,211,625</td>
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
<td align="right">12,800</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,700</td>
<td align="right">40.5%</td>
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
<td align="right">10,814,400</td>
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
<td align="right">3,840</td>
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
<td align="right">13,180</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,340</td>
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
<td align="right">4,340</td>
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
<td align="right">20,022,900</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">104,979,004</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">19,071,171</td>
<td align="right">13.2%</td>
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
<td align="right">468,720</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">78,780</td>
<td align="right">14.4%</td>
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
<td align="right">11,460</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">9,760</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">5,240</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,720</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,820</td>
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
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">400</td>
<td align="right">0.5%</td>
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
<td align="right">320</td>
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
<td align="right">88,900</td>
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
<td align="right">1,180</td>
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
<td align="right">88,241,487</td>
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
<td align="right">44,580</td>
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
<td align="right">85,867</td>
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
<td align="right">2,972,040</td>
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
<td align="right">3,000</td>
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
<td align="right">62,780</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,000</td>
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
<td align="right">2,282,220</td>
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
<td align="right">17,375,380</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,445,580</td>
<td align="right">38.7%</td>
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
<td align="right">247,800</td>
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
<td align="right">42,840</td>
<td align="right">498.1%</td>
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
<td align="right">700</td>
<td align="right">8.1%</td>
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
<td align="right">2,090,000</td>
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
<td align="right">2,080</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">520</td>
<td align="right">20.0%</td>
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
<td align="right">541,086</td>
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
<td align="right">62,243,191</td>
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
<td align="right">4,551,220</td>
<td align="right">6.8%</td>
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
<td align="right">126,720</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,900</td>
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
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">760</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">720</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">520</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">460</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">120</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">80</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">80</td>
<td align="right">2.1%</td>
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
<td align="right">1,163,460</td>
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
<td align="right">18,104,259</td>
<td align="right">93.9%</td>
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
<td align="right">3,800</td>
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
<td align="right">864,774,837</td>
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
<td align="right">39,828,759</td>
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
<td align="right">591,376,403</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">43,386,511</td>
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
<td align="right">20,022,900</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">7,006,800</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,743,520</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,737,546</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,562,760</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,282,220</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,007,200</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,163,460</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">944,860</td>
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
<td align="right">12,445,540</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,689,660</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,083,820</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,829,840</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,773,980</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">3,392,800</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,622,140</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,206,700</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,758,700</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">934,580</td>
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
<td align="right">19,024,138</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">47,641,885</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">19,024,138</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">17,428,398</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">1,595,740</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">3,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">17,414,498</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">10,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">216,465</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">1,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">387,980</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">1,373</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">860,694</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">60,126,363</td>
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
<td align="right">38,710,321</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">38,807,201</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">63,196,065</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">62,694,658</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">285,860</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">215,547</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">53,661,851</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,074,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">363,911,090</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">432,171,655</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">264,268,604</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">259,504,316</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">35,318,531</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">13,502,926</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">297,248,894</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">241,722,121</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">264,760</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">31,020</td>
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
<td align="right">62,894,828</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,831,447</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,053,590</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">28,661,521</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">269,529</td>
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
<td align="right">33,560</td>
<td align="right">96,298,940</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">360</td>
<td align="right">178,680</td>
<td align="right">80,259,140</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">20</td>
<td align="right">920</td>
<td align="right">41,606,792</td>
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
<td align="right">0</td>
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
<td align="right">393,140</td>
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
Stats gathered on: 2026-06-26
