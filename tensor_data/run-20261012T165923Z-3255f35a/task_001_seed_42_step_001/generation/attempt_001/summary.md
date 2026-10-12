# Hook inspection: generation

Status: **complete**. 3870 full tensors; 5031 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -95.0 / 72.0 / -0.009262493796854997 / 2.790024840652027 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 287, 287] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.2122958518077407e+38 / 1.61381327794995e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 287, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8059103239704092 / 0.8702201565512877 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 287, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11909344536799918 / 0.6232883906716997 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 287] | torch.int64 → int64 | 0.0 / 286.0 / 143.0 / 82.84926070883192 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -95.0 / 72.0 / -0.009262493796854997 / 2.790024840652027 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 287, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.006446232493394251 / 0.7702745384585911 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 287, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.006446232493394251 / 0.7702745384585911 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 287, 287] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.2122958518077407e+38 / 1.61381327794995e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 287] | torch.int64 → int64 | 0.0 / 286.0 / 143.0 / 82.84926070883192 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 287, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8059103239704092 / 0.8702201565512877 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 287, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11909344536799918 / 0.6232883906716997 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.006446232493394251 / 0.7702745384585911 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 287, 4096] | torch.bfloat16 → float32 | -9.3125 / 12.25 / 0.02294550587479224 / 1.0151849093697118 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.006446232493394251 / 0.7702745384585911 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 287, 512] | torch.bfloat16 → float32 | -63.5 / 65.5 / 0.025347599480625645 / 5.7682243321717594 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.006446232493394251 / 0.7702745384585911 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 287, 512] | torch.bfloat16 → float32 | -6.84375 / 7.53125 / -0.011656391288345284 / 1.1879522616613098 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 287, 4096] | torch.bfloat16 → float32 | -6.84375 / 6.125 / -0.005279940004613988 / 0.533965589030992 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 287, 2880] | torch.bfloat16 → float32 | -38.5 / 52.25 / 0.026309765796550717 / 1.1610835599329559 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -38.5 / 52.25 / 0.026309765796550717 / 1.1610835599329559 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 287, 287] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0013913317634152182 / 0.024055735661845677 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -87.5 / 64.5 / 0.017040836312052728 / 2.9728394634650877 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 287, 2880] | torch.bfloat16 → float32 | -6.5 / 3.078125 / 0.0008908259951694501 / 0.3340196099604565 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -6.5 / 3.078125 / 0.0008908259951694501 / 0.3340196099604565 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [287, 2880] | torch.bfloat16 → float32 | -6.5 / 3.078125 / 0.0008908259951694501 / 0.3340196099604565 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [287, 2880] | torch.bfloat16 → float32 | -49.5 / 135.0 / 0.01717525678555194 / 0.867894513304826 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -49.5 / 135.0 / 0.01717525678555194 / 0.867894513304826 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [287, 32] | torch.bfloat16 → float32 | -5.1875 / 3.234375 / -0.11088175225340946 / 1.0219802129528321 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 287, 2880] | torch.bfloat16 → float32 | -85.0 / 156.0 / 0.03421974847171826 / 3.2326576690956283 | [NPY](tensors/0000038.npy) |
| 117 | `model.layers.0` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0000117.npy) |
| 118 | `model.layers.0` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000118.npy) |
| 119 | `model.layers.0` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.6712646484375 / 0.9670054124125442 | [NPY](tensors/0000119.npy) |
| 120 | `model.layers.0` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.12011004984378815 / 0.6397178164422894 | [NPY](tensors/0000120.npy) |
| 121 | `model.layers.0` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 287.0 / 287.0 / 287.0 / 0.0 | [NPY](tensors/0000121.npy) |
| 122 | `model.layers.0` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 123 | `model.layers.0` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 124 | `model.layers.0` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 125 | `model.layers.0.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0000125.npy) |
| 126 | `model.layers.0.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000126.npy) |
| 127 | `model.layers.0.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000127.npy) |
| 128 | `model.layers.0.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000128.npy) |
| 129 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 287.0 / 287.0 / 287.0 / 0.0 | [NPY](tensors/0000129.npy) |
| 130 | `model.layers.0.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 131 | `model.layers.0.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 132 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.6712646484375 / 0.9670054124125442 | [NPY](tensors/0000132.npy) |
| 133 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.12011004984378815 / 0.6397178164422894 | [NPY](tensors/0000133.npy) |
| 134 | `model.layers.0.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 135 | `model.layers.0.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000135.npy) |
| 136 | `model.layers.0.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.34375 / 8.125 / 0.009809806477278471 / 1.0602451281469458 | [NPY](tensors/0000136.npy) |
| 137 | `model.layers.0.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000137.npy) |
| 138 | `model.layers.0.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.5 / 52.75 / 0.05987404379993677 / 5.486411371880323 | [NPY](tensors/0000138.npy) |
| 139 | `model.layers.0.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000139.npy) |
| 140 | `model.layers.0.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.125 / 3.75 / 0.02330493927001953 / 1.1486258589347933 | [NPY](tensors/0000140.npy) |
| 141 | `model.layers.0.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 4.0 / -0.005132186284754425 / 0.7201158302115208 | [NPY](tensors/0000141.npy) |
| 142 | `model.layers.0.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.5 / 43.75 / 0.0374336302280426 / 1.3476549526644088 | [NPY](tensors/0000142.npy) |
| 143 | `model.layers.0.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.5 / 43.75 / 0.0374336302280426 / 1.3476549526644088 | [NPY](tensors/0000143.npy) |
| 144 | `model.layers.0.self_attn` | 1 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98046875 / 0.004510302599721868 / 0.044726340283383965 | [NPY](tensors/0000144.npy) |
| 145 | `model.layers.0.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 48.25 / -0.02656402587890625 / 2.8457933907683897 | [NPY](tensors/0000145.npy) |
| 146 | `model.layers.0.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.953125 / 1.625 / 0.003093605074617598 / 0.4000545904717944 | [NPY](tensors/0000146.npy) |
| 147 | `model.layers.0.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.953125 / 1.625 / 0.003093605074617598 / 0.4000545904717944 | [NPY](tensors/0000147.npy) |
| 148 | `model.layers.0.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.953125 / 1.625 / 0.003093605074617598 / 0.4000545904717944 | [NPY](tensors/0000148.npy) |
| 149 | `model.layers.0.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 150 | `model.layers.0.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 151 | `model.layers.0.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 152 | `model.layers.0.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.53125 / 22.125 / 0.018087322844399345 / 0.718407526513516 | [NPY](tensors/0000152.npy) |
| 153 | `model.layers.0.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.53125 / 22.125 / 0.018087322844399345 / 0.718407526513516 | [NPY](tensors/0000153.npy) |
| 154 | `model.layers.0.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.953125 / 1.828125 / -0.05750274658203125 / 0.8065243029472572 | [NPY](tensors/0000154.npy) |
| 155 | `model.layers.0` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 70.5 / -0.008365805943806965 / 3.173464791798555 | [NPY](tensors/0000155.npy) |
| 234 | `model.layers.0` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 34.75 / 0.06460592945416768 / 2.603620301499426 | [NPY](tensors/0000234.npy) |
| 235 | `model.layers.0` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000235.npy) |
| 236 | `model.layers.0` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.7242279052734375 / 0.9308467876495331 | [NPY](tensors/0000236.npy) |
| 237 | `model.layers.0` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.25 / 0.10570904612541199 / 0.6393518089241342 | [NPY](tensors/0000237.npy) |
| 238 | `model.layers.0` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 288.0 / 288.0 / 288.0 / 0.0 | [NPY](tensors/0000238.npy) |
| 239 | `model.layers.0` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 240 | `model.layers.0` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 241 | `model.layers.0` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 242 | `model.layers.0.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 34.75 / 0.06460592945416768 / 2.603620301499426 | [NPY](tensors/0000242.npy) |
| 243 | `model.layers.0.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0000243.npy) |
| 244 | `model.layers.0.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0000244.npy) |
| 245 | `model.layers.0.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000245.npy) |
| 246 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 288.0 / 288.0 / 288.0 / 0.0 | [NPY](tensors/0000246.npy) |
| 247 | `model.layers.0.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 248 | `model.layers.0.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 249 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.7242279052734375 / 0.9308467876495331 | [NPY](tensors/0000249.npy) |
| 250 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.25 / 0.10570904612541199 / 0.6393518089241342 | [NPY](tensors/0000250.npy) |
| 251 | `model.layers.0.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 252 | `model.layers.0.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0000252.npy) |
| 253 | `model.layers.0.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.71875 / 8.4375 / 0.008836216118652374 / 1.127863321857116 | [NPY](tensors/0000253.npy) |
| 254 | `model.layers.0.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0000254.npy) |
| 255 | `model.layers.0.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -47.25 / 52.5 / -0.01974540948867798 / 5.528074362257702 | [NPY](tensors/0000255.npy) |
| 256 | `model.layers.0.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0000256.npy) |
| 257 | `model.layers.0.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.34375 / 5.1875 / 0.04988500475883484 / 1.3788012115777875 | [NPY](tensors/0000257.npy) |
| 258 | `model.layers.0.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.90625 / 3.859375 / -0.004610374002368189 / 0.595354062703137 | [NPY](tensors/0000258.npy) |
| 259 | `model.layers.0.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.75 / 43.0 / 0.03180115040805605 / 1.274406233884986 | [NPY](tensors/0000259.npy) |
| 260 | `model.layers.0.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.75 / 43.0 / 0.03180115040805605 / 1.274406233884986 | [NPY](tensors/0000260.npy) |
| 261 | `model.layers.0.self_attn` | 2 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003145222661703766 / 0.037418338035918756 | [NPY](tensors/0000261.npy) |
| 262 | `model.layers.0.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 42.0 / 0.09632537629869249 / 2.903282211177423 | [NPY](tensors/0000262.npy) |
| 263 | `model.layers.0.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.75 / 1.5546875 / 0.004960115750630697 / 0.3841002614467395 | [NPY](tensors/0000263.npy) |
| 264 | `model.layers.0.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.75 / 1.5546875 / 0.004960115750630697 / 0.3841002614467395 | [NPY](tensors/0000264.npy) |
| 265 | `model.layers.0.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.75 / 1.5546875 / 0.004960115750630697 / 0.3841002614467395 | [NPY](tensors/0000265.npy) |
| 266 | `model.layers.0.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 267 | `model.layers.0.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 268 | `model.layers.0.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 269 | `model.layers.0.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.34375 / 22.625 / 0.02374889784389072 / 0.6980434413762364 | [NPY](tensors/0000269.npy) |
| 270 | `model.layers.0.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.34375 / 22.625 / 0.02374889784389072 / 0.6980434413762364 | [NPY](tensors/0000270.npy) |
| 271 | `model.layers.0.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.328125 / 1.90625 / -0.21349716186523438 / 0.8402714879195985 | [NPY](tensors/0000271.npy) |
| 272 | `model.layers.0` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 62.0 / 0.12003379397922093 / 3.1911695542717378 | [NPY](tensors/0000272.npy) |
| 351 | `model.layers.0` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0000351.npy) |
| 352 | `model.layers.0` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000352.npy) |
| 353 | `model.layers.0` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.76885986328125 / 0.9124536436370704 | [NPY](tensors/0000353.npy) |
| 354 | `model.layers.0` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2421875 / 0.1397949606180191 / 0.6049175711104398 | [NPY](tensors/0000354.npy) |
| 355 | `model.layers.0` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 289.0 / 289.0 / 289.0 / 0.0 | [NPY](tensors/0000355.npy) |
| 356 | `model.layers.0` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 357 | `model.layers.0` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 358 | `model.layers.0` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 359 | `model.layers.0.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0000359.npy) |
| 360 | `model.layers.0.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0000360.npy) |
| 361 | `model.layers.0.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0000361.npy) |
| 362 | `model.layers.0.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000362.npy) |
| 363 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 289.0 / 289.0 / 289.0 / 0.0 | [NPY](tensors/0000363.npy) |
| 364 | `model.layers.0.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 365 | `model.layers.0.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 366 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.76885986328125 / 0.9124536436370704 | [NPY](tensors/0000366.npy) |
| 367 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2421875 / 0.1397949606180191 / 0.6049175711104398 | [NPY](tensors/0000367.npy) |
| 368 | `model.layers.0.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 369 | `model.layers.0.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0000369.npy) |
| 370 | `model.layers.0.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 7.625 / 0.011268170550465584 / 0.9167789321734896 | [NPY](tensors/0000370.npy) |
| 371 | `model.layers.0.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0000371.npy) |
| 372 | `model.layers.0.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 43.75 / 0.046514674089848995 / 4.791095594233786 | [NPY](tensors/0000372.npy) |
| 373 | `model.layers.0.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0000373.npy) |
| 374 | `model.layers.0.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.84375 / 4.125 / -0.01808762550354004 / 1.3178383551916408 | [NPY](tensors/0000374.npy) |
| 375 | `model.layers.0.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.3125 / 4.875 / -0.010103763052029535 / 0.46443376906703904 | [NPY](tensors/0000375.npy) |
| 376 | `model.layers.0.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.25 / 40.25 / 0.025694271756543055 / 1.1911805704776828 | [NPY](tensors/0000376.npy) |
| 377 | `model.layers.0.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.25 / 40.25 / 0.025694271756543055 / 1.1911805704776828 | [NPY](tensors/0000377.npy) |
| 378 | `model.layers.0.self_attn` | 3 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.003218433533247086 / 0.02711749071891224 | [NPY](tensors/0000378.npy) |
| 379 | `model.layers.0.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 41.25 / 0.015193367004394531 / 2.8577994719379207 | [NPY](tensors/0000379.npy) |
| 380 | `model.layers.0.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.125 / 1.921875 / 0.006773049963845147 / 0.3728971489026009 | [NPY](tensors/0000380.npy) |
| 381 | `model.layers.0.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.125 / 1.921875 / 0.006773049963845147 / 0.3728971489026009 | [NPY](tensors/0000381.npy) |
| 382 | `model.layers.0.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.125 / 1.921875 / 0.006773049963845147 / 0.3728971489026009 | [NPY](tensors/0000382.npy) |
| 383 | `model.layers.0.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 384 | `model.layers.0.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 385 | `model.layers.0.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 386 | `model.layers.0.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.875 / 12.0625 / 0.03487643003463745 / 0.6320420699904978 | [NPY](tensors/0000386.npy) |
| 387 | `model.layers.0.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.875 / 12.0625 / 0.03487643003463745 / 0.6320420699904978 | [NPY](tensors/0000387.npy) |
| 388 | `model.layers.0.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0625 / 1.8046875 / -0.08551025390625 / 0.6484672901480346 | [NPY](tensors/0000388.npy) |
| 389 | `model.layers.0` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 53.25 / 0.05020161204867893 / 3.1494924446440025 | [NPY](tensors/0000389.npy) |
| 468 | `model.layers.0` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 43.75 / 0.02880006796783871 / 2.9013049797239288 | [NPY](tensors/0000468.npy) |
| 469 | `model.layers.0` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000469.npy) |
| 470 | `model.layers.0` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.77325439453125 / 0.9030595537086521 | [NPY](tensors/0000470.npy) |
| 471 | `model.layers.0` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2421875 / 0.19747132062911987 / 0.5978860929332719 | [NPY](tensors/0000471.npy) |
| 472 | `model.layers.0` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 290.0 / 290.0 / 290.0 / 0.0 | [NPY](tensors/0000472.npy) |
| 473 | `model.layers.0` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 474 | `model.layers.0` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 475 | `model.layers.0` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 476 | `model.layers.0.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 43.75 / 0.02880006796783871 / 2.9013049797239288 | [NPY](tensors/0000476.npy) |
| 477 | `model.layers.0.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000477.npy) |
| 478 | `model.layers.0.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000478.npy) |
| 479 | `model.layers.0.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000479.npy) |
| 480 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 290.0 / 290.0 / 290.0 / 0.0 | [NPY](tensors/0000480.npy) |
| 481 | `model.layers.0.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 482 | `model.layers.0.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 483 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.77325439453125 / 0.9030595537086521 | [NPY](tensors/0000483.npy) |
| 484 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2421875 / 0.19747132062911987 / 0.5978860929332719 | [NPY](tensors/0000484.npy) |
| 485 | `model.layers.0.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 486 | `model.layers.0.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000486.npy) |
| 487 | `model.layers.0.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 7.4375 / 0.039632019703276455 / 0.9975220123045838 | [NPY](tensors/0000487.npy) |
| 488 | `model.layers.0.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000488.npy) |
| 489 | `model.layers.0.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.5 / 41.25 / 0.060565054416656494 / 4.792407804689708 | [NPY](tensors/0000489.npy) |
| 490 | `model.layers.0.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000490.npy) |
| 491 | `model.layers.0.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.9375 / 3.90625 / 0.001153320074081421 / 1.2325447380756387 | [NPY](tensors/0000491.npy) |
| 492 | `model.layers.0.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.8125 / 3.25 / 0.0008042893605306745 / 0.6574672546486238 | [NPY](tensors/0000492.npy) |
| 493 | `model.layers.0.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.4375 / 41.5 / 0.04059134721755982 / 1.252603118410025 | [NPY](tensors/0000493.npy) |
| 494 | `model.layers.0.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.4375 / 41.5 / 0.04059134721755982 / 1.252603118410025 | [NPY](tensors/0000494.npy) |
| 495 | `model.layers.0.self_attn` | 4 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004084528943304815 / 0.04003374042971705 | [NPY](tensors/0000495.npy) |
| 496 | `model.layers.0.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 43.75 / 0.06931091944376627 / 3.0629681557363044 | [NPY](tensors/0000496.npy) |
| 497 | `model.layers.0.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.78125 / 2.125 / 0.008593725164731343 / 0.3549952983631354 | [NPY](tensors/0000497.npy) |
| 498 | `model.layers.0.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.78125 / 2.125 / 0.008593725164731343 / 0.3549952983631354 | [NPY](tensors/0000498.npy) |
| 499 | `model.layers.0.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.78125 / 2.125 / 0.008593725164731343 / 0.3549952983631354 | [NPY](tensors/0000499.npy) |
| 500 | `model.layers.0.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 501 | `model.layers.0.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 502 | `model.layers.0.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 503 | `model.layers.0.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.28125 / 33.75 / 0.0211177420285013 / 1.0939304723648478 | [NPY](tensors/0000503.npy) |
| 504 | `model.layers.0.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.28125 / 33.75 / 0.0211177420285013 / 1.0939304723648478 | [NPY](tensors/0000504.npy) |
| 505 | `model.layers.0.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.34375 / 2.296875 / -0.04593658447265625 / 0.9430068111666695 | [NPY](tensors/0000505.npy) |
| 506 | `model.layers.0` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 62.5 / 0.09039475123087565 / 3.3662799929457456 | [NPY](tensors/0000506.npy) |
| 585 | `model.layers.0` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 45.75 / 0.04227736194928487 / 3.1518798398795616 | [NPY](tensors/0000585.npy) |
| 586 | `model.layers.0` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000586.npy) |
| 587 | `model.layers.0` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.73895263671875 / 0.9515453580587002 | [NPY](tensors/0000587.npy) |
| 588 | `model.layers.0` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.8203125 / 1.265625 / 0.2415669560432434 / 0.5473552672930101 | [NPY](tensors/0000588.npy) |
| 589 | `model.layers.0` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 291.0 / 291.0 / 291.0 / 0.0 | [NPY](tensors/0000589.npy) |
| 590 | `model.layers.0` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 591 | `model.layers.0` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 592 | `model.layers.0` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 593 | `model.layers.0.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 45.75 / 0.04227736194928487 / 3.1518798398795616 | [NPY](tensors/0000593.npy) |
| 594 | `model.layers.0.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000594.npy) |
| 595 | `model.layers.0.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000595.npy) |
| 596 | `model.layers.0.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000596.npy) |
| 597 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 291.0 / 291.0 / 291.0 / 0.0 | [NPY](tensors/0000597.npy) |
| 598 | `model.layers.0.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 599 | `model.layers.0.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 600 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.73895263671875 / 0.9515453580587002 | [NPY](tensors/0000600.npy) |
| 601 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.8203125 / 1.265625 / 0.2415669560432434 / 0.5473552672930101 | [NPY](tensors/0000601.npy) |
| 602 | `model.layers.0.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 603 | `model.layers.0.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000603.npy) |
| 604 | `model.layers.0.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5 / 8.1875 / 0.022865560371428728 / 0.9733268065645532 | [NPY](tensors/0000604.npy) |
| 605 | `model.layers.0.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000605.npy) |
| 606 | `model.layers.0.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.75 / 47.0 / 0.09419560432434082 / 4.904277940788795 | [NPY](tensors/0000606.npy) |
| 607 | `model.layers.0.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000607.npy) |
| 608 | `model.layers.0.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 4.34375 / -0.08974748849868774 / 1.1126171556291353 | [NPY](tensors/0000608.npy) |
| 609 | `model.layers.0.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.1875 / 3.796875 / -0.008081591600785032 / 0.6012645012928962 | [NPY](tensors/0000609.npy) |
| 610 | `model.layers.0.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.71875 / 39.25 / 0.032179732248187064 / 1.1974818309834885 | [NPY](tensors/0000610.npy) |
| 611 | `model.layers.0.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.71875 / 39.25 / 0.032179732248187064 / 1.1974818309834885 | [NPY](tensors/0000611.npy) |
| 612 | `model.layers.0.self_attn` | 5 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004200806247515517 / 0.04297552008212808 | [NPY](tensors/0000612.npy) |
| 613 | `model.layers.0.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 46.75 / 0.0742861443095737 / 3.3281498743911566 | [NPY](tensors/0000613.npy) |
| 614 | `model.layers.0.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.171875 / 1.9609375 / 0.010478709141413372 / 0.323456474139304 | [NPY](tensors/0000614.npy) |
| 615 | `model.layers.0.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.171875 / 1.9609375 / 0.010478709141413372 / 0.323456474139304 | [NPY](tensors/0000615.npy) |
| 616 | `model.layers.0.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.171875 / 1.9609375 / 0.010478709141413372 / 0.323456474139304 | [NPY](tensors/0000616.npy) |
| 617 | `model.layers.0.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 618 | `model.layers.0.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 619 | `model.layers.0.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 620 | `model.layers.0.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.90625 / 16.0 / 0.02640501939588123 / 0.6738901219336562 | [NPY](tensors/0000620.npy) |
| 621 | `model.layers.0.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.90625 / 16.0 / 0.02640501939588123 / 0.6738901219336562 | [NPY](tensors/0000621.npy) |
| 622 | `model.layers.0.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.65625 / 1.9375 / -0.13210296630859375 / 1.0284867063473904 | [NPY](tensors/0000622.npy) |
| 623 | `model.layers.0` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 58.75 / 0.10078352822197809 / 3.430550208418501 | [NPY](tensors/0000623.npy) |
| 702 | `model.layers.0` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0000702.npy) |
| 703 | `model.layers.0` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000703.npy) |
| 704 | `model.layers.0` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.6932373046875 / 1.0101839228451497 | [NPY](tensors/0000704.npy) |
| 705 | `model.layers.0` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.80078125 / 1.3203125 / 0.25535039603710175 / 0.49363048052358244 | [NPY](tensors/0000705.npy) |
| 706 | `model.layers.0` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 292.0 / 292.0 / 292.0 / 0.0 | [NPY](tensors/0000706.npy) |
| 707 | `model.layers.0` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 708 | `model.layers.0` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 709 | `model.layers.0` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 710 | `model.layers.0.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0000710.npy) |
| 711 | `model.layers.0.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000711.npy) |
| 712 | `model.layers.0.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000712.npy) |
| 713 | `model.layers.0.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000713.npy) |
| 714 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 292.0 / 292.0 / 292.0 / 0.0 | [NPY](tensors/0000714.npy) |
| 715 | `model.layers.0.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 716 | `model.layers.0.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 717 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.6932373046875 / 1.0101839228451497 | [NPY](tensors/0000717.npy) |
| 718 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.80078125 / 1.3203125 / 0.25535039603710175 / 0.49363048052358244 | [NPY](tensors/0000718.npy) |
| 719 | `model.layers.0.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 720 | `model.layers.0.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000720.npy) |
| 721 | `model.layers.0.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 9.25 / 0.06582052947487682 / 1.0317253511582722 | [NPY](tensors/0000721.npy) |
| 722 | `model.layers.0.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000722.npy) |
| 723 | `model.layers.0.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.5 / 59.75 / -0.027341485023498535 / 6.496414800406944 | [NPY](tensors/0000723.npy) |
| 724 | `model.layers.0.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000724.npy) |
| 725 | `model.layers.0.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.453125 / 4.6875 / 0.06333106756210327 / 0.9556167387162166 | [NPY](tensors/0000725.npy) |
| 726 | `model.layers.0.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.21875 / 4.34375 / -0.01602612648275681 / 0.5825717788893111 | [NPY](tensors/0000726.npy) |
| 727 | `model.layers.0.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.25 / 40.5 / 0.03340401889549361 / 1.187979520087046 | [NPY](tensors/0000727.npy) |
| 728 | `model.layers.0.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.25 / 40.5 / 0.03340401889549361 / 1.187979520087046 | [NPY](tensors/0000728.npy) |
| 729 | `model.layers.0.self_attn` | 6 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0036940522299185475 / 0.04095233528547925 | [NPY](tensors/0000729.npy) |
| 730 | `model.layers.0.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 39.25 / 0.0824280924267239 / 2.662406205879419 | [NPY](tensors/0000730.npy) |
| 731 | `model.layers.0.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.421875 / 1.875 / 0.01092720992035336 / 0.3286461771041884 | [NPY](tensors/0000731.npy) |
| 732 | `model.layers.0.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.421875 / 1.875 / 0.01092720992035336 / 0.3286461771041884 | [NPY](tensors/0000732.npy) |
| 733 | `model.layers.0.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.421875 / 1.875 / 0.01092720992035336 / 0.3286461771041884 | [NPY](tensors/0000733.npy) |
| 734 | `model.layers.0.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 735 | `model.layers.0.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 736 | `model.layers.0.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 737 | `model.layers.0.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.8125 / 23.875 / 0.018700159961978595 / 0.9822182574168646 | [NPY](tensors/0000737.npy) |
| 738 | `model.layers.0.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 23.875 / 0.018700159961978595 / 0.9822182574168646 | [NPY](tensors/0000738.npy) |
| 739 | `model.layers.0.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.296875 / 2.484375 / -0.092620849609375 / 1.3027274687067807 | [NPY](tensors/0000739.npy) |
| 740 | `model.layers.0` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 61.5 / 0.100969484117296 / 2.8655318937696 | [NPY](tensors/0000740.npy) |
| 819 | `model.layers.0` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 32.5 / -0.009058822732832697 / 2.9289717824977175 | [NPY](tensors/0000819.npy) |
| 820 | `model.layers.0` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000820.npy) |
| 821 | `model.layers.0` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6579437255859375 / 0.9936083133652351 | [NPY](tensors/0000821.npy) |
| 822 | `model.layers.0` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.99609375 / 1.34375 / 0.25000885128974915 / 0.5715972585679053 | [NPY](tensors/0000822.npy) |
| 823 | `model.layers.0` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 293.0 / 293.0 / 293.0 / 0.0 | [NPY](tensors/0000823.npy) |
| 824 | `model.layers.0` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 825 | `model.layers.0` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 826 | `model.layers.0` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 827 | `model.layers.0.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 32.5 / -0.009058822732832697 / 2.9289717824977175 | [NPY](tensors/0000827.npy) |
| 828 | `model.layers.0.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0 / 8.4375 / -0.003499142411682341 / 0.756295290970313 | [NPY](tensors/0000828.npy) |
| 829 | `model.layers.0.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0 / 8.4375 / -0.003499142411682341 / 0.756295290970313 | [NPY](tensors/0000829.npy) |
| 830 | `model.layers.0.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000830.npy) |
| 831 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 293.0 / 293.0 / 293.0 / 0.0 | [NPY](tensors/0000831.npy) |
| 832 | `model.layers.0.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 833 | `model.layers.0.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 834 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6579437255859375 / 0.9936083133652351 | [NPY](tensors/0000834.npy) |
| 835 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.99609375 / 1.34375 / 0.25000885128974915 / 0.5715972585679053 | [NPY](tensors/0000835.npy) |
| 836 | `model.layers.0.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 837 | `model.layers.0.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0 / 8.4375 / -0.003499142411682341 / 0.756295290970313 | [NPY](tensors/0000837.npy) |
| 838 | `model.layers.0.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5 / 8.3125 / 0.03190597961656749 / 0.972221122494744 | [NPY](tensors/0000838.npy) |
| 839 | `model.layers.0.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0 / 8.4375 / -0.003499142411682341 / 0.756295290970313 | [NPY](tensors/0000839.npy) |
| 840 | `model.layers.0.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -46.5 / 49.25 / 0.053331129252910614 / 5.238182680079618 | [NPY](tensors/0000840.npy) |
| 841 | `model.layers.0.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0 / 8.4375 / -0.003499142411682341 / 0.756295290970313 | [NPY](tensors/0000841.npy) |
| 842 | `model.layers.0.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.90625 / 5.4375 / -0.061801716685295105 / 1.196117678001311 | [NPY](tensors/0000842.npy) |
| 843 | `model.layers.0.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.25 / 4.34375 / -0.01369868585607037 / 0.5412067962873487 | [NPY](tensors/0000843.npy) |
| 844 | `model.layers.0.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.3125 / 41.75 / 0.04147530042747449 / 1.2312980568381562 | [NPY](tensors/0000844.npy) |
| 845 | `model.layers.0.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.3125 / 41.75 / 0.04147530042747449 / 1.2312980568381562 | [NPY](tensors/0000845.npy) |
| 846 | `model.layers.0.self_attn` | 7 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0033497748551616297 / 0.0356859200055276 | [NPY](tensors/0000846.npy) |
| 847 | `model.layers.0.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 41.5 / 0.032526644070943196 / 3.0981585635161037 | [NPY](tensors/0000847.npy) |
| 848 | `model.layers.0.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.6875 / 1.6875 / 0.000615431202782525 / 0.33634545041422903 | [NPY](tensors/0000848.npy) |
| 849 | `model.layers.0.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.6875 / 1.6875 / 0.000615431202782525 / 0.33634545041422903 | [NPY](tensors/0000849.npy) |
| 850 | `model.layers.0.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.6875 / 1.6875 / 0.000615431202782525 / 0.33634545041422903 | [NPY](tensors/0000850.npy) |
| 851 | `model.layers.0.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 852 | `model.layers.0.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 853 | `model.layers.0.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 854 | `model.layers.0.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.3125 / 30.125 / 0.03690370379222764 / 0.9601718362963502 | [NPY](tensors/0000854.npy) |
| 855 | `model.layers.0.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.3125 / 30.125 / 0.03690370379222764 / 0.9601718362963502 | [NPY](tensors/0000855.npy) |
| 856 | `model.layers.0.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.015625 / 1.1484375 / -0.1434478759765625 / 0.8652844983634685 | [NPY](tensors/0000856.npy) |
| 857 | `model.layers.0` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 71.5 / 0.06928305361005994 / 3.482991980796552 | [NPY](tensors/0000857.npy) |
| 936 | `model.layers.0` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.25 / 47.5 / -0.07714509665966034 / 2.8903843139436933 | [NPY](tensors/0000936.npy) |
| 937 | `model.layers.0` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000937.npy) |
| 938 | `model.layers.0` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.63275146484375 / 0.9803225324656689 | [NPY](tensors/0000938.npy) |
| 939 | `model.layers.0` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.24692200124263763 / 0.6218146623522595 | [NPY](tensors/0000939.npy) |
| 940 | `model.layers.0` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 294.0 / 294.0 / 294.0 / 0.0 | [NPY](tensors/0000940.npy) |
| 941 | `model.layers.0` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 942 | `model.layers.0` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 943 | `model.layers.0` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 944 | `model.layers.0.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.25 / 47.5 / -0.07714509665966034 / 2.8903843139436933 | [NPY](tensors/0000944.npy) |
| 945 | `model.layers.0.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.8125 / 11.625 / -0.019445320632722644 / 0.7548993498126012 | [NPY](tensors/0000945.npy) |
| 946 | `model.layers.0.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.8125 / 11.625 / -0.019445320632722644 / 0.7548993498126012 | [NPY](tensors/0000946.npy) |
| 947 | `model.layers.0.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000947.npy) |
| 948 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 294.0 / 294.0 / 294.0 / 0.0 | [NPY](tensors/0000948.npy) |
| 949 | `model.layers.0.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 950 | `model.layers.0.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 951 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.63275146484375 / 0.9803225324656689 | [NPY](tensors/0000951.npy) |
| 952 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.24692200124263763 / 0.6218146623522595 | [NPY](tensors/0000952.npy) |
| 953 | `model.layers.0.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 954 | `model.layers.0.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.8125 / 11.625 / -0.019445320632722644 / 0.7548993498126012 | [NPY](tensors/0000954.npy) |
| 955 | `model.layers.0.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.09375 / 8.5625 / 0.007327124010771513 / 0.9674108364103003 | [NPY](tensors/0000955.npy) |
| 956 | `model.layers.0.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.8125 / 11.625 / -0.019445320632722644 / 0.7548993498126012 | [NPY](tensors/0000956.npy) |
| 957 | `model.layers.0.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -46.75 / 51.75 / -0.08909627050161362 / 5.483739429517544 | [NPY](tensors/0000957.npy) |
| 958 | `model.layers.0.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.8125 / 11.625 / -0.019445320632722644 / 0.7548993498126012 | [NPY](tensors/0000958.npy) |
| 959 | `model.layers.0.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.40625 / 5.3125 / -0.06997242569923401 / 1.277362917731272 | [NPY](tensors/0000959.npy) |
| 960 | `model.layers.0.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.21875 / 5.125 / -0.02024669139791513 / 0.5463272746743009 | [NPY](tensors/0000960.npy) |
| 961 | `model.layers.0.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 47.0 / 0.036342234909534456 / 1.4359279671535699 | [NPY](tensors/0000961.npy) |
| 962 | `model.layers.0.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 47.0 / 0.036342234909534456 / 1.4359279671535699 | [NPY](tensors/0000962.npy) |
| 963 | `model.layers.0.self_attn` | 8 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98046875 / 0.0029768865352184865 / 0.03457454098458765 | [NPY](tensors/0000963.npy) |
| 964 | `model.layers.0.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.75 / 47.25 / -0.04077272415161133 / 3.3116322335622765 | [NPY](tensors/0000964.npy) |
| 965 | `model.layers.0.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.40625 / 2.125 / 0.0012015783124499852 / 0.31571950195100257 | [NPY](tensors/0000965.npy) |
| 966 | `model.layers.0.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.40625 / 2.125 / 0.0012015783124499852 / 0.31571950195100257 | [NPY](tensors/0000966.npy) |
| 967 | `model.layers.0.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.40625 / 2.125 / 0.0012015783124499852 / 0.31571950195100257 | [NPY](tensors/0000967.npy) |
| 968 | `model.layers.0.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 969 | `model.layers.0.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 970 | `model.layers.0.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 971 | `model.layers.0.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.71875 / 20.25 / 0.011296783387660981 / 0.6210595849452826 | [NPY](tensors/0000971.npy) |
| 972 | `model.layers.0.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.71875 / 20.25 / 0.011296783387660981 / 0.6210595849452826 | [NPY](tensors/0000972.npy) |
| 973 | `model.layers.0.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.25 / 1.1484375 / -0.16301536560058594 / 0.6304077949428172 | [NPY](tensors/0000973.npy) |
| 974 | `model.layers.0` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.75 / 66.0 / -0.02932507726881239 / 3.5870379933427325 | [NPY](tensors/0000974.npy) |
| 1053 | `model.layers.0` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.75 / 35.0 / 0.029632277372810576 / 3.0790713420157756 | [NPY](tensors/0001053.npy) |
| 1054 | `model.layers.0` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001054.npy) |
| 1055 | `model.layers.0` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59735107421875 / 1.0432862341497364 | [NPY](tensors/0001055.npy) |
| 1056 | `model.layers.0` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.73828125 / 1.3046875 / 0.24880489706993103 / 0.5509575399105547 | [NPY](tensors/0001056.npy) |
| 1057 | `model.layers.0` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 295.0 / 295.0 / 295.0 / 0.0 | [NPY](tensors/0001057.npy) |
| 1058 | `model.layers.0` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1059 | `model.layers.0` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1060 | `model.layers.0` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1061 | `model.layers.0.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.75 / 35.0 / 0.029632277372810576 / 3.0790713420157756 | [NPY](tensors/0001061.npy) |
| 1062 | `model.layers.0.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0001062.npy) |
| 1063 | `model.layers.0.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0001063.npy) |
| 1064 | `model.layers.0.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001064.npy) |
| 1065 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 295.0 / 295.0 / 295.0 / 0.0 | [NPY](tensors/0001065.npy) |
| 1066 | `model.layers.0.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1067 | `model.layers.0.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1068 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59735107421875 / 1.0432862341497364 | [NPY](tensors/0001068.npy) |
| 1069 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.73828125 / 1.3046875 / 0.24880489706993103 / 0.5509575399105547 | [NPY](tensors/0001069.npy) |
| 1070 | `model.layers.0.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1071 | `model.layers.0.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0001071.npy) |
| 1072 | `model.layers.0.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.25 / 10.1875 / 0.01786483358591795 / 0.975573086522404 | [NPY](tensors/0001072.npy) |
| 1073 | `model.layers.0.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0001073.npy) |
| 1074 | `model.layers.0.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -55.5 / 43.25 / -0.043908245861530304 / 5.450620468537411 | [NPY](tensors/0001074.npy) |
| 1075 | `model.layers.0.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0001075.npy) |
| 1076 | `model.layers.0.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.84375 / 5.65625 / -0.12457606196403503 / 1.1890564225679914 | [NPY](tensors/0001076.npy) |
| 1077 | `model.layers.0.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.1875 / 4.8125 / -0.028739152738125995 / 0.6892308985430038 | [NPY](tensors/0001077.npy) |
| 1078 | `model.layers.0.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.25 / 45.0 / 0.045303498208522794 / 1.3399812792816108 | [NPY](tensors/0001078.npy) |
| 1079 | `model.layers.0.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.25 / 45.0 / 0.045303498208522794 / 1.3399812792816108 | [NPY](tensors/0001079.npy) |
| 1080 | `model.layers.0.self_attn` | 9 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003865040091374116 / 0.04196754137428159 | [NPY](tensors/0001080.npy) |
| 1081 | `model.layers.0.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.0 / 44.25 / 0.07498295704523722 / 3.4088378510664383 | [NPY](tensors/0001081.npy) |
| 1082 | `model.layers.0.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.171875 / 1.4609375 / 0.005614772770139906 / 0.3027767223883159 | [NPY](tensors/0001082.npy) |
| 1083 | `model.layers.0.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.171875 / 1.4609375 / 0.005614772770139906 / 0.3027767223883159 | [NPY](tensors/0001083.npy) |
| 1084 | `model.layers.0.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.171875 / 1.4609375 / 0.005614772770139906 / 0.3027767223883159 | [NPY](tensors/0001084.npy) |
| 1085 | `model.layers.0.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1086 | `model.layers.0.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1087 | `model.layers.0.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1088 | `model.layers.0.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.3125 / 24.875 / 0.02163122408092022 / 0.7628843878955307 | [NPY](tensors/0001088.npy) |
| 1089 | `model.layers.0.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.3125 / 24.875 / 0.02163122408092022 / 0.7628843878955307 | [NPY](tensors/0001089.npy) |
| 1090 | `model.layers.0.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.1875 / 1.609375 / -0.11709165573120117 / 0.7072841780812803 | [NPY](tensors/0001090.npy) |
| 1091 | `model.layers.0` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 69.0 / 0.09669018321567112 / 3.6576089630628124 | [NPY](tensors/0001091.npy) |
| 1170 | `model.layers.0` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 32.5 / 0.01878972484005822 / 2.7798793569859233 | [NPY](tensors/0001170.npy) |
| 1171 | `model.layers.0` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001171.npy) |
| 1172 | `model.layers.0` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.54443359375 / 1.0951336419407118 | [NPY](tensors/0001172.npy) |
| 1173 | `model.layers.0` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.2265625 / 0.23366539180278778 / 0.5085507755708512 | [NPY](tensors/0001173.npy) |
| 1174 | `model.layers.0` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 296.0 / 296.0 / 296.0 / 0.0 | [NPY](tensors/0001174.npy) |
| 1175 | `model.layers.0` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1176 | `model.layers.0` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1177 | `model.layers.0` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1178 | `model.layers.0.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 32.5 / 0.01878972484005822 / 2.7798793569859233 | [NPY](tensors/0001178.npy) |
| 1179 | `model.layers.0.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5 / 8.875 / -0.002318682604365879 / 0.7426183872737632 | [NPY](tensors/0001179.npy) |
| 1180 | `model.layers.0.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5 / 8.875 / -0.002318682604365879 / 0.7426183872737632 | [NPY](tensors/0001180.npy) |
| 1181 | `model.layers.0.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001181.npy) |
| 1182 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 296.0 / 296.0 / 296.0 / 0.0 | [NPY](tensors/0001182.npy) |
| 1183 | `model.layers.0.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1184 | `model.layers.0.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1185 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.54443359375 / 1.0951336419407118 | [NPY](tensors/0001185.npy) |
| 1186 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.2265625 / 0.23366539180278778 / 0.5085507755708512 | [NPY](tensors/0001186.npy) |
| 1187 | `model.layers.0.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1188 | `model.layers.0.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5 / 8.875 / -0.002318682604365879 / 0.7426183872737632 | [NPY](tensors/0001188.npy) |
| 1189 | `model.layers.0.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.3125 / 8.625 / 0.0474619222804904 / 0.9712427645837794 | [NPY](tensors/0001189.npy) |
| 1190 | `model.layers.0.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5 / 8.875 / -0.002318682604365879 / 0.7426183872737632 | [NPY](tensors/0001190.npy) |
| 1191 | `model.layers.0.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.25 / 51.5 / 0.03446221351623535 / 5.746072652121225 | [NPY](tensors/0001191.npy) |
| 1192 | `model.layers.0.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5 / 8.875 / -0.002318682604365879 / 0.7426183872737632 | [NPY](tensors/0001192.npy) |
| 1193 | `model.layers.0.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.265625 / 5.125 / 0.08859586715698242 / 1.003477910350097 | [NPY](tensors/0001193.npy) |
| 1194 | `model.layers.0.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.4375 / 4.15625 / -0.012417284888215363 / 0.5049260844036253 | [NPY](tensors/0001194.npy) |
| 1195 | `model.layers.0.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 39.25 / 0.046178751604424584 / 1.1533458700644328 | [NPY](tensors/0001195.npy) |
| 1196 | `model.layers.0.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 39.25 / 0.046178751604424584 / 1.1533458700644328 | [NPY](tensors/0001196.npy) |
| 1197 | `model.layers.0.self_attn` | 10 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002920070085077835 / 0.031162247789137745 | [NPY](tensors/0001197.npy) |
| 1198 | `model.layers.0.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.0 / 39.25 / 0.06489374902513292 / 2.9163733844377404 | [NPY](tensors/0001198.npy) |
| 1199 | `model.layers.0.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.96875 / 1.78125 / 0.0006146093209584554 / 0.30742556022750034 | [NPY](tensors/0001199.npy) |
| 1200 | `model.layers.0.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.96875 / 1.78125 / 0.0006146093209584554 / 0.30742556022750034 | [NPY](tensors/0001200.npy) |
| 1201 | `model.layers.0.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.96875 / 1.78125 / 0.0006146093209584554 / 0.30742556022750034 | [NPY](tensors/0001201.npy) |
| 1202 | `model.layers.0.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1203 | `model.layers.0.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1204 | `model.layers.0.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1205 | `model.layers.0.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.46875 / 25.625 / 0.03968140019310845 / 0.8469255592435596 | [NPY](tensors/0001205.npy) |
| 1206 | `model.layers.0.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.46875 / 25.625 / 0.03968140019310845 / 0.8469255592435596 | [NPY](tensors/0001206.npy) |
| 1207 | `model.layers.0.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.453125 / 2.359375 / -0.14180755615234375 / 0.9618068753650066 | [NPY](tensors/0001207.npy) |
| 1208 | `model.layers.0` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 62.75 / 0.1045423083835178 / 3.1843624189986004 | [NPY](tensors/0001208.npy) |
| 1287 | `model.layers.0` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 43.25 / -0.034352450587579776 / 3.143983932257166 | [NPY](tensors/0001287.npy) |
| 1288 | `model.layers.0` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001288.npy) |
| 1289 | `model.layers.0` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.4918212890625 / 1.117229907691466 | [NPY](tensors/0001289.npy) |
| 1290 | `model.layers.0` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.3359375 / 0.18026646971702576 / 0.5362459422402894 | [NPY](tensors/0001290.npy) |
| 1291 | `model.layers.0` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 297.0 / 297.0 / 297.0 / 0.0 | [NPY](tensors/0001291.npy) |
| 1292 | `model.layers.0` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1293 | `model.layers.0` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1294 | `model.layers.0` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1295 | `model.layers.0.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 43.25 / -0.034352450587579776 / 3.143983932257166 | [NPY](tensors/0001295.npy) |
| 1296 | `model.layers.0.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 7.0 / -0.010667433015381296 / 0.740064713677182 | [NPY](tensors/0001296.npy) |
| 1297 | `model.layers.0.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 7.0 / -0.010667433015381296 / 0.740064713677182 | [NPY](tensors/0001297.npy) |
| 1298 | `model.layers.0.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001298.npy) |
| 1299 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 297.0 / 297.0 / 297.0 / 0.0 | [NPY](tensors/0001299.npy) |
| 1300 | `model.layers.0.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1301 | `model.layers.0.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1302 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.4918212890625 / 1.117229907691466 | [NPY](tensors/0001302.npy) |
| 1303 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.3359375 / 0.18026646971702576 / 0.5362459422402894 | [NPY](tensors/0001303.npy) |
| 1304 | `model.layers.0.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1305 | `model.layers.0.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 7.0 / -0.010667433015381296 / 0.740064713677182 | [NPY](tensors/0001305.npy) |
| 1306 | `model.layers.0.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.96875 / 10.75 / 0.03389013931155205 / 1.0133434807008517 | [NPY](tensors/0001306.npy) |
| 1307 | `model.layers.0.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 7.0 / -0.010667433015381296 / 0.740064713677182 | [NPY](tensors/0001307.npy) |
| 1308 | `model.layers.0.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -55.0 / 59.0 / -0.017447173595428467 / 7.043934623847653 | [NPY](tensors/0001308.npy) |
| 1309 | `model.layers.0.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 7.0 / -0.010667433015381296 / 0.740064713677182 | [NPY](tensors/0001309.npy) |
| 1310 | `model.layers.0.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 4.3125 / 0.0012288093566894531 / 1.0756639608258283 | [NPY](tensors/0001310.npy) |
| 1311 | `model.layers.0.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.4375 / 4.3125 / -0.0004703717638676608 / 0.4577646781000253 | [NPY](tensors/0001311.npy) |
| 1312 | `model.layers.0.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.4375 / 32.75 / 0.0310063769419988 / 1.0196475310829038 | [NPY](tensors/0001312.npy) |
| 1313 | `model.layers.0.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.4375 / 32.75 / 0.0310063769419988 / 1.0196475310829038 | [NPY](tensors/0001313.npy) |
| 1314 | `model.layers.0.self_attn` | 11 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0025763534858757233 / 0.02787754883578079 | [NPY](tensors/0001314.npy) |
| 1315 | `model.layers.0.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 43.0 / -0.0032653384738498266 / 3.0660276910530135 | [NPY](tensors/0001315.npy) |
| 1316 | `model.layers.0.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.34375 / 1.6875 / 0.004564074012968275 / 0.26852371473004455 | [NPY](tensors/0001316.npy) |
| 1317 | `model.layers.0.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.34375 / 1.6875 / 0.004564074012968275 / 0.26852371473004455 | [NPY](tensors/0001317.npy) |
| 1318 | `model.layers.0.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.34375 / 1.6875 / 0.004564074012968275 / 0.26852371473004455 | [NPY](tensors/0001318.npy) |
| 1319 | `model.layers.0.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1320 | `model.layers.0.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1321 | `model.layers.0.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1322 | `model.layers.0.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.3125 / 7.4375 / -0.003806693148281839 / 0.5387832016393248 | [NPY](tensors/0001322.npy) |
| 1323 | `model.layers.0.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.3125 / 7.4375 / -0.003806693148281839 / 0.5387832016393248 | [NPY](tensors/0001323.npy) |
| 1324 | `model.layers.0.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.671875 / 2.71875 / -0.061603546142578125 / 1.2423106069596572 | [NPY](tensors/0001324.npy) |
| 1325 | `model.layers.0` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 41.5 / -0.007202800114949544 / 2.893677688598837 | [NPY](tensors/0001325.npy) |
| 1404 | `model.layers.0` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 41.0 / 0.03955754496985012 / 2.701753214068154 | [NPY](tensors/0001404.npy) |
| 1405 | `model.layers.0` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001405.npy) |
| 1406 | `model.layers.0` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.47601318359375 / 1.1300177711987256 | [NPY](tensors/0001406.npy) |
| 1407 | `model.layers.0` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2265625 / 0.09335732460021973 / 0.5447921260742894 | [NPY](tensors/0001407.npy) |
| 1408 | `model.layers.0` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 298.0 / 298.0 / 298.0 / 0.0 | [NPY](tensors/0001408.npy) |
| 1409 | `model.layers.0` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1410 | `model.layers.0` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1411 | `model.layers.0` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1412 | `model.layers.0.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 41.0 / 0.03955754496985012 / 2.701753214068154 | [NPY](tensors/0001412.npy) |
| 1413 | `model.layers.0.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.5 / 10.0625 / 0.0029281093842453425 / 0.8251928586446045 | [NPY](tensors/0001413.npy) |
| 1414 | `model.layers.0.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.5 / 10.0625 / 0.0029281093842453425 / 0.8251928586446045 | [NPY](tensors/0001414.npy) |
| 1415 | `model.layers.0.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001415.npy) |
| 1416 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 298.0 / 298.0 / 298.0 / 0.0 | [NPY](tensors/0001416.npy) |
| 1417 | `model.layers.0.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1418 | `model.layers.0.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1419 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.47601318359375 / 1.1300177711987256 | [NPY](tensors/0001419.npy) |
| 1420 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2265625 / 0.09335732460021973 / 0.5447921260742894 | [NPY](tensors/0001420.npy) |
| 1421 | `model.layers.0.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1422 | `model.layers.0.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.5 / 10.0625 / 0.0029281093842453425 / 0.8251928586446045 | [NPY](tensors/0001422.npy) |
| 1423 | `model.layers.0.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.71875 / 9.25 / 0.02498816657316638 / 1.0109400314006454 | [NPY](tensors/0001423.npy) |
| 1424 | `model.layers.0.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.5 / 10.0625 / 0.0029281093842453425 / 0.8251928586446045 | [NPY](tensors/0001424.npy) |
| 1425 | `model.layers.0.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.75 / 47.75 / 0.012916848063468933 / 5.3875171995196185 | [NPY](tensors/0001425.npy) |
| 1426 | `model.layers.0.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.5 / 10.0625 / 0.0029281093842453425 / 0.8251928586446045 | [NPY](tensors/0001426.npy) |
| 1427 | `model.layers.0.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.46875 / 5.59375 / -0.07838350534439087 / 1.2959394544050418 | [NPY](tensors/0001427.npy) |
| 1428 | `model.layers.0.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.4375 / 3.640625 / -0.01817828329281479 / 0.4236677625251357 | [NPY](tensors/0001428.npy) |
| 1429 | `model.layers.0.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.0 / 45.0 / 0.030329986413319906 / 1.3668935943289675 | [NPY](tensors/0001429.npy) |
| 1430 | `model.layers.0.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.0 / 45.0 / 0.030329986413319906 / 1.3668935943289675 | [NPY](tensors/0001430.npy) |
| 1431 | `model.layers.0.self_attn` | 12 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.002439398267189481 / 0.026561920767676973 | [NPY](tensors/0001431.npy) |
| 1432 | `model.layers.0.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 44.5 / 0.06995322439405653 / 3.106156386757989 | [NPY](tensors/0001432.npy) |
| 1433 | `model.layers.0.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.71875 / 2.046875 / 0.005338819821675619 / 0.3423231483989545 | [NPY](tensors/0001433.npy) |
| 1434 | `model.layers.0.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.71875 / 2.046875 / 0.005338819821675619 / 0.3423231483989545 | [NPY](tensors/0001434.npy) |
| 1435 | `model.layers.0.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.71875 / 2.046875 / 0.005338819821675619 / 0.3423231483989545 | [NPY](tensors/0001435.npy) |
| 1436 | `model.layers.0.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1437 | `model.layers.0.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1438 | `model.layers.0.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1439 | `model.layers.0.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.40625 / 15.25 / 0.014238736778497695 / 0.5088923580066675 | [NPY](tensors/0001439.npy) |
| 1440 | `model.layers.0.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.40625 / 15.25 / 0.014238736778497695 / 0.5088923580066675 | [NPY](tensors/0001440.npy) |
| 1441 | `model.layers.0.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.484375 / 1.5546875 / -0.1514129638671875 / 0.7268336843329183 | [NPY](tensors/0001441.npy) |
| 1442 | `model.layers.0` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.75 / 58.0 / 0.0842730787065294 / 3.386074155655847 | [NPY](tensors/0001442.npy) |
| 1521 | `model.layers.0` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001521.npy) |
| 1522 | `model.layers.0` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001522.npy) |
| 1523 | `model.layers.0` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.518310546875 / 1.0946292885024063 | [NPY](tensors/0001523.npy) |
| 1524 | `model.layers.0` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.234375 / 0.009437993168830872 / 0.5857162614275052 | [NPY](tensors/0001524.npy) |
| 1525 | `model.layers.0` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 299.0 / 299.0 / 299.0 / 0.0 | [NPY](tensors/0001525.npy) |
| 1526 | `model.layers.0` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1527 | `model.layers.0` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1528 | `model.layers.0` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1529 | `model.layers.0.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001529.npy) |
| 1530 | `model.layers.0.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001530.npy) |
| 1531 | `model.layers.0.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001531.npy) |
| 1532 | `model.layers.0.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001532.npy) |
| 1533 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 299.0 / 299.0 / 299.0 / 0.0 | [NPY](tensors/0001533.npy) |
| 1534 | `model.layers.0.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1535 | `model.layers.0.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1536 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.518310546875 / 1.0946292885024063 | [NPY](tensors/0001536.npy) |
| 1537 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.234375 / 0.009437993168830872 / 0.5857162614275052 | [NPY](tensors/0001537.npy) |
| 1538 | `model.layers.0.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1539 | `model.layers.0.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001539.npy) |
| 1540 | `model.layers.0.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.84375 / 8.5625 / 0.0153301190584898 / 1.0113524420299036 | [NPY](tensors/0001540.npy) |
| 1541 | `model.layers.0.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001541.npy) |
| 1542 | `model.layers.0.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.0 / 65.5 / 0.032654017210006714 / 6.89507515667232 | [NPY](tensors/0001542.npy) |
| 1543 | `model.layers.0.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001543.npy) |
| 1544 | `model.layers.0.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.28125 / 3.390625 / -0.002120666205883026 / 0.8566653376613583 | [NPY](tensors/0001544.npy) |
| 1545 | `model.layers.0.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.546875 / 4.15625 / -0.008414664247538894 / 0.4795364433749172 | [NPY](tensors/0001545.npy) |
| 1546 | `model.layers.0.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5625 / 31.375 / 0.032523035009702043 / 1.0223901045406907 | [NPY](tensors/0001546.npy) |
| 1547 | `model.layers.0.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5625 / 31.375 / 0.032523035009702043 / 1.0223901045406907 | [NPY](tensors/0001547.npy) |
| 1548 | `model.layers.0.self_attn` | 13 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003063883536896568 / 0.030923688796456947 | [NPY](tensors/0001548.npy) |
| 1549 | `model.layers.0.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.0 / 34.75 / 0.030545171101888022 / 3.059277465637533 | [NPY](tensors/0001549.npy) |
| 1550 | `model.layers.0.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.546875 / 1.421875 / 0.0034440630012088354 / 0.28726757143747644 | [NPY](tensors/0001550.npy) |
| 1551 | `model.layers.0.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.546875 / 1.421875 / 0.0034440630012088354 / 0.28726757143747644 | [NPY](tensors/0001551.npy) |
| 1552 | `model.layers.0.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.546875 / 1.421875 / 0.0034440630012088354 / 0.28726757143747644 | [NPY](tensors/0001552.npy) |
| 1553 | `model.layers.0.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1554 | `model.layers.0.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1555 | `model.layers.0.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1556 | `model.layers.0.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.1875 / 13.5625 / 0.016597825951046415 / 0.6796670926747921 | [NPY](tensors/0001556.npy) |
| 1557 | `model.layers.0.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.1875 / 13.5625 / 0.016597825951046415 / 0.6796670926747921 | [NPY](tensors/0001557.npy) |
| 1558 | `model.layers.0.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.375 / 2.921875 / -0.002773284912109375 / 1.5279156542924308 | [NPY](tensors/0001558.npy) |
| 1559 | `model.layers.0` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.75 / 48.25 / 0.047010334332784016 / 2.987555472579903 | [NPY](tensors/0001559.npy) |
| 1638 | `model.layers.0` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 49.25 / -0.03481262918147776 / 3.3040972398817177 | [NPY](tensors/0001638.npy) |
| 1639 | `model.layers.0` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001639.npy) |
| 1640 | `model.layers.0` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6011199951171875 / 1.029134772776266 | [NPY](tensors/0001640.npy) |
| 1641 | `model.layers.0` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.02744269371032715 / 0.6241199078176489 | [NPY](tensors/0001641.npy) |
| 1642 | `model.layers.0` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 300.0 / 300.0 / 300.0 / 0.0 | [NPY](tensors/0001642.npy) |
| 1643 | `model.layers.0` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1644 | `model.layers.0` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1645 | `model.layers.0` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1646 | `model.layers.0.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 49.25 / -0.03481262918147776 / 3.3040972398817177 | [NPY](tensors/0001646.npy) |
| 1647 | `model.layers.0.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001647.npy) |
| 1648 | `model.layers.0.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001648.npy) |
| 1649 | `model.layers.0.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001649.npy) |
| 1650 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 300.0 / 300.0 / 300.0 / 0.0 | [NPY](tensors/0001650.npy) |
| 1651 | `model.layers.0.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1652 | `model.layers.0.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1653 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6011199951171875 / 1.029134772776266 | [NPY](tensors/0001653.npy) |
| 1654 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.02744269371032715 / 0.6241199078176489 | [NPY](tensors/0001654.npy) |
| 1655 | `model.layers.0.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1656 | `model.layers.0.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001656.npy) |
| 1657 | `model.layers.0.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 6.25 / 0.025897369312588125 / 0.9110042125091211 | [NPY](tensors/0001657.npy) |
| 1658 | `model.layers.0.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001658.npy) |
| 1659 | `model.layers.0.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.75 / 46.25 / 0.08283017575740814 / 5.101942263816244 | [NPY](tensors/0001659.npy) |
| 1660 | `model.layers.0.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001660.npy) |
| 1661 | `model.layers.0.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.765625 / 3.28125 / 0.0731726735830307 / 0.9884409409989561 | [NPY](tensors/0001661.npy) |
| 1662 | `model.layers.0.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.671875 / 2.84375 / 0.007494508558011148 / 0.4326548712464359 | [NPY](tensors/0001662.npy) |
| 1663 | `model.layers.0.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.46875 / 35.25 / 0.03383281131585439 / 1.0463837800801954 | [NPY](tensors/0001663.npy) |
| 1664 | `model.layers.0.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.46875 / 35.25 / 0.03383281131585439 / 1.0463837800801954 | [NPY](tensors/0001664.npy) |
| 1665 | `model.layers.0.self_attn` | 14 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.00335143248150983 / 0.03321527985549887 | [NPY](tensors/0001665.npy) |
| 1666 | `model.layers.0.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 48.75 / -0.0009262111451890734 / 3.376224713886728 | [NPY](tensors/0001666.npy) |
| 1667 | `model.layers.0.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.109375 / 2.015625 / 0.0001078625520070394 / 0.29464070545691456 | [NPY](tensors/0001667.npy) |
| 1668 | `model.layers.0.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.109375 / 2.015625 / 0.0001078625520070394 / 0.29464070545691456 | [NPY](tensors/0001668.npy) |
| 1669 | `model.layers.0.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.109375 / 2.015625 / 0.0001078625520070394 / 0.29464070545691456 | [NPY](tensors/0001669.npy) |
| 1670 | `model.layers.0.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1671 | `model.layers.0.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1672 | `model.layers.0.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1673 | `model.layers.0.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.9375 / 21.75 / 0.03694841383645932 / 0.720091743375776 | [NPY](tensors/0001673.npy) |
| 1674 | `model.layers.0.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 21.75 / 0.03694841383645932 / 0.720091743375776 | [NPY](tensors/0001674.npy) |
| 1675 | `model.layers.0.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.390625 / 1.625 / -0.04761505126953125 / 0.9155245610194831 | [NPY](tensors/0001675.npy) |
| 1676 | `model.layers.0` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 50.0 / 0.035936297310723196 / 3.454192387854477 | [NPY](tensors/0001676.npy) |
| 1755 | `model.layers.0` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 34.5 / -0.00621017747455173 / 2.9689713325199563 | [NPY](tensors/0001755.npy) |
| 1756 | `model.layers.0` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001756.npy) |
| 1757 | `model.layers.0` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6781768798828125 / 0.9972778713983161 | [NPY](tensors/0001757.npy) |
| 1758 | `model.layers.0` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.0019666850566864014 / 0.5958225425092146 | [NPY](tensors/0001758.npy) |
| 1759 | `model.layers.0` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 301.0 / 301.0 / 301.0 / 0.0 | [NPY](tensors/0001759.npy) |
| 1760 | `model.layers.0` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1761 | `model.layers.0` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1762 | `model.layers.0` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1763 | `model.layers.0.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 34.5 / -0.00621017747455173 / 2.9689713325199563 | [NPY](tensors/0001763.npy) |
| 1764 | `model.layers.0.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 8.75 / -0.004585133658515083 / 0.7492337618014016 | [NPY](tensors/0001764.npy) |
| 1765 | `model.layers.0.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 8.75 / -0.004585133658515083 / 0.7492337618014016 | [NPY](tensors/0001765.npy) |
| 1766 | `model.layers.0.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001766.npy) |
| 1767 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 301.0 / 301.0 / 301.0 / 0.0 | [NPY](tensors/0001767.npy) |
| 1768 | `model.layers.0.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1769 | `model.layers.0.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1770 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6781768798828125 / 0.9972778713983161 | [NPY](tensors/0001770.npy) |
| 1771 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.0019666850566864014 / 0.5958225425092146 | [NPY](tensors/0001771.npy) |
| 1772 | `model.layers.0.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1773 | `model.layers.0.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 8.75 / -0.004585133658515083 / 0.7492337618014016 | [NPY](tensors/0001773.npy) |
| 1774 | `model.layers.0.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.625 / 10.125 / 0.029261586867505684 / 1.0112363812461085 | [NPY](tensors/0001774.npy) |
| 1775 | `model.layers.0.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 8.75 / -0.004585133658515083 / 0.7492337618014016 | [NPY](tensors/0001775.npy) |
| 1776 | `model.layers.0.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -56.75 / 46.75 / -0.0824456587433815 / 5.565340349748302 | [NPY](tensors/0001776.npy) |
| 1777 | `model.layers.0.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 8.75 / -0.004585133658515083 / 0.7492337618014016 | [NPY](tensors/0001777.npy) |
| 1778 | `model.layers.0.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.5625 / 5.90625 / -0.08182156085968018 / 1.2309353697889387 | [NPY](tensors/0001778.npy) |
| 1779 | `model.layers.0.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.21875 / 3.703125 / 0.012695263758359943 / 0.5153003900443363 | [NPY](tensors/0001779.npy) |
| 1780 | `model.layers.0.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.4375 / 46.25 / 0.04096394930448797 / 1.3737196809992906 | [NPY](tensors/0001780.npy) |
| 1781 | `model.layers.0.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.4375 / 46.25 / 0.04096394930448797 / 1.3737196809992906 | [NPY](tensors/0001781.npy) |
| 1782 | `model.layers.0.self_attn` | 15 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003302348384126741 / 0.03901301776151259 | [NPY](tensors/0001782.npy) |
| 1783 | `model.layers.0.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 44.25 / 0.03478164143032498 / 3.126197265958528 | [NPY](tensors/0001783.npy) |
| 1784 | `model.layers.0.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.765625 / 1.984375 / 0.003843998908996582 / 0.30915794252265405 | [NPY](tensors/0001784.npy) |
| 1785 | `model.layers.0.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.765625 / 1.984375 / 0.003843998908996582 / 0.30915794252265405 | [NPY](tensors/0001785.npy) |
| 1786 | `model.layers.0.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.765625 / 1.984375 / 0.003843998908996582 / 0.30915794252265405 | [NPY](tensors/0001786.npy) |
| 1787 | `model.layers.0.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1788 | `model.layers.0.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1789 | `model.layers.0.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1790 | `model.layers.0.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.625 / 38.5 / 0.04955862673620383 / 1.3047813600573341 | [NPY](tensors/0001790.npy) |
| 1791 | `model.layers.0.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.625 / 38.5 / 0.04955862673620383 / 1.3047813600573341 | [NPY](tensors/0001791.npy) |
| 1792 | `model.layers.0.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.59375 / 1.0859375 / -0.19982147216796875 / 0.6737784567353671 | [NPY](tensors/0001792.npy) |
| 1793 | `model.layers.0` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.875 / 75.5 / 0.08416679435306125 / 3.517685188719951 | [NPY](tensors/0001793.npy) |
| 1872 | `model.layers.0` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.75 / 35.0 / 0.029632277372810576 / 3.0790713420157756 | [NPY](tensors/0001872.npy) |
| 1873 | `model.layers.0` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001873.npy) |
| 1874 | `model.layers.0` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.707061767578125 / 0.9717983302810768 | [NPY](tensors/0001874.npy) |
| 1875 | `model.layers.0` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.234375 / 0.05849510431289673 / 0.601804974311013 | [NPY](tensors/0001875.npy) |
| 1876 | `model.layers.0` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 302.0 / 302.0 / 302.0 / 0.0 | [NPY](tensors/0001876.npy) |
| 1877 | `model.layers.0` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1878 | `model.layers.0` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1879 | `model.layers.0` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1880 | `model.layers.0.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.75 / 35.0 / 0.029632277372810576 / 3.0790713420157756 | [NPY](tensors/0001880.npy) |
| 1881 | `model.layers.0.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0001881.npy) |
| 1882 | `model.layers.0.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0001882.npy) |
| 1883 | `model.layers.0.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001883.npy) |
| 1884 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 302.0 / 302.0 / 302.0 / 0.0 | [NPY](tensors/0001884.npy) |
| 1885 | `model.layers.0.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1886 | `model.layers.0.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1887 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.707061767578125 / 0.9717983302810768 | [NPY](tensors/0001887.npy) |
| 1888 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.234375 / 0.05849510431289673 / 0.601804974311013 | [NPY](tensors/0001888.npy) |
| 1889 | `model.layers.0.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1890 | `model.layers.0.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0001890.npy) |
| 1891 | `model.layers.0.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.25 / 10.1875 / 0.01786483358591795 / 0.975573086522404 | [NPY](tensors/0001891.npy) |
| 1892 | `model.layers.0.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0001892.npy) |
| 1893 | `model.layers.0.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -55.5 / 43.25 / -0.043908245861530304 / 5.450620468537411 | [NPY](tensors/0001893.npy) |
| 1894 | `model.layers.0.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0001894.npy) |
| 1895 | `model.layers.0.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.84375 / 5.65625 / -0.12457606196403503 / 1.1890564225679914 | [NPY](tensors/0001895.npy) |
| 1896 | `model.layers.0.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.34375 / 5.59375 / -0.008582299131376203 / 0.6502623291223315 | [NPY](tensors/0001896.npy) |
| 1897 | `model.layers.0.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.6875 / 40.25 / 0.03046271043519179 / 1.2153534112161535 | [NPY](tensors/0001897.npy) |
| 1898 | `model.layers.0.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.6875 / 40.25 / 0.03046271043519179 / 1.2153534112161535 | [NPY](tensors/0001898.npy) |
| 1899 | `model.layers.0.self_attn` | 16 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.003733884784705012 / 0.04008494880773953 | [NPY](tensors/0001899.npy) |
| 1900 | `model.layers.0.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 41.5 / 0.06036287678612603 / 3.2943712407447645 | [NPY](tensors/0001900.npy) |
| 1901 | `model.layers.0.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.1875 / 1.5078125 / -0.0023370736175113253 / 0.3021710415003643 | [NPY](tensors/0001901.npy) |
| 1902 | `model.layers.0.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.1875 / 1.5078125 / -0.0023370736175113253 / 0.3021710415003643 | [NPY](tensors/0001902.npy) |
| 1903 | `model.layers.0.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.1875 / 1.5078125 / -0.0023370736175113253 / 0.3021710415003643 | [NPY](tensors/0001903.npy) |
| 1904 | `model.layers.0.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1905 | `model.layers.0.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1906 | `model.layers.0.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1907 | `model.layers.0.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.125 / 15.375 / 0.005053684115409851 / 0.5778716434837515 | [NPY](tensors/0001907.npy) |
| 1908 | `model.layers.0.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.125 / 15.375 / 0.005053684115409851 / 0.5778716434837515 | [NPY](tensors/0001908.npy) |
| 1909 | `model.layers.0.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.234375 / 1.40625 / -0.14682292938232422 / 0.6335126725002029 | [NPY](tensors/0001909.npy) |
| 1910 | `model.layers.0` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 56.5 / 0.06555485195583767 / 3.4669222614594837 | [NPY](tensors/0001910.npy) |
| 1989 | `model.layers.0` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001989.npy) |
| 1990 | `model.layers.0` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001990.npy) |
| 1991 | `model.layers.0` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.68243408203125 / 0.9684034292887866 | [NPY](tensors/0001991.npy) |
| 1992 | `model.layers.0` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3359375 / 0.10489383339881897 / 0.6297841334602801 | [NPY](tensors/0001992.npy) |
| 1993 | `model.layers.0` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 303.0 / 303.0 / 303.0 / 0.0 | [NPY](tensors/0001993.npy) |
| 1994 | `model.layers.0` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1995 | `model.layers.0` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1996 | `model.layers.0` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1997 | `model.layers.0.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001997.npy) |
| 1998 | `model.layers.0.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001998.npy) |
| 1999 | `model.layers.0.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001999.npy) |
| 2000 | `model.layers.0.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002000.npy) |
| 2001 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 303.0 / 303.0 / 303.0 / 0.0 | [NPY](tensors/0002001.npy) |
| 2002 | `model.layers.0.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2003 | `model.layers.0.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2004 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.68243408203125 / 0.9684034292887866 | [NPY](tensors/0002004.npy) |
| 2005 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3359375 / 0.10489383339881897 / 0.6297841334602801 | [NPY](tensors/0002005.npy) |
| 2006 | `model.layers.0.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2007 | `model.layers.0.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0002007.npy) |
| 2008 | `model.layers.0.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.84375 / 8.5625 / 0.0153301190584898 / 1.0113524420299036 | [NPY](tensors/0002008.npy) |
| 2009 | `model.layers.0.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0002009.npy) |
| 2010 | `model.layers.0.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.0 / 65.5 / 0.032654017210006714 / 6.89507515667232 | [NPY](tensors/0002010.npy) |
| 2011 | `model.layers.0.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0002011.npy) |
| 2012 | `model.layers.0.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.28125 / 3.390625 / -0.002120666205883026 / 0.8566653376613583 | [NPY](tensors/0002012.npy) |
| 2013 | `model.layers.0.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.53125 / 3.390625 / 0.011594074391268805 / 0.4814857403224971 | [NPY](tensors/0002013.npy) |
| 2014 | `model.layers.0.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.5625 / 31.25 / 0.032723042803506054 / 1.0362628810946088 | [NPY](tensors/0002014.npy) |
| 2015 | `model.layers.0.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.5625 / 31.25 / 0.032723042803506054 / 1.0362628810946088 | [NPY](tensors/0002015.npy) |
| 2016 | `model.layers.0.self_attn` | 17 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0033197744466951272 / 0.033926596856823345 | [NPY](tensors/0002016.npy) |
| 2017 | `model.layers.0.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.125 / 34.5 / 0.030639076232910158 / 3.0267638726396493 | [NPY](tensors/0002017.npy) |
| 2018 | `model.layers.0.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.53125 / 1.421875 / 0.0012250992986891005 / 0.2876022476163168 | [NPY](tensors/0002018.npy) |
| 2019 | `model.layers.0.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.53125 / 1.421875 / 0.0012250992986891005 / 0.2876022476163168 | [NPY](tensors/0002019.npy) |
| 2020 | `model.layers.0.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.53125 / 1.421875 / 0.0012250992986891005 / 0.2876022476163168 | [NPY](tensors/0002020.npy) |
| 2021 | `model.layers.0.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2022 | `model.layers.0.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2023 | `model.layers.0.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2024 | `model.layers.0.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.53125 / 10.6875 / 0.024012840456432767 / 0.6616272666716899 | [NPY](tensors/0002024.npy) |
| 2025 | `model.layers.0.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.53125 / 10.6875 / 0.024012840456432767 / 0.6616272666716899 | [NPY](tensors/0002025.npy) |
| 2026 | `model.layers.0.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.34375 / 2.875 / -0.014003753662109375 / 1.5155872342214591 | [NPY](tensors/0002026.npy) |
| 2027 | `model.layers.0` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.5 / 45.25 / 0.05470776557922363 / 2.9005191500038 | [NPY](tensors/0002027.npy) |
| 2106 | `model.layers.0` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 32.75 / 0.03959848284721375 / 2.636727096419094 | [NPY](tensors/0002106.npy) |
| 2107 | `model.layers.0` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002107.npy) |
| 2108 | `model.layers.0` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6405029296875 / 1.0356892994687845 | [NPY](tensors/0002108.npy) |
| 2109 | `model.layers.0` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1875 / 1.2421875 / 0.10542488098144531 / 0.5631099040524371 | [NPY](tensors/0002109.npy) |
| 2110 | `model.layers.0` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 304.0 / 304.0 / 304.0 / 0.0 | [NPY](tensors/0002110.npy) |
| 2111 | `model.layers.0` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2112 | `model.layers.0` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2113 | `model.layers.0` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2114 | `model.layers.0.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 32.75 / 0.03959848284721375 / 2.636727096419094 | [NPY](tensors/0002114.npy) |
| 2115 | `model.layers.0.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002115.npy) |
| 2116 | `model.layers.0.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002116.npy) |
| 2117 | `model.layers.0.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002117.npy) |
| 2118 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 304.0 / 304.0 / 304.0 / 0.0 | [NPY](tensors/0002118.npy) |
| 2119 | `model.layers.0.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2120 | `model.layers.0.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2121 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6405029296875 / 1.0356892994687845 | [NPY](tensors/0002121.npy) |
| 2122 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1875 / 1.2421875 / 0.10542488098144531 / 0.5631099040524371 | [NPY](tensors/0002122.npy) |
| 2123 | `model.layers.0.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2124 | `model.layers.0.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002124.npy) |
| 2125 | `model.layers.0.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.0625 / 6.78125 / -0.006842018279712647 / 0.8517376388261615 | [NPY](tensors/0002125.npy) |
| 2126 | `model.layers.0.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002126.npy) |
| 2127 | `model.layers.0.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.25 / 35.75 / 0.051442623138427734 / 3.999531927842787 | [NPY](tensors/0002127.npy) |
| 2128 | `model.layers.0.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002128.npy) |
| 2129 | `model.layers.0.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 4.625 / 0.04163137078285217 / 1.1435466539669636 | [NPY](tensors/0002129.npy) |
| 2130 | `model.layers.0.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.03125 / 2.71875 / 0.0010730749854701571 / 0.40438378767158445 | [NPY](tensors/0002130.npy) |
| 2131 | `model.layers.0.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.875 / 42.5 / 0.031832978791660735 / 1.2901430904863034 | [NPY](tensors/0002131.npy) |
| 2132 | `model.layers.0.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.875 / 42.5 / 0.031832978791660735 / 1.2901430904863034 | [NPY](tensors/0002132.npy) |
| 2133 | `model.layers.0.self_attn` | 18 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.95703125 / 0.0029927242682479148 / 0.02768667544919042 | [NPY](tensors/0002133.npy) |
| 2134 | `model.layers.0.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.0 / 41.25 / 0.07141548792521159 / 2.9465911017284308 | [NPY](tensors/0002134.npy) |
| 2135 | `model.layers.0.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.21875 / 1.6484375 / 8.491608831617567e-05 / 0.3709274065652964 | [NPY](tensors/0002135.npy) |
| 2136 | `model.layers.0.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.21875 / 1.6484375 / 8.491608831617567e-05 / 0.3709274065652964 | [NPY](tensors/0002136.npy) |
| 2137 | `model.layers.0.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.21875 / 1.6484375 / 8.491608831617567e-05 / 0.3709274065652964 | [NPY](tensors/0002137.npy) |
| 2138 | `model.layers.0.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2139 | `model.layers.0.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2140 | `model.layers.0.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2141 | `model.layers.0.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.28125 / 15.5 / 0.03632880730761422 / 0.6890893077386662 | [NPY](tensors/0002141.npy) |
| 2142 | `model.layers.0.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.28125 / 15.5 / 0.03632880730761422 / 0.6890893077386662 | [NPY](tensors/0002142.npy) |
| 2143 | `model.layers.0.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6015625 / 1.4140625 / -0.19287109375 / 0.7467724673866603 | [NPY](tensors/0002143.npy) |
| 2144 | `model.layers.0` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 56.75 / 0.10787653923034668 / 3.2531445737523748 | [NPY](tensors/0002144.npy) |
| 2223 | `model.layers.0` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 32.5 / 0.02340112761594355 / 2.5180141341639093 | [NPY](tensors/0002223.npy) |
| 2224 | `model.layers.0` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002224.npy) |
| 2225 | `model.layers.0` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0002225.npy) |
| 2226 | `model.layers.0` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0002226.npy) |
| 2227 | `model.layers.0` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0002227.npy) |
| 2228 | `model.layers.0` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2229 | `model.layers.0` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2230 | `model.layers.0` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2231 | `model.layers.0.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 32.5 / 0.02340112761594355 / 2.5180141341639093 | [NPY](tensors/0002231.npy) |
| 2232 | `model.layers.0.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002232.npy) |
| 2233 | `model.layers.0.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002233.npy) |
| 2234 | `model.layers.0.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002234.npy) |
| 2235 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0002235.npy) |
| 2236 | `model.layers.0.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2237 | `model.layers.0.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2238 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0002238.npy) |
| 2239 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0002239.npy) |
| 2240 | `model.layers.0.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2241 | `model.layers.0.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002241.npy) |
| 2242 | `model.layers.0.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.4375 / 5.40625 / -0.007190447126049548 / 0.8410779943508924 | [NPY](tensors/0002242.npy) |
| 2243 | `model.layers.0.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002243.npy) |
| 2244 | `model.layers.0.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.375 / 29.25 / -0.0019535720348358154 / 3.219451134212101 | [NPY](tensors/0002244.npy) |
| 2245 | `model.layers.0.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002245.npy) |
| 2246 | `model.layers.0.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.71875 / 3.5625 / -0.03649583458900452 / 1.2017397564519863 | [NPY](tensors/0002246.npy) |
| 2247 | `model.layers.0.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.09375 / 3.9375 / 0.013717840425670147 / 0.549679412443397 | [NPY](tensors/0002247.npy) |
| 2248 | `model.layers.0.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 45.25 / 0.02797563067740864 / 1.444461037613985 | [NPY](tensors/0002248.npy) |
| 2249 | `model.layers.0.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 45.25 / 0.02797563067740864 / 1.444461037613985 | [NPY](tensors/0002249.npy) |
| 2250 | `model.layers.0.self_attn` | 19 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0037658450298630416 / 0.034909867170175864 | [NPY](tensors/0002250.npy) |
| 2251 | `model.layers.0.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 47.25 / 0.05126122898525662 / 2.9759292828253194 | [NPY](tensors/0002251.npy) |
| 2252 | `model.layers.0.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.109375 / 1.640625 / -0.0051158183150821265 / 0.37640495256249207 | [NPY](tensors/0002252.npy) |
| 2253 | `model.layers.0.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.109375 / 1.640625 / -0.0051158183150821265 / 0.37640495256249207 | [NPY](tensors/0002253.npy) |
| 2254 | `model.layers.0.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.109375 / 1.640625 / -0.0051158183150821265 / 0.37640495256249207 | [NPY](tensors/0002254.npy) |
| 2255 | `model.layers.0.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2256 | `model.layers.0.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2257 | `model.layers.0.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2258 | `model.layers.0.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.375 / 5.875 / 0.019770103030734593 / 0.4620809663312991 | [NPY](tensors/0002258.npy) |
| 2259 | `model.layers.0.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.375 / 5.875 / 0.019770103030734593 / 0.4620809663312991 | [NPY](tensors/0002259.npy) |
| 2260 | `model.layers.0.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.65625 / 1.2578125 / -0.17955780029296875 / 0.6884368559956596 | [NPY](tensors/0002260.npy) |
| 2261 | `model.layers.0` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 49.0 / 0.07116861873202854 / 3.122144619565526 | [NPY](tensors/0002261.npy) |
| 2340 | `model.layers.0` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.25 / 32.0 / 0.061791101429197526 / 2.238756913453412 | [NPY](tensors/0002340.npy) |
| 2341 | `model.layers.0` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002341.npy) |
| 2342 | `model.layers.0` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0002342.npy) |
| 2343 | `model.layers.0` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0002343.npy) |
| 2344 | `model.layers.0` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0002344.npy) |
| 2345 | `model.layers.0` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2346 | `model.layers.0` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2347 | `model.layers.0` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2348 | `model.layers.0.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.25 / 32.0 / 0.061791101429197526 / 2.238756913453412 | [NPY](tensors/0002348.npy) |
| 2349 | `model.layers.0.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002349.npy) |
| 2350 | `model.layers.0.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002350.npy) |
| 2351 | `model.layers.0.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002351.npy) |
| 2352 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0002352.npy) |
| 2353 | `model.layers.0.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2354 | `model.layers.0.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2355 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0002355.npy) |
| 2356 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0002356.npy) |
| 2357 | `model.layers.0.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2358 | `model.layers.0.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002358.npy) |
| 2359 | `model.layers.0.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.375 / 8.125 / 0.007972375839017332 / 1.0483744761991842 | [NPY](tensors/0002359.npy) |
| 2360 | `model.layers.0.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002360.npy) |
| 2361 | `model.layers.0.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.0 / 52.0 / -0.06352853029966354 / 5.834851084637073 | [NPY](tensors/0002361.npy) |
| 2362 | `model.layers.0.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002362.npy) |
| 2363 | `model.layers.0.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.75 / 4.5 / 0.031710169510915875 / 1.4942407070139319 | [NPY](tensors/0002363.npy) |
| 2364 | `model.layers.0.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.6875 / 3.546875 / -0.019981834615464322 / 0.7170334228945925 | [NPY](tensors/0002364.npy) |
| 2365 | `model.layers.0.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.0 / 41.25 / 0.015798440648035872 / 1.3108362028885252 | [NPY](tensors/0002365.npy) |
| 2366 | `model.layers.0.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.0 / 41.25 / 0.015798440648035872 / 1.3108362028885252 | [NPY](tensors/0002366.npy) |
| 2367 | `model.layers.0.self_attn` | 20 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.004356023662767774 / 0.045307230723716396 | [NPY](tensors/0002367.npy) |
| 2368 | `model.layers.0.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 41.0 / 0.07744897736443414 / 2.6226829780375382 | [NPY](tensors/0002368.npy) |
| 2369 | `model.layers.0.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.40625 / 1.7890625 / 0.008066860834757487 / 0.45168644822787835 | [NPY](tensors/0002369.npy) |
| 2370 | `model.layers.0.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.40625 / 1.7890625 / 0.008066860834757487 / 0.45168644822787835 | [NPY](tensors/0002370.npy) |
| 2371 | `model.layers.0.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.40625 / 1.7890625 / 0.008066860834757487 / 0.45168644822787835 | [NPY](tensors/0002371.npy) |
| 2372 | `model.layers.0.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2373 | `model.layers.0.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2374 | `model.layers.0.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2375 | `model.layers.0.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.875 / 35.5 / 0.01891016869081391 / 1.1402939137586496 | [NPY](tensors/0002375.npy) |
| 2376 | `model.layers.0.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.875 / 35.5 / 0.01891016869081391 / 1.1402939137586496 | [NPY](tensors/0002376.npy) |
| 2377 | `model.layers.0.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.15625 / 1.796875 / -0.17085349559783936 / 0.7959784838906326 | [NPY](tensors/0002377.npy) |
| 2378 | `model.layers.0` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.75 / 76.0 / 0.09636648495992024 / 3.256496178418876 | [NPY](tensors/0002378.npy) |
| 2457 | `model.layers.0` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0002457.npy) |
| 2458 | `model.layers.0` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002458.npy) |
| 2459 | `model.layers.0` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0002459.npy) |
| 2460 | `model.layers.0` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0002460.npy) |
| 2461 | `model.layers.0` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0002461.npy) |
| 2462 | `model.layers.0` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2463 | `model.layers.0` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2464 | `model.layers.0` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2465 | `model.layers.0.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0002465.npy) |
| 2466 | `model.layers.0.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002466.npy) |
| 2467 | `model.layers.0.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002467.npy) |
| 2468 | `model.layers.0.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002468.npy) |
| 2469 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0002469.npy) |
| 2470 | `model.layers.0.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2471 | `model.layers.0.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2472 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0002472.npy) |
| 2473 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0002473.npy) |
| 2474 | `model.layers.0.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2475 | `model.layers.0.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002475.npy) |
| 2476 | `model.layers.0.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.34375 / 8.125 / 0.009809806477278471 / 1.0602451281469458 | [NPY](tensors/0002476.npy) |
| 2477 | `model.layers.0.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002477.npy) |
| 2478 | `model.layers.0.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.5 / 52.75 / 0.05987404379993677 / 5.486411371880323 | [NPY](tensors/0002478.npy) |
| 2479 | `model.layers.0.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002479.npy) |
| 2480 | `model.layers.0.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.125 / 3.75 / 0.02330493927001953 / 1.1486258589347933 | [NPY](tensors/0002480.npy) |
| 2481 | `model.layers.0.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 4.0 / 0.003241180704208091 / 0.7358744651189664 | [NPY](tensors/0002481.npy) |
| 2482 | `model.layers.0.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.75 / 44.25 / 0.03696266313393911 / 1.3355528337066351 | [NPY](tensors/0002482.npy) |
| 2483 | `model.layers.0.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.75 / 44.25 / 0.03696266313393911 / 1.3355528337066351 | [NPY](tensors/0002483.npy) |
| 2484 | `model.layers.0.self_attn` | 21 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.004672837702076309 / 0.04619051109498539 | [NPY](tensors/0002484.npy) |
| 2485 | `model.layers.0.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 48.75 / -0.027000766330295137 / 2.8378357673121593 | [NPY](tensors/0002485.npy) |
| 2486 | `model.layers.0.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.03125 / 1.640625 / 0.0032856371667650012 / 0.4004836741524095 | [NPY](tensors/0002486.npy) |
| 2487 | `model.layers.0.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.03125 / 1.640625 / 0.0032856371667650012 / 0.4004836741524095 | [NPY](tensors/0002487.npy) |
| 2488 | `model.layers.0.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.03125 / 1.640625 / 0.0032856371667650012 / 0.4004836741524095 | [NPY](tensors/0002488.npy) |
| 2489 | `model.layers.0.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2490 | `model.layers.0.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2491 | `model.layers.0.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2492 | `model.layers.0.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.34375 / 25.0 / 0.021414592882825267 / 0.7543651799396668 | [NPY](tensors/0002492.npy) |
| 2493 | `model.layers.0.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.34375 / 25.0 / 0.021414592882825267 / 0.7543651799396668 | [NPY](tensors/0002493.npy) |
| 2494 | `model.layers.0.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9140625 / 1.953125 / -0.044677734375 / 0.8356596939656746 | [NPY](tensors/0002494.npy) |
| 2495 | `model.layers.0` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 74.0 / -0.005607324176364475 / 3.200460819183013 | [NPY](tensors/0002495.npy) |
| 2574 | `model.layers.0` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.5 / 35.0 / -0.07696556953920258 / 2.4397689873402366 | [NPY](tensors/0002574.npy) |
| 2575 | `model.layers.0` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002575.npy) |
| 2576 | `model.layers.0` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0002576.npy) |
| 2577 | `model.layers.0` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0002577.npy) |
| 2578 | `model.layers.0` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0002578.npy) |
| 2579 | `model.layers.0` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2580 | `model.layers.0` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2581 | `model.layers.0` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2582 | `model.layers.0.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.5 / 35.0 / -0.07696556953920258 / 2.4397689873402366 | [NPY](tensors/0002582.npy) |
| 2583 | `model.layers.0.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.1875 / 10.9375 / -0.028581078350543975 / 0.7922689698645601 | [NPY](tensors/0002583.npy) |
| 2584 | `model.layers.0.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.1875 / 10.9375 / -0.028581078350543975 / 0.7922689698645601 | [NPY](tensors/0002584.npy) |
| 2585 | `model.layers.0.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002585.npy) |
| 2586 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0002586.npy) |
| 2587 | `model.layers.0.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2588 | `model.layers.0.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2589 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0002589.npy) |
| 2590 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0002590.npy) |
| 2591 | `model.layers.0.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2592 | `model.layers.0.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.1875 / 10.9375 / -0.028581078350543975 / 0.7922689698645601 | [NPY](tensors/0002592.npy) |
| 2593 | `model.layers.0.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.71875 / 8.8125 / 0.02896638447418809 / 1.0597160611273537 | [NPY](tensors/0002593.npy) |
| 2594 | `model.layers.0.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.1875 / 10.9375 / -0.028581078350543975 / 0.7922689698645601 | [NPY](tensors/0002594.npy) |
| 2595 | `model.layers.0.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -46.25 / 56.25 / 0.03592613339424133 / 5.733245040932467 | [NPY](tensors/0002595.npy) |
| 2596 | `model.layers.0.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.1875 / 10.9375 / -0.028581078350543975 / 0.7922689698645601 | [NPY](tensors/0002596.npy) |
| 2597 | `model.layers.0.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.03125 / 4.3125 / -0.08557575941085815 / 1.4700339890570895 | [NPY](tensors/0002597.npy) |
| 2598 | `model.layers.0.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.03125 / 2.890625 / -0.011096805639681406 / 0.45865561307263975 | [NPY](tensors/0002598.npy) |
| 2599 | `model.layers.0.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.875 / 44.75 / 0.021746825509601168 / 1.3213822570392726 | [NPY](tensors/0002599.npy) |
| 2600 | `model.layers.0.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.875 / 44.75 / 0.021746825509601168 / 1.3213822570392726 | [NPY](tensors/0002600.npy) |
| 2601 | `model.layers.0.self_attn` | 22 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.002872294154993776 / 0.029752047201215177 | [NPY](tensors/0002601.npy) |
| 2602 | `model.layers.0.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 45.25 / -0.05527113808525933 / 2.859571529678839 | [NPY](tensors/0002602.npy) |
| 2603 | `model.layers.0.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.65625 / 1.9453125 / -0.011243886417812772 / 0.3573754239799881 | [NPY](tensors/0002603.npy) |
| 2604 | `model.layers.0.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.65625 / 1.9453125 / -0.011243886417812772 / 0.3573754239799881 | [NPY](tensors/0002604.npy) |
| 2605 | `model.layers.0.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.65625 / 1.9453125 / -0.011243886417812772 / 0.3573754239799881 | [NPY](tensors/0002605.npy) |
| 2606 | `model.layers.0.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2607 | `model.layers.0.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2608 | `model.layers.0.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2609 | `model.layers.0.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.75 / 17.125 / 0.018009005155828265 / 0.6145529109268639 | [NPY](tensors/0002609.npy) |
| 2610 | `model.layers.0.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.75 / 17.125 / 0.018009005155828265 / 0.6145529109268639 | [NPY](tensors/0002610.npy) |
| 2611 | `model.layers.0.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.96875 / 2.21875 / -0.2222599983215332 / 0.9201306767179724 | [NPY](tensors/0002611.npy) |
| 2612 | `model.layers.0` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 62.5 / -0.037192381752861874 / 3.1930988161070446 | [NPY](tensors/0002612.npy) |
| 2691 | `model.layers.0` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 46.0 / -0.023602605362733207 / 2.2747406072903233 | [NPY](tensors/0002691.npy) |
| 2692 | `model.layers.0` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002692.npy) |
| 2693 | `model.layers.0` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0002693.npy) |
| 2694 | `model.layers.0` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0002694.npy) |
| 2695 | `model.layers.0` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0002695.npy) |
| 2696 | `model.layers.0` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2697 | `model.layers.0` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2698 | `model.layers.0` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2699 | `model.layers.0.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 46.0 / -0.023602605362733207 / 2.2747406072903233 | [NPY](tensors/0002699.npy) |
| 2700 | `model.layers.0.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0625 / 12.5 / -0.011853186289469402 / 0.7477935227731929 | [NPY](tensors/0002700.npy) |
| 2701 | `model.layers.0.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0625 / 12.5 / -0.011853186289469402 / 0.7477935227731929 | [NPY](tensors/0002701.npy) |
| 2702 | `model.layers.0.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002702.npy) |
| 2703 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0002703.npy) |
| 2704 | `model.layers.0.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2705 | `model.layers.0.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2706 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0002706.npy) |
| 2707 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0002707.npy) |
| 2708 | `model.layers.0.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2709 | `model.layers.0.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0625 / 12.5 / -0.011853186289469402 / 0.7477935227731929 | [NPY](tensors/0002709.npy) |
| 2710 | `model.layers.0.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.4375 / 9.0 / 0.03394485544413328 / 1.1635386579173397 | [NPY](tensors/0002710.npy) |
| 2711 | `model.layers.0.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0625 / 12.5 / -0.011853186289469402 / 0.7477935227731929 | [NPY](tensors/0002711.npy) |
| 2712 | `model.layers.0.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.5 / 53.25 / -0.09332975745201111 / 5.4531951114019135 | [NPY](tensors/0002712.npy) |
| 2713 | `model.layers.0.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0625 / 12.5 / -0.011853186289469402 / 0.7477935227731929 | [NPY](tensors/0002713.npy) |
| 2714 | `model.layers.0.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.15625 / 7.375 / 0.09305919706821442 / 1.4655234850178176 | [NPY](tensors/0002714.npy) |
| 2715 | `model.layers.0.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.03125 / 4.3125 / -0.01958687254227698 / 0.7723049343758716 | [NPY](tensors/0002715.npy) |
| 2716 | `model.layers.0.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.9375 / 28.625 / 0.02280191249317593 / 0.9881340152731447 | [NPY](tensors/0002716.npy) |
| 2717 | `model.layers.0.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.9375 / 28.625 / 0.02280191249317593 / 0.9881340152731447 | [NPY](tensors/0002717.npy) |
| 2718 | `model.layers.0.self_attn` | 23 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003327194342096041 / 0.0437603205734028 | [NPY](tensors/0002718.npy) |
| 2719 | `model.layers.0.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 47.25 / -0.0007606347401936849 / 2.625260623192182 | [NPY](tensors/0002719.npy) |
| 2720 | `model.layers.0.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.046875 / 2.0625 / -0.0027860694461398655 / 0.3919548511085001 | [NPY](tensors/0002720.npy) |
| 2721 | `model.layers.0.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.046875 / 2.0625 / -0.0027860694461398655 / 0.3919548511085001 | [NPY](tensors/0002721.npy) |
| 2722 | `model.layers.0.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.046875 / 2.0625 / -0.0027860694461398655 / 0.3919548511085001 | [NPY](tensors/0002722.npy) |
| 2723 | `model.layers.0.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2724 | `model.layers.0.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2725 | `model.layers.0.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2726 | `model.layers.0.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -17.875 / 32.75 / 0.03540602922439575 / 1.5657394148619361 | [NPY](tensors/0002726.npy) |
| 2727 | `model.layers.0.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.875 / 32.75 / 0.03540602922439575 / 1.5657394148619361 | [NPY](tensors/0002727.npy) |
| 2728 | `model.layers.0.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3671875 / 2.421875 / -0.13489818572998047 / 0.8100094470837379 | [NPY](tensors/0002728.npy) |
| 2729 | `model.layers.0` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 69.0 / 0.034545644124348955 / 3.212941503703269 | [NPY](tensors/0002729.npy) |
| 2808 | `model.layers.0` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0002808.npy) |
| 2809 | `model.layers.0` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002809.npy) |
| 2810 | `model.layers.0` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0002810.npy) |
| 2811 | `model.layers.0` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0002811.npy) |
| 2812 | `model.layers.0` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0002812.npy) |
| 2813 | `model.layers.0` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2814 | `model.layers.0` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2815 | `model.layers.0` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2816 | `model.layers.0.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0002816.npy) |
| 2817 | `model.layers.0.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002817.npy) |
| 2818 | `model.layers.0.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002818.npy) |
| 2819 | `model.layers.0.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002819.npy) |
| 2820 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0002820.npy) |
| 2821 | `model.layers.0.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2822 | `model.layers.0.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2823 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0002823.npy) |
| 2824 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0002824.npy) |
| 2825 | `model.layers.0.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2826 | `model.layers.0.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002826.npy) |
| 2827 | `model.layers.0.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 9.25 / 0.06582052947487682 / 1.0317253511582722 | [NPY](tensors/0002827.npy) |
| 2828 | `model.layers.0.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002828.npy) |
| 2829 | `model.layers.0.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.5 / 59.75 / -0.027341485023498535 / 6.496414800406944 | [NPY](tensors/0002829.npy) |
| 2830 | `model.layers.0.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002830.npy) |
| 2831 | `model.layers.0.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.453125 / 4.6875 / 0.06333106756210327 / 0.9556167387162166 | [NPY](tensors/0002831.npy) |
| 2832 | `model.layers.0.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.1875 / 6.46875 / 0.007576732819870813 / 0.47420089052437797 | [NPY](tensors/0002832.npy) |
| 2833 | `model.layers.0.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.96875 / 32.5 / 0.021089373503087296 / 0.9628158857732934 | [NPY](tensors/0002833.npy) |
| 2834 | `model.layers.0.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.96875 / 32.5 / 0.021089373503087296 / 0.9628158857732934 | [NPY](tensors/0002834.npy) |
| 2835 | `model.layers.0.self_attn` | 24 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002638461618028054 / 0.027126861439437308 | [NPY](tensors/0002835.npy) |
| 2836 | `model.layers.0.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 32.75 / 0.07021809154086643 / 2.594809046404451 | [NPY](tensors/0002836.npy) |
| 2837 | `model.layers.0.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.5 / 1.8828125 / 0.005536417166392009 / 0.326911091212887 | [NPY](tensors/0002837.npy) |
| 2838 | `model.layers.0.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.5 / 1.8828125 / 0.005536417166392009 / 0.326911091212887 | [NPY](tensors/0002838.npy) |
| 2839 | `model.layers.0.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.5 / 1.8828125 / 0.005536417166392009 / 0.326911091212887 | [NPY](tensors/0002839.npy) |
| 2840 | `model.layers.0.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2841 | `model.layers.0.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2842 | `model.layers.0.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2843 | `model.layers.0.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.5625 / 5.75 / -0.00046558893389172026 / 0.4468955644733807 | [NPY](tensors/0002843.npy) |
| 2844 | `model.layers.0.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.5625 / 5.75 / -0.00046558893389172026 / 0.4468955644733807 | [NPY](tensors/0002844.npy) |
| 2845 | `model.layers.0.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.875 / 2.90625 / -0.13647747039794922 / 1.2494489512315619 | [NPY](tensors/0002845.npy) |
| 2846 | `model.layers.0` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 38.25 / 0.06980786853366427 / 2.5754908770116742 | [NPY](tensors/0002846.npy) |
| 2925 | `model.layers.0` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.75 / 36.5 / -0.03277786038815975 / 2.7829041357151567 | [NPY](tensors/0002925.npy) |
| 2926 | `model.layers.0` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002926.npy) |
| 2927 | `model.layers.0` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0002927.npy) |
| 2928 | `model.layers.0` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0002928.npy) |
| 2929 | `model.layers.0` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0002929.npy) |
| 2930 | `model.layers.0` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2931 | `model.layers.0` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2932 | `model.layers.0` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2933 | `model.layers.0.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.75 / 36.5 / -0.03277786038815975 / 2.7829041357151567 | [NPY](tensors/0002933.npy) |
| 2934 | `model.layers.0.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002934.npy) |
| 2935 | `model.layers.0.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002935.npy) |
| 2936 | `model.layers.0.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002936.npy) |
| 2937 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0002937.npy) |
| 2938 | `model.layers.0.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2939 | `model.layers.0.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2940 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0002940.npy) |
| 2941 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0002941.npy) |
| 2942 | `model.layers.0.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2943 | `model.layers.0.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002943.npy) |
| 2944 | `model.layers.0.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0625 / 8.75 / 0.007699438836425543 / 0.9554901933770389 | [NPY](tensors/0002944.npy) |
| 2945 | `model.layers.0.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002945.npy) |
| 2946 | `model.layers.0.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.5 / 55.25 / -0.05697989463806152 / 6.049655579159513 | [NPY](tensors/0002946.npy) |
| 2947 | `model.layers.0.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002947.npy) |
| 2948 | `model.layers.0.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -2.703125 / 3.4375 / 0.04050885885953903 / 0.8799544405823716 | [NPY](tensors/0002948.npy) |
| 2949 | `model.layers.0.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.765625 / 4.125 / 0.00625862977176439 / 0.47473586096856357 | [NPY](tensors/0002949.npy) |
| 2950 | `model.layers.0.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.1875 / 31.0 / 0.03008667255441348 / 0.9397459786860317 | [NPY](tensors/0002950.npy) |
| 2951 | `model.layers.0.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.1875 / 31.0 / 0.03008667255441348 / 0.9397459786860317 | [NPY](tensors/0002951.npy) |
| 2952 | `model.layers.0.self_attn` | 25 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.0031260618922599515 / 0.03128046969948227 | [NPY](tensors/0002952.npy) |
| 2953 | `model.layers.0.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -60.0 / 37.0 / -0.002819347381591797 / 2.8866382158419555 | [NPY](tensors/0002953.npy) |
| 2954 | `model.layers.0.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.109375 / 2.75 / 0.00581291119257609 / 0.28360926351600757 | [NPY](tensors/0002954.npy) |
| 2955 | `model.layers.0.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.109375 / 2.75 / 0.00581291119257609 / 0.28360926351600757 | [NPY](tensors/0002955.npy) |
| 2956 | `model.layers.0.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.109375 / 2.75 / 0.00581291119257609 / 0.28360926351600757 | [NPY](tensors/0002956.npy) |
| 2957 | `model.layers.0.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2958 | `model.layers.0.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2959 | `model.layers.0.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2960 | `model.layers.0.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.875 / 14.4375 / 0.01662431839439604 / 0.6731601529820589 | [NPY](tensors/0002960.npy) |
| 2961 | `model.layers.0.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.875 / 14.4375 / 0.01662431839439604 / 0.6731601529820589 | [NPY](tensors/0002961.npy) |
| 2962 | `model.layers.0.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.15625 / 1.6171875 / -0.06203460693359375 / 0.9873746935032537 | [NPY](tensors/0002962.npy) |
| 2963 | `model.layers.0` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 42.0 / 0.013762948248121474 / 2.8218447542765897 | [NPY](tensors/0002963.npy) |
| 3042 | `model.layers.0` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 25.375 / 0.03148116301745176 / 2.4913610061559237 | [NPY](tensors/0003042.npy) |
| 3043 | `model.layers.0` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003043.npy) |
| 3044 | `model.layers.0` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0003044.npy) |
| 3045 | `model.layers.0` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0003045.npy) |
| 3046 | `model.layers.0` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0003046.npy) |
| 3047 | `model.layers.0` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3048 | `model.layers.0` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3049 | `model.layers.0` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3050 | `model.layers.0.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 25.375 / 0.03148116301745176 / 2.4913610061559237 | [NPY](tensors/0003050.npy) |
| 3051 | `model.layers.0.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003051.npy) |
| 3052 | `model.layers.0.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003052.npy) |
| 3053 | `model.layers.0.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003053.npy) |
| 3054 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0003054.npy) |
| 3055 | `model.layers.0.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3056 | `model.layers.0.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3057 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0003057.npy) |
| 3058 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0003058.npy) |
| 3059 | `model.layers.0.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3060 | `model.layers.0.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003060.npy) |
| 3061 | `model.layers.0.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.8125 / 9.875 / 0.001175960642285645 / 1.0708778134614567 | [NPY](tensors/0003061.npy) |
| 3062 | `model.layers.0.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003062.npy) |
| 3063 | `model.layers.0.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.0 / 46.0 / -0.07610408216714859 / 5.694328378141193 | [NPY](tensors/0003063.npy) |
| 3064 | `model.layers.0.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003064.npy) |
| 3065 | `model.layers.0.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.46875 / 6.09375 / -0.02648264169692993 / 1.4472391438112524 | [NPY](tensors/0003065.npy) |
| 3066 | `model.layers.0.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.21875 / 2.71875 / 0.0023504288528783945 / 0.4600915757845929 | [NPY](tensors/0003066.npy) |
| 3067 | `model.layers.0.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.5 / 43.75 / 0.020977453551151687 / 1.3584527305372542 | [NPY](tensors/0003067.npy) |
| 3068 | `model.layers.0.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.5 / 43.75 / 0.020977453551151687 / 1.3584527305372542 | [NPY](tensors/0003068.npy) |
| 3069 | `model.layers.0.self_attn` | 26 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0030351657736734008 / 0.034036731057057866 | [NPY](tensors/0003069.npy) |
| 3070 | `model.layers.0.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 44.75 / 0.05238340695699056 / 2.949531139350582 | [NPY](tensors/0003070.npy) |
| 3071 | `model.layers.0.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.1875 / 1.4609375 / 0.008814635541703966 / 0.3633308241769975 | [NPY](tensors/0003071.npy) |
| 3072 | `model.layers.0.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.1875 / 1.4609375 / 0.008814635541703966 / 0.3633308241769975 | [NPY](tensors/0003072.npy) |
| 3073 | `model.layers.0.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -5.1875 / 1.4609375 / 0.008814635541703966 / 0.3633308241769975 | [NPY](tensors/0003073.npy) |
| 3074 | `model.layers.0.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3075 | `model.layers.0.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3076 | `model.layers.0.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3077 | `model.layers.0.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.46875 / 12.625 / 0.01929215850929419 / 0.4707136690561782 | [NPY](tensors/0003077.npy) |
| 3078 | `model.layers.0.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.46875 / 12.625 / 0.01929215850929419 / 0.4707136690561782 | [NPY](tensors/0003078.npy) |
| 3079 | `model.layers.0.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.140625 / 2.125 / -0.20476531982421875 / 0.8254277375647031 | [NPY](tensors/0003079.npy) |
| 3080 | `model.layers.0` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.0 / 56.5 / 0.07178003787994384 / 3.214026272668905 | [NPY](tensors/0003080.npy) |
| 3159 | `model.layers.0` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.25 / 22.875 / 0.02578953950562411 / 2.1256093624936447 | [NPY](tensors/0003159.npy) |
| 3160 | `model.layers.0` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003160.npy) |
| 3161 | `model.layers.0` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0003161.npy) |
| 3162 | `model.layers.0` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0003162.npy) |
| 3163 | `model.layers.0` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0003163.npy) |
| 3164 | `model.layers.0` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3165 | `model.layers.0` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3166 | `model.layers.0` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3167 | `model.layers.0.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.25 / 22.875 / 0.02578953950562411 / 2.1256093624936447 | [NPY](tensors/0003167.npy) |
| 3168 | `model.layers.0.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003168.npy) |
| 3169 | `model.layers.0.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003169.npy) |
| 3170 | `model.layers.0.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003170.npy) |
| 3171 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0003171.npy) |
| 3172 | `model.layers.0.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3173 | `model.layers.0.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3174 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0003174.npy) |
| 3175 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0003175.npy) |
| 3176 | `model.layers.0.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3177 | `model.layers.0.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003177.npy) |
| 3178 | `model.layers.0.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.8125 / 7.9375 / -0.014699231367558241 / 1.1007098219776468 | [NPY](tensors/0003178.npy) |
| 3179 | `model.layers.0.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003179.npy) |
| 3180 | `model.layers.0.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.25 / 55.25 / 0.1305762529373169 / 5.5847358405435745 | [NPY](tensors/0003180.npy) |
| 3181 | `model.layers.0.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003181.npy) |
| 3182 | `model.layers.0.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.21875 / 5.84375 / -0.07473260164260864 / 1.5255124313159032 | [NPY](tensors/0003182.npy) |
| 3183 | `model.layers.0.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.4375 / 6.09375 / -0.004787968588061631 / 0.8134905274319892 | [NPY](tensors/0003183.npy) |
| 3184 | `model.layers.0.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.5 / 47.0 / 0.0421022983888785 / 1.50934837876779 | [NPY](tensors/0003184.npy) |
| 3185 | `model.layers.0.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.5 / 47.0 / 0.0421022983888785 / 1.50934837876779 | [NPY](tensors/0003185.npy) |
| 3186 | `model.layers.0.self_attn` | 27 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003857310282690223 / 0.04620558567697511 | [NPY](tensors/0003186.npy) |
| 3187 | `model.layers.0.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 49.75 / 0.06793098979526097 / 2.726553245614828 | [NPY](tensors/0003187.npy) |
| 3188 | `model.layers.0.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6171875 / 1.7421875 / 0.011833266748322382 / 0.46085402062664665 | [NPY](tensors/0003188.npy) |
| 3189 | `model.layers.0.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6171875 / 1.7421875 / 0.011833266748322382 / 0.46085402062664665 | [NPY](tensors/0003189.npy) |
| 3190 | `model.layers.0.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.6171875 / 1.7421875 / 0.011833266748322382 / 0.46085402062664665 | [NPY](tensors/0003190.npy) |
| 3191 | `model.layers.0.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3192 | `model.layers.0.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3193 | `model.layers.0.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3194 | `model.layers.0.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -18.375 / 40.5 / 0.010029850817388958 / 1.4172664967521662 | [NPY](tensors/0003194.npy) |
| 3195 | `model.layers.0.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.375 / 40.5 / 0.010029850817388958 / 1.4172664967521662 | [NPY](tensors/0003195.npy) |
| 3196 | `model.layers.0.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.921875 / 2.5 / -0.05030059814453125 / 0.8044259597317704 | [NPY](tensors/0003196.npy) |
| 3197 | `model.layers.0` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.5 / 90.0 / 0.07803965674506294 / 3.5712354820125776 | [NPY](tensors/0003197.npy) |
| 3276 | `model.layers.0` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 89.0 / 0.026544343266222212 / 4.541275344485995 | [NPY](tensors/0003276.npy) |
| 3277 | `model.layers.0` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003277.npy) |
| 3278 | `model.layers.0` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0003278.npy) |
| 3279 | `model.layers.0` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0003279.npy) |
| 3280 | `model.layers.0` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0003280.npy) |
| 3281 | `model.layers.0` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3282 | `model.layers.0` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3283 | `model.layers.0` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3284 | `model.layers.0.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 89.0 / 0.026544343266222212 / 4.541275344485995 | [NPY](tensors/0003284.npy) |
| 3285 | `model.layers.0.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003285.npy) |
| 3286 | `model.layers.0.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003286.npy) |
| 3287 | `model.layers.0.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003287.npy) |
| 3288 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0003288.npy) |
| 3289 | `model.layers.0.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3290 | `model.layers.0.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3291 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0003291.npy) |
| 3292 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0003292.npy) |
| 3293 | `model.layers.0.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3294 | `model.layers.0.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003294.npy) |
| 3295 | `model.layers.0.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.875 / 7.84375 / 0.015290047216694802 / 0.914624676971129 | [NPY](tensors/0003295.npy) |
| 3296 | `model.layers.0.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003296.npy) |
| 3297 | `model.layers.0.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.25 / 34.5 / -0.11417865753173828 / 4.434976879466014 | [NPY](tensors/0003297.npy) |
| 3298 | `model.layers.0.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003298.npy) |
| 3299 | `model.layers.0.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.03125 / 4.8125 / -0.07233588397502899 / 1.0561324517062678 | [NPY](tensors/0003299.npy) |
| 3300 | `model.layers.0.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.09375 / 5.71875 / -0.0383169911801815 / 0.778951392221896 | [NPY](tensors/0003300.npy) |
| 3301 | `model.layers.0.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.5 / 27.125 / 0.025102673289883467 / 1.1508888746475636 | [NPY](tensors/0003301.npy) |
| 3302 | `model.layers.0.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.5 / 27.125 / 0.025102673289883467 / 1.1508888746475636 | [NPY](tensors/0003302.npy) |
| 3303 | `model.layers.0.self_attn` | 28 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003954787866094785 / 0.04208081867834901 | [NPY](tensors/0003303.npy) |
| 3304 | `model.layers.0.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -59.75 / 67.5 / 0.051644410027398 / 4.046679709450981 | [NPY](tensors/0003304.npy) |
| 3305 | `model.layers.0.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.03125 / 2.1875 / 0.00916527509689331 / 0.2833744877857845 | [NPY](tensors/0003305.npy) |
| 3306 | `model.layers.0.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.03125 / 2.1875 / 0.00916527509689331 / 0.2833744877857845 | [NPY](tensors/0003306.npy) |
| 3307 | `model.layers.0.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.03125 / 2.1875 / 0.00916527509689331 / 0.2833744877857845 | [NPY](tensors/0003307.npy) |
| 3308 | `model.layers.0.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3309 | `model.layers.0.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3310 | `model.layers.0.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3311 | `model.layers.0.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -29.0 / 28.5 / 0.025470738278494942 / 1.3394031185940258 | [NPY](tensors/0003311.npy) |
| 3312 | `model.layers.0.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 28.5 / 0.025470738278494942 / 1.3394031185940258 | [NPY](tensors/0003312.npy) |
| 3313 | `model.layers.0.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.515625 / 2.9375 / -0.17319881916046143 / 0.8343968370693335 | [NPY](tensors/0003313.npy) |
| 3314 | `model.layers.0` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 59.0 / 0.07720714145236546 / 3.59707156837847 | [NPY](tensors/0003314.npy) |
| 3393 | `model.layers.0` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0003393.npy) |
| 3394 | `model.layers.0` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003394.npy) |
| 3395 | `model.layers.0` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0003395.npy) |
| 3396 | `model.layers.0` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0003396.npy) |
| 3397 | `model.layers.0` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0003397.npy) |
| 3398 | `model.layers.0` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3399 | `model.layers.0` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3400 | `model.layers.0` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3401 | `model.layers.0.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0003401.npy) |
| 3402 | `model.layers.0.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003402.npy) |
| 3403 | `model.layers.0.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003403.npy) |
| 3404 | `model.layers.0.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003404.npy) |
| 3405 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0003405.npy) |
| 3406 | `model.layers.0.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3407 | `model.layers.0.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3408 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0003408.npy) |
| 3409 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0003409.npy) |
| 3410 | `model.layers.0.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3411 | `model.layers.0.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003411.npy) |
| 3412 | `model.layers.0.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 7.625 / 0.011268170550465584 / 0.9167789321734896 | [NPY](tensors/0003412.npy) |
| 3413 | `model.layers.0.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003413.npy) |
| 3414 | `model.layers.0.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 43.75 / 0.046514674089848995 / 4.791095594233786 | [NPY](tensors/0003414.npy) |
| 3415 | `model.layers.0.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003415.npy) |
| 3416 | `model.layers.0.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.84375 / 4.125 / -0.01808762550354004 / 1.3178383551916408 | [NPY](tensors/0003416.npy) |
| 3417 | `model.layers.0.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.3125 / 4.1875 / -0.01621350791901932 / 0.502916679747166 | [NPY](tensors/0003417.npy) |
| 3418 | `model.layers.0.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.875 / 39.25 / 0.030955380698045095 / 1.1393671974771935 | [NPY](tensors/0003418.npy) |
| 3419 | `model.layers.0.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.875 / 39.25 / 0.030955380698045095 / 1.1393671974771935 | [NPY](tensors/0003419.npy) |
| 3420 | `model.layers.0.self_attn` | 29 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.0031895363511669165 / 0.0283969966795764 | [NPY](tensors/0003420.npy) |
| 3421 | `model.layers.0.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.75 / 40.25 / 0.020323032803005642 / 2.847926322918223 | [NPY](tensors/0003421.npy) |
| 3422 | `model.layers.0.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.125 / 1.9296875 / 0.009047591023974948 / 0.37644425253961494 | [NPY](tensors/0003422.npy) |
| 3423 | `model.layers.0.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.125 / 1.9296875 / 0.009047591023974948 / 0.37644425253961494 | [NPY](tensors/0003423.npy) |
| 3424 | `model.layers.0.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.125 / 1.9296875 / 0.009047591023974948 / 0.37644425253961494 | [NPY](tensors/0003424.npy) |
| 3425 | `model.layers.0.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3426 | `model.layers.0.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3427 | `model.layers.0.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3428 | `model.layers.0.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.40625 / 14.8125 / 0.023185939714312553 / 0.5439925316146557 | [NPY](tensors/0003428.npy) |
| 3429 | `model.layers.0.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.40625 / 14.8125 / 0.023185939714312553 / 0.5439925316146557 | [NPY](tensors/0003429.npy) |
| 3430 | `model.layers.0.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.046875 / 1.8671875 / -0.06475353240966797 / 0.6375473705813504 | [NPY](tensors/0003430.npy) |
| 3431 | `model.layers.0` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.5 / 55.0 / 0.04354850980970595 / 3.09325291379408 | [NPY](tensors/0003431.npy) |
| 3510 | `model.layers.0` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 30.875 / -0.03053326966861884 / 2.629557572976096 | [NPY](tensors/0003510.npy) |
| 3511 | `model.layers.0` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003511.npy) |
| 3512 | `model.layers.0` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0003512.npy) |
| 3513 | `model.layers.0` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0003513.npy) |
| 3514 | `model.layers.0` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0003514.npy) |
| 3515 | `model.layers.0` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3516 | `model.layers.0` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3517 | `model.layers.0` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3518 | `model.layers.0.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 30.875 / -0.03053326966861884 / 2.629557572976096 | [NPY](tensors/0003518.npy) |
| 3519 | `model.layers.0.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003519.npy) |
| 3520 | `model.layers.0.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003520.npy) |
| 3521 | `model.layers.0.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003521.npy) |
| 3522 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0003522.npy) |
| 3523 | `model.layers.0.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3524 | `model.layers.0.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3525 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0003525.npy) |
| 3526 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0003526.npy) |
| 3527 | `model.layers.0.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3528 | `model.layers.0.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003528.npy) |
| 3529 | `model.layers.0.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 9.375 / -0.0057218477595597506 / 1.0817809599468158 | [NPY](tensors/0003529.npy) |
| 3530 | `model.layers.0.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003530.npy) |
| 3531 | `model.layers.0.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.75 / 60.25 / 0.21187177300453186 / 5.623456193541793 | [NPY](tensors/0003531.npy) |
| 3532 | `model.layers.0.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003532.npy) |
| 3533 | `model.layers.0.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.15625 / 3.484375 / -0.04266364127397537 / 1.132992277020041 | [NPY](tensors/0003533.npy) |
| 3534 | `model.layers.0.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.78125 / 4.09375 / -0.008665622415719554 / 0.827463778399266 | [NPY](tensors/0003534.npy) |
| 3535 | `model.layers.0.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.25 / 49.5 / 0.03837819745143255 / 1.4802670263454973 | [NPY](tensors/0003535.npy) |
| 3536 | `model.layers.0.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.25 / 49.5 / 0.03837819745143255 / 1.4802670263454973 | [NPY](tensors/0003536.npy) |
| 3537 | `model.layers.0.self_attn` | 30 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004780853317100861 / 0.05157486164850181 | [NPY](tensors/0003537.npy) |
| 3538 | `model.layers.0.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 53.5 / 0.007841205596923828 / 3.0829861027633227 | [NPY](tensors/0003538.npy) |
| 3539 | `model.layers.0.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.765625 / 1.6640625 / 0.006508113774988386 / 0.39394240562498767 | [NPY](tensors/0003539.npy) |
| 3540 | `model.layers.0.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.765625 / 1.6640625 / 0.006508113774988386 / 0.39394240562498767 | [NPY](tensors/0003540.npy) |
| 3541 | `model.layers.0.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.765625 / 1.6640625 / 0.006508113774988386 / 0.39394240562498767 | [NPY](tensors/0003541.npy) |
| 3542 | `model.layers.0.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3543 | `model.layers.0.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3544 | `model.layers.0.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3545 | `model.layers.0.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.8125 / 34.75 / 0.04690028808804022 / 1.1119873853633389 | [NPY](tensors/0003545.npy) |
| 3546 | `model.layers.0.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 34.75 / 0.04690028808804022 / 1.1119873853633389 | [NPY](tensors/0003546.npy) |
| 3547 | `model.layers.0.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.4609375 / 1.640625 / -0.13898849487304688 / 0.6298400441956068 | [NPY](tensors/0003547.npy) |
| 3548 | `model.layers.0` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 88.0 / 0.05465574264526367 / 3.6663669960759946 | [NPY](tensors/0003548.npy) |
| 3627 | `model.layers.0` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 29.875 / -0.024451741410626306 / 2.4041472308375256 | [NPY](tensors/0003627.npy) |
| 3628 | `model.layers.0` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003628.npy) |
| 3629 | `model.layers.0` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0003629.npy) |
| 3630 | `model.layers.0` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0003630.npy) |
| 3631 | `model.layers.0` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0003631.npy) |
| 3632 | `model.layers.0` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3633 | `model.layers.0` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3634 | `model.layers.0` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3635 | `model.layers.0.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 29.875 / -0.024451741410626306 / 2.4041472308375256 | [NPY](tensors/0003635.npy) |
| 3636 | `model.layers.0.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003636.npy) |
| 3637 | `model.layers.0.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003637.npy) |
| 3638 | `model.layers.0.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003638.npy) |
| 3639 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0003639.npy) |
| 3640 | `model.layers.0.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3641 | `model.layers.0.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3642 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0003642.npy) |
| 3643 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0003643.npy) |
| 3644 | `model.layers.0.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3645 | `model.layers.0.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003645.npy) |
| 3646 | `model.layers.0.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.96875 / 9.3125 / 0.013412588275969028 / 1.162217466520388 | [NPY](tensors/0003646.npy) |
| 3647 | `model.layers.0.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003647.npy) |
| 3648 | `model.layers.0.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.5 / 52.75 / 0.024785220623016357 / 5.9833002218429145 | [NPY](tensors/0003648.npy) |
| 3649 | `model.layers.0.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003649.npy) |
| 3650 | `model.layers.0.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.8125 / 6.03125 / -0.03467495460063219 / 1.460652286605354 | [NPY](tensors/0003650.npy) |
| 3651 | `model.layers.0.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.0 / 2.84375 / -0.035983755409688456 / 0.5732192106673399 | [NPY](tensors/0003651.npy) |
| 3652 | `model.layers.0.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.875 / 44.25 / 0.019794619000620312 / 1.3121912363361057 | [NPY](tensors/0003652.npy) |
| 3653 | `model.layers.0.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.875 / 44.25 / 0.019794619000620312 / 1.3121912363361057 | [NPY](tensors/0003653.npy) |
| 3654 | `model.layers.0.self_attn` | 31 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0031338686653939393 / 0.03784902872189619 | [NPY](tensors/0003654.npy) |
| 3655 | `model.layers.0.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 43.25 / -0.004698475201924642 / 2.796386068597073 | [NPY](tensors/0003655.npy) |
| 3656 | `model.layers.0.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9765625 / 1.9140625 / 0.007373248206244575 / 0.3788116000736693 | [NPY](tensors/0003656.npy) |
| 3657 | `model.layers.0.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9765625 / 1.9140625 / 0.007373248206244575 / 0.3788116000736693 | [NPY](tensors/0003657.npy) |
| 3658 | `model.layers.0.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.9765625 / 1.9140625 / 0.007373248206244575 / 0.3788116000736693 | [NPY](tensors/0003658.npy) |
| 3659 | `model.layers.0.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3660 | `model.layers.0.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3661 | `model.layers.0.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3662 | `model.layers.0.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -10.625 / 31.0 / 0.03484701481130388 / 1.0229188498374464 | [NPY](tensors/0003662.npy) |
| 3663 | `model.layers.0.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.625 / 31.0 / 0.03484701481130388 / 1.0229188498374464 | [NPY](tensors/0003663.npy) |
| 3664 | `model.layers.0.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9375 / 2.046875 / -0.15447044372558594 / 0.8012883309532577 | [NPY](tensors/0003664.npy) |
| 3665 | `model.layers.0` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 73.5 / 0.030125541157192653 / 3.321465283733663 | [NPY](tensors/0003665.npy) |
| 3744 | `model.layers.0` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 35.0 / -0.0015044911040200128 / 2.4601390841825688 | [NPY](tensors/0003744.npy) |
| 3745 | `model.layers.0` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003745.npy) |
| 3746 | `model.layers.0` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0003746.npy) |
| 3747 | `model.layers.0` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0003747.npy) |
| 3748 | `model.layers.0` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0003748.npy) |
| 3749 | `model.layers.0` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3750 | `model.layers.0` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3751 | `model.layers.0` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3752 | `model.layers.0.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 35.0 / -0.0015044911040200128 / 2.4601390841825688 | [NPY](tensors/0003752.npy) |
| 3753 | `model.layers.0.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003753.npy) |
| 3754 | `model.layers.0.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003754.npy) |
| 3755 | `model.layers.0.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003755.npy) |
| 3756 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0003756.npy) |
| 3757 | `model.layers.0.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3758 | `model.layers.0.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3759 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0003759.npy) |
| 3760 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0003760.npy) |
| 3761 | `model.layers.0.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3762 | `model.layers.0.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003762.npy) |
| 3763 | `model.layers.0.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 6.875 / 0.0073078901041299105 / 1.018639785574501 | [NPY](tensors/0003763.npy) |
| 3764 | `model.layers.0.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003764.npy) |
| 3765 | `model.layers.0.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.0 / 49.0 / 0.1723565487191081 / 4.808040616212344 | [NPY](tensors/0003765.npy) |
| 3766 | `model.layers.0.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003766.npy) |
| 3767 | `model.layers.0.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.8125 / 3.265625 / 0.014979145489633083 / 1.106498243297265 | [NPY](tensors/0003767.npy) |
| 3768 | `model.layers.0.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.65625 / 5.8125 / -0.010126832414243836 / 0.7574700148960191 | [NPY](tensors/0003768.npy) |
| 3769 | `model.layers.0.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.0 / 46.25 / 0.02664423431787226 / 1.397482044278513 | [NPY](tensors/0003769.npy) |
| 3770 | `model.layers.0.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.0 / 46.25 / 0.02664423431787226 / 1.397482044278513 | [NPY](tensors/0003770.npy) |
| 3771 | `model.layers.0.self_attn` | 32 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.004127723192186447 / 0.043123619763117356 | [NPY](tensors/0003771.npy) |
| 3772 | `model.layers.0.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.375 / 44.25 / 0.025170968638526067 / 2.8608743233393663 | [NPY](tensors/0003772.npy) |
| 3773 | `model.layers.0.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.078125 / 2.21875 / -0.0017564853032430014 / 0.4217020683464454 | [NPY](tensors/0003773.npy) |
| 3774 | `model.layers.0.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.078125 / 2.21875 / -0.0017564853032430014 / 0.4217020683464454 | [NPY](tensors/0003774.npy) |
| 3775 | `model.layers.0.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.078125 / 2.21875 / -0.0017564853032430014 / 0.4217020683464454 | [NPY](tensors/0003775.npy) |
| 3776 | `model.layers.0.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3777 | `model.layers.0.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3778 | `model.layers.0.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3779 | `model.layers.0.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.75 / 24.5 / 0.021549010028441746 / 1.0576353970038859 | [NPY](tensors/0003779.npy) |
| 3780 | `model.layers.0.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.75 / 24.5 / 0.021549010028441746 / 1.0576353970038859 | [NPY](tensors/0003780.npy) |
| 3781 | `model.layers.0.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.0625 / 1.921875 / -0.013685226440429688 / 1.2467832384000752 | [NPY](tensors/0003781.npy) |
| 3782 | `model.layers.0` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.5 / 67.5 / 0.04654403262668186 / 3.269132963401237 | [NPY](tensors/0003782.npy) |
| 3861 | `model.layers.0` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 22.625 / -0.02912892893784576 / 2.1983857303463927 | [NPY](tensors/0003861.npy) |
| 3862 | `model.layers.0` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003862.npy) |
| 3863 | `model.layers.0` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0003863.npy) |
| 3864 | `model.layers.0` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0003864.npy) |
| 3865 | `model.layers.0` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0003865.npy) |
| 3866 | `model.layers.0` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3867 | `model.layers.0` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3868 | `model.layers.0` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3869 | `model.layers.0.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 22.625 / -0.02912892893784576 / 2.1983857303463927 | [NPY](tensors/0003869.npy) |
| 3870 | `model.layers.0.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003870.npy) |
| 3871 | `model.layers.0.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003871.npy) |
| 3872 | `model.layers.0.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003872.npy) |
| 3873 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0003873.npy) |
| 3874 | `model.layers.0.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3875 | `model.layers.0.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3876 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0003876.npy) |
| 3877 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0003877.npy) |
| 3878 | `model.layers.0.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3879 | `model.layers.0.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003879.npy) |
| 3880 | `model.layers.0.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.78125 / 0.008440272184088826 / 1.120452857679885 | [NPY](tensors/0003880.npy) |
| 3881 | `model.layers.0.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003881.npy) |
| 3882 | `model.layers.0.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.5 / 51.5 / 0.1618337631225586 / 5.774741101565946 | [NPY](tensors/0003882.npy) |
| 3883 | `model.layers.0.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003883.npy) |
| 3884 | `model.layers.0.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.9375 / 4.875 / -0.08827418088912964 / 1.3724833169271258 | [NPY](tensors/0003884.npy) |
| 3885 | `model.layers.0.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.34375 / 5.3125 / -0.015093297544808593 / 0.6647990170283071 | [NPY](tensors/0003885.npy) |
| 3886 | `model.layers.0.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 48.25 / 0.02392752021551132 / 1.5245228102199586 | [NPY](tensors/0003886.npy) |
| 3887 | `model.layers.0.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 48.25 / 0.02392752021551132 / 1.5245228102199586 | [NPY](tensors/0003887.npy) |
| 3888 | `model.layers.0.self_attn` | 33 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003806568798653407 / 0.041814878029135395 | [NPY](tensors/0003888.npy) |
| 3889 | `model.layers.0.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.75 / 54.75 / -0.005198580357763502 / 2.866571737640592 | [NPY](tensors/0003889.npy) |
| 3890 | `model.layers.0.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6328125 / 1.828125 / 0.004071451558007135 / 0.3647958004303597 | [NPY](tensors/0003890.npy) |
| 3891 | `model.layers.0.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6328125 / 1.828125 / 0.004071451558007135 / 0.3647958004303597 | [NPY](tensors/0003891.npy) |
| 3892 | `model.layers.0.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.6328125 / 1.828125 / 0.004071451558007135 / 0.3647958004303597 | [NPY](tensors/0003892.npy) |
| 3893 | `model.layers.0.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3894 | `model.layers.0.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3895 | `model.layers.0.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3896 | `model.layers.0.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.625 / 28.75 / 0.030143014589945474 / 0.9928600407030995 | [NPY](tensors/0003896.npy) |
| 3897 | `model.layers.0.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.625 / 28.75 / 0.030143014589945474 / 0.9928600407030995 | [NPY](tensors/0003897.npy) |
| 3898 | `model.layers.0.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.1875 / 1.6875 / -0.07118606567382812 / 0.726012106760757 | [NPY](tensors/0003898.npy) |
| 3899 | `model.layers.0` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 79.0 / 0.024884849124484593 / 3.1957548459706606 | [NPY](tensors/0003899.npy) |
| 3978 | `model.layers.0` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0003978.npy) |
| 3979 | `model.layers.0` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003979.npy) |
| 3980 | `model.layers.0` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0003980.npy) |
| 3981 | `model.layers.0` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0003981.npy) |
| 3982 | `model.layers.0` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0003982.npy) |
| 3983 | `model.layers.0` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3984 | `model.layers.0` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3985 | `model.layers.0` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3986 | `model.layers.0.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0003986.npy) |
| 3987 | `model.layers.0.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003987.npy) |
| 3988 | `model.layers.0.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003988.npy) |
| 3989 | `model.layers.0.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003989.npy) |
| 3990 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0003990.npy) |
| 3991 | `model.layers.0.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3992 | `model.layers.0.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3993 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0003993.npy) |
| 3994 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0003994.npy) |
| 3995 | `model.layers.0.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3996 | `model.layers.0.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003996.npy) |
| 3997 | `model.layers.0.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 8.0 / 0.0014486645814031363 / 1.027321203413773 | [NPY](tensors/0003997.npy) |
| 3998 | `model.layers.0.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003998.npy) |
| 3999 | `model.layers.0.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.75 / 53.75 / 0.06940409168601036 / 5.734687316339554 | [NPY](tensors/0003999.npy) |
| 4000 | `model.layers.0.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004000.npy) |
| 4001 | `model.layers.0.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.8125 / 3.75 / -0.006423294544219971 / 0.9290448609736645 | [NPY](tensors/0004001.npy) |
| 4002 | `model.layers.0.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.09375 / 4.53125 / -0.0034896387842309196 / 0.6791059940713923 | [NPY](tensors/0004002.npy) |
| 4003 | `model.layers.0.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.5 / 37.75 / 0.025996973862250645 / 1.190431639722736 | [NPY](tensors/0004003.npy) |
| 4004 | `model.layers.0.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.5 / 37.75 / 0.025996973862250645 / 1.190431639722736 | [NPY](tensors/0004004.npy) |
| 4005 | `model.layers.0.self_attn` | 34 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004272641420678689 / 0.045460429141107275 | [NPY](tensors/0004005.npy) |
| 4006 | `model.layers.0.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -66.0 / 38.25 / -0.06524257924821641 / 2.991665769221125 | [NPY](tensors/0004006.npy) |
| 4007 | `model.layers.0.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8828125 / 1.4765625 / 0.0010029170248243545 / 0.3440029677081044 | [NPY](tensors/0004007.npy) |
| 4008 | `model.layers.0.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8828125 / 1.4765625 / 0.0010029170248243545 / 0.3440029677081044 | [NPY](tensors/0004008.npy) |
| 4009 | `model.layers.0.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.8828125 / 1.4765625 / 0.0010029170248243545 / 0.3440029677081044 | [NPY](tensors/0004009.npy) |
| 4010 | `model.layers.0.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4011 | `model.layers.0.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4012 | `model.layers.0.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4013 | `model.layers.0.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.0 / 13.1875 / 0.021223234716388914 / 0.5294428167948341 | [NPY](tensors/0004013.npy) |
| 4014 | `model.layers.0.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.0 / 13.1875 / 0.021223234716388914 / 0.5294428167948341 | [NPY](tensors/0004014.npy) |
| 4015 | `model.layers.0.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.4375 / 1.5 / 0.02725982666015625 / 1.3625024585108043 | [NPY](tensors/0004015.npy) |
| 4016 | `model.layers.0` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.75 / 42.75 / -0.043828550974527994 / 2.9640493253781024 | [NPY](tensors/0004016.npy) |
| 4095 | `model.layers.0` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 30.0 / -0.032196171374784574 / 2.820171892718441 | [NPY](tensors/0004095.npy) |
| 4096 | `model.layers.0` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004096.npy) |
| 4097 | `model.layers.0` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0004097.npy) |
| 4098 | `model.layers.0` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0004098.npy) |
| 4099 | `model.layers.0` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0004099.npy) |
| 4100 | `model.layers.0` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4101 | `model.layers.0` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4102 | `model.layers.0` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4103 | `model.layers.0.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 30.0 / -0.032196171374784574 / 2.820171892718441 | [NPY](tensors/0004103.npy) |
| 4104 | `model.layers.0.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004104.npy) |
| 4105 | `model.layers.0.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004105.npy) |
| 4106 | `model.layers.0.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004106.npy) |
| 4107 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0004107.npy) |
| 4108 | `model.layers.0.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4109 | `model.layers.0.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4110 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0004110.npy) |
| 4111 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0004111.npy) |
| 4112 | `model.layers.0.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4113 | `model.layers.0.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004113.npy) |
| 4114 | `model.layers.0.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.6875 / 10.0625 / 0.016296769957989454 / 1.0275877120532655 | [NPY](tensors/0004114.npy) |
| 4115 | `model.layers.0.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004115.npy) |
| 4116 | `model.layers.0.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -57.0 / 59.0 / -0.06925755739212036 / 5.9291873125568 | [NPY](tensors/0004116.npy) |
| 4117 | `model.layers.0.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004117.npy) |
| 4118 | `model.layers.0.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.0625 / 3.890625 / -0.020120687782764435 / 1.0179532107822138 | [NPY](tensors/0004118.npy) |
| 4119 | `model.layers.0.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.78125 / 3.4375 / -0.02474473958136514 / 0.5734634871178346 | [NPY](tensors/0004119.npy) |
| 4120 | `model.layers.0.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.625 / 37.25 / 0.020388836330837674 / 1.1598935516105113 | [NPY](tensors/0004120.npy) |
| 4121 | `model.layers.0.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.625 / 37.25 / 0.020388836330837674 / 1.1598935516105113 | [NPY](tensors/0004121.npy) |
| 4122 | `model.layers.0.self_attn` | 35 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.003748046469507621 / 0.04186477186444624 | [NPY](tensors/0004122.npy) |
| 4123 | `model.layers.0.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 38.5 / -0.0116729736328125 / 2.923730382397291 | [NPY](tensors/0004123.npy) |
| 4124 | `model.layers.0.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0 / 1.5078125 / 0.003351058562596639 / 0.27273943432766234 | [NPY](tensors/0004124.npy) |
| 4125 | `model.layers.0.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0 / 1.5078125 / 0.003351058562596639 / 0.27273943432766234 | [NPY](tensors/0004125.npy) |
| 4126 | `model.layers.0.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.0 / 1.5078125 / 0.003351058562596639 / 0.27273943432766234 | [NPY](tensors/0004126.npy) |
| 4127 | `model.layers.0.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4128 | `model.layers.0.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4129 | `model.layers.0.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4130 | `model.layers.0.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.625 / 10.375 / 0.009823864450057347 / 0.5557877998318892 | [NPY](tensors/0004130.npy) |
| 4131 | `model.layers.0.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.625 / 10.375 / 0.009823864450057347 / 0.5557877998318892 | [NPY](tensors/0004131.npy) |
| 4132 | `model.layers.0.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.421875 / 1.6953125 / -0.024837493896484375 / 0.9979186619487888 | [NPY](tensors/0004132.npy) |
| 4133 | `model.layers.0` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 49.0 / -0.001917637719048394 / 2.9081585606899525 | [NPY](tensors/0004133.npy) |
| 4212 | `model.layers.0` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.5 / 30.625 / 0.03435131601161427 / 2.148670063069294 | [NPY](tensors/0004212.npy) |
| 4213 | `model.layers.0` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004213.npy) |
| 4214 | `model.layers.0` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0004214.npy) |
| 4215 | `model.layers.0` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0004215.npy) |
| 4216 | `model.layers.0` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0004216.npy) |
| 4217 | `model.layers.0` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4218 | `model.layers.0` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4219 | `model.layers.0` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4220 | `model.layers.0.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.5 / 30.625 / 0.03435131601161427 / 2.148670063069294 | [NPY](tensors/0004220.npy) |
| 4221 | `model.layers.0.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004221.npy) |
| 4222 | `model.layers.0.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004222.npy) |
| 4223 | `model.layers.0.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004223.npy) |
| 4224 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0004224.npy) |
| 4225 | `model.layers.0.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4226 | `model.layers.0.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4227 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0004227.npy) |
| 4228 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0004228.npy) |
| 4229 | `model.layers.0.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4230 | `model.layers.0.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004230.npy) |
| 4231 | `model.layers.0.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.59375 / 8.875 / -0.01820482179755345 / 1.2112680722654519 | [NPY](tensors/0004231.npy) |
| 4232 | `model.layers.0.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004232.npy) |
| 4233 | `model.layers.0.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -47.25 / 51.0 / 0.04916292428970337 / 5.661126585935481 | [NPY](tensors/0004233.npy) |
| 4234 | `model.layers.0.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004234.npy) |
| 4235 | `model.layers.0.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.59375 / 4.9375 / -0.02149730920791626 / 1.5738961772339104 | [NPY](tensors/0004235.npy) |
| 4236 | `model.layers.0.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.03125 / 3.03125 / -0.018543873382441234 / 0.45541216016879527 | [NPY](tensors/0004236.npy) |
| 4237 | `model.layers.0.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.75 / 30.625 / 0.008288550128539404 / 0.9985268121431764 | [NPY](tensors/0004237.npy) |
| 4238 | `model.layers.0.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.75 / 30.625 / 0.008288550128539404 / 0.9985268121431764 | [NPY](tensors/0004238.npy) |
| 4239 | `model.layers.0.self_attn` | 36 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0021792159900517207 / 0.03410594948659605 | [NPY](tensors/0004239.npy) |
| 4240 | `model.layers.0.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 32.25 / 0.04269087314605713 / 2.453193825847444 | [NPY](tensors/0004240.npy) |
| 4241 | `model.layers.0.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 2.453125 / 0.00497970183690389 / 0.42168271707165894 | [NPY](tensors/0004241.npy) |
| 4242 | `model.layers.0.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 2.453125 / 0.00497970183690389 / 0.42168271707165894 | [NPY](tensors/0004242.npy) |
| 4243 | `model.layers.0.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 2.453125 / 0.00497970183690389 / 0.42168271707165894 | [NPY](tensors/0004243.npy) |
| 4244 | `model.layers.0.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4245 | `model.layers.0.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4246 | `model.layers.0.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4247 | `model.layers.0.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.0625 / 47.25 / 0.03329368813170327 / 1.466482260027812 | [NPY](tensors/0004247.npy) |
| 4248 | `model.layers.0.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0625 / 47.25 / 0.03329368813170327 / 1.466482260027812 | [NPY](tensors/0004248.npy) |
| 4249 | `model.layers.0.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.328125 / 2.015625 / -0.13678359985351562 / 0.8638543528761768 | [NPY](tensors/0004249.npy) |
| 4250 | `model.layers.0` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 75.0 / 0.07611062791612414 / 3.269710526558343 | [NPY](tensors/0004250.npy) |
| 4329 | `model.layers.0` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0004329.npy) |
| 4330 | `model.layers.0` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004330.npy) |
| 4331 | `model.layers.0` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0004331.npy) |
| 4332 | `model.layers.0` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0004332.npy) |
| 4333 | `model.layers.0` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0004333.npy) |
| 4334 | `model.layers.0` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4335 | `model.layers.0` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4336 | `model.layers.0` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4337 | `model.layers.0.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0004337.npy) |
| 4338 | `model.layers.0.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004338.npy) |
| 4339 | `model.layers.0.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004339.npy) |
| 4340 | `model.layers.0.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004340.npy) |
| 4341 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0004341.npy) |
| 4342 | `model.layers.0.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4343 | `model.layers.0.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4344 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0004344.npy) |
| 4345 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0004345.npy) |
| 4346 | `model.layers.0.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4347 | `model.layers.0.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004347.npy) |
| 4348 | `model.layers.0.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 8.0 / 0.0014486645814031363 / 1.027321203413773 | [NPY](tensors/0004348.npy) |
| 4349 | `model.layers.0.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004349.npy) |
| 4350 | `model.layers.0.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.75 / 53.75 / 0.06940409168601036 / 5.734687316339554 | [NPY](tensors/0004350.npy) |
| 4351 | `model.layers.0.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004351.npy) |
| 4352 | `model.layers.0.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.8125 / 3.75 / -0.006423294544219971 / 0.9290448609736645 | [NPY](tensors/0004352.npy) |
| 4353 | `model.layers.0.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.28125 / 3.734375 / -0.004733989103442582 / 0.6365266937763558 | [NPY](tensors/0004353.npy) |
| 4354 | `model.layers.0.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.25 / 34.25 / 0.026766169236765967 / 1.0852135582774154 | [NPY](tensors/0004354.npy) |
| 4355 | `model.layers.0.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.25 / 34.25 / 0.026766169236765967 / 1.0852135582774154 | [NPY](tensors/0004355.npy) |
| 4356 | `model.layers.0.self_attn` | 37 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0037731625710376616 / 0.041131318596069236 | [NPY](tensors/0004356.npy) |
| 4357 | `model.layers.0.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -67.5 / 34.75 / -0.06431025399102105 / 2.984195500228793 | [NPY](tensors/0004357.npy) |
| 4358 | `model.layers.0.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9296875 / 1.4921875 / 0.0027867794036865235 / 0.33306949669277025 | [NPY](tensors/0004358.npy) |
| 4359 | `model.layers.0.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9296875 / 1.4921875 / 0.0027867794036865235 / 0.33306949669277025 | [NPY](tensors/0004359.npy) |
| 4360 | `model.layers.0.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.9296875 / 1.4921875 / 0.0027867794036865235 / 0.33306949669277025 | [NPY](tensors/0004360.npy) |
| 4361 | `model.layers.0.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4362 | `model.layers.0.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4363 | `model.layers.0.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4364 | `model.layers.0.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.21875 / 11.5 / 0.014639533431747825 / 0.522256120841106 | [NPY](tensors/0004364.npy) |
| 4365 | `model.layers.0.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.21875 / 11.5 / 0.014639533431747825 / 0.522256120841106 | [NPY](tensors/0004365.npy) |
| 4366 | `model.layers.0.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.4375 / 1.421875 / -0.012800216674804688 / 1.2934157037337826 | [NPY](tensors/0004366.npy) |
| 4367 | `model.layers.0` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -56.0 / 45.25 / -0.0497758600446913 / 3.0121210722901735 | [NPY](tensors/0004367.npy) |
| 4446 | `model.layers.0` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.75 / 32.0 / 0.02612974349823263 / 2.3052590463349314 | [NPY](tensors/0004446.npy) |
| 4447 | `model.layers.0` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004447.npy) |
| 4448 | `model.layers.0` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0004448.npy) |
| 4449 | `model.layers.0` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0004449.npy) |
| 4450 | `model.layers.0` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0004450.npy) |
| 4451 | `model.layers.0` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4452 | `model.layers.0` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4453 | `model.layers.0` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4454 | `model.layers.0.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.75 / 32.0 / 0.02612974349823263 / 2.3052590463349314 | [NPY](tensors/0004454.npy) |
| 4455 | `model.layers.0.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004455.npy) |
| 4456 | `model.layers.0.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004456.npy) |
| 4457 | `model.layers.0.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004457.npy) |
| 4458 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0004458.npy) |
| 4459 | `model.layers.0.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4460 | `model.layers.0.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4461 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0004461.npy) |
| 4462 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0004462.npy) |
| 4463 | `model.layers.0.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4464 | `model.layers.0.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004464.npy) |
| 4465 | `model.layers.0.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.375 / 10.0625 / -0.0011312136193737388 / 1.2762524673806912 | [NPY](tensors/0004465.npy) |
| 4466 | `model.layers.0.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004466.npy) |
| 4467 | `model.layers.0.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.5 / 51.25 / 0.02611599490046501 / 5.9708322691785325 | [NPY](tensors/0004467.npy) |
| 4468 | `model.layers.0.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004468.npy) |
| 4469 | `model.layers.0.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / 0.016116023063659668 / 1.5717161949904705 | [NPY](tensors/0004469.npy) |
| 4470 | `model.layers.0.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.1875 / 3.953125 / -0.017835254780948162 / 0.620750270225644 | [NPY](tensors/0004470.npy) |
| 4471 | `model.layers.0.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.125 / 33.75 / 0.01958285735713111 / 1.0657655752092383 | [NPY](tensors/0004471.npy) |
| 4472 | `model.layers.0.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.125 / 33.75 / 0.01958285735713111 / 1.0657655752092383 | [NPY](tensors/0004472.npy) |
| 4473 | `model.layers.0.self_attn` | 38 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0037846481877845547 / 0.04752066673296614 | [NPY](tensors/0004473.npy) |
| 4474 | `model.layers.0.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 36.5 / 0.04565734598371718 / 2.611663924295841 | [NPY](tensors/0004474.npy) |
| 4475 | `model.layers.0.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.671875 / 0.014192130830552842 / 0.4085355561430625 | [NPY](tensors/0004475.npy) |
| 4476 | `model.layers.0.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.671875 / 0.014192130830552842 / 0.4085355561430625 | [NPY](tensors/0004476.npy) |
| 4477 | `model.layers.0.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.671875 / 0.014192130830552842 / 0.4085355561430625 | [NPY](tensors/0004477.npy) |
| 4478 | `model.layers.0.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4479 | `model.layers.0.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4480 | `model.layers.0.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4481 | `model.layers.0.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -11.0 / 25.25 / 0.020281307068136002 / 1.0935389061380238 | [NPY](tensors/0004481.npy) |
| 4482 | `model.layers.0.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0 / 25.25 / 0.020281307068136002 / 1.0935389061380238 | [NPY](tensors/0004482.npy) |
| 4483 | `model.layers.0.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.7265625 / 3.359375 / -0.27642822265625 / 1.190263517515631 | [NPY](tensors/0004483.npy) |
| 4484 | `model.layers.0` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 61.75 / 0.06612621943155925 / 3.085361510108704 | [NPY](tensors/0004484.npy) |
| 4563 | `model.layers.0` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 38.75 / -0.019637677404615615 / 2.869533421530457 | [NPY](tensors/0004563.npy) |
| 4564 | `model.layers.0` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004564.npy) |
| 4565 | `model.layers.0` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0004565.npy) |
| 4566 | `model.layers.0` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0004566.npy) |
| 4567 | `model.layers.0` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0004567.npy) |
| 4568 | `model.layers.0` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4569 | `model.layers.0` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4570 | `model.layers.0` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4571 | `model.layers.0.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 38.75 / -0.019637677404615615 / 2.869533421530457 | [NPY](tensors/0004571.npy) |
| 4572 | `model.layers.0.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0004572.npy) |
| 4573 | `model.layers.0.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0004573.npy) |
| 4574 | `model.layers.0.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004574.npy) |
| 4575 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0004575.npy) |
| 4576 | `model.layers.0.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4577 | `model.layers.0.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4578 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0004578.npy) |
| 4579 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0004579.npy) |
| 4580 | `model.layers.0.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4581 | `model.layers.0.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0004581.npy) |
| 4582 | `model.layers.0.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0 / 9.4375 / 0.009774616220965981 / 1.008080585961609 | [NPY](tensors/0004582.npy) |
| 4583 | `model.layers.0.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0004583.npy) |
| 4584 | `model.layers.0.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.5 / 52.0 / -0.04840673506259918 / 6.119228313490181 | [NPY](tensors/0004584.npy) |
| 4585 | `model.layers.0.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0004585.npy) |
| 4586 | `model.layers.0.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.34375 / 3.625 / -0.03821904957294464 / 0.9543836895451787 | [NPY](tensors/0004586.npy) |
| 4587 | `model.layers.0.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.125 / 4.15625 / -0.008111281706078444 / 0.5414699905981852 | [NPY](tensors/0004587.npy) |
| 4588 | `model.layers.0.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.6875 / 33.5 / 0.030925079849031235 / 1.0523178787003034 | [NPY](tensors/0004588.npy) |
| 4589 | `model.layers.0.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.6875 / 33.5 / 0.030925079849031235 / 1.0523178787003034 | [NPY](tensors/0004589.npy) |
| 4590 | `model.layers.0.self_attn` | 39 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003331721150700062 / 0.03561156829503056 | [NPY](tensors/0004590.npy) |
| 4591 | `model.layers.0.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.75 / 38.75 / 0.011316278245713976 / 2.864947355229164 | [NPY](tensors/0004591.npy) |
| 4592 | `model.layers.0.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.4375 / 2.109375 / 0.0023830845952033997 / 0.2851751813925033 | [NPY](tensors/0004592.npy) |
| 4593 | `model.layers.0.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.4375 / 2.109375 / 0.0023830845952033997 / 0.2851751813925033 | [NPY](tensors/0004593.npy) |
| 4594 | `model.layers.0.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.4375 / 2.109375 / 0.0023830845952033997 / 0.2851751813925033 | [NPY](tensors/0004594.npy) |
| 4595 | `model.layers.0.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4596 | `model.layers.0.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4597 | `model.layers.0.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4598 | `model.layers.0.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -12.625 / 19.875 / 0.01921366055806478 / 0.8410989567765066 | [NPY](tensors/0004598.npy) |
| 4599 | `model.layers.0.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.625 / 19.875 / 0.01921366055806478 / 0.8410989567765066 | [NPY](tensors/0004599.npy) |
| 4600 | `model.layers.0.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.875 / 1.7890625 / -0.016084671020507812 / 1.1670905366044768 | [NPY](tensors/0004600.npy) |
| 4601 | `model.layers.0` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 50.5 / 0.03047859403822157 / 3.0301627227852648 | [NPY](tensors/0004601.npy) |
| 4680 | `model.layers.0` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 25.0 / 0.01804563016113308 / 2.3323165527333782 | [NPY](tensors/0004680.npy) |
| 4681 | `model.layers.0` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004681.npy) |
| 4682 | `model.layers.0` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0004682.npy) |
| 4683 | `model.layers.0` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0004683.npy) |
| 4684 | `model.layers.0` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0004684.npy) |
| 4685 | `model.layers.0` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4686 | `model.layers.0` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4687 | `model.layers.0` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4688 | `model.layers.0.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 25.0 / 0.01804563016113308 / 2.3323165527333782 | [NPY](tensors/0004688.npy) |
| 4689 | `model.layers.0.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0004689.npy) |
| 4690 | `model.layers.0.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0004690.npy) |
| 4691 | `model.layers.0.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004691.npy) |
| 4692 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0004692.npy) |
| 4693 | `model.layers.0.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4694 | `model.layers.0.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4695 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0004695.npy) |
| 4696 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0004696.npy) |
| 4697 | `model.layers.0.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4698 | `model.layers.0.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0004698.npy) |
| 4699 | `model.layers.0.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 8.75 / 0.005578655982390046 / 1.1564340991725837 | [NPY](tensors/0004699.npy) |
| 4700 | `model.layers.0.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0004700.npy) |
| 4701 | `model.layers.0.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -56.25 / 41.75 / -0.16974663734436035 / 5.496621344446725 | [NPY](tensors/0004701.npy) |
| 4702 | `model.layers.0.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0004702.npy) |
| 4703 | `model.layers.0.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.6875 / 4.5 / 0.06943026185035706 / 1.339855997999367 | [NPY](tensors/0004703.npy) |
| 4704 | `model.layers.0.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.3125 / 4.28125 / -0.007479188321667607 / 0.5089794785826152 | [NPY](tensors/0004704.npy) |
| 4705 | `model.layers.0.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.5 / 37.0 / 0.01549987726741367 / 1.1662243764181912 | [NPY](tensors/0004705.npy) |
| 4706 | `model.layers.0.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.5 / 37.0 / 0.01549987726741367 / 1.1662243764181912 | [NPY](tensors/0004706.npy) |
| 4707 | `model.layers.0.self_attn` | 40 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002928844611576774 / 0.037135903829301674 | [NPY](tensors/0004707.npy) |
| 4708 | `model.layers.0.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 42.5 / 0.033490057786305746 / 2.7590941456176448 | [NPY](tensors/0004708.npy) |
| 4709 | `model.layers.0.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.109375 / 1.4921875 / 0.006449392603503333 / 0.2963610821061281 | [NPY](tensors/0004709.npy) |
| 4710 | `model.layers.0.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.109375 / 1.4921875 / 0.006449392603503333 / 0.2963610821061281 | [NPY](tensors/0004710.npy) |
| 4711 | `model.layers.0.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.109375 / 1.4921875 / 0.006449392603503333 / 0.2963610821061281 | [NPY](tensors/0004711.npy) |
| 4712 | `model.layers.0.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4713 | `model.layers.0.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4714 | `model.layers.0.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4715 | `model.layers.0.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.5625 / 28.25 / 0.018549992392460506 / 0.9923764358604463 | [NPY](tensors/0004715.npy) |
| 4716 | `model.layers.0.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.5625 / 28.25 / 0.018549992392460506 / 0.9923764358604463 | [NPY](tensors/0004716.npy) |
| 4717 | `model.layers.0.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3828125 / 2.03125 / -0.14588165283203125 / 0.7306822073099465 | [NPY](tensors/0004717.npy) |
| 4718 | `model.layers.0` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.5 / 68.0 / 0.05182503594292535 / 3.302202641458996 | [NPY](tensors/0004718.npy) |
| 4797 | `model.layers.0` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 40.25 / -0.06394515766037835 / 2.6467228965831135 | [NPY](tensors/0004797.npy) |
| 4798 | `model.layers.0` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004798.npy) |
| 4799 | `model.layers.0` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0004799.npy) |
| 4800 | `model.layers.0` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0004800.npy) |
| 4801 | `model.layers.0` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0004801.npy) |
| 4802 | `model.layers.0` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4803 | `model.layers.0` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4804 | `model.layers.0` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4805 | `model.layers.0.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 40.25 / -0.06394515766037835 / 2.6467228965831135 | [NPY](tensors/0004805.npy) |
| 4806 | `model.layers.0.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004806.npy) |
| 4807 | `model.layers.0.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004807.npy) |
| 4808 | `model.layers.0.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004808.npy) |
| 4809 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0004809.npy) |
| 4810 | `model.layers.0.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4811 | `model.layers.0.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4812 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0004812.npy) |
| 4813 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0004813.npy) |
| 4814 | `model.layers.0.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4815 | `model.layers.0.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004815.npy) |
| 4816 | `model.layers.0.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.6875 / 7.625 / -0.005639673676341772 / 1.046891081389267 | [NPY](tensors/0004816.npy) |
| 4817 | `model.layers.0.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004817.npy) |
| 4818 | `model.layers.0.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.75 / 51.5 / 0.029395833611488342 / 5.690317737756353 | [NPY](tensors/0004818.npy) |
| 4819 | `model.layers.0.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004819.npy) |
| 4820 | `model.layers.0.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.5625 / 4.03125 / 0.016885966062545776 / 1.1800325387513315 | [NPY](tensors/0004820.npy) |
| 4821 | `model.layers.0.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.4375 / 3.65625 / 0.006782118680803251 / 0.5338424385318744 | [NPY](tensors/0004821.npy) |
| 4822 | `model.layers.0.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.25 / 41.25 / 0.029333271293176547 / 1.2178318820852938 | [NPY](tensors/0004822.npy) |
| 4823 | `model.layers.0.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.25 / 41.25 / 0.029333271293176547 / 1.2178318820852938 | [NPY](tensors/0004823.npy) |
| 4824 | `model.layers.0.self_attn` | 41 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0032738586637654833 / 0.03392884602080014 | [NPY](tensors/0004824.npy) |
| 4825 | `model.layers.0.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 42.75 / -0.03450627856784397 / 3.014608972516309 | [NPY](tensors/0004825.npy) |
| 4826 | `model.layers.0.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9296875 / 2.953125 / 0.0042027917173173696 / 0.3109277632400683 | [NPY](tensors/0004826.npy) |
| 4827 | `model.layers.0.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9296875 / 2.953125 / 0.0042027917173173696 / 0.3109277632400683 | [NPY](tensors/0004827.npy) |
| 4828 | `model.layers.0.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.9296875 / 2.953125 / 0.0042027917173173696 / 0.3109277632400683 | [NPY](tensors/0004828.npy) |
| 4829 | `model.layers.0.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4830 | `model.layers.0.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4831 | `model.layers.0.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4832 | `model.layers.0.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.96875 / 17.75 / 0.01567674097087648 / 0.7142336482987736 | [NPY](tensors/0004832.npy) |
| 4833 | `model.layers.0.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.96875 / 17.75 / 0.01567674097087648 / 0.7142336482987736 | [NPY](tensors/0004833.npy) |
| 4834 | `model.layers.0.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.59375 / 1.9609375 / -0.05594635009765625 / 1.1322869152150232 | [NPY](tensors/0004834.npy) |
| 4835 | `model.layers.0` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 60.5 / -0.01864479382832845 / 3.127126778279295 | [NPY](tensors/0004835.npy) |
| 4914 | `model.layers.0` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 50.75 / -0.03880806507335769 / 2.8720089898153187 | [NPY](tensors/0004914.npy) |
| 4915 | `model.layers.0` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004915.npy) |
| 4916 | `model.layers.0` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0004916.npy) |
| 4917 | `model.layers.0` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0004917.npy) |
| 4918 | `model.layers.0` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0004918.npy) |
| 4919 | `model.layers.0` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4920 | `model.layers.0` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4921 | `model.layers.0` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4922 | `model.layers.0.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 50.75 / -0.03880806507335769 / 2.8720089898153187 | [NPY](tensors/0004922.npy) |
| 4923 | `model.layers.0.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0004923.npy) |
| 4924 | `model.layers.0.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0004924.npy) |
| 4925 | `model.layers.0.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004925.npy) |
| 4926 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0004926.npy) |
| 4927 | `model.layers.0.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4928 | `model.layers.0.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4929 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0004929.npy) |
| 4930 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0004930.npy) |
| 4931 | `model.layers.0.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4932 | `model.layers.0.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0004932.npy) |
| 4933 | `model.layers.0.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.15625 / 6.84375 / 0.0022307498147711158 / 0.9416562142053898 | [NPY](tensors/0004933.npy) |
| 4934 | `model.layers.0.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0004934.npy) |
| 4935 | `model.layers.0.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.0 / 42.75 / -0.03451061248779297 / 5.165071669827751 | [NPY](tensors/0004935.npy) |
| 4936 | `model.layers.0.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0004936.npy) |
| 4937 | `model.layers.0.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.5625 / 3.5 / 0.010839223861694336 / 0.9793238812790538 | [NPY](tensors/0004937.npy) |
| 4938 | `model.layers.0.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.40625 / 3.796875 / 0.0056554212260380154 / 0.5866469554748618 | [NPY](tensors/0004938.npy) |
| 4939 | `model.layers.0.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.875 / 34.75 / 0.03773577246401045 / 1.05983514292514 | [NPY](tensors/0004939.npy) |
| 4940 | `model.layers.0.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.875 / 34.75 / 0.03773577246401045 / 1.05983514292514 | [NPY](tensors/0004940.npy) |
| 4941 | `model.layers.0.self_attn` | 42 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.003586458385473318 / 0.03877654037073738 | [NPY](tensors/0004941.npy) |
| 4942 | `model.layers.0.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 52.5 / -0.0009868330425686306 / 2.9775571422506104 | [NPY](tensors/0004942.npy) |
| 4943 | `model.layers.0.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6640625 / 3.78125 / -0.002192427714665731 / 0.30191481130522413 | [NPY](tensors/0004943.npy) |
| 4944 | `model.layers.0.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6640625 / 3.78125 / -0.002192427714665731 / 0.30191481130522413 | [NPY](tensors/0004944.npy) |
| 4945 | `model.layers.0.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.6640625 / 3.78125 / -0.002192427714665731 / 0.30191481130522413 | [NPY](tensors/0004945.npy) |
| 4946 | `model.layers.0.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4947 | `model.layers.0.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4948 | `model.layers.0.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4949 | `model.layers.0.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.96875 / 31.875 / 0.022293574776914384 / 0.9748690762621899 | [NPY](tensors/0004949.npy) |
| 4950 | `model.layers.0.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.96875 / 31.875 / 0.022293574776914384 / 0.9748690762621899 | [NPY](tensors/0004950.npy) |
| 4951 | `model.layers.0.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.09375 / 2.328125 / -0.07628822326660156 / 1.0483386287095144 | [NPY](tensors/0004951.npy) |
| 4952 | `model.layers.0` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 68.0 / 0.021010743247138128 / 3.180115563294993 | [NPY](tensors/0004952.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -41728.0 / 1104.0 / 0.4688976555151207 / 51.173493883379344 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 287, 287] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6888605876758521e+38 / 1.6947554069517734e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 287, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8059103239704092 / 0.8702201565512877 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 287, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11909344536799918 / 0.6232883906716997 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 287] | torch.int64 → int64 | 0.0 / 286.0 / 143.0 / 82.84926070883192 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -41728.0 / 1104.0 / 0.4688976555151207 / 51.173493883379344 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 287, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05926392632390564 / 3.1039007485945094 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 287, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05926392632390564 / 3.1039007485945094 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 287, 287] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6888605876758521e+38 / 1.6947554069517734e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 287] | torch.int64 → int64 | 0.0 / 286.0 / 143.0 / 82.84926070883192 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 287, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8059103239704092 / 0.8702201565512877 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 287, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11909344536799918 / 0.6232883906716997 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05926392632390564 / 3.1039007485945094 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 287, 4096] | torch.bfloat16 → float32 | -12.4375 / 14.625 / 0.03627891375233051 / 1.3776453609625179 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05926392632390564 / 3.1039007485945094 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 287, 512] | torch.bfloat16 → float32 | -37.5 / 41.0 / 0.04069799802652219 / 3.3801272923361605 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05926392632390564 / 3.1039007485945094 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 287, 512] | torch.bfloat16 → float32 | -15.9375 / 22.0 / -0.004533468950085524 / 2.546014025981907 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 287, 4096] | torch.bfloat16 → float32 | -11.0 / 13.0625 / -0.010435616806388225 / 1.427164207034608 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 287, 2880] | torch.bfloat16 → float32 | -470.0 / 400.0 / -0.03703334981347013 / 5.990955949737094 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -470.0 / 400.0 / -0.03703334981347013 / 5.990955949737094 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 287, 287] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0028017831503963898 / 0.018441829165388054 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -41728.0 / 656.0 / 0.43187487757672094 / 50.53831933677629 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 287, 2880] | torch.bfloat16 → float32 | -78.5 / 6.375 / 0.010600653100445825 / 0.782601246034893 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -78.5 / 6.375 / 0.010600653100445825 / 0.782601246034893 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [287, 2880] | torch.bfloat16 → float32 | -78.5 / 6.375 / 0.010600653100445825 / 0.782601246034893 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [287, 2880] | torch.bfloat16 → float32 | -408.0 / 340.0 / 0.08923737372088192 / 8.003379526447306 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -408.0 / 340.0 / 0.08923737372088192 / 8.003379526447306 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [287, 32] | torch.bfloat16 → float32 | -10.75 / 3.109375 / -0.16868357708229836 / 0.8018049652692885 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 287, 2880] | torch.bfloat16 → float32 | -41728.0 / 772.0 / 0.5210970210696763 / 52.55651875245747 | [NPY](tensors/0000077.npy) |
| 156 | `model.layers.11` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -238.0 / 384.0 / 0.9440253363715277 / 18.097377435613 | [NPY](tensors/0000156.npy) |
| 157 | `model.layers.11` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 288] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000157.npy) |
| 158 | `model.layers.11` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.6712646484375 / 0.9670054124125442 | [NPY](tensors/0000158.npy) |
| 159 | `model.layers.11` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.12011004984378815 / 0.6397178164422894 | [NPY](tensors/0000159.npy) |
| 160 | `model.layers.11` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 287.0 / 287.0 / 287.0 / 0.0 | [NPY](tensors/0000160.npy) |
| 161 | `model.layers.11` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 162 | `model.layers.11` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 163 | `model.layers.11` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 164 | `model.layers.11.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -238.0 / 384.0 / 0.9440253363715277 / 18.097377435613 | [NPY](tensors/0000164.npy) |
| 165 | `model.layers.11.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 94.0 / 0.11138428449630737 / 2.9033010278907776 | [NPY](tensors/0000165.npy) |
| 166 | `model.layers.11.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 94.0 / 0.11138428449630737 / 2.9033010278907776 | [NPY](tensors/0000166.npy) |
| 167 | `model.layers.11.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 288] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000167.npy) |
| 168 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 287.0 / 287.0 / 287.0 / 0.0 | [NPY](tensors/0000168.npy) |
| 169 | `model.layers.11.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 170 | `model.layers.11.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 171 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.6712646484375 / 0.9670054124125442 | [NPY](tensors/0000171.npy) |
| 172 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.12011004984378815 / 0.6397178164422894 | [NPY](tensors/0000172.npy) |
| 173 | `model.layers.11.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 174 | `model.layers.11.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 94.0 / 0.11138428449630737 / 2.9033010278907776 | [NPY](tensors/0000174.npy) |
| 175 | `model.layers.11.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.8125 / 10.5 / 0.07106236275285482 / 1.3406894561880547 | [NPY](tensors/0000175.npy) |
| 176 | `model.layers.11.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 94.0 / 0.11138428449630737 / 2.9033010278907776 | [NPY](tensors/0000176.npy) |
| 177 | `model.layers.11.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 33.5 / 0.0362166166305542 / 3.7947532257261267 | [NPY](tensors/0000177.npy) |
| 178 | `model.layers.11.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 94.0 / 0.11138428449630737 / 2.9033010278907776 | [NPY](tensors/0000178.npy) |
| 179 | `model.layers.11.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.8125 / 10.5 / 0.09844797849655151 / 2.565995204532302 | [NPY](tensors/0000179.npy) |
| 180 | `model.layers.11.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.9375 / 7.90625 / -0.004178196657449007 / 1.2798742394970664 | [NPY](tensors/0000180.npy) |
| 181 | `model.layers.11.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 44.5 / -0.12291891309950087 / 3.8743532563876943 | [NPY](tensors/0000181.npy) |
| 182 | `model.layers.11.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 44.5 / -0.12291891309950087 / 3.8743532563876943 | [NPY](tensors/0000182.npy) |
| 183 | `model.layers.11.self_attn` | 1 | `output[1]` | [1, 64, 1, 288] | torch.bfloat16 → float32 | 5.820766091346741e-11 / 0.82421875 / 0.0032167256775633333 / 0.014429140644830158 | [NPY](tensors/0000183.npy) |
| 184 | `model.layers.11.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -194.0 / 332.0 / 0.8211754692925347 / 17.626682555691648 | [NPY](tensors/0000184.npy) |
| 185 | `model.layers.11.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.46875 / 3.15625 / 0.02410293552610609 / 0.7625004700391365 | [NPY](tensors/0000185.npy) |
| 186 | `model.layers.11.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.46875 / 3.15625 / 0.02410293552610609 / 0.7625004700391365 | [NPY](tensors/0000186.npy) |
| 187 | `model.layers.11.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.46875 / 3.15625 / 0.02410293552610609 / 0.7625004700391365 | [NPY](tensors/0000187.npy) |
| 188 | `model.layers.11.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 189 | `model.layers.11.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 190 | `model.layers.11.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 191 | `model.layers.11.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -153.0 / 133.0 / 0.20284225253595245 / 6.423271982536265 | [NPY](tensors/0000191.npy) |
| 192 | `model.layers.11.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -153.0 / 133.0 / 0.20284225253595245 / 6.423271982536265 | [NPY](tensors/0000192.npy) |
| 193 | `model.layers.11.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.5 / 1.15625 / -0.1067962646484375 / 0.5661221940864162 | [NPY](tensors/0000193.npy) |
| 194 | `model.layers.11` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -348.0 / 432.0 / 1.023585679796007 / 21.233657244911807 | [NPY](tensors/0000194.npy) |
| 273 | `model.layers.11` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -342.0 / 732.0 / 0.8805762396918403 / 27.42942234693856 | [NPY](tensors/0000273.npy) |
| 274 | `model.layers.11` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 289] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000274.npy) |
| 275 | `model.layers.11` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.7242279052734375 / 0.9308467876495331 | [NPY](tensors/0000275.npy) |
| 276 | `model.layers.11` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.25 / 0.10570904612541199 / 0.6393518089241342 | [NPY](tensors/0000276.npy) |
| 277 | `model.layers.11` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 288.0 / 288.0 / 288.0 / 0.0 | [NPY](tensors/0000277.npy) |
| 278 | `model.layers.11` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 279 | `model.layers.11` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 280 | `model.layers.11` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 281 | `model.layers.11.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -342.0 / 732.0 / 0.8805762396918403 / 27.42942234693856 | [NPY](tensors/0000281.npy) |
| 282 | `model.layers.11.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 125.0 / 0.07875569131639269 / 3.119423762019139 | [NPY](tensors/0000282.npy) |
| 283 | `model.layers.11.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 125.0 / 0.07875569131639269 / 3.119423762019139 | [NPY](tensors/0000283.npy) |
| 284 | `model.layers.11.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 289] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000284.npy) |
| 285 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 288.0 / 288.0 / 288.0 / 0.0 | [NPY](tensors/0000285.npy) |
| 286 | `model.layers.11.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 287 | `model.layers.11.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 288 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.7242279052734375 / 0.9308467876495331 | [NPY](tensors/0000288.npy) |
| 289 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.25 / 0.10570904612541199 / 0.6393518089241342 | [NPY](tensors/0000289.npy) |
| 290 | `model.layers.11.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 291 | `model.layers.11.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 125.0 / 0.07875569131639269 / 3.119423762019139 | [NPY](tensors/0000291.npy) |
| 292 | `model.layers.11.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.8125 / 9.6875 / 0.004424724727869034 / 1.3750377123044752 | [NPY](tensors/0000292.npy) |
| 293 | `model.layers.11.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 125.0 / 0.07875569131639269 / 3.119423762019139 | [NPY](tensors/0000293.npy) |
| 294 | `model.layers.11.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.0 / 31.125 / -0.041958823800086975 / 3.7636838020375345 | [NPY](tensors/0000294.npy) |
| 295 | `model.layers.11.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 125.0 / 0.07875569131639269 / 3.119423762019139 | [NPY](tensors/0000295.npy) |
| 296 | `model.layers.11.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.5 / 8.9375 / 0.0852055549621582 / 3.033121271644375 | [NPY](tensors/0000296.npy) |
| 297 | `model.layers.11.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.90625 / 8.8125 / 0.012536512687802315 / 1.836779995750857 | [NPY](tensors/0000297.npy) |
| 298 | `model.layers.11.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.25 / 65.5 / -0.09530827734205458 / 5.454639642739843 | [NPY](tensors/0000298.npy) |
| 299 | `model.layers.11.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.25 / 65.5 / -0.09530827734205458 / 5.454639642739843 | [NPY](tensors/0000299.npy) |
| 300 | `model.layers.11.self_attn` | 2 | `output[1]` | [1, 64, 1, 289] | torch.bfloat16 → float32 | 9.731593308970332e-11 / 0.9453125 / 0.0032921383995353436 / 0.01569127791771064 | [NPY](tensors/0000300.npy) |
| 301 | `model.layers.11.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -316.0 / 668.0 / 0.7861575656467014 / 28.642368903579115 | [NPY](tensors/0000301.npy) |
| 302 | `model.layers.11.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.8125 / 0.01108334329393175 / 0.7746623071989114 | [NPY](tensors/0000302.npy) |
| 303 | `model.layers.11.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.8125 / 0.01108334329393175 / 0.7746623071989114 | [NPY](tensors/0000303.npy) |
| 304 | `model.layers.11.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.8125 / 0.01108334329393175 / 0.7746623071989114 | [NPY](tensors/0000304.npy) |
| 305 | `model.layers.11.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 306 | `model.layers.11.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 307 | `model.layers.11.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 308 | `model.layers.11.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -312.0 / 304.0 / 0.23821205447117488 / 10.937389143489789 | [NPY](tensors/0000308.npy) |
| 309 | `model.layers.11.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 304.0 / 0.23821205447117488 / 10.937389143489789 | [NPY](tensors/0000309.npy) |
| 310 | `model.layers.11.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.0625 / 1.203125 / -0.102783203125 / 0.625861506965005 | [NPY](tensors/0000310.npy) |
| 311 | `model.layers.11` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -628.0 / 972.0 / 1.0245934380425348 / 36.33000408634142 | [NPY](tensors/0000311.npy) |
| 390 | `model.layers.11` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -200.0 / 572.0 / 0.6845473395453558 / 23.02357124265403 | [NPY](tensors/0000390.npy) |
| 391 | `model.layers.11` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 290] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000391.npy) |
| 392 | `model.layers.11` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.76885986328125 / 0.9124536436370704 | [NPY](tensors/0000392.npy) |
| 393 | `model.layers.11` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2421875 / 0.1397949606180191 / 0.6049175711104398 | [NPY](tensors/0000393.npy) |
| 394 | `model.layers.11` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 289.0 / 289.0 / 289.0 / 0.0 | [NPY](tensors/0000394.npy) |
| 395 | `model.layers.11` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 396 | `model.layers.11` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 397 | `model.layers.11` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 398 | `model.layers.11.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -200.0 / 572.0 / 0.6845473395453558 / 23.02357124265403 | [NPY](tensors/0000398.npy) |
| 399 | `model.layers.11.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 116.5 / 0.08714440531200833 / 2.871651328053226 | [NPY](tensors/0000399.npy) |
| 400 | `model.layers.11.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 116.5 / 0.08714440531200833 / 2.871651328053226 | [NPY](tensors/0000400.npy) |
| 401 | `model.layers.11.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 290] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000401.npy) |
| 402 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 289.0 / 289.0 / 289.0 / 0.0 | [NPY](tensors/0000402.npy) |
| 403 | `model.layers.11.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 404 | `model.layers.11.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 405 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.76885986328125 / 0.9124536436370704 | [NPY](tensors/0000405.npy) |
| 406 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2421875 / 0.1397949606180191 / 0.6049175711104398 | [NPY](tensors/0000406.npy) |
| 407 | `model.layers.11.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 408 | `model.layers.11.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 116.5 / 0.08714440531200833 / 2.871651328053226 | [NPY](tensors/0000408.npy) |
| 409 | `model.layers.11.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.96875 / 13.0 / 0.039713765610940754 / 1.3887914235621177 | [NPY](tensors/0000409.npy) |
| 410 | `model.layers.11.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 116.5 / 0.08714440531200833 / 2.871651328053226 | [NPY](tensors/0000410.npy) |
| 411 | `model.layers.11.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.875 / 31.75 / 0.054288119077682495 / 3.8018661476626647 | [NPY](tensors/0000411.npy) |
| 412 | `model.layers.11.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 116.5 / 0.08714440531200833 / 2.871651328053226 | [NPY](tensors/0000412.npy) |
| 413 | `model.layers.11.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.8125 / 7.625 / 0.09988939762115479 / 2.8297173660219874 | [NPY](tensors/0000413.npy) |
| 414 | `model.layers.11.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.25 / 7.59375 / 0.027508526807650924 / 1.7628754285141963 | [NPY](tensors/0000414.npy) |
| 415 | `model.layers.11.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.75 / 85.0 / -0.07025549146864149 / 5.196949332125026 | [NPY](tensors/0000415.npy) |
| 416 | `model.layers.11.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.75 / 85.0 / -0.07025549146864149 / 5.196949332125026 | [NPY](tensors/0000416.npy) |
| 417 | `model.layers.11.self_attn` | 3 | `output[1]` | [1, 64, 1, 290] | torch.bfloat16 → float32 | 1.0587086762825493e-12 / 0.953125 / 0.0033416275973135287 / 0.015339363370138076 | [NPY](tensors/0000417.npy) |
| 418 | `model.layers.11.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -254.0 / 536.0 / 0.6139122856987848 / 24.775837468473036 | [NPY](tensors/0000418.npy) |
| 419 | `model.layers.11.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.703125 / 3.875 / 0.006010510192977057 / 0.7857592948524892 | [NPY](tensors/0000419.npy) |
| 420 | `model.layers.11.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.703125 / 3.875 / 0.006010510192977057 / 0.7857592948524892 | [NPY](tensors/0000420.npy) |
| 421 | `model.layers.11.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.703125 / 3.875 / 0.006010510192977057 / 0.7857592948524892 | [NPY](tensors/0000421.npy) |
| 422 | `model.layers.11.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 423 | `model.layers.11.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 424 | `model.layers.11.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 425 | `model.layers.11.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -195.0 / 158.0 / 0.24955216033591165 / 7.611579528766741 | [NPY](tensors/0000425.npy) |
| 426 | `model.layers.11.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -195.0 / 158.0 / 0.24955216033591165 / 7.611579528766741 | [NPY](tensors/0000426.npy) |
| 427 | `model.layers.11.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.5078125 / 1.28125 / -0.0876007080078125 / 0.7213167649479975 | [NPY](tensors/0000427.npy) |
| 428 | `model.layers.11` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -448.0 / 696.0 / 0.8652916802300348 / 29.224669808176156 | [NPY](tensors/0000428.npy) |
| 507 | `model.layers.11` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -188.0 / 288.0 / 0.43257073296440973 / 16.349055631526515 | [NPY](tensors/0000507.npy) |
| 508 | `model.layers.11` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 291] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000508.npy) |
| 509 | `model.layers.11` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.77325439453125 / 0.9030595537086521 | [NPY](tensors/0000509.npy) |
| 510 | `model.layers.11` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2421875 / 0.19747132062911987 / 0.5978860929332719 | [NPY](tensors/0000510.npy) |
| 511 | `model.layers.11` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 290.0 / 290.0 / 290.0 / 0.0 | [NPY](tensors/0000511.npy) |
| 512 | `model.layers.11` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 513 | `model.layers.11` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 514 | `model.layers.11` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 515 | `model.layers.11.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -188.0 / 288.0 / 0.43257073296440973 / 16.349055631526515 | [NPY](tensors/0000515.npy) |
| 516 | `model.layers.11.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -60.25 / 82.5 / 0.07666432791286044 / 2.7119100608072224 | [NPY](tensors/0000516.npy) |
| 517 | `model.layers.11.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -60.25 / 82.5 / 0.07666432791286044 / 2.7119100608072224 | [NPY](tensors/0000517.npy) |
| 518 | `model.layers.11.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 291] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000518.npy) |
| 519 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 290.0 / 290.0 / 290.0 / 0.0 | [NPY](tensors/0000519.npy) |
| 520 | `model.layers.11.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 521 | `model.layers.11.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 522 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.77325439453125 / 0.9030595537086521 | [NPY](tensors/0000522.npy) |
| 523 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2421875 / 0.19747132062911987 / 0.5978860929332719 | [NPY](tensors/0000523.npy) |
| 524 | `model.layers.11.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 525 | `model.layers.11.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -60.25 / 82.5 / 0.07666432791286044 / 2.7119100608072224 | [NPY](tensors/0000525.npy) |
| 526 | `model.layers.11.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.53125 / 9.875 / 0.04468944785185158 / 1.3115997342766041 | [NPY](tensors/0000526.npy) |
| 527 | `model.layers.11.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -60.25 / 82.5 / 0.07666432791286044 / 2.7119100608072224 | [NPY](tensors/0000527.npy) |
| 528 | `model.layers.11.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -24.25 / 26.5 / 0.05265296995639801 / 3.432737794464733 | [NPY](tensors/0000528.npy) |
| 529 | `model.layers.11.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -60.25 / 82.5 / 0.07666432791286044 / 2.7119100608072224 | [NPY](tensors/0000529.npy) |
| 530 | `model.layers.11.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.25 / 6.4375 / 0.014474868774414062 / 2.2170073879723424 | [NPY](tensors/0000530.npy) |
| 531 | `model.layers.11.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.90625 / 6.875 / 0.02160395309329033 / 1.5197287745722254 | [NPY](tensors/0000531.npy) |
| 532 | `model.layers.11.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 110.0 / 0.04763153791427612 / 4.712161635722856 | [NPY](tensors/0000532.npy) |
| 533 | `model.layers.11.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 110.0 / 0.04763153791427612 / 4.712161635722856 | [NPY](tensors/0000533.npy) |
| 534 | `model.layers.11.self_attn` | 4 | `output[1]` | [1, 64, 1, 291] | torch.bfloat16 → float32 | 7.239577826112509e-10 / 0.84375 / 0.0032101728154281563 / 0.012986870795510273 | [NPY](tensors/0000534.npy) |
| 535 | `model.layers.11.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -278.0 / 336.0 / 0.4811248779296875 / 18.962330902376035 | [NPY](tensors/0000535.npy) |
| 536 | `model.layers.11.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.3125 / 3.359375 / 0.009210051430596247 / 0.7477066776208974 | [NPY](tensors/0000536.npy) |
| 537 | `model.layers.11.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.3125 / 3.359375 / 0.009210051430596247 / 0.7477066776208974 | [NPY](tensors/0000537.npy) |
| 538 | `model.layers.11.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.3125 / 3.359375 / 0.009210051430596247 / 0.7477066776208974 | [NPY](tensors/0000538.npy) |
| 539 | `model.layers.11.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 540 | `model.layers.11.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 541 | `model.layers.11.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 542 | `model.layers.11.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -19.25 / 81.0 / 0.039444488949245876 / 4.9721868566668475 | [NPY](tensors/0000542.npy) |
| 543 | `model.layers.11.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.25 / 81.0 / 0.039444488949245876 / 4.9721868566668475 | [NPY](tensors/0000543.npy) |
| 544 | `model.layers.11.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3515625 / 1.6484375 / -0.060577392578125 / 0.6817905751592185 | [NPY](tensors/0000544.npy) |
| 545 | `model.layers.11` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -286.0 / 416.0 / 0.5197436862521702 / 20.985617160334556 | [NPY](tensors/0000545.npy) |
| 624 | `model.layers.11` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -304.0 / 402.0 / 0.4433746337890625 / 18.639092865189856 | [NPY](tensors/0000624.npy) |
| 625 | `model.layers.11` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 292] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000625.npy) |
| 626 | `model.layers.11` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.73895263671875 / 0.9515453580587002 | [NPY](tensors/0000626.npy) |
| 627 | `model.layers.11` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.8203125 / 1.265625 / 0.2415669560432434 / 0.5473552672930101 | [NPY](tensors/0000627.npy) |
| 628 | `model.layers.11` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 291.0 / 291.0 / 291.0 / 0.0 | [NPY](tensors/0000628.npy) |
| 629 | `model.layers.11` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 630 | `model.layers.11` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 631 | `model.layers.11` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 632 | `model.layers.11.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -304.0 / 402.0 / 0.4433746337890625 / 18.639092865189856 | [NPY](tensors/0000632.npy) |
| 633 | `model.layers.11.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 101.0 / 0.06507225566440158 / 3.1111202053872766 | [NPY](tensors/0000633.npy) |
| 634 | `model.layers.11.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 101.0 / 0.06507225566440158 / 3.1111202053872766 | [NPY](tensors/0000634.npy) |
| 635 | `model.layers.11.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 292] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000635.npy) |
| 636 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 291.0 / 291.0 / 291.0 / 0.0 | [NPY](tensors/0000636.npy) |
| 637 | `model.layers.11.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 638 | `model.layers.11.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 639 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.73895263671875 / 0.9515453580587002 | [NPY](tensors/0000639.npy) |
| 640 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.8203125 / 1.265625 / 0.2415669560432434 / 0.5473552672930101 | [NPY](tensors/0000640.npy) |
| 641 | `model.layers.11.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 642 | `model.layers.11.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 101.0 / 0.06507225566440158 / 3.1111202053872766 | [NPY](tensors/0000642.npy) |
| 643 | `model.layers.11.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5625 / 9.9375 / 0.04921533539891243 / 1.2289113356759476 | [NPY](tensors/0000643.npy) |
| 644 | `model.layers.11.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 101.0 / 0.06507225566440158 / 3.1111202053872766 | [NPY](tensors/0000644.npy) |
| 645 | `model.layers.11.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.0 / 33.0 / 0.10971809178590775 / 3.454724850257713 | [NPY](tensors/0000645.npy) |
| 646 | `model.layers.11.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 101.0 / 0.06507225566440158 / 3.1111202053872766 | [NPY](tensors/0000646.npy) |
| 647 | `model.layers.11.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.0 / 5.6875 / -0.004941597580909729 / 1.7634961010439871 | [NPY](tensors/0000647.npy) |
| 648 | `model.layers.11.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.40625 / 6.03125 / 0.008618272840976715 / 1.3670117013144045 | [NPY](tensors/0000648.npy) |
| 649 | `model.layers.11.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 42.0 / 0.03554552131228977 / 3.7816827926075693 | [NPY](tensors/0000649.npy) |
| 650 | `model.layers.11.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 42.0 / 0.03554552131228977 / 3.7816827926075693 | [NPY](tensors/0000650.npy) |
| 651 | `model.layers.11.self_attn` | 5 | `output[1]` | [1, 64, 1, 292] | torch.bfloat16 → float32 | 3.637978807091713e-11 / 0.9609375 / 0.0032634714831896567 / 0.014193838269952562 | [NPY](tensors/0000651.npy) |
| 652 | `model.layers.11.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -288.0 / 368.0 / 0.47828776041666665 / 19.338021636122857 | [NPY](tensors/0000652.npy) |
| 653 | `model.layers.11.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.40625 / -0.002368197176191542 / 0.6894078097654116 | [NPY](tensors/0000653.npy) |
| 654 | `model.layers.11.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.40625 / -0.002368197176191542 / 0.6894078097654116 | [NPY](tensors/0000654.npy) |
| 655 | `model.layers.11.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.40625 / -0.002368197176191542 / 0.6894078097654116 | [NPY](tensors/0000655.npy) |
| 656 | `model.layers.11.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 657 | `model.layers.11.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 658 | `model.layers.11.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 659 | `model.layers.11.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -59.5 / 115.0 / 0.10753668149312337 / 4.921032580197561 | [NPY](tensors/0000659.npy) |
| 660 | `model.layers.11.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -59.5 / 115.0 / 0.10753668149312337 / 4.921032580197561 | [NPY](tensors/0000660.npy) |
| 661 | `model.layers.11.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8828125 / 0.84375 / -0.08737754821777344 / 0.5994158043396718 | [NPY](tensors/0000661.npy) |
| 662 | `model.layers.11` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -348.0 / 428.0 / 0.5852281358506944 / 21.979847087515584 | [NPY](tensors/0000662.npy) |
| 741 | `model.layers.11` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -286.0 / 360.0 / 0.5935505761040581 / 15.940808192656165 | [NPY](tensors/0000741.npy) |
| 742 | `model.layers.11` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 293] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000742.npy) |
| 743 | `model.layers.11` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.6932373046875 / 1.0101839228451497 | [NPY](tensors/0000743.npy) |
| 744 | `model.layers.11` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.80078125 / 1.3203125 / 0.25535039603710175 / 0.49363048052358244 | [NPY](tensors/0000744.npy) |
| 745 | `model.layers.11` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 292.0 / 292.0 / 292.0 / 0.0 | [NPY](tensors/0000745.npy) |
| 746 | `model.layers.11` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 747 | `model.layers.11` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 748 | `model.layers.11` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 749 | `model.layers.11.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -286.0 / 360.0 / 0.5935505761040581 / 15.940808192656165 | [NPY](tensors/0000749.npy) |
| 750 | `model.layers.11.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 106.0 / 0.0784795085589091 / 3.26479731767196 | [NPY](tensors/0000750.npy) |
| 751 | `model.layers.11.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 106.0 / 0.0784795085589091 / 3.26479731767196 | [NPY](tensors/0000751.npy) |
| 752 | `model.layers.11.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 293] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000752.npy) |
| 753 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 292.0 / 292.0 / 292.0 / 0.0 | [NPY](tensors/0000753.npy) |
| 754 | `model.layers.11.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 755 | `model.layers.11.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 756 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.6932373046875 / 1.0101839228451497 | [NPY](tensors/0000756.npy) |
| 757 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.80078125 / 1.3203125 / 0.25535039603710175 / 0.49363048052358244 | [NPY](tensors/0000757.npy) |
| 758 | `model.layers.11.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 759 | `model.layers.11.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 106.0 / 0.0784795085589091 / 3.26479731767196 | [NPY](tensors/0000759.npy) |
| 760 | `model.layers.11.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.59375 / 7.71875 / 0.03335337503813207 / 1.190621600538494 | [NPY](tensors/0000760.npy) |
| 761 | `model.layers.11.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 106.0 / 0.0784795085589091 / 3.26479731767196 | [NPY](tensors/0000761.npy) |
| 762 | `model.layers.11.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.625 / 33.75 / 0.11136285960674286 / 3.4989367298772525 | [NPY](tensors/0000762.npy) |
| 763 | `model.layers.11.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 106.0 / 0.0784795085589091 / 3.26479731767196 | [NPY](tensors/0000763.npy) |
| 764 | `model.layers.11.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.15625 / 6.0625 / 0.09192708134651184 / 1.8326625992189445 | [NPY](tensors/0000764.npy) |
| 765 | `model.layers.11.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.84375 / 5.53125 / 0.023411709116771817 / 1.321422046982903 | [NPY](tensors/0000765.npy) |
| 766 | `model.layers.11.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 65.5 / -0.01149010161558787 / 4.061910114327974 | [NPY](tensors/0000766.npy) |
| 767 | `model.layers.11.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 65.5 / -0.01149010161558787 / 4.061910114327974 | [NPY](tensors/0000767.npy) |
| 768 | `model.layers.11.self_attn` | 6 | `output[1]` | [1, 64, 1, 293] | torch.bfloat16 → float32 | 2.582964953035116e-10 / 0.921875 / 0.003257507358103001 / 0.01455714778540544 | [NPY](tensors/0000768.npy) |
| 769 | `model.layers.11.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -220.0 / 338.0 / 0.581414794921875 / 16.07367444361107 | [NPY](tensors/0000769.npy) |
| 770 | `model.layers.11.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.65625 / 3.265625 / 0.019244694709777833 / 0.6726285743524978 | [NPY](tensors/0000770.npy) |
| 771 | `model.layers.11.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.65625 / 3.265625 / 0.019244694709777833 / 0.6726285743524978 | [NPY](tensors/0000771.npy) |
| 772 | `model.layers.11.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.65625 / 3.265625 / 0.019244694709777833 / 0.6726285743524978 | [NPY](tensors/0000772.npy) |
| 773 | `model.layers.11.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 774 | `model.layers.11.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 775 | `model.layers.11.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 776 | `model.layers.11.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -131.0 / 128.0 / -0.03925216214524375 / 6.688879507194869 | [NPY](tensors/0000776.npy) |
| 777 | `model.layers.11.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -131.0 / 128.0 / -0.03925216214524375 / 6.688879507194869 | [NPY](tensors/0000777.npy) |
| 778 | `model.layers.11.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3671875 / 1.28125 / -0.09895133972167969 / 0.5148258271625061 | [NPY](tensors/0000778.npy) |
| 779 | `model.layers.11` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -352.0 / 422.0 / 0.5428588519493739 / 20.282281368643144 | [NPY](tensors/0000779.npy) |
| 858 | `model.layers.11` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -348.0 / 448.0 / 0.6064628601074219 / 19.244245521318913 | [NPY](tensors/0000858.npy) |
| 859 | `model.layers.11` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 294] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000859.npy) |
| 860 | `model.layers.11` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6579437255859375 / 0.9936083133652351 | [NPY](tensors/0000860.npy) |
| 861 | `model.layers.11` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.99609375 / 1.34375 / 0.25000885128974915 / 0.5715972585679053 | [NPY](tensors/0000861.npy) |
| 862 | `model.layers.11` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 293.0 / 293.0 / 293.0 / 0.0 | [NPY](tensors/0000862.npy) |
| 863 | `model.layers.11` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 864 | `model.layers.11` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 865 | `model.layers.11` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 866 | `model.layers.11.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -348.0 / 448.0 / 0.6064628601074219 / 19.244245521318913 | [NPY](tensors/0000866.npy) |
| 867 | `model.layers.11.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.0 / 109.0 / 0.06795724497901069 / 3.3155684311487197 | [NPY](tensors/0000867.npy) |
| 868 | `model.layers.11.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.0 / 109.0 / 0.06795724497901069 / 3.3155684311487197 | [NPY](tensors/0000868.npy) |
| 869 | `model.layers.11.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 294] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000869.npy) |
| 870 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 293.0 / 293.0 / 293.0 / 0.0 | [NPY](tensors/0000870.npy) |
| 871 | `model.layers.11.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 872 | `model.layers.11.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 873 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6579437255859375 / 0.9936083133652351 | [NPY](tensors/0000873.npy) |
| 874 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.99609375 / 1.34375 / 0.25000885128974915 / 0.5715972585679053 | [NPY](tensors/0000874.npy) |
| 875 | `model.layers.11.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 876 | `model.layers.11.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.0 / 109.0 / 0.06795724497901069 / 3.3155684311487197 | [NPY](tensors/0000876.npy) |
| 877 | `model.layers.11.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.0 / 8.5 / 0.03442587649624329 / 1.2189688359374447 | [NPY](tensors/0000877.npy) |
| 878 | `model.layers.11.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.0 / 109.0 / 0.06795724497901069 / 3.3155684311487197 | [NPY](tensors/0000878.npy) |
| 879 | `model.layers.11.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.75 / 34.75 / 0.07125416398048401 / 3.7794499627838385 | [NPY](tensors/0000879.npy) |
| 880 | `model.layers.11.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.0 / 109.0 / 0.06795724497901069 / 3.3155684311487197 | [NPY](tensors/0000880.npy) |
| 881 | `model.layers.11.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.46875 / 7.46875 / 0.0726999044418335 / 1.9749772708634579 | [NPY](tensors/0000881.npy) |
| 882 | `model.layers.11.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.4375 / 6.09375 / 0.033021162438672036 / 1.2811489133919869 | [NPY](tensors/0000882.npy) |
| 883 | `model.layers.11.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.0 / 83.5 / -0.05180122057596843 / 4.3324467741442545 | [NPY](tensors/0000883.npy) |
| 884 | `model.layers.11.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.0 / 83.5 / -0.05180122057596843 / 4.3324467741442545 | [NPY](tensors/0000884.npy) |
| 885 | `model.layers.11.self_attn` | 7 | `output[1]` | [1, 64, 1, 294] | torch.bfloat16 → float32 | 4.5929482439532876e-11 / 0.94921875 / 0.0031756594526855006 / 0.017784723900337626 | [NPY](tensors/0000885.npy) |
| 886 | `model.layers.11.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -264.0 / 372.0 / 0.5545528835720486 / 18.73044729587814 | [NPY](tensors/0000886.npy) |
| 887 | `model.layers.11.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5 / 3.078125 / 0.010748212867312961 / 0.7010757721003342 | [NPY](tensors/0000887.npy) |
| 888 | `model.layers.11.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5 / 3.078125 / 0.010748212867312961 / 0.7010757721003342 | [NPY](tensors/0000888.npy) |
| 889 | `model.layers.11.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.5 / 3.078125 / 0.010748212867312961 / 0.7010757721003342 | [NPY](tensors/0000889.npy) |
| 890 | `model.layers.11.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 891 | `model.layers.11.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 892 | `model.layers.11.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 893 | `model.layers.11.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -216.0 / 214.0 / 0.05098404884338379 / 8.12475841179448 | [NPY](tensors/0000893.npy) |
| 894 | `model.layers.11.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -216.0 / 214.0 / 0.05098404884338379 / 8.12475841179448 | [NPY](tensors/0000894.npy) |
| 895 | `model.layers.11.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.5859375 / 1.3984375 / -0.07796192169189453 / 0.5637397223705785 | [NPY](tensors/0000895.npy) |
| 896 | `model.layers.11` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -480.0 / 568.0 / 0.6053931342230903 / 24.115443428853297 | [NPY](tensors/0000896.npy) |
| 975 | `model.layers.11` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -620.0 / 560.0 / 0.39112108018663194 / 24.442568029358362 | [NPY](tensors/0000975.npy) |
| 976 | `model.layers.11` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 295] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000976.npy) |
| 977 | `model.layers.11` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.63275146484375 / 0.9803225324656689 | [NPY](tensors/0000977.npy) |
| 978 | `model.layers.11` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.24692200124263763 / 0.6218146623522595 | [NPY](tensors/0000978.npy) |
| 979 | `model.layers.11` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 294.0 / 294.0 / 294.0 / 0.0 | [NPY](tensors/0000979.npy) |
| 980 | `model.layers.11` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 981 | `model.layers.11` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 982 | `model.layers.11` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 983 | `model.layers.11.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -620.0 / 560.0 / 0.39112108018663194 / 24.442568029358362 | [NPY](tensors/0000983.npy) |
| 984 | `model.layers.11.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -133.0 / 101.0 / 0.024186354213290743 / 3.6650188953186102 | [NPY](tensors/0000984.npy) |
| 985 | `model.layers.11.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -133.0 / 101.0 / 0.024186354213290743 / 3.6650188953186102 | [NPY](tensors/0000985.npy) |
| 986 | `model.layers.11.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 295] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000986.npy) |
| 987 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 294.0 / 294.0 / 294.0 / 0.0 | [NPY](tensors/0000987.npy) |
| 988 | `model.layers.11.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 989 | `model.layers.11.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 990 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.63275146484375 / 0.9803225324656689 | [NPY](tensors/0000990.npy) |
| 991 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.24692200124263763 / 0.6218146623522595 | [NPY](tensors/0000991.npy) |
| 992 | `model.layers.11.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 993 | `model.layers.11.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -133.0 / 101.0 / 0.024186354213290743 / 3.6650188953186102 | [NPY](tensors/0000993.npy) |
| 994 | `model.layers.11.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.34375 / 8.25 / 0.05311978608369827 / 1.1867481778843347 | [NPY](tensors/0000994.npy) |
| 995 | `model.layers.11.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -133.0 / 101.0 / 0.024186354213290743 / 3.6650188953186102 | [NPY](tensors/0000995.npy) |
| 996 | `model.layers.11.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.0 / 43.0 / 0.05448628403246403 / 3.9853066747624237 | [NPY](tensors/0000996.npy) |
| 997 | `model.layers.11.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -133.0 / 101.0 / 0.024186354213290743 / 3.6650188953186102 | [NPY](tensors/0000997.npy) |
| 998 | `model.layers.11.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.15625 / 8.3125 / -0.0365881621837616 / 2.236821708473568 | [NPY](tensors/0000998.npy) |
| 999 | `model.layers.11.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 7.1875 / 0.015124194324016571 / 1.2766167005478315 | [NPY](tensors/0000999.npy) |
| 1000 | `model.layers.11.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -156.0 / 239.0 / -0.08566928439670139 / 6.626238218198771 | [NPY](tensors/0001000.npy) |
| 1001 | `model.layers.11.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -156.0 / 239.0 / -0.08566928439670139 / 6.626238218198771 | [NPY](tensors/0001001.npy) |
| 1002 | `model.layers.11.self_attn` | 8 | `output[1]` | [1, 64, 1, 295] | torch.bfloat16 → float32 | 8.753886504564434e-12 / 0.9609375 / 0.0029935457072439906 / 0.020578657919747043 | [NPY](tensors/0001002.npy) |
| 1003 | `model.layers.11.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -380.0 / 460.0 / 0.30710415310329864 / 21.055329848498502 | [NPY](tensors/0001003.npy) |
| 1004 | `model.layers.11.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.03125 / 3.40625 / 0.008434242010116577 / 0.68450381326217 | [NPY](tensors/0001004.npy) |
| 1005 | `model.layers.11.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.03125 / 3.40625 / 0.008434242010116577 / 0.68450381326217 | [NPY](tensors/0001005.npy) |
| 1006 | `model.layers.11.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.03125 / 3.40625 / 0.008434242010116577 / 0.68450381326217 | [NPY](tensors/0001006.npy) |
| 1007 | `model.layers.11.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1008 | `model.layers.11.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1009 | `model.layers.11.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1010 | `model.layers.11.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -248.0 / 274.0 / 0.12904317643907334 / 10.078867108671728 | [NPY](tensors/0001010.npy) |
| 1011 | `model.layers.11.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -248.0 / 274.0 / 0.12904317643907334 / 10.078867108671728 | [NPY](tensors/0001011.npy) |
| 1012 | `model.layers.11.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.109375 / 1.4609375 / -0.16109466552734375 / 0.7466095746758975 | [NPY](tensors/0001012.npy) |
| 1013 | `model.layers.11` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -628.0 / 648.0 / 0.43607889811197914 / 28.276426453853546 | [NPY](tensors/0001013.npy) |
| 1092 | `model.layers.11` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -496.0 / 532.0 / 0.585422600640191 / 21.56130659084653 | [NPY](tensors/0001092.npy) |
| 1093 | `model.layers.11` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 296] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001093.npy) |
| 1094 | `model.layers.11` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59735107421875 / 1.0432862341497364 | [NPY](tensors/0001094.npy) |
| 1095 | `model.layers.11` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.73828125 / 1.3046875 / 0.24880489706993103 / 0.5509575399105547 | [NPY](tensors/0001095.npy) |
| 1096 | `model.layers.11` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 295.0 / 295.0 / 295.0 / 0.0 | [NPY](tensors/0001096.npy) |
| 1097 | `model.layers.11` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1098 | `model.layers.11` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1099 | `model.layers.11` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1100 | `model.layers.11.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -496.0 / 532.0 / 0.585422600640191 / 21.56130659084653 | [NPY](tensors/0001100.npy) |
| 1101 | `model.layers.11.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -120.5 / 103.5 / 0.05347305138905843 / 3.563790246935513 | [NPY](tensors/0001101.npy) |
| 1102 | `model.layers.11.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -120.5 / 103.5 / 0.05347305138905843 / 3.563790246935513 | [NPY](tensors/0001102.npy) |
| 1103 | `model.layers.11.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 296] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001103.npy) |
| 1104 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 295.0 / 295.0 / 295.0 / 0.0 | [NPY](tensors/0001104.npy) |
| 1105 | `model.layers.11.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1106 | `model.layers.11.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1107 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59735107421875 / 1.0432862341497364 | [NPY](tensors/0001107.npy) |
| 1108 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.73828125 / 1.3046875 / 0.24880489706993103 / 0.5509575399105547 | [NPY](tensors/0001108.npy) |
| 1109 | `model.layers.11.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1110 | `model.layers.11.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -120.5 / 103.5 / 0.05347305138905843 / 3.563790246935513 | [NPY](tensors/0001110.npy) |
| 1111 | `model.layers.11.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.46875 / 8.0 / 0.05696024210192263 / 1.143326311704916 | [NPY](tensors/0001111.npy) |
| 1112 | `model.layers.11.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -120.5 / 103.5 / 0.05347305138905843 / 3.563790246935513 | [NPY](tensors/0001112.npy) |
| 1113 | `model.layers.11.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.5 / 37.0 / 0.019070953130722046 / 3.861075477623591 | [NPY](tensors/0001113.npy) |
| 1114 | `model.layers.11.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -120.5 / 103.5 / 0.05347305138905843 / 3.563790246935513 | [NPY](tensors/0001114.npy) |
| 1115 | `model.layers.11.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.3125 / 6.21875 / 0.07518401741981506 / 2.0383275600900626 | [NPY](tensors/0001115.npy) |
| 1116 | `model.layers.11.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.03125 / 5.78125 / 0.021781422663480043 / 1.1717363897002384 | [NPY](tensors/0001116.npy) |
| 1117 | `model.layers.11.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -128.0 / 165.0 / -0.005255370669894748 / 5.100886404881877 | [NPY](tensors/0001117.npy) |
| 1118 | `model.layers.11.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -128.0 / 165.0 / -0.005255370669894748 / 5.100886404881877 | [NPY](tensors/0001118.npy) |
| 1119 | `model.layers.11.self_attn` | 9 | `output[1]` | [1, 64, 1, 296] | torch.bfloat16 → float32 | 1.6608936448392342e-13 / 0.953125 / 0.0029926210404107407 / 0.01737102269470613 | [NPY](tensors/0001119.npy) |
| 1120 | `model.layers.11.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -332.0 / 452.0 / 0.57978515625 / 19.450623572789794 | [NPY](tensors/0001120.npy) |
| 1121 | `model.layers.11.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.625 / 2.796875 / 0.016087556547588772 / 0.6717806594255087 | [NPY](tensors/0001121.npy) |
| 1122 | `model.layers.11.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.625 / 2.796875 / 0.016087556547588772 / 0.6717806594255087 | [NPY](tensors/0001122.npy) |
| 1123 | `model.layers.11.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.625 / 2.796875 / 0.016087556547588772 / 0.6717806594255087 | [NPY](tensors/0001123.npy) |
| 1124 | `model.layers.11.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1125 | `model.layers.11.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1126 | `model.layers.11.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1127 | `model.layers.11.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -306.0 / 242.0 / 0.01978002389272054 / 10.532102120266416 | [NPY](tensors/0001127.npy) |
| 1128 | `model.layers.11.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -306.0 / 242.0 / 0.01978002389272054 / 10.532102120266416 | [NPY](tensors/0001128.npy) |
| 1129 | `model.layers.11.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.453125 / -0.10473251342773438 / 0.4882561777204516 | [NPY](tensors/0001129.npy) |
| 1130 | `model.layers.11` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -640.0 / 616.0 / 0.6004365709092881 / 27.248635545780793 | [NPY](tensors/0001130.npy) |
| 1209 | `model.layers.11` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -412.0 / 504.0 / 0.710093519422743 / 20.048446942558726 | [NPY](tensors/0001209.npy) |
| 1210 | `model.layers.11` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 297] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001210.npy) |
| 1211 | `model.layers.11` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.54443359375 / 1.0951336419407118 | [NPY](tensors/0001211.npy) |
| 1212 | `model.layers.11` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.2265625 / 0.23366539180278778 / 0.5085507755708512 | [NPY](tensors/0001212.npy) |
| 1213 | `model.layers.11` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 296.0 / 296.0 / 296.0 / 0.0 | [NPY](tensors/0001213.npy) |
| 1214 | `model.layers.11` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1215 | `model.layers.11` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1216 | `model.layers.11` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1217 | `model.layers.11.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -412.0 / 504.0 / 0.710093519422743 / 20.048446942558726 | [NPY](tensors/0001217.npy) |
| 1218 | `model.layers.11.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.0 / 118.0 / 0.07547120220131344 / 3.5353914759849654 | [NPY](tensors/0001218.npy) |
| 1219 | `model.layers.11.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.0 / 118.0 / 0.07547120220131344 / 3.5353914759849654 | [NPY](tensors/0001219.npy) |
| 1220 | `model.layers.11.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 297] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001220.npy) |
| 1221 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 296.0 / 296.0 / 296.0 / 0.0 | [NPY](tensors/0001221.npy) |
| 1222 | `model.layers.11.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1223 | `model.layers.11.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1224 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.54443359375 / 1.0951336419407118 | [NPY](tensors/0001224.npy) |
| 1225 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.2265625 / 0.23366539180278778 / 0.5085507755708512 | [NPY](tensors/0001225.npy) |
| 1226 | `model.layers.11.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1227 | `model.layers.11.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.0 / 118.0 / 0.07547120220131344 / 3.5353914759849654 | [NPY](tensors/0001227.npy) |
| 1228 | `model.layers.11.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.84375 / 7.375 / 0.05901078582974151 / 1.1604812486606737 | [NPY](tensors/0001228.npy) |
| 1229 | `model.layers.11.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.0 / 118.0 / 0.07547120220131344 / 3.5353914759849654 | [NPY](tensors/0001229.npy) |
| 1230 | `model.layers.11.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.25 / 33.25 / 0.03916012495756149 / 3.754381393258973 | [NPY](tensors/0001230.npy) |
| 1231 | `model.layers.11.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.0 / 118.0 / 0.07547120220131344 / 3.5353914759849654 | [NPY](tensors/0001231.npy) |
| 1232 | `model.layers.11.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.875 / 5.6875 / 0.06886538863182068 / 1.860626480781582 | [NPY](tensors/0001232.npy) |
| 1233 | `model.layers.11.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.21875 / 5.21875 / 0.0328366884496063 / 1.185617948762732 | [NPY](tensors/0001233.npy) |
| 1234 | `model.layers.11.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.0 / 147.0 / -0.03840504222446018 / 4.816940094793894 | [NPY](tensors/0001234.npy) |
| 1235 | `model.layers.11.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.0 / 147.0 / -0.03840504222446018 / 4.816940094793894 | [NPY](tensors/0001235.npy) |
| 1236 | `model.layers.11.self_attn` | 10 | `output[1]` | [1, 64, 1, 297] | torch.bfloat16 → float32 | 1.8758328224066645e-11 / 0.92578125 / 0.00312594021338963 / 0.015777687738780695 | [NPY](tensors/0001236.npy) |
| 1237 | `model.layers.11.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -264.0 / 408.0 / 0.6727939181857638 / 18.93489133070259 | [NPY](tensors/0001237.npy) |
| 1238 | `model.layers.11.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.453125 / 2.453125 / 0.019551143381330703 / 0.6733906636613762 | [NPY](tensors/0001238.npy) |
| 1239 | `model.layers.11.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.453125 / 2.453125 / 0.019551143381330703 / 0.6733906636613762 | [NPY](tensors/0001239.npy) |
| 1240 | `model.layers.11.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.453125 / 2.453125 / 0.019551143381330703 / 0.6733906636613762 | [NPY](tensors/0001240.npy) |
| 1241 | `model.layers.11.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1242 | `model.layers.11.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1243 | `model.layers.11.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1244 | `model.layers.11.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -240.0 / 199.0 / 0.1375603093041314 / 8.09220677751196 | [NPY](tensors/0001244.npy) |
| 1245 | `model.layers.11.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -240.0 / 199.0 / 0.1375603093041314 / 8.09220677751196 | [NPY](tensors/0001245.npy) |
| 1246 | `model.layers.11.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / -0.06906890869140625 / 0.46942399905495547 | [NPY](tensors/0001246.npy) |
| 1247 | `model.layers.11` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -504.0 / 600.0 / 0.8106035020616319 / 24.308318336405826 | [NPY](tensors/0001247.npy) |
| 1326 | `model.layers.11` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -340.0 / 432.0 / 0.394844733344184 / 18.323493906792717 | [NPY](tensors/0001326.npy) |
| 1327 | `model.layers.11` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 298] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001327.npy) |
| 1328 | `model.layers.11` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.4918212890625 / 1.117229907691466 | [NPY](tensors/0001328.npy) |
| 1329 | `model.layers.11` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.3359375 / 0.18026646971702576 / 0.5362459422402894 | [NPY](tensors/0001329.npy) |
| 1330 | `model.layers.11` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 297.0 / 297.0 / 297.0 / 0.0 | [NPY](tensors/0001330.npy) |
| 1331 | `model.layers.11` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1332 | `model.layers.11` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1333 | `model.layers.11` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1334 | `model.layers.11.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -340.0 / 432.0 / 0.394844733344184 / 18.323493906792717 | [NPY](tensors/0001334.npy) |
| 1335 | `model.layers.11.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 110.5 / 0.05341181755065918 / 3.328815941524077 | [NPY](tensors/0001335.npy) |
| 1336 | `model.layers.11.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 110.5 / 0.05341181755065918 / 3.328815941524077 | [NPY](tensors/0001336.npy) |
| 1337 | `model.layers.11.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 298] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001337.npy) |
| 1338 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 297.0 / 297.0 / 297.0 / 0.0 | [NPY](tensors/0001338.npy) |
| 1339 | `model.layers.11.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1340 | `model.layers.11.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1341 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.4918212890625 / 1.117229907691466 | [NPY](tensors/0001341.npy) |
| 1342 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.3359375 / 0.18026646971702576 / 0.5362459422402894 | [NPY](tensors/0001342.npy) |
| 1343 | `model.layers.11.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1344 | `model.layers.11.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 110.5 / 0.05341181755065918 / 3.328815941524077 | [NPY](tensors/0001344.npy) |
| 1345 | `model.layers.11.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.0625 / 7.875 / 0.027584105962887406 / 1.1592322295317499 | [NPY](tensors/0001345.npy) |
| 1346 | `model.layers.11.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 110.5 / 0.05341181755065918 / 3.328815941524077 | [NPY](tensors/0001346.npy) |
| 1347 | `model.layers.11.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -23.0 / 27.875 / 0.0884423777461052 / 3.009864038667338 | [NPY](tensors/0001347.npy) |
| 1348 | `model.layers.11.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 110.5 / 0.05341181755065918 / 3.328815941524077 | [NPY](tensors/0001348.npy) |
| 1349 | `model.layers.11.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.25 / 6.4375 / 0.046298980712890625 / 2.0849233965200615 | [NPY](tensors/0001349.npy) |
| 1350 | `model.layers.11.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.75 / 6.09375 / 0.01930952537804842 / 1.2167970044910374 | [NPY](tensors/0001350.npy) |
| 1351 | `model.layers.11.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.5 / 81.5 / -0.08484086990356446 / 3.999486498120853 | [NPY](tensors/0001351.npy) |
| 1352 | `model.layers.11.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.5 / 81.5 / -0.08484086990356446 / 3.999486498120853 | [NPY](tensors/0001352.npy) |
| 1353 | `model.layers.11.self_attn` | 11 | `output[1]` | [1, 64, 1, 298] | torch.bfloat16 → float32 | 5.384208634495735e-10 / 0.9140625 / 0.0031211509993388457 / 0.014031131413343867 | [NPY](tensors/0001353.npy) |
| 1354 | `model.layers.11.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -258.0 / 326.0 / 0.3097466150919596 / 17.033530015753712 | [NPY](tensors/0001354.npy) |
| 1355 | `model.layers.11.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.265625 / 3.96875 / 0.0028562148412068686 / 0.6852033530198139 | [NPY](tensors/0001355.npy) |
| 1356 | `model.layers.11.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.265625 / 3.96875 / 0.0028562148412068686 / 0.6852033530198139 | [NPY](tensors/0001356.npy) |
| 1357 | `model.layers.11.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.265625 / 3.96875 / 0.0028562148412068686 / 0.6852033530198139 | [NPY](tensors/0001357.npy) |
| 1358 | `model.layers.11.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1359 | `model.layers.11.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1360 | `model.layers.11.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1361 | `model.layers.11.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -109.0 / 122.0 / 0.029462395773993597 / 6.832987489319109 | [NPY](tensors/0001361.npy) |
| 1362 | `model.layers.11.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 122.0 / 0.029462395773993597 / 6.832987489319109 | [NPY](tensors/0001362.npy) |
| 1363 | `model.layers.11.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.3359375 / -0.12887191772460938 / 0.5440547764779946 | [NPY](tensors/0001363.npy) |
| 1364 | `model.layers.11` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -368.0 / 446.0 / 0.33834940592447915 / 21.330814474892314 | [NPY](tensors/0001364.npy) |
| 1443 | `model.layers.11` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -404.0 / 588.0 / 0.5961320665147569 / 22.787400774965583 | [NPY](tensors/0001443.npy) |
| 1444 | `model.layers.11` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 299] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001444.npy) |
| 1445 | `model.layers.11` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.47601318359375 / 1.1300177711987256 | [NPY](tensors/0001445.npy) |
| 1446 | `model.layers.11` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2265625 / 0.09335732460021973 / 0.5447921260742894 | [NPY](tensors/0001446.npy) |
| 1447 | `model.layers.11` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 298.0 / 298.0 / 298.0 / 0.0 | [NPY](tensors/0001447.npy) |
| 1448 | `model.layers.11` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1449 | `model.layers.11` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1450 | `model.layers.11` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1451 | `model.layers.11.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -404.0 / 588.0 / 0.5961320665147569 / 22.787400774965583 | [NPY](tensors/0001451.npy) |
| 1452 | `model.layers.11.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 121.0 / 0.06103031635284424 / 3.407312337516832 | [NPY](tensors/0001452.npy) |
| 1453 | `model.layers.11.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 121.0 / 0.06103031635284424 / 3.407312337516832 | [NPY](tensors/0001453.npy) |
| 1454 | `model.layers.11.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 299] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001454.npy) |
| 1455 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 298.0 / 298.0 / 298.0 / 0.0 | [NPY](tensors/0001455.npy) |
| 1456 | `model.layers.11.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1457 | `model.layers.11.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1458 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.47601318359375 / 1.1300177711987256 | [NPY](tensors/0001458.npy) |
| 1459 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2265625 / 0.09335732460021973 / 0.5447921260742894 | [NPY](tensors/0001459.npy) |
| 1460 | `model.layers.11.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1461 | `model.layers.11.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 121.0 / 0.06103031635284424 / 3.407312337516832 | [NPY](tensors/0001461.npy) |
| 1462 | `model.layers.11.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.59375 / 9.1875 / 0.04092540219426155 / 1.2059964921663133 | [NPY](tensors/0001462.npy) |
| 1463 | `model.layers.11.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 121.0 / 0.06103031635284424 / 3.407312337516832 | [NPY](tensors/0001463.npy) |
| 1464 | `model.layers.11.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -26.5 / 31.5 / -0.01892542839050293 / 3.5337110598228554 | [NPY](tensors/0001464.npy) |
| 1465 | `model.layers.11.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 121.0 / 0.06103031635284424 / 3.407312337516832 | [NPY](tensors/0001465.npy) |
| 1466 | `model.layers.11.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.34375 / 7.84375 / 0.03415849804878235 / 2.3193823387645365 | [NPY](tensors/0001466.npy) |
| 1467 | `model.layers.11.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.9375 / 6.84375 / 0.02098105603363365 / 1.390539345331612 | [NPY](tensors/0001467.npy) |
| 1468 | `model.layers.11.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -125.0 / 95.5 / -0.04173524909549289 / 4.818860473722844 | [NPY](tensors/0001468.npy) |
| 1469 | `model.layers.11.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -125.0 / 95.5 / -0.04173524909549289 / 4.818860473722844 | [NPY](tensors/0001469.npy) |
| 1470 | `model.layers.11.self_attn` | 12 | `output[1]` | [1, 64, 1, 299] | torch.bfloat16 → float32 | 1.0231815394945443e-11 / 0.9453125 / 0.003102707823266386 / 0.0178853210484081 | [NPY](tensors/0001470.npy) |
| 1471 | `model.layers.11.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -308.0 / 464.0 / 0.5549343532986111 / 21.980120369602574 | [NPY](tensors/0001471.npy) |
| 1472 | `model.layers.11.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.96875 / 3.484375 / 0.01585740910636054 / 0.6667338891772353 | [NPY](tensors/0001472.npy) |
| 1473 | `model.layers.11.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.96875 / 3.484375 / 0.01585740910636054 / 0.6667338891772353 | [NPY](tensors/0001473.npy) |
| 1474 | `model.layers.11.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.96875 / 3.484375 / 0.01585740910636054 / 0.6667338891772353 | [NPY](tensors/0001474.npy) |
| 1475 | `model.layers.11.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1476 | `model.layers.11.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1477 | `model.layers.11.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1478 | `model.layers.11.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -154.0 / 185.0 / -0.002127998736169603 / 7.250772552951819 | [NPY](tensors/0001478.npy) |
| 1479 | `model.layers.11.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -154.0 / 185.0 / -0.002127998736169603 / 7.250772552951819 | [NPY](tensors/0001479.npy) |
| 1480 | `model.layers.11.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.4140625 / 1.3671875 / -0.14498519897460938 / 0.5482286332272014 | [NPY](tensors/0001480.npy) |
| 1481 | `model.layers.11` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -462.0 / 628.0 / 0.5540062798394098 / 26.946095607415117 | [NPY](tensors/0001481.npy) |
| 1560 | `model.layers.11` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -201.0 / 384.0 / 0.870081075032552 / 16.984612305483832 | [NPY](tensors/0001560.npy) |
| 1561 | `model.layers.11` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 300] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001561.npy) |
| 1562 | `model.layers.11` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.518310546875 / 1.0946292885024063 | [NPY](tensors/0001562.npy) |
| 1563 | `model.layers.11` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.234375 / 0.009437993168830872 / 0.5857162614275052 | [NPY](tensors/0001563.npy) |
| 1564 | `model.layers.11` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 299.0 / 299.0 / 299.0 / 0.0 | [NPY](tensors/0001564.npy) |
| 1565 | `model.layers.11` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1566 | `model.layers.11` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1567 | `model.layers.11` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1568 | `model.layers.11.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -201.0 / 384.0 / 0.870081075032552 / 16.984612305483832 | [NPY](tensors/0001568.npy) |
| 1569 | `model.layers.11.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.0 / 106.0 / 0.11470295853084989 / 3.0681717490287705 | [NPY](tensors/0001569.npy) |
| 1570 | `model.layers.11.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.0 / 106.0 / 0.11470295853084989 / 3.0681717490287705 | [NPY](tensors/0001570.npy) |
| 1571 | `model.layers.11.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 300] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001571.npy) |
| 1572 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 299.0 / 299.0 / 299.0 / 0.0 | [NPY](tensors/0001572.npy) |
| 1573 | `model.layers.11.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1574 | `model.layers.11.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1575 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.518310546875 / 1.0946292885024063 | [NPY](tensors/0001575.npy) |
| 1576 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.234375 / 0.009437993168830872 / 0.5857162614275052 | [NPY](tensors/0001576.npy) |
| 1577 | `model.layers.11.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1578 | `model.layers.11.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.0 / 106.0 / 0.11470295853084989 / 3.0681717490287705 | [NPY](tensors/0001578.npy) |
| 1579 | `model.layers.11.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.53125 / 7.9375 / 0.06489914795383811 / 1.2017806536246365 | [NPY](tensors/0001579.npy) |
| 1580 | `model.layers.11.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.0 / 106.0 / 0.11470295853084989 / 3.0681717490287705 | [NPY](tensors/0001580.npy) |
| 1581 | `model.layers.11.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.75 / 36.5 / 0.07311010360717773 / 3.9666212428379395 | [NPY](tensors/0001581.npy) |
| 1582 | `model.layers.11.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.0 / 106.0 / 0.11470295853084989 / 3.0681717490287705 | [NPY](tensors/0001582.npy) |
| 1583 | `model.layers.11.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.90625 / 8.1875 / 0.07255852222442627 / 2.216533824630972 | [NPY](tensors/0001583.npy) |
| 1584 | `model.layers.11.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5 / 5.625 / 0.028255364013602957 / 1.2195293479669436 | [NPY](tensors/0001584.npy) |
| 1585 | `model.layers.11.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.75 / 71.0 / 0.1350609767768118 / 3.447058044231067 | [NPY](tensors/0001585.npy) |
| 1586 | `model.layers.11.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.75 / 71.0 / 0.1350609767768118 / 3.447058044231067 | [NPY](tensors/0001586.npy) |
| 1587 | `model.layers.11.self_attn` | 13 | `output[1]` | [1, 64, 1, 300] | torch.bfloat16 → float32 | 4.874891601502895e-10 / 0.828125 / 0.0031045220249658694 / 0.01324994985064686 | [NPY](tensors/0001587.npy) |
| 1588 | `model.layers.11.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -191.0 / 400.0 / 1.0046763949924045 / 18.453388663221155 | [NPY](tensors/0001588.npy) |
| 1589 | `model.layers.11.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.078125 / 2.796875 / 0.038931770622730254 / 0.6567033908457319 | [NPY](tensors/0001589.npy) |
| 1590 | `model.layers.11.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.078125 / 2.796875 / 0.038931770622730254 / 0.6567033908457319 | [NPY](tensors/0001590.npy) |
| 1591 | `model.layers.11.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.078125 / 2.796875 / 0.038931770622730254 / 0.6567033908457319 | [NPY](tensors/0001591.npy) |
| 1592 | `model.layers.11.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1593 | `model.layers.11.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1594 | `model.layers.11.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1595 | `model.layers.11.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -139.0 / 104.0 / 0.15479429827796087 / 5.110563222733852 | [NPY](tensors/0001595.npy) |
| 1596 | `model.layers.11.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -139.0 / 104.0 / 0.15479429827796087 / 5.110563222733852 | [NPY](tensors/0001596.npy) |
| 1597 | `model.layers.11.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.34375 / 0.9921875 / -0.04915142059326172 / 0.48517873299769765 | [NPY](tensors/0001597.npy) |
| 1598 | `model.layers.11` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -330.0 / 504.0 / 1.1588148328993055 / 21.55895286210348 | [NPY](tensors/0001598.npy) |
| 1677 | `model.layers.11` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -198.0 / 322.0 / 0.6263824462890625 / 16.235075655708368 | [NPY](tensors/0001677.npy) |
| 1678 | `model.layers.11` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 301] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001678.npy) |
| 1679 | `model.layers.11` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6011199951171875 / 1.029134772776266 | [NPY](tensors/0001679.npy) |
| 1680 | `model.layers.11` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.02744269371032715 / 0.6241199078176489 | [NPY](tensors/0001680.npy) |
| 1681 | `model.layers.11` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 300.0 / 300.0 / 300.0 / 0.0 | [NPY](tensors/0001681.npy) |
| 1682 | `model.layers.11` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1683 | `model.layers.11` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1684 | `model.layers.11` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1685 | `model.layers.11.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -198.0 / 322.0 / 0.6263824462890625 / 16.235075655708368 | [NPY](tensors/0001685.npy) |
| 1686 | `model.layers.11.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.0 / 93.0 / 0.0945032364792294 / 2.8830868262233817 | [NPY](tensors/0001686.npy) |
| 1687 | `model.layers.11.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.0 / 93.0 / 0.0945032364792294 / 2.8830868262233817 | [NPY](tensors/0001687.npy) |
| 1688 | `model.layers.11.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 301] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001688.npy) |
| 1689 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 300.0 / 300.0 / 300.0 / 0.0 | [NPY](tensors/0001689.npy) |
| 1690 | `model.layers.11.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1691 | `model.layers.11.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1692 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6011199951171875 / 1.029134772776266 | [NPY](tensors/0001692.npy) |
| 1693 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.02744269371032715 / 0.6241199078176489 | [NPY](tensors/0001693.npy) |
| 1694 | `model.layers.11.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1695 | `model.layers.11.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.0 / 93.0 / 0.0945032364792294 / 2.8830868262233817 | [NPY](tensors/0001695.npy) |
| 1696 | `model.layers.11.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.46875 / 9.125 / 0.04998381884070113 / 1.2682158938843116 | [NPY](tensors/0001696.npy) |
| 1697 | `model.layers.11.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.0 / 93.0 / 0.0945032364792294 / 2.8830868262233817 | [NPY](tensors/0001697.npy) |
| 1698 | `model.layers.11.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.375 / 35.0 / 0.10307269543409348 / 3.6460485061101298 | [NPY](tensors/0001698.npy) |
| 1699 | `model.layers.11.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.0 / 93.0 / 0.0945032364792294 / 2.8830868262233817 | [NPY](tensors/0001699.npy) |
| 1700 | `model.layers.11.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.53125 / 6.40625 / 0.13899201154708862 / 2.0741203446670524 | [NPY](tensors/0001700.npy) |
| 1701 | `model.layers.11.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.75 / 6.0 / 0.022381295450031757 / 1.3483578264436253 | [NPY](tensors/0001701.npy) |
| 1702 | `model.layers.11.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.625 / 74.0 / 0.09617511961195203 / 4.045765684929035 | [NPY](tensors/0001702.npy) |
| 1703 | `model.layers.11.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.625 / 74.0 / 0.09617511961195203 / 4.045765684929035 | [NPY](tensors/0001703.npy) |
| 1704 | `model.layers.11.self_attn` | 14 | `output[1]` | [1, 64, 1, 301] | torch.bfloat16 → float32 | 1.4642864698544145e-10 / 0.86328125 / 0.0031070796183749368 / 0.01304510373972436 | [NPY](tensors/0001704.npy) |
| 1705 | `model.layers.11.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -211.0 / 360.0 / 0.7222212049696181 / 18.19360649146223 | [NPY](tensors/0001705.npy) |
| 1706 | `model.layers.11.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.90625 / 2.90625 / 0.02423140737745497 / 0.7257781295016936 | [NPY](tensors/0001706.npy) |
| 1707 | `model.layers.11.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.90625 / 2.90625 / 0.02423140737745497 / 0.7257781295016936 | [NPY](tensors/0001707.npy) |
| 1708 | `model.layers.11.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.90625 / 2.90625 / 0.02423140737745497 / 0.7257781295016936 | [NPY](tensors/0001708.npy) |
| 1709 | `model.layers.11.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1710 | `model.layers.11.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1711 | `model.layers.11.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1712 | `model.layers.11.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -115.5 / 134.0 / 0.10065507623884414 / 5.750788472303328 | [NPY](tensors/0001712.npy) |
| 1713 | `model.layers.11.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -115.5 / 134.0 / 0.10065507623884414 / 5.750788472303328 | [NPY](tensors/0001713.npy) |
| 1714 | `model.layers.11.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.5703125 / 1.1171875 / -0.05759429931640625 / 0.6194977117439684 | [NPY](tensors/0001714.npy) |
| 1715 | `model.layers.11` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -326.0 / 494.0 / 0.8230509440104167 / 21.661907692577444 | [NPY](tensors/0001715.npy) |
| 1794 | `model.layers.11` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -416.0 / 572.0 / 0.6949366251627604 / 23.05579901512956 | [NPY](tensors/0001794.npy) |
| 1795 | `model.layers.11` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 302] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001795.npy) |
| 1796 | `model.layers.11` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6781768798828125 / 0.9972778713983161 | [NPY](tensors/0001796.npy) |
| 1797 | `model.layers.11` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.0019666850566864014 / 0.5958225425092146 | [NPY](tensors/0001797.npy) |
| 1798 | `model.layers.11` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 301.0 / 301.0 / 301.0 / 0.0 | [NPY](tensors/0001798.npy) |
| 1799 | `model.layers.11` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1800 | `model.layers.11` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1801 | `model.layers.11` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1802 | `model.layers.11.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -416.0 / 572.0 / 0.6949366251627604 / 23.05579901512956 | [NPY](tensors/0001802.npy) |
| 1803 | `model.layers.11.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 116.0 / 0.07312834577427971 / 3.426129265988773 | [NPY](tensors/0001803.npy) |
| 1804 | `model.layers.11.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 116.0 / 0.07312834577427971 / 3.426129265988773 | [NPY](tensors/0001804.npy) |
| 1805 | `model.layers.11.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 302] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001805.npy) |
| 1806 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 301.0 / 301.0 / 301.0 / 0.0 | [NPY](tensors/0001806.npy) |
| 1807 | `model.layers.11.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1808 | `model.layers.11.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1809 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6781768798828125 / 0.9972778713983161 | [NPY](tensors/0001809.npy) |
| 1810 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.0019666850566864014 / 0.5958225425092146 | [NPY](tensors/0001810.npy) |
| 1811 | `model.layers.11.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1812 | `model.layers.11.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 116.0 / 0.07312834577427971 / 3.426129265988773 | [NPY](tensors/0001812.npy) |
| 1813 | `model.layers.11.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.75 / 7.625 / 0.03366019402164966 / 1.1657465516345324 | [NPY](tensors/0001813.npy) |
| 1814 | `model.layers.11.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 116.0 / 0.07312834577427971 / 3.426129265988773 | [NPY](tensors/0001814.npy) |
| 1815 | `model.layers.11.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -26.375 / 34.0 / 0.04577096551656723 / 3.4045748922694536 | [NPY](tensors/0001815.npy) |
| 1816 | `model.layers.11.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 116.0 / 0.07312834577427971 / 3.426129265988773 | [NPY](tensors/0001816.npy) |
| 1817 | `model.layers.11.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.875 / 8.6875 / 0.029103100299835205 / 2.2481509902301213 | [NPY](tensors/0001817.npy) |
| 1818 | `model.layers.11.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.90625 / 5.0625 / 0.019091654336079955 / 1.2009649477096225 | [NPY](tensors/0001818.npy) |
| 1819 | `model.layers.11.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -165.0 / 159.0 / -0.056352702776590984 / 5.695748304671921 | [NPY](tensors/0001819.npy) |
| 1820 | `model.layers.11.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -165.0 / 159.0 / -0.056352702776590984 / 5.695748304671921 | [NPY](tensors/0001820.npy) |
| 1821 | `model.layers.11.self_attn` | 15 | `output[1]` | [1, 64, 1, 302] | torch.bfloat16 → float32 | 1.5120349416974932e-11 / 0.9609375 / 0.0029140115976670896 / 0.016387410711451528 | [NPY](tensors/0001821.npy) |
| 1822 | `model.layers.11.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -256.0 / 416.0 / 0.6385006374782987 / 20.83564101125676 | [NPY](tensors/0001822.npy) |
| 1823 | `model.layers.11.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.765625 / 3.421875 / 0.01846970584657457 / 0.7279062055572473 | [NPY](tensors/0001823.npy) |
| 1824 | `model.layers.11.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.765625 / 3.421875 / 0.01846970584657457 / 0.7279062055572473 | [NPY](tensors/0001824.npy) |
| 1825 | `model.layers.11.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.765625 / 3.421875 / 0.01846970584657457 / 0.7279062055572473 | [NPY](tensors/0001825.npy) |
| 1826 | `model.layers.11.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1827 | `model.layers.11.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1828 | `model.layers.11.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1829 | `model.layers.11.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -290.0 / 288.0 / 0.25233399073282875 / 11.130934285491824 | [NPY](tensors/0001829.npy) |
| 1830 | `model.layers.11.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -290.0 / 288.0 / 0.25233399073282875 / 11.130934285491824 | [NPY](tensors/0001830.npy) |
| 1831 | `model.layers.11.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.53125 / -0.05617523193359375 / 0.6105152989584971 | [NPY](tensors/0001831.npy) |
| 1832 | `model.layers.11` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -544.0 / 696.0 / 0.8920830620659722 / 28.32693289572051 | [NPY](tensors/0001832.npy) |
| 1911 | `model.layers.11` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -400.0 / 552.0 / 0.5526769002278645 / 21.929794940597517 | [NPY](tensors/0001911.npy) |
| 1912 | `model.layers.11` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 303] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001912.npy) |
| 1913 | `model.layers.11` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.707061767578125 / 0.9717983302810768 | [NPY](tensors/0001913.npy) |
| 1914 | `model.layers.11` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.234375 / 0.05849510431289673 / 0.601804974311013 | [NPY](tensors/0001914.npy) |
| 1915 | `model.layers.11` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 302.0 / 302.0 / 302.0 / 0.0 | [NPY](tensors/0001915.npy) |
| 1916 | `model.layers.11` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1917 | `model.layers.11` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1918 | `model.layers.11` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1919 | `model.layers.11.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -400.0 / 552.0 / 0.5526769002278645 / 21.929794940597517 | [NPY](tensors/0001919.npy) |
| 1920 | `model.layers.11.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.5 / 118.0 / 0.05797008408440484 / 3.4011132234498445 | [NPY](tensors/0001920.npy) |
| 1921 | `model.layers.11.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.5 / 118.0 / 0.05797008408440484 / 3.4011132234498445 | [NPY](tensors/0001921.npy) |
| 1922 | `model.layers.11.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 303] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001922.npy) |
| 1923 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 302.0 / 302.0 / 302.0 / 0.0 | [NPY](tensors/0001923.npy) |
| 1924 | `model.layers.11.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1925 | `model.layers.11.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1926 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.707061767578125 / 0.9717983302810768 | [NPY](tensors/0001926.npy) |
| 1927 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.234375 / 0.05849510431289673 / 0.601804974311013 | [NPY](tensors/0001927.npy) |
| 1928 | `model.layers.11.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1929 | `model.layers.11.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.5 / 118.0 / 0.05797008408440484 / 3.4011132234498445 | [NPY](tensors/0001929.npy) |
| 1930 | `model.layers.11.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.84375 / 7.125 / 0.0337968363892287 / 1.1488675390780236 | [NPY](tensors/0001930.npy) |
| 1931 | `model.layers.11.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.5 / 118.0 / 0.05797008408440484 / 3.4011132234498445 | [NPY](tensors/0001931.npy) |
| 1932 | `model.layers.11.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.125 / 36.5 / 0.058487676084041595 / 3.577459207117371 | [NPY](tensors/0001932.npy) |
| 1933 | `model.layers.11.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.5 / 118.0 / 0.05797008408440484 / 3.4011132234498445 | [NPY](tensors/0001933.npy) |
| 1934 | `model.layers.11.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.4375 / 6.90625 / -0.046520233154296875 / 2.1234896142564947 | [NPY](tensors/0001934.npy) |
| 1935 | `model.layers.11.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 5.625 / 0.013294210482854396 / 1.2394356301641607 | [NPY](tensors/0001935.npy) |
| 1936 | `model.layers.11.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -220.0 / 172.0 / -0.1491270356708103 / 6.429581046586001 | [NPY](tensors/0001936.npy) |
| 1937 | `model.layers.11.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -220.0 / 172.0 / -0.1491270356708103 / 6.429581046586001 | [NPY](tensors/0001937.npy) |
| 1938 | `model.layers.11.self_attn` | 16 | `output[1]` | [1, 64, 1, 303] | torch.bfloat16 → float32 | 6.002665031701326e-11 / 0.96484375 / 0.0029769483806342412 / 0.016239433665354002 | [NPY](tensors/0001938.npy) |
| 1939 | `model.layers.11.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -228.0 / 352.0 / 0.4037268744574653 / 19.117252256362594 | [NPY](tensors/0001939.npy) |
| 1940 | `model.layers.11.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.3125 / 3.3125 / -0.00031962030463748506 / 0.7154068412444526 | [NPY](tensors/0001940.npy) |
| 1941 | `model.layers.11.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.3125 / 3.3125 / -0.00031962030463748506 / 0.7154068412444526 | [NPY](tensors/0001941.npy) |
| 1942 | `model.layers.11.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.3125 / 3.3125 / -0.00031962030463748506 / 0.7154068412444526 | [NPY](tensors/0001942.npy) |
| 1943 | `model.layers.11.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1944 | `model.layers.11.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1945 | `model.layers.11.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1946 | `model.layers.11.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -340.0 / 272.0 / -0.027531613243950738 / 11.604069457131546 | [NPY](tensors/0001946.npy) |
| 1947 | `model.layers.11.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -340.0 / 272.0 / -0.027531613243950738 / 11.604069457131546 | [NPY](tensors/0001947.npy) |
| 1948 | `model.layers.11.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.5 / 1.53125 / -0.11136627197265625 / 0.6184680369403209 | [NPY](tensors/0001948.npy) |
| 1949 | `model.layers.11` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -568.0 / 604.0 / 0.3763373480902778 / 27.419116889903034 | [NPY](tensors/0001949.npy) |
| 2028 | `model.layers.11` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -247.0 / 448.0 / 0.9093897501627605 / 19.020765048758676 | [NPY](tensors/0002028.npy) |
| 2029 | `model.layers.11` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 304] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002029.npy) |
| 2030 | `model.layers.11` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.68243408203125 / 0.9684034292887866 | [NPY](tensors/0002030.npy) |
| 2031 | `model.layers.11` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3359375 / 0.10489383339881897 / 0.6297841334602801 | [NPY](tensors/0002031.npy) |
| 2032 | `model.layers.11` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 303.0 / 303.0 / 303.0 / 0.0 | [NPY](tensors/0002032.npy) |
| 2033 | `model.layers.11` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2034 | `model.layers.11` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2035 | `model.layers.11` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2036 | `model.layers.11.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -247.0 / 448.0 / 0.9093897501627605 / 19.020765048758676 | [NPY](tensors/0002036.npy) |
| 2037 | `model.layers.11.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 110.5 / 0.11021049287584093 / 3.1374369755842575 | [NPY](tensors/0002037.npy) |
| 2038 | `model.layers.11.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 110.5 / 0.11021049287584093 / 3.1374369755842575 | [NPY](tensors/0002038.npy) |
| 2039 | `model.layers.11.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 304] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002039.npy) |
| 2040 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 303.0 / 303.0 / 303.0 / 0.0 | [NPY](tensors/0002040.npy) |
| 2041 | `model.layers.11.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2042 | `model.layers.11.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2043 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.68243408203125 / 0.9684034292887866 | [NPY](tensors/0002043.npy) |
| 2044 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3359375 / 0.10489383339881897 / 0.6297841334602801 | [NPY](tensors/0002044.npy) |
| 2045 | `model.layers.11.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2046 | `model.layers.11.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 110.5 / 0.11021049287584093 / 3.1374369755842575 | [NPY](tensors/0002046.npy) |
| 2047 | `model.layers.11.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.875 / 9.1875 / 0.05153378564864397 / 1.2793037047102271 | [NPY](tensors/0002047.npy) |
| 2048 | `model.layers.11.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 110.5 / 0.11021049287584093 / 3.1374369755842575 | [NPY](tensors/0002048.npy) |
| 2049 | `model.layers.11.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -26.25 / 33.0 / 0.10770268738269806 / 3.6744119807755418 | [NPY](tensors/0002049.npy) |
| 2050 | `model.layers.11.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 110.5 / 0.11021049287584093 / 3.1374369755842575 | [NPY](tensors/0002050.npy) |
| 2051 | `model.layers.11.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.8125 / 7.34375 / 0.10449650883674622 / 2.395104362162377 | [NPY](tensors/0002051.npy) |
| 2052 | `model.layers.11.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0 / 5.6875 / 0.02252088999375701 / 1.3386528080186932 | [NPY](tensors/0002052.npy) |
| 2053 | `model.layers.11.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 71.0 / -0.01147089269426134 / 3.965935391263669 | [NPY](tensors/0002053.npy) |
| 2054 | `model.layers.11.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 71.0 / -0.01147089269426134 / 3.965935391263669 | [NPY](tensors/0002054.npy) |
| 2055 | `model.layers.11.self_attn` | 17 | `output[1]` | [1, 64, 1, 304] | torch.bfloat16 → float32 | 3.115019353572279e-11 / 0.93359375 / 0.0030269906374916834 / 0.01580073976216578 | [NPY](tensors/0002055.npy) |
| 2056 | `model.layers.11.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -176.0 / 400.0 / 0.8987735324435764 / 19.136668948924395 | [NPY](tensors/0002056.npy) |
| 2057 | `model.layers.11.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5625 / 2.546875 / 0.03135338624318441 / 0.7431958111776181 | [NPY](tensors/0002057.npy) |
| 2058 | `model.layers.11.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5625 / 2.546875 / 0.03135338624318441 / 0.7431958111776181 | [NPY](tensors/0002058.npy) |
| 2059 | `model.layers.11.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.5625 / 2.546875 / 0.03135338624318441 / 0.7431958111776181 | [NPY](tensors/0002059.npy) |
| 2060 | `model.layers.11.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2061 | `model.layers.11.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2062 | `model.layers.11.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2063 | `model.layers.11.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -208.0 / 213.0 / 0.2717566993501451 / 8.23730831380057 | [NPY](tensors/0002063.npy) |
| 2064 | `model.layers.11.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -208.0 / 213.0 / 0.2717566993501451 / 8.23730831380057 | [NPY](tensors/0002064.npy) |
| 2065 | `model.layers.11.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.7265625 / 1.046875 / -0.036429405212402344 / 0.5683089087857423 | [NPY](tensors/0002065.npy) |
| 2066 | `model.layers.11` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -384.0 / 612.0 / 1.1697591145833333 / 24.614069997086947 | [NPY](tensors/0002066.npy) |
| 2145 | `model.layers.11` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -256.0 / 416.0 / 1.0356600443522135 / 21.064344964310173 | [NPY](tensors/0002145.npy) |
| 2146 | `model.layers.11` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 305] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002146.npy) |
| 2147 | `model.layers.11` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6405029296875 / 1.0356892994687845 | [NPY](tensors/0002147.npy) |
| 2148 | `model.layers.11` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1875 / 1.2421875 / 0.10542488098144531 / 0.5631099040524371 | [NPY](tensors/0002148.npy) |
| 2149 | `model.layers.11` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 304.0 / 304.0 / 304.0 / 0.0 | [NPY](tensors/0002149.npy) |
| 2150 | `model.layers.11` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2151 | `model.layers.11` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2152 | `model.layers.11` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2153 | `model.layers.11.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -256.0 / 416.0 / 1.0356600443522135 / 21.064344964310173 | [NPY](tensors/0002153.npy) |
| 2154 | `model.layers.11.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.75 / 92.5 / 0.11086054709222581 / 2.808345612264078 | [NPY](tensors/0002154.npy) |
| 2155 | `model.layers.11.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.75 / 92.5 / 0.11086054709222581 / 2.808345612264078 | [NPY](tensors/0002155.npy) |
| 2156 | `model.layers.11.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 305] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002156.npy) |
| 2157 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 304.0 / 304.0 / 304.0 / 0.0 | [NPY](tensors/0002157.npy) |
| 2158 | `model.layers.11.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2159 | `model.layers.11.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2160 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6405029296875 / 1.0356892994687845 | [NPY](tensors/0002160.npy) |
| 2161 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1875 / 1.2421875 / 0.10542488098144531 / 0.5631099040524371 | [NPY](tensors/0002161.npy) |
| 2162 | `model.layers.11.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2163 | `model.layers.11.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.75 / 92.5 / 0.11086054709222581 / 2.808345612264078 | [NPY](tensors/0002163.npy) |
| 2164 | `model.layers.11.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0 / 11.25 / 0.0402162407990545 / 1.3529144425390718 | [NPY](tensors/0002164.npy) |
| 2165 | `model.layers.11.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.75 / 92.5 / 0.11086054709222581 / 2.808345612264078 | [NPY](tensors/0002165.npy) |
| 2166 | `model.layers.11.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.75 / 34.75 / 0.029693961143493652 / 4.091191974126561 | [NPY](tensors/0002166.npy) |
| 2167 | `model.layers.11.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.75 / 92.5 / 0.11086054709222581 / 2.808345612264078 | [NPY](tensors/0002167.npy) |
| 2168 | `model.layers.11.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.125 / 10.375 / 0.1029435396194458 / 2.3870240724141705 | [NPY](tensors/0002168.npy) |
| 2169 | `model.layers.11.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5625 / 7.15625 / 0.010296856984496117 / 1.5313597022499392 | [NPY](tensors/0002169.npy) |
| 2170 | `model.layers.11.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.0 / 58.25 / 0.15755533642239042 / 3.991962623318311 | [NPY](tensors/0002170.npy) |
| 2171 | `model.layers.11.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.0 / 58.25 / 0.15755533642239042 / 3.991962623318311 | [NPY](tensors/0002171.npy) |
| 2172 | `model.layers.11.self_attn` | 18 | `output[1]` | [1, 64, 1, 305] | torch.bfloat16 → float32 | 5.911715561524034e-11 / 0.94921875 / 0.0030610831682442957 / 0.015052907296026078 | [NPY](tensors/0002172.npy) |
| 2173 | `model.layers.11.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -221.0 / 416.0 / 1.1928320990668402 / 22.227126515890642 | [NPY](tensors/0002173.npy) |
| 2174 | `model.layers.11.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.40625 / 4.25 / 0.03654041356510586 / 0.7650999891638756 | [NPY](tensors/0002174.npy) |
| 2175 | `model.layers.11.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.40625 / 4.25 / 0.03654041356510586 / 0.7650999891638756 | [NPY](tensors/0002175.npy) |
| 2176 | `model.layers.11.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.40625 / 4.25 / 0.03654041356510586 / 0.7650999891638756 | [NPY](tensors/0002176.npy) |
| 2177 | `model.layers.11.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2178 | `model.layers.11.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2179 | `model.layers.11.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2180 | `model.layers.11.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -200.0 / 210.0 / 0.1666984823015001 / 7.7937827084491165 | [NPY](tensors/0002180.npy) |
| 2181 | `model.layers.11.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -200.0 / 210.0 / 0.1666984823015001 / 7.7937827084491165 | [NPY](tensors/0002181.npy) |
| 2182 | `model.layers.11.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.7734375 / 1.3515625 / -0.10560798645019531 / 0.6856759100087731 | [NPY](tensors/0002182.npy) |
| 2183 | `model.layers.11` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -420.0 / 624.0 / 1.3589847140842013 / 26.953470362571434 | [NPY](tensors/0002183.npy) |
| 2262 | `model.layers.11` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -348.0 / 520.0 / 0.6690792507595487 / 22.709544223039423 | [NPY](tensors/0002262.npy) |
| 2263 | `model.layers.11` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 306] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002263.npy) |
| 2264 | `model.layers.11` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0002264.npy) |
| 2265 | `model.layers.11` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0002265.npy) |
| 2266 | `model.layers.11` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0002266.npy) |
| 2267 | `model.layers.11` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2268 | `model.layers.11` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2269 | `model.layers.11` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2270 | `model.layers.11.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -348.0 / 520.0 / 0.6690792507595487 / 22.709544223039423 | [NPY](tensors/0002270.npy) |
| 2271 | `model.layers.11.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.5 / 107.5 / 0.07101513875855339 / 3.091449969721937 | [NPY](tensors/0002271.npy) |
| 2272 | `model.layers.11.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.5 / 107.5 / 0.07101513875855339 / 3.091449969721937 | [NPY](tensors/0002272.npy) |
| 2273 | `model.layers.11.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 306] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002273.npy) |
| 2274 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0002274.npy) |
| 2275 | `model.layers.11.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2276 | `model.layers.11.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2277 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0002277.npy) |
| 2278 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0002278.npy) |
| 2279 | `model.layers.11.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2280 | `model.layers.11.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.5 / 107.5 / 0.07101513875855339 / 3.091449969721937 | [NPY](tensors/0002280.npy) |
| 2281 | `model.layers.11.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.34375 / 9.3125 / 0.020663161296397448 / 1.3324169048890968 | [NPY](tensors/0002281.npy) |
| 2282 | `model.layers.11.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.5 / 107.5 / 0.07101513875855339 / 3.091449969721937 | [NPY](tensors/0002282.npy) |
| 2283 | `model.layers.11.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 36.0 / -0.03084498643875122 / 4.00527701042327 | [NPY](tensors/0002283.npy) |
| 2284 | `model.layers.11.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.5 / 107.5 / 0.07101513875855339 / 3.091449969721937 | [NPY](tensors/0002284.npy) |
| 2285 | `model.layers.11.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.875 / 9.5 / 0.019033119082450867 / 2.2848314663686073 | [NPY](tensors/0002285.npy) |
| 2286 | `model.layers.11.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.375 / 6.5625 / 0.006757735856808722 / 1.493002151394808 | [NPY](tensors/0002286.npy) |
| 2287 | `model.layers.11.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.25 / 102.0 / 0.05355266034603119 / 4.614127027191571 | [NPY](tensors/0002287.npy) |
| 2288 | `model.layers.11.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.25 / 102.0 / 0.05355266034603119 / 4.614127027191571 | [NPY](tensors/0002288.npy) |
| 2289 | `model.layers.11.self_attn` | 19 | `output[1]` | [1, 64, 1, 306] | torch.bfloat16 → float32 | 3.865352482534945e-11 / 0.90234375 / 0.0029664141987420524 / 0.01661821273781094 | [NPY](tensors/0002289.npy) |
| 2290 | `model.layers.11.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -246.0 / 466.0 / 0.7223388671875 / 22.73297458793836 | [NPY](tensors/0002290.npy) |
| 2291 | `model.layers.11.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.5625 / 4.21875 / 0.010412847995758057 / 0.7500642250562957 | [NPY](tensors/0002291.npy) |
| 2292 | `model.layers.11.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.5625 / 4.21875 / 0.010412847995758057 / 0.7500642250562957 | [NPY](tensors/0002292.npy) |
| 2293 | `model.layers.11.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.5625 / 4.21875 / 0.010412847995758057 / 0.7500642250562957 | [NPY](tensors/0002293.npy) |
| 2294 | `model.layers.11.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2295 | `model.layers.11.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2296 | `model.layers.11.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2297 | `model.layers.11.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -194.0 / 231.0 / 0.15486618942684596 / 7.838758404909602 | [NPY](tensors/0002297.npy) |
| 2298 | `model.layers.11.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -194.0 / 231.0 / 0.15486618942684596 / 7.838758404909602 | [NPY](tensors/0002298.npy) |
| 2299 | `model.layers.11.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.53125 / 1.3984375 / -0.1783599853515625 / 0.7436734030290898 | [NPY](tensors/0002299.npy) |
| 2300 | `model.layers.11` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -440.0 / 696.0 / 0.8749415079752604 / 27.613508620502042 | [NPY](tensors/0002300.npy) |
| 2379 | `model.layers.11` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 528.0 / 0.7499701605902778 / 24.13131166788609 | [NPY](tensors/0002379.npy) |
| 2380 | `model.layers.11` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 307] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002380.npy) |
| 2381 | `model.layers.11` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0002381.npy) |
| 2382 | `model.layers.11` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0002382.npy) |
| 2383 | `model.layers.11` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0002383.npy) |
| 2384 | `model.layers.11` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2385 | `model.layers.11` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2386 | `model.layers.11` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2387 | `model.layers.11.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 528.0 / 0.7499701605902778 / 24.13131166788609 | [NPY](tensors/0002387.npy) |
| 2388 | `model.layers.11.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 102.5 / 0.07696695062849257 / 2.933837236083189 | [NPY](tensors/0002388.npy) |
| 2389 | `model.layers.11.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 102.5 / 0.07696695062849257 / 2.933837236083189 | [NPY](tensors/0002389.npy) |
| 2390 | `model.layers.11.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 307] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002390.npy) |
| 2391 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0002391.npy) |
| 2392 | `model.layers.11.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2393 | `model.layers.11.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2394 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0002394.npy) |
| 2395 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0002395.npy) |
| 2396 | `model.layers.11.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2397 | `model.layers.11.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 102.5 / 0.07696695062849257 / 2.933837236083189 | [NPY](tensors/0002397.npy) |
| 2398 | `model.layers.11.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.21875 / 9.1875 / 0.02410998585401103 / 1.4121303457198149 | [NPY](tensors/0002398.npy) |
| 2399 | `model.layers.11.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 102.5 / 0.07696695062849257 / 2.933837236083189 | [NPY](tensors/0002399.npy) |
| 2400 | `model.layers.11.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.25 / 34.5 / -0.0005460307002067566 / 3.9970598415275878 | [NPY](tensors/0002400.npy) |
| 2401 | `model.layers.11.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 102.5 / 0.07696695062849257 / 2.933837236083189 | [NPY](tensors/0002401.npy) |
| 2402 | `model.layers.11.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.59375 / 12.3125 / -0.10654586553573608 / 2.730511667974939 | [NPY](tensors/0002402.npy) |
| 2403 | `model.layers.11.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 8.625 / -0.011681223753839731 / 1.7374188104800263 | [NPY](tensors/0002403.npy) |
| 2404 | `model.layers.11.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 82.5 / 0.19998285240597194 / 4.8248454670235885 | [NPY](tensors/0002404.npy) |
| 2405 | `model.layers.11.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 82.5 / 0.19998285240597194 / 4.8248454670235885 | [NPY](tensors/0002405.npy) |
| 2406 | `model.layers.11.self_attn` | 20 | `output[1]` | [1, 64, 1, 307] | torch.bfloat16 → float32 | 2.6557245291769505e-10 / 0.9609375 / 0.0030236294519403613 / 0.019481443659037846 | [NPY](tensors/0002406.npy) |
| 2407 | `model.layers.11.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -274.0 / 524.0 / 0.949141099717882 / 25.2532072210686 | [NPY](tensors/0002407.npy) |
| 2408 | `model.layers.11.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.078125 / 3.84375 / 0.023044096099005804 / 0.7725907230827902 | [NPY](tensors/0002408.npy) |
| 2409 | `model.layers.11.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.078125 / 3.84375 / 0.023044096099005804 / 0.7725907230827902 | [NPY](tensors/0002409.npy) |
| 2410 | `model.layers.11.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.078125 / 3.84375 / 0.023044096099005804 / 0.7725907230827902 | [NPY](tensors/0002410.npy) |
| 2411 | `model.layers.11.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2412 | `model.layers.11.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2413 | `model.layers.11.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2414 | `model.layers.11.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -209.0 / 200.0 / 0.13345638049973382 / 8.510261413029392 | [NPY](tensors/0002414.npy) |
| 2415 | `model.layers.11.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -209.0 / 200.0 / 0.13345638049973382 / 8.510261413029392 | [NPY](tensors/0002415.npy) |
| 2416 | `model.layers.11.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.1875 / 1.0390625 / -0.1432037353515625 / 0.5591140669177492 | [NPY](tensors/0002416.npy) |
| 2417 | `model.layers.11` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -484.0 / 724.0 / 1.082222154405382 / 30.738746410748654 | [NPY](tensors/0002417.npy) |
| 2496 | `model.layers.11` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -126.0 / 360.0 / 0.8131493462456597 / 17.41119806024637 | [NPY](tensors/0002496.npy) |
| 2497 | `model.layers.11` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 308] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002497.npy) |
| 2498 | `model.layers.11` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0002498.npy) |
| 2499 | `model.layers.11` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0002499.npy) |
| 2500 | `model.layers.11` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0002500.npy) |
| 2501 | `model.layers.11` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2502 | `model.layers.11` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2503 | `model.layers.11` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2504 | `model.layers.11.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -126.0 / 360.0 / 0.8131493462456597 / 17.41119806024637 | [NPY](tensors/0002504.npy) |
| 2505 | `model.layers.11.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 97.0 / 0.11156994501749674 / 2.7974153467770133 | [NPY](tensors/0002505.npy) |
| 2506 | `model.layers.11.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 97.0 / 0.11156994501749674 / 2.7974153467770133 | [NPY](tensors/0002506.npy) |
| 2507 | `model.layers.11.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 308] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002507.npy) |
| 2508 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0002508.npy) |
| 2509 | `model.layers.11.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2510 | `model.layers.11.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2511 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0002511.npy) |
| 2512 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0002512.npy) |
| 2513 | `model.layers.11.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2514 | `model.layers.11.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 97.0 / 0.11156994501749674 / 2.7974153467770133 | [NPY](tensors/0002514.npy) |
| 2515 | `model.layers.11.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.3125 / 9.5625 / 0.04230353608727455 / 1.422106546368425 | [NPY](tensors/0002515.npy) |
| 2516 | `model.layers.11.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 97.0 / 0.11156994501749674 / 2.7974153467770133 | [NPY](tensors/0002516.npy) |
| 2517 | `model.layers.11.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.5 / 34.0 / 0.04216562211513519 / 4.244357922582589 | [NPY](tensors/0002517.npy) |
| 2518 | `model.layers.11.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 97.0 / 0.11156994501749674 / 2.7974153467770133 | [NPY](tensors/0002518.npy) |
| 2519 | `model.layers.11.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.9375 / 9.8125 / 0.11771249771118164 / 2.737989489849183 | [NPY](tensors/0002519.npy) |
| 2520 | `model.layers.11.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.625 / 7.625 / 0.012350651901215315 / 1.453422157108617 | [NPY](tensors/0002520.npy) |
| 2521 | `model.layers.11.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.0 / 122.0 / 0.15641518963707818 / 4.949177003162988 | [NPY](tensors/0002521.npy) |
| 2522 | `model.layers.11.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.0 / 122.0 / 0.15641518963707818 / 4.949177003162988 | [NPY](tensors/0002522.npy) |
| 2523 | `model.layers.11.self_attn` | 21 | `output[1]` | [1, 64, 1, 308] | torch.bfloat16 → float32 | 1.0186340659856796e-10 / 0.8125 / 0.0029724323630830624 / 0.014906428169602299 | [NPY](tensors/0002523.npy) |
| 2524 | `model.layers.11.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -191.0 / 456.0 / 0.9695014105902777 / 20.035633797227057 | [NPY](tensors/0002524.npy) |
| 2525 | `model.layers.11.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.28125 / 2.78125 / 0.0282068133354187 / 0.7470646239653507 | [NPY](tensors/0002525.npy) |
| 2526 | `model.layers.11.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.28125 / 2.78125 / 0.0282068133354187 / 0.7470646239653507 | [NPY](tensors/0002526.npy) |
| 2527 | `model.layers.11.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.28125 / 2.78125 / 0.0282068133354187 / 0.7470646239653507 | [NPY](tensors/0002527.npy) |
| 2528 | `model.layers.11.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2529 | `model.layers.11.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2530 | `model.layers.11.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2531 | `model.layers.11.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -115.0 / 79.5 / 0.059170985221862794 / 5.5421574950828845 | [NPY](tensors/0002531.npy) |
| 2532 | `model.layers.11.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -115.0 / 79.5 / 0.059170985221862794 / 5.5421574950828845 | [NPY](tensors/0002532.npy) |
| 2533 | `model.layers.11.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.421875 / 1.3515625 / -0.07550048828125 / 0.5940752025063415 | [NPY](tensors/0002533.npy) |
| 2534 | `model.layers.11` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -306.0 / 536.0 / 1.028151618109809 / 22.903315323143634 | [NPY](tensors/0002534.npy) |
| 2613 | `model.layers.11` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -284.0 / 440.0 / 0.47608710394965276 / 21.139408223616687 | [NPY](tensors/0002613.npy) |
| 2614 | `model.layers.11` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 309] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002614.npy) |
| 2615 | `model.layers.11` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0002615.npy) |
| 2616 | `model.layers.11` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0002616.npy) |
| 2617 | `model.layers.11` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0002617.npy) |
| 2618 | `model.layers.11` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2619 | `model.layers.11` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2620 | `model.layers.11` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2621 | `model.layers.11.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -284.0 / 440.0 / 0.47608710394965276 / 21.139408223616687 | [NPY](tensors/0002621.npy) |
| 2622 | `model.layers.11.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.5 / 97.5 / 0.06691883471277026 / 2.926024456919049 | [NPY](tensors/0002622.npy) |
| 2623 | `model.layers.11.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.5 / 97.5 / 0.06691883471277026 / 2.926024456919049 | [NPY](tensors/0002623.npy) |
| 2624 | `model.layers.11.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 309] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002624.npy) |
| 2625 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0002625.npy) |
| 2626 | `model.layers.11.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2627 | `model.layers.11.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2628 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0002628.npy) |
| 2629 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0002629.npy) |
| 2630 | `model.layers.11.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2631 | `model.layers.11.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.5 / 97.5 / 0.06691883471277026 / 2.926024456919049 | [NPY](tensors/0002631.npy) |
| 2632 | `model.layers.11.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.5625 / 8.875 / 0.015083335816598265 / 1.424982780434642 | [NPY](tensors/0002632.npy) |
| 2633 | `model.layers.11.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.5 / 97.5 / 0.06691883471277026 / 2.926024456919049 | [NPY](tensors/0002633.npy) |
| 2634 | `model.layers.11.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 33.75 / -0.0016642361879348755 / 4.1401710954460516 | [NPY](tensors/0002634.npy) |
| 2635 | `model.layers.11.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.5 / 97.5 / 0.06691883471277026 / 2.926024456919049 | [NPY](tensors/0002635.npy) |
| 2636 | `model.layers.11.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.78125 / 10.0 / 0.0009774267673492432 / 2.616083503494685 | [NPY](tensors/0002636.npy) |
| 2637 | `model.layers.11.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.25 / 8.25 / -0.002402682846877724 / 1.9261227669824894 | [NPY](tensors/0002637.npy) |
| 2638 | `model.layers.11.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 150.0 / 0.06953958935207791 / 5.47446157544591 | [NPY](tensors/0002638.npy) |
| 2639 | `model.layers.11.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 150.0 / 0.06953958935207791 / 5.47446157544591 | [NPY](tensors/0002639.npy) |
| 2640 | `model.layers.11.self_attn` | 22 | `output[1]` | [1, 64, 1, 309] | torch.bfloat16 → float32 | 9.208633855450898e-12 / 0.9375 / 0.003037066078282941 / 0.019071129168728936 | [NPY](tensors/0002640.npy) |
| 2641 | `model.layers.11.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -276.0 / 410.0 / 0.5456943088107639 / 23.108721296783703 | [NPY](tensors/0002641.npy) |
| 2642 | `model.layers.11.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.375 / 4.34375 / 0.013962381415896945 / 0.7596825390165644 | [NPY](tensors/0002642.npy) |
| 2643 | `model.layers.11.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.375 / 4.34375 / 0.013962381415896945 / 0.7596825390165644 | [NPY](tensors/0002643.npy) |
| 2644 | `model.layers.11.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.375 / 4.34375 / 0.013962381415896945 / 0.7596825390165644 | [NPY](tensors/0002644.npy) |
| 2645 | `model.layers.11.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2646 | `model.layers.11.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2647 | `model.layers.11.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2648 | `model.layers.11.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -231.0 / 223.0 / 0.059170907735824584 / 7.832970416920556 | [NPY](tensors/0002648.npy) |
| 2649 | `model.layers.11.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -231.0 / 223.0 / 0.059170907735824584 / 7.832970416920556 | [NPY](tensors/0002649.npy) |
| 2650 | `model.layers.11.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.296875 / 1.046875 / -0.127593994140625 / 0.5857360676391361 | [NPY](tensors/0002650.npy) |
| 2651 | `model.layers.11` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -508.0 / 632.0 / 0.6025056627061632 / 27.934445955957347 | [NPY](tensors/0002651.npy) |
| 2730 | `model.layers.11` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -356.0 / 482.0 / 0.42439507378472224 / 22.67668484668805 | [NPY](tensors/0002730.npy) |
| 2731 | `model.layers.11` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 310] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002731.npy) |
| 2732 | `model.layers.11` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0002732.npy) |
| 2733 | `model.layers.11` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0002733.npy) |
| 2734 | `model.layers.11` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0002734.npy) |
| 2735 | `model.layers.11` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2736 | `model.layers.11` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2737 | `model.layers.11` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2738 | `model.layers.11.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -356.0 / 482.0 / 0.42439507378472224 / 22.67668484668805 | [NPY](tensors/0002738.npy) |
| 2739 | `model.layers.11.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 99.5 / 0.05822423564063178 / 3.0227650700163857 | [NPY](tensors/0002739.npy) |
| 2740 | `model.layers.11.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 99.5 / 0.05822423564063178 / 3.0227650700163857 | [NPY](tensors/0002740.npy) |
| 2741 | `model.layers.11.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 310] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002741.npy) |
| 2742 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0002742.npy) |
| 2743 | `model.layers.11.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2744 | `model.layers.11.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2745 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0002745.npy) |
| 2746 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0002746.npy) |
| 2747 | `model.layers.11.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2748 | `model.layers.11.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 99.5 / 0.05822423564063178 / 3.0227650700163857 | [NPY](tensors/0002748.npy) |
| 2749 | `model.layers.11.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.3125 / 8.6875 / 0.017549520824104548 / 1.3785866951439816 | [NPY](tensors/0002749.npy) |
| 2750 | `model.layers.11.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 99.5 / 0.05822423564063178 / 3.0227650700163857 | [NPY](tensors/0002750.npy) |
| 2751 | `model.layers.11.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.25 / 35.5 / -0.013891831040382385 / 4.0988242888719535 | [NPY](tensors/0002751.npy) |
| 2752 | `model.layers.11.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 99.5 / 0.05822423564063178 / 3.0227650700163857 | [NPY](tensors/0002752.npy) |
| 2753 | `model.layers.11.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -10.125 / 8.875 / 0.08616174757480621 / 2.8945797876180697 | [NPY](tensors/0002753.npy) |
| 2754 | `model.layers.11.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.875 / 8.6875 / 0.005693092942237854 / 1.8569724752832564 | [NPY](tensors/0002754.npy) |
| 2755 | `model.layers.11.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 111.5 / 0.04014585812886556 / 5.247976430489691 | [NPY](tensors/0002755.npy) |
| 2756 | `model.layers.11.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 111.5 / 0.04014585812886556 / 5.247976430489691 | [NPY](tensors/0002756.npy) |
| 2757 | `model.layers.11.self_attn` | 23 | `output[1]` | [1, 64, 1, 310] | torch.bfloat16 → float32 | 2.114575181622058e-11 / 0.8984375 / 0.0030000644619286917 / 0.017577524421590118 | [NPY](tensors/0002757.npy) |
| 2758 | `model.layers.11.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -316.0 / 438.0 / 0.4656551784939236 / 23.845440819199595 | [NPY](tensors/0002758.npy) |
| 2759 | `model.layers.11.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.625 / 3.5625 / 0.013426529036627876 / 0.7972495018175367 | [NPY](tensors/0002759.npy) |
| 2760 | `model.layers.11.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.625 / 3.5625 / 0.013426529036627876 / 0.7972495018175367 | [NPY](tensors/0002760.npy) |
| 2761 | `model.layers.11.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.625 / 3.5625 / 0.013426529036627876 / 0.7972495018175367 | [NPY](tensors/0002761.npy) |
| 2762 | `model.layers.11.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2763 | `model.layers.11.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2764 | `model.layers.11.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2765 | `model.layers.11.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -225.0 / 241.0 / 0.0969157165951199 / 8.610545990786068 | [NPY](tensors/0002765.npy) |
| 2766 | `model.layers.11.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -225.0 / 241.0 / 0.0969157165951199 / 8.610545990786068 | [NPY](tensors/0002766.npy) |
| 2767 | `model.layers.11.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.890625 / 1.0859375 / -0.10422515869140625 / 0.6036136182201027 | [NPY](tensors/0002767.npy) |
| 2768 | `model.layers.11` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -540.0 / 680.0 / 0.5619264390733507 / 29.28528558589523 | [NPY](tensors/0002768.npy) |
| 2847 | `model.layers.11` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -352.0 / 470.0 / 0.18751695421006945 / 22.594229875825945 | [NPY](tensors/0002847.npy) |
| 2848 | `model.layers.11` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 311] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002848.npy) |
| 2849 | `model.layers.11` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0002849.npy) |
| 2850 | `model.layers.11` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0002850.npy) |
| 2851 | `model.layers.11` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0002851.npy) |
| 2852 | `model.layers.11` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2853 | `model.layers.11` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2854 | `model.layers.11` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2855 | `model.layers.11.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -352.0 / 470.0 / 0.18751695421006945 / 22.594229875825945 | [NPY](tensors/0002855.npy) |
| 2856 | `model.layers.11.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 97.5 / 0.04260555770662096 / 2.9832194274244466 | [NPY](tensors/0002856.npy) |
| 2857 | `model.layers.11.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 97.5 / 0.04260555770662096 / 2.9832194274244466 | [NPY](tensors/0002857.npy) |
| 2858 | `model.layers.11.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 311] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002858.npy) |
| 2859 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0002859.npy) |
| 2860 | `model.layers.11.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2861 | `model.layers.11.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2862 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0002862.npy) |
| 2863 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0002863.npy) |
| 2864 | `model.layers.11.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2865 | `model.layers.11.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 97.5 / 0.04260555770662096 / 2.9832194274244466 | [NPY](tensors/0002865.npy) |
| 2866 | `model.layers.11.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.1875 / 9.3125 / 0.015795286279171705 / 1.2943340289411807 | [NPY](tensors/0002866.npy) |
| 2867 | `model.layers.11.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 97.5 / 0.04260555770662096 / 2.9832194274244466 | [NPY](tensors/0002867.npy) |
| 2868 | `model.layers.11.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.875 / 35.0 / 0.07183724641799927 / 3.6795695792460914 | [NPY](tensors/0002868.npy) |
| 2869 | `model.layers.11.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 97.5 / 0.04260555770662096 / 2.9832194274244466 | [NPY](tensors/0002869.npy) |
| 2870 | `model.layers.11.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.0625 / 6.96875 / 0.03686562180519104 / 2.271843372580716 | [NPY](tensors/0002870.npy) |
| 2871 | `model.layers.11.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.59375 / 7.40625 / -0.0036868711467832327 / 1.6583585947910373 | [NPY](tensors/0002871.npy) |
| 2872 | `model.layers.11.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 77.0 / 0.0585626482963562 / 4.190964463786845 | [NPY](tensors/0002872.npy) |
| 2873 | `model.layers.11.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 77.0 / 0.0585626482963562 / 4.190964463786845 | [NPY](tensors/0002873.npy) |
| 2874 | `model.layers.11.self_attn` | 24 | `output[1]` | [1, 64, 1, 311] | torch.bfloat16 → float32 | 1.191438059322536e-10 / 0.90625 / 0.0030341818397279664 / 0.01172580581209612 | [NPY](tensors/0002874.npy) |
| 2875 | `model.layers.11.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -304.0 / 424.0 / 0.24745025634765624 / 23.21072672321847 | [NPY](tensors/0002875.npy) |
| 2876 | `model.layers.11.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.921875 / 5.15625 / -0.0014039172066582573 / 0.7877309173170598 | [NPY](tensors/0002876.npy) |
| 2877 | `model.layers.11.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.921875 / 5.15625 / -0.0014039172066582573 / 0.7877309173170598 | [NPY](tensors/0002877.npy) |
| 2878 | `model.layers.11.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.921875 / 5.15625 / -0.0014039172066582573 / 0.7877309173170598 | [NPY](tensors/0002878.npy) |
| 2879 | `model.layers.11.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2880 | `model.layers.11.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2881 | `model.layers.11.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2882 | `model.layers.11.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -166.0 / 117.0 / -0.007637161678738064 / 6.421829759579655 | [NPY](tensors/0002882.npy) |
| 2883 | `model.layers.11.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -166.0 / 117.0 / -0.007637161678738064 / 6.421829759579655 | [NPY](tensors/0002883.npy) |
| 2884 | `model.layers.11.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.375 / 1.171875 / -0.09514617919921875 / 0.5738310615640182 | [NPY](tensors/0002884.npy) |
| 2885 | `model.layers.11` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -470.0 / 540.0 / 0.23954942491319445 / 26.871813559596518 | [NPY](tensors/0002885.npy) |
| 2964 | `model.layers.11` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -422.0 / 612.0 / 0.09694790310329861 / 24.504245250651287 | [NPY](tensors/0002964.npy) |
| 2965 | `model.layers.11` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 312] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002965.npy) |
| 2966 | `model.layers.11` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0002966.npy) |
| 2967 | `model.layers.11` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0002967.npy) |
| 2968 | `model.layers.11` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0002968.npy) |
| 2969 | `model.layers.11` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2970 | `model.layers.11` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2971 | `model.layers.11` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2972 | `model.layers.11.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -422.0 / 612.0 / 0.09694790310329861 / 24.504245250651287 | [NPY](tensors/0002972.npy) |
| 2973 | `model.layers.11.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 117.0 / 0.036635410785675046 / 3.238945662032511 | [NPY](tensors/0002973.npy) |
| 2974 | `model.layers.11.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 117.0 / 0.036635410785675046 / 3.238945662032511 | [NPY](tensors/0002974.npy) |
| 2975 | `model.layers.11.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 312] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002975.npy) |
| 2976 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0002976.npy) |
| 2977 | `model.layers.11.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2978 | `model.layers.11.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2979 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0002979.npy) |
| 2980 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0002980.npy) |
| 2981 | `model.layers.11.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2982 | `model.layers.11.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 117.0 / 0.036635410785675046 / 3.238945662032511 | [NPY](tensors/0002982.npy) |
| 2983 | `model.layers.11.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.53125 / 8.5 / 0.006312571349553764 / 1.3159167790150197 | [NPY](tensors/0002983.npy) |
| 2984 | `model.layers.11.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 117.0 / 0.036635410785675046 / 3.238945662032511 | [NPY](tensors/0002984.npy) |
| 2985 | `model.layers.11.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.25 / 30.875 / 0.016723990440368652 / 3.3143124479827764 | [NPY](tensors/0002985.npy) |
| 2986 | `model.layers.11.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 117.0 / 0.036635410785675046 / 3.238945662032511 | [NPY](tensors/0002986.npy) |
| 2987 | `model.layers.11.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.03125 / 8.875 / 0.01279708743095398 / 2.4190945604452954 | [NPY](tensors/0002987.npy) |
| 2988 | `model.layers.11.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.71875 / 8.6875 / -0.01363822491839528 / 1.5554439002368834 | [NPY](tensors/0002988.npy) |
| 2989 | `model.layers.11.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -190.0 / 179.0 / -0.036148534880744085 / 6.015094199804257 | [NPY](tensors/0002989.npy) |
| 2990 | `model.layers.11.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -190.0 / 179.0 / -0.036148534880744085 / 6.015094199804257 | [NPY](tensors/0002990.npy) |
| 2991 | `model.layers.11.self_attn` | 25 | `output[1]` | [1, 64, 1, 312] | torch.bfloat16 → float32 | 6.111804395914078e-10 / 0.90625 / 0.002747614997547615 / 0.013902230672749042 | [NPY](tensors/0002991.npy) |
| 2992 | `model.layers.11.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -243.0 / 422.0 / 0.06075414021809896 / 22.12558296485229 | [NPY](tensors/0002992.npy) |
| 2993 | `model.layers.11.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.84375 / 4.53125 / -0.010586015714539421 / 0.8054014709050982 | [NPY](tensors/0002993.npy) |
| 2994 | `model.layers.11.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.84375 / 4.53125 / -0.010586015714539421 / 0.8054014709050982 | [NPY](tensors/0002994.npy) |
| 2995 | `model.layers.11.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.84375 / 4.53125 / -0.010586015714539421 / 0.8054014709050982 | [NPY](tensors/0002995.npy) |
| 2996 | `model.layers.11.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2997 | `model.layers.11.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2998 | `model.layers.11.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2999 | `model.layers.11.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -282.0 / 190.0 / 0.029454035229153103 / 8.414162425438697 | [NPY](tensors/0002999.npy) |
| 3000 | `model.layers.11.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -282.0 / 190.0 / 0.029454035229153103 / 8.414162425438697 | [NPY](tensors/0003000.npy) |
| 3001 | `model.layers.11.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.09375 / 1.3359375 / -0.20314311981201172 / 0.7611639844874855 | [NPY](tensors/0003001.npy) |
| 3002 | `model.layers.11` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -524.0 / 612.0 / 0.08997328016493056 / 27.078068672594924 | [NPY](tensors/0003002.npy) |
| 3081 | `model.layers.11` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -356.0 / 576.0 / 0.3685082329644097 / 22.753204800115224 | [NPY](tensors/0003081.npy) |
| 3082 | `model.layers.11` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 313] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003082.npy) |
| 3083 | `model.layers.11` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0003083.npy) |
| 3084 | `model.layers.11` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0003084.npy) |
| 3085 | `model.layers.11` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0003085.npy) |
| 3086 | `model.layers.11` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3087 | `model.layers.11` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3088 | `model.layers.11` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3089 | `model.layers.11.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -356.0 / 576.0 / 0.3685082329644097 / 22.753204800115224 | [NPY](tensors/0003089.npy) |
| 3090 | `model.layers.11.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 118.5 / 0.05678126811981201 / 3.2708259175031134 | [NPY](tensors/0003090.npy) |
| 3091 | `model.layers.11.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 118.5 / 0.05678126811981201 / 3.2708259175031134 | [NPY](tensors/0003091.npy) |
| 3092 | `model.layers.11.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 313] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003092.npy) |
| 3093 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0003093.npy) |
| 3094 | `model.layers.11.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3095 | `model.layers.11.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3096 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0003096.npy) |
| 3097 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0003097.npy) |
| 3098 | `model.layers.11.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3099 | `model.layers.11.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 118.5 / 0.05678126811981201 / 3.2708259175031134 | [NPY](tensors/0003099.npy) |
| 3100 | `model.layers.11.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.78125 / 10.125 / 0.020443782093934715 / 1.3465209672745184 | [NPY](tensors/0003100.npy) |
| 3101 | `model.layers.11.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 118.5 / 0.05678126811981201 / 3.2708259175031134 | [NPY](tensors/0003101.npy) |
| 3102 | `model.layers.11.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -26.25 / 33.25 / -0.005395054817199707 / 3.753720089543339 | [NPY](tensors/0003102.npy) |
| 3103 | `model.layers.11.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 118.5 / 0.05678126811981201 / 3.2708259175031134 | [NPY](tensors/0003103.npy) |
| 3104 | `model.layers.11.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.5625 / 8.625 / 0.12179994583129883 / 2.581322835005214 | [NPY](tensors/0003104.npy) |
| 3105 | `model.layers.11.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.3125 / 7.40625 / 0.014232149347662926 / 1.55853809387001 | [NPY](tensors/0003105.npy) |
| 3106 | `model.layers.11.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -144.0 / 94.0 / -0.009806874063279894 / 4.827462267968073 | [NPY](tensors/0003106.npy) |
| 3107 | `model.layers.11.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -144.0 / 94.0 / -0.009806874063279894 / 4.827462267968073 | [NPY](tensors/0003107.npy) |
| 3108 | `model.layers.11.self_attn` | 26 | `output[1]` | [1, 64, 1, 313] | torch.bfloat16 → float32 | 9.038103598868474e-12 / 0.9453125 / 0.002956323933728232 / 0.01423432597990454 | [NPY](tensors/0003108.npy) |
| 3109 | `model.layers.11.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -262.0 / 432.0 / 0.35817175971137155 / 21.724902133573362 | [NPY](tensors/0003109.npy) |
| 3110 | `model.layers.11.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.15625 / 3.296875 / 0.008471612135569255 / 0.7355699889873857 | [NPY](tensors/0003110.npy) |
| 3111 | `model.layers.11.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.15625 / 3.296875 / 0.008471612135569255 / 0.7355699889873857 | [NPY](tensors/0003111.npy) |
| 3112 | `model.layers.11.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.15625 / 3.296875 / 0.008471612135569255 / 0.7355699889873857 | [NPY](tensors/0003112.npy) |
| 3113 | `model.layers.11.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3114 | `model.layers.11.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3115 | `model.layers.11.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3116 | `model.layers.11.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -244.0 / 178.0 / 0.09004235797458225 / 8.41193087411574 | [NPY](tensors/0003116.npy) |
| 3117 | `model.layers.11.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -244.0 / 178.0 / 0.09004235797458225 / 8.41193087411574 | [NPY](tensors/0003117.npy) |
| 3118 | `model.layers.11.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.90625 / 1.453125 / -0.17917585372924805 / 0.8232392303741368 | [NPY](tensors/0003118.npy) |
| 3119 | `model.layers.11` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -506.0 / 608.0 / 0.44669664171006945 / 27.044152027581983 | [NPY](tensors/0003119.npy) |
| 3198 | `model.layers.11` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -410.0 / 608.0 / 0.5932305230034722 / 24.232895600372267 | [NPY](tensors/0003198.npy) |
| 3199 | `model.layers.11` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 314] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003199.npy) |
| 3200 | `model.layers.11` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0003200.npy) |
| 3201 | `model.layers.11` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0003201.npy) |
| 3202 | `model.layers.11` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0003202.npy) |
| 3203 | `model.layers.11` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3204 | `model.layers.11` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3205 | `model.layers.11` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3206 | `model.layers.11.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -410.0 / 608.0 / 0.5932305230034722 / 24.232895600372267 | [NPY](tensors/0003206.npy) |
| 3207 | `model.layers.11.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.0 / 117.5 / 0.07251637511783177 / 3.3144912420836112 | [NPY](tensors/0003207.npy) |
| 3208 | `model.layers.11.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.0 / 117.5 / 0.07251637511783177 / 3.3144912420836112 | [NPY](tensors/0003208.npy) |
| 3209 | `model.layers.11.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 314] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003209.npy) |
| 3210 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0003210.npy) |
| 3211 | `model.layers.11.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3212 | `model.layers.11.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3213 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0003213.npy) |
| 3214 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0003214.npy) |
| 3215 | `model.layers.11.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3216 | `model.layers.11.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.0 / 117.5 / 0.07251637511783177 / 3.3144912420836112 | [NPY](tensors/0003216.npy) |
| 3217 | `model.layers.11.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.5625 / 8.875 / 0.016882935538887978 / 1.3522572506680273 | [NPY](tensors/0003217.npy) |
| 3218 | `model.layers.11.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.0 / 117.5 / 0.07251637511783177 / 3.3144912420836112 | [NPY](tensors/0003218.npy) |
| 3219 | `model.layers.11.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.5 / 36.75 / 0.024234562646597624 / 3.8164927742973465 | [NPY](tensors/0003219.npy) |
| 3220 | `model.layers.11.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.0 / 117.5 / 0.07251637511783177 / 3.3144912420836112 | [NPY](tensors/0003220.npy) |
| 3221 | `model.layers.11.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.0625 / 10.5625 / 0.07401818037033081 / 2.6179941235026383 | [NPY](tensors/0003221.npy) |
| 3222 | `model.layers.11.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.28125 / 6.875 / 0.022705573588609695 / 1.5649569017477936 | [NPY](tensors/0003222.npy) |
| 3223 | `model.layers.11.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -135.0 / 98.0 / 0.019136643409729003 / 4.876919902508564 | [NPY](tensors/0003223.npy) |
| 3224 | `model.layers.11.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -135.0 / 98.0 / 0.019136643409729003 / 4.876919902508564 | [NPY](tensors/0003224.npy) |
| 3225 | `model.layers.11.self_attn` | 27 | `output[1]` | [1, 64, 1, 314] | torch.bfloat16 → float32 | 3.115019353572279e-11 / 0.93359375 / 0.0028377567426256228 / 0.015079984235868224 | [NPY](tensors/0003225.npy) |
| 3226 | `model.layers.11.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 472.0 / 0.6127392239040799 / 23.64481127583813 | [NPY](tensors/0003226.npy) |
| 3227 | `model.layers.11.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.390625 / 2.890625 / 0.01622261603673299 / 0.7382572737914904 | [NPY](tensors/0003227.npy) |
| 3228 | `model.layers.11.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.390625 / 2.890625 / 0.01622261603673299 / 0.7382572737914904 | [NPY](tensors/0003228.npy) |
| 3229 | `model.layers.11.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.390625 / 2.890625 / 0.01622261603673299 / 0.7382572737914904 | [NPY](tensors/0003229.npy) |
| 3230 | `model.layers.11.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3231 | `model.layers.11.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3232 | `model.layers.11.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3233 | `model.layers.11.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -235.0 / 209.0 / 0.1142356342739529 / 8.347037482359188 | [NPY](tensors/0003233.npy) |
| 3234 | `model.layers.11.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -235.0 / 209.0 / 0.1142356342739529 / 8.347037482359188 | [NPY](tensors/0003234.npy) |
| 3235 | `model.layers.11.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.609375 / 1.234375 / -0.14483016729354858 / 0.7856455392767078 | [NPY](tensors/0003235.npy) |
| 3236 | `model.layers.11` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -548.0 / 680.0 / 0.727167256673177 / 29.074969541381776 | [NPY](tensors/0003236.npy) |
| 3315 | `model.layers.11` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -366.0 / 448.0 / 0.5278656005859375 / 22.187185736734897 | [NPY](tensors/0003315.npy) |
| 3316 | `model.layers.11` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 315] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003316.npy) |
| 3317 | `model.layers.11` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0003317.npy) |
| 3318 | `model.layers.11` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0003318.npy) |
| 3319 | `model.layers.11` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0003319.npy) |
| 3320 | `model.layers.11` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3321 | `model.layers.11` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3322 | `model.layers.11` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3323 | `model.layers.11.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -366.0 / 448.0 / 0.5278656005859375 / 22.187185736734897 | [NPY](tensors/0003323.npy) |
| 3324 | `model.layers.11.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 94.5 / 0.0614512840906779 / 3.038045474406962 | [NPY](tensors/0003324.npy) |
| 3325 | `model.layers.11.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 94.5 / 0.0614512840906779 / 3.038045474406962 | [NPY](tensors/0003325.npy) |
| 3326 | `model.layers.11.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 315] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003326.npy) |
| 3327 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0003327.npy) |
| 3328 | `model.layers.11.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3329 | `model.layers.11.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3330 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0003330.npy) |
| 3331 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0003331.npy) |
| 3332 | `model.layers.11.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3333 | `model.layers.11.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 94.5 / 0.0614512840906779 / 3.038045474406962 | [NPY](tensors/0003333.npy) |
| 3334 | `model.layers.11.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.5625 / 7.96875 / 0.004593114135786891 / 1.3925096831915313 | [NPY](tensors/0003334.npy) |
| 3335 | `model.layers.11.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 94.5 / 0.0614512840906779 / 3.038045474406962 | [NPY](tensors/0003335.npy) |
| 3336 | `model.layers.11.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -26.5 / 34.75 / 0.014731794595718384 / 3.6222510941449664 | [NPY](tensors/0003336.npy) |
| 3337 | `model.layers.11.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 94.5 / 0.0614512840906779 / 3.038045474406962 | [NPY](tensors/0003337.npy) |
| 3338 | `model.layers.11.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.9375 / 7.03125 / -0.1877281665802002 / 2.4342743795308786 | [NPY](tensors/0003338.npy) |
| 3339 | `model.layers.11.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.0625 / -0.03757065813988447 / 1.4864021859429564 | [NPY](tensors/0003339.npy) |
| 3340 | `model.layers.11.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -113.5 / 116.0 / 0.012188869052463108 / 4.563615217084607 | [NPY](tensors/0003340.npy) |
| 3341 | `model.layers.11.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -113.5 / 116.0 / 0.012188869052463108 / 4.563615217084607 | [NPY](tensors/0003341.npy) |
| 3342 | `model.layers.11.self_attn` | 28 | `output[1]` | [1, 64, 1, 315] | torch.bfloat16 → float32 | 2.2737367544323206e-12 / 0.94140625 / 0.0025194736202272514 / 0.01662856548031637 | [NPY](tensors/0003342.npy) |
| 3343 | `model.layers.11.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -250.0 / 334.0 / 0.538853030734592 / 21.422905348393016 | [NPY](tensors/0003343.npy) |
| 3344 | `model.layers.11.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.953125 / 3.71875 / 0.011476129955715604 / 0.7874556492436171 | [NPY](tensors/0003344.npy) |
| 3345 | `model.layers.11.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.953125 / 3.71875 / 0.011476129955715604 / 0.7874556492436171 | [NPY](tensors/0003345.npy) |
| 3346 | `model.layers.11.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.953125 / 3.71875 / 0.011476129955715604 / 0.7874556492436171 | [NPY](tensors/0003346.npy) |
| 3347 | `model.layers.11.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3348 | `model.layers.11.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3349 | `model.layers.11.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3350 | `model.layers.11.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -230.0 / 256.0 / 0.1204857137468126 / 9.076577781940655 | [NPY](tensors/0003350.npy) |
| 3351 | `model.layers.11.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -230.0 / 256.0 / 0.1204857137468126 / 9.076577781940655 | [NPY](tensors/0003351.npy) |
| 3352 | `model.layers.11.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.34375 / 1.578125 / -0.169586181640625 / 0.8275182177799653 | [NPY](tensors/0003352.npy) |
| 3353 | `model.layers.11` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -480.0 / 592.0 / 0.6604888916015625 / 27.037881929524843 | [NPY](tensors/0003353.npy) |
| 3432 | `model.layers.11` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -250.0 / 412.0 / 0.5917471991644965 / 19.959858059245757 | [NPY](tensors/0003432.npy) |
| 3433 | `model.layers.11` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 316] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003433.npy) |
| 3434 | `model.layers.11` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0003434.npy) |
| 3435 | `model.layers.11` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0003435.npy) |
| 3436 | `model.layers.11` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0003436.npy) |
| 3437 | `model.layers.11` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3438 | `model.layers.11` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3439 | `model.layers.11` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3440 | `model.layers.11.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -250.0 / 412.0 / 0.5917471991644965 / 19.959858059245757 | [NPY](tensors/0003440.npy) |
| 3441 | `model.layers.11.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 96.5 / 0.08086290094587538 / 2.92509061617858 | [NPY](tensors/0003441.npy) |
| 3442 | `model.layers.11.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 96.5 / 0.08086290094587538 / 2.92509061617858 | [NPY](tensors/0003442.npy) |
| 3443 | `model.layers.11.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 316] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003443.npy) |
| 3444 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0003444.npy) |
| 3445 | `model.layers.11.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3446 | `model.layers.11.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3447 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0003447.npy) |
| 3448 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0003448.npy) |
| 3449 | `model.layers.11.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3450 | `model.layers.11.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 96.5 / 0.08086290094587538 / 2.92509061617858 | [NPY](tensors/0003450.npy) |
| 3451 | `model.layers.11.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.96875 / 9.75 / 0.034949255641549826 / 1.413183275747906 | [NPY](tensors/0003451.npy) |
| 3452 | `model.layers.11.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 96.5 / 0.08086290094587538 / 2.92509061617858 | [NPY](tensors/0003452.npy) |
| 3453 | `model.layers.11.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.0 / 37.25 / 0.05356781184673309 / 4.091284041179467 | [NPY](tensors/0003453.npy) |
| 3454 | `model.layers.11.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 96.5 / 0.08086290094587538 / 2.92509061617858 | [NPY](tensors/0003454.npy) |
| 3455 | `model.layers.11.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.90625 / 9.375 / 0.05826050043106079 / 2.481736848112611 | [NPY](tensors/0003455.npy) |
| 3456 | `model.layers.11.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 7.71875 / 0.024994679959490895 / 1.6209427042721098 | [NPY](tensors/0003456.npy) |
| 3457 | `model.layers.11.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 62.75 / 0.05894319746229384 / 4.222910548642352 | [NPY](tensors/0003457.npy) |
| 3458 | `model.layers.11.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 62.75 / 0.05894319746229384 / 4.222910548642352 | [NPY](tensors/0003458.npy) |
| 3459 | `model.layers.11.self_attn` | 29 | `output[1]` | [1, 64, 1, 316] | torch.bfloat16 → float32 | 2.2168933355715126e-11 / 0.96875 / 0.002927676782818929 / 0.016169264913937366 | [NPY](tensors/0003459.npy) |
| 3460 | `model.layers.11.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -187.0 / 376.0 / 0.6516128540039062 / 20.796396044761586 | [NPY](tensors/0003460.npy) |
| 3461 | `model.layers.11.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.5 / 3.390625 / 0.01278418434990777 / 0.766280973264347 | [NPY](tensors/0003461.npy) |
| 3462 | `model.layers.11.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.5 / 3.390625 / 0.01278418434990777 / 0.766280973264347 | [NPY](tensors/0003462.npy) |
| 3463 | `model.layers.11.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.5 / 3.390625 / 0.01278418434990777 / 0.766280973264347 | [NPY](tensors/0003463.npy) |
| 3464 | `model.layers.11.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3465 | `model.layers.11.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3466 | `model.layers.11.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3467 | `model.layers.11.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -227.0 / 216.0 / 0.17802711592780218 / 8.611353956398396 | [NPY](tensors/0003467.npy) |
| 3468 | `model.layers.11.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -227.0 / 216.0 / 0.17802711592780218 / 8.611353956398396 | [NPY](tensors/0003468.npy) |
| 3469 | `model.layers.11.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8828125 / 1.6796875 / -0.12243270874023438 / 0.7317884843932466 | [NPY](tensors/0003469.npy) |
| 3470 | `model.layers.11` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -414.0 / 592.0 / 0.8277364095052083 / 25.9561627904923 | [NPY](tensors/0003470.npy) |
| 3549 | `model.layers.11` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -320.0 / 442.0 / 0.20609639485677084 / 19.778859647455672 | [NPY](tensors/0003549.npy) |
| 3550 | `model.layers.11` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 317] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003550.npy) |
| 3551 | `model.layers.11` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0003551.npy) |
| 3552 | `model.layers.11` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0003552.npy) |
| 3553 | `model.layers.11` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0003553.npy) |
| 3554 | `model.layers.11` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3555 | `model.layers.11` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3556 | `model.layers.11` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3557 | `model.layers.11.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -320.0 / 442.0 / 0.20609639485677084 / 19.778859647455672 | [NPY](tensors/0003557.npy) |
| 3558 | `model.layers.11.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 104.5 / 0.03801265425152249 / 3.140445916604965 | [NPY](tensors/0003558.npy) |
| 3559 | `model.layers.11.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 104.5 / 0.03801265425152249 / 3.140445916604965 | [NPY](tensors/0003559.npy) |
| 3560 | `model.layers.11.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 317] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003560.npy) |
| 3561 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0003561.npy) |
| 3562 | `model.layers.11.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3563 | `model.layers.11.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3564 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0003564.npy) |
| 3565 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0003565.npy) |
| 3566 | `model.layers.11.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3567 | `model.layers.11.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 104.5 / 0.03801265425152249 / 3.140445916604965 | [NPY](tensors/0003567.npy) |
| 3568 | `model.layers.11.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.125 / 8.6875 / 0.02031078631989658 / 1.344192687454417 | [NPY](tensors/0003568.npy) |
| 3569 | `model.layers.11.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 104.5 / 0.03801265425152249 / 3.140445916604965 | [NPY](tensors/0003569.npy) |
| 3570 | `model.layers.11.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.875 / 30.0 / 0.10054951906204224 / 3.5832637321176737 | [NPY](tensors/0003570.npy) |
| 3571 | `model.layers.11.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 104.5 / 0.03801265425152249 / 3.140445916604965 | [NPY](tensors/0003571.npy) |
| 3572 | `model.layers.11.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.3125 / 7.125 / -0.1044778823852539 / 2.2452088668985963 | [NPY](tensors/0003572.npy) |
| 3573 | `model.layers.11.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 7.09375 / 0.016351261583622545 / 1.3729109024710484 | [NPY](tensors/0003573.npy) |
| 3574 | `model.layers.11.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -195.0 / 223.0 / 0.0018240610758463542 / 6.776955432640001 | [NPY](tensors/0003574.npy) |
| 3575 | `model.layers.11.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -195.0 / 223.0 / 0.0018240610758463542 / 6.776955432640001 | [NPY](tensors/0003575.npy) |
| 3576 | `model.layers.11.self_attn` | 30 | `output[1]` | [1, 64, 1, 317] | torch.bfloat16 → float32 | 2.7625901566352695e-11 / 0.9375 / 0.0026744386407037803 / 0.016193024076308047 | [NPY](tensors/0003576.npy) |
| 3577 | `model.layers.11.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -209.0 / 247.0 / 0.20811021592881945 / 18.300593984366433 | [NPY](tensors/0003577.npy) |
| 3578 | `model.layers.11.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.640625 / 3.875 / -7.306469811333551e-05 / 0.8254561306039604 | [NPY](tensors/0003578.npy) |
| 3579 | `model.layers.11.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.640625 / 3.875 / -7.306469811333551e-05 / 0.8254561306039604 | [NPY](tensors/0003579.npy) |
| 3580 | `model.layers.11.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.640625 / 3.875 / -7.306469811333551e-05 / 0.8254561306039604 | [NPY](tensors/0003580.npy) |
| 3581 | `model.layers.11.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3582 | `model.layers.11.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3583 | `model.layers.11.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3584 | `model.layers.11.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -262.0 / 320.0 / 0.30224266052246096 / 10.791414312113583 | [NPY](tensors/0003584.npy) |
| 3585 | `model.layers.11.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -262.0 / 320.0 / 0.30224266052246096 / 10.791414312113583 | [NPY](tensors/0003585.npy) |
| 3586 | `model.layers.11.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.875 / 1.6875 / -0.17449951171875 / 0.9451238112859033 | [NPY](tensors/0003586.npy) |
| 3587 | `model.layers.11` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -360.0 / 568.0 / 0.5102671305338542 / 24.380479367856775 | [NPY](tensors/0003587.npy) |
| 3666 | `model.layers.11` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -384.0 / 632.0 / 0.4249248928493924 / 22.79450596054779 | [NPY](tensors/0003666.npy) |
| 3667 | `model.layers.11` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 318] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003667.npy) |
| 3668 | `model.layers.11` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0003668.npy) |
| 3669 | `model.layers.11` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0003669.npy) |
| 3670 | `model.layers.11` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0003670.npy) |
| 3671 | `model.layers.11` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3672 | `model.layers.11` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3673 | `model.layers.11` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3674 | `model.layers.11.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -384.0 / 632.0 / 0.4249248928493924 / 22.79450596054779 | [NPY](tensors/0003674.npy) |
| 3675 | `model.layers.11.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 130.0 / 0.06339537567562527 / 3.4330471205198876 | [NPY](tensors/0003675.npy) |
| 3676 | `model.layers.11.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 130.0 / 0.06339537567562527 / 3.4330471205198876 | [NPY](tensors/0003676.npy) |
| 3677 | `model.layers.11.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 318] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003677.npy) |
| 3678 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0003678.npy) |
| 3679 | `model.layers.11.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3680 | `model.layers.11.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3681 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0003681.npy) |
| 3682 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0003682.npy) |
| 3683 | `model.layers.11.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3684 | `model.layers.11.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 130.0 / 0.06339537567562527 / 3.4330471205198876 | [NPY](tensors/0003684.npy) |
| 3685 | `model.layers.11.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.5 / 8.9375 / 0.0015899776481091976 / 1.284376071484831 | [NPY](tensors/0003685.npy) |
| 3686 | `model.layers.11.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 130.0 / 0.06339537567562527 / 3.4330471205198876 | [NPY](tensors/0003686.npy) |
| 3687 | `model.layers.11.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -25.5 / 31.75 / -0.03380128741264343 / 3.541821445622589 | [NPY](tensors/0003687.npy) |
| 3688 | `model.layers.11.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 130.0 / 0.06339537567562527 / 3.4330471205198876 | [NPY](tensors/0003688.npy) |
| 3689 | `model.layers.11.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.46875 / 9.125 / -0.0886492133140564 / 2.4108842370109387 | [NPY](tensors/0003689.npy) |
| 3690 | `model.layers.11.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5625 / 7.46875 / 0.008882041089236736 / 1.401744509237509 | [NPY](tensors/0003690.npy) |
| 3691 | `model.layers.11.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -246.0 / 165.0 / -0.09600835243860881 / 6.652399409386853 | [NPY](tensors/0003691.npy) |
| 3692 | `model.layers.11.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -246.0 / 165.0 / -0.09600835243860881 / 6.652399409386853 | [NPY](tensors/0003692.npy) |
| 3693 | `model.layers.11.self_attn` | 31 | `output[1]` | [1, 64, 1, 318] | torch.bfloat16 → float32 | 1.0345502232667059e-11 / 0.95703125 / 0.002602272779313269 / 0.016436871997005036 | [NPY](tensors/0003693.npy) |
| 3694 | `model.layers.11.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -219.0 / 386.0 / 0.3285129123263889 / 19.98909789499556 | [NPY](tensors/0003694.npy) |
| 3695 | `model.layers.11.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.78125 / 4.8125 / 0.009150029553307428 / 0.7593666080305492 | [NPY](tensors/0003695.npy) |
| 3696 | `model.layers.11.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.78125 / 4.8125 / 0.009150029553307428 / 0.7593666080305492 | [NPY](tensors/0003696.npy) |
| 3697 | `model.layers.11.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.78125 / 4.8125 / 0.009150029553307428 / 0.7593666080305492 | [NPY](tensors/0003697.npy) |
| 3698 | `model.layers.11.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3699 | `model.layers.11.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3700 | `model.layers.11.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3701 | `model.layers.11.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -390.0 / 354.0 / 0.30365285873413084 / 14.19718875722423 | [NPY](tensors/0003701.npy) |
| 3702 | `model.layers.11.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -390.0 / 354.0 / 0.30365285873413084 / 14.19718875722423 | [NPY](tensors/0003702.npy) |
| 3703 | `model.layers.11.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.296875 / 1.8515625 / -0.20568561553955078 / 1.0537765434435393 | [NPY](tensors/0003703.npy) |
| 3704 | `model.layers.11` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -608.0 / 740.0 / 0.6320753309461805 / 29.34061860943975 | [NPY](tensors/0003704.npy) |
| 3783 | `model.layers.11` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -302.0 / 424.0 / 0.5975323147243924 / 17.69881167992558 | [NPY](tensors/0003783.npy) |
| 3784 | `model.layers.11` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 319] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003784.npy) |
| 3785 | `model.layers.11` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0003785.npy) |
| 3786 | `model.layers.11` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0003786.npy) |
| 3787 | `model.layers.11` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0003787.npy) |
| 3788 | `model.layers.11` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3789 | `model.layers.11` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3790 | `model.layers.11` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3791 | `model.layers.11.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -302.0 / 424.0 / 0.5975323147243924 / 17.69881167992558 | [NPY](tensors/0003791.npy) |
| 3792 | `model.layers.11.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.5 / 112.0 / 0.0765275862481859 / 3.2932271926017767 | [NPY](tensors/0003792.npy) |
| 3793 | `model.layers.11.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.5 / 112.0 / 0.0765275862481859 / 3.2932271926017767 | [NPY](tensors/0003793.npy) |
| 3794 | `model.layers.11.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 319] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003794.npy) |
| 3795 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0003795.npy) |
| 3796 | `model.layers.11.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3797 | `model.layers.11.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3798 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0003798.npy) |
| 3799 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0003799.npy) |
| 3800 | `model.layers.11.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3801 | `model.layers.11.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.5 / 112.0 / 0.0765275862481859 / 3.2932271926017767 | [NPY](tensors/0003801.npy) |
| 3802 | `model.layers.11.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5 / 8.4375 / 0.04080653272103518 / 1.2189261773303988 | [NPY](tensors/0003802.npy) |
| 3803 | `model.layers.11.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.5 / 112.0 / 0.0765275862481859 / 3.2932271926017767 | [NPY](tensors/0003803.npy) |
| 3804 | `model.layers.11.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.25 / 34.0 / 0.12435192614793777 / 3.6327184084538726 | [NPY](tensors/0003804.npy) |
| 3805 | `model.layers.11.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.5 / 112.0 / 0.0765275862481859 / 3.2932271926017767 | [NPY](tensors/0003805.npy) |
| 3806 | `model.layers.11.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.15625 / 5.53125 / -0.00537244975566864 / 2.0481695403491886 | [NPY](tensors/0003806.npy) |
| 3807 | `model.layers.11.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.9375 / 4.90625 / 0.01422712323255837 / 1.253422174936578 | [NPY](tensors/0003807.npy) |
| 3808 | `model.layers.11.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.0 / 90.0 / -0.057270071903864544 / 3.6229353972887615 | [NPY](tensors/0003808.npy) |
| 3809 | `model.layers.11.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.0 / 90.0 / -0.057270071903864544 / 3.6229353972887615 | [NPY](tensors/0003809.npy) |
| 3810 | `model.layers.11.self_attn` | 32 | `output[1]` | [1, 64, 1, 319] | torch.bfloat16 → float32 | 1.2005330063402653e-10 / 0.91015625 / 0.0028671403430586898 / 0.014320277740557387 | [NPY](tensors/0003810.npy) |
| 3811 | `model.layers.11.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -212.0 / 360.0 / 0.5403101603190105 / 17.239167164817633 | [NPY](tensors/0003811.npy) |
| 3812 | `model.layers.11.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.203125 / 2.5625 / 0.01504157649146186 / 0.7012588101415614 | [NPY](tensors/0003812.npy) |
| 3813 | `model.layers.11.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.203125 / 2.5625 / 0.01504157649146186 / 0.7012588101415614 | [NPY](tensors/0003813.npy) |
| 3814 | `model.layers.11.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.203125 / 2.5625 / 0.01504157649146186 / 0.7012588101415614 | [NPY](tensors/0003814.npy) |
| 3815 | `model.layers.11.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3816 | `model.layers.11.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3817 | `model.layers.11.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3818 | `model.layers.11.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -142.0 / 133.0 / 0.094997419251336 / 6.456117969633219 | [NPY](tensors/0003818.npy) |
| 3819 | `model.layers.11.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -142.0 / 133.0 / 0.094997419251336 / 6.456117969633219 | [NPY](tensors/0003819.npy) |
| 3820 | `model.layers.11.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.140625 / -0.09945797920227051 / 0.5387323505838773 | [NPY](tensors/0003820.npy) |
| 3821 | `model.layers.11` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -354.0 / 482.0 / 0.6346586439344618 / 21.285991392486782 | [NPY](tensors/0003821.npy) |
| 3900 | `model.layers.11` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -370.0 / 572.0 / 0.33329179551866317 / 21.278268474250602 | [NPY](tensors/0003900.npy) |
| 3901 | `model.layers.11` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 320] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003901.npy) |
| 3902 | `model.layers.11` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0003902.npy) |
| 3903 | `model.layers.11` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0003903.npy) |
| 3904 | `model.layers.11` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0003904.npy) |
| 3905 | `model.layers.11` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3906 | `model.layers.11` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3907 | `model.layers.11` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3908 | `model.layers.11.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -370.0 / 572.0 / 0.33329179551866317 / 21.278268474250602 | [NPY](tensors/0003908.npy) |
| 3909 | `model.layers.11.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.5 / 126.0 / 0.053821402788162234 / 3.371562151692713 | [NPY](tensors/0003909.npy) |
| 3910 | `model.layers.11.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.5 / 126.0 / 0.053821402788162234 / 3.371562151692713 | [NPY](tensors/0003910.npy) |
| 3911 | `model.layers.11.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 320] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003911.npy) |
| 3912 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0003912.npy) |
| 3913 | `model.layers.11.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3914 | `model.layers.11.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3915 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0003915.npy) |
| 3916 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0003916.npy) |
| 3917 | `model.layers.11.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3918 | `model.layers.11.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.5 / 126.0 / 0.053821402788162234 / 3.371562151692713 | [NPY](tensors/0003918.npy) |
| 3919 | `model.layers.11.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.34375 / 10.4375 / 0.021327872294932604 / 1.2824971357713144 | [NPY](tensors/0003919.npy) |
| 3920 | `model.layers.11.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.5 / 126.0 / 0.053821402788162234 / 3.371562151692713 | [NPY](tensors/0003920.npy) |
| 3921 | `model.layers.11.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -25.5 / 29.625 / -0.03596442937850952 / 3.369647792766066 | [NPY](tensors/0003921.npy) |
| 3922 | `model.layers.11.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.5 / 126.0 / 0.053821402788162234 / 3.371562151692713 | [NPY](tensors/0003922.npy) |
| 3923 | `model.layers.11.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.3125 / 8.625 / -0.007151663303375244 / 2.4411384411433534 | [NPY](tensors/0003923.npy) |
| 3924 | `model.layers.11.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.125 / 6.59375 / 0.0184234413318336 / 1.3655463211680818 | [NPY](tensors/0003924.npy) |
| 3925 | `model.layers.11.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -185.0 / 143.0 / -0.021825577153099907 / 5.603506220001828 | [NPY](tensors/0003925.npy) |
| 3926 | `model.layers.11.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -185.0 / 143.0 / -0.021825577153099907 / 5.603506220001828 | [NPY](tensors/0003926.npy) |
| 3927 | `model.layers.11.self_attn` | 33 | `output[1]` | [1, 64, 1, 320] | torch.bfloat16 → float32 | 4.661160346586257e-11 / 0.9609375 / 0.002856724869585825 / 0.015704069113183824 | [NPY](tensors/0003927.npy) |
| 3928 | `model.layers.11.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -227.0 / 388.0 / 0.3122995164659288 / 19.26829335178371 | [NPY](tensors/0003928.npy) |
| 3929 | `model.layers.11.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.640625 / 4.28125 / 0.008151627911461724 / 0.738249187760829 | [NPY](tensors/0003929.npy) |
| 3930 | `model.layers.11.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.640625 / 4.28125 / 0.008151627911461724 / 0.738249187760829 | [NPY](tensors/0003930.npy) |
| 3931 | `model.layers.11.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.640625 / 4.28125 / 0.008151627911461724 / 0.738249187760829 | [NPY](tensors/0003931.npy) |
| 3932 | `model.layers.11.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3933 | `model.layers.11.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3934 | `model.layers.11.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3935 | `model.layers.11.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -241.0 / 209.0 / 0.19354947408040366 / 8.621645390952862 | [NPY](tensors/0003935.npy) |
| 3936 | `model.layers.11.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -241.0 / 209.0 / 0.19354947408040366 / 8.621645390952862 | [NPY](tensors/0003936.npy) |
| 3937 | `model.layers.11.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.65625 / 1.578125 / -0.20804977416992188 / 0.9405932153601053 | [NPY](tensors/0003937.npy) |
| 3938 | `model.layers.11` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -468.0 / 596.0 / 0.5044708251953125 / 25.012102354228226 | [NPY](tensors/0003938.npy) |
| 4017 | `model.layers.11` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -221.0 / 396.0 / 0.6428465101453993 / 15.886604620062647 | [NPY](tensors/0004017.npy) |
| 4018 | `model.layers.11` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 321] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004018.npy) |
| 4019 | `model.layers.11` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0004019.npy) |
| 4020 | `model.layers.11` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0004020.npy) |
| 4021 | `model.layers.11` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0004021.npy) |
| 4022 | `model.layers.11` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4023 | `model.layers.11` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4024 | `model.layers.11` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4025 | `model.layers.11.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -221.0 / 396.0 / 0.6428465101453993 / 15.886604620062647 | [NPY](tensors/0004025.npy) |
| 4026 | `model.layers.11.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 106.5 / 0.09356193211343554 / 3.17745091450001 | [NPY](tensors/0004026.npy) |
| 4027 | `model.layers.11.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 106.5 / 0.09356193211343554 / 3.17745091450001 | [NPY](tensors/0004027.npy) |
| 4028 | `model.layers.11.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 321] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004028.npy) |
| 4029 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0004029.npy) |
| 4030 | `model.layers.11.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4031 | `model.layers.11.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4032 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0004032.npy) |
| 4033 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0004033.npy) |
| 4034 | `model.layers.11.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4035 | `model.layers.11.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 106.5 / 0.09356193211343554 / 3.17745091450001 | [NPY](tensors/0004035.npy) |
| 4036 | `model.layers.11.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.6875 / 7.96875 / 0.05794071266427636 / 1.255721906396076 | [NPY](tensors/0004036.npy) |
| 4037 | `model.layers.11.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 106.5 / 0.09356193211343554 / 3.17745091450001 | [NPY](tensors/0004037.npy) |
| 4038 | `model.layers.11.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.25 / 37.75 / 0.11747859418392181 / 3.985015471334981 | [NPY](tensors/0004038.npy) |
| 4039 | `model.layers.11.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 106.5 / 0.09356193211343554 / 3.17745091450001 | [NPY](tensors/0004039.npy) |
| 4040 | `model.layers.11.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.5 / 5.6875 / 0.08758455514907837 / 2.1368625682863684 | [NPY](tensors/0004040.npy) |
| 4041 | `model.layers.11.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 5.59375 / 0.026953975029755384 / 1.235139726851636 | [NPY](tensors/0004041.npy) |
| 4042 | `model.layers.11.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.5 / 68.5 / 0.1444235258632236 / 3.808944201251999 | [NPY](tensors/0004042.npy) |
| 4043 | `model.layers.11.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.5 / 68.5 / 0.1444235258632236 / 3.808944201251999 | [NPY](tensors/0004043.npy) |
| 4044 | `model.layers.11.self_attn` | 34 | `output[1]` | [1, 64, 1, 321] | torch.bfloat16 → float32 | 2.0236257114447653e-11 / 0.8828125 / 0.0028759553099575487 / 0.01425704390963021 | [NPY](tensors/0004044.npy) |
| 4045 | `model.layers.11.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -160.0 / 396.0 / 0.7874647352430556 / 16.25757793810134 | [NPY](tensors/0004045.npy) |
| 4046 | `model.layers.11.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.875 / 2.5 / 0.039447275466389126 / 0.6903339836428604 | [NPY](tensors/0004046.npy) |
| 4047 | `model.layers.11.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.875 / 2.5 / 0.039447275466389126 / 0.6903339836428604 | [NPY](tensors/0004047.npy) |
| 4048 | `model.layers.11.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.875 / 2.5 / 0.039447275466389126 / 0.6903339836428604 | [NPY](tensors/0004048.npy) |
| 4049 | `model.layers.11.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4050 | `model.layers.11.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4051 | `model.layers.11.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4052 | `model.layers.11.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -214.0 / 141.0 / 0.15086261166466608 / 6.5821936849930545 | [NPY](tensors/0004052.npy) |
| 4053 | `model.layers.11.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -214.0 / 141.0 / 0.15086261166466608 / 6.5821936849930545 | [NPY](tensors/0004053.npy) |
| 4054 | `model.layers.11.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.71875 / 0.80078125 / -0.1199483871459961 / 0.5281331318286401 | [NPY](tensors/0004054.npy) |
| 4055 | `model.layers.11` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -366.0 / 504.0 / 0.9390782674153646 / 20.412541615729133 | [NPY](tensors/0004055.npy) |
| 4134 | `model.layers.11` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -484.0 / 452.0 / 0.3522649129231771 / 18.979504431735666 | [NPY](tensors/0004134.npy) |
| 4135 | `model.layers.11` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004135.npy) |
| 4136 | `model.layers.11` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0004136.npy) |
| 4137 | `model.layers.11` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0004137.npy) |
| 4138 | `model.layers.11` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0004138.npy) |
| 4139 | `model.layers.11` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4140 | `model.layers.11` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4141 | `model.layers.11` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4142 | `model.layers.11.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -484.0 / 452.0 / 0.3522649129231771 / 18.979504431735666 | [NPY](tensors/0004142.npy) |
| 4143 | `model.layers.11.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -134.0 / 98.0 / 0.03398639361063639 / 3.6319397291647744 | [NPY](tensors/0004143.npy) |
| 4144 | `model.layers.11.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -134.0 / 98.0 / 0.03398639361063639 / 3.6319397291647744 | [NPY](tensors/0004144.npy) |
| 4145 | `model.layers.11.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004145.npy) |
| 4146 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0004146.npy) |
| 4147 | `model.layers.11.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4148 | `model.layers.11.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4149 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0004149.npy) |
| 4150 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0004150.npy) |
| 4151 | `model.layers.11.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4152 | `model.layers.11.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -134.0 / 98.0 / 0.03398639361063639 / 3.6319397291647744 | [NPY](tensors/0004152.npy) |
| 4153 | `model.layers.11.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.03125 / 6.84375 / 0.028024666011333466 / 1.118513145677883 | [NPY](tensors/0004153.npy) |
| 4154 | `model.layers.11.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -134.0 / 98.0 / 0.03398639361063639 / 3.6319397291647744 | [NPY](tensors/0004154.npy) |
| 4155 | `model.layers.11.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.75 / 32.75 / 0.15493784844875336 / 3.251627010099214 | [NPY](tensors/0004155.npy) |
| 4156 | `model.layers.11.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -134.0 / 98.0 / 0.03398639361063639 / 3.6319397291647744 | [NPY](tensors/0004156.npy) |
| 4157 | `model.layers.11.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.0625 / 5.5625 / -0.00017315149307250977 / 1.5434017317711692 | [NPY](tensors/0004157.npy) |
| 4158 | `model.layers.11.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5625 / 4.65625 / 0.011597379809245467 / 1.052015593703123 | [NPY](tensors/0004158.npy) |
| 4159 | `model.layers.11.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -175.0 / 229.0 / -0.12885598606533474 / 6.629538104655114 | [NPY](tensors/0004159.npy) |
| 4160 | `model.layers.11.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -175.0 / 229.0 / -0.12885598606533474 / 6.629538104655114 | [NPY](tensors/0004160.npy) |
| 4161 | `model.layers.11.self_attn` | 35 | `output[1]` | [1, 64, 1, 322] | torch.bfloat16 → float32 | 3.1468516681343317e-10 / 0.87890625 / 0.0028416553241004364 / 0.014727585827896142 | [NPY](tensors/0004161.npy) |
| 4162 | `model.layers.11.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -255.0 / 338.0 / 0.22294464111328124 / 15.35529466134347 | [NPY](tensors/0004162.npy) |
| 4163 | `model.layers.11.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.828125 / 4.125 / -0.0037353833516438804 / 0.6774387833804562 | [NPY](tensors/0004163.npy) |
| 4164 | `model.layers.11.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.828125 / 4.125 / -0.0037353833516438804 / 0.6774387833804562 | [NPY](tensors/0004164.npy) |
| 4165 | `model.layers.11.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.828125 / 4.125 / -0.0037353833516438804 / 0.6774387833804562 | [NPY](tensors/0004165.npy) |
| 4166 | `model.layers.11.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4167 | `model.layers.11.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4168 | `model.layers.11.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4169 | `model.layers.11.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -188.0 / 179.0 / 0.11854193475511339 / 7.354616382412952 | [NPY](tensors/0004169.npy) |
| 4170 | `model.layers.11.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -188.0 / 179.0 / 0.11854193475511339 / 7.354616382412952 | [NPY](tensors/0004170.npy) |
| 4171 | `model.layers.11.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.734375 / 1.390625 / -0.18202877044677734 / 0.7469467958645151 | [NPY](tensors/0004171.npy) |
| 4172 | `model.layers.11` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -444.0 / 444.0 / 0.3403995090060764 / 20.381607151585843 | [NPY](tensors/0004172.npy) |
| 4251 | `model.layers.11` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -384.0 / 568.0 / 0.7716510348849827 / 22.932207681763387 | [NPY](tensors/0004251.npy) |
| 4252 | `model.layers.11` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004252.npy) |
| 4253 | `model.layers.11` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0004253.npy) |
| 4254 | `model.layers.11` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0004254.npy) |
| 4255 | `model.layers.11` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0004255.npy) |
| 4256 | `model.layers.11` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4257 | `model.layers.11` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4258 | `model.layers.11` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4259 | `model.layers.11.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -384.0 / 568.0 / 0.7716510348849827 / 22.932207681763387 | [NPY](tensors/0004259.npy) |
| 4260 | `model.layers.11.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 116.0 / 0.08686937623553806 / 3.2569735049696127 | [NPY](tensors/0004260.npy) |
| 4261 | `model.layers.11.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 116.0 / 0.08686937623553806 / 3.2569735049696127 | [NPY](tensors/0004261.npy) |
| 4262 | `model.layers.11.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004262.npy) |
| 4263 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0004263.npy) |
| 4264 | `model.layers.11.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4265 | `model.layers.11.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4266 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0004266.npy) |
| 4267 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0004267.npy) |
| 4268 | `model.layers.11.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4269 | `model.layers.11.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 116.0 / 0.08686937623553806 / 3.2569735049696127 | [NPY](tensors/0004269.npy) |
| 4270 | `model.layers.11.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.84375 / 9.875 / 0.04496656230185181 / 1.3215113722296323 | [NPY](tensors/0004270.npy) |
| 4271 | `model.layers.11.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 116.0 / 0.08686937623553806 / 3.2569735049696127 | [NPY](tensors/0004271.npy) |
| 4272 | `model.layers.11.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.25 / 31.875 / 0.03192228078842163 / 3.588514834977208 | [NPY](tensors/0004272.npy) |
| 4273 | `model.layers.11.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 116.0 / 0.08686937623553806 / 3.2569735049696127 | [NPY](tensors/0004273.npy) |
| 4274 | `model.layers.11.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.1875 / 10.375 / -0.02688443660736084 / 2.474906196441243 | [NPY](tensors/0004274.npy) |
| 4275 | `model.layers.11.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.71875 / 6.28125 / 0.012923190835863352 / 1.3430835785510193 | [NPY](tensors/0004275.npy) |
| 4276 | `model.layers.11.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -192.0 / 171.0 / -0.04568474292755127 / 6.111322975115825 | [NPY](tensors/0004276.npy) |
| 4277 | `model.layers.11.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -192.0 / 171.0 / -0.04568474292755127 / 6.111322975115825 | [NPY](tensors/0004277.npy) |
| 4278 | `model.layers.11.self_attn` | 36 | `output[1]` | [1, 64, 1, 323] | torch.bfloat16 → float32 | 2.7711166694643907e-12 / 0.89453125 / 0.002677484095958889 / 0.012647594903434133 | [NPY](tensors/0004278.npy) |
| 4279 | `model.layers.11.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -213.0 / 376.0 / 0.7256561279296875 / 20.60273332447833 | [NPY](tensors/0004279.npy) |
| 4280 | `model.layers.11.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.75 / 5.34375 / 0.017254177729288736 / 0.7361999987142206 | [NPY](tensors/0004280.npy) |
| 4281 | `model.layers.11.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.75 / 5.34375 / 0.017254177729288736 / 0.7361999987142206 | [NPY](tensors/0004281.npy) |
| 4282 | `model.layers.11.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.75 / 5.34375 / 0.017254177729288736 / 0.7361999987142206 | [NPY](tensors/0004282.npy) |
| 4283 | `model.layers.11.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4284 | `model.layers.11.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4285 | `model.layers.11.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4286 | `model.layers.11.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -218.0 / 232.0 / 0.3434769809246063 / 8.481237192803121 | [NPY](tensors/0004286.npy) |
| 4287 | `model.layers.11.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -218.0 / 232.0 / 0.3434769809246063 / 8.481237192803121 | [NPY](tensors/0004287.npy) |
| 4288 | `model.layers.11.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.34375 / 1.796875 / -0.1856222152709961 / 0.9440557156608766 | [NPY](tensors/0004288.npy) |
| 4289 | `model.layers.11` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -432.0 / 608.0 / 1.0684332953559028 / 26.100382467799506 | [NPY](tensors/0004289.npy) |
| 4368 | `model.layers.11` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -448.0 / 548.0 / 0.42709791395399305 / 21.569191119655898 | [NPY](tensors/0004368.npy) |
| 4369 | `model.layers.11` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004369.npy) |
| 4370 | `model.layers.11` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0004370.npy) |
| 4371 | `model.layers.11` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0004371.npy) |
| 4372 | `model.layers.11` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0004372.npy) |
| 4373 | `model.layers.11` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4374 | `model.layers.11` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4375 | `model.layers.11` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4376 | `model.layers.11.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -448.0 / 548.0 / 0.42709791395399305 / 21.569191119655898 | [NPY](tensors/0004376.npy) |
| 4377 | `model.layers.11.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 119.0 / 0.05882396035724216 / 3.541193313574489 | [NPY](tensors/0004377.npy) |
| 4378 | `model.layers.11.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 119.0 / 0.05882396035724216 / 3.541193313574489 | [NPY](tensors/0004378.npy) |
| 4379 | `model.layers.11.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004379.npy) |
| 4380 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0004380.npy) |
| 4381 | `model.layers.11.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4382 | `model.layers.11.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4383 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0004383.npy) |
| 4384 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0004384.npy) |
| 4385 | `model.layers.11.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4386 | `model.layers.11.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 119.0 / 0.05882396035724216 / 3.541193313574489 | [NPY](tensors/0004386.npy) |
| 4387 | `model.layers.11.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.4375 / 7.25 / 0.023594195023179054 / 1.165366262614693 | [NPY](tensors/0004387.npy) |
| 4388 | `model.layers.11.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 119.0 / 0.05882396035724216 / 3.541193313574489 | [NPY](tensors/0004388.npy) |
| 4389 | `model.layers.11.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.375 / 31.125 / 0.03777052462100983 / 3.3160723224741626 | [NPY](tensors/0004389.npy) |
| 4390 | `model.layers.11.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 119.0 / 0.05882396035724216 / 3.541193313574489 | [NPY](tensors/0004390.npy) |
| 4391 | `model.layers.11.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.1875 / 6.03125 / 0.05310046672821045 / 1.8931702634011496 | [NPY](tensors/0004391.npy) |
| 4392 | `model.layers.11.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.6875 / 5.8125 / 0.017837417777627707 / 1.2380149973100867 | [NPY](tensors/0004392.npy) |
| 4393 | `model.layers.11.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -190.0 / 215.0 / -0.02760789692401886 / 6.405185624372434 | [NPY](tensors/0004393.npy) |
| 4394 | `model.layers.11.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -190.0 / 215.0 / -0.02760789692401886 / 6.405185624372434 | [NPY](tensors/0004394.npy) |
| 4395 | `model.layers.11.self_attn` | 37 | `output[1]` | [1, 64, 1, 324] | torch.bfloat16 → float32 | 1.028865881380625e-11 / 0.953125 / 0.0027442601644958454 / 0.012779672091464904 | [NPY](tensors/0004395.npy) |
| 4396 | `model.layers.11.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -233.0 / 358.0 / 0.39907260470920136 / 18.897895908860345 | [NPY](tensors/0004396.npy) |
| 4397 | `model.layers.11.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.9375 / 0.005815521876017252 / 0.7171337087059468 | [NPY](tensors/0004397.npy) |
| 4398 | `model.layers.11.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.9375 / 0.005815521876017252 / 0.7171337087059468 | [NPY](tensors/0004398.npy) |
| 4399 | `model.layers.11.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.9375 / 0.005815521876017252 / 0.7171337087059468 | [NPY](tensors/0004399.npy) |
| 4400 | `model.layers.11.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4401 | `model.layers.11.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4402 | `model.layers.11.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4403 | `model.layers.11.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -245.0 / 238.0 / 0.22291506661309135 / 9.646155266457264 | [NPY](tensors/0004403.npy) |
| 4404 | `model.layers.11.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -245.0 / 238.0 / 0.22291506661309135 / 9.646155266457264 | [NPY](tensors/0004404.npy) |
| 4405 | `model.layers.11.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.203125 / 1.59375 / -0.1489429473876953 / 0.7913297678780137 | [NPY](tensors/0004405.npy) |
| 4406 | `model.layers.11` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -478.0 / 596.0 / 0.6219816419813368 / 25.4657933426494 | [NPY](tensors/0004406.npy) |
| 4485 | `model.layers.11` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -488.0 / 672.0 / 0.4870144314236111 / 26.000680827838323 | [NPY](tensors/0004485.npy) |
| 4486 | `model.layers.11` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004486.npy) |
| 4487 | `model.layers.11` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0004487.npy) |
| 4488 | `model.layers.11` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0004488.npy) |
| 4489 | `model.layers.11` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0004489.npy) |
| 4490 | `model.layers.11` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4491 | `model.layers.11` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4492 | `model.layers.11` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4493 | `model.layers.11.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -488.0 / 672.0 / 0.4870144314236111 / 26.000680827838323 | [NPY](tensors/0004493.npy) |
| 4494 | `model.layers.11.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 121.0 / 0.05756688581572639 / 3.4203432823218 | [NPY](tensors/0004494.npy) |
| 4495 | `model.layers.11.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 121.0 / 0.05756688581572639 / 3.4203432823218 | [NPY](tensors/0004495.npy) |
| 4496 | `model.layers.11.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004496.npy) |
| 4497 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0004497.npy) |
| 4498 | `model.layers.11.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4499 | `model.layers.11.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4500 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0004500.npy) |
| 4501 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0004501.npy) |
| 4502 | `model.layers.11.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4503 | `model.layers.11.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 121.0 / 0.05756688581572639 / 3.4203432823218 | [NPY](tensors/0004503.npy) |
| 4504 | `model.layers.11.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.90625 / 8.6875 / 0.03930274042068049 / 1.1716195805280647 | [NPY](tensors/0004504.npy) |
| 4505 | `model.layers.11.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 121.0 / 0.05756688581572639 / 3.4203432823218 | [NPY](tensors/0004505.npy) |
| 4506 | `model.layers.11.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -25.625 / 35.75 / -0.025794915854930878 / 3.4453363971712907 | [NPY](tensors/0004506.npy) |
| 4507 | `model.layers.11.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 121.0 / 0.05756688581572639 / 3.4203432823218 | [NPY](tensors/0004507.npy) |
| 4508 | `model.layers.11.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.4375 / 9.125 / -0.1016755998134613 / 2.4855196063293707 | [NPY](tensors/0004508.npy) |
| 4509 | `model.layers.11.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.3125 / 5.625 / 0.0001902482472360134 / 1.1762190179426404 | [NPY](tensors/0004509.npy) |
| 4510 | `model.layers.11.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -268.0 / 196.0 / -0.09779495133294 / 7.271256860245125 | [NPY](tensors/0004510.npy) |
| 4511 | `model.layers.11.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -268.0 / 196.0 / -0.09779495133294 / 7.271256860245125 | [NPY](tensors/0004511.npy) |
| 4512 | `model.layers.11.self_attn` | 38 | `output[1]` | [1, 64, 1, 325] | torch.bfloat16 → float32 | 3.161915174132446e-13 / 0.96875 / 0.0025640813276360313 / 0.01618135472880966 | [NPY](tensors/0004512.npy) |
| 4513 | `model.layers.11.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -292.0 / 404.0 / 0.38978373209635414 / 22.62316044564262 | [NPY](tensors/0004513.npy) |
| 4514 | `model.layers.11.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.25 / 4.1875 / 0.008573687076568604 / 0.7668754249916591 | [NPY](tensors/0004514.npy) |
| 4515 | `model.layers.11.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.25 / 4.1875 / 0.008573687076568604 / 0.7668754249916591 | [NPY](tensors/0004515.npy) |
| 4516 | `model.layers.11.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.25 / 4.1875 / 0.008573687076568604 / 0.7668754249916591 | [NPY](tensors/0004516.npy) |
| 4517 | `model.layers.11.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4518 | `model.layers.11.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4519 | `model.layers.11.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4520 | `model.layers.11.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -288.0 / 294.0 / 0.10415777100457085 / 10.815277594383831 | [NPY](tensors/0004520.npy) |
| 4521 | `model.layers.11.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -288.0 / 294.0 / 0.10415777100457085 / 10.815277594383831 | [NPY](tensors/0004521.npy) |
| 4522 | `model.layers.11.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.1875 / 1.640625 / -0.14429378509521484 / 0.8496487641156325 | [NPY](tensors/0004522.npy) |
| 4523 | `model.layers.11` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -580.0 / 696.0 / 0.4926381429036458 / 29.84739345452499 | [NPY](tensors/0004523.npy) |
| 4602 | `model.layers.11` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -476.0 / 600.0 / 0.1865096198187934 / 23.433572950537705 | [NPY](tensors/0004602.npy) |
| 4603 | `model.layers.11` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004603.npy) |
| 4604 | `model.layers.11` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0004604.npy) |
| 4605 | `model.layers.11` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0004605.npy) |
| 4606 | `model.layers.11` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0004606.npy) |
| 4607 | `model.layers.11` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4608 | `model.layers.11` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4609 | `model.layers.11` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4610 | `model.layers.11.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -476.0 / 600.0 / 0.1865096198187934 / 23.433572950537705 | [NPY](tensors/0004610.npy) |
| 4611 | `model.layers.11.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -106.5 / 120.0 / 0.04417672289742364 / 3.4805066452996547 | [NPY](tensors/0004611.npy) |
| 4612 | `model.layers.11.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -106.5 / 120.0 / 0.04417672289742364 / 3.4805066452996547 | [NPY](tensors/0004612.npy) |
| 4613 | `model.layers.11.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004613.npy) |
| 4614 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0004614.npy) |
| 4615 | `model.layers.11.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4616 | `model.layers.11.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4617 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0004617.npy) |
| 4618 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0004618.npy) |
| 4619 | `model.layers.11.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4620 | `model.layers.11.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -106.5 / 120.0 / 0.04417672289742364 / 3.4805066452996547 | [NPY](tensors/0004620.npy) |
| 4621 | `model.layers.11.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 8.8125 / 0.041400279849767685 / 1.1263800508414625 | [NPY](tensors/0004621.npy) |
| 4622 | `model.layers.11.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -106.5 / 120.0 / 0.04417672289742364 / 3.4805066452996547 | [NPY](tensors/0004622.npy) |
| 4623 | `model.layers.11.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.5 / 35.5 / 0.029936902225017548 / 3.2907580965503462 | [NPY](tensors/0004623.npy) |
| 4624 | `model.layers.11.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -106.5 / 120.0 / 0.04417672289742364 / 3.4805066452996547 | [NPY](tensors/0004624.npy) |
| 4625 | `model.layers.11.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.28125 / 5.96875 / -0.05641934275627136 / 1.929336690962855 | [NPY](tensors/0004625.npy) |
| 4626 | `model.layers.11.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.28125 / 5.75 / -0.005841808044351637 / 1.1769754699330635 | [NPY](tensors/0004626.npy) |
| 4627 | `model.layers.11.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -226.0 / 209.0 / 0.005846730536884732 / 6.972426110636413 | [NPY](tensors/0004627.npy) |
| 4628 | `model.layers.11.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -226.0 / 209.0 / 0.005846730536884732 / 6.972426110636413 | [NPY](tensors/0004628.npy) |
| 4629 | `model.layers.11.self_attn` | 39 | `output[1]` | [1, 64, 1, 326] | torch.bfloat16 → float32 | 3.808509063674137e-12 / 0.9609375 / 0.0026034798940102965 / 0.01529300359025001 | [NPY](tensors/0004629.npy) |
| 4630 | `model.layers.11.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -268.0 / 374.0 / 0.19226311577690972 / 20.534695662543395 | [NPY](tensors/0004630.npy) |
| 4631 | `model.layers.11.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.125 / 4.90625 / 0.004744505882263184 / 0.7614141254293482 | [NPY](tensors/0004631.npy) |
| 4632 | `model.layers.11.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.125 / 4.90625 / 0.004744505882263184 / 0.7614141254293482 | [NPY](tensors/0004632.npy) |
| 4633 | `model.layers.11.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.125 / 4.90625 / 0.004744505882263184 / 0.7614141254293482 | [NPY](tensors/0004633.npy) |
| 4634 | `model.layers.11.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4635 | `model.layers.11.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4636 | `model.layers.11.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4637 | `model.layers.11.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -320.0 / 272.0 / 0.10880321131812201 / 11.351898684984345 | [NPY](tensors/0004637.npy) |
| 4638 | `model.layers.11.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -320.0 / 272.0 / 0.10880321131812201 / 11.351898684984345 | [NPY](tensors/0004638.npy) |
| 4639 | `model.layers.11.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.328125 / 1.6796875 / -0.18240737915039062 / 0.8298873632996961 | [NPY](tensors/0004639.npy) |
| 4640 | `model.layers.11` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -588.0 / 648.0 / 0.3011993408203125 / 28.11802190519703 | [NPY](tensors/0004640.npy) |
| 4719 | `model.layers.11` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -576.0 / 632.0 / 0.7703403049045139 / 26.8132293978593 | [NPY](tensors/0004719.npy) |
| 4720 | `model.layers.11` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004720.npy) |
| 4721 | `model.layers.11` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0004721.npy) |
| 4722 | `model.layers.11` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0004722.npy) |
| 4723 | `model.layers.11` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0004723.npy) |
| 4724 | `model.layers.11` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4725 | `model.layers.11` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4726 | `model.layers.11` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4727 | `model.layers.11.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -576.0 / 632.0 / 0.7703403049045139 / 26.8132293978593 | [NPY](tensors/0004727.npy) |
| 4728 | `model.layers.11.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -112.5 / 110.5 / 0.06861096090740627 / 3.394083133082841 | [NPY](tensors/0004728.npy) |
| 4729 | `model.layers.11.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -112.5 / 110.5 / 0.06861096090740627 / 3.394083133082841 | [NPY](tensors/0004729.npy) |
| 4730 | `model.layers.11.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004730.npy) |
| 4731 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0004731.npy) |
| 4732 | `model.layers.11.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4733 | `model.layers.11.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4734 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0004734.npy) |
| 4735 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0004735.npy) |
| 4736 | `model.layers.11.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4737 | `model.layers.11.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -112.5 / 110.5 / 0.06861096090740627 / 3.394083133082841 | [NPY](tensors/0004737.npy) |
| 4738 | `model.layers.11.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.125 / 9.875 / 0.059954108437523246 / 1.3138258566757277 | [NPY](tensors/0004738.npy) |
| 4739 | `model.layers.11.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -112.5 / 110.5 / 0.06861096090740627 / 3.394083133082841 | [NPY](tensors/0004739.npy) |
| 4740 | `model.layers.11.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.5 / 31.5 / 0.1249038577079773 / 3.4223720294703757 | [NPY](tensors/0004740.npy) |
| 4741 | `model.layers.11.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -112.5 / 110.5 / 0.06861096090740627 / 3.394083133082841 | [NPY](tensors/0004741.npy) |
| 4742 | `model.layers.11.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.625 / 9.0 / 0.047128915786743164 / 2.7487357806702617 | [NPY](tensors/0004742.npy) |
| 4743 | `model.layers.11.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.65625 / 7.03125 / -0.019030140771064907 / 1.1746270357143884 | [NPY](tensors/0004743.npy) |
| 4744 | `model.layers.11.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -282.0 / 296.0 / -0.16947392755084567 / 8.482623833111312 | [NPY](tensors/0004744.npy) |
| 4745 | `model.layers.11.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -282.0 / 296.0 / -0.16947392755084567 / 8.482623833111312 | [NPY](tensors/0004745.npy) |
| 4746 | `model.layers.11.self_attn` | 40 | `output[1]` | [1, 64, 1, 327] | torch.bfloat16 → float32 | 1.0969003483296547e-13 / 0.9140625 / 0.002321847537999592 / 0.01747137655593118 | [NPY](tensors/0004746.npy) |
| 4747 | `model.layers.11.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -280.0 / 350.0 / 0.5992563883463542 / 22.835935239869134 | [NPY](tensors/0004747.npy) |
| 4748 | `model.layers.11.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.25 / 5.1875 / 0.010000967979431152 / 0.8216669929907346 | [NPY](tensors/0004748.npy) |
| 4749 | `model.layers.11.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.25 / 5.1875 / 0.010000967979431152 / 0.8216669929907346 | [NPY](tensors/0004749.npy) |
| 4750 | `model.layers.11.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.25 / 5.1875 / 0.010000967979431152 / 0.8216669929907346 | [NPY](tensors/0004750.npy) |
| 4751 | `model.layers.11.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4752 | `model.layers.11.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4753 | `model.layers.11.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4754 | `model.layers.11.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -374.0 / 298.0 / 0.14443512227800157 / 12.356094423978272 | [NPY](tensors/0004754.npy) |
| 4755 | `model.layers.11.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -374.0 / 298.0 / 0.14443512227800157 / 12.356094423978272 | [NPY](tensors/0004755.npy) |
| 4756 | `model.layers.11.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.4375 / 1.5859375 / -0.18448257446289062 / 0.8858412075496789 | [NPY](tensors/0004756.npy) |
| 4757 | `model.layers.11` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -656.0 / 648.0 / 0.7431603325737848 / 30.628379784164686 | [NPY](tensors/0004757.npy) |
| 4836 | `model.layers.11` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -254.0 / 490.0 / 0.7649732801649306 / 20.646502444139404 | [NPY](tensors/0004836.npy) |
| 4837 | `model.layers.11` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004837.npy) |
| 4838 | `model.layers.11` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0004838.npy) |
| 4839 | `model.layers.11` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0004839.npy) |
| 4840 | `model.layers.11` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0004840.npy) |
| 4841 | `model.layers.11` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4842 | `model.layers.11` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4843 | `model.layers.11` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4844 | `model.layers.11.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -254.0 / 490.0 / 0.7649732801649306 / 20.646502444139404 | [NPY](tensors/0004844.npy) |
| 4845 | `model.layers.11.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 111.0 / 0.09831091297997369 / 3.1084304440204247 | [NPY](tensors/0004845.npy) |
| 4846 | `model.layers.11.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 111.0 / 0.09831091297997369 / 3.1084304440204247 | [NPY](tensors/0004846.npy) |
| 4847 | `model.layers.11.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004847.npy) |
| 4848 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0004848.npy) |
| 4849 | `model.layers.11.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4850 | `model.layers.11.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4851 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0004851.npy) |
| 4852 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0004852.npy) |
| 4853 | `model.layers.11.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4854 | `model.layers.11.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 111.0 / 0.09831091297997369 / 3.1084304440204247 | [NPY](tensors/0004854.npy) |
| 4855 | `model.layers.11.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.125 / 9.1875 / 0.05367992352694273 / 1.291442121082971 | [NPY](tensors/0004855.npy) |
| 4856 | `model.layers.11.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 111.0 / 0.09831091297997369 / 3.1084304440204247 | [NPY](tensors/0004856.npy) |
| 4857 | `model.layers.11.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -26.5 / 29.5 / 0.06512679159641266 / 3.674308386822736 | [NPY](tensors/0004857.npy) |
| 4858 | `model.layers.11.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 111.0 / 0.09831091297997369 / 3.1084304440204247 | [NPY](tensors/0004858.npy) |
| 4859 | `model.layers.11.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.25 / 8.375 / 0.017824888229370117 / 2.693495942121309 | [NPY](tensors/0004859.npy) |
| 4860 | `model.layers.11.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.0 / 6.4375 / 0.0009232824668288231 / 1.3822261240874165 | [NPY](tensors/0004860.npy) |
| 4861 | `model.layers.11.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -127.0 / 118.0 / -0.06273017194535997 / 4.688613028039602 | [NPY](tensors/0004861.npy) |
| 4862 | `model.layers.11.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -127.0 / 118.0 / -0.06273017194535997 / 4.688613028039602 | [NPY](tensors/0004862.npy) |
| 4863 | `model.layers.11.self_attn` | 41 | `output[1]` | [1, 64, 1, 328] | torch.bfloat16 → float32 | 2.6147972675971687e-12 / 0.95703125 / 0.0027277986344561335 / 0.015324503982035852 | [NPY](tensors/0004863.npy) |
| 4864 | `model.layers.11.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -179.0 / 364.0 / 0.7020885891384548 / 19.84750794631758 | [NPY](tensors/0004864.npy) |
| 4865 | `model.layers.11.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.765625 / 3.1875 / 0.0255305548508962 / 0.7684891159145454 | [NPY](tensors/0004865.npy) |
| 4866 | `model.layers.11.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.765625 / 3.1875 / 0.0255305548508962 / 0.7684891159145454 | [NPY](tensors/0004866.npy) |
| 4867 | `model.layers.11.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.765625 / 3.1875 / 0.0255305548508962 / 0.7684891159145454 | [NPY](tensors/0004867.npy) |
| 4868 | `model.layers.11.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4869 | `model.layers.11.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4870 | `model.layers.11.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4871 | `model.layers.11.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -178.0 / 232.0 / 0.13541732894049752 / 8.75227001272589 | [NPY](tensors/0004871.npy) |
| 4872 | `model.layers.11.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -178.0 / 232.0 / 0.13541732894049752 / 8.75227001272589 | [NPY](tensors/0004872.npy) |
| 4873 | `model.layers.11.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.828125 / 1.015625 / -0.10306549072265625 / 0.594237695439394 | [NPY](tensors/0004873.npy) |
| 4874 | `model.layers.11` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -314.0 / 596.0 / 0.838185289171007 / 25.34868745874513 | [NPY](tensors/0004874.npy) |
| 4953 | `model.layers.11` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -236.0 / 448.0 / 0.80987548828125 / 19.744526275498345 | [NPY](tensors/0004953.npy) |
| 4954 | `model.layers.11` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004954.npy) |
| 4955 | `model.layers.11` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0004955.npy) |
| 4956 | `model.layers.11` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0004956.npy) |
| 4957 | `model.layers.11` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0004957.npy) |
| 4958 | `model.layers.11` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4959 | `model.layers.11` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4960 | `model.layers.11` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4961 | `model.layers.11.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -236.0 / 448.0 / 0.80987548828125 / 19.744526275498345 | [NPY](tensors/0004961.npy) |
| 4962 | `model.layers.11.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.75 / 106.5 / 0.10956368181440565 / 3.0359123295659494 | [NPY](tensors/0004962.npy) |
| 4963 | `model.layers.11.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.75 / 106.5 / 0.10956368181440565 / 3.0359123295659494 | [NPY](tensors/0004963.npy) |
| 4964 | `model.layers.11.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004964.npy) |
| 4965 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0004965.npy) |
| 4966 | `model.layers.11.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4967 | `model.layers.11.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4968 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0004968.npy) |
| 4969 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0004969.npy) |
| 4970 | `model.layers.11.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4971 | `model.layers.11.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.75 / 106.5 / 0.10956368181440565 / 3.0359123295659494 | [NPY](tensors/0004971.npy) |
| 4972 | `model.layers.11.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.9375 / 8.1875 / 0.045380704337731004 / 1.3598697423321733 | [NPY](tensors/0004972.npy) |
| 4973 | `model.layers.11.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.75 / 106.5 / 0.10956368181440565 / 3.0359123295659494 | [NPY](tensors/0004973.npy) |
| 4974 | `model.layers.11.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -26.375 / 31.125 / 0.09536599740386009 / 3.8414468855555617 | [NPY](tensors/0004974.npy) |
| 4975 | `model.layers.11.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.75 / 106.5 / 0.10956368181440565 / 3.0359123295659494 | [NPY](tensors/0004975.npy) |
| 4976 | `model.layers.11.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.375 / 11.375 / 0.134099543094635 / 2.7393374298613433 | [NPY](tensors/0004976.npy) |
| 4977 | `model.layers.11.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.625 / 6.9375 / 0.02793822856619954 / 1.4772223629045518 | [NPY](tensors/0004977.npy) |
| 4978 | `model.layers.11.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.0 / 79.0 / -0.024360700448354086 / 4.197685933033529 | [NPY](tensors/0004978.npy) |
| 4979 | `model.layers.11.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.0 / 79.0 / -0.024360700448354086 / 4.197685933033529 | [NPY](tensors/0004979.npy) |
| 4980 | `model.layers.11.self_attn` | 42 | `output[1]` | [1, 64, 1, 329] | torch.bfloat16 → float32 | 3.808509063674137e-12 / 0.95703125 / 0.0028334326662942124 / 0.013165434030413044 | [NPY](tensors/0004980.npy) |
| 4981 | `model.layers.11.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -157.0 / 356.0 / 0.7839725070529514 / 19.471090017891264 | [NPY](tensors/0004981.npy) |
| 4982 | `model.layers.11.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.6875 / 3.015625 / 0.03508914179272122 / 0.7718098375799015 | [NPY](tensors/0004982.npy) |
| 4983 | `model.layers.11.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.6875 / 3.015625 / 0.03508914179272122 / 0.7718098375799015 | [NPY](tensors/0004983.npy) |
| 4984 | `model.layers.11.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.6875 / 3.015625 / 0.03508914179272122 / 0.7718098375799015 | [NPY](tensors/0004984.npy) |
| 4985 | `model.layers.11.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4986 | `model.layers.11.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4987 | `model.layers.11.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4988 | `model.layers.11.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -183.0 / 185.0 / 0.15507608254750568 / 7.409291762474294 | [NPY](tensors/0004988.npy) |
| 4989 | `model.layers.11.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -183.0 / 185.0 / 0.15507608254750568 / 7.409291762474294 | [NPY](tensors/0004989.npy) |
| 4990 | `model.layers.11.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.28125 / 1.1015625 / -0.1178741455078125 / 0.7426276117675938 | [NPY](tensors/0004990.npy) |
| 4991 | `model.layers.11` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -340.0 / 540.0 / 0.9380211724175347 / 24.014154578067295 | [NPY](tensors/0004991.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -12672.0 / 14208.0 / -0.7289453935493945 / 423.63025873360414 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 287, 287] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6888605876758521e+38 / 1.6947554069517734e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 287, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8059103239704092 / 0.8702201565512877 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 287, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11909344536799918 / 0.6232883906716997 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 287] | torch.int64 → int64 | 0.0 / 286.0 / 143.0 / 82.84926070883192 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -12672.0 / 14208.0 / -0.7289453935493945 / 423.63025873360414 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 287, 2880] | torch.bfloat16 → float32 | -57.5 / 71.0 / 0.01131056575115411 / 1.7715710532034883 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 287, 2880] | torch.bfloat16 → float32 | -57.5 / 71.0 / 0.01131056575115411 / 1.7715710532034883 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 287, 287] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6888605876758521e+38 / 1.6947554069517734e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 287] | torch.int64 → int64 | 0.0 / 286.0 / 143.0 / 82.84926070883192 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 287, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8059103239704092 / 0.8702201565512877 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 287, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11909344536799918 / 0.6232883906716997 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -57.5 / 71.0 / 0.01131056575115411 / 1.7715710532034883 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 287, 4096] | torch.bfloat16 → float32 | -18.875 / 25.125 / 0.03612546554195147 / 1.6578040878760283 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -57.5 / 71.0 / 0.01131056575115411 / 1.7715710532034883 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 287, 512] | torch.bfloat16 → float32 | -77.0 / 57.0 / -0.10803555659235874 / 4.722722135134659 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -57.5 / 71.0 / 0.01131056575115411 / 1.7715710532034883 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 287, 512] | torch.bfloat16 → float32 | -21.875 / 18.25 / -0.013663769806718991 / 3.2551562299665275 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 287, 4096] | torch.bfloat16 → float32 | -19.5 / 14.75 / -0.008569967820738334 / 1.1171288995969912 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 287, 2880] | torch.bfloat16 → float32 | -4480.0 / 4832.0 / 2.172218428036408 / 140.91933349227827 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -4480.0 / 4832.0 / 2.172218428036408 / 140.91933349227827 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 287, 287] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0016616383489394 / 0.01357686016857689 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -11264.0 / 11392.0 / 1.4421809014450706 / 361.61874568580885 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 287, 2880] | torch.bfloat16 → float32 | -49.5 / 18.375 / -0.013339609077017851 / 1.209262980745412 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -49.5 / 18.375 / -0.013339609077017851 / 1.209262980745412 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [287, 2880] | torch.bfloat16 → float32 | -49.5 / 18.375 / -0.013339609077017851 / 1.209262980745412 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [287, 2880] | torch.bfloat16 → float32 | -6528.0 / 6496.0 / -1.1408556759472832 / 153.59273165106703 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 287, 2880] | torch.bfloat16 → float32 | -6528.0 / 6496.0 / -1.1408556759472832 / 153.59273165106703 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [287, 32] | torch.bfloat16 → float32 | -6.71875 / 3.859375 / 0.24075777273144872 / 2.4496209708162135 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 287, 2880] | torch.bfloat16 → float32 | -11840.0 / 12032.0 / 0.3015088230890679 / 403.3974654776465 | [NPY](tensors/0000116.npy) |
| 195 | `model.layers.23` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7808.0 / 9088.0 / 0.33146565755208335 / 375.70596427467143 | [NPY](tensors/0000195.npy) |
| 196 | `model.layers.23` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 288] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000196.npy) |
| 197 | `model.layers.23` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.6712646484375 / 0.9670054124125442 | [NPY](tensors/0000197.npy) |
| 198 | `model.layers.23` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.12011004984378815 / 0.6397178164422894 | [NPY](tensors/0000198.npy) |
| 199 | `model.layers.23` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 287.0 / 287.0 / 287.0 / 0.0 | [NPY](tensors/0000199.npy) |
| 200 | `model.layers.23` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 201 | `model.layers.23` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 202 | `model.layers.23` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 203 | `model.layers.23.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7808.0 / 9088.0 / 0.33146565755208335 / 375.70596427467143 | [NPY](tensors/0000203.npy) |
| 204 | `model.layers.23.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 65.0 / 0.020241963863372802 / 1.8162502350818008 | [NPY](tensors/0000204.npy) |
| 205 | `model.layers.23.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 65.0 / 0.020241963863372802 / 1.8162502350818008 | [NPY](tensors/0000205.npy) |
| 206 | `model.layers.23.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 288] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000206.npy) |
| 207 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 287.0 / 287.0 / 287.0 / 0.0 | [NPY](tensors/0000207.npy) |
| 208 | `model.layers.23.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 209 | `model.layers.23.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 210 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.6712646484375 / 0.9670054124125442 | [NPY](tensors/0000210.npy) |
| 211 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.12011004984378815 / 0.6397178164422894 | [NPY](tensors/0000211.npy) |
| 212 | `model.layers.23.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 213 | `model.layers.23.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 65.0 / 0.020241963863372802 / 1.8162502350818008 | [NPY](tensors/0000213.npy) |
| 214 | `model.layers.23.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.4375 / 17.5 / 0.04861951823113486 / 1.6748242326147544 | [NPY](tensors/0000214.npy) |
| 215 | `model.layers.23.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 65.0 / 0.020241963863372802 / 1.8162502350818008 | [NPY](tensors/0000215.npy) |
| 216 | `model.layers.23.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -64.5 / 45.0 / -0.004077047109603882 / 5.725439282973476 | [NPY](tensors/0000216.npy) |
| 217 | `model.layers.23.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 65.0 / 0.020241963863372802 / 1.8162502350818008 | [NPY](tensors/0000217.npy) |
| 218 | `model.layers.23.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.0 / 12.375 / -0.18544399738311768 / 3.546091647634272 | [NPY](tensors/0000218.npy) |
| 219 | `model.layers.23.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.75 / 10.0 / -0.018107936717569828 / 1.6937937930827247 | [NPY](tensors/0000219.npy) |
| 220 | `model.layers.23.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2320.0 / 2512.0 / 1.9801663928561741 / 161.7938192624586 | [NPY](tensors/0000220.npy) |
| 221 | `model.layers.23.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2320.0 / 2512.0 / 1.9801663928561741 / 161.7938192624586 | [NPY](tensors/0000221.npy) |
| 222 | `model.layers.23.self_attn` | 1 | `output[1]` | [1, 64, 1, 288] | torch.bfloat16 → float32 | 6.217248937900877e-14 / 0.8515625 / 0.002759630886649589 / 0.01947563358089361 | [NPY](tensors/0000222.npy) |
| 223 | `model.layers.23.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 6784.0 / 2.3153781467013888 / 329.1467533744155 | [NPY](tensors/0000223.npy) |
| 224 | `model.layers.23.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 13.375 / 0.00033542844984266494 / 1.339593063703759 | [NPY](tensors/0000224.npy) |
| 225 | `model.layers.23.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 13.375 / 0.00033542844984266494 / 1.339593063703759 | [NPY](tensors/0000225.npy) |
| 226 | `model.layers.23.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.5 / 13.375 / 0.00033542844984266494 / 1.339593063703759 | [NPY](tensors/0000226.npy) |
| 227 | `model.layers.23.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 228 | `model.layers.23.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 229 | `model.layers.23.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 230 | `model.layers.23.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2672.0 / 2720.0 / -2.6854932996961804 / 177.1936470669223 | [NPY](tensors/0000230.npy) |
| 231 | `model.layers.23.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2672.0 / 2720.0 / -2.6854932996961804 / 177.1936470669223 | [NPY](tensors/0000231.npy) |
| 232 | `model.layers.23.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.84375 / 2.109375 / 0.074951171875 / 1.934454077242858 | [NPY](tensors/0000232.npy) |
| 233 | `model.layers.23` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3040.0 / 4096.0 / -0.3765787760416667 / 288.5788971008131 | [NPY](tensors/0000233.npy) |
| 312 | `model.layers.23` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8640.0 / 9088.0 / 9.122878689236112 / 441.93254804238995 | [NPY](tensors/0000312.npy) |
| 313 | `model.layers.23` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 289] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000313.npy) |
| 314 | `model.layers.23` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.7242279052734375 / 0.9308467876495331 | [NPY](tensors/0000314.npy) |
| 315 | `model.layers.23` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.25 / 0.10570904612541199 / 0.6393518089241342 | [NPY](tensors/0000315.npy) |
| 316 | `model.layers.23` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 288.0 / 288.0 / 288.0 / 0.0 | [NPY](tensors/0000316.npy) |
| 317 | `model.layers.23` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 318 | `model.layers.23` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 319 | `model.layers.23` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 320 | `model.layers.23.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8640.0 / 9088.0 / 9.122878689236112 / 441.93254804238995 | [NPY](tensors/0000320.npy) |
| 321 | `model.layers.23.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 55.25 / 0.042901971605088976 / 1.7348051663169386 | [NPY](tensors/0000321.npy) |
| 322 | `model.layers.23.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 55.25 / 0.042901971605088976 / 1.7348051663169386 | [NPY](tensors/0000322.npy) |
| 323 | `model.layers.23.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 289] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000323.npy) |
| 324 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 288.0 / 288.0 / 288.0 / 0.0 | [NPY](tensors/0000324.npy) |
| 325 | `model.layers.23.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 326 | `model.layers.23.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 327 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.7242279052734375 / 0.9308467876495331 | [NPY](tensors/0000327.npy) |
| 328 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.25 / 0.10570904612541199 / 0.6393518089241342 | [NPY](tensors/0000328.npy) |
| 329 | `model.layers.23.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 330 | `model.layers.23.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 55.25 / 0.042901971605088976 / 1.7348051663169386 | [NPY](tensors/0000330.npy) |
| 331 | `model.layers.23.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.9375 / 16.875 / 0.03976271767169237 / 1.7135932827301377 | [NPY](tensors/0000331.npy) |
| 332 | `model.layers.23.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 55.25 / 0.042901971605088976 / 1.7348051663169386 | [NPY](tensors/0000332.npy) |
| 333 | `model.layers.23.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -37.0 / 34.5 / 0.06476366519927979 / 4.960992523551482 | [NPY](tensors/0000333.npy) |
| 334 | `model.layers.23.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 55.25 / 0.042901971605088976 / 1.7348051663169386 | [NPY](tensors/0000334.npy) |
| 335 | `model.layers.23.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -11.5625 / 13.125 / -0.028836965560913086 / 3.7230592603195207 | [NPY](tensors/0000335.npy) |
| 336 | `model.layers.23.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.8125 / 12.0 / 0.0732605342491297 / 1.860054023981158 | [NPY](tensors/0000336.npy) |
| 337 | `model.layers.23.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2848.0 / 2784.0 / 1.694075224134657 / 186.5839812555132 | [NPY](tensors/0000337.npy) |
| 338 | `model.layers.23.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2848.0 / 2784.0 / 1.694075224134657 / 186.5839812555132 | [NPY](tensors/0000338.npy) |
| 339 | `model.layers.23.self_attn` | 2 | `output[1]` | [1, 64, 1, 289] | torch.bfloat16 → float32 | 1.9610979506978765e-12 / 0.92578125 / 0.0023785900571433862 / 0.018418026049257456 | [NPY](tensors/0000339.npy) |
| 340 | `model.layers.23.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7360.0 / 7840.0 / 10.796761067708333 / 463.55345921721187 | [NPY](tensors/0000340.npy) |
| 341 | `model.layers.23.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 10.25 / 0.012185973591274685 / 1.4150463308887442 | [NPY](tensors/0000341.npy) |
| 342 | `model.layers.23.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 10.25 / 0.012185973591274685 / 1.4150463308887442 | [NPY](tensors/0000342.npy) |
| 343 | `model.layers.23.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.5 / 10.25 / 0.012185973591274685 / 1.4150463308887442 | [NPY](tensors/0000343.npy) |
| 344 | `model.layers.23.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 345 | `model.layers.23.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 346 | `model.layers.23.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 347 | `model.layers.23.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4640.0 / 4576.0 / -4.260834587944879 / 317.7030964824056 | [NPY](tensors/0000347.npy) |
| 348 | `model.layers.23.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4640.0 / 4576.0 / -4.260834587944879 / 317.7030964824056 | [NPY](tensors/0000348.npy) |
| 349 | `model.layers.23.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.671875 / 2.03125 / 0.07794189453125 / 1.2289659178254 | [NPY](tensors/0000349.npy) |
| 350 | `model.layers.23` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3312.0 / 3392.0 / 6.522970920138889 / 440.36504043628713 | [NPY](tensors/0000350.npy) |
| 429 | `model.layers.23` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9536.0 / -0.8630750868055556 / 428.6340739934224 | [NPY](tensors/0000429.npy) |
| 430 | `model.layers.23` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 290] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000430.npy) |
| 431 | `model.layers.23` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.76885986328125 / 0.9124536436370704 | [NPY](tensors/0000431.npy) |
| 432 | `model.layers.23` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2421875 / 0.1397949606180191 / 0.6049175711104398 | [NPY](tensors/0000432.npy) |
| 433 | `model.layers.23` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 289.0 / 289.0 / 289.0 / 0.0 | [NPY](tensors/0000433.npy) |
| 434 | `model.layers.23` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 435 | `model.layers.23` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 436 | `model.layers.23` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 437 | `model.layers.23.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9536.0 / -0.8630750868055556 / 428.6340739934224 | [NPY](tensors/0000437.npy) |
| 438 | `model.layers.23.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 59.75 / 0.010718722144762676 / 1.7830369031595852 | [NPY](tensors/0000438.npy) |
| 439 | `model.layers.23.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 59.75 / 0.010718722144762676 / 1.7830369031595852 | [NPY](tensors/0000439.npy) |
| 440 | `model.layers.23.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 290] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000440.npy) |
| 441 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 289.0 / 289.0 / 289.0 / 0.0 | [NPY](tensors/0000441.npy) |
| 442 | `model.layers.23.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 443 | `model.layers.23.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 444 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.76885986328125 / 0.9124536436370704 | [NPY](tensors/0000444.npy) |
| 445 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2421875 / 0.1397949606180191 / 0.6049175711104398 | [NPY](tensors/0000445.npy) |
| 446 | `model.layers.23.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 447 | `model.layers.23.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 59.75 / 0.010718722144762676 / 1.7830369031595852 | [NPY](tensors/0000447.npy) |
| 448 | `model.layers.23.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.8125 / 14.875 / 0.054388459073379636 / 1.449384315325895 | [NPY](tensors/0000448.npy) |
| 449 | `model.layers.23.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 59.75 / 0.010718722144762676 / 1.7830369031595852 | [NPY](tensors/0000449.npy) |
| 450 | `model.layers.23.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -54.75 / 38.75 / -0.03032657504081726 / 5.171760654738165 | [NPY](tensors/0000450.npy) |
| 451 | `model.layers.23.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 59.75 / 0.010718722144762676 / 1.7830369031595852 | [NPY](tensors/0000451.npy) |
| 452 | `model.layers.23.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.0 / 10.1875 / 0.1340862512588501 / 3.5716482663720557 | [NPY](tensors/0000452.npy) |
| 453 | `model.layers.23.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.75 / 6.84375 / 0.00280617643147707 / 1.1913475656679906 | [NPY](tensors/0000453.npy) |
| 454 | `model.layers.23.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5056.0 / 5312.0 / 6.833402718438043 / 223.9199841809536 | [NPY](tensors/0000454.npy) |
| 455 | `model.layers.23.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5056.0 / 5312.0 / 6.833402718438043 / 223.9199841809536 | [NPY](tensors/0000455.npy) |
| 456 | `model.layers.23.self_attn` | 3 | `output[1]` | [1, 64, 1, 290] | torch.bfloat16 → float32 | 1.1102230246251565e-13 / 0.81640625 / 0.0020976551527951666 / 0.011716309046022794 | [NPY](tensors/0000456.npy) |
| 457 | `model.layers.23.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 9088.0 / 5.971034071180555 / 489.0883488218766 | [NPY](tensors/0000457.npy) |
| 458 | `model.layers.23.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 9.5625 / -0.0018172038926018608 / 1.079611211662562 | [NPY](tensors/0000458.npy) |
| 459 | `model.layers.23.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 9.5625 / -0.0018172038926018608 / 1.079611211662562 | [NPY](tensors/0000459.npy) |
| 460 | `model.layers.23.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.5 / 9.5625 / -0.0018172038926018608 / 1.079611211662562 | [NPY](tensors/0000460.npy) |
| 461 | `model.layers.23.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 462 | `model.layers.23.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 463 | `model.layers.23.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 464 | `model.layers.23.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -920.0 / 1000.0 / 0.009046109517415364 / 70.11301021981778 | [NPY](tensors/0000464.npy) |
| 465 | `model.layers.23.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -920.0 / 1000.0 / 0.009046109517415364 / 70.11301021981778 | [NPY](tensors/0000465.npy) |
| 466 | `model.layers.23.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.296875 / 0.93359375 / -0.012115478515625 / 0.4681015416915412 | [NPY](tensors/0000466.npy) |
| 467 | `model.layers.23` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8448.0 / 8384.0 / 5.964095052083334 / 452.29007240968076 | [NPY](tensors/0000467.npy) |
| 546 | `model.layers.23` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10560.0 / -0.6421332465277778 / 472.2651325006035 | [NPY](tensors/0000546.npy) |
| 547 | `model.layers.23` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 291] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000547.npy) |
| 548 | `model.layers.23` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.77325439453125 / 0.9030595537086521 | [NPY](tensors/0000548.npy) |
| 549 | `model.layers.23` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2421875 / 0.19747132062911987 / 0.5978860929332719 | [NPY](tensors/0000549.npy) |
| 550 | `model.layers.23` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 290.0 / 290.0 / 290.0 / 0.0 | [NPY](tensors/0000550.npy) |
| 551 | `model.layers.23` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 552 | `model.layers.23` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 553 | `model.layers.23` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 554 | `model.layers.23.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10560.0 / -0.6421332465277778 / 472.2651325006035 | [NPY](tensors/0000554.npy) |
| 555 | `model.layers.23.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 60.0 / 0.0083024220334159 / 1.7803737780845836 | [NPY](tensors/0000555.npy) |
| 556 | `model.layers.23.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 60.0 / 0.0083024220334159 / 1.7803737780845836 | [NPY](tensors/0000556.npy) |
| 557 | `model.layers.23.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 291] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000557.npy) |
| 558 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 290.0 / 290.0 / 290.0 / 0.0 | [NPY](tensors/0000558.npy) |
| 559 | `model.layers.23.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 560 | `model.layers.23.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 561 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.77325439453125 / 0.9030595537086521 | [NPY](tensors/0000561.npy) |
| 562 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2421875 / 0.19747132062911987 / 0.5978860929332719 | [NPY](tensors/0000562.npy) |
| 563 | `model.layers.23.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 564 | `model.layers.23.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 60.0 / 0.0083024220334159 / 1.7803737780845836 | [NPY](tensors/0000564.npy) |
| 565 | `model.layers.23.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.5625 / 18.75 / 0.045207642717286944 / 1.440855859440103 | [NPY](tensors/0000565.npy) |
| 566 | `model.layers.23.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 60.0 / 0.0083024220334159 / 1.7803737780845836 | [NPY](tensors/0000566.npy) |
| 567 | `model.layers.23.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.25 / 37.75 / -0.16743247210979462 / 4.923371012686974 | [NPY](tensors/0000567.npy) |
| 568 | `model.layers.23.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 60.0 / 0.0083024220334159 / 1.7803737780845836 | [NPY](tensors/0000568.npy) |
| 569 | `model.layers.23.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.625 / 5.21875 / -0.03281724452972412 / 2.2263267494757732 | [NPY](tensors/0000569.npy) |
| 570 | `model.layers.23.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.375 / 5.03125 / -0.015663656871765852 / 0.9553823692384282 | [NPY](tensors/0000570.npy) |
| 571 | `model.layers.23.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5792.0 / 6080.0 / 6.475919723510742 / 258.321313283128 | [NPY](tensors/0000571.npy) |
| 572 | `model.layers.23.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5792.0 / 6080.0 / 6.475919723510742 / 258.321313283128 | [NPY](tensors/0000572.npy) |
| 573 | `model.layers.23.self_attn` | 4 | `output[1]` | [1, 64, 1, 291] | torch.bfloat16 → float32 | 2.4646951146678475e-14 / 0.921875 / 0.00160028294976889 / 0.01265312713764992 | [NPY](tensors/0000573.npy) |
| 574 | `model.layers.23.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 10432.0 / 5.782598198784722 / 561.0883711110721 | [NPY](tensors/0000574.npy) |
| 575 | `model.layers.23.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 8.625 / -0.007692799303266737 / 0.9758235875195274 | [NPY](tensors/0000575.npy) |
| 576 | `model.layers.23.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 8.625 / -0.007692799303266737 / 0.9758235875195274 | [NPY](tensors/0000576.npy) |
| 577 | `model.layers.23.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -35.25 / 8.625 / -0.007692799303266737 / 0.9758235875195274 | [NPY](tensors/0000577.npy) |
| 578 | `model.layers.23.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 579 | `model.layers.23.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 580 | `model.layers.23.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 581 | `model.layers.23.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1240.0 / 1208.0 / -1.5029579374525281 / 78.37448115418677 | [NPY](tensors/0000581.npy) |
| 582 | `model.layers.23.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1240.0 / 1208.0 / -1.5029579374525281 / 78.37448115418677 | [NPY](tensors/0000582.npy) |
| 583 | `model.layers.23.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.63671875 / 1.203125 / 0.08252716064453125 / 0.3221389043623389 | [NPY](tensors/0000583.npy) |
| 584 | `model.layers.23` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9664.0 / 9600.0 / 4.286330837673611 / 504.4919201180429 | [NPY](tensors/0000584.npy) |
| 663 | `model.layers.23` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9600.0 / 2.4908854166666665 / 440.3830486879125 | [NPY](tensors/0000663.npy) |
| 664 | `model.layers.23` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 292] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000664.npy) |
| 665 | `model.layers.23` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.73895263671875 / 0.9515453580587002 | [NPY](tensors/0000665.npy) |
| 666 | `model.layers.23` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.8203125 / 1.265625 / 0.2415669560432434 / 0.5473552672930101 | [NPY](tensors/0000666.npy) |
| 667 | `model.layers.23` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 291.0 / 291.0 / 291.0 / 0.0 | [NPY](tensors/0000667.npy) |
| 668 | `model.layers.23` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 669 | `model.layers.23` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 670 | `model.layers.23` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 671 | `model.layers.23.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9600.0 / 2.4908854166666665 / 440.3830486879125 | [NPY](tensors/0000671.npy) |
| 672 | `model.layers.23.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 58.5 / 0.01629934244685703 / 1.7487943454651078 | [NPY](tensors/0000672.npy) |
| 673 | `model.layers.23.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 58.5 / 0.01629934244685703 / 1.7487943454651078 | [NPY](tensors/0000673.npy) |
| 674 | `model.layers.23.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 292] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000674.npy) |
| 675 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 291.0 / 291.0 / 291.0 / 0.0 | [NPY](tensors/0000675.npy) |
| 676 | `model.layers.23.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 677 | `model.layers.23.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 678 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.73895263671875 / 0.9515453580587002 | [NPY](tensors/0000678.npy) |
| 679 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.8203125 / 1.265625 / 0.2415669560432434 / 0.5473552672930101 | [NPY](tensors/0000679.npy) |
| 680 | `model.layers.23.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 681 | `model.layers.23.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 58.5 / 0.01629934244685703 / 1.7487943454651078 | [NPY](tensors/0000681.npy) |
| 682 | `model.layers.23.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.25 / 16.5 / 0.04272046312689781 / 1.3682165794361956 | [NPY](tensors/0000682.npy) |
| 683 | `model.layers.23.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 58.5 / 0.01629934244685703 / 1.7487943454651078 | [NPY](tensors/0000683.npy) |
| 684 | `model.layers.23.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.0 / 36.0 / -0.11168612912297249 / 4.859331396829085 | [NPY](tensors/0000684.npy) |
| 685 | `model.layers.23.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 58.5 / 0.01629934244685703 / 1.7487943454651078 | [NPY](tensors/0000685.npy) |
| 686 | `model.layers.23.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.1875 / 7.3125 / -0.027801513671875 / 2.727683721121477 | [NPY](tensors/0000686.npy) |
| 687 | `model.layers.23.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.4375 / 5.03125 / 0.005334109300747514 / 1.1327822020318326 | [NPY](tensors/0000687.npy) |
| 688 | `model.layers.23.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5216.0 / 5472.0 / 6.838298543294271 / 228.67422093874768 | [NPY](tensors/0000688.npy) |
| 689 | `model.layers.23.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5216.0 / 5472.0 / 6.838298543294271 / 228.67422093874768 | [NPY](tensors/0000689.npy) |
| 690 | `model.layers.23.self_attn` | 5 | `output[1]` | [1, 64, 1, 292] | torch.bfloat16 → float32 | 1.0347278589506459e-13 / 0.859375 / 0.002391646172746934 / 0.012260745509315283 | [NPY](tensors/0000690.npy) |
| 691 | `model.layers.23.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 9088.0 / 9.315275065104167 / 497.15284020953305 | [NPY](tensors/0000691.npy) |
| 692 | `model.layers.23.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 8.5625 / 0.004805552297168308 / 0.8929495845868595 | [NPY](tensors/0000692.npy) |
| 693 | `model.layers.23.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 8.5625 / 0.004805552297168308 / 0.8929495845868595 | [NPY](tensors/0000693.npy) |
| 694 | `model.layers.23.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -28.625 / 8.5625 / 0.004805552297168308 / 0.8929495845868595 | [NPY](tensors/0000694.npy) |
| 695 | `model.layers.23.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 696 | `model.layers.23.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 697 | `model.layers.23.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 698 | `model.layers.23.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1176.0 / 1200.0 / -0.47665996021694607 / 77.40029762623766 | [NPY](tensors/0000698.npy) |
| 699 | `model.layers.23.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1176.0 / 1200.0 / -0.47665996021694607 / 77.40029762623766 | [NPY](tensors/0000699.npy) |
| 700 | `model.layers.23.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0703125 / 0.9609375 / 0.11321258544921875 / 0.43314663814728993 | [NPY](tensors/0000700.npy) |
| 701 | `model.layers.23` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7872.0 / 8000.0 / 8.84215087890625 / 443.83168333239865 | [NPY](tensors/0000701.npy) |
| 780 | `model.layers.23` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9792.0 / 9344.0 / -4.339013671875 / 456.8186955221328 | [NPY](tensors/0000780.npy) |
| 781 | `model.layers.23` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 293] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000781.npy) |
| 782 | `model.layers.23` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.6932373046875 / 1.0101839228451497 | [NPY](tensors/0000782.npy) |
| 783 | `model.layers.23` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.80078125 / 1.3203125 / 0.25535039603710175 / 0.49363048052358244 | [NPY](tensors/0000783.npy) |
| 784 | `model.layers.23` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 292.0 / 292.0 / 292.0 / 0.0 | [NPY](tensors/0000784.npy) |
| 785 | `model.layers.23` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 786 | `model.layers.23` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 787 | `model.layers.23` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 788 | `model.layers.23.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9792.0 / 9344.0 / -4.339013671875 / 456.8186955221328 | [NPY](tensors/0000788.npy) |
| 789 | `model.layers.23.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 55.0 / -0.0010478566090265909 / 1.7185787133636443 | [NPY](tensors/0000789.npy) |
| 790 | `model.layers.23.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 55.0 / -0.0010478566090265909 / 1.7185787133636443 | [NPY](tensors/0000790.npy) |
| 791 | `model.layers.23.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 293] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000791.npy) |
| 792 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 292.0 / 292.0 / 292.0 / 0.0 | [NPY](tensors/0000792.npy) |
| 793 | `model.layers.23.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 794 | `model.layers.23.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 795 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.6932373046875 / 1.0101839228451497 | [NPY](tensors/0000795.npy) |
| 796 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.80078125 / 1.3203125 / 0.25535039603710175 / 0.49363048052358244 | [NPY](tensors/0000796.npy) |
| 797 | `model.layers.23.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 798 | `model.layers.23.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 55.0 / -0.0010478566090265909 / 1.7185787133636443 | [NPY](tensors/0000798.npy) |
| 799 | `model.layers.23.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.0 / 16.125 / 0.047776758670806885 / 1.4338847301722637 | [NPY](tensors/0000799.npy) |
| 800 | `model.layers.23.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 55.0 / -0.0010478566090265909 / 1.7185787133636443 | [NPY](tensors/0000800.npy) |
| 801 | `model.layers.23.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.0 / 41.0 / -0.09481507539749146 / 4.914301550054612 | [NPY](tensors/0000801.npy) |
| 802 | `model.layers.23.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 55.0 / -0.0010478566090265909 / 1.7185787133636443 | [NPY](tensors/0000802.npy) |
| 803 | `model.layers.23.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.25 / 6.875 / -0.06063055992126465 / 2.0707078476942713 | [NPY](tensors/0000803.npy) |
| 804 | `model.layers.23.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.6875 / 5.78125 / -0.006847771466709673 / 1.012952788749682 | [NPY](tensors/0000804.npy) |
| 805 | `model.layers.23.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 5824.0 / 6.688153044382731 / 245.3416155145016 | [NPY](tensors/0000805.npy) |
| 806 | `model.layers.23.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 5824.0 / 6.688153044382731 / 245.3416155145016 | [NPY](tensors/0000806.npy) |
| 807 | `model.layers.23.self_attn` | 6 | `output[1]` | [1, 64, 1, 293] | torch.bfloat16 → float32 | 2.220446049250313e-13 / 0.87109375 / 0.002002331912620282 / 0.012515435844668335 | [NPY](tensors/0000807.npy) |
| 808 | `model.layers.23.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9984.0 / 9600.0 / 2.3396620008680555 / 547.7442984062978 | [NPY](tensors/0000808.npy) |
| 809 | `model.layers.23.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 8.6875 / -0.014727969964345297 / 0.9868363209369395 | [NPY](tensors/0000809.npy) |
| 810 | `model.layers.23.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 8.6875 / -0.014727969964345297 / 0.9868363209369395 | [NPY](tensors/0000810.npy) |
| 811 | `model.layers.23.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.5 / 8.6875 / -0.014727969964345297 / 0.9868363209369395 | [NPY](tensors/0000811.npy) |
| 812 | `model.layers.23.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 813 | `model.layers.23.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 814 | `model.layers.23.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 815 | `model.layers.23.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -960.0 / 752.0 / -0.8351694107055664 / 59.92928558925581 | [NPY](tensors/0000815.npy) |
| 816 | `model.layers.23.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -960.0 / 752.0 / -0.8351694107055664 / 59.92928558925581 | [NPY](tensors/0000816.npy) |
| 817 | `model.layers.23.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.90234375 / 1.3671875 / 0.010249137878417969 / 0.4605855245807507 | [NPY](tensors/0000817.npy) |
| 818 | `model.layers.23` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9408.0 / 9088.0 / 1.5299669053819445 / 519.2197303499158 | [NPY](tensors/0000818.npy) |
| 897 | `model.layers.23` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9984.0 / 8.2246337890625 / 478.08850404640407 | [NPY](tensors/0000897.npy) |
| 898 | `model.layers.23` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 294] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000898.npy) |
| 899 | `model.layers.23` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6579437255859375 / 0.9936083133652351 | [NPY](tensors/0000899.npy) |
| 900 | `model.layers.23` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.99609375 / 1.34375 / 0.25000885128974915 / 0.5715972585679053 | [NPY](tensors/0000900.npy) |
| 901 | `model.layers.23` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 293.0 / 293.0 / 293.0 / 0.0 | [NPY](tensors/0000901.npy) |
| 902 | `model.layers.23` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 903 | `model.layers.23` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 904 | `model.layers.23` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 905 | `model.layers.23.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9984.0 / 8.2246337890625 / 478.08850404640407 | [NPY](tensors/0000905.npy) |
| 906 | `model.layers.23.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 56.0 / 0.029832159148322213 / 1.7367226007545626 | [NPY](tensors/0000906.npy) |
| 907 | `model.layers.23.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 56.0 / 0.029832159148322213 / 1.7367226007545626 | [NPY](tensors/0000907.npy) |
| 908 | `model.layers.23.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 294] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000908.npy) |
| 909 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 293.0 / 293.0 / 293.0 / 0.0 | [NPY](tensors/0000909.npy) |
| 910 | `model.layers.23.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 911 | `model.layers.23.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 912 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6579437255859375 / 0.9936083133652351 | [NPY](tensors/0000912.npy) |
| 913 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.99609375 / 1.34375 / 0.25000885128974915 / 0.5715972585679053 | [NPY](tensors/0000913.npy) |
| 914 | `model.layers.23.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 915 | `model.layers.23.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 56.0 / 0.029832159148322213 / 1.7367226007545626 | [NPY](tensors/0000915.npy) |
| 916 | `model.layers.23.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.6875 / 14.25 / 0.040470277424901724 / 1.4004059028273894 | [NPY](tensors/0000916.npy) |
| 917 | `model.layers.23.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 56.0 / 0.029832159148322213 / 1.7367226007545626 | [NPY](tensors/0000917.npy) |
| 918 | `model.layers.23.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -55.25 / 40.75 / -0.09819227457046509 / 5.289302835992366 | [NPY](tensors/0000918.npy) |
| 919 | `model.layers.23.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 56.0 / 0.029832159148322213 / 1.7367226007545626 | [NPY](tensors/0000919.npy) |
| 920 | `model.layers.23.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.375 / 6.9375 / -0.05104506015777588 / 2.916395270849654 | [NPY](tensors/0000920.npy) |
| 921 | `model.layers.23.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.6875 / 5.9375 / 0.02189445064868778 / 1.1546450475920937 | [NPY](tensors/0000921.npy) |
| 922 | `model.layers.23.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5664.0 / 5952.0 / 7.465536541408962 / 248.60463372625483 | [NPY](tensors/0000922.npy) |
| 923 | `model.layers.23.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5664.0 / 5952.0 / 7.465536541408962 / 248.60463372625483 | [NPY](tensors/0000923.npy) |
| 924 | `model.layers.23.self_attn` | 7 | `output[1]` | [1, 64, 1, 294] | torch.bfloat16 → float32 | 1.9806378759312793e-13 / 0.8828125 / 0.0019964081478563616 / 0.01390526469769739 | [NPY](tensors/0000924.npy) |
| 925 | `model.layers.23.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 9984.0 / 15.73544921875 / 557.5931108114817 | [NPY](tensors/0000925.npy) |
| 926 | `model.layers.23.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 9.875 / 0.014900967809889051 / 0.980461328065126 | [NPY](tensors/0000926.npy) |
| 927 | `model.layers.23.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 9.875 / 0.014900967809889051 / 0.980461328065126 | [NPY](tensors/0000927.npy) |
| 928 | `model.layers.23.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.75 / 9.875 / 0.014900967809889051 / 0.980461328065126 | [NPY](tensors/0000928.npy) |
| 929 | `model.layers.23.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 930 | `model.layers.23.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 931 | `model.layers.23.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 932 | `model.layers.23.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1672.0 / 1256.0 / -0.62665769788954 / 68.47550423750388 | [NPY](tensors/0000932.npy) |
| 933 | `model.layers.23.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1672.0 / 1256.0 / -0.62665769788954 / 68.47550423750388 | [NPY](tensors/0000933.npy) |
| 934 | `model.layers.23.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.97265625 / 1.203125 / 0.09928512573242188 / 0.4382014841293817 | [NPY](tensors/0000934.npy) |
| 935 | `model.layers.23` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 9984.0 / 15.11810302734375 / 559.2995897382013 | [NPY](tensors/0000935.npy) |
| 1014 | `model.layers.23` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11264.0 / 11136.0 / 4.280368381076389 / 504.73125070950675 | [NPY](tensors/0001014.npy) |
| 1015 | `model.layers.23` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 295] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001015.npy) |
| 1016 | `model.layers.23` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.63275146484375 / 0.9803225324656689 | [NPY](tensors/0001016.npy) |
| 1017 | `model.layers.23` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.24692200124263763 / 0.6218146623522595 | [NPY](tensors/0001017.npy) |
| 1018 | `model.layers.23` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 294.0 / 294.0 / 294.0 / 0.0 | [NPY](tensors/0001018.npy) |
| 1019 | `model.layers.23` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1020 | `model.layers.23` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1021 | `model.layers.23` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1022 | `model.layers.23.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11264.0 / 11136.0 / 4.280368381076389 / 504.73125070950675 | [NPY](tensors/0001022.npy) |
| 1023 | `model.layers.23.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 59.25 / 0.014779170354207357 / 1.768375276086516 | [NPY](tensors/0001023.npy) |
| 1024 | `model.layers.23.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 59.25 / 0.014779170354207357 / 1.768375276086516 | [NPY](tensors/0001024.npy) |
| 1025 | `model.layers.23.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 295] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001025.npy) |
| 1026 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 294.0 / 294.0 / 294.0 / 0.0 | [NPY](tensors/0001026.npy) |
| 1027 | `model.layers.23.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1028 | `model.layers.23.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1029 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.63275146484375 / 0.9803225324656689 | [NPY](tensors/0001029.npy) |
| 1030 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.24692200124263763 / 0.6218146623522595 | [NPY](tensors/0001030.npy) |
| 1031 | `model.layers.23.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1032 | `model.layers.23.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 59.25 / 0.014779170354207357 / 1.768375276086516 | [NPY](tensors/0001032.npy) |
| 1033 | `model.layers.23.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.0625 / 16.375 / 0.050725618202704936 / 1.5678382859656068 | [NPY](tensors/0001033.npy) |
| 1034 | `model.layers.23.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 59.25 / 0.014779170354207357 / 1.768375276086516 | [NPY](tensors/0001034.npy) |
| 1035 | `model.layers.23.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -62.0 / 48.25 / -0.016530953347682953 / 5.595737318336516 | [NPY](tensors/0001035.npy) |
| 1036 | `model.layers.23.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 59.25 / 0.014779170354207357 / 1.768375276086516 | [NPY](tensors/0001036.npy) |
| 1037 | `model.layers.23.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.5625 / 15.0625 / 0.09318917989730835 / 3.300121948323875 | [NPY](tensors/0001037.npy) |
| 1038 | `model.layers.23.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.875 / 5.84375 / -0.002389185829088092 / 1.1902993977315972 | [NPY](tensors/0001038.npy) |
| 1039 | `model.layers.23.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5792.0 / 6080.0 / 5.994572597079807 / 254.82227521984316 | [NPY](tensors/0001039.npy) |
| 1040 | `model.layers.23.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5792.0 / 6080.0 / 5.994572597079807 / 254.82227521984316 | [NPY](tensors/0001040.npy) |
| 1041 | `model.layers.23.self_attn` | 8 | `output[1]` | [1, 64, 1, 295] | torch.bfloat16 → float32 | 5.1736392947532295e-14 / 0.9140625 / 0.0017636765427369878 / 0.0144551141712577 | [NPY](tensors/0001041.npy) |
| 1042 | `model.layers.23.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10944.0 / 10816.0 / 10.282048882378472 / 578.4506702681706 | [NPY](tensors/0001042.npy) |
| 1043 | `model.layers.23.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 11.0 / 0.0027296927240159775 / 1.1322553472937713 | [NPY](tensors/0001043.npy) |
| 1044 | `model.layers.23.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 11.0 / 0.0027296927240159775 / 1.1322553472937713 | [NPY](tensors/0001044.npy) |
| 1045 | `model.layers.23.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -46.75 / 11.0 / 0.0027296927240159775 / 1.1322553472937713 | [NPY](tensors/0001045.npy) |
| 1046 | `model.layers.23.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1047 | `model.layers.23.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1048 | `model.layers.23.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1049 | `model.layers.23.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2008.0 / 1736.0 / 0.33844405280219186 / 84.87639809832483 | [NPY](tensors/0001049.npy) |
| 1050 | `model.layers.23.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2008.0 / 1736.0 / 0.33844405280219186 / 84.87639809832483 | [NPY](tensors/0001050.npy) |
| 1051 | `model.layers.23.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.234375 / 0.953125 / 0.0996856689453125 / 0.4551385194278487 | [NPY](tensors/0001051.npy) |
| 1052 | `model.layers.23` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10816.0 / 10688.0 / 10.610804578993056 / 585.827729124041 | [NPY](tensors/0001052.npy) |
| 1131 | `model.layers.23` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9856.0 / 0.26165771484375 / 462.36970678232495 | [NPY](tensors/0001131.npy) |
| 1132 | `model.layers.23` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 296] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001132.npy) |
| 1133 | `model.layers.23` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59735107421875 / 1.0432862341497364 | [NPY](tensors/0001133.npy) |
| 1134 | `model.layers.23` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.73828125 / 1.3046875 / 0.24880489706993103 / 0.5509575399105547 | [NPY](tensors/0001134.npy) |
| 1135 | `model.layers.23` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 295.0 / 295.0 / 295.0 / 0.0 | [NPY](tensors/0001135.npy) |
| 1136 | `model.layers.23` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1137 | `model.layers.23` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1138 | `model.layers.23` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1139 | `model.layers.23.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9856.0 / 0.26165771484375 / 462.36970678232495 | [NPY](tensors/0001139.npy) |
| 1140 | `model.layers.23.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 57.25 / 0.003916455639733208 / 1.7559641044183365 | [NPY](tensors/0001140.npy) |
| 1141 | `model.layers.23.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 57.25 / 0.003916455639733208 / 1.7559641044183365 | [NPY](tensors/0001141.npy) |
| 1142 | `model.layers.23.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 296] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001142.npy) |
| 1143 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 295.0 / 295.0 / 295.0 / 0.0 | [NPY](tensors/0001143.npy) |
| 1144 | `model.layers.23.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1145 | `model.layers.23.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1146 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59735107421875 / 1.0432862341497364 | [NPY](tensors/0001146.npy) |
| 1147 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.73828125 / 1.3046875 / 0.24880489706993103 / 0.5509575399105547 | [NPY](tensors/0001147.npy) |
| 1148 | `model.layers.23.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1149 | `model.layers.23.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 57.25 / 0.003916455639733208 / 1.7559641044183365 | [NPY](tensors/0001149.npy) |
| 1150 | `model.layers.23.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.8125 / 17.25 / 0.04122823476791382 / 1.4898479216564349 | [NPY](tensors/0001150.npy) |
| 1151 | `model.layers.23.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 57.25 / 0.003916455639733208 / 1.7559641044183365 | [NPY](tensors/0001151.npy) |
| 1152 | `model.layers.23.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -57.75 / 43.25 / -0.08884054142981768 / 5.444029979792534 | [NPY](tensors/0001152.npy) |
| 1153 | `model.layers.23.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 57.25 / 0.003916455639733208 / 1.7559641044183365 | [NPY](tensors/0001153.npy) |
| 1154 | `model.layers.23.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.5625 / 10.25 / 0.09377920627593994 / 2.7577082243456914 | [NPY](tensors/0001154.npy) |
| 1155 | `model.layers.23.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.5625 / 6.28125 / 0.0017232269747182727 / 1.0717886936057266 | [NPY](tensors/0001155.npy) |
| 1156 | `model.layers.23.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 5728.0 / 6.673638105392456 / 239.3220339801549 | [NPY](tensors/0001156.npy) |
| 1157 | `model.layers.23.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 5728.0 / 6.673638105392456 / 239.3220339801549 | [NPY](tensors/0001157.npy) |
| 1158 | `model.layers.23.self_attn` | 9 | `output[1]` | [1, 64, 1, 296] | torch.bfloat16 → float32 | 5.1514348342607263e-14 / 0.90625 / 0.0017703197329352102 / 0.011632948380746326 | [NPY](tensors/0001158.npy) |
| 1159 | `model.layers.23.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9984.0 / 9728.0 / 6.957524956597222 / 538.149623395701 | [NPY](tensors/0001159.npy) |
| 1160 | `model.layers.23.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 8.5 / -0.005597858958774142 / 0.9812705806256654 | [NPY](tensors/0001160.npy) |
| 1161 | `model.layers.23.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 8.5 / -0.005597858958774142 / 0.9812705806256654 | [NPY](tensors/0001161.npy) |
| 1162 | `model.layers.23.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -35.25 / 8.5 / -0.005597858958774142 / 0.9812705806256654 | [NPY](tensors/0001162.npy) |
| 1163 | `model.layers.23.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1164 | `model.layers.23.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1165 | `model.layers.23.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1166 | `model.layers.23.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -724.0 / 712.0 / -0.015234947204589844 / 52.93787797594487 | [NPY](tensors/0001166.npy) |
| 1167 | `model.layers.23.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -724.0 / 712.0 / -0.015234947204589844 / 52.93787797594487 | [NPY](tensors/0001167.npy) |
| 1168 | `model.layers.23.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.2265625 / 0.104766845703125 / 0.4314445227067038 | [NPY](tensors/0001168.npy) |
| 1169 | `model.layers.23` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9088.0 / 6.931776258680555 / 505.2530947220169 | [NPY](tensors/0001169.npy) |
| 1248 | `model.layers.23` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11520.0 / 10368.0 / 5.835704210069444 / 511.2339317822655 | [NPY](tensors/0001248.npy) |
| 1249 | `model.layers.23` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 297] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001249.npy) |
| 1250 | `model.layers.23` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.54443359375 / 1.0951336419407118 | [NPY](tensors/0001250.npy) |
| 1251 | `model.layers.23` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.2265625 / 0.23366539180278778 / 0.5085507755708512 | [NPY](tensors/0001251.npy) |
| 1252 | `model.layers.23` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 296.0 / 296.0 / 296.0 / 0.0 | [NPY](tensors/0001252.npy) |
| 1253 | `model.layers.23` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1254 | `model.layers.23` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1255 | `model.layers.23` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1256 | `model.layers.23.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11520.0 / 10368.0 / 5.835704210069444 / 511.2339317822655 | [NPY](tensors/0001256.npy) |
| 1257 | `model.layers.23.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 54.5 / 0.025468386544121636 / 1.7251374450027197 | [NPY](tensors/0001257.npy) |
| 1258 | `model.layers.23.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 54.5 / 0.025468386544121636 / 1.7251374450027197 | [NPY](tensors/0001258.npy) |
| 1259 | `model.layers.23.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 297] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001259.npy) |
| 1260 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 296.0 / 296.0 / 296.0 / 0.0 | [NPY](tensors/0001260.npy) |
| 1261 | `model.layers.23.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1262 | `model.layers.23.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1263 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.54443359375 / 1.0951336419407118 | [NPY](tensors/0001263.npy) |
| 1264 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.2265625 / 0.23366539180278778 / 0.5085507755708512 | [NPY](tensors/0001264.npy) |
| 1265 | `model.layers.23.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1266 | `model.layers.23.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 54.5 / 0.025468386544121636 / 1.7251374450027197 | [NPY](tensors/0001266.npy) |
| 1267 | `model.layers.23.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.3125 / 14.8125 / 0.03629616927355528 / 1.3738456875530234 | [NPY](tensors/0001267.npy) |
| 1268 | `model.layers.23.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 54.5 / 0.025468386544121636 / 1.7251374450027197 | [NPY](tensors/0001268.npy) |
| 1269 | `model.layers.23.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.25 / 44.25 / -0.1766975987702608 / 5.197838610731308 | [NPY](tensors/0001269.npy) |
| 1270 | `model.layers.23.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 54.5 / 0.025468386544121636 / 1.7251374450027197 | [NPY](tensors/0001270.npy) |
| 1271 | `model.layers.23.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.25 / 8.0 / 0.014880657196044922 / 2.2864007906491977 | [NPY](tensors/0001271.npy) |
| 1272 | `model.layers.23.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.875 / 7.21875 / 0.009927047649398446 / 1.3045985757049408 | [NPY](tensors/0001272.npy) |
| 1273 | `model.layers.23.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5408.0 / 5536.0 / 7.309403726789687 / 234.80211724373433 | [NPY](tensors/0001273.npy) |
| 1274 | `model.layers.23.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5408.0 / 5536.0 / 7.309403726789687 / 234.80211724373433 | [NPY](tensors/0001274.npy) |
| 1275 | `model.layers.23.self_attn` | 10 | `output[1]` | [1, 64, 1, 297] | torch.bfloat16 → float32 | 1.7195134205394424e-12 / 0.9140625 / 0.002299548393446865 / 0.015294997637833428 | [NPY](tensors/0001275.npy) |
| 1276 | `model.layers.23.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10944.0 / 9792.0 / 13.15530056423611 / 562.9472540424555 | [NPY](tensors/0001276.npy) |
| 1277 | `model.layers.23.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 8.625 / 0.014396123091379802 / 1.0429083731205384 | [NPY](tensors/0001277.npy) |
| 1278 | `model.layers.23.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 8.625 / 0.014396123091379802 / 1.0429083731205384 | [NPY](tensors/0001278.npy) |
| 1279 | `model.layers.23.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.75 / 8.625 / 0.014396123091379802 / 1.0429083731205384 | [NPY](tensors/0001279.npy) |
| 1280 | `model.layers.23.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1281 | `model.layers.23.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1282 | `model.layers.23.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1283 | `model.layers.23.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1784.0 / 1328.0 / -0.8494963963826497 / 82.10057117989999 | [NPY](tensors/0001283.npy) |
| 1284 | `model.layers.23.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1784.0 / 1328.0 / -0.8494963963826497 / 82.10057117989999 | [NPY](tensors/0001284.npy) |
| 1285 | `model.layers.23.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.1640625 / 0.10386276245117188 / 0.5016424753228323 | [NPY](tensors/0001285.npy) |
| 1286 | `model.layers.23` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 9344.0 / 12.2880859375 / 551.7277840587956 | [NPY](tensors/0001286.npy) |
| 1365 | `model.layers.23` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11520.0 / 11328.0 / 3.196023220486111 / 524.9817239123015 | [NPY](tensors/0001365.npy) |
| 1366 | `model.layers.23` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 298] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001366.npy) |
| 1367 | `model.layers.23` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.4918212890625 / 1.117229907691466 | [NPY](tensors/0001367.npy) |
| 1368 | `model.layers.23` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.3359375 / 0.18026646971702576 / 0.5362459422402894 | [NPY](tensors/0001368.npy) |
| 1369 | `model.layers.23` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 297.0 / 297.0 / 297.0 / 0.0 | [NPY](tensors/0001369.npy) |
| 1370 | `model.layers.23` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1371 | `model.layers.23` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1372 | `model.layers.23` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1373 | `model.layers.23.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11520.0 / 11328.0 / 3.196023220486111 / 524.9817239123015 | [NPY](tensors/0001373.npy) |
| 1374 | `model.layers.23.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 58.0 / 0.018271233638127646 / 1.7456007254633874 | [NPY](tensors/0001374.npy) |
| 1375 | `model.layers.23.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 58.0 / 0.018271233638127646 / 1.7456007254633874 | [NPY](tensors/0001375.npy) |
| 1376 | `model.layers.23.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 298] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001376.npy) |
| 1377 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 297.0 / 297.0 / 297.0 / 0.0 | [NPY](tensors/0001377.npy) |
| 1378 | `model.layers.23.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1379 | `model.layers.23.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1380 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.4918212890625 / 1.117229907691466 | [NPY](tensors/0001380.npy) |
| 1381 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.3359375 / 0.18026646971702576 / 0.5362459422402894 | [NPY](tensors/0001381.npy) |
| 1382 | `model.layers.23.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1383 | `model.layers.23.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 58.0 / 0.018271233638127646 / 1.7456007254633874 | [NPY](tensors/0001383.npy) |
| 1384 | `model.layers.23.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.625 / 16.375 / 0.03301569796167314 / 1.41290597777237 | [NPY](tensors/0001384.npy) |
| 1385 | `model.layers.23.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 58.0 / 0.018271233638127646 / 1.7456007254633874 | [NPY](tensors/0001385.npy) |
| 1386 | `model.layers.23.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.75 / 37.0 / -0.19401715422281995 / 4.663164659379977 | [NPY](tensors/0001386.npy) |
| 1387 | `model.layers.23.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 58.0 / 0.018271233638127646 / 1.7456007254633874 | [NPY](tensors/0001387.npy) |
| 1388 | `model.layers.23.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -12.6875 / 8.6875 / 0.03118959069252014 / 2.0563486125159436 | [NPY](tensors/0001388.npy) |
| 1389 | `model.layers.23.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.375 / 7.5 / 0.016571798361837864 / 1.4067518866964586 | [NPY](tensors/0001389.npy) |
| 1390 | `model.layers.23.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5312.0 / 5504.0 / 6.949565082126194 / 233.4608632768673 | [NPY](tensors/0001390.npy) |
| 1391 | `model.layers.23.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5312.0 / 5504.0 / 6.949565082126194 / 233.4608632768673 | [NPY](tensors/0001391.npy) |
| 1392 | `model.layers.23.self_attn` | 11 | `output[1]` | [1, 64, 1, 298] | torch.bfloat16 → float32 | 1.2789769243681803e-13 / 0.9375 / 0.0024202752161653126 / 0.018025854989802963 | [NPY](tensors/0001392.npy) |
| 1393 | `model.layers.23.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11008.0 / 10752.0 / 10.121446397569445 / 577.5322436057983 | [NPY](tensors/0001393.npy) |
| 1394 | `model.layers.23.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 8.5625 / 0.005894810292455885 / 1.042157383639512 | [NPY](tensors/0001394.npy) |
| 1395 | `model.layers.23.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 8.5625 / 0.005894810292455885 / 1.042157383639512 | [NPY](tensors/0001395.npy) |
| 1396 | `model.layers.23.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.75 / 8.5625 / 0.005894810292455885 / 1.042157383639512 | [NPY](tensors/0001396.npy) |
| 1397 | `model.layers.23.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1398 | `model.layers.23.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1399 | `model.layers.23.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1400 | `model.layers.23.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1456.0 / 1016.0 / -0.06014874776204427 / 85.0838771621755 | [NPY](tensors/0001400.npy) |
| 1401 | `model.layers.23.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1456.0 / 1016.0 / -0.06014874776204427 / 85.0838771621755 | [NPY](tensors/0001401.npy) |
| 1402 | `model.layers.23.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.171875 / 0.057413578033447266 / 0.49501311254789065 | [NPY](tensors/0001402.npy) |
| 1403 | `model.layers.23` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9920.0 / 10.049131944444444 / 548.2931962225181 | [NPY](tensors/0001403.npy) |
| 1482 | `model.layers.23` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10176.0 / 9856.0 / 2.145828586154514 / 462.90125378188486 | [NPY](tensors/0001482.npy) |
| 1483 | `model.layers.23` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 299] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001483.npy) |
| 1484 | `model.layers.23` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.47601318359375 / 1.1300177711987256 | [NPY](tensors/0001484.npy) |
| 1485 | `model.layers.23` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2265625 / 0.09335732460021973 / 0.5447921260742894 | [NPY](tensors/0001485.npy) |
| 1486 | `model.layers.23` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 298.0 / 298.0 / 298.0 / 0.0 | [NPY](tensors/0001486.npy) |
| 1487 | `model.layers.23` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1488 | `model.layers.23` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1489 | `model.layers.23` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1490 | `model.layers.23.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10176.0 / 9856.0 / 2.145828586154514 / 462.90125378188486 | [NPY](tensors/0001490.npy) |
| 1491 | `model.layers.23.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 56.75 / 0.009821293751398723 / 1.7453889228756847 | [NPY](tensors/0001491.npy) |
| 1492 | `model.layers.23.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 56.75 / 0.009821293751398723 / 1.7453889228756847 | [NPY](tensors/0001492.npy) |
| 1493 | `model.layers.23.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 299] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001493.npy) |
| 1494 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 298.0 / 298.0 / 298.0 / 0.0 | [NPY](tensors/0001494.npy) |
| 1495 | `model.layers.23.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1496 | `model.layers.23.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1497 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.47601318359375 / 1.1300177711987256 | [NPY](tensors/0001497.npy) |
| 1498 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2265625 / 0.09335732460021973 / 0.5447921260742894 | [NPY](tensors/0001498.npy) |
| 1499 | `model.layers.23.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1500 | `model.layers.23.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 56.75 / 0.009821293751398723 / 1.7453889228756847 | [NPY](tensors/0001500.npy) |
| 1501 | `model.layers.23.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.8125 / 16.875 / 0.03695849532959983 / 1.5374764826056153 | [NPY](tensors/0001501.npy) |
| 1502 | `model.layers.23.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 56.75 / 0.009821293751398723 / 1.7453889228756847 | [NPY](tensors/0001502.npy) |
| 1503 | `model.layers.23.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.25 / 33.25 / -0.14896826446056366 / 4.5670042264232285 | [NPY](tensors/0001503.npy) |
| 1504 | `model.layers.23.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 56.75 / 0.009821293751398723 / 1.7453889228756847 | [NPY](tensors/0001504.npy) |
| 1505 | `model.layers.23.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -11.8125 / 15.25 / 0.1558298021554947 / 3.676156113267083 | [NPY](tensors/0001505.npy) |
| 1506 | `model.layers.23.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.125 / 8.125 / 0.01761428569443524 / 1.225573363690161 | [NPY](tensors/0001506.npy) |
| 1507 | `model.layers.23.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5024.0 / 5216.0 / 6.581413014729818 / 219.12335483981897 | [NPY](tensors/0001507.npy) |
| 1508 | `model.layers.23.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5024.0 / 5216.0 / 6.581413014729818 / 219.12335483981897 | [NPY](tensors/0001508.npy) |
| 1509 | `model.layers.23.self_attn` | 12 | `output[1]` | [1, 64, 1, 299] | torch.bfloat16 → float32 | 1.4033219031261979e-13 / 0.91015625 / 0.00203947955627242 / 0.013871237293553633 | [NPY](tensors/0001509.npy) |
| 1510 | `model.layers.23.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9216.0 / 8.709060329861112 / 507.40435218683973 | [NPY](tensors/0001510.npy) |
| 1511 | `model.layers.23.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 9.3125 / 0.0020846101972791884 / 1.0204813083310504 | [NPY](tensors/0001511.npy) |
| 1512 | `model.layers.23.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 9.3125 / 0.0020846101972791884 / 1.0204813083310504 | [NPY](tensors/0001512.npy) |
| 1513 | `model.layers.23.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -35.25 / 9.3125 / 0.0020846101972791884 / 1.0204813083310504 | [NPY](tensors/0001513.npy) |
| 1514 | `model.layers.23.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1515 | `model.layers.23.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1516 | `model.layers.23.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1517 | `model.layers.23.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -892.0 / 474.0 / -0.3076225068834093 / 49.52353221623546 | [NPY](tensors/0001517.npy) |
| 1518 | `model.layers.23.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -892.0 / 474.0 / -0.3076225068834093 / 49.52353221623546 | [NPY](tensors/0001518.npy) |
| 1519 | `model.layers.23.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.1953125 / 0.1459197998046875 / 0.4779996949188747 | [NPY](tensors/0001519.npy) |
| 1520 | `model.layers.23` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 8704.0 / 8.386908637152779 / 490.233054214003 | [NPY](tensors/0001520.npy) |
| 1599 | `model.layers.23` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 9728.0 / -2.857834201388889 / 450.81575224116773 | [NPY](tensors/0001599.npy) |
| 1600 | `model.layers.23` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 300] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001600.npy) |
| 1601 | `model.layers.23` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.518310546875 / 1.0946292885024063 | [NPY](tensors/0001601.npy) |
| 1602 | `model.layers.23` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.234375 / 0.009437993168830872 / 0.5857162614275052 | [NPY](tensors/0001602.npy) |
| 1603 | `model.layers.23` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 299.0 / 299.0 / 299.0 / 0.0 | [NPY](tensors/0001603.npy) |
| 1604 | `model.layers.23` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1605 | `model.layers.23` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1606 | `model.layers.23` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1607 | `model.layers.23.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 9728.0 / -2.857834201388889 / 450.81575224116773 | [NPY](tensors/0001607.npy) |
| 1608 | `model.layers.23.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 55.0 / 0.0037592689196268717 / 1.7476615696385231 | [NPY](tensors/0001608.npy) |
| 1609 | `model.layers.23.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 55.0 / 0.0037592689196268717 / 1.7476615696385231 | [NPY](tensors/0001609.npy) |
| 1610 | `model.layers.23.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 300] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001610.npy) |
| 1611 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 299.0 / 299.0 / 299.0 / 0.0 | [NPY](tensors/0001611.npy) |
| 1612 | `model.layers.23.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1613 | `model.layers.23.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1614 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.518310546875 / 1.0946292885024063 | [NPY](tensors/0001614.npy) |
| 1615 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.234375 / 0.009437993168830872 / 0.5857162614275052 | [NPY](tensors/0001615.npy) |
| 1616 | `model.layers.23.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1617 | `model.layers.23.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 55.0 / 0.0037592689196268717 / 1.7476615696385231 | [NPY](tensors/0001617.npy) |
| 1618 | `model.layers.23.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.6875 / 14.5625 / 0.03578981081955135 / 1.4105983469889238 | [NPY](tensors/0001618.npy) |
| 1619 | `model.layers.23.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 55.0 / 0.0037592689196268717 / 1.7476615696385231 | [NPY](tensors/0001619.npy) |
| 1620 | `model.layers.23.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -47.75 / 46.75 / -0.100441113114357 / 5.315341984796742 | [NPY](tensors/0001620.npy) |
| 1621 | `model.layers.23.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 55.0 / 0.0037592689196268717 / 1.7476615696385231 | [NPY](tensors/0001621.npy) |
| 1622 | `model.layers.23.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -12.9375 / 8.4375 / 0.04632973670959473 / 2.2238957254231964 | [NPY](tensors/0001622.npy) |
| 1623 | `model.layers.23.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.125 / 8.0 / 0.006392502458766103 / 1.3142328549447793 | [NPY](tensors/0001623.npy) |
| 1624 | `model.layers.23.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5568.0 / 5856.0 / 7.264398913913303 / 250.30501096850475 | [NPY](tensors/0001624.npy) |
| 1625 | `model.layers.23.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5568.0 / 5856.0 / 7.264398913913303 / 250.30501096850475 | [NPY](tensors/0001625.npy) |
| 1626 | `model.layers.23.self_attn` | 13 | `output[1]` | [1, 64, 1, 300] | torch.bfloat16 → float32 | 8.668621376273222e-13 / 0.859375 / 0.0024501228733541398 / 0.0141692554030151 | [NPY](tensors/0001626.npy) |
| 1627 | `model.layers.23.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 9792.0 / 4.423942057291667 / 536.2207687020566 | [NPY](tensors/0001627.npy) |
| 1628 | `model.layers.23.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.25 / 8.1875 / -0.009336645073360867 / 1.0055267276684536 | [NPY](tensors/0001628.npy) |
| 1629 | `model.layers.23.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.25 / 8.1875 / -0.009336645073360867 / 1.0055267276684536 | [NPY](tensors/0001629.npy) |
| 1630 | `model.layers.23.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.25 / 8.1875 / -0.009336645073360867 / 1.0055267276684536 | [NPY](tensors/0001630.npy) |
| 1631 | `model.layers.23.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1632 | `model.layers.23.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1633 | `model.layers.23.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1634 | `model.layers.23.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -788.0 / 792.0 / -0.769378662109375 / 62.28229649407618 | [NPY](tensors/0001634.npy) |
| 1635 | `model.layers.23.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -788.0 / 792.0 / -0.769378662109375 / 62.28229649407618 | [NPY](tensors/0001635.npy) |
| 1636 | `model.layers.23.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.72265625 / 1.375 / 0.020129680633544922 / 0.454059451768366 | [NPY](tensors/0001636.npy) |
| 1637 | `model.layers.23` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9664.0 / 9088.0 / 3.6546223958333335 / 506.3503731614025 | [NPY](tensors/0001637.npy) |
| 1716 | `model.layers.23` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 10496.0 / -2.8211371527777778 / 503.6303651249272 | [NPY](tensors/0001716.npy) |
| 1717 | `model.layers.23` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 301] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001717.npy) |
| 1718 | `model.layers.23` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6011199951171875 / 1.029134772776266 | [NPY](tensors/0001718.npy) |
| 1719 | `model.layers.23` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.02744269371032715 / 0.6241199078176489 | [NPY](tensors/0001719.npy) |
| 1720 | `model.layers.23` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 300.0 / 300.0 / 300.0 / 0.0 | [NPY](tensors/0001720.npy) |
| 1721 | `model.layers.23` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1722 | `model.layers.23` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1723 | `model.layers.23` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1724 | `model.layers.23.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 10496.0 / -2.8211371527777778 / 503.6303651249272 | [NPY](tensors/0001724.npy) |
| 1725 | `model.layers.23.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 56.0 / 0.0036805974112616643 / 1.7265857761279022 | [NPY](tensors/0001725.npy) |
| 1726 | `model.layers.23.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 56.0 / 0.0036805974112616643 / 1.7265857761279022 | [NPY](tensors/0001726.npy) |
| 1727 | `model.layers.23.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 301] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001727.npy) |
| 1728 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 300.0 / 300.0 / 300.0 / 0.0 | [NPY](tensors/0001728.npy) |
| 1729 | `model.layers.23.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1730 | `model.layers.23.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1731 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6011199951171875 / 1.029134772776266 | [NPY](tensors/0001731.npy) |
| 1732 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.02744269371032715 / 0.6241199078176489 | [NPY](tensors/0001732.npy) |
| 1733 | `model.layers.23.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1734 | `model.layers.23.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 56.0 / 0.0036805974112616643 / 1.7265857761279022 | [NPY](tensors/0001734.npy) |
| 1735 | `model.layers.23.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.875 / 16.75 / 0.03824830602388829 / 1.441833171862935 | [NPY](tensors/0001735.npy) |
| 1736 | `model.layers.23.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 56.0 / 0.0036805974112616643 / 1.7265857761279022 | [NPY](tensors/0001736.npy) |
| 1737 | `model.layers.23.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.25 / 41.25 / -0.138840539380908 / 4.724908996831201 | [NPY](tensors/0001737.npy) |
| 1738 | `model.layers.23.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 56.0 / 0.0036805974112616643 / 1.7265857761279022 | [NPY](tensors/0001738.npy) |
| 1739 | `model.layers.23.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.375 / 9.25 / 0.03691871464252472 / 2.8079528323438145 | [NPY](tensors/0001739.npy) |
| 1740 | `model.layers.23.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.1875 / 8.0625 / -0.009522524429485202 / 1.0419359721214367 | [NPY](tensors/0001740.npy) |
| 1741 | `model.layers.23.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5440.0 / 5760.0 / 5.520797411600749 / 242.0480963447877 | [NPY](tensors/0001741.npy) |
| 1742 | `model.layers.23.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5440.0 / 5760.0 / 5.520797411600749 / 242.0480963447877 | [NPY](tensors/0001742.npy) |
| 1743 | `model.layers.23.self_attn` | 14 | `output[1]` | [1, 64, 1, 301] | torch.bfloat16 → float32 | 8.715250743307479e-15 / 0.8828125 / 0.0017437363402023171 / 0.011028116548287354 | [NPY](tensors/0001743.npy) |
| 1744 | `model.layers.23.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 10624.0 / 2.7130777994791666 / 580.3044803387273 | [NPY](tensors/0001744.npy) |
| 1745 | `model.layers.23.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 8.75 / -0.01607984436882867 / 1.1301714616576948 | [NPY](tensors/0001745.npy) |
| 1746 | `model.layers.23.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 8.75 / -0.01607984436882867 / 1.1301714616576948 | [NPY](tensors/0001746.npy) |
| 1747 | `model.layers.23.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -40.25 / 8.75 / -0.01607984436882867 / 1.1301714616576948 | [NPY](tensors/0001747.npy) |
| 1748 | `model.layers.23.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1749 | `model.layers.23.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1750 | `model.layers.23.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1751 | `model.layers.23.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1288.0 / 896.0 / -0.990130254957411 / 62.18551584530125 | [NPY](tensors/0001751.npy) |
| 1752 | `model.layers.23.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1288.0 / 896.0 / -0.990130254957411 / 62.18551584530125 | [NPY](tensors/0001752.npy) |
| 1753 | `model.layers.23.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.09375 / 1.4140625 / 0.02752220630645752 / 0.5127738389308125 | [NPY](tensors/0001753.npy) |
| 1754 | `model.layers.23` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 10304.0 / 1.7253472222222221 / 572.1739619899274 | [NPY](tensors/0001754.npy) |
| 1833 | `model.layers.23` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11776.0 / 10496.0 / 4.506315104166666 / 501.2543373130852 | [NPY](tensors/0001833.npy) |
| 1834 | `model.layers.23` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 302] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001834.npy) |
| 1835 | `model.layers.23` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6781768798828125 / 0.9972778713983161 | [NPY](tensors/0001835.npy) |
| 1836 | `model.layers.23` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.0019666850566864014 / 0.5958225425092146 | [NPY](tensors/0001836.npy) |
| 1837 | `model.layers.23` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 301.0 / 301.0 / 301.0 / 0.0 | [NPY](tensors/0001837.npy) |
| 1838 | `model.layers.23` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1839 | `model.layers.23` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1840 | `model.layers.23` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1841 | `model.layers.23.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11776.0 / 10496.0 / 4.506315104166666 / 501.2543373130852 | [NPY](tensors/0001841.npy) |
| 1842 | `model.layers.23.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 56.25 / 0.01943771309322781 / 1.754698524363743 | [NPY](tensors/0001842.npy) |
| 1843 | `model.layers.23.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 56.25 / 0.01943771309322781 / 1.754698524363743 | [NPY](tensors/0001843.npy) |
| 1844 | `model.layers.23.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 302] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001844.npy) |
| 1845 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 301.0 / 301.0 / 301.0 / 0.0 | [NPY](tensors/0001845.npy) |
| 1846 | `model.layers.23.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1847 | `model.layers.23.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1848 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6781768798828125 / 0.9972778713983161 | [NPY](tensors/0001848.npy) |
| 1849 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.0019666850566864014 / 0.5958225425092146 | [NPY](tensors/0001849.npy) |
| 1850 | `model.layers.23.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1851 | `model.layers.23.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 56.25 / 0.01943771309322781 / 1.754698524363743 | [NPY](tensors/0001851.npy) |
| 1852 | `model.layers.23.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.625 / 15.8125 / 0.04900377994636074 / 1.3942292615429217 | [NPY](tensors/0001852.npy) |
| 1853 | `model.layers.23.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 56.25 / 0.01943771309322781 / 1.754698524363743 | [NPY](tensors/0001853.npy) |
| 1854 | `model.layers.23.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.5 / 42.25 / -0.1531015019863844 / 5.203634454897972 | [NPY](tensors/0001854.npy) |
| 1855 | `model.layers.23.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 56.25 / 0.01943771309322781 / 1.754698524363743 | [NPY](tensors/0001855.npy) |
| 1856 | `model.layers.23.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -12.75 / 8.5 / 0.05157426372170448 / 3.2723256846158044 | [NPY](tensors/0001856.npy) |
| 1857 | `model.layers.23.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.9375 / 6.34375 / 0.020713128586066887 / 1.1665522693121193 | [NPY](tensors/0001857.npy) |
| 1858 | `model.layers.23.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5248.0 / 5536.0 / 7.725572882758247 / 230.92396525357188 | [NPY](tensors/0001858.npy) |
| 1859 | `model.layers.23.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5248.0 / 5536.0 / 7.725572882758247 / 230.92396525357188 | [NPY](tensors/0001859.npy) |
| 1860 | `model.layers.23.self_attn` | 15 | `output[1]` | [1, 64, 1, 302] | torch.bfloat16 → float32 | 1.5126788710517758e-15 / 0.8828125 / 0.0018027613906737385 / 0.012836998181074333 | [NPY](tensors/0001860.npy) |
| 1861 | `model.layers.23.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11200.0 / 9920.0 / 12.220567491319445 / 556.0917910132746 | [NPY](tensors/0001861.npy) |
| 1862 | `model.layers.23.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 10.1875 / 0.013684231705135769 / 1.037044768652613 | [NPY](tensors/0001862.npy) |
| 1863 | `model.layers.23.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 10.1875 / 0.013684231705135769 / 1.037044768652613 | [NPY](tensors/0001863.npy) |
| 1864 | `model.layers.23.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.75 / 10.1875 / 0.013684231705135769 / 1.037044768652613 | [NPY](tensors/0001864.npy) |
| 1865 | `model.layers.23.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1866 | `model.layers.23.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1867 | `model.layers.23.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1868 | `model.layers.23.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1296.0 / 1320.0 / -1.0156101438734266 / 89.8955648400206 | [NPY](tensors/0001868.npy) |
| 1869 | `model.layers.23.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1296.0 / 1320.0 / -1.0156101438734266 / 89.8955648400206 | [NPY](tensors/0001869.npy) |
| 1870 | `model.layers.23.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.1171875 / 0.1443328857421875 / 0.46991307462623527 | [NPY](tensors/0001870.npy) |
| 1871 | `model.layers.23` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9984.0 / 8832.0 / 11.182661946614584 / 503.87768295769087 | [NPY](tensors/0001871.npy) |
| 1950 | `model.layers.23` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 9536.0 / 0.23135308159722223 / 445.7797620762427 | [NPY](tensors/0001950.npy) |
| 1951 | `model.layers.23` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 303] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001951.npy) |
| 1952 | `model.layers.23` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.707061767578125 / 0.9717983302810768 | [NPY](tensors/0001952.npy) |
| 1953 | `model.layers.23` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.234375 / 0.05849510431289673 / 0.601804974311013 | [NPY](tensors/0001953.npy) |
| 1954 | `model.layers.23` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 302.0 / 302.0 / 302.0 / 0.0 | [NPY](tensors/0001954.npy) |
| 1955 | `model.layers.23` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1956 | `model.layers.23` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1957 | `model.layers.23` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1958 | `model.layers.23.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 9536.0 / 0.23135308159722223 / 445.7797620762427 | [NPY](tensors/0001958.npy) |
| 1959 | `model.layers.23.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 55.5 / 0.0036676154368453554 / 1.7452219970262535 | [NPY](tensors/0001959.npy) |
| 1960 | `model.layers.23.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 55.5 / 0.0036676154368453554 / 1.7452219970262535 | [NPY](tensors/0001960.npy) |
| 1961 | `model.layers.23.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 303] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001961.npy) |
| 1962 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 302.0 / 302.0 / 302.0 / 0.0 | [NPY](tensors/0001962.npy) |
| 1963 | `model.layers.23.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1964 | `model.layers.23.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1965 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.707061767578125 / 0.9717983302810768 | [NPY](tensors/0001965.npy) |
| 1966 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.234375 / 0.05849510431289673 / 0.601804974311013 | [NPY](tensors/0001966.npy) |
| 1967 | `model.layers.23.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1968 | `model.layers.23.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 55.5 / 0.0036676154368453554 / 1.7452219970262535 | [NPY](tensors/0001968.npy) |
| 1969 | `model.layers.23.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.0625 / 17.375 / 0.040322088869288564 / 1.509463357063177 | [NPY](tensors/0001969.npy) |
| 1970 | `model.layers.23.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 55.5 / 0.0036676154368453554 / 1.7452219970262535 | [NPY](tensors/0001970.npy) |
| 1971 | `model.layers.23.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.5 / 36.0 / -0.12746742367744446 / 4.895451231934336 | [NPY](tensors/0001971.npy) |
| 1972 | `model.layers.23.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 55.5 / 0.0036676154368453554 / 1.7452219970262535 | [NPY](tensors/0001972.npy) |
| 1973 | `model.layers.23.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -12.875 / 12.125 / 0.05327010154724121 / 3.35671958835791 | [NPY](tensors/0001973.npy) |
| 1974 | `model.layers.23.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.0625 / 6.59375 / 0.013561097090132535 / 1.1610253667991386 | [NPY](tensors/0001974.npy) |
| 1975 | `model.layers.23.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5280.0 / 5600.0 / 6.747523583306206 / 232.81152177663284 | [NPY](tensors/0001975.npy) |
| 1976 | `model.layers.23.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5280.0 / 5600.0 / 6.747523583306206 / 232.81152177663284 | [NPY](tensors/0001976.npy) |
| 1977 | `model.layers.23.self_attn` | 16 | `output[1]` | [1, 64, 1, 303] | torch.bfloat16 → float32 | 1.6479873021779667e-16 / 0.91015625 / 0.0016249384568614417 / 0.012335462631062364 | [NPY](tensors/0001977.npy) |
| 1978 | `model.layers.23.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9792.0 / 9280.0 / 6.966379801432292 / 509.80319642780404 | [NPY](tensors/0001978.npy) |
| 1979 | `model.layers.23.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 9.3125 / -0.001836475067668491 / 1.0336893451812628 | [NPY](tensors/0001979.npy) |
| 1980 | `model.layers.23.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 9.3125 / -0.001836475067668491 / 1.0336893451812628 | [NPY](tensors/0001980.npy) |
| 1981 | `model.layers.23.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.25 / 9.3125 / -0.001836475067668491 / 1.0336893451812628 | [NPY](tensors/0001981.npy) |
| 1982 | `model.layers.23.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1983 | `model.layers.23.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1984 | `model.layers.23.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1985 | `model.layers.23.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -832.0 / 576.0 / -1.071091482374403 / 52.00752097144334 | [NPY](tensors/0001985.npy) |
| 1986 | `model.layers.23.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -832.0 / 576.0 / -1.071091482374403 / 52.00752097144334 | [NPY](tensors/0001986.npy) |
| 1987 | `model.layers.23.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0859375 / 1.1953125 / 0.15019917488098145 / 0.44754944687476994 | [NPY](tensors/0001987.npy) |
| 1988 | `model.layers.23` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9280.0 / 8640.0 / 5.886626519097222 / 488.21443953534555 | [NPY](tensors/0001988.npy) |
| 2067 | `model.layers.23` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11072.0 / 9856.0 / -2.4597791883680555 / 476.43400886629587 | [NPY](tensors/0002067.npy) |
| 2068 | `model.layers.23` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 304] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002068.npy) |
| 2069 | `model.layers.23` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.68243408203125 / 0.9684034292887866 | [NPY](tensors/0002069.npy) |
| 2070 | `model.layers.23` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3359375 / 0.10489383339881897 / 0.6297841334602801 | [NPY](tensors/0002070.npy) |
| 2071 | `model.layers.23` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 303.0 / 303.0 / 303.0 / 0.0 | [NPY](tensors/0002071.npy) |
| 2072 | `model.layers.23` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2073 | `model.layers.23` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2074 | `model.layers.23` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2075 | `model.layers.23.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11072.0 / 9856.0 / -2.4597791883680555 / 476.43400886629587 | [NPY](tensors/0002075.npy) |
| 2076 | `model.layers.23.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 52.75 / 0.004983091354370117 / 1.7373939407034003 | [NPY](tensors/0002076.npy) |
| 2077 | `model.layers.23.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 52.75 / 0.004983091354370117 / 1.7373939407034003 | [NPY](tensors/0002077.npy) |
| 2078 | `model.layers.23.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 304] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002078.npy) |
| 2079 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 303.0 / 303.0 / 303.0 / 0.0 | [NPY](tensors/0002079.npy) |
| 2080 | `model.layers.23.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2081 | `model.layers.23.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2082 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.68243408203125 / 0.9684034292887866 | [NPY](tensors/0002082.npy) |
| 2083 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3359375 / 0.10489383339881897 / 0.6297841334602801 | [NPY](tensors/0002083.npy) |
| 2084 | `model.layers.23.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2085 | `model.layers.23.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 52.75 / 0.004983091354370117 / 1.7373939407034003 | [NPY](tensors/0002085.npy) |
| 2086 | `model.layers.23.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 14.0625 / 0.0351551272906363 / 1.420648235936507 | [NPY](tensors/0002086.npy) |
| 2087 | `model.layers.23.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 52.75 / 0.004983091354370117 / 1.7373939407034003 | [NPY](tensors/0002087.npy) |
| 2088 | `model.layers.23.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.0 / 41.5 / -0.11948981136083603 / 5.191384215549177 | [NPY](tensors/0002088.npy) |
| 2089 | `model.layers.23.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 52.75 / 0.004983091354370117 / 1.7373939407034003 | [NPY](tensors/0002089.npy) |
| 2090 | `model.layers.23.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.0 / 7.3125 / -0.03358165919780731 / 2.3947029600127845 | [NPY](tensors/0002090.npy) |
| 2091 | `model.layers.23.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.625 / 11.6875 / 0.021581233479082584 / 1.5500532093341297 | [NPY](tensors/0002091.npy) |
| 2092 | `model.layers.23.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6048.0 / 6112.0 / 6.516221703423394 / 271.7171263376025 | [NPY](tensors/0002092.npy) |
| 2093 | `model.layers.23.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6048.0 / 6112.0 / 6.516221703423394 / 271.7171263376025 | [NPY](tensors/0002093.npy) |
| 2094 | `model.layers.23.self_attn` | 17 | `output[1]` | [1, 64, 1, 304] | torch.bfloat16 → float32 | 3.8191672047105385e-14 / 0.9765625 / 0.002586773879358569 / 0.015643526431547334 | [NPY](tensors/0002094.npy) |
| 2095 | `model.layers.23.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11008.0 / 9856.0 / 4.062215169270833 / 568.7510510442646 | [NPY](tensors/0002095.npy) |
| 2096 | `model.layers.23.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 9.375 / -0.008515258630116781 / 1.099102845773443 | [NPY](tensors/0002096.npy) |
| 2097 | `model.layers.23.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 9.375 / -0.008515258630116781 / 1.099102845773443 | [NPY](tensors/0002097.npy) |
| 2098 | `model.layers.23.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.5 / 9.375 / -0.008515258630116781 / 1.099102845773443 | [NPY](tensors/0002098.npy) |
| 2099 | `model.layers.23.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2100 | `model.layers.23.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2101 | `model.layers.23.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2102 | `model.layers.23.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1496.0 / 1376.0 / -3.0685351053873697 / 84.72461004580681 | [NPY](tensors/0002102.npy) |
| 2103 | `model.layers.23.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1496.0 / 1376.0 / -3.0685351053873697 / 84.72461004580681 | [NPY](tensors/0002103.npy) |
| 2104 | `model.layers.23.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.1015625 / 1.21875 / 0.012947142124176025 / 0.43229251489172393 | [NPY](tensors/0002104.npy) |
| 2105 | `model.layers.23` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10944.0 / 9920.0 / 1.0192491319444446 / 584.3190587638287 | [NPY](tensors/0002105.npy) |
| 2184 | `model.layers.23` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9792.0 / 9984.0 / -2.585956488715278 / 429.583718210116 | [NPY](tensors/0002184.npy) |
| 2185 | `model.layers.23` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 305] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002185.npy) |
| 2186 | `model.layers.23` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6405029296875 / 1.0356892994687845 | [NPY](tensors/0002186.npy) |
| 2187 | `model.layers.23` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1875 / 1.2421875 / 0.10542488098144531 / 0.5631099040524371 | [NPY](tensors/0002187.npy) |
| 2188 | `model.layers.23` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 304.0 / 304.0 / 304.0 / 0.0 | [NPY](tensors/0002188.npy) |
| 2189 | `model.layers.23` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2190 | `model.layers.23` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2191 | `model.layers.23` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2192 | `model.layers.23.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9792.0 / 9984.0 / -2.585956488715278 / 429.583718210116 | [NPY](tensors/0002192.npy) |
| 2193 | `model.layers.23.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 62.5 / 0.012248722712198894 / 1.8158544190982036 | [NPY](tensors/0002193.npy) |
| 2194 | `model.layers.23.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 62.5 / 0.012248722712198894 / 1.8158544190982036 | [NPY](tensors/0002194.npy) |
| 2195 | `model.layers.23.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 305] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002195.npy) |
| 2196 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 304.0 / 304.0 / 304.0 / 0.0 | [NPY](tensors/0002196.npy) |
| 2197 | `model.layers.23.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2198 | `model.layers.23.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2199 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6405029296875 / 1.0356892994687845 | [NPY](tensors/0002199.npy) |
| 2200 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1875 / 1.2421875 / 0.10542488098144531 / 0.5631099040524371 | [NPY](tensors/0002200.npy) |
| 2201 | `model.layers.23.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2202 | `model.layers.23.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 62.5 / 0.012248722712198894 / 1.8158544190982036 | [NPY](tensors/0002202.npy) |
| 2203 | `model.layers.23.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.6875 / 17.5 / 0.05687012942507863 / 1.647493772828879 | [NPY](tensors/0002203.npy) |
| 2204 | `model.layers.23.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 62.5 / 0.012248722712198894 / 1.8158544190982036 | [NPY](tensors/0002204.npy) |
| 2205 | `model.layers.23.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.0 / 35.0 / -0.103984534740448 / 4.729015868691042 | [NPY](tensors/0002205.npy) |
| 2206 | `model.layers.23.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 62.5 / 0.012248722712198894 / 1.8158544190982036 | [NPY](tensors/0002206.npy) |
| 2207 | `model.layers.23.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.1875 / 14.3125 / 0.0743023157119751 / 3.665098958001479 | [NPY](tensors/0002207.npy) |
| 2208 | `model.layers.23.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.5 / 8.0 / 0.05621710140258074 / 1.3838705937287767 | [NPY](tensors/0002208.npy) |
| 2209 | `model.layers.23.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3152.0 / 3024.0 / 2.0548837502797443 / 163.67610324028013 | [NPY](tensors/0002209.npy) |
| 2210 | `model.layers.23.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3152.0 / 3024.0 / 2.0548837502797443 / 163.67610324028013 | [NPY](tensors/0002210.npy) |
| 2211 | `model.layers.23.self_attn` | 18 | `output[1]` | [1, 64, 1, 305] | torch.bfloat16 → float32 | 2.123301534595612e-15 / 0.96484375 / 0.0022798485610654264 / 0.01463891321219122 | [NPY](tensors/0002211.npy) |
| 2212 | `model.layers.23.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7904.0 / 7936.0 / -0.5319552951388888 / 405.08098026052136 | [NPY](tensors/0002212.npy) |
| 2213 | `model.layers.23.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 8.9375 / -0.020220159159766302 / 1.2373119171187021 | [NPY](tensors/0002213.npy) |
| 2214 | `model.layers.23.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 8.9375 / -0.020220159159766302 / 1.2373119171187021 | [NPY](tensors/0002214.npy) |
| 2215 | `model.layers.23.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.0 / 8.9375 / -0.020220159159766302 / 1.2373119171187021 | [NPY](tensors/0002215.npy) |
| 2216 | `model.layers.23.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2217 | `model.layers.23.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2218 | `model.layers.23.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2219 | `model.layers.23.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4864.0 / 4736.0 / -4.921131282382541 / 238.23928217543272 | [NPY](tensors/0002219.npy) |
| 2220 | `model.layers.23.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4864.0 / 4736.0 / -4.921131282382541 / 238.23928217543272 | [NPY](tensors/0002220.npy) |
| 2221 | `model.layers.23.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.640625 / 1.140625 / -0.03165435791015625 / 0.9293049991339439 | [NPY](tensors/0002221.npy) |
| 2222 | `model.layers.23` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3328.0 / 3072.0 / -5.438529459635417 / 286.31508209594335 | [NPY](tensors/0002222.npy) |
| 2301 | `model.layers.23` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10752.0 / 10752.0 / 0.25910373263888886 / 454.4602721229703 | [NPY](tensors/0002301.npy) |
| 2302 | `model.layers.23` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 306] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002302.npy) |
| 2303 | `model.layers.23` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0002303.npy) |
| 2304 | `model.layers.23` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0002304.npy) |
| 2305 | `model.layers.23` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0002305.npy) |
| 2306 | `model.layers.23` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2307 | `model.layers.23` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2308 | `model.layers.23` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2309 | `model.layers.23.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10752.0 / 10752.0 / 0.25910373263888886 / 454.4602721229703 | [NPY](tensors/0002309.npy) |
| 2310 | `model.layers.23.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 63.5 / 0.016785445478227405 / 1.8360878786850918 | [NPY](tensors/0002310.npy) |
| 2311 | `model.layers.23.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 63.5 / 0.016785445478227405 / 1.8360878786850918 | [NPY](tensors/0002311.npy) |
| 2312 | `model.layers.23.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 306] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002312.npy) |
| 2313 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0002313.npy) |
| 2314 | `model.layers.23.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2315 | `model.layers.23.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2316 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0002316.npy) |
| 2317 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0002317.npy) |
| 2318 | `model.layers.23.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2319 | `model.layers.23.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 63.5 / 0.016785445478227405 / 1.8360878786850918 | [NPY](tensors/0002319.npy) |
| 2320 | `model.layers.23.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.75 / 14.4375 / 0.05605308641679585 / 1.5252618505386772 | [NPY](tensors/0002320.npy) |
| 2321 | `model.layers.23.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 63.5 / 0.016785445478227405 / 1.8360878786850918 | [NPY](tensors/0002321.npy) |
| 2322 | `model.layers.23.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -46.5 / 30.5 / -0.09004351496696472 / 4.859320660255813 | [NPY](tensors/0002322.npy) |
| 2323 | `model.layers.23.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 63.5 / 0.016785445478227405 / 1.8360878786850918 | [NPY](tensors/0002323.npy) |
| 2324 | `model.layers.23.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.375 / 17.375 / 0.02621746063232422 / 4.447720273267019 | [NPY](tensors/0002324.npy) |
| 2325 | `model.layers.23.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.9375 / 7.25 / 0.02564837457612157 / 1.5126157845452572 | [NPY](tensors/0002325.npy) |
| 2326 | `model.layers.23.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3488.0 / 3408.0 / 5.26381581624349 / 169.1778923017113 | [NPY](tensors/0002326.npy) |
| 2327 | `model.layers.23.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3488.0 / 3408.0 / 5.26381581624349 / 169.1778923017113 | [NPY](tensors/0002327.npy) |
| 2328 | `model.layers.23.self_attn` | 19 | `output[1]` | [1, 64, 1, 306] | torch.bfloat16 → float32 | 1.7541523789077473e-14 / 0.94921875 / 0.002361251737595179 / 0.01587072006785083 | [NPY](tensors/0002328.npy) |
| 2329 | `model.layers.23.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9216.0 / 9216.0 / 5.491276041666667 / 440.5644439530943 | [NPY](tensors/0002329.npy) |
| 2330 | `model.layers.23.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 9.0 / 0.000574689441257053 / 1.1628144748152096 | [NPY](tensors/0002330.npy) |
| 2331 | `model.layers.23.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 9.0 / 0.000574689441257053 / 1.1628144748152096 | [NPY](tensors/0002331.npy) |
| 2332 | `model.layers.23.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.0 / 9.0 / 0.000574689441257053 / 1.1628144748152096 | [NPY](tensors/0002332.npy) |
| 2333 | `model.layers.23.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2334 | `model.layers.23.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2335 | `model.layers.23.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2336 | `model.layers.23.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2448.0 / 2464.0 / -3.533218044704861 / 136.85115061547484 | [NPY](tensors/0002336.npy) |
| 2337 | `model.layers.23.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2448.0 / 2464.0 / -3.533218044704861 / 136.85115061547484 | [NPY](tensors/0002337.npy) |
| 2338 | `model.layers.23.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.96875 / 1.3984375 / -0.01267242431640625 / 0.9923882851215601 | [NPY](tensors/0002338.npy) |
| 2339 | `model.layers.23` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6848.0 / 6784.0 / 1.9516493055555555 / 369.873304748181 | [NPY](tensors/0002339.npy) |
| 2418 | `model.layers.23` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9216.0 / 5.629931640625 / 446.8597120932339 | [NPY](tensors/0002418.npy) |
| 2419 | `model.layers.23` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 307] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002419.npy) |
| 2420 | `model.layers.23` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0002420.npy) |
| 2421 | `model.layers.23` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0002421.npy) |
| 2422 | `model.layers.23` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0002422.npy) |
| 2423 | `model.layers.23` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2424 | `model.layers.23` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2425 | `model.layers.23` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2426 | `model.layers.23.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9216.0 / 5.629931640625 / 446.8597120932339 | [NPY](tensors/0002426.npy) |
| 2427 | `model.layers.23.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 48.0 / 0.030565343962775337 / 1.7055721486719437 | [NPY](tensors/0002427.npy) |
| 2428 | `model.layers.23.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 48.0 / 0.030565343962775337 / 1.7055721486719437 | [NPY](tensors/0002428.npy) |
| 2429 | `model.layers.23.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 307] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002429.npy) |
| 2430 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0002430.npy) |
| 2431 | `model.layers.23.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2432 | `model.layers.23.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2433 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0002433.npy) |
| 2434 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0002434.npy) |
| 2435 | `model.layers.23.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2436 | `model.layers.23.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 48.0 / 0.030565343962775337 / 1.7055721486719437 | [NPY](tensors/0002436.npy) |
| 2437 | `model.layers.23.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.1875 / 13.1875 / 0.034884722117567435 / 1.5972836805190282 | [NPY](tensors/0002437.npy) |
| 2438 | `model.layers.23.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 48.0 / 0.030565343962775337 / 1.7055721486719437 | [NPY](tensors/0002438.npy) |
| 2439 | `model.layers.23.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.5 / 30.75 / -0.00039996951818466187 / 5.153889081219822 | [NPY](tensors/0002439.npy) |
| 2440 | `model.layers.23.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 48.0 / 0.030565343962775337 / 1.7055721486719437 | [NPY](tensors/0002440.npy) |
| 2441 | `model.layers.23.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.3125 / 11.0625 / 0.06762486696243286 / 3.962776459997999 | [NPY](tensors/0002441.npy) |
| 2442 | `model.layers.23.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.8125 / 10.4375 / 0.08130987919867039 / 1.992753543646677 | [NPY](tensors/0002442.npy) |
| 2443 | `model.layers.23.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3760.0 / 3552.0 / 1.569492933485243 / 203.85380930402326 | [NPY](tensors/0002443.npy) |
| 2444 | `model.layers.23.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3760.0 / 3552.0 / 1.569492933485243 / 203.85380930402326 | [NPY](tensors/0002444.npy) |
| 2445 | `model.layers.23.self_attn` | 20 | `output[1]` | [1, 64, 1, 307] | torch.bfloat16 → float32 | 1.8118839761882555e-13 / 0.98046875 / 0.002759678852867828 / 0.01965277766410149 | [NPY](tensors/0002445.npy) |
| 2446 | `model.layers.23.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 8512.0 / 7.1886610243055555 / 480.1980812400636 | [NPY](tensors/0002446.npy) |
| 2447 | `model.layers.23.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 7.65625 / 0.0010903239250183105 / 1.3139071261780768 | [NPY](tensors/0002447.npy) |
| 2448 | `model.layers.23.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 7.65625 / 0.0010903239250183105 / 1.3139071261780768 | [NPY](tensors/0002448.npy) |
| 2449 | `model.layers.23.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -30.125 / 7.65625 / 0.0010903239250183105 / 1.3139071261780768 | [NPY](tensors/0002449.npy) |
| 2450 | `model.layers.23.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2451 | `model.layers.23.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2452 | `model.layers.23.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2453 | `model.layers.23.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4352.0 / 3952.0 / -5.297604073418511 / 291.77513784723146 | [NPY](tensors/0002453.npy) |
| 2454 | `model.layers.23.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4352.0 / 3952.0 / -5.297604073418511 / 291.77513784723146 | [NPY](tensors/0002454.npy) |
| 2455 | `model.layers.23.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.7421875 / 2.15625 / -0.11688613891601562 / 0.7220413497977425 | [NPY](tensors/0002455.npy) |
| 2456 | `model.layers.23` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5376.0 / 4672.0 / 1.8906032986111112 / 446.5422607007866 | [NPY](tensors/0002456.npy) |
| 2535 | `model.layers.23` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9600.0 / 3.6298177083333334 / 450.38799535359965 | [NPY](tensors/0002535.npy) |
| 2536 | `model.layers.23` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 308] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002536.npy) |
| 2537 | `model.layers.23` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0002537.npy) |
| 2538 | `model.layers.23` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0002538.npy) |
| 2539 | `model.layers.23` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0002539.npy) |
| 2540 | `model.layers.23` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2541 | `model.layers.23` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2542 | `model.layers.23` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2543 | `model.layers.23.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9600.0 / 3.6298177083333334 / 450.38799535359965 | [NPY](tensors/0002543.npy) |
| 2544 | `model.layers.23.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 57.25 / 0.02430204153060913 / 1.7618081146915006 | [NPY](tensors/0002544.npy) |
| 2545 | `model.layers.23.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 57.25 / 0.02430204153060913 / 1.7618081146915006 | [NPY](tensors/0002545.npy) |
| 2546 | `model.layers.23.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 308] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002546.npy) |
| 2547 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0002547.npy) |
| 2548 | `model.layers.23.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2549 | `model.layers.23.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2550 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0002550.npy) |
| 2551 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0002551.npy) |
| 2552 | `model.layers.23.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2553 | `model.layers.23.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 57.25 / 0.02430204153060913 / 1.7618081146915006 | [NPY](tensors/0002553.npy) |
| 2554 | `model.layers.23.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.25 / 13.75 / 0.05141565011581406 / 1.5577541310636909 | [NPY](tensors/0002554.npy) |
| 2555 | `model.layers.23.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 57.25 / 0.02430204153060913 / 1.7618081146915006 | [NPY](tensors/0002555.npy) |
| 2556 | `model.layers.23.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.75 / 39.5 / -0.07523243129253387 / 5.119090958548786 | [NPY](tensors/0002556.npy) |
| 2557 | `model.layers.23.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 57.25 / 0.02430204153060913 / 1.7618081146915006 | [NPY](tensors/0002557.npy) |
| 2558 | `model.layers.23.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.9375 / 12.25 / -0.017979860305786133 / 3.8278566110142327 | [NPY](tensors/0002558.npy) |
| 2559 | `model.layers.23.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.5625 / 7.5625 / -0.005337212234735489 / 1.5733986993642446 | [NPY](tensors/0002559.npy) |
| 2560 | `model.layers.23.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3664.0 / 3728.0 / 3.197831376393636 / 173.8792111530218 | [NPY](tensors/0002560.npy) |
| 2561 | `model.layers.23.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3664.0 / 3728.0 / 3.197831376393636 / 173.8792111530218 | [NPY](tensors/0002561.npy) |
| 2562 | `model.layers.23.self_attn` | 21 | `output[1]` | [1, 64, 1, 308] | torch.bfloat16 → float32 | 5.950795411990839e-14 / 0.921875 / 0.002557045794932888 / 0.017577374033324086 | [NPY](tensors/0002562.npy) |
| 2563 | `model.layers.23.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8768.0 / 8448.0 / 6.820479329427084 / 456.66784164880704 | [NPY](tensors/0002563.npy) |
| 2564 | `model.layers.23.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 8.375 / 0.0032094518343607583 / 1.2024719856976662 | [NPY](tensors/0002564.npy) |
| 2565 | `model.layers.23.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 8.375 / 0.0032094518343607583 / 1.2024719856976662 | [NPY](tensors/0002565.npy) |
| 2566 | `model.layers.23.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.0 / 8.375 / 0.0032094518343607583 / 1.2024719856976662 | [NPY](tensors/0002566.npy) |
| 2567 | `model.layers.23.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2568 | `model.layers.23.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2569 | `model.layers.23.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2570 | `model.layers.23.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4320.0 / 3984.0 / -0.4270421346028646 / 216.82374802494493 | [NPY](tensors/0002570.npy) |
| 2571 | `model.layers.23.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4320.0 / 3984.0 / -0.4270421346028646 / 216.82374802494493 | [NPY](tensors/0002571.npy) |
| 2572 | `model.layers.23.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.546875 / 1.9296875 / -0.05234885215759277 / 0.88542362863069 | [NPY](tensors/0002572.npy) |
| 2573 | `model.layers.23` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4800.0 / 4640.0 / 6.384299045138889 / 342.79393867940445 | [NPY](tensors/0002573.npy) |
| 2652 | `model.layers.23` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 9088.0 / 1.9373697916666666 / 498.87392590242234 | [NPY](tensors/0002652.npy) |
| 2653 | `model.layers.23` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 309] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002653.npy) |
| 2654 | `model.layers.23` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0002654.npy) |
| 2655 | `model.layers.23` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0002655.npy) |
| 2656 | `model.layers.23` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0002656.npy) |
| 2657 | `model.layers.23` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2658 | `model.layers.23` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2659 | `model.layers.23` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2660 | `model.layers.23.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 9088.0 / 1.9373697916666666 / 498.87392590242234 | [NPY](tensors/0002660.npy) |
| 2661 | `model.layers.23.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 48.5 / 0.01625294155544705 / 1.6783595115000283 | [NPY](tensors/0002661.npy) |
| 2662 | `model.layers.23.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 48.5 / 0.01625294155544705 / 1.6783595115000283 | [NPY](tensors/0002662.npy) |
| 2663 | `model.layers.23.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 309] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002663.npy) |
| 2664 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0002664.npy) |
| 2665 | `model.layers.23.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2666 | `model.layers.23.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2667 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0002667.npy) |
| 2668 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0002668.npy) |
| 2669 | `model.layers.23.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2670 | `model.layers.23.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 48.5 / 0.01625294155544705 / 1.6783595115000283 | [NPY](tensors/0002670.npy) |
| 2671 | `model.layers.23.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.4375 / 17.625 / 0.04217394313309342 / 1.6346758846345868 | [NPY](tensors/0002671.npy) |
| 2672 | `model.layers.23.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 48.5 / 0.01625294155544705 / 1.6783595115000283 | [NPY](tensors/0002672.npy) |
| 2673 | `model.layers.23.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.75 / 28.0 / 0.0646200180053711 / 4.259193208236851 | [NPY](tensors/0002673.npy) |
| 2674 | `model.layers.23.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 48.5 / 0.01625294155544705 / 1.6783595115000283 | [NPY](tensors/0002674.npy) |
| 2675 | `model.layers.23.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.5 / 13.75 / -0.4229137897491455 / 4.220861119792656 | [NPY](tensors/0002675.npy) |
| 2676 | `model.layers.23.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.0625 / 6.84375 / -0.002861473709344864 / 1.3992166139658355 | [NPY](tensors/0002676.npy) |
| 2677 | `model.layers.23.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3376.0 / 3424.0 / 3.0398968166775173 / 167.0424315458684 | [NPY](tensors/0002677.npy) |
| 2678 | `model.layers.23.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3376.0 / 3424.0 / 3.0398968166775173 / 167.0424315458684 | [NPY](tensors/0002678.npy) |
| 2679 | `model.layers.23.self_attn` | 22 | `output[1]` | [1, 64, 1, 309] | torch.bfloat16 → float32 | 1.438849039914203e-13 / 0.8203125 / 0.0021971321235211266 / 0.013719134846125216 | [NPY](tensors/0002679.npy) |
| 2680 | `model.layers.23.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 8096.0 / 4.986664496527778 / 498.96396799919825 | [NPY](tensors/0002680.npy) |
| 2681 | `model.layers.23.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 9.1875 / -0.0011506014400058323 / 1.3016909579664808 | [NPY](tensors/0002681.npy) |
| 2682 | `model.layers.23.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 9.1875 / -0.0011506014400058323 / 1.3016909579664808 | [NPY](tensors/0002682.npy) |
| 2683 | `model.layers.23.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.25 / 9.1875 / -0.0011506014400058323 / 1.3016909579664808 | [NPY](tensors/0002683.npy) |
| 2684 | `model.layers.23.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2685 | `model.layers.23.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2686 | `model.layers.23.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2687 | `model.layers.23.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5440.0 / 5088.0 / -4.855570899115668 / 276.58619959476937 | [NPY](tensors/0002687.npy) |
| 2688 | `model.layers.23.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5440.0 / 5088.0 / -4.855570899115668 / 276.58619959476937 | [NPY](tensors/0002688.npy) |
| 2689 | `model.layers.23.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.375 / 1.828125 / -0.0088653564453125 / 0.8941204352857539 | [NPY](tensors/0002689.npy) |
| 2690 | `model.layers.23` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4320.0 / 3088.0 / 0.126513671875 / 384.64340418396216 | [NPY](tensors/0002690.npy) |
| 2769 | `model.layers.23` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8320.0 / 7744.0 / 4.11561279296875 / 421.5418438100106 | [NPY](tensors/0002769.npy) |
| 2770 | `model.layers.23` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 310] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002770.npy) |
| 2771 | `model.layers.23` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0002771.npy) |
| 2772 | `model.layers.23` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0002772.npy) |
| 2773 | `model.layers.23` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0002773.npy) |
| 2774 | `model.layers.23` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2775 | `model.layers.23` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2776 | `model.layers.23` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2777 | `model.layers.23.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8320.0 / 7744.0 / 4.11561279296875 / 421.5418438100106 | [NPY](tensors/0002777.npy) |
| 2778 | `model.layers.23.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 48.25 / 0.02572620577282376 / 1.6886089972602996 | [NPY](tensors/0002778.npy) |
| 2779 | `model.layers.23.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 48.25 / 0.02572620577282376 / 1.6886089972602996 | [NPY](tensors/0002779.npy) |
| 2780 | `model.layers.23.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 310] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002780.npy) |
| 2781 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0002781.npy) |
| 2782 | `model.layers.23.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2783 | `model.layers.23.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2784 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0002784.npy) |
| 2785 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0002785.npy) |
| 2786 | `model.layers.23.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2787 | `model.layers.23.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 48.25 / 0.02572620577282376 / 1.6886089972602996 | [NPY](tensors/0002787.npy) |
| 2788 | `model.layers.23.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.8125 / 16.5 / 0.03955829219194129 / 1.7799244929789577 | [NPY](tensors/0002788.npy) |
| 2789 | `model.layers.23.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 48.25 / 0.02572620577282376 / 1.6886089972602996 | [NPY](tensors/0002789.npy) |
| 2790 | `model.layers.23.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 41.0 / 0.10055053234100342 / 5.063427786361086 | [NPY](tensors/0002790.npy) |
| 2791 | `model.layers.23.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 48.25 / 0.02572620577282376 / 1.6886089972602996 | [NPY](tensors/0002791.npy) |
| 2792 | `model.layers.23.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.375 / 11.0 / -0.076488196849823 / 3.9036825590436655 | [NPY](tensors/0002792.npy) |
| 2793 | `model.layers.23.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.75 / 6.40625 / 0.04293474508449435 / 1.3934617638959692 | [NPY](tensors/0002793.npy) |
| 2794 | `model.layers.23.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4384.0 / 4416.0 / 2.7478353288438586 / 200.94457524281762 | [NPY](tensors/0002794.npy) |
| 2795 | `model.layers.23.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4384.0 / 4416.0 / 2.7478353288438586 / 200.94457524281762 | [NPY](tensors/0002795.npy) |
| 2796 | `model.layers.23.self_attn` | 23 | `output[1]` | [1, 64, 1, 310] | torch.bfloat16 → float32 | 5.1958437552457326e-14 / 0.9140625 / 0.0022859712642799516 / 0.013844924667493382 | [NPY](tensors/0002796.npy) |
| 2797 | `model.layers.23.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8384.0 / 7840.0 / 6.8631591796875 / 479.1013170312476 | [NPY](tensors/0002797.npy) |
| 2798 | `model.layers.23.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 6.875 / -0.0020410895347595217 / 1.2623041319582167 | [NPY](tensors/0002798.npy) |
| 2799 | `model.layers.23.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 6.875 / -0.0020410895347595217 / 1.2623041319582167 | [NPY](tensors/0002799.npy) |
| 2800 | `model.layers.23.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.375 / 6.875 / -0.0020410895347595217 / 1.2623041319582167 | [NPY](tensors/0002800.npy) |
| 2801 | `model.layers.23.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2802 | `model.layers.23.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2803 | `model.layers.23.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2804 | `model.layers.23.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4288.0 / 4448.0 / -2.2423569997151693 / 270.7946206126177 | [NPY](tensors/0002804.npy) |
| 2805 | `model.layers.23.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4288.0 / 4448.0 / -2.2423569997151693 / 270.7946206126177 | [NPY](tensors/0002805.npy) |
| 2806 | `model.layers.23.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.0 / 2.0625 / -0.053127288818359375 / 0.7128661776847254 | [NPY](tensors/0002806.npy) |
| 2807 | `model.layers.23` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4320.0 / 3712.0 / 4.611382378472222 / 406.14955417141164 | [NPY](tensors/0002807.npy) |
| 2886 | `model.layers.23` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11008.0 / 10944.0 / -1.6629720052083334 / 473.98110836723686 | [NPY](tensors/0002886.npy) |
| 2887 | `model.layers.23` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 311] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002887.npy) |
| 2888 | `model.layers.23` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0002888.npy) |
| 2889 | `model.layers.23` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0002889.npy) |
| 2890 | `model.layers.23` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0002890.npy) |
| 2891 | `model.layers.23` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2892 | `model.layers.23` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2893 | `model.layers.23` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2894 | `model.layers.23.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11008.0 / 10944.0 / -1.6629720052083334 / 473.98110836723686 | [NPY](tensors/0002894.npy) |
| 2895 | `model.layers.23.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 62.0 / 0.008617348803414238 / 1.8019838307114833 | [NPY](tensors/0002895.npy) |
| 2896 | `model.layers.23.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 62.0 / 0.008617348803414238 / 1.8019838307114833 | [NPY](tensors/0002896.npy) |
| 2897 | `model.layers.23.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 311] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002897.npy) |
| 2898 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0002898.npy) |
| 2899 | `model.layers.23.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2900 | `model.layers.23.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2901 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0002901.npy) |
| 2902 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0002902.npy) |
| 2903 | `model.layers.23.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2904 | `model.layers.23.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 62.0 / 0.008617348803414238 / 1.8019838307114833 | [NPY](tensors/0002904.npy) |
| 2905 | `model.layers.23.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.3125 / 14.5 / 0.029158180579543114 / 1.5177955774765457 | [NPY](tensors/0002905.npy) |
| 2906 | `model.layers.23.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 62.0 / 0.008617348803414238 / 1.8019838307114833 | [NPY](tensors/0002906.npy) |
| 2907 | `model.layers.23.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.25 / 37.75 / -0.07524009142071009 / 4.795739872564626 | [NPY](tensors/0002907.npy) |
| 2908 | `model.layers.23.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 62.0 / 0.008617348803414238 / 1.8019838307114833 | [NPY](tensors/0002908.npy) |
| 2909 | `model.layers.23.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.6875 / 8.0 / -0.08721033483743668 / 2.8762617925892773 | [NPY](tensors/0002909.npy) |
| 2910 | `model.layers.23.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.6875 / 6.21875 / 0.01779607916250825 / 1.1932086798187176 | [NPY](tensors/0002910.npy) |
| 2911 | `model.layers.23.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2752.0 / 2640.0 / 2.573084259033203 / 149.19971276947274 | [NPY](tensors/0002911.npy) |
| 2912 | `model.layers.23.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2752.0 / 2640.0 / 2.573084259033203 / 149.19971276947274 | [NPY](tensors/0002912.npy) |
| 2913 | `model.layers.23.self_attn` | 24 | `output[1]` | [1, 64, 1, 311] | torch.bfloat16 → float32 | 9.85878045867139e-14 / 0.9296875 / 0.002162012045120024 / 0.01182388818063748 | [NPY](tensors/0002913.npy) |
| 2914 | `model.layers.23.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8704.0 / 8448.0 / 0.8984754774305556 / 410.88591258986605 | [NPY](tensors/0002914.npy) |
| 2915 | `model.layers.23.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 7.8125 / -0.024328136444091798 / 1.202492088650362 | [NPY](tensors/0002915.npy) |
| 2916 | `model.layers.23.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 7.8125 / -0.024328136444091798 / 1.202492088650362 | [NPY](tensors/0002916.npy) |
| 2917 | `model.layers.23.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.0 / 7.8125 / -0.024328136444091798 / 1.202492088650362 | [NPY](tensors/0002917.npy) |
| 2918 | `model.layers.23.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2919 | `model.layers.23.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2920 | `model.layers.23.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2921 | `model.layers.23.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3840.0 / 3744.0 / -0.7882867601182726 / 191.5815506192977 | [NPY](tensors/0002921.npy) |
| 2922 | `model.layers.23.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3840.0 / 3744.0 / -0.7882867601182726 / 191.5815506192977 | [NPY](tensors/0002922.npy) |
| 2923 | `model.layers.23.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.484375 / 1.203125 / -0.03267669677734375 / 0.8884784616062512 | [NPY](tensors/0002923.npy) |
| 2924 | `model.layers.23` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5120.0 / 4736.0 / 0.08009982638888889 / 298.77220656827615 | [NPY](tensors/0002924.npy) |
| 3003 | `model.layers.23` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10880.0 / -3.1306532118055554 / 467.20699673053804 | [NPY](tensors/0003003.npy) |
| 3004 | `model.layers.23` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 312] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003004.npy) |
| 3005 | `model.layers.23` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0003005.npy) |
| 3006 | `model.layers.23` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0003006.npy) |
| 3007 | `model.layers.23` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0003007.npy) |
| 3008 | `model.layers.23` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3009 | `model.layers.23` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3010 | `model.layers.23` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3011 | `model.layers.23.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10880.0 / -3.1306532118055554 / 467.20699673053804 | [NPY](tensors/0003011.npy) |
| 3012 | `model.layers.23.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 62.5 / 0.0031652344597710505 / 1.8071613226902739 | [NPY](tensors/0003012.npy) |
| 3013 | `model.layers.23.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 62.5 / 0.0031652344597710505 / 1.8071613226902739 | [NPY](tensors/0003013.npy) |
| 3014 | `model.layers.23.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 312] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003014.npy) |
| 3015 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0003015.npy) |
| 3016 | `model.layers.23.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3017 | `model.layers.23.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3018 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0003018.npy) |
| 3019 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0003019.npy) |
| 3020 | `model.layers.23.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3021 | `model.layers.23.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 62.5 / 0.0031652344597710505 / 1.8071613226902739 | [NPY](tensors/0003021.npy) |
| 3022 | `model.layers.23.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.875 / 13.75 / 0.056069307029247284 / 1.5315731629858742 | [NPY](tensors/0003022.npy) |
| 3023 | `model.layers.23.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 62.5 / 0.0031652344597710505 / 1.8071613226902739 | [NPY](tensors/0003023.npy) |
| 3024 | `model.layers.23.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.25 / 34.0 / -0.08628142438828945 / 4.4057076492470495 | [NPY](tensors/0003024.npy) |
| 3025 | `model.layers.23.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 62.5 / 0.0031652344597710505 / 1.8071613226902739 | [NPY](tensors/0003025.npy) |
| 3026 | `model.layers.23.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.25 / 7.53125 / 0.1048937439918518 / 2.791018154386953 | [NPY](tensors/0003026.npy) |
| 3027 | `model.layers.23.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.5625 / 6.34375 / 0.02841370739042759 / 1.324889835050286 | [NPY](tensors/0003027.npy) |
| 3028 | `model.layers.23.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3088.0 / 3040.0 / 4.149082027541267 / 147.74062573614896 | [NPY](tensors/0003028.npy) |
| 3029 | `model.layers.23.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3088.0 / 3040.0 / 4.149082027541267 / 147.74062573614896 | [NPY](tensors/0003029.npy) |
| 3030 | `model.layers.23.self_attn` | 25 | `output[1]` | [1, 64, 1, 312] | torch.bfloat16 → float32 | 4.867217739956686e-13 / 0.90625 / 0.0022357022759340425 / 0.014282883433487138 | [NPY](tensors/0003030.npy) |
| 3031 | `model.layers.23.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9024.0 / 9280.0 / 1.0092393663194446 / 439.8721696509201 | [NPY](tensors/0003031.npy) |
| 3032 | `model.layers.23.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 9.3125 / -0.01668227455682225 / 1.1054909216445514 | [NPY](tensors/0003032.npy) |
| 3033 | `model.layers.23.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 9.3125 / -0.01668227455682225 / 1.1054909216445514 | [NPY](tensors/0003033.npy) |
| 3034 | `model.layers.23.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.5 / 9.3125 / -0.01668227455682225 / 1.1054909216445514 | [NPY](tensors/0003034.npy) |
| 3035 | `model.layers.23.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3036 | `model.layers.23.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3037 | `model.layers.23.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3038 | `model.layers.23.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4832.0 / 4672.0 / -5.377426613701714 / 292.8227466904838 | [NPY](tensors/0003038.npy) |
| 3039 | `model.layers.23.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4832.0 / 4672.0 / -5.377426613701714 / 292.8227466904838 | [NPY](tensors/0003039.npy) |
| 3040 | `model.layers.23.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.78125 / 2.25 / -0.038204193115234375 / 1.0736087521413662 | [NPY](tensors/0003040.npy) |
| 3041 | `model.layers.23` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4608.0 / 4448.0 / -4.376421440972222 / 357.39603188060767 | [NPY](tensors/0003041.npy) |
| 3120 | `model.layers.23` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11776.0 / 10688.0 / -0.22095269097222223 / 485.70536252242897 | [NPY](tensors/0003120.npy) |
| 3121 | `model.layers.23` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 313] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003121.npy) |
| 3122 | `model.layers.23` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0003122.npy) |
| 3123 | `model.layers.23` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0003123.npy) |
| 3124 | `model.layers.23` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0003124.npy) |
| 3125 | `model.layers.23` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3126 | `model.layers.23` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3127 | `model.layers.23` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3128 | `model.layers.23.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11776.0 / 10688.0 / -0.22095269097222223 / 485.70536252242897 | [NPY](tensors/0003128.npy) |
| 3129 | `model.layers.23.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 59.25 / 0.00933161067465941 / 1.7959599469091787 | [NPY](tensors/0003129.npy) |
| 3130 | `model.layers.23.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 59.25 / 0.00933161067465941 / 1.7959599469091787 | [NPY](tensors/0003130.npy) |
| 3131 | `model.layers.23.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 313] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003131.npy) |
| 3132 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0003132.npy) |
| 3133 | `model.layers.23.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3134 | `model.layers.23.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3135 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0003135.npy) |
| 3136 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0003136.npy) |
| 3137 | `model.layers.23.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3138 | `model.layers.23.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 59.25 / 0.00933161067465941 / 1.7959599469091787 | [NPY](tensors/0003138.npy) |
| 3139 | `model.layers.23.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.0 / 15.6875 / 0.0409575377125293 / 1.5514823381163911 | [NPY](tensors/0003139.npy) |
| 3140 | `model.layers.23.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 59.25 / 0.00933161067465941 / 1.7959599469091787 | [NPY](tensors/0003140.npy) |
| 3141 | `model.layers.23.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.25 / 29.625 / -0.1357930637896061 / 4.628889250885522 | [NPY](tensors/0003141.npy) |
| 3142 | `model.layers.23.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 59.25 / 0.00933161067465941 / 1.7959599469091787 | [NPY](tensors/0003142.npy) |
| 3143 | `model.layers.23.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.0 / 14.5625 / -0.15392017364501953 / 4.5925616640530365 | [NPY](tensors/0003143.npy) |
| 3144 | `model.layers.23.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.6875 / 8.375 / 0.03662194189382717 / 1.1284148118865744 | [NPY](tensors/0003144.npy) |
| 3145 | `model.layers.23.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3328.0 / 3552.0 / 1.729755613538954 / 157.76097127854808 | [NPY](tensors/0003145.npy) |
| 3146 | `model.layers.23.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3328.0 / 3552.0 / 1.729755613538954 / 157.76097127854808 | [NPY](tensors/0003146.npy) |
| 3147 | `model.layers.23.self_attn` | 26 | `output[1]` | [1, 64, 1, 313] | torch.bfloat16 → float32 | 5.906386491005833e-14 / 0.921875 / 0.001744598776316009 / 0.011818837044890776 | [NPY](tensors/0003147.npy) |
| 3148 | `model.layers.23.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8640.0 / 7680.0 / 1.5137885199652779 / 378.14422589386777 | [NPY](tensors/0003148.npy) |
| 3149 | `model.layers.23.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 13.1875 / -0.015591465102301704 / 1.2464098147698839 | [NPY](tensors/0003149.npy) |
| 3150 | `model.layers.23.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 13.1875 / -0.015591465102301704 / 1.2464098147698839 | [NPY](tensors/0003150.npy) |
| 3151 | `model.layers.23.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.25 / 13.1875 / -0.015591465102301704 / 1.2464098147698839 | [NPY](tensors/0003151.npy) |
| 3152 | `model.layers.23.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3153 | `model.layers.23.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3154 | `model.layers.23.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3155 | `model.layers.23.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5184.0 / 4640.0 / -0.5557515780131023 / 236.36608029157415 | [NPY](tensors/0003155.npy) |
| 3156 | `model.layers.23.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5184.0 / 4640.0 / -0.5557515780131023 / 236.36608029157415 | [NPY](tensors/0003156.npy) |
| 3157 | `model.layers.23.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.515625 / 2.015625 / -0.0875701904296875 / 1.2774670836455637 | [NPY](tensors/0003157.npy) |
| 3158 | `model.layers.23` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4032.0 / 2912.0 / 0.9633355034722222 / 273.96118712622246 | [NPY](tensors/0003158.npy) |
| 3237 | `model.layers.23` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8704.0 / 8064.0 / -1.9015462239583334 / 410.2025431588411 | [NPY](tensors/0003237.npy) |
| 3238 | `model.layers.23` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 314] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003238.npy) |
| 3239 | `model.layers.23` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0003239.npy) |
| 3240 | `model.layers.23` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0003240.npy) |
| 3241 | `model.layers.23` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0003241.npy) |
| 3242 | `model.layers.23` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3243 | `model.layers.23` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3244 | `model.layers.23` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3245 | `model.layers.23.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8704.0 / 8064.0 / -1.9015462239583334 / 410.2025431588411 | [NPY](tensors/0003245.npy) |
| 3246 | `model.layers.23.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 50.0 / 0.005384529961480034 / 1.7294148305631332 | [NPY](tensors/0003246.npy) |
| 3247 | `model.layers.23.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 50.0 / 0.005384529961480034 / 1.7294148305631332 | [NPY](tensors/0003247.npy) |
| 3248 | `model.layers.23.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 314] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003248.npy) |
| 3249 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0003249.npy) |
| 3250 | `model.layers.23.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3251 | `model.layers.23.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3252 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0003252.npy) |
| 3253 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0003253.npy) |
| 3254 | `model.layers.23.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3255 | `model.layers.23.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 50.0 / 0.005384529961480034 / 1.7294148305631332 | [NPY](tensors/0003255.npy) |
| 3256 | `model.layers.23.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.6875 / 17.625 / 0.055840436019934714 / 1.9677673995933511 | [NPY](tensors/0003256.npy) |
| 3257 | `model.layers.23.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 50.0 / 0.005384529961480034 / 1.7294148305631332 | [NPY](tensors/0003257.npy) |
| 3258 | `model.layers.23.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.75 / 35.75 / -0.03982643783092499 / 5.330308249927418 | [NPY](tensors/0003258.npy) |
| 3259 | `model.layers.23.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 50.0 / 0.005384529961480034 / 1.7294148305631332 | [NPY](tensors/0003259.npy) |
| 3260 | `model.layers.23.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -12.125 / 14.375 / 0.259580135345459 / 3.979521955454121 | [NPY](tensors/0003260.npy) |
| 3261 | `model.layers.23.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.3125 / 7.34375 / 0.039101102855056524 / 1.282989530707955 | [NPY](tensors/0003261.npy) |
| 3262 | `model.layers.23.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2784.0 / 2800.0 / -0.23941802978515625 / 146.91638810608288 | [NPY](tensors/0003262.npy) |
| 3263 | `model.layers.23.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2784.0 / 2800.0 / -0.23941802978515625 / 146.91638810608288 | [NPY](tensors/0003263.npy) |
| 3264 | `model.layers.23.self_attn` | 27 | `output[1]` | [1, 64, 1, 314] | torch.bfloat16 → float32 | 7.7021722333370235e-16 / 0.953125 / 0.0018354208136070517 / 0.013829979062897495 | [NPY](tensors/0003264.npy) |
| 3265 | `model.layers.23.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7232.0 / 6816.0 / -2.1457221137152778 / 400.58805069301525 | [NPY](tensors/0003265.npy) |
| 3266 | `model.layers.23.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.75 / 9.8125 / -0.037913842995961504 / 1.43098243155139 | [NPY](tensors/0003266.npy) |
| 3267 | `model.layers.23.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.75 / 9.8125 / -0.037913842995961504 / 1.43098243155139 | [NPY](tensors/0003267.npy) |
| 3268 | `model.layers.23.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -39.75 / 9.8125 / -0.037913842995961504 / 1.43098243155139 | [NPY](tensors/0003268.npy) |
| 3269 | `model.layers.23.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3270 | `model.layers.23.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3271 | `model.layers.23.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3272 | `model.layers.23.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6464.0 / 6016.0 / -0.4948702918158637 / 336.3458062169017 | [NPY](tensors/0003272.npy) |
| 3273 | `model.layers.23.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6464.0 / 6016.0 / -0.4948702918158637 / 336.3458062169017 | [NPY](tensors/0003273.npy) |
| 3274 | `model.layers.23.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.828125 / 2.046875 / -0.11872100830078125 / 1.036621264871187 | [NPY](tensors/0003274.npy) |
| 3275 | `model.layers.23` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1344.0 / 1584.0 / -2.6369059244791666 / 312.13477154976937 | [NPY](tensors/0003275.npy) |
| 3354 | `model.layers.23` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7680.0 / 7712.0 / 3.3338053385416666 / 435.78615150562865 | [NPY](tensors/0003354.npy) |
| 3355 | `model.layers.23` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 315] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003355.npy) |
| 3356 | `model.layers.23` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0003356.npy) |
| 3357 | `model.layers.23` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0003357.npy) |
| 3358 | `model.layers.23` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0003358.npy) |
| 3359 | `model.layers.23` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3360 | `model.layers.23` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3361 | `model.layers.23` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3362 | `model.layers.23.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7680.0 / 7712.0 / 3.3338053385416666 / 435.78615150562865 | [NPY](tensors/0003362.npy) |
| 3363 | `model.layers.23.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 47.5 / 0.026032013363308376 / 1.6800043070353428 | [NPY](tensors/0003363.npy) |
| 3364 | `model.layers.23.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 47.5 / 0.026032013363308376 / 1.6800043070353428 | [NPY](tensors/0003364.npy) |
| 3365 | `model.layers.23.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 315] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003365.npy) |
| 3366 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0003366.npy) |
| 3367 | `model.layers.23.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3368 | `model.layers.23.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3369 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0003369.npy) |
| 3370 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0003370.npy) |
| 3371 | `model.layers.23.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3372 | `model.layers.23.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 47.5 / 0.026032013363308376 / 1.6800043070353428 | [NPY](tensors/0003372.npy) |
| 3373 | `model.layers.23.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.375 / 14.5625 / 0.036959902150556445 / 1.8480976888422533 | [NPY](tensors/0003373.npy) |
| 3374 | `model.layers.23.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 47.5 / 0.026032013363308376 / 1.6800043070353428 | [NPY](tensors/0003374.npy) |
| 3375 | `model.layers.23.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.875 / 33.0 / -0.07500644028186798 / 4.51861915482338 | [NPY](tensors/0003375.npy) |
| 3376 | `model.layers.23.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 47.5 / 0.026032013363308376 / 1.6800043070353428 | [NPY](tensors/0003376.npy) |
| 3377 | `model.layers.23.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.125 / 13.25 / 0.06499463319778442 / 4.633645951462915 | [NPY](tensors/0003377.npy) |
| 3378 | `model.layers.23.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.25 / 10.375 / 0.06314614313305356 / 1.5712453368050838 | [NPY](tensors/0003378.npy) |
| 3379 | `model.layers.23.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2368.0 / 2336.0 / -1.5973031838734946 / 167.9176568237507 | [NPY](tensors/0003379.npy) |
| 3380 | `model.layers.23.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2368.0 / 2336.0 / -1.5973031838734946 / 167.9176568237507 | [NPY](tensors/0003380.npy) |
| 3381 | `model.layers.23.self_attn` | 28 | `output[1]` | [1, 64, 1, 315] | torch.bfloat16 → float32 | 9.048317650695026e-15 / 0.91796875 / 0.0016983129681651173 / 0.01641523190566638 | [NPY](tensors/0003381.npy) |
| 3382 | `model.layers.23.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6528.0 / 6560.0 / 1.7267442491319445 / 452.81003077606243 | [NPY](tensors/0003382.npy) |
| 3383 | `model.layers.23.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 10.4375 / -0.02076047658920288 / 1.5433207187834153 | [NPY](tensors/0003383.npy) |
| 3384 | `model.layers.23.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 10.4375 / -0.02076047658920288 / 1.5433207187834153 | [NPY](tensors/0003384.npy) |
| 3385 | `model.layers.23.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.25 / 10.4375 / -0.02076047658920288 / 1.5433207187834153 | [NPY](tensors/0003385.npy) |
| 3386 | `model.layers.23.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3387 | `model.layers.23.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3388 | `model.layers.23.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3389 | `model.layers.23.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5216.0 / 4672.0 / -3.8997694227430557 / 422.6002839690438 | [NPY](tensors/0003389.npy) |
| 3390 | `model.layers.23.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5216.0 / 4672.0 / -3.8997694227430557 / 422.6002839690438 | [NPY](tensors/0003390.npy) |
| 3391 | `model.layers.23.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.515625 / 2.265625 / -0.103790283203125 / 0.9326920056165631 | [NPY](tensors/0003391.npy) |
| 3392 | `model.layers.23` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2112.0 / 2096.0 / -2.2143120659722224 / 515.9220191276311 | [NPY](tensors/0003392.npy) |
| 3471 | `model.layers.23` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9984.0 / 9216.0 / 1.6762580023871527 / 418.600529132456 | [NPY](tensors/0003471.npy) |
| 3472 | `model.layers.23` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 316] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003472.npy) |
| 3473 | `model.layers.23` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0003473.npy) |
| 3474 | `model.layers.23` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0003474.npy) |
| 3475 | `model.layers.23` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0003475.npy) |
| 3476 | `model.layers.23` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3477 | `model.layers.23` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3478 | `model.layers.23` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3479 | `model.layers.23.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9984.0 / 9216.0 / 1.6762580023871527 / 418.600529132456 | [NPY](tensors/0003479.npy) |
| 3480 | `model.layers.23.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 59.25 / 0.020402007632785372 / 1.8062344104526842 | [NPY](tensors/0003480.npy) |
| 3481 | `model.layers.23.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 59.25 / 0.020402007632785372 / 1.8062344104526842 | [NPY](tensors/0003481.npy) |
| 3482 | `model.layers.23.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 316] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003482.npy) |
| 3483 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0003483.npy) |
| 3484 | `model.layers.23.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3485 | `model.layers.23.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3486 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0003486.npy) |
| 3487 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0003487.npy) |
| 3488 | `model.layers.23.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3489 | `model.layers.23.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 59.25 / 0.020402007632785372 / 1.8062344104526842 | [NPY](tensors/0003489.npy) |
| 3490 | `model.layers.23.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.75 / 15.375 / 0.055464360397309065 / 1.4911092286641248 | [NPY](tensors/0003490.npy) |
| 3491 | `model.layers.23.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 59.25 / 0.020402007632785372 / 1.8062344104526842 | [NPY](tensors/0003491.npy) |
| 3492 | `model.layers.23.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.5 / 36.25 / -0.08955257572233677 / 4.636823232856326 | [NPY](tensors/0003492.npy) |
| 3493 | `model.layers.23.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 59.25 / 0.020402007632785372 / 1.8062344104526842 | [NPY](tensors/0003493.npy) |
| 3494 | `model.layers.23.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.125 / 12.5625 / 0.2833818346261978 / 3.782856275228265 | [NPY](tensors/0003494.npy) |
| 3495 | `model.layers.23.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.875 / 7.25 / 0.026803433429449797 / 1.0588710585464787 | [NPY](tensors/0003495.npy) |
| 3496 | `model.layers.23.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3776.0 / 3872.0 / 3.3235674805111355 / 166.13459417705153 | [NPY](tensors/0003496.npy) |
| 3497 | `model.layers.23.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3776.0 / 3872.0 / 3.3235674805111355 / 166.13459417705153 | [NPY](tensors/0003497.npy) |
| 3498 | `model.layers.23.self_attn` | 29 | `output[1]` | [1, 64, 1, 316] | torch.bfloat16 → float32 | 5.941427905220564e-17 / 0.89453125 / 0.001439621945024105 / 0.011378908419627473 | [NPY](tensors/0003498.npy) |
| 3499 | `model.layers.23.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 8064.0 / 5.006092664930556 / 429.9005920425412 | [NPY](tensors/0003499.npy) |
| 3500 | `model.layers.23.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 8.625 / 0.000315356089009179 / 1.1486846409637763 | [NPY](tensors/0003500.npy) |
| 3501 | `model.layers.23.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 8.625 / 0.000315356089009179 / 1.1486846409637763 | [NPY](tensors/0003501.npy) |
| 3502 | `model.layers.23.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -35.25 / 8.625 / 0.000315356089009179 / 1.1486846409637763 | [NPY](tensors/0003502.npy) |
| 3503 | `model.layers.23.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3504 | `model.layers.23.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3505 | `model.layers.23.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3506 | `model.layers.23.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4864.0 / 4608.0 / -4.921013726128472 / 255.13122784786503 | [NPY](tensors/0003506.npy) |
| 3507 | `model.layers.23.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4864.0 / 4608.0 / -4.921013726128472 / 255.13122784786503 | [NPY](tensors/0003507.npy) |
| 3508 | `model.layers.23.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.53125 / 1.9609375 / -0.021448135375976562 / 0.9615785535084862 | [NPY](tensors/0003508.npy) |
| 3509 | `model.layers.23` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4256.0 / 3296.0 / 0.08349609375 / 286.0720411641951 | [NPY](tensors/0003509.npy) |
| 3588 | `model.layers.23` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7552.0 / 7744.0 / 3.3307779947916667 / 412.81091013692185 | [NPY](tensors/0003588.npy) |
| 3589 | `model.layers.23` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 317] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003589.npy) |
| 3590 | `model.layers.23` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0003590.npy) |
| 3591 | `model.layers.23` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0003591.npy) |
| 3592 | `model.layers.23` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0003592.npy) |
| 3593 | `model.layers.23` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3594 | `model.layers.23` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3595 | `model.layers.23` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3596 | `model.layers.23.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7552.0 / 7744.0 / 3.3307779947916667 / 412.81091013692185 | [NPY](tensors/0003596.npy) |
| 3597 | `model.layers.23.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 50.5 / 0.024427898724873862 / 1.6952256319240198 | [NPY](tensors/0003597.npy) |
| 3598 | `model.layers.23.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 50.5 / 0.024427898724873862 / 1.6952256319240198 | [NPY](tensors/0003598.npy) |
| 3599 | `model.layers.23.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 317] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003599.npy) |
| 3600 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0003600.npy) |
| 3601 | `model.layers.23.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3602 | `model.layers.23.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3603 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0003603.npy) |
| 3604 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0003604.npy) |
| 3605 | `model.layers.23.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3606 | `model.layers.23.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 50.5 / 0.024427898724873862 / 1.6952256319240198 | [NPY](tensors/0003606.npy) |
| 3607 | `model.layers.23.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.1875 / 12.5 / 0.03812410950195044 / 1.4822104988665725 | [NPY](tensors/0003607.npy) |
| 3608 | `model.layers.23.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 50.5 / 0.024427898724873862 / 1.6952256319240198 | [NPY](tensors/0003608.npy) |
| 3609 | `model.layers.23.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.25 / 29.75 / -0.06137854605913162 / 4.456167713261717 | [NPY](tensors/0003609.npy) |
| 3610 | `model.layers.23.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 50.5 / 0.024427898724873862 / 1.6952256319240198 | [NPY](tensors/0003610.npy) |
| 3611 | `model.layers.23.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.0 / 10.8125 / 0.09142130613327026 / 3.826332080406384 | [NPY](tensors/0003611.npy) |
| 3612 | `model.layers.23.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.5625 / 9.1875 / 0.0266022046089347 / 1.135657277117525 | [NPY](tensors/0003612.npy) |
| 3613 | `model.layers.23.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2512.0 / 2560.0 / 1.17925173441569 / 120.48798054217895 | [NPY](tensors/0003613.npy) |
| 3614 | `model.layers.23.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2512.0 / 2560.0 / 1.17925173441569 / 120.48798054217895 | [NPY](tensors/0003614.npy) |
| 3615 | `model.layers.23.self_attn` | 30 | `output[1]` | [1, 64, 1, 317] | torch.bfloat16 → float32 | 4.0323300254385686e-13 / 0.84765625 / 0.0011137534765850326 / 0.011398411298690563 | [NPY](tensors/0003615.npy) |
| 3616 | `model.layers.23.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6176.0 / 6400.0 / 4.510902235243056 / 391.46046000864203 | [NPY](tensors/0003616.npy) |
| 3617 | `model.layers.23.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 9.375 / -4.5500861273871525e-05 / 1.5668163068129812 | [NPY](tensors/0003617.npy) |
| 3618 | `model.layers.23.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 9.375 / -4.5500861273871525e-05 / 1.5668163068129812 | [NPY](tensors/0003618.npy) |
| 3619 | `model.layers.23.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -49.5 / 9.375 / -4.5500861273871525e-05 / 1.5668163068129812 | [NPY](tensors/0003619.npy) |
| 3620 | `model.layers.23.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3621 | `model.layers.23.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3622 | `model.layers.23.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3623 | `model.layers.23.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4160.0 / 4000.0 / -1.6763631608751086 / 231.45597284495884 | [NPY](tensors/0003623.npy) |
| 3624 | `model.layers.23.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4160.0 / 4000.0 / -1.6763631608751086 / 231.45597284495884 | [NPY](tensors/0003624.npy) |
| 3625 | `model.layers.23.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.421875 / 2.640625 / 0.081390380859375 / 1.464512853442284 | [NPY](tensors/0003625.npy) |
| 3626 | `model.layers.23` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3632.0 / 2496.0 / 2.8373914930555557 / 337.0943421608974 | [NPY](tensors/0003626.npy) |
| 3705 | `model.layers.23` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6848.0 / 7104.0 / 0.6259223090277778 / 387.71819429435016 | [NPY](tensors/0003705.npy) |
| 3706 | `model.layers.23` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 318] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003706.npy) |
| 3707 | `model.layers.23` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0003707.npy) |
| 3708 | `model.layers.23` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0003708.npy) |
| 3709 | `model.layers.23` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0003709.npy) |
| 3710 | `model.layers.23` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3711 | `model.layers.23` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3712 | `model.layers.23` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3713 | `model.layers.23.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6848.0 / 7104.0 / 0.6259223090277778 / 387.71819429435016 | [NPY](tensors/0003713.npy) |
| 3714 | `model.layers.23.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 49.25 / 0.012912458843655057 / 1.6831895663545187 | [NPY](tensors/0003714.npy) |
| 3715 | `model.layers.23.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 49.25 / 0.012912458843655057 / 1.6831895663545187 | [NPY](tensors/0003715.npy) |
| 3716 | `model.layers.23.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 318] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003716.npy) |
| 3717 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0003717.npy) |
| 3718 | `model.layers.23.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3719 | `model.layers.23.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3720 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0003720.npy) |
| 3721 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0003721.npy) |
| 3722 | `model.layers.23.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3723 | `model.layers.23.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 49.25 / 0.012912458843655057 / 1.6831895663545187 | [NPY](tensors/0003723.npy) |
| 3724 | `model.layers.23.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.25 / 13.9375 / 0.014115512603893876 / 1.6301258869555926 | [NPY](tensors/0003724.npy) |
| 3725 | `model.layers.23.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 49.25 / 0.012912458843655057 / 1.6831895663545187 | [NPY](tensors/0003725.npy) |
| 3726 | `model.layers.23.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.25 / 23.625 / -0.122093316167593 / 4.252250442980197 | [NPY](tensors/0003726.npy) |
| 3727 | `model.layers.23.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 49.25 / 0.012912458843655057 / 1.6831895663545187 | [NPY](tensors/0003727.npy) |
| 3728 | `model.layers.23.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -11.625 / 12.4375 / 0.2403261661529541 / 3.934949850016851 | [NPY](tensors/0003728.npy) |
| 3729 | `model.layers.23.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.0 / 9.375 / -0.002846637857146561 / 1.1800593308330456 | [NPY](tensors/0003729.npy) |
| 3730 | `model.layers.23.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3024.0 / 3200.0 / 2.6326001485188804 / 135.923763190153 | [NPY](tensors/0003730.npy) |
| 3731 | `model.layers.23.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3024.0 / 3200.0 / 2.6326001485188804 / 135.923763190153 | [NPY](tensors/0003731.npy) |
| 3732 | `model.layers.23.self_attn` | 31 | `output[1]` | [1, 64, 1, 318] | torch.bfloat16 → float32 | 2.8406096919120216e-17 / 0.90234375 / 0.0010337373938512063 / 0.012852268090022136 | [NPY](tensors/0003732.npy) |
| 3733 | `model.layers.23.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6528.0 / 6688.0 / 3.25101318359375 / 398.73392316349657 | [NPY](tensors/0003733.npy) |
| 3734 | `model.layers.23.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 10.875 / -0.013771851857503256 / 1.5496769853194299 | [NPY](tensors/0003734.npy) |
| 3735 | `model.layers.23.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 10.875 / -0.013771851857503256 / 1.5496769853194299 | [NPY](tensors/0003735.npy) |
| 3736 | `model.layers.23.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -49.25 / 10.875 / -0.013771851857503256 / 1.5496769853194299 | [NPY](tensors/0003736.npy) |
| 3737 | `model.layers.23.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3738 | `model.layers.23.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3739 | `model.layers.23.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3740 | `model.layers.23.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2912.0 / 2864.0 / 0.15990193684895834 / 212.29856287156784 | [NPY](tensors/0003740.npy) |
| 3741 | `model.layers.23.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2912.0 / 2864.0 / 0.15990193684895834 / 212.29856287156784 | [NPY](tensors/0003741.npy) |
| 3742 | `model.layers.23.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.515625 / 2.28125 / 0.068634033203125 / 1.334645929333912 | [NPY](tensors/0003742.npy) |
| 3743 | `model.layers.23` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7744.0 / 7552.0 / 3.3822428385416665 / 494.61802569766894 | [NPY](tensors/0003743.npy) |
| 3822 | `model.layers.23` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7264.0 / 8000.0 / -2.275928412543403 / 382.15973387580715 | [NPY](tensors/0003822.npy) |
| 3823 | `model.layers.23` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 319] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003823.npy) |
| 3824 | `model.layers.23` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0003824.npy) |
| 3825 | `model.layers.23` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0003825.npy) |
| 3826 | `model.layers.23` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0003826.npy) |
| 3827 | `model.layers.23` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3828 | `model.layers.23` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3829 | `model.layers.23` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3830 | `model.layers.23.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7264.0 / 8000.0 / -2.275928412543403 / 382.15973387580715 | [NPY](tensors/0003830.npy) |
| 3831 | `model.layers.23.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 56.25 / 0.007725148730807834 / 1.7485688989301744 | [NPY](tensors/0003831.npy) |
| 3832 | `model.layers.23.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 56.25 / 0.007725148730807834 / 1.7485688989301744 | [NPY](tensors/0003832.npy) |
| 3833 | `model.layers.23.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 319] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003833.npy) |
| 3834 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0003834.npy) |
| 3835 | `model.layers.23.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3836 | `model.layers.23.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3837 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0003837.npy) |
| 3838 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0003838.npy) |
| 3839 | `model.layers.23.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3840 | `model.layers.23.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 56.25 / 0.007725148730807834 / 1.7485688989301744 | [NPY](tensors/0003840.npy) |
| 3841 | `model.layers.23.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.25 / 15.8125 / 0.03865994920488447 / 1.673593283763551 | [NPY](tensors/0003841.npy) |
| 3842 | `model.layers.23.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 56.25 / 0.007725148730807834 / 1.7485688989301744 | [NPY](tensors/0003842.npy) |
| 3843 | `model.layers.23.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.375 / 30.25 / -0.13320332020521164 / 4.687627837179661 | [NPY](tensors/0003843.npy) |
| 3844 | `model.layers.23.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 56.25 / 0.007725148730807834 / 1.7485688989301744 | [NPY](tensors/0003844.npy) |
| 3845 | `model.layers.23.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.25 / 8.75 / 0.14613842964172363 / 3.1613227209343737 | [NPY](tensors/0003845.npy) |
| 3846 | `model.layers.23.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.4375 / 7.53125 / 0.016107765899505466 / 1.0807159430461546 | [NPY](tensors/0003846.npy) |
| 3847 | `model.layers.23.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2656.0 / 2640.0 / 1.643527963426378 / 119.741385391139 | [NPY](tensors/0003847.npy) |
| 3848 | `model.layers.23.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2656.0 / 2640.0 / 1.643527963426378 / 119.741385391139 | [NPY](tensors/0003848.npy) |
| 3849 | `model.layers.23.self_attn` | 32 | `output[1]` | [1, 64, 1, 319] | torch.bfloat16 → float32 | 8.500145032286355e-16 / 0.8203125 / 0.001115314547177454 / 0.012165590681184637 | [NPY](tensors/0003849.npy) |
| 3850 | `model.layers.23.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6400.0 / 7168.0 / -0.6332411024305555 / 376.6463545770369 | [NPY](tensors/0003850.npy) |
| 3851 | `model.layers.23.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 11.3125 / -0.018015378051333956 / 1.4511134264347243 | [NPY](tensors/0003851.npy) |
| 3852 | `model.layers.23.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 11.3125 / -0.018015378051333956 / 1.4511134264347243 | [NPY](tensors/0003852.npy) |
| 3853 | `model.layers.23.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -44.0 / 11.3125 / -0.018015378051333956 / 1.4511134264347243 | [NPY](tensors/0003853.npy) |
| 3854 | `model.layers.23.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3855 | `model.layers.23.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3856 | `model.layers.23.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3857 | `model.layers.23.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4192.0 / 4096.0 / -0.5739320966932508 / 257.576704098018 | [NPY](tensors/0003857.npy) |
| 3858 | `model.layers.23.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4192.0 / 4096.0 / -0.5739320966932508 / 257.576704098018 | [NPY](tensors/0003858.npy) |
| 3859 | `model.layers.23.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.984375 / 2.90625 / 0.11260986328125 / 1.7022062577425134 | [NPY](tensors/0003859.npy) |
| 3860 | `model.layers.23` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3120.0 / 3232.0 / -1.199755859375 / 318.88672915064956 | [NPY](tensors/0003860.npy) |
| 3939 | `model.layers.23` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7136.0 / 7360.0 / 0.6464626736111111 / 384.47244870225876 | [NPY](tensors/0003939.npy) |
| 3940 | `model.layers.23` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 320] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003940.npy) |
| 3941 | `model.layers.23` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0003941.npy) |
| 3942 | `model.layers.23` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0003942.npy) |
| 3943 | `model.layers.23` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0003943.npy) |
| 3944 | `model.layers.23` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3945 | `model.layers.23` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3946 | `model.layers.23` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3947 | `model.layers.23.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7136.0 / 7360.0 / 0.6464626736111111 / 384.47244870225876 | [NPY](tensors/0003947.npy) |
| 3948 | `model.layers.23.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 49.25 / 0.015543413162231446 / 1.6961193680465283 | [NPY](tensors/0003948.npy) |
| 3949 | `model.layers.23.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 49.25 / 0.015543413162231446 / 1.6961193680465283 | [NPY](tensors/0003949.npy) |
| 3950 | `model.layers.23.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 320] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003950.npy) |
| 3951 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0003951.npy) |
| 3952 | `model.layers.23.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3953 | `model.layers.23.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3954 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0003954.npy) |
| 3955 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0003955.npy) |
| 3956 | `model.layers.23.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3957 | `model.layers.23.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 49.25 / 0.015543413162231446 / 1.6961193680465283 | [NPY](tensors/0003957.npy) |
| 3958 | `model.layers.23.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.875 / 18.125 / 0.022477570455521345 / 1.6820170475694902 | [NPY](tensors/0003958.npy) |
| 3959 | `model.layers.23.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 49.25 / 0.015543413162231446 / 1.6961193680465283 | [NPY](tensors/0003959.npy) |
| 3960 | `model.layers.23.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.5 / 32.25 / -0.22531147301197052 / 4.5773092066795025 | [NPY](tensors/0003960.npy) |
| 3961 | `model.layers.23.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 49.25 / 0.015543413162231446 / 1.6961193680465283 | [NPY](tensors/0003961.npy) |
| 3962 | `model.layers.23.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.6875 / 18.375 / 0.33959370851516724 / 4.414309010085741 | [NPY](tensors/0003962.npy) |
| 3963 | `model.layers.23.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.0625 / 8.5 / -0.008658843580633402 / 1.253022924061321 | [NPY](tensors/0003963.npy) |
| 3964 | `model.layers.23.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2880.0 / 2832.0 / 2.624791081746419 / 126.63052682135523 | [NPY](tensors/0003964.npy) |
| 3965 | `model.layers.23.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2880.0 / 2832.0 / 2.624791081746419 / 126.63052682135523 | [NPY](tensors/0003965.npy) |
| 3966 | `model.layers.23.self_attn` | 33 | `output[1]` | [1, 64, 1, 320] | torch.bfloat16 → float32 | 5.898059818321144e-17 / 0.88671875 / 0.0011802888480819148 / 0.012397846065542855 | [NPY](tensors/0003966.npy) |
| 3967 | `model.layers.23.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6624.0 / 6688.0 / 3.26707763671875 / 381.9294077964495 | [NPY](tensors/0003967.npy) |
| 3968 | `model.layers.23.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 13.125 / -0.008139808972676596 / 1.4955150089110751 | [NPY](tensors/0003968.npy) |
| 3969 | `model.layers.23.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 13.125 / -0.008139808972676596 / 1.4955150089110751 | [NPY](tensors/0003969.npy) |
| 3970 | `model.layers.23.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -46.75 / 13.125 / -0.008139808972676596 / 1.4955150089110751 | [NPY](tensors/0003970.npy) |
| 3971 | `model.layers.23.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3972 | `model.layers.23.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3973 | `model.layers.23.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3974 | `model.layers.23.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3584.0 / 3552.0 / -2.530992635091146 / 199.68490199325208 | [NPY](tensors/0003974.npy) |
| 3975 | `model.layers.23.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3584.0 / 3552.0 / -2.530992635091146 / 199.68490199325208 | [NPY](tensors/0003975.npy) |
| 3976 | `model.layers.23.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.34375 / 2.578125 / 0.11090087890625 / 1.7471698446904989 | [NPY](tensors/0003976.npy) |
| 3977 | `model.layers.23` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3072.0 / 3232.0 / 0.745947265625 / 306.64715451282586 | [NPY](tensors/0003977.npy) |
| 4056 | `model.layers.23` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 6176.0 / 4.494770982530382 / 368.4632411847903 | [NPY](tensors/0004056.npy) |
| 4057 | `model.layers.23` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 321] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004057.npy) |
| 4058 | `model.layers.23` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0004058.npy) |
| 4059 | `model.layers.23` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0004059.npy) |
| 4060 | `model.layers.23` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0004060.npy) |
| 4061 | `model.layers.23` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4062 | `model.layers.23` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4063 | `model.layers.23` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4064 | `model.layers.23.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 6176.0 / 4.494770982530382 / 368.4632411847903 | [NPY](tensors/0004064.npy) |
| 4065 | `model.layers.23.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 45.0 / 0.029083392355177137 / 1.660998425219009 | [NPY](tensors/0004065.npy) |
| 4066 | `model.layers.23.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 45.0 / 0.029083392355177137 / 1.660998425219009 | [NPY](tensors/0004066.npy) |
| 4067 | `model.layers.23.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 321] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004067.npy) |
| 4068 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0004068.npy) |
| 4069 | `model.layers.23.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4070 | `model.layers.23.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4071 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0004071.npy) |
| 4072 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0004072.npy) |
| 4073 | `model.layers.23.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4074 | `model.layers.23.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 45.0 / 0.029083392355177137 / 1.660998425219009 | [NPY](tensors/0004074.npy) |
| 4075 | `model.layers.23.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.0 / 17.875 / 0.04558353777974844 / 1.8824038196290989 | [NPY](tensors/0004075.npy) |
| 4076 | `model.layers.23.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 45.0 / 0.029083392355177137 / 1.660998425219009 | [NPY](tensors/0004076.npy) |
| 4077 | `model.layers.23.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.0 / 49.5 / -0.07557724416255951 / 5.487501337477615 | [NPY](tensors/0004077.npy) |
| 4078 | `model.layers.23.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 45.0 / 0.029083392355177137 / 1.660998425219009 | [NPY](tensors/0004078.npy) |
| 4079 | `model.layers.23.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -23.625 / 12.0 / 0.18752017617225647 / 4.367389487128676 | [NPY](tensors/0004079.npy) |
| 4080 | `model.layers.23.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.625 / 13.25 / -0.0033048472832888365 / 1.3652841641426536 | [NPY](tensors/0004080.npy) |
| 4081 | `model.layers.23.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3504.0 / 3520.0 / -0.17405018276638454 / 160.929823864637 | [NPY](tensors/0004081.npy) |
| 4082 | `model.layers.23.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3504.0 / 3520.0 / -0.17405018276638454 / 160.929823864637 | [NPY](tensors/0004082.npy) |
| 4083 | `model.layers.23.self_attn` | 34 | `output[1]` | [1, 64, 1, 321] | torch.bfloat16 → float32 | 5.759281940243e-16 / 0.9140625 / 0.0010934324435661127 / 0.01614014589923733 | [NPY](tensors/0004083.npy) |
| 4084 | `model.layers.23.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5888.0 / 6592.0 / 4.335139973958333 / 417.0190816285466 | [NPY](tensors/0004084.npy) |
| 4085 | `model.layers.23.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 12.5625 / -0.0002517633967929416 / 1.49597216398518 | [NPY](tensors/0004085.npy) |
| 4086 | `model.layers.23.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 12.5625 / -0.0002517633967929416 / 1.49597216398518 | [NPY](tensors/0004086.npy) |
| 4087 | `model.layers.23.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -40.0 / 12.5625 / -0.0002517633967929416 / 1.49597216398518 | [NPY](tensors/0004087.npy) |
| 4088 | `model.layers.23.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4089 | `model.layers.23.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4090 | `model.layers.23.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4091 | `model.layers.23.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5824.0 / 5184.0 / -5.552452744377984 / 317.5437046022262 | [NPY](tensors/0004091.npy) |
| 4092 | `model.layers.23.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5824.0 / 5184.0 / -5.552452744377984 / 317.5437046022262 | [NPY](tensors/0004092.npy) |
| 4093 | `model.layers.23.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.5 / 2.53125 / 0.137451171875 / 1.8373328405368283 | [NPY](tensors/0004093.npy) |
| 4094 | `model.layers.23` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3152.0 / 2080.0 / -1.2177842881944445 / 347.3699196748615 | [NPY](tensors/0004094.npy) |
| 4173 | `model.layers.23` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6368.0 / 6432.0 / 3.9705512152777778 / 367.39355206869743 | [NPY](tensors/0004173.npy) |
| 4174 | `model.layers.23` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004174.npy) |
| 4175 | `model.layers.23` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0004175.npy) |
| 4176 | `model.layers.23` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0004176.npy) |
| 4177 | `model.layers.23` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0004177.npy) |
| 4178 | `model.layers.23` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4179 | `model.layers.23` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4180 | `model.layers.23` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4181 | `model.layers.23.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6368.0 / 6432.0 / 3.9705512152777778 / 367.39355206869743 | [NPY](tensors/0004181.npy) |
| 4182 | `model.layers.23.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 45.5 / 0.026728513505723743 / 1.637508486716463 | [NPY](tensors/0004182.npy) |
| 4183 | `model.layers.23.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 45.5 / 0.026728513505723743 / 1.637508486716463 | [NPY](tensors/0004183.npy) |
| 4184 | `model.layers.23.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004184.npy) |
| 4185 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0004185.npy) |
| 4186 | `model.layers.23.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4187 | `model.layers.23.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4188 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0004188.npy) |
| 4189 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0004189.npy) |
| 4190 | `model.layers.23.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4191 | `model.layers.23.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 45.5 / 0.026728513505723743 / 1.637508486716463 | [NPY](tensors/0004191.npy) |
| 4192 | `model.layers.23.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.625 / 19.375 / 0.052725730784004554 / 1.9020888282774002 | [NPY](tensors/0004192.npy) |
| 4193 | `model.layers.23.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 45.5 / 0.026728513505723743 / 1.637508486716463 | [NPY](tensors/0004193.npy) |
| 4194 | `model.layers.23.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.25 / 43.0 / -0.03865227848291397 / 4.784904402331293 | [NPY](tensors/0004194.npy) |
| 4195 | `model.layers.23.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 45.5 / 0.026728513505723743 / 1.637508486716463 | [NPY](tensors/0004195.npy) |
| 4196 | `model.layers.23.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.9375 / 11.875 / -0.05873298645019531 / 3.9182027265579924 | [NPY](tensors/0004196.npy) |
| 4197 | `model.layers.23.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -18.375 / 14.3125 / -0.024543119012378156 / 1.4796652972119768 | [NPY](tensors/0004197.npy) |
| 4198 | `model.layers.23.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3088.0 / 3072.0 / -1.0142262776692708 / 148.76910279236014 | [NPY](tensors/0004198.npy) |
| 4199 | `model.layers.23.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3088.0 / 3072.0 / -1.0142262776692708 / 148.76910279236014 | [NPY](tensors/0004199.npy) |
| 4200 | `model.layers.23.self_attn` | 35 | `output[1]` | [1, 64, 1, 322] | torch.bfloat16 → float32 | 3.2390539903004445e-18 / 0.9765625 / 0.0012550182320486799 / 0.01806355868429129 | [NPY](tensors/0004200.npy) |
| 4201 | `model.layers.23.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5856.0 / 5888.0 / 2.9523383246527777 / 385.3843091899382 | [NPY](tensors/0004201.npy) |
| 4202 | `model.layers.23.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 12.0625 / -0.0002613067626953125 / 1.4864698123673452 | [NPY](tensors/0004202.npy) |
| 4203 | `model.layers.23.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 12.0625 / -0.0002613067626953125 / 1.4864698123673452 | [NPY](tensors/0004203.npy) |
| 4204 | `model.layers.23.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -41.25 / 12.0625 / -0.0002613067626953125 / 1.4864698123673452 | [NPY](tensors/0004204.npy) |
| 4205 | `model.layers.23.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4206 | `model.layers.23.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4207 | `model.layers.23.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4208 | `model.layers.23.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4736.0 / 4384.0 / -7.802183108859592 / 308.30906668265334 | [NPY](tensors/0004208.npy) |
| 4209 | `model.layers.23.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4736.0 / 4384.0 / -7.802183108859592 / 308.30906668265334 | [NPY](tensors/0004209.npy) |
| 4210 | `model.layers.23.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.21875 / 2.703125 / 0.1015625 / 1.7603219663289955 | [NPY](tensors/0004210.npy) |
| 4211 | `model.layers.23` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2960.0 / 1776.0 / -4.856293402777778 / 379.2968615321734 | [NPY](tensors/0004211.npy) |
| 4290 | `model.layers.23` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 9856.0 / 1.0006727430555555 / 444.2775890757678 | [NPY](tensors/0004290.npy) |
| 4291 | `model.layers.23` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004291.npy) |
| 4292 | `model.layers.23` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0004292.npy) |
| 4293 | `model.layers.23` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0004293.npy) |
| 4294 | `model.layers.23` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0004294.npy) |
| 4295 | `model.layers.23` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4296 | `model.layers.23` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4297 | `model.layers.23` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4298 | `model.layers.23.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 9856.0 / 1.0006727430555555 / 444.2775890757678 | [NPY](tensors/0004298.npy) |
| 4299 | `model.layers.23.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 59.5 / 0.016952308019002278 / 1.7725386369507559 | [NPY](tensors/0004299.npy) |
| 4300 | `model.layers.23.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 59.5 / 0.016952308019002278 / 1.7725386369507559 | [NPY](tensors/0004300.npy) |
| 4301 | `model.layers.23.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004301.npy) |
| 4302 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0004302.npy) |
| 4303 | `model.layers.23.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4304 | `model.layers.23.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4305 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0004305.npy) |
| 4306 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0004306.npy) |
| 4307 | `model.layers.23.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4308 | `model.layers.23.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 59.5 / 0.016952308019002278 / 1.7725386369507559 | [NPY](tensors/0004308.npy) |
| 4309 | `model.layers.23.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.6875 / 17.25 / 0.04045625799335539 / 1.5783924962300941 | [NPY](tensors/0004309.npy) |
| 4310 | `model.layers.23.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 59.5 / 0.016952308019002278 / 1.7725386369507559 | [NPY](tensors/0004310.npy) |
| 4311 | `model.layers.23.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.0 / 26.875 / -0.1506922491826117 / 4.126573254885477 | [NPY](tensors/0004311.npy) |
| 4312 | `model.layers.23.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 59.5 / 0.016952308019002278 / 1.7725386369507559 | [NPY](tensors/0004312.npy) |
| 4313 | `model.layers.23.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.625 / 14.125 / 0.19277581572532654 / 4.001386249474691 | [NPY](tensors/0004313.npy) |
| 4314 | `model.layers.23.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.5625 / 7.1875 / 0.011352081724908203 / 1.1414571822720638 | [NPY](tensors/0004314.npy) |
| 4315 | `model.layers.23.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2736.0 / 2816.0 / 2.4520901997884113 / 146.7587364991468 | [NPY](tensors/0004315.npy) |
| 4316 | `model.layers.23.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2736.0 / 2816.0 / 2.4520901997884113 / 146.7587364991468 | [NPY](tensors/0004316.npy) |
| 4317 | `model.layers.23.self_attn` | 36 | `output[1]` | [1, 64, 1, 323] | torch.bfloat16 → float32 | 1.0824674490095276e-15 / 0.80859375 / 0.001085163257259878 / 0.010016226155499797 | [NPY](tensors/0004317.npy) |
| 4318 | `model.layers.23.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6848.0 / 7680.0 / 3.4539116753472223 / 401.0092796598262 | [NPY](tensors/0004318.npy) |
| 4319 | `model.layers.23.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 12.3125 / -0.011327360073725383 / 1.4729745557292775 | [NPY](tensors/0004319.npy) |
| 4320 | `model.layers.23.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 12.3125 / -0.011327360073725383 / 1.4729745557292775 | [NPY](tensors/0004320.npy) |
| 4321 | `model.layers.23.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -46.5 / 12.3125 / -0.011327360073725383 / 1.4729745557292775 | [NPY](tensors/0004321.npy) |
| 4322 | `model.layers.23.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4323 | `model.layers.23.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4324 | `model.layers.23.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4325 | `model.layers.23.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5248.0 / 5312.0 / -0.5814974466959636 / 258.2422696241352 | [NPY](tensors/0004325.npy) |
| 4326 | `model.layers.23.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5248.0 / 5312.0 / -0.5814974466959636 / 258.2422696241352 | [NPY](tensors/0004326.npy) |
| 4327 | `model.layers.23.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.15625 / 2.171875 / 0.035400390625 / 1.5749794421292393 | [NPY](tensors/0004327.npy) |
| 4328 | `model.layers.23` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1808.0 / 2432.0 / 2.896533203125 / 296.5447839403767 | [NPY](tensors/0004328.npy) |
| 4407 | `model.layers.23` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11264.0 / 11392.0 / -1.0214626736111112 / 511.6534505933637 | [NPY](tensors/0004407.npy) |
| 4408 | `model.layers.23` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004408.npy) |
| 4409 | `model.layers.23` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0004409.npy) |
| 4410 | `model.layers.23` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0004410.npy) |
| 4411 | `model.layers.23` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0004411.npy) |
| 4412 | `model.layers.23` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4413 | `model.layers.23` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4414 | `model.layers.23` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4415 | `model.layers.23.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11264.0 / 11392.0 / -1.0214626736111112 / 511.6534505933637 | [NPY](tensors/0004415.npy) |
| 4416 | `model.layers.23.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 59.75 / 0.012361138065656026 / 1.7732821985968172 | [NPY](tensors/0004416.npy) |
| 4417 | `model.layers.23.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 59.75 / 0.012361138065656026 / 1.7732821985968172 | [NPY](tensors/0004417.npy) |
| 4418 | `model.layers.23.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004418.npy) |
| 4419 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0004419.npy) |
| 4420 | `model.layers.23.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4421 | `model.layers.23.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4422 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0004422.npy) |
| 4423 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0004423.npy) |
| 4424 | `model.layers.23.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4425 | `model.layers.23.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 59.75 / 0.012361138065656026 / 1.7732821985968172 | [NPY](tensors/0004425.npy) |
| 4426 | `model.layers.23.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.5 / 13.5 / 0.03704871574882418 / 1.406210028446351 | [NPY](tensors/0004426.npy) |
| 4427 | `model.layers.23.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 59.75 / 0.012361138065656026 / 1.7732821985968172 | [NPY](tensors/0004427.npy) |
| 4428 | `model.layers.23.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.5 / 36.75 / -0.108686164021492 / 4.255617284048991 | [NPY](tensors/0004428.npy) |
| 4429 | `model.layers.23.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 59.75 / 0.012361138065656026 / 1.7732821985968172 | [NPY](tensors/0004429.npy) |
| 4430 | `model.layers.23.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.25 / 8.0625 / 0.06550538539886475 / 2.6460095843308644 | [NPY](tensors/0004430.npy) |
| 4431 | `model.layers.23.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.25 / 6.15625 / 0.03038900066167116 / 1.0417638076737215 | [NPY](tensors/0004431.npy) |
| 4432 | `model.layers.23.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4544.0 / 4672.0 / 5.053301933076646 / 197.26806972677207 | [NPY](tensors/0004432.npy) |
| 4433 | `model.layers.23.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4544.0 / 4672.0 / 5.053301933076646 / 197.26806972677207 | [NPY](tensors/0004433.npy) |
| 4434 | `model.layers.23.self_attn` | 37 | `output[1]` | [1, 64, 1, 324] | torch.bfloat16 → float32 | 2.6367796834847468e-15 / 0.7265625 / 0.00144685591717722 / 0.010470032638733657 | [NPY](tensors/0004434.npy) |
| 4435 | `model.layers.23.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10688.0 / 4.014145236545139 / 550.557242952921 | [NPY](tensors/0004435.npy) |
| 4436 | `model.layers.23.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 7.4375 / -0.001844820711347792 / 1.1881555713431289 | [NPY](tensors/0004436.npy) |
| 4437 | `model.layers.23.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 7.4375 / -0.001844820711347792 / 1.1881555713431289 | [NPY](tensors/0004437.npy) |
| 4438 | `model.layers.23.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.75 / 7.4375 / -0.001844820711347792 / 1.1881555713431289 | [NPY](tensors/0004438.npy) |
| 4439 | `model.layers.23.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4440 | `model.layers.23.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4441 | `model.layers.23.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4442 | `model.layers.23.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3632.0 / 3488.0 / -3.886936232778761 / 206.10868591371448 | [NPY](tensors/0004442.npy) |
| 4443 | `model.layers.23.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3632.0 / 3488.0 / -3.886936232778761 / 206.10868591371448 | [NPY](tensors/0004443.npy) |
| 4444 | `model.layers.23.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.3125 / 1.8515625 / -0.04280853271484375 / 0.843828157075311 | [NPY](tensors/0004444.npy) |
| 4445 | `model.layers.23` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7136.0 / 7136.0 / 0.1224609375 / 435.8461073029038 | [NPY](tensors/0004445.npy) |
| 4524 | `model.layers.23` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9728.0 / -6.50430908203125 / 494.0069668304763 | [NPY](tensors/0004524.npy) |
| 4525 | `model.layers.23` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004525.npy) |
| 4526 | `model.layers.23` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0004526.npy) |
| 4527 | `model.layers.23` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0004527.npy) |
| 4528 | `model.layers.23` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0004528.npy) |
| 4529 | `model.layers.23` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4530 | `model.layers.23` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4531 | `model.layers.23` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4532 | `model.layers.23.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9728.0 / -6.50430908203125 / 494.0069668304763 | [NPY](tensors/0004532.npy) |
| 4533 | `model.layers.23.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 53.0 / -0.007363507482740614 / 1.7067597355795796 | [NPY](tensors/0004533.npy) |
| 4534 | `model.layers.23.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 53.0 / -0.007363507482740614 / 1.7067597355795796 | [NPY](tensors/0004534.npy) |
| 4535 | `model.layers.23.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004535.npy) |
| 4536 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0004536.npy) |
| 4537 | `model.layers.23.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4538 | `model.layers.23.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4539 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0004539.npy) |
| 4540 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0004540.npy) |
| 4541 | `model.layers.23.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4542 | `model.layers.23.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 53.0 / -0.007363507482740614 / 1.7067597355795796 | [NPY](tensors/0004542.npy) |
| 4543 | `model.layers.23.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.0 / 18.875 / 0.03446922532748431 / 1.4194188418027918 | [NPY](tensors/0004543.npy) |
| 4544 | `model.layers.23.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 53.0 / -0.007363507482740614 / 1.7067597355795796 | [NPY](tensors/0004544.npy) |
| 4545 | `model.layers.23.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.0 / 39.25 / -0.1555868275463581 / 5.013228747739377 | [NPY](tensors/0004545.npy) |
| 4546 | `model.layers.23.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 53.0 / -0.007363507482740614 / 1.7067597355795796 | [NPY](tensors/0004546.npy) |
| 4547 | `model.layers.23.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.25 / 13.8125 / 0.24309420585632324 / 4.007023539008476 | [NPY](tensors/0004547.npy) |
| 4548 | `model.layers.23.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.25 / 8.0 / 0.02325309067964554 / 1.0842208109841005 | [NPY](tensors/0004548.npy) |
| 4549 | `model.layers.23.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5152.0 / 5280.0 / 6.122595384385851 / 221.30982054799648 | [NPY](tensors/0004549.npy) |
| 4550 | `model.layers.23.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5152.0 / 5280.0 / 6.122595384385851 / 221.30982054799648 | [NPY](tensors/0004550.npy) |
| 4551 | `model.layers.23.self_attn` | 38 | `output[1]` | [1, 64, 1, 325] | torch.bfloat16 → float32 | 6.439293542825908e-15 / 0.83984375 / 0.0012523604206386746 / 0.010143150052989306 | [NPY](tensors/0004551.npy) |
| 4552 | `model.layers.23.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10176.0 / 9408.0 / -0.37493760850694446 / 550.9474017179448 | [NPY](tensors/0004552.npy) |
| 4553 | `model.layers.23.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 8.0 / -0.025496752477354473 / 1.1793404925069342 | [NPY](tensors/0004553.npy) |
| 4554 | `model.layers.23.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 8.0 / -0.025496752477354473 / 1.1793404925069342 | [NPY](tensors/0004554.npy) |
| 4555 | `model.layers.23.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -39.5 / 8.0 / -0.025496752477354473 / 1.1793404925069342 | [NPY](tensors/0004555.npy) |
| 4556 | `model.layers.23.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4557 | `model.layers.23.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4558 | `model.layers.23.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4559 | `model.layers.23.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3152.0 / 3072.0 / -1.7179302639431424 / 185.97530546782932 | [NPY](tensors/0004559.npy) |
| 4560 | `model.layers.23.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3152.0 / 3072.0 / -1.7179302639431424 / 185.97530546782932 | [NPY](tensors/0004560.npy) |
| 4561 | `model.layers.23.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.3125 / 1.3359375 / -0.0236663818359375 / 0.860114983967464 | [NPY](tensors/0004561.npy) |
| 4562 | `model.layers.23` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7168.0 / 6272.0 / -2.08330078125 / 427.7994997586442 | [NPY](tensors/0004562.npy) |
| 4641 | `model.layers.23` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9600.0 / -6.792084418402778 / 498.55822486266266 | [NPY](tensors/0004641.npy) |
| 4642 | `model.layers.23` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004642.npy) |
| 4643 | `model.layers.23` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0004643.npy) |
| 4644 | `model.layers.23` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0004644.npy) |
| 4645 | `model.layers.23` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0004645.npy) |
| 4646 | `model.layers.23` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4647 | `model.layers.23` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4648 | `model.layers.23` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4649 | `model.layers.23.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9600.0 / -6.792084418402778 / 498.55822486266266 | [NPY](tensors/0004649.npy) |
| 4650 | `model.layers.23.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 48.25 / -0.006685006618499756 / 1.6650506921739823 | [NPY](tensors/0004650.npy) |
| 4651 | `model.layers.23.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 48.25 / -0.006685006618499756 / 1.6650506921739823 | [NPY](tensors/0004651.npy) |
| 4652 | `model.layers.23.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004652.npy) |
| 4653 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0004653.npy) |
| 4654 | `model.layers.23.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4655 | `model.layers.23.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4656 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0004656.npy) |
| 4657 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0004657.npy) |
| 4658 | `model.layers.23.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4659 | `model.layers.23.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 48.25 / -0.006685006618499756 / 1.6650506921739823 | [NPY](tensors/0004659.npy) |
| 4660 | `model.layers.23.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.5625 / 16.375 / 0.04864149703644216 / 1.5187875914144418 | [NPY](tensors/0004660.npy) |
| 4661 | `model.layers.23.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 48.25 / -0.006685006618499756 / 1.6650506921739823 | [NPY](tensors/0004661.npy) |
| 4662 | `model.layers.23.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -58.25 / 47.5 / -0.07949325442314148 / 5.030623274939889 | [NPY](tensors/0004662.npy) |
| 4663 | `model.layers.23.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 48.25 / -0.006685006618499756 / 1.6650506921739823 | [NPY](tensors/0004663.npy) |
| 4664 | `model.layers.23.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -12.4375 / 13.9375 / -0.05210888385772705 / 3.5870952428120373 | [NPY](tensors/0004664.npy) |
| 4665 | `model.layers.23.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.375 / 7.96875 / 0.012561272276798263 / 0.8312150358371936 | [NPY](tensors/0004665.npy) |
| 4666 | `model.layers.23.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3744.0 / 3936.0 / 3.285603290134006 / 165.05842338409144 | [NPY](tensors/0004666.npy) |
| 4667 | `model.layers.23.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3744.0 / 3936.0 / 3.285603290134006 / 165.05842338409144 | [NPY](tensors/0004667.npy) |
| 4668 | `model.layers.23.self_attn` | 39 | `output[1]` | [1, 64, 1, 326] | torch.bfloat16 → float32 | 6.572520305780927e-14 / 0.5625 / 0.00078272242054506 / 0.008068961933045559 | [NPY](tensors/0004668.npy) |
| 4669 | `model.layers.23.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9024.0 / 9280.0 / -3.5036512586805557 / 524.7877632644891 | [NPY](tensors/0004669.npy) |
| 4670 | `model.layers.23.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 9.9375 / -0.02979648378160265 / 1.4394921338738664 | [NPY](tensors/0004670.npy) |
| 4671 | `model.layers.23.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 9.9375 / -0.02979648378160265 / 1.4394921338738664 | [NPY](tensors/0004671.npy) |
| 4672 | `model.layers.23.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -48.0 / 9.9375 / -0.02979648378160265 / 1.4394921338738664 | [NPY](tensors/0004672.npy) |
| 4673 | `model.layers.23.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4674 | `model.layers.23.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4675 | `model.layers.23.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4676 | `model.layers.23.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3472.0 / 3952.0 / -2.1463446723090276 / 230.70178291507943 | [NPY](tensors/0004676.npy) |
| 4677 | `model.layers.23.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3472.0 / 3952.0 / -2.1463446723090276 / 230.70178291507943 | [NPY](tensors/0004677.npy) |
| 4678 | `model.layers.23.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.34375 / 2.203125 / -0.04717540740966797 / 1.0578832460681267 | [NPY](tensors/0004678.npy) |
| 4679 | `model.layers.23` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 8704.0 / -5.638229709201389 / 603.1032404209016 | [NPY](tensors/0004679.npy) |
| 4758 | `model.layers.23` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 9536.0 / 1.1757269965277777 / 479.3798763712226 | [NPY](tensors/0004758.npy) |
| 4759 | `model.layers.23` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004759.npy) |
| 4760 | `model.layers.23` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0004760.npy) |
| 4761 | `model.layers.23` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0004761.npy) |
| 4762 | `model.layers.23` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0004762.npy) |
| 4763 | `model.layers.23` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4764 | `model.layers.23` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4765 | `model.layers.23` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4766 | `model.layers.23.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 9536.0 / 1.1757269965277777 / 479.3798763712226 | [NPY](tensors/0004766.npy) |
| 4767 | `model.layers.23.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 53.5 / 0.01480077240202162 / 1.7184249917191257 | [NPY](tensors/0004767.npy) |
| 4768 | `model.layers.23.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 53.5 / 0.01480077240202162 / 1.7184249917191257 | [NPY](tensors/0004768.npy) |
| 4769 | `model.layers.23.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004769.npy) |
| 4770 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0004770.npy) |
| 4771 | `model.layers.23.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4772 | `model.layers.23.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4773 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0004773.npy) |
| 4774 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0004774.npy) |
| 4775 | `model.layers.23.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4776 | `model.layers.23.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 53.5 / 0.01480077240202162 / 1.7184249917191257 | [NPY](tensors/0004776.npy) |
| 4777 | `model.layers.23.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.6875 / 19.25 / 0.03640994057059288 / 1.6023658714840843 | [NPY](tensors/0004777.npy) |
| 4778 | `model.layers.23.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 53.5 / 0.01480077240202162 / 1.7184249917191257 | [NPY](tensors/0004778.npy) |
| 4779 | `model.layers.23.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.75 / 34.25 / -0.022196292877197266 / 4.575187297127834 | [NPY](tensors/0004779.npy) |
| 4780 | `model.layers.23.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 53.5 / 0.01480077240202162 / 1.7184249917191257 | [NPY](tensors/0004780.npy) |
| 4781 | `model.layers.23.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -20.375 / 13.3125 / -0.15772685781121254 / 3.777980270109 | [NPY](tensors/0004781.npy) |
| 4782 | `model.layers.23.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.875 / 8.5 / 0.019521628390066326 / 1.2798737832570977 | [NPY](tensors/0004782.npy) |
| 4783 | `model.layers.23.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5280.0 / 5408.0 / 3.819247097439236 / 235.92190417054542 | [NPY](tensors/0004783.npy) |
| 4784 | `model.layers.23.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5280.0 / 5408.0 / 3.819247097439236 / 235.92190417054542 | [NPY](tensors/0004784.npy) |
| 4785 | `model.layers.23.self_attn` | 40 | `output[1]` | [1, 64, 1, 327] | torch.bfloat16 → float32 | 5.516420653606247e-16 / 0.875 / 0.0013454121407973933 / 0.01352077913385299 | [NPY](tensors/0004785.npy) |
| 4786 | `model.layers.23.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 9408.0 / 5.003162977430556 / 544.6602476365844 | [NPY](tensors/0004786.npy) |
| 4787 | `model.layers.23.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 8.25 / -0.006838450166914198 / 1.214128467319322 | [NPY](tensors/0004787.npy) |
| 4788 | `model.layers.23.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 8.25 / -0.006838450166914198 / 1.214128467319322 | [NPY](tensors/0004788.npy) |
| 4789 | `model.layers.23.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.25 / 8.25 / -0.006838450166914198 / 1.214128467319322 | [NPY](tensors/0004789.npy) |
| 4790 | `model.layers.23.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4791 | `model.layers.23.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4792 | `model.layers.23.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4793 | `model.layers.23.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2480.0 / 2608.0 / -2.2564842224121096 / 166.63597656081524 | [NPY](tensors/0004793.npy) |
| 4794 | `model.layers.23.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2480.0 / 2608.0 / -2.2564842224121096 / 166.63597656081524 | [NPY](tensors/0004794.npy) |
| 4795 | `model.layers.23.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.21875 / 1.390625 / -0.00799509882926941 / 0.7722744351403579 | [NPY](tensors/0004795.npy) |
| 4796 | `model.layers.23` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7296.0 / 6976.0 / 2.7494683159722224 / 460.8633949965137 | [NPY](tensors/0004796.npy) |
| 4875 | `model.layers.23` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9216.0 / 10368.0 / 1.6057562934027778 / 471.64809728389594 | [NPY](tensors/0004875.npy) |
| 4876 | `model.layers.23` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004876.npy) |
| 4877 | `model.layers.23` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0004877.npy) |
| 4878 | `model.layers.23` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0004878.npy) |
| 4879 | `model.layers.23` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0004879.npy) |
| 4880 | `model.layers.23` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4881 | `model.layers.23` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4882 | `model.layers.23` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4883 | `model.layers.23.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9216.0 / 10368.0 / 1.6057562934027778 / 471.64809728389594 | [NPY](tensors/0004883.npy) |
| 4884 | `model.layers.23.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 59.0 / 0.017162337568071152 / 1.7708286147898837 | [NPY](tensors/0004884.npy) |
| 4885 | `model.layers.23.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 59.0 / 0.017162337568071152 / 1.7708286147898837 | [NPY](tensors/0004885.npy) |
| 4886 | `model.layers.23.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004886.npy) |
| 4887 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0004887.npy) |
| 4888 | `model.layers.23.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4889 | `model.layers.23.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4890 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0004890.npy) |
| 4891 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0004891.npy) |
| 4892 | `model.layers.23.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4893 | `model.layers.23.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 59.0 / 0.017162337568071152 / 1.7708286147898837 | [NPY](tensors/0004893.npy) |
| 4894 | `model.layers.23.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.8125 / 16.75 / 0.05394402169622481 / 1.6721094008711208 | [NPY](tensors/0004894.npy) |
| 4895 | `model.layers.23.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 59.0 / 0.017162337568071152 / 1.7708286147898837 | [NPY](tensors/0004895.npy) |
| 4896 | `model.layers.23.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.25 / 29.375 / -0.09364387392997742 / 4.421115019161867 | [NPY](tensors/0004896.npy) |
| 4897 | `model.layers.23.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 59.0 / 0.017162337568071152 / 1.7708286147898837 | [NPY](tensors/0004897.npy) |
| 4898 | `model.layers.23.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -21.25 / 17.0 / -0.02917119860649109 / 5.033477954026821 | [NPY](tensors/0004898.npy) |
| 4899 | `model.layers.23.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.75 / 7.25 / 0.051313315285369754 / 1.3687495379569563 | [NPY](tensors/0004899.npy) |
| 4900 | `model.layers.23.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2768.0 / 2768.0 / 1.6932684845394559 / 155.4193161047608 | [NPY](tensors/0004900.npy) |
| 4901 | `model.layers.23.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2768.0 / 2768.0 / 1.6932684845394559 / 155.4193161047608 | [NPY](tensors/0004901.npy) |
| 4902 | `model.layers.23.self_attn` | 41 | `output[1]` | [1, 64, 1, 328] | torch.bfloat16 → float32 | 1.2420620087993939e-15 / 0.9296875 / 0.001557022839323153 / 0.013262495863902789 | [NPY](tensors/0004902.npy) |
| 4903 | `model.layers.23.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7488.0 / 8576.0 / 3.3132758246527776 / 450.1322020054995 | [NPY](tensors/0004903.npy) |
| 4904 | `model.layers.23.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 11.25 / -0.00952786472108629 / 1.4110327992413447 | [NPY](tensors/0004904.npy) |
| 4905 | `model.layers.23.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 11.25 / -0.00952786472108629 / 1.4110327992413447 | [NPY](tensors/0004905.npy) |
| 4906 | `model.layers.23.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.0 / 11.25 / -0.00952786472108629 / 1.4110327992413447 | [NPY](tensors/0004906.npy) |
| 4907 | `model.layers.23.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4908 | `model.layers.23.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4909 | `model.layers.23.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4910 | `model.layers.23.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5312.0 / 4960.0 / -11.833120404349433 / 356.540117604301 | [NPY](tensors/0004910.npy) |
| 4911 | `model.layers.23.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5312.0 / 4960.0 / -11.833120404349433 / 356.540117604301 | [NPY](tensors/0004911.npy) |
| 4912 | `model.layers.23.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.484375 / 2.21875 / 0.02008056640625 / 1.3085368571083977 | [NPY](tensors/0004912.npy) |
| 4913 | `model.layers.23` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2528.0 / 3264.0 / -8.53891330295139 / 434.0205595620197 | [NPY](tensors/0004913.npy) |
| 4992 | `model.layers.23` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8448.0 / 9344.0 / 2.0173841688368057 / 437.59704797020987 | [NPY](tensors/0004992.npy) |
| 4993 | `model.layers.23` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004993.npy) |
| 4994 | `model.layers.23` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0004994.npy) |
| 4995 | `model.layers.23` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0004995.npy) |
| 4996 | `model.layers.23` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0004996.npy) |
| 4997 | `model.layers.23` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4998 | `model.layers.23` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4999 | `model.layers.23` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5000 | `model.layers.23.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8448.0 / 9344.0 / 2.0173841688368057 / 437.59704797020987 | [NPY](tensors/0005000.npy) |
| 5001 | `model.layers.23.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 57.5 / 0.024725231197145252 / 1.7663885250767095 | [NPY](tensors/0005001.npy) |
| 5002 | `model.layers.23.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 57.5 / 0.024725231197145252 / 1.7663885250767095 | [NPY](tensors/0005002.npy) |
| 5003 | `model.layers.23.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005003.npy) |
| 5004 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0005004.npy) |
| 5005 | `model.layers.23.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5006 | `model.layers.23.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5007 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0005007.npy) |
| 5008 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0005008.npy) |
| 5009 | `model.layers.23.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5010 | `model.layers.23.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 57.5 / 0.024725231197145252 / 1.7663885250767095 | [NPY](tensors/0005010.npy) |
| 5011 | `model.layers.23.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.25 / 16.375 / 0.044620812754146755 / 1.768414798727042 | [NPY](tensors/0005011.npy) |
| 5012 | `model.layers.23.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 57.5 / 0.024725231197145252 / 1.7663885250767095 | [NPY](tensors/0005012.npy) |
| 5013 | `model.layers.23.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.0 / 33.25 / -0.0813918337225914 / 4.41809125891595 | [NPY](tensors/0005013.npy) |
| 5014 | `model.layers.23.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 57.5 / 0.024725231197145252 / 1.7663885250767095 | [NPY](tensors/0005014.npy) |
| 5015 | `model.layers.23.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.3125 / 11.9375 / 0.022898346185684204 / 3.3901737267760548 | [NPY](tensors/0005015.npy) |
| 5016 | `model.layers.23.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.8125 / 8.875 / 0.06984161026775837 / 1.7988702037063955 | [NPY](tensors/0005016.npy) |
| 5017 | `model.layers.23.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3520.0 / 3520.0 / 3.6888117260403104 / 185.79995445544813 | [NPY](tensors/0005017.npy) |
| 5018 | `model.layers.23.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3520.0 / 3520.0 / 3.6888117260403104 / 185.79995445544813 | [NPY](tensors/0005018.npy) |
| 5019 | `model.layers.23.self_attn` | 42 | `output[1]` | [1, 64, 1, 329] | torch.bfloat16 → float32 | 7.806255641895632e-16 / 0.96484375 / 0.0020230397326812073 / 0.017098170479648806 | [NPY](tensors/0005019.npy) |
| 5020 | `model.layers.23.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7584.0 / 8448.0 / 5.722873263888889 / 468.74783551669 | [NPY](tensors/0005020.npy) |
| 5021 | `model.layers.23.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 9.125 / -0.0020603153440687393 / 1.3647243098796056 | [NPY](tensors/0005021.npy) |
| 5022 | `model.layers.23.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 9.125 / -0.0020603153440687393 / 1.3647243098796056 | [NPY](tensors/0005022.npy) |
| 5023 | `model.layers.23.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.25 / 9.125 / -0.0020603153440687393 / 1.3647243098796056 | [NPY](tensors/0005023.npy) |
| 5024 | `model.layers.23.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5025 | `model.layers.23.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5026 | `model.layers.23.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5027 | `model.layers.23.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6848.0 / 6144.0 / -1.0104766805966696 / 372.35663162474236 | [NPY](tensors/0005027.npy) |
| 5028 | `model.layers.23.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6848.0 / 6144.0 / -1.0104766805966696 / 372.35663162474236 | [NPY](tensors/0005028.npy) |
| 5029 | `model.layers.23.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.234375 / 1.6171875 / 0.0171356201171875 / 1.1499051257016817 | [NPY](tensors/0005029.npy) |
| 5030 | `model.layers.23` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1632.0 / 2464.0 / 4.731597222222222 / 407.55298576562615 | [NPY](tensors/0005030.npy) |

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
