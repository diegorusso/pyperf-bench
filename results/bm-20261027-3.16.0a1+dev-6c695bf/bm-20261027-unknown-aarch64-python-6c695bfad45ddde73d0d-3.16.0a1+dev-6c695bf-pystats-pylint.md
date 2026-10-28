
# Pystats results

- benchmark: pylint
- fork: python
- ref: 6c695bfad45ddde73d0d674286800fbe295f0627
- commit hash: 6c695bf
- commit date: 2026-10-27T22:56:42+00:00

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
<td align="right">276,629,394</td>
<td align="right">17.8%</td>
<td align="right">17.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">67,545,733</td>
<td align="right">4.3%</td>
<td align="right">22.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">64,837,537</td>
<td align="right">4.2%</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">59,722,351</td>
<td align="right">3.8%</td>
<td align="right">30.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">57,924,584</td>
<td align="right">3.7%</td>
<td align="right">33.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">57,749,223</td>
<td align="right">3.7%</td>
<td align="right">37.6%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">55,442,161</td>
<td align="right">3.6%</td>
<td align="right">41.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">50,864,326</td>
<td align="right">3.3%</td>
<td align="right">44.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">48,187,412</td>
<td align="right">3.1%</td>
<td align="right">47.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">41,128,684</td>
<td align="right">2.6%</td>
<td align="right">50.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">34,723,427</td>
<td align="right">2.2%</td>
<td align="right">52.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">34,493,124</td>
<td align="right">2.2%</td>
<td align="right">54.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">33,142,712</td>
<td align="right">2.1%</td>
<td align="right">56.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">30,198,486</td>
<td align="right">1.9%</td>
<td align="right">58.7%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">27,603,940</td>
<td align="right">1.8%</td>
<td align="right">60.5%</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">27,432,424</td>
<td align="right">1.8%</td>
<td align="right">62.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">25,750,717</td>
<td align="right">1.7%</td>
<td align="right">63.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">24,969,301</td>
<td align="right">1.6%</td>
<td align="right">65.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">23,657,100</td>
<td align="right">1.5%</td>
<td align="right">67.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">23,194,918</td>
<td align="right">1.5%</td>
<td align="right">68.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">21,602,188</td>
<td align="right">1.4%</td>
<td align="right">70.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">20,849,040</td>
<td align="right">1.3%</td>
<td align="right">71.3%</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">20,803,580</td>
<td align="right">1.3%</td>
<td align="right">72.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">20,062,179</td>
<td align="right">1.3%</td>
<td align="right">73.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">19,372,285</td>
<td align="right">1.2%</td>
<td align="right">75.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">18,975,960</td>
<td align="right">1.2%</td>
<td align="right">76.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">18,285,599</td>
<td align="right">1.2%</td>
<td align="right">77.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">17,940,240</td>
<td align="right">1.2%</td>
<td align="right">78.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">17,296,993</td>
<td align="right">1.1%</td>
<td align="right">79.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,419,140</td>
<td align="right">1.1%</td>
<td align="right">80.9%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">11,292,420</td>
<td align="right">0.7%</td>
<td align="right">81.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">10,805,793</td>
<td align="right">0.7%</td>
<td align="right">82.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">10,020,026</td>
<td align="right">0.6%</td>
<td align="right">83.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">9,492,980</td>
<td align="right">0.6%</td>
<td align="right">83.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">9,361,440</td>
<td align="right">0.6%</td>
<td align="right">84.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">8,709,966</td>
<td align="right">0.6%</td>
<td align="right">84.7%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">8,704,353</td>
<td align="right">0.6%</td>
<td align="right">85.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,630,237</td>
<td align="right">0.6%</td>
<td align="right">85.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">8,382,140</td>
<td align="right">0.5%</td>
<td align="right">86.4%</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,352,983</td>
<td align="right">0.5%</td>
<td align="right">86.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">8,158,185</td>
<td align="right">0.5%</td>
<td align="right">87.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,296,095</td>
<td align="right">0.4%</td>
<td align="right">87.9%</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,143,353</td>
<td align="right">0.4%</td>
<td align="right">88.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,087,160</td>
<td align="right">0.4%</td>
<td align="right">88.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,704,980</td>
<td align="right">0.4%</td>
<td align="right">89.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">5,649,820</td>
<td align="right">0.4%</td>
<td align="right">89.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">5,534,220</td>
<td align="right">0.4%</td>
<td align="right">89.7%</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">5,382,460</td>
<td align="right">0.3%</td>
<td align="right">90.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">5,149,680</td>
<td align="right">0.3%</td>
<td align="right">90.4%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,089,398</td>
<td align="right">0.3%</td>
<td align="right">90.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,608,940</td>
<td align="right">0.3%</td>
<td align="right">91.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">4,479,573</td>
<td align="right">0.3%</td>
<td align="right">91.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,370,306</td>
<td align="right">0.3%</td>
<td align="right">91.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">4,346,960</td>
<td align="right">0.3%</td>
<td align="right">91.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,843,560</td>
<td align="right">0.2%</td>
<td align="right">92.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,785,912</td>
<td align="right">0.2%</td>
<td align="right">92.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,770,418</td>
<td align="right">0.2%</td>
<td align="right">92.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,641,580</td>
<td align="right">0.2%</td>
<td align="right">92.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,316,040</td>
<td align="right">0.2%</td>
<td align="right">93.1%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,280,340</td>
<td align="right">0.2%</td>
<td align="right">93.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,227,400</td>
<td align="right">0.2%</td>
<td align="right">93.5%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,201,933</td>
<td align="right">0.2%</td>
<td align="right">93.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,126,960</td>
<td align="right">0.2%</td>
<td align="right">93.9%</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,100,960</td>
<td align="right">0.2%</td>
<td align="right">94.1%</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">2,948,120</td>
<td align="right">0.2%</td>
<td align="right">94.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,909,331</td>
<td align="right">0.2%</td>
<td align="right">94.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,825,740</td>
<td align="right">0.2%</td>
<td align="right">94.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,823,160</td>
<td align="right">0.2%</td>
<td align="right">94.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,701,071</td>
<td align="right">0.2%</td>
<td align="right">95.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,679,720</td>
<td align="right">0.2%</td>
<td align="right">95.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,652,180</td>
<td align="right">0.2%</td>
<td align="right">95.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,630,380</td>
<td align="right">0.2%</td>
<td align="right">95.5%</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">2,549,080</td>
<td align="right">0.2%</td>
<td align="right">95.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,530,160</td>
<td align="right">0.2%</td>
<td align="right">95.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,453,920</td>
<td align="right">0.2%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,410,080</td>
<td align="right">0.2%</td>
<td align="right">96.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,383,880</td>
<td align="right">0.2%</td>
<td align="right">96.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">2,334,400</td>
<td align="right">0.2%</td>
<td align="right">96.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,202,500</td>
<td align="right">0.1%</td>
<td align="right">96.6%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,003,593</td>
<td align="right">0.1%</td>
<td align="right">96.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,998,706</td>
<td align="right">0.1%</td>
<td align="right">96.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,936,420</td>
<td align="right">0.1%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,844,740</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,832,560</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,756,751</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,732,280</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,714,513</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,501,340</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,495,040</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">1,452,613</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,348,520</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,344,020</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">SEND_VIRTUAL</td>
<td align="right">1,311,640</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,289,940</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,251,453</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,237,660</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,167,760</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,166,820</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,150,040</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,142,700</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,123,660</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,108,460</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,074,820</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,017,540</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">907,320</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">860,740</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">780,480</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">747,800</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">697,610</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">663,670</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">663,670</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">660,960</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">626,500</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">626,415</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">616,420</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">616,020</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">602,212</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">478,620</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">461,800</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">437,940</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">433,600</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">402,200</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right">303,400</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">284,120</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">270,140</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_VIRTUAL</td>
<td align="right">261,960</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">260,460</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">256,400</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">229,600</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">217,900</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">204,580</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">188,980</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_EX_PY</td>
<td align="right">179,460</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">176,765</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">166,640</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">157,380</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">156,460</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">152,600</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">143,300</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">141,520</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">126,080</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">125,200</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">111,920</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">111,680</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">95,360</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">91,740</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">79,665</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">79,600</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">72,300</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">69,820</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">68,740</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">67,280</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">63,540</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">38,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">31,540</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">27,080</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">26,960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">23,800</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">20,220</td>
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
<td align="right">18,240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">16,640</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">13,460</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">11,220</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">10,240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">9,820</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">9,380</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">9,220</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">8,200</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">6,760</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">MATCH_CLASS</td>
<td align="right">6,180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,580</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,400</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">4,200</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">4,160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">4,120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">3,440</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,780</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1,420</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,300</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">700</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
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
<td align="right">51,509,823</td>
<td align="right">3.3%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_BORROW</td>
<td align="right">36,607,580</td>
<td align="right">2.4%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">33,528,673</td>
<td align="right">2.2%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_BORROW</td>
<td align="right">25,614,477</td>
<td align="right">1.6%</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST_BORROW</td>
<td align="right">25,594,045</td>
<td align="right">1.6%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_BORROW</td>
<td align="right">22,828,816</td>
<td align="right">1.5%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">21,960,806</td>
<td align="right">1.4%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW</td>
<td align="right">21,938,970</td>
<td align="right">1.4%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">21,270,788</td>
<td align="right">1.4%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_LIST</td>
<td align="right">21,143,151</td>
<td align="right">1.4%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE JUMP_BACKWARD_NO_JIT</td>
<td align="right">21,132,005</td>
<td align="right">1.4%</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">20,782,720</td>
<td align="right">1.3%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">20,697,228</td>
<td align="right">1.3%</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST_BORROW</td>
<td align="right">20,522,068</td>
<td align="right">1.3%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT RETURN_VALUE</td>
<td align="right">18,784,228</td>
<td align="right">1.2%</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW PUSH_NULL</td>
<td align="right">18,095,080</td>
<td align="right">1.2%</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">17,723,380</td>
<td align="right">1.1%</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">17,414,625</td>
<td align="right">1.1%</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST</td>
<td align="right">17,396,179</td>
<td align="right">1.1%</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_PY_EXACT_ARGS</td>
<td align="right">17,373,393</td>
<td align="right">1.1%</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW POP_JUMP_IF_NONE</td>
<td align="right">17,326,300</td>
<td align="right">1.1%</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE LOAD_FAST_BORROW</td>
<td align="right">16,941,420</td>
<td align="right">1.1%</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST LOAD_FAST_BORROW</td>
<td align="right">16,622,199</td>
<td align="right">1.1%</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">16,120,100</td>
<td align="right">1.0%</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE NOP</td>
<td align="right">16,080,480</td>
<td align="right">1.0%</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">15,379,593</td>
<td align="right">1.0%</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_GLOBAL_MODULE</td>
<td align="right">13,613,899</td>
<td align="right">0.9%</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_NON_PY_GENERAL</td>
<td align="right">13,536,380</td>
<td align="right">0.9%</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">COPY TO_BOOL_BOOL</td>
<td align="right">13,425,780</td>
<td align="right">0.9%</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,602,160</td>
<td align="right">0.8%</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW COMPARE_OP_STR</td>
<td align="right">12,549,740</td>
<td align="right">0.8%</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE RETURN_VALUE</td>
<td align="right">11,789,060</td>
<td align="right">0.8%</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR COPY</td>
<td align="right">11,647,240</td>
<td align="right">0.7%</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_BORROW</td>
<td align="right">11,297,020</td>
<td align="right">0.7%</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,274,380</td>
<td align="right">0.7%</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL TO_BOOL_BOOL</td>
<td align="right">11,058,260</td>
<td align="right">0.7%</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,462,940</td>
<td align="right">0.7%</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_CONST</td>
<td align="right">10,284,620</td>
<td align="right">0.7%</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW RETURN_VALUE</td>
<td align="right">9,870,060</td>
<td align="right">0.6%</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_FAST_BORROW</td>
<td align="right">9,697,260</td>
<td align="right">0.6%</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<td align="right">9,476,580</td>
<td align="right">0.6%</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">8,687,313</td>
<td align="right">0.6%</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE CALL_ISINSTANCE</td>
<td align="right">8,302,940</td>
<td align="right">0.5%</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,853,263</td>
<td align="right">0.5%</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,679,073</td>
<td align="right">0.5%</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,498,805</td>
<td align="right">0.5%</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE</td>
<td align="right">7,312,205</td>
<td align="right">0.5%</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,971,880</td>
<td align="right">0.4%</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_WITH_HINT</td>
<td align="right">6,970,660</td>
<td align="right">0.4%</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_COMMON_CONSTANT</td>
<td align="right">6,856,195</td>
<td align="right">0.4%</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST</td>
<td align="right">6,777,918</td>
<td align="right">0.4%</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">6,752,526</td>
<td align="right">0.4%</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,745,600</td>
<td align="right">0.4%</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">6,674,380</td>
<td align="right">0.4%</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,563,680</td>
<td align="right">0.4%</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR</td>
<td align="right">6,361,560</td>
<td align="right">0.4%</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST_BORROW</td>
<td align="right">6,124,102</td>
<td align="right">0.4%</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW POP_JUMP_IF_NOT_NONE</td>
<td align="right">6,077,225</td>
<td align="right">0.4%</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST COMPARE_OP_STR</td>
<td align="right">6,029,320</td>
<td align="right">0.4%</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,011,593</td>
<td align="right">0.4%</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR POP_JUMP_IF_FALSE</td>
<td align="right">5,835,460</td>
<td align="right">0.4%</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE</td>
<td align="right">5,697,380</td>
<td align="right">0.4%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_SLOT</td>
<td align="right">5,621,780</td>
<td align="right">0.4%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">5,270,568</td>
<td align="right">0.3%</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST_BORROW</td>
<td align="right">5,118,600</td>
<td align="right">0.3%</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">5,011,660</td>
<td align="right">0.3%</td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST POP_ITER</td>
<td align="right">4,886,433</td>
<td align="right">0.3%</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_COMMON_CONSTANT</td>
<td align="right">4,830,600</td>
<td align="right">0.3%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE TO_BOOL_BOOL</td>
<td align="right">4,788,580</td>
<td align="right">0.3%</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL FOR_ITER_LIST</td>
<td align="right">4,720,520</td>
<td align="right">0.3%</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE LOAD_FAST_BORROW</td>
<td align="right">4,544,752</td>
<td align="right">0.3%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS RESUME_CHECK</td>
<td align="right">4,525,280</td>
<td align="right">0.3%</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT LOAD_FAST_BORROW</td>
<td align="right">4,460,880</td>
<td align="right">0.3%</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST_BORROW</td>
<td align="right">4,276,640</td>
<td align="right">0.3%</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL RESUME_CHECK</td>
<td align="right">4,258,040</td>
<td align="right">0.3%</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">4,203,880</td>
<td align="right">0.3%</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_COMMON_CONSTANT</td>
<td align="right">4,122,480</td>
<td align="right">0.3%</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW CALL_PY_EXACT_ARGS</td>
<td align="right">4,107,640</td>
<td align="right">0.3%</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_BORROW</td>
<td align="right">4,066,600</td>
<td align="right">0.3%</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE COMPARE_OP_INT</td>
<td align="right">3,931,720</td>
<td align="right">0.3%</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">3,931,208</td>
<td align="right">0.3%</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS</td>
<td align="right">3,917,400</td>
<td align="right">0.3%</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_SMALL_INT</td>
<td align="right">3,903,831</td>
<td align="right">0.3%</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS MAKE_CELL</td>
<td align="right">3,826,100</td>
<td align="right">0.2%</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BINARY_OP_SUBSCR_DICT</td>
<td align="right">3,788,360</td>
<td align="right">0.2%</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,632,700</td>
<td align="right">0.2%</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">POP_TOP JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,578,286</td>
<td align="right">0.2%</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">POP_ITER LOAD_FAST_BORROW</td>
<td align="right">3,535,780</td>
<td align="right">0.2%</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">NOP LOAD_COMMON_CONSTANT</td>
<td align="right">3,519,420</td>
<td align="right">0.2%</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE</td>
<td align="right">3,453,820</td>
<td align="right">0.2%</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT STORE_FAST</td>
<td align="right">3,368,375</td>
<td align="right">0.2%</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE</td>
<td align="right">3,332,180</td>
<td align="right">0.2%</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF LOAD_FAST_BORROW</td>
<td align="right">3,321,540</td>
<td align="right">0.2%</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST CALL_KW_PY</td>
<td align="right">3,308,920</td>
<td align="right">0.2%</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_DEREF</td>
<td align="right">3,304,260</td>
<td align="right">0.2%</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_TUPLE</td>
<td align="right">3,282,240</td>
<td align="right">0.2%</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW LOAD_FAST_BORROW</td>
<td align="right">3,226,280</td>
<td align="right">0.2%</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,214,860</td>
<td align="right">0.2%</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">POP_TOP RESUME_CHECK</td>
<td align="right">3,196,653</td>
<td align="right">0.2%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_GLOBAL_MODULE</td>
<td align="right">3,161,220</td>
<td align="right">0.2%</td>
<td align="right">66.9%</td>
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
<td align="right">589,300</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">217,060</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">37,600</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">16,920</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">16,920</td>
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
<td align="left">STORE_FAST</td>
<td align="right">248,880</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">173,360</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">145,060</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">100,860</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">63,420</td>
<td align="right">7.0%</td>
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
<td align="right">700</td>
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
<td align="right">700</td>
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
<td align="right">334,740</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">112,020</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">98,260</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">16,740</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">16,040</td>
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
<td align="left">FOR_ITER</td>
<td align="right">383,040</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">124,320</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">69,420</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">19,360</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">9,220</td>
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
<td align="right">16,120,100</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,313,320</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">469,440</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">73,960</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">67,180</td>
<td align="right">0.4%</td>
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
<td align="right">57,380</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,160</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,320</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">460</td>
<td align="right">0.7%</td>
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
<td align="right">67,280</td>
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
<td align="right">1,260</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">440</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">80</td>
<td align="right">4.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">380</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">CALL_EX_PY</td>
<td align="right">220</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">120</td>
<td align="right">6.8%</td>
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
<td align="right">499,720</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">153,220</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">40,265</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,300</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,820</td>
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
<td align="right">697,590</td>
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
<td align="right">18,240</td>
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
<td align="right">16,820</td>
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
<td align="right">52,640</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">13,680</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,920</td>
<td align="right">8.2%</td>
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
<td align="right">52,600</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">13,680</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,780</td>
<td align="right">5.2%</td>
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
<td align="right">1,452,613</td>
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
<td align="right">1,452,613</td>
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
<td align="right">801,520</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">693,100</td>
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
<td align="right">1,495,040</td>
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
<td align="right">433,600</td>
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
<td align="right">433,600</td>
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
<td align="right">430,580</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">299,660</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">153,860</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">111,680</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">62,880</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">614,940</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">491,000</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">13,900</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,820</td>
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
<td align="right">17,723,380</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,117,960</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">134,620</td>
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
<td align="right">8,600</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">440</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">420</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">220</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">140</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">10,240</td>
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
<td align="right">4,160</td>
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
<td align="right">4,160</td>
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
<td align="right">1,251,453</td>
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
<td align="right">988,620</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">169,513</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">49,020</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">21,560</td>
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
<td align="right">16,080,480</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,039,320</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,466,560</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,162,600</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">956,860</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,274,380</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">3,519,420</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,082,760</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,916,480</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,845,120</td>
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
<td align="right">259,185</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">181,740</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">99,765</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">91,100</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">23,820</td>
<td align="right">3.6%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">243,740</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">179,620</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">91,100</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">61,645</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">32,825</td>
<td align="right">4.9%</td>
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
<td align="right">4,886,433</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,361,140</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">1,452,613</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">710,240</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">455,240</td>
<td align="right">4.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">3,535,780</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">2,730,306</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,134,200</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">379,160</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">364,240</td>
<td align="right">3.6%</td>
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
<td align="right">9,476,580</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,725,733</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,722,483</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">2,081,553</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,714,513</td>
<td align="right">6.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">6,856,195</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,118,600</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,578,286</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,196,653</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,589,780</td>
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
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">131,440</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">120,600</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">118,320</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">115,740</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">73,960</td>
<td align="right">11.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">514,605</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">138,860</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,400</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,700</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,005</td>
<td align="right">0.2%</td>
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
<td align="right">18,095,080</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,931,208</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,094,700</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">887,193</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">549,980</td>
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
<td align="right">20,522,068</td>
<td align="right">82.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,307,840</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">885,153</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">326,700</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">262,840</td>
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
<td align="right">1,326,640</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">856,353</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">233,460</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">169,280</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">162,900</td>
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
<td align="right">1,655,220</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">887,193</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">134,980</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">134,620</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">108,980</td>
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
<td align="right">18,784,228</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,789,060</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,870,060</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,674,380</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,306,060</td>
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
<td align="right">17,723,380</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,476,580</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,687,313</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,674,380</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,788,580</td>
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
<td align="right">1,280</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">1,140</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">160</td>
<td align="right">12.3%</td>
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
<td align="right">87,240</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">27,100</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">25,620</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,340</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">6,080</td>
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
<td align="right">93,720</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">24,140</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">11,020</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,520</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">7,140</td>
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
<td align="right">245,060</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">208,832</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">61,660</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">16,820</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,840</td>
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
<td align="right">302,540</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">250,432</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">30,900</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,880</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,040</td>
<td align="right">0.5%</td>
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
<td align="right">2,900</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,300</td>
<td align="right">31.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">4,100</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">40</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">40</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20</td>
<td align="right">0.5%</td>
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
<td align="right">1,440</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">680</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">620</td>
<td align="right">3.1%</td>
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
<td align="right">238,820</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">12,640</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,300</td>
<td align="right">0.9%</td>
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
<td align="right">175,820</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">73,260</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,160</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,300</td>
<td align="right">0.9%</td>
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
<td align="right">4,400</td>
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
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,240</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">240</td>
<td align="right">5.5%</td>
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
<td align="right">848,540</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">375,020</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">332,880</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">193,920</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">98,200</td>
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
<td align="left">STORE_FAST</td>
<td align="right">786,693</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">451,580</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">222,280</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">151,820</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">96,160</td>
<td align="right">4.8%</td>
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
<td align="right">2,762,220</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">741,280</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">674,700</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">325,320</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">324,980</td>
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
<td align="right">2,762,440</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,476,660</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">733,440</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">671,560</td>
<td align="right">10.9%</td>
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
<td align="right">680,240</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">330,960</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">216,180</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">170,880</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">139,400</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,360,580</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">283,260</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">98,200</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">70,280</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">35,780</td>
<td align="right">1.8%</td>
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
<td align="right">87,720</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">67,820</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,480</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,380</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,200</td>
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
<td align="right">90,460</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">69,040</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,480</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">860</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">500</td>
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
<td align="right">23,700</td>
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
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,340</td>
<td align="right">47.6%</td>
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
<td align="right">491,000</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">135,500</td>
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
<td align="right">444,940</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">101,760</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,200</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">11,660</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">11,300</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">985,720</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">848,933</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">754,040</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">749,040</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">544,420</td>
<td align="right">10.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,368,920</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">950,220</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">916,600</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">472,020</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">222,500</td>
<td align="right">4.4%</td>
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
<td align="right">56,540</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">34,000</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">19,740</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">12,340</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,860</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">33,840</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">23,360</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">20,320</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">16,820</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">16,720</td>
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
<td align="right">98,720</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">80,600</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">16,820</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">14,040</td>
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
<td align="right">104,340</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">96,700</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,260</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,580</td>
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

### CALL_INTRINSIC_2

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_2 </summary>

<table>
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
<td align="right">8,060</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">100</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">40</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,160</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">40</td>
<td align="right">0.5%</td>
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
<td align="right">20,220</td>
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
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">3,580</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,120</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,780</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,660</td>
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
<td align="right">2,110,800</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">1,369,660</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">145,192</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">35,260</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">27,560</td>
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
<td align="right">2,262,212</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,480,880</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">17,800</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">6,700</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,060</td>
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
<td align="right">1,368,920</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">912,020</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">538,240</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">321,820</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">196,420</td>
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
<td align="right">2,327,280</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,037,120</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">201,700</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">40,220</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">12,720</td>
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
<td align="right">109,740</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,840</td>
<td align="right">1.6%</td>
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
<td align="right">111,680</td>
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
<td align="right">11,647,240</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,190,340</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">953,620</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">885,773</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">458,160</td>
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
<td align="right">13,425,780</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">887,173</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">575,020</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">518,480</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">517,540</td>
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
<td align="right">2,313,320</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,515,740</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">493,440</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">115,280</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">75,180</td>
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
<td align="right">4,525,280</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">77,340</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5,500</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">820</td>
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
<td align="right">11,220</td>
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
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">4,480</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">4,460</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,060</td>
<td align="right">18.4%</td>
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
<td align="right">456,880</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,600</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,320</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">500</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">500</td>
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
<td align="right">282,340</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">CALL_EX_PY</td>
<td align="right">176,880</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,320</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,260</td>
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
<td align="left">MAP_ADD</td>
<td align="right">940</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">320</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">120</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">20</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">20</td>
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
<td align="left">BUILD_MAP</td>
<td align="right">840</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">340</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">100</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">100</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">40</td>
<td align="right">2.8%</td>
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
<td align="right">2,171,860</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,783,280</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">409,520</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">403,760</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">276,480</td>
<td align="right">4.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">2,936,940</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,031,480</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">974,500</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">918,540</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">105,880</td>
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
<td align="right">2,062,720</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">918,540</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">389,240</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">383,040</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">74,020</td>
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
<td align="right">2,385,880</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">717,040</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">710,240</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">8,840</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,920</td>
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
<td align="right">140,900</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,460</td>
<td align="right">7.5%</td>
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
<td align="right">121,560</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">27,040</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">4,000</td>
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
<td align="right">140,760</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">15,440</td>
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
<td align="right">140,900</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">8,400</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,100</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20</td>
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
<td align="right">1,230,978</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">911,253</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">477,960</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">149,540</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">36,000</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,342,658</td>
<td align="right">80.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">429,320</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">80,513</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">30,080</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,340</td>
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
<td align="right">4,760</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,900</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,200</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,400</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,380</td>
<td align="right">8.3%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">16,640</td>
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
<td align="right">1,015,860</td>
<td align="right">78.8%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">243,740</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">29,180</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,140</td>
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
<td align="right">498,180</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">442,380</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">145,280</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">97,820</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">76,440</td>
<td align="right">5.9%</td>
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
<td align="right">2,316,720</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">417,640</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">301,633</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">166,860</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">120,740</td>
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
<td align="right">2,288,300</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">266,645</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">226,993</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">210,620</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">201,780</td>
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
<td align="right">1,841,640</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">285,720</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">181,440</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">100,860</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">98,320</td>
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
<td align="right">2,789,960</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">11,940</td>
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
<td align="right">2,200</td>
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
<td align="right">33,480</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">23,620</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,380</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">3,220</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,900</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">33,560</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">14,040</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">13,180</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,160</td>
<td align="right">7.4%</td>
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
<td align="right">6,361,560</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">889,040</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">555,100</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">404,700</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">209,600</td>
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
<td align="right">1,437,700</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,169,600</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">957,660</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">856,800</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">748,460</td>
<td align="right">7.9%</td>
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
<td align="right">6,856,195</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,830,600</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,122,480</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,519,420</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,730,306</td>
<td align="right">7.9%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">18,784,228</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,460,880</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,786,440</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,740,220</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">911,253</td>
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
<td align="right">10,284,620</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,293,100</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,566,140</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,032,020</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">950,220</td>
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
<td align="right">6,029,320</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,308,920</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">2,545,500</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,916,480</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,251,453</td>
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
<td align="right">3,304,260</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,109,820</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,845,120</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,240,860</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,013,540</td>
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
<td align="right">3,321,540</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,854,700</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,094,700</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">704,120</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">457,560</td>
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
<td align="right">2,013,015</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,493,620</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,154,973</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">850,165</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">593,880</td>
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
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">1,539,833</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,376,200</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,241,400</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,190,340</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,001,600</td>
<td align="right">12.0%</td>
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
<td align="right">1,376,200</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,052,380</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">164,400</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">96,960</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">54,300</td>
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
<td align="left">SWAP</td>
<td align="right">2,771,440</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">54,300</td>
<td align="right">1.9%</td>
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
<td align="right">36,607,580</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">25,614,477</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">25,594,045</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">22,828,816</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21,938,970</td>
<td align="right">7.9%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">51,509,823</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18,095,080</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,373,393</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">17,326,300</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,613,899</td>
<td align="right">4.9%</td>
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
<td align="right">11,274,380</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,971,880</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,745,600</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,011,660</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,632,700</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">20,782,720</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,107,640</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,226,280</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,628,340</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,112,540</td>
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
<td align="right">120,560</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">119,540</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">78,720</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">77,720</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">37,180</td>
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
<td align="right">122,020</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">119,520</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">75,620</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">75,620</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">37,340</td>
<td align="right">7.8%</td>
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
<td align="right">96,400</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">32,240</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">28,720</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,900</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,340</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">76,700</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">29,360</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">28,740</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">14,420</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">12,360</td>
<td align="right">6.5%</td>
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
<td align="right">3,440</td>
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
<td align="right">3,140</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">300</td>
<td align="right">8.7%</td>
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
<td align="right">29,260</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">26,160</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">25,700</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">11,360</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">11,360</td>
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
<td align="right">50,405</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">36,020</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">31,840</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,100</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,640</td>
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
<td align="right">32,320</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">16,920</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">10,320</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,440</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,600</td>
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
<td align="right">17,500</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">15,340</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">12,180</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">12,100</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,440</td>
<td align="right">10.3%</td>
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
<td align="right">3,903,831</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">549,140</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">527,906</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">522,300</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">420,060</td>
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
<td align="right">1,843,460</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,028,086</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">863,060</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">848,540</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">787,206</td>
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
<td align="right">575,020</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">575,020</td>
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
<td align="right">575,020</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">557,260</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">16,480</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,280</td>
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
<td align="right">4,120</td>
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
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,360</td>
<td align="right">33.0%</td>
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
<td align="right">5.3%</td>
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
<td align="right">3,826,100</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,322,720</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">455,240</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">16,380</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">15,200</td>
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
<td align="right">4,258,040</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,322,720</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">61,320</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">7,740</td>
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
<td align="left">BUILD_MAP</td>
<td align="right">15,300</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,360</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,080</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,380</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,320</td>
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
<td align="left">EXTENDED_ARG</td>
<td align="right">12,060</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,880</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,880</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">940</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">160</td>
<td align="right">0.6%</td>
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
<td align="right">3,960</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">2,220</td>
<td align="right">35.9%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">6,180</td>
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
<td align="right">33,528,673</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,752,526</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,835,460</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,453,820</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,936,940</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">25,614,477</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">11,789,060</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,462,940</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">4,122,480</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,332,180</td>
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
<td align="right">17,326,300</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">234,040</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">221,200</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">81,380</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">52,960</td>
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
<td align="right">16,941,420</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">555,940</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">166,140</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">120,560</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">61,800</td>
<td align="right">0.3%</td>
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
<td align="right">6,077,225</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,390,860</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">448,380</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">157,660</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,780</td>
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
<td align="right">4,544,752</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">956,860</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">922,593</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">478,260</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">463,620</td>
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
<td align="right">21,270,788</td>
<td align="right">64.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,262,212</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,005,360</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,685,220</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,330,960</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">21,132,005</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,124,102</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,281,240</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,109,180</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">974,860</td>
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
<td align="right">111,180</td>
<td align="right">88.2%</td>
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
<td align="right">115,740</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">4,460</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,320</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,140</td>
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
<td align="right">104,340</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">91,100</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">78,880</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">4,460</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,200</td>
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
<td align="right">88,880</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">80,600</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">14,380</td>
<td align="right">7.8%</td>
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
<td align="right">76,440</td>
<td align="right">96.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">3,040</td>
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
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">960</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">960</td>
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
<td align="right">21,200</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,380</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,140</td>
<td align="right">13.1%</td>
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
<td align="right">30,260</td>
<td align="right">95.9%</td>
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
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">20</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
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
<td align="right">988,620</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">86,200</td>
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
<td align="right">696,140</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">99,020</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">86,200</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">79,800</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">52,100</td>
<td align="right">4.8%</td>
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
<td align="right">68,720</td>
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
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">420</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">300</td>
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
<td align="right">1,504,080</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">482,280</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">338,040</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">70,760</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,800</td>
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
<td align="right">1,025,640</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">779,840</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">233,120</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">133,640</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">74,760</td>
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
<td align="right">82,540</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">59,760</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">25,480</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">17,320</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">15,680</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">93,120</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">81,380</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">23,980</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">18,020</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">14,960</td>
<td align="right">5.5%</td>
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
<td align="right">8,687,313</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,777,918</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,368,375</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">3,129,240</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,632,260</td>
<td align="right">4.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">21,938,970</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,679,073</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,971,880</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,270,568</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,863,893</td>
<td align="right">4.9%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">1,860</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">180</td>
<td align="right">8.8%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,820</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">140</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">40</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">40</td>
<td align="right">2.0%</td>
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
<td align="right">17,396,179</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,162,940</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">792,480</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">379,160</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">158,860</td>
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
<td align="right">16,622,199</td>
<td align="right">82.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,228,640</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">792,480</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">727,100</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">275,920</td>
<td align="right">1.4%</td>
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
<td align="right">260</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">200</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">60</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">20</td>
<td align="right">7.1%</td>
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
<td align="right">33,400</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">31,700</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">27,040</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">21,560</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20,320</td>
<td align="right">9.9%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">78,800</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">32,320</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">20,860</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">17,940</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">15,580</td>
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
<td align="right">2,771,440</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,762,440</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,134,200</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">592,760</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">575,020</td>
<td align="right">6.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">2,762,220</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">2,716,140</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,091,720</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">592,760</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">575,020</td>
<td align="right">6.1%</td>
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
<td align="right">387,500</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,440</td>
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
<td align="right">1,162,940</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,380</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">300</td>
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
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">733,580</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">SEND_VIRTUAL</td>
<td align="right">510,120</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">448,920</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">243,260</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,564,000</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,117,960</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,104,013</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">448,920</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">181,440</td>
<td align="right">4.1%</td>
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
<td align="right">16,720</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">14,120</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">7,740</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">5,500</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,080</td>
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
<td align="right">16,480</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">11,360</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,320</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,620</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,940</td>
<td align="right">6.2%</td>
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
<td align="right">863,060</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">755,720</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">755,720</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">141,040</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">78,480</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,820,120</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">278,200</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">97,580</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">93,260</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">92,360</td>
<td align="right">3.5%</td>
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
<td align="right">357,480</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">268,160</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">58,460</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">48,800</td>
<td align="right">6.5%</td>
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
<td align="right">257,560</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">234,060</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">82,020</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">57,380</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">40,540</td>
<td align="right">5.4%</td>
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
<td align="right">97,940</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">12,120</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,600</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,000</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">4,100</td>
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
<td align="left">TO_BOOL_INT</td>
<td align="right">99,620</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,060</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">10,340</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">5,300</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,000</td>
<td align="right">2.8%</td>
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
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">8,680</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">8,440</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,720</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,060</td>
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
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">16,580</td>
<td align="right">13.2%</td>
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
<td align="right">8,420</td>
<td align="right">6.7%</td>
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
<td align="right">3,788,360</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,206,340</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">133,440</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">112,060</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">42,060</td>
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
<td align="right">1,617,720</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">1,508,120</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,036,100</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">755,020</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">131,440</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">29,425</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">28,140</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">21,180</td>
<td align="right">26.6%</td>
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
<td align="right">76,345</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,980</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">700</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">380</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">240</td>
<td align="right">0.3%</td>
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
<td align="right">891,680</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">787,206</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">556,625</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">386,060</td>
<td align="right">14.3%</td>
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
<td align="right">1,244,360</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">420,060</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">387,745</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">149,380</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">115,800</td>
<td align="right">4.3%</td>
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
<td align="right">241,660</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">12,360</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,080</td>
<td align="right">2.3%</td>
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
<td align="right">133,320</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">91,420</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,480</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,680</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">6,080</td>
<td align="right">2.3%</td>
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
<td align="right">1,045,160</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">242,420</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">212,280</td>
<td align="right">14.1%</td>
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
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">313,760</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">111,840</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">87,800</td>
<td align="right">5.8%</td>
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
<td align="right">1,843,460</td>
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
<td align="right">490,100</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">472,400</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">403,060</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">88,880</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">80,680</td>
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
<td align="right">679,120</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">41,200</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">35,680</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">8,960</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,740</td>
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
<td align="left">STORE_FAST</td>
<td align="right">247,700</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">209,040</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">135,400</td>
<td align="right">17.3%</td>
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
<td align="right">274,360</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">100,640</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">35,420</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">13,460</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">6,080</td>
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
<td align="right">391,060</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">43,160</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,040</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">460</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">100</td>
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
<td align="right">1,299,320</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">933,400</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">217,620</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">98,340</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">38,640</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">1,944,220</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">493,440</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">169,280</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,720</td>
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
<td align="right">6,120</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,100</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,080</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">200</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">100</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">9,620</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">100</td>
<td align="right">1.0%</td>
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
<td align="right">316,540</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">167,880</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">CALL_EX_NON_PY_GENERAL</td>
<td align="right">134,500</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">93,380</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">45,880</td>
<td align="right">4.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">351,380</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">282,300</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">116,740</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">112,020</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">74,000</td>
<td align="right">7.3%</td>
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
<td align="right">2,628,340</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">464,280</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">369,620</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">364,800</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">216,580</td>
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
<td align="left">STORE_FAST</td>
<td align="right">2,632,260</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">655,260</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">316,260</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">208,060</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">139,660</td>
<td align="right">3.2%</td>
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
<td align="right">2,018,960</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">468,340</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">82,640</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">32,240</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">21,560</td>
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
<td align="right">1,476,960</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">755,720</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">183,195</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">161,600</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">41,210</td>
<td align="right">1.5%</td>
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
<td align="right">493,175</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">28,040</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">27,620</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">24,740</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">10,460</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">246,315</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">174,020</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">98,180</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">45,880</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">31,320</td>
<td align="right">5.0%</td>
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
<td align="right">282,340</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">12,520</td>
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
<td align="right">134,500</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">80,880</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">47,400</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">35,720</td>
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
<td align="right">176,880</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,340</td>
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
<td align="right">114,820</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">62,140</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">860</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">380</td>
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
<td align="right">8,302,940</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,312,205</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,159,480</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">916,600</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">658,080</td>
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
<td align="right">17,414,625</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">953,620</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">854,620</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">117,460</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">17,280</td>
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
<td align="right">616,060</td>
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
<td align="right">583,440</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">28,040</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">4,560</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">260</td>
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
<td align="right">2,545,500</td>
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
<td align="right">1,874,120</td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">233,380</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">166,860</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">111,180</td>
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
<td align="right">3,308,920</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">5,200</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,800</td>
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
<td align="right">2,948,380</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">233,460</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">115,280</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">16,380</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,800</td>
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
<td align="right">1,452,206</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">160,585</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">45,300</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,700</td>
<td align="right">1.1%</td>
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
<td align="right">570,840</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">527,906</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">123,420</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">93,380</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">80,260</td>
<td align="right">4.6%</td>
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
<td align="right">1,247,940</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">84,893</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">82,020</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">57,880</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">44,760</td>
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
<td align="left">POP_TOP</td>
<td align="right">1,714,513</td>
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
<td align="right">1,050,460</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">746,020</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">731,340</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">671,560</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">567,160</td>
<td align="right">11.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,597,940</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,306,060</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">999,980</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">591,840</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">269,440</td>
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
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">110,040</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">90,080</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">73,660</td>
<td align="right">18.3%</td>
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
<td align="right">140,140</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">83,540</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">73,400</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">46,520</td>
<td align="right">11.6%</td>
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
<td align="right">2,500,320</td>
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
<td align="right">2,640</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">700</td>
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
<td align="right">980,940</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">696,680</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">334,740</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">231,860</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">117,380</td>
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
<td align="right">368,980</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">78,860</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">64,160</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">54,400</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">46,340</td>
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
<td align="left">POP_TOP</td>
<td align="right">312,700</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">120,600</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">74,620</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">62,760</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">54,640</td>
<td align="right">8.3%</td>
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
<td align="right">13,536,380</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">858,600</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">757,920</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">427,520</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">326,700</td>
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
<td align="right">11,058,260</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,716,160</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,278,620</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">773,900</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">556,220</td>
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
<td align="right">17,373,393</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,107,640</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,917,400</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">755,720</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">618,813</td>
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
<td align="right">21,960,806</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,826,100</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,515,740</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,486,820</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">1,326,640</td>
<td align="right">4.4%</td>
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
<td align="right">1,341,800</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">604,840</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">487,860</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">465,580</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">183,040</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">2,414,620</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">455,240</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">162,900</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">113,260</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">75,180</td>
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
<td align="right">22,140</td>
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
<td align="right">5.2%</td>
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
<td align="right">11,000</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,080</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,240</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,120</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,700</td>
<td align="right">6.3%</td>
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
<td align="right">111,020</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">460</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">340</td>
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
<td align="right">108,300</td>
<td align="right">96.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,060</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">620</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">600</td>
<td align="right">0.5%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">773,400</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">328,580</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,320</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,060</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">743,420</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">128,520</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">120,340</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">42,060</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">37,160</td>
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
<td align="right">5,840</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">880</td>
<td align="right">13.0%</td>
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
<td align="right">5,840</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">900</td>
<td align="right">13.3%</td>
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
<td align="right">3,931,720</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,111,460</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,028,086</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">704,120</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">484,820</td>
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
<td align="right">6,752,526</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,685,220</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">151,860</td>
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
<td align="right">12,549,740</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,029,320</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,001,100</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">696,680</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">120,360</td>
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
<td align="left">COPY</td>
<td align="right">11,647,240</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,835,460</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,171,860</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">850,080</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">275,800</td>
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
<td align="right">1,566,080</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">260,020</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">236,520</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">151,820</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">94,320</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,313,460</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">77,720</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">42,280</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">10,700</td>
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
<td align="right">851,146</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">318,620</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">277,980</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">271,140</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">119,860</td>
<td align="right">6.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">864,946</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">804,460</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">195,140</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">69,760</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">36,220</td>
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
<td align="right">2,195,353</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">GET_ITER_SELF</td>
<td align="right">1,130,980</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">885,153</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">105,880</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">48,040</td>
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
<td align="right">2,283,413</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,081,553</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,940</td>
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
<td align="right">21,143,151</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">4,720,520</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">974,500</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">586,593</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,920</td>
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
<td align="right">15,379,593</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,777,918</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">4,886,433</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">387,500</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">440</td>
<td align="right">0.0%</td>
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
<td align="right">1,032,740</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">124,320</td>
<td align="right">10.7%</td>
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
<td align="right">1,056,580</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">110,240</td>
<td align="right">9.4%</td>
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
<td align="right">3,282,240</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">GET_ITER_VIRTUAL</td>
<td align="right">2,162,200</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">256,860</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,220</td>
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
<td align="right">3,129,240</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,361,140</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">213,320</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">440</td>
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
<td align="right">249,540</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">12,220</td>
<td align="right">4.7%</td>
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
<td align="right">246,320</td>
<td align="right">94.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">12,420</td>
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
<td align="right">1,655,220</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">282,300</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">165,000</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">98,420</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">71,880</td>
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
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,130,980</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">700,020</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">389,240</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">58,780</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">54,160</td>
<td align="right">2.3%</td>
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
<td align="right">2,716,140</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,560,440</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,539,833</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,508,120</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">456,680</td>
<td align="right">5.2%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">4,720,520</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,162,200</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">856,353</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">812,980</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">148,120</td>
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
<td align="right">21,132,005</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,578,286</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,863,893</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,789,960</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,272,240</td>
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
<td align="right">21,143,151</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">3,282,240</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,412,300</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">2,195,353</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,062,720</td>
<td align="right">6.0%</td>
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
<td align="right">1,648,360</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">36,920</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">21,060</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,640</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,620</td>
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
<td align="right">1,032,020</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">549,980</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">67,580</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">45,220</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,900</td>
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
<td align="right">3,214,860</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">37,160</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">15,960</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,680</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,360</td>
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
<td align="right">1,369,660</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">731,340</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">550,540</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">544,420</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">37,240</td>
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
<td align="right">9,100</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">120</td>
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
<td align="right">6,240</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,860</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">120</td>
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
<td align="right">51,509,823</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,397,700</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,112,540</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">947,840</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">364,800</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">25,594,045</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,697,380</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,626,600</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,397,700</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,293,100</td>
<td align="right">4.0%</td>
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
<td align="right">11,840</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,080</td>
<td align="right">8.0%</td>
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
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,320</td>
<td align="right">24.7%</td>
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
<td align="right">6,011,593</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,348,820</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">856,800</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">591,840</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">579,920</td>
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
<td align="right">4,066,600</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,500,320</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,566,140</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">757,260</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">504,793</td>
<td align="right">4.7%</td>
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
<td align="right">12,602,160</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,854,700</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,980,120</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,001,600</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">885,700</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">11,297,020</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,917,400</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,875,500</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,341,800</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">593,880</td>
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
<td align="right">20,697,228</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">622,640</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">184,560</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">47,640</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">28,440</td>
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
<td align="right">8,302,940</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,931,720</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,931,208</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,584,720</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">985,720</td>
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
<td align="right">139,440</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">980</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">480</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">480</td>
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
<td align="right">135,760</td>
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
<td align="right">2,799,860</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">242,420</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">41,200</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">6,440</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,420</td>
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
<td align="right">1,560,440</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">890,660</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">234,040</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">196,420</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">46,160</td>
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
<td align="right">878,100</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">371,220</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">254,800</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">231,560</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">70,440</td>
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
<td align="right">1,821,420</td>
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
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">180</td>
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
<td align="right">5,621,780</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">316,740</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">183,195</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">53,880</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">53,320</td>
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
<td align="right">3,368,375</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">990,860</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">579,920</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">282,680</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">228,000</td>
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
<td align="right">6,970,660</td>
<td align="right">83.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">647,360</td>
<td align="right">7.7%</td>
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
<td align="right">99,980</td>
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
<td align="right">1,133,740</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">947,840</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">889,040</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">885,700</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">843,260</td>
<td align="right">10.1%</td>
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
<td align="right">10,462,940</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,853,263</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,679,073</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">7,498,805</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,916,480</td>
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
<td align="right">22,828,816</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">7,312,205</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">5,011,660</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,304,260</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">885,773</td>
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
<td align="right">13,613,899</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,697,380</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,270,568</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,203,880</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,332,180</td>
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
<td align="right">20,697,228</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,276,640</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,214,860</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,161,220</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,050,940</td>
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
<td align="right">37,780</td>
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
<td align="right">34,160</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,280</td>
<td align="right">6.0%</td>
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
<td align="right">2,946,340</td>
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
<td align="right">2,806,080</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">98,380</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">31,120</td>
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
<td align="right">21,960,806</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">16,120,100</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,525,280</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,258,040</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,196,653</td>
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
<td align="right">36,607,580</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,853,263</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,745,600</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,203,880</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,725,733</td>
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
<td align="right">699,360</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">442,380</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">960</td>
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
<td align="right">649,780</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">492,300</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">620</td>
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
<td align="right">812,560</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">498,180</td>
<td align="right">38.0%</td>
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
<td align="right">801,520</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">510,120</td>
<td align="right">38.9%</td>
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
<td align="right">20,782,720</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,563,680</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">235,280</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">11,920</td>
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
<td align="right">16,080,480</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">4,830,600</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,632,700</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,346,420</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">862,700</td>
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
<td align="right">2,096,420</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">278,100</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,120</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,360</td>
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
<td align="right">1,162,600</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">612,700</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">294,940</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">143,260</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">93,020</td>
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
<td align="right">506,780</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">406,680</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">182,480</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">88,500</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">34,400</td>
<td align="right">2.8%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">472,400</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">236,920</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">191,700</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">185,400</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">55,600</td>
<td align="right">4.5%</td>
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
<td align="right">764,100</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">70,480</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">18,820</td>
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
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">74,320</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">19,740</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">9,560</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,380</td>
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
<td align="right">2,268,260</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,736,120</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">843,260</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">476,600</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">69,800</td>
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
<td align="right">3,453,820</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,005,360</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">61,280</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">9,780</td>
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
<td align="right">17,414,625</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">13,425,780</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">11,058,260</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,788,580</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,800,515</td>
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
<td align="right">33,528,673</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">21,270,788</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">403,760</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">238,820</td>
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
<td align="right">661,600</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">361,580</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">101,200</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">99,620</td>
<td align="right">7.4%</td>
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
<td align="right">850,100</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">272,680</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">208,520</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">12,640</td>
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
<td align="right">685,240</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">419,160</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">119,020</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">78,440</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">20,980</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">796,620</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">543,720</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">5,300</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">2,300</td>
<td align="right">0.2%</td>
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
<td align="right">1,489,040</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">776,760</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">518,480</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">174,320</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">99,760</td>
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
<td align="right">2,183,220</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">929,560</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">9,820</td>
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
<td align="right">1,199,540</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">517,540</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">175,120</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">173,360</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">88,580</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,330,960</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">865,020</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,760</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,140</td>
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
<td align="right">69.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,060</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">180</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">80</td>
<td align="right">1.7%</td>
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
<td align="right">76.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,100</td>
<td align="right">24.0%</td>
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
<td align="right">73,220</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">7,400</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">4,280</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,600</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,360</td>
<td align="right">2.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">81,660</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">10,320</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,580</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,460</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">340</td>
<td align="right">0.4%</td>
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
<td align="right">15,379,593</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,385,880</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">213,320</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">195,473</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">48,380</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">17,396,179</td>
<td align="right">95.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">883,900</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">2,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,180</td>
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
<td align="right">1,982,393</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,261,596</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24,460</td>
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
<td align="right">14,080</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,520</td>
<td align="right">34.8%</td>
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
<td align="right">2,020</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">1,300</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">1,240</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,040</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">320</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">200</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">180</td>
<td align="right">2.4%</td>
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
<td align="left">multiply different types</td>
<td align="right">40</td>
<td align="right">0.5%</td>
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
<td align="left">and different types</td>
<td align="right">20</td>
<td align="right">0.3%</td>
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
<td align="right">907,320</td>
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
<td align="right">6,992,420</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">72,358,290</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,987,800</td>
<td align="right">8.8%</td>
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
<td align="right">224,980</td>
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
<td align="right">2,220</td>
<td align="right">55.5%</td>
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
<td align="right">120,120</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">110,960</td>
<td align="right">84.6%</td>
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
<td align="right">3,768,032</td>
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
<td align="right">29,419,526</td>
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
<td align="right">100,780</td>
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
<td align="right">12,800</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,960</td>
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
<td align="left">baseobject</td>
<td align="right">2,100</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,880</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">1,540</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">460</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">380</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">340</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">100</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">80</td>
<td align="right">1.1%</td>
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
<td align="right">3,630,500</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,449,906</td>
<td align="right">55.0%</td>
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
<td align="right">3,580</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,540</td>
<td align="right">67.8%</td>
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
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,940</td>
<td align="right">25.7%</td>
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
<td align="right">3,822,060</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,654,090</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">20,440</td>
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
<td align="right">12,980</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,860</td>
<td align="right">40.6%</td>
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
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">2,120</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,200</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">600</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">520</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">440</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">440</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">340</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">280</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">180</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">160</td>
<td align="right">1.8%</td>
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
<td align="right">598,280</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,034,833</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,920</td>
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
<td align="right">13,360</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,400</td>
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
<td align="right">4,400</td>
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
<td align="right">9,293,600</td>
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
<td align="right">116,131,749</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">19,663,070</td>
<td align="right">13.5%</td>
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
<td align="right">488,840</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">67,500</td>
<td align="right">12.1%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">9,840</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">5,240</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,740</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,860</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">920</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">520</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">400</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">380</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">340</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">340</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">180</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">160</td>
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
<tr>
<td align="left">class attr simple</td>
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
<td align="right">90,340</td>
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
<td align="right">460</td>
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
<td align="right">89,272,076</td>
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
<td align="right">44,020</td>
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
<td align="right">87,105</td>
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
<td align="right">2,080</td>
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
<td align="right">2,986,160</td>
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
<td align="right">2,860</td>
<td align="right">4.3%</td>
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
<td align="right">63,540</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,860</td>
<td align="right">4.3%</td>
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
<td align="right">77,620</td>
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
<td align="right">1,142,700</td>
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
<td align="right">1,860</td>
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
<td align="right">2,387,600</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,490,600</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,506,600</td>
<td align="right">38.6%</td>
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
<td align="right">248,960</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">9,020</td>
<td align="right">3.5%</td>
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
<td align="right">42,800</td>
<td align="right">474.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,200</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,820</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">1,120</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">820</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">520</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">400</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">380</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">320</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">100</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40</td>
<td align="right">0.4%</td>
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
<td align="right">700</td>
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
<td align="right">154,720</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,098,400</td>
<td align="right">93.0%</td>
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
<td align="right">78.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">580</td>
<td align="right">21.8%</td>
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
<td align="right">280</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">120</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">100</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">20</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">bytearray slice</td>
<td align="right">20</td>
<td align="right">3.4%</td>
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
<td align="right">556,492</td>
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
<td align="right">62,703,981</td>
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
<td align="right">4,573,460</td>
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
<td align="right">127,600</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,440</td>
<td align="right">2.6%</td>
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
<td align="right">760</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">760</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">720</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">540</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">360</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">120</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">100</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">80</td>
<td align="right">2.3%</td>
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
<td align="right">18,385,539</td>
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
<td align="right">3,780</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">500</td>
<td align="right">11.7%</td>
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
<td align="right">873,235,948</td>
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
<td align="right">29,204,722</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">606,944,607</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">44,043,310</td>
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
<td align="right">9,293,600</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,992,420</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,822,060</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,768,032</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,630,500</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,387,600</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,982,393</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,163,480</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">907,320</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">598,280</td>
<td align="right">1.7%</td>
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
<td align="right">12,506,560</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,212,260</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,090,220</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,843,680</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,813,280</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">3,427,580</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,640,540</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,219,100</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,768,240</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">947,040</td>
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
<td align="right">19,095,260</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">48,123,717</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">19,095,260</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">17,562,640</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">1,532,620</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">17,548,400</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">10,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">220,005</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">1,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">389,540</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">2,275</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">837,990</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">60,608,691</td>
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
<td align="right">37,114,956</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">37,209,156</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">48,928,242</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">48,503,157</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">340,200</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">84,885</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">42,243,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">4,728,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">369,506,220</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">434,525,059</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">283,041,797</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">276,777,280</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">35,545,741</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">13,605,678</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">258,265,423</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">212,165,576</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">265,640</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">31,200</td>
<td align="right">0.7%</td>
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
<td align="right">54,983,355</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">617,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache too big</td>
<td align="right">0</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">28,960,970</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">131,320</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache invalidations</td>
<td align="right">44,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache resizes</td>
<td align="right">78,160</td>
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
<td align="right">34,640</td>
<td align="right">94,290,240</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">360</td>
<td align="right">179,780</td>
<td align="right">79,081,940</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">20</td>
<td align="right">920</td>
<td align="right">41,872,840</td>
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
<td align="right">5,860</td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">398,200</td>
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
Stats gathered on: 2026-10-28
