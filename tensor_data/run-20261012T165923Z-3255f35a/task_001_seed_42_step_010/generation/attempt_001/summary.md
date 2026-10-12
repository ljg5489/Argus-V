# Hook inspection: generation

Status: **failed**. 120 full tensors; 156 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.015074250655709196 / 2.688866707583197 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1446, 1446] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -3.1026659797171738e+38 / 9.434233126862522e+37 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1446, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6899605950889375 / 0.9333726687897778 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1446, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09463895696860526 / 0.6735252633541252 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 1446] | torch.int64 → int64 | 0.0 / 1445.0 / 722.5 / 417.4241448055762 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.015074250655709196 / 2.688866707583197 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 1446, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.006207083701510317 / 0.757601359089753 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1446, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.006207083701510317 / 0.757601359089753 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1446, 1446] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -3.1026659797171738e+38 / 9.434233126862522e+37 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1446] | torch.int64 → int64 | 0.0 / 1445.0 / 722.5 / 417.4241448055762 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1446, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6899605950889375 / 0.9333726687897778 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1446, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09463895696860526 / 0.6735252633541252 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.006207083701510317 / 0.757601359089753 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 1446, 4096] | torch.bfloat16 → float32 | -9.5 / 14.0 / 0.01576015175644798 / 1.033534139369453 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.006207083701510317 / 0.757601359089753 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 1446, 512] | torch.bfloat16 → float32 | -63.5 / 67.5 / 0.01618317167473027 / 5.697362466961824 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.006207083701510317 / 0.757601359089753 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 1446, 512] | torch.bfloat16 → float32 | -7.78125 / 9.0 / -0.015087417733918664 / 1.2197004869740247 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1446, 4096] | torch.bfloat16 → float32 | -7.0625 / 6.625 / -0.007146648655325998 / 0.5654978000786861 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 1446, 2880] | torch.bfloat16 → float32 | -50.75 / 58.0 / 0.027975742203925427 / 1.250892874695337 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -50.75 / 58.0 / 0.027975742203925427 / 1.250892874695337 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 1446, 1446] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0002785672520197753 / 0.01080200529387854 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -90.5 / 71.0 / 0.01290739752490784 / 2.9584745950361016 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 1446, 2880] | torch.bfloat16 → float32 | -6.5 / 3.828125 / 0.0023994900301512164 / 0.3446261027163768 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -6.5 / 3.828125 / 0.0023994900301512164 / 0.3446261027163768 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [1446, 2880] | torch.bfloat16 → float32 | -6.5 / 3.828125 / 0.0023994900301512164 / 0.3446261027163768 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [1446, 2880] | torch.bfloat16 → float32 | -49.5 / 135.0 / 0.018825579104040212 / 0.8945846733159484 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -49.5 / 135.0 / 0.018825579104040212 / 0.8945846733159484 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [1446, 32] | torch.bfloat16 → float32 | -5.1875 / 3.8125 / -0.11445633240590287 / 0.9676947599087292 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 1446, 2880] | torch.bfloat16 → float32 | -85.5 / 156.0 / 0.03173524362848196 / 3.2657162362369756 | [NPY](tensors/0000038.npy) |
| 117 | `model.layers.0` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0000117.npy) |
| 118 | `model.layers.0` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000118.npy) |
| 119 | `model.layers.0` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.546173095703125 / 0.9889620892499638 | [NPY](tensors/0000119.npy) |
| 120 | `model.layers.0` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.007547855377197266 / 0.730153031268875 | [NPY](tensors/0000120.npy) |
| 121 | `model.layers.0` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 1446.0 / 1446.0 / 1446.0 / 0.0 | [NPY](tensors/0000121.npy) |
| 122 | `model.layers.0` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 123 | `model.layers.0` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 124 | `model.layers.0` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 125 | `model.layers.0.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0000125.npy) |
| 126 | `model.layers.0.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000126.npy) |
| 127 | `model.layers.0.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000127.npy) |
| 128 | `model.layers.0.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000128.npy) |
| 129 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 1446.0 / 1446.0 / 1446.0 / 0.0 | [NPY](tensors/0000129.npy) |
| 130 | `model.layers.0.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 131 | `model.layers.0.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 132 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.546173095703125 / 0.9889620892499638 | [NPY](tensors/0000132.npy) |
| 133 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.007547855377197266 / 0.730153031268875 | [NPY](tensors/0000133.npy) |
| 134 | `model.layers.0.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 135 | `model.layers.0.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000135.npy) |
| 136 | `model.layers.0.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.34375 / 8.125 / 0.009809806477278471 / 1.0602451281469458 | [NPY](tensors/0000136.npy) |
| 137 | `model.layers.0.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000137.npy) |
| 138 | `model.layers.0.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.5 / 52.75 / 0.05987404379993677 / 5.486411371880323 | [NPY](tensors/0000138.npy) |
| 139 | `model.layers.0.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000139.npy) |
| 140 | `model.layers.0.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.125 / 3.75 / 0.02330493927001953 / 1.1486258589347933 | [NPY](tensors/0000140.npy) |
| 141 | `model.layers.0.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.09375 / 3.984375 / -0.0009481197921559215 / 0.7238064687558732 | [NPY](tensors/0000141.npy) |
| 142 | `model.layers.0.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.625 / 44.0 / 0.03626914057466719 / 1.334387501786571 | [NPY](tensors/0000142.npy) |
| 143 | `model.layers.0.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.625 / 44.0 / 0.03626914057466719 / 1.334387501786571 | [NPY](tensors/0000143.npy) |
| 144 | `model.layers.0.self_attn` | 1 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.004596554445057111 / 0.045817391573268154 | [NPY](tensors/0000144.npy) |
| 145 | `model.layers.0.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 48.5 / -0.027747302585177953 / 2.8216031516189366 | [NPY](tensors/0000145.npy) |
| 146 | `model.layers.0.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0 / 1.6484375 / 0.0030477974149915907 / 0.4006557406987489 | [NPY](tensors/0000146.npy) |
| 147 | `model.layers.0.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0 / 1.6484375 / 0.0030477974149915907 / 0.4006557406987489 | [NPY](tensors/0000147.npy) |
| 148 | `model.layers.0.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.0 / 1.6484375 / 0.0030477974149915907 / 0.4006557406987489 | [NPY](tensors/0000148.npy) |
| 149 | `model.layers.0.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 150 | `model.layers.0.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 151 | `model.layers.0.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 152 | `model.layers.0.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.65625 / 23.25 / 0.017625713513957128 / 0.7170954508646846 | [NPY](tensors/0000152.npy) |
| 153 | `model.layers.0.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.65625 / 23.25 / 0.017625713513957128 / 0.7170954508646846 | [NPY](tensors/0000153.npy) |
| 154 | `model.layers.0.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.859375 / 1.9765625 / -0.0528106689453125 / 0.8128912067308136 | [NPY](tensors/0000154.npy) |
| 155 | `model.layers.0` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 72.0 / -0.01022118992275662 / 3.1591397401076065 | [NPY](tensors/0000155.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -41728.0 / 1088.0 / 0.4486721463992663 / 27.97918538530931 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1446, 1446] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6935936574925548e+38 / 1.6947652893570008e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1446, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6899605950889375 / 0.9333726687897778 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1446, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09463895696860526 / 0.6735252633541252 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 1446] | torch.int64 → int64 | 0.0 / 1445.0 / 722.5 / 417.4241448055762 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -41728.0 / 1088.0 / 0.4486721463992663 / 27.97918538530931 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 1446, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.061700226566352795 / 3.117880050523557 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1446, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.061700226566352795 / 3.117880050523557 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1446, 1446] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6935936574925548e+38 / 1.6947652893570008e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1446] | torch.int64 → int64 | 0.0 / 1445.0 / 722.5 / 417.4241448055762 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1446, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6899605950889375 / 0.9333726687897778 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1446, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09463895696860526 / 0.6735252633541252 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.061700226566352795 / 3.117880050523557 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 1446, 4096] | torch.bfloat16 → float32 | -14.0625 / 14.625 / 0.03941805347443467 / 1.322362055003698 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.061700226566352795 / 3.117880050523557 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 1446, 512] | torch.bfloat16 → float32 | -49.0 / 53.0 / 0.11015890151265846 / 3.928201193316688 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.061700226566352795 / 3.117880050523557 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 1446, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.02247543579985402 / 2.380803931777005 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1446, 4096] | torch.bfloat16 → float32 | -11.1875 / 12.9375 / -0.010244642972554834 / 1.3935848993440165 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 1446, 2880] | torch.bfloat16 → float32 | -474.0 / 432.0 / 0.018273064228061277 / 5.124662092762768 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -474.0 / 432.0 / 0.018273064228061277 / 5.124662092762768 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 1446, 1446] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0006231146721113109 / 0.007343133446181638 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -41728.0 / 640.0 / 0.4669233513937323 / 28.02310742627785 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 1446, 2880] | torch.bfloat16 → float32 | -78.5 / 7.8125 / 0.01043674252184192 / 0.7511670287504201 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -78.5 / 7.8125 / 0.01043674252184192 / 0.7511670287504201 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [1446, 2880] | torch.bfloat16 → float32 | -78.5 / 7.8125 / 0.01043674252184192 / 0.7511670287504201 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [1446, 2880] | torch.bfloat16 → float32 | -446.0 / 390.0 / 0.09827483029423797 / 7.4253642955577215 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -446.0 / 390.0 / 0.09827483029423797 / 7.4253642955577215 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [1446, 32] | torch.bfloat16 → float32 | -10.75 / 5.71875 / -0.1748461047313685 / 0.9506543577620681 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 1446, 2880] | torch.bfloat16 → float32 | -41728.0 / 864.0 / 0.5652199967218579 / 31.068052315564575 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -12672.0 / 14208.0 / -1.147741779065341 / 396.522663026974 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1446, 1446] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6935936574925548e+38 / 1.6947652893570008e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1446, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6899605950889375 / 0.9333726687897778 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1446, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09463895696860526 / 0.6735252633541252 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 1446] | torch.int64 → int64 | 0.0 / 1445.0 / 722.5 / 417.4241448055762 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -12672.0 / 14208.0 / -1.147741779065341 / 396.522663026974 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 1446, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010060922324225775 / 1.746507596523361 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1446, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010060922324225775 / 1.746507596523361 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1446, 1446] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6935936574925548e+38 / 1.6947652893570008e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1446] | torch.int64 → int64 | 0.0 / 1445.0 / 722.5 / 417.4241448055762 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1446, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6899605950889375 / 0.9333726687897778 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1446, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09463895696860526 / 0.6735252633541252 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010060922324225775 / 1.746507596523361 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 1446, 4096] | torch.bfloat16 → float32 | -20.75 / 28.25 / 0.02908116372331949 / 1.6433035861641723 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010060922324225775 / 1.746507596523361 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 1446, 512] | torch.bfloat16 → float32 | -90.5 / 72.0 / -0.054480943078471705 / 5.425685974208672 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010060922324225775 / 1.746507596523361 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 1446, 512] | torch.bfloat16 → float32 | -42.25 / 23.375 / -0.0024306560159629634 / 3.4437550482596535 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1446, 4096] | torch.bfloat16 → float32 | -36.25 / 17.625 / 0.00025747398274178913 / 1.3603854689797767 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 1446, 2880] | torch.bfloat16 → float32 | -8032.0 / 8576.0 / 3.348164972365796 / 174.25749107492234 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -8032.0 / 8576.0 / 3.348164972365796 / 174.25749107492234 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 1446, 1446] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.00038530572425839334 / 0.006058215231508539 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -11584.0 / 11392.0 / 2.2003994978205195 / 407.4319170314196 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 1446, 2880] | torch.bfloat16 → float32 | -50.75 / 22.5 / -0.011684827273074648 / 1.2631081748115895 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -50.75 / 22.5 / -0.011684827273074648 / 1.2631081748115895 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [1446, 2880] | torch.bfloat16 → float32 | -50.75 / 22.5 / -0.011684827273074648 / 1.2631081748115895 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [1446, 2880] | torch.bfloat16 → float32 | -6976.0 / 7072.0 / -1.7482379674142055 / 169.8254444658197 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 1446, 2880] | torch.bfloat16 → float32 | -6976.0 / 7072.0 / -1.7482379674142055 / 169.8254444658197 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [1446, 32] | torch.bfloat16 → float32 | -8.1875 / 4.96875 / 0.22241937570057468 / 2.4285876190851976 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 1446, 2880] | torch.bfloat16 → float32 | -11840.0 / 11968.0 / 0.4526021452933499 / 401.06314206582704 | [NPY](tensors/0000116.npy) |

## Registered modules that did not execute

- `model.layers.0.mlp.router` (GptOssTopKRouter)
- `model.layers.11.mlp.router` (GptOssTopKRouter)
- `model.layers.23.mlp.router` (GptOssTopKRouter)

## Interpretation

- Block input: residual operand for the Attention addition.
- post_attention_layernorm input: Attention residual result / MLP residual operand.
- MLP first return tensor: MLP branch before residual addition.
- Block first return tensor: after both residual additions, before final model norm.
- Router tuple slots, attention weights and fused expert internals depend on the installed backend. Use records.jsonl for exact paths, dtypes, nonfinite counts and availability.
