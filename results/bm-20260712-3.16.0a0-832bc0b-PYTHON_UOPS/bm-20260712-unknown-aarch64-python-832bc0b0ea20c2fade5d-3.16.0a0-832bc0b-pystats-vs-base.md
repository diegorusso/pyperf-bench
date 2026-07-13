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
<td align="right">223,383,840</td>
<td align="right">1</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,855,952,485</td>
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
<td align="right">9,616,543</td>
<td align="right">2</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">8,775,634</td>
<td align="right">2</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">417,178,751</td>
<td align="right">217</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">266,020,150</td>
<td align="right">162</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">66,805,431</td>
<td align="right">42</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">133,615,721</td>
<td align="right">85</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">443,213,852</td>
<td align="right">284</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">225,772,786</td>
<td align="right">162</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">128,213,801</td>
<td align="right">96</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">22,506,080</td>
<td align="right">24</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">154,667,839</td>
<td align="right">324</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">493,123,439</td>
<td align="right">1,048</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,168,053</td>
<td align="right">5</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,753,785,391</td>
<td align="right">4,420</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,053,028,659</td>
<td align="right">2,741</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">254,037,574</td>
<td align="right">774</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,746,383</td>
<td align="right">519</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,484,481,653</td>
<td align="right">4,919</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">46,773,559</td>
<td align="right">162</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,749,626,966</td>
<td align="right">6,241</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,618,129,470</td>
<td align="right">9,781</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">195,534,891</td>
<td align="right">767</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">76,507,607</td>
<td align="right">324</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">247,514,943</td>
<td align="right">1,113</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">245,457,713</td>
<td align="right">1,113</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">443,903,659</td>
<td align="right">2,094</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">610,062,340</td>
<td align="right">3,565</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,472,008,379</td>
<td align="right">9,172</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">535,920,832</td>
<td align="right">3,429</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">434,966,898</td>
<td align="right">2,888</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,204,404</td>
<td align="right">68</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">79,689,444</td>
<td align="right">546</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">111,731,817</td>
<td align="right">795</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">346,800,081</td>
<td align="right">2,515</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,394,836,409</td>
<td align="right">10,532</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">309,715,229</td>
<td align="right">2,451</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">77,076,876</td>
<td align="right">636</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,605,749,253</td>
<td align="right">14,599</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">366,011,893</td>
<td align="right">3,359</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,079,291,129</td>
<td align="right">21,091</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">429,730,721</td>
<td align="right">4,547</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">379,130,484</td>
<td align="right">4,104</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,913,278,385</td>
<td align="right">20,918</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">64,761,199</td>
<td align="right">734</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">192,689,324</td>
<td align="right">2,342</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">686,119,344</td>
<td align="right">8,477</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,835,390</td>
<td align="right">735</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,515,436,122</td>
<td align="right">20,495</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,422,989,626</td>
<td align="right">20,210</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,541,735,468</td>
<td align="right">36,317</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">335,229,464</td>
<td align="right">4,838</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">267,307,536</td>
<td align="right">3,996</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,218,442,930</td>
<td align="right">19,672</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">361,391,635</td>
<td align="right">5,863</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,070,129,639</td>
<td align="right">17,397</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">195,300,717</td>
<td align="right">3,344</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">117,877,253</td>
<td align="right">2,054</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,833,523,823</td>
<td align="right">66,800</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">162,132,971</td>
<td align="right">2,838</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">814,899,047</td>
<td align="right">14,390</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,998,513,896</td>
<td align="right">91,603</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,193,466,676</td>
<td align="right">25,062</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">659,363,795</td>
<td align="right">13,948</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,176,082,231</td>
<td align="right">46,906</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">75,970,742</td>
<td align="right">1,693</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">252,885,824</td>
<td align="right">5,703</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">9,177,439</td>
<td align="right">211</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">500,805,509</td>
<td align="right">12,068</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">540,071,286</td>
<td align="right">13,886</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">90,729,705</td>
<td align="right">2,341</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,277,940,610</td>
<td align="right">58,804</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">356,326,583</td>
<td align="right">9,736</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">568,552,089</td>
<td align="right">16,966</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">167,660,913</td>
<td align="right">5,043</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,678,907</td>
<td align="right">232</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">178,413,702</td>
<td align="right">5,633</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,151,596</td>
<td align="right">147</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">247,103,608</td>
<td align="right">8,986</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right">161,969,059</td>
<td align="right">6,288</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">501,909,532</td>
<td align="right">19,683</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">118,675,475</td>
<td align="right">5,049</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">798,646,083</td>
<td align="right">34,194</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">100,790,071</td>
<td align="right">5,047</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">90,829,253</td>
<td align="right">4,836</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">505,407,404</td>
<td align="right">27,878</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">550,417,280</td>
<td align="right">30,767</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">82,309,782</td>
<td align="right">4,665</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,027,778,899</td>
<td align="right">60,528</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,598,821,414</td>
<td align="right">907,346</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">75,578,959</td>
<td align="right">5,335</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">775,524,172</td>
<td align="right">54,968</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">77,903,948</td>
<td align="right">5,645</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">405,512,387</td>
<td align="right">31,696</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">154,492,723</td>
<td align="right">12,462</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">798,132,926</td>
<td align="right">65,261</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">266,019,778</td>
<td align="right">24,168</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">710,602,526</td>
<td align="right">64,676</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">143,598,623</td>
<td align="right">13,609</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,075,128,329</td>
<td align="right">1,155,522</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">90,518,138</td>
<td align="right">9,668</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">SEND_VIRTUAL</td>
<td align="right">2,500,194</td>
<td align="right">315</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">78,421,409</td>
<td align="right">10,800</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,556,492,853</td>
<td align="right">384,161</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">71,942,335</td>
<td align="right">11,816</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,135,970,978</td>
<td align="right">768,513</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,843,703,760</td>
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
<td align="left">CALL_EX_PY</td>
<td align="right">24,413,991</td>
<td align="right">6,186</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">87,270,337</td>
<td align="right">22,541</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,524,075,231</td>
<td align="right">740,019</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,024,689,566</td>
<td align="right">1,844,274</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">725,284,407</td>
<td align="right">366,212</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,183,542,150</td>
<td align="right">758,414</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">904,564,128</td>
<td align="right">724,007</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">501,240,233</td>
<td align="right">412,399</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">403,096,144</td>
<td align="right">361,932</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">408,514,928</td>
<td align="right">369,946</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">371,961,499</td>
<td align="right">370,002</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">14,990,586</td>
<td align="right">17,280</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,821,602</td>
<td align="right">2,213</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">260,709,693</td>
<td align="right">360,427</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">15,653,745</td>
<td align="right">22,402</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">366,871,521</td>
<td align="right">707,538</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">860,051,809</td>
<td align="right">2,136,964</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">36,815,942,940</td>
<td align="right">147,864,061</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,889,419,359</td>
<td align="right">59,877,660</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">220,153</td>
<td align="right">1,446</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,420,607,105</td>
<td align="right">29,143,858</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,521,428,935</td>
<td align="right">58,281,075</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,596,329,995</td>
<td align="right">59,087,771</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,806,667</td>
<td align="right">21,294</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">498,279</td>
<td align="right">6,026</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">4,827,759,394</td>
<td align="right">58,819,543</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,420,619,921</td>
<td align="right">59,076,237</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,660,278,968</td>
<td align="right">60,212,791</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,026,768,794</td>
<td align="right">116,594,695</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">98,930</td>
<td align="right">1,736</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,298,580,429</td>
<td align="right">58,667,811</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">19,184,581</td>
<td align="right">355,843</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">19,184,380</td>
<td align="right">355,842</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">18,804,148</td>
<td align="right">355,842</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">17,122,187</td>
<td align="right">354,106</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,713,544,612</td>
<td align="right">58,337,597</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,917,175,749</td>
<td align="right">58,689,468</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,551,953,851</td>
<td align="right">58,272,889</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">46,560</td>
<td align="right">2,114</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">531,833,786</td>
<td align="right">58,268,148</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">353,543,720</td>
<td align="right">58,272,798</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">238,663,205</td>
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
<td align="right">1,197,584,680</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,029,653,782</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">887,388,188</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">423,511,829</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">189,812,032</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">123,245,777</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">113,712,343</td>
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
<td align="right">85,937,004</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">77,110,840</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_VIRTUAL</td>
<td align="right">74,850,136</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">73,643,818</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">63,640,805</td>
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
<td align="right">42,190,533</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">40,805,204</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">34,033,330</td>
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
<td align="right">7,592,825</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,153,930</td>
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
<td align="right">5,768,061</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,736,138</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">2,998,155</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">2,478,191</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,557,047</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">717,573</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MATCH_CLASS</td>
<td align="right">302,532</td>
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
<td align="right">82,460</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">46,305</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">30,884</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">24,522</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">18,672</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,760</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">12,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">3,620</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">3,480</td>
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
<td align="right">1,483,926,139</td>
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
<td align="right">60,418,110</td>
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
<td align="right">13,794,112,961</td>
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
<td align="right">383,115</td>
<td align="right">22.6%</td>
<td align="right">44</td>
<td align="right">2.8%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,310,348</td>
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
<td align="right">26,814</td>
<td align="right">7.0%</td>
<td align="right">1</td>
<td align="right">2.3%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">18,882</td>
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
<td align="right">71,667</td>
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
<td align="right">35,189</td>
<td align="right">9.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">22,030</td>
<td align="right">5.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">15,726</td>
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
<td align="right">13,501</td>
<td align="right">3.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">13,236</td>
<td align="right">3.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">12,144</td>
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
<td align="right">10,269</td>
<td align="right">2.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">7,945</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">7,181</td>
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
<td align="right">4,853</td>
<td align="right">1.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">4,471</td>
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
<td align="right">2,841</td>
<td align="right">0.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">1,880</td>
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
<td align="right">1,631</td>
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
<td align="right">951</td>
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
<td align="right">799</td>
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
<td align="right">535,920,832</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">199,213,383</td>
<td align="right">1.7%</td>
<td align="right">150</td>
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
<td align="right">196,637,809</td>
<td align="right">1.7%</td>
<td align="right">12,600</td>
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
<td align="right">11,195,160,697</td>
<td align="right">98.2%</td>
<td align="right">60,570,064</td>
<td align="right">100.0%</td>
<td align="right">-99.5%</td>
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
<td align="right">4,381,335</td>
<td align="right">100.0%</td>
<td align="right">8,844</td>
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
<td align="right">20.3%</td>
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
<td align="right">35,289</td>
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
<td align="right">23,122</td>
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
<td align="right">290,125</td>
<td align="right">84.2%</td>
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
<td align="right">124,448</td>
<td align="right">36.1%</td>
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
<td align="right">54,196</td>
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
<td align="right">539,840,610</td>
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
<td align="right">1,183,437</td>
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
<td align="right">4,507,922,460</td>
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
<td align="right">160,030</td>
<td align="right">63.3%</td>
<td align="right">342</td>
<td align="right">7.4%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">92,669</td>
<td align="right">36.7%</td>
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
<td align="right">47,648</td>
<td align="right">29.8%</td>
<td align="right">12</td>
<td align="right">3.5%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">22,757</td>
<td align="right">14.2%</td>
<td align="right">18</td>
<td align="right">5.3%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,512</td>
<td align="right">6.6%</td>
<td align="right">12</td>
<td align="right">3.5%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">39,838</td>
<td align="right">24.9%</td>
<td align="right">282</td>
<td align="right">82.5%</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,850</td>
<td align="right">1.2%</td>
<td align="right">18</td>
<td align="right">5.3%</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">13,388</td>
<td align="right">8.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">7,920</td>
<td align="right">4.9%</td>
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
<td align="right">2,021</td>
<td align="right">1.3%</td>
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
<td align="right">2,190,337,432</td>
<td align="right">89.8%</td>
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
<td align="right">247,007,586</td>
<td align="right">10.1%</td>
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
<td align="right">63,788</td>
<td align="right">44.6%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">79,355</td>
<td align="right">55.4%</td>
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
<td align="right">22,941</td>
<td align="right">28.9%</td>
<td align="right">8</td>
<td align="right">100.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">19,195</td>
<td align="right">24.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">19,108</td>
<td align="right">24.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">18,111</td>
<td align="right">22.8%</td>
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
<td align="right">160,133,994</td>
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
<td align="right">1,471,665,567</td>
<td align="right">28.6%</td>
<td align="right">7,893</td>
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
<td align="right">3,517,190,214</td>
<td align="right">68.3%</td>
<td align="right">85,640</td>
<td align="right">90.3%</td>
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
<td align="right">3,085,741</td>
<td align="right">91.7%</td>
<td align="right">999</td>
<td align="right">78.1%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">278,101</td>
<td align="right">8.3%</td>
<td align="right">280</td>
<td align="right">21.9%</td>
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
<td align="right">45,931</td>
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
<td align="right">26,168</td>
<td align="right">9.4%</td>
<td align="right">13</td>
<td align="right">4.6%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">7,139</td>
<td align="right">2.6%</td>
<td align="right">253</td>
<td align="right">90.4%</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">85,722</td>
<td align="right">30.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">60,967</td>
<td align="right">21.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">16,367</td>
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
<td align="right">7,587</td>
<td align="right">2.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,129</td>
<td align="right">1.1%</td>
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
<td align="right">702</td>
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
<td align="right">195,154,141</td>
<td align="right">17.3%</td>
<td align="right">2,676</td>
<td align="right">14.6%</td>
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
<td align="right">935,653,800</td>
<td align="right">82.7%</td>
<td align="right">14,722</td>
<td align="right">80.4%</td>
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
<td align="right">118,607</td>
<td align="right">0.0%</td>
<td align="right">234</td>
<td align="right">1.3%</td>
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
<td align="right">90,179</td>
<td align="right">60.7%</td>
<td align="right">72</td>
<td align="right">10.8%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">58,491</td>
<td align="right">39.3%</td>
<td align="right">596</td>
<td align="right">89.2%</td>
<td align="right">-99.0%</td>
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
<td align="right">90,179</td>
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
<td align="right">796,197,004</td>
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
<td align="right">12,731,392,481</td>
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
<td align="right">857,622,790</td>
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
<td align="right">16,863,143</td>
<td align="right">97.3%</td>
<td align="right">11,189</td>
<td align="right">97.1%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">471,880</td>
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
<td align="right">73,016</td>
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
<td align="right">80,100</td>
<td align="right">17.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">59,705</td>
<td align="right">12.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">24,508</td>
<td align="right">5.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">17,842</td>
<td align="right">3.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,515</td>
<td align="right">2.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">8,369</td>
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
<td align="right">760</td>
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
<td align="right">15,116,146</td>
<td align="right">0.2%</td>
<td align="right">12,912</td>
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
<td align="right">9,684,630,756</td>
<td align="right">99.8%</td>
<td align="right">62,054,603</td>
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
<td align="right">337,778</td>
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
<td align="right">10,451</td>
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
<td align="right">543,577</td>
<td align="right">100.0%</td>
<td align="right">9,490</td>
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
<td align="right">7,878</td>
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
<td align="right">80,108,995</td>
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
<td align="right">151,784</td>
<td align="right">23.3%</td>
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
<td align="right">151,984</td>
<td align="right">23.6%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">492,619</td>
<td align="right">76.4%</td>
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
<td align="right">22,494,787</td>
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
<td align="right">531,810,149</td>
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
<td align="right">48.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,350</td>
<td align="right">52.0%</td>
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
<td align="right">1,935,351,092</td>
<td align="right">89.9%</td>
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
<td align="right">87,059,771</td>
<td align="right">4.0%</td>
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
<td align="right">130,958,209</td>
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
<td align="right">2,590,131</td>
<td align="right">96.7%</td>
<td align="right">3,408</td>
<td align="right">80.5%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">87,028</td>
<td align="right">3.3%</td>
<td align="right">828</td>
<td align="right">19.5%</td>
<td align="right">-99.0%</td>
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
<td align="right">40,844</td>
<td align="right">46.9%</td>
<td align="right">552</td>
<td align="right">66.7%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">5,553</td>
<td align="right">6.4%</td>
<td align="right">276</td>
<td align="right">33.3%</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">158,537</td>
<td align="right">182.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">12,980</td>
<td align="right">14.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">6,386</td>
<td align="right">7.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,007</td>
<td align="right">6.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">5,494</td>
<td align="right">6.3%</td>
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
<td align="right">2.6%</td>
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
<td align="right">980</td>
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
<td align="right">609,940,133</td>
<td align="right">39.8%</td>
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
<td align="right">922,854,160</td>
<td align="right">60.2%</td>
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
<td align="right">103,360</td>
<td align="right">84.6%</td>
<td align="right">6</td>
<td align="right">2.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,847</td>
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
<td align="right">4,580</td>
<td align="right">4.4%</td>
<td align="right">6</td>
<td align="right">100.0%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40,981</td>
<td align="right">39.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">27,102</td>
<td align="right">26.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">26,323</td>
<td align="right">25.5%</td>
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
<td align="right">110,932,414</td>
<td align="right">2.1%</td>
<td align="right">336</td>
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
<td align="right">265,492,242</td>
<td align="right">4.9%</td>
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
<td align="right">5,013,022,355</td>
<td align="right">93.0%</td>
<td align="right">1,157,788</td>
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
<td align="right">2,330,409</td>
<td align="right">89.1%</td>
<td align="right">4,980</td>
<td align="right">83.4%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">284,877</td>
<td align="right">10.9%</td>
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
<td align="right">111,446</td>
<td align="right">39.1%</td>
<td align="right">6</td>
<td align="right">0.6%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,482</td>
<td align="right">5.8%</td>
<td align="right">42</td>
<td align="right">4.2%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">12,093</td>
<td align="right">4.2%</td>
<td align="right">36</td>
<td align="right">3.6%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">81,108</td>
<td align="right">28.5%</td>
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
<td align="right">36,006</td>
<td align="right">12.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">10,365</td>
<td align="right">3.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">9,213</td>
<td align="right">3.2%</td>
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
<td align="right">1,178,963,677</td>
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
<td align="right">1,780,410</td>
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
<td align="right">1,674</td>
<td align="right">4.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39,558</td>
<td align="right">95.9%</td>
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
<td align="right">1,345</td>
<td align="right">80.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">206</td>
<td align="right">12.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">123</td>
<td align="right">7.3%</td>
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
<td align="right">1,523,760,503</td>
<td align="right">0.7%</td>
<td align="right">5,168</td>
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
<td align="right">6,392,170,522</td>
<td align="right">3.0%</td>
<td align="right">183,741</td>
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
<td align="right">82,299,607,956</td>
<td align="right">38.4%</td>
<td align="right">389,309,237</td>
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
<td align="right">124,371,176,519</td>
<td align="right">58.0%</td>
<td align="right">742,841,552</td>
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
<td align="right">1,483,926,139</td>
<td align="right">22.5%</td>
<td align="right">3,358</td>
<td align="right">2.6%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,471,665,567</td>
<td align="right">22.4%</td>
<td align="right">7,893</td>
<td align="right">6.2%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">535,920,832</td>
<td align="right">8.1%</td>
<td align="right">3,429</td>
<td align="right">2.7%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">539,840,610</td>
<td align="right">8.2%</td>
<td align="right">9,247</td>
<td align="right">7.3%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">796,197,004</td>
<td align="right">12.1%</td>
<td align="right">22,663</td>
<td align="right">17.8%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">247,007,586</td>
<td align="right">3.8%</td>
<td align="right">8,978</td>
<td align="right">7.1%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">196,637,809</td>
<td align="right">3.0%</td>
<td align="right">12,600</td>
<td align="right">9.9%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">265,492,242</td>
<td align="right">4.0%</td>
<td align="right">18,210</td>
<td align="right">14.3%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">609,940,133</td>
<td align="right">9.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">195,154,141</td>
<td align="right">3.0%</td>
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
<td align="right">12,912</td>
<td align="right">10.2%</td>
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
<td align="right">366,517,742</td>
<td align="right">24.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">255,942,196</td>
<td align="right">16.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">104,549,678</td>
<td align="right">6.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">94,833,211</td>
<td align="right">6.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">85,021,464</td>
<td align="right">5.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">81,708,544</td>
<td align="right">5.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">80,172,157</td>
<td align="right">5.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">79,857,033</td>
<td align="right">5.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">52,225,531</td>
<td align="right">3.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">51,361,516</td>
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
<td align="right">47.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">504</td>
<td align="right">9.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">417</td>
<td align="right">8.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">302</td>
<td align="right">5.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">234</td>
<td align="right">4.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">230</td>
<td align="right">4.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">201</td>
<td align="right">3.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">179</td>
<td align="right">3.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">162</td>
<td align="right">3.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">150</td>
<td align="right">2.9%</td>
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
<td align="right">22,276</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">46,305</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">133,287,293</td>
<td align="right">2.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">277,401,303</td>
<td align="right">4.1%</td>
<td align="right">2,353</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">549,755,856</td>
<td align="right">8.1%</td>
<td align="right">4,927</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,519,794,915</td>
<td align="right">22.4%</td>
<td align="right">21,450</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,519,794,915</td>
<td align="right">22.4%</td>
<td align="right">21,450</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,325,378</td>
<td align="right">3.8%</td>
<td align="right">3,888</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">970,039,059</td>
<td align="right">14.3%</td>
<td align="right">16,523</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">969,970,478</td>
<td align="right">14.3%</td>
<td align="right">16,523</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">72,588,635</td>
<td align="right">1.1%</td>
<td align="right">356,493</td>
<td align="right">0.3%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,652,191,813</td>
<td align="right">83.1%</td>
<td align="right">59,088,193</td>
<td align="right">50.3%</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,278,244,073</td>
<td align="right">77.6%</td>
<td align="right">117,341,168</td>
<td align="right">100.0%</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">13,388</td>
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
<td align="right">5,183,086</td>
<td align="right">2.8%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">749,563</td>
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
<td align="right">2,216,366,288</td>
<td align="right"></td>
<td align="right">59,112</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">184,143,254</td>
<td align="right"></td>
<td align="right">7,957</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,186,625,243</td>
<td align="right">68.9%</td>
<td align="right">1,602,757</td>
<td align="right">2.4%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,190,690,151</td>
<td align="right"></td>
<td align="right">1,611,251</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">74,276,527</td>
<td align="right"></td>
<td align="right">13,651</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">68,107,647</td>
<td align="right"></td>
<td align="right">14,098</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">74,581,905</td>
<td align="right">0.4%</td>
<td align="right">16,182</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">20,159,942,114</td>
<td align="right">20.4%</td>
<td align="right">4,765,727</td>
<td align="right">1.2%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,430,061,401</td>
<td align="right"></td>
<td align="right">761,415</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,109,437</td>
<td align="right">0.0%</td>
<td align="right">4,130</td>
<td align="right">0.0%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,080,462</td>
<td align="right"></td>
<td align="right">3,675</td>
<td align="right"></td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">22,913,851,539</td>
<td align="right">26.5%</td>
<td align="right">17,704,965</td>
<td align="right">4.6%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">27,790,924,930</td>
<td align="right">28.1%</td>
<td align="right">24,387,284</td>
<td align="right">6.3%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">22,120,313,819</td>
<td align="right">25.6%</td>
<td align="right">68,854,330</td>
<td align="right">17.9%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">37,597,818,255</td>
<td align="right">43.5%</td>
<td align="right">181,246,029</td>
<td align="right">47.1%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">49,041,495,282</td>
<td align="right">49.6%</td>
<td align="right">240,768,081</td>
<td align="right">62.3%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,064,482,807</td>
<td align="right"></td>
<td align="right">66,411,879</td>
<td align="right"></td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,496,595,489</td>
<td align="right">31.1%</td>
<td align="right">64,827,825</td>
<td align="right">97.6%</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,413,904,147</td>
<td align="right">30.6%</td>
<td align="right">64,807,513</td>
<td align="right">97.6%</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">3,733,236,781</td>
<td align="right">4.3%</td>
<td align="right">116,610,782</td>
<td align="right">30.3%</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,859,199,549</td>
<td align="right">1.9%</td>
<td align="right">116,574,327</td>
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
<td align="right">328,575</td>
<td align="right">54,834,450</td>
<td align="right">6,625,650,318</td>
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
<td align="right">29,725</td>
<td align="right">17,113,300</td>
<td align="right">4,641,347,825</td>
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
<td align="right">10,404</td>
<td align="right">35,525,544</td>
<td align="right">9,620,096,329</td>
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
<td align="right">720</td>
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
<td align="right">13,527</td>
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
<td align="right">7,520,537</td>
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
Stats gathered on: 2026-07-13
