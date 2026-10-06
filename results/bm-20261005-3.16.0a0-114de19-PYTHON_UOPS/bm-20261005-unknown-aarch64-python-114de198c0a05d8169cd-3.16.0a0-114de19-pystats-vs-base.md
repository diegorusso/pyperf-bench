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
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">223,365,614</td>
<td align="right">1</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,889,047,612</td>
<td align="right">181</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,716,663</td>
<td align="right">18</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,617,824</td>
<td align="right">2</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">8,735,322</td>
<td align="right">2</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">417,180,178</td>
<td align="right">217</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">266,020,228</td>
<td align="right">162</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">66,781,561</td>
<td align="right">42</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">451,185,769</td>
<td align="right">284</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">133,616,781</td>
<td align="right">85</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">225,728,391</td>
<td align="right">162</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">124,373,020</td>
<td align="right">96</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">22,506,125</td>
<td align="right">24</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">154,657,018</td>
<td align="right">324</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">493,140,522</td>
<td align="right">1,048</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,170,293</td>
<td align="right">5</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,753,835,325</td>
<td align="right">4,420</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,052,935,685</td>
<td align="right">2,741</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">254,043,707</td>
<td align="right">774</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,746,803</td>
<td align="right">519</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,484,398,650</td>
<td align="right">4,919</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">47,348,162</td>
<td align="right">162</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,749,673,811</td>
<td align="right">6,241</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,618,153,002</td>
<td align="right">9,781</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">195,633,101</td>
<td align="right">767</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">76,450,887</td>
<td align="right">324</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">247,500,913</td>
<td align="right">1,113</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">245,444,139</td>
<td align="right">1,113</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">443,905,467</td>
<td align="right">2,094</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">613,323,844</td>
<td align="right">3,565</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">535,860,796</td>
<td align="right">3,429</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,204,484</td>
<td align="right">68</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,471,901,470</td>
<td align="right">9,844</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">79,715,087</td>
<td align="right">546</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">111,814,221</td>
<td align="right">795</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">346,611,434</td>
<td align="right">2,515</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,394,844,235</td>
<td align="right">10,532</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">77,051,676</td>
<td align="right">636</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,605,726,773</td>
<td align="right">14,599</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">366,030,098</td>
<td align="right">3,359</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,078,911,331</td>
<td align="right">21,091</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">429,740,893</td>
<td align="right">4,547</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,515,353,757</td>
<td align="right">16,211</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">375,257,757</td>
<td align="right">4,104</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">192,690,989</td>
<td align="right">2,342</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,913,253,176</td>
<td align="right">23,258</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">60,083,641</td>
<td align="right">734</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">693,723,255</td>
<td align="right">8,477</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,835,962</td>
<td align="right">735</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,422,921,327</td>
<td align="right">20,210</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">339,504,529</td>
<td align="right">4,838</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,541,306,240</td>
<td align="right">36,317</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">267,307,895</td>
<td align="right">3,996</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,218,510,364</td>
<td align="right">19,672</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">361,401,382</td>
<td align="right">5,863</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">435,092,739</td>
<td align="right">7,172</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,829,668,611</td>
<td align="right">66,800</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">162,116,868</td>
<td align="right">2,838</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">814,871,944</td>
<td align="right">14,390</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,176,076,526</td>
<td align="right">20,772</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,014,181,517</td>
<td align="right">91,603</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,074,503,219</td>
<td align="right">19,737</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">195,333,176</td>
<td align="right">4,016</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">659,463,395</td>
<td align="right">13,948</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,176,255,039</td>
<td align="right">46,906</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">309,718,392</td>
<td align="right">6,735</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">76,026,978</td>
<td align="right">1,693</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">252,874,382</td>
<td align="right">5,703</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">9,184,579</td>
<td align="right">211</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">505,079,404</td>
<td align="right">12,068</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,316,431,764</td>
<td align="right">58,804</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">540,155,250</td>
<td align="right">13,886</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">90,730,490</td>
<td align="right">2,341</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">356,292,166</td>
<td align="right">9,736</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">568,737,034</td>
<td align="right">16,966</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">167,718,670</td>
<td align="right">5,043</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,680,372</td>
<td align="right">232</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">178,435,079</td>
<td align="right">5,633</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">272,775,990</td>
<td align="right">8,986</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,153,591</td>
<td align="right">147</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">117,930,074</td>
<td align="right">4,196</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right">161,901,415</td>
<td align="right">6,288</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">501,889,998</td>
<td align="right">19,683</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">798,424,473</td>
<td align="right">34,194</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">114,848,572</td>
<td align="right">5,049</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">96,953,938</td>
<td align="right">5,047</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">90,905,385</td>
<td align="right">4,836</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">505,185,534</td>
<td align="right">27,878</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">549,764,589</td>
<td align="right">30,767</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">82,344,941</td>
<td align="right">4,665</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,027,406,463</td>
<td align="right">60,528</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,623,028,082</td>
<td align="right">909,686</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">792,386,426</td>
<td align="right">54,968</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">75,587,842</td>
<td align="right">5,335</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">175,919,454</td>
<td align="right">12,462</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">77,895,150</td>
<td align="right">5,645</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">397,286,941</td>
<td align="right">31,696</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">798,167,838</td>
<td align="right">65,261</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">274,553,587</td>
<td align="right">24,168</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">710,646,947</td>
<td align="right">64,676</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">143,537,832</td>
<td align="right">13,609</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,127,433,657</td>
<td align="right">1,155,522</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">90,587,412</td>
<td align="right">9,668</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">SEND_VIRTUAL</td>
<td align="right">2,501,034</td>
<td align="right">315</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">78,404,430</td>
<td align="right">10,800</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,556,200,728</td>
<td align="right">379,481</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">71,956,604</td>
<td align="right">11,816</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,166,500,928</td>
<td align="right">768,513</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,846,904,569</td>
<td align="right">355,382</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,801</td>
<td align="right">1</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">93,740,625</td>
<td align="right">22,541</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_EX_PY</td>
<td align="right">24,412,850</td>
<td align="right">6,186</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,516,347,926</td>
<td align="right">740,019</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,042,209,851</td>
<td align="right">1,837,848</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">709,877,980</td>
<td align="right">366,211</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,179,818,523</td>
<td align="right">758,414</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">917,451,105</td>
<td align="right">724,007</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">501,205,204</td>
<td align="right">412,399</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">409,880,212</td>
<td align="right">361,933</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">408,430,833</td>
<td align="right">369,946</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">380,739,896</td>
<td align="right">370,002</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">14,910,116</td>
<td align="right">17,280</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,821,532</td>
<td align="right">2,213</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">265,017,202</td>
<td align="right">360,427</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">15,651,257</td>
<td align="right">21,394</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">366,673,910</td>
<td align="right">707,538</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">859,874,858</td>
<td align="right">2,136,964</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">36,845,501,409</td>
<td align="right">147,866,401</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,927,597,327</td>
<td align="right">59,875,320</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">220,713</td>
<td align="right">1,446</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,420,557,487</td>
<td align="right">29,143,858</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,533,754,806</td>
<td align="right">58,281,075</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,608,720,708</td>
<td align="right">59,087,771</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,806,551</td>
<td align="right">20,622</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">496,969</td>
<td align="right">6,026</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">4,817,313,825</td>
<td align="right">58,819,543</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,428,915,763</td>
<td align="right">59,078,577</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,685,945,927</td>
<td align="right">60,212,791</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,036,095,189</td>
<td align="right">116,594,695</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">99,355</td>
<td align="right">1,736</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,302,114,470</td>
<td align="right">58,667,811</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">19,020,306</td>
<td align="right">353,503</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">19,020,105</td>
<td align="right">353,502</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">18,640,603</td>
<td align="right">353,502</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">17,123,449</td>
<td align="right">354,106</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,713,424,276</td>
<td align="right">58,337,597</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,934,291,261</td>
<td align="right">58,689,468</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,558,241,518</td>
<td align="right">58,272,889</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">46,334</td>
<td align="right">2,114</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">531,834,818</td>
<td align="right">58,268,148</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">353,560,689</td>
<td align="right">58,272,798</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">238,664,305</td>
<td align="right">58,268,258</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">115,070,726</td>
<td align="right">58,268,160</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_USTR_INT</td>
<td align="right">1,197,580,160</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,029,457,900</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">887,388,264</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">423,511,781</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">189,800,419</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">123,255,849</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">113,712,755</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_VIRTUAL</td>
<td align="right">104,995,414</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND_ASYNC_GEN</td>
<td align="right">100,136,700</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">94,136,760</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">85,937,797</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">77,117,478</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">73,672,526</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">63,645,165</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">42,190,753</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">40,805,084</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">34,033,355</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,660</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,876,620</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,591,479</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,153,910</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">5,768,386</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,736,328</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">2,998,383</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">2,472,571</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,560,387</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">738,891</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">296,792</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">219,420</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">82,540</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">46,485</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">32,804</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">24,682</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">18,732</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,758</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">9,220</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MATCH_CLASS</td>
<td align="right">6,180</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">3,940</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">3,680</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,580</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,760</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK_JIT</td>
<td align="right"></td>
<td align="right">802,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">83,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TRACE_RECORD</td>
<td align="right"></td>
<td align="right">1,428</td>
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

Not included in comparative output.


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each Tier 1 opcode. </summary>


This does not include the unspecialized instructions that occur after a
specialized instruction deoptimizes.

Not included in comparative output.


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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">1,483,843,359</td>
<td align="right">9.7%</td>
<td align="right">3,358</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">60,423,579</td>
<td align="right">0.4%</td>
<td align="right">1,330</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,803,560,245</td>
<td align="right">89.9%</td>
<td align="right">87,812,658</td>
<td align="right">100.0%</td>
<td align="right">-99.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Failure</td>
<td align="right">382,941</td>
<td align="right">22.6%</td>
<td align="right">44</td>
<td align="right">2.8%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,310,454</td>
<td align="right">77.4%</td>
<td align="right">1,524</td>
<td align="right">97.2%</td>
<td align="right">-99.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">out of range</td>
<td align="right">26,794</td>
<td align="right">7.0%</td>
<td align="right">1</td>
<td align="right">2.3%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">18,844</td>
<td align="right">4.9%</td>
<td align="right">19</td>
<td align="right">43.2%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,576</td>
<td align="right">1.7%</td>
<td align="right">12</td>
<td align="right">27.3%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">12</td>
<td align="right">27.3%</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">71,665</td>
<td align="right">18.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">63,595</td>
<td align="right">16.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">35,244</td>
<td align="right">9.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">22,026</td>
<td align="right">5.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">15,723</td>
<td align="right">4.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">15,358</td>
<td align="right">4.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">13,483</td>
<td align="right">3.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">13,160</td>
<td align="right">3.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">12,142</td>
<td align="right">3.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">10,400</td>
<td align="right">2.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">10,214</td>
<td align="right">2.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">7,943</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">7,179</td>
<td align="right">1.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">5,650</td>
<td align="right">1.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">4,833</td>
<td align="right">1.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">4,463</td>
<td align="right">1.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,272</td>
<td align="right">0.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,839</td>
<td align="right">0.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">1,900</td>
<td align="right">0.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,774</td>
<td align="right">0.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,651</td>
<td align="right">0.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">1,340</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">953</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr structtime</td>
<td align="right">840</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">800</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">780</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">540</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">440</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr re match</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">535,860,796</td>
<td align="right">100.0%</td>
<td align="right">3,429</td>
<td align="right">100.0%</td>
<td align="right">-100.0%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">194,377,493</td>
<td align="right">1.7%</td>
<td align="right">12,060</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,229,606,241</td>
<td align="right">98.3%</td>
<td align="right">60,565,925</td>
<td align="right">100.0%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">196,909,273</td>
<td align="right">1.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Failure</td>
<td align="right">906</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,337,425</td>
<td align="right">100.0%</td>
<td align="right">8,562</td>
<td align="right">100.0%</td>
<td align="right">-99.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">init not simple</td>
<td align="right">3,328</td>
<td align="right">367.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">1,186</td>
<td align="right">130.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">941</td>
<td align="right">103.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">11,851</td>
<td align="right">20.4%</td>
<td align="right">282</td>
<td align="right">11.8%</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">35,161</td>
<td align="right">60.4%</td>
<td align="right">1,490</td>
<td align="right">62.2%</td>
<td align="right">-95.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">23,024</td>
<td align="right">100.0%</td>
<td align="right">906</td>
<td align="right">100.0%</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">288,523</td>
<td align="right">84.1%</td>
<td align="right">815</td>
<td align="right">56.4%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">122,388</td>
<td align="right">35.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Failure</td>
<td align="right">280</td>
<td align="right">0.5%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">54,298</td>
<td align="right">99.5%</td>
<td align="right">631</td>
<td align="right">100.0%</td>
<td align="right">-98.8%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">539,924,193</td>
<td align="right">10.7%</td>
<td align="right">9,247</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,184,298</td>
<td align="right">0.0%</td>
<td align="right">302</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,507,767,170</td>
<td align="right">89.3%</td>
<td align="right">58,351,894</td>
<td align="right">100.0%</td>
<td align="right">-98.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Failure</td>
<td align="right">160,397</td>
<td align="right">63.4%</td>
<td align="right">342</td>
<td align="right">7.4%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">92,715</td>
<td align="right">36.6%</td>
<td align="right">4,303</td>
<td align="right">92.6%</td>
<td align="right">-95.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">tuple</td>
<td align="right">47,646</td>
<td align="right">29.7%</td>
<td align="right">12</td>
<td align="right">3.5%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">22,725</td>
<td align="right">14.2%</td>
<td align="right">18</td>
<td align="right">5.3%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,584</td>
<td align="right">6.6%</td>
<td align="right">12</td>
<td align="right">3.5%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">40,137</td>
<td align="right">25.0%</td>
<td align="right">282</td>
<td align="right">82.5%</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,810</td>
<td align="right">1.1%</td>
<td align="right">18</td>
<td align="right">5.3%</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">13,448</td>
<td align="right">8.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">7,949</td>
<td align="right">5.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">7,115</td>
<td align="right">4.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">4,547</td>
<td align="right">2.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">2,002</td>
<td align="right">1.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,733</td>
<td align="right">1.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">701</td>
<td align="right">0.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,198,356,194</td>
<td align="right">88.9%</td>
<td align="right">6,525</td>
<td align="right">42.1%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">272,676,457</td>
<td align="right">11.0%</td>
<td align="right">8,978</td>
<td align="right">57.9%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,503,386</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">63,908</td>
<td align="right">43.6%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">82,746</td>
<td align="right">56.4%</td>
<td align="right">8</td>
<td align="right">100.0%</td>
<td align="right">-100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">str</td>
<td align="right">22,939</td>
<td align="right">27.7%</td>
<td align="right">8</td>
<td align="right">100.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">22,351</td>
<td align="right">27.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">19,345</td>
<td align="right">23.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">18,111</td>
<td align="right">21.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">160,149,188</td>
<td align="right">3.1%</td>
<td align="right">72</td>
<td align="right">0.1%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,471,557,915</td>
<td align="right">28.5%</td>
<td align="right">8,289</td>
<td align="right">8.3%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,524,733,032</td>
<td align="right">68.4%</td>
<td align="right">89,924</td>
<td align="right">90.1%</td>
<td align="right">-100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">3,087,471</td>
<td align="right">91.8%</td>
<td align="right">1,275</td>
<td align="right">82.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">277,387</td>
<td align="right">8.2%</td>
<td align="right">280</td>
<td align="right">18.0%</td>
<td align="right">-99.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dict keys</td>
<td align="right">45,831</td>
<td align="right">16.5%</td>
<td align="right">12</td>
<td align="right">4.3%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,329</td>
<td align="right">1.6%</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">26,167</td>
<td align="right">9.4%</td>
<td align="right">13</td>
<td align="right">4.6%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">7,279</td>
<td align="right">2.6%</td>
<td align="right">253</td>
<td align="right">90.4%</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">85,722</td>
<td align="right">30.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">59,855</td>
<td align="right">21.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">16,346</td>
<td align="right">5.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">9,209</td>
<td align="right">3.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,075</td>
<td align="right">3.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">7,727</td>
<td align="right">2.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,249</td>
<td align="right">1.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,596</td>
<td align="right">0.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">822</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">180</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">195,184,934</td>
<td align="right">17.2%</td>
<td align="right">3,072</td>
<td align="right">13.2%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">940,052,947</td>
<td align="right">82.8%</td>
<td align="right">19,006</td>
<td align="right">81.7%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">119,196</td>
<td align="right">0.0%</td>
<td align="right">234</td>
<td align="right">1.0%</td>
<td align="right">-99.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Failure</td>
<td align="right">90,378</td>
<td align="right">60.1%</td>
<td align="right">72</td>
<td align="right">7.6%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">59,966</td>
<td align="right">39.9%</td>
<td align="right">872</td>
<td align="right">92.4%</td>
<td align="right">-98.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">other</td>
<td align="right">90,378</td>
<td align="right">100.0%</td>
<td align="right">72</td>
<td align="right">100.0%</td>
<td align="right">-99.9%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">795,973,041</td>
<td align="right">5.5%</td>
<td align="right">22,663</td>
<td align="right">2.3%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,751,837,961</td>
<td align="right">88.5%</td>
<td align="right">932,938</td>
<td align="right">96.5%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">857,680,037</td>
<td align="right">6.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">16,865,977</td>
<td align="right">97.3%</td>
<td align="right">11,189</td>
<td align="right">97.1%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">472,257</td>
<td align="right">2.7%</td>
<td align="right">330</td>
<td align="right">2.9%</td>
<td align="right">-99.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">method</td>
<td align="right">73,076</td>
<td align="right">15.5%</td>
<td align="right">36</td>
<td align="right">10.9%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">11,700</td>
<td align="right">2.5%</td>
<td align="right">12</td>
<td align="right">3.6%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,927</td>
<td align="right">0.4%</td>
<td align="right">6</td>
<td align="right">1.8%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">80,265</td>
<td align="right">17.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">60,005</td>
<td align="right">12.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">24,524</td>
<td align="right">5.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">17,882</td>
<td align="right">3.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,613</td>
<td align="right">2.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">8,373</td>
<td align="right">1.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,720</td>
<td align="right">1.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,637</td>
<td align="right">0.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">2,100</td>
<td align="right">0.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,969</td>
<td align="right">0.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,352</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">740</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">340</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">240</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">property not py function</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">audited slot</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">slot after items</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">15,114,716</td>
<td align="right">0.2%</td>
<td align="right">12,318</td>
<td align="right">0.0%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,727,825,471</td>
<td align="right">99.8%</td>
<td align="right">62,048,177</td>
<td align="right">100.0%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">330,307</td>
<td align="right">0.0%</td>
<td align="right">2,462</td>
<td align="right">0.0%</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,351</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">542,198</td>
<td align="right">100.0%</td>
<td align="right">9,076</td>
<td align="right">100.0%</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">7,876</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">80,115,861</td>
<td align="right">100.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">7,882</td>
<td align="right">100.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">149,796</td>
<td align="right">23.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Failure</td>
<td align="right">149,996</td>
<td align="right">23.4%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">491,309</td>
<td align="right">76.6%</td>
<td align="right">6,026</td>
<td align="right">100.0%</td>
<td align="right">-98.8%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">22,494,812</td>
<td align="right">4.1%</td>
<td align="right">12</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">531,811,181</td>
<td align="right">95.9%</td>
<td align="right">58,268,148</td>
<td align="right">100.0%</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">47,652</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Failure</td>
<td align="right">5,852</td>
<td align="right">47.9%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,370</td>
<td align="right">52.1%</td>
<td align="right">12</td>
<td align="right">100.0%</td>
<td align="right">-99.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">other</td>
<td align="right">5,852</td>
<td align="right">100.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,934,746,314</td>
<td align="right">89.6%</td>
<td align="right">60,528</td>
<td align="right">72.9%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">93,528,581</td>
<td align="right">4.3%</td>
<td align="right">18,305</td>
<td align="right">22.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">130,994,669</td>
<td align="right">6.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">2,590,532</td>
<td align="right">96.7%</td>
<td align="right">3,408</td>
<td align="right">80.5%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">88,826</td>
<td align="right">3.3%</td>
<td align="right">828</td>
<td align="right">19.5%</td>
<td align="right">-99.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">class attr simple</td>
<td align="right">41,726</td>
<td align="right">47.0%</td>
<td align="right">552</td>
<td align="right">66.7%</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">5,549</td>
<td align="right">6.2%</td>
<td align="right">276</td>
<td align="right">33.3%</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">158,251</td>
<td align="right">178.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">12,980</td>
<td align="right">14.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">6,566</td>
<td align="right">7.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,147</td>
<td align="right">6.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">6,054</td>
<td align="right">6.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">2,800</td>
<td align="right">3.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2,244</td>
<td align="right">2.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,071</td>
<td align="right">1.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,000</td>
<td align="right">1.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">400</td>
<td align="right">0.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">112,716,663</td>
<td align="right">100.0%</td>
<td align="right">18</td>
<td align="right">100.0%</td>
<td align="right">-100.0%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">613,201,133</td>
<td align="right">39.9%</td>
<td align="right">3,261</td>
<td align="right">35.6%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">922,881,415</td>
<td align="right">60.1%</td>
<td align="right">5,595</td>
<td align="right">61.1%</td>
<td align="right">-100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Failure</td>
<td align="right">103,780</td>
<td align="right">84.6%</td>
<td align="right">6</td>
<td align="right">2.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,931</td>
<td align="right">15.4%</td>
<td align="right">298</td>
<td align="right">98.0%</td>
<td align="right">-98.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,000</td>
<td align="right">4.8%</td>
<td align="right">6</td>
<td align="right">100.0%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40,981</td>
<td align="right">39.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">27,102</td>
<td align="right">26.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">26,323</td>
<td align="right">25.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,689</td>
<td align="right">2.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,560</td>
<td align="right">1.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">105</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">bytearray slice</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">110,682,243</td>
<td align="right">2.0%</td>
<td align="right">312</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">274,023,980</td>
<td align="right">5.0%</td>
<td align="right">18,210</td>
<td align="right">1.5%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,048,223,259</td>
<td align="right">92.9%</td>
<td align="right">1,157,812</td>
<td align="right">97.9%</td>
<td align="right">-100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">2,326,743</td>
<td align="right">89.0%</td>
<td align="right">4,980</td>
<td align="right">83.4%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">286,110</td>
<td align="right">11.0%</td>
<td align="right">990</td>
<td align="right">16.6%</td>
<td align="right">-99.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">number</td>
<td align="right">111,627</td>
<td align="right">39.0%</td>
<td align="right">6</td>
<td align="right">0.6%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,702</td>
<td align="right">5.8%</td>
<td align="right">42</td>
<td align="right">4.2%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">12,173</td>
<td align="right">4.3%</td>
<td align="right">36</td>
<td align="right">3.6%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">81,133</td>
<td align="right">28.4%</td>
<td align="right">570</td>
<td align="right">57.6%</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">6,803</td>
<td align="right">2.4%</td>
<td align="right">336</td>
<td align="right">33.9%</td>
<td align="right">-95.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">35,953</td>
<td align="right">12.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">11,562</td>
<td align="right">4.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">8,796</td>
<td align="right">3.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,041</td>
<td align="right">0.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">240</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,178,809,967</td>
<td align="right">99.8%</td>
<td align="right">67,776</td>
<td align="right">96.8%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,780,364</td>
<td align="right">0.2%</td>
<td align="right">1,284</td>
<td align="right">1.8%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Failure</td>
<td align="right">1,668</td>
<td align="right">4.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39,540</td>
<td align="right">96.0%</td>
<td align="right">929</td>
<td align="right">100.0%</td>
<td align="right">-97.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sequence</td>
<td align="right">1,339</td>
<td align="right">80.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">206</td>
<td align="right">12.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">123</td>
<td align="right">7.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,521,310,523</td>
<td align="right">0.7%</td>
<td align="right">4,994</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">6,435,749,763</td>
<td align="right">3.0%</td>
<td align="right">183,405</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">82,530,278,478</td>
<td align="right">38.4%</td>
<td align="right">389,307,263</td>
<td align="right">34.4%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">124,560,936,121</td>
<td align="right">57.9%</td>
<td align="right">742,837,070</td>
<td align="right">65.6%</td>
<td align="right">-99.4%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,483,843,359</td>
<td align="right">22.4%</td>
<td align="right">3,358</td>
<td align="right">2.6%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,471,557,915</td>
<td align="right">22.2%</td>
<td align="right">8,289</td>
<td align="right">6.5%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">535,860,796</td>
<td align="right">8.1%</td>
<td align="right">3,429</td>
<td align="right">2.7%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">539,924,193</td>
<td align="right">8.2%</td>
<td align="right">9,247</td>
<td align="right">7.3%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">795,973,041</td>
<td align="right">12.0%</td>
<td align="right">22,663</td>
<td align="right">17.9%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">272,676,457</td>
<td align="right">4.1%</td>
<td align="right">8,978</td>
<td align="right">7.1%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">194,377,493</td>
<td align="right">2.9%</td>
<td align="right">12,060</td>
<td align="right">9.5%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">274,023,980</td>
<td align="right">4.1%</td>
<td align="right">18,210</td>
<td align="right">14.4%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">613,201,133</td>
<td align="right">9.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">195,184,934</td>
<td align="right">2.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">18,305</td>
<td align="right">14.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">12,318</td>
<td align="right">9.7%</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">366,522,487</td>
<td align="right">24.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">255,942,463</td>
<td align="right">16.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">104,579,038</td>
<td align="right">6.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">94,868,421</td>
<td align="right">6.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">85,013,671</td>
<td align="right">5.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">81,787,176</td>
<td align="right">5.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">80,187,906</td>
<td align="right">5.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">79,856,478</td>
<td align="right">5.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">52,247,048</td>
<td align="right">3.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">51,329,986</td>
<td align="right">3.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">2,462</td>
<td align="right">49.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">504</td>
<td align="right">10.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">417</td>
<td align="right">8.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">302</td>
<td align="right">6.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">234</td>
<td align="right">4.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">230</td>
<td align="right">4.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">201</td>
<td align="right">4.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">179</td>
<td align="right">3.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">162</td>
<td align="right">3.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_EX_PY</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">120</td>
<td align="right">2.4%</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">22,456</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">46,485</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">133,287,353</td>
<td align="right">2.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">549,666,067</td>
<td align="right">8.1%</td>
<td align="right">643</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">277,407,715</td>
<td align="right">4.1%</td>
<td align="right">2,353</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,519,712,752</td>
<td align="right">22.3%</td>
<td align="right">17,166</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,519,712,752</td>
<td align="right">22.3%</td>
<td align="right">17,166</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,339,333</td>
<td align="right">3.8%</td>
<td align="right">3,888</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">970,046,685</td>
<td align="right">14.2%</td>
<td align="right">16,523</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">969,977,744</td>
<td align="right">14.2%</td>
<td align="right">16,523</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">72,366,904</td>
<td align="right">1.1%</td>
<td align="right">354,153</td>
<td align="right">0.3%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,664,596,998</td>
<td align="right">83.2%</td>
<td align="right">59,088,193</td>
<td align="right">50.3%</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,290,659,441</td>
<td align="right">77.7%</td>
<td align="right">117,345,452</td>
<td align="right">100.0%</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">13,364</td>
<td align="right">0.0%</td>
<td align="right">775</td>
<td align="right">0.0%</td>
<td align="right">-94.2%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">5,163,346</td>
<td align="right">2.8%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">749,623</td>
<td align="right">0.4%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">22,360</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,259,881,661</td>
<td align="right"></td>
<td align="right">62,861</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">184,132,956</td>
<td align="right"></td>
<td align="right">7,957</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,116,957,416</td>
<td align="right">68.9%</td>
<td align="right">1,246,213</td>
<td align="right">1.9%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,121,044,811</td>
<td align="right"></td>
<td align="right">1,254,744</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">74,722,138</td>
<td align="right">0.4%</td>
<td align="right">16,580</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">20,006,021,009</td>
<td align="right">20.3%</td>
<td align="right">4,749,126</td>
<td align="right">1.2%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,441,094,331</td>
<td align="right"></td>
<td align="right">762,633</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">30,708,261</td>
<td align="right"></td>
<td align="right">10,349</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,047,672</td>
<td align="right">0.0%</td>
<td align="right">4,129</td>
<td align="right">0.0%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">22,672,006,378</td>
<td align="right">26.4%</td>
<td align="right">17,338,687</td>
<td align="right">4.5%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">27,420,881,048</td>
<td align="right">27.9%</td>
<td align="right">23,661,889</td>
<td align="right">6.1%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">21,973,329,584</td>
<td align="right">25.5%</td>
<td align="right">68,843,455</td>
<td align="right">17.9%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">37,644,374,913</td>
<td align="right">43.8%</td>
<td align="right">181,241,565</td>
<td align="right">47.2%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">49,103,254,983</td>
<td align="right">49.9%</td>
<td align="right">240,758,541</td>
<td align="right">62.4%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">Method cache invalidations</td>
<td align="right">200,903</td>
<td align="right"></td>
<td align="right">998</td>
<td align="right"></td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">398,098</td>
<td align="right"></td>
<td align="right">2,457</td>
<td align="right"></td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">Method cache resizes</td>
<td align="right">353,008</td>
<td align="right"></td>
<td align="right">2,956</td>
<td align="right"></td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,040,542,028</td>
<td align="right"></td>
<td align="right">66,406,564</td>
<td align="right"></td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,466,234,220</td>
<td align="right">31.1%</td>
<td align="right">64,823,793</td>
<td align="right">98.1%</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,383,464,410</td>
<td align="right">30.6%</td>
<td align="right">64,803,084</td>
<td align="right">98.1%</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">3,732,777,784</td>
<td align="right">4.3%</td>
<td align="right">116,608,460</td>
<td align="right">30.4%</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,859,123,414</td>
<td align="right">1.9%</td>
<td align="right">116,572,185</td>
<td align="right">30.2%</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">Materialize dict (str subclass)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache too big</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
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
<th align="right">Base Collections</th>
<th align="right">Base Objects collected</th>
<th align="right">Base Object visits</th>
<th align="right">Base Reachable from roots</th>
<th align="right">Base Not reachable from roots</th>
<th align="right">Head Collections</th>
<th align="right">Head Objects collected</th>
<th align="right">Head Object visits</th>
<th align="right">Head Reachable from roots</th>
<th align="right">Head Not reachable from roots</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right">0</td>
<td align="right">328,933</td>
<td align="right">54,726,950</td>
<td align="right">6,664,770,291</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">29,726</td>
<td align="right">17,189,983</td>
<td align="right">4,649,087,250</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">10,424</td>
<td align="right">35,571,973</td>
<td align="right">9,631,651,736</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
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
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
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
<td align="right">21,180</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">800</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
func modification
<details>
<summary>ⓘ</summary>

Modifying a function, e.g. `func.__defaults__ = ...`, etc.
</details>
</td>
<td align="right">14,247</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">7,521,877</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Number of data files</td>
<td align="right">2,619</td>
<td align="right">217</td>
<td align="right">-91.7%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2026-10-06
