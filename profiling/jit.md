
## 2to3

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.23% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.63% | `[JIT]` | `jit` | jit |
| 4.37% | `python` | `gc_collect_main` | gc |
| 2.45% | `python` | `_PyObject_Malloc` | memory |
| 2.20% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.95% | `python` | `sre_ucs1_match` | library |
| 1.90% | `python` | `_Py_dict_lookup` | lookup |
| 1.64% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.64% | `python` | `_Py_Dealloc` | memory |
| 1.60% | `python` | `visit_decref` | gc |
| 1.56% | `python` | `_PyObject_Free` | memory |
| 1.56% | `python` | `tuple_dealloc` | memory |
| 1.48% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.16% | `python` | `visit_reachable` | gc |
| 0.95% | `python` | `tuple_alloc` | memory |
| 0.86% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.84% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.83% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.75% | `python` | `initialize_locals` | interpreter |
| 0.66% | `python` | `gen_dealloc` | memory |
| 0.61% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.61% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.58% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.53% | `python` | `r_object` | import |
| 0.48% | `python` | `dict_traverse` | gc |
| 0.46% | `python` | `_Py_NewReference` | memory |
| 0.44% | `python` | `find_name_in_mro` | lookup |
| 0.44% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 0.42% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.42% | `python` | `_PyJIT_Entry` | compiler |
| 0.40% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.39% | `python` | `_PyCode_Quicken` | interpreter |
| 0.39% | `python` | `insertdict` | dict |
| 0.36% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.36% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.35% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 0.35% | `python` | `_PyEval_Vector` | interpreter |
| 0.34% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.34% | `python` | `PyDict_GetItemRef` | dict |
| 0.33% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.32% | `python` | `PyObject_GetItem` | dynamic |
| 0.32% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.32% | `python` | `list_dealloc` | memory |
| 0.31% | `python` | `siphash13` | str |
| 0.31% | `python` | `PyObject_SetAttr` | dynamic |
| 0.30% | `python` | `list_subscript` | list |
| 0.30% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.29% | `python` | `insert_to_emptydict` | dict |
| 0.28% | `python` | `_PyUnicode_FromUCS1.part.0` | str |
| 0.28% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.27% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.27% | `python` | `PyObject_GC_Del` | gc |
| 0.27% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.27% | `python` | `new_dict.constprop.0` | dict |
| 0.27% | `python` | `_PyType_GetDict` | dynamic |
| 0.27% | `python` | `_Py_dict_lookup_threadsafe_stackref` | lookup |
| 0.27% | `python` | `dict_dealloc` | memory |
| 0.26% | `python` | `_PyDict_Subscript` | dict |
| 0.26% | `python` | `type_ready` | dynamic |
| 0.25% | `libc.so.6` | `_int_malloc` | libc |

## argparse

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.19% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.23% | `[JIT]` | `jit` | jit |
| 3.52% | `python` | `_PyObject_Malloc` | memory |
| 2.06% | `python` | `_PyObject_Free` | memory |
| 1.95% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.93% | `python` | `_Py_dict_lookup` | lookup |
| 1.76% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.68% | `python` | `_Py_Dealloc` | memory |
| 1.64% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.20% | `python` | `gc_collect_main` | gc |
| 1.08% | `python` | `initialize_locals` | interpreter |
| 0.93% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.93% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.90% | `python` | `tuple_dealloc` | memory |
| 0.89% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.72% | `python` | `tuple_alloc` | memory |
| 0.64% | `[kernel.kallsyms]` | `el0_svc` | kernel |
| 0.61% | `python` | `insertdict` | dict |
| 0.59% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.57% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 0.56% | `python` | `PyList_New.constprop.0` | memory |
| 0.56% | `libc.so.6` | `__gconv_transform_utf8_internal` | libc |
| 0.51% | `python` | `PyDict_GetItemRef` | dict |
| 0.50% | `python` | `_Py_NewReference` | memory |
| 0.48% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.46% | `python` | `PyUnicode_New.part.0` | memory |
| 0.46% | `python` | `visit_decref` | gc |
| 0.46% | `python` | `_copy_characters.constprop.0.isra.0` | str |
| 0.46% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.44% | `python` | `PyObject_Malloc` | dynamic |
| 0.44% | `python` | `_PyJIT_Entry` | compiler |
| 0.44% | `libc.so.6` | `__GI___fstatat64` | libc |
| 0.43% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.42% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.41% | `python` | `PyUnicode_Format` | str |
| 0.39% | `python` | `PyType_IsSubtype` | dynamic |
| 0.38% | `python` | `PyObject_GC_Del` | gc |
| 0.38% | `python` | `new_dict.constprop.0` | dict |
| 0.37% | `python` | `_PyObject_Realloc` | memory |
| 0.37% | `python` | `list_dealloc` | memory |
| 0.36% | `python` | `_PyType_GetDict` | dynamic |
| 0.36% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.35% | `[kernel.kallsyms]` | `kmem_cache_alloc` | kernel |
| 0.33% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.33% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.32% | `python` | `PyObject_SetAttr` | dynamic |
| 0.32% | `python` | `get_exception_handler.isra.0` | unknown |
| 0.31% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.31% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.31% | `python` | `dict_dealloc` | memory |
| 0.30% | `python` | `unicode_dealloc` | memory |
| 0.30% | `python` | `PyUnicode_Contains` | str |
| 0.29% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.29% | `libc.so.6` | `__mbsrtowcs_l` | libc |
| 0.29% | `python` | `_PyObject_GC_New` | gc |
| 0.28% | `python` | `insert_to_emptydict` | dict |
| 0.28% | `python` | `PyUnicode_Append` | str |
| 0.27% | `python` | `PyObject_Free` | dynamic |
| 0.27% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.27% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 0.27% | `[kernel.kallsyms]` | `link_path_walk.part.0.constprop.0` | kernel |
| 0.26% | `libc.so.6` | `malloc` | libc |

## argparse_subparsers

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 15.01% | `[JIT]` | `jit` | jit |
| 13.96% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.65% | `python` | `_PyObject_Malloc` | memory |
| 3.57% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.59% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.56% | `python` | `_Py_dict_lookup` | lookup |
| 2.42% | `python` | `_PyObject_Free` | memory |
| 1.93% | `python` | `initialize_locals` | interpreter |
| 1.77% | `python` | `_Py_Dealloc` | memory |
| 1.62% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.44% | `python` | `gc_collect_main` | gc |
| 1.21% | `python` | `tuple_dealloc` | memory |
| 1.13% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.95% | `python` | `long_to_decimal_string_internal` | int |
| 0.91% | `python` | `insertdict` | dict |
| 0.89% | `python` | `tuple_alloc` | memory |
| 0.86% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.84% | `python` | `visit_decref` | gc |
| 0.78% | `libc.so.6` | `_int_malloc` | libc |
| 0.78% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.71% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.71% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.68% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.65% | `python` | `_PyJIT_Entry` | compiler |
| 0.61% | `python` | `list_dealloc` | memory |
| 0.61% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.60% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.58% | `python` | `_Py_NewReference` | memory |
| 0.57% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.56% | `python` | `_PyDict_Subscript` | dict |
| 0.55% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.54% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.52% | `python` | `PyMethod_New` | memory |
| 0.51% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.50% | `python` | `_Py_BuildString_StackRefSteal` | unknown |
| 0.48% | `python` | `sre_ucs1_match` | library |
| 0.48% | `python` | `PyObject_Malloc` | dynamic |
| 0.48% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.47% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 0.44% | `python` | `unicode_dealloc` | memory |
| 0.43% | `python` | `PyUnicode_Contains` | str |
| 0.40% | `python` | `PyErr_CheckSignals` | exceptions |
| 0.39% | `python` | `PyType_IsSubtype` | dynamic |
| 0.38% | `python` | `_PyEval_Vector` | interpreter |
| 0.38% | `python` | `_PyErr_CheckSignalsTstate` | exceptions |
| 0.37% | `python` | `_sre_SRE_Pattern_prefixmatch` | library |
| 0.37% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.37% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.36% | `python` | `PyObject_Hash` | dynamic |
| 0.36% | `python` | `insert_to_emptydict` | dict |
| 0.36% | `python` | `PyUnicode_New.part.0` | memory |
| 0.35% | `python` | `dict_get` | dict |
| 0.34% | `python` | `PyList_New.constprop.0` | memory |
| 0.34% | `python` | `PyDict_Contains` | dict |
| 0.34% | `python` | `siphash13` | str |
| 0.31% | `python` | `PyThread_get_thread_ident` | threading |
| 0.30% | `python` | `set_add_entry_takeref` | miscobj |
| 0.30% | `python` | `PyDict_Next` | dict |
| 0.29% | `python` | `visit_reachable` | gc |
| 0.29% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.29% | `libc.so.6` | `malloc` | libc |
| 0.28% | `python` | `dict_dealloc` | memory |
| 0.28% | `python` | `PyUnicode_New` | memory |
| 0.27% | `python` | `clone_combined_dict_keys` | unknown |
| 0.26% | `python` | `replace` | str |
| 0.26% | `python` | `PyObject_Str` | dynamic |
| 0.26% | `python` | `PyObject_Free` | dynamic |
| 0.26% | `python` | `PyDict_GetItemRef` | dict |
| 0.25% | `python` | `PyUnicode_Format` | str |

## async_generators

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 15.83% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.42% | `[JIT]` | `jit` | jit |
| 5.36% | `python` | `_Py_Dealloc` | memory |
| 3.66% | `python` | `async_gen_asend_dealloc` | memory |
| 3.08% | `python` | `_PyAsyncGenASend_Send` | unknown |
| 2.61% | `python` | `tuple_dealloc` | memory |
| 2.53% | `python` | `_PyObject_Free` | memory |
| 2.51% | `python` | `_PyObject_Malloc` | memory |
| 2.24% | `python` | `async_gen_anext` | async |
| 2.18% | `python` | `_PyJIT_Entry` | compiler |
| 1.92% | `python` | `_PyType_AllocNoTrack` | memory |
| 1.89% | `python` | `_Py_NewReference` | memory |
| 1.69% | `python` | `PyErr_ExceptionMatches` | exceptions |
| 1.68% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.61% | `python` | `gc_collect_main` | gc |
| 1.60% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 1.59% | `python` | `PyObject_CallOneArg` | dynamic |
| 1.45% | `python` | `type_call` | dynamic |
| 1.44% | `python` | `_PyAsyncGenValueWrapperNew` | memory |
| 1.44% | `python` | `async_gen_wrapped_val_dealloc` | memory |
| 1.40% | `python` | `StopIteration_dealloc` | memory |
| 1.37% | `python` | `PyObject_GC_Del` | gc |
| 1.34% | `python` | `_PyGen_FetchStopIterationValue` | miscobj |
| 1.25% | `python` | `StopIteration_init` | dynamic |
| 1.25% | `python` | `PyType_GenericAlloc` | memory |
| 1.13% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 1.10% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.07% | `python` | `PyTuple_FromArray.part.0` | tuple |
| 1.04% | `python` | `tuple_alloc` | memory |
| 0.91% | `python` | `initialize_locals` | interpreter |
| 0.89% | `python` | `BaseException_new` | memory |
| 0.70% | `python` | `_PyEval_GetANext` | interpreter |
| 0.69% | `python` | `PyErr_SetRaisedException` | exceptions |
| 0.68% | `python` | `_PyObject_GC_Link` | gc |
| 0.67% | `libc.so.6` | `__memset_zva64` | libc |
| 0.66% | `python` | `visit_reachable` | gc |
| 0.66% | `python` | `PyType_IsSubtype` | dynamic |
| 0.65% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.64% | `python` | `PyObject_Malloc` | dynamic |
| 0.63% | `python` | `_PyErr_SetObject.part.0` | exceptions |
| 0.62% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.61% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.59% | `python` | `PyObject_Free` | dynamic |
| 0.59% | `python` | `PyErr_GetRaisedException` | exceptions |
| 0.58% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.54% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.51% | `python` | `visit_decref` | gc |
| 0.47% | `python` | `_PyEval_Vector` | interpreter |
| 0.45% | `python` | `_PyLong_FromMedium` | int |
| 0.45% | `python` | `get_exception_handler.isra.0` | unknown |
| 0.44% | `python` | `range_subscript` | miscobj |
| 0.40% | `python` | `subtype_traverse` | gc |
| 0.40% | `python` | `long_dealloc` | memory |
| 0.39% | `python` | `make_range_object` | unknown |
| 0.36% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.35% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.35% | `python` | `PyArg_UnpackTuple` | calls |
| 0.34% | `python` | `gen_dealloc` | memory |
| 0.34% | `python` | `_PySlice_GetLongIndices` | miscobj |
| 0.33% | `python` | `PyNumber_Add` | dynamic |
| 0.32% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.30% | `python` | `long_add` | int |
| 0.29% | `python` | `PySlice_New` | memory |
| 0.29% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.29% | `python` | `long_richcompare` | int |
| 0.29% | `python` | `async_gen_asend_finalize` | async |
| 0.27% | `python` | `PyTuple_FromArray` | tuple |
| 0.26% | `python` | `weakref___new__` | memory |

## async_tree

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 15.51% | `[JIT]` | `jit` | jit |
| 10.87% | `python` | `gc_collect_main` | gc |
| 5.51% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.01% | `python` | `visit_reachable` | gc |
| 4.42% | `python` | `visit_decref` | gc |
| 3.16% | `python` | `_PyObject_Malloc` | memory |
| 2.22% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.96% | `python` | `initialize_locals` | interpreter |
| 1.72% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.57% | `python` | `_PyObject_Free` | memory |
| 1.56% | `python` | `_Py_Dealloc` | memory |
| 1.33% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.25% | `python` | `subtype_traverse` | gc |
| 1.25% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.10% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.03% | `python` | `_PyEval_Vector` | interpreter |
| 0.75% | `python` | `_PyMember_GetOffset` | unknown |
| 0.75% | `python` | `tuple_dealloc` | memory |
| 0.65% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.64% | `python` | `TaskObj_traverse` | gc |
| 0.61% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.58% | `python` | `_PyGC_VisitFrameStack` | gc |
| 0.54% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 0.54% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.54% | `python` | `_PyJIT_Entry` | compiler |
| 0.53% | `python` | `context_tp_dealloc` | memory |
| 0.51% | `python` | `clear_slots` | unknown |
| 0.51% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.51% | `python` | `_Py_NewReference` | memory |
| 0.48% | `python` | `tuple_alloc` | memory |
| 0.47% | `python` | `_PyObject_Calloc` | memory |
| 0.47% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.46% | `python` | `gen_dealloc` | memory |
| 0.45% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.44% | `python` | `PyCMethod_New` | memory |
| 0.43% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.43% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.42% | `python` | `_Py_dict_lookup` | lookup |
| 0.42% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.42% | `python` | `PyObject_GC_Del` | gc |
| 0.41% | `python` | `_PyLong_FromMedium` | int |
| 0.38% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.37% | `python` | `_PyObject_GC_New` | gc |
| 0.35% | `python` | `insert_to_emptydict` | dict |
| 0.35% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 0.34% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.33% | `python` | `PyUnicode_RichCompare` | str |
| 0.33% | `python` | `_PyObject_Realloc` | memory |
| 0.33% | `python` | `context_tp_traverse` | gc |
| 0.33% | `python` | `PyIter_Send` | dynamic |
| 0.32% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.32% | `python` | `TaskObj_clear` | unknown |
| 0.32% | `python` | `_asyncio_Task___init__` | unknown |
| 0.32% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.31% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.31% | `python` | `_PyObject_GC_Link` | gc |
| 0.31% | `python` | `subtype_dealloc` | memory |
| 0.31% | `python` | `gen_traverse` | gc |
| 0.30% | `python` | `future_schedule_callbacks` | unknown |
| 0.30% | `[kernel.kallsyms]` | `el0_da` | kernel |
| 0.30% | `python` | `task_step_impl` | unknown |
| 0.30% | `[kernel.kallsyms]` | `__pi_clear_page` | kernel |
| 0.30% | `python` | `_PyType_GetDict` | dynamic |
| 0.29% | `python` | `_asyncio_future_discard_from_awaited_by` | unknown |
| 0.29% | `python` | `PyContext_CopyCurrent` | unknown |
| 0.28% | `python` | `deque_append` | miscobj |
| 0.28% | `python` | `PyObject_Call` | dynamic |
| 0.28% | `python` | `PyObject_Malloc` | dynamic |
| 0.27% | `python` | `type_is_gc` | gc |

## async_tree_cpu_io_mixed

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.83% | `python` | `k_mul` | int |
| 8.62% | `[JIT]` | `jit` | jit |
| 7.19% | `python` | `gc_collect_main` | gc |
| 4.40% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.50% | `python` | `_PyObject_Malloc` | memory |
| 3.28% | `python` | `visit_reachable` | gc |
| 2.90% | `python` | `visit_decref` | gc |
| 2.58% | `python` | `_PyObject_Free` | memory |
| 2.32% | `python` | `PyErr_CheckSignals` | exceptions |
| 1.48% | `python` | `_Py_Dealloc` | memory |
| 1.43% | `python` | `_PyErr_CheckSignalsTstate` | exceptions |
| 1.39% | `python` | `_PyRunRemoteDebugger` | unknown |
| 1.29% | `python` | `PyThread_get_thread_ident` | threading |
| 1.25% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.16% | `python` | `initialize_locals` | interpreter |
| 1.07% | `_math_integer.cpython-316-aarch64-linux-gnu.so` | `factorial_partial_product` | library |
| 0.97% | `python` | `subtype_traverse` | gc |
| 0.91% | `python` | `_Py_IsMainThread` | unknown |
| 0.89% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.77% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.75% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.74% | `python` | `_PyInterpreterState_Main` | unknown |
| 0.69% | `python` | `_Py_NewReference` | memory |
| 0.67% | `python` | `_PyEval_Vector` | interpreter |
| 0.64% | `python` | `_PyInterpreterState_GetConfig` | unknown |
| 0.62% | `python` | `PyLong_FromUnsignedLong` | int |
| 0.60% | `python` | `long_dealloc` | memory |
| 0.59% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.58% | `python` | `PyObject_Free` | dynamic |
| 0.58% | `python` | `PyObject_Malloc` | dynamic |
| 0.57% | `python` | `_PyMember_GetOffset` | unknown |
| 0.53% | `python` | `PyNumber_Multiply` | dynamic |
| 0.50% | `python` | `long_alloc` | memory |
| 0.45% | `python` | `long_mul` | int |
| 0.38% | `python` | `tuple_dealloc` | memory |
| 0.38% | `libc.so.6` | `__memset_zva64` | libc |
| 0.37% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.35% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.34% | `python` | `TaskObj_traverse` | gc |
| 0.33% | `python` | `context_tp_dealloc` | memory |
| 0.33% | `python` | `_PyGC_VisitFrameStack` | gc |
| 0.32% | `python` | `_PyJIT_Entry` | compiler |
| 0.31% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.31% | `python` | `gen_dealloc` | memory |
| 0.30% | `python` | `clear_slots` | unknown |
| 0.29% | `python` | `long_lshift1` | int |
| 0.29% | `python` | `tuple_alloc` | memory |
| 0.28% | `python` | `pthread_self@plt` | unknown |
| 0.28% | `python` | `_PyLong_FromMedium` | int |
| 0.27% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 0.27% | `python` | `_Py_dict_lookup` | lookup |
| 0.26% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.26% | `python` | `_PyObject_Calloc` | memory |
| 0.25% | `python` | `unicodekeys_lookup_unicode` | lookup |

## async_tree_cpu_io_mixed_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.70% | `python` | `k_mul` | int |
| 8.43% | `[JIT]` | `jit` | jit |
| 6.55% | `python` | `gc_collect_main` | gc |
| 4.25% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.45% | `python` | `_PyObject_Malloc` | memory |
| 3.00% | `python` | `visit_reachable` | gc |
| 2.75% | `python` | `visit_decref` | gc |
| 2.64% | `python` | `_PyObject_Free` | memory |
| 2.41% | `python` | `PyErr_CheckSignals` | exceptions |
| 1.59% | `python` | `_Py_Dealloc` | memory |
| 1.52% | `python` | `_PyErr_CheckSignalsTstate` | exceptions |
| 1.49% | `python` | `_PyRunRemoteDebugger` | unknown |
| 1.28% | `python` | `PyThread_get_thread_ident` | threading |
| 1.14% | `_math_integer.cpython-316-aarch64-linux-gnu.so` | `factorial_partial_product` | library |
| 1.13% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.98% | `python` | `subtype_traverse` | gc |
| 0.97% | `python` | `initialize_locals` | interpreter |
| 0.94% | `python` | `_Py_IsMainThread` | unknown |
| 0.82% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.78% | `python` | `_PyInterpreterState_Main` | unknown |
| 0.76% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.72% | `python` | `_Py_NewReference` | memory |
| 0.67% | `python` | `_PyEval_Vector` | interpreter |
| 0.67% | `python` | `PyLong_FromUnsignedLong` | int |
| 0.65% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.63% | `python` | `_PyInterpreterState_GetConfig` | unknown |
| 0.59% | `python` | `PyObject_Malloc` | dynamic |
| 0.59% | `python` | `long_dealloc` | memory |
| 0.59% | `python` | `_PyGC_VisitFrameStack` | gc |
| 0.58% | `python` | `PyObject_Free` | dynamic |
| 0.58% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.57% | `python` | `PyNumber_Multiply` | dynamic |
| 0.54% | `python` | `_PyMember_GetOffset` | unknown |
| 0.51% | `python` | `long_alloc` | memory |
| 0.44% | `python` | `long_mul` | int |
| 0.41% | `python` | `gen_dealloc` | memory |
| 0.40% | `libc.so.6` | `__memset_zva64` | libc |
| 0.38% | `python` | `_PyJIT_Entry` | compiler |
| 0.37% | `python` | `TaskObj_traverse` | gc |
| 0.36% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.36% | `python` | `tuple_dealloc` | memory |
| 0.34% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.33% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.32% | `python` | `set_lookkey` | miscobj |
| 0.30% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.30% | `python` | `clear_slots` | unknown |
| 0.30% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.29% | `python` | `gen_traverse` | gc |
| 0.29% | `python` | `pthread_self@plt` | unknown |
| 0.29% | `python` | `long_lshift1` | int |
| 0.28% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.28% | `python` | `_PyLong_FromMedium` | int |
| 0.26% | `python` | `set_traverse` | gc |
| 0.26% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 0.26% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.26% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.25% | `python` | `tuple_alloc` | memory |

## async_tree_io

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 15.71% | `python` | `gc_collect_main` | gc |
| 12.00% | `[JIT]` | `jit` | jit |
| 7.83% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.45% | `python` | `visit_reachable` | gc |
| 5.87% | `python` | `visit_decref` | gc |
| 2.13% | `python` | `_PyObject_Malloc` | memory |
| 2.00% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.85% | `python` | `initialize_locals` | interpreter |
| 1.59% | `python` | `subtype_traverse` | gc |
| 1.44% | `python` | `_PyEval_Vector` | interpreter |
| 1.26% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.22% | `python` | `_PyGC_VisitFrameStack` | gc |
| 1.22% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.19% | `python` | `_PyObject_Free` | memory |
| 1.18% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.14% | `python` | `_Py_Dealloc` | memory |
| 0.94% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.93% | `python` | `_PyMember_GetOffset` | unknown |
| 0.85% | `python` | `_PyJIT_Entry` | compiler |
| 0.72% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.69% | `_heapq.cpython-316-aarch64-linux-gnu.so` | `siftup` | library |
| 0.62% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.60% | `python` | `gen_traverse` | gc |
| 0.58% | `python` | `tuple_dealloc` | memory |
| 0.56% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.50% | `python` | `slot_tp_richcompare` | dynamic |
| 0.45% | `python` | `clear_slots` | unknown |
| 0.45% | `python` | `gen_dealloc` | memory |
| 0.44% | `python` | `TaskObj_traverse` | gc |
| 0.44% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.43% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 0.43% | `python` | `_PyObject_Calloc` | memory |
| 0.41% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.39% | `python` | `_PyGC_VisitStackRef` | gc |
| 0.38% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.37% | `python` | `_Py_NewReference` | memory |
| 0.37% | `python` | `tuple_alloc` | memory |
| 0.37% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.36% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.35% | `python` | `tuple_traverse` | gc |
| 0.34% | `python` | `_PyObject_Realloc` | memory |
| 0.34% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.32% | `python` | `PyCMethod_New` | memory |
| 0.30% | `python` | `insert_to_emptydict` | dict |
| 0.29% | `python` | `PyObject_GC_Del` | gc |
| 0.29% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.29% | `python` | `context_tp_traverse` | gc |
| 0.28% | `python` | `_Py_dict_lookup` | lookup |
| 0.28% | `python` | `context_tp_dealloc` | memory |
| 0.27% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.27% | `[kernel.kallsyms]` | `el0_da` | kernel |
| 0.27% | `[kernel.kallsyms]` | `__pi_clear_page` | kernel |
| 0.26% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.26% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.26% | `python` | `type_is_gc` | gc |

## async_tree_io_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 14.45% | `python` | `gc_collect_main` | gc |
| 12.07% | `[JIT]` | `jit` | jit |
| 7.94% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.39% | `python` | `visit_reachable` | gc |
| 5.80% | `python` | `visit_decref` | gc |
| 2.12% | `python` | `_PyObject_Malloc` | memory |
| 1.92% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.75% | `python` | `initialize_locals` | interpreter |
| 1.67% | `python` | `subtype_traverse` | gc |
| 1.56% | `python` | `_PyGC_VisitFrameStack` | gc |
| 1.49% | `python` | `_PyEval_Vector` | interpreter |
| 1.27% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.20% | `python` | `_Py_Dealloc` | memory |
| 1.18% | `python` | `_PyObject_Free` | memory |
| 1.18% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.15% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.97% | `python` | `_PyMember_GetOffset` | unknown |
| 0.89% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.84% | `python` | `_PyJIT_Entry` | compiler |
| 0.74% | `_heapq.cpython-316-aarch64-linux-gnu.so` | `siftup` | library |
| 0.72% | `python` | `gen_traverse` | gc |
| 0.71% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.70% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.59% | `python` | `tuple_dealloc` | memory |
| 0.57% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.53% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 0.53% | `python` | `slot_tp_richcompare` | dynamic |
| 0.51% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.50% | `python` | `gen_dealloc` | memory |
| 0.49% | `python` | `TaskObj_traverse` | gc |
| 0.47% | `python` | `clear_slots` | unknown |
| 0.47% | `python` | `_PyGC_VisitStackRef` | gc |
| 0.45% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.42% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.42% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.40% | `python` | `_Py_NewReference` | memory |
| 0.38% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.36% | `python` | `set_traverse` | gc |
| 0.36% | `python` | `_PyObject_Calloc` | memory |
| 0.36% | `python` | `tuple_alloc` | memory |
| 0.35% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.35% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.33% | `[kernel.kallsyms]` | `__pi_clear_page` | kernel |
| 0.32% | `[kernel.kallsyms]` | `el0_da` | kernel |
| 0.31% | `python` | `PyObject_GC_Del` | gc |
| 0.31% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.29% | `python` | `PyObject_Call` | dynamic |
| 0.29% | `python` | `_PyObject_Realloc` | memory |
| 0.28% | `python` | `PyCMethod_New` | memory |
| 0.27% | `python` | `type_is_gc` | gc |
| 0.26% | `python` | `context_tp_traverse` | gc |
| 0.26% | `python` | `_PyLong_FromMedium` | int |
| 0.26% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.26% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.25% | `python` | `PyList_New` | memory |
| 0.25% | `python` | `set_lookkey` | miscobj |
| 0.25% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.25% | `python` | `insert_to_emptydict` | dict |

## async_tree_memoization

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 14.92% | `[JIT]` | `jit` | jit |
| 11.65% | `python` | `gc_collect_main` | gc |
| 7.22% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.40% | `python` | `visit_reachable` | gc |
| 4.79% | `python` | `visit_decref` | gc |
| 3.05% | `python` | `_PyObject_Malloc` | memory |
| 2.13% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.94% | `python` | `initialize_locals` | interpreter |
| 1.62% | `python` | `subtype_traverse` | gc |
| 1.52% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.44% | `python` | `_PyObject_Free` | memory |
| 1.41% | `python` | `_Py_Dealloc` | memory |
| 1.30% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.26% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.12% | `python` | `_PyEval_Vector` | interpreter |
| 1.02% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.99% | `python` | `_PyMember_GetOffset` | unknown |
| 0.67% | `python` | `tuple_dealloc` | memory |
| 0.62% | `python` | `_PyJIT_Entry` | compiler |
| 0.61% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.61% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.59% | `python` | `_PyGC_VisitFrameStack` | gc |
| 0.54% | `python` | `TaskObj_traverse` | gc |
| 0.53% | `python` | `context_tp_dealloc` | memory |
| 0.49% | `python` | `_Py_dict_lookup` | lookup |
| 0.49% | `python` | `clear_slots` | unknown |
| 0.45% | `python` | `gen_dealloc` | memory |
| 0.45% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.45% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.45% | `python` | `_Py_NewReference` | memory |
| 0.44% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 0.44% | `python` | `tuple_alloc` | memory |
| 0.44% | `python` | `_PyObject_Calloc` | memory |
| 0.43% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.42% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.39% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.38% | `python` | `PyCMethod_New` | memory |
| 0.38% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.37% | `python` | `_PyLong_FromMedium` | int |
| 0.37% | `python` | `PyObject_GC_Del` | gc |
| 0.36% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.36% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.35% | `python` | `TaskObj_clear` | unknown |
| 0.33% | `python` | `gen_traverse` | gc |
| 0.32% | `python` | `_PyObject_GC_New` | gc |
| 0.32% | `python` | `_asyncio_future_discard_from_awaited_by` | unknown |
| 0.32% | `python` | `PyIter_Send` | dynamic |
| 0.32% | `python` | `_PyObject_Realloc` | memory |
| 0.31% | `python` | `tuple_traverse` | gc |
| 0.31% | `python` | `insert_to_emptydict` | dict |
| 0.31% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.31% | `python` | `context_tp_traverse` | gc |
| 0.30% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.29% | `python` | `PyUnicode_RichCompare` | str |
| 0.29% | `python` | `future_schedule_callbacks` | unknown |
| 0.29% | `python` | `task_step_impl` | unknown |
| 0.28% | `python` | `type_is_gc` | gc |
| 0.28% | `python` | `_Py_VectorCallInstrumentation_StackRefSteal` | unknown |
| 0.28% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.28% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.28% | `python` | `_PyType_GetDict` | dynamic |
| 0.28% | `python` | `_PyObject_GC_Link` | gc |
| 0.27% | `python` | `_asyncio_Task___init__` | unknown |
| 0.26% | `python` | `PyObject_Call` | dynamic |
| 0.26% | `python` | `deque_append` | miscobj |
| 0.26% | `python` | `subtype_dealloc` | memory |
| 0.26% | `python` | `context_run` | unknown |
| 0.26% | `python` | `PyType_GenericAlloc` | memory |
| 0.25% | `python` | `PyObject_Malloc` | dynamic |

## async_tree_memoization_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 14.53% | `[JIT]` | `jit` | jit |
| 11.94% | `python` | `gc_collect_main` | gc |
| 7.08% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.49% | `python` | `visit_reachable` | gc |
| 4.89% | `python` | `visit_decref` | gc |
| 2.77% | `python` | `_PyObject_Malloc` | memory |
| 1.91% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.75% | `python` | `subtype_traverse` | gc |
| 1.64% | `python` | `initialize_locals` | interpreter |
| 1.54% | `python` | `_Py_Dealloc` | memory |
| 1.38% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.33% | `python` | `_PyObject_Free` | memory |
| 1.23% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.17% | `python` | `_PyEval_Vector` | interpreter |
| 1.14% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.06% | `python` | `_PyGC_VisitFrameStack` | gc |
| 1.01% | `python` | `_PyMember_GetOffset` | unknown |
| 1.01% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.75% | `python` | `_PyJIT_Entry` | compiler |
| 0.64% | `python` | `TaskObj_traverse` | gc |
| 0.63% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.61% | `python` | `tuple_dealloc` | memory |
| 0.58% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.58% | `python` | `gen_dealloc` | memory |
| 0.55% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.53% | `python` | `set_lookkey` | miscobj |
| 0.52% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.52% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.51% | `python` | `gen_traverse` | gc |
| 0.50% | `python` | `clear_slots` | unknown |
| 0.49% | `python` | `_Py_NewReference` | memory |
| 0.45% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.45% | `python` | `set_traverse` | gc |
| 0.45% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.42% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 0.40% | `python` | `tuple_alloc` | memory |
| 0.39% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.38% | `python` | `PyObject_GC_Del` | gc |
| 0.37% | `python` | `PyObject_Call` | dynamic |
| 0.37% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.36% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.36% | `python` | `_PyLong_FromMedium` | int |
| 0.34% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.33% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.33% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.33% | `python` | `_PyObject_Calloc` | memory |
| 0.32% | `[kernel.kallsyms]` | `__pi_clear_page` | kernel |
| 0.32% | `python` | `_PyGC_VisitStackRef` | gc |
| 0.31% | `python` | `dict_dealloc` | memory |
| 0.31% | `python` | `PyCMethod_New` | memory |
| 0.30% | `python` | `context_tp_traverse` | gc |
| 0.30% | `[kernel.kallsyms]` | `el0_da` | kernel |
| 0.29% | `python` | `_PyObject_GC_New` | gc |
| 0.29% | `python` | `type_is_gc` | gc |
| 0.29% | `python` | `PyUnicode_RichCompare` | str |
| 0.29% | `python` | `PyIter_Send` | dynamic |
| 0.29% | `python` | `_PyObject_GC_Link` | gc |
| 0.29% | `python` | `_PyType_GetDict` | dynamic |
| 0.29% | `python` | `_Py_dict_lookup` | lookup |
| 0.28% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.28% | `python` | `context_tp_dealloc` | memory |
| 0.28% | `python` | `_asyncio_Task___init__` | unknown |
| 0.27% | `python` | `TaskStepMethWrapper_call` | unknown |
| 0.27% | `python` | `task_step_impl` | unknown |
| 0.27% | `python` | `TaskObj_clear` | unknown |
| 0.26% | `python` | `deque_append` | miscobj |
| 0.26% | `python` | `PyContext_CopyCurrent` | unknown |
| 0.26% | `python` | `PyMethod_New` | memory |

## async_tree_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 15.32% | `[JIT]` | `jit` | jit |
| 10.70% | `python` | `gc_collect_main` | gc |
| 5.17% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.12% | `python` | `visit_reachable` | gc |
| 4.47% | `python` | `visit_decref` | gc |
| 3.16% | `python` | `_PyObject_Malloc` | memory |
| 1.98% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.81% | `python` | `_Py_Dealloc` | memory |
| 1.70% | `python` | `initialize_locals` | interpreter |
| 1.52% | `python` | `_PyObject_Free` | memory |
| 1.41% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.37% | `python` | `subtype_traverse` | gc |
| 1.26% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.18% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.15% | `python` | `_PyEval_Vector` | interpreter |
| 1.10% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.05% | `python` | `_PyGC_VisitFrameStack` | gc |
| 0.81% | `python` | `_PyMember_GetOffset` | unknown |
| 0.74% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.69% | `python` | `TaskObj_traverse` | gc |
| 0.66% | `python` | `tuple_dealloc` | memory |
| 0.64% | `python` | `gen_dealloc` | memory |
| 0.61% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.59% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.59% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 0.59% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.56% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.56% | `python` | `clear_slots` | unknown |
| 0.55% | `python` | `_Py_NewReference` | memory |
| 0.53% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.52% | `python` | `set_traverse` | gc |
| 0.51% | `python` | `set_lookkey` | miscobj |
| 0.51% | `python` | `_PyJIT_Entry` | compiler |
| 0.49% | `python` | `gen_traverse` | gc |
| 0.47% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.47% | `python` | `tuple_alloc` | memory |
| 0.46% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.45% | `python` | `PyObject_GC_Del` | gc |
| 0.44% | `[kernel.kallsyms]` | `__pi_clear_page` | kernel |
| 0.44% | `[kernel.kallsyms]` | `el0_da` | kernel |
| 0.42% | `python` | `_PyLong_FromMedium` | int |
| 0.42% | `python` | `PyObject_Call` | dynamic |
| 0.42% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.39% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.38% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.37% | `python` | `_PyObject_Calloc` | memory |
| 0.37% | `python` | `dict_dealloc` | memory |
| 0.37% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.36% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.35% | `python` | `_asyncio_Task___init__` | unknown |
| 0.34% | `python` | `PyUnicode_RichCompare` | str |
| 0.34% | `python` | `PyCMethod_New` | memory |
| 0.34% | `python` | `_PyObject_GC_New` | gc |
| 0.32% | `python` | `_PyGC_VisitStackRef` | gc |
| 0.32% | `python` | `context_tp_traverse` | gc |
| 0.32% | `python` | `PyContext_CopyCurrent` | unknown |
| 0.32% | `python` | `TaskStepMethWrapper_call` | unknown |
| 0.31% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.31% | `python` | `_PyObject_GC_Link` | gc |
| 0.30% | `python` | `_PyType_GetDict` | dynamic |
| 0.30% | `python` | `task_step_impl` | unknown |
| 0.30% | `python` | `deque_append` | miscobj |
| 0.29% | `python` | `PyMethod_New` | memory |
| 0.28% | `python` | `PyObject_Malloc` | dynamic |
| 0.28% | `python` | `PyIter_Send` | dynamic |
| 0.28% | `python` | `type_is_gc` | gc |
| 0.28% | `python` | `PyList_New` | memory |
| 0.27% | `python` | `subtype_dealloc` | memory |
| 0.27% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.26% | `python` | `PyDict_New` | memory |
| 0.26% | `python` | `context_tp_dealloc` | memory |
| 0.26% | `python` | `_PyObject_VectorcallPrepend` | dynamic |
| 0.25% | `python` | `future_schedule_callbacks` | unknown |
| 0.25% | `python` | `TaskObj_clear` | unknown |

## asyncio_websockets

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 13.53% | `libz.so.1.3` | `0x00000000000080c4` | library |
| 6.30% | `libz.so.1.3` | `0x0000000000002a84` | library |
| 4.99% | `libz.so.1.3` | `0x0000000000002a8c` | library |
| 4.96% | `libz.so.1.3` | `0x0000000000002a6c` | library |
| 3.31% | `libz.so.1.3` | `0x0000000000002a88` | library |
| 2.99% | `libz.so.1.3` | `0x00000000000080cc` | library |
| 2.94% | `libz.so.1.3` | `0x00000000000080c0` | library |
| 2.11% | `libz.so.1.3` | `0x0000000000002a64` | library |
| 2.10% | `libz.so.1.3` | `0x00000000000080a4` | library |
| 1.98% | `libz.so.1.3` | `0x0000000000008070` | library |
| 1.87% | `libz.so.1.3` | `0x00000000000080c8` | library |
| 1.84% | `libz.so.1.3` | `0x00000000000080b4` | library |
| 1.82% | `libz.so.1.3` | `0x0000000000008094` | library |
| 1.80% | `libz.so.1.3` | `0x0000000000008080` | library |
| 1.80% | `libz.so.1.3` | `0x0000000000002a7c` | library |
| 1.61% | `libz.so.1.3` | `0x0000000000002a80` | library |
| 1.60% | `libz.so.1.3` | `0x0000000000002a68` | library |
| 1.56% | `libz.so.1.3` | `0x0000000000002a78` | library |
| 1.53% | `libz.so.1.3` | `0x00000000000080bc` | library |
| 1.37% | `libz.so.1.3` | `0x0000000000002a60` | library |
| 1.26% | `libz.so.1.3` | `0x0000000000008078` | library |
| 1.18% | `libz.so.1.3` | `0x00000000000076e4` | library |
| 1.18% | `libz.so.1.3` | `0x000000000000809c` | library |
| 1.16% | `libz.so.1.3` | `0x000000000000784c` | library |
| 1.15% | `libz.so.1.3` | `0x00000000000080d0` | library |
| 1.15% | `libz.so.1.3` | `0x0000000000008098` | library |
| 1.14% | `libz.so.1.3` | `0x00000000000080a8` | library |
| 1.13% | `libz.so.1.3` | `0x000000000000808c` | library |
| 1.13% | `libz.so.1.3` | `0x00000000000080b8` | library |
| 1.12% | `libz.so.1.3` | `0x0000000000008074` | library |
| 1.12% | `libz.so.1.3` | `0x0000000000008088` | library |
| 1.06% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.92% | `libz.so.1.3` | `0x00000000000080ac` | library |
| 0.85% | `libz.so.1.3` | `0x00000000000080b0` | library |
| 0.82% | `libz.so.1.3` | `0x00000000000076d8` | library |
| 0.81% | `libz.so.1.3` | `0x0000000000007840` | library |
| 0.63% | `libz.so.1.3` | `0x0000000000008090` | library |
| 0.62% | `libz.so.1.3` | `0x00000000000080d4` | library |
| 0.61% | `libz.so.1.3` | `0x000000000000807c` | library |
| 0.61% | `libz.so.1.3` | `0x00000000000080a0` | library |
| 0.60% | `libz.so.1.3` | `0x00000000000076e8` | library |
| 0.60% | `libz.so.1.3` | `0x00000000000076bc` | library |
| 0.59% | `libz.so.1.3` | `0x0000000000007850` | library |
| 0.59% | `libz.so.1.3` | `0x00000000000076c8` | library |
| 0.58% | `libz.so.1.3` | `0x0000000000007830` | library |
| 0.58% | `libz.so.1.3` | `0x00000000000076dc` | library |
| 0.58% | `libz.so.1.3` | `0x0000000000007824` | library |
| 0.57% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 0.56% | `libz.so.1.3` | `0x0000000000007844` | library |
| 0.49% | `libz.so.1.3` | `0x0000000000002348` | library |
| 0.44% | `libz.so.1.3` | `0x0000000000007f38` | library |
| 0.34% | `libz.so.1.3` | `0x00000000000076e0` | library |
| 0.34% | `[kernel.kallsyms]` | `el0_da` | kernel |
| 0.33% | `libz.so.1.3` | `0x0000000000007848` | library |
| 0.31% | `libz.so.1.3` | `0x0000000000002318` | library |
| 0.30% | `libz.so.1.3` | `0x0000000000002338` | library |
| 0.29% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.29% | `libz.so.1.3` | `0x0000000000002328` | library |
| 0.28% | `libz.so.1.3` | `0x0000000000002308` | library |
| 0.26% | `[kernel.kallsyms]` | `__pi_clear_page` | kernel |
| 0.26% | `libz.so.1.3` | `0x0000000000007f7c` | library |
| 0.25% | `libz.so.1.3` | `0x00000000000022d8` | library |

## base64

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 10.50% | `binascii.cpython-316-aarch64-linux-gnu.so` | `binascii_a2b_base85` | library |
| 9.50% | `binascii.cpython-316-aarch64-linux-gnu.so` | `binascii_a2b_ascii85` | library |
| 6.98% | `binascii.cpython-316-aarch64-linux-gnu.so` | `binascii_a2b_base64` | library |
| 6.68% | `binascii.cpython-316-aarch64-linux-gnu.so` | `binascii_a2b_base32` | library |
| 6.36% | `[JIT]` | `jit` | jit |
| 5.52% | `binascii.cpython-316-aarch64-linux-gnu.so` | `binascii_b2a_base64` | library |
| 5.20% | `binascii.cpython-316-aarch64-linux-gnu.so` | `binascii_b2a_base32` | library |
| 4.78% | `binascii.cpython-316-aarch64-linux-gnu.so` | `binascii_a2b_hex_impl.isra.0` | library |
| 3.86% | `binascii.cpython-316-aarch64-linux-gnu.so` | `binascii_b2a_base85` | library |
| 3.39% | `python` | `_PyArg_UnpackKeywords` | calls |
| 2.76% | `python` | `_Py_bytes_upper` | unknown |
| 2.57% | `binascii.cpython-316-aarch64-linux-gnu.so` | `binascii_b2a_ascii85` | library |
| 1.99% | `python` | `initialize_locals` | interpreter |
| 1.80% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.65% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 1.60% | `python` | `_Py_dict_lookup` | lookup |
| 1.58% | `python` | `PyDict_GetItemRef` | dict |
| 1.28% | `python` | `_PyObject_Free` | memory |
| 1.21% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.20% | `python` | `_PyObject_Malloc` | memory |
| 1.20% | `libc.so.6` | `__memchr_generic` | libc |
| 1.10% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.02% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.87% | `python` | `PyBytesWriter_Create` | unknown |
| 0.76% | `python` | `bytes_translate_impl` | str |
| 0.69% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.69% | `python` | `PyBuffer_FillInfo` | miscobj |
| 0.68% | `python` | `PyObject_GetBuffer` | dynamic |
| 0.60% | `python` | `PyBytesWriter_FinishWithPointer` | unknown |
| 0.55% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.53% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.51% | `python` | `PyBuffer_Release` | miscobj |
| 0.42% | `python` | `_Py_strhex_impl` | unknown |
| 0.42% | `python` | `cfunction_vectorcall_FASTCALL_KEYWORDS` | calls |
| 0.33% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.33% | `python` | `PyObject_Free` | dynamic |
| 0.33% | `python` | `PyObject_IsInstance` | dynamic |
| 0.33% | `python` | `_PyType_GetDict` | dynamic |
| 0.32% | `python` | `_Py_Dealloc` | memory |
| 0.32% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.32% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.31% | `python` | `PyObject_Malloc` | dynamic |
| 0.31% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.30% | `python` | `PyObject_IsTrue` | dynamic |
| 0.30% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.28% | `python` | `_PyUnicode_Equal` | str |
| 0.27% | `python` | `object_dealloc` | memory |
| 0.25% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.25% | `python` | `_PyLong_Size_t_Converter` | int |
| 0.25% | `python` | `bytes_buffer_getbuffer` | str |

## bpe_tokeniser

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 17.57% | `[JIT]` | `jit` | jit |
| 5.06% | `python` | `tuple_dealloc` | memory |
| 4.59% | `python` | `_Py_Dealloc` | memory |
| 3.44% | `python` | `_Py_dict_lookup` | lookup |
| 3.32% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.74% | `python` | `tuple_alloc` | memory |
| 2.51% | `python` | `_PyObject_Free` | memory |
| 2.50% | `python` | `PyObject_GC_UnTrack` | gc |
| 2.27% | `python` | `list_dealloc` | memory |
| 2.19% | `python` | `_PyObject_Malloc` | memory |
| 1.96% | `python` | `gc_collect_main` | gc |
| 1.88% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.77% | `python` | `PyTuple_FromArray.part.0` | tuple |
| 1.62% | `python` | `PyList_New.constprop.0` | memory |
| 1.52% | `python` | `_Py_NewReference` | memory |
| 1.47% | `python` | `list_traverse` | gc |
| 1.44% | `python` | `listiter_next` | list |
| 1.44% | `python` | `visit_reachable` | gc |
| 1.43% | `python` | `zip_next` | unknown |
| 1.15% | `python` | `tuple_richcompare` | tuple |
| 1.13% | `python` | `PyTuple_New` | memory |
| 1.08% | `python` | `visit_decref` | gc |
| 1.03% | `python` | `list_slice_lock_held` | list |
| 1.02% | `python` | `_PyCompactLong_Add` | unknown |
| 1.02% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 1.02% | `python` | `_PyCompactLong_Subtract` | unknown |
| 0.97% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.96% | `python` | `_PyJIT_Entry` | compiler |
| 0.93% | `python` | `tuple_hash` | tuple |
| 0.90% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.89% | `python` | `list_iter` | list |
| 0.89% | `python` | `insertdict` | dict |
| 0.82% | `python` | `_PyDict_Subscript` | dict |
| 0.76% | `python` | `listiter_dealloc` | memory |
| 0.75% | `python` | `PyArg_UnpackTuple` | calls |
| 0.72% | `python` | `_PyEval_SliceIndex` | interpreter |
| 0.72% | `python` | `_PyList_BinarySlice` | list |
| 0.68% | `python` | `zip_new` | memory |
| 0.68% | `python` | `wrap_objobjargproc` | unknown |
| 0.65% | `python` | `PyObject_Hash` | dynamic |
| 0.63% | `python` | `slot_mp_ass_subscript` | unknown |
| 0.61% | `python` | `PyLong_FromSsize_t` | int |
| 0.60% | `python` | `_PyList_SliceSubscript` | list |
| 0.54% | `python` | `PyObject_GC_Del` | gc |
| 0.53% | `python` | `_PyDict_StoreSubscript` | dict |
| 0.52% | `python` | `initialize_locals` | interpreter |
| 0.51% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.50% | `python` | `_PyEval_Vector` | interpreter |
| 0.46% | `python` | `wrapperdescr_call` | unknown |
| 0.45% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.45% | `python` | `PyObject_GetIter` | dynamic |
| 0.44% | `python` | `PyObject_GetItem` | dynamic |
| 0.43% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.42% | `libc.so.6` | `__memset_zva64` | libc |
| 0.42% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.42% | `python` | `_PyList_AppendTakeRefListResize` | list |
| 0.41% | `python` | `PyObject_Size` | dynamic |
| 0.41% | `python` | `type_call` | dynamic |
| 0.40% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.39% | `python` | `PyMem_Free` | memory |
| 0.37% | `python` | `PyObject_RichCompare` | dynamic |
| 0.37% | `python` | `bytes_hash` | str |
| 0.37% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.35% | `python` | `PySlice_Unpack` | miscobj |
| 0.34% | `python` | `_PyObject_GC_Link` | gc |
| 0.33% | `python` | `PyType_GenericAlloc` | memory |
| 0.33% | `python` | `_PyObject_GC_New` | gc |
| 0.32% | `python` | `bytes_richcompare` | str |
| 0.32% | `python` | `zip_dealloc` | memory |
| 0.30% | `python` | `PyMethod_New` | memory |
| 0.30% | `python` | `_PyObject_RealIsSubclass` | dynamic |
| 0.28% | `python` | `list_slice_wrap` | list |
| 0.28% | `python` | `PyObject_SetItem` | dynamic |
| 0.28% | `python` | `lookup_method_ex.constprop.0` | unknown |
| 0.26% | `python` | `_PyObject_Realloc` | memory |
| 0.25% | `python` | `_PyForIter_VirtualIteratorNext` | unknown |

## chameleon

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 19.28% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.97% | `[JIT]` | `jit` | jit |
| 6.89% | `python` | `_PyObject_Malloc` | memory |
| 3.78% | `python` | `unicode_from_format` | str |
| 2.37% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.17% | `python` | `_PyObject_Free` | memory |
| 2.09% | `python` | `_PyObject_Realloc` | memory |
| 1.83% | `python` | `_Py_dict_lookup` | lookup |
| 1.79% | `python` | `_Py_VectorCallInstrumentation_StackRefSteal` | unknown |
| 1.59% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.51% | `libc.so.6` | `__memcpy_generic` | libc |
| 1.32% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 1.30% | `python` | `PyDict_GetItemRef` | dict |
| 1.22% | `libc.so.6` | `strchr` | libc |
| 1.19% | `python` | `PyUnicode_Format` | str |
| 1.18% | `python` | `long_to_decimal_string_internal` | int |
| 1.17% | `python` | `PyErr_Format` | exceptions |
| 1.16% | `python` | `_PyUnicode_ResizeCompact` | str |
| 1.00% | `python` | `list_append` | list |
| 1.00% | `python` | `PyUnicode_New` | memory |
| 0.99% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.95% | `python` | `_copy_characters.constprop.0.isra.0` | str |
| 0.94% | `python` | `_Py_Dealloc` | memory |
| 0.90% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.84% | `python` | `PyUnicode_FromFormat` | str |
| 0.79% | `python` | `PyObject_Malloc` | dynamic |
| 0.78% | `python` | `_PyJIT_Entry` | compiler |
| 0.76% | `python` | `sre_search` | library |
| 0.76% | `python` | `_PyUnicodeWriter_WriteStr` | str |
| 0.73% | `python` | `vgetargskeywords_impl.constprop.0` | unknown |
| 0.71% | `python` | `tuple_alloc` | memory |
| 0.64% | `python` | `PyType_IsSubtype` | dynamic |
| 0.64% | `python` | `dict_get` | dict |
| 0.63% | `python` | `unicode_fromformat_write_str` | str |
| 0.61% | `python` | `_PyUnicodeWriter_WriteASCIIString` | str |
| 0.61% | `python` | `insertdict` | dict |
| 0.59% | `python` | `method_vectorcall_FASTCALL` | calls |
| 0.58% | `python` | `unicode_dealloc` | memory |
| 0.56% | `python` | `PyArg_ParseTupleAndKeywords` | calls |
| 0.56% | `python` | `PyErr_ExceptionMatches` | exceptions |
| 0.56% | `python` | `PyMember_GetOne` | lookup |
| 0.55% | `python` | `_PySuper_LookupDescr` | unknown |
| 0.53% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.53% | `python` | `_Py_NewReference` | memory |
| 0.51% | `python` | `AttributeError_init` | exceptions |
| 0.50% | `python` | `_PyErr_CheckSignalsTstate` | exceptions |
| 0.50% | `python` | `_sre_SRE_Pattern_search` | library |
| 0.48% | `python` | `_PyErr_SetObject.part.0` | exceptions |
| 0.45% | `libc.so.6` | `__strlen_asimd` | libc |
| 0.44% | `python` | `_PyUnicodeWriter_Finish` | str |
| 0.42% | `python` | `PyObject_Free` | dynamic |
| 0.40% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.39% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.39% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.39% | `python` | `PyType_GetFullyQualifiedName` | unknown |
| 0.38% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.38% | `python` | `unicode_fromformat_write_utf8` | str |
| 0.37% | `python` | `builtin_getattr` | lookup |
| 0.37% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.37% | `python` | `tuple_dealloc` | memory |
| 0.36% | `python` | `PyErr_CheckSignals` | exceptions |
| 0.33% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 0.33% | `python` | `PyThread_get_thread_ident` | threading |
| 0.32% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.31% | `python` | `memcpy@plt` | memory |
| 0.28% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.28% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.27% | `python` | `_PyUnicode_DecodeUTF8Writer` | str |
| 0.26% | `python` | `PyObject_Str` | dynamic |
| 0.25% | `python` | `list_dealloc` | memory |
| 0.25% | `python` | `_PyErr_Restore` | exceptions |

## chaos

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 33.60% | `[JIT]` | `jit` | jit |
| 7.56% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.55% | `python` | `PyFloat_FromDouble` | float |
| 3.32% | `python` | `_PyCompactLong_Subtract` | unknown |
| 2.49% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.44% | `python` | `_PyCompactLong_Add` | unknown |
| 2.39% | `python` | `_Py_Dealloc` | memory |
| 1.95% | `python` | `float_dealloc` | memory |
| 1.77% | `python` | `_Py_NewReference` | memory |
| 1.57% | `python` | `initialize_locals` | interpreter |
| 1.55% | `python` | `float_compactlong_true_div` | float |
| 1.42% | `libm.so.6` | `pow@@GLIBC_2.29` | library |
| 1.42% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.35% | `python` | `make_range_object` | unknown |
| 1.31% | `python` | `_PyFloat_ExactDealloc` | memory |
| 1.25% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.22% | `python` | `float_richcompare` | float |
| 1.19% | `python` | `PyLong_FromLong` | int |
| 1.05% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 1.02% | `python` | `float_pow` | float |
| 0.96% | `python` | `_PyObject_Malloc` | memory |
| 0.95% | `python` | `PyType_IsSubtype` | dynamic |
| 0.86% | `python` | `_PyObject_Free` | memory |
| 0.86% | `python` | `_Py_CallBuiltinClass_StackRef` | unknown |
| 0.84% | `python` | `PyLong_AsLong` | int |
| 0.84% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.78% | `python` | `range_iter` | miscobj |
| 0.77% | `python` | `_PyJIT_Entry` | compiler |
| 0.73% | `python` | `range_dealloc` | memory |
| 0.73% | `python` | `subtype_dealloc` | memory |
| 0.71% | `python` | `tuple_dealloc` | memory |
| 0.71% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.64% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.61% | `python` | `PyType_GenericAlloc` | memory |
| 0.59% | `python` | `PyLong_AsDouble` | int |
| 0.57% | `python` | `float_compactlong_subtract` | float |
| 0.55% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.54% | `math.cpython-316-aarch64-linux-gnu.so` | `math_sqrt` | library |
| 0.53% | `python` | `PyNumber_Index` | dynamic |
| 0.52% | `python` | `PyObject_RichCompare` | dynamic |
| 0.50% | `python` | `PyObject_GC_Del` | gc |
| 0.48% | `python` | `tuple_alloc` | memory |
| 0.44% | `python` | `nonzero_float_compactlong_guard` | unknown |
| 0.43% | `python` | `compactlong_float_subtract` | unknown |
| 0.36% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.36% | `python` | `range_vectorcall` | miscobj |
| 0.35% | `python` | `_PyEval_Vector` | interpreter |
| 0.34% | `python` | `rangeiter_dealloc` | memory |
| 0.32% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.32% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.30% | `python` | `_Py_VectorCallInstrumentation_StackRefSteal` | unknown |
| 0.30% | `python` | `float_compactlong_guard` | float |
| 0.27% | `python` | `PyObject_IsTrue` | dynamic |
| 0.27% | `python` | `_PyObject_InitInlineValues` | dynamic |
| 0.26% | `libc.so.6` | `__memset_zva64` | libc |

## comprehensions

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.08% | `[JIT]` | `jit` | jit |
| 5.82% | `python` | `_Py_dict_lookup` | lookup |
| 4.42% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 3.69% | `python` | `_PyObject_Malloc` | memory |
| 3.59% | `python` | `dict_get` | dict |
| 2.23% | `python` | `_PyObject_Free` | memory |
| 2.14% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.74% | `python` | `PyObject_Hash` | dynamic |
| 1.63% | `python` | `insertdict` | dict |
| 1.53% | `python` | `long_hash` | int |
| 1.50% | `python` | `_PyDict_Subscript` | dict |
| 1.42% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.42% | `python` | `_PyObject_Realloc` | memory |
| 1.40% | `python` | `_PyDict_LoadBuiltinsFromGlobals` | dict |
| 1.40% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.37% | `python` | `PyObject_GetItem` | dynamic |
| 1.36% | `python` | `_Py_Dealloc` | memory |
| 1.28% | `python` | `long_richcompare` | int |
| 1.13% | `python` | `gen_dealloc` | memory |
| 1.08% | `python` | `list_dealloc` | memory |
| 1.01% | `python` | `PyFunction_NewWithQualName` | memory |
| 1.01% | `python` | `_PyList_AppendTakeRefListResize` | list |
| 0.96% | `python` | `unsafe_tuple_compare` | unknown |
| 0.81% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.80% | `python` | `func_clear` | unknown |
| 0.77% | `python` | `tuple_alloc` | memory |
| 0.76% | `python` | `func_dealloc` | memory |
| 0.74% | `python` | `tuple_dealloc` | memory |
| 0.72% | `python` | `PyObject_RichCompare` | dynamic |
| 0.64% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.61% | `python` | `list_sort_impl` | list |
| 0.59% | `python` | `gen_close` | unknown |
| 0.58% | `python` | `PyDict_GetItemRef` | dict |
| 0.57% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.55% | `python` | `PyList_New.constprop.0` | memory |
| 0.53% | `python` | `PyObject_GC_Del` | gc |
| 0.48% | `python` | `make_gen` | miscobj |
| 0.43% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.43% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.43% | `python` | `_PyDict_SetItem_Take2` | dict |
| 0.43% | `python` | `PyMem_Realloc` | memory |
| 0.42% | `python` | `_PyObject_GC_Link` | gc |
| 0.42% | `python` | `tuple_subscript` | tuple |
| 0.41% | `python` | `_Py_NewReference` | memory |
| 0.37% | `python` | `_PyObject_GC_New` | gc |
| 0.35% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.35% | `python` | `PyObject_IsTrue` | dynamic |
| 0.34% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.32% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.31% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.31% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 0.28% | `python` | `build_indices_generic` | unknown |
| 0.27% | `python` | `PyLong_FromSsize_t` | int |
| 0.27% | `python` | `PyObject_Free` | dynamic |
| 0.26% | `python` | `PyObject_Malloc` | dynamic |

## coroutines

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 47.04% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 11.28% | `python` | `gen_dealloc` | memory |
| 3.92% | `python` | `make_gen` | miscobj |
| 3.70% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 3.54% | `python` | `_PyObject_GC_NewVar` | gc |
| 2.74% | `python` | `_PyObject_Free` | memory |
| 2.69% | `python` | `_PyObject_Malloc` | memory |
| 2.57% | `python` | `_Py_Dealloc` | memory |
| 2.52% | `python` | `_PyCompactLong_Subtract` | unknown |
| 2.38% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.11% | `python` | `_PyObject_GC_Link` | gc |
| 2.03% | `python` | `_Py_MakeCoro` | unknown |
| 1.95% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.95% | `python` | `PyObject_GC_Del` | gc |
| 1.79% | `python` | `_PyEval_GetAwaitable` | interpreter |
| 1.75% | `python` | `_PyCoro_GetAwaitableIter` | unknown |
| 1.32% | `python` | `_PyCompactLong_Add` | unknown |
| 1.20% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.93% | `python` | `PyObject_Malloc` | dynamic |
| 0.91% | `python` | `PyObject_Free` | dynamic |
| 0.83% | `python` | `gen_finalize` | unknown |
| 0.79% | `python` | `_Py_NewReference` | memory |

## coverage

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 11.51% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.93% | `tracer.cpython-316-aarch64-linux-gnu.so` | `CTracer_trace` | library |
| 6.73% | `python` | `call_instrumentation_vector.part.0.isra.0` | interpreter |
| 6.21% | `python` | `_Py_call_instrumentation_line` | interpreter |
| 3.79% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.75% | `python` | `_Py_dict_lookup` | lookup |
| 2.68% | `python` | `_PyObject_Free` | memory |
| 2.58% | `python` | `_PyTypeCache_Lookup` | unknown |
| 2.31% | `python` | `PyDict_GetItem` | dict |
| 2.20% | `python` | `_PyObject_Malloc` | memory |
| 2.00% | `python` | `set_add_entry_takeref` | miscobj |
| 1.90% | `python` | `PyLong_FromLong` | int |
| 1.83% | `python` | `unicode_decode_utf8.part.0` | str |
| 1.83% | `python` | `siphash13` | str |
| 1.50% | `python` | `PyUnicode_InternFromString` | str |
| 1.40% | `python` | `PyFrame_GetCode` | exceptions |
| 1.31% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 1.30% | `python` | `_Py_Dealloc` | memory |
| 1.24% | `python` | `sys_trace_start` | library |
| 1.21% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 1.14% | `python` | `PySet_Add` | miscobj |
| 1.10% | `python` | `sys_trace_return` | library |
| 1.03% | `python` | `_Py_call_instrumentation` | unknown |
| 1.02% | `python` | `PyObject_Hash` | dynamic |
| 1.00% | `python` | `PyUnicode_New.part.0` | memory |
| 0.92% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.92% | `python` | `_PyCode_GetCode` | interpreter |
| 0.92% | `python` | `PyObject_GC_Del` | gc |
| 0.90% | `python` | `_Py_call_instrumentation_arg` | unknown |
| 0.83% | `python` | `_PyType_GetDict` | dynamic |
| 0.83% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.81% | `python` | `PyObject_SetAttr` | dynamic |
| 0.81% | `python` | `PyEval_GetFrame` | interpreter |
| 0.81% | `python` | `_PyCompactLong_Subtract` | unknown |
| 0.76% | `tracer.cpython-316-aarch64-linux-gnu.so` | `CTracer_set_pdata_stack.constprop.0` | library |
| 0.76% | `python` | `PyFrame_GetLineNumber` | exceptions |
| 0.76% | `python` | `long_hash` | int |
| 0.72% | `python` | `_PyErr_GetRaisedException` | exceptions |
| 0.66% | `python` | `_PyUnicode_InternMortal` | str |
| 0.65% | `python` | `frame_dealloc` | memory |
| 0.62% | `python` | `_PyDict_LoadGlobalStackRef` | dict |
| 0.61% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.61% | `libc.so.6` | `memcmp` | libc |
| 0.61% | `python` | `PyObject_SetAttrString` | dynamic |
| 0.59% | `python` | `_PyStaticType_GetState` | unknown |
| 0.58% | `python` | `unicode_dealloc` | memory |
| 0.56% | `python` | `_Py_NewReference` | memory |
| 0.56% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.53% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.53% | `python` | `PyObject_Malloc` | dynamic |
| 0.52% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.52% | `libc.so.6` | `__strlen_asimd` | libc |
| 0.52% | `python` | `_PyCompactLong_Add` | unknown |
| 0.51% | `python` | `frame_trace_set` | unknown |
| 0.50% | `python` | `find_first_nonascii` | str |
| 0.49% | `python` | `getset_set` | unknown |
| 0.46% | `python` | `hashtable_unicode_hash` | unknown |
| 0.46% | `python` | `PyFrame_GetLasti` | exceptions |
| 0.46% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.45% | `python` | `_PyObject_GC_Link` | gc |
| 0.43% | `python` | `PyObject_Free` | dynamic |
| 0.41% | `python` | `_PyFrame_MakeAndSetFrameObject` | interpreter |
| 0.41% | `python` | `pysiphash` | unknown |
| 0.40% | `python` | `_PyEval_LoadGlobalStackRef` | interpreter |
| 0.40% | `python` | `_PyFrame_New_NoTrack` | interpreter |
| 0.39% | `python` | `PyCode_GetCode` | unknown |
| 0.37% | `python` | `_PyErr_SetRaisedException` | exceptions |
| 0.36% | `tracer.cpython-316-aarch64-linux-gnu.so` | `DataStack_grow` | library |
| 0.29% | `tracer.cpython-316-aarch64-linux-gnu.so` | `PyFrame_GetCode@plt` | library |
| 0.29% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.27% | `python` | `PyErr_SetRaisedException` | exceptions |

## crypto_pyaes

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 33.55% | `[JIT]` | `jit` | jit |
| 6.28% | `python` | `long_bitwise` | int |
| 5.95% | `python` | `_PyObject_Free` | memory |
| 4.13% | `python` | `_PyObject_Malloc` | memory |
| 3.45% | `python` | `long_alloc` | memory |
| 2.77% | `python` | `_Py_Dealloc` | memory |
| 2.76% | `python` | `long_rshift1` | int |
| 2.58% | `python` | `maybe_small_long` | unknown |
| 2.46% | `python` | `long_dealloc` | memory |
| 2.19% | `python` | `l_mod` | int |
| 2.04% | `python` | `long_rshift` | int |
| 1.99% | `python` | `PyNumber_Xor` | dynamic |
| 1.77% | `python` | `_Py_NewReference` | memory |
| 1.58% | `python` | `PyLong_FromSsize_t` | int |
| 1.58% | `python` | `PyLong_AsNativeBytes.constprop.0` | int |
| 1.53% | `python` | `PyLong_FromLong` | int |
| 1.37% | `python` | `PyObject_Free` | dynamic |
| 1.37% | `python` | `compactlongs_guard` | unknown |
| 1.34% | `python` | `PyObject_Malloc` | dynamic |
| 1.34% | `python` | `PyNumber_Rshift` | dynamic |
| 1.30% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.28% | `python` | `_PyCompactLong_Add` | unknown |
| 1.23% | `python` | `long_mod` | int |
| 1.19% | `python` | `PyNumber_Remainder` | dynamic |
| 1.11% | `python` | `compactlongs_and` | unknown |
| 0.93% | `python` | `_PyLong_FromMedium` | int |
| 0.83% | `python` | `long_xor` | int |
| 0.73% | `python` | `make_range_object` | unknown |
| 0.63% | `python` | `list_dealloc` | memory |
| 0.48% | `python` | `range_dealloc` | memory |
| 0.43% | `python` | `PyList_New.constprop.0` | memory |
| 0.40% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.38% | `python` | `set_lookkey` | miscobj |
| 0.36% | `python` | `_Py_CallBuiltinClass_StackRef` | unknown |
| 0.36% | `python` | `PyNumber_And` | dynamic |
| 0.35% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.34% | `python` | `range_iter` | miscobj |
| 0.32% | `python` | `list_slice_lock_held` | list |
| 0.32% | `python` | `PyLong_AsLong` | int |
| 0.32% | `python` | `zip_next` | unknown |
| 0.31% | `libc.so.6` | `__memcpy_generic` | libc |

## deepcopy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 24.88% | `[JIT]` | `jit` | jit |
| 5.90% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.51% | `python` | `_Py_dict_lookup` | lookup |
| 4.33% | `python` | `_PyObject_Malloc` | memory |
| 3.16% | `python` | `PySys_Audit` | unknown |
| 2.97% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.84% | `python` | `_PyObject_Free` | memory |
| 2.08% | `python` | `set_lookkey` | miscobj |
| 1.85% | `python` | `_Py_Dealloc` | memory |
| 1.59% | `python` | `long_richcompare` | int |
| 1.50% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.47% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.42% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.22% | `python` | `_PySet_Contains` | miscobj |
| 1.17% | `python` | `PyObject_Hash` | dynamic |
| 1.14% | `python` | `initialize_locals` | interpreter |
| 1.01% | `python` | `PyLong_FromVoidPtr` | int |
| 0.97% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.95% | `python` | `insertdict` | dict |
| 0.89% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.85% | `python` | `long_hash` | int |
| 0.85% | `python` | `sys_audit_tstate` | unknown |
| 0.83% | `python` | `_PyObject_Realloc` | memory |
| 0.81% | `python` | `list_append` | list |
| 0.80% | `python` | `_Py_NewReference` | memory |
| 0.80% | `python` | `_PyDict_Subscript` | dict |
| 0.76% | `python` | `tuple_dealloc` | memory |
| 0.73% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.67% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.65% | `python` | `_PyJIT_Entry` | compiler |
| 0.65% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.62% | `python` | `PyDict_Contains` | dict |
| 0.61% | `python` | `tuple_alloc` | memory |
| 0.59% | `python` | `list_dealloc` | memory |
| 0.54% | `python` | `dictiter_iternextitem` | dict |
| 0.53% | `python` | `PyObject_Free` | dynamic |
| 0.51% | `python` | `long_dealloc` | memory |
| 0.48% | `python` | `PyObject_GenericHash` | dynamic |
| 0.48% | `python` | `PyObject_GetItem` | dynamic |
| 0.48% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.47% | `python` | `PyObject_Malloc` | dynamic |
| 0.45% | `python` | `builtin_id` | unknown |
| 0.43% | `python` | `insert_to_emptydict` | dict |
| 0.43% | `python` | `PyCMethod_New` | memory |
| 0.43% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.42% | `python` | `_PyObject_Calloc` | memory |
| 0.40% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 0.39% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.39% | `python` | `dict_get` | dict |
| 0.37% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.37% | `python` | `PyObject_GC_Del` | gc |
| 0.36% | `python` | `PyType_IsSubtype` | dynamic |
| 0.33% | `python` | `_PyDict_StoreSubscript` | dict |
| 0.32% | `python` | `PyList_New` | memory |
| 0.30% | `python` | `_PyType_GetDict` | dynamic |
| 0.30% | `python` | `PyObject_SetItem` | dynamic |
| 0.30% | `python` | `_PyDict_Next` | dict |
| 0.29% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.27% | `python` | `_PyObject_GC_New` | gc |
| 0.27% | `python` | `dict_dealloc` | memory |
| 0.27% | `python` | `PyMethod_New` | memory |
| 0.26% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.26% | `python` | `PyDict_GetItemRef` | dict |
| 0.26% | `python` | `new_dict.constprop.0` | dict |
| 0.25% | `python` | `dict_merge` | dict |
| 0.25% | `libc.so.6` | `__memcpy_generic` | libc |

## deltablue

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 42.73% | `[JIT]` | `jit` | jit |
| 11.19% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.81% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 3.81% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.60% | `python` | `_PyTypeCache_Lookup` | unknown |
| 2.50% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 1.83% | `python` | `_PyThreadState_PopFrame` | threading |
| 1.79% | `python` | `gc_collect_main` | gc |
| 1.29% | `python` | `_PyJIT_Entry` | compiler |
| 1.29% | `python` | `_PyObject_Malloc` | memory |
| 1.21% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.20% | `python` | `_Py_VectorCallInstrumentation_StackRefSteal` | unknown |
| 1.11% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 1.09% | `python` | `listiter_next` | list |
| 1.00% | `python` | `_Py_LoadAttr_StackRefSteal` | unknown |
| 0.86% | `python` | `_PyType_GetDict` | dynamic |
| 0.84% | `python` | `_Py_Dealloc` | memory |
| 0.78% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.68% | `python` | `_PyObject_Free` | memory |
| 0.63% | `python` | `visit_decref` | gc |
| 0.57% | `python` | `PyType_IsSubtype` | dynamic |
| 0.53% | `python` | `PyMethod_New` | memory |
| 0.53% | `python` | `_Py_type_getattro` | lookup |
| 0.44% | `python` | `method_dealloc` | memory |
| 0.43% | `python` | `subtype_dealloc` | memory |
| 0.41% | `python` | `list_iter` | list |
| 0.40% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.39% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.38% | `python` | `object_richcompare` | dynamic |
| 0.38% | `python` | `PyObject_RichCompare` | dynamic |
| 0.37% | `python` | `_Py_NewReference` | memory |
| 0.35% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.35% | `python` | `_PyCompactLong_Add` | unknown |
| 0.35% | `python` | `subtype_traverse` | gc |
| 0.33% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.33% | `python` | `PyDict_GetItemRef` | dict |
| 0.33% | `python` | `_PySuper_LookupDescr` | unknown |
| 0.31% | `python` | `initialize_locals` | interpreter |
| 0.29% | `python` | `list_append` | list |
| 0.28% | `python` | `PyUnicode_Format` | str |
| 0.27% | `python` | `method_vectorcall_O` | calls |
| 0.25% | `libc.so.6` | `__memcpy_generic` | libc |

## django_template

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.52% | `[JIT]` | `jit` | jit |
| 12.47% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.30% | `python` | `_PyObject_Malloc` | memory |
| 3.28% | `python` | `_PyTypeCache_Lookup` | unknown |
| 2.79% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.29% | `python` | `initialize_locals` | interpreter |
| 1.89% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.88% | `python` | `_PyObject_Free` | memory |
| 1.78% | `python` | `_Py_Dealloc` | memory |
| 1.53% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.44% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.41% | `python` | `replace` | str |
| 1.35% | `python` | `_Py_dict_lookup` | lookup |
| 1.25% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.19% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 1.19% | `python` | `PyType_IsSubtype` | dynamic |
| 1.17% | `python` | `tuple_dealloc` | memory |
| 1.14% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 1.08% | `python` | `tuple_alloc` | memory |
| 1.05% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.88% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.87% | `python` | `_PyType_GetDict` | dynamic |
| 0.87% | `python` | `insertdict` | dict |
| 0.74% | `python` | `object_isinstance` | dynamic |
| 0.74% | `python` | `_PyJIT_Entry` | compiler |
| 0.74% | `python` | `unicode_replace` | str |
| 0.73% | `python` | `_PyEvalFramePushAndInit_Ex` | interpreter |
| 0.72% | `python` | `_PyCallMethodDescriptorFastWithKeywords_StackRef` | unknown |
| 0.70% | `python` | `_Py_NewReference` | memory |
| 0.68% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.55% | `python` | `PyDict_GetItemRef` | dict |
| 0.55% | `python` | `_PyStaticType_GetState` | unknown |
| 0.54% | `python` | `PyObject_GC_Del` | gc |
| 0.53% | `python` | `PyObject_SetItem` | dynamic |
| 0.53% | `python` | `listiter_next` | list |
| 0.51% | `python` | `long_to_decimal_string_internal` | int |
| 0.46% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.43% | `python` | `dict_dealloc` | memory |
| 0.41% | `python` | `PyErr_Occurred` | exceptions |
| 0.41% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.40% | `python` | `_PyObject_GC_New` | gc |
| 0.39% | `python` | `tupleiter_next` | tuple |
| 0.39% | `python` | `list_dealloc` | memory |
| 0.38% | `python` | `_PyErr_CheckSignalsTstate` | exceptions |
| 0.37% | `python` | `tuple_iter` | tuple |
| 0.37% | `python` | `_PyCompactLong_Subtract` | unknown |
| 0.37% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.36% | `python` | `_PyObject_Calloc` | memory |
| 0.35% | `python` | `PyErr_CheckSignals` | exceptions |
| 0.32% | `python` | `list_subscript` | list |
| 0.32% | `python` | `chain_next` | unknown |
| 0.32% | `python` | `gen_dealloc` | memory |
| 0.31% | `python` | `PyObject_GetIter` | dynamic |
| 0.31% | `python` | `enum_next` | miscobj |
| 0.30% | `python` | `PyType_GenericAlloc` | memory |
| 0.30% | `python` | `PyDict_New` | memory |
| 0.30% | `python` | `PyObject_Str` | dynamic |
| 0.29% | `python` | `PyObject_IsInstance` | dynamic |
| 0.29% | `python` | `PyObject_Malloc` | dynamic |
| 0.29% | `python` | `new_dict.constprop.0` | dict |
| 0.29% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.29% | `python` | `PyMethod_New` | memory |
| 0.28% | `python` | `getset_get` | dynamic |
| 0.27% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.26% | `python` | `_PyDict_StoreSubscript` | dict |
| 0.25% | `python` | `PyThread_get_thread_ident` | threading |

## docutils

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 14.21% | `[JIT]` | `jit` | jit |
| 10.82% | `python` | `sre_ucs1_match` | library |
| 7.34% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.63% | `python` | `gc_collect_main` | gc |
| 3.43% | `python` | `_PyTypeCache_Lookup` | unknown |
| 2.73% | `python` | `_PyObject_Malloc` | memory |
| 2.11% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.09% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.79% | `python` | `visit_decref` | gc |
| 1.48% | `python` | `_PyObject_Free` | memory |
| 1.41% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.40% | `python` | `_Py_dict_lookup` | lookup |
| 1.22% | `python` | `_Py_Dealloc` | memory |
| 1.16% | `libc.so.6` | `__memcpy_generic` | libc |
| 1.13% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 1.05% | `python` | `list_dealloc` | memory |
| 0.93% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.92% | `python` | `initialize_locals` | interpreter |
| 0.92% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.84% | `python` | `visit_reachable` | gc |
| 0.78% | `python` | `_PyJIT_Entry` | compiler |
| 0.70% | `python` | `PyType_IsSubtype` | dynamic |
| 0.69% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.65% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.55% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.54% | `python` | `tuple_alloc` | memory |
| 0.54% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.52% | `python` | `PyUnicode_Format` | str |
| 0.52% | `python` | `tuple_dealloc` | memory |
| 0.51% | `python` | `_PyType_GetDict` | dynamic |
| 0.49% | `python` | `list_traverse` | gc |
| 0.47% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.47% | `python` | `list_slice_lock_held` | list |
| 0.43% | `python` | `sre_search` | library |
| 0.42% | `python` | `dict_traverse` | gc |
| 0.38% | `python` | `PyDict_GetItemRef` | dict |
| 0.38% | `python` | `insertdict` | dict |
| 0.38% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 0.36% | `python` | `_Py_NewReference` | memory |
| 0.36% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.35% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 0.34% | `python` | `PyList_New.constprop.0` | memory |
| 0.34% | `python` | `_PyObject_Realloc` | memory |
| 0.33% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.33% | `python` | `_PyDict_Subscript` | dict |
| 0.33% | `python` | `list_extend_lock_held` | list |
| 0.33% | `python` | `PyObject_SetAttr` | dynamic |
| 0.33% | `python` | `gen_dealloc` | memory |
| 0.33% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.32% | `python` | `_copy_characters.constprop.0.isra.0` | str |
| 0.31% | `python` | `sre_ucs1_count` | library |
| 0.29% | `libc.so.6` | `_int_malloc` | libc |
| 0.29% | `python` | `PyMethod_New` | memory |
| 0.26% | `python` | `store_instance_attr_lock_held` | unknown |
| 0.26% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.25% | `python` | `PyObject_Malloc` | dynamic |
| 0.25% | `python` | `getset_get` | dynamic |
| 0.25% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |

## dulwich_log

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 14.77% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.72% | `[JIT]` | `jit` | jit |
| 3.64% | `python` | `_PyObject_Malloc` | memory |
| 2.19% | `python` | `_PyObject_Free` | memory |
| 1.91% | `libz.so.1.3` | `inflate` | library |
| 1.73% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.70% | `python` | `_Py_Dealloc` | memory |
| 1.41% | `libc.so.6` | `__memcpy_generic` | libc |
| 1.05% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 0.97% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.93% | `libz.so.1.3` | `0x00000000000033dc` | library |
| 0.87% | `python` | `initialize_locals` | interpreter |
| 0.86% | `python` | `tuple_alloc` | memory |
| 0.80% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.75% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.69% | `python` | `tuple_dealloc` | memory |
| 0.69% | `python` | `_PyCallMethodDescriptorFastWithKeywords_StackRef` | unknown |
| 0.65% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.64% | `python` | `_Py_NewReference` | memory |
| 0.59% | `libc.so.6` | `_int_malloc` | libc |
| 0.58% | `python` | `PyObject_Malloc` | dynamic |
| 0.49% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.46% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.46% | `python` | `PyList_New.constprop.0` | memory |
| 0.46% | `[kernel.kallsyms]` | `link_path_walk.part.0.constprop.0` | kernel |
| 0.45% | `python` | `PyUnicode_Decode` | str |
| 0.45% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.44% | `python` | `PyUnicode_AsEncodedString` | str |
| 0.44% | `python` | `PyLong_FromString` | int |
| 0.43% | `python` | `PySlice_New` | memory |
| 0.43% | `python` | `siphash13` | str |
| 0.42% | `libz.so.1.3` | `0x00000000000024c0` | library |
| 0.42% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.42% | `python` | `PyObject_RichCompare` | dynamic |
| 0.41% | `python` | `PyObject_Free` | dynamic |
| 0.40% | `python` | `do_mkvalue` | unknown |
| 0.39% | `libz.so.1.3` | `0x00000000000024a8` | library |
| 0.38% | `python` | `PyObject_GC_Del` | gc |
| 0.37% | `python` | `_Py_dict_lookup` | lookup |
| 0.37% | `python` | `clear_slots` | unknown |
| 0.36% | `[kernel.kallsyms]` | `__update_cpu_freelist_fast` | kernel |
| 0.34% | `libz.so.1.3` | `adler32_z` | library |
| 0.34% | `[kernel.kallsyms]` | `el0_svc` | kernel |
| 0.33% | `python` | `PyObject_GetItem` | dynamic |
| 0.33% | `python` | `bytes_subscript` | str |
| 0.33% | `python` | `_PyCompactLong_Add` | unknown |
| 0.33% | `binascii.cpython-316-aarch64-linux-gnu.so` | `binascii_a2b_hex_impl.isra.0` | library |
| 0.33% | `libc.so.6` | `__GI___libc_open` | libc |
| 0.33% | `python` | `list_dealloc` | memory |
| 0.32% | `python` | `set_lookkey` | miscobj |
| 0.32% | `python` | `_PyJIT_Entry` | compiler |
| 0.32% | `python` | `long_dealloc` | memory |
| 0.31% | `[kernel.kallsyms]` | `step_into` | kernel |
| 0.31% | `python` | `bytes_richcompare` | str |
| 0.31% | `python` | `_PyEval_SliceIndex` | interpreter |
| 0.30% | `libz.so.1.3` | `0x00000000000033e4` | library |
| 0.30% | `[kernel.kallsyms]` | `kmem_cache_alloc` | kernel |
| 0.29% | `libz.so.1.3` | `0x00000000000033d4` | library |
| 0.28% | `python` | `PyObject_IsTrue` | dynamic |
| 0.28% | `[kernel.kallsyms]` | `__arch_copy_to_user` | kernel |
| 0.28% | `libz.so.1.3` | `0x000000000000376c` | library |
| 0.27% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.27% | `libz.so.1.3` | `0x00000000000024ac` | library |
| 0.27% | `python` | `PyBytesWriter_Create` | unknown |
| 0.26% | `[kernel.kallsyms]` | `generic_permission` | kernel |
| 0.26% | `libc.so.6` | `__gconv_transform_utf8_internal` | libc |
| 0.25% | `libz.so.1.3` | `0x00000000000033d8` | library |

## fannkuch

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 26.55% | `[JIT]` | `jit` | jit |
| 5.96% | `python` | `list_ass_slice_lock_held` | list |
| 5.26% | `python` | `_Py_Dealloc` | memory |
| 4.67% | `python` | `list_slice_wrap` | list |
| 3.93% | `python` | `list_dealloc` | memory |
| 3.86% | `python` | `_PyEval_SliceIndex` | interpreter |
| 3.62% | `python` | `PyObject_GC_UnTrack` | gc |
| 3.46% | `python` | `_PyObject_Malloc` | memory |
| 3.37% | `python` | `slice_dealloc` | memory |
| 3.32% | `python` | `_PyList_SliceSubscript` | list |
| 3.27% | `python` | `PySlice_Unpack` | miscobj |
| 2.85% | `python` | `PySlice_New` | memory |
| 2.84% | `python` | `_PyObject_Free` | memory |
| 2.79% | `python` | `list_ass_subscript` | list |
| 2.78% | `python` | `PySlice_AdjustIndices` | miscobj |
| 2.68% | `python` | `_PyCompactLong_Add` | unknown |
| 2.39% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 2.38% | `python` | `PyList_New.constprop.0` | memory |
| 1.88% | `python` | `PySequence_Fast` | dynamic |
| 1.67% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 1.56% | `python` | `_Py_NewReference` | memory |
| 1.27% | `python` | `list_insert` | list |
| 1.03% | `python` | `_PyCompactLong_Subtract` | unknown |
| 0.94% | `python` | `PyObject_SetItem` | dynamic |
| 0.91% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.79% | `python` | `_PyNumber_Index` | dynamic |
| 0.71% | `python` | `PyMem_Malloc` | memory |
| 0.71% | `python` | `list_pop` | list |
| 0.66% | `python` | `list_slice_lock_held` | list |
| 0.63% | `python` | `PyMem_Free` | memory |
| 0.46% | `python` | `PyLong_AsSsize_t` | int |
| 0.30% | `python` | `list_resize` | list |

## float

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 26.77% | `[JIT]` | `jit` | jit |
| 5.08% | `libm.so.6` | `__sin` | library |
| 4.91% | `python` | `PyFloat_FromDouble` | float |
| 4.46% | `libm.so.6` | `__cos` | library |
| 3.77% | `python` | `subtype_traverse` | gc |
| 3.30% | `python` | `_Py_Dealloc` | memory |
| 3.12% | `python` | `visit_reachable` | gc |
| 3.11% | `python` | `gc_collect_main` | gc |
| 3.04% | `math.cpython-316-aarch64-linux-gnu.so` | `math_sqrt` | library |
| 2.80% | `python` | `visit_decref` | gc |
| 2.72% | `python` | `float_dealloc` | memory |
| 2.27% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.26% | `python` | `_Py_NewReference` | memory |
| 2.18% | `python` | `_PyObject_Malloc` | memory |
| 2.18% | `python` | `_PyObject_Free` | memory |
| 1.85% | `python` | `_PyMember_GetOffset` | unknown |
| 1.31% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.14% | `python` | `_PyFloat_ExactDealloc` | memory |
| 1.06% | `python` | `clear_slots` | unknown |
| 1.06% | `python` | `PyFloat_AsDouble` | float |
| 1.00% | `math.cpython-316-aarch64-linux-gnu.so` | `math_cos` | library |
| 0.99% | `math.cpython-316-aarch64-linux-gnu.so` | `math_sin` | library |
| 0.99% | `python` | `long_float` | int |
| 0.87% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.80% | `python` | `initialize_locals` | interpreter |
| 0.77% | `python` | `subtype_dealloc` | memory |
| 0.75% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.66% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.66% | `python` | `PyObject_Malloc` | dynamic |
| 0.61% | `python` | `list_dealloc` | memory |
| 0.58% | `python` | `_PyLong_FromMedium` | int |
| 0.55% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 0.54% | `python` | `PyType_GenericAlloc` | memory |
| 0.53% | `python` | `list_traverse` | gc |
| 0.51% | `python` | `PyObject_Free` | dynamic |
| 0.51% | `python` | `float_compactlong_true_div` | float |
| 0.47% | `python` | `PyType_IsSubtype` | dynamic |
| 0.44% | `python` | `list_slice_lock_held` | list |
| 0.42% | `[kernel.kallsyms]` | `__pi_clear_page` | kernel |
| 0.40% | `[kernel.kallsyms]` | `el0_da` | kernel |
| 0.39% | `python` | `type_is_gc` | gc |
| 0.37% | `libc.so.6` | `__errno_location` | libc |
| 0.35% | `python` | `_PyObject_GC_Link` | gc |
| 0.32% | `python` | `nonzero_float_compactlong_guard` | unknown |
| 0.32% | `python` | `long_dealloc` | memory |
| 0.31% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.28% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.27% | `python` | `float_compactlong_guard` | float |
| 0.27% | `python` | `PyLong_FromLong` | int |
| 0.27% | `python` | `PyObject_GC_Del` | gc |
| 0.26% | `[kernel.kallsyms]` | `zap_pte_range` | kernel |

## gc_collect

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 27.95% | `python` | `gc_collect_main` | gc |
| 21.54% | `python` | `visit_reachable` | gc |
| 19.65% | `python` | `visit_decref` | gc |
| 8.21% | `python` | `dict_traverse` | gc |
| 2.58% | `python` | `func_traverse` | gc |
| 2.54% | `[JIT]` | `jit` | jit |
| 1.81% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 1.77% | `python` | `type_is_gc` | gc |
| 1.52% | `python` | `subtype_traverse` | gc |
| 1.19% | `python` | `type_traverse` | gc |
| 1.16% | `python` | `tuple_traverse` | gc |
| 0.77% | `python` | `PyObject_IS_GC` | gc |
| 0.76% | `python` | `list_traverse` | gc |
| 0.72% | `python` | `set_traverse` | gc |
| 0.50% | `python` | `meth_traverse` | gc |
| 0.48% | `python` | `_PyObject_Malloc` | memory |
| 0.46% | `python` | `_PyTuple_MaybeUntrack` | gc |
| 0.45% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.34% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.30% | `python` | `descr_traverse` | gc |
| 0.30% | `python` | `initialize_locals` | interpreter |
| 0.27% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.26% | `python` | `subtype_dealloc` | memory |

## gc_traversal

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.67% | `python` | `visit_decref` | gc |
| 27.64% | `python` | `visit_reachable` | gc |
| 11.21% | `python` | `list_traverse` | gc |
| 10.55% | `python` | `gc_collect_main` | gc |
| 5.02% | `[JIT]` | `jit` | jit |
| 3.55% | `python` | `dict_traverse` | gc |
| 1.12% | `python` | `list_dealloc` | memory |
| 1.09% | `python` | `func_traverse` | gc |
| 0.99% | `python` | `PyLong_FromLong` | int |
| 0.67% | `python` | `type_is_gc` | gc |
| 0.55% | `python` | `type_traverse` | gc |
| 0.49% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.49% | `python` | `tuple_traverse` | gc |
| 0.38% | `python` | `subtype_traverse` | gc |
| 0.33% | `python` | `set_traverse` | gc |
| 0.33% | `python` | `PyObject_IS_GC` | gc |

## generators

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.57% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 12.05% | `[JIT]` | `jit` | jit |
| 6.55% | `python` | `gc_collect_main` | gc |
| 3.09% | `python` | `_PyObject_Malloc` | memory |
| 2.47% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 2.46% | `python` | `visit_reachable` | gc |
| 2.31% | `python` | `PyObject_RichCompareBool` | dynamic |
| 2.19% | `python` | `_Py_Dealloc` | memory |
| 2.11% | `python` | `visit_decref` | gc |
| 1.92% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.78% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.67% | `python` | `_PyLong_FromMedium` | int |
| 1.64% | `python` | `range_subscript` | miscobj |
| 1.59% | `python` | `long_dealloc` | memory |
| 1.42% | `python` | `subtype_traverse` | gc |
| 1.40% | `python` | `PyLong_AsLongAndOverflow` | int |
| 1.35% | `python` | `make_range_object` | unknown |
| 1.28% | `python` | `_PySlice_GetLongIndices` | miscobj |
| 1.21% | `python` | `initialize_locals` | interpreter |
| 1.19% | `python` | `PySlice_New` | memory |
| 1.19% | `python` | `PyNumber_Add` | dynamic |
| 1.18% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.18% | `python` | `long_richcompare` | int |
| 1.13% | `python` | `long_add` | int |
| 1.10% | `python` | `gen_dealloc` | memory |
| 1.06% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 1.03% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.02% | `python` | `_PyObject_Free` | memory |
| 0.91% | `python` | `_Py_NewReference` | memory |
| 0.83% | `python` | `range_dealloc` | memory |
| 0.82% | `python` | `PyObject_GetItem` | dynamic |
| 0.80% | `python` | `_PyJIT_Entry` | compiler |
| 0.66% | `python` | `long_mul` | int |
| 0.63% | `python` | `PyType_GenericAlloc` | memory |
| 0.62% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.57% | `python` | `slice_dealloc` | memory |
| 0.54% | `python` | `PyNumber_Multiply` | dynamic |
| 0.54% | `python` | `_PyEval_Vector` | interpreter |
| 0.54% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.52% | `python` | `PyLong_FromLong` | int |
| 0.48% | `python` | `subtype_dealloc` | memory |
| 0.47% | `python` | `PyNumber_Index` | dynamic |
| 0.47% | `python` | `long_add_method` | int |
| 0.44% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 0.43% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.40% | `python` | `PyLong_FromSsize_t` | int |
| 0.39% | `python` | `make_gen` | miscobj |
| 0.36% | `python` | `compute_range_item` | unknown |
| 0.36% | `python` | `slot_tp_iter` | unknown |
| 0.36% | `python` | `PyObject_GC_Del` | gc |
| 0.36% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.35% | `python` | `_PyObject_GC_Link` | gc |
| 0.34% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.32% | `python` | `long_div` | int |
| 0.30% | `python` | `PyObject_Malloc` | dynamic |
| 0.30% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.29% | `python` | `PyObject_Free` | dynamic |
| 0.28% | `python` | `PyLong_AsSsize_t` | int |
| 0.28% | `python` | `type_is_gc` | gc |
| 0.28% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.27% | `python` | `_PyEval_GetIter` | interpreter |
| 0.27% | `python` | `_PyCompactLong_Add` | unknown |
| 0.26% | `python` | `PyNumber_FloorDivide` | dynamic |

## go

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 52.09% | `[JIT]` | `jit` | jit |
| 14.11% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.20% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.71% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.79% | `python` | `initialize_locals` | interpreter |
| 1.32% | `python` | `_PyObject_Free` | memory |
| 1.28% | `python` | `long_bitwise` | int |
| 1.23% | `python` | `insertdict` | dict |
| 1.18% | `python` | `_PyCompactLong_Add` | unknown |
| 1.15% | `python` | `_PyThreadState_PopFrame` | threading |
| 1.13% | `python` | `_PyJIT_Entry` | compiler |
| 1.03% | `python` | `_PyObject_Malloc` | memory |
| 1.02% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.83% | `python` | `long_dealloc` | memory |
| 0.80% | `python` | `_PyCompactLong_Subtract` | unknown |
| 0.75% | `python` | `_Py_Dealloc` | memory |
| 0.72% | `python` | `PyNumber_InPlaceXor` | dynamic |
| 0.57% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.51% | `python` | `_Py_dict_lookup` | lookup |
| 0.50% | `python` | `PyDict_SetItem` | dict |
| 0.49% | `python` | `_Py_NewReference` | memory |
| 0.48% | `python` | `set_lookkey` | miscobj |
| 0.46% | `python` | `PyFloat_FromDouble` | float |
| 0.42% | `python` | `long_alloc` | memory |
| 0.32% | `python` | `float_dealloc` | memory |
| 0.30% | `python` | `PyObject_Free` | dynamic |
| 0.28% | `python` | `set_add_entry_takeref` | miscobj |
| 0.27% | `_random.cpython-316-aarch64-linux-gnu.so` | `genrand_uint32` | library |
| 0.27% | `python` | `PyLong_FromLong` | int |
| 0.27% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.27% | `python` | `_Py_CallBuiltinClass_StackRef` | unknown |

## hexiom

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 40.79% | `[JIT]` | `jit` | jit |
| 16.97% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.09% | `python` | `PyObject_RichCompareBool` | dynamic |
| 3.64% | `python` | `long_richcompare` | int |
| 3.28% | `python` | `_PyJIT_Entry` | compiler |
| 3.01% | `python` | `list_contains` | list |
| 2.55% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.17% | `python` | `gen_iternext` | miscobj |
| 1.75% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.49% | `python` | `PyObject_Size` | dynamic |
| 1.27% | `python` | `PyLong_FromSsize_t` | int |
| 1.02% | `python` | `PyLong_FromLong` | int |
| 0.95% | `python` | `_PyObject_Malloc` | memory |
| 0.94% | `python` | `builtin_sum` | unknown |
| 0.80% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.79% | `python` | `_PyObject_Free` | memory |
| 0.69% | `python` | `_Py_Dealloc` | memory |
| 0.63% | `python` | `PySequence_Contains` | dynamic |
| 0.58% | `python` | `PyIter_Next` | dynamic |
| 0.52% | `python` | `make_range_object` | unknown |
| 0.46% | `python` | `_PyDict_LoadBuiltinsFromGlobals` | dict |
| 0.39% | `python` | `_PyCompactLong_Add` | unknown |
| 0.35% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.35% | `python` | `list_length` | list |
| 0.35% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.35% | `python` | `gen_dealloc` | memory |
| 0.33% | `python` | `PyList_New.constprop.0` | memory |
| 0.28% | `python` | `range_dealloc` | memory |
| 0.28% | `python` | `PyLong_AsLong` | int |
| 0.26% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.26% | `python` | `list_dealloc` | memory |
| 0.26% | `python` | `unicodekeys_lookup_unicode` | lookup |

## html5lib

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.56% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 14.52% | `[JIT]` | `jit` | jit |
| 8.17% | `python` | `sre_search` | library |
| 2.51% | `python` | `_PyObject_Malloc` | memory |
| 2.22% | `python` | `_Py_dict_lookup` | lookup |
| 2.04% | `python` | `gc_collect_main` | gc |
| 1.83% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.52% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.19% | `python` | `_PyObject_Free` | memory |
| 1.18% | `python` | `_PyDict_Subscript` | dict |
| 1.12% | `python` | `_Py_Dealloc` | memory |
| 1.10% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.10% | `python` | `sre_ucs1_count` | library |
| 1.08% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.02% | `python` | `_PyJIT_Entry` | compiler |
| 0.99% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.96% | `python` | `initialize_locals` | interpreter |
| 0.76% | `python` | `set_lookkey` | miscobj |
| 0.76% | `python` | `visit_decref` | gc |
| 0.76% | `python` | `insertdict` | dict |
| 0.69% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.68% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.56% | `python` | `PyMethod_New` | memory |
| 0.55% | `python` | `PyObject_IsTrue` | dynamic |
| 0.55% | `python` | `visit_reachable` | gc |
| 0.54% | `python` | `_PyCompactLong_Add` | unknown |
| 0.52% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.51% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.49% | `python` | `PyList_New.constprop.0` | memory |
| 0.47% | `python` | `_Py_NewReference` | memory |
| 0.45% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.45% | `python` | `list_subscript` | list |
| 0.43% | `python` | `_PyUnicode_Equal` | str |
| 0.41% | `python` | `insert_to_emptydict` | dict |
| 0.41% | `python` | `PyObject_GetItem` | dynamic |
| 0.39% | `python` | `long_dealloc` | memory |
| 0.38% | `python` | `_PyUnicode_TranslateCharmap` | str |
| 0.38% | `libc.so.6` | `_int_malloc` | libc |
| 0.38% | `libc.so.6` | `memcmp` | libc |
| 0.36% | `python` | `sre_ucs1_match` | library |
| 0.36% | `python` | `list_contains` | list |
| 0.31% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.31% | `python` | `PyObject_Hash` | dynamic |
| 0.31% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.30% | `python` | `method_dealloc` | memory |
| 0.29% | `python` | `_Py_BuildMap_StackRefSteal` | unknown |
| 0.29% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.28% | `python` | `tuple_dealloc` | memory |
| 0.28% | `python` | `_PySet_Contains` | miscobj |
| 0.28% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.28% | `python` | `_copy_characters.constprop.0.isra.0` | str |
| 0.27% | `python` | `list_dealloc` | memory |
| 0.27% | `python` | `_PyDict_FromItems` | dict |
| 0.27% | `python` | `PyObject_Malloc` | dynamic |
| 0.26% | `python` | `_sre_SRE_Pattern_prefixmatch` | library |
| 0.26% | `python` | `PyUnicode_New.part.0` | memory |
| 0.26% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.25% | `python` | `PyObject_RichCompare` | dynamic |

## json

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 11.42% | `_json.cpython-316-aarch64-linux-gnu.so` | `scanstring_unicode` | library |
| 6.58% | `python` | `_PyObject_Malloc` | memory |
| 5.27% | `_json.cpython-316-aarch64-linux-gnu.so` | `scan_once_unicode` | library |
| 4.68% | `python` | `_PyObject_Free` | memory |
| 4.01% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 3.72% | `python` | `PyUnicode_Substring` | str |
| 3.29% | `python` | `_Py_dict_lookup` | lookup |
| 3.27% | `[JIT]` | `jit` | jit |
| 3.24% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.14% | `python` | `PyLong_FromString` | int |
| 3.13% | `python` | `siphash13` | str |
| 2.86% | `python` | `insertdict` | dict |
| 2.35% | `python` | `PyUnicode_New.part.0` | memory |
| 2.02% | `python` | `_Py_Dealloc` | memory |
| 1.67% | `libc.so.6` | `__memcpy_generic` | libc |
| 1.62% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 1.54% | `python` | `unicode_dealloc` | memory |
| 1.49% | `python` | `PyUnicode_Splitlines` | str |
| 1.48% | `python` | `find_empty_slot` | dict |
| 1.29% | `python` | `build_indices_unicode` | dict |
| 1.27% | `libc.so.6` | `_int_malloc` | libc |
| 1.19% | `python` | `PyObject_Malloc` | dynamic |
| 1.00% | `python` | `initialize_locals` | interpreter |
| 0.96% | `python` | `_Py_NewReference` | memory |
| 0.91% | `python` | `PyObject_Free` | dynamic |
| 0.84% | `python` | `sre_ucs1_match` | library |
| 0.82% | `python` | `_PyDict_SetItem_Take2` | dict |
| 0.80% | `python` | `unicode_hash` | str |
| 0.70% | `python` | `dictresize` | dict |
| 0.67% | `python` | `_sre_SRE_Pattern_prefixmatch` | library |
| 0.65% | `python` | `PyDict_GetItemRef` | dict |
| 0.62% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.61% | `python` | `maybe_small_long` | unknown |
| 0.60% | `python` | `insert_to_emptydict` | dict |
| 0.58% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.52% | `_json.cpython-316-aarch64-linux-gnu.so` | `PyUnicode_Substring@plt` | library |
| 0.46% | `python` | `_PyObject_Realloc` | memory |
| 0.45% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.45% | `libc.so.6` | `__memset_zva64` | libc |
| 0.44% | `python` | `PyDict_New` | memory |
| 0.43% | `python` | `new_keys_object` | dict |
| 0.43% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.43% | `libc.so.6` | `malloc` | libc |
| 0.42% | `python` | `pysiphash` | unknown |
| 0.42% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.40% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.38% | `python` | `long_alloc` | memory |
| 0.38% | `python` | `PyObject_Hash` | dynamic |
| 0.38% | `python` | `PyUnicodeWriter_WriteChar` | str |
| 0.38% | `python` | `tuple_dealloc` | memory |
| 0.37% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.36% | `python` | `vgetargskeywords_impl.constprop.0` | unknown |
| 0.35% | `python` | `Py_HashBuffer` | unknown |
| 0.35% | `python` | `convertitem.constprop.0` | unknown |
| 0.32% | `python` | `tuple_alloc` | memory |
| 0.31% | `libc.so.6` | `unlink_chunk.isra.0` | libc |
| 0.31% | `python` | `PyDict_SetDefaultRef` | dict |
| 0.30% | `python` | `dict_dealloc` | memory |
| 0.29% | `libc.so.6` | `_int_free` | libc |
| 0.27% | `libc.so.6` | `_int_free_merge_chunk` | libc |

## json_dumps

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 6.47% | `[JIT]` | `jit` | jit |
| 4.68% | `_json.cpython-316-aarch64-linux-gnu.so` | `encoder_listencode_obj` | library |
| 4.50% | `python` | `_PyObject_Malloc` | memory |
| 4.15% | `python` | `PyUnicodeWriter_WriteChar` | str |
| 3.64% | `python` | `PyUnicodeWriter_WriteASCII` | str |
| 3.36% | `python` | `_Py_dict_lookup` | lookup |
| 3.21% | `_json.cpython-316-aarch64-linux-gnu.so` | `ascii_escape_size` | library |
| 2.81% | `python` | `_PyUnicodeWriter_WriteStr` | str |
| 2.79% | `libc.so.6` | `__memcpy_generic` | libc |
| 2.63% | `python` | `convertitem.constprop.0` | unknown |
| 2.42% | `python` | `PyDict_Next` | dict |
| 2.30% | `_json.cpython-316-aarch64-linux-gnu.so` | `encoder_encode_key_value` | library |
| 2.29% | `python` | `vgetargskeywords_impl.constprop.0` | unknown |
| 2.25% | `_json.cpython-316-aarch64-linux-gnu.so` | `write_escaped_ascii` | library |
| 2.16% | `python` | `_PyObject_Realloc` | memory |
| 2.03% | `python` | `_copy_characters.constprop.0.isra.0` | str |
| 1.75% | `python` | `_PyUnicode_ResizeCompact` | str |
| 1.74% | `python` | `initialize_locals` | interpreter |
| 1.73% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.66% | `python` | `_PyObject_Free` | memory |
| 1.62% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.61% | `python` | `_Py_Dealloc` | memory |
| 1.56% | `python` | `PyDict_GetItemRef` | dict |
| 1.55% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.43% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 1.24% | `python` | `tuple_dealloc` | memory |
| 1.17% | `python` | `long_to_decimal_string_internal` | int |
| 1.12% | `python` | `tuple_alloc` | memory |
| 1.06% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.05% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.81% | `_json.cpython-316-aarch64-linux-gnu.so` | `encoder_write_string` | library |
| 0.73% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.67% | `python` | `PyTuple_FromArray.part.0` | tuple |
| 0.67% | `python` | `_PyType_GetDict` | dynamic |
| 0.67% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.66% | `python` | `PyType_IsSubtype` | dynamic |
| 0.66% | `_json.cpython-316-aarch64-linux-gnu.so` | `PyUnicodeWriter_WriteChar@plt` | library |
| 0.65% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.65% | `python` | `_Py_NewReference` | memory |
| 0.60% | `python` | `delitem_common` | dynamic |
| 0.59% | `python` | `long_hash` | int |
| 0.57% | `python` | `memcpy@plt` | memory |
| 0.56% | `_json.cpython-316-aarch64-linux-gnu.so` | `encoder_new` | library |
| 0.55% | `python` | `PyUnicodeWriter_Create` | str |
| 0.54% | `python` | `_PyUnicode_FastCopyCharacters` | str |
| 0.54% | `python` | `insertdict` | dict |
| 0.52% | `python` | `PyDict_DelItem` | dict |
| 0.49% | `python` | `new_dict.constprop.0` | dict |
| 0.48% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.43% | `python` | `PyMethod_New` | memory |
| 0.43% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.42% | `libc.so.6` | `strchr` | libc |
| 0.41% | `python` | `PyArg_ParseTupleAndKeywords` | calls |
| 0.39% | `python` | `long_alloc` | memory |
| 0.38% | `python` | `PyUnicodeWriter_WriteStr` | str |
| 0.38% | `python` | `object_isinstance` | dynamic |
| 0.36% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.36% | `python` | `PyDict_SetItem` | dict |
| 0.35% | `python` | `PyLong_FromVoidPtr` | int |
| 0.34% | `_json.cpython-316-aarch64-linux-gnu.so` | `encoder_dealloc` | library |
| 0.34% | `python` | `PyDict_Contains` | dict |
| 0.34% | `python` | `dict_dealloc` | memory |
| 0.34% | `python` | `PyObject_Realloc` | memory |
| 0.33% | `python` | `PyObject_Hash` | dynamic |
| 0.32% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.31% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.31% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.30% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.30% | `python` | `_Py_NewReferenceNoTotal` | memory |
| 0.30% | `_json.cpython-316-aarch64-linux-gnu.so` | `ascii_escape_unicode_and_size` | library |
| 0.29% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.27% | `python` | `PyUnicode_New` | memory |
| 0.27% | `_json.cpython-316-aarch64-linux-gnu.so` | `PyUnicodeWriter_WriteASCII@plt` | library |
| 0.26% | `python` | `unicode_dealloc` | memory |
| 0.26% | `python` | `PyObject_IsInstance` | dynamic |
| 0.25% | `_json.cpython-316-aarch64-linux-gnu.so` | `PyUnicodeWriter_WriteStr@plt` | library |

## json_loads

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 12.68% | `_json.cpython-316-aarch64-linux-gnu.so` | `scanstring_unicode` | library |
| 7.64% | `_json.cpython-316-aarch64-linux-gnu.so` | `scan_once_unicode` | library |
| 6.40% | `python` | `_PyObject_Malloc` | memory |
| 5.95% | `python` | `PyUnicode_Substring` | str |
| 4.85% | `python` | `_PyObject_Free` | memory |
| 4.05% | `python` | `siphash13` | str |
| 4.04% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.95% | `python` | `_Py_dict_lookup` | lookup |
| 3.91% | `python` | `PyUnicode_New.part.0` | memory |
| 3.74% | `python` | `PyLong_FromString` | int |
| 3.71% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 3.59% | `python` | `insertdict` | dict |
| 2.47% | `python` | `_Py_Dealloc` | memory |
| 2.08% | `python` | `unicode_dealloc` | memory |
| 1.48% | `python` | `build_indices_unicode` | dict |
| 1.42% | `libc.so.6` | `__memcpy_generic` | libc |
| 1.38% | `python` | `_Py_NewReference` | memory |
| 1.34% | `python` | `PyObject_Malloc` | dynamic |
| 1.31% | `[JIT]` | `jit` | jit |
| 1.26% | `python` | `find_empty_slot` | dict |
| 1.25% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 1.18% | `python` | `_PyDict_SetItem_Take2` | dict |
| 1.09% | `python` | `PyObject_Free` | dynamic |
| 0.96% | `python` | `unicode_hash` | str |
| 0.95% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.85% | `_json.cpython-316-aarch64-linux-gnu.so` | `PyUnicode_Substring@plt` | library |
| 0.61% | `python` | `initialize_locals` | interpreter |
| 0.54% | `python` | `dictresize` | dict |
| 0.52% | `python` | `pysiphash` | unknown |
| 0.52% | `python` | `PyObject_Hash` | dynamic |
| 0.51% | `python` | `maybe_small_long` | unknown |
| 0.49% | `python` | `Py_HashBuffer` | unknown |
| 0.44% | `python` | `sre_ucs1_match` | library |
| 0.42% | `libc.so.6` | `__memset_zva64` | libc |
| 0.42% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.40% | `python` | `_sre_SRE_Pattern_prefixmatch` | library |
| 0.40% | `libc.so.6` | `malloc` | libc |
| 0.38% | `libc.so.6` | `memcmp` | libc |
| 0.36% | `libc.so.6` | `_int_malloc` | libc |
| 0.36% | `python` | `insert_to_emptydict` | dict |
| 0.36% | `python` | `PyDict_SetDefaultRef` | dict |
| 0.35% | `python` | `new_keys_object` | dict |
| 0.33% | `python` | `memcpy@plt` | memory |
| 0.33% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.31% | `python` | `PyDict_New` | memory |
| 0.31% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.31% | `python` | `PyDict_GetItemRef` | dict |
| 0.31% | `python` | `long_alloc` | memory |
| 0.30% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.26% | `python` | `long_dealloc` | memory |

## logging

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.78% | `[JIT]` | `jit` | jit |
| 12.69% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.45% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.88% | `python` | `initialize_locals` | interpreter |
| 2.75% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.35% | `python` | `_Py_dict_lookup` | lookup |
| 2.20% | `python` | `_PyObject_Malloc` | memory |
| 2.09% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.96% | `python` | `_Py_Dealloc` | memory |
| 1.92% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.91% | `python` | `_PyCode_CheckLineNumber` | interpreter |
| 1.89% | `python` | `_PyJIT_Entry` | compiler |
| 1.80% | `python` | `dict_dealloc` | memory |
| 1.52% | `python` | `_PyDict_Subscript` | dict |
| 1.40% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.40% | `python` | `_PyObject_Free` | memory |
| 1.39% | `python` | `PyDict_New` | memory |
| 1.26% | `python` | `_PyThreadState_PopFrame` | threading |
| 1.04% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.98% | `python` | `PyObject_GetItem` | dynamic |
| 0.79% | `[kernel.kallsyms]` | `el0_svc` | kernel |
| 0.71% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.69% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.66% | `python` | `_Py_NewReference` | memory |
| 0.65% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.60% | `python` | `_PyType_GetDict` | dynamic |
| 0.59% | `python` | `PyUnicode_Format` | str |
| 0.58% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.55% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.51% | `python` | `long_hash` | int |
| 0.49% | `libc.so.6` | `__getpid` | libc |
| 0.47% | `python` | `_PyLong_Frexp` | int |
| 0.47% | `python` | `PyObject_Hash` | dynamic |
| 0.45% | `python` | `PySys_Audit` | unknown |
| 0.43% | `python` | `PyUnicode_Contains` | str |
| 0.41% | `python` | `_PyUnicode_BinarySlice` | str |
| 0.37% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.36% | `python` | `any_find_slice` | unknown |
| 0.35% | `python` | `tuple_dealloc` | memory |
| 0.35% | `python` | `tuple_alloc` | memory |
| 0.33% | `python` | `PyUnicode_Splitlines` | str |
| 0.33% | `python` | `PyType_IsSubtype` | dynamic |
| 0.32% | `[kernel.kallsyms]` | `get_random_u16` | kernel |
| 0.30% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 0.29% | `python` | `PyUnicode_New.part.0` | memory |
| 0.28% | `python` | `PyObject_Malloc` | dynamic |
| 0.27% | `python` | `_PyLong_FromMedium` | int |
| 0.27% | `python` | `_PyEval_Vector` | interpreter |
| 0.26% | `python` | `frame_back_get` | unknown |
| 0.26% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.26% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.26% | `python` | `l_mod` | int |
| 0.25% | `python` | `_Py_BuiltinCallFastWithKeywords_StackRef` | unknown |

## mako

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.83% | `[JIT]` | `jit` | jit |
| 9.13% | `python` | `replace` | str |
| 6.44% | `python` | `long_to_decimal_string_internal` | int |
| 6.00% | `python` | `dequeiter_next` | miscobj |
| 5.15% | `python` | `_PyObject_Malloc` | memory |
| 4.81% | `python` | `_PyCallMethodDescriptorFastWithKeywords_StackRef` | unknown |
| 4.57% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 3.60% | `python` | `unicode_replace` | str |
| 3.22% | `python` | `deque_append` | miscobj |
| 2.79% | `python` | `_PyObject_Free` | memory |
| 2.03% | `libc.so.6` | `__memcpy_generic` | libc |
| 1.60% | `python` | `PyErr_CheckSignals` | exceptions |
| 1.53% | `python` | `PyUnicode_New` | memory |
| 1.52% | `python` | `list_dealloc` | memory |
| 1.37% | `python` | `PyObject_Malloc` | dynamic |
| 1.14% | `python` | `_list_extend` | list |
| 1.11% | `python` | `PyObject_Str` | dynamic |
| 1.11% | `python` | `_PyErr_CheckSignalsTstate` | exceptions |
| 1.06% | `python` | `_PyRunRemoteDebugger` | unknown |
| 1.00% | `python` | `deque_clear.part.0` | miscobj |
| 0.96% | `python` | `long_alloc` | memory |
| 0.93% | `python` | `_Py_IsMainThread` | unknown |
| 0.90% | `python` | `PyThread_get_thread_ident` | threading |
| 0.87% | `python` | `_Py_NewReference` | memory |
| 0.86% | `python` | `unicode_dealloc` | memory |
| 0.86% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.75% | `python` | `sre_search` | library |
| 0.74% | `python` | `long_to_decimal_string` | int |
| 0.72% | `python` | `PyObject_Free` | dynamic |
| 0.68% | `python` | `PyLong_FromLong` | int |
| 0.64% | `python` | `_Py_Dealloc` | memory |
| 0.62% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 0.56% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.49% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.47% | `python` | `_PyInterpreterState_Main` | unknown |
| 0.47% | `[kernel.kallsyms]` | `el0_da` | kernel |
| 0.46% | `[kernel.kallsyms]` | `__pi_clear_page` | kernel |
| 0.45% | `python` | `_PyInterpreterState_GetConfig` | unknown |
| 0.44% | `python` | `object_str` | dynamic |
| 0.31% | `python` | `memcpy@plt` | memory |

## mdp

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 18.56% | `[JIT]` | `jit` | jit |
| 13.36% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.67% | `python` | `_Py_dict_lookup` | lookup |
| 8.03% | `python` | `PyObject_RichCompareBool` | dynamic |
| 4.08% | `python` | `tuple_richcompare` | tuple |
| 2.75% | `python` | `_PyDict_Subscript` | dict |
| 2.00% | `python` | `_PyJIT_Entry` | compiler |
| 1.75% | `python` | `builtin_sum` | unknown |
| 1.61% | `python` | `_PyLong_GCD` | int |
| 1.53% | `python` | `gen_iternext` | miscobj |
| 1.43% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.38% | `python` | `PyDict_GetItemRef` | dict |
| 1.34% | `python` | `_PyObject_Free` | memory |
| 1.31% | `python` | `_PyObject_Malloc` | memory |
| 1.31% | `python` | `_Py_Dealloc` | memory |
| 1.05% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.04% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.03% | `python` | `PyObject_GetItem` | dynamic |
| 0.88% | `python` | `PyFloat_FromDouble` | float |
| 0.70% | `python` | `set_lookkey` | miscobj |
| 0.69% | `python` | `_PyDict_LoadBuiltinsFromGlobals` | dict |
| 0.66% | `python` | `_Py_NewReference` | memory |
| 0.66% | `python` | `tuple_hash` | tuple |
| 0.64% | `python` | `insertdict` | dict |
| 0.63% | `python` | `gen_dealloc` | memory |
| 0.59% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.59% | `python` | `PyObject_Hash` | dynamic |
| 0.57% | `python` | `tuple_dealloc` | memory |
| 0.53% | `python` | `func_clear` | unknown |
| 0.49% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.47% | `python` | `_PyCompactLong_Multiply` | unknown |
| 0.47% | `python` | `subtype_dealloc` | memory |
| 0.46% | `python` | `_PySuper_LookupDescr` | unknown |
| 0.43% | `python` | `PyIter_Next` | dynamic |
| 0.41% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.40% | `python` | `_Py_BuiltinCallFastWithKeywords_StackRef` | unknown |
| 0.39% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.38% | `python` | `PyObject_GC_Del` | gc |
| 0.37% | `python` | `initialize_locals` | interpreter |
| 0.36% | `python` | `PyLong_FromLong` | int |
| 0.36% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 0.36% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.35% | `python` | `tuple_alloc` | memory |
| 0.34% | `python` | `float_dealloc` | memory |
| 0.32% | `python` | `func_dealloc` | memory |
| 0.31% | `python` | `_PyObject_GC_Link` | gc |
| 0.31% | `python` | `long_div` | int |
| 0.31% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.30% | `python` | `PyNumber_Add` | dynamic |
| 0.30% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.29% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.27% | `python` | `min_max` | unknown |
| 0.27% | `python` | `_PyEval_Vector` | interpreter |
| 0.26% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.25% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 0.25% | `python` | `float_add` | float |
| 0.25% | `python` | `PyMethod_New` | memory |

## meteor_contest

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.60% | `[JIT]` | `jit` | jit |
| 10.92% | `python` | `set_lookkey` | miscobj |
| 10.32% | `python` | `set_issubset_impl` | miscobj |
| 7.83% | `python` | `setiter_iternext` | miscobj |
| 4.14% | `python` | `PyObject_RichCompareBool` | dynamic |
| 3.91% | `python` | `set_difference_untracked` | miscobj |
| 3.22% | `python` | `set_dealloc` | memory |
| 3.01% | `python` | `set_add_entry_takeref` | miscobj |
| 2.87% | `python` | `_PyObject_Malloc` | memory |
| 2.45% | `python` | `_PyObject_Free` | memory |
| 2.03% | `python` | `list_dealloc` | memory |
| 2.02% | `python` | `long_richcompare` | int |
| 1.95% | `python` | `list_slice_lock_held` | list |
| 1.67% | `python` | `PyObject_RichCompare` | dynamic |
| 1.47% | `python` | `min_max` | unknown |
| 1.34% | `python` | `_Py_Dealloc` | memory |
| 1.30% | `python` | `set_table_resize` | miscobj |
| 1.21% | `python` | `set_intersection` | miscobj |
| 1.10% | `python` | `set_richcompare` | miscobj |
| 1.07% | `python` | `PyIter_Next` | dynamic |
| 0.81% | `python` | `set_merge_lock_held` | miscobj |
| 0.73% | `python` | `PyObject_GC_Del` | gc |
| 0.70% | `python` | `PyList_New.constprop.0` | memory |
| 0.69% | `libc.so.6` | `__memset_zva64` | libc |
| 0.64% | `python` | `initialize_locals` | interpreter |
| 0.58% | `python` | `PyObject_IsTrue` | dynamic |
| 0.55% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.51% | `python` | `set_difference_update_internal` | miscobj |
| 0.50% | `python` | `_PyList_SliceSubscript` | list |
| 0.49% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.47% | `python` | `list_ass_slice_lock_held` | list |
| 0.46% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.45% | `python` | `PyMem_Free` | memory |
| 0.44% | `python` | `PyLong_FromSsize_t` | int |
| 0.43% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.42% | `python` | `PyObject_Size` | dynamic |
| 0.39% | `python` | `set_sub` | miscobj |
| 0.37% | `python` | `_PyObject_GC_New` | gc |
| 0.36% | `python` | `set_iter` | miscobj |
| 0.34% | `python` | `PySlice_Unpack` | miscobj |
| 0.34% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.32% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.31% | `python` | `setiter_dealloc` | memory |
| 0.31% | `python` | `_PyObject_GC_Link` | gc |
| 0.28% | `python` | `PyObject_Free` | dynamic |
| 0.27% | `python` | `_Py_NewReference` | memory |
| 0.27% | `python` | `list_remove` | list |
| 0.27% | `python` | `PyObject_Malloc` | dynamic |
| 0.26% | `python` | `list_slice_wrap` | list |

## nbody

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 56.05% | `[JIT]` | `jit` | jit |
| 11.74% | `python` | `PyFloat_FromDouble` | float |
| 7.81% | `libm.so.6` | `pow@@GLIBC_2.29` | library |
| 7.04% | `python` | `float_dealloc` | memory |
| 6.05% | `python` | `_Py_Dealloc` | memory |
| 4.23% | `python` | `_Py_NewReference` | memory |
| 3.41% | `python` | `float_pow` | float |
| 1.74% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.73% | `python` | `_PyNumber_PowerNoMod` | dynamic |
| 0.45% | `python` | `_PyEval_EvalFrameDefault` | interpreter |

## networkx

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.67% | `python` | `set_lookkey` | miscobj |
| 19.88% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 16.86% | `python` | `dictiter_iternextkey` | dict |
| 11.11% | `[JIT]` | `jit` | jit |
| 2.77% | `python` | `_PyDict_Subscript` | dict |
| 1.41% | `python` | `unicode_hash` | str |
| 1.26% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.26% | `python` | `_PySet_Contains` | miscobj |
| 1.23% | `libc.so.6` | `memcmp` | libc |
| 1.18% | `python` | `build_indices_unicode` | dict |
| 0.93% | `python` | `set_dealloc` | memory |
| 0.79% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.72% | `python` | `PyObject_Hash` | dynamic |
| 0.66% | `python` | `_Py_dict_lookup` | lookup |
| 0.62% | `python` | `list_dealloc` | memory |
| 0.60% | `python` | `deque_clear.part.0` | miscobj |
| 0.57% | `python` | `_PyObject_Free` | memory |
| 0.53% | `python` | `insertdict` | dict |
| 0.48% | `python` | `set_table_resize` | miscobj |
| 0.43% | `python` | `_Py_Dealloc` | memory |
| 0.39% | `python` | `tuple_dealloc` | memory |
| 0.36% | `python` | `set_add_entry_takeref` | miscobj |
| 0.32% | `python` | `merge_from_seq2_lock_held` | unknown |
| 0.31% | `python` | `_PyJIT_Entry` | compiler |
| 0.29% | `python` | `PyObject_GetItem` | dynamic |
| 0.28% | `python` | `tuple_alloc` | memory |
| 0.28% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.28% | `python` | `gen_iternext` | miscobj |

## networkx_connected_components

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.94% | `python` | `set_lookkey` | miscobj |
| 17.70% | `python` | `dictiter_iternextkey` | dict |
| 13.96% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 12.27% | `[JIT]` | `jit` | jit |
| 3.22% | `python` | `_PyDict_Subscript` | dict |
| 1.97% | `python` | `set_dealloc` | memory |
| 1.70% | `python` | `_PySet_Contains` | miscobj |
| 1.67% | `python` | `unicode_hash` | str |
| 1.54% | `libc.so.6` | `memcmp` | libc |
| 1.08% | `python` | `set_merge_lock_held` | miscobj |
| 0.81% | `python` | `PyObject_Hash` | dynamic |
| 0.67% | `python` | `list_dealloc` | memory |
| 0.59% | `python` | `_PyObject_Free` | memory |
| 0.52% | `python` | `set_table_resize` | miscobj |
| 0.39% | `python` | `_Py_dict_lookup` | lookup |
| 0.39% | `python` | `set_add_entry_takeref` | miscobj |
| 0.29% | `python` | `PyObject_GetItem` | dynamic |
| 0.28% | `python` | `set_add` | miscobj |
| 0.27% | `python` | `dict_iter` | dict |
| 0.27% | `python` | `_Py_Dealloc` | memory |
| 0.26% | `python` | `_PyObject_GC_New` | gc |

## networkx_k_core

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 30.98% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 17.80% | `[JIT]` | `jit` | jit |
| 8.73% | `python` | `list_remove` | list |
| 6.29% | `python` | `_PyDict_Subscript` | dict |
| 3.54% | `python` | `dictiter_iternextkey` | dict |
| 3.48% | `python` | `_Py_dict_lookup` | lookup |
| 2.75% | `python` | `visit_reachable` | gc |
| 2.48% | `python` | `visit_decref` | gc |
| 2.35% | `python` | `gc_collect_main` | gc |
| 1.46% | `python` | `PyUnicode_RichCompare` | str |
| 1.45% | `python` | `dict_traverse` | gc |
| 1.33% | `python` | `insertdict` | dict |
| 1.29% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.11% | `python` | `PyObject_GetItem` | dynamic |
| 1.11% | `python` | `listiter_next` | list |
| 0.92% | `libc.so.6` | `memcmp` | libc |
| 0.81% | `python` | `list_dealloc` | memory |
| 0.60% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.51% | `python` | `_PyObject_Malloc` | memory |
| 0.47% | `python` | `build_indices_unicode` | dict |
| 0.47% | `python` | `list_traverse` | gc |
| 0.46% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.46% | `python` | `list_ass_slice_lock_held` | list |
| 0.38% | `python` | `_PyDict_StoreSubscript` | dict |
| 0.37% | `python` | `dict_get` | dict |
| 0.34% | `python` | `_Py_Dealloc` | memory |
| 0.33% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.27% | `python` | `list_sort_impl` | list |

## nqueens

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 36.81% | `[JIT]` | `jit` | jit |
| 4.27% | `python` | `_PyObject_Malloc` | memory |
| 3.46% | `python` | `_PyObject_Free` | memory |
| 3.30% | `python` | `_Py_Dealloc` | memory |
| 2.38% | `python` | `set_add_entry_takeref` | miscobj |
| 2.23% | `python` | `PyList_New.constprop.0` | memory |
| 1.91% | `python` | `_PyCompactLong_Add` | unknown |
| 1.71% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.39% | `python` | `list_dealloc` | memory |
| 1.29% | `python` | `PyFunction_NewWithQualName` | memory |
| 1.26% | `python` | `_PyDict_LoadBuiltinsFromGlobals` | dict |
| 1.25% | `python` | `_PyList_BinarySlice` | list |
| 1.25% | `python` | `_PyEval_SliceIndex` | interpreter |
| 1.23% | `python` | `set_table_resize` | miscobj |
| 1.20% | `python` | `PyLong_FromLong` | int |
| 1.17% | `python` | `set_dealloc` | memory |
| 1.13% | `python` | `gen_dealloc` | memory |
| 1.02% | `python` | `_Py_NewReference` | memory |
| 0.99% | `python` | `list_ass_subscript` | list |
| 0.98% | `python` | `tuple_dealloc` | memory |
| 0.91% | `python` | `list_slice_lock_held` | list |
| 0.86% | `python` | `tuple_alloc` | memory |
| 0.86% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.84% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.82% | `python` | `list_ass_slice_lock_held` | list |
| 0.79% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.79% | `python` | `_PyCompactLong_Subtract` | unknown |
| 0.76% | `python` | `func_clear` | unknown |
| 0.71% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.68% | `python` | `PyMem_Free` | memory |
| 0.61% | `python` | `make_range_object` | unknown |
| 0.61% | `python` | `PyObject_GC_Del` | gc |
| 0.60% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.59% | `python` | `func_dealloc` | memory |
| 0.55% | `python` | `make_gen` | miscobj |
| 0.54% | `python` | `PyObject_Hash` | dynamic |
| 0.54% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.54% | `python` | `PyDict_GetItemRef` | dict |
| 0.53% | `python` | `PyLong_AsLong` | int |
| 0.53% | `python` | `_PyObject_GC_Link` | gc |
| 0.52% | `python` | `long_hash` | int |
| 0.51% | `python` | `_Py_dict_lookup` | lookup |
| 0.51% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.50% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 0.50% | `python` | `_PySet_AddTakeRef` | miscobj |
| 0.47% | `python` | `range_dealloc` | memory |
| 0.46% | `python` | `_PyList_Concat` | list |
| 0.43% | `python` | `_PyObject_Realloc` | memory |
| 0.42% | `python` | `PySet_New` | memory |
| 0.41% | `python` | `PyCMethod_New` | memory |
| 0.41% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.40% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.40% | `python` | `_Py_CallBuiltinClass_StackRef` | unknown |
| 0.39% | `libc.so.6` | `__memset_zva64` | libc |
| 0.39% | `python` | `_PyTuple_FromArraySteal` | tuple |
| 0.39% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.38% | `python` | `PyMem_Malloc` | memory |
| 0.33% | `python` | `_PyObject_GC_New` | gc |
| 0.33% | `python` | `PyObject_SetItem` | dynamic |
| 0.32% | `python` | `PyObject_Malloc` | dynamic |
| 0.31% | `python` | `_PyList_AppendTakeRefListResize` | list |
| 0.31% | `python` | `range_reverse` | miscobj |
| 0.31% | `python` | `list_subscript` | list |
| 0.30% | `python` | `reversed_new_impl` | memory |
| 0.30% | `python` | `rangeiter_dealloc` | memory |
| 0.30% | `python` | `long_neg_method` | int |
| 0.30% | `python` | `PySequence_Fast` | dynamic |
| 0.29% | `python` | `slice_dealloc` | memory |
| 0.29% | `python` | `range_iter` | miscobj |
| 0.28% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.27% | `python` | `PySlice_Unpack` | miscobj |
| 0.27% | `python` | `_PyStaticType_GetState` | unknown |

## pathlib

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 6.05% | `[JIT]` | `jit` | jit |
| 3.61% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.53% | `python` | `_PyObject_Malloc` | memory |
| 2.97% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 2.76% | `python` | `_PyObject_Free` | memory |
| 2.06% | `[kernel.kallsyms]` | `el0_svc` | kernel |
| 1.93% | `[kernel.kallsyms]` | `__update_cpu_freelist_fast` | kernel |
| 1.87% | `python` | `_Py_Dealloc` | memory |
| 1.56% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.45% | `[kernel.kallsyms]` | `half_md4_transform.isra.0` | kernel |
| 1.37% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.34% | `[kernel.kallsyms]` | `memset` | kernel |
| 1.32% | `libc.so.6` | `__GI___fstatat64` | libc |
| 1.21% | `[kernel.kallsyms]` | `security_inode_getattr` | kernel |
| 1.15% | `python` | `initialize_locals` | interpreter |
| 1.08% | `[kernel.kallsyms]` | `kmem_cache_alloc` | kernel |
| 1.04% | `libc.so.6` | `pthread_mutex_lock@@GLIBC_2.17` | libc |
| 1.02% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.89% | `python` | `PyLong_FromLongLong` | int |
| 0.85% | `python` | `take_gil` | gil |
| 0.85% | `python` | `ScandirIterator_iternext` | unknown |
| 0.80% | `[kernel.kallsyms]` | `link_path_walk.part.0.constprop.0` | kernel |
| 0.79% | `[kernel.kallsyms]` | `apparmor_inode_getattr` | kernel |
| 0.77% | `python` | `_Py_NewReference` | memory |
| 0.77% | `[kernel.kallsyms]` | `get_random_u16` | kernel |
| 0.77% | `python` | `__aarch64_cas1_acq_rel` | unknown |
| 0.73% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.72% | `python` | `clear_slots` | unknown |
| 0.71% | `[kernel.kallsyms]` | `memblock_is_map_memory` | kernel |
| 0.69% | `python` | `tuple_dealloc` | memory |
| 0.67% | `python` | `_PyJIT_Entry` | compiler |
| 0.66% | `libc.so.6` | `__GI___pthread_mutex_unlock_usercnt` | libc |
| 0.66% | `python` | `_PyEval_Vector` | interpreter |
| 0.65% | `[kernel.kallsyms]` | `filldir64` | kernel |
| 0.64% | `python` | `structseq_dealloc` | memory |
| 0.61% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.59% | `python` | `long_dealloc` | memory |
| 0.59% | `python` | `_PyLong_FromMedium` | int |
| 0.58% | `[kernel.kallsyms]` | `ext4_getattr` | kernel |
| 0.57% | `libc.so.6` | `_int_malloc` | libc |
| 0.57% | `python` | `__aarch64_ldclr8_acq_rel` | unknown |
| 0.56% | `python` | `PyObject_Free` | dynamic |
| 0.55% | `python` | `sre_ucs1_match` | library |
| 0.54% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.53% | `[kernel.kallsyms]` | `ext4_htree_store_dirent` | kernel |
| 0.52% | `[kernel.kallsyms]` | `__kmalloc` | kernel |
| 0.52% | `[kernel.kallsyms]` | `__legitimize_mnt` | kernel |
| 0.50% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.49% | `[kernel.kallsyms]` | `step_into` | kernel |
| 0.49% | `python` | `tuple_alloc` | memory |
| 0.48% | `python` | `PyStructSequence_SetItem` | unknown |
| 0.48% | `[kernel.kallsyms]` | `slab_update_freelist.isra.0` | kernel |
| 0.47% | `[kernel.kallsyms]` | `__ext4fs_dirhash` | kernel |
| 0.45% | `python` | `path_converter` | unknown |
| 0.45% | `python` | `PyObject_Malloc` | dynamic |
| 0.45% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.44% | `python` | `fill_time` | unknown |
| 0.43% | `python` | `_PyType_GetDict` | dynamic |
| 0.43% | `python` | `_Py_dict_lookup` | lookup |
| 0.42% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.41% | `libc.so.6` | `pthread_cond_signal@@GLIBC_2.17` | libc |
| 0.41% | `python` | `os_stat` | unknown |
| 0.40% | `[kernel.kallsyms]` | `make_vfsuid` | kernel |
| 0.40% | `python` | `PyDict_GetItemWithError` | dict |
| 0.40% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.39% | `python` | `_PyMember_GetOffset` | unknown |
| 0.39% | `python` | `float_dealloc` | memory |
| 0.39% | `python` | `DirEntry_dealloc` | memory |
| 0.39% | `[kernel.kallsyms]` | `common_perm_cond` | kernel |
| 0.38% | `python` | `subtype_dealloc` | memory |
| 0.38% | `python` | `_PyThreadState_Attach` | threading |
| 0.38% | `[kernel.kallsyms]` | `mntput_no_expire` | kernel |
| 0.38% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.38% | `[kernel.kallsyms]` | `__check_heap_object` | kernel |
| 0.37% | `[kernel.kallsyms]` | `call_filldir` | kernel |
| 0.37% | `[kernel.kallsyms]` | `generic_permission` | kernel |
| 0.37% | `libc.so.6` | `__strlen_asimd` | libc |
| 0.36% | `python` | `posix_do_stat.isra.0` | unknown |
| 0.36% | `libc.so.6` | `pthread_mutex_unlock@@GLIBC_2.17` | libc |
| 0.35% | `[kernel.kallsyms]` | `str2hashbuf_unsigned` | kernel |
| 0.34% | `libc.so.6` | `__aarch64_cas4_acq` | libc |
| 0.34% | `[kernel.kallsyms]` | `__ext4_check_dir_entry` | kernel |
| 0.34% | `[kernel.kallsyms]` | `__slab_free` | kernel |
| 0.34% | `[kernel.kallsyms]` | `strncpy_from_user` | kernel |
| 0.33% | `[kernel.kallsyms]` | `check_heap_object` | kernel |
| 0.33% | `[kernel.kallsyms]` | `__check_object_size.part.0` | kernel |
| 0.32% | `python` | `tp_new_wrapper` | memory |
| 0.32% | `[kernel.kallsyms]` | `putname` | kernel |
| 0.32% | `[kernel.kallsyms]` | `map_id_up` | kernel |
| 0.32% | `python` | `PyUnicode_New.part.0` | memory |
| 0.31% | `[kernel.kallsyms]` | `generic_fillattr` | kernel |
| 0.30% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.30% | `[kernel.kallsyms]` | `lockref_get_not_dead` | kernel |
| 0.30% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.30% | `[kernel.kallsyms]` | `set_root` | kernel |
| 0.30% | `python` | `PyLong_AsSsize_t` | int |
| 0.30% | `libc.so.6` | `__aarch64_swp4_rel` | libc |
| 0.29% | `[kernel.kallsyms]` | `getname_flags.part.0` | kernel |
| 0.29% | `python` | `drop_gil` | gil |
| 0.29% | `python` | `_pystat_fromstructstat` | unknown |
| 0.29% | `python` | `PyObject_GC_Del` | gc |
| 0.29% | `python` | `_sre_SRE_Pattern_prefixmatch` | library |
| 0.29% | `python` | `list_dealloc` | memory |
| 0.28% | `python` | `PyMethod_New` | memory |
| 0.28% | `python` | `_PyObject_Call_Prepend` | dynamic |
| 0.28% | `python` | `slot_tp_init` | unknown |
| 0.27% | `[kernel.kallsyms]` | `ext4_file_getattr` | kernel |
| 0.27% | `[kernel.kallsyms]` | `kfree` | kernel |
| 0.27% | `python` | `_PyObject_GC_Link` | gc |
| 0.27% | `[kernel.kallsyms]` | `vfs_getattr_nosec` | kernel |
| 0.26% | `[kernel.kallsyms]` | `lookup_fast` | kernel |
| 0.26% | `python` | `PyList_New.constprop.0` | memory |
| 0.25% | `[kernel.kallsyms]` | `__arch_copy_to_user` | kernel |
| 0.25% | `libc.so.6` | `__errno_location` | libc |
| 0.25% | `python` | `_Py_BuiltinCallFastWithKeywords_StackRef` | unknown |
| 0.25% | `[kernel.kallsyms]` | `filename_lookup` | kernel |

## pickle_pure_python

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 27.99% | `[JIT]` | `jit` | jit |
| 5.34% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.98% | `python` | `_PyObject_Malloc` | memory |
| 3.52% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 3.29% | `python` | `_Py_dict_lookup` | lookup |
| 3.17% | `python` | `_PyObject_Free` | memory |
| 2.58% | `python` | `initialize_locals` | interpreter |
| 2.46% | `python` | `PySys_Audit` | unknown |
| 1.98% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.85% | `python` | `tuple_dealloc` | memory |
| 1.51% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.42% | `python` | `PyBuffer_FillInfo` | miscobj |
| 1.32% | `python` | `_Py_Dealloc` | memory |
| 1.29% | `python` | `_PyTuple_Resize` | tuple |
| 1.29% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 1.24% | `python` | `PyObject_GetBuffer` | dynamic |
| 1.18% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 1.09% | `python` | `dict_get` | dict |
| 1.07% | `_struct.cpython-316-aarch64-linux-gnu.so` | `pack` | library |
| 1.06% | `python` | `PyBuffer_Release` | miscobj |
| 1.01% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.88% | `python` | `PyLong_FromSsize_t` | int |
| 0.86% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.86% | `python` | `_PyBytes_Concat` | unknown |
| 0.84% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.84% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.79% | `python` | `PyObject_Free` | dynamic |
| 0.79% | `python` | `write_bytes_lock_held` | unknown |
| 0.77% | `_struct.cpython-316-aarch64-linux-gnu.so` | `s_pack_internal` | library |
| 0.75% | `python` | `tuple_alloc` | memory |
| 0.74% | `python` | `PyBytesWriter_FinishWithSize` | unknown |
| 0.74% | `python` | `PyLong_FromVoidPtr` | int |
| 0.74% | `python` | `PyUnicode_AsEncodedString` | str |
| 0.71% | `python` | `_Py_NewReference` | memory |
| 0.68% | `python` | `PyObject_Malloc` | dynamic |
| 0.68% | `python` | `PyObject_Hash` | dynamic |
| 0.64% | `python` | `PyDict_GetItemRef` | dict |
| 0.64% | `python` | `sys_audit_tstate` | unknown |
| 0.59% | `python` | `insertdict` | dict |
| 0.59% | `python` | `bytes_buffer_getbuffer` | str |
| 0.57% | `python` | `long_hash` | int |
| 0.51% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.49% | `python` | `unicode_encode` | str |
| 0.47% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.46% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.44% | `python` | `_PyJIT_Entry` | compiler |
| 0.40% | `python` | `PyBytes_FromStringAndSize.constprop.0` | str |
| 0.40% | `python` | `_PyLong_FromMedium` | int |
| 0.39% | `python` | `PyBytesWriter_Create` | unknown |
| 0.38% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.37% | `libc.so.6` | `__memset_zva64` | libc |
| 0.35% | `python` | `PyUnicode_AsUTF8AndSize` | str |
| 0.34% | `python` | `long_dealloc` | memory |
| 0.33% | `python` | `PyObject_Size` | dynamic |
| 0.33% | `python` | `builtin_id` | unknown |
| 0.33% | `python` | `object_dealloc` | memory |
| 0.31% | `python` | `_PyCallMethodDescriptorFastWithKeywords_StackRef` | unknown |
| 0.31% | `python` | `PyErr_Occurred` | exceptions |
| 0.31% | `python` | `builtin_getattr` | lookup |
| 0.27% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.25% | `python` | `_PyObject_Realloc` | memory |

## pidigits

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 43.11% | `python` | `x_divrem` | int |
| 28.00% | `python` | `k_mul` | int |
| 14.99% | `python` | `x_add` | int |
| 5.88% | `python` | `x_sub` | int |
| 1.28% | `libc.so.6` | `_int_malloc` | libc |
| 0.83% | `[JIT]` | `jit` | jit |
| 0.74% | `libc.so.6` | `__memset_zva64` | libc |
| 0.34% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.31% | `libc.so.6` | `malloc` | libc |
| 0.29% | `python` | `_PyObject_Free` | memory |

## pprint

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 24.46% | `[JIT]` | `jit` | jit |
| 4.28% | `python` | `_PyObject_Malloc` | memory |
| 3.67% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 3.52% | `python` | `_PyTypeCache_Lookup` | unknown |
| 3.48% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 2.91% | `python` | `_PyObject_Free` | memory |
| 1.77% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 1.72% | `python` | `PyUnicode_Format` | str |
| 1.71% | `python` | `long_to_decimal_string_internal` | int |
| 1.59% | `python` | `_Py_type_getattro_stackref` | unknown |
| 1.59% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.50% | `python` | `_Py_Dealloc` | memory |
| 1.41% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.38% | `python` | `_PyStolenTuple_Free` | unknown |
| 1.25% | `python` | `tuple_alloc` | memory |
| 1.21% | `python` | `_Py_dict_lookup` | lookup |
| 1.12% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.97% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.94% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.91% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.88% | `python` | `set_lookkey` | miscobj |
| 0.87% | `python` | `_Py_NewReference` | memory |
| 0.83% | `python` | `PyObject_IsSubclass` | dynamic |
| 0.82% | `python` | `unicode_dealloc` | memory |
| 0.81% | `python` | `PyUnicode_New` | memory |
| 0.81% | `python` | `PyErr_CheckSignals` | exceptions |
| 0.78% | `python` | `PyObject_Malloc` | dynamic |
| 0.77% | `python` | `tuple_dealloc` | memory |
| 0.74% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.68% | `python` | `_PyStaticType_GetState` | unknown |
| 0.67% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.65% | `python` | `_PyObject_Realloc` | memory |
| 0.64% | `python` | `_PyErr_CheckSignalsTstate` | exceptions |
| 0.61% | `python` | `initialize_locals` | interpreter |
| 0.59% | `python` | `PyThread_get_thread_ident` | threading |
| 0.59% | `python` | `list_append` | list |
| 0.57% | `python` | `list_sort_impl` | list |
| 0.56% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.55% | `python` | `PyType_IsSubtype` | dynamic |
| 0.53% | `python` | `PySys_Audit` | unknown |
| 0.50% | `python` | `PyObject_Free` | dynamic |
| 0.50% | `python` | `PyCMethod_New` | memory |
| 0.49% | `python` | `PyList_New.constprop.0` | memory |
| 0.49% | `python` | `_PySet_Contains` | miscobj |
| 0.48% | `python` | `insertdict` | dict |
| 0.47% | `python` | `recursive_issubclass` | unknown |
| 0.46% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 0.46% | `python` | `_copy_characters.constprop.0.isra.0` | str |
| 0.45% | `python` | `_PyRunRemoteDebugger` | unknown |
| 0.44% | `python` | `delitem_common` | dynamic |
| 0.43% | `python` | `PyObject_Repr` | dynamic |
| 0.43% | `python` | `builtin_issubclass` | unknown |
| 0.42% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.41% | `python` | `PyObject_Hash` | dynamic |
| 0.41% | `python` | `_PyUnicode_ResizeCompact` | str |
| 0.40% | `python` | `PyUnicode_New.part.0` | memory |
| 0.38% | `python` | `_Py_IsMainThread` | unknown |
| 0.38% | `python` | `_PyUnicodeWriter_WriteSubstring` | str |
| 0.38% | `python` | `unicode_repr` | str |
| 0.37% | `python` | `builtin_getattr` | lookup |
| 0.36% | `python` | `list_dealloc` | memory |
| 0.35% | `python` | `long_hash` | int |
| 0.33% | `python` | `_Py_BuildString_StackRefSteal` | unknown |
| 0.33% | `python` | `PyBool_FromLong` | miscobj |
| 0.33% | `python` | `_PyJIT_Entry` | compiler |
| 0.30% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.30% | `python` | `subtype_dealloc` | memory |
| 0.30% | `python` | `PyObject_DelItem` | dynamic |
| 0.30% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.28% | `python` | `_PyDict_StoreSubscript` | dict |
| 0.28% | `python` | `slot_tp_richcompare` | dynamic |
| 0.27% | `python` | `_PyEval_Vector` | interpreter |
| 0.27% | `python` | `_PyInterpreterState_Main` | unknown |
| 0.26% | `python` | `meth_dealloc` | memory |

## pycparser

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 19.84% | `[JIT]` | `jit` | jit |
| 11.34% | `python` | `sre_ucs1_match` | library |
| 7.69% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.84% | `python` | `gc_collect_main` | gc |
| 2.50% | `python` | `_PyObject_Malloc` | memory |
| 2.23% | `python` | `_Py_dict_lookup` | lookup |
| 2.10% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.69% | `python` | `_PyObject_Free` | memory |
| 1.51% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.44% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.17% | `python` | `_PyDict_Subscript` | dict |
| 1.17% | `python` | `visit_decref` | gc |
| 1.10% | `python` | `_Py_Dealloc` | memory |
| 1.05% | `python` | `list_ass_slice_lock_held` | list |
| 1.03% | `python` | `initialize_locals` | interpreter |
| 1.02% | `libc.so.6` | `_int_malloc` | libc |
| 0.97% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.94% | `python` | `_PyJIT_Entry` | compiler |
| 0.88% | `python` | `subtype_traverse` | gc |
| 0.87% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.81% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.75% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.74% | `python` | `visit_reachable` | gc |
| 0.69% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.68% | `python` | `_sre_SRE_Pattern_prefixmatch` | library |
| 0.68% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.68% | `python` | `PySlice_New` | memory |
| 0.65% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.64% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.62% | `python` | `dict_get` | dict |
| 0.61% | `python` | `PyObject_GetItem` | dynamic |
| 0.59% | `libc.so.6` | `malloc` | libc |
| 0.57% | `python` | `pattern_new_match` | memory |
| 0.54% | `python` | `sre_ucs1_count` | library |
| 0.54% | `python` | `list_ass_subscript` | list |
| 0.50% | `python` | `_PyEval_Vector` | interpreter |
| 0.49% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.47% | `python` | `subtype_dealloc` | memory |
| 0.46% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.43% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.40% | `python` | `_PyEval_SliceIndex` | interpreter |
| 0.39% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.39% | `python` | `long_neg_method` | int |
| 0.39% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.38% | `python` | `PyList_New.constprop.0` | memory |
| 0.38% | `python` | `PyType_IsSubtype` | dynamic |
| 0.37% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.36% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.36% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.35% | `python` | `_PyType_GetDict` | dynamic |
| 0.35% | `python` | `PyErr_Occurred` | exceptions |
| 0.35% | `python` | `list_resize` | list |
| 0.34% | `python` | `PyNumber_Negative` | dynamic |
| 0.34% | `python` | `list_subscript` | list |
| 0.33% | `libc.so.6` | `_int_free` | libc |
| 0.32% | `python` | `slice_dealloc` | memory |
| 0.32% | `python` | `PyObject_GC_Del` | gc |
| 0.32% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.31% | `python` | `_PyMember_GetOffset` | unknown |
| 0.29% | `python` | `slot_mp_ass_subscript` | unknown |
| 0.29% | `python` | `object_isinstance` | dynamic |
| 0.29% | `python` | `list_dealloc` | memory |
| 0.28% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.28% | `python` | `insertdict` | dict |
| 0.28% | `python` | `type_call` | dynamic |
| 0.28% | `python` | `PyType_GenericAlloc` | memory |
| 0.27% | `python` | `PyObject_DelItem` | dynamic |
| 0.27% | `python` | `_Py_NewReference` | memory |
| 0.27% | `libc.so.6` | `cfree@GLIBC_2.17` | libc |
| 0.25% | `python` | `PyUnicode_Contains` | str |
| 0.25% | `libc.so.6` | `_int_free_merge_chunk` | libc |

## pyflate

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 34.83% | `[JIT]` | `jit` | jit |
| 6.90% | `python` | `list_dealloc` | memory |
| 6.05% | `python` | `list_ass_slice_lock_held` | list |
| 3.63% | `python` | `_PyList_Concat` | list |
| 2.39% | `python` | `list_slice_lock_held` | list |
| 1.97% | `python` | `_PyCompactLong_Add` | unknown |
| 1.80% | `python` | `_PyCompactLong_Subtract` | unknown |
| 1.63% | `python` | `_Py_Dealloc` | memory |
| 1.57% | `libc.so.6` | `_int_malloc` | libc |
| 1.54% | `python` | `_PyObject_Malloc` | memory |
| 1.52% | `python` | `bytes_subscript` | str |
| 1.52% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.50% | `python` | `_PyObject_Free` | memory |
| 1.38% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.32% | `python` | `PyLong_AsNativeBytes.constprop.0` | int |
| 1.21% | `python` | `_PyLong_FromMedium` | int |
| 1.21% | `python` | `long_dealloc` | memory |
| 1.20% | `python` | `long_lshift_method` | int |
| 1.11% | `libc.so.6` | `__memcpy_generic` | libc |
| 1.09% | `python` | `_Py_NewReference` | memory |
| 0.97% | `python` | `PyLong_AsSsize_t` | int |
| 0.95% | `python` | `unsafe_long_compare` | unknown |
| 0.89% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.87% | `python` | `PyObject_GetItem` | dynamic |
| 0.87% | `python` | `PyLong_FromSsize_t` | int |
| 0.86% | `python` | `PyList_New.constprop.0` | memory |
| 0.85% | `python` | `list_sort_impl` | list |
| 0.83% | `python` | `_PyLong_ExactDealloc` | memory |
| 0.79% | `python` | `_PyEval_SliceIndex` | interpreter |
| 0.79% | `python` | `long_lshift1` | int |
| 0.73% | `python` | `PyNumber_Lshift` | dynamic |
| 0.72% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.70% | `python` | `stringlib_bytes_join` | str |
| 0.63% | `python` | `long_rshift` | int |
| 0.55% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.52% | `python` | `PySlice_New` | memory |
| 0.50% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.47% | `libc.so.6` | `__memchr_generic` | libc |
| 0.45% | `python` | `_PyList_BinarySlice` | list |
| 0.44% | `libc.so.6` | `malloc` | libc |
| 0.40% | `python` | `PyNumber_Rshift` | dynamic |
| 0.40% | `python` | `PyBuffer_Release` | miscobj |
| 0.39% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.37% | `python` | `enum_next` | miscobj |
| 0.36% | `python` | `compactlongs_and` | unknown |
| 0.36% | `python` | `long_rshift1` | int |
| 0.35% | `libc.so.6` | `unlink_chunk.isra.0` | libc |
| 0.35% | `python` | `PyMem_Free` | memory |
| 0.34% | `python` | `slice_dealloc` | memory |
| 0.33% | `python` | `compactlongs_guard` | unknown |
| 0.32% | `libc.so.6` | `_int_free_merge_chunk` | libc |
| 0.29% | `libc.so.6` | `_int_free` | libc |
| 0.29% | `python` | `PySlice_Unpack` | miscobj |
| 0.29% | `python` | `list_ass_subscript` | list |
| 0.26% | `python` | `striter_next` | unknown |
| 0.26% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.25% | `libc.so.6` | `cfree@GLIBC_2.17` | libc |
| 0.25% | `libc.so.6` | `_int_free_create_chunk` | libc |

## pylint

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 16.98% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.61% | `[JIT]` | `jit` | jit |
| 4.26% | `python` | `gc_collect_main` | gc |
| 2.92% | `python` | `_PyObject_Malloc` | memory |
| 2.43% | `python` | `_PyTypeCache_Lookup` | unknown |
| 2.24% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.86% | `python` | `_Py_dict_lookup` | lookup |
| 1.79% | `python` | `visit_reachable` | gc |
| 1.65% | `python` | `visit_decref` | gc |
| 1.60% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.53% | `python` | `_PyObject_Free` | memory |
| 1.52% | `python` | `initialize_locals` | interpreter |
| 1.48% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.10% | `python` | `_Py_Dealloc` | memory |
| 0.94% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.90% | `python` | `_PyPegen_expect_token` | interpreter |
| 0.83% | `python` | `PyDict_GetItemRef` | dict |
| 0.78% | `python` | `insertdict` | dict |
| 0.76% | `python` | `tuple_dealloc` | memory |
| 0.76% | `python` | `islice_next` | unknown |
| 0.74% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.71% | `python` | `dict_traverse` | gc |
| 0.70% | `python` | `listiter_next` | list |
| 0.68% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.66% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.65% | `python` | `_PyLexer_get_normal` | unknown |
| 0.63% | `python` | `_PyJIT_Entry` | compiler |
| 0.62% | `python` | `PyType_IsSubtype` | dynamic |
| 0.61% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.59% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.55% | `python` | `partial_vectorcall` | unknown |
| 0.54% | `python` | `subtype_traverse` | gc |
| 0.53% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 0.51% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.50% | `python` | `tuple_alloc` | memory |
| 0.49% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.49% | `python` | `_PyEval_Vector` | interpreter |
| 0.48% | `python` | `_PyPegen_is_memoized` | interpreter |
| 0.48% | `python` | `unicode_repr` | str |
| 0.41% | `python` | `_Py_NewReference` | memory |
| 0.40% | `python` | `PyObject_SetAttr` | dynamic |
| 0.39% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.38% | `python` | `_PyType_GetDict` | dynamic |
| 0.37% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.37% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.36% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.35% | `python` | `sre_ucs1_match` | library |
| 0.34% | `python` | `list_traverse` | gc |
| 0.32% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.31% | `python` | `tupleiter_next` | tuple |
| 0.30% | `python` | `PyObject_Malloc` | dynamic |
| 0.30% | `python` | `PyObject_GC_Del` | gc |
| 0.30% | `python` | `do_mkvalue` | unknown |
| 0.30% | `python` | `PyDict_Next` | dict |
| 0.29% | `python` | `_PyObject_GC_New` | gc |
| 0.29% | `python` | `object_isinstance` | dynamic |
| 0.27% | `python` | `gen_dealloc` | memory |
| 0.26% | `python` | `_PyObject_GC_Link` | gc |
| 0.25% | `python` | `_PyUnicode_InternMortal` | str |
| 0.25% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |

## python_startup

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 6.55% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.50% | `python` | `gc_collect_main` | gc |
| 4.35% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.03% | `python` | `visit_decref` | gc |
| 2.81% | `python` | `_Py_dict_lookup` | lookup |
| 2.80% | `python` | `_PyObject_Malloc` | memory |
| 2.49% | `python` | `visit_reachable` | gc |
| 1.68% | `python` | `r_object` | import |
| 1.53% | `python` | `_PyObject_Free` | memory |
| 1.45% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 1.36% | `python` | `find_name_in_mro` | lookup |
| 1.23% | `python` | `type_ready` | dynamic |
| 1.17% | `python` | `dict_traverse` | gc |
| 1.17% | `python` | `_PyCode_Quicken` | interpreter |
| 1.04% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.96% | `python` | `_Py_Dealloc` | memory |
| 0.96% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.93% | `python` | `_PyUnicode_FromUCS1.part.0` | str |
| 0.85% | `python` | `siphash13` | str |
| 0.77% | `python` | `_Py_dict_lookup_threadsafe_stackref` | lookup |
| 0.77% | `python` | `insertdict` | dict |
| 0.71% | `python` | `tuple_dealloc` | memory |
| 0.68% | `python` | `update_one_slot` | lookup |
| 0.67% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.66% | `[kernel.kallsyms]` | `el0_da` | kernel |
| 0.66% | `[kernel.kallsyms]` | `perf_iterate_ctx` | kernel |
| 0.64% | `[kernel.kallsyms]` | `__pi_clear_page` | kernel |
| 0.60% | `[kernel.kallsyms]` | `next_uptodate_folio` | kernel |
| 0.59% | `python` | `_PyUnicode_InternImmortal` | str |
| 0.57% | `[kernel.kallsyms]` | `zap_pte_range` | kernel |
| 0.57% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.52% | `python` | `PyUnicode_New.part.0` | memory |
| 0.48% | `[kernel.kallsyms]` | `percpu_counter_add_batch` | kernel |
| 0.48% | `libc.so.6` | `_int_malloc` | libc |
| 0.48% | `python` | `r_long` | import |
| 0.47% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 0.46% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.45% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.44% | `python` | `intern_constants` | str |
| 0.42% | `libc.so.6` | `__strlen_asimd` | libc |
| 0.42% | `python` | `PyDict_GetItemRef` | dict |
| 0.40% | `[kernel.kallsyms]` | `__pi_copy_page` | kernel |
| 0.40% | `python` | `build_indices_unicode` | dict |
| 0.39% | `python` | `tuple_traverse` | gc |
| 0.37% | `python` | `PyObject_Malloc` | dynamic |
| 0.37% | `python` | `_PyCode_New` | interpreter |
| 0.37% | `python` | `unicode_dealloc` | memory |
| 0.35% | `python` | `tuple_alloc` | memory |
| 0.34% | `[kernel.kallsyms]` | `__update_cpu_freelist_fast` | kernel |
| 0.34% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.33% | `[kernel.kallsyms]` | `__arch_copy_to_user` | kernel |
| 0.32% | `python` | `_PyTypeCache_Insert` | unknown |
| 0.32% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.31% | `python` | `find_empty_slot` | dict |
| 0.31% | `[kernel.kallsyms]` | `handle_mm_fault` | kernel |
| 0.31% | `python` | `initialize_locals` | interpreter |
| 0.30% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.30% | `python` | `func_traverse` | gc |
| 0.29% | `python` | `_Py_NewReference` | memory |
| 0.28% | `python` | `type_is_gc` | gc |
| 0.28% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.27% | `python` | `code_dealloc` | memory |
| 0.27% | `ld-linux-aarch64.so.1` | `_dl_relocate_object` | library |
| 0.27% | `python` | `PyList_Append` | list |
| 0.27% | `python` | `PyObject_GC_Del` | gc |
| 0.26% | `[kernel.kallsyms]` | `mas_walk` | kernel |
| 0.26% | `[kernel.kallsyms]` | `mem_cgroup_commit_charge` | kernel |
| 0.25% | `[kernel.kallsyms]` | `el0_svc` | kernel |
| 0.25% | `libc.so.6` | `__memset_zva64` | libc |
| 0.25% | `ld-linux-aarch64.so.1` | `do_lookup_x` | library |

## python_startup_no_site

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 6.48% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.70% | `python` | `gc_collect_main` | gc |
| 3.95% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.06% | `python` | `visit_decref` | gc |
| 2.80% | `python` | `_PyObject_Malloc` | memory |
| 2.63% | `python` | `visit_reachable` | gc |
| 2.54% | `python` | `_Py_dict_lookup` | lookup |
| 1.50% | `python` | `_PyObject_Free` | memory |
| 1.49% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 1.45% | `python` | `r_object` | import |
| 1.27% | `python` | `dict_traverse` | gc |
| 1.26% | `python` | `type_ready` | dynamic |
| 1.18% | `python` | `find_name_in_mro` | lookup |
| 1.09% | `python` | `_PyCode_Quicken` | interpreter |
| 0.98% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.98% | `python` | `_Py_Dealloc` | memory |
| 0.97% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.84% | `python` | `siphash13` | str |
| 0.83% | `python` | `_PyUnicode_FromUCS1.part.0` | str |
| 0.83% | `[kernel.kallsyms]` | `perf_iterate_ctx` | kernel |
| 0.78% | `[kernel.kallsyms]` | `next_uptodate_folio` | kernel |
| 0.76% | `python` | `insertdict` | dict |
| 0.70% | `python` | `tuple_dealloc` | memory |
| 0.68% | `python` | `_Py_dict_lookup_threadsafe_stackref` | lookup |
| 0.65% | `[kernel.kallsyms]` | `__pi_clear_page` | kernel |
| 0.64% | `[kernel.kallsyms]` | `el0_da` | kernel |
| 0.64% | `[kernel.kallsyms]` | `zap_pte_range` | kernel |
| 0.63% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.61% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.57% | `python` | `update_one_slot` | lookup |
| 0.54% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 0.53% | `[kernel.kallsyms]` | `__pi_copy_page` | kernel |
| 0.52% | `python` | `_PyUnicode_InternImmortal` | str |
| 0.51% | `[kernel.kallsyms]` | `percpu_counter_add_batch` | kernel |
| 0.51% | `libc.so.6` | `__strlen_asimd` | libc |
| 0.51% | `python` | `PyUnicode_New.part.0` | memory |
| 0.46% | `libc.so.6` | `_int_malloc` | libc |
| 0.46% | `python` | `build_indices_unicode` | dict |
| 0.44% | `python` | `intern_constants` | str |
| 0.41% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.41% | `python` | `r_long` | import |
| 0.40% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.39% | `python` | `PyObject_Malloc` | dynamic |
| 0.38% | `python` | `PyDict_GetItemRef` | dict |
| 0.38% | `python` | `tuple_traverse` | gc |
| 0.37% | `python` | `unicode_dealloc` | memory |
| 0.36% | `ld-linux-aarch64.so.1` | `_dl_relocate_object` | library |
| 0.35% | `[kernel.kallsyms]` | `__arch_copy_to_user` | kernel |
| 0.35% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.35% | `python` | `find_empty_slot` | dict |
| 0.34% | `[kernel.kallsyms]` | `__update_cpu_freelist_fast` | kernel |
| 0.34% | `[kernel.kallsyms]` | `handle_mm_fault` | kernel |
| 0.33% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.33% | `python` | `_PyCode_New` | interpreter |
| 0.33% | `python` | `tuple_alloc` | memory |
| 0.31% | `python` | `initialize_locals` | interpreter |
| 0.31% | `python` | `_Py_NewReference` | memory |
| 0.29% | `ld-linux-aarch64.so.1` | `do_lookup_x` | library |
| 0.29% | `python` | `type_is_gc` | gc |
| 0.28% | `[kernel.kallsyms]` | `mas_walk` | kernel |
| 0.28% | `python` | `code_dealloc` | memory |
| 0.28% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.27% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.27% | `python` | `func_traverse` | gc |
| 0.26% | `[kernel.kallsyms]` | `mem_cgroup_commit_charge` | kernel |
| 0.26% | `[kernel.kallsyms]` | `arch_local_irq_restore` | kernel |
| 0.26% | `python` | `PyObject_Free` | dynamic |
| 0.26% | `python` | `_PyTypeCache_Insert` | unknown |
| 0.25% | `python` | `PyDict_Next` | dict |

## raytrace

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 38.47% | `[JIT]` | `jit` | jit |
| 4.95% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 4.16% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.93% | `python` | `PyFloat_FromDouble` | float |
| 3.61% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.58% | `python` | `float_dealloc` | memory |
| 2.52% | `python` | `_Py_Dealloc` | memory |
| 2.32% | `python` | `initialize_locals` | interpreter |
| 2.06% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.99% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 1.70% | `python` | `_PyThreadState_PopFrame` | threading |
| 1.58% | `python` | `_Py_NewReference` | memory |
| 1.47% | `python` | `_PyFloat_ExactDealloc` | memory |
| 1.44% | `python` | `_PyObject_Free` | memory |
| 1.38% | `python` | `subtype_dealloc` | memory |
| 1.14% | `python` | `_PyObject_Malloc` | memory |
| 0.98% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.94% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.92% | `math.cpython-316-aarch64-linux-gnu.so` | `math_sqrt` | library |
| 0.86% | `python` | `_PyEval_Vector` | interpreter |
| 0.85% | `python` | `float_richcompare` | float |
| 0.82% | `python` | `PyType_GenericAlloc` | memory |
| 0.80% | `python` | `vectorcall_maybe` | unknown |
| 0.79% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.77% | `python` | `_PyJIT_Entry` | compiler |
| 0.76% | `python` | `PyObject_GC_Del` | gc |
| 0.72% | `python` | `PyType_IsSubtype` | dynamic |
| 0.70% | `python` | `compactlong_float_subtract` | unknown |
| 0.64% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.63% | `python` | `PyNumber_Subtract` | dynamic |
| 0.61% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.56% | `python` | `slot_nb_subtract` | unknown |
| 0.50% | `libc.so.6` | `__memset_zva64` | libc |
| 0.47% | `python` | `_PyObject_InitInlineValues` | dynamic |
| 0.47% | `python` | `compactlong_float_guard` | unknown |
| 0.41% | `python` | `tuple_dealloc` | memory |
| 0.39% | `python` | `PyLong_AsDouble` | int |
| 0.38% | `python` | `_PyObject_GC_Link` | gc |
| 0.37% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.37% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.36% | `python` | `float_sub` | float |
| 0.33% | `python` | `lookup_method_ex.constprop.0` | unknown |
| 0.32% | `python` | `PyObject_RichCompare` | dynamic |
| 0.26% | `python` | `object_dealloc` | memory |
| 0.26% | `python` | `tuple_alloc` | memory |
| 0.25% | `python` | `PyObject_Free` | dynamic |

## regex_compile

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.70% | `[JIT]` | `jit` | jit |
| 17.36% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.77% | `python` | `_PyObject_Malloc` | memory |
| 2.76% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.43% | `python` | `_Py_Dealloc` | memory |
| 1.92% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.40% | `python` | `_PyObject_Free` | memory |
| 1.36% | `python` | `tuple_dealloc` | memory |
| 1.28% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.19% | `python` | `bytearray_ass_subscript_lock_held` | miscobj |
| 1.15% | `python` | `_PyJIT_Entry` | compiler |
| 1.08% | `python` | `tuple_alloc` | memory |
| 1.07% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.01% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 1.00% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.94% | `python` | `PyType_IsSubtype` | dynamic |
| 0.93% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.79% | `python` | `initialize_locals` | interpreter |
| 0.78% | `python` | `_Py_NewReference` | memory |
| 0.76% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.75% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.73% | `python` | `_PyLong_FromMedium` | int |
| 0.68% | `python` | `PyLong_FromSsize_t` | int |
| 0.66% | `python` | `long_richcompare` | int |
| 0.63% | `python` | `set_lookkey` | miscobj |
| 0.61% | `python` | `PyLong_FromLong` | int |
| 0.61% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.61% | `python` | `PyUnicode_Contains` | str |
| 0.59% | `python` | `long_dealloc` | memory |
| 0.58% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.56% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.55% | `python` | `list_append` | list |
| 0.53% | `python` | `list_dealloc` | memory |
| 0.53% | `python` | `_PyType_GetDict` | dynamic |
| 0.52% | `python` | `PyObject_SetItem` | dynamic |
| 0.51% | `python` | `_PyEval_Vector` | interpreter |
| 0.45% | `python` | `bytearray_ass_subscript` | miscobj |
| 0.43% | `python` | `PyLong_AsSsize_t` | int |
| 0.43% | `python` | `PyObject_GC_Del` | gc |
| 0.43% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.42% | `python` | `_PyUnicode_Equal` | str |
| 0.41% | `python` | `gen_dealloc` | memory |
| 0.40% | `python` | `PyMethod_New` | memory |
| 0.39% | `python` | `_Py_dict_lookup` | lookup |
| 0.39% | `python` | `make_range_object` | unknown |
| 0.39% | `python` | `PyList_New.constprop.0` | memory |
| 0.35% | `python` | `_PyCompactLong_Add` | unknown |
| 0.35% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.34% | `python` | `_PyObject_Realloc` | memory |
| 0.33% | `python` | `min_max` | unknown |
| 0.33% | `python` | `_PySet_Contains` | miscobj |
| 0.33% | `python` | `_Py_BuiltinCallFastWithKeywords_StackRef` | unknown |
| 0.31% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.31% | `python` | `slot_sq_item` | unknown |
| 0.28% | `python` | `PyCMethod_New` | memory |
| 0.27% | `python` | `object_isinstance` | dynamic |
| 0.27% | `python` | `PyObject_Hash` | dynamic |
| 0.26% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.26% | `python` | `PyObject_Malloc` | dynamic |

## regex_dna

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 67.01% | `python` | `sre_ucs1_match` | library |
| 26.65% | `python` | `sre_search` | library |
| 1.01% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.62% | `python` | `stringlib_bytes_join` | str |
| 0.59% | `python` | `_PyObject_Malloc` | memory |
| 0.44% | `python` | `pattern_subx` | library |
| 0.39% | `python` | `PyBuffer_Release` | miscobj |
| 0.32% | `python` | `list_dealloc` | memory |
| 0.26% | `python` | `_PyObject_Free` | memory |

## regex_effbot

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 77.83% | `python` | `sre_ucs1_match` | library |
| 12.81% | `python` | `sre_search` | library |
| 4.88% | `python` | `sre_ucs1_count` | library |
| 1.00% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.34% | `python` | `siphash13` | str |
| 0.26% | `python` | `_PyObject_Malloc` | memory |

## regex_v8

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 58.40% | `python` | `sre_ucs1_match` | library |
| 6.12% | `python` | `sre_search` | library |
| 3.58% | `python` | `sre_ucs1_count` | library |
| 3.02% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.68% | `libc.so.6` | `_int_malloc` | libc |
| 1.92% | `python` | `_PyObject_Malloc` | memory |
| 1.36% | `python` | `_PyObject_Free` | memory |
| 1.28% | `python` | `pattern_subx` | library |
| 1.28% | `python` | `sre_category` | library |
| 1.28% | `[JIT]` | `jit` | jit |
| 1.09% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.89% | `python` | `_sre_SRE_Pattern_search` | library |
| 0.84% | `python` | `_PyUnicode_ToLowercase` | str |
| 0.78% | `python` | `_PyUnicode_IsAlpha` | str |
| 0.71% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.59% | `python` | `PyUnicode_Substring` | str |
| 0.57% | `python` | `PyErr_Occurred` | exceptions |
| 0.57% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.55% | `python` | `pattern_new_match` | memory |
| 0.54% | `libc.so.6` | `malloc` | libc |
| 0.47% | `python` | `_Py_Dealloc` | memory |
| 0.37% | `libc.so.6` | `_int_free` | libc |
| 0.36% | `libc.so.6` | `_int_free_merge_chunk` | libc |
| 0.36% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.35% | `libc.so.6` | `unlink_chunk.isra.0` | libc |
| 0.34% | `python` | `method_vectorcall_FASTCALL_KEYWORDS_METHOD` | calls |
| 0.34% | `python` | `_Py_dict_lookup` | lookup |
| 0.32% | `libc.so.6` | `cfree@GLIBC_2.17` | libc |
| 0.31% | `libc.so.6` | `_int_free_create_chunk` | libc |
| 0.29% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.29% | `python` | `_PyUnicode_IsDecimalDigit` | str |
| 0.28% | `python` | `PyMem_Free` | memory |
| 0.27% | `python` | `PyUnicode_New.part.0` | memory |
| 0.26% | `python` | `PyObject_Vectorcall` | dynamic |

## richards

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 62.28% | `[JIT]` | `jit` | jit |
| 8.19% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 6.58% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 5.76% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.67% | `python` | `_PyThreadState_PopFrame` | threading |
| 1.93% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 1.53% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.28% | `python` | `_PyCompactLong_Add` | unknown |
| 1.11% | `python` | `long_dealloc` | memory |
| 1.07% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.78% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.76% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.69% | `python` | `_Py_LoadAttr_StackRefSteal` | unknown |
| 0.52% | `python` | `PyObject_IsInstance` | dynamic |
| 0.50% | `python` | `_PyCompactLong_Subtract` | unknown |
| 0.47% | `python` | `_Py_Dealloc` | memory |
| 0.41% | `python` | `_PyLong_FromMedium` | int |
| 0.30% | `python` | `_PyType_GetDict` | dynamic |
| 0.29% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |

## richards_super

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 64.32% | `[JIT]` | `jit` | jit |
| 8.43% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 6.65% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 4.62% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.66% | `python` | `_PyThreadState_PopFrame` | threading |
| 1.95% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 1.31% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.17% | `python` | `_PyCompactLong_Add` | unknown |
| 0.96% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.92% | `python` | `long_dealloc` | memory |
| 0.73% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.69% | `python` | `_Py_LoadAttr_StackRefSteal` | unknown |
| 0.66% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.46% | `python` | `_Py_Dealloc` | memory |
| 0.43% | `python` | `_PyCompactLong_Subtract` | unknown |
| 0.40% | `python` | `_PyLong_FromMedium` | int |
| 0.35% | `python` | `PyObject_IsInstance` | dynamic |
| 0.27% | `python` | `_Py_NewReference` | memory |
| 0.25% | `python` | `_PyJIT_Entry` | compiler |

## scimark

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.82% | `[JIT]` | `jit` | jit |
| 6.19% | `python` | `PyFloat_FromDouble` | float |
| 4.37% | `array.cpython-316-aarch64-linux-gnu.so` | `array_subscr` | library |
| 3.89% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 3.21% | `python` | `convertitem.constprop.0` | unknown |
| 3.13% | `python` | `vgetargs1_impl.constprop.0` | calls |
| 2.95% | `python` | `PyObject_GetItem` | dynamic |
| 2.66% | `python` | `_PyCompactLong_Add` | unknown |
| 2.61% | `python` | `_Py_NewReference` | memory |
| 2.58% | `python` | `_Py_Dealloc` | memory |
| 2.33% | `array.cpython-316-aarch64-linux-gnu.so` | `array_ass_subscr` | library |
| 2.10% | `python` | `_PyFloat_ExactDealloc` | memory |
| 2.08% | `python` | `PyLong_AsSsize_t` | int |
| 2.07% | `python` | `float_dealloc` | memory |
| 1.96% | `python` | `PyArg_Parse` | calls |
| 1.83% | `python` | `PyIndex_Check` | unknown |
| 1.68% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.60% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.45% | `array.cpython-316-aarch64-linux-gnu.so` | `d_setitem` | library |
| 1.42% | `python` | `_PyCompactLong_Multiply` | unknown |
| 1.13% | `python` | `PyObject_SetItem` | dynamic |
| 1.04% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.99% | `python` | `PyType_GetModuleByDef` | dynamic |
| 0.94% | `python` | `long_dealloc` | memory |
| 0.88% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.81% | `python` | `PyLong_FromLong` | int |
| 0.70% | `python` | `PyFloat_AsDouble` | float |
| 0.69% | `array.cpython-316-aarch64-linux-gnu.so` | `d_getitem` | library |
| 0.69% | `python` | `tuple_dealloc` | memory |
| 0.63% | `python` | `_PyLong_ExactDealloc` | memory |
| 0.58% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.52% | `python` | `PyType_IsSubtype` | dynamic |
| 0.50% | `python` | `tuple_alloc` | memory |
| 0.48% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.48% | `array.cpython-316-aarch64-linux-gnu.so` | `PyNumber_AsSsize_t@plt` | library |
| 0.46% | `array.cpython-316-aarch64-linux-gnu.so` | `PyIndex_Check@plt` | library |
| 0.46% | `array.cpython-316-aarch64-linux-gnu.so` | `PyType_GetModuleByDef@plt` | library |
| 0.45% | `python` | `_PyLong_Frexp` | int |
| 0.43% | `python` | `_PyType_GetDict` | dynamic |
| 0.42% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.41% | `python` | `_PyCompactLong_Subtract` | unknown |
| 0.40% | `python` | `object_isinstance` | dynamic |
| 0.38% | `python` | `float_richcompare` | float |
| 0.35% | `python` | `_PyLong_FromMedium` | int |
| 0.32% | `python` | `_PyJIT_Entry` | compiler |
| 0.31% | `array.cpython-316-aarch64-linux-gnu.so` | `PyFloat_FromDouble@plt` | library |
| 0.30% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.30% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.27% | `python` | `_Py_CallBuiltinClass_StackRef` | unknown |

## spectral_norm

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 40.22% | `[JIT]` | `jit` | jit |
| 10.97% | `python` | `float_compactlong_true_div` | float |
| 9.96% | `python` | `_PyCompactLong_Add` | unknown |
| 4.06% | `python` | `_PyLong_ExactDealloc` | memory |
| 3.74% | `python` | `_PyCompactLong_Multiply` | unknown |
| 3.17% | `python` | `_Py_NewReference` | memory |
| 3.16% | `python` | `enum_next` | miscobj |
| 3.11% | `python` | `PyFloat_FromDouble` | float |
| 2.32% | `python` | `long_div` | int |
| 2.19% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.18% | `python` | `PyNumber_FloorDivide` | dynamic |
| 2.00% | `python` | `_PyLong_FromMedium` | int |
| 1.89% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.46% | `python` | `nonzero_float_compactlong_guard` | unknown |
| 1.39% | `python` | `PyLong_FromSsize_t` | int |
| 1.38% | `python` | `_PyFloat_ExactDealloc` | memory |
| 1.34% | `python` | `PyLong_FromLong` | int |
| 1.18% | `python` | `listiter_next` | list |
| 0.98% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.77% | `python` | `_Py_Dealloc` | memory |
| 0.72% | `python` | `float_dealloc` | memory |
| 0.63% | `python` | `float_compactlong_guard` | float |
| 0.30% | `python` | `_PyEval_EvalFrameDefault` | interpreter |

## sphinx

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 11.46% | `[JIT]` | `jit` | jit |
| 10.41% | `python` | `sre_ucs1_match` | library |
| 9.20% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.69% | `python` | `gc_collect_main` | gc |
| 3.55% | `python` | `_PyTypeCache_Lookup` | unknown |
| 2.64% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 2.41% | `python` | `_PyObject_Malloc` | memory |
| 1.97% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.50% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.42% | `python` | `_PyObject_Free` | memory |
| 1.34% | `python` | `visit_decref` | gc |
| 1.30% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 1.27% | `python` | `_Py_dict_lookup` | lookup |
| 1.12% | `python` | `_Py_Dealloc` | memory |
| 1.10% | `python` | `PyType_IsSubtype` | dynamic |
| 1.06% | `python` | `initialize_locals` | interpreter |
| 1.03% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.95% | `python` | `_PyJIT_Entry` | compiler |
| 0.94% | `_pickle.cpython-316-aarch64-linux-gnu.so` | `save.constprop.0` | library |
| 0.88% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.88% | `python` | `visit_reachable` | gc |
| 0.88% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.75% | `python` | `gen_dealloc` | memory |
| 0.72% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.69% | `python` | `siphash13` | str |
| 0.68% | `python` | `PyUnicode_Format` | str |
| 0.63% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.62% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.61% | `python` | `object_isinstance` | dynamic |
| 0.61% | `python` | `sre_search` | library |
| 0.59% | `python` | `tuple_dealloc` | memory |
| 0.58% | `python` | `_PyType_GetDict` | dynamic |
| 0.57% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.56% | `python` | `tuple_alloc` | memory |
| 0.54% | `python` | `PyDict_GetItemRef` | dict |
| 0.51% | `_pickle.cpython-316-aarch64-linux-gnu.so` | `save_dict` | library |
| 0.45% | `python` | `dict_traverse` | gc |
| 0.44% | `python` | `sre_ucs2_match` | library |
| 0.43% | `python` | `_PyEval_Vector` | interpreter |
| 0.39% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.38% | `python` | `list_dealloc` | memory |
| 0.38% | `python` | `PyObject_IsInstance` | dynamic |
| 0.37% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.34% | `python` | `getset_get` | dynamic |
| 0.33% | `_pickle.cpython-316-aarch64-linux-gnu.so` | `PyMemoTable_Set` | library |
| 0.33% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.32% | `python` | `_Py_NewReference` | memory |
| 0.32% | `python` | `sre_category` | library |
| 0.31% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 0.29% | `python` | `_PyDict_Subscript` | dict |
| 0.29% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.29% | `python` | `PyObject_GC_Del` | gc |
| 0.29% | `python` | `make_gen` | miscobj |
| 0.27% | `python` | `pattern_subx` | library |
| 0.27% | `python` | `PyObject_Malloc` | dynamic |
| 0.26% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.25% | `libc.so.6` | `_int_malloc` | libc |

## sqlalchemy_declarative

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.83% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.09% | `[JIT]` | `jit` | jit |
| 3.85% | `python` | `_PyTypeCache_Lookup` | unknown |
| 2.83% | `python` | `_PyObject_Malloc` | memory |
| 2.22% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.17% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.07% | `python` | `_Py_Dealloc` | memory |
| 1.70% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.67% | `python` | `_PyObject_Free` | memory |
| 1.51% | `python` | `tuple_dealloc` | memory |
| 1.40% | `python` | `_Py_dict_lookup` | lookup |
| 1.32% | `python` | `initialize_locals` | interpreter |
| 1.30% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 1.19% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 1.11% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.02% | `python` | `tuple_alloc` | memory |
| 1.00% | `python` | `PyObject_SetAttr` | dynamic |
| 0.93% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 0.88% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.83% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.82% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.78% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.76% | `python` | `store_instance_attr_lock_held` | unknown |
| 0.64% | `libc.so.6` | `pthread_mutex_lock@@GLIBC_2.17` | libc |
| 0.57% | `python` | `PyObject_GC_Del` | gc |
| 0.54% | `python` | `_PyDict_Subscript` | dict |
| 0.54% | `python` | `_PyEval_Vector` | interpreter |
| 0.52% | `libc.so.6` | `__GI___pthread_mutex_unlock_usercnt` | libc |
| 0.51% | `python` | `_PyJIT_Entry` | compiler |
| 0.50% | `python` | `_Py_NewReference` | memory |
| 0.49% | `python` | `PyType_IsSubtype` | dynamic |
| 0.48% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.48% | `python` | `set_lookkey` | miscobj |
| 0.46% | `python` | `subtype_dealloc` | memory |
| 0.46% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.45% | `python` | `_PyType_GetDict` | dynamic |
| 0.45% | `python` | `_PyUnicode_InternMortal` | str |
| 0.44% | `python` | `insertdict` | dict |
| 0.43% | `libsqlite3.so.0.8.6` | `sqlite3VdbeExec` | library |
| 0.42% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.42% | `python` | `take_gil` | gil |
| 0.41% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.39% | `python` | `PyObject_IsTrue` | dynamic |
| 0.39% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.37% | `python` | `list_dealloc` | memory |
| 0.35% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.35% | `python` | `PyObject_Hash` | dynamic |
| 0.35% | `libc.so.6` | `__memset_zva64` | libc |
| 0.35% | `python` | `dict_dealloc` | memory |
| 0.35% | `python` | `__aarch64_ldclr8_acq_rel` | unknown |
| 0.34% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.33% | `python` | `PyDict_GetItemRef` | dict |
| 0.32% | `python` | `PyTuple_FromArray.part.0` | tuple |
| 0.32% | `python` | `PyList_New.constprop.0` | memory |
| 0.30% | `python` | `_PyObject_GC_New` | gc |
| 0.30% | `python` | `PyObject_Malloc` | dynamic |
| 0.29% | `python` | `tuple_hash` | tuple |
| 0.26% | `python` | `_PyObject_StoreInstanceAttribute` | dynamic |
| 0.25% | `python` | `PyMethod_New` | memory |

## sqlalchemy_imperative

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.05% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.38% | `python` | `_PyTypeCache_Lookup` | unknown |
| 4.32% | `[JIT]` | `jit` | jit |
| 2.62% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 2.39% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.27% | `python` | `_PyObject_Malloc` | memory |
| 1.88% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 1.77% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.70% | `python` | `initialize_locals` | interpreter |
| 1.62% | `python` | `_Py_dict_lookup` | lookup |
| 1.54% | `python` | `_Py_Dealloc` | memory |
| 1.41% | `python` | `_PyObject_Free` | memory |
| 1.35% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 1.27% | `python` | `tuple_dealloc` | memory |
| 1.19% | `python` | `tuple_alloc` | memory |
| 1.12% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.08% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 1.05% | `python` | `gc_collect_main` | gc |
| 0.82% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.78% | `python` | `PyObject_SetAttr` | dynamic |
| 0.70% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.69% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.68% | `python` | `insertdict` | dict |
| 0.64% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.63% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 0.57% | `python` | `PyObject_IsTrue` | dynamic |
| 0.56% | `python` | `PyDict_GetItemRef` | dict |
| 0.56% | `python` | `PyType_IsSubtype` | dynamic |
| 0.54% | `python` | `_PyType_GetDict` | dynamic |
| 0.49% | `libsqlite3.so.0.8.6` | `sqlite3VdbeExec` | library |
| 0.44% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.43% | `python` | `dict_dealloc` | memory |
| 0.43% | `python` | `_Py_NewReference` | memory |
| 0.43% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.38% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.36% | `libc.so.6` | `pthread_mutex_lock@@GLIBC_2.17` | libc |
| 0.36% | `python` | `_PyEval_Vector` | interpreter |
| 0.35% | `python` | `insert_to_emptydict` | dict |
| 0.35% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.31% | `python` | `PyObject_GC_Del` | gc |
| 0.31% | `python` | `_PyJIT_Entry` | compiler |
| 0.31% | `python` | `subtype_dealloc` | memory |
| 0.30% | `python` | `_PyUnicode_InternMortal` | str |
| 0.30% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.29% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.29% | `python` | `_PyDict_Subscript` | dict |
| 0.29% | `libc.so.6` | `__memset_zva64` | libc |
| 0.27% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.27% | `libc.so.6` | `__GI___pthread_mutex_unlock_usercnt` | libc |
| 0.26% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.26% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.26% | `python` | `list_dealloc` | memory |
| 0.25% | `python` | `PyList_New` | memory |

## sqlglot_v2

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 16.17% | `[JIT]` | `jit` | jit |
| 13.02% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.92% | `python` | `_PyTypeCache_Lookup` | unknown |
| 3.88% | `python` | `_PyObject_Malloc` | memory |
| 3.30% | `python` | `_Py_Dealloc` | memory |
| 2.68% | `python` | `_PyObject_Free` | memory |
| 2.67% | `python` | `PyType_IsSubtype` | dynamic |
| 2.34% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 2.23% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.86% | `python` | `tuple_dealloc` | memory |
| 1.66% | `python` | `dictiter_iternextitem` | dict |
| 1.47% | `python` | `PyObject_IsInstance` | dynamic |
| 1.46% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 1.42% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 1.41% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.34% | `python` | `object_isinstance` | dynamic |
| 1.32% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.30% | `python` | `_PyJIT_Entry` | compiler |
| 1.24% | `python` | `tuple_alloc` | memory |
| 1.16% | `python` | `PyCMethod_New` | memory |
| 1.13% | `python` | `initialize_locals` | interpreter |
| 1.09% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.94% | `python` | `_Py_NewReference` | memory |
| 0.87% | `python` | `gen_dealloc` | memory |
| 0.85% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.80% | `python` | `_PyObject_GC_New` | gc |
| 0.77% | `python` | `getset_get` | dynamic |
| 0.76% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.75% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.74% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.70% | `python` | `PyObject_GC_Del` | gc |
| 0.68% | `python` | `_Py_dict_lookup` | lookup |
| 0.66% | `python` | `meth_dealloc` | memory |
| 0.66% | `python` | `_PyObject_RealIsInstance` | dynamic |
| 0.65% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.64% | `python` | `insert_to_emptydict` | dict |
| 0.51% | `python` | `_PyObject_Calloc` | memory |
| 0.51% | `python` | `tuple_hash` | tuple |
| 0.51% | `python` | `object_get_class` | dynamic |
| 0.49% | `python` | `_PyObject_GC_Link` | gc |
| 0.48% | `python` | `PyList_New` | memory |
| 0.46% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.46% | `python` | `PyObject_Malloc` | dynamic |
| 0.43% | `python` | `_PyEval_Vector` | interpreter |
| 0.41% | `python` | `cfunction_vectorcall_O` | calls |
| 0.39% | `python` | `PyObject_IsTrue` | dynamic |
| 0.39% | `python` | `PyObject_Free` | dynamic |
| 0.39% | `python` | `_PyType_GetDict` | dynamic |
| 0.39% | `python` | `PyObject_Hash` | dynamic |
| 0.38% | `python` | `dict_get` | dict |
| 0.38% | `python` | `dict_items` | dict |
| 0.37% | `python` | `make_gen` | miscobj |
| 0.36% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.36% | `python` | `list_dealloc` | memory |
| 0.36% | `python` | `dictitems_iter` | unknown |
| 0.35% | `python` | `method_get` | dynamic |
| 0.34% | `python` | `PyDescr_IsData` | dynamic |
| 0.33% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.33% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 0.31% | `python` | `new_dict.constprop.0` | dict |
| 0.30% | `python` | `_PyTuple_FromPairSteal` | tuple |
| 0.30% | `python` | `_PyDict_LoadBuiltinsFromGlobals` | dict |
| 0.30% | `python` | `func_clear` | unknown |
| 0.29% | `python` | `siphash13` | str |
| 0.28% | `python` | `dictview_dealloc` | memory |
| 0.28% | `python` | `dictiter_dealloc` | memory |
| 0.27% | `python` | `PyDict_GetItemRef` | dict |
| 0.27% | `python` | `object_recursive_isinstance` | dynamic |
| 0.27% | `python` | `PyList_New.constprop.0` | memory |

## sqlglot_v2_optimize

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 15.73% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 13.08% | `[JIT]` | `jit` | jit |
| 4.59% | `python` | `_PyTypeCache_Lookup` | unknown |
| 3.41% | `python` | `_PyObject_Malloc` | memory |
| 3.05% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 2.86% | `python` | `PyType_IsSubtype` | dynamic |
| 2.75% | `python` | `_Py_Dealloc` | memory |
| 2.45% | `python` | `_PyObject_Free` | memory |
| 1.87% | `python` | `dictiter_iternextitem` | dict |
| 1.81% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 1.78% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.71% | `python` | `tuple_dealloc` | memory |
| 1.63% | `python` | `PyObject_IsInstance` | dynamic |
| 1.49% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 1.46% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.31% | `python` | `object_isinstance` | dynamic |
| 1.24% | `python` | `PyCMethod_New` | memory |
| 1.14% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.12% | `python` | `tuple_alloc` | memory |
| 0.99% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.99% | `python` | `_PyJIT_Entry` | compiler |
| 0.97% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.91% | `python` | `_Py_NewReference` | memory |
| 0.83% | `python` | `getset_get` | dynamic |
| 0.80% | `python` | `initialize_locals` | interpreter |
| 0.79% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.77% | `python` | `_Py_dict_lookup` | lookup |
| 0.76% | `python` | `_PyObject_RealIsInstance` | dynamic |
| 0.71% | `python` | `meth_dealloc` | memory |
| 0.71% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.68% | `python` | `_PyType_GetDict` | dynamic |
| 0.62% | `python` | `_PyObject_GC_New` | gc |
| 0.57% | `python` | `PyList_New` | memory |
| 0.56% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.56% | `python` | `_PyObject_Calloc` | memory |
| 0.55% | `python` | `PyObject_GC_Del` | gc |
| 0.52% | `python` | `object_get_class` | dynamic |
| 0.49% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.45% | `python` | `PyDescr_IsData` | dynamic |
| 0.44% | `python` | `tuple_hash` | tuple |
| 0.44% | `python` | `cfunction_vectorcall_O` | calls |
| 0.44% | `python` | `insertdict` | dict |
| 0.43% | `python` | `method_get` | dynamic |
| 0.43% | `python` | `insert_to_emptydict` | dict |
| 0.41% | `python` | `list_dealloc` | memory |
| 0.41% | `python` | `PyObject_Malloc` | dynamic |
| 0.39% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.38% | `python` | `PyMember_GetOne` | lookup |
| 0.38% | `python` | `dict_get` | dict |
| 0.37% | `python` | `_PyObject_GC_Link` | gc |
| 0.36% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.36% | `python` | `PyObject_IsTrue` | dynamic |
| 0.35% | `python` | `PyObject_Hash` | dynamic |
| 0.35% | `python` | `gen_dealloc` | memory |
| 0.34% | `python` | `object_recursive_isinstance` | dynamic |
| 0.34% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.34% | `python` | `_PyEval_Vector` | interpreter |
| 0.34% | `python` | `PyObject_Free` | dynamic |
| 0.33% | `python` | `gc_collect_main` | gc |
| 0.29% | `python` | `PyList_New.constprop.0` | memory |
| 0.28% | `python` | `siphash13` | str |
| 0.27% | `python` | `dictitems_iter` | unknown |
| 0.26% | `python` | `dict_items` | dict |
| 0.26% | `python` | `_PyDict_LoadBuiltinsFromGlobals` | dict |
| 0.25% | `python` | `PyDict_GetItemRef` | dict |

## sqlglot_v2_parse

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.98% | `[JIT]` | `jit` | jit |
| 18.83% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.10% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.73% | `python` | `initialize_locals` | interpreter |
| 2.48% | `python` | `_PyObject_Malloc` | memory |
| 2.34% | `python` | `_PyTypeCache_Lookup` | unknown |
| 2.13% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.96% | `python` | `gc_collect_main` | gc |
| 1.84% | `python` | `_PyObject_Free` | memory |
| 1.82% | `python` | `_Py_dict_lookup` | lookup |
| 1.72% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.57% | `python` | `_PyJIT_Entry` | compiler |
| 1.38% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.25% | `python` | `_Py_Dealloc` | memory |
| 1.14% | `python` | `PyObject_RichCompare` | dynamic |
| 0.96% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.91% | `python` | `_PyCompactLong_Add` | unknown |
| 0.87% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.81% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.75% | `python` | `PyType_IsSubtype` | dynamic |
| 0.74% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.66% | `python` | `dict_get` | dict |
| 0.66% | `python` | `PyDict_Contains` | dict |
| 0.59% | `python` | `_PyEval_Vector` | interpreter |
| 0.59% | `python` | `dictiter_iternextitem` | dict |
| 0.59% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.59% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.56% | `python` | `visit_decref` | gc |
| 0.52% | `python` | `_PyCompactLong_Subtract` | unknown |
| 0.50% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.44% | `python` | `_Py_NewReference` | memory |
| 0.42% | `python` | `insert_to_emptydict` | dict |
| 0.41% | `python` | `object_richcompare` | dynamic |
| 0.35% | `python` | `insertdict` | dict |
| 0.35% | `python` | `tuple_dealloc` | memory |
| 0.35% | `python` | `slot_tp_hash` | unknown |
| 0.34% | `python` | `PyObject_Malloc` | dynamic |
| 0.34% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.34% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.33% | `python` | `_PyObject_GC_New` | gc |
| 0.33% | `python` | `PyObject_SetAttr` | dynamic |
| 0.33% | `python` | `dict_traverse` | gc |
| 0.32% | `python` | `PyObject_IsTrue` | dynamic |
| 0.32% | `python` | `PyLong_FromSsize_t` | int |
| 0.32% | `python` | `clear_slots` | unknown |
| 0.30% | `python` | `PyCMethod_New` | memory |
| 0.30% | `python` | `_PyType_GetDict` | dynamic |
| 0.29% | `python` | `PyObject_IsInstance` | dynamic |
| 0.29% | `python` | `PyMember_SetOne` | lookup |
| 0.29% | `python` | `PyObject_Free` | dynamic |
| 0.28% | `python` | `subtype_traverse` | gc |
| 0.27% | `python` | `_PyUnicode_BinarySlice` | str |
| 0.26% | `python` | `long_dealloc` | memory |

## sqlglot_v2_transpile

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 19.81% | `[JIT]` | `jit` | jit |
| 19.78% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.84% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.65% | `python` | `_PyObject_Malloc` | memory |
| 2.63% | `python` | `initialize_locals` | interpreter |
| 2.54% | `python` | `_PyTypeCache_Lookup` | unknown |
| 2.06% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.90% | `python` | `_Py_dict_lookup` | lookup |
| 1.90% | `python` | `_PyObject_Free` | memory |
| 1.74% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.55% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.55% | `python` | `gc_collect_main` | gc |
| 1.35% | `python` | `_Py_Dealloc` | memory |
| 1.22% | `python` | `_PyJIT_Entry` | compiler |
| 1.18% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.99% | `python` | `PyObject_RichCompare` | dynamic |
| 0.99% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.97% | `python` | `PyType_IsSubtype` | dynamic |
| 0.90% | `python` | `dict_get` | dict |
| 0.88% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.88% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.85% | `python` | `_PyCompactLong_Add` | unknown |
| 0.52% | `python` | `PyDict_Contains` | dict |
| 0.52% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.50% | `python` | `dictiter_iternextitem` | dict |
| 0.50% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.49% | `python` | `_PyEval_Vector` | interpreter |
| 0.46% | `python` | `_Py_NewReference` | memory |
| 0.44% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.43% | `python` | `visit_decref` | gc |
| 0.40% | `python` | `PyObject_IsInstance` | dynamic |
| 0.39% | `python` | `insert_to_emptydict` | dict |
| 0.38% | `python` | `PyObject_IsTrue` | dynamic |
| 0.37% | `python` | `_PyType_GetDict` | dynamic |
| 0.37% | `python` | `_PyCompactLong_Subtract` | unknown |
| 0.36% | `python` | `object_richcompare` | dynamic |
| 0.35% | `python` | `PyLong_FromSsize_t` | int |
| 0.34% | `python` | `tuple_dealloc` | memory |
| 0.34% | `python` | `PyObject_SetAttr` | dynamic |
| 0.33% | `python` | `slot_tp_hash` | unknown |
| 0.33% | `python` | `insertdict` | dict |
| 0.33% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.32% | `python` | `subtype_traverse` | gc |
| 0.31% | `python` | `PyCMethod_New` | memory |
| 0.30% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.30% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.30% | `python` | `PyMethod_New` | memory |
| 0.30% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.29% | `python` | `PyObject_Free` | dynamic |
| 0.29% | `python` | `PyObject_Malloc` | dynamic |
| 0.28% | `python` | `object_isinstance` | dynamic |
| 0.27% | `python` | `PyUnicode_New.part.0` | memory |
| 0.27% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.27% | `python` | `dict_traverse` | gc |
| 0.26% | `python` | `_PyObject_GC_New` | gc |
| 0.26% | `python` | `tuple_alloc` | memory |

## sqlite_synth

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 6.16% | `libc.so.6` | `pthread_mutex_lock@@GLIBC_2.17` | libc |
| 4.82% | `libc.so.6` | `__GI___pthread_mutex_unlock_usercnt` | libc |
| 4.55% | `python` | `take_gil` | gil |
| 4.55% | `libsqlite3.so.0.8.6` | `sqlite3VdbeExec` | library |
| 3.80% | `python` | `__aarch64_ldclr8_acq_rel` | unknown |
| 3.80% | `libm.so.6` | `__cos` | library |
| 3.20% | `[JIT]` | `jit` | jit |
| 2.03% | `python` | `_Py_Dealloc` | memory |
| 1.59% | `python` | `drop_gil` | gil |
| 1.45% | `libc.so.6` | `pthread_cond_signal@@GLIBC_2.17` | libc |
| 1.42% | `libc.so.6` | `pthread_mutex_unlock@@GLIBC_2.17` | libc |
| 1.39% | `libsqlite3.so.0.8.6` | `0x00000000000a1120` | library |
| 1.35% | `python` | `_PyObject_Free` | memory |
| 1.21% | `python` | `_PyThreadState_Attach` | threading |
| 1.16% | `_sqlite3.cpython-316-aarch64-linux-gnu.so` | `_pysqlite_query_execute` | library |
| 1.12% | `python` | `_PyObject_Malloc` | memory |
| 1.00% | `python` | `tuple_dealloc` | memory |
| 1.00% | `python` | `PyThread_get_thread_ident` | threading |
| 0.93% | `python` | `_PyThreadState_Detach` | threading |
| 0.90% | `python` | `_Py_NewReference` | memory |
| 0.90% | `libsqlite3.so.0.8.6` | `sqlite3_mutex_enter` | library |
| 0.85% | `python` | `tuple_alloc` | memory |
| 0.84% | `python` | `long_to_decimal_string_internal` | int |
| 0.81% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.79% | `libsqlite3.so.0.8.6` | `sqlite3BtreeInsert` | library |
| 0.76% | `libsqlite3.so.0.8.6` | `0x00000000000a1110` | library |
| 0.76% | `libsqlite3.so.0.8.6` | `0x00000000000a10d0` | library |
| 0.75% | `python` | `_PyThreadState_MustExit` | threading |
| 0.73% | `libsqlite3.so.0.8.6` | `sqlite3_mutex_leave` | library |
| 0.72% | `math.cpython-316-aarch64-linux-gnu.so` | `math_cos` | library |
| 0.71% | `python` | `PyList_New` | memory |
| 0.67% | `python` | `long_float` | int |
| 0.65% | `python` | `float_dealloc` | memory |
| 0.62% | `python` | `long_dealloc` | memory |
| 0.59% | `python` | `PyFloat_FromDouble` | float |
| 0.59% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.58% | `libsqlite3.so.0.8.6` | `sqlite3ApiExit` | library |
| 0.53% | `python` | `PyFloat_AsDouble` | float |
| 0.52% | `python` | `PyEval_SaveThread` | interpreter |
| 0.51% | `libc.so.6` | `__errno_location` | libc |
| 0.50% | `_sqlite3.cpython-316-aarch64-linux-gnu.so` | `pysqlite_cursor_init` | library |
| 0.50% | `python` | `_Py_IsMainThread` | unknown |
| 0.49% | `python` | `_PyLong_FromMedium` | int |
| 0.49% | `libsqlite3.so.0.8.6` | `sqlite3DbMallocRawNN` | library |
| 0.43% | `libsqlite3.so.0.8.6` | `sqlite3BtreeBeginTrans` | library |
| 0.43% | `libsqlite3.so.0.8.6` | `sqlite3_step` | library |
| 0.42% | `python` | `pthread_mutex_unlock@plt` | unknown |
| 0.40% | `libsqlite3.so.0.8.6` | `sqlite3BtreeCursorHasMoved` | library |
| 0.39% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.38% | `python` | `_Py_dict_lookup` | lookup |
| 0.38% | `libsqlite3.so.0.8.6` | `sqlite3VdbeHalt` | library |
| 0.37% | `python` | `pthread_mutex_lock@plt` | unknown |
| 0.37% | `python` | `PyTuple_New` | memory |
| 0.37% | `python` | `_PyDict_GetItemRef_KnownHash_LockHeld` | dict |
| 0.37% | `_sqlite3.cpython-316-aarch64-linux-gnu.so` | `bind_param` | library |
| 0.34% | `_sqlite3.cpython-316-aarch64-linux-gnu.so` | `_pysqlite_fetch_one_row.constprop.0` | library |
| 0.34% | `python` | `list_dealloc` | memory |
| 0.33% | `libsqlite3.so.0.8.6` | `sqlite3PcacheRelease` | library |
| 0.33% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.33% | `python` | `PyMethod_New` | memory |
| 0.32% | `python` | `_PyEval_ReleaseLock` | interpreter |
| 0.31% | `python` | `_PyCompactLong_Add` | unknown |
| 0.30% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.30% | `libsqlite3.so.0.8.6` | `0x00000000000a10c0` | library |
| 0.30% | `python` | `bounded_lru_cache_wrapper` | unknown |
| 0.29% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.29% | `libsqlite3.so.0.8.6` | `sqlite3VdbeOneByteSerialTypeLen` | library |
| 0.29% | `_sqlite3.cpython-316-aarch64-linux-gnu.so` | `_pysqlite_build_py_params` | library |
| 0.28% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.27% | `python` | `pthread_cond_signal@plt` | unknown |
| 0.27% | `libsqlite3.so.0.8.6` | `sqlite3_column_type` | library |
| 0.27% | `python` | `PyObject_CallObject` | dynamic |
| 0.26% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.26% | `libsqlite3.so.0.8.6` | `sqlite3BtreeNext` | library |
| 0.26% | `libc.so.6` | `__memset_zva64` | libc |
| 0.25% | `libsqlite3.so.0.8.6` | `sqlite3_reset` | library |
| 0.25% | `libsqlite3.so.0.8.6` | `sqlite3VdbeMemTooBig` | library |
| 0.25% | `_sqlite3.cpython-316-aarch64-linux-gnu.so` | `pysqlite_connection_execute` | library |
| 0.25% | `python` | `PyObject_Malloc` | dynamic |

## sympy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 12.73% | `[JIT]` | `jit` | jit |
| 11.96% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.38% | `python` | `_PyTypeCache_Lookup` | unknown |
| 2.57% | `python` | `_Py_dict_lookup` | lookup |
| 2.39% | `python` | `_Py_Dealloc` | memory |
| 2.27% | `python` | `_PyObject_Malloc` | memory |
| 2.20% | `python` | `tuple_dealloc` | memory |
| 2.05% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.03% | `python` | `initialize_locals` | interpreter |
| 2.02% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.96% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.65% | `python` | `tuple_alloc` | memory |
| 1.61% | `python` | `_PyObject_Free` | memory |
| 1.58% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.49% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.47% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 1.31% | `python` | `_PyJIT_Entry` | compiler |
| 1.29% | `python` | `PyType_IsSubtype` | dynamic |
| 1.07% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.93% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.91% | `python` | `PyDict_GetItemRef` | dict |
| 0.87% | `python` | `_PyEval_Vector` | interpreter |
| 0.85% | `python` | `insertdict` | dict |
| 0.77% | `python` | `_Py_NewReference` | memory |
| 0.72% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.70% | `python` | `PyUnicode_RichCompare` | str |
| 0.67% | `python` | `PyTuple_FromArray.part.0` | tuple |
| 0.60% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.60% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.60% | `python` | `_Py_type_getattro_stackref` | unknown |
| 0.57% | `python` | `dictiter_iternextitem` | dict |
| 0.50% | `python` | `PyCMethod_New` | memory |
| 0.49% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.49% | `python` | `_PyType_GetDict` | dynamic |
| 0.48% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.47% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.44% | `python` | `_Py_VectorCallInstrumentation_StackRefSteal` | unknown |
| 0.43% | `python` | `PyDict_Next` | dict |
| 0.43% | `python` | `slot_tp_richcompare` | dynamic |
| 0.43% | `python` | `insert_to_emptydict` | dict |
| 0.40% | `python` | `PyObject_IsInstance` | dynamic |
| 0.39% | `python` | `dict_dealloc` | memory |
| 0.38% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 0.38% | `python` | `PyObject_GC_Del` | gc |
| 0.37% | `python` | `dict_merge` | dict |
| 0.36% | `python` | `setiter_iternext` | miscobj |
| 0.34% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.34% | `python` | `_PyObject_GC_New` | gc |
| 0.34% | `python` | `new_dict.constprop.0` | dict |
| 0.32% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.31% | `python` | `PyObject_Hash` | dynamic |
| 0.30% | `python` | `_PyStack_UnpackDict` | interpreter |
| 0.30% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.30% | `python` | `lookup_method_ex.constprop.0` | unknown |
| 0.30% | `python` | `_PyObject_GC_Link` | gc |
| 0.30% | `python` | `PyBool_FromLong` | miscobj |
| 0.29% | `python` | `PyList_New.constprop.0` | memory |
| 0.27% | `python` | `PyObject_IsTrue` | dynamic |
| 0.27% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.27% | `python` | `PyObject_RichCompare` | dynamic |
| 0.27% | `python` | `list_dealloc` | memory |
| 0.26% | `python` | `PyDict_SetItem` | dict |
| 0.25% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.25% | `libc.so.6` | `__memset_zva64` | libc |

## telco

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 7.72% | `[JIT]` | `jit` | jit |
| 5.02% | `python` | `_PyObject_Malloc` | memory |
| 4.10% | `python` | `_PyObject_Free` | memory |
| 3.49% | `python` | `_Py_Dealloc` | memory |
| 2.97% | `python` | `PyContextVar_Get` | unknown |
| 2.45% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 2.26% | `_decimal.cpython-316-aarch64-linux-gnu.so` | `nm_mpd_qadd` | library |
| 2.03% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.98% | `python` | `_PyObject_GC_New` | gc |
| 1.87% | `_decimal.cpython-316-aarch64-linux-gnu.so` | `nm_mpd_qmul` | library |
| 1.84% | `libmpdec.so.4.0.1` | `mpd_qfinalize` | library |
| 1.76% | `python` | `PyObject_GC_Del` | gc |
| 1.67% | `python` | `PyCMethod_New` | memory |
| 1.61% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.43% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.38% | `python` | `_PyObject_GC_Link` | gc |
| 1.32% | `python` | `_PyArg_UnpackKeywords` | calls |
| 1.24% | `libmpdec.so.4.0.1` | `mpd_qquantize` | library |
| 1.17% | `python` | `PyObject_GC_Track` | gc |
| 1.17% | `python` | `_Py_NewReference` | memory |
| 1.08% | `python` | `PyObject_Free` | dynamic |
| 1.00% | `_decimal.cpython-316-aarch64-linux-gnu.so` | `dec_dealloc` | library |
| 0.95% | `_decimal.cpython-316-aarch64-linux-gnu.so` | `dec_addstatus` | library |
| 0.95% | `python` | `PyObject_Malloc` | dynamic |
| 0.88% | `libmpdec.so.4.0.1` | `mpd_del` | library |
| 0.85% | `libc.so.6` | `__strlen_asimd` | libc |
| 0.82% | `_decimal.cpython-316-aarch64-linux-gnu.so` | `_decimal_Decimal_quantize` | library |
| 0.79% | `python` | `tuple_alloc` | memory |
| 0.74% | `python` | `PyType_GetBaseByToken` | unknown |
| 0.67% | `python` | `write_str` | unknown |
| 0.67% | `_decimal.cpython-316-aarch64-linux-gnu.so` | `dec_str` | library |
| 0.66% | `libmpdec.so.4.0.1` | `mpd_qshiftr` | library |
| 0.66% | `python` | `meth_dealloc` | memory |
| 0.63% | `python` | `PyDict_GetItemRef` | dict |
| 0.63% | `libmpdec.so.4.0.1` | `mpd_qadd` | library |
| 0.62% | `python` | `builtin_print` | unknown |
| 0.61% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.60% | `_decimal.cpython-316-aarch64-linux-gnu.so` | `_decimal_Context_quantize` | library |
| 0.58% | `python` | `PyObject_RichCompare` | dynamic |
| 0.55% | `python` | `PyNumber_Multiply` | dynamic |
| 0.55% | `python` | `PyObject_GetAttr` | dynamic |
| 0.54% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.54% | `python` | `method_get` | dynamic |
| 0.53% | `_struct.cpython-316-aarch64-linux-gnu.so` | `s_unpack_internal` | library |
| 0.53% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.52% | `python` | `PyType_IsSubtype` | dynamic |
| 0.48% | `python` | `PyUnicode_AsUCS4` | str |
| 0.47% | `python` | `_PyUnicode_Equal` | str |
| 0.46% | `python` | `PyLong_FromSsize_t` | int |
| 0.46% | `python` | `_PyLong_FromMedium` | int |
| 0.45% | `libmpdec.so.4.0.1` | `mpd_qsset_ssize` | library |
| 0.45% | `python` | `_Py_dict_lookup` | lookup |
| 0.44% | `python` | `PyErr_CheckSignals` | exceptions |
| 0.44% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.43% | `python` | `_PyErr_CheckSignalsTstate` | exceptions |
| 0.43% | `_struct.cpython-316-aarch64-linux-gnu.so` | `cache_struct_converter.constprop.0` | library |
| 0.42% | `python` | `PyThread_get_thread_ident` | threading |
| 0.42% | `python` | `binary_op1` | unknown |
| 0.41% | `python` | `PyObject_Str` | dynamic |
| 0.41% | `python` | `_Py_convert_optional_to_ssize_t` | unknown |
| 0.39% | `python` | `PyUnicode_CompareWithASCIIString` | str |
| 0.38% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 0.38% | `python` | `PyFile_WriteObject` | unknown |
| 0.37% | `_struct.cpython-316-aarch64-linux-gnu.so` | `unpack` | library |
| 0.37% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.37% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.36% | `python` | `unicode_dealloc` | memory |
| 0.36% | `python` | `PyNumber_InPlaceAdd` | dynamic |
| 0.35% | `libc.so.6` | `memcmp` | libc |
| 0.35% | `libmpdec.so.4.0.1` | `mpd_qset_ssize` | library |
| 0.35% | `python` | `cfunction_vectorcall_O` | calls |
| 0.34% | `_decimal.cpython-316-aarch64-linux-gnu.so` | `dec_from_long` | library |
| 0.34% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.33% | `libmpdec.so.4.0.1` | `mpd_digits_to_size` | library |
| 0.32% | `python` | `_PyRunRemoteDebugger` | unknown |
| 0.32% | `python` | `tuple_dealloc` | memory |
| 0.31% | `python` | `PyUnicode_New` | memory |
| 0.31% | `python` | `PyFile_WriteString` | unknown |
| 0.30% | `python` | `PyType_GetModuleByDef` | dynamic |
| 0.29% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.29% | `python` | `method_vectorcall_FASTCALL_KEYWORDS_METHOD` | calls |
| 0.27% | `_decimal.cpython-316-aarch64-linux-gnu.so` | `PyDecType_FromLongExact` | library |
| 0.26% | `_struct.cpython-316-aarch64-linux-gnu.so` | `bu_ulonglong` | library |
| 0.26% | `python` | `unicodekeys_lookup_unicode` | lookup |

## thrift

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 15.65% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.34% | `[JIT]` | `jit` | jit |
| 3.04% | `python` | `_PyObject_Malloc` | memory |
| 3.01% | `apache::thrift::py::TType,` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::encodeValue(_object*,` | unknown |
| 2.74% | `python` | `initialize_locals` | interpreter |
| 2.65% | `python` | `_PyObject_Free` | memory |
| 2.40% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.11% | `python` | `_PyTypeCache_Lookup` | unknown |
| 2.11% | `python` | `_Py_dict_lookup` | lookup |
| 1.96% | `python` | `_Py_Dealloc` | memory |
| 1.71% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.70% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.64% | `python` | `insert_to_emptydict` | dict |
| 1.62% | `python` | `insertdict` | dict |
| 1.46% | `python` | `PyDict_GetItemRef` | dict |
| 1.21% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 1.20% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.10% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.09% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 1.08% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.03% | `python` | `PyLong_AsLong` | int |
| 1.02% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.99% | `python` | `tuple_dealloc` | memory |
| 0.97% | `python` | `subtype_dealloc` | memory |
| 0.92% | `int)` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readBytes(char**,` | unknown |
| 0.90% | `_object*)` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::decodeValue(apache::thrift::py::TType,` | unknown |
| 0.87% | `python` | `_PyEval_Vector` | interpreter |
| 0.83% | `python` | `_PyStack_UnpackDict` | interpreter |
| 0.81% | `python` | `PyDict_Next` | dict |
| 0.81% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.78% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.72% | `python` | `_PyType_GetDict` | dynamic |
| 0.70% | `_object*,` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readStruct(_object*,` | unknown |
| 0.69% | `short&)` | `apache::thrift::py::BinaryProtocol::readFieldBegin(apache::thrift::py::TType&,` | unknown |
| 0.68% | `libc.so.6` | `__memset_zva64` | libc |
| 0.68% | `python` | `tuple_alloc` | memory |
| 0.65% | `python` | `dict_dealloc` | memory |
| 0.60% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.60% | `python` | `PyDict_SetItem` | dict |
| 0.59% | `python` | `_Py_NewReference` | memory |
| 0.59% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.59% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.54% | `python` | `PyDict_New` | memory |
| 0.52% | `python` | `PyUnicode_RichCompare` | str |
| 0.49% | `python` | `PyObject_GC_Del` | gc |
| 0.49% | `python` | `unicode_from_format` | str |
| 0.48% | `python` | `PyType_GenericAlloc` | memory |
| 0.47% | `python` | `object_vacall` | dynamic |
| 0.45% | `python` | `_PyObject_VectorcallDictTstate` | dynamic |
| 0.44% | `python` | `PyImport_ImportModuleLevelObject` | import |
| 0.43% | `python` | `vgetargs1_impl` | calls |
| 0.43% | `python` | `convertitem.constprop.0` | unknown |
| 0.42% | `python` | `PyObject_Call` | dynamic |
| 0.42% | `python` | `PyTuple_Size` | tuple |
| 0.40% | `python` | `_PyJIT_Entry` | compiler |
| 0.40% | `python` | `find_empty_slot` | dict |
| 0.40% | `python` | `_PyObject_Realloc` | memory |
| 0.38% | `_object*)` | `apache::thrift::py::parse_struct_item_spec(apache::thrift::py::StructItemSpec*,` | unknown |
| 0.37% | `python` | `_PyThreadState_PushFrame` | threading |
| 0.37% | `python` | `PyObject_GetAttr` | dynamic |
| 0.36% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.36% | `python` | `PyObject_Free` | dynamic |
| 0.36% | `python` | `PyList_New` | memory |
| 0.35% | `python` | `PyObject_Malloc` | dynamic |
| 0.35% | `python` | `_PyDict_FromItems` | dict |
| 0.34% | `python` | `_PyObject_Calloc` | memory |
| 0.33% | `python` | `new_dict.constprop.0` | dict |
| 0.33% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.32% | `python` | `_PyEval_ImportName` | interpreter |
| 0.32% | `python` | `_PyDict_Next` | dict |
| 0.32% | `libc.so.6` | `strchr` | libc |
| 0.31% | `python` | `list_dealloc` | memory |
| 0.31% | `python` | `_PyObject_InitInlineValues` | dynamic |
| 0.31% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.30% | `python` | `dict_merge` | dict |
| 0.30% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.30% | `python` | `PyErr_Format` | exceptions |
| 0.29% | `python` | `PyTuple_FromArray.part.0` | tuple |
| 0.29% | `python` | `_Py_module_getattro_impl` | unknown |
| 0.29% | `python` | `PyTuple_New` | memory |
| 0.29% | `python` | `PyMethod_New` | memory |
| 0.29% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.29% | `python` | `type_call` | dynamic |
| 0.28% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.28% | `python` | `PyMem_Free` | memory |
| 0.27% | `python` | `PyObject_CallMethodObjArgs` | dynamic |
| 0.26% | `python` | `new_keys_object` | dict |
| 0.26% | `python` | `slot_tp_init` | unknown |
| 0.26% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.25% | `fastbinary.cpython-316-aarch64-linux-gnu.so` | `decode_binary` | library |

## tomli_loads

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.06% | `[JIT]` | `jit` | jit |
| 4.72% | `python` | `set_lookkey` | miscobj |
| 4.38% | `python` | `_PyCompactLong_Add` | unknown |
| 3.90% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.88% | `python` | `_PyUnicode_Equal` | str |
| 2.62% | `python` | `_PySet_Contains` | miscobj |
| 2.37% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.00% | `python` | `_Py_dict_lookup` | lookup |
| 1.96% | `libc.so.6` | `memcmp` | libc |
| 1.78% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.60% | `python` | `_PyObject_Malloc` | memory |
| 1.55% | `python` | `_PyLong_ExactDealloc` | memory |
| 1.40% | `python` | `PyObject_Hash` | dynamic |
| 1.17% | `python` | `_Py_NewReference` | memory |
| 1.13% | `python` | `_PyDict_Subscript` | dict |
| 1.07% | `python` | `_Py_Dealloc` | memory |
| 1.06% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.98% | `python` | `unicode_hash` | str |
| 0.93% | `python` | `_PyIncrementalNewlineDecoder_decode` | memory |
| 0.91% | `python` | `_PyObject_Free` | memory |
| 0.86% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.82% | `python` | `_PyUnicode_FromUCS4.part.0` | str |
| 0.80% | `python` | `tuple_alloc` | memory |
| 0.77% | `python` | `PyObject_GetItem` | dynamic |
| 0.76% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.72% | `python` | `_PyTuple_FromStackRefStealOnSuccess` | tuple |
| 0.68% | `python` | `tuple_dealloc` | memory |
| 0.57% | `python` | `long_dealloc` | memory |
| 0.56% | `python` | `replace` | str |
| 0.55% | `python` | `sre_ucs4_match` | library |
| 0.52% | `python` | `PyDict_Contains` | dict |
| 0.50% | `python` | `_PyJIT_Entry` | compiler |
| 0.46% | `python` | `initialize_locals` | interpreter |
| 0.45% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 0.41% | `python` | `memcmp@plt` | unknown |
| 0.40% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.40% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.38% | `python` | `_PyType_GetDict` | dynamic |
| 0.37% | `python` | `PyType_IsSubtype` | dynamic |
| 0.36% | `python` | `_PyStolenTuple_Free` | unknown |
| 0.34% | `[kernel.kallsyms]` | `__pi_clear_page` | kernel |
| 0.34% | `python` | `PyDict_GetItemRef` | dict |
| 0.33% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.32% | `python` | `unicode_decode_utf8_impl` | str |
| 0.31% | `python` | `_PyEval_UnpackIndices` | interpreter |
| 0.29% | `python` | `object_isinstance` | dynamic |
| 0.28% | `python` | `tuple_subscript` | tuple |
| 0.28% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.27% | `[kernel.kallsyms]` | `el0_da` | kernel |
| 0.27% | `python` | `make_range_object` | unknown |
| 0.27% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.27% | `python` | `siphash13` | str |
| 0.26% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.26% | `python` | `PyUnicode_New.part.0` | memory |
| 0.25% | `python` | `_PyEval_SliceIndexNotNone` | interpreter |

## tornado_http

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.40% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.43% | `[JIT]` | `jit` | jit |
| 2.32% | `python` | `_PyObject_Malloc` | memory |
| 1.97% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.96% | `python` | `_PyTypeCache_Lookup` | unknown |
| 1.87% | `libc.so.6` | `__memcpy_generic` | libc |
| 1.46% | `python` | `sre_ucs1_match` | library |
| 1.41% | `python` | `_Py_Dealloc` | memory |
| 1.37% | `python` | `_PyObject_Free` | memory |
| 1.34% | `python` | `initialize_locals` | interpreter |
| 1.05% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.05% | `[kernel.kallsyms]` | `_raw_spin_unlock_irqrestore` | kernel |
| 0.94% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.79% | `python` | `tuple_dealloc` | memory |
| 0.77% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.76% | `python` | `_Py_dict_lookup` | lookup |
| 0.75% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.71% | `python` | `tuple_alloc` | memory |
| 0.67% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.65% | `[kernel.kallsyms]` | `__arch_copy_to_user` | kernel |
| 0.65% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.62% | `python` | `_PyJIT_Entry` | compiler |
| 0.58% | `python` | `_PyEval_Vector` | interpreter |
| 0.57% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 0.56% | `[kernel.kallsyms]` | `handle_softirqs` | kernel |
| 0.55% | `[kernel.kallsyms]` | `arch_local_irq_restore` | kernel |
| 0.49% | `[kernel.kallsyms]` | `el0_svc` | kernel |
| 0.49% | `libc.so.6` | `__memset_zva64` | libc |
| 0.44% | `python` | `sre_ucs1_count` | library |
| 0.42% | `[kernel.kallsyms]` | `__arch_copy_from_user` | kernel |
| 0.41% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.40% | `[kernel.kallsyms]` | `__update_cpu_freelist_fast` | kernel |
| 0.38% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.38% | `python` | `PyObject_GC_Del` | gc |
| 0.37% | `libc.so.6` | `__aarch64_swp4_rel` | libc |
| 0.37% | `python` | `PyType_IsSubtype` | dynamic |
| 0.36% | `libc.so.6` | `_int_malloc` | libc |
| 0.36% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.35% | `libc.so.6` | `__aarch64_cas4_acq` | libc |
| 0.35% | `python` | `_Py_NewReference` | memory |
| 0.33% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.31% | `python` | `sre_search` | library |
| 0.28% | `python` | `PyDict_GetItemRef` | dict |
| 0.26% | `python` | `_PyType_GetDict` | dynamic |
| 0.26% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.26% | `python` | `_PyFunction_Vectorcall` | calls |

## typing_runtime_protocols

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 16.07% | `[JIT]` | `jit` | jit |
| 6.81% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.91% | `python` | `_PyTypeCache_Lookup` | unknown |
| 3.54% | `python` | `_PyObject_Malloc` | memory |
| 2.80% | `python` | `_Py_Dealloc` | memory |
| 2.37% | `python` | `tuple_dealloc` | memory |
| 2.22% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.21% | `python` | `_Py_dict_lookup` | lookup |
| 2.21% | `python` | `PyArg_UnpackTuple` | calls |
| 2.21% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 2.15% | `python` | `weakref___new__` | memory |
| 2.11% | `python` | `_PyObject_Free` | memory |
| 1.97% | `python` | `PyTuple_FromArray.part.0` | tuple |
| 1.66% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.66% | `python` | `_Py_type_getattro_stackref` | unknown |
| 1.64% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 1.57% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 1.39% | `python` | `tuple_alloc` | memory |
| 1.30% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.15% | `python` | `set_lookkey` | miscobj |
| 1.03% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.00% | `python` | `_Py_BuiltinCallFast_StackRef` | unknown |
| 0.95% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.91% | `python` | `frame_dealloc` | memory |
| 0.86% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.84% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.82% | `python` | `initialize_locals` | interpreter |
| 0.81% | `python` | `_Py_NewReference` | memory |
| 0.80% | `python` | `wrap_descr_get` | unknown |
| 0.72% | `python` | `_PyObject_GC_New` | gc |
| 0.71% | `python` | `getset_get` | dynamic |
| 0.70% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.70% | `python` | `PyObject_GC_Del` | gc |
| 0.68% | `python` | `PySequence_Contains` | dynamic |
| 0.66% | `python` | `PyType_IsSubtype` | dynamic |
| 0.62% | `python` | `PyObject_Hash` | dynamic |
| 0.60% | `python` | `type_call` | dynamic |
| 0.57% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.50% | `python` | `_abc__abc_instancecheck` | unknown |
| 0.50% | `python` | `PyWeakref_NewRef` | memory |
| 0.46% | `python` | `_PyObject_GC_Link` | gc |
| 0.45% | `python` | `PyDictProxy_New` | memory |
| 0.44% | `python` | `setiter_iternext` | miscobj |
| 0.44% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.44% | `python` | `PyObject_Malloc` | dynamic |
| 0.44% | `python` | `lru_cache_make_key` | unknown |
| 0.43% | `python` | `bounded_lru_cache_wrapper` | unknown |
| 0.43% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.43% | `python` | `PyList_New.constprop.0` | memory |
| 0.43% | `python` | `tuple_hash` | tuple |
| 0.42% | `python` | `weakref_hash` | miscobj |
| 0.41% | `python` | `_PyJIT_Entry` | compiler |
| 0.41% | `python` | `vgetargskeywords_impl.constprop.0` | unknown |
| 0.38% | `python` | `object_richcompare` | dynamic |
| 0.38% | `python` | `PyTraceBack_Here` | exceptions |
| 0.38% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.38% | `python` | `PyErr_GetRaisedException` | exceptions |
| 0.38% | `python` | `_PyStaticType_GetState` | unknown |
| 0.37% | `python` | `builtin_getattr` | lookup |
| 0.35% | `python` | `PyMapping_Check` | dynamic |
| 0.32% | `python` | `PyObject_Free` | dynamic |
| 0.32% | `python` | `_PyEval_Vector` | interpreter |
| 0.32% | `python` | `get_exception_handler.isra.0` | unknown |
| 0.32% | `python` | `weakref___init__` | miscobj |
| 0.31% | `python` | `PyDict_Contains` | dict |
| 0.31% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.31% | `python` | `dict_get` | dict |
| 0.31% | `python` | `mappingproxy_dealloc` | memory |
| 0.30% | `python` | `type_get_mro` | dynamic |
| 0.30% | `python` | `PyTuple_FromArray` | tuple |
| 0.30% | `python` | `_PyDict_GetItemRef_KnownHash` | dict |
| 0.29% | `python` | `_PyDict_GetItemRef_KnownHash_LockHeld` | dict |
| 0.29% | `python` | `PyMethod_New` | memory |
| 0.28% | `python` | `tuple_richcompare` | tuple |
| 0.27% | `python` | `list_dealloc` | memory |
| 0.27% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 0.27% | `python` | `new_dict.constprop.0` | dict |
| 0.27% | `python` | `PySet_Contains` | miscobj |
| 0.26% | `python` | `AttributeError_init` | exceptions |
| 0.26% | `python` | `_PyObject_VectorcallPrepend` | dynamic |
| 0.26% | `python` | `PyObject_IsInstance` | dynamic |
| 0.25% | `python` | `subtype_dict` | unknown |

## unpickle_pure_python

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 38.06% | `[JIT]` | `jit` | jit |
| 5.65% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.44% | `python` | `_PyCallMethodDescriptorFast_StackRef` | unknown |
| 2.85% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.35% | `python` | `_PyObject_Malloc` | memory |
| 2.34% | `python` | `PyObject_IsTrue` | dynamic |
| 2.34% | `python` | `_Py_dict_lookup` | lookup |
| 2.16% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 1.97% | `python` | `_io_BytesIO_read` | unknown |
| 1.96% | `python` | `_PyDict_Subscript` | dict |
| 1.94% | `python` | `PyObject_GetItem` | dynamic |
| 1.90% | `python` | `_Py_convert_optional_to_ssize_t` | unknown |
| 1.81% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.62% | `python` | `_PyObject_Free` | memory |
| 1.54% | `python` | `insertdict` | dict |
| 1.44% | `python` | `bytes_subscript` | str |
| 1.37% | `python` | `PyUnicode_Decode` | str |
| 1.13% | `python` | `PyLong_AsSsize_t` | int |
| 1.03% | `python` | `PyLong_FromSsize_t` | int |
| 1.02% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.96% | `python` | `PyObject_IsInstance` | dynamic |
| 0.94% | `python` | `unicode_vectorcall` | str |
| 0.78% | `python` | `bytes_length` | str |
| 0.76% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.72% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.69% | `python` | `PyObject_Size` | dynamic |
| 0.60% | `python` | `_Py_Dealloc` | memory |
| 0.57% | `python` | `_PyJIT_Entry` | compiler |
| 0.51% | `python` | `long_hash` | int |
| 0.49% | `python` | `_Py_CallBuiltinClass_StackRef` | unknown |
| 0.46% | `python` | `PyUnicode_New.part.0` | memory |
| 0.46% | `python` | `_PyDict_StoreSubscript` | dict |
| 0.44% | `python` | `PyUnicode_AsUTF8AndSize` | str |
| 0.43% | `python` | `PyObject_Hash` | dynamic |
| 0.43% | `python` | `initialize_locals` | interpreter |
| 0.42% | `python` | `list_subscript` | list |
| 0.41% | `python` | `list_append` | list |
| 0.40% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.39% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.39% | `python` | `find_first_nonascii` | str |
| 0.35% | `python` | `PyObject_Malloc` | dynamic |
| 0.34% | `python` | `PyObject_SetItem` | dynamic |
| 0.34% | `python` | `siphash13` | str |
| 0.32% | `python` | `object_recursive_isinstance` | dynamic |
| 0.29% | `python` | `PyUnicode_FromEncodedObject` | str |
| 0.29% | `python` | `dictkeys_decref.part.0.constprop.0` | dict |
| 0.28% | `python` | `find_empty_slot` | dict |
| 0.28% | `python` | `_Py_NewReference` | memory |
| 0.28% | `libc.so.6` | `__strlen_asimd` | libc |
| 0.28% | `python` | `_PyTypeCache_Lookup` | unknown |
| 0.26% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.26% | `python` | `_PyObject_Realloc` | memory |

## xdsl

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 15.59% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.63% | `[JIT]` | `jit` | jit |
| 4.62% | `python` | `gc_collect_main` | gc |
| 4.30% | `python` | `_PyTypeCache_Lookup` | unknown |
| 3.49% | `python` | `_PyObject_Malloc` | memory |
| 2.43% | `python` | `_Py_Dealloc` | memory |
| 1.90% | `python` | `_PyObject_Free` | memory |
| 1.87% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.80% | `python` | `tuple_dealloc` | memory |
| 1.77% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.42% | `python` | `_Py_dict_lookup` | lookup |
| 1.33% | `python` | `initialize_locals` | interpreter |
| 1.24% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 1.20% | `python` | `visit_decref` | gc |
| 1.16% | `python` | `tuple_alloc` | memory |
| 1.16% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.11% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 1.11% | `python` | `PyDict_GetItemRef` | dict |
| 1.02% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.01% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.89% | `python` | `PyObject_SetAttr` | dynamic |
| 0.88% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.81% | `python` | `_PyJIT_Entry` | compiler |
| 0.77% | `python` | `_PyType_AllocNoTrack` | memory |
| 0.73% | `python` | `_Py_VectorCall_StackRefSteal` | unknown |
| 0.72% | `python` | `_Py_NewReference` | memory |
| 0.69% | `python` | `_PyEval_Vector` | interpreter |
| 0.68% | `python` | `unicode_from_format` | str |
| 0.67% | `python` | `dict_traverse` | gc |
| 0.66% | `python` | `visit_reachable` | gc |
| 0.63% | `python` | `set_lookkey` | miscobj |
| 0.62% | `python` | `_PyType_GetDict` | dynamic |
| 0.62% | `libc.so.6` | `strchr` | libc |
| 0.57% | `python` | `PyTuple_FromArray.part.0` | tuple |
| 0.54% | `python` | `subtype_traverse` | gc |
| 0.53% | `python` | `PyType_IsSubtype` | dynamic |
| 0.53% | `python` | `PyObject_GC_Del` | gc |
| 0.49% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.47% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.46% | `python` | `_PyThreadState_PopFrame` | threading |
| 0.44% | `python` | `_PyUnicode_InternMortal` | str |
| 0.43% | `python` | `PyErr_Format` | exceptions |
| 0.43% | `python` | `PyType_GenericAlloc` | memory |
| 0.42% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.42% | `python` | `PyObject_Malloc` | dynamic |
| 0.40% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.39% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.38% | `python` | `_PyObject_GC_Link` | gc |
| 0.35% | `python` | `_abc__abc_instancecheck` | unknown |
| 0.34% | `python` | `_Py_type_getattro_stackref` | unknown |
| 0.34% | `python` | `vgetargskeywords_impl.constprop.0` | unknown |
| 0.34% | `python` | `PyObject_Free` | dynamic |
| 0.32% | `python` | `PyWeakref_NewRef` | memory |
| 0.31% | `python` | `PyErr_ExceptionMatches` | exceptions |
| 0.31% | `python` | `store_instance_attr_lock_held` | unknown |
| 0.30% | `python` | `subtype_dealloc` | memory |
| 0.30% | `python` | `_PyObject_Realloc` | memory |
| 0.30% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.30% | `libc.so.6` | `__memset_zva64` | libc |
| 0.29% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.28% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.28% | `python` | `type_call` | dynamic |
| 0.27% | `libc.so.6` | `__strlen_asimd` | libc |
| 0.26% | `python` | `_PyStaticType_GetState` | unknown |
| 0.26% | `python` | `PyTuple_New` | memory |
| 0.26% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |

## xml_etree

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 7.43% | `[JIT]` | `jit` | jit |
| 5.37% | `python` | `_PyObject_Malloc` | memory |
| 5.32% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.50% | `pyexpat.cpython-316-aarch64-linux-gnu.so` | `normal_updatePosition` | library |
| 3.38% | `pyexpat.cpython-316-aarch64-linux-gnu.so` | `accountingDiffTolerated.part.0` | library |
| 3.27% | `pyexpat.cpython-316-aarch64-linux-gnu.so` | `normal_contentTok` | library |
| 2.69% | `python` | `_PyTypeCache_Lookup` | unknown |
| 2.31% | `python` | `_PyObject_Free` | memory |
| 2.30% | `pyexpat.cpython-316-aarch64-linux-gnu.so` | `doContent` | library |
| 2.04% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.65% | `python` | `gc_collect_main` | gc |
| 1.60% | `python` | `visit_reachable` | gc |
| 1.50% | `python` | `_Py_Dealloc` | memory |
| 1.47% | `python` | `visit_decref` | gc |
| 1.20% | `pyexpat.cpython-316-aarch64-linux-gnu.so` | `sip24_update.isra.0` | library |
| 1.20% | `pyexpat.cpython-316-aarch64-linux-gnu.so` | `storeAtts` | library |
| 1.16% | `python` | `_io_TextIOWrapper_write` | unknown |
| 1.11% | `python` | `_PyType_LookupStackRefAndVersion` | unknown |
| 1.10% | `_elementtree.cpython-316-aarch64-linux-gnu.so` | `element_gc_traverse` | library |
| 1.08% | `pyexpat.cpython-316-aarch64-linux-gnu.so` | `normal_nameLength` | library |
| 1.03% | `python` | `initialize_locals` | interpreter |
| 1.01% | `pyexpat.cpython-316-aarch64-linux-gnu.so` | `normal_getAtts` | library |
| 1.00% | `libc.so.6` | `__memcpy_generic` | libc |
| 0.96% | `python` | `_Py_dict_lookup` | lookup |
| 0.92% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.91% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.90% | `python` | `_PyJIT_Entry` | compiler |
| 0.77% | `python` | `PyUnicode_Contains` | str |
| 0.76% | `python` | `PyUnicode_New.part.0` | memory |
| 0.75% | `_elementtree.cpython-316-aarch64-linux-gnu.so` | `treebuilder_handle_start` | library |
| 0.74% | `pyexpat.cpython-316-aarch64-linux-gnu.so` | `sip24_final` | library |
| 0.70% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.69% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.67% | `python` | `_PyType_GetDict` | dynamic |
| 0.67% | `python` | `_Py_NewReference` | memory |
| 0.67% | `python` | `PyObject_Malloc` | dynamic |
| 0.65% | `python` | `siphash13` | str |
| 0.64% | `python` | `list_dealloc` | memory |
| 0.64% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.64% | `python` | `tuple_dealloc` | memory |
| 0.63% | `python` | `getset_get` | dynamic |
| 0.61% | `_elementtree.cpython-316-aarch64-linux-gnu.so` | `element_dealloc` | library |
| 0.60% | `python` | `_PyObject_GetMethodStackRef` | dynamic |
| 0.59% | `pyexpat.cpython-316-aarch64-linux-gnu.so` | `lookupWithLength` | library |
| 0.58% | `_elementtree.cpython-316-aarch64-linux-gnu.so` | `elementiter_next` | library |
| 0.56% | `libc.so.6` | `__strlen_asimd` | libc |
| 0.55% | `python` | `_PyObject_GetAttrStackRef` | dynamic |
| 0.53% | `python` | `_PyEval_Vector` | interpreter |
| 0.53% | `python` | `_copy_characters.constprop.0.isra.0` | str |
| 0.52% | `python` | `PyUnicode_Format` | str |
| 0.51% | `python` | `unicode_dealloc` | memory |
| 0.50% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.49% | `python` | `PyObject_Free` | dynamic |
| 0.48% | `_elementtree.cpython-316-aarch64-linux-gnu.so` | `expat_end_handler` | library |
| 0.44% | `python` | `PyType_IsSubtype` | dynamic |
| 0.43% | `python` | `_PyObject_GC_New` | gc |
| 0.41% | `python` | `PyObject_GC_Del` | gc |
| 0.40% | `libc.so.6` | `strncmp` | libc |
| 0.38% | `python` | `tuple_alloc` | memory |
| 0.38% | `python` | `long_to_decimal_string_internal` | int |
| 0.37% | `python` | `PyList_Append` | list |
| 0.36% | `python` | `PyUnicode_Concat` | str |
| 0.36% | `python` | `object_isinstance` | dynamic |
| 0.36% | `python` | `vgetargs1_impl` | calls |
| 0.36% | `_elementtree.cpython-316-aarch64-linux-gnu.so` | `element_getitem` | library |
| 0.35% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.34% | `pyexpat.cpython-316-aarch64-linux-gnu.so` | `utf8_toUtf8` | library |
| 0.32% | `_elementtree.cpython-316-aarch64-linux-gnu.so` | `expat_start_handler` | library |
| 0.31% | `python` | `PyErr_Occurred` | exceptions |
| 0.30% | `python` | `PyDescr_IsData` | dynamic |
| 0.28% | `python` | `_PyObject_GC_Link` | gc |
| 0.28% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.28% | `python` | `find_first_nonascii` | str |
| 0.27% | `python` | `PyList_New` | memory |
| 0.27% | `python` | `_PyObject_Realloc` | memory |
| 0.27% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.27% | `_elementtree.cpython-316-aarch64-linux-gnu.so` | `makeuniversal` | library |
| 0.25% | `python` | `_PyTuple_FromPair` | tuple |
| 0.25% | `python` | `PyDict_GetItemWithError` | dict |
| 0.25% | `python` | `convertitem.constprop.0` | unknown |


## Categories

### jit

17.19% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 17.19% | [JIT] | jit |

### memory

14.57% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 2.29% | python | _PyObject_Malloc |
| 1.94% | python | _Py_Dealloc |
| 1.69% | python | _PyObject_Free |
| 1.34% | python | tuple_dealloc |
| 0.89% | python | tuple_alloc |
| 0.81% | python | _Py_NewReference |
| 0.76% | python | list_dealloc |
| 0.42% | python | PyList_New.constprop.0 |
| 0.23% | python | _PyType_AllocNoTrack |
| 0.21% | python | gen_dealloc |
| 0.21% | python | _PyObject_Realloc |
| 0.21% | python | PyTuple_New |
| 0.18% | python | long_dealloc |
| 0.16% | python | PyType_GenericAlloc |
| 0.15% | python | PyCMethod_New |
| 0.14% | python | _PyLong_ExactDealloc |
| 0.13% | python | subtype_dealloc |
| 0.13% | python | PyMem_Free |
| 0.13% | python | unicode_dealloc |
| 0.13% | python | listiter_dealloc |
| 0.12% | python | PyMethod_New |
| 0.12% | python | zip_new |
| 0.11% | python | PyUnicode_New.part.0 |
| 0.11% | python | float_dealloc |
| 0.09% | python | PyObject_CallFinalizerFromDealloc |
| 0.09% | python | dict_dealloc |
| 0.08% | python | _PyFloat_ExactDealloc |
| 0.08% | python | PyUnicode_New |
| 0.08% | python | PyList_New |
| 0.08% | python | _PyObject_Calloc |
| 0.08% | python | method_dealloc |
| 0.07% | python | PyFunction_NewWithQualName |
| 0.07% | python | PySlice_New |
| 0.07% | python | meth_dealloc |
| 0.07% | python | memcpy@plt |
| 0.06% | python | PyMem_Realloc |
| 0.06% | python | slice_dealloc |
| 0.06% | python | PyMem_Malloc |
| 0.06% | python | _PyIncrementalNewlineDecoder_decode |
| 0.06% | python | long_alloc |
| 0.05% | python | zip_dealloc |
| 0.05% | python | async_gen_asend_dealloc |
| 0.05% | python | PyDict_New |
| 0.05% | python | set_dealloc |
| 0.04% | python | memset@plt |
| 0.04% | python | context_tp_dealloc |
| 0.04% | python | func_dealloc |
| 0.03% | python | object_dealloc |
| 0.03% | python | pattern_new_match |
| 0.02% | python | range_dealloc |
| 0.02% | python | _PyAsyncGenValueWrapperNew |
| 0.02% | python | async_gen_wrapped_val_dealloc |
| 0.02% | python | StopIteration_dealloc |
| 0.02% | python | tp_new_wrapper |
| 0.02% | python | allocate_from_new_pool |
| 0.02% | python | object_new |
| 0.01% | python | cell_dealloc |
| 0.01% | python | BaseException_new |
| 0.01% | python | PyMem_Calloc |
| 0.01% | python | PyCell_New |
| 0.01% | python | frame_dealloc |
| 0.01% | python | dictiter_dealloc |
| 0.01% | python | dictview_dealloc |
| 0.01% | python | rangeiter_dealloc |
| 0.01% | python | PyObject_Realloc |
| 0.01% | python | _PyMem_RawMalloc |
| 0.01% | python | weakref___new__ |
| 0.01% | python | _PyUnicode_ExactDealloc |
| 0.01% | python | PyFunction_New |
| 0.01% | python | _Py_NewReferenceNoTotal |
| 0.01% | python | tupleiter_dealloc |
| 0.01% | python | _PyMem_RawFree |
| 0.01% | python | BaseException_dealloc |
| 0.00% | python | slot_tp_new |
| 0.00% | python | code_dealloc |
| 0.00% | python | match_dealloc |
| 0.00% | python | future_new_iter |
| 0.00% | python | TaskObj_dealloc |
| 0.00% | python | TaskStepMethWrapper_dealloc |
| 0.00% | python | PyWeakref_NewRef |
| 0.00% | python | tb_dealloc |
| 0.00% | python | PyType_GenericNew |
| 0.00% | python | PySeqIter_New |
| 0.00% | python | AttributeError_dealloc |
| 0.00% | python | setiter_dealloc |

### interpreter

10.42% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 5.99% | python | _PyEval_EvalFrameDefault |
| 1.44% | python | _PyFrame_ClearExceptCode |
| 0.79% | python | initialize_locals |
| 0.74% | python | _PyEval_FrameClearAndPop |
| 0.53% | python | _PyEvalFramePushAndInit |
| 0.40% | python | _PyEval_Vector |
| 0.20% | python | _PyEval_SliceIndex |
| 0.06% | python | _PyFrame_Traverse |
| 0.03% | python | _PyStack_UnpackDict |
| 0.03% | python | _PyEval_UnpackIndices |
| 0.02% | python | call_instrumentation_vector.part.0.isra.0 |
| 0.02% | python | _PyCode_Quicken |
| 0.02% | python | _Py_call_instrumentation_line |
| 0.02% | python | _PyEval_SliceIndexNotNone |
| 0.01% | python | _PyEval_GetAwaitable |
| 0.01% | python | _PyEval_GetIter |
| 0.01% | python | _PyEvalFramePushAndInit_Ex |
| 0.01% | python | _PyPegen_expect_token |
| 0.01% | python | _PyEval_GetANext |
| 0.01% | python | _PyCode_CheckLineNumber |
| 0.01% | python | _PyPegen_is_memoized |
| 0.01% | python | _PyCode_New |
| 0.01% | python | _PyFrame_New_NoTrack |
| 0.01% | python | _PyFrame_MakeAndSetFrameObject |
| 0.00% | python | _PyEval_MonitorRaise |
| 0.00% | python | _PyEval_ImportName |
| 0.00% | python | _PyPegen_name_from_token |
| 0.00% | python | _PyCode_GetCode |
| 0.00% | python | _PyEval_LoadGlobalStackRef |
| 0.00% | python | PyEval_GetFrame |

### gc

9.49% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 3.14% | python | gc_collect_main |
| 1.45% | python | visit_reachable |
| 1.42% | python | visit_decref |
| 1.00% | python | PyObject_GC_UnTrack |
| 0.37% | python | list_traverse |
| 0.31% | python | PyObject_GC_Del |
| 0.28% | python | subtype_traverse |
| 0.24% | python | dict_traverse |
| 0.21% | python | _PyObject_GC_Link |
| 0.18% | python | _PyObject_GC_New |
| 0.12% | python | _PyGC_VisitFrameStack |
| 0.11% | python | _PyObject_GC_NewVar |
| 0.09% | python | tuple_traverse |
| 0.06% | python | TaskObj_traverse |
| 0.06% | python | gen_traverse |
| 0.06% | python | type_is_gc |
| 0.05% | python | _PyTuple_MaybeUntrack |
| 0.04% | python | _PyGC_VisitStackRef |
| 0.04% | python | PyObject_IS_GC |
| 0.03% | python | context_tp_traverse |
| 0.03% | python | func_traverse |
| 0.03% | python | set_traverse |
| 0.02% | python | TaskStepMethWrapper_traverse |
| 0.02% | python | FutureObj_traverse |
| 0.02% | python | PyObject_GC_Track |
| 0.02% | python | meth_traverse |
| 0.02% | python | type_traverse |
| 0.01% | python | method_traverse |
| 0.01% | python | FutureIter_traverse |
| 0.01% | python | cell_traverse |
| 0.00% | python | descr_traverse |
| 0.00% | python | gc_traverse |
| 0.00% | python | partial_traverse |

### unknown

8.10% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.58% | python | _PyTypeCache_Lookup |
| 0.67% | python | _PyCompactLong_Add |
| 0.51% | python | _PyType_LookupStackRefAndVersion |
| 0.43% | python | _Py_BuiltinCallFast_StackRef |
| 0.37% | python | _Py_VectorCall_StackRefSteal |
| 0.25% | python | _PyCompactLong_Subtract |
| 0.24% | python | zip_next |
| 0.19% | python | _Py_type_getattro_stackref |
| 0.15% | python | _PyStolenTuple_Free |
| 0.13% | python | _PyMember_GetOffset |
| 0.13% | python | _PyStaticType_GetState |
| 0.12% | python | slot_mp_ass_subscript |
| 0.11% | python | wrap_objobjargproc |
| 0.10% | python | _PyRunRemoteDebugger |
| 0.10% | python | clear_slots |
| 0.09% | python | lookup_method_ex.constprop.0 |
| 0.09% | python | builtin_sum |
| 0.09% | python | wrapperdescr_call |
| 0.08% | python | _PyCallMethodDescriptorFast_StackRef |
| 0.08% | python | _Py_IsMainThread |
| 0.08% | python | convertitem.constprop.0 |
| 0.07% | python | _PyForIter_VirtualIteratorNext |
| 0.07% | python | PySys_Audit |
| 0.06% | python | _PyCompactLong_Multiply |
| 0.06% | python | _PyInterpreterState_Main |
| 0.05% | python | func_clear |
| 0.05% | python | _PyInterpreterState_GetConfig |
| 0.05% | python | make_range_object |
| 0.05% | python | memcmp@plt |
| 0.05% | python | _Py_BuildString_StackRefSteal |
| 0.04% | python | _Py_BuildMap_StackRefSteal |
| 0.04% | python | PyIndex_Check |
| 0.04% | python | _PyAsyncGenASend_Send |
| 0.04% | python | _Py_bytes_upper |
| 0.04% | python | recursive_issubclass |
| 0.04% | python | _Py_BuiltinCallFastWithKeywords_StackRef |
| 0.04% | python | store_instance_attr_lock_held |
| 0.04% | python | _Py_CallBuiltinClass_StackRef |
| 0.04% | python | min_max |
| 0.04% | python | builtin_issubclass |
| 0.04% | python | _Py_VectorCallInstrumentation_StackRefSteal |
| 0.03% | python | _PySuper_LookupDescr |
| 0.03% | python | task_step_impl |
| 0.03% | python | gen_finalize |
| 0.03% | python | TaskObj_clear |
| 0.03% | python | _asyncio_Task___init__ |
| 0.03% | python | PyContext_CopyCurrent |
| 0.03% | python | _Py_LoadAttr_StackRefSteal |
| 0.03% | python | future_schedule_callbacks |
| 0.02% | python | pthread_self@plt |
| 0.02% | python | _Py_MakeCoro |
| 0.02% | python | _asyncio_future_discard_from_awaited_by |
| 0.02% | python | TaskStepMethWrapper_call |
| 0.02% | python | unsafe_long_compare |
| 0.02% | python | build_indices_generic |
| 0.02% | python | context_run |
| 0.02% | python | _io_TextIOWrapper_write |
| 0.02% | python | get_exception_handler.isra.0 |
| 0.02% | python | _PyContext_Exit |
| 0.02% | python | sys_audit_tstate |
| 0.02% | python | _PyCallMethodDescriptorFastWithKeywords_StackRef |
| 0.02% | python | Py_HashBuffer |
| 0.02% | python | wrapperdescr_get |
| 0.02% | python | pysiphash |
| 0.02% | python | vectorcall_maybe |
| 0.02% | python | _PyContext_Enter |
| 0.02% | python | clone_combined_dict_keys |
| 0.02% | python | _PyCoro_GetAwaitableIter |
| 0.02% | python | func_descr_get |
| 0.01% | python | PyBytesWriter_Create |
| 0.01% | python | slot_tp_init |
| 0.01% | python | map_next |
| 0.01% | python | _PyFunction_SetVersion |
| 0.01% | python | builtin_hasattr |
| 0.01% | python | task_wakeup |
| 0.01% | python | vgetargskeywords_impl.constprop.0 |
| 0.01% | python | unsafe_tuple_compare |
| 0.01% | python | charmaptranslate_lookup |
| 0.01% | python | __aarch64_ldclr8_acq_rel |
| 0.01% | python | builtin_repr |
| 0.01% | python | _PyIter_Send |
| 0.01% | python | builtin_id |
| 0.01% | python | maybe_small_long |
| 0.01% | python | supercheck |
| 0.01% | python | insert_split_key |
| 0.01% | python | task_call_step_soon |
| 0.01% | python | tailmatch |
| 0.01% | python | builtin_sorted |
| 0.01% | python | PyBytesWriter_FinishWithPointer |
| 0.01% | python | FutureObj_clear |
| 0.01% | python | _asyncio_future_add_to_awaited_by |
| 0.01% | python | compactlongs_guard |
| 0.01% | python | _PyLexer_get_normal |
| 0.01% | python | PyTime_AsSecondsDouble |
| 0.01% | python | compactlongs_and |
| 0.01% | python | dictitems_iter |
| 0.01% | python | PyType_GetModule |
| 0.01% | python | slot_sq_length |
| 0.01% | python | slot_nb_add |
| 0.01% | python | slot_tp_hash |
| 0.01% | python | bounded_lru_cache_wrapper |
| 0.01% | python | call_soon |
| 0.01% | python | lru_cache_make_key |
| 0.01% | python | future_add_done_callback |
| 0.01% | python | _Py_module_getattro_impl |
| 0.01% | python | _asyncio_Future_add_done_callback |
| 0.01% | python | partial_vectorcall |
| 0.01% | python | compactlong_float_subtract |
| 0.01% | python | merge_from_seq2_lock_held |
| 0.01% | python | binary_op1 |
| 0.01% | python | _PyOptimizer_Optimize |
| 0.01% | python | _Py_strhex_impl |
| 0.01% | python | _Py_slot_tp_getattr_hook |
| 0.01% | python | slot_sq_contains |
| 0.01% | python | setitem_take2_lock_held |
| 0.01% | python | _asyncio_Future___init__ |
| 0.01% | python | any_find_slice |
| 0.01% | python | slot_sq_item |
| 0.01% | python | nonzero_float_compactlong_guard |
| 0.01% | python | match_getslice_by_index |
| 0.01% | python | _PyTypeCache_Insert |
| 0.01% | python | do_mkvalue |
| 0.01% | python | gallop_left |
| 0.01% | python | merge_at |
| 0.00% | python | gallop_right |
| 0.00% | python | slot_nb_subtract |
| 0.00% | python | mro_implementation_unlocked |
| 0.00% | python | _asyncio_Future_cancelled |
| 0.00% | python | unsafe_object_compare |
| 0.00% | python | compactlong_float_guard |
| 0.00% | python | richcmp_eq |
| 0.00% | python | islice_next |
| 0.00% | python | _Py_Specialize_LoadAttr |
| 0.00% | python | slot_nb_bool |
| 0.00% | python | copy_lock_held_untracked |
| 0.00% | python | _PyJit_translate_single_bytecode_to_trace |
| 0.00% | python | slot_tp_iternext |
| 0.00% | python | iter_iternext |
| 0.00% | python | getset_set |
| 0.00% | python | task_step |
| 0.00% | python | hashtable_unicode_hash |
| 0.00% | python | _Py_convert_optional_to_ssize_t |
| 0.00% | python | _Py_bytes_contains |
| 0.00% | python | memmove@plt |
| 0.00% | python | int_bit_length |
| 0.00% | python | make_dict_from_instance_attributes |
| 0.00% | python | FutureIter_am_send |
| 0.00% | python | write_str |
| 0.00% | python | _PyBytes_Concat |
| 0.00% | python | _abc__abc_instancecheck |
| 0.00% | python | listreviter_next |
| 0.00% | apache::thrift::py::TType, | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::encodeValue(_object*, |
| 0.00% | python | _textiowrapper_writeflush |
| 0.00% | python | _Py_call_instrumentation |
| 0.00% | python | unsafe_latin_compare |
| 0.00% | python | malloc@plt |
| 0.00% | python | subtype_clear |
| 0.00% | python | __aarch64_cas1_acq_rel |
| 0.00% | python | PyContextVar_Get |
| 0.00% | python | _asyncio_Future_exception |
| 0.00% | python | PyBytesWriter_FinishWithSize |
| 0.00% | python | striter_next |
| 0.00% | python | match_getindex |
| 0.00% | python | _Py_call_instrumentation_arg |
| 0.00% | python | gen_close |
| 0.00% | python | match_group |
| 0.00% | python | property_descr_get |
| 0.00% | python | _PyArena_Malloc |
| 0.00% | python | free@plt |
| 0.00% | python | hashtable_unicode_compare |
| 0.00% | python | compute_range_item |
| 0.00% | python | _io_BytesIO_read |
| 0.00% | python | PyCallable_Check |
| 0.00% | python | _Py_bytes_lower |
| 0.00% | python | defdict_missing |
| 0.00% | python | _Py_uop_analyze_and_optimize |
| 0.00% | python | PyBytesWriter_GetData |
| 0.00% | python | import_ensure_initialized |
| 0.00% | python | _asyncio_Future_done |

### dynamic

7.71% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.05% | python | PyObject_RichCompareBool |
| 0.61% | python | _PyObject_GenericGetAttrWithDict |
| 0.38% | python | PyObject_GetItem |
| 0.36% | python | PyType_IsSubtype |
| 0.35% | python | PyObject_Hash |
| 0.29% | python | PyObject_Malloc |
| 0.27% | python | _PyObject_GetAttrStackRef |
| 0.24% | python | _PyObject_MakeTpCall |
| 0.24% | python | PyObject_Free |
| 0.21% | python | _PyType_GetDict |
| 0.20% | python | PyObject_GetOptionalAttr |
| 0.16% | python | _PyObject_TryGetInstanceAttribute |
| 0.15% | python | PyObject_SetItem |
| 0.14% | python | _PyObject_GetMethodStackRef |
| 0.13% | python | PyNumber_AsSsize_t |
| 0.13% | python | type_call |
| 0.12% | python | PyObject_VisitManagedDict |
| 0.12% | python | PyObject_CallOneArg |
| 0.12% | python | PyObject_Vectorcall |
| 0.11% | python | PyObject_GetIter |
| 0.10% | python | object_isinstance |
| 0.10% | python | PyObject_Size |
| 0.10% | python | PyObject_RichCompare |
| 0.10% | python | PyObject_IsInstance |
| 0.10% | python | PyObject_IsTrue |
| 0.09% | python | PyObject_ClearManagedDict |
| 0.08% | python | getset_get |
| 0.07% | python | PyDescr_IsData |
| 0.07% | python | PyObject_IsSubclass |
| 0.07% | python | PyObject_GenericSetAttr |
| 0.07% | python | slot_tp_richcompare |
| 0.07% | python | PyObject_SetAttr |
| 0.06% | python | _PyObject_LookupSpecial |
| 0.06% | python | PySequence_Fast |
| 0.06% | python | _PyObject_RealIsSubclass |
| 0.06% | python | _PyObject_VectorcallPrepend |
| 0.06% | python | PyObject_VectorcallMethod |
| 0.05% | python | PyObject_Call |
| 0.05% | python | PyObject_ClearWeakRefs |
| 0.04% | python | PyType_GetModuleByDef |
| 0.04% | python | delitem_common |
| 0.04% | python | PyObject_GenericGetAttr |
| 0.04% | python | PyIter_Next |
| 0.04% | python | method_get |
| 0.04% | python | PyObject_Repr |
| 0.04% | python | PyObject_DelItem |
| 0.03% | python | PyObject_GenericHash |
| 0.03% | python | PyIter_Send |
| 0.03% | python | PyNumber_Multiply |
| 0.03% | python | object_get_class |
| 0.03% | python | object_init |
| 0.03% | python | PyNumber_Add |
| 0.03% | python | PyNumber_Remainder |
| 0.02% | python | PyObject_Str |
| 0.02% | python | _PyObject_InitInlineValues |
| 0.02% | python | _PyObject_VectorcallDictTstate |
| 0.02% | python | PyNumber_Index |
| 0.02% | python | type_ready |
| 0.02% | python | PyNumber_FloorDivide |
| 0.02% | python | PyObject_GetAttr |
| 0.02% | python | StopIteration_init |
| 0.02% | python | _PyObject_StoreInstanceAttribute |
| 0.02% | python | _PyNumber_Index |
| 0.02% | python | PySequence_Contains |
| 0.01% | python | PyObject_GetBuffer |
| 0.01% | python | _PyObject_Call_Prepend |
| 0.01% | python | PyNumber_Negative |
| 0.01% | python | PyMapping_Check |
| 0.01% | python | _PySuper_Lookup |
| 0.01% | python | _PyObject_RealIsInstance |
| 0.01% | python | object_richcompare |
| 0.01% | python | PyMapping_GetOptionalItem |
| 0.01% | python | object_recursive_isinstance |
| 0.01% | python | PyNumber_Lshift |
| 0.01% | python | _Py_type_getattro_impl |
| 0.01% | python | PyNumber_InPlaceAdd |
| 0.01% | python | PyNumber_Rshift |
| 0.01% | python | PyNumber_Subtract |
| 0.01% | python | PyObject_LengthHint |
| 0.01% | python | PyObject_SelfIter |
| 0.01% | python | _PyObject_MaterializeManagedDict |
| 0.01% | python | PySequence_GetItem |
| 0.01% | python | PySequence_Tuple |
| 0.01% | python | PySequence_List |
| 0.00% | python | type_name |
| 0.00% | python | PyNumber_Xor |
| 0.00% | python | _PyObject_ClearFreeLists |
| 0.00% | python | type___instancecheck__ |
| 0.00% | python | object_vacall |
| 0.00% | python | PyObject_GenericGetDict |
| 0.00% | python | PyNumber_Long |
| 0.00% | python | object___reduce_ex__ |

### library

6.26% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.95% | python | sre_ucs1_match |
| 0.25% | libz.so.1.3 | 0x00000000000080c4 |
| 0.20% | python | sre_search |
| 0.16% | binascii.cpython-316-aarch64-linux-gnu.so | binascii_a2b_base85 |
| 0.14% | binascii.cpython-316-aarch64-linux-gnu.so | binascii_a2b_ascii85 |
| 0.12% | libz.so.1.3 | 0x0000000000002a84 |
| 0.11% | binascii.cpython-316-aarch64-linux-gnu.so | binascii_a2b_base64 |
| 0.10% | binascii.cpython-316-aarch64-linux-gnu.so | binascii_a2b_base32 |
| 0.09% | libz.so.1.3 | 0x0000000000002a8c |
| 0.09% | libz.so.1.3 | 0x0000000000002a6c |
| 0.09% | array.cpython-316-aarch64-linux-gnu.so | array_subscr |
| 0.09% | pyexpat.cpython-316-aarch64-linux-gnu.so | normal_updatePosition |
| 0.08% | binascii.cpython-316-aarch64-linux-gnu.so | binascii_b2a_base64 |
| 0.08% | binascii.cpython-316-aarch64-linux-gnu.so | binascii_b2a_base32 |
| 0.07% | binascii.cpython-316-aarch64-linux-gnu.so | binascii_a2b_hex_impl.isra.0 |
| 0.06% | pyexpat.cpython-316-aarch64-linux-gnu.so | accountingDiffTolerated.part.0 |
| 0.06% | python | sre_ucs1_count |
| 0.06% | pyexpat.cpython-316-aarch64-linux-gnu.so | normal_contentTok |
| 0.06% | libz.so.1.3 | 0x0000000000002a88 |
| 0.06% | binascii.cpython-316-aarch64-linux-gnu.so | binascii_b2a_base85 |
| 0.06% | libz.so.1.3 | 0x00000000000080cc |
| 0.05% | libz.so.1.3 | 0x00000000000080c0 |
| 0.05% | array.cpython-316-aarch64-linux-gnu.so | array_ass_subscr |
| 0.04% | python | _sre_SRE_Pattern_prefixmatch |
| 0.04% | pyexpat.cpython-316-aarch64-linux-gnu.so | doContent |
| 0.04% | _math_integer.cpython-316-aarch64-linux-gnu.so | factorial_partial_product |
| 0.04% | _heapq.cpython-316-aarch64-linux-gnu.so | siftup |
| 0.04% | libz.so.1.3 | 0x0000000000002a64 |
| 0.04% | libz.so.1.3 | 0x00000000000080a4 |
| 0.04% | binascii.cpython-316-aarch64-linux-gnu.so | binascii_b2a_ascii85 |
| 0.04% | libz.so.1.3 | 0x0000000000008070 |
| 0.04% | python | sre_ucs4_match |
| 0.03% | libz.so.1.3 | 0x00000000000080c8 |
| 0.03% | libz.so.1.3 | 0x00000000000080b4 |
| 0.03% | libz.so.1.3 | 0x0000000000008094 |
| 0.03% | libz.so.1.3 | 0x0000000000008080 |
| 0.03% | libz.so.1.3 | 0x0000000000002a7c |
| 0.03% | libz.so.1.3 | 0x0000000000002a80 |
| 0.03% | libz.so.1.3 | 0x0000000000002a68 |
| 0.03% | array.cpython-316-aarch64-linux-gnu.so | d_setitem |
| 0.03% | libz.so.1.3 | 0x0000000000002a78 |
| 0.03% | libz.so.1.3 | 0x00000000000080bc |
| 0.03% | python | sre_category |
| 0.03% | _pickle.cpython-316-aarch64-linux-gnu.so | save.constprop.0 |
| 0.03% | _json.cpython-316-aarch64-linux-gnu.so | scanstring_unicode |
| 0.03% | libz.so.1.3 | 0x0000000000002a60 |
| 0.02% | libz.so.1.3 | 0x0000000000008078 |
| 0.02% | pyexpat.cpython-316-aarch64-linux-gnu.so | sip24_update.isra.0 |
| 0.02% | pyexpat.cpython-316-aarch64-linux-gnu.so | storeAtts |
| 0.02% | libz.so.1.3 | 0x00000000000076e4 |
| 0.02% | libz.so.1.3 | 0x000000000000809c |
| 0.02% | tracer.cpython-316-aarch64-linux-gnu.so | CTracer_trace |
| 0.02% | libz.so.1.3 | 0x000000000000784c |
| 0.02% | libz.so.1.3 | 0x00000000000080d0 |
| 0.02% | libz.so.1.3 | 0x0000000000008098 |
| 0.02% | libz.so.1.3 | 0x00000000000080a8 |
| 0.02% | _elementtree.cpython-316-aarch64-linux-gnu.so | element_gc_traverse |
| 0.02% | libz.so.1.3 | 0x000000000000808c |
| 0.02% | libz.so.1.3 | 0x00000000000080b8 |
| 0.02% | libm.so.6 | pow@@GLIBC_2.29 |
| 0.02% | libz.so.1.3 | 0x0000000000008074 |
| 0.02% | libz.so.1.3 | 0x0000000000008088 |
| 0.02% | pyexpat.cpython-316-aarch64-linux-gnu.so | normal_nameLength |
| 0.02% | pyexpat.cpython-316-aarch64-linux-gnu.so | normal_getAtts |
| 0.02% | python | sre_ucs2_match |
| 0.02% | libz.so.1.3 | 0x00000000000080ac |
| 0.02% | libm.so.6 | __cos |
| 0.02% | math.cpython-316-aarch64-linux-gnu.so | math_sqrt |
| 0.02% | libz.so.1.3 | 0x00000000000080b0 |
| 0.02% | libz.so.1.3 | 0x00000000000076d8 |
| 0.02% | _pickle.cpython-316-aarch64-linux-gnu.so | save_dict |
| 0.02% | python | pattern_subx |
| 0.02% | libz.so.1.3 | 0x0000000000007840 |
| 0.01% | _json.cpython-316-aarch64-linux-gnu.so | scan_once_unicode |
| 0.01% | _elementtree.cpython-316-aarch64-linux-gnu.so | treebuilder_handle_start |
| 0.01% | pyexpat.cpython-316-aarch64-linux-gnu.so | sip24_final |
| 0.01% | array.cpython-316-aarch64-linux-gnu.so | d_getitem |
| 0.01% | libm.so.6 | __sin |
| 0.01% | libz.so.1.3 | 0x0000000000008090 |
| 0.01% | _elementtree.cpython-316-aarch64-linux-gnu.so | element_dealloc |
| 0.01% | libz.so.1.3 | 0x00000000000080d4 |
| 0.01% | libz.so.1.3 | 0x000000000000807c |
| 0.01% | libz.so.1.3 | 0x00000000000080a0 |
| 0.01% | libz.so.1.3 | 0x00000000000076e8 |
| 0.01% | libz.so.1.3 | 0x00000000000076bc |
| 0.01% | pyexpat.cpython-316-aarch64-linux-gnu.so | lookupWithLength |
| 0.01% | _elementtree.cpython-316-aarch64-linux-gnu.so | elementiter_next |
| 0.01% | libz.so.1.3 | 0x0000000000007850 |
| 0.01% | libz.so.1.3 | 0x00000000000076c8 |
| 0.01% | libz.so.1.3 | 0x0000000000007830 |
| 0.01% | libz.so.1.3 | 0x00000000000076dc |
| 0.01% | libz.so.1.3 | 0x0000000000007824 |
| 0.01% | libz.so.1.3 | 0x0000000000007844 |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3VdbeExec |
| 0.01% | _pickle.cpython-316-aarch64-linux-gnu.so | PyMemoTable_Set |
| 0.01% | array.cpython-316-aarch64-linux-gnu.so | PyNumber_AsSsize_t@plt |
| 0.01% | array.cpython-316-aarch64-linux-gnu.so | PyIndex_Check@plt |
| 0.01% | array.cpython-316-aarch64-linux-gnu.so | PyType_GetModuleByDef@plt |
| 0.01% | libz.so.1.3 | 0x0000000000002348 |
| 0.01% | _elementtree.cpython-316-aarch64-linux-gnu.so | expat_end_handler |
| 0.01% | _heapq.cpython-316-aarch64-linux-gnu.so | siftdown |
| 0.01% | libz.so.1.3 | 0x0000000000007f38 |
| 0.01% | _math_integer.cpython-316-aarch64-linux-gnu.so | math_integer_gcd |
| 0.01% | _pickle.cpython-316-aarch64-linux-gnu.so | _Pickler_Write |
| 0.01% | _elementtree.cpython-316-aarch64-linux-gnu.so | element_getitem |
| 0.01% | pyexpat.cpython-316-aarch64-linux-gnu.so | utf8_toUtf8 |
| 0.01% | libz.so.1.3 | 0x00000000000076e0 |
| 0.01% | _random.cpython-316-aarch64-linux-gnu.so | genrand_uint32 |
| 0.01% | array.cpython-316-aarch64-linux-gnu.so | PyFloat_FromDouble@plt |
| 0.01% | libz.so.1.3 | 0x0000000000007848 |
| 0.01% | _elementtree.cpython-316-aarch64-linux-gnu.so | expat_start_handler |
| 0.01% | _pickle.cpython-316-aarch64-linux-gnu.so | Pickler_clear |
| 0.01% | libz.so.1.3 | 0x0000000000002318 |
| 0.01% | python | _sre_SRE_Pattern_search |
| 0.01% | libz.so.1.3 | 0x0000000000002338 |
| 0.01% | _json.cpython-316-aarch64-linux-gnu.so | encoder_listencode_obj |
| 0.01% | _math_integer.cpython-316-aarch64-linux-gnu.so | math_integer_factorial |
| 0.01% | libz.so.1.3 | 0x0000000000002328 |
| 0.01% | libz.so.1.3 | 0x0000000000002308 |
| 0.01% | _pickle.cpython-316-aarch64-linux-gnu.so | memo_get |
| 0.01% | _elementtree.cpython-316-aarch64-linux-gnu.so | makeuniversal |
| 0.00% | libz.so.1.3 | 0x0000000000007f7c |
| 0.00% | _heapq.cpython-316-aarch64-linux-gnu.so | _heapq_heappop |
| 0.00% | libz.so.1.3 | 0x00000000000022d8 |
| 0.00% | libz.so.1.3 | 0x0000000000002304 |
| 0.00% | python | sre_ucs4_count |
| 0.00% | _elementtree.cpython-316-aarch64-linux-gnu.so | treebuilder_extend_element_text_or_tail.isra.0 |
| 0.00% | _elementtree.cpython-316-aarch64-linux-gnu.so | expat_data_handler |
| 0.00% | _elementtree.cpython-316-aarch64-linux-gnu.so | dealloc_extra.part.0 |
| 0.00% | libz.so.1.3 | 0x00000000000022f0 |
| 0.00% | libz.so.1.3 | 0x00000000000022d4 |
| 0.00% | _math_integer.cpython-316-aarch64-linux-gnu.so | _Py_Dealloc@plt |
| 0.00% | _elementtree.cpython-316-aarch64-linux-gnu.so | create_new_element.isra.0 |
| 0.00% | _pickle.cpython-316-aarch64-linux-gnu.so | _Pickler_Write.constprop.0 |
| 0.00% | ld-linux-aarch64.so.1 | _dl_relocate_object |
| 0.00% | ld-linux-aarch64.so.1 | do_lookup_x |
| 0.00% | python | sys_trace_start |
| 0.00% | _elementtree.cpython-316-aarch64-linux-gnu.so | xmlparser_append_event.isra.0 |
| 0.00% | _json.cpython-316-aarch64-linux-gnu.so | ascii_escape_size |
| 0.00% | libz.so.1.3 | inflate |
| 0.00% | _random.cpython-316-aarch64-linux-gnu.so | _random_Random_getrandbits |
| 0.00% | math.cpython-316-aarch64-linux-gnu.so | math_cos |
| 0.00% | _elementtree.cpython-316-aarch64-linux-gnu.so | element_text_getter |
| 0.00% | python | sys_trace_return |
| 0.00% | libz.so.1.3 | 0x00000000000022f8 |
| 0.00% | libz.so.1.3 | 0x000000000000234c |
| 0.00% | libz.so.1.3 | 0x0000000000002344 |
| 0.00% | _elementtree.cpython-316-aarch64-linux-gnu.so | element_resize |
| 0.00% | _pickle.cpython-316-aarch64-linux-gnu.so | Pickler_traverse |
| 0.00% | _heapq.cpython-316-aarch64-linux-gnu.so | _heapq_heappush |
| 0.00% | libsqlite3.so.0.8.6 | 0x00000000000a1120 |
| 0.00% | libz.so.1.3 | 0x0000000000002320 |
| 0.00% | _pickle.cpython-316-aarch64-linux-gnu.so | save_reduce |
| 0.00% | array.cpython-316-aarch64-linux-gnu.so | PyArg_Parse@plt |
| 0.00% | libz.so.1.3 | 0x00000000000022e8 |
| 0.00% | python | _sre_SRE_Pattern_sub |
| 0.00% | _math_integer.cpython-316-aarch64-linux-gnu.so | PyLong_FromUnsignedLong@plt |
| 0.00% | _pickle.cpython-316-aarch64-linux-gnu.so | memo_put |
| 0.00% | unicodedata.cpython-316-aarch64-linux-gnu.so | unicodedata_UCD_combining |
| 0.00% | _json.cpython-316-aarch64-linux-gnu.so | encoder_encode_key_value |
| 0.00% | _json.cpython-316-aarch64-linux-gnu.so | write_escaped_ascii |
| 0.00% | libz.so.1.3 | 0x0000000000002204 |
| 0.00% | _elementtree.cpython-316-aarch64-linux-gnu.so | element_tag_getter |
| 0.00% | ld-linux-aarch64.so.1 | strcmp |
| 0.00% | libz.so.1.3 | 0x0000000000002330 |
| 0.00% | _math_integer.cpython-316-aarch64-linux-gnu.so | PyNumber_Multiply@plt |

### lookup

5.15% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 2.96% | python | unicodekeys_lookup_unicode |
| 2.01% | python | _Py_dict_lookup |
| 0.04% | python | builtin_getattr |
| 0.04% | python | find_name_in_mro |
| 0.02% | python | _Py_dict_lookup_threadsafe_stackref |
| 0.02% | python | _Py_hashtable_get_entry_generic |
| 0.02% | python | _Py_type_getattro |
| 0.01% | python | update_one_slot |
| 0.01% | python | PyMember_GetOne |
| 0.00% | python | PyMember_SetOne |
| 0.00% | python | member_get |

### dict

3.53% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.88% | python | _PyDict_Subscript |
| 0.60% | python | dictiter_iternextkey |
| 0.45% | python | insertdict |
| 0.25% | python | PyDict_GetItemRef |
| 0.18% | python | dictkeys_decref.part.0.constprop.0 |
| 0.16% | python | _PyDict_StoreSubscript |
| 0.10% | python | PyDict_Contains |
| 0.10% | python | insert_to_emptydict |
| 0.08% | python | dict_get |
| 0.07% | python | find_empty_slot |
| 0.07% | python | build_indices_unicode |
| 0.07% | python | _PyDict_LoadBuiltinsFromGlobals |
| 0.06% | python | new_dict.constprop.0 |
| 0.06% | python | dictiter_iternextitem |
| 0.05% | python | PyDict_Next |
| 0.04% | python | _PyDict_FromItems |
| 0.04% | python | _PyDict_Next |
| 0.04% | python | dict_merge |
| 0.03% | python | dict_setdefault_ref_lock_held |
| 0.02% | python | dictresize |
| 0.02% | python | _PyDict_DelItem_KnownHash_LockHeld |
| 0.02% | python | _PyDict_SetItem_Take2 |
| 0.02% | python | PyDict_SetItem |
| 0.02% | python | dict_items |
| 0.01% | python | new_keys_object |
| 0.01% | python | dictiter_iternextvalue |
| 0.01% | python | PyDict_GetItemWithError |
| 0.01% | python | _PyDict_MergeUniq |
| 0.01% | python | dict_iter |
| 0.01% | python | PyDict_GetItem |
| 0.01% | python | dict_pop |
| 0.01% | python | _PyDict_GetMethodStackRef |
| 0.01% | python | _PyDict_GetItemRef_KnownHash_LockHeld |
| 0.01% | python | _PyDict_LoadGlobalStackRef |
| 0.00% | python | dict_length |
| 0.00% | python | PyDict_SetDefaultRef |
| 0.00% | python | dict_update |
| 0.00% | python | dict___contains__ |
| 0.00% | python | _PyDict_SendEvent |

### int

2.71% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.01% | python | k_mul |
| 0.26% | python | x_divrem |
| 0.18% | python | PyLong_FromSsize_t |
| 0.17% | python | long_to_decimal_string_internal |
| 0.12% | python | _PyLong_FromMedium |
| 0.11% | python | PyLong_FromLong |
| 0.09% | python | x_add |
| 0.09% | python | PyLong_AsSsize_t |
| 0.08% | python | _PyLong_GCD |
| 0.07% | python | long_hash |
| 0.06% | python | long_richcompare |
| 0.05% | python | PyLong_AsLongAndOverflow |
| 0.04% | python | x_sub |
| 0.03% | python | PyLong_FromUnsignedLong |
| 0.02% | python | long_div |
| 0.02% | python | long_mul |
| 0.02% | python | PyLong_FromVoidPtr |
| 0.02% | python | PyLong_AsNativeBytes.constprop.0 |
| 0.02% | python | long_lshift1 |
| 0.02% | python | PyLong_AsLong |
| 0.02% | python | long_to_decimal_string |
| 0.02% | python | long_bitwise |
| 0.02% | python | PyLong_AsDouble |
| 0.02% | python | long_lshift_method |
| 0.01% | python | long_rshift |
| 0.01% | python | long_neg_method |
| 0.01% | python | PyLong_FromString |
| 0.01% | python | long_rshift1 |
| 0.01% | python | long_add |
| 0.01% | python | _PyLong_Frexp |
| 0.01% | python | long_mul_method |
| 0.01% | python | long_add_method |
| 0.01% | python | l_mod |
| 0.00% | python | _PyLong_Size_t_Converter |
| 0.00% | python | long_float |
| 0.00% | python | long_mod |
| 0.00% | python | PyLong_FromUnsignedLongLong |
| 0.00% | python | PyLong_AsInt |
| 0.00% | python | PyLong_GetSign |

### list

2.51% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.51% | python | list_remove |
| 0.32% | python | listiter_next |
| 0.25% | python | list_slice_lock_held |
| 0.21% | python | list_ass_slice_lock_held |
| 0.15% | python | list_iter |
| 0.14% | python | _PyList_SliceSubscript |
| 0.13% | python | _PyList_BinarySlice |
| 0.10% | python | list_slice_wrap |
| 0.09% | python | _PyList_AppendTakeRefListResize |
| 0.09% | python | list_sort_impl |
| 0.06% | python | _list_extend |
| 0.06% | python | list_ass_subscript |
| 0.06% | python | list_append |
| 0.06% | python | list_extend_lock_held |
| 0.04% | python | _PyList_Concat |
| 0.04% | python | list_length |
| 0.04% | python | list_subscript |
| 0.02% | python | list_resize |
| 0.02% | python | _PyList_FromStackRefStealOnSuccess |
| 0.02% | python | list_insert |
| 0.01% | python | PyList_Append |
| 0.01% | python | list_pop |
| 0.01% | python | list_contains |
| 0.01% | python | _PyList_Extend |
| 0.01% | python | list_sort |
| 0.01% | python | _PyList_AsTupleAndClear |
| 0.01% | python | list_vectorcall |
| 0.01% | python | list_to_tuple |
| 0.00% | python | list_iteritem |
| 0.00% | python | list_richcompare |
| 0.00% | python | list_index |
| 0.00% | python | PyList_GetItemRef |
| 0.00% | python | PyList_SetItem |

### miscobj

2.45% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.17% | python | set_lookkey |
| 0.26% | python | _PySet_Contains |
| 0.16% | python | PySlice_AdjustIndices |
| 0.11% | python | PySlice_Unpack |
| 0.10% | python | gen_iternext |
| 0.09% | python | PyBool_FromLong |
| 0.08% | python | make_gen |
| 0.05% | python | set_add_entry_takeref |
| 0.04% | python | deque_append |
| 0.04% | python | setiter_iternext |
| 0.03% | python | _PyBuildSlice_ConsumeRefs |
| 0.03% | python | set_issubset_impl |
| 0.03% | python | enum_next |
| 0.02% | python | PyGen_am_send |
| 0.02% | python | set_table_resize |
| 0.02% | python | range_iter |
| 0.02% | python | _PyGen_FetchStopIterationValue |
| 0.02% | python | PyBuffer_Release |
| 0.02% | python | deque_popleft |
| 0.02% | python | PyBuffer_FillInfo |
| 0.01% | python | set_merge_lock_held |
| 0.01% | python | range_subscript |
| 0.01% | python | set_difference_untracked |
| 0.01% | python | _PySlice_GetLongIndices |
| 0.01% | python | dequeiter_next |
| 0.01% | python | set_add |
| 0.01% | python | range_vectorcall |
| 0.01% | python | deque_clear.part.0 |
| 0.01% | python | bytearray_ass_subscript_lock_held |
| 0.00% | python | set_discard |
| 0.00% | python | PySet_Add |
| 0.00% | python | set_intersection |
| 0.00% | python | set_richcompare |
| 0.00% | python | set_iter |
| 0.00% | python | weakref_hash |

### str

2.27% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.27% | python | _PyUnicode_Equal |
| 0.22% | python | PyUnicode_Format |
| 0.21% | python | _PyUnicode_JoinArray.part.0 |
| 0.15% | python | PyUnicode_RichCompare |
| 0.11% | python | unicode_hash |
| 0.10% | python | siphash13 |
| 0.09% | python | _copy_characters.constprop.0.isra.0 |
| 0.06% | python | replace |
| 0.06% | python | bytes_hash |
| 0.06% | python | _PyUnicodeWriter_PrepareInternal |
| 0.06% | python | bytes_richcompare |
| 0.05% | python | _PyUnicode_FromUCS4.part.0 |
| 0.05% | python | _PyUnicode_ResizeCompact |
| 0.04% | python | unicode_repr |
| 0.04% | python | _PyUnicodeWriter_WriteSubstring |
| 0.04% | python | _PyUnicode_InternMortal |
| 0.04% | python | unicode_decode_utf8.part.0 |
| 0.03% | python | PyUnicode_Contains |
| 0.03% | python | PyUnicode_Substring |
| 0.03% | python | _PyUnicode_BinarySlice |
| 0.02% | python | _PyUnicodeWriter_Finish |
| 0.02% | python | PyBytes_FromStringAndSize |
| 0.02% | python | split |
| 0.02% | python | _PyUnicodeWriter_WriteStr |
| 0.02% | python | unicode_decode_utf8_impl |
| 0.02% | python | unicode_from_format |
| 0.02% | python | PyUnicode_Concat |
| 0.02% | python | bytes_subscript |
| 0.02% | python | unicode_join |
| 0.02% | python | _PyUnicode_FromUCS1.part.0 |
| 0.01% | python | _PyUnicode_TranslateCharmap |
| 0.01% | python | _PyUnicode_FastCopyCharacters |
| 0.01% | python | find_first_nonascii |
| 0.01% | python | _PyUnicodeWriter_Init |
| 0.01% | python | unicode_startswith |
| 0.01% | python | bytes_translate_impl |
| 0.01% | python | _PyUnicode_FindMaxChar |
| 0.01% | python | _PyUnicode_IsAlpha |
| 0.01% | python | stringlib_bytes_join |
| 0.01% | python | _PyUnicode_InternImmortal |
| 0.01% | python | unicode_replace |
| 0.01% | python | intern_constants |
| 0.01% | python | PyUnicode_Splitlines |
| 0.01% | python | _PyUnicode_Result |
| 0.01% | python | PyUnicode_InternFromString |
| 0.01% | python | bytes_buffer_getbuffer |
| 0.01% | python | unicode_lower |
| 0.01% | python | _PyUnicode_IsDecimalDigit |
| 0.01% | python | unicode_mod |
| 0.01% | python | PyUnicodeWriter_WriteChar |
| 0.01% | python | unicode_expandtabs |
| 0.01% | python | _PyUnicode_JoinArray |
| 0.00% | python | _PyUnicodeWriter_WriteASCIIString |
| 0.00% | python | unicode_fromformat_write_utf8 |
| 0.00% | python | PyUnicodeWriter_WriteASCII |
| 0.00% | python | stringlib__two_way |
| 0.00% | python | PyUnicode_AsUTF8AndSize |
| 0.00% | python | _PyUnicode_FromUCS2.part.0 |
| 0.00% | python | PyUnicode_AsEncodedString |
| 0.00% | python | unicode_split |
| 0.00% | python | PyUnicode_Decode |
| 0.00% | python | unicode_rfind |
| 0.00% | python | bytes_length |
| 0.00% | python | bytes_iteritem |
| 0.00% | python | PyUnicode_FromWideChar |
| 0.00% | python | unicode_strip |
| 0.00% | python | PyUnicode_Append |

### tuple

1.60% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.41% | python | tuple_richcompare |
| 0.38% | python | PyTuple_FromArray.part.0 |
| 0.35% | python | _PyTuple_FromStackRefStealOnSuccess |
| 0.20% | python | tuple_hash |
| 0.04% | python | PyTuple_GetSlice |
| 0.04% | python | PyTuple_FromArray |
| 0.03% | python | _PyTuple_FromArraySteal |
| 0.03% | python | tuple_subscript |
| 0.02% | python | _PyTuple_FromPair |
| 0.02% | python | _PyTuple_BinarySlice |
| 0.01% | python | tupleiter_next |
| 0.01% | python | tuple_length |
| 0.01% | python | tuple_iteritem |
| 0.01% | python | tuplegetter_descr_get |
| 0.01% | python | tuple_iter |
| 0.01% | python | _PyTuple_FromPairSteal |
| 0.01% | python | _PyTuple_Concat |
| 0.00% | python | tuple_contains |
| 0.00% | python | PyTuple_Pack |

### kernel

1.56% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.14% | [kernel.kallsyms] | _raw_spin_unlock_irqrestore |
| 0.09% | [kernel.kallsyms] | __pi_clear_page |
| 0.09% | [kernel.kallsyms] | el0_da |
| 0.05% | [kernel.kallsyms] | task_mm_cid_work |
| 0.05% | [kernel.kallsyms] | zap_pte_range |
| 0.04% | [kernel.kallsyms] | handle_mm_fault |
| 0.04% | [kernel.kallsyms] | mem_cgroup_commit_charge |
| 0.03% | [kernel.kallsyms] | mas_walk |
| 0.03% | [kernel.kallsyms] | percpu_counter_add_batch |
| 0.03% | [kernel.kallsyms] | __lruvec_stat_mod_folio |
| 0.03% | [kernel.kallsyms] | __rmqueue_pcplist |
| 0.03% | [kernel.kallsyms] | post_alloc_hook |
| 0.02% | [kernel.kallsyms] | perf_iterate_ctx |
| 0.02% | [kernel.kallsyms] | get_mem_cgroup_from_mm |
| 0.02% | [kernel.kallsyms] | __arch_copy_to_user |
| 0.02% | [kernel.kallsyms] | __d_lookup_rcu |
| 0.02% | [kernel.kallsyms] | folio_add_lru |
| 0.02% | [kernel.kallsyms] | handle_softirqs |
| 0.02% | [kernel.kallsyms] | percpu_ref_put_many.constprop.0 |
| 0.02% | [kernel.kallsyms] | arch_local_irq_restore |
| 0.02% | [kernel.kallsyms] | __mod_memcg_lruvec_state |
| 0.02% | [kernel.kallsyms] | __alloc_pages |
| 0.02% | [kernel.kallsyms] | el0_svc |
| 0.02% | [kernel.kallsyms] | __rcu_read_unlock |
| 0.02% | [kernel.kallsyms] | up_read |
| 0.02% | [kernel.kallsyms] | down_read_trylock |
| 0.02% | [kernel.kallsyms] | __handle_mm_fault |
| 0.01% | [kernel.kallsyms] | get_page_from_freelist |
| 0.01% | [kernel.kallsyms] | percpu_ref_get_many |
| 0.01% | [kernel.kallsyms] | _raw_spin_lock |
| 0.01% | [kernel.kallsyms] | __rcu_read_lock |
| 0.01% | [kernel.kallsyms] | rmqueue |
| 0.01% | [kernel.kallsyms] | folio_remove_rmap_ptes |
| 0.01% | [kernel.kallsyms] | memset |
| 0.01% | [kernel.kallsyms] | __update_cpu_freelist_fast |
| 0.01% | [kernel.kallsyms] | _raw_spin_trylock |
| 0.01% | [kernel.kallsyms] | lock_vma_under_rcu |
| 0.01% | [kernel.kallsyms] | do_page_fault |
| 0.01% | [kernel.kallsyms] | folio_add_new_anon_rmap |
| 0.01% | [kernel.kallsyms] | get_pfnblock_flags_mask |
| 0.01% | [kernel.kallsyms] | do_anonymous_page |
| 0.01% | [kernel.kallsyms] | _raw_spin_unlock |
| 0.01% | [kernel.kallsyms] | try_charge_memcg |
| 0.01% | [kernel.kallsyms] | kmem_cache_alloc |
| 0.01% | [kernel.kallsyms] | next_uptodate_folio |
| 0.01% | [kernel.kallsyms] | __mod_node_page_state |
| 0.01% | [kernel.kallsyms] | release_pages |
| 0.01% | [kernel.kallsyms] | alloc_pages_mpol |
| 0.01% | [kernel.kallsyms] | get_random_u16 |
| 0.01% | [kernel.kallsyms] | free_unref_page_commit |
| 0.01% | [kernel.kallsyms] | free_unref_page_prepare |
| 0.01% | [kernel.kallsyms] | __perf_addr_filters_adjust |
| 0.01% | [kernel.kallsyms] | do_mem_abort |
| 0.01% | [kernel.kallsyms] | __pte_offset_map |
| 0.01% | [kernel.kallsyms] | get_task_policy.part.0 |
| 0.01% | [kernel.kallsyms] | __pi_copy_page |
| 0.01% | [kernel.kallsyms] | free_unref_page_list |
| 0.01% | [kernel.kallsyms] | cgroup_rstat_updated |
| 0.01% | [kernel.kallsyms] | vma_alloc_folio |
| 0.01% | [kernel.kallsyms] | blk_cgroup_congested |
| 0.01% | [kernel.kallsyms] | alloc_anon_folio |
| 0.01% | [kernel.kallsyms] | link_path_walk.part.0.constprop.0 |
| 0.00% | [kernel.kallsyms] | inode_permission |
| 0.00% | [kernel.kallsyms] | __pte_offset_map_lock |
| 0.00% | [kernel.kallsyms] | __mod_lruvec_state |
| 0.00% | [kernel.kallsyms] | half_md4_transform.isra.0 |
| 0.00% | [kernel.kallsyms] | handle_pte_fault |
| 0.00% | [kernel.kallsyms] | free_swap_cache |
| 0.00% | [kernel.kallsyms] | __mem_cgroup_charge |
| 0.00% | [kernel.kallsyms] | uncharge_folio |
| 0.00% | [kernel.kallsyms] | pte_offset_map_nolock |
| 0.00% | [kernel.kallsyms] | step_into |
| 0.00% | [kernel.kallsyms] | zone_statistics |
| 0.00% | [kernel.kallsyms] | do_translation_fault |
| 0.00% | [kernel.kallsyms] | kmem_cache_free |
| 0.00% | [kernel.kallsyms] | get_vma_policy |
| 0.00% | [kernel.kallsyms] | __flush_tlb_range |
| 0.00% | [kernel.kallsyms] | filemap_get_read_batch |
| 0.00% | [kernel.kallsyms] | __memcg_slab_free_hook |
| 0.00% | [kernel.kallsyms] | set_ptes.isra.0 |
| 0.00% | [kernel.kallsyms] | vma_alloc_zeroed_movable_folio |
| 0.00% | [kernel.kallsyms] | __memcg_slab_post_alloc_hook |
| 0.00% | [kernel.kallsyms] | generic_permission |
| 0.00% | [kernel.kallsyms] | __call_rcu_common |
| 0.00% | [kernel.kallsyms] | perf_event_alloc |
| 0.00% | [kernel.kallsyms] | memblock_is_map_memory |
| 0.00% | [kernel.kallsyms] | vm_normal_page |
| 0.00% | [kernel.kallsyms] | do_pte_missing |
| 0.00% | [kernel.kallsyms] | invoke_syscall |

### libc

1.39% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.39% | libc.so.6 | __memcpy_generic |
| 0.26% | libc.so.6 | memcmp |
| 0.19% | libc.so.6 | __memset_zva64 |
| 0.13% | libc.so.6 | _int_malloc |
| 0.06% | libc.so.6 | malloc |
| 0.03% | libc.so.6 | _int_free |
| 0.03% | libc.so.6 | __strlen_asimd |
| 0.03% | libc.so.6 | _int_free_merge_chunk |
| 0.03% | libc.so.6 | __memchr_generic |
| 0.03% | libc.so.6 | unlink_chunk.isra.0 |
| 0.03% | libc.so.6 | cfree@GLIBC_2.17 |
| 0.03% | libc.so.6 | __GI___pthread_self |
| 0.02% | libc.so.6 | _int_free_create_chunk |
| 0.02% | libc.so.6 | pthread_mutex_lock@@GLIBC_2.17 |
| 0.01% | libc.so.6 | strchr |
| 0.01% | libc.so.6 | __GI___pthread_mutex_unlock_usercnt |
| 0.01% | libc.so.6 | __memmove_generic |
| 0.01% | libc.so.6 | realloc |
| 0.01% | libc.so.6 | strncmp |
| 0.01% | libc.so.6 | _int_realloc |
| 0.00% | libc.so.6 | __errno_location |
| 0.00% | libc.so.6 | pthread_cond_signal@@GLIBC_2.17 |
| 0.00% | libc.so.6 | pthread_mutex_unlock@@GLIBC_2.17 |
| 0.00% | libc.so.6 | __GI___fstatat64 |
| 0.00% | libc.so.6 | __aarch64_swp8_acq |
| 0.00% | libc.so.6 | __GI___memrchr |
| 0.00% | libc.so.6 | clock_gettime@@GLIBC_2.17 |

### calls

0.71% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.14% | python | PyArg_UnpackTuple |
| 0.12% | python | _PyArg_UnpackKeywords |
| 0.11% | python | _PyFunction_Vectorcall |
| 0.09% | python | _Py_CheckFunctionResult |
| 0.06% | python | vgetargs1_impl.constprop.0 |
| 0.04% | python | PyArg_Parse |
| 0.03% | python | method_vectorcall_FASTCALL_KEYWORDS_METHOD |
| 0.03% | python | cfunction_vectorcall_FASTCALL_KEYWORDS |
| 0.01% | python | method_vectorcall |
| 0.01% | python | cfunction_vectorcall_O |
| 0.01% | python | cfunction_vectorcall_NOARGS |
| 0.01% | python | _PyArg_UnpackStack |
| 0.01% | python | vgetargs1_impl |
| 0.01% | python | vectorcall_method |
| 0.01% | python | method_vectorcall_O |
| 0.00% | python | PyArg_ParseTupleAndKeywords |
| 0.00% | python | cfunction_vectorcall_FASTCALL |
| 0.00% | python | method_vectorcall_NOARGS |
| 0.00% | python | method_vectorcall_VARARGS_KEYWORDS |
| 0.00% | python | method_vectorcall_VARARGS |
| 0.00% | python | cfunction_vectorcall_FASTCALL_KEYWORDS_METHOD |
| 0.00% | python | method_vectorcall_FASTCALL |

### compiler

0.70% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.69% | python | _PyJIT_Entry |
| 0.00% | python | optimize_uops.isra.0 |
| 0.00% | python | _PyJIT_Compile |

### threading

0.64% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.35% | python | _PyThreadState_PopFrame |
| 0.16% | python | _PyThreadState_PushFrame |
| 0.12% | python | PyThread_get_thread_ident |
| 0.00% | python | _PyThreadState_Attach |
| 0.00% | python | _PyThreadState_Detach |

### exceptions

0.53% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.18% | python | PyErr_CheckSignals |
| 0.13% | python | _PyErr_CheckSignalsTstate |
| 0.05% | python | PyErr_Occurred |
| 0.03% | python | PyErr_ExceptionMatches |
| 0.02% | python | _PyErr_SetObject.part.0 |
| 0.02% | python | PyErr_GetRaisedException |
| 0.02% | python | PyErr_SetRaisedException |
| 0.01% | python | PyErr_Format |
| 0.01% | python | PyTraceBack_Here |
| 0.01% | python | _PyErr_Restore |
| 0.01% | python | _PyErr_CreateException |
| 0.01% | python | PyErr_GivenExceptionMatches |
| 0.01% | python | PyException_GetTraceback |
| 0.00% | python | _PyErr_GetRaisedException |
| 0.00% | python | PyFrame_GetCode |
| 0.00% | python | AttributeError_init |
| 0.00% | python | BaseException_vectorcall |
| 0.00% | python | PyException_SetTraceback |

### float

0.38% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.26% | python | PyFloat_FromDouble |
| 0.03% | python | float_compactlong_true_div |
| 0.02% | python | float_richcompare |
| 0.02% | python | PyFloat_AsDouble |
| 0.02% | python | float_add |
| 0.01% | python | float_pow |
| 0.00% | python | float_compactlong_guard |
| 0.00% | python | float_sub |

### import

0.06% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.03% | python | r_object |
| 0.01% | python | r_long |
| 0.01% | python | PyImport_ImportModuleLevelObject |
| 0.00% | python | r_byte |
| 0.00% | python | r_string |

### async

0.04% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.03% | python | async_gen_anext |
| 0.00% | python | async_gen_asend_finalize |

### gil

0.02% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.01% | python | take_gil |
| 0.00% | python | drop_gil |
