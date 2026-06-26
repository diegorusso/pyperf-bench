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
<td align="left">EXTENDED_ARG</td>
<td align="right">23,940</td>
<td align="right">7,182</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">18,600</td>
<td align="right">5,580</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">18,340</td>
<td align="right">5,502</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">12,480</td>
<td align="right">3,744</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">11,880</td>
<td align="right">3,564</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">11,180</td>
<td align="right">3,354</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">10,840</td>
<td align="right">3,252</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">10,220</td>
<td align="right">3,066</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,280</td>
<td align="right">2,784</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">9,260</td>
<td align="right">2,778</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">8,720</td>
<td align="right">2,616</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">8,180</td>
<td align="right">2,454</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,060</td>
<td align="right">2,418</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">7,280</td>
<td align="right">2,184</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">7,020</td>
<td align="right">2,106</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,520</td>
<td align="right">1,656</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">5,040</td>
<td align="right">1,512</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">4,280</td>
<td align="right">1,284</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">4,040</td>
<td align="right">1,212</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,940</td>
<td align="right">882</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,900</td>
<td align="right">870</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,820</td>
<td align="right">846</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,580</td>
<td align="right">774</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,560</td>
<td align="right">768</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,080</td>
<td align="right">624</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,820</td>
<td align="right">546</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,800</td>
<td align="right">540</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,680</td>
<td align="right">504</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,680</td>
<td align="right">504</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">1,560</td>
<td align="right">468</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,320</td>
<td align="right">396</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">1,240</td>
<td align="right">372</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,160</td>
<td align="right">348</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">960</td>
<td align="right">288</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">960</td>
<td align="right">288</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">940</td>
<td align="right">282</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">840</td>
<td align="right">252</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">840</td>
<td align="right">252</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">840</td>
<td align="right">252</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">840</td>
<td align="right">252</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">840</td>
<td align="right">252</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">840</td>
<td align="right">252</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">780</td>
<td align="right">234</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">540</td>
<td align="right">162</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">420</td>
<td align="right">126</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">420</td>
<td align="right">126</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">360</td>
<td align="right">108</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">340</td>
<td align="right">102</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">340</td>
<td align="right">102</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">320</td>
<td align="right">96</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">320</td>
<td align="right">96</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">220</td>
<td align="right">66</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">160</td>
<td align="right">48</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">36</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">100</td>
<td align="right">30</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">80</td>
<td align="right">24</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">20</td>
<td align="right">6</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">20</td>
<td align="right">6</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">36,940</td>
<td align="right">11,124</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">20,740</td>
<td align="right">6,264</td>
<td align="right">-69.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">12,500</td>
<td align="right">3,792</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">45,220</td>
<td align="right">13,734</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,700</td>
<td align="right">2,652</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">7,860</td>
<td align="right">2,400</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,840</td>
<td align="right">2,094</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">6,040</td>
<td align="right">1,854</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,340</td>
<td align="right">1,650</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,500</td>
<td align="right">1,392</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">17,980</td>
<td align="right">5,562</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,900</td>
<td align="right">1,212</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">7,000</td>
<td align="right">2,184</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,200</td>
<td align="right">8,496</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,680</td>
<td align="right">2,088</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">37,660</td>
<td align="right">11,844</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">282,120</td>
<td align="right">89,718</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">81,020</td>
<td align="right">25,776</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">83,320</td>
<td align="right">26,550</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">4,500</td>
<td align="right">1,434</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,220</td>
<td align="right">714</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">6,020</td>
<td align="right">1,974</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,700</td>
<td align="right">558</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">15,560</td>
<td align="right">5,172</td>
<td align="right">-66.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">35,960</td>
<td align="right">12,048</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">13,360</td>
<td align="right">4,512</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">12,460</td>
<td align="right">4,242</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">41,780</td>
<td align="right">14,550</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">860</td>
<td align="right">300</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">800</td>
<td align="right">282</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">72,240</td>
<td align="right">25,494</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">42,440</td>
<td align="right">15,042</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">16,920</td>
<td align="right">6,000</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">16,740</td>
<td align="right">5,988</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">15,080</td>
<td align="right">5,448</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,920</td>
<td align="right">2,154</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">11,180</td>
<td align="right">4,236</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">11,280</td>
<td align="right">4,392</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">460</td>
<td align="right">180</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">34,980</td>
<td align="right">13,728</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,540</td>
<td align="right">4,806</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">280</td>
<td align="right">126</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,260</td>
<td align="right">1,230</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,040</td>
<td align="right">1,962</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">40</td>
<td align="right">54</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right">40</td>
<td align="right">54</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">CALL_EX_PY</td>
<td align="right">40</td>
<td align="right">54</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,520</td>
<td align="right">1,128</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,180</td>
<td align="right">1,620</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">840</td>
<td align="right">630</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,860</td>
<td align="right">1,440</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,460</td>
<td align="right">1,320</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,280</td>
<td align="right">1,308</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">40,360</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">23,380</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK_JIT</td>
<td align="right"></td>
<td align="right">14,124</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">7,938</td>
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
<td align="right">2,760</td>
<td align="right">5.2%</td>
<td align="right">828</td>
<td align="right">4.9%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,540</td>
<td align="right">4.8%</td>
<td align="right">762</td>
<td align="right">4.5%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,460</td>
<td align="right">89.6%</td>
<td align="right">15,204</td>
<td align="right">90.2%</td>
<td align="right">-68.0%</td>
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
<td align="right">120</td>
<td align="right">66.7%</td>
<td align="right">36</td>
<td align="right">66.7%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">60</td>
<td align="right">33.3%</td>
<td align="right">18</td>
<td align="right">33.3%</td>
<td align="right">-70.0%</td>
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
<td align="left">add other</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">6</td>
<td align="right">33.3%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">6</td>
<td align="right">33.3%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">6</td>
<td align="right">33.3%</td>
<td align="right">-70.0%</td>
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
<td align="right">2,580</td>
<td align="right">100.0%</td>
<td align="right">774</td>
<td align="right">100.0%</td>
<td align="right">-70.0%</td>
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
<td align="right">800</td>
<td align="right">0.8%</td>
<td align="right">240</td>
<td align="right">0.7%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">340</td>
<td align="right">0.3%</td>
<td align="right">102</td>
<td align="right">0.3%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">99,480</td>
<td align="right">98.7%</td>
<td align="right">33,960</td>
<td align="right">98.9%</td>
<td align="right">-65.9%</td>
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
<td align="right">500</td>
<td align="right">100.0%</td>
<td align="right">150</td>
<td align="right">100.0%</td>
<td align="right">-70.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">40</td>
<td align="right">50.0%</td>
<td align="right">12</td>
<td align="right">50.0%</td>
<td align="right">-70.0%</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">12</td>
<td align="right">100.0%</td>
<td align="right">-70.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">19,080</td>
<td align="right">90.0%</td>
<td align="right">5,724</td>
<td align="right">89.3%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">420</td>
<td align="right">2.0%</td>
<td align="right">126</td>
<td align="right">2.0%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,600</td>
<td align="right">7.5%</td>
<td align="right">522</td>
<td align="right">8.1%</td>
<td align="right">-67.4%</td>
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
<td align="right">100</td>
<td align="right">100.0%</td>
<td align="right">36</td>
<td align="right">100.0%</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="left">big int</td>
<td align="right">40</td>
<td align="right">40.0%</td>
<td align="right">12</td>
<td align="right">33.3%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">40</td>
<td align="right">40.0%</td>
<td align="right">12</td>
<td align="right">33.3%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">20</td>
<td align="right">20.0%</td>
<td align="right">12</td>
<td align="right">33.3%</td>
<td align="right">-40.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,280</td>
<td align="right">41.1%</td>
<td align="right">2,184</td>
<td align="right">41.1%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,440</td>
<td align="right">58.9%</td>
<td align="right">3,132</td>
<td align="right">58.9%</td>
<td align="right">-70.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,200</td>
<td align="right">21.0%</td>
<td align="right">1,602</td>
<td align="right">18.9%</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">19,460</td>
<td align="right">78.5%</td>
<td align="right">6,846</td>
<td align="right">80.6%</td>
<td align="right">-64.8%</td>
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
<td align="right">80</td>
<td align="right">57.1%</td>
<td align="right">24</td>
<td align="right">50.0%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">60</td>
<td align="right">42.9%</td>
<td align="right">24</td>
<td align="right">50.0%</td>
<td align="right">-60.0%</td>
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
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">6</td>
<td align="right">25.0%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">6</td>
<td align="right">25.0%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">12</td>
<td align="right">50.0%</td>
<td align="right">-40.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">420</td>
<td align="right">6.2%</td>
<td align="right">126</td>
<td align="right">5.9%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,100</td>
<td align="right">31.2%</td>
<td align="right">672</td>
<td align="right">31.3%</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,080</td>
<td align="right">60.7%</td>
<td align="right">1,308</td>
<td align="right">60.9%</td>
<td align="right">-67.9%</td>
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
<td align="right">60</td>
<td align="right">50.0%</td>
<td align="right">18</td>
<td align="right">42.9%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">60</td>
<td align="right">50.0%</td>
<td align="right">24</td>
<td align="right">57.1%</td>
<td align="right">-60.0%</td>
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
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">24</td>
<td align="right">100.0%</td>
<td align="right">-60.0%</td>
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
<td align="right">7,620</td>
<td align="right">10.0%</td>
<td align="right">2,286</td>
<td align="right">9.0%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">68,380</td>
<td align="right">89.5%</td>
<td align="right">23,118</td>
<td align="right">90.5%</td>
<td align="right">-66.2%</td>
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
<td align="right">340</td>
<td align="right">77.3%</td>
<td align="right">102</td>
<td align="right">77.3%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">100</td>
<td align="right">22.7%</td>
<td align="right">30</td>
<td align="right">22.7%</td>
<td align="right">-70.0%</td>
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
<td align="right">100</td>
<td align="right">100.0%</td>
<td align="right">30</td>
<td align="right">100.0%</td>
<td align="right">-70.0%</td>
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
<td align="right">380</td>
<td align="right">0.3%</td>
<td align="right">114</td>
<td align="right">0.3%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">114,680</td>
<td align="right">99.3%</td>
<td align="right">40,536</td>
<td align="right">99.4%</td>
<td align="right">-64.7%</td>
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
<td align="right">400</td>
<td align="right">100.0%</td>
<td align="right">120</td>
<td align="right">100.0%</td>
<td align="right">-70.0%</td>
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

### RESUME

<details>
<summary> specialization stats for RESUME family </summary>

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
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">48</td>
<td align="right">100.0%</td>
<td align="right">-70.0%</td>
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
<td align="right">18,600</td>
<td align="right">100.0%</td>
<td align="right">5,580</td>
<td align="right">100.0%</td>
<td align="right">-70.0%</td>
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
<td align="right">1,320</td>
<td align="right">35.5%</td>
<td align="right">396</td>
<td align="right">35.5%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,400</td>
<td align="right">64.5%</td>
<td align="right">720</td>
<td align="right">64.5%</td>
<td align="right">-70.0%</td>
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
<td align="right">220</td>
<td align="right">0.6%</td>
<td align="right">66</td>
<td align="right">0.6%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,140</td>
<td align="right">92.8%</td>
<td align="right">10,566</td>
<td align="right">89.1%</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,100</td>
<td align="right">6.1%</td>
<td align="right">1,176</td>
<td align="right">9.9%</td>
<td align="right">-44.0%</td>
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
<td align="right">80</td>
<td align="right">44.4%</td>
<td align="right">24</td>
<td align="right">40.0%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">100</td>
<td align="right">55.6%</td>
<td align="right">36</td>
<td align="right">60.0%</td>
<td align="right">-64.0%</td>
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
<td align="left">mapping</td>
<td align="right">60</td>
<td align="right">60.0%</td>
<td align="right">18</td>
<td align="right">50.0%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">40</td>
<td align="right">40.0%</td>
<td align="right">18</td>
<td align="right">50.0%</td>
<td align="right">-55.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">12</td>
<td align="right">0.2%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,980</td>
<td align="right">99.4%</td>
<td align="right">5,298</td>
<td align="right">99.4%</td>
<td align="right">-66.8%</td>
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
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">18</td>
<td align="right">100.0%</td>
<td align="right">-70.0%</td>
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
<td align="right">3,940</td>
<td align="right">0.3%</td>
<td align="right">1,182</td>
<td align="right">0.3%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">35,780</td>
<td align="right">2.6%</td>
<td align="right">11,430</td>
<td align="right">2.5%</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">839,300</td>
<td align="right">60.4%</td>
<td align="right">270,858</td>
<td align="right">59.2%</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">510,420</td>
<td align="right">36.7%</td>
<td align="right">174,126</td>
<td align="right">38.1%</td>
<td align="right">-65.9%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">7,620</td>
<td align="right">22.5%</td>
<td align="right">2,286</td>
<td align="right">21.1%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">7,280</td>
<td align="right">21.5%</td>
<td align="right">2,184</td>
<td align="right">20.2%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,760</td>
<td align="right">8.2%</td>
<td align="right">828</td>
<td align="right">7.7%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,580</td>
<td align="right">7.6%</td>
<td align="right">774</td>
<td align="right">7.2%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,320</td>
<td align="right">3.9%</td>
<td align="right">396</td>
<td align="right">3.7%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">800</td>
<td align="right">2.4%</td>
<td align="right">240</td>
<td align="right">2.2%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,200</td>
<td align="right">15.4%</td>
<td align="right">1,602</td>
<td align="right">14.8%</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,100</td>
<td align="right">6.2%</td>
<td align="right">672</td>
<td align="right">6.2%</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,600</td>
<td align="right">4.7%</td>
<td align="right">522</td>
<td align="right">4.8%</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,100</td>
<td align="right">6.2%</td>
<td align="right">1,176</td>
<td align="right">10.9%</td>
<td align="right">-44.0%</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,680</td>
<td align="right">42.6%</td>
<td align="right">504</td>
<td align="right">42.6%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">420</td>
<td align="right">10.7%</td>
<td align="right">126</td>
<td align="right">10.7%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">420</td>
<td align="right">10.7%</td>
<td align="right">126</td>
<td align="right">10.7%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">420</td>
<td align="right">10.7%</td>
<td align="right">126</td>
<td align="right">10.7%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">420</td>
<td align="right">10.7%</td>
<td align="right">126</td>
<td align="right">10.7%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">340</td>
<td align="right">8.6%</td>
<td align="right">102</td>
<td align="right">8.6%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">120</td>
<td align="right">3.0%</td>
<td align="right">36</td>
<td align="right">3.0%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">100</td>
<td align="right">2.5%</td>
<td align="right">30</td>
<td align="right">2.5%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">20</td>
<td align="right">0.5%</td>
<td align="right">6</td>
<td align="right">0.5%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">5,280</td>
<td align="right">13.0%</td>
<td align="right">1,584</td>
<td align="right">11.2%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">1,680</td>
<td align="right">4.1%</td>
<td align="right">504</td>
<td align="right">3.6%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">5,520</td>
<td align="right">13.6%</td>
<td align="right">1,698</td>
<td align="right">12.0%</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">5,520</td>
<td align="right">13.6%</td>
<td align="right">1,698</td>
<td align="right">12.0%</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">5,520</td>
<td align="right">13.6%</td>
<td align="right">1,698</td>
<td align="right">12.0%</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">5,520</td>
<td align="right">13.6%</td>
<td align="right">1,698</td>
<td align="right">12.0%</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">42,200</td>
<td align="right">104.1%</td>
<td align="right">14,676</td>
<td align="right">103.6%</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">35,000</td>
<td align="right">86.4%</td>
<td align="right">12,474</td>
<td align="right">88.0%</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">91</td>
<td align="right"></td>
<td align="right">14</td>
<td align="right"></td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">327</td>
<td align="right"></td>
<td align="right">74</td>
<td align="right"></td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">256</td>
<td align="right"></td>
<td align="right">72</td>
<td align="right"></td>
<td align="right">-71.9%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,680</td>
<td align="right"></td>
<td align="right">504</td>
<td align="right"></td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,984</td>
<td align="right"></td>
<td align="right">2,400</td>
<td align="right"></td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">14,800</td>
<td align="right">0.1%</td>
<td align="right">4,482</td>
<td align="right">0.0%</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">19,900</td>
<td align="right">0.1%</td>
<td align="right">6,390</td>
<td align="right">0.0%</td>
<td align="right">-67.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">267,420</td>
<td align="right">1.3%</td>
<td align="right">91,818</td>
<td align="right">0.5%</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">298,580</td>
<td align="right">1.5%</td>
<td align="right">105,534</td>
<td align="right">0.5%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">41,100</td>
<td align="right"></td>
<td align="right">15,606</td>
<td align="right"></td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">38,000</td>
<td align="right">0.8%</td>
<td align="right">14,676</td>
<td align="right">0.3%</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">17,809</td>
<td align="right"></td>
<td align="right">7,120</td>
<td align="right"></td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">2,250,448</td>
<td align="right">11.1%</td>
<td align="right">2,177,201</td>
<td align="right">10.9%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">7,027,167</td>
<td align="right">34.9%</td>
<td align="right">6,950,984</td>
<td align="right">35.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">17,693,813</td>
<td align="right">87.3%</td>
<td align="right">17,632,084</td>
<td align="right">88.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">12,825,434</td>
<td align="right">63.7%</td>
<td align="right">12,781,957</td>
<td align="right">64.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">4,851,320</td>
<td align="right">98.9%</td>
<td align="right">4,835,388</td>
<td align="right">99.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">4,867,500</td>
<td align="right">99.2%</td>
<td align="right">4,851,540</td>
<td align="right">99.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">5,896,638</td>
<td align="right"></td>
<td align="right">5,880,498</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">13,420</td>
<td align="right">0.3%</td>
<td align="right">13,392</td>
<td align="right">0.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">2,760</td>
<td align="right">0.1%</td>
<td align="right">2,760</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
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
func modification
<details>
<summary>ⓘ</summary>

Modifying a function, e.g. `func.__defaults__ = ...`, etc.
</details>
</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
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
<td align="right">20</td>
<td align="right">6</td>
<td align="right">-70.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2026-06-26
