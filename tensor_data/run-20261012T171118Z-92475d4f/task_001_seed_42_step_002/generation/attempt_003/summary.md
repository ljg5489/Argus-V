# Hook inspection: generation

Status: **complete**. 3870 full tensors; 5031 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.01282004653808037 / 2.782804974166853 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 873, 873] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.928704305609938e+38 / 1.1617341623636698e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 873, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7211662215764238 / 0.9199891152809843 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 873, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10053101652705901 / 0.6581213818663489 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 873] | torch.int64 → int64 | 0.0 / 872.0 / 436.0 / 252.01322716608877 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.01282004653808037 / 2.782804974166853 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 873, 2880] | torch.bfloat16 → float32 | -30.75 / 16.625 / -0.006904672552813602 / 0.7662174879723846 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 873, 2880] | torch.bfloat16 → float32 | -30.75 / 16.625 / -0.006904672552813602 / 0.7662174879723846 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 873, 873] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.928704305609938e+38 / 1.1617341623636698e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 873] | torch.int64 → int64 | 0.0 / 872.0 / 436.0 / 252.01322716608877 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 873, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7211662215764238 / 0.9199891152809843 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 873, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10053101652705901 / 0.6581213818663489 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -30.75 / 16.625 / -0.006904672552813602 / 0.7662174879723846 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 873, 4096] | torch.bfloat16 → float32 | -9.375 / 12.3125 / 0.023476189012862716 / 1.0167670773929487 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -30.75 / 16.625 / -0.006904672552813602 / 0.7662174879723846 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 873, 512] | torch.bfloat16 → float32 | -63.75 / 68.0 / 0.0293792572859536 / 5.747625237976729 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -30.75 / 16.625 / -0.006904672552813602 / 0.7662174879723846 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 873, 512] | torch.bfloat16 → float32 | -7.375 / 9.0 / -0.009682987253090958 / 1.1997622283918778 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 873, 4096] | torch.bfloat16 → float32 | -6.84375 / 6.5625 / -0.0058502151849089135 / 0.535631324552948 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 873, 2880] | torch.bfloat16 → float32 | -39.25 / 54.75 / 0.02885621755269568 / 1.1943378064330874 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -39.25 / 54.75 / 0.02885621755269568 / 1.1943378064330874 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 873, 873] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.000453370216687906 / 0.013448159636340726 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -89.0 / 71.0 / 0.016039339578817768 / 2.9912983882715185 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 873, 2880] | torch.bfloat16 → float32 | -6.625 / 3.0625 / 0.0011388357714969752 / 0.3325420922597567 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -6.625 / 3.0625 / 0.0011388357714969752 / 0.3325420922597567 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [873, 2880] | torch.bfloat16 → float32 | -6.625 / 3.0625 / 0.0011388357714969752 / 0.3325420922597567 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [873, 2880] | torch.bfloat16 → float32 | -49.75 / 135.0 / 0.016907212332903817 / 0.8127675084355972 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -49.75 / 135.0 / 0.016907212332903817 / 0.8127675084355972 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [873, 32] | torch.bfloat16 → float32 | -5.125 / 4.40625 / -0.11315649454263205 / 0.9906223071571594 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 873, 2880] | torch.bfloat16 → float32 | -85.0 / 156.0 / 0.03294539362840773 / 3.233935571938582 | [NPY](tensors/0000038.npy) |
| 117 | `model.layers.0` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0000117.npy) |
| 118 | `model.layers.0` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000118.npy) |
| 119 | `model.layers.0` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.649322509765625 / 0.9833264324529841 | [NPY](tensors/0000119.npy) |
| 120 | `model.layers.0` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.024361848831176758 / 0.6489880782497579 | [NPY](tensors/0000120.npy) |
| 121 | `model.layers.0` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 873.0 / 873.0 / 873.0 / 0.0 | [NPY](tensors/0000121.npy) |
| 122 | `model.layers.0` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 123 | `model.layers.0` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 124 | `model.layers.0` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 125 | `model.layers.0.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0000125.npy) |
| 126 | `model.layers.0.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000126.npy) |
| 127 | `model.layers.0.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000127.npy) |
| 128 | `model.layers.0.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000128.npy) |
| 129 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 873.0 / 873.0 / 873.0 / 0.0 | [NPY](tensors/0000129.npy) |
| 130 | `model.layers.0.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 131 | `model.layers.0.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 132 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.649322509765625 / 0.9833264324529841 | [NPY](tensors/0000132.npy) |
| 133 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.024361848831176758 / 0.6489880782497579 | [NPY](tensors/0000133.npy) |
| 134 | `model.layers.0.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 135 | `model.layers.0.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000135.npy) |
| 136 | `model.layers.0.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.34375 / 8.125 / 0.009809806477278471 / 1.0602451281469458 | [NPY](tensors/0000136.npy) |
| 137 | `model.layers.0.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000137.npy) |
| 138 | `model.layers.0.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.5 / 52.75 / 0.05987404379993677 / 5.486411371880323 | [NPY](tensors/0000138.npy) |
| 139 | `model.layers.0.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0000139.npy) |
| 140 | `model.layers.0.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.125 / 3.75 / 0.02330493927001953 / 1.1486258589347933 | [NPY](tensors/0000140.npy) |
| 141 | `model.layers.0.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 4.0 / 0.0003490097587928176 / 0.7125054102902398 | [NPY](tensors/0000141.npy) |
| 142 | `model.layers.0.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.875 / 41.25 / 0.03225293548570739 / 1.2731934371801212 | [NPY](tensors/0000142.npy) |
| 143 | `model.layers.0.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.875 / 41.25 / 0.03225293548570739 / 1.2731934371801212 | [NPY](tensors/0000143.npy) |
| 144 | `model.layers.0.self_attn` | 1 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.004450508875851838 / 0.04477675032771631 | [NPY](tensors/0000144.npy) |
| 145 | `model.layers.0.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.75 / 45.75 / -0.031755553351508245 / 2.8067207307951856 | [NPY](tensors/0000145.npy) |
| 146 | `model.layers.0.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.015625 / 1.5625 / 0.0017045746246973673 / 0.40336030379891896 | [NPY](tensors/0000146.npy) |
| 147 | `model.layers.0.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.015625 / 1.5625 / 0.0017045746246973673 / 0.40336030379891896 | [NPY](tensors/0000147.npy) |
| 148 | `model.layers.0.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.015625 / 1.5625 / 0.0017045746246973673 / 0.40336030379891896 | [NPY](tensors/0000148.npy) |
| 149 | `model.layers.0.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 150 | `model.layers.0.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 151 | `model.layers.0.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 152 | `model.layers.0.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.25 / 21.25 / 0.014266606503062778 / 0.6830772379670581 | [NPY](tensors/0000152.npy) |
| 153 | `model.layers.0.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.25 / 21.25 / 0.014266606503062778 / 0.6830772379670581 | [NPY](tensors/0000153.npy) |
| 154 | `model.layers.0.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.84375 / 1.96875 / -0.053619384765625 / 0.7981761840449126 | [NPY](tensors/0000154.npy) |
| 155 | `model.layers.0` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 67.0 / -0.01721350351969401 / 3.110993534558239 | [NPY](tensors/0000155.npy) |
| 234 | `model.layers.0` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 34.75 / 0.06460592945416768 / 2.603620301499426 | [NPY](tensors/0000234.npy) |
| 235 | `model.layers.0` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000235.npy) |
| 236 | `model.layers.0` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.663970947265625 / 0.9817896713297021 | [NPY](tensors/0000236.npy) |
| 237 | `model.layers.0` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.25 / 1.34375 / 0.07146221399307251 / 0.6328787006162191 | [NPY](tensors/0000237.npy) |
| 238 | `model.layers.0` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 874.0 / 874.0 / 874.0 / 0.0 | [NPY](tensors/0000238.npy) |
| 239 | `model.layers.0` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 240 | `model.layers.0` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 241 | `model.layers.0` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 242 | `model.layers.0.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 34.75 / 0.06460592945416768 / 2.603620301499426 | [NPY](tensors/0000242.npy) |
| 243 | `model.layers.0.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0000243.npy) |
| 244 | `model.layers.0.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0000244.npy) |
| 245 | `model.layers.0.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000245.npy) |
| 246 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 874.0 / 874.0 / 874.0 / 0.0 | [NPY](tensors/0000246.npy) |
| 247 | `model.layers.0.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 248 | `model.layers.0.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 249 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.663970947265625 / 0.9817896713297021 | [NPY](tensors/0000249.npy) |
| 250 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.25 / 1.34375 / 0.07146221399307251 / 0.6328787006162191 | [NPY](tensors/0000250.npy) |
| 251 | `model.layers.0.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 252 | `model.layers.0.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0000252.npy) |
| 253 | `model.layers.0.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.71875 / 8.4375 / 0.008836216118652374 / 1.127863321857116 | [NPY](tensors/0000253.npy) |
| 254 | `model.layers.0.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0000254.npy) |
| 255 | `model.layers.0.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -47.25 / 52.5 / -0.01974540948867798 / 5.528074362257702 | [NPY](tensors/0000255.npy) |
| 256 | `model.layers.0.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0000256.npy) |
| 257 | `model.layers.0.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.34375 / 5.1875 / 0.04988500475883484 / 1.3788012115777875 | [NPY](tensors/0000257.npy) |
| 258 | `model.layers.0.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.96875 / 3.90625 / -0.0043751135090133175 / 0.6043462327442407 | [NPY](tensors/0000258.npy) |
| 259 | `model.layers.0.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.375 / 42.75 / 0.032042082813051015 / 1.2610786638358924 | [NPY](tensors/0000259.npy) |
| 260 | `model.layers.0.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.375 / 42.75 / 0.032042082813051015 / 1.2610786638358924 | [NPY](tensors/0000260.npy) |
| 261 | `model.layers.0.self_attn` | 2 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003168363757344355 / 0.03788593233899117 | [NPY](tensors/0000261.npy) |
| 262 | `model.layers.0.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 41.75 / 0.09666644202338324 / 2.906992502981706 | [NPY](tensors/0000262.npy) |
| 263 | `model.layers.0.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.75 / 1.578125 / 0.004193162586953905 / 0.38329261699046485 | [NPY](tensors/0000263.npy) |
| 264 | `model.layers.0.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.75 / 1.578125 / 0.004193162586953905 / 0.38329261699046485 | [NPY](tensors/0000264.npy) |
| 265 | `model.layers.0.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.75 / 1.578125 / 0.004193162586953905 / 0.38329261699046485 | [NPY](tensors/0000265.npy) |
| 266 | `model.layers.0.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 267 | `model.layers.0.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 268 | `model.layers.0.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 269 | `model.layers.0.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.09375 / 18.5 / 0.020857090730634 / 0.5968550383327169 | [NPY](tensors/0000269.npy) |
| 270 | `model.layers.0.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.09375 / 18.5 / 0.020857090730634 / 0.5968550383327169 | [NPY](tensors/0000270.npy) |
| 271 | `model.layers.0.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.453125 / 1.875 / -0.21675872802734375 / 0.8463419602771692 | [NPY](tensors/0000271.npy) |
| 272 | `model.layers.0` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 58.0 / 0.11750557687547472 / 3.1261753280943414 | [NPY](tensors/0000272.npy) |
| 351 | `model.layers.0` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0000351.npy) |
| 352 | `model.layers.0` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000352.npy) |
| 353 | `model.layers.0` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.6338043212890625 / 0.990232497628255 | [NPY](tensors/0000353.npy) |
| 354 | `model.layers.0` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.10754281282424927 / 0.6458776678737284 | [NPY](tensors/0000354.npy) |
| 355 | `model.layers.0` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 875.0 / 875.0 / 875.0 / 0.0 | [NPY](tensors/0000355.npy) |
| 356 | `model.layers.0` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 357 | `model.layers.0` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 358 | `model.layers.0` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 359 | `model.layers.0.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0000359.npy) |
| 360 | `model.layers.0.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0000360.npy) |
| 361 | `model.layers.0.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0000361.npy) |
| 362 | `model.layers.0.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000362.npy) |
| 363 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 875.0 / 875.0 / 875.0 / 0.0 | [NPY](tensors/0000363.npy) |
| 364 | `model.layers.0.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 365 | `model.layers.0.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 366 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.6338043212890625 / 0.990232497628255 | [NPY](tensors/0000366.npy) |
| 367 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.10754281282424927 / 0.6458776678737284 | [NPY](tensors/0000367.npy) |
| 368 | `model.layers.0.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 369 | `model.layers.0.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0000369.npy) |
| 370 | `model.layers.0.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 7.625 / 0.011268170550465584 / 0.9167789321734896 | [NPY](tensors/0000370.npy) |
| 371 | `model.layers.0.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0000371.npy) |
| 372 | `model.layers.0.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 43.75 / 0.046514674089848995 / 4.791095594233786 | [NPY](tensors/0000372.npy) |
| 373 | `model.layers.0.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0000373.npy) |
| 374 | `model.layers.0.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.84375 / 4.125 / -0.01808762550354004 / 1.3178383551916408 | [NPY](tensors/0000374.npy) |
| 375 | `model.layers.0.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.28125 / 4.875 / -0.008545308031898458 / 0.4550382388299658 | [NPY](tensors/0000375.npy) |
| 376 | `model.layers.0.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.625 / 39.5 / 0.02660040400094456 / 1.1531095099356694 | [NPY](tensors/0000376.npy) |
| 377 | `model.layers.0.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.625 / 39.5 / 0.02660040400094456 / 1.1531095099356694 | [NPY](tensors/0000377.npy) |
| 378 | `model.layers.0.self_attn` | 3 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.00314317062846075 / 0.025762025401688243 | [NPY](tensors/0000378.npy) |
| 379 | `model.layers.0.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.75 / 40.5 / 0.015775622261895075 / 2.8532914030062297 | [NPY](tensors/0000379.npy) |
| 380 | `model.layers.0.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.1875 / 1.921875 / 0.007847221030129328 / 0.37123810122223616 | [NPY](tensors/0000380.npy) |
| 381 | `model.layers.0.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.1875 / 1.921875 / 0.007847221030129328 / 0.37123810122223616 | [NPY](tensors/0000381.npy) |
| 382 | `model.layers.0.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.1875 / 1.921875 / 0.007847221030129328 / 0.37123810122223616 | [NPY](tensors/0000382.npy) |
| 383 | `model.layers.0.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 384 | `model.layers.0.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 385 | `model.layers.0.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 386 | `model.layers.0.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.125 / 8.25 / 0.031560373140705957 / 0.5243531647994433 | [NPY](tensors/0000386.npy) |
| 387 | `model.layers.0.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.125 / 8.25 / 0.031560373140705957 / 0.5243531647994433 | [NPY](tensors/0000387.npy) |
| 388 | `model.layers.0.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0234375 / 1.8046875 / -0.07893228530883789 / 0.6500535876412055 | [NPY](tensors/0000388.npy) |
| 389 | `model.layers.0` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.25 / 48.5 / 0.047314389546712236 / 3.0506646948436185 | [NPY](tensors/0000389.npy) |
| 468 | `model.layers.0` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 43.75 / 0.02880006796783871 / 2.9013049797239288 | [NPY](tensors/0000468.npy) |
| 469 | `model.layers.0` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000469.npy) |
| 470 | `model.layers.0` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.58746337890625 / 1.0206486490707742 | [NPY](tensors/0000470.npy) |
| 471 | `model.layers.0` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.3203125 / 0.10449105501174927 / 0.6417963143458147 | [NPY](tensors/0000471.npy) |
| 472 | `model.layers.0` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 876.0 / 876.0 / 876.0 / 0.0 | [NPY](tensors/0000472.npy) |
| 473 | `model.layers.0` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 474 | `model.layers.0` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 475 | `model.layers.0` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 476 | `model.layers.0.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 43.75 / 0.02880006796783871 / 2.9013049797239288 | [NPY](tensors/0000476.npy) |
| 477 | `model.layers.0.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000477.npy) |
| 478 | `model.layers.0.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000478.npy) |
| 479 | `model.layers.0.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000479.npy) |
| 480 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 876.0 / 876.0 / 876.0 / 0.0 | [NPY](tensors/0000480.npy) |
| 481 | `model.layers.0.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 482 | `model.layers.0.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 483 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.58746337890625 / 1.0206486490707742 | [NPY](tensors/0000483.npy) |
| 484 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.3203125 / 0.10449105501174927 / 0.6417963143458147 | [NPY](tensors/0000484.npy) |
| 485 | `model.layers.0.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 486 | `model.layers.0.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000486.npy) |
| 487 | `model.layers.0.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 7.4375 / 0.039632019703276455 / 0.9975220123045838 | [NPY](tensors/0000487.npy) |
| 488 | `model.layers.0.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000488.npy) |
| 489 | `model.layers.0.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.5 / 41.25 / 0.060565054416656494 / 4.792407804689708 | [NPY](tensors/0000489.npy) |
| 490 | `model.layers.0.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000490.npy) |
| 491 | `model.layers.0.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.9375 / 3.90625 / 0.001153320074081421 / 1.2325447380756387 | [NPY](tensors/0000491.npy) |
| 492 | `model.layers.0.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.46875 / 3.25 / 0.00212897831806913 / 0.6468720093470368 | [NPY](tensors/0000492.npy) |
| 493 | `model.layers.0.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.6875 / 39.25 / 0.04004447240796354 / 1.18740467254306 | [NPY](tensors/0000493.npy) |
| 494 | `model.layers.0.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.6875 / 39.25 / 0.04004447240796354 / 1.18740467254306 | [NPY](tensors/0000494.npy) |
| 495 | `model.layers.0.self_attn` | 4 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.00404216895460871 / 0.0395885804887854 | [NPY](tensors/0000495.npy) |
| 496 | `model.layers.0.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 42.75 / 0.06863897111680772 / 3.015357710430079 | [NPY](tensors/0000496.npy) |
| 497 | `model.layers.0.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.78125 / 2.109375 / 0.009276022844844394 / 0.3567421813131599 | [NPY](tensors/0000497.npy) |
| 498 | `model.layers.0.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.78125 / 2.109375 / 0.009276022844844394 / 0.3567421813131599 | [NPY](tensors/0000498.npy) |
| 499 | `model.layers.0.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.78125 / 2.109375 / 0.009276022844844394 / 0.3567421813131599 | [NPY](tensors/0000499.npy) |
| 500 | `model.layers.0.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 501 | `model.layers.0.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 502 | `model.layers.0.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 503 | `model.layers.0.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.21875 / 36.5 / 0.023873837292194368 / 1.1635990371333755 | [NPY](tensors/0000503.npy) |
| 504 | `model.layers.0.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.21875 / 36.5 / 0.023873837292194368 / 1.1635990371333755 | [NPY](tensors/0000504.npy) |
| 505 | `model.layers.0.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.4609375 / 2.375 / -0.048614501953125 / 0.9624996508676651 | [NPY](tensors/0000505.npy) |
| 506 | `model.layers.0` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.5 / 61.25 / 0.09266423119439018 / 3.3228819560328913 | [NPY](tensors/0000506.npy) |
| 585 | `model.layers.0` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 45.75 / 0.04227736194928487 / 3.1518798398795616 | [NPY](tensors/0000585.npy) |
| 586 | `model.layers.0` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000586.npy) |
| 587 | `model.layers.0` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.558441162109375 / 1.0101761449217725 | [NPY](tensors/0000587.npy) |
| 588 | `model.layers.0` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3359375 / 0.06921488046646118 / 0.6876239253025267 | [NPY](tensors/0000588.npy) |
| 589 | `model.layers.0` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 877.0 / 877.0 / 877.0 / 0.0 | [NPY](tensors/0000589.npy) |
| 590 | `model.layers.0` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 591 | `model.layers.0` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 592 | `model.layers.0` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 593 | `model.layers.0.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 45.75 / 0.04227736194928487 / 3.1518798398795616 | [NPY](tensors/0000593.npy) |
| 594 | `model.layers.0.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000594.npy) |
| 595 | `model.layers.0.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000595.npy) |
| 596 | `model.layers.0.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000596.npy) |
| 597 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 877.0 / 877.0 / 877.0 / 0.0 | [NPY](tensors/0000597.npy) |
| 598 | `model.layers.0.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 599 | `model.layers.0.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 600 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.558441162109375 / 1.0101761449217725 | [NPY](tensors/0000600.npy) |
| 601 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3359375 / 0.06921488046646118 / 0.6876239253025267 | [NPY](tensors/0000601.npy) |
| 602 | `model.layers.0.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 603 | `model.layers.0.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000603.npy) |
| 604 | `model.layers.0.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5 / 8.1875 / 0.022865560371428728 / 0.9733268065645532 | [NPY](tensors/0000604.npy) |
| 605 | `model.layers.0.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000605.npy) |
| 606 | `model.layers.0.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.75 / 47.0 / 0.09419560432434082 / 4.904277940788795 | [NPY](tensors/0000606.npy) |
| 607 | `model.layers.0.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000607.npy) |
| 608 | `model.layers.0.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 4.34375 / -0.08974748849868774 / 1.1126171556291353 | [NPY](tensors/0000608.npy) |
| 609 | `model.layers.0.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.09375 / 3.796875 / -0.006726770778186619 / 0.5811128196706009 | [NPY](tensors/0000609.npy) |
| 610 | `model.layers.0.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 37.25 / 0.028425772653685677 / 1.1489226725145643 | [NPY](tensors/0000610.npy) |
| 611 | `model.layers.0.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 37.25 / 0.028425772653685677 / 1.1489226725145643 | [NPY](tensors/0000611.npy) |
| 612 | `model.layers.0.self_attn` | 5 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004129380072965364 / 0.041670199692871036 | [NPY](tensors/0000612.npy) |
| 613 | `model.layers.0.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 44.75 / 0.07060761451721191 / 3.2884472549198462 | [NPY](tensors/0000613.npy) |
| 614 | `model.layers.0.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.203125 / 1.96875 / 0.009547676146030425 / 0.32460673434977405 | [NPY](tensors/0000614.npy) |
| 615 | `model.layers.0.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.203125 / 1.96875 / 0.009547676146030425 / 0.32460673434977405 | [NPY](tensors/0000615.npy) |
| 616 | `model.layers.0.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.203125 / 1.96875 / 0.009547676146030425 / 0.32460673434977405 | [NPY](tensors/0000616.npy) |
| 617 | `model.layers.0.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 618 | `model.layers.0.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 619 | `model.layers.0.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 620 | `model.layers.0.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.96875 / 17.75 / 0.02936712106068929 / 0.7199396440882879 | [NPY](tensors/0000620.npy) |
| 621 | `model.layers.0.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.96875 / 17.75 / 0.02936712106068929 / 0.7199396440882879 | [NPY](tensors/0000621.npy) |
| 622 | `model.layers.0.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.828125 / 2.0 / -0.12928009033203125 / 1.0760535107309155 | [NPY](tensors/0000622.npy) |
| 623 | `model.layers.0` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 58.25 / 0.10018157958984375 / 3.430106338070662 | [NPY](tensors/0000623.npy) |
| 702 | `model.layers.0` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0000702.npy) |
| 703 | `model.layers.0` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000703.npy) |
| 704 | `model.layers.0` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5615997314453125 / 0.9848671705266577 | [NPY](tensors/0000704.npy) |
| 705 | `model.layers.0` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.030482351779937744 / 0.7236419726526301 | [NPY](tensors/0000705.npy) |
| 706 | `model.layers.0` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 878.0 / 878.0 / 878.0 / 0.0 | [NPY](tensors/0000706.npy) |
| 707 | `model.layers.0` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 708 | `model.layers.0` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 709 | `model.layers.0` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 710 | `model.layers.0.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0000710.npy) |
| 711 | `model.layers.0.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000711.npy) |
| 712 | `model.layers.0.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000712.npy) |
| 713 | `model.layers.0.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000713.npy) |
| 714 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 878.0 / 878.0 / 878.0 / 0.0 | [NPY](tensors/0000714.npy) |
| 715 | `model.layers.0.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 716 | `model.layers.0.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 717 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5615997314453125 / 0.9848671705266577 | [NPY](tensors/0000717.npy) |
| 718 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.030482351779937744 / 0.7236419726526301 | [NPY](tensors/0000718.npy) |
| 719 | `model.layers.0.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 720 | `model.layers.0.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000720.npy) |
| 721 | `model.layers.0.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 9.25 / 0.06582052947487682 / 1.0317253511582722 | [NPY](tensors/0000721.npy) |
| 722 | `model.layers.0.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000722.npy) |
| 723 | `model.layers.0.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.5 / 59.75 / -0.027341485023498535 / 6.496414800406944 | [NPY](tensors/0000723.npy) |
| 724 | `model.layers.0.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000724.npy) |
| 725 | `model.layers.0.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.453125 / 4.6875 / 0.06333106756210327 / 0.9556167387162166 | [NPY](tensors/0000725.npy) |
| 726 | `model.layers.0.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.28125 / 4.34375 / -0.014057498221518472 / 0.5695777655597617 | [NPY](tensors/0000726.npy) |
| 727 | `model.layers.0.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 39.25 / 0.033039094507694246 / 1.16319834182343 | [NPY](tensors/0000727.npy) |
| 728 | `model.layers.0.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 39.25 / 0.033039094507694246 / 1.16319834182343 | [NPY](tensors/0000728.npy) |
| 729 | `model.layers.0.self_attn` | 6 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0036878591837909863 / 0.04097076463221661 | [NPY](tensors/0000729.npy) |
| 730 | `model.layers.0.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.5 / 37.75 / 0.0821401490105523 / 2.6478429779219863 | [NPY](tensors/0000730.npy) |
| 731 | `model.layers.0.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.46875 / 1.8984375 / 0.009819889730877347 / 0.32597175150716684 | [NPY](tensors/0000731.npy) |
| 732 | `model.layers.0.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.46875 / 1.8984375 / 0.009819889730877347 / 0.32597175150716684 | [NPY](tensors/0000732.npy) |
| 733 | `model.layers.0.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.46875 / 1.8984375 / 0.009819889730877347 / 0.32597175150716684 | [NPY](tensors/0000733.npy) |
| 734 | `model.layers.0.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 735 | `model.layers.0.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 736 | `model.layers.0.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 737 | `model.layers.0.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.375 / 29.625 / 0.02462968346145418 / 1.1272174968767195 | [NPY](tensors/0000737.npy) |
| 738 | `model.layers.0.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.375 / 29.625 / 0.02462968346145418 / 1.1272174968767195 | [NPY](tensors/0000738.npy) |
| 739 | `model.layers.0.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.34375 / 2.53125 / -0.09344482421875 / 1.3286211643735168 | [NPY](tensors/0000739.npy) |
| 740 | `model.layers.0` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 66.0 / 0.10694075690375435 / 2.9536432908438646 | [NPY](tensors/0000740.npy) |
| 819 | `model.layers.0` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 34.0 / -0.06892566875451141 / 2.9103161811185028 | [NPY](tensors/0000819.npy) |
| 820 | `model.layers.0` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000820.npy) |
| 821 | `model.layers.0` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.5797119140625 / 1.0186800490978136 | [NPY](tensors/0000821.npy) |
| 822 | `model.layers.0` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.296875 / 0.009048700332641602 / 0.6598895155407865 | [NPY](tensors/0000822.npy) |
| 823 | `model.layers.0` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 879.0 / 879.0 / 879.0 / 0.0 | [NPY](tensors/0000823.npy) |
| 824 | `model.layers.0` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 825 | `model.layers.0` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 826 | `model.layers.0` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 827 | `model.layers.0.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 34.0 / -0.06892566875451141 / 2.9103161811185028 | [NPY](tensors/0000827.npy) |
| 828 | `model.layers.0.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.25 / 6.8125 / -0.02531518783006403 / 0.7801355582869979 | [NPY](tensors/0000828.npy) |
| 829 | `model.layers.0.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.25 / 6.8125 / -0.02531518783006403 / 0.7801355582869979 | [NPY](tensors/0000829.npy) |
| 830 | `model.layers.0.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000830.npy) |
| 831 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 879.0 / 879.0 / 879.0 / 0.0 | [NPY](tensors/0000831.npy) |
| 832 | `model.layers.0.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 833 | `model.layers.0.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 834 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.5797119140625 / 1.0186800490978136 | [NPY](tensors/0000834.npy) |
| 835 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.296875 / 0.009048700332641602 / 0.6598895155407865 | [NPY](tensors/0000835.npy) |
| 836 | `model.layers.0.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 837 | `model.layers.0.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.25 / 6.8125 / -0.02531518783006403 / 0.7801355582869979 | [NPY](tensors/0000837.npy) |
| 838 | `model.layers.0.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.25 / 8.4375 / 0.02174369659041986 / 0.9935657308954511 | [NPY](tensors/0000838.npy) |
| 839 | `model.layers.0.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.25 / 6.8125 / -0.02531518783006403 / 0.7801355582869979 | [NPY](tensors/0000839.npy) |
| 840 | `model.layers.0.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -54.0 / 46.75 / -0.054525554180145264 / 5.650706713110041 | [NPY](tensors/0000840.npy) |
| 841 | `model.layers.0.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.25 / 6.8125 / -0.02531518783006403 / 0.7801355582869979 | [NPY](tensors/0000841.npy) |
| 842 | `model.layers.0.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.875 / 5.1875 / -0.10895019769668579 / 1.2129399361509814 | [NPY](tensors/0000842.npy) |
| 843 | `model.layers.0.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.09375 / 3.5 / -0.004269229067517699 / 0.5224029757578368 | [NPY](tensors/0000843.npy) |
| 844 | `model.layers.0.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0625 / 43.75 / 0.03269975417190128 / 1.2531223181046365 | [NPY](tensors/0000844.npy) |
| 845 | `model.layers.0.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0625 / 43.75 / 0.03269975417190128 / 1.2531223181046365 | [NPY](tensors/0000845.npy) |
| 846 | `model.layers.0.self_attn` | 7 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.0032166184194155787 / 0.0342154911169952 | [NPY](tensors/0000846.npy) |
| 847 | `model.layers.0.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.5 / 40.5 / -0.03621266153123644 / 3.105901238146278 | [NPY](tensors/0000847.npy) |
| 848 | `model.layers.0.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.28125 / 1.453125 / -0.0070608192019992405 / 0.3311586116247547 | [NPY](tensors/0000848.npy) |
| 849 | `model.layers.0.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.28125 / 1.453125 / -0.0070608192019992405 / 0.3311586116247547 | [NPY](tensors/0000849.npy) |
| 850 | `model.layers.0.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.28125 / 1.453125 / -0.0070608192019992405 / 0.3311586116247547 | [NPY](tensors/0000850.npy) |
| 851 | `model.layers.0.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 852 | `model.layers.0.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 853 | `model.layers.0.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 854 | `model.layers.0.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.5625 / 33.25 / 0.03940439754062229 / 1.0067543443029365 | [NPY](tensors/0000854.npy) |
| 855 | `model.layers.0.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.5625 / 33.25 / 0.03940439754062229 / 1.0067543443029365 | [NPY](tensors/0000855.npy) |
| 856 | `model.layers.0.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.046875 / 1.2265625 / -0.17240524291992188 / 0.7521881687423816 | [NPY](tensors/0000856.npy) |
| 857 | `model.layers.0` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 73.0 / 0.003281924459669325 / 3.538704785435855 | [NPY](tensors/0000857.npy) |
| 936 | `model.layers.0` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 40.75 / -0.019926850539114742 / 2.69944275663135 | [NPY](tensors/0000936.npy) |
| 937 | `model.layers.0` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000937.npy) |
| 938 | `model.layers.0` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5914459228515625 / 1.036270522436494 | [NPY](tensors/0000938.npy) |
| 939 | `model.layers.0` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.0005860328674316406 / 0.6206299087009224 | [NPY](tensors/0000939.npy) |
| 940 | `model.layers.0` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 880.0 / 880.0 / 880.0 / 0.0 | [NPY](tensors/0000940.npy) |
| 941 | `model.layers.0` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 942 | `model.layers.0` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 943 | `model.layers.0` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 944 | `model.layers.0.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 40.75 / -0.019926850539114742 / 2.69944275663135 | [NPY](tensors/0000944.npy) |
| 945 | `model.layers.0.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.1875 / 9.625 / -0.011637009142173662 / 0.7441323285093859 | [NPY](tensors/0000945.npy) |
| 946 | `model.layers.0.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.1875 / 9.625 / -0.011637009142173662 / 0.7441323285093859 | [NPY](tensors/0000946.npy) |
| 947 | `model.layers.0.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000947.npy) |
| 948 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 880.0 / 880.0 / 880.0 / 0.0 | [NPY](tensors/0000948.npy) |
| 949 | `model.layers.0.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 950 | `model.layers.0.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 951 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5914459228515625 / 1.036270522436494 | [NPY](tensors/0000951.npy) |
| 952 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.0005860328674316406 / 0.6206299087009224 | [NPY](tensors/0000952.npy) |
| 953 | `model.layers.0.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 954 | `model.layers.0.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.1875 / 9.625 / -0.011637009142173662 / 0.7441323285093859 | [NPY](tensors/0000954.npy) |
| 955 | `model.layers.0.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.78125 / 8.625 / 0.041696956381201744 / 1.038301012764146 | [NPY](tensors/0000955.npy) |
| 956 | `model.layers.0.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.1875 / 9.625 / -0.011637009142173662 / 0.7441323285093859 | [NPY](tensors/0000956.npy) |
| 957 | `model.layers.0.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -56.0 / 53.75 / -0.09252414107322693 / 6.3870725073466925 | [NPY](tensors/0000957.npy) |
| 958 | `model.layers.0.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.1875 / 9.625 / -0.011637009142173662 / 0.7441323285093859 | [NPY](tensors/0000958.npy) |
| 959 | `model.layers.0.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.0 / 4.25 / 0.05876107420772314 / 1.2365558933978904 | [NPY](tensors/0000959.npy) |
| 960 | `model.layers.0.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.15625 / 4.15625 / -0.019669356060148857 / 0.533657845941416 | [NPY](tensors/0000960.npy) |
| 961 | `model.layers.0.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.15625 / 35.75 / 0.02486373963507099 / 1.0737422075611327 | [NPY](tensors/0000961.npy) |
| 962 | `model.layers.0.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.15625 / 35.75 / 0.02486373963507099 / 1.0737422075611327 | [NPY](tensors/0000962.npy) |
| 963 | `model.layers.0.self_attn` | 8 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003113275805672778 / 0.03608883523045256 | [NPY](tensors/0000963.npy) |
| 964 | `model.layers.0.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.875 / 39.0 / 0.0050753169589572485 / 2.74830756111953 | [NPY](tensors/0000964.npy) |
| 965 | `model.layers.0.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.90625 / 2.640625 / -0.005183468593491448 / 0.31234847616715994 | [NPY](tensors/0000965.npy) |
| 966 | `model.layers.0.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.90625 / 2.640625 / -0.005183468593491448 / 0.31234847616715994 | [NPY](tensors/0000966.npy) |
| 967 | `model.layers.0.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.90625 / 2.640625 / -0.005183468593491448 / 0.31234847616715994 | [NPY](tensors/0000967.npy) |
| 968 | `model.layers.0.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 969 | `model.layers.0.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 970 | `model.layers.0.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 971 | `model.layers.0.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.09375 / 17.875 / 0.012228465576966604 / 0.7215867415117255 | [NPY](tensors/0000971.npy) |
| 972 | `model.layers.0.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.09375 / 17.875 / 0.012228465576966604 / 0.7215867415117255 | [NPY](tensors/0000972.npy) |
| 973 | `model.layers.0.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.625 / 1.9453125 / -0.06769561767578125 / 0.9895076723013477 | [NPY](tensors/0000973.npy) |
| 974 | `model.layers.0` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 53.0 / 0.017438602447509766 / 2.795664058909391 | [NPY](tensors/0000974.npy) |
| 1053 | `model.layers.0` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.625 / 33.75 / -0.0492422280419204 / 2.5527406175507075 | [NPY](tensors/0001053.npy) |
| 1054 | `model.layers.0` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001054.npy) |
| 1055 | `model.layers.0` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.594635009765625 / 0.998380462956763 | [NPY](tensors/0001055.npy) |
| 1056 | `model.layers.0` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3125 / -0.016051054000854492 / 0.6776192851250942 | [NPY](tensors/0001056.npy) |
| 1057 | `model.layers.0` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 881.0 / 881.0 / 881.0 / 0.0 | [NPY](tensors/0001057.npy) |
| 1058 | `model.layers.0` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1059 | `model.layers.0` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1060 | `model.layers.0` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1061 | `model.layers.0.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.625 / 33.75 / -0.0492422280419204 / 2.5527406175507075 | [NPY](tensors/0001061.npy) |
| 1062 | `model.layers.0.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 8.1875 / -0.014487382024526596 / 0.7412558308273887 | [NPY](tensors/0001062.npy) |
| 1063 | `model.layers.0.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 8.1875 / -0.014487382024526596 / 0.7412558308273887 | [NPY](tensors/0001063.npy) |
| 1064 | `model.layers.0.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001064.npy) |
| 1065 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 881.0 / 881.0 / 881.0 / 0.0 | [NPY](tensors/0001065.npy) |
| 1066 | `model.layers.0.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1067 | `model.layers.0.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1068 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.594635009765625 / 0.998380462956763 | [NPY](tensors/0001068.npy) |
| 1069 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3125 / -0.016051054000854492 / 0.6776192851250942 | [NPY](tensors/0001069.npy) |
| 1070 | `model.layers.0.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1071 | `model.layers.0.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 8.1875 / -0.014487382024526596 / 0.7412558308273887 | [NPY](tensors/0001071.npy) |
| 1072 | `model.layers.0.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.6875 / 9.6875 / 0.014851998537778854 / 1.0286167741209238 | [NPY](tensors/0001072.npy) |
| 1073 | `model.layers.0.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 8.1875 / -0.014487382024526596 / 0.7412558308273887 | [NPY](tensors/0001073.npy) |
| 1074 | `model.layers.0.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.0 / 53.75 / 0.1754077970981598 / 5.899641413829817 | [NPY](tensors/0001074.npy) |
| 1075 | `model.layers.0.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 8.1875 / -0.014487382024526596 / 0.7412558308273887 | [NPY](tensors/0001075.npy) |
| 1076 | `model.layers.0.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.40625 / 7.25 / -0.04820074886083603 / 1.4493330464200218 | [NPY](tensors/0001076.npy) |
| 1077 | `model.layers.0.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.53125 / 4.0625 / -0.00039557719583172 / 0.47785352493610794 | [NPY](tensors/0001077.npy) |
| 1078 | `model.layers.0.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 40.75 / 0.02915318104852405 / 1.2245181541717276 | [NPY](tensors/0001078.npy) |
| 1079 | `model.layers.0.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 40.75 / 0.02915318104852405 / 1.2245181541717276 | [NPY](tensors/0001079.npy) |
| 1080 | `model.layers.0.self_attn` | 9 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.953125 / 0.00262209696455913 / 0.03046553804706537 | [NPY](tensors/0001080.npy) |
| 1081 | `model.layers.0.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 40.0 / -0.020062033335367838 / 2.8765022993505123 | [NPY](tensors/0001081.npy) |
| 1082 | `model.layers.0.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9765625 / 1.3125 / 0.0024035768376456366 / 0.34622894200994053 | [NPY](tensors/0001082.npy) |
| 1083 | `model.layers.0.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9765625 / 1.3125 / 0.0024035768376456366 / 0.34622894200994053 | [NPY](tensors/0001083.npy) |
| 1084 | `model.layers.0.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.9765625 / 1.3125 / 0.0024035768376456366 / 0.34622894200994053 | [NPY](tensors/0001084.npy) |
| 1085 | `model.layers.0.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1086 | `model.layers.0.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1087 | `model.layers.0.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1088 | `model.layers.0.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -30.125 / 18.375 / -0.008894079485132048 / 0.8268020615486761 | [NPY](tensors/0001088.npy) |
| 1089 | `model.layers.0.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 18.375 / -0.008894079485132048 / 0.8268020615486761 | [NPY](tensors/0001089.npy) |
| 1090 | `model.layers.0.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.828125 / 1.3359375 / -0.14555740356445312 / 0.6571959746750227 | [NPY](tensors/0001090.npy) |
| 1091 | `model.layers.0` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 57.5 / -0.028901057773166233 / 3.3579385867563585 | [NPY](tensors/0001091.npy) |
| 1170 | `model.layers.0` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.625 / 47.5 / 0.005106970005565219 / 2.6215914903750863 | [NPY](tensors/0001170.npy) |
| 1171 | `model.layers.0` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001171.npy) |
| 1172 | `model.layers.0` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.611114501953125 / 0.9771971733502269 | [NPY](tensors/0001172.npy) |
| 1173 | `model.layers.0` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / -0.047824978828430176 / 0.6921356554670257 | [NPY](tensors/0001173.npy) |
| 1174 | `model.layers.0` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 882.0 / 882.0 / 882.0 / 0.0 | [NPY](tensors/0001174.npy) |
| 1175 | `model.layers.0` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1176 | `model.layers.0` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1177 | `model.layers.0` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1178 | `model.layers.0.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.625 / 47.5 / 0.005106970005565219 / 2.6215914903750863 | [NPY](tensors/0001178.npy) |
| 1179 | `model.layers.0.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 14.125 / 0.0005866729550891452 / 0.7554183234523332 | [NPY](tensors/0001179.npy) |
| 1180 | `model.layers.0.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 14.125 / 0.0005866729550891452 / 0.7554183234523332 | [NPY](tensors/0001180.npy) |
| 1181 | `model.layers.0.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001181.npy) |
| 1182 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 882.0 / 882.0 / 882.0 / 0.0 | [NPY](tensors/0001182.npy) |
| 1183 | `model.layers.0.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1184 | `model.layers.0.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1185 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.611114501953125 / 0.9771971733502269 | [NPY](tensors/0001185.npy) |
| 1186 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / -0.047824978828430176 / 0.6921356554670257 | [NPY](tensors/0001186.npy) |
| 1187 | `model.layers.0.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1188 | `model.layers.0.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 14.125 / 0.0005866729550891452 / 0.7554183234523332 | [NPY](tensors/0001188.npy) |
| 1189 | `model.layers.0.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.21875 / 11.25 / 0.010708235728088766 / 1.060515732660661 | [NPY](tensors/0001189.npy) |
| 1190 | `model.layers.0.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 14.125 / 0.0005866729550891452 / 0.7554183234523332 | [NPY](tensors/0001190.npy) |
| 1191 | `model.layers.0.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -58.75 / 50.25 / -0.06230086088180542 / 6.016812680413199 | [NPY](tensors/0001191.npy) |
| 1192 | `model.layers.0.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 14.125 / 0.0005866729550891452 / 0.7554183234523332 | [NPY](tensors/0001192.npy) |
| 1193 | `model.layers.0.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.65625 / 5.46875 / -0.0845739059150219 / 1.4068414576152921 | [NPY](tensors/0001193.npy) |
| 1194 | `model.layers.0.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.09375 / 5.875 / -0.02986099008887777 / 0.6754310270600915 | [NPY](tensors/0001194.npy) |
| 1195 | `model.layers.0.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 45.25 / 0.02392111528250906 / 1.3896896912373462 | [NPY](tensors/0001195.npy) |
| 1196 | `model.layers.0.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 45.25 / 0.02392111528250906 / 1.3896896912373462 | [NPY](tensors/0001196.npy) |
| 1197 | `model.layers.0.self_attn` | 10 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.003286601768919626 / 0.03699024086091826 | [NPY](tensors/0001197.npy) |
| 1198 | `model.layers.0.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 48.0 / 0.02882266574435764 / 3.119593012702438 | [NPY](tensors/0001198.npy) |
| 1199 | `model.layers.0.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.203125 / 2.421875 / 0.007642153236601088 / 0.333739179220242 | [NPY](tensors/0001199.npy) |
| 1200 | `model.layers.0.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.203125 / 2.421875 / 0.007642153236601088 / 0.333739179220242 | [NPY](tensors/0001200.npy) |
| 1201 | `model.layers.0.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.203125 / 2.421875 / 0.007642153236601088 / 0.333739179220242 | [NPY](tensors/0001201.npy) |
| 1202 | `model.layers.0.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1203 | `model.layers.0.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1204 | `model.layers.0.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1205 | `model.layers.0.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.8125 / 17.75 / 0.013007569809754689 / 0.6736122604981664 | [NPY](tensors/0001205.npy) |
| 1206 | `model.layers.0.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.8125 / 17.75 / 0.013007569809754689 / 0.6736122604981664 | [NPY](tensors/0001206.npy) |
| 1207 | `model.layers.0.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.453125 / 1.484375 / -0.1650238037109375 / 0.6347828494082539 | [NPY](tensors/0001207.npy) |
| 1208 | `model.layers.0` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 66.0 / 0.04193482928805881 / 3.3564307737275287 | [NPY](tensors/0001208.npy) |
| 1287 | `model.layers.0` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001287.npy) |
| 1288 | `model.layers.0` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001288.npy) |
| 1289 | `model.layers.0` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.659881591796875 / 0.9579637378310449 | [NPY](tensors/0001289.npy) |
| 1290 | `model.layers.0` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / -0.07649624347686768 / 0.6710666469829912 | [NPY](tensors/0001290.npy) |
| 1291 | `model.layers.0` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 883.0 / 883.0 / 883.0 / 0.0 | [NPY](tensors/0001291.npy) |
| 1292 | `model.layers.0` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1293 | `model.layers.0` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1294 | `model.layers.0` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1295 | `model.layers.0.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001295.npy) |
| 1296 | `model.layers.0.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001296.npy) |
| 1297 | `model.layers.0.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001297.npy) |
| 1298 | `model.layers.0.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001298.npy) |
| 1299 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 883.0 / 883.0 / 883.0 / 0.0 | [NPY](tensors/0001299.npy) |
| 1300 | `model.layers.0.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1301 | `model.layers.0.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1302 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.659881591796875 / 0.9579637378310449 | [NPY](tensors/0001302.npy) |
| 1303 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / -0.07649624347686768 / 0.6710666469829912 | [NPY](tensors/0001303.npy) |
| 1304 | `model.layers.0.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1305 | `model.layers.0.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001305.npy) |
| 1306 | `model.layers.0.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.84375 / 8.5625 / 0.0153301190584898 / 1.0113524420299036 | [NPY](tensors/0001306.npy) |
| 1307 | `model.layers.0.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001307.npy) |
| 1308 | `model.layers.0.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.0 / 65.5 / 0.032654017210006714 / 6.89507515667232 | [NPY](tensors/0001308.npy) |
| 1309 | `model.layers.0.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001309.npy) |
| 1310 | `model.layers.0.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.28125 / 3.390625 / -0.002120666205883026 / 0.8566653376613583 | [NPY](tensors/0001310.npy) |
| 1311 | `model.layers.0.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.75 / 3.65625 / -0.004208057723189995 / 0.48929357258705597 | [NPY](tensors/0001311.npy) |
| 1312 | `model.layers.0.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.5 / 29.25 / 0.02741609232293235 / 0.9656625089990887 | [NPY](tensors/0001312.npy) |
| 1313 | `model.layers.0.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.5 / 29.25 / 0.02741609232293235 / 0.9656625089990887 | [NPY](tensors/0001313.npy) |
| 1314 | `model.layers.0.self_attn` | 11 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0031757094092970395 / 0.030632223152010796 | [NPY](tensors/0001314.npy) |
| 1315 | `model.layers.0.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.375 / 32.5 / 0.025426774554782445 / 3.0343219700298736 | [NPY](tensors/0001315.npy) |
| 1316 | `model.layers.0.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.546875 / 1.4296875 / 0.0017377588484022352 / 0.2870892159118451 | [NPY](tensors/0001316.npy) |
| 1317 | `model.layers.0.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.546875 / 1.4296875 / 0.0017377588484022352 / 0.2870892159118451 | [NPY](tensors/0001317.npy) |
| 1318 | `model.layers.0.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.546875 / 1.4296875 / 0.0017377588484022352 / 0.2870892159118451 | [NPY](tensors/0001318.npy) |
| 1319 | `model.layers.0.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1320 | `model.layers.0.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1321 | `model.layers.0.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1322 | `model.layers.0.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.75 / 13.4375 / 0.021735236959324944 / 0.7100976062474601 | [NPY](tensors/0001322.npy) |
| 1323 | `model.layers.0.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.75 / 13.4375 / 0.021735236959324944 / 0.7100976062474601 | [NPY](tensors/0001323.npy) |
| 1324 | `model.layers.0.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.40625 / 2.78125 / -0.016693115234375 / 1.4816174916297642 | [NPY](tensors/0001324.npy) |
| 1325 | `model.layers.0` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.625 / 46.0 / 0.04708422554863824 / 2.9459582974805443 | [NPY](tensors/0001325.npy) |
| 1404 | `model.layers.0` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 32.75 / 0.03959848284721375 / 2.636727096419094 | [NPY](tensors/0001404.npy) |
| 1405 | `model.layers.0` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001405.npy) |
| 1406 | `model.layers.0` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.734130859375 / 0.896956143048102 | [NPY](tensors/0001406.npy) |
| 1407 | `model.layers.0` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.296875 / -0.06761544942855835 / 0.6796756860615183 | [NPY](tensors/0001407.npy) |
| 1408 | `model.layers.0` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 884.0 / 884.0 / 884.0 / 0.0 | [NPY](tensors/0001408.npy) |
| 1409 | `model.layers.0` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1410 | `model.layers.0` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1411 | `model.layers.0` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1412 | `model.layers.0.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 32.75 / 0.03959848284721375 / 2.636727096419094 | [NPY](tensors/0001412.npy) |
| 1413 | `model.layers.0.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0001413.npy) |
| 1414 | `model.layers.0.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0001414.npy) |
| 1415 | `model.layers.0.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001415.npy) |
| 1416 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 884.0 / 884.0 / 884.0 / 0.0 | [NPY](tensors/0001416.npy) |
| 1417 | `model.layers.0.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1418 | `model.layers.0.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1419 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.734130859375 / 0.896956143048102 | [NPY](tensors/0001419.npy) |
| 1420 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.296875 / -0.06761544942855835 / 0.6796756860615183 | [NPY](tensors/0001420.npy) |
| 1421 | `model.layers.0.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1422 | `model.layers.0.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0001422.npy) |
| 1423 | `model.layers.0.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.0625 / 6.78125 / -0.006842018279712647 / 0.8517376388261615 | [NPY](tensors/0001423.npy) |
| 1424 | `model.layers.0.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0001424.npy) |
| 1425 | `model.layers.0.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.25 / 35.75 / 0.051442623138427734 / 3.999531927842787 | [NPY](tensors/0001425.npy) |
| 1426 | `model.layers.0.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0001426.npy) |
| 1427 | `model.layers.0.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 4.625 / 0.04163137078285217 / 1.1435466539669636 | [NPY](tensors/0001427.npy) |
| 1428 | `model.layers.0.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.0 / 2.578125 / -0.004297302641134593 / 0.40215400695185755 | [NPY](tensors/0001428.npy) |
| 1429 | `model.layers.0.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.5 / 41.25 / 0.03033496853378084 / 1.273097966748824 | [NPY](tensors/0001429.npy) |
| 1430 | `model.layers.0.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.5 / 41.25 / 0.03033496853378084 / 1.273097966748824 | [NPY](tensors/0001430.npy) |
| 1431 | `model.layers.0.self_attn` | 12 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9375 / 0.002998074000864278 / 0.028449779217172618 | [NPY](tensors/0001431.npy) |
| 1432 | `model.layers.0.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 39.75 / 0.07003011306126912 / 2.9344355422319954 | [NPY](tensors/0001432.npy) |
| 1433 | `model.layers.0.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.21875 / 1.640625 / 0.000633558299806383 / 0.37275415579527615 | [NPY](tensors/0001433.npy) |
| 1434 | `model.layers.0.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.21875 / 1.640625 / 0.000633558299806383 / 0.37275415579527615 | [NPY](tensors/0001434.npy) |
| 1435 | `model.layers.0.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.21875 / 1.640625 / 0.000633558299806383 / 0.37275415579527615 | [NPY](tensors/0001435.npy) |
| 1436 | `model.layers.0.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1437 | `model.layers.0.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1438 | `model.layers.0.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1439 | `model.layers.0.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.65625 / 20.125 / 0.040992957353591916 / 0.8176059714887802 | [NPY](tensors/0001439.npy) |
| 1440 | `model.layers.0.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.65625 / 20.125 / 0.040992957353591916 / 0.8176059714887802 | [NPY](tensors/0001440.npy) |
| 1441 | `model.layers.0.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6796875 / 1.453125 / -0.2000274658203125 / 0.7717781990697679 | [NPY](tensors/0001441.npy) |
| 1442 | `model.layers.0` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 57.5 / 0.11109371185302734 / 3.2748667659639095 | [NPY](tensors/0001442.npy) |
| 1521 | `model.layers.0` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 32.5 / 0.02340112761594355 / 2.5180141341639093 | [NPY](tensors/0001521.npy) |
| 1522 | `model.layers.0` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001522.npy) |
| 1523 | `model.layers.0` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.7958755493164062 / 0.858839493189722 | [NPY](tensors/0001523.npy) |
| 1524 | `model.layers.0` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.005351245403289795 / 0.6623439987299442 | [NPY](tensors/0001524.npy) |
| 1525 | `model.layers.0` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 885.0 / 885.0 / 885.0 / 0.0 | [NPY](tensors/0001525.npy) |
| 1526 | `model.layers.0` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1527 | `model.layers.0` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1528 | `model.layers.0` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1529 | `model.layers.0.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 32.5 / 0.02340112761594355 / 2.5180141341639093 | [NPY](tensors/0001529.npy) |
| 1530 | `model.layers.0.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0001530.npy) |
| 1531 | `model.layers.0.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0001531.npy) |
| 1532 | `model.layers.0.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001532.npy) |
| 1533 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 885.0 / 885.0 / 885.0 / 0.0 | [NPY](tensors/0001533.npy) |
| 1534 | `model.layers.0.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1535 | `model.layers.0.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1536 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.7958755493164062 / 0.858839493189722 | [NPY](tensors/0001536.npy) |
| 1537 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.005351245403289795 / 0.6623439987299442 | [NPY](tensors/0001537.npy) |
| 1538 | `model.layers.0.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1539 | `model.layers.0.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0001539.npy) |
| 1540 | `model.layers.0.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.4375 / 5.40625 / -0.007190447126049548 / 0.8410779943508924 | [NPY](tensors/0001540.npy) |
| 1541 | `model.layers.0.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0001541.npy) |
| 1542 | `model.layers.0.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.375 / 29.25 / -0.0019535720348358154 / 3.219451134212101 | [NPY](tensors/0001542.npy) |
| 1543 | `model.layers.0.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0001543.npy) |
| 1544 | `model.layers.0.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.71875 / 3.5625 / -0.03649583458900452 / 1.2017397564519863 | [NPY](tensors/0001544.npy) |
| 1545 | `model.layers.0.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.0625 / 3.890625 / 0.011478353382699424 / 0.5419365220586085 | [NPY](tensors/0001545.npy) |
| 1546 | `model.layers.0.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 44.5 / 0.028298920227421656 / 1.402217248344546 | [NPY](tensors/0001546.npy) |
| 1547 | `model.layers.0.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 44.5 / 0.028298920227421656 / 1.402217248344546 | [NPY](tensors/0001547.npy) |
| 1548 | `model.layers.0.self_attn` | 13 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0036922183651381343 / 0.03518312473942115 | [NPY](tensors/0001548.npy) |
| 1549 | `model.layers.0.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.25 / 46.5 / 0.05173416667514377 / 2.953922007956645 | [NPY](tensors/0001549.npy) |
| 1550 | `model.layers.0.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.140625 / 1.640625 / -0.00423579282230801 / 0.3779409916476406 | [NPY](tensors/0001550.npy) |
| 1551 | `model.layers.0.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.140625 / 1.640625 / -0.00423579282230801 / 0.3779409916476406 | [NPY](tensors/0001551.npy) |
| 1552 | `model.layers.0.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.140625 / 1.640625 / -0.00423579282230801 / 0.3779409916476406 | [NPY](tensors/0001552.npy) |
| 1553 | `model.layers.0.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1554 | `model.layers.0.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1555 | `model.layers.0.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1556 | `model.layers.0.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.765625 / 11.625 / 0.02430660244491365 / 0.483295827752863 | [NPY](tensors/0001556.npy) |
| 1557 | `model.layers.0.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.765625 / 11.625 / 0.02430660244491365 / 0.483295827752863 | [NPY](tensors/0001557.npy) |
| 1558 | `model.layers.0.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6640625 / 1.1171875 / -0.17649078369140625 / 0.6741055770412708 | [NPY](tensors/0001558.npy) |
| 1559 | `model.layers.0` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.25 / 47.5 / 0.07611812088224623 / 3.0716596625601498 | [NPY](tensors/0001559.npy) |
| 1638 | `model.layers.0` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.25 / 32.0 / 0.061791101429197526 / 2.238756913453412 | [NPY](tensors/0001638.npy) |
| 1639 | `model.layers.0` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001639.npy) |
| 1640 | `model.layers.0` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.805328369140625 / 0.858282942374398 | [NPY](tensors/0001640.npy) |
| 1641 | `model.layers.0` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.2890625 / 0.08753019571304321 / 0.6450265564714699 | [NPY](tensors/0001641.npy) |
| 1642 | `model.layers.0` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 886.0 / 886.0 / 886.0 / 0.0 | [NPY](tensors/0001642.npy) |
| 1643 | `model.layers.0` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1644 | `model.layers.0` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1645 | `model.layers.0` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1646 | `model.layers.0.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.25 / 32.0 / 0.061791101429197526 / 2.238756913453412 | [NPY](tensors/0001646.npy) |
| 1647 | `model.layers.0.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0001647.npy) |
| 1648 | `model.layers.0.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0001648.npy) |
| 1649 | `model.layers.0.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001649.npy) |
| 1650 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 886.0 / 886.0 / 886.0 / 0.0 | [NPY](tensors/0001650.npy) |
| 1651 | `model.layers.0.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1652 | `model.layers.0.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1653 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.805328369140625 / 0.858282942374398 | [NPY](tensors/0001653.npy) |
| 1654 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.2890625 / 0.08753019571304321 / 0.6450265564714699 | [NPY](tensors/0001654.npy) |
| 1655 | `model.layers.0.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1656 | `model.layers.0.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0001656.npy) |
| 1657 | `model.layers.0.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.375 / 8.125 / 0.007972375839017332 / 1.0483744761991842 | [NPY](tensors/0001657.npy) |
| 1658 | `model.layers.0.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0001658.npy) |
| 1659 | `model.layers.0.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.0 / 52.0 / -0.06352853029966354 / 5.834851084637073 | [NPY](tensors/0001659.npy) |
| 1660 | `model.layers.0.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0001660.npy) |
| 1661 | `model.layers.0.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.75 / 4.5 / 0.031710169510915875 / 1.4942407070139319 | [NPY](tensors/0001661.npy) |
| 1662 | `model.layers.0.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.6875 / 3.546875 / -0.016928321158047765 / 0.7392116150671464 | [NPY](tensors/0001662.npy) |
| 1663 | `model.layers.0.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.625 / 41.0 / 0.014375044571028815 / 1.3479347222298588 | [NPY](tensors/0001663.npy) |
| 1664 | `model.layers.0.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.625 / 41.0 / 0.014375044571028815 / 1.3479347222298588 | [NPY](tensors/0001664.npy) |
| 1665 | `model.layers.0.self_attn` | 14 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.00450653489725197 / 0.04704422265346385 | [NPY](tensors/0001665.npy) |
| 1666 | `model.layers.0.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.5 / 40.5 / 0.07628997696770562 / 2.6471704261275355 | [NPY](tensors/0001666.npy) |
| 1667 | `model.layers.0.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.375 / 1.7421875 / 0.007262592845492893 / 0.44963418478508627 | [NPY](tensors/0001667.npy) |
| 1668 | `model.layers.0.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.375 / 1.7421875 / 0.007262592845492893 / 0.44963418478508627 | [NPY](tensors/0001668.npy) |
| 1669 | `model.layers.0.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.375 / 1.7421875 / 0.007262592845492893 / 0.44963418478508627 | [NPY](tensors/0001669.npy) |
| 1670 | `model.layers.0.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1671 | `model.layers.0.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1672 | `model.layers.0.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1673 | `model.layers.0.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.9375 / 33.0 / 0.01927970958252748 / 1.1171433264728967 | [NPY](tensors/0001673.npy) |
| 1674 | `model.layers.0.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 33.0 / 0.01927970958252748 / 1.1171433264728967 | [NPY](tensors/0001674.npy) |
| 1675 | `model.layers.0.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.171875 / 1.8515625 / -0.17304611206054688 / 0.8014427975570002 | [NPY](tensors/0001675.npy) |
| 1676 | `model.layers.0` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.875 / 73.5 / 0.09563159942626953 / 3.23747161359952 | [NPY](tensors/0001676.npy) |
| 1755 | `model.layers.0` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0001755.npy) |
| 1756 | `model.layers.0` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001756.npy) |
| 1757 | `model.layers.0` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.752716064453125 / 0.8717363915407874 | [NPY](tensors/0001757.npy) |
| 1758 | `model.layers.0` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / 0.1641445755958557 / 0.6760071928531548 | [NPY](tensors/0001758.npy) |
| 1759 | `model.layers.0` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 887.0 / 887.0 / 887.0 / 0.0 | [NPY](tensors/0001759.npy) |
| 1760 | `model.layers.0` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1761 | `model.layers.0` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1762 | `model.layers.0` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1763 | `model.layers.0.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0001763.npy) |
| 1764 | `model.layers.0.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0001764.npy) |
| 1765 | `model.layers.0.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0001765.npy) |
| 1766 | `model.layers.0.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001766.npy) |
| 1767 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 887.0 / 887.0 / 887.0 / 0.0 | [NPY](tensors/0001767.npy) |
| 1768 | `model.layers.0.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1769 | `model.layers.0.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1770 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.752716064453125 / 0.8717363915407874 | [NPY](tensors/0001770.npy) |
| 1771 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / 0.1641445755958557 / 0.6760071928531548 | [NPY](tensors/0001771.npy) |
| 1772 | `model.layers.0.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1773 | `model.layers.0.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0001773.npy) |
| 1774 | `model.layers.0.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.34375 / 8.125 / 0.009809806477278471 / 1.0602451281469458 | [NPY](tensors/0001774.npy) |
| 1775 | `model.layers.0.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0001775.npy) |
| 1776 | `model.layers.0.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.5 / 52.75 / 0.05987404379993677 / 5.486411371880323 | [NPY](tensors/0001776.npy) |
| 1777 | `model.layers.0.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0001777.npy) |
| 1778 | `model.layers.0.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.125 / 3.75 / 0.02330493927001953 / 1.1486258589347933 | [NPY](tensors/0001778.npy) |
| 1779 | `model.layers.0.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.03125 / 3.9375 / -0.003735901671461761 / 0.7334671185855856 | [NPY](tensors/0001779.npy) |
| 1780 | `model.layers.0.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.75 / 42.25 / 0.035103348228666516 / 1.2956677711565707 | [NPY](tensors/0001780.npy) |
| 1781 | `model.layers.0.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.75 / 42.25 / 0.035103348228666516 / 1.2956677711565707 | [NPY](tensors/0001781.npy) |
| 1782 | `model.layers.0.self_attn` | 15 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.004689409006589488 / 0.04534349276831848 | [NPY](tensors/0001782.npy) |
| 1783 | `model.layers.0.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 46.75 / -0.028856865564982095 / 2.8114859058542354 | [NPY](tensors/0001783.npy) |
| 1784 | `model.layers.0.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.046875 / 1.59375 / 0.00367560519112481 / 0.4049019838973261 | [NPY](tensors/0001784.npy) |
| 1785 | `model.layers.0.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.046875 / 1.59375 / 0.00367560519112481 / 0.4049019838973261 | [NPY](tensors/0001785.npy) |
| 1786 | `model.layers.0.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.046875 / 1.59375 / 0.00367560519112481 / 0.4049019838973261 | [NPY](tensors/0001786.npy) |
| 1787 | `model.layers.0.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1788 | `model.layers.0.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1789 | `model.layers.0.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1790 | `model.layers.0.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.9375 / 24.125 / 0.01771838665008545 / 0.7490796885351366 | [NPY](tensors/0001790.npy) |
| 1791 | `model.layers.0.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.9375 / 24.125 / 0.01771838665008545 / 0.7490796885351366 | [NPY](tensors/0001791.npy) |
| 1792 | `model.layers.0.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8671875 / 2.015625 / -0.0466156005859375 / 0.8264496066762195 | [NPY](tensors/0001792.npy) |
| 1793 | `model.layers.0` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 71.0 / -0.011050261391533745 / 3.157948482063685 | [NPY](tensors/0001793.npy) |
| 1872 | `model.layers.0` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 31.5 / -0.13233292235268487 / 2.5137617368694567 | [NPY](tensors/0001872.npy) |
| 1873 | `model.layers.0` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001873.npy) |
| 1874 | `model.layers.0` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6714019775390625 / 0.9432200886540145 | [NPY](tensors/0001874.npy) |
| 1875 | `model.layers.0` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.18380916118621826 / 0.659819262490622 | [NPY](tensors/0001875.npy) |
| 1876 | `model.layers.0` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 888.0 / 888.0 / 888.0 / 0.0 | [NPY](tensors/0001876.npy) |
| 1877 | `model.layers.0` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1878 | `model.layers.0` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1879 | `model.layers.0` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1880 | `model.layers.0.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 31.5 / -0.13233292235268487 / 2.5137617368694567 | [NPY](tensors/0001880.npy) |
| 1881 | `model.layers.0.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.75 / 8.6875 / -0.036875887504882285 / 0.7783508003627001 | [NPY](tensors/0001881.npy) |
| 1882 | `model.layers.0.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.75 / 8.6875 / -0.036875887504882285 / 0.7783508003627001 | [NPY](tensors/0001882.npy) |
| 1883 | `model.layers.0.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001883.npy) |
| 1884 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 888.0 / 888.0 / 888.0 / 0.0 | [NPY](tensors/0001884.npy) |
| 1885 | `model.layers.0.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1886 | `model.layers.0.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1887 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6714019775390625 / 0.9432200886540145 | [NPY](tensors/0001887.npy) |
| 1888 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.18380916118621826 / 0.659819262490622 | [NPY](tensors/0001888.npy) |
| 1889 | `model.layers.0.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1890 | `model.layers.0.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.75 / 8.6875 / -0.036875887504882285 / 0.7783508003627001 | [NPY](tensors/0001890.npy) |
| 1891 | `model.layers.0.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 9.8125 / -0.004403205588459969 / 1.0735847228482056 | [NPY](tensors/0001891.npy) |
| 1892 | `model.layers.0.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.75 / 8.6875 / -0.036875887504882285 / 0.7783508003627001 | [NPY](tensors/0001892.npy) |
| 1893 | `model.layers.0.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.75 / 51.25 / -0.042498648166656494 / 5.714046666721153 | [NPY](tensors/0001893.npy) |
| 1894 | `model.layers.0.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.75 / 8.6875 / -0.036875887504882285 / 0.7783508003627001 | [NPY](tensors/0001894.npy) |
| 1895 | `model.layers.0.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.46875 / 4.5625 / 0.019675567746162415 / 1.460954858233445 | [NPY](tensors/0001895.npy) |
| 1896 | `model.layers.0.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.0 / 3.28125 / -0.013248017437945236 / 0.5051127606505694 | [NPY](tensors/0001896.npy) |
| 1897 | `model.layers.0.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.375 / 44.25 / 0.02972020846274164 / 1.3196737631893285 | [NPY](tensors/0001897.npy) |
| 1898 | `model.layers.0.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.375 / 44.25 / 0.02972020846274164 / 1.3196737631893285 | [NPY](tensors/0001898.npy) |
| 1899 | `model.layers.0.self_attn` | 16 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.002793451895630063 / 0.034001526281407506 | [NPY](tensors/0001899.npy) |
| 1900 | `model.layers.0.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 44.0 / -0.10246693293253581 / 2.856635273587177 | [NPY](tensors/0001900.npy) |
| 1901 | `model.layers.0.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.171875 / 1.7421875 / 0.0022669156392415364 / 0.3641346213362451 | [NPY](tensors/0001901.npy) |
| 1902 | `model.layers.0.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.171875 / 1.7421875 / 0.0022669156392415364 / 0.3641346213362451 | [NPY](tensors/0001902.npy) |
| 1903 | `model.layers.0.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.171875 / 1.7421875 / 0.0022669156392415364 / 0.3641346213362451 | [NPY](tensors/0001903.npy) |
| 1904 | `model.layers.0.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1905 | `model.layers.0.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1906 | `model.layers.0.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1907 | `model.layers.0.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.8125 / 21.375 / 0.010834580659866333 / 0.630774466832456 | [NPY](tensors/0001907.npy) |
| 1908 | `model.layers.0.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.8125 / 21.375 / 0.010834580659866333 / 0.630774466832456 | [NPY](tensors/0001908.npy) |
| 1909 | `model.layers.0.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9140625 / 2.140625 / -0.13686847686767578 / 0.7778013471374806 | [NPY](tensors/0001909.npy) |
| 1910 | `model.layers.0` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 61.5 / -0.09157041841083102 / 3.200379775185868 | [NPY](tensors/0001910.npy) |
| 1989 | `model.layers.0` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0001989.npy) |
| 1990 | `model.layers.0` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001990.npy) |
| 1991 | `model.layers.0` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.61199951171875 / 1.0116022827243683 | [NPY](tensors/0001991.npy) |
| 1992 | `model.layers.0` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14778363704681396 / 0.6247390563478729 | [NPY](tensors/0001992.npy) |
| 1993 | `model.layers.0` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 889.0 / 889.0 / 889.0 / 0.0 | [NPY](tensors/0001993.npy) |
| 1994 | `model.layers.0` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1995 | `model.layers.0` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1996 | `model.layers.0` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1997 | `model.layers.0.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0001997.npy) |
| 1998 | `model.layers.0.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0001998.npy) |
| 1999 | `model.layers.0.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0001999.npy) |
| 2000 | `model.layers.0.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002000.npy) |
| 2001 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 889.0 / 889.0 / 889.0 / 0.0 | [NPY](tensors/0002001.npy) |
| 2002 | `model.layers.0.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2003 | `model.layers.0.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2004 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.61199951171875 / 1.0116022827243683 | [NPY](tensors/0002004.npy) |
| 2005 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14778363704681396 / 0.6247390563478729 | [NPY](tensors/0002005.npy) |
| 2006 | `model.layers.0.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2007 | `model.layers.0.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0002007.npy) |
| 2008 | `model.layers.0.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 7.625 / 0.011268170550465584 / 0.9167789321734896 | [NPY](tensors/0002008.npy) |
| 2009 | `model.layers.0.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0002009.npy) |
| 2010 | `model.layers.0.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 43.75 / 0.046514674089848995 / 4.791095594233786 | [NPY](tensors/0002010.npy) |
| 2011 | `model.layers.0.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0002011.npy) |
| 2012 | `model.layers.0.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.84375 / 4.125 / -0.01808762550354004 / 1.3178383551916408 | [NPY](tensors/0002012.npy) |
| 2013 | `model.layers.0.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.03125 / 4.1875 / -0.0008142775186570361 / 0.659770640034918 | [NPY](tensors/0002013.npy) |
| 2014 | `model.layers.0.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.5625 / 34.5 / 0.012369242476092444 / 1.0269074853160758 | [NPY](tensors/0002014.npy) |
| 2015 | `model.layers.0.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.5625 / 34.5 / 0.012369242476092444 / 1.0269074853160758 | [NPY](tensors/0002015.npy) |
| 2016 | `model.layers.0.self_attn` | 17 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.95703125 / 0.0036571065950158294 / 0.03267445708816064 | [NPY](tensors/0002016.npy) |
| 2017 | `model.layers.0.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.75 / 35.5 / 0.0015748076968722874 / 2.7996223796675945 | [NPY](tensors/0002017.npy) |
| 2018 | `model.layers.0.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.21875 / 1.8828125 / 0.00042816102504730227 / 0.4072358016661628 | [NPY](tensors/0002018.npy) |
| 2019 | `model.layers.0.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.21875 / 1.8828125 / 0.00042816102504730227 / 0.4072358016661628 | [NPY](tensors/0002019.npy) |
| 2020 | `model.layers.0.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.21875 / 1.8828125 / 0.00042816102504730227 / 0.4072358016661628 | [NPY](tensors/0002020.npy) |
| 2021 | `model.layers.0.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2022 | `model.layers.0.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2023 | `model.layers.0.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2024 | `model.layers.0.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -21.875 / 19.5 / 0.023193068781660664 / 0.8849675067563388 | [NPY](tensors/0002024.npy) |
| 2025 | `model.layers.0.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 19.5 / 0.023193068781660664 / 0.8849675067563388 | [NPY](tensors/0002025.npy) |
| 2026 | `model.layers.0.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.1875 / 2.140625 / -0.0500335693359375 / 0.7167674896326144 | [NPY](tensors/0002026.npy) |
| 2027 | `model.layers.0` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 55.0 / 0.024803124533759224 / 3.164395003929952 | [NPY](tensors/0002027.npy) |
| 2106 | `model.layers.0` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.0 / 65.0 / -0.04449875156084696 / 4.688755940234463 | [NPY](tensors/0002106.npy) |
| 2107 | `model.layers.0` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002107.npy) |
| 2108 | `model.layers.0` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6052932739257812 / 0.9920321858005083 | [NPY](tensors/0002108.npy) |
| 2109 | `model.layers.0` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.0962597131729126 / 0.670037121922543 | [NPY](tensors/0002109.npy) |
| 2110 | `model.layers.0` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 890.0 / 890.0 / 890.0 / 0.0 | [NPY](tensors/0002110.npy) |
| 2111 | `model.layers.0` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2112 | `model.layers.0` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2113 | `model.layers.0` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2114 | `model.layers.0.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.0 / 65.0 / -0.04449875156084696 / 4.688755940234463 | [NPY](tensors/0002114.npy) |
| 2115 | `model.layers.0.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.1875 / 9.0625 / -0.006527311272091336 / 0.7175813521305182 | [NPY](tensors/0002115.npy) |
| 2116 | `model.layers.0.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.1875 / 9.0625 / -0.006527311272091336 / 0.7175813521305182 | [NPY](tensors/0002116.npy) |
| 2117 | `model.layers.0.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002117.npy) |
| 2118 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 890.0 / 890.0 / 890.0 / 0.0 | [NPY](tensors/0002118.npy) |
| 2119 | `model.layers.0.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2120 | `model.layers.0.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2121 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6052932739257812 / 0.9920321858005083 | [NPY](tensors/0002121.npy) |
| 2122 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.0962597131729126 / 0.670037121922543 | [NPY](tensors/0002122.npy) |
| 2123 | `model.layers.0.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2124 | `model.layers.0.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.1875 / 9.0625 / -0.006527311272091336 / 0.7175813521305182 | [NPY](tensors/0002124.npy) |
| 2125 | `model.layers.0.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.34375 / 7.9375 / 0.007687008008360863 / 0.9037118963900772 | [NPY](tensors/0002125.npy) |
| 2126 | `model.layers.0.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.1875 / 9.0625 / -0.006527311272091336 / 0.7175813521305182 | [NPY](tensors/0002126.npy) |
| 2127 | `model.layers.0.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.5 / 48.5 / -0.07982254028320312 / 5.567176472387403 | [NPY](tensors/0002127.npy) |
| 2128 | `model.layers.0.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.1875 / 9.0625 / -0.006527311272091336 / 0.7175813521305182 | [NPY](tensors/0002128.npy) |
| 2129 | `model.layers.0.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.359375 / 3.359375 / -0.040451206266880035 / 0.8356518609055628 | [NPY](tensors/0002129.npy) |
| 2130 | `model.layers.0.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5 / 3.3125 / -0.0011989486229140311 / 0.7570053634322625 | [NPY](tensors/0002130.npy) |
| 2131 | `model.layers.0.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.6875 / 29.625 / 0.043646016799741325 / 1.10989090050186 | [NPY](tensors/0002131.npy) |
| 2132 | `model.layers.0.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.6875 / 29.625 / 0.043646016799741325 / 1.10989090050186 | [NPY](tensors/0002132.npy) |
| 2133 | `model.layers.0.self_attn` | 18 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.005037459517610945 / 0.04651120551172964 | [NPY](tensors/0002133.npy) |
| 2134 | `model.layers.0.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 62.0 / -0.0009913259082370335 / 4.43778864524541 | [NPY](tensors/0002134.npy) |
| 2135 | `model.layers.0.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.0 / 0.003067044417063395 / 0.280150226232165 | [NPY](tensors/0002135.npy) |
| 2136 | `model.layers.0.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.0 / 0.003067044417063395 / 0.280150226232165 | [NPY](tensors/0002136.npy) |
| 2137 | `model.layers.0.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.0 / 0.003067044417063395 / 0.280150226232165 | [NPY](tensors/0002137.npy) |
| 2138 | `model.layers.0.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2139 | `model.layers.0.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2140 | `model.layers.0.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2141 | `model.layers.0.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -25.375 / 22.5 / 0.047755982933772936 / 1.3980470349220429 | [NPY](tensors/0002141.npy) |
| 2142 | `model.layers.0.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.375 / 22.5 / 0.047755982933772936 / 1.3980470349220429 | [NPY](tensors/0002142.npy) |
| 2143 | `model.layers.0.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.640625 / 2.828125 / -0.01210784912109375 / 1.1081123215673236 | [NPY](tensors/0002143.npy) |
| 2144 | `model.layers.0` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -66.0 / 54.25 / 0.04684571160210504 / 3.76131039547647 | [NPY](tensors/0002144.npy) |
| 2223 | `model.layers.0` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.75 / 32.5 / -0.03096004476149877 / 2.338928604184066 | [NPY](tensors/0002223.npy) |
| 2224 | `model.layers.0` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002224.npy) |
| 2225 | `model.layers.0` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6360321044921875 / 0.965021007945482 | [NPY](tensors/0002225.npy) |
| 2226 | `model.layers.0` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.07508242130279541 / 0.6832161663666542 | [NPY](tensors/0002226.npy) |
| 2227 | `model.layers.0` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 891.0 / 891.0 / 891.0 / 0.0 | [NPY](tensors/0002227.npy) |
| 2228 | `model.layers.0` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2229 | `model.layers.0` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2230 | `model.layers.0` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2231 | `model.layers.0.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.75 / 32.5 / -0.03096004476149877 / 2.338928604184066 | [NPY](tensors/0002231.npy) |
| 2232 | `model.layers.0.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.4375 / 8.5625 / -0.005111249950197008 / 0.7311115081860402 | [NPY](tensors/0002232.npy) |
| 2233 | `model.layers.0.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.4375 / 8.5625 / -0.005111249950197008 / 0.7311115081860402 | [NPY](tensors/0002233.npy) |
| 2234 | `model.layers.0.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002234.npy) |
| 2235 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 891.0 / 891.0 / 891.0 / 0.0 | [NPY](tensors/0002235.npy) |
| 2236 | `model.layers.0.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2237 | `model.layers.0.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2238 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6360321044921875 / 0.965021007945482 | [NPY](tensors/0002238.npy) |
| 2239 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.07508242130279541 / 0.6832161663666542 | [NPY](tensors/0002239.npy) |
| 2240 | `model.layers.0.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2241 | `model.layers.0.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.4375 / 8.5625 / -0.005111249950197008 / 0.7311115081860402 | [NPY](tensors/0002241.npy) |
| 2242 | `model.layers.0.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.625 / 10.6875 / 0.0013446081429719925 / 1.1380012152202463 | [NPY](tensors/0002242.npy) |
| 2243 | `model.layers.0.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.4375 / 8.5625 / -0.005111249950197008 / 0.7311115081860402 | [NPY](tensors/0002243.npy) |
| 2244 | `model.layers.0.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.0 / 59.0 / 0.20760822296142578 / 6.020610095582916 | [NPY](tensors/0002244.npy) |
| 2245 | `model.layers.0.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.4375 / 8.5625 / -0.005111249950197008 / 0.7311115081860402 | [NPY](tensors/0002245.npy) |
| 2246 | `model.layers.0.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.0625 / 6.59375 / -0.050874412059783936 / 1.4746310037536234 | [NPY](tensors/0002246.npy) |
| 2247 | `model.layers.0.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.5 / 5.40625 / -0.01878645209581009 / 0.48093483895853284 | [NPY](tensors/0002247.npy) |
| 2248 | `model.layers.0.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.25 / 37.5 / 0.029998837576972113 / 1.160877139381313 | [NPY](tensors/0002248.npy) |
| 2249 | `model.layers.0.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.25 / 37.5 / 0.029998837576972113 / 1.160877139381313 | [NPY](tensors/0002249.npy) |
| 2250 | `model.layers.0.self_attn` | 19 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0028846663588052 / 0.03541504661757216 | [NPY](tensors/0002250.npy) |
| 2251 | `model.layers.0.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 37.0 / -0.0008933597140842014 / 2.666635307976409 | [NPY](tensors/0002251.npy) |
| 2252 | `model.layers.0.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5 / 1.375 / 0.009489577346377903 / 0.37893138525044706 | [NPY](tensors/0002252.npy) |
| 2253 | `model.layers.0.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5 / 1.375 / 0.009489577346377903 / 0.37893138525044706 | [NPY](tensors/0002253.npy) |
| 2254 | `model.layers.0.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.5 / 1.375 / 0.009489577346377903 / 0.37893138525044706 | [NPY](tensors/0002254.npy) |
| 2255 | `model.layers.0.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2256 | `model.layers.0.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2257 | `model.layers.0.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2258 | `model.layers.0.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.53125 / 19.5 / 0.012865162392457326 / 0.7150861269568728 | [NPY](tensors/0002258.npy) |
| 2259 | `model.layers.0.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.53125 / 19.5 / 0.012865162392457326 / 0.7150861269568728 | [NPY](tensors/0002259.npy) |
| 2260 | `model.layers.0.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.390625 / 1.7265625 / -0.17919540405273438 / 0.6853948357192338 | [NPY](tensors/0002260.npy) |
| 2261 | `model.layers.0` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 56.0 / 0.011921792560153537 / 2.8995170602729883 | [NPY](tensors/0002261.npy) |
| 2340 | `model.layers.0` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 40.25 / -0.0720830635064178 / 2.807944408004145 | [NPY](tensors/0002340.npy) |
| 2341 | `model.layers.0` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002341.npy) |
| 2342 | `model.layers.0` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.66259765625 / 0.9932594816118745 | [NPY](tensors/0002342.npy) |
| 2343 | `model.layers.0` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.09707069396972656 / 0.6118488978099847 | [NPY](tensors/0002343.npy) |
| 2344 | `model.layers.0` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 892.0 / 892.0 / 892.0 / 0.0 | [NPY](tensors/0002344.npy) |
| 2345 | `model.layers.0` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2346 | `model.layers.0` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2347 | `model.layers.0` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2348 | `model.layers.0.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 40.25 / -0.0720830635064178 / 2.807944408004145 | [NPY](tensors/0002348.npy) |
| 2349 | `model.layers.0.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 10.6875 / -0.02149651630057229 / 0.7312095148244325 | [NPY](tensors/0002349.npy) |
| 2350 | `model.layers.0.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 10.6875 / -0.02149651630057229 / 0.7312095148244325 | [NPY](tensors/0002350.npy) |
| 2351 | `model.layers.0.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002351.npy) |
| 2352 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 892.0 / 892.0 / 892.0 / 0.0 | [NPY](tensors/0002352.npy) |
| 2353 | `model.layers.0.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2354 | `model.layers.0.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2355 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.66259765625 / 0.9932594816118745 | [NPY](tensors/0002355.npy) |
| 2356 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.09707069396972656 / 0.6118488978099847 | [NPY](tensors/0002356.npy) |
| 2357 | `model.layers.0.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2358 | `model.layers.0.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 10.6875 / -0.02149651630057229 / 0.7312095148244325 | [NPY](tensors/0002358.npy) |
| 2359 | `model.layers.0.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.53125 / 8.25 / -0.0001119786174967885 / 1.001871981892237 | [NPY](tensors/0002359.npy) |
| 2360 | `model.layers.0.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 10.6875 / -0.02149651630057229 / 0.7312095148244325 | [NPY](tensors/0002360.npy) |
| 2361 | `model.layers.0.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -63.5 / 61.25 / 0.05675972253084183 / 6.787186147577963 | [NPY](tensors/0002361.npy) |
| 2362 | `model.layers.0.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 10.6875 / -0.02149651630057229 / 0.7312095148244325 | [NPY](tensors/0002362.npy) |
| 2363 | `model.layers.0.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -2.625 / 3.875 / -0.005966342985630035 / 0.8080072099289167 | [NPY](tensors/0002363.npy) |
| 2364 | `model.layers.0.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.65625 / 2.828125 / -0.009241587249562144 / 0.5881177833411879 | [NPY](tensors/0002364.npy) |
| 2365 | `model.layers.0.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.625 / 31.375 / 0.032099822657700214 / 1.0356462885919868 | [NPY](tensors/0002365.npy) |
| 2366 | `model.layers.0.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.625 / 31.375 / 0.032099822657700214 / 1.0356462885919868 | [NPY](tensors/0002366.npy) |
| 2367 | `model.layers.0.self_attn` | 20 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.004018130985212082 / 0.03932598182695022 | [NPY](tensors/0002367.npy) |
| 2368 | `model.layers.0.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 39.25 / -0.04010509914822048 / 2.7829781968446645 | [NPY](tensors/0002368.npy) |
| 2369 | `model.layers.0.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6328125 / 1.5390625 / -0.00020480487081739638 / 0.3225121639622776 | [NPY](tensors/0002369.npy) |
| 2370 | `model.layers.0.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6328125 / 1.5390625 / -0.00020480487081739638 / 0.3225121639622776 | [NPY](tensors/0002370.npy) |
| 2371 | `model.layers.0.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.6328125 / 1.5390625 / -0.00020480487081739638 / 0.3225121639622776 | [NPY](tensors/0002371.npy) |
| 2372 | `model.layers.0.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2373 | `model.layers.0.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2374 | `model.layers.0.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2375 | `model.layers.0.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -14.6875 / 39.25 / 0.05710217071076234 / 1.401053760569549 | [NPY](tensors/0002375.npy) |
| 2376 | `model.layers.0.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.6875 / 39.25 / 0.05710217071076234 / 1.401053760569549 | [NPY](tensors/0002376.npy) |
| 2377 | `model.layers.0.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.125 / 2.3125 / -0.02675628662109375 / 1.4940807353706103 | [NPY](tensors/0002377.npy) |
| 2378 | `model.layers.0` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.5 / 73.0 / 0.016991768942938912 / 3.2190730927159374 | [NPY](tensors/0002378.npy) |
| 2457 | `model.layers.0` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 72.0 / -0.050589884403679106 / 4.345168052644205 | [NPY](tensors/0002457.npy) |
| 2458 | `model.layers.0` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002458.npy) |
| 2459 | `model.layers.0` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6520881652832031 / 1.010377882001008 | [NPY](tensors/0002459.npy) |
| 2460 | `model.layers.0` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.328125 / 0.13654857873916626 / 0.5864893104951562 | [NPY](tensors/0002460.npy) |
| 2461 | `model.layers.0` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 893.0 / 893.0 / 893.0 / 0.0 | [NPY](tensors/0002461.npy) |
| 2462 | `model.layers.0` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2463 | `model.layers.0` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2464 | `model.layers.0` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2465 | `model.layers.0.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 72.0 / -0.050589884403679106 / 4.345168052644205 | [NPY](tensors/0002465.npy) |
| 2466 | `model.layers.0.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.875 / 8.4375 / -0.010570532476736439 / 0.6798166368247869 | [NPY](tensors/0002466.npy) |
| 2467 | `model.layers.0.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.875 / 8.4375 / -0.010570532476736439 / 0.6798166368247869 | [NPY](tensors/0002467.npy) |
| 2468 | `model.layers.0.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002468.npy) |
| 2469 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 893.0 / 893.0 / 893.0 / 0.0 | [NPY](tensors/0002469.npy) |
| 2470 | `model.layers.0.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2471 | `model.layers.0.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2472 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6520881652832031 / 1.010377882001008 | [NPY](tensors/0002472.npy) |
| 2473 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.328125 / 0.13654857873916626 / 0.5864893104951562 | [NPY](tensors/0002473.npy) |
| 2474 | `model.layers.0.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2475 | `model.layers.0.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.875 / 8.4375 / -0.010570532476736439 / 0.6798166368247869 | [NPY](tensors/0002475.npy) |
| 2476 | `model.layers.0.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.03125 / 7.59375 / 0.020286140614189208 / 0.9096967169339552 | [NPY](tensors/0002476.npy) |
| 2477 | `model.layers.0.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.875 / 8.4375 / -0.010570532476736439 / 0.6798166368247869 | [NPY](tensors/0002477.npy) |
| 2478 | `model.layers.0.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -46.5 / 52.5 / 0.05589032173156738 / 5.7564007012879195 | [NPY](tensors/0002478.npy) |
| 2479 | `model.layers.0.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.875 / 8.4375 / -0.010570532476736439 / 0.6798166368247869 | [NPY](tensors/0002479.npy) |
| 2480 | `model.layers.0.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.921875 / 3.546875 / -0.037179671227931976 / 0.9386212138751641 | [NPY](tensors/0002480.npy) |
| 2481 | `model.layers.0.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.5625 / 2.546875 / -0.010938421390164876 / 0.5091410955800377 | [NPY](tensors/0002481.npy) |
| 2482 | `model.layers.0.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.25 / 27.375 / 0.03854243531823158 / 1.1015493320243088 | [NPY](tensors/0002482.npy) |
| 2483 | `model.layers.0.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.25 / 27.375 / 0.03854243531823158 / 1.1015493320243088 | [NPY](tensors/0002483.npy) |
| 2484 | `model.layers.0.self_attn` | 21 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003936668097563405 / 0.04442256067502888 | [NPY](tensors/0002484.npy) |
| 2485 | `model.layers.0.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 64.0 / -0.012068794833289253 / 3.873011299957379 | [NPY](tensors/0002485.npy) |
| 2486 | `model.layers.0.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.140625 / 1.984375 / 0.006917242209116618 / 0.2571311776997332 | [NPY](tensors/0002486.npy) |
| 2487 | `model.layers.0.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.140625 / 1.984375 / 0.006917242209116618 / 0.2571311776997332 | [NPY](tensors/0002487.npy) |
| 2488 | `model.layers.0.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.140625 / 1.984375 / 0.006917242209116618 / 0.2571311776997332 | [NPY](tensors/0002488.npy) |
| 2489 | `model.layers.0.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2490 | `model.layers.0.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2491 | `model.layers.0.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2492 | `model.layers.0.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -16.5 / 45.25 / 0.053408367600705886 / 1.449290081870587 | [NPY](tensors/0002492.npy) |
| 2493 | `model.layers.0.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.5 / 45.25 / 0.053408367600705886 / 1.449290081870587 | [NPY](tensors/0002493.npy) |
| 2494 | `model.layers.0.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.40625 / 2.09375 / -0.021129608154296875 / 0.9307056856801497 | [NPY](tensors/0002494.npy) |
| 2495 | `model.layers.0` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.0 / 60.5 / 0.04144466188218859 / 3.7238716755338768 | [NPY](tensors/0002495.npy) |
| 2574 | `model.layers.0` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 37.0 / 0.01003110408782959 / 2.8182615668403335 | [NPY](tensors/0002574.npy) |
| 2575 | `model.layers.0` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002575.npy) |
| 2576 | `model.layers.0` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6077041625976562 / 1.0143983018780602 | [NPY](tensors/0002576.npy) |
| 2577 | `model.layers.0` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.15405970811843872 / 0.6224309502943564 | [NPY](tensors/0002577.npy) |
| 2578 | `model.layers.0` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 894.0 / 894.0 / 894.0 / 0.0 | [NPY](tensors/0002578.npy) |
| 2579 | `model.layers.0` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2580 | `model.layers.0` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2581 | `model.layers.0` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2582 | `model.layers.0.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 37.0 / 0.01003110408782959 / 2.8182615668403335 | [NPY](tensors/0002582.npy) |
| 2583 | `model.layers.0.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.875 / 9.1875 / -0.0061541578835911225 / 0.8510383023699726 | [NPY](tensors/0002583.npy) |
| 2584 | `model.layers.0.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.875 / 9.1875 / -0.0061541578835911225 / 0.8510383023699726 | [NPY](tensors/0002584.npy) |
| 2585 | `model.layers.0.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002585.npy) |
| 2586 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 894.0 / 894.0 / 894.0 / 0.0 | [NPY](tensors/0002586.npy) |
| 2587 | `model.layers.0.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2588 | `model.layers.0.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2589 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6077041625976562 / 1.0143983018780602 | [NPY](tensors/0002589.npy) |
| 2590 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.15405970811843872 / 0.6224309502943564 | [NPY](tensors/0002590.npy) |
| 2591 | `model.layers.0.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2592 | `model.layers.0.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.875 / 9.1875 / -0.0061541578835911225 / 0.8510383023699726 | [NPY](tensors/0002592.npy) |
| 2593 | `model.layers.0.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.75 / 9.4375 / 0.026633934816345572 / 0.9901209524173128 | [NPY](tensors/0002593.npy) |
| 2594 | `model.layers.0.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.875 / 9.1875 / -0.0061541578835911225 / 0.8510383023699726 | [NPY](tensors/0002594.npy) |
| 2595 | `model.layers.0.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.5 / 52.25 / 0.10294234752655029 / 5.473896623285773 | [NPY](tensors/0002595.npy) |
| 2596 | `model.layers.0.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.875 / 9.1875 / -0.0061541578835911225 / 0.8510383023699726 | [NPY](tensors/0002596.npy) |
| 2597 | `model.layers.0.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.125 / 5.28125 / -0.037626445293426514 / 1.245541664338603 | [NPY](tensors/0002597.npy) |
| 2598 | `model.layers.0.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.21875 / 2.484375 / -0.026770263837846642 / 0.46126846389719667 | [NPY](tensors/0002598.npy) |
| 2599 | `model.layers.0.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 40.25 / 0.02280812950597869 / 1.2031854810888492 | [NPY](tensors/0002599.npy) |
| 2600 | `model.layers.0.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 40.25 / 0.02280812950597869 / 1.2031854810888492 | [NPY](tensors/0002600.npy) |
| 2601 | `model.layers.0.self_attn` | 22 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0031934770836190823 / 0.035558033901452096 | [NPY](tensors/0002601.npy) |
| 2602 | `model.layers.0.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 39.0 / 0.032921987109714085 / 3.0698566824462374 | [NPY](tensors/0002602.npy) |
| 2603 | `model.layers.0.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.65625 / 1.9140625 / 0.004861289262771606 / 0.35611027171775617 | [NPY](tensors/0002603.npy) |
| 2604 | `model.layers.0.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.65625 / 1.9140625 / 0.004861289262771606 / 0.35611027171775617 | [NPY](tensors/0002604.npy) |
| 2605 | `model.layers.0.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -5.65625 / 1.9140625 / 0.004861289262771606 / 0.35611027171775617 | [NPY](tensors/0002605.npy) |
| 2606 | `model.layers.0.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2607 | `model.layers.0.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2608 | `model.layers.0.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2609 | `model.layers.0.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.03125 / 27.125 / 0.022080559531847635 / 0.886851367292576 | [NPY](tensors/0002609.npy) |
| 2610 | `model.layers.0.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.03125 / 27.125 / 0.022080559531847635 / 0.886851367292576 | [NPY](tensors/0002610.npy) |
| 2611 | `model.layers.0.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.296875 / 1.6796875 / -0.14957809448242188 / 0.8834613629090526 | [NPY](tensors/0002611.npy) |
| 2612 | `model.layers.0` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 66.0 / 0.05492958492702908 / 3.5152989778796897 | [NPY](tensors/0002612.npy) |
| 2691 | `model.layers.0` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 35.75 / 0.10075970540444056 / 2.923894051659387 | [NPY](tensors/0002691.npy) |
| 2692 | `model.layers.0` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002692.npy) |
| 2693 | `model.layers.0` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5635757446289062 / 1.0167091376095412 | [NPY](tensors/0002693.npy) |
| 2694 | `model.layers.0` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.13094085454940796 / 0.6637995182317289 | [NPY](tensors/0002694.npy) |
| 2695 | `model.layers.0` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 895.0 / 895.0 / 895.0 / 0.0 | [NPY](tensors/0002695.npy) |
| 2696 | `model.layers.0` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2697 | `model.layers.0` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2698 | `model.layers.0` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2699 | `model.layers.0.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 35.75 / 0.10075970540444056 / 2.923894051659387 | [NPY](tensors/0002699.npy) |
| 2700 | `model.layers.0.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.625 / 9.4375 / 0.01594721625248591 / 0.8267508378178091 | [NPY](tensors/0002700.npy) |
| 2701 | `model.layers.0.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.625 / 9.4375 / 0.01594721625248591 / 0.8267508378178091 | [NPY](tensors/0002701.npy) |
| 2702 | `model.layers.0.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002702.npy) |
| 2703 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 895.0 / 895.0 / 895.0 / 0.0 | [NPY](tensors/0002703.npy) |
| 2704 | `model.layers.0.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2705 | `model.layers.0.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2706 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5635757446289062 / 1.0167091376095412 | [NPY](tensors/0002706.npy) |
| 2707 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.13094085454940796 / 0.6637995182317289 | [NPY](tensors/0002707.npy) |
| 2708 | `model.layers.0.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2709 | `model.layers.0.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.625 / 9.4375 / 0.01594721625248591 / 0.8267508378178091 | [NPY](tensors/0002709.npy) |
| 2710 | `model.layers.0.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.53125 / 10.5 / 0.010230433661490679 / 1.027950574599858 | [NPY](tensors/0002710.npy) |
| 2711 | `model.layers.0.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.625 / 9.4375 / 0.01594721625248591 / 0.8267508378178091 | [NPY](tensors/0002711.npy) |
| 2712 | `model.layers.0.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.5 / 45.75 / -0.032315611839294434 / 5.614069358648372 | [NPY](tensors/0002712.npy) |
| 2713 | `model.layers.0.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.625 / 9.4375 / 0.01594721625248591 / 0.8267508378178091 | [NPY](tensors/0002713.npy) |
| 2714 | `model.layers.0.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.28125 / 5.28125 / -0.13151683285832405 / 1.2635844659353312 | [NPY](tensors/0002714.npy) |
| 2715 | `model.layers.0.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.21875 / 4.59375 / -0.021940280115813948 / 0.5605265419536204 | [NPY](tensors/0002715.npy) |
| 2716 | `model.layers.0.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.75 / 42.75 / 0.02111331867054105 / 1.2456947977604433 | [NPY](tensors/0002716.npy) |
| 2717 | `model.layers.0.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.75 / 42.75 / 0.02111331867054105 / 1.2456947977604433 | [NPY](tensors/0002717.npy) |
| 2718 | `model.layers.0.self_attn` | 23 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0035854391741279726 / 0.038380290934905296 | [NPY](tensors/0002718.npy) |
| 2719 | `model.layers.0.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 42.75 / 0.1218773259056939 / 3.1798992166903 | [NPY](tensors/0002719.npy) |
| 2720 | `model.layers.0.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.15625 / 1.8046875 / 0.010930868320994908 / 0.32957422805832176 | [NPY](tensors/0002720.npy) |
| 2721 | `model.layers.0.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.15625 / 1.8046875 / 0.010930868320994908 / 0.32957422805832176 | [NPY](tensors/0002721.npy) |
| 2722 | `model.layers.0.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -5.15625 / 1.8046875 / 0.010930868320994908 / 0.32957422805832176 | [NPY](tensors/0002722.npy) |
| 2723 | `model.layers.0.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2724 | `model.layers.0.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2725 | `model.layers.0.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2726 | `model.layers.0.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.953125 / 24.125 / 0.01490692471464475 / 0.6804143754374996 | [NPY](tensors/0002726.npy) |
| 2727 | `model.layers.0.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.953125 / 24.125 / 0.01490692471464475 / 0.6804143754374996 | [NPY](tensors/0002727.npy) |
| 2728 | `model.layers.0.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.25 / 1.4921875 / -0.17441749572753906 / 0.7263722456824571 | [NPY](tensors/0002728.npy) |
| 2729 | `model.layers.0` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 65.5 / 0.13665951622856987 / 3.4832234268200506 | [NPY](tensors/0002729.npy) |
| 2808 | `model.layers.0` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 41.5 / -0.06117983510096868 / 3.239521730305888 | [NPY](tensors/0002808.npy) |
| 2809 | `model.layers.0` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002809.npy) |
| 2810 | `model.layers.0` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5521621704101562 / 0.9747722822304562 | [NPY](tensors/0002810.npy) |
| 2811 | `model.layers.0` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.08557838201522827 / 0.7397982213081387 | [NPY](tensors/0002811.npy) |
| 2812 | `model.layers.0` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 896.0 / 896.0 / 896.0 / 0.0 | [NPY](tensors/0002812.npy) |
| 2813 | `model.layers.0` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2814 | `model.layers.0` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2815 | `model.layers.0` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2816 | `model.layers.0.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 41.5 / -0.06117983510096868 / 3.239521730305888 | [NPY](tensors/0002816.npy) |
| 2817 | `model.layers.0.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.25 / 6.71875 / -0.012421331637435489 / 0.6732175755280392 | [NPY](tensors/0002817.npy) |
| 2818 | `model.layers.0.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.25 / 6.71875 / -0.012421331637435489 / 0.6732175755280392 | [NPY](tensors/0002818.npy) |
| 2819 | `model.layers.0.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002819.npy) |
| 2820 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 896.0 / 896.0 / 896.0 / 0.0 | [NPY](tensors/0002820.npy) |
| 2821 | `model.layers.0.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2822 | `model.layers.0.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2823 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5521621704101562 / 0.9747722822304562 | [NPY](tensors/0002823.npy) |
| 2824 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.08557838201522827 / 0.7397982213081387 | [NPY](tensors/0002824.npy) |
| 2825 | `model.layers.0.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2826 | `model.layers.0.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.25 / 6.71875 / -0.012421331637435489 / 0.6732175755280392 | [NPY](tensors/0002826.npy) |
| 2827 | `model.layers.0.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.65625 / 8.6875 / 0.003311319276690483 / 0.9372361304093813 | [NPY](tensors/0002827.npy) |
| 2828 | `model.layers.0.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.25 / 6.71875 / -0.012421331637435489 / 0.6732175755280392 | [NPY](tensors/0002828.npy) |
| 2829 | `model.layers.0.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.25 / 55.25 / 0.019097506999969482 / 5.677525600430573 | [NPY](tensors/0002829.npy) |
| 2830 | `model.layers.0.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.25 / 6.71875 / -0.012421331637435489 / 0.6732175755280392 | [NPY](tensors/0002830.npy) |
| 2831 | `model.layers.0.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.59375 / 3.953125 / 0.026920944452285767 / 0.8723734543291857 | [NPY](tensors/0002831.npy) |
| 2832 | `model.layers.0.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.09375 / 4.34375 / -0.021622370841214433 / 0.5738215455928727 | [NPY](tensors/0002832.npy) |
| 2833 | `model.layers.0.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.6875 / 35.5 / 0.044880624612172446 / 1.1461076510535495 | [NPY](tensors/0002833.npy) |
| 2834 | `model.layers.0.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.6875 / 35.5 / 0.044880624612172446 / 1.1461076510535495 | [NPY](tensors/0002834.npy) |
| 2835 | `model.layers.0.self_attn` | 24 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0034506303288623567 / 0.03542891735190265 | [NPY](tensors/0002835.npy) |
| 2836 | `model.layers.0.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 40.5 / -0.016378969616360133 / 3.145651545481193 | [NPY](tensors/0002836.npy) |
| 2837 | `model.layers.0.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6953125 / 1.8984375 / 0.002747859060764313 / 0.2627449484787168 | [NPY](tensors/0002837.npy) |
| 2838 | `model.layers.0.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6953125 / 1.8984375 / 0.002747859060764313 / 0.2627449484787168 | [NPY](tensors/0002838.npy) |
| 2839 | `model.layers.0.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.6953125 / 1.8984375 / 0.002747859060764313 / 0.2627449484787168 | [NPY](tensors/0002839.npy) |
| 2840 | `model.layers.0.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2841 | `model.layers.0.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2842 | `model.layers.0.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2843 | `model.layers.0.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.1875 / 12.5625 / 0.03356278373135461 / 0.6697900691074019 | [NPY](tensors/0002843.npy) |
| 2844 | `model.layers.0.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.1875 / 12.5625 / 0.03356278373135461 / 0.6697900691074019 | [NPY](tensors/0002844.npy) |
| 2845 | `model.layers.0.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.984375 / 2.171875 / -0.04541778564453125 / 1.011556281820277 | [NPY](tensors/0002845.npy) |
| 2846 | `model.layers.0` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 44.5 / 0.017224068111843533 / 3.025407465342992 | [NPY](tensors/0002846.npy) |
| 2925 | `model.layers.0` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 25.5 / 0.05456397972173161 / 2.1700013252387307 | [NPY](tensors/0002925.npy) |
| 2926 | `model.layers.0` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002926.npy) |
| 2927 | `model.layers.0` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.576171875 / 0.9367379826853268 | [NPY](tensors/0002927.npy) |
| 2928 | `model.layers.0` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05449014902114868 / 0.7727124058266066 | [NPY](tensors/0002928.npy) |
| 2929 | `model.layers.0` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 897.0 / 897.0 / 897.0 / 0.0 | [NPY](tensors/0002929.npy) |
| 2930 | `model.layers.0` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2931 | `model.layers.0` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2932 | `model.layers.0` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2933 | `model.layers.0.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 25.5 / 0.05456397972173161 / 2.1700013252387307 | [NPY](tensors/0002933.npy) |
| 2934 | `model.layers.0.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5625 / 7.5625 / 0.017565650285945998 / 0.7820149012526071 | [NPY](tensors/0002934.npy) |
| 2935 | `model.layers.0.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5625 / 7.5625 / 0.017565650285945998 / 0.7820149012526071 | [NPY](tensors/0002935.npy) |
| 2936 | `model.layers.0.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002936.npy) |
| 2937 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 897.0 / 897.0 / 897.0 / 0.0 | [NPY](tensors/0002937.npy) |
| 2938 | `model.layers.0.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2939 | `model.layers.0.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2940 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.576171875 / 0.9367379826853268 | [NPY](tensors/0002940.npy) |
| 2941 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05449014902114868 / 0.7727124058266066 | [NPY](tensors/0002941.npy) |
| 2942 | `model.layers.0.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2943 | `model.layers.0.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5625 / 7.5625 / 0.017565650285945998 / 0.7820149012526071 | [NPY](tensors/0002943.npy) |
| 2944 | `model.layers.0.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.1875 / 11.375 / 0.02602137252688408 / 1.2562051867090098 | [NPY](tensors/0002944.npy) |
| 2945 | `model.layers.0.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5625 / 7.5625 / 0.017565650285945998 / 0.7820149012526071 | [NPY](tensors/0002945.npy) |
| 2946 | `model.layers.0.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -41.0 / 47.5 / -0.0025826692581176758 / 5.691282708926989 | [NPY](tensors/0002946.npy) |
| 2947 | `model.layers.0.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5625 / 7.5625 / 0.017565650285945998 / 0.7820149012526071 | [NPY](tensors/0002947.npy) |
| 2948 | `model.layers.0.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.96875 / 6.125 / 0.05672263354063034 / 1.4433839120581216 | [NPY](tensors/0002948.npy) |
| 2949 | `model.layers.0.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.796875 / 2.515625 / -0.008188236340174626 / 0.36292439473414656 | [NPY](tensors/0002949.npy) |
| 2950 | `model.layers.0.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.5 / 33.0 / 0.011684851803713375 / 0.9948346449305981 | [NPY](tensors/0002950.npy) |
| 2951 | `model.layers.0.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.5 / 33.0 / 0.011684851803713375 / 0.9948346449305981 | [NPY](tensors/0002951.npy) |
| 2952 | `model.layers.0.self_attn` | 25 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002197230298098407 / 0.03177722820774534 | [NPY](tensors/0002952.npy) |
| 2953 | `model.layers.0.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 32.75 / 0.06630591286553277 / 2.436343990419945 | [NPY](tensors/0002953.npy) |
| 2954 | `model.layers.0.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.78125 / 1.90625 / 0.010491712225808037 / 0.38596622183985974 | [NPY](tensors/0002954.npy) |
| 2955 | `model.layers.0.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.78125 / 1.90625 / 0.010491712225808037 / 0.38596622183985974 | [NPY](tensors/0002955.npy) |
| 2956 | `model.layers.0.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.78125 / 1.90625 / 0.010491712225808037 / 0.38596622183985974 | [NPY](tensors/0002956.npy) |
| 2957 | `model.layers.0.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2958 | `model.layers.0.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2959 | `model.layers.0.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2960 | `model.layers.0.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -13.5625 / 17.5 / 0.006019900304575761 / 0.9531654466583551 | [NPY](tensors/0002960.npy) |
| 2961 | `model.layers.0.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5625 / 17.5 / 0.006019900304575761 / 0.9531654466583551 | [NPY](tensors/0002961.npy) |
| 2962 | `model.layers.0.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.546875 / 3.03125 / -0.2587432861328125 / 1.091041387897612 | [NPY](tensors/0002962.npy) |
| 2963 | `model.layers.0` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 48.75 / 0.0723017586602105 / 2.8665952969753214 | [NPY](tensors/0002963.npy) |
| 3042 | `model.layers.0` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 25.5 / 0.05456397972173161 / 2.1700013252387307 | [NPY](tensors/0003042.npy) |
| 3043 | `model.layers.0` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003043.npy) |
| 3044 | `model.layers.0` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.60968017578125 / 0.9551838287803889 | [NPY](tensors/0003044.npy) |
| 3045 | `model.layers.0` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05779397487640381 / 0.7235452926755772 | [NPY](tensors/0003045.npy) |
| 3046 | `model.layers.0` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 898.0 / 898.0 / 898.0 / 0.0 | [NPY](tensors/0003046.npy) |
| 3047 | `model.layers.0` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3048 | `model.layers.0` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3049 | `model.layers.0` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3050 | `model.layers.0.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 25.5 / 0.05456397972173161 / 2.1700013252387307 | [NPY](tensors/0003050.npy) |
| 3051 | `model.layers.0.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5625 / 7.5625 / 0.017565650285945998 / 0.7820149012526071 | [NPY](tensors/0003051.npy) |
| 3052 | `model.layers.0.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5625 / 7.5625 / 0.017565650285945998 / 0.7820149012526071 | [NPY](tensors/0003052.npy) |
| 3053 | `model.layers.0.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003053.npy) |
| 3054 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 898.0 / 898.0 / 898.0 / 0.0 | [NPY](tensors/0003054.npy) |
| 3055 | `model.layers.0.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3056 | `model.layers.0.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3057 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.60968017578125 / 0.9551838287803889 | [NPY](tensors/0003057.npy) |
| 3058 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05779397487640381 / 0.7235452926755772 | [NPY](tensors/0003058.npy) |
| 3059 | `model.layers.0.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3060 | `model.layers.0.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5625 / 7.5625 / 0.017565650285945998 / 0.7820149012526071 | [NPY](tensors/0003060.npy) |
| 3061 | `model.layers.0.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.1875 / 11.375 / 0.02602137252688408 / 1.2562051867090098 | [NPY](tensors/0003061.npy) |
| 3062 | `model.layers.0.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5625 / 7.5625 / 0.017565650285945998 / 0.7820149012526071 | [NPY](tensors/0003062.npy) |
| 3063 | `model.layers.0.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -41.0 / 47.5 / -0.0025826692581176758 / 5.691282708926989 | [NPY](tensors/0003063.npy) |
| 3064 | `model.layers.0.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5625 / 7.5625 / 0.017565650285945998 / 0.7820149012526071 | [NPY](tensors/0003064.npy) |
| 3065 | `model.layers.0.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.96875 / 6.125 / 0.05672263354063034 / 1.4433839120581216 | [NPY](tensors/0003065.npy) |
| 3066 | `model.layers.0.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.3125 / 5.96875 / 0.0005498234066863006 / 0.6340903256997753 | [NPY](tensors/0003066.npy) |
| 3067 | `model.layers.0.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.25 / 18.625 / 0.009896619783507452 / 0.69409840794608 | [NPY](tensors/0003067.npy) |
| 3068 | `model.layers.0.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.25 / 18.625 / 0.009896619783507452 / 0.69409840794608 | [NPY](tensors/0003068.npy) |
| 3069 | `model.layers.0.self_attn` | 26 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9765625 / 0.0020858448007215393 / 0.03016984896093101 | [NPY](tensors/0003069.npy) |
| 3070 | `model.layers.0.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.5 / 27.0 / 0.06431614028082953 / 2.3429880957248623 | [NPY](tensors/0003070.npy) |
| 3071 | `model.layers.0.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9140625 / 1.9921875 / 0.007725636826621161 / 0.4394617492207764 | [NPY](tensors/0003071.npy) |
| 3072 | `model.layers.0.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9140625 / 1.9921875 / 0.007725636826621161 / 0.4394617492207764 | [NPY](tensors/0003072.npy) |
| 3073 | `model.layers.0.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.9140625 / 1.9921875 / 0.007725636826621161 / 0.4394617492207764 | [NPY](tensors/0003073.npy) |
| 3074 | `model.layers.0.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3075 | `model.layers.0.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3076 | `model.layers.0.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3077 | `model.layers.0.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -10.25 / 15.0625 / 0.0033848661101526685 / 0.790974577450866 | [NPY](tensors/0003077.npy) |
| 3078 | `model.layers.0.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.25 / 15.0625 / 0.0033848661101526685 / 0.790974577450866 | [NPY](tensors/0003078.npy) |
| 3079 | `model.layers.0.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3515625 / 2.34375 / -0.2111644744873047 / 0.8460462607544108 | [NPY](tensors/0003079.npy) |
| 3080 | `model.layers.0` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.75 / 33.75 / 0.06762170791625977 / 2.59168942093758 | [NPY](tensors/0003080.npy) |
| 3159 | `model.layers.0` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 29.0 / -0.03774418102370368 / 2.517368491406688 | [NPY](tensors/0003159.npy) |
| 3160 | `model.layers.0` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003160.npy) |
| 3161 | `model.layers.0` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.6215248107910156 / 0.953261420864228 | [NPY](tensors/0003161.npy) |
| 3162 | `model.layers.0` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.08504927158355713 / 0.7123271249161985 | [NPY](tensors/0003162.npy) |
| 3163 | `model.layers.0` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 899.0 / 899.0 / 899.0 / 0.0 | [NPY](tensors/0003163.npy) |
| 3164 | `model.layers.0` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3165 | `model.layers.0` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3166 | `model.layers.0` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3167 | `model.layers.0.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 29.0 / -0.03774418102370368 / 2.517368491406688 | [NPY](tensors/0003167.npy) |
| 3168 | `model.layers.0.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.4375 / 8.1875 / -0.009578915457758639 / 0.720525670998352 | [NPY](tensors/0003168.npy) |
| 3169 | `model.layers.0.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.4375 / 8.1875 / -0.009578915457758639 / 0.720525670998352 | [NPY](tensors/0003169.npy) |
| 3170 | `model.layers.0.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003170.npy) |
| 3171 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 899.0 / 899.0 / 899.0 / 0.0 | [NPY](tensors/0003171.npy) |
| 3172 | `model.layers.0.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3173 | `model.layers.0.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3174 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.6215248107910156 / 0.953261420864228 | [NPY](tensors/0003174.npy) |
| 3175 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.08504927158355713 / 0.7123271249161985 | [NPY](tensors/0003175.npy) |
| 3176 | `model.layers.0.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3177 | `model.layers.0.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.4375 / 8.1875 / -0.009578915457758639 / 0.720525670998352 | [NPY](tensors/0003177.npy) |
| 3178 | `model.layers.0.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.84375 / 9.625 / 0.005252554779872298 / 0.9763704305068986 | [NPY](tensors/0003178.npy) |
| 3179 | `model.layers.0.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.4375 / 8.1875 / -0.009578915457758639 / 0.720525670998352 | [NPY](tensors/0003179.npy) |
| 3180 | `model.layers.0.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.75 / 52.25 / 0.006677001714706421 / 5.939404291707201 | [NPY](tensors/0003180.npy) |
| 3181 | `model.layers.0.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.4375 / 8.1875 / -0.009578915457758639 / 0.720525670998352 | [NPY](tensors/0003181.npy) |
| 3182 | `model.layers.0.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.765625 / 3.640625 / -0.020492255687713623 / 1.0376857683306149 | [NPY](tensors/0003182.npy) |
| 3183 | `model.layers.0.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.25 / 3.796875 / -0.004490458588406909 / 0.5254933223290164 | [NPY](tensors/0003183.npy) |
| 3184 | `model.layers.0.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.21875 / 29.375 / 0.034116753935813905 / 0.8941990862407886 | [NPY](tensors/0003184.npy) |
| 3185 | `model.layers.0.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.21875 / 29.375 / 0.034116753935813905 / 0.8941990862407886 | [NPY](tensors/0003185.npy) |
| 3186 | `model.layers.0.self_attn` | 27 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.002791651547992567 / 0.031111689970126605 | [NPY](tensors/0003186.npy) |
| 3187 | `model.layers.0.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 30.75 / -0.0036810768975151908 / 2.651252555671307 | [NPY](tensors/0003187.npy) |
| 3188 | `model.layers.0.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.25 / 1.953125 / 0.0045718782477908665 / 0.29543646125106315 | [NPY](tensors/0003188.npy) |
| 3189 | `model.layers.0.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.25 / 1.953125 / 0.0045718782477908665 / 0.29543646125106315 | [NPY](tensors/0003189.npy) |
| 3190 | `model.layers.0.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.25 / 1.953125 / 0.0045718782477908665 / 0.29543646125106315 | [NPY](tensors/0003190.npy) |
| 3191 | `model.layers.0.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3192 | `model.layers.0.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3193 | `model.layers.0.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3194 | `model.layers.0.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.8125 / 18.5 / 0.018096540537145402 / 0.6135123033600529 | [NPY](tensors/0003194.npy) |
| 3195 | `model.layers.0.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.8125 / 18.5 / 0.018096540537145402 / 0.6135123033600529 | [NPY](tensors/0003195.npy) |
| 3196 | `model.layers.0.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.28125 / 2.1875 / -0.0766173005104065 / 1.1403311922768409 | [NPY](tensors/0003196.npy) |
| 3197 | `model.layers.0` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 49.25 / 0.014525543318854438 / 2.822571751261138 | [NPY](tensors/0003197.npy) |
| 3276 | `model.layers.0` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 24.5 / -0.07184715121984482 / 2.629652818677747 | [NPY](tensors/0003276.npy) |
| 3277 | `model.layers.0` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003277.npy) |
| 3278 | `model.layers.0` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.6053333282470703 / 0.9378499631722268 | [NPY](tensors/0003278.npy) |
| 3279 | `model.layers.0` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.10818588733673096 / 0.7432403804988892 | [NPY](tensors/0003279.npy) |
| 3280 | `model.layers.0` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 900.0 / 900.0 / 900.0 / 0.0 | [NPY](tensors/0003280.npy) |
| 3281 | `model.layers.0` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3282 | `model.layers.0` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3283 | `model.layers.0` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3284 | `model.layers.0.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 24.5 / -0.07184715121984482 / 2.629652818677747 | [NPY](tensors/0003284.npy) |
| 3285 | `model.layers.0.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 6.3125 / -0.02045272911588351 / 0.7053888978076066 | [NPY](tensors/0003285.npy) |
| 3286 | `model.layers.0.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 6.3125 / -0.02045272911588351 / 0.7053888978076066 | [NPY](tensors/0003286.npy) |
| 3287 | `model.layers.0.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003287.npy) |
| 3288 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 900.0 / 900.0 / 900.0 / 0.0 | [NPY](tensors/0003288.npy) |
| 3289 | `model.layers.0.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3290 | `model.layers.0.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3291 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.6053333282470703 / 0.9378499631722268 | [NPY](tensors/0003291.npy) |
| 3292 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.10818588733673096 / 0.7432403804988892 | [NPY](tensors/0003292.npy) |
| 3293 | `model.layers.0.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3294 | `model.layers.0.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 6.3125 / -0.02045272911588351 / 0.7053888978076066 | [NPY](tensors/0003294.npy) |
| 3295 | `model.layers.0.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5 / 8.6875 / 0.054075641091912985 / 1.0388639843125458 | [NPY](tensors/0003295.npy) |
| 3296 | `model.layers.0.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 6.3125 / -0.02045272911588351 / 0.7053888978076066 | [NPY](tensors/0003296.npy) |
| 3297 | `model.layers.0.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.25 / 48.25 / 0.06501370668411255 / 5.356391689665999 | [NPY](tensors/0003297.npy) |
| 3298 | `model.layers.0.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 6.3125 / -0.02045272911588351 / 0.7053888978076066 | [NPY](tensors/0003298.npy) |
| 3299 | `model.layers.0.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.09375 / 4.1875 / -0.007382184267044067 / 1.1528028508064896 | [NPY](tensors/0003299.npy) |
| 3300 | `model.layers.0.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.59375 / 3.203125 / -0.014664050093415426 / 0.44009525965177143 | [NPY](tensors/0003300.npy) |
| 3301 | `model.layers.0.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.5625 / 35.5 / 0.03227868734134568 / 1.0319703721785516 | [NPY](tensors/0003301.npy) |
| 3302 | `model.layers.0.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.5625 / 35.5 / 0.03227868734134568 / 1.0319703721785516 | [NPY](tensors/0003302.npy) |
| 3303 | `model.layers.0.self_attn` | 28 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002479859504444232 / 0.029345066228173095 | [NPY](tensors/0003303.npy) |
| 3304 | `model.layers.0.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 35.25 / -0.039666453997294106 / 2.792396176929813 | [NPY](tensors/0003304.npy) |
| 3305 | `model.layers.0.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.359375 / 1.5390625 / 0.0013326121701134576 / 0.30589008247925314 | [NPY](tensors/0003305.npy) |
| 3306 | `model.layers.0.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.359375 / 1.5390625 / 0.0013326121701134576 / 0.30589008247925314 | [NPY](tensors/0003306.npy) |
| 3307 | `model.layers.0.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.359375 / 1.5390625 / 0.0013326121701134576 / 0.30589008247925314 | [NPY](tensors/0003307.npy) |
| 3308 | `model.layers.0.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3309 | `model.layers.0.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3310 | `model.layers.0.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3311 | `model.layers.0.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.515625 / 22.375 / 0.027041319095426137 / 0.6689465178582148 | [NPY](tensors/0003311.npy) |
| 3312 | `model.layers.0.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.515625 / 22.375 / 0.027041319095426137 / 0.6689465178582148 | [NPY](tensors/0003312.npy) |
| 3313 | `model.layers.0.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.296875 / 1.1484375 / -0.08187675476074219 / 0.811289412415662 | [NPY](tensors/0003313.npy) |
| 3314 | `model.layers.0` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 56.5 / -0.0125975767771403 / 2.9776393127822325 | [NPY](tensors/0003314.npy) |
| 3393 | `model.layers.0` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.25 / 44.75 / -0.036300554778426884 / 2.7070791741410978 | [NPY](tensors/0003393.npy) |
| 3394 | `model.layers.0` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003394.npy) |
| 3395 | `model.layers.0` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.58184814453125 / 0.9804601915905449 | [NPY](tensors/0003395.npy) |
| 3396 | `model.layers.0` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / 0.11050879955291748 / 0.7066672716698735 | [NPY](tensors/0003396.npy) |
| 3397 | `model.layers.0` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 901.0 / 901.0 / 901.0 / 0.0 | [NPY](tensors/0003397.npy) |
| 3398 | `model.layers.0` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3399 | `model.layers.0` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3400 | `model.layers.0` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3401 | `model.layers.0.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.25 / 44.75 / -0.036300554778426884 / 2.7070791741410978 | [NPY](tensors/0003401.npy) |
| 3402 | `model.layers.0.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.5625 / 12.5625 / -0.008150073720349206 / 0.7364308595706629 | [NPY](tensors/0003402.npy) |
| 3403 | `model.layers.0.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.5625 / 12.5625 / -0.008150073720349206 / 0.7364308595706629 | [NPY](tensors/0003403.npy) |
| 3404 | `model.layers.0.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003404.npy) |
| 3405 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 901.0 / 901.0 / 901.0 / 0.0 | [NPY](tensors/0003405.npy) |
| 3406 | `model.layers.0.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3407 | `model.layers.0.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3408 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.58184814453125 / 0.9804601915905449 | [NPY](tensors/0003408.npy) |
| 3409 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / 0.11050879955291748 / 0.7066672716698735 | [NPY](tensors/0003409.npy) |
| 3410 | `model.layers.0.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3411 | `model.layers.0.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.5625 / 12.5625 / -0.008150073720349206 / 0.7364308595706629 | [NPY](tensors/0003411.npy) |
| 3412 | `model.layers.0.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 8.5 / 0.03105339384637773 / 1.0169544086728253 | [NPY](tensors/0003412.npy) |
| 3413 | `model.layers.0.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.5625 / 12.5625 / -0.008150073720349206 / 0.7364308595706629 | [NPY](tensors/0003413.npy) |
| 3414 | `model.layers.0.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.75 / 48.75 / 0.0851534903049469 / 5.703659410914989 | [NPY](tensors/0003414.npy) |
| 3415 | `model.layers.0.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.5625 / 12.5625 / -0.008150073720349206 / 0.7364308595706629 | [NPY](tensors/0003415.npy) |
| 3416 | `model.layers.0.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.90625 / 4.78125 / -0.006120890378952026 / 1.1550646421383879 | [NPY](tensors/0003416.npy) |
| 3417 | `model.layers.0.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.53125 / 3.171875 / -0.009767522971742437 / 0.5032404485260579 | [NPY](tensors/0003417.npy) |
| 3418 | `model.layers.0.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.8125 / 35.25 / 0.04036329579022196 / 1.0562956127268817 | [NPY](tensors/0003418.npy) |
| 3419 | `model.layers.0.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.8125 / 35.25 / 0.04036329579022196 / 1.0562956127268817 | [NPY](tensors/0003419.npy) |
| 3420 | `model.layers.0.self_attn` | 29 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.002918055998098796 / 0.03263862805499721 | [NPY](tensors/0003420.npy) |
| 3421 | `model.layers.0.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.125 / 46.75 / 0.004106860690646702 / 2.8703286065291604 | [NPY](tensors/0003421.npy) |
| 3422 | `model.layers.0.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.4140625 / 2.59375 / 0.0034872810045878094 / 0.3193770635891301 | [NPY](tensors/0003422.npy) |
| 3423 | `model.layers.0.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.4140625 / 2.59375 / 0.0034872810045878094 / 0.3193770635891301 | [NPY](tensors/0003423.npy) |
| 3424 | `model.layers.0.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.4140625 / 2.59375 / 0.0034872810045878094 / 0.3193770635891301 | [NPY](tensors/0003424.npy) |
| 3425 | `model.layers.0.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3426 | `model.layers.0.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3427 | `model.layers.0.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3428 | `model.layers.0.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.96875 / 18.125 / 0.032115828494230905 / 0.7702596000953105 | [NPY](tensors/0003428.npy) |
| 3429 | `model.layers.0.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.96875 / 18.125 / 0.032115828494230905 / 0.7702596000953105 | [NPY](tensors/0003429.npy) |
| 3430 | `model.layers.0.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.734375 / 2.390625 / -0.069549560546875 / 1.0806463511939326 | [NPY](tensors/0003430.npy) |
| 3431 | `model.layers.0` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 52.5 / 0.03614867130915324 / 3.084655197248767 | [NPY](tensors/0003431.npy) |
| 3510 | `model.layers.0` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 33.75 / -0.0287939449151357 / 2.66976579896416 | [NPY](tensors/0003510.npy) |
| 3511 | `model.layers.0` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003511.npy) |
| 3512 | `model.layers.0` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.57342529296875 / 1.011353752766297 | [NPY](tensors/0003512.npy) |
| 3513 | `model.layers.0` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.10230749845504761 / 0.668999264851671 | [NPY](tensors/0003513.npy) |
| 3514 | `model.layers.0` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 902.0 / 902.0 / 902.0 / 0.0 | [NPY](tensors/0003514.npy) |
| 3515 | `model.layers.0` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3516 | `model.layers.0` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3517 | `model.layers.0` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3518 | `model.layers.0.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 33.75 / -0.0287939449151357 / 2.66976579896416 | [NPY](tensors/0003518.npy) |
| 3519 | `model.layers.0.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.375 / 8.8125 / -0.008239281839794582 / 0.7735832441287327 | [NPY](tensors/0003519.npy) |
| 3520 | `model.layers.0.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.375 / 8.8125 / -0.008239281839794582 / 0.7735832441287327 | [NPY](tensors/0003520.npy) |
| 3521 | `model.layers.0.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003521.npy) |
| 3522 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 902.0 / 902.0 / 902.0 / 0.0 | [NPY](tensors/0003522.npy) |
| 3523 | `model.layers.0.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3524 | `model.layers.0.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3525 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.57342529296875 / 1.011353752766297 | [NPY](tensors/0003525.npy) |
| 3526 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.10230749845504761 / 0.668999264851671 | [NPY](tensors/0003526.npy) |
| 3527 | `model.layers.0.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3528 | `model.layers.0.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.375 / 8.8125 / -0.008239281839794582 / 0.7735832441287327 | [NPY](tensors/0003528.npy) |
| 3529 | `model.layers.0.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0625 / 7.34375 / 0.05205812203348614 / 0.9740426038893796 | [NPY](tensors/0003529.npy) |
| 3530 | `model.layers.0.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.375 / 8.8125 / -0.008239281839794582 / 0.7735832441287327 | [NPY](tensors/0003530.npy) |
| 3531 | `model.layers.0.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.75 / 50.75 / -0.020516306161880493 / 5.573563822652621 | [NPY](tensors/0003531.npy) |
| 3532 | `model.layers.0.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.375 / 8.8125 / -0.008239281839794582 / 0.7735832441287327 | [NPY](tensors/0003532.npy) |
| 3533 | `model.layers.0.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.1875 / 4.625 / -0.019698143005371094 / 1.2494061276922335 | [NPY](tensors/0003533.npy) |
| 3534 | `model.layers.0.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.5625 / 3.71875 / -0.025096095297044485 / 0.6075097024262249 | [NPY](tensors/0003534.npy) |
| 3535 | `model.layers.0.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.5 / 44.25 / 0.04989535568488969 / 1.2954408327238338 | [NPY](tensors/0003535.npy) |
| 3536 | `model.layers.0.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.5 / 44.25 / 0.04989535568488969 / 1.2954408327238338 | [NPY](tensors/0003536.npy) |
| 3537 | `model.layers.0.self_attn` | 30 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0031605156541382705 / 0.036100313396956095 | [NPY](tensors/0003537.npy) |
| 3538 | `model.layers.0.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 43.25 / 0.021140628390842013 / 3.030920191056959 | [NPY](tensors/0003538.npy) |
| 3539 | `model.layers.0.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.4375 / 2.078125 / 0.009401056501600478 / 0.35452392916045894 | [NPY](tensors/0003539.npy) |
| 3540 | `model.layers.0.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.4375 / 2.078125 / 0.009401056501600478 / 0.35452392916045894 | [NPY](tensors/0003540.npy) |
| 3541 | `model.layers.0.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.4375 / 2.078125 / 0.009401056501600478 / 0.35452392916045894 | [NPY](tensors/0003541.npy) |
| 3542 | `model.layers.0.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3543 | `model.layers.0.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3544 | `model.layers.0.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3545 | `model.layers.0.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.75 / 20.75 / 0.02536668326291773 / 0.7745067534778357 | [NPY](tensors/0003545.npy) |
| 3546 | `model.layers.0.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.75 / 20.75 / 0.02536668326291773 / 0.7745067534778357 | [NPY](tensors/0003546.npy) |
| 3547 | `model.layers.0.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.390625 / 1.953125 / -0.10678863525390625 / 0.9210887863087214 | [NPY](tensors/0003547.npy) |
| 3548 | `model.layers.0` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 64.0 / 0.04644594192504883 / 3.405516849031125 | [NPY](tensors/0003548.npy) |
| 3627 | `model.layers.0` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 32.5 / 0.01878972484005822 / 2.7798793569859233 | [NPY](tensors/0003627.npy) |
| 3628 | `model.layers.0` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003628.npy) |
| 3629 | `model.layers.0` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.576141357421875 / 0.9960825148117132 | [NPY](tensors/0003629.npy) |
| 3630 | `model.layers.0` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.10725325345993042 / 0.6890912510284947 | [NPY](tensors/0003630.npy) |
| 3631 | `model.layers.0` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 903.0 / 903.0 / 903.0 / 0.0 | [NPY](tensors/0003631.npy) |
| 3632 | `model.layers.0` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3633 | `model.layers.0` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3634 | `model.layers.0` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3635 | `model.layers.0.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 32.5 / 0.01878972484005822 / 2.7798793569859233 | [NPY](tensors/0003635.npy) |
| 3636 | `model.layers.0.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5 / 8.875 / -0.002318682604365879 / 0.7426183872737632 | [NPY](tensors/0003636.npy) |
| 3637 | `model.layers.0.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5 / 8.875 / -0.002318682604365879 / 0.7426183872737632 | [NPY](tensors/0003637.npy) |
| 3638 | `model.layers.0.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003638.npy) |
| 3639 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 903.0 / 903.0 / 903.0 / 0.0 | [NPY](tensors/0003639.npy) |
| 3640 | `model.layers.0.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3641 | `model.layers.0.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3642 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.576141357421875 / 0.9960825148117132 | [NPY](tensors/0003642.npy) |
| 3643 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.10725325345993042 / 0.6890912510284947 | [NPY](tensors/0003643.npy) |
| 3644 | `model.layers.0.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3645 | `model.layers.0.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5 / 8.875 / -0.002318682604365879 / 0.7426183872737632 | [NPY](tensors/0003645.npy) |
| 3646 | `model.layers.0.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.3125 / 8.625 / 0.0474619222804904 / 0.9712427645837794 | [NPY](tensors/0003646.npy) |
| 3647 | `model.layers.0.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5 / 8.875 / -0.002318682604365879 / 0.7426183872737632 | [NPY](tensors/0003647.npy) |
| 3648 | `model.layers.0.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.25 / 51.5 / 0.03446221351623535 / 5.746072652121225 | [NPY](tensors/0003648.npy) |
| 3649 | `model.layers.0.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5 / 8.875 / -0.002318682604365879 / 0.7426183872737632 | [NPY](tensors/0003649.npy) |
| 3650 | `model.layers.0.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.265625 / 5.125 / 0.08859586715698242 / 1.003477910350097 | [NPY](tensors/0003650.npy) |
| 3651 | `model.layers.0.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.59375 / 4.5625 / 0.0024667083998792805 / 0.595697001059235 | [NPY](tensors/0003651.npy) |
| 3652 | `model.layers.0.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.78125 / 38.25 / 0.04586562663316727 / 1.1198196430853697 | [NPY](tensors/0003652.npy) |
| 3653 | `model.layers.0.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.78125 / 38.25 / 0.04586562663316727 / 1.1198196430853697 | [NPY](tensors/0003653.npy) |
| 3654 | `model.layers.0.self_attn` | 31 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0035453243385496647 / 0.03898077910058051 | [NPY](tensors/0003654.npy) |
| 3655 | `model.layers.0.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.0 / 35.75 / 0.06472735934787327 / 2.910230938668938 | [NPY](tensors/0003655.npy) |
| 3656 | `model.layers.0.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.96875 / 1.7578125 / -0.0010098026858435737 / 0.31566222296627766 | [NPY](tensors/0003656.npy) |
| 3657 | `model.layers.0.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.96875 / 1.7578125 / -0.0010098026858435737 / 0.31566222296627766 | [NPY](tensors/0003657.npy) |
| 3658 | `model.layers.0.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.96875 / 1.7578125 / -0.0010098026858435737 / 0.31566222296627766 | [NPY](tensors/0003658.npy) |
| 3659 | `model.layers.0.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3660 | `model.layers.0.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3661 | `model.layers.0.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3662 | `model.layers.0.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.5 / 28.625 / 0.02741240660349528 / 0.9092405910444967 | [NPY](tensors/0003662.npy) |
| 3663 | `model.layers.0.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.5 / 28.625 / 0.02741240660349528 / 0.9092405910444967 | [NPY](tensors/0003663.npy) |
| 3664 | `model.layers.0.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.46875 / 2.4375 / -0.13112640380859375 / 1.0034621688117837 | [NPY](tensors/0003664.npy) |
| 3665 | `model.layers.0` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.0 / 61.5 / 0.09208992322285971 / 3.182835818683663 | [NPY](tensors/0003665.npy) |
| 3744 | `model.layers.0` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 43.25 / -0.034352450587579776 / 3.143983932257166 | [NPY](tensors/0003744.npy) |
| 3745 | `model.layers.0` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003745.npy) |
| 3746 | `model.layers.0` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.56591796875 / 1.009767041675747 | [NPY](tensors/0003746.npy) |
| 3747 | `model.layers.0` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.28125 / 0.13484972715377808 / 0.6728120153629138 | [NPY](tensors/0003747.npy) |
| 3748 | `model.layers.0` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 904.0 / 904.0 / 904.0 / 0.0 | [NPY](tensors/0003748.npy) |
| 3749 | `model.layers.0` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3750 | `model.layers.0` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3751 | `model.layers.0` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3752 | `model.layers.0.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 43.25 / -0.034352450587579776 / 3.143983932257166 | [NPY](tensors/0003752.npy) |
| 3753 | `model.layers.0.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 7.0 / -0.010667433015381296 / 0.740064713677182 | [NPY](tensors/0003753.npy) |
| 3754 | `model.layers.0.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 7.0 / -0.010667433015381296 / 0.740064713677182 | [NPY](tensors/0003754.npy) |
| 3755 | `model.layers.0.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003755.npy) |
| 3756 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 904.0 / 904.0 / 904.0 / 0.0 | [NPY](tensors/0003756.npy) |
| 3757 | `model.layers.0.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3758 | `model.layers.0.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3759 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.56591796875 / 1.009767041675747 | [NPY](tensors/0003759.npy) |
| 3760 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.28125 / 0.13484972715377808 / 0.6728120153629138 | [NPY](tensors/0003760.npy) |
| 3761 | `model.layers.0.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3762 | `model.layers.0.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 7.0 / -0.010667433015381296 / 0.740064713677182 | [NPY](tensors/0003762.npy) |
| 3763 | `model.layers.0.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.96875 / 10.75 / 0.03389013931155205 / 1.0133434807008517 | [NPY](tensors/0003763.npy) |
| 3764 | `model.layers.0.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 7.0 / -0.010667433015381296 / 0.740064713677182 | [NPY](tensors/0003764.npy) |
| 3765 | `model.layers.0.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -55.0 / 59.0 / -0.017447173595428467 / 7.043934623847653 | [NPY](tensors/0003765.npy) |
| 3766 | `model.layers.0.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 7.0 / -0.010667433015381296 / 0.740064713677182 | [NPY](tensors/0003766.npy) |
| 3767 | `model.layers.0.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 4.3125 / 0.0012288093566894531 / 1.0756639608258283 | [NPY](tensors/0003767.npy) |
| 3768 | `model.layers.0.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.46875 / 4.34375 / -0.0011141464042339067 / 0.47812170755599465 | [NPY](tensors/0003768.npy) |
| 3769 | `model.layers.0.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.0 / 29.625 / 0.02675423390335507 / 0.9639175029806432 | [NPY](tensors/0003769.npy) |
| 3770 | `model.layers.0.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.0 / 29.625 / 0.02675423390335507 / 0.9639175029806432 | [NPY](tensors/0003770.npy) |
| 3771 | `model.layers.0.self_attn` | 32 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002799362625175417 / 0.029622087768025693 | [NPY](tensors/0003771.npy) |
| 3772 | `model.layers.0.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 42.75 / -0.007660039265950521 / 3.0459527713538894 | [NPY](tensors/0003772.npy) |
| 3773 | `model.layers.0.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.34375 / 1.6875 / 0.001149839162826538 / 0.27164696485794915 | [NPY](tensors/0003773.npy) |
| 3774 | `model.layers.0.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.34375 / 1.6875 / 0.001149839162826538 / 0.27164696485794915 | [NPY](tensors/0003774.npy) |
| 3775 | `model.layers.0.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.34375 / 1.6875 / 0.001149839162826538 / 0.27164696485794915 | [NPY](tensors/0003775.npy) |
| 3776 | `model.layers.0.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3777 | `model.layers.0.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3778 | `model.layers.0.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3779 | `model.layers.0.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.78125 / 6.59375 / -0.006890330298079385 / 0.513967265303858 | [NPY](tensors/0003779.npy) |
| 3780 | `model.layers.0.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.78125 / 6.59375 / -0.006890330298079385 / 0.513967265303858 | [NPY](tensors/0003780.npy) |
| 3781 | `model.layers.0.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.671875 / 2.6875 / -0.066802978515625 / 1.2351038473348626 | [NPY](tensors/0003781.npy) |
| 3782 | `model.layers.0` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 40.5 / -0.014482210742102729 / 2.842344401967666 | [NPY](tensors/0003782.npy) |
| 3861 | `model.layers.0` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.375 / 46.25 / 0.04128313856716785 / 2.545045601740554 | [NPY](tensors/0003861.npy) |
| 3862 | `model.layers.0` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003862.npy) |
| 3863 | `model.layers.0` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.517730712890625 / 1.0482222047318746 | [NPY](tensors/0003863.npy) |
| 3864 | `model.layers.0` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.1620463728904724 / 0.645396390931362 | [NPY](tensors/0003864.npy) |
| 3865 | `model.layers.0` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 905.0 / 905.0 / 905.0 / 0.0 | [NPY](tensors/0003865.npy) |
| 3866 | `model.layers.0` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3867 | `model.layers.0` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3868 | `model.layers.0` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3869 | `model.layers.0.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.375 / 46.25 / 0.04128313856716785 / 2.545045601740554 | [NPY](tensors/0003869.npy) |
| 3870 | `model.layers.0.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.875 / 14.1875 / 0.005499152032037576 / 0.820284290275701 | [NPY](tensors/0003870.npy) |
| 3871 | `model.layers.0.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.875 / 14.1875 / 0.005499152032037576 / 0.820284290275701 | [NPY](tensors/0003871.npy) |
| 3872 | `model.layers.0.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003872.npy) |
| 3873 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 905.0 / 905.0 / 905.0 / 0.0 | [NPY](tensors/0003873.npy) |
| 3874 | `model.layers.0.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3875 | `model.layers.0.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3876 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.517730712890625 / 1.0482222047318746 | [NPY](tensors/0003876.npy) |
| 3877 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.1620463728904724 / 0.645396390931362 | [NPY](tensors/0003877.npy) |
| 3878 | `model.layers.0.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3879 | `model.layers.0.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.875 / 14.1875 / 0.005499152032037576 / 0.820284290275701 | [NPY](tensors/0003879.npy) |
| 3880 | `model.layers.0.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.53125 / 9.0 / -0.001307317754253745 / 0.9908759419925321 | [NPY](tensors/0003880.npy) |
| 3881 | `model.layers.0.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.875 / 14.1875 / 0.005499152032037576 / 0.820284290275701 | [NPY](tensors/0003881.npy) |
| 3882 | `model.layers.0.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.0 / 49.0 / -0.038557544350624084 / 5.29419210418564 | [NPY](tensors/0003882.npy) |
| 3883 | `model.layers.0.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.875 / 14.1875 / 0.005499152032037576 / 0.820284290275701 | [NPY](tensors/0003883.npy) |
| 3884 | `model.layers.0.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.625 / 5.125 / -0.026101887226104736 / 1.3921279475288024 | [NPY](tensors/0003884.npy) |
| 3885 | `model.layers.0.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.53125 / 3.40625 / -0.014514702031647175 / 0.4216487892428484 | [NPY](tensors/0003885.npy) |
| 3886 | `model.layers.0.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.25 / 43.0 / 0.02692124851875835 / 1.3210579355694438 | [NPY](tensors/0003886.npy) |
| 3887 | `model.layers.0.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.25 / 43.0 / 0.02692124851875835 / 1.3210579355694438 | [NPY](tensors/0003887.npy) |
| 3888 | `model.layers.0.self_attn` | 33 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9765625 / 0.0022427561092705993 / 0.02746230331678568 | [NPY](tensors/0003888.npy) |
| 3889 | `model.layers.0.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 46.75 / 0.06820267041524251 / 2.947783645894801 | [NPY](tensors/0003889.npy) |
| 3890 | `model.layers.0.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.53125 / 2.5625 / 0.006545358565118578 / 0.3587747217131225 | [NPY](tensors/0003890.npy) |
| 3891 | `model.layers.0.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.53125 / 2.5625 / 0.006545358565118578 / 0.3587747217131225 | [NPY](tensors/0003891.npy) |
| 3892 | `model.layers.0.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.53125 / 2.5625 / 0.006545358565118578 / 0.3587747217131225 | [NPY](tensors/0003892.npy) |
| 3893 | `model.layers.0.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3894 | `model.layers.0.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3895 | `model.layers.0.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3896 | `model.layers.0.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -15.6875 / 17.375 / 0.014150844514369964 / 0.632285798617605 | [NPY](tensors/0003896.npy) |
| 3897 | `model.layers.0.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.6875 / 17.375 / 0.014150844514369964 / 0.632285798617605 | [NPY](tensors/0003897.npy) |
| 3898 | `model.layers.0.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.734375 / 1.9453125 / -0.1920013427734375 / 0.8235998020370868 | [NPY](tensors/0003898.npy) |
| 3899 | `model.layers.0` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -60.25 / 61.5 / 0.08235180642869737 / 3.3516141263422496 | [NPY](tensors/0003899.npy) |
| 3978 | `model.layers.0` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 36.5 / 0.003960044019752079 / 2.604051180596326 | [NPY](tensors/0003978.npy) |
| 3979 | `model.layers.0` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003979.npy) |
| 3980 | `model.layers.0` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.439208984375 / 1.0785913702628929 | [NPY](tensors/0003980.npy) |
| 3981 | `model.layers.0` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.15223175287246704 / 0.6555427416634236 | [NPY](tensors/0003981.npy) |
| 3982 | `model.layers.0` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 906.0 / 906.0 / 906.0 / 0.0 | [NPY](tensors/0003982.npy) |
| 3983 | `model.layers.0` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3984 | `model.layers.0` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3985 | `model.layers.0` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3986 | `model.layers.0.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 36.5 / 0.003960044019752079 / 2.604051180596326 | [NPY](tensors/0003986.npy) |
| 3987 | `model.layers.0.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0003987.npy) |
| 3988 | `model.layers.0.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0003988.npy) |
| 3989 | `model.layers.0.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003989.npy) |
| 3990 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 906.0 / 906.0 / 906.0 / 0.0 | [NPY](tensors/0003990.npy) |
| 3991 | `model.layers.0.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3992 | `model.layers.0.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3993 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.439208984375 / 1.0785913702628929 | [NPY](tensors/0003993.npy) |
| 3994 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.15223175287246704 / 0.6555427416634236 | [NPY](tensors/0003994.npy) |
| 3995 | `model.layers.0.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3996 | `model.layers.0.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0003996.npy) |
| 3997 | `model.layers.0.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.875 / 0.01883023022674024 / 0.9918892179158483 | [NPY](tensors/0003997.npy) |
| 3998 | `model.layers.0.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0003998.npy) |
| 3999 | `model.layers.0.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -59.0 / 65.0 / 0.14313117787241936 / 6.505845010629575 | [NPY](tensors/0003999.npy) |
| 4000 | `model.layers.0.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0004000.npy) |
| 4001 | `model.layers.0.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.234375 / 2.921875 / 0.04315391927957535 / 0.7946671204576984 | [NPY](tensors/0004001.npy) |
| 4002 | `model.layers.0.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.671875 / 4.15625 / -0.008428503914728935 / 0.403362438776759 | [NPY](tensors/0004002.npy) |
| 4003 | `model.layers.0.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.5 / 35.25 / 0.031192021247827346 / 1.0438808710073424 | [NPY](tensors/0004003.npy) |
| 4004 | `model.layers.0.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.5 / 35.25 / 0.031192021247827346 / 1.0438808710073424 | [NPY](tensors/0004004.npy) |
| 4005 | `model.layers.0.self_attn` | 34 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0024913209083171897 / 0.026032532328224816 | [NPY](tensors/0004005.npy) |
| 4006 | `model.layers.0.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 36.75 / 0.03513379626803928 / 2.666848790238079 | [NPY](tensors/0004006.npy) |
| 4007 | `model.layers.0.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.015625 / 2.0 / 0.0036063366466098363 / 0.31990370966500525 | [NPY](tensors/0004007.npy) |
| 4008 | `model.layers.0.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.015625 / 2.0 / 0.0036063366466098363 / 0.31990370966500525 | [NPY](tensors/0004008.npy) |
| 4009 | `model.layers.0.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.015625 / 2.0 / 0.0036063366466098363 / 0.31990370966500525 | [NPY](tensors/0004009.npy) |
| 4010 | `model.layers.0.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4011 | `model.layers.0.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4012 | `model.layers.0.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4013 | `model.layers.0.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -11.25 / 19.0 / 0.0011364501176608934 / 0.6077592486937203 | [NPY](tensors/0004013.npy) |
| 4014 | `model.layers.0.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.25 / 19.0 / 0.0011364501176608934 / 0.6077592486937203 | [NPY](tensors/0004014.npy) |
| 4015 | `model.layers.0.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.75 / 2.28125 / -0.0200653076171875 / 1.553221626650155 | [NPY](tensors/0004015.npy) |
| 4016 | `model.layers.0` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.0 / 48.0 / 0.03622698254055447 / 2.7627741840792934 | [NPY](tensors/0004016.npy) |
| 4095 | `model.layers.0` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 39.0 / -0.019793536389867465 / 2.4892031664441374 | [NPY](tensors/0004095.npy) |
| 4096 | `model.layers.0` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004096.npy) |
| 4097 | `model.layers.0` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.369232177734375 / 1.1234051302987014 | [NPY](tensors/0004097.npy) |
| 4098 | `model.layers.0` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.328125 / 0.08310973644256592 / 0.636302055198959 | [NPY](tensors/0004098.npy) |
| 4099 | `model.layers.0` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 907.0 / 907.0 / 907.0 / 0.0 | [NPY](tensors/0004099.npy) |
| 4100 | `model.layers.0` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4101 | `model.layers.0` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4102 | `model.layers.0` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4103 | `model.layers.0.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 39.0 / -0.019793536389867465 / 2.4892031664441374 | [NPY](tensors/0004103.npy) |
| 4104 | `model.layers.0.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 11.6875 / -0.007737105505334007 / 0.7564929212212741 | [NPY](tensors/0004104.npy) |
| 4105 | `model.layers.0.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 11.6875 / -0.007737105505334007 / 0.7564929212212741 | [NPY](tensors/0004105.npy) |
| 4106 | `model.layers.0.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004106.npy) |
| 4107 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 907.0 / 907.0 / 907.0 / 0.0 | [NPY](tensors/0004107.npy) |
| 4108 | `model.layers.0.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4109 | `model.layers.0.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4110 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.369232177734375 / 1.1234051302987014 | [NPY](tensors/0004110.npy) |
| 4111 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.328125 / 0.08310973644256592 / 0.636302055198959 | [NPY](tensors/0004111.npy) |
| 4112 | `model.layers.0.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4113 | `model.layers.0.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 11.6875 / -0.007737105505334007 / 0.7564929212212741 | [NPY](tensors/0004113.npy) |
| 4114 | `model.layers.0.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.03125 / 7.0 / 0.023411387592204846 / 1.053285270001146 | [NPY](tensors/0004114.npy) |
| 4115 | `model.layers.0.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 11.6875 / -0.007737105505334007 / 0.7564929212212741 | [NPY](tensors/0004115.npy) |
| 4116 | `model.layers.0.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.5 / 54.25 / 0.14884635526686907 / 5.808985777834576 | [NPY](tensors/0004116.npy) |
| 4117 | `model.layers.0.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 11.6875 / -0.007737105505334007 / 0.7564929212212741 | [NPY](tensors/0004117.npy) |
| 4118 | `model.layers.0.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 3.90625 / 0.05080173909664154 / 1.1914257309385323 | [NPY](tensors/0004118.npy) |
| 4119 | `model.layers.0.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.375 / 3.375 / 0.004145333158703579 / 0.4182917112118797 | [NPY](tensors/0004119.npy) |
| 4120 | `model.layers.0.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.0 / 35.5 / 0.03077384800546699 / 1.0228953222787036 | [NPY](tensors/0004120.npy) |
| 4121 | `model.layers.0.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.0 / 35.5 / 0.03077384800546699 / 1.0228953222787036 | [NPY](tensors/0004121.npy) |
| 4122 | `model.layers.0.self_attn` | 35 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003180396323055825 / 0.033221079712352046 | [NPY](tensors/0004122.npy) |
| 4123 | `model.layers.0.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 38.75 / 0.011017391416761611 / 2.684147638691147 | [NPY](tensors/0004123.npy) |
| 4124 | `model.layers.0.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7890625 / 1.9609375 / 0.0030846955047713386 / 0.3404206462384704 | [NPY](tensors/0004124.npy) |
| 4125 | `model.layers.0.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7890625 / 1.9609375 / 0.0030846955047713386 / 0.3404206462384704 | [NPY](tensors/0004125.npy) |
| 4126 | `model.layers.0.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.7890625 / 1.9609375 / 0.0030846955047713386 / 0.3404206462384704 | [NPY](tensors/0004126.npy) |
| 4127 | `model.layers.0.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4128 | `model.layers.0.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4129 | `model.layers.0.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4130 | `model.layers.0.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.90625 / 34.0 / 0.03122271630499098 / 1.0121621977815152 | [NPY](tensors/0004130.npy) |
| 4131 | `model.layers.0.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.90625 / 34.0 / 0.03122271630499098 / 1.0121621977815152 | [NPY](tensors/0004131.npy) |
| 4132 | `model.layers.0.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.859375 / 1.3203125 / -0.12226486206054688 / 0.7984327873812312 | [NPY](tensors/0004132.npy) |
| 4133 | `model.layers.0` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.0 / 63.25 / 0.04220128059387207 / 3.149754631802449 | [NPY](tensors/0004133.npy) |
| 4212 | `model.layers.0` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.125 / 35.5 / -0.09633280614184009 / 2.5879327844318345 | [NPY](tensors/0004212.npy) |
| 4213 | `model.layers.0` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004213.npy) |
| 4214 | `model.layers.0` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.353973388671875 / 1.129845910800914 | [NPY](tensors/0004214.npy) |
| 4215 | `model.layers.0` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.328125 / -0.02260303497314453 / 0.6391623929271725 | [NPY](tensors/0004215.npy) |
| 4216 | `model.layers.0` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 908.0 / 908.0 / 908.0 / 0.0 | [NPY](tensors/0004216.npy) |
| 4217 | `model.layers.0` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4218 | `model.layers.0` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4219 | `model.layers.0` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4220 | `model.layers.0.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.125 / 35.5 / -0.09633280614184009 / 2.5879327844318345 | [NPY](tensors/0004220.npy) |
| 4221 | `model.layers.0.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.875 / 8.375 / -0.026235520653426648 / 0.7260482330841009 | [NPY](tensors/0004221.npy) |
| 4222 | `model.layers.0.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.875 / 8.375 / -0.026235520653426648 / 0.7260482330841009 | [NPY](tensors/0004222.npy) |
| 4223 | `model.layers.0.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004223.npy) |
| 4224 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 908.0 / 908.0 / 908.0 / 0.0 | [NPY](tensors/0004224.npy) |
| 4225 | `model.layers.0.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4226 | `model.layers.0.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4227 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.353973388671875 / 1.129845910800914 | [NPY](tensors/0004227.npy) |
| 4228 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.328125 / -0.02260303497314453 / 0.6391623929271725 | [NPY](tensors/0004228.npy) |
| 4229 | `model.layers.0.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4230 | `model.layers.0.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.875 / 8.375 / -0.026235520653426648 / 0.7260482330841009 | [NPY](tensors/0004230.npy) |
| 4231 | `model.layers.0.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.4375 / 9.25 / 0.03883407264947891 / 1.019933731796051 | [NPY](tensors/0004231.npy) |
| 4232 | `model.layers.0.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.875 / 8.375 / -0.026235520653426648 / 0.7260482330841009 | [NPY](tensors/0004232.npy) |
| 4233 | `model.layers.0.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.0 / 52.0 / 0.09645916521549225 / 5.762592914893347 | [NPY](tensors/0004233.npy) |
| 4234 | `model.layers.0.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.875 / 8.375 / -0.026235520653426648 / 0.7260482330841009 | [NPY](tensors/0004234.npy) |
| 4235 | `model.layers.0.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.0625 / 6.3125 / -0.004870682954788208 / 1.3634316940517819 | [NPY](tensors/0004235.npy) |
| 4236 | `model.layers.0.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.28125 / 3.890625 / 0.007105816766852513 / 0.44769159347308457 | [NPY](tensors/0004236.npy) |
| 4237 | `model.layers.0.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.75 / 38.75 / 0.035334214195609094 / 1.138608126256658 | [NPY](tensors/0004237.npy) |
| 4238 | `model.layers.0.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.75 / 38.75 / 0.035334214195609094 / 1.138608126256658 | [NPY](tensors/0004238.npy) |
| 4239 | `model.layers.0.self_attn` | 36 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0030397334318348693 / 0.029693856167505833 | [NPY](tensors/0004239.npy) |
| 4240 | `model.layers.0.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.25 / 37.5 / -0.060985602272881405 / 2.8583789975520144 | [NPY](tensors/0004240.npy) |
| 4241 | `model.layers.0.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.265625 / 1.7578125 / 0.00024464130401611326 / 0.32386820185808596 | [NPY](tensors/0004241.npy) |
| 4242 | `model.layers.0.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.265625 / 1.7578125 / 0.00024464130401611326 / 0.32386820185808596 | [NPY](tensors/0004242.npy) |
| 4243 | `model.layers.0.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.265625 / 1.7578125 / 0.00024464130401611326 / 0.32386820185808596 | [NPY](tensors/0004243.npy) |
| 4244 | `model.layers.0.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4245 | `model.layers.0.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4246 | `model.layers.0.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4247 | `model.layers.0.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.1875 / 14.6875 / 0.005338884890079498 / 0.5584263947777517 | [NPY](tensors/0004247.npy) |
| 4248 | `model.layers.0.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.1875 / 14.6875 / 0.005338884890079498 / 0.5584263947777517 | [NPY](tensors/0004248.npy) |
| 4249 | `model.layers.0.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6875 / 1.453125 / -0.10926055908203125 / 0.7302214131959701 | [NPY](tensors/0004249.npy) |
| 4250 | `model.layers.0` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.625 / 52.25 / -0.05560810301038954 / 3.1012681556062542 | [NPY](tensors/0004250.npy) |
| 4329 | `model.layers.0` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.25 / 47.5 / -0.07714509665966034 / 2.8903843139436933 | [NPY](tensors/0004329.npy) |
| 4330 | `model.layers.0` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004330.npy) |
| 4331 | `model.layers.0` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.40557861328125 / 1.0657613414649296 | [NPY](tensors/0004331.npy) |
| 4332 | `model.layers.0` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.2734375 / -0.11394071578979492 / 0.7046058830066726 | [NPY](tensors/0004332.npy) |
| 4333 | `model.layers.0` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 909.0 / 909.0 / 909.0 / 0.0 | [NPY](tensors/0004333.npy) |
| 4334 | `model.layers.0` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4335 | `model.layers.0` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4336 | `model.layers.0` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4337 | `model.layers.0.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.25 / 47.5 / -0.07714509665966034 / 2.8903843139436933 | [NPY](tensors/0004337.npy) |
| 4338 | `model.layers.0.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.8125 / 11.625 / -0.019445320632722644 / 0.7548993498126012 | [NPY](tensors/0004338.npy) |
| 4339 | `model.layers.0.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.8125 / 11.625 / -0.019445320632722644 / 0.7548993498126012 | [NPY](tensors/0004339.npy) |
| 4340 | `model.layers.0.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004340.npy) |
| 4341 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 909.0 / 909.0 / 909.0 / 0.0 | [NPY](tensors/0004341.npy) |
| 4342 | `model.layers.0.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4343 | `model.layers.0.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4344 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.40557861328125 / 1.0657613414649296 | [NPY](tensors/0004344.npy) |
| 4345 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.2734375 / -0.11394071578979492 / 0.7046058830066726 | [NPY](tensors/0004345.npy) |
| 4346 | `model.layers.0.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4347 | `model.layers.0.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.8125 / 11.625 / -0.019445320632722644 / 0.7548993498126012 | [NPY](tensors/0004347.npy) |
| 4348 | `model.layers.0.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.09375 / 8.5625 / 0.007327124010771513 / 0.9674108364103003 | [NPY](tensors/0004348.npy) |
| 4349 | `model.layers.0.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.8125 / 11.625 / -0.019445320632722644 / 0.7548993498126012 | [NPY](tensors/0004349.npy) |
| 4350 | `model.layers.0.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -46.75 / 51.75 / -0.08909627050161362 / 5.483739429517544 | [NPY](tensors/0004350.npy) |
| 4351 | `model.layers.0.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.8125 / 11.625 / -0.019445320632722644 / 0.7548993498126012 | [NPY](tensors/0004351.npy) |
| 4352 | `model.layers.0.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.40625 / 5.3125 / -0.06997242569923401 / 1.277362917731272 | [NPY](tensors/0004352.npy) |
| 4353 | `model.layers.0.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.375 / 5.0 / -0.019492633807203674 / 0.5277973097964647 | [NPY](tensors/0004353.npy) |
| 4354 | `model.layers.0.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.375 / 48.25 / 0.03454327285289764 / 1.4188162514542622 | [NPY](tensors/0004354.npy) |
| 4355 | `model.layers.0.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.375 / 48.25 / 0.03454327285289764 / 1.4188162514542622 | [NPY](tensors/0004355.npy) |
| 4356 | `model.layers.0.self_attn` | 37 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.0026200943744792917 / 0.03142512726201433 | [NPY](tensors/0004356.npy) |
| 4357 | `model.layers.0.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 48.0 / -0.042746718724568686 / 3.303609004921987 | [NPY](tensors/0004357.npy) |
| 4358 | `model.layers.0.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.453125 / 2.15625 / 0.0012868477238549127 / 0.31677262064270034 | [NPY](tensors/0004358.npy) |
| 4359 | `model.layers.0.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.453125 / 2.15625 / 0.0012868477238549127 / 0.31677262064270034 | [NPY](tensors/0004359.npy) |
| 4360 | `model.layers.0.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.453125 / 2.15625 / 0.0012868477238549127 / 0.31677262064270034 | [NPY](tensors/0004360.npy) |
| 4361 | `model.layers.0.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4362 | `model.layers.0.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4363 | `model.layers.0.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4364 | `model.layers.0.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -14.8125 / 16.75 / 0.002961050719022751 / 0.5774067763378284 | [NPY](tensors/0004364.npy) |
| 4365 | `model.layers.0.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.8125 / 16.75 / 0.002961050719022751 / 0.5774067763378284 | [NPY](tensors/0004365.npy) |
| 4366 | `model.layers.0.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.1875 / 1.7265625 / -0.19771194458007812 / 0.6722996323262409 | [NPY](tensors/0004366.npy) |
| 4367 | `model.layers.0` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 63.5 / -0.039763651953803165 / 3.598632266920181 | [NPY](tensors/0004367.npy) |
| 4446 | `model.layers.0` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 32.25 / 0.03891951702535153 / 3.1908127359696605 | [NPY](tensors/0004446.npy) |
| 4447 | `model.layers.0` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004447.npy) |
| 4448 | `model.layers.0` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.49200439453125 / 1.0259755074121442 | [NPY](tensors/0004448.npy) |
| 4449 | `model.layers.0` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.14840924739837646 / 0.7028633553324986 | [NPY](tensors/0004449.npy) |
| 4450 | `model.layers.0` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 910.0 / 910.0 / 910.0 / 0.0 | [NPY](tensors/0004450.npy) |
| 4451 | `model.layers.0` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4452 | `model.layers.0` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4453 | `model.layers.0` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4454 | `model.layers.0.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 32.25 / 0.03891951702535153 / 3.1908127359696605 | [NPY](tensors/0004454.npy) |
| 4455 | `model.layers.0.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.5625 / 7.15625 / 0.00408099384771453 / 0.7139321870494378 | [NPY](tensors/0004455.npy) |
| 4456 | `model.layers.0.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.5625 / 7.15625 / 0.00408099384771453 / 0.7139321870494378 | [NPY](tensors/0004456.npy) |
| 4457 | `model.layers.0.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004457.npy) |
| 4458 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 910.0 / 910.0 / 910.0 / 0.0 | [NPY](tensors/0004458.npy) |
| 4459 | `model.layers.0.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4460 | `model.layers.0.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4461 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.49200439453125 / 1.0259755074121442 | [NPY](tensors/0004461.npy) |
| 4462 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.14840924739837646 / 0.7028633553324986 | [NPY](tensors/0004462.npy) |
| 4463 | `model.layers.0.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4464 | `model.layers.0.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.5625 / 7.15625 / 0.00408099384771453 / 0.7139321870494378 | [NPY](tensors/0004464.npy) |
| 4465 | `model.layers.0.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.375 / 9.125 / 0.015682362718507648 / 0.9773017900836803 | [NPY](tensors/0004465.npy) |
| 4466 | `model.layers.0.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.5625 / 7.15625 / 0.00408099384771453 / 0.7139321870494378 | [NPY](tensors/0004466.npy) |
| 4467 | `model.layers.0.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -57.0 / 42.5 / -0.0382387638092041 / 5.721143634736198 | [NPY](tensors/0004467.npy) |
| 4468 | `model.layers.0.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.5625 / 7.15625 / 0.00408099384771453 / 0.7139321870494378 | [NPY](tensors/0004468.npy) |
| 4469 | `model.layers.0.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.6875 / 5.4375 / -0.1257996018975973 / 1.1474514874228652 | [NPY](tensors/0004469.npy) |
| 4470 | `model.layers.0.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.28125 / 4.84375 / -0.035456343277473934 / 0.7368689368840413 | [NPY](tensors/0004470.npy) |
| 4471 | `model.layers.0.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.9375 / 46.75 / 0.04477227727572123 / 1.3829620985598177 | [NPY](tensors/0004471.npy) |
| 4472 | `model.layers.0.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.9375 / 46.75 / 0.04477227727572123 / 1.3829620985598177 | [NPY](tensors/0004472.npy) |
| 4473 | `model.layers.0.self_attn` | 38 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.003992871225541427 / 0.04523392749178765 | [NPY](tensors/0004473.npy) |
| 4474 | `model.layers.0.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 46.25 / 0.08349007235633002 / 3.4786215126308226 | [NPY](tensors/0004474.npy) |
| 4475 | `model.layers.0.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6640625 / 1.5546875 / 0.0034726361433664956 / 0.30169716640775535 | [NPY](tensors/0004475.npy) |
| 4476 | `model.layers.0.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6640625 / 1.5546875 / 0.0034726361433664956 / 0.30169716640775535 | [NPY](tensors/0004476.npy) |
| 4477 | `model.layers.0.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.6640625 / 1.5546875 / 0.0034726361433664956 / 0.30169716640775535 | [NPY](tensors/0004477.npy) |
| 4478 | `model.layers.0.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4479 | `model.layers.0.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4480 | `model.layers.0.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4481 | `model.layers.0.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.0 / 21.375 / 0.015548404388957554 / 0.6974436188256702 | [NPY](tensors/0004481.npy) |
| 4482 | `model.layers.0.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.0 / 21.375 / 0.015548404388957554 / 0.6974436188256702 | [NPY](tensors/0004482.npy) |
| 4483 | `model.layers.0.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.875 / 1.5625 / -0.14019775390625 / 0.7666061255446776 | [NPY](tensors/0004483.npy) |
| 4484 | `model.layers.0` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 67.5 / 0.09896310700310601 / 3.671928372262384 | [NPY](tensors/0004484.npy) |
| 4563 | `model.layers.0` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 52.5 / -0.011121745242012872 / 3.095289700912499 | [NPY](tensors/0004563.npy) |
| 4564 | `model.layers.0` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004564.npy) |
| 4565 | `model.layers.0` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.559814453125 / 1.0371191164410525 | [NPY](tensors/0004565.npy) |
| 4566 | `model.layers.0` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2734375 / -0.12162959575653076 / 0.636397050487149 | [NPY](tensors/0004566.npy) |
| 4567 | `model.layers.0` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 911.0 / 911.0 / 911.0 / 0.0 | [NPY](tensors/0004567.npy) |
| 4568 | `model.layers.0` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4569 | `model.layers.0` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4570 | `model.layers.0` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4571 | `model.layers.0.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 52.5 / -0.011121745242012872 / 3.095289700912499 | [NPY](tensors/0004571.npy) |
| 4572 | `model.layers.0.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 10.8125 / -0.004110789961285061 / 0.7479932475408338 | [NPY](tensors/0004572.npy) |
| 4573 | `model.layers.0.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 10.8125 / -0.004110789961285061 / 0.7479932475408338 | [NPY](tensors/0004573.npy) |
| 4574 | `model.layers.0.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004574.npy) |
| 4575 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 911.0 / 911.0 / 911.0 / 0.0 | [NPY](tensors/0004575.npy) |
| 4576 | `model.layers.0.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4577 | `model.layers.0.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4578 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.559814453125 / 1.0371191164410525 | [NPY](tensors/0004578.npy) |
| 4579 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2734375 / -0.12162959575653076 / 0.636397050487149 | [NPY](tensors/0004579.npy) |
| 4580 | `model.layers.0.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4581 | `model.layers.0.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 10.8125 / -0.004110789961285061 / 0.7479932475408338 | [NPY](tensors/0004581.npy) |
| 4582 | `model.layers.0.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.8125 / 8.5 / 0.04400912587880157 / 1.0163239082040942 | [NPY](tensors/0004582.npy) |
| 4583 | `model.layers.0.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 10.8125 / -0.004110789961285061 / 0.7479932475408338 | [NPY](tensors/0004583.npy) |
| 4584 | `model.layers.0.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.75 / 50.0 / 0.012938499450683594 / 5.066769600012738 | [NPY](tensors/0004584.npy) |
| 4585 | `model.layers.0.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 10.8125 / -0.004110789961285061 / 0.7479932475408338 | [NPY](tensors/0004585.npy) |
| 4586 | `model.layers.0.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.4375 / 4.65625 / 0.045365482568740845 / 1.10549470387518 | [NPY](tensors/0004586.npy) |
| 4587 | `model.layers.0.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.46875 / 4.53125 / -0.005079436091364187 / 0.409710827107014 | [NPY](tensors/0004587.npy) |
| 4588 | `model.layers.0.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.5625 / 39.0 / 0.029881788707441754 / 1.1212186231863 | [NPY](tensors/0004588.npy) |
| 4589 | `model.layers.0.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.5625 / 39.0 / 0.029881788707441754 / 1.1212186231863 | [NPY](tensors/0004589.npy) |
| 4590 | `model.layers.0.self_attn` | 39 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0028324645813177186 / 0.027548697293208753 | [NPY](tensors/0004590.npy) |
| 4591 | `model.layers.0.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 51.25 / 0.01865605248345269 / 3.2612979831053637 | [NPY](tensors/0004591.npy) |
| 4592 | `model.layers.0.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.796875 / 2.9375 / -0.0010439958837297227 / 0.306317542237587 | [NPY](tensors/0004592.npy) |
| 4593 | `model.layers.0.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.796875 / 2.9375 / -0.0010439958837297227 / 0.306317542237587 | [NPY](tensors/0004593.npy) |
| 4594 | `model.layers.0.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.796875 / 2.9375 / -0.0010439958837297227 / 0.306317542237587 | [NPY](tensors/0004594.npy) |
| 4595 | `model.layers.0.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4596 | `model.layers.0.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4597 | `model.layers.0.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4598 | `model.layers.0.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.0 / 20.5 / 0.025607337223158944 / 0.6975689181193593 | [NPY](tensors/0004598.npy) |
| 4599 | `model.layers.0.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 20.5 / 0.025607337223158944 / 0.6975689181193593 | [NPY](tensors/0004599.npy) |
| 4600 | `model.layers.0.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.890625 / 1.671875 / -0.10094070434570312 / 0.9004195974902686 | [NPY](tensors/0004600.npy) |
| 4601 | `model.layers.0` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 56.5 / 0.04431496196322971 / 3.402049881408715 | [NPY](tensors/0004601.npy) |
| 4680 | `model.layers.0` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.25 / 37.0 / -0.026021352079179553 / 2.4881387291719217 | [NPY](tensors/0004680.npy) |
| 4681 | `model.layers.0` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004681.npy) |
| 4682 | `model.layers.0` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.57440185546875 / 1.030810795441952 | [NPY](tensors/0004682.npy) |
| 4683 | `model.layers.0` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.2734375 / -0.07393771409988403 / 0.6426875034418209 | [NPY](tensors/0004683.npy) |
| 4684 | `model.layers.0` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 912.0 / 912.0 / 912.0 / 0.0 | [NPY](tensors/0004684.npy) |
| 4685 | `model.layers.0` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4686 | `model.layers.0` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4687 | `model.layers.0` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4688 | `model.layers.0.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.25 / 37.0 / -0.026021352079179553 / 2.4881387291719217 | [NPY](tensors/0004688.npy) |
| 4689 | `model.layers.0.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.625 / 9.6875 / -0.01011135114563836 / 0.7502637058228022 | [NPY](tensors/0004689.npy) |
| 4690 | `model.layers.0.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.625 / 9.6875 / -0.01011135114563836 / 0.7502637058228022 | [NPY](tensors/0004690.npy) |
| 4691 | `model.layers.0.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004691.npy) |
| 4692 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 912.0 / 912.0 / 912.0 / 0.0 | [NPY](tensors/0004692.npy) |
| 4693 | `model.layers.0.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4694 | `model.layers.0.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4695 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.57440185546875 / 1.030810795441952 | [NPY](tensors/0004695.npy) |
| 4696 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.2734375 / -0.07393771409988403 / 0.6426875034418209 | [NPY](tensors/0004696.npy) |
| 4697 | `model.layers.0.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4698 | `model.layers.0.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.625 / 9.6875 / -0.01011135114563836 / 0.7502637058228022 | [NPY](tensors/0004698.npy) |
| 4699 | `model.layers.0.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.21875 / 9.1875 / 0.05721920728683472 / 1.0037615553598511 | [NPY](tensors/0004699.npy) |
| 4700 | `model.layers.0.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.625 / 9.6875 / -0.01011135114563836 / 0.7502637058228022 | [NPY](tensors/0004700.npy) |
| 4701 | `model.layers.0.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -47.25 / 51.5 / 0.04976591467857361 / 5.593182258907738 | [NPY](tensors/0004701.npy) |
| 4702 | `model.layers.0.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.625 / 9.6875 / -0.01011135114563836 / 0.7502637058228022 | [NPY](tensors/0004702.npy) |
| 4703 | `model.layers.0.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.0625 / 4.5 / 0.0262528657913208 / 1.1684869096101989 | [NPY](tensors/0004703.npy) |
| 4704 | `model.layers.0.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.5 / 4.53125 / -0.0003889738509315066 / 0.5210137099885213 | [NPY](tensors/0004704.npy) |
| 4705 | `model.layers.0.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 43.75 / 0.0379818222588963 / 1.227210507601082 | [NPY](tensors/0004705.npy) |
| 4706 | `model.layers.0.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 43.75 / 0.0379818222588963 / 1.227210507601082 | [NPY](tensors/0004706.npy) |
| 4707 | `model.layers.0.self_attn` | 40 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0032561174164400003 / 0.033295736885802875 | [NPY](tensors/0004707.npy) |
| 4708 | `model.layers.0.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.75 / 39.0 / 0.011992571089002821 / 2.7490291139690304 | [NPY](tensors/0004708.npy) |
| 4709 | `model.layers.0.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.140625 / 2.78125 / -0.0013479073842366537 / 0.30020582743832597 | [NPY](tensors/0004709.npy) |
| 4710 | `model.layers.0.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.140625 / 2.78125 / -0.0013479073842366537 / 0.30020582743832597 | [NPY](tensors/0004710.npy) |
| 4711 | `model.layers.0.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.140625 / 2.78125 / -0.0013479073842366537 / 0.30020582743832597 | [NPY](tensors/0004711.npy) |
| 4712 | `model.layers.0.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4713 | `model.layers.0.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4714 | `model.layers.0.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4715 | `model.layers.0.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.78125 / 12.8125 / 0.01234813125597106 / 0.47824047420944804 | [NPY](tensors/0004715.npy) |
| 4716 | `model.layers.0.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.78125 / 12.8125 / 0.01234813125597106 / 0.47824047420944804 | [NPY](tensors/0004716.npy) |
| 4717 | `model.layers.0.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.65625 / 1.609375 / -0.10147857666015625 / 0.9613685738312536 | [NPY](tensors/0004717.npy) |
| 4718 | `model.layers.0` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.125 / 48.75 / 0.024459271960788304 / 2.820534996424231 | [NPY](tensors/0004718.npy) |
| 4797 | `model.layers.0` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 27.0 / 0.003733634617593553 / 2.804623802992795 | [NPY](tensors/0004797.npy) |
| 4798 | `model.layers.0` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004798.npy) |
| 4799 | `model.layers.0` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.5457305908203125 / 1.0267502307475864 | [NPY](tensors/0004799.npy) |
| 4800 | `model.layers.0` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.051917850971221924 / 0.6740142912053045 | [NPY](tensors/0004800.npy) |
| 4801 | `model.layers.0` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 913.0 / 913.0 / 913.0 / 0.0 | [NPY](tensors/0004801.npy) |
| 4802 | `model.layers.0` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4803 | `model.layers.0` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4804 | `model.layers.0` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4805 | `model.layers.0.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 27.0 / 0.003733634617593553 / 2.804623802992795 | [NPY](tensors/0004805.npy) |
| 4806 | `model.layers.0.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0004806.npy) |
| 4807 | `model.layers.0.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0004807.npy) |
| 4808 | `model.layers.0.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004808.npy) |
| 4809 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 913.0 / 913.0 / 913.0 / 0.0 | [NPY](tensors/0004809.npy) |
| 4810 | `model.layers.0.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4811 | `model.layers.0.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4812 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.5457305908203125 / 1.0267502307475864 | [NPY](tensors/0004812.npy) |
| 4813 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.051917850971221924 / 0.6740142912053045 | [NPY](tensors/0004813.npy) |
| 4814 | `model.layers.0.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4815 | `model.layers.0.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0004815.npy) |
| 4816 | `model.layers.0.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.875 / 10.625 / 0.036541547160595655 / 1.020216334584807 | [NPY](tensors/0004816.npy) |
| 4817 | `model.layers.0.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0004817.npy) |
| 4818 | `model.layers.0.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.0 / 61.0 / 0.009755432605743408 / 5.9442685357666845 | [NPY](tensors/0004818.npy) |
| 4819 | `model.layers.0.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0004819.npy) |
| 4820 | `model.layers.0.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.65625 / 5.65625 / -0.0710136890411377 / 1.3093894403473694 | [NPY](tensors/0004820.npy) |
| 4821 | `model.layers.0.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.5625 / 4.5 / -0.01018762428429909 / 0.5467852539825775 | [NPY](tensors/0004821.npy) |
| 4822 | `model.layers.0.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.625 / 41.75 / 0.03913611074288686 / 1.2316655177895723 | [NPY](tensors/0004822.npy) |
| 4823 | `model.layers.0.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.625 / 41.75 / 0.03913611074288686 / 1.2316655177895723 | [NPY](tensors/0004823.npy) |
| 4824 | `model.layers.0.self_attn` | 41 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0028557844960643937 / 0.03286345799189787 | [NPY](tensors/0004824.npy) |
| 4825 | `model.layers.0.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.5 / 45.25 / 0.042630269792344834 / 3.114187745878422 | [NPY](tensors/0004825.npy) |
| 4826 | `model.layers.0.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9375 / 1.7421875 / 0.001986106899049547 / 0.3220897044427732 | [NPY](tensors/0004826.npy) |
| 4827 | `model.layers.0.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9375 / 1.7421875 / 0.001986106899049547 / 0.3220897044427732 | [NPY](tensors/0004827.npy) |
| 4828 | `model.layers.0.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.9375 / 1.7421875 / 0.001986106899049547 / 0.3220897044427732 | [NPY](tensors/0004828.npy) |
| 4829 | `model.layers.0.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4830 | `model.layers.0.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4831 | `model.layers.0.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4832 | `model.layers.0.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.5625 / 16.0 / 0.02115236504210366 / 0.7301081641414566 | [NPY](tensors/0004832.npy) |
| 4833 | `model.layers.0.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 16.0 / 0.02115236504210366 / 0.7301081641414566 | [NPY](tensors/0004833.npy) |
| 4834 | `model.layers.0.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.515625 / 1.484375 / -0.16803646087646484 / 0.6566296094787956 | [NPY](tensors/0004834.npy) |
| 4835 | `model.layers.0` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 61.25 / 0.06383644739786784 / 3.388805192728557 | [NPY](tensors/0004835.npy) |
| 4914 | `model.layers.0` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0004914.npy) |
| 4915 | `model.layers.0` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004915.npy) |
| 4916 | `model.layers.0` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.513641357421875 / 1.0381515204992577 | [NPY](tensors/0004916.npy) |
| 4917 | `model.layers.0` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / -0.07546013593673706 / 0.6806294351122038 | [NPY](tensors/0004917.npy) |
| 4918 | `model.layers.0` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 914.0 / 914.0 / 914.0 / 0.0 | [NPY](tensors/0004918.npy) |
| 4919 | `model.layers.0` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4920 | `model.layers.0` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4921 | `model.layers.0` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4922 | `model.layers.0.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0004922.npy) |
| 4923 | `model.layers.0.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0004923.npy) |
| 4924 | `model.layers.0.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0004924.npy) |
| 4925 | `model.layers.0.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004925.npy) |
| 4926 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 914.0 / 914.0 / 914.0 / 0.0 | [NPY](tensors/0004926.npy) |
| 4927 | `model.layers.0.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4928 | `model.layers.0.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4929 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.513641357421875 / 1.0381515204992577 | [NPY](tensors/0004929.npy) |
| 4930 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / -0.07546013593673706 / 0.6806294351122038 | [NPY](tensors/0004930.npy) |
| 4931 | `model.layers.0.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4932 | `model.layers.0.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0004932.npy) |
| 4933 | `model.layers.0.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.84375 / 8.5625 / 0.0153301190584898 / 1.0113524420299036 | [NPY](tensors/0004933.npy) |
| 4934 | `model.layers.0.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0004934.npy) |
| 4935 | `model.layers.0.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.0 / 65.5 / 0.032654017210006714 / 6.89507515667232 | [NPY](tensors/0004935.npy) |
| 4936 | `model.layers.0.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0004936.npy) |
| 4937 | `model.layers.0.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.28125 / 3.390625 / -0.002120666205883026 / 0.8566653376613583 | [NPY](tensors/0004937.npy) |
| 4938 | `model.layers.0.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.484375 / 4.46875 / -0.005091208786325296 / 0.43228221027199953 | [NPY](tensors/0004938.npy) |
| 4939 | `model.layers.0.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.9375 / 30.125 / 0.026712401542398664 / 0.9718866507112647 | [NPY](tensors/0004939.npy) |
| 4940 | `model.layers.0.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.9375 / 30.125 / 0.026712401542398664 / 0.9718866507112647 | [NPY](tensors/0004940.npy) |
| 4941 | `model.layers.0.self_attn` | 42 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0029311764856047627 / 0.026697255278798692 | [NPY](tensors/0004941.npy) |
| 4942 | `model.layers.0.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 33.5 / 0.024779452217949763 / 3.03896263510034 | [NPY](tensors/0004942.npy) |
| 4943 | `model.layers.0.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5234375 / 1.4453125 / 0.00044419434335496693 / 0.2810497542550462 | [NPY](tensors/0004943.npy) |
| 4944 | `model.layers.0.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5234375 / 1.4453125 / 0.00044419434335496693 / 0.2810497542550462 | [NPY](tensors/0004944.npy) |
| 4945 | `model.layers.0.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.5234375 / 1.4453125 / 0.00044419434335496693 / 0.2810497542550462 | [NPY](tensors/0004945.npy) |
| 4946 | `model.layers.0.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4947 | `model.layers.0.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4948 | `model.layers.0.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4949 | `model.layers.0.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.84375 / 18.5 / 0.014009021346767743 / 0.7019944920787771 | [NPY](tensors/0004949.npy) |
| 4950 | `model.layers.0.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.84375 / 18.5 / 0.014009021346767743 / 0.7019944920787771 | [NPY](tensors/0004950.npy) |
| 4951 | `model.layers.0.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.03125 / 2.984375 / -0.012409210205078125 / 1.47269945770891 | [NPY](tensors/0004951.npy) |
| 4952 | `model.layers.0` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 52.0 / 0.038666240374247235 / 3.050762206210799 | [NPY](tensors/0004952.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -41728.0 / 1104.0 / 0.42928332041977957 / 33.3831507741731 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 873, 873] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6928243822607898e+38 / 1.694764582762651e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 873, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7211662215764238 / 0.9199891152809843 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 873, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10053101652705901 / 0.6581213818663489 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 873] | torch.int64 → int64 | 0.0 / 872.0 / 436.0 / 252.01322716608877 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -41728.0 / 1104.0 / 0.42928332041977957 / 33.3831507741731 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 873, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.058601893171520106 / 3.077403387905317 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 873, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.058601893171520106 / 3.077403387905317 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 873, 873] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6928243822607898e+38 / 1.694764582762651e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 873] | torch.int64 → int64 | 0.0 / 872.0 / 436.0 / 252.01322716608877 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 873, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7211662215764238 / 0.9199891152809843 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 873, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10053101652705901 / 0.6581213818663489 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.058601893171520106 / 3.077403387905317 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 873, 4096] | torch.bfloat16 → float32 | -12.9375 / 15.6875 / 0.042367260708531945 / 1.371715749360324 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.058601893171520106 / 3.077403387905317 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 873, 512] | torch.bfloat16 → float32 | -49.25 / 55.5 / 0.0845597972712007 / 3.790238940194716 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.058601893171520106 / 3.077403387905317 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 873, 512] | torch.bfloat16 → float32 | -16.0 / 22.125 / -0.024835241928228304 / 2.494859917496933 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 873, 4096] | torch.bfloat16 → float32 | -11.75 / 13.0 / -0.02054826945015701 / 1.4598937060242296 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 873, 2880] | torch.bfloat16 → float32 | -486.0 / 440.0 / -0.0004636429806402397 / 5.217480420937494 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -486.0 / 440.0 / -0.0004636429806402397 / 5.217480420937494 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 873, 873] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0010090508860229389 / 0.009389385069389354 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -41728.0 / 656.0 / 0.42879576534962127 / 33.37204447673636 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 873, 2880] | torch.bfloat16 → float32 | -78.5 / 6.46875 / 0.00848326496305782 / 0.7401131230850189 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -78.5 / 6.46875 / 0.00848326496305782 / 0.7401131230850189 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [873, 2880] | torch.bfloat16 → float32 | -78.5 / 6.46875 / 0.00848326496305782 / 0.7401131230850189 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [873, 2880] | torch.bfloat16 → float32 | -414.0 / 408.0 / 0.080096931825146 / 7.325806461018334 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -414.0 / 408.0 / 0.080096931825146 / 7.325806461018334 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [873, 32] | torch.bfloat16 → float32 | -10.75 / 2.953125 / -0.13263464301722155 / 0.6531957298095841 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 873, 2880] | torch.bfloat16 → float32 | -41728.0 / 880.0 / 0.508897447385784 / 36.06230319659963 | [NPY](tensors/0000077.npy) |
| 156 | `model.layers.11` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -119.5 / 241.0 / 0.6496384514702691 / 15.934217238379428 | [NPY](tensors/0000156.npy) |
| 157 | `model.layers.11` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 874] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000157.npy) |
| 158 | `model.layers.11` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.649322509765625 / 0.9833264324529841 | [NPY](tensors/0000158.npy) |
| 159 | `model.layers.11` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.024361848831176758 / 0.6489880782497579 | [NPY](tensors/0000159.npy) |
| 160 | `model.layers.11` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 873.0 / 873.0 / 873.0 / 0.0 | [NPY](tensors/0000160.npy) |
| 161 | `model.layers.11` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 162 | `model.layers.11` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 163 | `model.layers.11` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 164 | `model.layers.11.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -119.5 / 241.0 / 0.6496384514702691 / 15.934217238379428 | [NPY](tensors/0000164.npy) |
| 165 | `model.layers.11.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 71.0 / 0.09902822441524929 / 2.5121795790011574 | [NPY](tensors/0000165.npy) |
| 166 | `model.layers.11.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 71.0 / 0.09902822441524929 / 2.5121795790011574 | [NPY](tensors/0000166.npy) |
| 167 | `model.layers.11.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 874] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000167.npy) |
| 168 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 873.0 / 873.0 / 873.0 / 0.0 | [NPY](tensors/0000168.npy) |
| 169 | `model.layers.11.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 170 | `model.layers.11.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 171 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.649322509765625 / 0.9833264324529841 | [NPY](tensors/0000171.npy) |
| 172 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.024361848831176758 / 0.6489880782497579 | [NPY](tensors/0000172.npy) |
| 173 | `model.layers.11.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 174 | `model.layers.11.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 71.0 / 0.09902822441524929 / 2.5121795790011574 | [NPY](tensors/0000174.npy) |
| 175 | `model.layers.11.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.125 / 9.8125 / 0.06046980479732156 / 1.5100104471789015 | [NPY](tensors/0000175.npy) |
| 176 | `model.layers.11.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 71.0 / 0.09902822441524929 / 2.5121795790011574 | [NPY](tensors/0000176.npy) |
| 177 | `model.layers.11.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.25 / 39.75 / 0.2125583291053772 / 4.8660701781725 | [NPY](tensors/0000177.npy) |
| 178 | `model.layers.11.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 71.0 / 0.09902822441524929 / 2.5121795790011574 | [NPY](tensors/0000178.npy) |
| 179 | `model.layers.11.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -11.4375 / 11.0625 / -0.11766000837087631 / 2.9541212440461955 | [NPY](tensors/0000179.npy) |
| 180 | `model.layers.11.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.84375 / 8.6875 / -0.07342365151271224 / 1.6902123229432857 | [NPY](tensors/0000180.npy) |
| 181 | `model.layers.11.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.0 / 139.0 / 0.0160420470767551 / 5.040338389261714 | [NPY](tensors/0000181.npy) |
| 182 | `model.layers.11.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.0 / 139.0 / 0.0160420470767551 / 5.040338389261714 | [NPY](tensors/0000182.npy) |
| 183 | `model.layers.11.self_attn` | 1 | `output[1]` | [1, 64, 1, 874] | torch.bfloat16 → float32 | 2.5579538487363607e-13 / 0.796875 / 0.0010911602299643933 / 0.006946245864238602 | [NPY](tensors/0000183.npy) |
| 184 | `model.layers.11.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -180.0 / 336.0 / 0.6652618408203125 / 18.80507032826922 | [NPY](tensors/0000184.npy) |
| 185 | `model.layers.11.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.421875 / 4.125 / 0.01552208529578315 / 0.7592862789607963 | [NPY](tensors/0000185.npy) |
| 186 | `model.layers.11.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.421875 / 4.125 / 0.01552208529578315 / 0.7592862789607963 | [NPY](tensors/0000186.npy) |
| 187 | `model.layers.11.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.421875 / 4.125 / 0.01552208529578315 / 0.7592862789607963 | [NPY](tensors/0000187.npy) |
| 188 | `model.layers.11.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 189 | `model.layers.11.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 190 | `model.layers.11.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 191 | `model.layers.11.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -63.5 / 119.0 / 0.2393434206644694 / 6.292319243353432 | [NPY](tensors/0000191.npy) |
| 192 | `model.layers.11.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.5 / 119.0 / 0.2393434206644694 / 6.292319243353432 | [NPY](tensors/0000192.npy) |
| 193 | `model.layers.11.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.1796875 / 1.4609375 / -0.08004188537597656 / 0.5576612453582692 | [NPY](tensors/0000193.npy) |
| 194 | `model.layers.11` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -244.0 / 454.0 / 0.9052446153428819 / 22.255523511710447 | [NPY](tensors/0000194.npy) |
| 273 | `model.layers.11` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -316.0 / 552.0 / 0.48155636257595485 / 23.701967945838216 | [NPY](tensors/0000273.npy) |
| 274 | `model.layers.11` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 875] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000274.npy) |
| 275 | `model.layers.11` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.663970947265625 / 0.9817896713297021 | [NPY](tensors/0000275.npy) |
| 276 | `model.layers.11` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.25 / 1.34375 / 0.07146221399307251 / 0.6328787006162191 | [NPY](tensors/0000276.npy) |
| 277 | `model.layers.11` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 874.0 / 874.0 / 874.0 / 0.0 | [NPY](tensors/0000277.npy) |
| 278 | `model.layers.11` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 279 | `model.layers.11` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 280 | `model.layers.11` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 281 | `model.layers.11.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -316.0 / 552.0 / 0.48155636257595485 / 23.701967945838216 | [NPY](tensors/0000281.npy) |
| 282 | `model.layers.11.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 109.0 / 0.059244919485516016 / 3.008688130724963 | [NPY](tensors/0000282.npy) |
| 283 | `model.layers.11.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 109.0 / 0.059244919485516016 / 3.008688130724963 | [NPY](tensors/0000283.npy) |
| 284 | `model.layers.11.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 875] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000284.npy) |
| 285 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 874.0 / 874.0 / 874.0 / 0.0 | [NPY](tensors/0000285.npy) |
| 286 | `model.layers.11.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 287 | `model.layers.11.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 288 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.663970947265625 / 0.9817896713297021 | [NPY](tensors/0000288.npy) |
| 289 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.25 / 1.34375 / 0.07146221399307251 / 0.6328787006162191 | [NPY](tensors/0000289.npy) |
| 290 | `model.layers.11.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 291 | `model.layers.11.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 109.0 / 0.059244919485516016 / 3.008688130724963 | [NPY](tensors/0000291.npy) |
| 292 | `model.layers.11.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.75 / 11.25 / 0.013075123773887753 / 1.4793877770436399 | [NPY](tensors/0000292.npy) |
| 293 | `model.layers.11.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 109.0 / 0.059244919485516016 / 3.008688130724963 | [NPY](tensors/0000293.npy) |
| 294 | `model.layers.11.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.5 / 37.5 / -0.003073960542678833 / 4.240592511732734 | [NPY](tensors/0000294.npy) |
| 295 | `model.layers.11.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 109.0 / 0.059244919485516016 / 3.008688130724963 | [NPY](tensors/0000295.npy) |
| 296 | `model.layers.11.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -10.0 / 8.375 / -0.05486401170492172 / 2.8582301831085295 | [NPY](tensors/0000296.npy) |
| 297 | `model.layers.11.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.28125 / 8.3125 / -0.004452683962881565 / 1.8169510000895543 | [NPY](tensors/0000297.npy) |
| 298 | `model.layers.11.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 107.5 / -0.0655628416273329 / 5.13445677303903 | [NPY](tensors/0000298.npy) |
| 299 | `model.layers.11.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 107.5 / -0.0655628416273329 / 5.13445677303903 | [NPY](tensors/0000299.npy) |
| 300 | `model.layers.11.self_attn` | 2 | `output[1]` | [1, 64, 1, 875] | torch.bfloat16 → float32 | 7.382983113757291e-15 / 0.96484375 / 0.001116858117724304 / 0.009121354479731903 | [NPY](tensors/0000300.npy) |
| 301 | `model.layers.11.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -358.0 / 560.0 / 0.41618338690863715 / 25.843375976647234 | [NPY](tensors/0000301.npy) |
| 302 | `model.layers.11.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.109375 / 4.125 / 0.002867037389013502 / 0.7439261449147829 | [NPY](tensors/0000302.npy) |
| 303 | `model.layers.11.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.109375 / 4.125 / 0.002867037389013502 / 0.7439261449147829 | [NPY](tensors/0000303.npy) |
| 304 | `model.layers.11.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.109375 / 4.125 / 0.002867037389013502 / 0.7439261449147829 | [NPY](tensors/0000304.npy) |
| 305 | `model.layers.11.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 306 | `model.layers.11.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 307 | `model.layers.11.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 308 | `model.layers.11.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -304.0 / 284.0 / 0.2024060328801473 / 10.197522913717181 | [NPY](tensors/0000308.npy) |
| 309 | `model.layers.11.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -304.0 / 284.0 / 0.2024060328801473 / 10.197522913717181 | [NPY](tensors/0000309.npy) |
| 310 | `model.layers.11.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.03125 / 1.0078125 / -0.09206008911132812 / 0.592668102990127 | [NPY](tensors/0000310.npy) |
| 311 | `model.layers.11` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -664.0 / 844.0 / 0.6166476779513889 / 33.039509216481285 | [NPY](tensors/0000311.npy) |
| 390 | `model.layers.11` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -210.0 / 404.0 / 0.6499394734700521 / 19.86211347337891 | [NPY](tensors/0000390.npy) |
| 391 | `model.layers.11` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 876] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000391.npy) |
| 392 | `model.layers.11` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.6338043212890625 / 0.990232497628255 | [NPY](tensors/0000392.npy) |
| 393 | `model.layers.11` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.10754281282424927 / 0.6458776678737284 | [NPY](tensors/0000393.npy) |
| 394 | `model.layers.11` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 875.0 / 875.0 / 875.0 / 0.0 | [NPY](tensors/0000394.npy) |
| 395 | `model.layers.11` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 396 | `model.layers.11` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 397 | `model.layers.11` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 398 | `model.layers.11.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -210.0 / 404.0 / 0.6499394734700521 / 19.86211347337891 | [NPY](tensors/0000398.npy) |
| 399 | `model.layers.11.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.5 / 95.5 / 0.0861247420310974 / 2.7636489086680034 | [NPY](tensors/0000399.npy) |
| 400 | `model.layers.11.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.5 / 95.5 / 0.0861247420310974 / 2.7636489086680034 | [NPY](tensors/0000400.npy) |
| 401 | `model.layers.11.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 876] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000401.npy) |
| 402 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 875.0 / 875.0 / 875.0 / 0.0 | [NPY](tensors/0000402.npy) |
| 403 | `model.layers.11.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 404 | `model.layers.11.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 405 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.6338043212890625 / 0.990232497628255 | [NPY](tensors/0000405.npy) |
| 406 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.10754281282424927 / 0.6458776678737284 | [NPY](tensors/0000406.npy) |
| 407 | `model.layers.11.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 408 | `model.layers.11.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.5 / 95.5 / 0.0861247420310974 / 2.7636489086680034 | [NPY](tensors/0000408.npy) |
| 409 | `model.layers.11.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.875 / 10.375 / 0.050757171120494604 / 1.454592828228485 | [NPY](tensors/0000409.npy) |
| 410 | `model.layers.11.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.5 / 95.5 / 0.0861247420310974 / 2.7636489086680034 | [NPY](tensors/0000410.npy) |
| 411 | `model.layers.11.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.5 / 39.75 / 0.07530185580253601 / 4.289312157247712 | [NPY](tensors/0000411.npy) |
| 412 | `model.layers.11.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.5 / 95.5 / 0.0861247420310974 / 2.7636489086680034 | [NPY](tensors/0000412.npy) |
| 413 | `model.layers.11.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -10.0 / 7.65625 / -0.05920112133026123 / 2.5642975467247973 | [NPY](tensors/0000413.npy) |
| 414 | `model.layers.11.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.65625 / 7.59375 / -0.023589730728417635 / 1.6656508770293148 | [NPY](tensors/0000414.npy) |
| 415 | `model.layers.11.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -115.5 / 127.0 / -0.05257524914211697 / 5.292306921488132 | [NPY](tensors/0000415.npy) |
| 416 | `model.layers.11.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -115.5 / 127.0 / -0.05257524914211697 / 5.292306921488132 | [NPY](tensors/0000416.npy) |
| 417 | `model.layers.11.self_attn` | 3 | `output[1]` | [1, 64, 1, 876] | torch.bfloat16 → float32 | 9.237055564881302e-14 / 0.9453125 / 0.0010997089477363898 / 0.008603708524415334 | [NPY](tensors/0000417.npy) |
| 418 | `model.layers.11.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -326.0 / 450.0 / 0.5978702121310764 / 22.582552601593115 | [NPY](tensors/0000418.npy) |
| 419 | `model.layers.11.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.46875 / 4.625 / 0.010122136274973551 / 0.730738043012769 | [NPY](tensors/0000419.npy) |
| 420 | `model.layers.11.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.46875 / 4.625 / 0.010122136274973551 / 0.730738043012769 | [NPY](tensors/0000420.npy) |
| 421 | `model.layers.11.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.46875 / 4.625 / 0.010122136274973551 / 0.730738043012769 | [NPY](tensors/0000421.npy) |
| 422 | `model.layers.11.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 423 | `model.layers.11.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 424 | `model.layers.11.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 425 | `model.layers.11.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -121.0 / 121.0 / 0.20458135472403632 / 6.087855842763874 | [NPY](tensors/0000425.npy) |
| 426 | `model.layers.11.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -121.0 / 121.0 / 0.20458135472403632 / 6.087855842763874 | [NPY](tensors/0000426.npy) |
| 427 | `model.layers.11.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.5546875 / 1.2578125 / -0.083831787109375 / 0.6848084366206016 | [NPY](tensors/0000427.npy) |
| 428 | `model.layers.11` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -448.0 / 560.0 / 0.8005242241753472 / 26.24866115394284 | [NPY](tensors/0000428.npy) |
| 507 | `model.layers.11` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -161.0 / 360.0 / 0.5040442572699653 / 16.848671536837106 | [NPY](tensors/0000507.npy) |
| 508 | `model.layers.11` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 877] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000508.npy) |
| 509 | `model.layers.11` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.58746337890625 / 1.0206486490707742 | [NPY](tensors/0000509.npy) |
| 510 | `model.layers.11` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.3203125 / 0.10449105501174927 / 0.6417963143458147 | [NPY](tensors/0000510.npy) |
| 511 | `model.layers.11` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 876.0 / 876.0 / 876.0 / 0.0 | [NPY](tensors/0000511.npy) |
| 512 | `model.layers.11` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 513 | `model.layers.11` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 514 | `model.layers.11` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 515 | `model.layers.11.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -161.0 / 360.0 / 0.5040442572699653 / 16.848671536837106 | [NPY](tensors/0000515.npy) |
| 516 | `model.layers.11.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 100.0 / 0.08650783167945014 / 2.898853107954646 | [NPY](tensors/0000516.npy) |
| 517 | `model.layers.11.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 100.0 / 0.08650783167945014 / 2.898853107954646 | [NPY](tensors/0000517.npy) |
| 518 | `model.layers.11.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 877] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000518.npy) |
| 519 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 876.0 / 876.0 / 876.0 / 0.0 | [NPY](tensors/0000519.npy) |
| 520 | `model.layers.11.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 521 | `model.layers.11.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 522 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.58746337890625 / 1.0206486490707742 | [NPY](tensors/0000522.npy) |
| 523 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.3203125 / 0.10449105501174927 / 0.6417963143458147 | [NPY](tensors/0000523.npy) |
| 524 | `model.layers.11.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 525 | `model.layers.11.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 100.0 / 0.08650783167945014 / 2.898853107954646 | [NPY](tensors/0000525.npy) |
| 526 | `model.layers.11.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.9375 / 9.125 / 0.039991053054109216 / 1.314928485446058 | [NPY](tensors/0000526.npy) |
| 527 | `model.layers.11.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 100.0 / 0.08650783167945014 / 2.898853107954646 | [NPY](tensors/0000527.npy) |
| 528 | `model.layers.11.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.375 / 36.75 / 0.11675317585468292 / 3.930557800914777 | [NPY](tensors/0000528.npy) |
| 529 | `model.layers.11.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 100.0 / 0.08650783167945014 / 2.898853107954646 | [NPY](tensors/0000529.npy) |
| 530 | `model.layers.11.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.5625 / 6.53125 / -0.12204796075820923 / 2.234181864843197 | [NPY](tensors/0000530.npy) |
| 531 | `model.layers.11.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.09375 / 6.875 / -0.03723186440765858 / 1.5168565160102387 | [NPY](tensors/0000531.npy) |
| 532 | `model.layers.11.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 118.5 / 0.042228469252586366 / 4.436789706025318 | [NPY](tensors/0000532.npy) |
| 533 | `model.layers.11.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 118.5 / 0.042228469252586366 / 4.436789706025318 | [NPY](tensors/0000533.npy) |
| 534 | `model.layers.11.self_attn` | 4 | `output[1]` | [1, 64, 1, 877] | torch.bfloat16 → float32 | 1.5845103007450234e-12 / 0.84375 / 0.0010777576272766618 / 0.006690194491619448 | [NPY](tensors/0000534.npy) |
| 535 | `model.layers.11.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -241.0 / 384.0 / 0.5453819698757596 / 19.006034698893277 | [NPY](tensors/0000535.npy) |
| 536 | `model.layers.11.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.609375 / 4.34375 / 0.011188585228390164 / 0.6995172479562465 | [NPY](tensors/0000536.npy) |
| 537 | `model.layers.11.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.609375 / 4.34375 / 0.011188585228390164 / 0.6995172479562465 | [NPY](tensors/0000537.npy) |
| 538 | `model.layers.11.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.609375 / 4.34375 / 0.011188585228390164 / 0.6995172479562465 | [NPY](tensors/0000538.npy) |
| 539 | `model.layers.11.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 540 | `model.layers.11.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 541 | `model.layers.11.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 542 | `model.layers.11.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -35.75 / 34.5 / 0.04272150960233476 / 4.098413652371829 | [NPY](tensors/0000542.npy) |
| 543 | `model.layers.11.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.75 / 34.5 / 0.04272150960233476 / 4.098413652371829 | [NPY](tensors/0000543.npy) |
| 544 | `model.layers.11.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3671875 / 1.40625 / -0.02692413330078125 / 0.6407896315435738 | [NPY](tensors/0000544.npy) |
| 545 | `model.layers.11` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -276.0 / 372.0 / 0.5873748779296875 / 20.220339752905833 | [NPY](tensors/0000545.npy) |
| 624 | `model.layers.11` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -268.0 / 404.0 / 0.5152353922526042 / 18.228051764613948 | [NPY](tensors/0000624.npy) |
| 625 | `model.layers.11` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 878] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000625.npy) |
| 626 | `model.layers.11` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.558441162109375 / 1.0101761449217725 | [NPY](tensors/0000626.npy) |
| 627 | `model.layers.11` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3359375 / 0.06921488046646118 / 0.6876239253025267 | [NPY](tensors/0000627.npy) |
| 628 | `model.layers.11` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 877.0 / 877.0 / 877.0 / 0.0 | [NPY](tensors/0000628.npy) |
| 629 | `model.layers.11` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 630 | `model.layers.11` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 631 | `model.layers.11` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 632 | `model.layers.11.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -268.0 / 404.0 / 0.5152353922526042 / 18.228051764613948 | [NPY](tensors/0000632.npy) |
| 633 | `model.layers.11.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 104.0 / 0.07853400508562723 / 3.1605206176888783 | [NPY](tensors/0000633.npy) |
| 634 | `model.layers.11.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 104.0 / 0.07853400508562723 / 3.1605206176888783 | [NPY](tensors/0000634.npy) |
| 635 | `model.layers.11.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 878] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000635.npy) |
| 636 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 877.0 / 877.0 / 877.0 / 0.0 | [NPY](tensors/0000636.npy) |
| 637 | `model.layers.11.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 638 | `model.layers.11.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 639 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.558441162109375 / 1.0101761449217725 | [NPY](tensors/0000639.npy) |
| 640 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3359375 / 0.06921488046646118 / 0.6876239253025267 | [NPY](tensors/0000640.npy) |
| 641 | `model.layers.11.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 642 | `model.layers.11.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 104.0 / 0.07853400508562723 / 3.1605206176888783 | [NPY](tensors/0000642.npy) |
| 643 | `model.layers.11.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.5 / 7.875 / 0.03473000368103385 / 1.3097285018493632 | [NPY](tensors/0000643.npy) |
| 644 | `model.layers.11.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 104.0 / 0.07853400508562723 / 3.1605206176888783 | [NPY](tensors/0000644.npy) |
| 645 | `model.layers.11.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.0 / 38.25 / 0.1016349047422409 / 3.870873131758738 | [NPY](tensors/0000645.npy) |
| 646 | `model.layers.11.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 104.0 / 0.07853400508562723 / 3.1605206176888783 | [NPY](tensors/0000646.npy) |
| 647 | `model.layers.11.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.875 / 6.0 / -0.13523995876312256 / 1.8353927259292266 | [NPY](tensors/0000647.npy) |
| 648 | `model.layers.11.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.90625 / 8.25 / -0.05945621442515403 / 1.5831016870952002 | [NPY](tensors/0000648.npy) |
| 649 | `model.layers.11.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.25 / 118.0 / 0.09049650960498386 / 4.100845545397757 | [NPY](tensors/0000649.npy) |
| 650 | `model.layers.11.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.25 / 118.0 / 0.09049650960498386 / 4.100845545397757 | [NPY](tensors/0000650.npy) |
| 651 | `model.layers.11.self_attn` | 5 | `output[1]` | [1, 64, 1, 878] | torch.bfloat16 → float32 | 3.2862601528904634e-14 / 0.953125 / 0.001085981716685559 / 0.006602935091024692 | [NPY](tensors/0000651.npy) |
| 652 | `model.layers.11.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -280.0 / 402.0 / 0.6063978407118056 / 19.800645606583323 | [NPY](tensors/0000652.npy) |
| 653 | `model.layers.11.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.9375 / 0.005594489309522841 / 0.652378305494163 | [NPY](tensors/0000653.npy) |
| 654 | `model.layers.11.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.9375 / 0.005594489309522841 / 0.652378305494163 | [NPY](tensors/0000654.npy) |
| 655 | `model.layers.11.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.9375 / 0.005594489309522841 / 0.652378305494163 | [NPY](tensors/0000655.npy) |
| 656 | `model.layers.11.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 657 | `model.layers.11.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 658 | `model.layers.11.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 659 | `model.layers.11.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -69.5 / 121.5 / 0.02721413771311442 / 5.094014988796326 | [NPY](tensors/0000659.npy) |
| 660 | `model.layers.11.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 121.5 / 0.02721413771311442 / 5.094014988796326 | [NPY](tensors/0000660.npy) |
| 661 | `model.layers.11.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.46875 / 0.95703125 / -0.06147956848144531 / 0.5617507230430832 | [NPY](tensors/0000661.npy) |
| 662 | `model.layers.11` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -350.0 / 524.0 / 0.6342919243706597 / 22.99764861800205 | [NPY](tensors/0000662.npy) |
| 741 | `model.layers.11` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -185.0 / 304.0 / 0.5177762349446614 / 15.021161446565527 | [NPY](tensors/0000741.npy) |
| 742 | `model.layers.11` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 879] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000742.npy) |
| 743 | `model.layers.11` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5615997314453125 / 0.9848671705266577 | [NPY](tensors/0000743.npy) |
| 744 | `model.layers.11` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.030482351779937744 / 0.7236419726526301 | [NPY](tensors/0000744.npy) |
| 745 | `model.layers.11` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 878.0 / 878.0 / 878.0 / 0.0 | [NPY](tensors/0000745.npy) |
| 746 | `model.layers.11` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 747 | `model.layers.11` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 748 | `model.layers.11` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 749 | `model.layers.11.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -185.0 / 304.0 / 0.5177762349446614 / 15.021161446565527 | [NPY](tensors/0000749.npy) |
| 750 | `model.layers.11.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 86.0 / 0.0862958828608195 / 3.0225089058054064 | [NPY](tensors/0000750.npy) |
| 751 | `model.layers.11.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 86.0 / 0.0862958828608195 / 3.0225089058054064 | [NPY](tensors/0000751.npy) |
| 752 | `model.layers.11.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 879] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000752.npy) |
| 753 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 878.0 / 878.0 / 878.0 / 0.0 | [NPY](tensors/0000753.npy) |
| 754 | `model.layers.11.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 755 | `model.layers.11.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 756 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5615997314453125 / 0.9848671705266577 | [NPY](tensors/0000756.npy) |
| 757 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.030482351779937744 / 0.7236419726526301 | [NPY](tensors/0000757.npy) |
| 758 | `model.layers.11.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 759 | `model.layers.11.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 86.0 / 0.0862958828608195 / 3.0225089058054064 | [NPY](tensors/0000759.npy) |
| 760 | `model.layers.11.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 8.125 / 0.036910990718752146 / 1.325346727400648 | [NPY](tensors/0000760.npy) |
| 761 | `model.layers.11.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 86.0 / 0.0862958828608195 / 3.0225089058054064 | [NPY](tensors/0000761.npy) |
| 762 | `model.layers.11.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -37.0 / 43.5 / 0.16888363659381866 / 4.254780605922886 | [NPY](tensors/0000762.npy) |
| 763 | `model.layers.11.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 86.0 / 0.0862958828608195 / 3.0225089058054064 | [NPY](tensors/0000763.npy) |
| 764 | `model.layers.11.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.25 / 8.0625 / -0.12284111976623535 / 1.9916916203223338 | [NPY](tensors/0000764.npy) |
| 765 | `model.layers.11.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.84375 / 8.3125 / -0.06160706194350496 / 1.5272035759196658 | [NPY](tensors/0000765.npy) |
| 766 | `model.layers.11.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 112.5 / 0.0732683120502366 / 4.0331874727374 | [NPY](tensors/0000766.npy) |
| 767 | `model.layers.11.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 112.5 / 0.0732683120502366 / 4.0331874727374 | [NPY](tensors/0000767.npy) |
| 768 | `model.layers.11.self_attn` | 6 | `output[1]` | [1, 64, 1, 879] | torch.bfloat16 → float32 | 1.3983481039758772e-11 / 0.88671875 / 0.0010628439066088752 / 0.00610576445851703 | [NPY](tensors/0000768.npy) |
| 769 | `model.layers.11.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -256.0 / 330.0 / 0.5910982131958008 / 17.28004677567637 | [NPY](tensors/0000769.npy) |
| 770 | `model.layers.11.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.53125 / 3.0 / 0.015142046080695259 / 0.6034678946282095 | [NPY](tensors/0000770.npy) |
| 771 | `model.layers.11.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.53125 / 3.0 / 0.015142046080695259 / 0.6034678946282095 | [NPY](tensors/0000771.npy) |
| 772 | `model.layers.11.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.53125 / 3.0 / 0.015142046080695259 / 0.6034678946282095 | [NPY](tensors/0000772.npy) |
| 773 | `model.layers.11.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 774 | `model.layers.11.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 775 | `model.layers.11.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 776 | `model.layers.11.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -22.125 / 31.625 / 0.04483024014366998 / 3.091496198134707 | [NPY](tensors/0000776.npy) |
| 777 | `model.layers.11.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 31.625 / 0.04483024014366998 / 3.091496198134707 | [NPY](tensors/0000777.npy) |
| 778 | `model.layers.11.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.015625 / 0.640625 / -0.06291317939758301 / 0.44370620204308675 | [NPY](tensors/0000778.npy) |
| 779 | `model.layers.11` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -224.0 / 334.0 / 0.6356787787543403 / 17.79784308750334 | [NPY](tensors/0000779.npy) |
| 858 | `model.layers.11` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -274.0 / 444.0 / 0.45657806396484374 / 19.280966123740907 | [NPY](tensors/0000858.npy) |
| 859 | `model.layers.11` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 880] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000859.npy) |
| 860 | `model.layers.11` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.5797119140625 / 1.0186800490978136 | [NPY](tensors/0000860.npy) |
| 861 | `model.layers.11` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.296875 / 0.009048700332641602 / 0.6598895155407865 | [NPY](tensors/0000861.npy) |
| 862 | `model.layers.11` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 879.0 / 879.0 / 879.0 / 0.0 | [NPY](tensors/0000862.npy) |
| 863 | `model.layers.11` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 864 | `model.layers.11` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 865 | `model.layers.11` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 866 | `model.layers.11.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -274.0 / 444.0 / 0.45657806396484374 / 19.280966123740907 | [NPY](tensors/0000866.npy) |
| 867 | `model.layers.11.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -74.5 / 108.0 / 0.06748889684677124 / 3.2644826164722858 | [NPY](tensors/0000867.npy) |
| 868 | `model.layers.11.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -74.5 / 108.0 / 0.06748889684677124 / 3.2644826164722858 | [NPY](tensors/0000868.npy) |
| 869 | `model.layers.11.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 880] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000869.npy) |
| 870 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 879.0 / 879.0 / 879.0 / 0.0 | [NPY](tensors/0000870.npy) |
| 871 | `model.layers.11.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 872 | `model.layers.11.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 873 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.5797119140625 / 1.0186800490978136 | [NPY](tensors/0000873.npy) |
| 874 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.296875 / 0.009048700332641602 / 0.6598895155407865 | [NPY](tensors/0000874.npy) |
| 875 | `model.layers.11.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 876 | `model.layers.11.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -74.5 / 108.0 / 0.06748889684677124 / 3.2644826164722858 | [NPY](tensors/0000876.npy) |
| 877 | `model.layers.11.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.9375 / 10.6875 / 0.005770333227701485 / 1.2915398258579602 | [NPY](tensors/0000877.npy) |
| 878 | `model.layers.11.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -74.5 / 108.0 / 0.06748889684677124 / 3.2644826164722858 | [NPY](tensors/0000878.npy) |
| 879 | `model.layers.11.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.5 / 44.5 / 0.04725721478462219 / 4.159760220707849 | [NPY](tensors/0000879.npy) |
| 880 | `model.layers.11.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -74.5 / 108.0 / 0.06748889684677124 / 3.2644826164722858 | [NPY](tensors/0000880.npy) |
| 881 | `model.layers.11.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.4375 / 6.9375 / -0.10976894944906235 / 2.1048036879296768 | [NPY](tensors/0000881.npy) |
| 882 | `model.layers.11.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.53125 / 6.71875 / -0.05225322721526027 / 1.6134249903189968 | [NPY](tensors/0000882.npy) |
| 883 | `model.layers.11.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.5 / 121.0 / 0.03311805460188124 / 4.149205306203607 | [NPY](tensors/0000883.npy) |
| 884 | `model.layers.11.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.5 / 121.0 / 0.03311805460188124 / 4.149205306203607 | [NPY](tensors/0000884.npy) |
| 885 | `model.layers.11.self_attn` | 7 | `output[1]` | [1, 64, 1, 880] | torch.bfloat16 → float32 | 5.440092820663267e-14 / 0.95703125 / 0.0010859380695045508 / 0.006220041885610868 | [NPY](tensors/0000885.npy) |
| 886 | `model.layers.11.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -344.0 / 462.0 / 0.4896016438802083 / 21.32607636088577 | [NPY](tensors/0000886.npy) |
| 887 | `model.layers.11.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5 / 3.3125 / 0.0029586361514197454 / 0.5881398414105029 | [NPY](tensors/0000887.npy) |
| 888 | `model.layers.11.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5 / 3.3125 / 0.0029586361514197454 / 0.5881398414105029 | [NPY](tensors/0000888.npy) |
| 889 | `model.layers.11.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.5 / 3.3125 / 0.0029586361514197454 / 0.5881398414105029 | [NPY](tensors/0000889.npy) |
| 890 | `model.layers.11.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 891 | `model.layers.11.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 892 | `model.layers.11.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 893 | `model.layers.11.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -47.0 / 136.0 / 0.041342143217722574 / 4.268262024500795 | [NPY](tensors/0000893.npy) |
| 894 | `model.layers.11.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 136.0 / 0.041342143217722574 / 4.268262024500795 | [NPY](tensors/0000894.npy) |
| 895 | `model.layers.11.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.90234375 / 0.765625 / -0.0885477066040039 / 0.43392613925559725 | [NPY](tensors/0000895.npy) |
| 896 | `model.layers.11` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -392.0 / 600.0 / 0.5320421006944445 / 24.034181006535196 | [NPY](tensors/0000896.npy) |
| 975 | `model.layers.11` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -304.0 / 368.0 / 0.33129747178819446 / 17.134569102740514 | [NPY](tensors/0000975.npy) |
| 976 | `model.layers.11` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 881] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000976.npy) |
| 977 | `model.layers.11` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5914459228515625 / 1.036270522436494 | [NPY](tensors/0000977.npy) |
| 978 | `model.layers.11` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.0005860328674316406 / 0.6206299087009224 | [NPY](tensors/0000978.npy) |
| 979 | `model.layers.11` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 880.0 / 880.0 / 880.0 / 0.0 | [NPY](tensors/0000979.npy) |
| 980 | `model.layers.11` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 981 | `model.layers.11` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 982 | `model.layers.11` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 983 | `model.layers.11.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -304.0 / 368.0 / 0.33129747178819446 / 17.134569102740514 | [NPY](tensors/0000983.npy) |
| 984 | `model.layers.11.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 100.5 / 0.054349825117323135 / 3.3540616027966035 | [NPY](tensors/0000984.npy) |
| 985 | `model.layers.11.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 100.5 / 0.054349825117323135 / 3.3540616027966035 | [NPY](tensors/0000985.npy) |
| 986 | `model.layers.11.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 881] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000986.npy) |
| 987 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 880.0 / 880.0 / 880.0 / 0.0 | [NPY](tensors/0000987.npy) |
| 988 | `model.layers.11.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 989 | `model.layers.11.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 990 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5914459228515625 / 1.036270522436494 | [NPY](tensors/0000990.npy) |
| 991 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.0005860328674316406 / 0.6206299087009224 | [NPY](tensors/0000991.npy) |
| 992 | `model.layers.11.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 993 | `model.layers.11.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 100.5 / 0.054349825117323135 / 3.3540616027966035 | [NPY](tensors/0000993.npy) |
| 994 | `model.layers.11.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.625 / 7.65625 / 0.023444929625838995 / 1.2567670962487536 | [NPY](tensors/0000994.npy) |
| 995 | `model.layers.11.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 100.5 / 0.054349825117323135 / 3.3540616027966035 | [NPY](tensors/0000995.npy) |
| 996 | `model.layers.11.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.5 / 47.25 / 0.11132678389549255 / 4.238459182336875 | [NPY](tensors/0000996.npy) |
| 997 | `model.layers.11.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 100.5 / 0.054349825117323135 / 3.3540616027966035 | [NPY](tensors/0000997.npy) |
| 998 | `model.layers.11.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.625 / 5.0 / -0.04693805053830147 / 1.7480186305309218 | [NPY](tensors/0000998.npy) |
| 999 | `model.layers.11.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 6.6875 / -0.058105713687837124 / 1.5480695029651996 | [NPY](tensors/0000999.npy) |
| 1000 | `model.layers.11.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 128.0 / 0.1132420984407266 / 4.109895397047768 | [NPY](tensors/0001000.npy) |
| 1001 | `model.layers.11.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 128.0 / 0.1132420984407266 / 4.109895397047768 | [NPY](tensors/0001001.npy) |
| 1002 | `model.layers.11.self_attn` | 8 | `output[1]` | [1, 64, 1, 881] | torch.bfloat16 → float32 | 4.860112312599085e-12 / 0.953125 / 0.001064142143790435 / 0.006303083102388599 | [NPY](tensors/0001002.npy) |
| 1003 | `model.layers.11.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -350.0 / 398.0 / 0.4447713216145833 / 19.35472782535528 | [NPY](tensors/0001003.npy) |
| 1004 | `model.layers.11.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.3125 / 2.875 / 0.006561022996902466 / 0.5682126657595837 | [NPY](tensors/0001004.npy) |
| 1005 | `model.layers.11.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.3125 / 2.875 / 0.006561022996902466 / 0.5682126657595837 | [NPY](tensors/0001005.npy) |
| 1006 | `model.layers.11.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.3125 / 2.875 / 0.006561022996902466 / 0.5682126657595837 | [NPY](tensors/0001006.npy) |
| 1007 | `model.layers.11.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1008 | `model.layers.11.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1009 | `model.layers.11.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1010 | `model.layers.11.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -15.1875 / 74.0 / 0.07332651085323758 / 3.1350086247355224 | [NPY](tensors/0001010.npy) |
| 1011 | `model.layers.11.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.1875 / 74.0 / 0.07332651085323758 / 3.1350086247355224 | [NPY](tensors/0001011.npy) |
| 1012 | `model.layers.11.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.72265625 / 0.9140625 / -0.06867790222167969 / 0.35088078933844585 | [NPY](tensors/0001012.npy) |
| 1013 | `model.layers.11` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -366.0 / 472.0 / 0.5183442857530381 / 20.85311064284135 | [NPY](tensors/0001013.npy) |
| 1092 | `model.layers.11` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -300.0 / 408.0 / 0.04643825954861111 / 18.644927544534244 | [NPY](tensors/0001092.npy) |
| 1093 | `model.layers.11` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 882] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001093.npy) |
| 1094 | `model.layers.11` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.594635009765625 / 0.998380462956763 | [NPY](tensors/0001094.npy) |
| 1095 | `model.layers.11` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3125 / -0.016051054000854492 / 0.6776192851250942 | [NPY](tensors/0001095.npy) |
| 1096 | `model.layers.11` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 881.0 / 881.0 / 881.0 / 0.0 | [NPY](tensors/0001096.npy) |
| 1097 | `model.layers.11` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1098 | `model.layers.11` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1099 | `model.layers.11` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1100 | `model.layers.11.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -300.0 / 408.0 / 0.04643825954861111 / 18.644927544534244 | [NPY](tensors/0001100.npy) |
| 1101 | `model.layers.11.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 89.0 / 0.022488709290822348 / 3.1961186593022135 | [NPY](tensors/0001101.npy) |
| 1102 | `model.layers.11.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 89.0 / 0.022488709290822348 / 3.1961186593022135 | [NPY](tensors/0001102.npy) |
| 1103 | `model.layers.11.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 882] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001103.npy) |
| 1104 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 881.0 / 881.0 / 881.0 / 0.0 | [NPY](tensors/0001104.npy) |
| 1105 | `model.layers.11.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1106 | `model.layers.11.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1107 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.594635009765625 / 0.998380462956763 | [NPY](tensors/0001107.npy) |
| 1108 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3125 / -0.016051054000854492 / 0.6776192851250942 | [NPY](tensors/0001108.npy) |
| 1109 | `model.layers.11.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1110 | `model.layers.11.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 89.0 / 0.022488709290822348 / 3.1961186593022135 | [NPY](tensors/0001110.npy) |
| 1111 | `model.layers.11.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.5 / 10.9375 / 0.024115502019412816 / 1.2851231127133762 | [NPY](tensors/0001111.npy) |
| 1112 | `model.layers.11.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 89.0 / 0.022488709290822348 / 3.1961186593022135 | [NPY](tensors/0001112.npy) |
| 1113 | `model.layers.11.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.25 / 52.25 / 0.0202600359916687 / 4.800227759492942 | [NPY](tensors/0001113.npy) |
| 1114 | `model.layers.11.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 89.0 / 0.022488709290822348 / 3.1961186593022135 | [NPY](tensors/0001114.npy) |
| 1115 | `model.layers.11.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.0 / 6.40625 / 0.041815757751464844 / 2.357281026106054 | [NPY](tensors/0001115.npy) |
| 1116 | `model.layers.11.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.3125 / 6.875 / -0.03675480713718571 / 1.642625779187577 | [NPY](tensors/0001116.npy) |
| 1117 | `model.layers.11.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.0 / 165.0 / 0.16563233799404567 / 5.272991356969053 | [NPY](tensors/0001117.npy) |
| 1118 | `model.layers.11.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.0 / 165.0 / 0.16563233799404567 / 5.272991356969053 | [NPY](tensors/0001118.npy) |
| 1119 | `model.layers.11.self_attn` | 9 | `output[1]` | [1, 64, 1, 882] | torch.bfloat16 → float32 | 8.526512829121202e-13 / 0.9609375 / 0.0010562450917867415 / 0.007783649452768937 | [NPY](tensors/0001119.npy) |
| 1120 | `model.layers.11.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -298.0 / 448.0 / 0.212396240234375 / 21.071547199751084 | [NPY](tensors/0001120.npy) |
| 1121 | `model.layers.11.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.625 / 2.875 / 0.004518233405219184 / 0.6063947017585862 | [NPY](tensors/0001121.npy) |
| 1122 | `model.layers.11.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.625 / 2.875 / 0.004518233405219184 / 0.6063947017585862 | [NPY](tensors/0001122.npy) |
| 1123 | `model.layers.11.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.625 / 2.875 / 0.004518233405219184 / 0.6063947017585862 | [NPY](tensors/0001123.npy) |
| 1124 | `model.layers.11.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1125 | `model.layers.11.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1126 | `model.layers.11.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1127 | `model.layers.11.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -190.0 / 185.0 / 0.06056949297587077 / 6.465878753138224 | [NPY](tensors/0001127.npy) |
| 1128 | `model.layers.11.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -190.0 / 185.0 / 0.06056949297587077 / 6.465878753138224 | [NPY](tensors/0001128.npy) |
| 1129 | `model.layers.11.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.6953125 / 0.71484375 / -0.08941841125488281 / 0.3458014221464133 | [NPY](tensors/0001129.npy) |
| 1130 | `model.layers.11` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -488.0 / 552.0 / 0.27351786295572916 / 25.50430766098591 | [NPY](tensors/0001130.npy) |
| 1209 | `model.layers.11` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -336.0 / 394.0 / 0.1802260504828559 / 18.64732688256682 | [NPY](tensors/0001209.npy) |
| 1210 | `model.layers.11` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 883] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001210.npy) |
| 1211 | `model.layers.11` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.611114501953125 / 0.9771971733502269 | [NPY](tensors/0001211.npy) |
| 1212 | `model.layers.11` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / -0.047824978828430176 / 0.6921356554670257 | [NPY](tensors/0001212.npy) |
| 1213 | `model.layers.11` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 882.0 / 882.0 / 882.0 / 0.0 | [NPY](tensors/0001213.npy) |
| 1214 | `model.layers.11` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1215 | `model.layers.11` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1216 | `model.layers.11` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1217 | `model.layers.11.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -336.0 / 394.0 / 0.1802260504828559 / 18.64732688256682 | [NPY](tensors/0001217.npy) |
| 1218 | `model.layers.11.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 99.0 / 0.0416874090830485 / 3.357902194933873 | [NPY](tensors/0001218.npy) |
| 1219 | `model.layers.11.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 99.0 / 0.0416874090830485 / 3.357902194933873 | [NPY](tensors/0001219.npy) |
| 1220 | `model.layers.11.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 883] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001220.npy) |
| 1221 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 882.0 / 882.0 / 882.0 / 0.0 | [NPY](tensors/0001221.npy) |
| 1222 | `model.layers.11.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1223 | `model.layers.11.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1224 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.611114501953125 / 0.9771971733502269 | [NPY](tensors/0001224.npy) |
| 1225 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / -0.047824978828430176 / 0.6921356554670257 | [NPY](tensors/0001225.npy) |
| 1226 | `model.layers.11.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1227 | `model.layers.11.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 99.0 / 0.0416874090830485 / 3.357902194933873 | [NPY](tensors/0001227.npy) |
| 1228 | `model.layers.11.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.25 / 10.625 / 0.013637273223139346 / 1.33870971946795 | [NPY](tensors/0001228.npy) |
| 1229 | `model.layers.11.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 99.0 / 0.0416874090830485 / 3.357902194933873 | [NPY](tensors/0001229.npy) |
| 1230 | `model.layers.11.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.75 / 49.75 / 0.00037294626235961914 / 4.435329419010836 | [NPY](tensors/0001230.npy) |
| 1231 | `model.layers.11.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 99.0 / 0.0416874090830485 / 3.357902194933873 | [NPY](tensors/0001231.npy) |
| 1232 | `model.layers.11.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.875 / 8.875 / 0.04366112872958183 / 2.4147704096730047 | [NPY](tensors/0001232.npy) |
| 1233 | `model.layers.11.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.4375 / 8.0 / -0.03675459208898246 / 1.7323116089690367 | [NPY](tensors/0001233.npy) |
| 1234 | `model.layers.11.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.5 / 161.0 / 0.1549493498272366 / 4.920288199968881 | [NPY](tensors/0001234.npy) |
| 1235 | `model.layers.11.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.5 / 161.0 / 0.1549493498272366 / 4.920288199968881 | [NPY](tensors/0001235.npy) |
| 1236 | `model.layers.11.self_attn` | 10 | `output[1]` | [1, 64, 1, 883] | torch.bfloat16 → float32 | 7.37188088351104e-14 / 0.94140625 / 0.0010601926083589504 / 0.007744050047510992 | [NPY](tensors/0001236.npy) |
| 1237 | `model.layers.11.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -332.0 / 404.0 / 0.33356170654296874 / 20.7205137802132 | [NPY](tensors/0001237.npy) |
| 1238 | `model.layers.11.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.921875 / 3.375 / 0.009647187921735976 / 0.6006482322794169 | [NPY](tensors/0001238.npy) |
| 1239 | `model.layers.11.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.921875 / 3.375 / 0.009647187921735976 / 0.6006482322794169 | [NPY](tensors/0001239.npy) |
| 1240 | `model.layers.11.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.921875 / 3.375 / 0.009647187921735976 / 0.6006482322794169 | [NPY](tensors/0001240.npy) |
| 1241 | `model.layers.11.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1242 | `model.layers.11.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1243 | `model.layers.11.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1244 | `model.layers.11.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -102.0 / 86.0 / -0.1396273268593682 / 4.172962158960204 | [NPY](tensors/0001244.npy) |
| 1245 | `model.layers.11.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.0 / 86.0 / -0.1396273268593682 / 4.172962158960204 | [NPY](tensors/0001245.npy) |
| 1246 | `model.layers.11.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.65625 / 0.984375 / -0.06662750244140625 / 0.41443459579660435 | [NPY](tensors/0001246.npy) |
| 1247 | `model.layers.11` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -434.0 / 490.0 / 0.19424608018663195 / 22.74920970517703 | [NPY](tensors/0001247.npy) |
| 1326 | `model.layers.11` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -214.0 / 292.0 / 0.6934391657511393 / 16.4144454077551 | [NPY](tensors/0001326.npy) |
| 1327 | `model.layers.11` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 884] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001327.npy) |
| 1328 | `model.layers.11` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.659881591796875 / 0.9579637378310449 | [NPY](tensors/0001328.npy) |
| 1329 | `model.layers.11` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / -0.07649624347686768 / 0.6710666469829912 | [NPY](tensors/0001329.npy) |
| 1330 | `model.layers.11` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 883.0 / 883.0 / 883.0 / 0.0 | [NPY](tensors/0001330.npy) |
| 1331 | `model.layers.11` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1332 | `model.layers.11` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1333 | `model.layers.11` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1334 | `model.layers.11.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -214.0 / 292.0 / 0.6934391657511393 / 16.4144454077551 | [NPY](tensors/0001334.npy) |
| 1335 | `model.layers.11.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.5 / 82.0 / 0.09313626289367676 / 2.98779109978977 | [NPY](tensors/0001335.npy) |
| 1336 | `model.layers.11.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.5 / 82.0 / 0.09313626289367676 / 2.98779109978977 | [NPY](tensors/0001336.npy) |
| 1337 | `model.layers.11.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 884] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001337.npy) |
| 1338 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 883.0 / 883.0 / 883.0 / 0.0 | [NPY](tensors/0001338.npy) |
| 1339 | `model.layers.11.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1340 | `model.layers.11.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1341 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.659881591796875 / 0.9579637378310449 | [NPY](tensors/0001341.npy) |
| 1342 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / -0.07649624347686768 / 0.6710666469829912 | [NPY](tensors/0001342.npy) |
| 1343 | `model.layers.11.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1344 | `model.layers.11.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.5 / 82.0 / 0.09313626289367676 / 2.98779109978977 | [NPY](tensors/0001344.npy) |
| 1345 | `model.layers.11.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.1875 / 10.1875 / 0.032564531080424786 / 1.418042524054635 | [NPY](tensors/0001345.npy) |
| 1346 | `model.layers.11.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.5 / 82.0 / 0.09313626289367676 / 2.98779109978977 | [NPY](tensors/0001346.npy) |
| 1347 | `model.layers.11.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.75 / 45.75 / 0.0292731374502182 / 4.7112627460522205 | [NPY](tensors/0001347.npy) |
| 1348 | `model.layers.11.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.5 / 82.0 / 0.09313626289367676 / 2.98779109978977 | [NPY](tensors/0001348.npy) |
| 1349 | `model.layers.11.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.4375 / 8.0625 / -0.09194575250148773 / 2.6542649225419446 | [NPY](tensors/0001349.npy) |
| 1350 | `model.layers.11.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.3125 / 8.1875 / -0.04764920985326171 / 1.6763493980305144 | [NPY](tensors/0001350.npy) |
| 1351 | `model.layers.11.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.0 / 173.0 / 0.03163355390230815 / 5.645514864804486 | [NPY](tensors/0001351.npy) |
| 1352 | `model.layers.11.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.0 / 173.0 / 0.03163355390230815 / 5.645514864804486 | [NPY](tensors/0001352.npy) |
| 1353 | `model.layers.11.self_attn` | 11 | `output[1]` | [1, 64, 1, 884] | torch.bfloat16 → float32 | 2.886579864025407e-14 / 0.8984375 / 0.0010443697222589862 / 0.007570583470527595 | [NPY](tensors/0001353.npy) |
| 1354 | `model.layers.11.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -304.0 / 368.0 / 0.7253734164767796 / 19.50795933889804 | [NPY](tensors/0001354.npy) |
| 1355 | `model.layers.11.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.234375 / 2.9375 / 0.02103796402613322 / 0.6460128387158602 | [NPY](tensors/0001355.npy) |
| 1356 | `model.layers.11.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.234375 / 2.9375 / 0.02103796402613322 / 0.6460128387158602 | [NPY](tensors/0001356.npy) |
| 1357 | `model.layers.11.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.234375 / 2.9375 / 0.02103796402613322 / 0.6460128387158602 | [NPY](tensors/0001357.npy) |
| 1358 | `model.layers.11.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1359 | `model.layers.11.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1360 | `model.layers.11.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1361 | `model.layers.11.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -34.5 / 134.0 / 0.04389393329620361 / 4.662155405499184 | [NPY](tensors/0001361.npy) |
| 1362 | `model.layers.11.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 134.0 / 0.04389393329620361 / 4.662155405499184 | [NPY](tensors/0001362.npy) |
| 1363 | `model.layers.11.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.63671875 / 1.078125 / -0.03057098388671875 / 0.40077658628411905 | [NPY](tensors/0001363.npy) |
| 1364 | `model.layers.11` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -310.0 / 502.0 / 0.7691212972005208 / 21.879989964415234 | [NPY](tensors/0001364.npy) |
| 1443 | `model.layers.11` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -180.0 / 228.0 / 0.9492869906955295 / 18.212916150413534 | [NPY](tensors/0001443.npy) |
| 1444 | `model.layers.11` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 885] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001444.npy) |
| 1445 | `model.layers.11` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.734130859375 / 0.896956143048102 | [NPY](tensors/0001445.npy) |
| 1446 | `model.layers.11` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.296875 / -0.06761544942855835 / 0.6796756860615183 | [NPY](tensors/0001446.npy) |
| 1447 | `model.layers.11` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 884.0 / 884.0 / 884.0 / 0.0 | [NPY](tensors/0001447.npy) |
| 1448 | `model.layers.11` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1449 | `model.layers.11` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1450 | `model.layers.11` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1451 | `model.layers.11.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -180.0 / 228.0 / 0.9492869906955295 / 18.212916150413534 | [NPY](tensors/0001451.npy) |
| 1452 | `model.layers.11.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.75 / 54.25 / 0.10626733303070068 / 2.3910992882903352 | [NPY](tensors/0001452.npy) |
| 1453 | `model.layers.11.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.75 / 54.25 / 0.10626733303070068 / 2.3910992882903352 | [NPY](tensors/0001453.npy) |
| 1454 | `model.layers.11.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 885] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001454.npy) |
| 1455 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 884.0 / 884.0 / 884.0 / 0.0 | [NPY](tensors/0001455.npy) |
| 1456 | `model.layers.11.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1457 | `model.layers.11.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1458 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.734130859375 / 0.896956143048102 | [NPY](tensors/0001458.npy) |
| 1459 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.296875 / -0.06761544942855835 / 0.6796756860615183 | [NPY](tensors/0001459.npy) |
| 1460 | `model.layers.11.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1461 | `model.layers.11.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.75 / 54.25 / 0.10626733303070068 / 2.3910992882903352 | [NPY](tensors/0001461.npy) |
| 1462 | `model.layers.11.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.8125 / 10.375 / 0.025436523370444775 / 1.4273186169252954 | [NPY](tensors/0001462.npy) |
| 1463 | `model.layers.11.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.75 / 54.25 / 0.10626733303070068 / 2.3910992882903352 | [NPY](tensors/0001463.npy) |
| 1464 | `model.layers.11.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.5 / 44.25 / 0.023947983980178833 / 4.672962502399495 | [NPY](tensors/0001464.npy) |
| 1465 | `model.layers.11.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.75 / 54.25 / 0.10626733303070068 / 2.3910992882903352 | [NPY](tensors/0001465.npy) |
| 1466 | `model.layers.11.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.4375 / 9.6875 / 0.006675064563751221 / 2.644649700692192 | [NPY](tensors/0001466.npy) |
| 1467 | `model.layers.11.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.5625 / 9.0625 / -0.025729366578161716 / 1.6274340080761762 | [NPY](tensors/0001467.npy) |
| 1468 | `model.layers.11.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -131.0 / 183.0 / 0.06267368462350634 / 6.625460213340632 | [NPY](tensors/0001468.npy) |
| 1469 | `model.layers.11.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -131.0 / 183.0 / 0.06267368462350634 / 6.625460213340632 | [NPY](tensors/0001469.npy) |
| 1470 | `model.layers.11.self_attn` | 12 | `output[1]` | [1, 64, 1, 885] | torch.bfloat16 → float32 | 4.206412995699793e-12 / 0.73046875 / 0.0010399148060915267 / 0.007542255378089685 | [NPY](tensors/0001470.npy) |
| 1471 | `model.layers.11.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 370.0 / 1.0110914442274306 / 21.4481509159075 | [NPY](tensors/0001471.npy) |
| 1472 | `model.layers.11.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.125 / 4.21875 / 0.0382434950934516 / 0.7461076973730095 | [NPY](tensors/0001472.npy) |
| 1473 | `model.layers.11.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.125 / 4.21875 / 0.0382434950934516 / 0.7461076973730095 | [NPY](tensors/0001473.npy) |
| 1474 | `model.layers.11.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.125 / 4.21875 / 0.0382434950934516 / 0.7461076973730095 | [NPY](tensors/0001474.npy) |
| 1475 | `model.layers.11.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1476 | `model.layers.11.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1477 | `model.layers.11.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1478 | `model.layers.11.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -15.9375 / 69.0 / 0.12798267470465766 / 4.279492740241852 | [NPY](tensors/0001478.npy) |
| 1479 | `model.layers.11.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.9375 / 69.0 / 0.12798267470465766 / 4.279492740241852 | [NPY](tensors/0001479.npy) |
| 1480 | `model.layers.11.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.625 / 1.4765625 / -0.09049034118652344 / 0.6434700091190186 | [NPY](tensors/0001480.npy) |
| 1481 | `model.layers.11` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -280.0 / 440.0 / 1.1385777791341145 / 22.97368405654467 | [NPY](tensors/0001481.npy) |
| 1560 | `model.layers.11` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -210.0 / 328.0 / 0.6130274454752604 / 19.054250908576474 | [NPY](tensors/0001560.npy) |
| 1561 | `model.layers.11` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 886] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001561.npy) |
| 1562 | `model.layers.11` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.7958755493164062 / 0.858839493189722 | [NPY](tensors/0001562.npy) |
| 1563 | `model.layers.11` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.005351245403289795 / 0.6623439987299442 | [NPY](tensors/0001563.npy) |
| 1564 | `model.layers.11` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 885.0 / 885.0 / 885.0 / 0.0 | [NPY](tensors/0001564.npy) |
| 1565 | `model.layers.11` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1566 | `model.layers.11` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1567 | `model.layers.11` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1568 | `model.layers.11.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -210.0 / 328.0 / 0.6130274454752604 / 19.054250908576474 | [NPY](tensors/0001568.npy) |
| 1569 | `model.layers.11.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.75 / 80.5 / 0.07536965211232503 / 2.6645051596072373 | [NPY](tensors/0001569.npy) |
| 1570 | `model.layers.11.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.75 / 80.5 / 0.07536965211232503 / 2.6645051596072373 | [NPY](tensors/0001570.npy) |
| 1571 | `model.layers.11.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 886] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001571.npy) |
| 1572 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 885.0 / 885.0 / 885.0 / 0.0 | [NPY](tensors/0001572.npy) |
| 1573 | `model.layers.11.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1574 | `model.layers.11.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1575 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.7958755493164062 / 0.858839493189722 | [NPY](tensors/0001575.npy) |
| 1576 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.005351245403289795 / 0.6623439987299442 | [NPY](tensors/0001576.npy) |
| 1577 | `model.layers.11.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1578 | `model.layers.11.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.75 / 80.5 / 0.07536965211232503 / 2.6645051596072373 | [NPY](tensors/0001578.npy) |
| 1579 | `model.layers.11.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.375 / 11.1875 / -0.00028380495496094227 / 1.4396665549339558 | [NPY](tensors/0001579.npy) |
| 1580 | `model.layers.11.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.75 / 80.5 / 0.07536965211232503 / 2.6645051596072373 | [NPY](tensors/0001580.npy) |
| 1581 | `model.layers.11.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.5 / 39.25 / -0.06328022480010986 / 4.575679567905147 | [NPY](tensors/0001581.npy) |
| 1582 | `model.layers.11.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.75 / 80.5 / 0.07536965211232503 / 2.6645051596072373 | [NPY](tensors/0001582.npy) |
| 1583 | `model.layers.11.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.8125 / 7.6875 / 0.07759237289428711 / 2.528304115734444 | [NPY](tensors/0001583.npy) |
| 1584 | `model.layers.11.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.3125 / 7.71875 / -0.013920075260102749 / 1.783641430407894 | [NPY](tensors/0001584.npy) |
| 1585 | `model.layers.11.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 186.0 / 0.1541340668996175 / 6.155833061303771 | [NPY](tensors/0001585.npy) |
| 1586 | `model.layers.11.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 186.0 / 0.1541340668996175 / 6.155833061303771 | [NPY](tensors/0001586.npy) |
| 1587 | `model.layers.11.self_attn` | 13 | `output[1]` | [1, 64, 1, 886] | torch.bfloat16 → float32 | 3.042011087472929e-14 / 0.85546875 / 0.0010784820617836268 / 0.00815095869682599 | [NPY](tensors/0001587.npy) |
| 1588 | `model.layers.11.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -308.0 / 448.0 / 0.7662673950195312 / 22.27290612209144 | [NPY](tensors/0001588.npy) |
| 1589 | `model.layers.11.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.15625 / 4.3125 / 0.015316269132826063 / 0.7215684082030677 | [NPY](tensors/0001589.npy) |
| 1590 | `model.layers.11.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.15625 / 4.3125 / 0.015316269132826063 / 0.7215684082030677 | [NPY](tensors/0001590.npy) |
| 1591 | `model.layers.11.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.15625 / 4.3125 / 0.015316269132826063 / 0.7215684082030677 | [NPY](tensors/0001591.npy) |
| 1592 | `model.layers.11.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1593 | `model.layers.11.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1594 | `model.layers.11.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1595 | `model.layers.11.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -25.875 / 118.5 / 0.13670044077767265 / 4.734718548752113 | [NPY](tensors/0001595.npy) |
| 1596 | `model.layers.11.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.875 / 118.5 / 0.13670044077767265 / 4.734718548752113 | [NPY](tensors/0001596.npy) |
| 1597 | `model.layers.11.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.53125 / 1.3359375 / -0.15592193603515625 / 0.6865757603719498 | [NPY](tensors/0001597.npy) |
| 1598 | `model.layers.11` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -328.0 / 568.0 / 0.9038113064236111 / 24.88337124028011 | [NPY](tensors/0001598.npy) |
| 1677 | `model.layers.11` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -296.0 / 426.0 / 0.44755113389756945 / 21.627483281365425 | [NPY](tensors/0001677.npy) |
| 1678 | `model.layers.11` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 887] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001678.npy) |
| 1679 | `model.layers.11` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.805328369140625 / 0.858282942374398 | [NPY](tensors/0001679.npy) |
| 1680 | `model.layers.11` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.2890625 / 0.08753019571304321 / 0.6450265564714699 | [NPY](tensors/0001680.npy) |
| 1681 | `model.layers.11` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 886.0 / 886.0 / 886.0 / 0.0 | [NPY](tensors/0001681.npy) |
| 1682 | `model.layers.11` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1683 | `model.layers.11` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1684 | `model.layers.11` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1685 | `model.layers.11.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -296.0 / 426.0 / 0.44755113389756945 / 21.627483281365425 | [NPY](tensors/0001685.npy) |
| 1686 | `model.layers.11.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 92.5 / 0.05813509093390571 / 2.9115633056787376 | [NPY](tensors/0001686.npy) |
| 1687 | `model.layers.11.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 92.5 / 0.05813509093390571 / 2.9115633056787376 | [NPY](tensors/0001687.npy) |
| 1688 | `model.layers.11.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 887] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001688.npy) |
| 1689 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 886.0 / 886.0 / 886.0 / 0.0 | [NPY](tensors/0001689.npy) |
| 1690 | `model.layers.11.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1691 | `model.layers.11.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1692 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.805328369140625 / 0.858282942374398 | [NPY](tensors/0001692.npy) |
| 1693 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.2890625 / 0.08753019571304321 / 0.6450265564714699 | [NPY](tensors/0001693.npy) |
| 1694 | `model.layers.11.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1695 | `model.layers.11.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 92.5 / 0.05813509093390571 / 2.9115633056787376 | [NPY](tensors/0001695.npy) |
| 1696 | `model.layers.11.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.125 / 10.5625 / -0.0075221864972263575 / 1.390086984767029 | [NPY](tensors/0001696.npy) |
| 1697 | `model.layers.11.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 92.5 / 0.05813509093390571 / 2.9115633056787376 | [NPY](tensors/0001697.npy) |
| 1698 | `model.layers.11.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.75 / 41.0 / -0.0181894451379776 / 4.411799661308547 | [NPY](tensors/0001698.npy) |
| 1699 | `model.layers.11.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 92.5 / 0.05813509093390571 / 2.9115633056787376 | [NPY](tensors/0001699.npy) |
| 1700 | `model.layers.11.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.90625 / 7.9375 / -0.003063380718231201 / 2.742942868688812 | [NPY](tensors/0001700.npy) |
| 1701 | `model.layers.11.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.125 / 7.71875 / -0.034954970702528954 / 1.8966307863545093 | [NPY](tensors/0001701.npy) |
| 1702 | `model.layers.11.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.5 / 158.0 / 0.1694064610534244 / 5.283054458431712 | [NPY](tensors/0001702.npy) |
| 1703 | `model.layers.11.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.5 / 158.0 / 0.1694064610534244 / 5.283054458431712 | [NPY](tensors/0001703.npy) |
| 1704 | `model.layers.11.self_attn` | 14 | `output[1]` | [1, 64, 1, 887] | torch.bfloat16 → float32 | 2.7755575615628914e-14 / 0.8046875 / 0.0010914821375846407 / 0.00856813726548578 | [NPY](tensors/0001704.npy) |
| 1705 | `model.layers.11.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -370.0 / 478.0 / 0.6174989488389757 / 23.96905269418076 | [NPY](tensors/0001705.npy) |
| 1706 | `model.layers.11.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.453125 / 3.953125 / 0.016160041756100123 / 0.7217354006682414 | [NPY](tensors/0001706.npy) |
| 1707 | `model.layers.11.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.453125 / 3.953125 / 0.016160041756100123 / 0.7217354006682414 | [NPY](tensors/0001707.npy) |
| 1708 | `model.layers.11.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.453125 / 3.953125 / 0.016160041756100123 / 0.7217354006682414 | [NPY](tensors/0001708.npy) |
| 1709 | `model.layers.11.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1710 | `model.layers.11.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1711 | `model.layers.11.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1712 | `model.layers.11.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -86.5 / 172.0 / 0.18229693836636013 / 6.343863172355322 | [NPY](tensors/0001712.npy) |
| 1713 | `model.layers.11.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 172.0 / 0.18229693836636013 / 6.343863172355322 | [NPY](tensors/0001713.npy) |
| 1714 | `model.layers.11.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.28125 / 1.1171875 / -0.1394805908203125 / 0.5727766230453046 | [NPY](tensors/0001714.npy) |
| 1715 | `model.layers.11` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -456.0 / 648.0 / 0.8000020345052083 / 27.946893833918512 | [NPY](tensors/0001715.npy) |
| 1794 | `model.layers.11` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -148.0 / 197.0 / 0.4944254557291667 / 15.004118027765372 | [NPY](tensors/0001794.npy) |
| 1795 | `model.layers.11` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 888] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001795.npy) |
| 1796 | `model.layers.11` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.752716064453125 / 0.8717363915407874 | [NPY](tensors/0001796.npy) |
| 1797 | `model.layers.11` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / 0.1641445755958557 / 0.6760071928531548 | [NPY](tensors/0001797.npy) |
| 1798 | `model.layers.11` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 887.0 / 887.0 / 887.0 / 0.0 | [NPY](tensors/0001798.npy) |
| 1799 | `model.layers.11` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1800 | `model.layers.11` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1801 | `model.layers.11` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1802 | `model.layers.11.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -148.0 / 197.0 / 0.4944254557291667 / 15.004118027765372 | [NPY](tensors/0001802.npy) |
| 1803 | `model.layers.11.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.75 / 48.75 / 0.07591009669833713 / 2.402954876774282 | [NPY](tensors/0001803.npy) |
| 1804 | `model.layers.11.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.75 / 48.75 / 0.07591009669833713 / 2.402954876774282 | [NPY](tensors/0001804.npy) |
| 1805 | `model.layers.11.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 888] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001805.npy) |
| 1806 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 887.0 / 887.0 / 887.0 / 0.0 | [NPY](tensors/0001806.npy) |
| 1807 | `model.layers.11.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1808 | `model.layers.11.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1809 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.752716064453125 / 0.8717363915407874 | [NPY](tensors/0001809.npy) |
| 1810 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / 0.1641445755958557 / 0.6760071928531548 | [NPY](tensors/0001810.npy) |
| 1811 | `model.layers.11.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1812 | `model.layers.11.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.75 / 48.75 / 0.07591009669833713 / 2.402954876774282 | [NPY](tensors/0001812.npy) |
| 1813 | `model.layers.11.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.375 / 10.9375 / 0.02346089738421142 / 1.4982140054085344 | [NPY](tensors/0001813.npy) |
| 1814 | `model.layers.11.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.75 / 48.75 / 0.07591009669833713 / 2.402954876774282 | [NPY](tensors/0001814.npy) |
| 1815 | `model.layers.11.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.0 / 45.25 / 0.07165613770484924 / 4.989044803824869 | [NPY](tensors/0001815.npy) |
| 1816 | `model.layers.11.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.75 / 48.75 / 0.07591009669833713 / 2.402954876774282 | [NPY](tensors/0001816.npy) |
| 1817 | `model.layers.11.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.9375 / 9.0625 / 0.04107391834259033 / 2.7180097349952588 | [NPY](tensors/0001817.npy) |
| 1818 | `model.layers.11.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.34375 / 8.6875 / -0.03816000500228256 / 1.6709072814198498 | [NPY](tensors/0001818.npy) |
| 1819 | `model.layers.11.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -172.0 / 238.0 / 0.1565924843152364 / 8.249754699464592 | [NPY](tensors/0001819.npy) |
| 1820 | `model.layers.11.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -172.0 / 238.0 / 0.1565924843152364 / 8.249754699464592 | [NPY](tensors/0001820.npy) |
| 1821 | `model.layers.11.self_attn` | 15 | `output[1]` | [1, 64, 1, 888] | torch.bfloat16 → float32 | 7.638334409421077e-14 / 0.63671875 / 0.0010517271286056352 / 0.0069861445232964866 | [NPY](tensors/0001821.npy) |
| 1822 | `model.layers.11.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -320.0 / 394.0 / 0.6505350748697917 / 19.58786732988619 | [NPY](tensors/0001822.npy) |
| 1823 | `model.layers.11.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.171875 / 4.25 / 0.02107166846593221 / 0.7172293580065074 | [NPY](tensors/0001823.npy) |
| 1824 | `model.layers.11.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.171875 / 4.25 / 0.02107166846593221 / 0.7172293580065074 | [NPY](tensors/0001824.npy) |
| 1825 | `model.layers.11.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.171875 / 4.25 / 0.02107166846593221 / 0.7172293580065074 | [NPY](tensors/0001825.npy) |
| 1826 | `model.layers.11.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1827 | `model.layers.11.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1828 | `model.layers.11.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1829 | `model.layers.11.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -27.25 / 94.5 / 0.12398087448543972 / 4.8306496128330725 | [NPY](tensors/0001829.npy) |
| 1830 | `model.layers.11.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.25 / 94.5 / 0.12398087448543972 / 4.8306496128330725 | [NPY](tensors/0001830.npy) |
| 1831 | `model.layers.11.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.515625 / 1.734375 / -0.07094573974609375 / 0.6855979092378878 | [NPY](tensors/0001831.npy) |
| 1832 | `model.layers.11` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -226.0 / 388.0 / 0.7739312065972223 / 20.318754319639236 | [NPY](tensors/0001832.npy) |
| 1911 | `model.layers.11` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -252.0 / 362.0 / 0.2394716050889757 / 20.12373072857533 | [NPY](tensors/0001911.npy) |
| 1912 | `model.layers.11` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 889] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001912.npy) |
| 1913 | `model.layers.11` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6714019775390625 / 0.9432200886540145 | [NPY](tensors/0001913.npy) |
| 1914 | `model.layers.11` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.18380916118621826 / 0.659819262490622 | [NPY](tensors/0001914.npy) |
| 1915 | `model.layers.11` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 888.0 / 888.0 / 888.0 / 0.0 | [NPY](tensors/0001915.npy) |
| 1916 | `model.layers.11` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1917 | `model.layers.11` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1918 | `model.layers.11` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1919 | `model.layers.11.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -252.0 / 362.0 / 0.2394716050889757 / 20.12373072857533 | [NPY](tensors/0001919.npy) |
| 1920 | `model.layers.11.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.75 / 84.5 / 0.04817461172739665 / 2.7534911447503396 | [NPY](tensors/0001920.npy) |
| 1921 | `model.layers.11.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.75 / 84.5 / 0.04817461172739665 / 2.7534911447503396 | [NPY](tensors/0001921.npy) |
| 1922 | `model.layers.11.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 889] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001922.npy) |
| 1923 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 888.0 / 888.0 / 888.0 / 0.0 | [NPY](tensors/0001923.npy) |
| 1924 | `model.layers.11.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1925 | `model.layers.11.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1926 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6714019775390625 / 0.9432200886540145 | [NPY](tensors/0001926.npy) |
| 1927 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.18380916118621826 / 0.659819262490622 | [NPY](tensors/0001927.npy) |
| 1928 | `model.layers.11.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1929 | `model.layers.11.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.75 / 84.5 / 0.04817461172739665 / 2.7534911447503396 | [NPY](tensors/0001929.npy) |
| 1930 | `model.layers.11.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.3125 / 11.8125 / -0.004473099717870355 / 1.4358139432990291 | [NPY](tensors/0001930.npy) |
| 1931 | `model.layers.11.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.75 / 84.5 / 0.04817461172739665 / 2.7534911447503396 | [NPY](tensors/0001931.npy) |
| 1932 | `model.layers.11.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.0 / 44.75 / 0.008692383766174316 / 4.892592647418442 | [NPY](tensors/0001932.npy) |
| 1933 | `model.layers.11.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.75 / 84.5 / 0.04817461172739665 / 2.7534911447503396 | [NPY](tensors/0001933.npy) |
| 1934 | `model.layers.11.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -10.0625 / 9.9375 / -0.018192321062088013 / 2.7745255808310816 | [NPY](tensors/0001934.npy) |
| 1935 | `model.layers.11.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.96875 / 7.3125 / -0.048952959245070815 / 1.8091818030301734 | [NPY](tensors/0001935.npy) |
| 1936 | `model.layers.11.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -60.0 / 160.0 / 0.05801981820000542 / 5.244241271685765 | [NPY](tensors/0001936.npy) |
| 1937 | `model.layers.11.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -60.0 / 160.0 / 0.05801981820000542 / 5.244241271685765 | [NPY](tensors/0001937.npy) |
| 1938 | `model.layers.11.self_attn` | 16 | `output[1]` | [1, 64, 1, 889] | torch.bfloat16 → float32 | 6.140921104957897e-16 / 0.97265625 / 0.0010883490560818624 / 0.0077904373816355095 | [NPY](tensors/0001938.npy) |
| 1939 | `model.layers.11.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -284.0 / 376.0 / 0.29601609971788195 / 22.035161169599608 | [NPY](tensors/0001939.npy) |
| 1940 | `model.layers.11.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.734375 / 3.90625 / 0.003658963574303521 / 0.7342849963978387 | [NPY](tensors/0001940.npy) |
| 1941 | `model.layers.11.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.734375 / 3.90625 / 0.003658963574303521 / 0.7342849963978387 | [NPY](tensors/0001941.npy) |
| 1942 | `model.layers.11.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.734375 / 3.90625 / 0.003658963574303521 / 0.7342849963978387 | [NPY](tensors/0001942.npy) |
| 1943 | `model.layers.11.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1944 | `model.layers.11.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1945 | `model.layers.11.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1946 | `model.layers.11.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -138.0 / 142.0 / 0.1796863211525811 / 6.620268295852722 | [NPY](tensors/0001946.npy) |
| 1947 | `model.layers.11.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -138.0 / 142.0 / 0.1796863211525811 / 6.620268295852722 | [NPY](tensors/0001947.npy) |
| 1948 | `model.layers.11.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.25 / 1.2890625 / -0.09905624389648438 / 0.6267811771033629 | [NPY](tensors/0001948.npy) |
| 1949 | `model.layers.11` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -422.0 / 520.0 / 0.4761383056640625 / 26.128850836855776 | [NPY](tensors/0001949.npy) |
| 2028 | `model.layers.11` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -220.0 / 310.0 / 0.4575998094346788 / 17.939733392129174 | [NPY](tensors/0002028.npy) |
| 2029 | `model.layers.11` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 890] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002029.npy) |
| 2030 | `model.layers.11` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.61199951171875 / 1.0116022827243683 | [NPY](tensors/0002030.npy) |
| 2031 | `model.layers.11` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14778363704681396 / 0.6247390563478729 | [NPY](tensors/0002031.npy) |
| 2032 | `model.layers.11` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 889.0 / 889.0 / 889.0 / 0.0 | [NPY](tensors/0002032.npy) |
| 2033 | `model.layers.11` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2034 | `model.layers.11` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2035 | `model.layers.11` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2036 | `model.layers.11.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -220.0 / 310.0 / 0.4575998094346788 / 17.939733392129174 | [NPY](tensors/0002036.npy) |
| 2037 | `model.layers.11.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 81.0 / 0.06949303348859151 / 2.804693468583202 | [NPY](tensors/0002037.npy) |
| 2038 | `model.layers.11.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 81.0 / 0.06949303348859151 / 2.804693468583202 | [NPY](tensors/0002038.npy) |
| 2039 | `model.layers.11.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 890] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002039.npy) |
| 2040 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 889.0 / 889.0 / 889.0 / 0.0 | [NPY](tensors/0002040.npy) |
| 2041 | `model.layers.11.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2042 | `model.layers.11.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2043 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.61199951171875 / 1.0116022827243683 | [NPY](tensors/0002043.npy) |
| 2044 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14778363704681396 / 0.6247390563478729 | [NPY](tensors/0002044.npy) |
| 2045 | `model.layers.11.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2046 | `model.layers.11.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 81.0 / 0.06949303348859151 / 2.804693468583202 | [NPY](tensors/0002046.npy) |
| 2047 | `model.layers.11.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.1875 / 9.5625 / 0.015369532629847527 / 1.3935984254795823 | [NPY](tensors/0002047.npy) |
| 2048 | `model.layers.11.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 81.0 / 0.06949303348859151 / 2.804693468583202 | [NPY](tensors/0002048.npy) |
| 2049 | `model.layers.11.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.5 / 54.75 / 0.1473097801208496 / 5.142240681973674 | [NPY](tensors/0002049.npy) |
| 2050 | `model.layers.11.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 81.0 / 0.06949303348859151 / 2.804693468583202 | [NPY](tensors/0002050.npy) |
| 2051 | `model.layers.11.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.125 / 6.59375 / 0.029412809759378433 / 2.373859906490237 | [NPY](tensors/0002051.npy) |
| 2052 | `model.layers.11.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.125 / 6.96875 / -0.04618911072611809 / 1.6876212250957812 | [NPY](tensors/0002052.npy) |
| 2053 | `model.layers.11.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 137.0 / -0.007300657033920288 / 5.272612954531612 | [NPY](tensors/0002053.npy) |
| 2054 | `model.layers.11.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 137.0 / -0.007300657033920288 / 5.272612954531612 | [NPY](tensors/0002054.npy) |
| 2055 | `model.layers.11.self_attn` | 17 | `output[1]` | [1, 64, 1, 890] | torch.bfloat16 → float32 | 1.0231815394945443e-12 / 0.8984375 / 0.0010793323317756585 / 0.007231182078416113 | [NPY](tensors/0002055.npy) |
| 2056 | `model.layers.11.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -308.0 / 336.0 / 0.4512346055772569 / 20.312870459619052 | [NPY](tensors/0002056.npy) |
| 2057 | `model.layers.11.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.828125 / 3.21875 / 0.007910527123345269 / 0.7190190647024938 | [NPY](tensors/0002057.npy) |
| 2058 | `model.layers.11.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.828125 / 3.21875 / 0.007910527123345269 / 0.7190190647024938 | [NPY](tensors/0002058.npy) |
| 2059 | `model.layers.11.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.828125 / 3.21875 / 0.007910527123345269 / 0.7190190647024938 | [NPY](tensors/0002059.npy) |
| 2060 | `model.layers.11.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2061 | `model.layers.11.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2062 | `model.layers.11.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2063 | `model.layers.11.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -35.75 / 150.0 / 0.16360253228081598 / 5.839064720238153 | [NPY](tensors/0002063.npy) |
| 2064 | `model.layers.11.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.75 / 150.0 / 0.16360253228081598 / 5.839064720238153 | [NPY](tensors/0002064.npy) |
| 2065 | `model.layers.11.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.796875 / 1.453125 / -0.08838272094726562 / 0.7301438920443776 | [NPY](tensors/0002065.npy) |
| 2066 | `model.layers.11` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -344.0 / 486.0 / 0.6150316026475694 / 23.52102143574423 | [NPY](tensors/0002066.npy) |
| 2145 | `model.layers.11` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -318.0 / 358.0 / 0.6663925170898437 / 19.632488039769243 | [NPY](tensors/0002145.npy) |
| 2146 | `model.layers.11` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 891] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002146.npy) |
| 2147 | `model.layers.11` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6052932739257812 / 0.9920321858005083 | [NPY](tensors/0002147.npy) |
| 2148 | `model.layers.11` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.0962597131729126 / 0.670037121922543 | [NPY](tensors/0002148.npy) |
| 2149 | `model.layers.11` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 890.0 / 890.0 / 890.0 / 0.0 | [NPY](tensors/0002149.npy) |
| 2150 | `model.layers.11` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2151 | `model.layers.11` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2152 | `model.layers.11` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2153 | `model.layers.11.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -318.0 / 358.0 / 0.6663925170898437 / 19.632488039769243 | [NPY](tensors/0002153.npy) |
| 2154 | `model.layers.11.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 85.5 / 0.07450978689723545 / 3.092080743849907 | [NPY](tensors/0002154.npy) |
| 2155 | `model.layers.11.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 85.5 / 0.07450978689723545 / 3.092080743849907 | [NPY](tensors/0002155.npy) |
| 2156 | `model.layers.11.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 891] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002156.npy) |
| 2157 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 890.0 / 890.0 / 890.0 / 0.0 | [NPY](tensors/0002157.npy) |
| 2158 | `model.layers.11.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2159 | `model.layers.11.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2160 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6052932739257812 / 0.9920321858005083 | [NPY](tensors/0002160.npy) |
| 2161 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.0962597131729126 / 0.670037121922543 | [NPY](tensors/0002161.npy) |
| 2162 | `model.layers.11.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2163 | `model.layers.11.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 85.5 / 0.07450978689723545 / 3.092080743849907 | [NPY](tensors/0002163.npy) |
| 2164 | `model.layers.11.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.9375 / 8.6875 / 0.0077192948665469885 / 1.2983079895340501 | [NPY](tensors/0002164.npy) |
| 2165 | `model.layers.11.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 85.5 / 0.07450978689723545 / 3.092080743849907 | [NPY](tensors/0002165.npy) |
| 2166 | `model.layers.11.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.0 / 52.75 / 0.058502569794654846 / 4.853963657408374 | [NPY](tensors/0002166.npy) |
| 2167 | `model.layers.11.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 85.5 / 0.07450978689723545 / 3.092080743849907 | [NPY](tensors/0002167.npy) |
| 2168 | `model.layers.11.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.25 / 7.0625 / -0.09689679741859436 / 2.256270583533962 | [NPY](tensors/0002168.npy) |
| 2169 | `model.layers.11.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.4375 / 6.40625 / -0.05977554386481643 / 1.7307888515965788 | [NPY](tensors/0002169.npy) |
| 2170 | `model.layers.11.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.625 / 79.5 / 0.0949681176079644 / 4.469212756260468 | [NPY](tensors/0002170.npy) |
| 2171 | `model.layers.11.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.625 / 79.5 / 0.0949681176079644 / 4.469212756260468 | [NPY](tensors/0002171.npy) |
| 2172 | `model.layers.11.self_attn` | 18 | `output[1]` | [1, 64, 1, 891] | torch.bfloat16 → float32 | 2.433608869978343e-13 / 0.9609375 / 0.001064500587440234 / 0.008017601074435077 | [NPY](tensors/0002172.npy) |
| 2173 | `model.layers.11.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -310.0 / 328.0 / 0.7617469787597656 / 21.210505945677024 | [NPY](tensors/0002173.npy) |
| 2174 | `model.layers.11.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.0625 / 3.203125 / 0.025951912668016223 / 0.7066238991907348 | [NPY](tensors/0002174.npy) |
| 2175 | `model.layers.11.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.0625 / 3.203125 / 0.025951912668016223 / 0.7066238991907348 | [NPY](tensors/0002175.npy) |
| 2176 | `model.layers.11.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.0625 / 3.203125 / 0.025951912668016223 / 0.7066238991907348 | [NPY](tensors/0002176.npy) |
| 2177 | `model.layers.11.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2178 | `model.layers.11.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2179 | `model.layers.11.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2180 | `model.layers.11.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -148.0 / 216.0 / 0.15357030232747396 / 7.327039101549386 | [NPY](tensors/0002180.npy) |
| 2181 | `model.layers.11.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -148.0 / 216.0 / 0.15357030232747396 / 7.327039101549386 | [NPY](tensors/0002181.npy) |
| 2182 | `model.layers.11.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.109375 / 1.421875 / -0.09417724609375 / 0.6705762680982276 | [NPY](tensors/0002182.npy) |
| 2183 | `model.layers.11` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -458.0 / 544.0 / 0.9163855658637152 / 25.648929394264293 | [NPY](tensors/0002183.npy) |
| 2262 | `model.layers.11` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -296.0 / 380.0 / 0.0735812717013889 / 18.919209171401892 | [NPY](tensors/0002262.npy) |
| 2263 | `model.layers.11` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 892] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002263.npy) |
| 2264 | `model.layers.11` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6360321044921875 / 0.965021007945482 | [NPY](tensors/0002264.npy) |
| 2265 | `model.layers.11` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.07508242130279541 / 0.6832161663666542 | [NPY](tensors/0002265.npy) |
| 2266 | `model.layers.11` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 891.0 / 891.0 / 891.0 / 0.0 | [NPY](tensors/0002266.npy) |
| 2267 | `model.layers.11` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2268 | `model.layers.11` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2269 | `model.layers.11` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2270 | `model.layers.11.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -296.0 / 380.0 / 0.0735812717013889 / 18.919209171401892 | [NPY](tensors/0002270.npy) |
| 2271 | `model.layers.11.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 91.5 / 0.025949852334128484 / 3.149545699553739 | [NPY](tensors/0002271.npy) |
| 2272 | `model.layers.11.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 91.5 / 0.025949852334128484 / 3.149545699553739 | [NPY](tensors/0002272.npy) |
| 2273 | `model.layers.11.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 892] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002273.npy) |
| 2274 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 891.0 / 891.0 / 891.0 / 0.0 | [NPY](tensors/0002274.npy) |
| 2275 | `model.layers.11.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2276 | `model.layers.11.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2277 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6360321044921875 / 0.965021007945482 | [NPY](tensors/0002277.npy) |
| 2278 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.07508242130279541 / 0.6832161663666542 | [NPY](tensors/0002278.npy) |
| 2279 | `model.layers.11.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2280 | `model.layers.11.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 91.5 / 0.025949852334128484 / 3.149545699553739 | [NPY](tensors/0002280.npy) |
| 2281 | `model.layers.11.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.8125 / 9.4375 / 0.021575765684247017 / 1.2645248089791092 | [NPY](tensors/0002281.npy) |
| 2282 | `model.layers.11.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 91.5 / 0.025949852334128484 / 3.149545699553739 | [NPY](tensors/0002282.npy) |
| 2283 | `model.layers.11.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -41.25 / 51.75 / 0.021579086780548096 / 4.752244765410261 | [NPY](tensors/0002283.npy) |
| 2284 | `model.layers.11.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.0 / 91.5 / 0.025949852334128484 / 3.149545699553739 | [NPY](tensors/0002284.npy) |
| 2285 | `model.layers.11.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.5 / 8.0 / -0.01991581916809082 / 2.3622146310710974 | [NPY](tensors/0002285.npy) |
| 2286 | `model.layers.11.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.0 / 7.15625 / -0.037412778940051794 / 1.6777424237302097 | [NPY](tensors/0002286.npy) |
| 2287 | `model.layers.11.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 187.0 / 0.15901222229003906 / 5.649648661407041 | [NPY](tensors/0002287.npy) |
| 2288 | `model.layers.11.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 187.0 / 0.15901222229003906 / 5.649648661407041 | [NPY](tensors/0002288.npy) |
| 2289 | `model.layers.11.self_attn` | 19 | `output[1]` | [1, 64, 1, 892] | torch.bfloat16 → float32 | 1.0587086762825493e-12 / 0.9296875 / 0.0010343870252020819 / 0.007811378210859357 | [NPY](tensors/0002289.npy) |
| 2290 | `model.layers.11.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -292.0 / 436.0 / 0.23255886501736112 / 21.53496146470696 | [NPY](tensors/0002290.npy) |
| 2291 | `model.layers.11.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.046875 / 2.609375 / 0.008930358621809218 / 0.6293889133601972 | [NPY](tensors/0002291.npy) |
| 2292 | `model.layers.11.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.046875 / 2.609375 / 0.008930358621809218 / 0.6293889133601972 | [NPY](tensors/0002292.npy) |
| 2293 | `model.layers.11.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.046875 / 2.609375 / 0.008930358621809218 / 0.6293889133601972 | [NPY](tensors/0002293.npy) |
| 2294 | `model.layers.11.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2295 | `model.layers.11.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2296 | `model.layers.11.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2297 | `model.layers.11.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -136.0 / 149.0 / 0.05681587325202094 / 5.440152213022667 | [NPY](tensors/0002297.npy) |
| 2298 | `model.layers.11.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -136.0 / 149.0 / 0.05681587325202094 / 5.440152213022667 | [NPY](tensors/0002298.npy) |
| 2299 | `model.layers.11.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9140625 / 0.87890625 / -0.09326553344726562 / 0.5402929634253572 | [NPY](tensors/0002299.npy) |
| 2300 | `model.layers.11` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -428.0 / 556.0 / 0.28929206000434027 / 24.958875583248414 | [NPY](tensors/0002300.npy) |
| 2379 | `model.layers.11` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -296.0 / 394.0 / 0.5084862603081597 / 17.31762193096671 | [NPY](tensors/0002379.npy) |
| 2380 | `model.layers.11` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 893] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002380.npy) |
| 2381 | `model.layers.11` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.66259765625 / 0.9932594816118745 | [NPY](tensors/0002381.npy) |
| 2382 | `model.layers.11` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.09707069396972656 / 0.6118488978099847 | [NPY](tensors/0002382.npy) |
| 2383 | `model.layers.11` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 892.0 / 892.0 / 892.0 / 0.0 | [NPY](tensors/0002383.npy) |
| 2384 | `model.layers.11` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2385 | `model.layers.11` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2386 | `model.layers.11` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2387 | `model.layers.11.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -296.0 / 394.0 / 0.5084862603081597 / 17.31762193096671 | [NPY](tensors/0002387.npy) |
| 2388 | `model.layers.11.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.5 / 80.5 / 0.06529276346166929 / 3.1265291114556115 | [NPY](tensors/0002388.npy) |
| 2389 | `model.layers.11.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.5 / 80.5 / 0.06529276346166929 / 3.1265291114556115 | [NPY](tensors/0002389.npy) |
| 2390 | `model.layers.11.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 893] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002390.npy) |
| 2391 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 892.0 / 892.0 / 892.0 / 0.0 | [NPY](tensors/0002391.npy) |
| 2392 | `model.layers.11.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2393 | `model.layers.11.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2394 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.66259765625 / 0.9932594816118745 | [NPY](tensors/0002394.npy) |
| 2395 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.09707069396972656 / 0.6118488978099847 | [NPY](tensors/0002395.npy) |
| 2396 | `model.layers.11.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2397 | `model.layers.11.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.5 / 80.5 / 0.06529276346166929 / 3.1265291114556115 | [NPY](tensors/0002397.npy) |
| 2398 | `model.layers.11.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.53125 / 9.1875 / 0.059592035599052906 / 1.3120798312925976 | [NPY](tensors/0002398.npy) |
| 2399 | `model.layers.11.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.5 / 80.5 / 0.06529276346166929 / 3.1265291114556115 | [NPY](tensors/0002399.npy) |
| 2400 | `model.layers.11.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.25 / 52.75 / 0.12247474491596222 / 4.474622373461561 | [NPY](tensors/0002400.npy) |
| 2401 | `model.layers.11.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.5 / 80.5 / 0.06529276346166929 / 3.1265291114556115 | [NPY](tensors/0002401.npy) |
| 2402 | `model.layers.11.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.3125 / 6.625 / 0.021825537085533142 / 1.9468482538556051 | [NPY](tensors/0002402.npy) |
| 2403 | `model.layers.11.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.90625 / 8.25 / -0.03354948898777366 / 1.5750254679234996 | [NPY](tensors/0002403.npy) |
| 2404 | `model.layers.11.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.125 / 140.0 / 0.009701257281833225 / 5.143934467737951 | [NPY](tensors/0002404.npy) |
| 2405 | `model.layers.11.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.125 / 140.0 / 0.009701257281833225 / 5.143934467737951 | [NPY](tensors/0002405.npy) |
| 2406 | `model.layers.11.self_attn` | 20 | `output[1]` | [1, 64, 1, 893] | torch.bfloat16 → float32 | 4.298783551348606e-13 / 0.91796875 / 0.0010475460354862685 / 0.007068147749647665 | [NPY](tensors/0002406.npy) |
| 2407 | `model.layers.11.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -292.0 / 422.0 / 0.5189548068576388 / 19.57277382118352 | [NPY](tensors/0002407.npy) |
| 2408 | `model.layers.11.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.1875 / 3.5 / 0.021247037251790366 / 0.655721163738033 | [NPY](tensors/0002408.npy) |
| 2409 | `model.layers.11.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.1875 / 3.5 / 0.021247037251790366 / 0.655721163738033 | [NPY](tensors/0002409.npy) |
| 2410 | `model.layers.11.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.1875 / 3.5 / 0.021247037251790366 / 0.655721163738033 | [NPY](tensors/0002410.npy) |
| 2411 | `model.layers.11.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2412 | `model.layers.11.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2413 | `model.layers.11.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2414 | `model.layers.11.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -112.5 / 199.0 / 0.2222598287794325 / 6.416219986370126 | [NPY](tensors/0002414.npy) |
| 2415 | `model.layers.11.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -112.5 / 199.0 / 0.2222598287794325 / 6.416219986370126 | [NPY](tensors/0002415.npy) |
| 2416 | `model.layers.11.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3203125 / -0.06609916687011719 / 0.5847391525415596 | [NPY](tensors/0002416.npy) |
| 2417 | `model.layers.11` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -404.0 / 516.0 / 0.7411709255642361 / 23.74251372536039 | [NPY](tensors/0002417.npy) |
| 2496 | `model.layers.11` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -270.0 / 328.0 / 0.497641838921441 / 16.546098737439323 | [NPY](tensors/0002496.npy) |
| 2497 | `model.layers.11` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 894] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002497.npy) |
| 2498 | `model.layers.11` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6520881652832031 / 1.010377882001008 | [NPY](tensors/0002498.npy) |
| 2499 | `model.layers.11` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.328125 / 0.13654857873916626 / 0.5864893104951562 | [NPY](tensors/0002499.npy) |
| 2500 | `model.layers.11` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 893.0 / 893.0 / 893.0 / 0.0 | [NPY](tensors/0002500.npy) |
| 2501 | `model.layers.11` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2502 | `model.layers.11` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2503 | `model.layers.11` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2504 | `model.layers.11.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -270.0 / 328.0 / 0.497641838921441 / 16.546098737439323 | [NPY](tensors/0002504.npy) |
| 2505 | `model.layers.11.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 88.0 / 0.06599614686436123 / 3.1000364899682644 | [NPY](tensors/0002505.npy) |
| 2506 | `model.layers.11.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 88.0 / 0.06599614686436123 / 3.1000364899682644 | [NPY](tensors/0002506.npy) |
| 2507 | `model.layers.11.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 894] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002507.npy) |
| 2508 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 893.0 / 893.0 / 893.0 / 0.0 | [NPY](tensors/0002508.npy) |
| 2509 | `model.layers.11.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2510 | `model.layers.11.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2511 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6520881652832031 / 1.010377882001008 | [NPY](tensors/0002511.npy) |
| 2512 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.328125 / 0.13654857873916626 / 0.5864893104951562 | [NPY](tensors/0002512.npy) |
| 2513 | `model.layers.11.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2514 | `model.layers.11.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 88.0 / 0.06599614686436123 / 3.1000364899682644 | [NPY](tensors/0002514.npy) |
| 2515 | `model.layers.11.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.75 / 8.6875 / 0.06192125822417438 / 1.307138009111197 | [NPY](tensors/0002515.npy) |
| 2516 | `model.layers.11.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 88.0 / 0.06599614686436123 / 3.1000364899682644 | [NPY](tensors/0002516.npy) |
| 2517 | `model.layers.11.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.0 / 50.0 / 0.13409800827503204 / 4.409317514840551 | [NPY](tensors/0002517.npy) |
| 2518 | `model.layers.11.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 88.0 / 0.06599614686436123 / 3.1000364899682644 | [NPY](tensors/0002518.npy) |
| 2519 | `model.layers.11.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.09375 / 8.5625 / 0.013458847999572754 / 1.877626873342207 | [NPY](tensors/0002519.npy) |
| 2520 | `model.layers.11.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.5 / 8.5 / -0.04445946426130831 / 1.4265960462780019 | [NPY](tensors/0002520.npy) |
| 2521 | `model.layers.11.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 107.0 / -0.052556488249037 / 4.375898876486804 | [NPY](tensors/0002521.npy) |
| 2522 | `model.layers.11.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 107.0 / -0.052556488249037 / 4.375898876486804 | [NPY](tensors/0002522.npy) |
| 2523 | `model.layers.11.self_attn` | 21 | `output[1]` | [1, 64, 1, 894] | torch.bfloat16 → float32 | 1.3822276656583199e-14 / 0.78125 / 0.001032352669126109 / 0.00719560218706525 | [NPY](tensors/0002523.npy) |
| 2524 | `model.layers.11.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 344.0 / 0.4446804470486111 / 18.484272387866184 | [NPY](tensors/0002524.npy) |
| 2525 | `model.layers.11.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.03125 / 3.34375 / 0.016090081797705755 / 0.6439401870461269 | [NPY](tensors/0002525.npy) |
| 2526 | `model.layers.11.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.03125 / 3.34375 / 0.016090081797705755 / 0.6439401870461269 | [NPY](tensors/0002526.npy) |
| 2527 | `model.layers.11.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.03125 / 3.34375 / 0.016090081797705755 / 0.6439401870461269 | [NPY](tensors/0002527.npy) |
| 2528 | `model.layers.11.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2529 | `model.layers.11.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2530 | `model.layers.11.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2531 | `model.layers.11.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -87.0 / 133.0 / 0.12928834093941582 / 5.4977118702503365 | [NPY](tensors/0002531.npy) |
| 2532 | `model.layers.11.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 133.0 / 0.12928834093941582 / 5.4977118702503365 | [NPY](tensors/0002532.npy) |
| 2533 | `model.layers.11.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0078125 / 1.2421875 / -0.06153273582458496 / 0.5304117644755348 | [NPY](tensors/0002533.npy) |
| 2534 | `model.layers.11` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -400.0 / 424.0 / 0.5730497572157118 / 21.888159434624043 | [NPY](tensors/0002534.npy) |
| 2613 | `model.layers.11` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -376.0 / 394.0 / 0.2061234368218316 / 19.119587390249606 | [NPY](tensors/0002613.npy) |
| 2614 | `model.layers.11` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 895] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002614.npy) |
| 2615 | `model.layers.11` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6077041625976562 / 1.0143983018780602 | [NPY](tensors/0002615.npy) |
| 2616 | `model.layers.11` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.15405970811843872 / 0.6224309502943564 | [NPY](tensors/0002616.npy) |
| 2617 | `model.layers.11` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 894.0 / 894.0 / 894.0 / 0.0 | [NPY](tensors/0002617.npy) |
| 2618 | `model.layers.11` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2619 | `model.layers.11` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2620 | `model.layers.11` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2621 | `model.layers.11.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -376.0 / 394.0 / 0.2061234368218316 / 19.119587390249606 | [NPY](tensors/0002621.npy) |
| 2622 | `model.layers.11.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 96.5 / 0.027545838885837132 / 3.211454044981586 | [NPY](tensors/0002622.npy) |
| 2623 | `model.layers.11.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 96.5 / 0.027545838885837132 / 3.211454044981586 | [NPY](tensors/0002623.npy) |
| 2624 | `model.layers.11.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 895] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002624.npy) |
| 2625 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 894.0 / 894.0 / 894.0 / 0.0 | [NPY](tensors/0002625.npy) |
| 2626 | `model.layers.11.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2627 | `model.layers.11.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2628 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6077041625976562 / 1.0143983018780602 | [NPY](tensors/0002628.npy) |
| 2629 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.15405970811843872 / 0.6224309502943564 | [NPY](tensors/0002629.npy) |
| 2630 | `model.layers.11.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2631 | `model.layers.11.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 96.5 / 0.027545838885837132 / 3.211454044981586 | [NPY](tensors/0002631.npy) |
| 2632 | `model.layers.11.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.96875 / 8.375 / 0.07344330986961722 / 1.2583949091602746 | [NPY](tensors/0002632.npy) |
| 2633 | `model.layers.11.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 96.5 / 0.027545838885837132 / 3.211454044981586 | [NPY](tensors/0002633.npy) |
| 2634 | `model.layers.11.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.25 / 46.5 / 0.12075355648994446 / 4.324020173701479 | [NPY](tensors/0002634.npy) |
| 2635 | `model.layers.11.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 96.5 / 0.027545838885837132 / 3.211454044981586 | [NPY](tensors/0002635.npy) |
| 2636 | `model.layers.11.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.03125 / 6.0 / -0.10583364963531494 / 1.9775190669957001 | [NPY](tensors/0002636.npy) |
| 2637 | `model.layers.11.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.3125 / 5.40625 / -0.03229428603663109 / 1.2667251897503453 | [NPY](tensors/0002637.npy) |
| 2638 | `model.layers.11.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.0 / 86.5 / 0.07635030713346269 / 3.94431370625752 | [NPY](tensors/0002638.npy) |
| 2639 | `model.layers.11.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.0 / 86.5 / 0.07635030713346269 / 3.94431370625752 | [NPY](tensors/0002639.npy) |
| 2640 | `model.layers.11.self_attn` | 22 | `output[1]` | [1, 64, 1, 895] | torch.bfloat16 → float32 | 5.009326287108706e-13 / 0.94140625 / 0.0010444111671100832 / 0.007803330921088805 | [NPY](tensors/0002640.npy) |
| 2641 | `model.layers.11.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -428.0 / 444.0 / 0.2820314195421007 / 21.0445847012071 | [NPY](tensors/0002641.npy) |
| 2642 | `model.layers.11.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.078125 / 2.640625 / -0.00026339822345309785 / 0.6271968702225224 | [NPY](tensors/0002642.npy) |
| 2643 | `model.layers.11.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.078125 / 2.640625 / -0.00026339822345309785 / 0.6271968702225224 | [NPY](tensors/0002643.npy) |
| 2644 | `model.layers.11.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.078125 / 2.640625 / -0.00026339822345309785 / 0.6271968702225224 | [NPY](tensors/0002644.npy) |
| 2645 | `model.layers.11.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2646 | `model.layers.11.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2647 | `model.layers.11.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2648 | `model.layers.11.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -97.0 / 100.0 / 0.10532763534122043 / 4.36473111529278 | [NPY](tensors/0002648.npy) |
| 2649 | `model.layers.11.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.0 / 100.0 / 0.10532763534122043 / 4.36473111529278 | [NPY](tensors/0002649.npy) |
| 2650 | `model.layers.11.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.453125 / 0.77734375 / -0.11090397834777832 / 0.4699667350871661 | [NPY](tensors/0002650.npy) |
| 2651 | `model.layers.11` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -524.0 / 544.0 / 0.3883345709906684 / 23.69951453657364 | [NPY](tensors/0002651.npy) |
| 2730 | `model.layers.11` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -372.0 / 414.0 / 0.3099480523003472 / 18.628039893388912 | [NPY](tensors/0002730.npy) |
| 2731 | `model.layers.11` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 896] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002731.npy) |
| 2732 | `model.layers.11` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5635757446289062 / 1.0167091376095412 | [NPY](tensors/0002732.npy) |
| 2733 | `model.layers.11` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.13094085454940796 / 0.6637995182317289 | [NPY](tensors/0002733.npy) |
| 2734 | `model.layers.11` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 895.0 / 895.0 / 895.0 / 0.0 | [NPY](tensors/0002734.npy) |
| 2735 | `model.layers.11` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2736 | `model.layers.11` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2737 | `model.layers.11` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2738 | `model.layers.11.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -372.0 / 414.0 / 0.3099480523003472 / 18.628039893388912 | [NPY](tensors/0002738.npy) |
| 2739 | `model.layers.11.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.0 / 104.0 / 0.037818223900265166 / 3.3631455461859545 | [NPY](tensors/0002739.npy) |
| 2740 | `model.layers.11.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.0 / 104.0 / 0.037818223900265166 / 3.3631455461859545 | [NPY](tensors/0002740.npy) |
| 2741 | `model.layers.11.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 896] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002741.npy) |
| 2742 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 895.0 / 895.0 / 895.0 / 0.0 | [NPY](tensors/0002742.npy) |
| 2743 | `model.layers.11.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2744 | `model.layers.11.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2745 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5635757446289062 / 1.0167091376095412 | [NPY](tensors/0002745.npy) |
| 2746 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.13094085454940796 / 0.6637995182317289 | [NPY](tensors/0002746.npy) |
| 2747 | `model.layers.11.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2748 | `model.layers.11.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.0 / 104.0 / 0.037818223900265166 / 3.3631455461859545 | [NPY](tensors/0002748.npy) |
| 2749 | `model.layers.11.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.5625 / 8.1875 / 0.05584369238931686 / 1.174136757368785 | [NPY](tensors/0002749.npy) |
| 2750 | `model.layers.11.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.0 / 104.0 / 0.037818223900265166 / 3.3631455461859545 | [NPY](tensors/0002750.npy) |
| 2751 | `model.layers.11.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.5 / 55.25 / 0.06270331144332886 / 4.718142935169752 | [NPY](tensors/0002751.npy) |
| 2752 | `model.layers.11.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.0 / 104.0 / 0.037818223900265166 / 3.3631455461859545 | [NPY](tensors/0002752.npy) |
| 2753 | `model.layers.11.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -10.25 / 7.6875 / 0.005474311299622059 / 1.9738349123668313 | [NPY](tensors/0002753.npy) |
| 2754 | `model.layers.11.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.125 / 6.875 / -0.02662560110911727 / 1.3918903753892893 | [NPY](tensors/0002754.npy) |
| 2755 | `model.layers.11.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.0 / 77.5 / 0.05518445438808865 / 4.311315992015294 | [NPY](tensors/0002755.npy) |
| 2756 | `model.layers.11.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.0 / 77.5 / 0.05518445438808865 / 4.311315992015294 | [NPY](tensors/0002756.npy) |
| 2757 | `model.layers.11.self_attn` | 23 | `output[1]` | [1, 64, 1, 896] | torch.bfloat16 → float32 | 1.1146639167236572e-13 / 0.9296875 / 0.0010507861536102794 / 0.008733309967257439 | [NPY](tensors/0002757.npy) |
| 2758 | `model.layers.11.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -380.0 / 470.0 / 0.3651641845703125 / 20.623710380320365 | [NPY](tensors/0002758.npy) |
| 2759 | `model.layers.11.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.515625 / 3.046875 / 0.0033097121450636124 / 0.6304278695292198 | [NPY](tensors/0002759.npy) |
| 2760 | `model.layers.11.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.515625 / 3.046875 / 0.0033097121450636124 / 0.6304278695292198 | [NPY](tensors/0002760.npy) |
| 2761 | `model.layers.11.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.515625 / 3.046875 / 0.0033097121450636124 / 0.6304278695292198 | [NPY](tensors/0002761.npy) |
| 2762 | `model.layers.11.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2763 | `model.layers.11.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2764 | `model.layers.11.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2765 | `model.layers.11.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -220.0 / 175.0 / 0.10863217562437058 / 6.919912059167768 | [NPY](tensors/0002765.npy) |
| 2766 | `model.layers.11.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -220.0 / 175.0 / 0.10863217562437058 / 6.919912059167768 | [NPY](tensors/0002766.npy) |
| 2767 | `model.layers.11.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.59375 / 1.0390625 / -0.12800359725952148 / 0.5509210849455808 | [NPY](tensors/0002767.npy) |
| 2768 | `model.layers.11` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -600.0 / 644.0 / 0.47350523206922746 / 25.5866913240114 | [NPY](tensors/0002768.npy) |
| 2847 | `model.layers.11` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -314.0 / 366.0 / 0.37989603678385414 / 17.25835518832974 | [NPY](tensors/0002847.npy) |
| 2848 | `model.layers.11` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 897] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002848.npy) |
| 2849 | `model.layers.11` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5521621704101562 / 0.9747722822304562 | [NPY](tensors/0002849.npy) |
| 2850 | `model.layers.11` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.08557838201522827 / 0.7397982213081387 | [NPY](tensors/0002850.npy) |
| 2851 | `model.layers.11` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 896.0 / 896.0 / 896.0 / 0.0 | [NPY](tensors/0002851.npy) |
| 2852 | `model.layers.11` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2853 | `model.layers.11` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2854 | `model.layers.11` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2855 | `model.layers.11.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -314.0 / 366.0 / 0.37989603678385414 / 17.25835518832974 | [NPY](tensors/0002855.npy) |
| 2856 | `model.layers.11.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.5 / 99.5 / 0.05019188986884223 / 3.2343728830499927 | [NPY](tensors/0002856.npy) |
| 2857 | `model.layers.11.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.5 / 99.5 / 0.05019188986884223 / 3.2343728830499927 | [NPY](tensors/0002857.npy) |
| 2858 | `model.layers.11.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 897] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002858.npy) |
| 2859 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 896.0 / 896.0 / 896.0 / 0.0 | [NPY](tensors/0002859.npy) |
| 2860 | `model.layers.11.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2861 | `model.layers.11.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2862 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5521621704101562 / 0.9747722822304562 | [NPY](tensors/0002862.npy) |
| 2863 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.08557838201522827 / 0.7397982213081387 | [NPY](tensors/0002863.npy) |
| 2864 | `model.layers.11.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2865 | `model.layers.11.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.5 / 99.5 / 0.05019188986884223 / 3.2343728830499927 | [NPY](tensors/0002865.npy) |
| 2866 | `model.layers.11.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.875 / 9.6875 / 0.07740713655948639 / 1.2916292090233024 | [NPY](tensors/0002866.npy) |
| 2867 | `model.layers.11.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.5 / 99.5 / 0.05019188986884223 / 3.2343728830499927 | [NPY](tensors/0002867.npy) |
| 2868 | `model.layers.11.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -37.75 / 50.5 / 0.07082152366638184 / 4.363003549050024 | [NPY](tensors/0002868.npy) |
| 2869 | `model.layers.11.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.5 / 99.5 / 0.05019188986884223 / 3.2343728830499927 | [NPY](tensors/0002869.npy) |
| 2870 | `model.layers.11.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.375 / 7.5625 / -0.12170559167861938 / 1.9808076789006506 | [NPY](tensors/0002870.npy) |
| 2871 | `model.layers.11.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.375 / 7.625 / -0.05741517257411033 / 1.499563432624056 | [NPY](tensors/0002871.npy) |
| 2872 | `model.layers.11.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 72.5 / 0.002208273278342353 / 4.095061128508648 | [NPY](tensors/0002872.npy) |
| 2873 | `model.layers.11.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 72.5 / 0.002208273278342353 / 4.095061128508648 | [NPY](tensors/0002873.npy) |
| 2874 | `model.layers.11.self_attn` | 24 | `output[1]` | [1, 64, 1, 897] | torch.bfloat16 → float32 | 4.04121180963557e-14 / 0.94921875 / 0.0010477544847570374 / 0.011015273374914347 | [NPY](tensors/0002874.npy) |
| 2875 | `model.layers.11.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -294.0 / 354.0 / 0.3826582166883681 / 18.076754274270854 | [NPY](tensors/0002875.npy) |
| 2876 | `model.layers.11.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.65625 / 3.9375 / 0.012030545870463054 / 0.6737197272919057 | [NPY](tensors/0002876.npy) |
| 2877 | `model.layers.11.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.65625 / 3.9375 / 0.012030545870463054 / 0.6737197272919057 | [NPY](tensors/0002877.npy) |
| 2878 | `model.layers.11.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.65625 / 3.9375 / 0.012030545870463054 / 0.6737197272919057 | [NPY](tensors/0002878.npy) |
| 2879 | `model.layers.11.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2880 | `model.layers.11.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2881 | `model.layers.11.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2882 | `model.layers.11.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -158.0 / 153.0 / 0.1479388184017605 / 5.988800665888068 | [NPY](tensors/0002882.npy) |
| 2883 | `model.layers.11.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -158.0 / 153.0 / 0.1479388184017605 / 5.988800665888068 | [NPY](tensors/0002883.npy) |
| 2884 | `model.layers.11.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9375 / 0.78125 / -0.1410369873046875 / 0.5949199638833818 | [NPY](tensors/0002884.npy) |
| 2885 | `model.layers.11` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -452.0 / 508.0 / 0.5315775553385417 / 21.804339325234082 | [NPY](tensors/0002885.npy) |
| 2964 | `model.layers.11` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -250.0 / 318.0 / 0.6385988023546006 / 16.426866186909674 | [NPY](tensors/0002964.npy) |
| 2965 | `model.layers.11` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 898] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002965.npy) |
| 2966 | `model.layers.11` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.576171875 / 0.9367379826853268 | [NPY](tensors/0002966.npy) |
| 2967 | `model.layers.11` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05449014902114868 / 0.7727124058266066 | [NPY](tensors/0002967.npy) |
| 2968 | `model.layers.11` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 897.0 / 897.0 / 897.0 / 0.0 | [NPY](tensors/0002968.npy) |
| 2969 | `model.layers.11` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2970 | `model.layers.11` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2971 | `model.layers.11` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2972 | `model.layers.11.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -250.0 / 318.0 / 0.6385988023546006 / 16.426866186909674 | [NPY](tensors/0002972.npy) |
| 2973 | `model.layers.11.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 84.5 / 0.08050099809964498 / 2.943015107108649 | [NPY](tensors/0002973.npy) |
| 2974 | `model.layers.11.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 84.5 / 0.08050099809964498 / 2.943015107108649 | [NPY](tensors/0002974.npy) |
| 2975 | `model.layers.11.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 898] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002975.npy) |
| 2976 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 897.0 / 897.0 / 897.0 / 0.0 | [NPY](tensors/0002976.npy) |
| 2977 | `model.layers.11.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2978 | `model.layers.11.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2979 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.576171875 / 0.9367379826853268 | [NPY](tensors/0002979.npy) |
| 2980 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05449014902114868 / 0.7727124058266066 | [NPY](tensors/0002980.npy) |
| 2981 | `model.layers.11.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2982 | `model.layers.11.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 84.5 / 0.08050099809964498 / 2.943015107108649 | [NPY](tensors/0002982.npy) |
| 2983 | `model.layers.11.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.75 / 8.6875 / 0.06613635737448931 / 1.3536270110399415 | [NPY](tensors/0002983.npy) |
| 2984 | `model.layers.11.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 84.5 / 0.08050099809964498 / 2.943015107108649 | [NPY](tensors/0002984.npy) |
| 2985 | `model.layers.11.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.0 / 52.0 / 0.20059555768966675 / 4.854062641930361 | [NPY](tensors/0002985.npy) |
| 2986 | `model.layers.11.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 84.5 / 0.08050099809964498 / 2.943015107108649 | [NPY](tensors/0002986.npy) |
| 2987 | `model.layers.11.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.4375 / 6.5 / -0.03612220287322998 / 1.9807932758223834 | [NPY](tensors/0002987.npy) |
| 2988 | `model.layers.11.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 5.75 / -0.02997467014938593 / 1.2994475414880948 | [NPY](tensors/0002988.npy) |
| 2989 | `model.layers.11.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 76.5 / 0.0036639160580105253 / 3.7308791795850937 | [NPY](tensors/0002989.npy) |
| 2990 | `model.layers.11.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 76.5 / 0.0036639160580105253 / 3.7308791795850937 | [NPY](tensors/0002990.npy) |
| 2991 | `model.layers.11.self_attn` | 25 | `output[1]` | [1, 64, 1, 898] | torch.bfloat16 → float32 | 1.807620719773695e-11 / 0.8984375 / 0.0010502640337594648 / 0.007484116885676714 | [NPY](tensors/0002991.npy) |
| 2992 | `model.layers.11.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -247.0 / 326.0 / 0.6420271131727431 / 17.461588061961155 | [NPY](tensors/0002992.npy) |
| 2993 | `model.layers.11.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.828125 / 3.765625 / 0.014523422718048096 / 0.644326284701951 | [NPY](tensors/0002993.npy) |
| 2994 | `model.layers.11.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.828125 / 3.765625 / 0.014523422718048096 / 0.644326284701951 | [NPY](tensors/0002994.npy) |
| 2995 | `model.layers.11.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.828125 / 3.765625 / 0.014523422718048096 / 0.644326284701951 | [NPY](tensors/0002995.npy) |
| 2996 | `model.layers.11.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2997 | `model.layers.11.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2998 | `model.layers.11.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2999 | `model.layers.11.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -55.75 / 51.5 / 0.059319421980116104 / 3.888999999319729 | [NPY](tensors/0002999.npy) |
| 3000 | `model.layers.11.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.75 / 51.5 / 0.059319421980116104 / 3.888999999319729 | [NPY](tensors/0003000.npy) |
| 3001 | `model.layers.11.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.125 / 1.0625 / -0.1507272720336914 / 0.7172647382030747 | [NPY](tensors/0003001.npy) |
| 3002 | `model.layers.11` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -302.0 / 376.0 / 0.7011116875542535 / 19.132680995629162 | [NPY](tensors/0003002.npy) |
| 3081 | `model.layers.11` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -326.0 / 378.0 / 0.5529429965549045 / 18.502377166560265 | [NPY](tensors/0003081.npy) |
| 3082 | `model.layers.11` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 899] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003082.npy) |
| 3083 | `model.layers.11` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.60968017578125 / 0.9551838287803889 | [NPY](tensors/0003083.npy) |
| 3084 | `model.layers.11` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05779397487640381 / 0.7235452926755772 | [NPY](tensors/0003084.npy) |
| 3085 | `model.layers.11` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 898.0 / 898.0 / 898.0 / 0.0 | [NPY](tensors/0003085.npy) |
| 3086 | `model.layers.11` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3087 | `model.layers.11` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3088 | `model.layers.11` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3089 | `model.layers.11.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -326.0 / 378.0 / 0.5529429965549045 / 18.502377166560265 | [NPY](tensors/0003089.npy) |
| 3090 | `model.layers.11.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 95.5 / 0.062258609135945636 / 3.154257682509324 | [NPY](tensors/0003090.npy) |
| 3091 | `model.layers.11.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 95.5 / 0.062258609135945636 / 3.154257682509324 | [NPY](tensors/0003091.npy) |
| 3092 | `model.layers.11.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 899] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003092.npy) |
| 3093 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 898.0 / 898.0 / 898.0 / 0.0 | [NPY](tensors/0003093.npy) |
| 3094 | `model.layers.11.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3095 | `model.layers.11.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3096 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.60968017578125 / 0.9551838287803889 | [NPY](tensors/0003096.npy) |
| 3097 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05779397487640381 / 0.7235452926755772 | [NPY](tensors/0003097.npy) |
| 3098 | `model.layers.11.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3099 | `model.layers.11.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 95.5 / 0.062258609135945636 / 3.154257682509324 | [NPY](tensors/0003099.npy) |
| 3100 | `model.layers.11.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.5625 / 9.875 / 0.07686100283171982 / 1.2512170340421507 | [NPY](tensors/0003100.npy) |
| 3101 | `model.layers.11.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 95.5 / 0.062258609135945636 / 3.154257682509324 | [NPY](tensors/0003101.npy) |
| 3102 | `model.layers.11.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.0 / 52.75 / 0.10179898142814636 / 4.752366525125419 | [NPY](tensors/0003102.npy) |
| 3103 | `model.layers.11.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 95.5 / 0.062258609135945636 / 3.154257682509324 | [NPY](tensors/0003103.npy) |
| 3104 | `model.layers.11.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -10.625 / 6.78125 / -0.10424923896789551 / 2.200273647951385 | [NPY](tensors/0003104.npy) |
| 3105 | `model.layers.11.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.3125 / 7.9375 / -0.04017053241841495 / 1.5346253304703878 | [NPY](tensors/0003105.npy) |
| 3106 | `model.layers.11.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.625 / 75.0 / 0.18811752531263565 / 4.532872022010176 | [NPY](tensors/0003106.npy) |
| 3107 | `model.layers.11.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.625 / 75.0 / 0.18811752531263565 / 4.532872022010176 | [NPY](tensors/0003107.npy) |
| 3108 | `model.layers.11.self_attn` | 26 | `output[1]` | [1, 64, 1, 899] | torch.bfloat16 → float32 | 3.7481129311345285e-13 / 0.9609375 / 0.0010705841939291872 / 0.009445989338537622 | [NPY](tensors/0003108.npy) |
| 3109 | `model.layers.11.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -314.0 / 422.0 / 0.7407019721137152 / 20.235406747242912 | [NPY](tensors/0003109.npy) |
| 3110 | `model.layers.11.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.171875 / 0.02200027306874593 / 0.6540019044577147 | [NPY](tensors/0003110.npy) |
| 3111 | `model.layers.11.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.171875 / 0.02200027306874593 / 0.6540019044577147 | [NPY](tensors/0003111.npy) |
| 3112 | `model.layers.11.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.171875 / 0.02200027306874593 / 0.6540019044577147 | [NPY](tensors/0003112.npy) |
| 3113 | `model.layers.11.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3114 | `model.layers.11.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3115 | `model.layers.11.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3116 | `model.layers.11.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -151.0 / 141.0 / 0.05234695010715061 / 5.534069439506464 | [NPY](tensors/0003116.npy) |
| 3117 | `model.layers.11.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -151.0 / 141.0 / 0.05234695010715061 / 5.534069439506464 | [NPY](tensors/0003117.npy) |
| 3118 | `model.layers.11.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.59375 / 0.75 / -0.14220046997070312 / 0.6396336010379808 | [NPY](tensors/0003118.npy) |
| 3119 | `model.layers.11` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -464.0 / 528.0 / 0.7932960510253906 / 23.577779005680224 | [NPY](tensors/0003119.npy) |
| 3198 | `model.layers.11` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -223.0 / 314.0 / 0.3636480543348524 / 15.855101456470514 | [NPY](tensors/0003198.npy) |
| 3199 | `model.layers.11` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 900] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003199.npy) |
| 3200 | `model.layers.11` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.6215248107910156 / 0.953261420864228 | [NPY](tensors/0003200.npy) |
| 3201 | `model.layers.11` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.08504927158355713 / 0.7123271249161985 | [NPY](tensors/0003201.npy) |
| 3202 | `model.layers.11` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 899.0 / 899.0 / 899.0 / 0.0 | [NPY](tensors/0003202.npy) |
| 3203 | `model.layers.11` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3204 | `model.layers.11` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3205 | `model.layers.11` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3206 | `model.layers.11.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -223.0 / 314.0 / 0.3636480543348524 / 15.855101456470514 | [NPY](tensors/0003206.npy) |
| 3207 | `model.layers.11.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -74.0 / 93.0 / 0.06345567438337538 / 3.014099073870932 | [NPY](tensors/0003207.npy) |
| 3208 | `model.layers.11.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -74.0 / 93.0 / 0.06345567438337538 / 3.014099073870932 | [NPY](tensors/0003208.npy) |
| 3209 | `model.layers.11.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 900] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003209.npy) |
| 3210 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 899.0 / 899.0 / 899.0 / 0.0 | [NPY](tensors/0003210.npy) |
| 3211 | `model.layers.11.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3212 | `model.layers.11.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3213 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.6215248107910156 / 0.953261420864228 | [NPY](tensors/0003213.npy) |
| 3214 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.08504927158355713 / 0.7123271249161985 | [NPY](tensors/0003214.npy) |
| 3215 | `model.layers.11.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3216 | `model.layers.11.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -74.0 / 93.0 / 0.06345567438337538 / 3.014099073870932 | [NPY](tensors/0003216.npy) |
| 3217 | `model.layers.11.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.0 / 9.0 / 0.09700423968024552 / 1.395925802480786 | [NPY](tensors/0003217.npy) |
| 3218 | `model.layers.11.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -74.0 / 93.0 / 0.06345567438337538 / 3.014099073870932 | [NPY](tensors/0003218.npy) |
| 3219 | `model.layers.11.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -41.25 / 50.0 / 0.17050664871931076 / 4.727947749023017 | [NPY](tensors/0003219.npy) |
| 3220 | `model.layers.11.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -74.0 / 93.0 / 0.06345567438337538 / 3.014099073870932 | [NPY](tensors/0003220.npy) |
| 3221 | `model.layers.11.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.8125 / 8.9375 / -0.0828140377998352 / 2.2412625700108824 | [NPY](tensors/0003221.npy) |
| 3222 | `model.layers.11.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.0625 / 8.0625 / -0.05210267973598093 / 1.4825856125681305 | [NPY](tensors/0003222.npy) |
| 3223 | `model.layers.11.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.0 / 105.5 / -0.023249922858344183 / 4.570017576140333 | [NPY](tensors/0003223.npy) |
| 3224 | `model.layers.11.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.0 / 105.5 / -0.023249922858344183 / 4.570017576140333 | [NPY](tensors/0003224.npy) |
| 3225 | `model.layers.11.self_attn` | 27 | `output[1]` | [1, 64, 1, 900] | torch.bfloat16 → float32 | 2.3037127760972e-15 / 0.8515625 / 0.0010478699702832896 / 0.00829329800492383 | [NPY](tensors/0003225.npy) |
| 3226 | `model.layers.11.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -306.0 / 364.0 / 0.33991580539279515 / 18.243035284079617 | [NPY](tensors/0003226.npy) |
| 3227 | `model.layers.11.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.9375 / 3.0 / 0.011415934562683106 / 0.664855907946164 | [NPY](tensors/0003227.npy) |
| 3228 | `model.layers.11.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.9375 / 3.0 / 0.011415934562683106 / 0.664855907946164 | [NPY](tensors/0003228.npy) |
| 3229 | `model.layers.11.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.9375 / 3.0 / 0.011415934562683106 / 0.664855907946164 | [NPY](tensors/0003229.npy) |
| 3230 | `model.layers.11.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3231 | `model.layers.11.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3232 | `model.layers.11.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3233 | `model.layers.11.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -135.0 / 120.5 / 0.004102459218766954 / 5.698747693800624 | [NPY](tensors/0003233.npy) |
| 3234 | `model.layers.11.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -135.0 / 120.5 / 0.004102459218766954 / 5.698747693800624 | [NPY](tensors/0003234.npy) |
| 3235 | `model.layers.11.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.83203125 / 0.9140625 / -0.0759429931640625 / 0.4403148200532877 | [NPY](tensors/0003235.npy) |
| 3236 | `model.layers.11` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -440.0 / 484.0 / 0.34440850151909724 / 21.630960678720637 | [NPY](tensors/0003236.npy) |
| 3315 | `model.layers.11` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -178.0 / 251.0 / 0.5479502360026042 / 14.652781544640652 | [NPY](tensors/0003315.npy) |
| 3316 | `model.layers.11` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 901] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003316.npy) |
| 3317 | `model.layers.11` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.6053333282470703 / 0.9378499631722268 | [NPY](tensors/0003317.npy) |
| 3318 | `model.layers.11` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.10818588733673096 / 0.7432403804988892 | [NPY](tensors/0003318.npy) |
| 3319 | `model.layers.11` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 900.0 / 900.0 / 900.0 / 0.0 | [NPY](tensors/0003319.npy) |
| 3320 | `model.layers.11` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3321 | `model.layers.11` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3322 | `model.layers.11` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3323 | `model.layers.11.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -178.0 / 251.0 / 0.5479502360026042 / 14.652781544640652 | [NPY](tensors/0003323.npy) |
| 3324 | `model.layers.11.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.75 / 68.0 / 0.0810727768474155 / 2.8018518222136373 | [NPY](tensors/0003324.npy) |
| 3325 | `model.layers.11.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.75 / 68.0 / 0.0810727768474155 / 2.8018518222136373 | [NPY](tensors/0003325.npy) |
| 3326 | `model.layers.11.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 901] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003326.npy) |
| 3327 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 900.0 / 900.0 / 900.0 / 0.0 | [NPY](tensors/0003327.npy) |
| 3328 | `model.layers.11.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3329 | `model.layers.11.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3330 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.6053333282470703 / 0.9378499631722268 | [NPY](tensors/0003330.npy) |
| 3331 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.10818588733673096 / 0.7432403804988892 | [NPY](tensors/0003331.npy) |
| 3332 | `model.layers.11.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3333 | `model.layers.11.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.75 / 68.0 / 0.0810727768474155 / 2.8018518222136373 | [NPY](tensors/0003333.npy) |
| 3334 | `model.layers.11.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.625 / 10.6875 / 0.04646274575497955 / 1.401426468296228 | [NPY](tensors/0003334.npy) |
| 3335 | `model.layers.11.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.75 / 68.0 / 0.0810727768474155 / 2.8018518222136373 | [NPY](tensors/0003335.npy) |
| 3336 | `model.layers.11.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.5 / 56.25 / 0.1914381980895996 / 5.251344452596549 | [NPY](tensors/0003336.npy) |
| 3337 | `model.layers.11.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.75 / 68.0 / 0.0810727768474155 / 2.8018518222136373 | [NPY](tensors/0003337.npy) |
| 3338 | `model.layers.11.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.625 / 7.5 / -0.0002529025077819824 / 2.5056999260994592 | [NPY](tensors/0003338.npy) |
| 3339 | `model.layers.11.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0 / 6.34375 / -0.03952035866677761 / 1.5124868794709518 | [NPY](tensors/0003339.npy) |
| 3340 | `model.layers.11.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -79.0 / 181.0 / 0.12535335752699112 / 5.832102474797641 | [NPY](tensors/0003340.npy) |
| 3341 | `model.layers.11.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -79.0 / 181.0 / 0.12535335752699112 / 5.832102474797641 | [NPY](tensors/0003341.npy) |
| 3342 | `model.layers.11.self_attn` | 28 | `output[1]` | [1, 64, 1, 901] | torch.bfloat16 → float32 | 1.2789769243681803e-12 / 0.6796875 / 0.0010180796350152833 / 0.0064933909297536455 | [NPY](tensors/0003342.npy) |
| 3343 | `model.layers.11.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -256.0 / 314.0 / 0.6741880628797743 / 17.92860393239094 | [NPY](tensors/0003343.npy) |
| 3344 | `model.layers.11.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.65625 / 3.046875 / 0.027510793672667608 / 0.6728695312388215 | [NPY](tensors/0003344.npy) |
| 3345 | `model.layers.11.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.65625 / 3.046875 / 0.027510793672667608 / 0.6728695312388215 | [NPY](tensors/0003345.npy) |
| 3346 | `model.layers.11.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.65625 / 3.046875 / 0.027510793672667608 / 0.6728695312388215 | [NPY](tensors/0003346.npy) |
| 3347 | `model.layers.11.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3348 | `model.layers.11.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3349 | `model.layers.11.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3350 | `model.layers.11.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -44.25 / 102.5 / 0.14969298044840496 / 4.865790943574513 | [NPY](tensors/0003350.npy) |
| 3351 | `model.layers.11.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 102.5 / 0.14969298044840496 / 4.865790943574513 | [NPY](tensors/0003351.npy) |
| 3352 | `model.layers.11.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.765625 / 1.2890625 / -0.0826253890991211 / 0.5897766065164944 | [NPY](tensors/0003352.npy) |
| 3353 | `model.layers.11` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -270.0 / 416.0 / 0.8233823988172743 / 20.332749397174517 | [NPY](tensors/0003353.npy) |
| 3432 | `model.layers.11` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -260.0 / 304.0 / 0.40498216417100696 / 14.612589830519006 | [NPY](tensors/0003432.npy) |
| 3433 | `model.layers.11` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 902] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003433.npy) |
| 3434 | `model.layers.11` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.58184814453125 / 0.9804601915905449 | [NPY](tensors/0003434.npy) |
| 3435 | `model.layers.11` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / 0.11050879955291748 / 0.7066672716698735 | [NPY](tensors/0003435.npy) |
| 3436 | `model.layers.11` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 901.0 / 901.0 / 901.0 / 0.0 | [NPY](tensors/0003436.npy) |
| 3437 | `model.layers.11` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3438 | `model.layers.11` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3439 | `model.layers.11` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3440 | `model.layers.11.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -260.0 / 304.0 / 0.40498216417100696 / 14.612589830519006 | [NPY](tensors/0003440.npy) |
| 3441 | `model.layers.11.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 73.5 / 0.05387994845708211 / 3.0665535494532263 | [NPY](tensors/0003441.npy) |
| 3442 | `model.layers.11.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 73.5 / 0.05387994845708211 / 3.0665535494532263 | [NPY](tensors/0003442.npy) |
| 3443 | `model.layers.11.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 902] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003443.npy) |
| 3444 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 901.0 / 901.0 / 901.0 / 0.0 | [NPY](tensors/0003444.npy) |
| 3445 | `model.layers.11.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3446 | `model.layers.11.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3447 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.58184814453125 / 0.9804601915905449 | [NPY](tensors/0003447.npy) |
| 3448 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / 0.11050879955291748 / 0.7066672716698735 | [NPY](tensors/0003448.npy) |
| 3449 | `model.layers.11.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3450 | `model.layers.11.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 73.5 / 0.05387994845708211 / 3.0665535494532263 | [NPY](tensors/0003450.npy) |
| 3451 | `model.layers.11.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.0 / 8.3125 / 0.0492432109604124 / 1.3758321526450799 | [NPY](tensors/0003451.npy) |
| 3452 | `model.layers.11.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 73.5 / 0.05387994845708211 / 3.0665535494532263 | [NPY](tensors/0003452.npy) |
| 3453 | `model.layers.11.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.5 / 52.0 / 0.22281178832054138 / 4.732623595395612 | [NPY](tensors/0003453.npy) |
| 3454 | `model.layers.11.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 73.5 / 0.05387994845708211 / 3.0665535494532263 | [NPY](tensors/0003454.npy) |
| 3455 | `model.layers.11.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.5625 / 6.46875 / 0.038210272789001465 / 1.960407839151282 | [NPY](tensors/0003455.npy) |
| 3456 | `model.layers.11.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.8125 / 6.1875 / -0.0276816263794899 / 1.3823294250212863 | [NPY](tensors/0003456.npy) |
| 3457 | `model.layers.11.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.25 / 105.0 / 0.1462253597047594 / 3.869311427527819 | [NPY](tensors/0003457.npy) |
| 3458 | `model.layers.11.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.25 / 105.0 / 0.1462253597047594 / 3.869311427527819 | [NPY](tensors/0003458.npy) |
| 3459 | `model.layers.11.self_attn` | 29 | `output[1]` | [1, 64, 1, 902] | torch.bfloat16 → float32 | 4.320099833421409e-11 / 0.8828125 / 0.0010257820177268103 / 0.006302071719447031 | [NPY](tensors/0003459.npy) |
| 3460 | `model.layers.11.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -236.0 / 312.0 / 0.5514105055067274 / 15.68715642865671 | [NPY](tensors/0003460.npy) |
| 3461 | `model.layers.11.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.421875 / 4.03125 / 0.022173193428251477 / 0.6543990587074664 | [NPY](tensors/0003461.npy) |
| 3462 | `model.layers.11.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.421875 / 4.03125 / 0.022173193428251477 / 0.6543990587074664 | [NPY](tensors/0003462.npy) |
| 3463 | `model.layers.11.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.421875 / 4.03125 / 0.022173193428251477 / 0.6543990587074664 | [NPY](tensors/0003463.npy) |
| 3464 | `model.layers.11.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3465 | `model.layers.11.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3466 | `model.layers.11.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3467 | `model.layers.11.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -48.75 / 33.5 / 0.027148689164055717 / 3.382491314573232 | [NPY](tensors/0003467.npy) |
| 3468 | `model.layers.11.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 33.5 / 0.027148689164055717 / 3.382491314573232 | [NPY](tensors/0003468.npy) |
| 3469 | `model.layers.11.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.09375 / 1.03125 / -0.14590120315551758 / 0.662408682245859 | [NPY](tensors/0003469.npy) |
| 3470 | `model.layers.11` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -284.0 / 340.0 / 0.5784618801540798 / 16.871604389384697 | [NPY](tensors/0003470.npy) |
| 3549 | `model.layers.11` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -364.0 / 476.0 / 0.41300616794162326 / 19.36541251972509 | [NPY](tensors/0003549.npy) |
| 3550 | `model.layers.11` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 903] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003550.npy) |
| 3551 | `model.layers.11` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.57342529296875 / 1.011353752766297 | [NPY](tensors/0003551.npy) |
| 3552 | `model.layers.11` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.10230749845504761 / 0.668999264851671 | [NPY](tensors/0003552.npy) |
| 3553 | `model.layers.11` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 902.0 / 902.0 / 902.0 / 0.0 | [NPY](tensors/0003553.npy) |
| 3554 | `model.layers.11` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3555 | `model.layers.11` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3556 | `model.layers.11` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3557 | `model.layers.11.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -364.0 / 476.0 / 0.41300616794162326 / 19.36541251972509 | [NPY](tensors/0003557.npy) |
| 3558 | `model.layers.11.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 115.0 / 0.05026991830931769 / 3.3835373281984054 | [NPY](tensors/0003558.npy) |
| 3559 | `model.layers.11.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 115.0 / 0.05026991830931769 / 3.3835373281984054 | [NPY](tensors/0003559.npy) |
| 3560 | `model.layers.11.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 903] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003560.npy) |
| 3561 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 902.0 / 902.0 / 902.0 / 0.0 | [NPY](tensors/0003561.npy) |
| 3562 | `model.layers.11.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3563 | `model.layers.11.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3564 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.57342529296875 / 1.011353752766297 | [NPY](tensors/0003564.npy) |
| 3565 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.10230749845504761 / 0.668999264851671 | [NPY](tensors/0003565.npy) |
| 3566 | `model.layers.11.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3567 | `model.layers.11.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 115.0 / 0.05026991830931769 / 3.3835373281984054 | [NPY](tensors/0003567.npy) |
| 3568 | `model.layers.11.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.59375 / 9.125 / 0.08453381201252341 / 1.1937761866590473 | [NPY](tensors/0003568.npy) |
| 3569 | `model.layers.11.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 115.0 / 0.05026991830931769 / 3.3835373281984054 | [NPY](tensors/0003569.npy) |
| 3570 | `model.layers.11.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.75 / 48.5 / 0.10934829711914062 / 4.484910861310972 | [NPY](tensors/0003570.npy) |
| 3571 | `model.layers.11.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 115.0 / 0.05026991830931769 / 3.3835373281984054 | [NPY](tensors/0003571.npy) |
| 3572 | `model.layers.11.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.5 / 8.75 / -0.15044432878494263 / 2.2079492388978195 | [NPY](tensors/0003572.npy) |
| 3573 | `model.layers.11.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.25 / 7.96875 / -0.05560306692495942 / 1.4748118210171912 | [NPY](tensors/0003573.npy) |
| 3574 | `model.layers.11.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 62.25 / 0.018223134676615398 / 3.864267282787092 | [NPY](tensors/0003574.npy) |
| 3575 | `model.layers.11.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 62.25 / 0.018223134676615398 / 3.864267282787092 | [NPY](tensors/0003575.npy) |
| 3576 | `model.layers.11.self_attn` | 30 | `output[1]` | [1, 64, 1, 903] | torch.bfloat16 → float32 | 1.5654144647214707e-14 / 0.96484375 / 0.0010555623130290514 / 0.00884416500563922 | [NPY](tensors/0003576.npy) |
| 3577 | `model.layers.11.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -362.0 / 488.0 / 0.43133748372395836 / 20.769106336196195 | [NPY](tensors/0003577.npy) |
| 3578 | `model.layers.11.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.578125 / 2.53125 / 0.006299375163184272 / 0.6334439943780582 | [NPY](tensors/0003578.npy) |
| 3579 | `model.layers.11.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.578125 / 2.53125 / 0.006299375163184272 / 0.6334439943780582 | [NPY](tensors/0003579.npy) |
| 3580 | `model.layers.11.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.578125 / 2.53125 / 0.006299375163184272 / 0.6334439943780582 | [NPY](tensors/0003580.npy) |
| 3581 | `model.layers.11.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3582 | `model.layers.11.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3583 | `model.layers.11.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3584 | `model.layers.11.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -183.0 / 162.0 / 0.034435335795084634 / 6.045530544060995 | [NPY](tensors/0003584.npy) |
| 3585 | `model.layers.11.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -183.0 / 162.0 / 0.034435335795084634 / 6.045530544060995 | [NPY](tensors/0003585.npy) |
| 3586 | `model.layers.11.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.76171875 / 0.92578125 / -0.07789421081542969 / 0.40790975666733637 | [NPY](tensors/0003586.npy) |
| 3587 | `model.layers.11` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -544.0 / 648.0 / 0.4657630072699653 / 24.77180042265968 | [NPY](tensors/0003587.npy) |
| 3666 | `model.layers.11` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -370.0 / 404.0 / 0.23331086900499132 / 18.157406811196573 | [NPY](tensors/0003666.npy) |
| 3667 | `model.layers.11` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 904] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003667.npy) |
| 3668 | `model.layers.11` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.576141357421875 / 0.9960825148117132 | [NPY](tensors/0003668.npy) |
| 3669 | `model.layers.11` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.10725325345993042 / 0.6890912510284947 | [NPY](tensors/0003669.npy) |
| 3670 | `model.layers.11` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 903.0 / 903.0 / 903.0 / 0.0 | [NPY](tensors/0003670.npy) |
| 3671 | `model.layers.11` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3672 | `model.layers.11` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3673 | `model.layers.11` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3674 | `model.layers.11.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -370.0 / 404.0 / 0.23331086900499132 / 18.157406811196573 | [NPY](tensors/0003674.npy) |
| 3675 | `model.layers.11.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -107.0 / 104.5 / 0.037399999300638836 / 3.3782766550876193 | [NPY](tensors/0003675.npy) |
| 3676 | `model.layers.11.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -107.0 / 104.5 / 0.037399999300638836 / 3.3782766550876193 | [NPY](tensors/0003676.npy) |
| 3677 | `model.layers.11.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 904] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003677.npy) |
| 3678 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 903.0 / 903.0 / 903.0 / 0.0 | [NPY](tensors/0003678.npy) |
| 3679 | `model.layers.11.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3680 | `model.layers.11.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3681 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.576141357421875 / 0.9960825148117132 | [NPY](tensors/0003681.npy) |
| 3682 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.10725325345993042 / 0.6890912510284947 | [NPY](tensors/0003682.npy) |
| 3683 | `model.layers.11.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3684 | `model.layers.11.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -107.0 / 104.5 / 0.037399999300638836 / 3.3782766550876193 | [NPY](tensors/0003684.npy) |
| 3685 | `model.layers.11.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.6875 / 9.875 / 0.06235969439148903 / 1.2385367508404708 | [NPY](tensors/0003685.npy) |
| 3686 | `model.layers.11.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -107.0 / 104.5 / 0.037399999300638836 / 3.3782766550876193 | [NPY](tensors/0003686.npy) |
| 3687 | `model.layers.11.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.25 / 47.25 / 0.12305030133575201 / 4.256068170936515 | [NPY](tensors/0003687.npy) |
| 3688 | `model.layers.11.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -107.0 / 104.5 / 0.037399999300638836 / 3.3782766550876193 | [NPY](tensors/0003688.npy) |
| 3689 | `model.layers.11.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.0625 / 5.625 / -0.03835463523864746 / 1.853521329531626 | [NPY](tensors/0003689.npy) |
| 3690 | `model.layers.11.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 5.40625 / -0.025637882528826594 / 1.2899519667791182 | [NPY](tensors/0003690.npy) |
| 3691 | `model.layers.11.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.75 / 75.0 / 0.0006181346045600044 / 3.6989958308949302 | [NPY](tensors/0003691.npy) |
| 3692 | `model.layers.11.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.75 / 75.0 / 0.0006181346045600044 / 3.6989958308949302 | [NPY](tensors/0003692.npy) |
| 3693 | `model.layers.11.self_attn` | 31 | `output[1]` | [1, 64, 1, 904] | torch.bfloat16 → float32 | 1.4210854715202004e-11 / 0.90234375 / 0.0010309982447100337 / 0.007830657012096221 | [NPY](tensors/0003693.npy) |
| 3694 | `model.layers.11.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -354.0 / 416.0 / 0.23363206651475693 / 19.362379896716924 | [NPY](tensors/0003694.npy) |
| 3695 | `model.layers.11.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.546875 / 3.171875 / 0.0050540751881069605 / 0.6469566797894588 | [NPY](tensors/0003695.npy) |
| 3696 | `model.layers.11.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.546875 / 3.171875 / 0.0050540751881069605 / 0.6469566797894588 | [NPY](tensors/0003696.npy) |
| 3697 | `model.layers.11.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.546875 / 3.171875 / 0.0050540751881069605 / 0.6469566797894588 | [NPY](tensors/0003697.npy) |
| 3698 | `model.layers.11.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3699 | `model.layers.11.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3700 | `model.layers.11.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3701 | `model.layers.11.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -188.0 / 175.0 / 0.08477889166937934 / 6.986564576068428 | [NPY](tensors/0003701.npy) |
| 3702 | `model.layers.11.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -188.0 / 175.0 / 0.08477889166937934 / 6.986564576068428 | [NPY](tensors/0003702.npy) |
| 3703 | `model.layers.11.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.375 / 1.0859375 / -0.12871170043945312 / 0.5512412276485155 | [NPY](tensors/0003703.npy) |
| 3704 | `model.layers.11` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -544.0 / 584.0 / 0.3171827528211806 / 24.195723281524426 | [NPY](tensors/0003704.npy) |
| 3783 | `model.layers.11` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -235.0 / 304.0 / 0.45170199076334633 / 14.9515512350874 | [NPY](tensors/0003783.npy) |
| 3784 | `model.layers.11` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 905] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003784.npy) |
| 3785 | `model.layers.11` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.56591796875 / 1.009767041675747 | [NPY](tensors/0003785.npy) |
| 3786 | `model.layers.11` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.28125 / 0.13484972715377808 / 0.6728120153629138 | [NPY](tensors/0003786.npy) |
| 3787 | `model.layers.11` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 904.0 / 904.0 / 904.0 / 0.0 | [NPY](tensors/0003787.npy) |
| 3788 | `model.layers.11` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3789 | `model.layers.11` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3790 | `model.layers.11` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3791 | `model.layers.11.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -235.0 / 304.0 / 0.45170199076334633 / 14.9515512350874 | [NPY](tensors/0003791.npy) |
| 3792 | `model.layers.11.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 91.0 / 0.06936476363076104 / 3.1057419139517273 | [NPY](tensors/0003792.npy) |
| 3793 | `model.layers.11.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 91.0 / 0.06936476363076104 / 3.1057419139517273 | [NPY](tensors/0003793.npy) |
| 3794 | `model.layers.11.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 905] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003794.npy) |
| 3795 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 904.0 / 904.0 / 904.0 / 0.0 | [NPY](tensors/0003795.npy) |
| 3796 | `model.layers.11.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3797 | `model.layers.11.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3798 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.56591796875 / 1.009767041675747 | [NPY](tensors/0003798.npy) |
| 3799 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.28125 / 0.13484972715377808 / 0.6728120153629138 | [NPY](tensors/0003799.npy) |
| 3800 | `model.layers.11.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3801 | `model.layers.11.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 91.0 / 0.06936476363076104 / 3.1057419139517273 | [NPY](tensors/0003801.npy) |
| 3802 | `model.layers.11.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.78125 / 9.75 / 0.021918705198913813 / 1.3121062265266696 | [NPY](tensors/0003802.npy) |
| 3803 | `model.layers.11.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 91.0 / 0.06936476363076104 / 3.1057419139517273 | [NPY](tensors/0003803.npy) |
| 3804 | `model.layers.11.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.25 / 54.25 / 0.19885939359664917 / 4.829113920426829 | [NPY](tensors/0003804.npy) |
| 3805 | `model.layers.11.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 91.0 / 0.06936476363076104 / 3.1057419139517273 | [NPY](tensors/0003805.npy) |
| 3806 | `model.layers.11.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.59375 / 7.28125 / 0.05462002754211426 / 2.0472101620803507 | [NPY](tensors/0003806.npy) |
| 3807 | `model.layers.11.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5 / 5.75 / -0.027869751560501754 / 1.3787441566181937 | [NPY](tensors/0003807.npy) |
| 3808 | `model.layers.11.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.5 / 131.0 / 0.16418873998853895 / 4.1647768414366055 | [NPY](tensors/0003808.npy) |
| 3809 | `model.layers.11.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.5 / 131.0 / 0.16418873998853895 / 4.1647768414366055 | [NPY](tensors/0003809.npy) |
| 3810 | `model.layers.11.self_attn` | 32 | `output[1]` | [1, 64, 1, 905] | torch.bfloat16 → float32 | 4.1654857341200113e-10 / 0.70703125 / 0.0010196261705019633 / 0.00594355122711944 | [NPY](tensors/0003810.npy) |
| 3811 | `model.layers.11.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -276.0 / 336.0 / 0.6166112263997395 / 17.07950021629061 | [NPY](tensors/0003811.npy) |
| 3812 | `model.layers.11.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.40625 / 2.71875 / 0.01886354751057095 / 0.6286697369919981 | [NPY](tensors/0003812.npy) |
| 3813 | `model.layers.11.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.40625 / 2.71875 / 0.01886354751057095 / 0.6286697369919981 | [NPY](tensors/0003813.npy) |
| 3814 | `model.layers.11.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.40625 / 2.71875 / 0.01886354751057095 / 0.6286697369919981 | [NPY](tensors/0003814.npy) |
| 3815 | `model.layers.11.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3816 | `model.layers.11.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3817 | `model.layers.11.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3818 | `model.layers.11.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -29.0 / 45.5 / -0.029608806636598376 / 3.4974255261629827 | [NPY](tensors/0003818.npy) |
| 3819 | `model.layers.11.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 45.5 / -0.029608806636598376 / 3.4974255261629827 | [NPY](tensors/0003819.npy) |
| 3820 | `model.layers.11.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.25 / 0.95703125 / -0.1291046142578125 / 0.6154977883586492 | [NPY](tensors/0003820.npy) |
| 3821 | `model.layers.11` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -246.0 / 348.0 / 0.5870143466525608 / 17.727527039919266 | [NPY](tensors/0003821.npy) |
| 3900 | `model.layers.11` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -304.0 / 414.0 / 0.1967044406467014 / 18.73396173324796 | [NPY](tensors/0003900.npy) |
| 3901 | `model.layers.11` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 906] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003901.npy) |
| 3902 | `model.layers.11` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.517730712890625 / 1.0482222047318746 | [NPY](tensors/0003902.npy) |
| 3903 | `model.layers.11` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.1620463728904724 / 0.645396390931362 | [NPY](tensors/0003903.npy) |
| 3904 | `model.layers.11` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 905.0 / 905.0 / 905.0 / 0.0 | [NPY](tensors/0003904.npy) |
| 3905 | `model.layers.11` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3906 | `model.layers.11` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3907 | `model.layers.11` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3908 | `model.layers.11.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -304.0 / 414.0 / 0.1967044406467014 / 18.73396173324796 | [NPY](tensors/0003908.npy) |
| 3909 | `model.layers.11.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 103.5 / 0.033994716737005444 / 3.1451260579247 | [NPY](tensors/0003909.npy) |
| 3910 | `model.layers.11.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 103.5 / 0.033994716737005444 / 3.1451260579247 | [NPY](tensors/0003910.npy) |
| 3911 | `model.layers.11.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 906] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003911.npy) |
| 3912 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 905.0 / 905.0 / 905.0 / 0.0 | [NPY](tensors/0003912.npy) |
| 3913 | `model.layers.11.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3914 | `model.layers.11.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3915 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.517730712890625 / 1.0482222047318746 | [NPY](tensors/0003915.npy) |
| 3916 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.1620463728904724 / 0.645396390931362 | [NPY](tensors/0003916.npy) |
| 3917 | `model.layers.11.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3918 | `model.layers.11.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 103.5 / 0.033994716737005444 / 3.1451260579247 | [NPY](tensors/0003918.npy) |
| 3919 | `model.layers.11.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.5625 / 10.375 / 0.07624807713727932 / 1.2647692509973487 | [NPY](tensors/0003919.npy) |
| 3920 | `model.layers.11.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 103.5 / 0.033994716737005444 / 3.1451260579247 | [NPY](tensors/0003920.npy) |
| 3921 | `model.layers.11.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.25 / 49.75 / 0.11213505268096924 / 4.7336522291336545 | [NPY](tensors/0003921.npy) |
| 3922 | `model.layers.11.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 103.5 / 0.033994716737005444 / 3.1451260579247 | [NPY](tensors/0003922.npy) |
| 3923 | `model.layers.11.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -11.8125 / 8.875 / -0.005089133977890015 / 2.3421144568945174 | [NPY](tensors/0003923.npy) |
| 3924 | `model.layers.11.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.0 / 5.3125 / -0.010045553557574749 / 1.3296321001360027 | [NPY](tensors/0003924.npy) |
| 3925 | `model.layers.11.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -132.0 / 146.0 / 0.02961991760465834 / 5.316059888483623 | [NPY](tensors/0003925.npy) |
| 3926 | `model.layers.11.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -132.0 / 146.0 / 0.02961991760465834 / 5.316059888483623 | [NPY](tensors/0003926.npy) |
| 3927 | `model.layers.11.self_attn` | 33 | `output[1]` | [1, 64, 1, 906] | torch.bfloat16 → float32 | 9.094947017729282e-12 / 0.89453125 / 0.001058866336103671 / 0.007620646541669427 | [NPY](tensors/0003927.npy) |
| 3928 | `model.layers.11.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -436.0 / 496.0 / 0.22647425333658855 / 22.169190190934533 | [NPY](tensors/0003928.npy) |
| 3929 | `model.layers.11.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.484375 / 2.828125 / 0.002398045857747396 / 0.6044567892301054 | [NPY](tensors/0003929.npy) |
| 3930 | `model.layers.11.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.484375 / 2.828125 / 0.002398045857747396 / 0.6044567892301054 | [NPY](tensors/0003930.npy) |
| 3931 | `model.layers.11.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.484375 / 2.828125 / 0.002398045857747396 / 0.6044567892301054 | [NPY](tensors/0003931.npy) |
| 3932 | `model.layers.11.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3933 | `model.layers.11.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3934 | `model.layers.11.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3935 | `model.layers.11.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -31.75 / 44.0 / -0.026799752314885458 / 2.9956555191074346 | [NPY](tensors/0003935.npy) |
| 3936 | `model.layers.11.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.75 / 44.0 / -0.026799752314885458 / 2.9956555191074346 | [NPY](tensors/0003936.npy) |
| 3937 | `model.layers.11.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6953125 / 0.734375 / -0.1215057373046875 / 0.5242996044294654 | [NPY](tensors/0003937.npy) |
| 3938 | `model.layers.11` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -446.0 / 502.0 / 0.19857669406467013 / 22.966305523654253 | [NPY](tensors/0003938.npy) |
| 4017 | `model.layers.11` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -201.0 / 278.0 / 0.29531639946831595 / 15.931931704596808 | [NPY](tensors/0004017.npy) |
| 4018 | `model.layers.11` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 907] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004018.npy) |
| 4019 | `model.layers.11` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.439208984375 / 1.0785913702628929 | [NPY](tensors/0004019.npy) |
| 4020 | `model.layers.11` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.15223175287246704 / 0.6555427416634236 | [NPY](tensors/0004020.npy) |
| 4021 | `model.layers.11` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 906.0 / 906.0 / 906.0 / 0.0 | [NPY](tensors/0004021.npy) |
| 4022 | `model.layers.11` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4023 | `model.layers.11` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4024 | `model.layers.11` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4025 | `model.layers.11.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -201.0 / 278.0 / 0.29531639946831595 / 15.931931704596808 | [NPY](tensors/0004025.npy) |
| 4026 | `model.layers.11.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.25 / 82.0 / 0.05833086172739665 / 2.780130850626099 | [NPY](tensors/0004026.npy) |
| 4027 | `model.layers.11.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.25 / 82.0 / 0.05833086172739665 / 2.780130850626099 | [NPY](tensors/0004027.npy) |
| 4028 | `model.layers.11.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 907] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004028.npy) |
| 4029 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 906.0 / 906.0 / 906.0 / 0.0 | [NPY](tensors/0004029.npy) |
| 4030 | `model.layers.11.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4031 | `model.layers.11.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4032 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.439208984375 / 1.0785913702628929 | [NPY](tensors/0004032.npy) |
| 4033 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.15223175287246704 / 0.6555427416634236 | [NPY](tensors/0004033.npy) |
| 4034 | `model.layers.11.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4035 | `model.layers.11.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.25 / 82.0 / 0.05833086172739665 / 2.780130850626099 | [NPY](tensors/0004035.npy) |
| 4036 | `model.layers.11.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.5 / 10.5 / 0.08936697244644165 / 1.5461703531154736 | [NPY](tensors/0004036.npy) |
| 4037 | `model.layers.11.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.25 / 82.0 / 0.05833086172739665 / 2.780130850626099 | [NPY](tensors/0004037.npy) |
| 4038 | `model.layers.11.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -37.75 / 47.0 / 0.19690925255417824 / 4.567076317411395 | [NPY](tensors/0004038.npy) |
| 4039 | `model.layers.11.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.25 / 82.0 / 0.05833086172739665 / 2.780130850626099 | [NPY](tensors/0004039.npy) |
| 4040 | `model.layers.11.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.3125 / 11.6875 / -0.10089050233364105 / 2.5424605174214148 | [NPY](tensors/0004040.npy) |
| 4041 | `model.layers.11.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.9375 / 10.375 / -0.05908077140338719 / 1.6525500017829973 | [NPY](tensors/0004041.npy) |
| 4042 | `model.layers.11.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -111.5 / 144.0 / -0.008505535125732423 / 5.532100060794401 | [NPY](tensors/0004042.npy) |
| 4043 | `model.layers.11.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -111.5 / 144.0 / -0.008505535125732423 / 5.532100060794401 | [NPY](tensors/0004043.npy) |
| 4044 | `model.layers.11.self_attn` | 34 | `output[1]` | [1, 64, 1, 907] | torch.bfloat16 → float32 | 2.168404344971009e-19 / 0.859375 / 0.0010318307771622116 / 0.00861196351953381 | [NPY](tensors/0004044.npy) |
| 4045 | `model.layers.11.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -288.0 / 344.0 / 0.28693822224934895 / 18.70260164395063 | [NPY](tensors/0004045.npy) |
| 4046 | `model.layers.11.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.625 / 2.578125 / 0.009671790732277764 / 0.7022806595086988 | [NPY](tensors/0004046.npy) |
| 4047 | `model.layers.11.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.625 / 2.578125 / 0.009671790732277764 / 0.7022806595086988 | [NPY](tensors/0004047.npy) |
| 4048 | `model.layers.11.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.625 / 2.578125 / 0.009671790732277764 / 0.7022806595086988 | [NPY](tensors/0004048.npy) |
| 4049 | `model.layers.11.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4050 | `model.layers.11.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4051 | `model.layers.11.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4052 | `model.layers.11.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -103.5 / 120.0 / 0.05325304137335883 / 5.5739632006435 | [NPY](tensors/0004052.npy) |
| 4053 | `model.layers.11.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.5 / 120.0 / 0.05325304137335883 / 5.5739632006435 | [NPY](tensors/0004053.npy) |
| 4054 | `model.layers.11.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.9765625 / 1.125 / -0.06772375106811523 / 0.5192243161990833 | [NPY](tensors/0004054.npy) |
| 4055 | `model.layers.11` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -392.0 / 444.0 / 0.3400048149956597 / 21.98223062867998 | [NPY](tensors/0004055.npy) |
| 4134 | `model.layers.11` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -340.0 / 414.0 / 0.3481530083550347 / 18.269801881012746 | [NPY](tensors/0004134.npy) |
| 4135 | `model.layers.11` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 908] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004135.npy) |
| 4136 | `model.layers.11` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.369232177734375 / 1.1234051302987014 | [NPY](tensors/0004136.npy) |
| 4137 | `model.layers.11` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.328125 / 0.08310973644256592 / 0.636302055198959 | [NPY](tensors/0004137.npy) |
| 4138 | `model.layers.11` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 907.0 / 907.0 / 907.0 / 0.0 | [NPY](tensors/0004138.npy) |
| 4139 | `model.layers.11` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4140 | `model.layers.11` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4141 | `model.layers.11` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4142 | `model.layers.11.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -340.0 / 414.0 / 0.3481530083550347 / 18.269801881012746 | [NPY](tensors/0004142.npy) |
| 4143 | `model.layers.11.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 106.0 / 0.048772574795616995 / 3.2817169731447198 | [NPY](tensors/0004143.npy) |
| 4144 | `model.layers.11.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 106.0 / 0.048772574795616995 / 3.2817169731447198 | [NPY](tensors/0004144.npy) |
| 4145 | `model.layers.11.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 908] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004145.npy) |
| 4146 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 907.0 / 907.0 / 907.0 / 0.0 | [NPY](tensors/0004146.npy) |
| 4147 | `model.layers.11.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4148 | `model.layers.11.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4149 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.369232177734375 / 1.1234051302987014 | [NPY](tensors/0004149.npy) |
| 4150 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.328125 / 0.08310973644256592 / 0.636302055198959 | [NPY](tensors/0004150.npy) |
| 4151 | `model.layers.11.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4152 | `model.layers.11.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 106.0 / 0.048772574795616995 / 3.2817169731447198 | [NPY](tensors/0004152.npy) |
| 4153 | `model.layers.11.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.4375 / 8.8125 / 0.0737062415573746 / 1.2907995399330963 | [NPY](tensors/0004153.npy) |
| 4154 | `model.layers.11.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 106.0 / 0.048772574795616995 / 3.2817169731447198 | [NPY](tensors/0004154.npy) |
| 4155 | `model.layers.11.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.0 / 45.5 / 0.08090758323669434 / 4.353535521216824 | [NPY](tensors/0004155.npy) |
| 4156 | `model.layers.11.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 106.0 / 0.048772574795616995 / 3.2817169731447198 | [NPY](tensors/0004156.npy) |
| 4157 | `model.layers.11.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.0 / 5.78125 / -0.008061051368713379 / 1.7801105130631312 | [NPY](tensors/0004157.npy) |
| 4158 | `model.layers.11.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.03125 / 5.34375 / -0.032331248512491584 / 1.3053135398387772 | [NPY](tensors/0004158.npy) |
| 4159 | `model.layers.11.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.5 / 98.0 / 0.033849541346232095 / 4.003504869904531 | [NPY](tensors/0004159.npy) |
| 4160 | `model.layers.11.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.5 / 98.0 / 0.033849541346232095 / 4.003504869904531 | [NPY](tensors/0004160.npy) |
| 4161 | `model.layers.11.self_attn` | 35 | `output[1]` | [1, 64, 1, 908] | torch.bfloat16 → float32 | 5.467848396278896e-15 / 0.90625 / 0.001014699952318926 / 0.007847085744141762 | [NPY](tensors/0004161.npy) |
| 4162 | `model.layers.11.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -404.0 / 432.0 / 0.3824123806423611 / 20.293585692630778 | [NPY](tensors/0004162.npy) |
| 4163 | `model.layers.11.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.78125 / 2.53125 / 0.00471353100405799 / 0.6143358382277969 | [NPY](tensors/0004163.npy) |
| 4164 | `model.layers.11.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.78125 / 2.53125 / 0.00471353100405799 / 0.6143358382277969 | [NPY](tensors/0004164.npy) |
| 4165 | `model.layers.11.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.78125 / 2.53125 / 0.00471353100405799 / 0.6143358382277969 | [NPY](tensors/0004165.npy) |
| 4166 | `model.layers.11.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4167 | `model.layers.11.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4168 | `model.layers.11.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4169 | `model.layers.11.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -105.0 / 89.5 / 0.07530356115765041 / 4.091648916338622 | [NPY](tensors/0004169.npy) |
| 4170 | `model.layers.11.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.0 / 89.5 / 0.07530356115765041 / 4.091648916338622 | [NPY](tensors/0004170.npy) |
| 4171 | `model.layers.11.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.953125 / 0.859375 / -0.057834625244140625 / 0.46635766568483067 | [NPY](tensors/0004171.npy) |
| 4172 | `model.layers.11` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -508.0 / 520.0 / 0.45837554931640623 / 22.807379165815128 | [NPY](tensors/0004172.npy) |
| 4251 | `model.layers.11` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -394.0 / 418.0 / 0.20732591417100693 / 18.90560004568462 | [NPY](tensors/0004251.npy) |
| 4252 | `model.layers.11` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 909] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004252.npy) |
| 4253 | `model.layers.11` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.353973388671875 / 1.129845910800914 | [NPY](tensors/0004253.npy) |
| 4254 | `model.layers.11` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.328125 / -0.02260303497314453 / 0.6391623929271725 | [NPY](tensors/0004254.npy) |
| 4255 | `model.layers.11` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 908.0 / 908.0 / 908.0 / 0.0 | [NPY](tensors/0004255.npy) |
| 4256 | `model.layers.11` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4257 | `model.layers.11` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4258 | `model.layers.11` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4259 | `model.layers.11.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -394.0 / 418.0 / 0.20732591417100693 / 18.90560004568462 | [NPY](tensors/0004259.npy) |
| 4260 | `model.layers.11.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.5 / 103.5 / 0.027107028828726874 / 3.3654519221709505 | [NPY](tensors/0004260.npy) |
| 4261 | `model.layers.11.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.5 / 103.5 / 0.027107028828726874 / 3.3654519221709505 | [NPY](tensors/0004261.npy) |
| 4262 | `model.layers.11.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 909] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004262.npy) |
| 4263 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 908.0 / 908.0 / 908.0 / 0.0 | [NPY](tensors/0004263.npy) |
| 4264 | `model.layers.11.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4265 | `model.layers.11.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4266 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.353973388671875 / 1.129845910800914 | [NPY](tensors/0004266.npy) |
| 4267 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.328125 / -0.02260303497314453 / 0.6391623929271725 | [NPY](tensors/0004267.npy) |
| 4268 | `model.layers.11.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4269 | `model.layers.11.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.5 / 103.5 / 0.027107028828726874 / 3.3654519221709505 | [NPY](tensors/0004269.npy) |
| 4270 | `model.layers.11.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.71875 / 8.875 / 0.061710432171821594 / 1.1947728172410244 | [NPY](tensors/0004270.npy) |
| 4271 | `model.layers.11.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.5 / 103.5 / 0.027107028828726874 / 3.3654519221709505 | [NPY](tensors/0004271.npy) |
| 4272 | `model.layers.11.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.5 / 44.5 / 0.11524808406829834 / 4.209244520994963 | [NPY](tensors/0004272.npy) |
| 4273 | `model.layers.11.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.5 / 103.5 / 0.027107028828726874 / 3.3654519221709505 | [NPY](tensors/0004273.npy) |
| 4274 | `model.layers.11.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.875 / 4.90625 / -0.01642589271068573 / 1.642031724631989 | [NPY](tensors/0004274.npy) |
| 4275 | `model.layers.11.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0 / 4.9375 / -0.00012289569713175297 / 1.201803971116317 | [NPY](tensors/0004275.npy) |
| 4276 | `model.layers.11.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.5 / 105.5 / 0.11702042950524225 / 4.2560288546026985 | [NPY](tensors/0004276.npy) |
| 4277 | `model.layers.11.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.5 / 105.5 / 0.11702042950524225 / 4.2560288546026985 | [NPY](tensors/0004277.npy) |
| 4278 | `model.layers.11.self_attn` | 36 | `output[1]` | [1, 64, 1, 909] | torch.bfloat16 → float32 | 1.2434497875801753e-13 / 0.92578125 / 0.0009922154762111585 / 0.007400108538035338 | [NPY](tensors/0004278.npy) |
| 4279 | `model.layers.11.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -478.0 / 466.0 / 0.32445526123046875 / 21.3679668204762 | [NPY](tensors/0004279.npy) |
| 4280 | `model.layers.11.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 2.3125 / 0.005187866422865126 / 0.586230897855137 | [NPY](tensors/0004280.npy) |
| 4281 | `model.layers.11.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 2.3125 / 0.005187866422865126 / 0.586230897855137 | [NPY](tensors/0004281.npy) |
| 4282 | `model.layers.11.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.8125 / 2.3125 / 0.005187866422865126 / 0.586230897855137 | [NPY](tensors/0004282.npy) |
| 4283 | `model.layers.11.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4284 | `model.layers.11.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4285 | `model.layers.11.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4286 | `model.layers.11.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -109.0 / 76.0 / -0.0036585741572909883 / 3.5786066524019686 | [NPY](tensors/0004286.npy) |
| 4287 | `model.layers.11.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 76.0 / -0.0036585741572909883 / 3.5786066524019686 | [NPY](tensors/0004287.npy) |
| 4288 | `model.layers.11.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.1171875 / 0.6328125 / -0.0932464599609375 / 0.4171410017005419 | [NPY](tensors/0004288.npy) |
| 4289 | `model.layers.11` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -588.0 / 544.0 / 0.3216801961263021 / 23.64420798944099 | [NPY](tensors/0004289.npy) |
| 4368 | `model.layers.11` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -380.0 / 326.0 / 0.22536595662434897 / 17.678730805210787 | [NPY](tensors/0004368.npy) |
| 4369 | `model.layers.11` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 910] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004369.npy) |
| 4370 | `model.layers.11` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.40557861328125 / 1.0657613414649296 | [NPY](tensors/0004370.npy) |
| 4371 | `model.layers.11` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.2734375 / -0.11394071578979492 / 0.7046058830066726 | [NPY](tensors/0004371.npy) |
| 4372 | `model.layers.11` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 909.0 / 909.0 / 909.0 / 0.0 | [NPY](tensors/0004372.npy) |
| 4373 | `model.layers.11` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4374 | `model.layers.11` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4375 | `model.layers.11` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4376 | `model.layers.11.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -380.0 / 326.0 / 0.22536595662434897 / 17.678730805210787 | [NPY](tensors/0004376.npy) |
| 4377 | `model.layers.11.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -113.0 / 79.0 / 0.02381594909562005 / 3.288338787168057 | [NPY](tensors/0004377.npy) |
| 4378 | `model.layers.11.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -113.0 / 79.0 / 0.02381594909562005 / 3.288338787168057 | [NPY](tensors/0004378.npy) |
| 4379 | `model.layers.11.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 910] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004379.npy) |
| 4380 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 909.0 / 909.0 / 909.0 / 0.0 | [NPY](tensors/0004380.npy) |
| 4381 | `model.layers.11.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4382 | `model.layers.11.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4383 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.40557861328125 / 1.0657613414649296 | [NPY](tensors/0004383.npy) |
| 4384 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.2734375 / -0.11394071578979492 / 0.7046058830066726 | [NPY](tensors/0004384.npy) |
| 4385 | `model.layers.11.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4386 | `model.layers.11.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -113.0 / 79.0 / 0.02381594909562005 / 3.288338787168057 | [NPY](tensors/0004386.npy) |
| 4387 | `model.layers.11.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.78125 / 7.9375 / 0.059597996121738106 / 1.2023191751119562 | [NPY](tensors/0004387.npy) |
| 4388 | `model.layers.11.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -113.0 / 79.0 / 0.02381594909562005 / 3.288338787168057 | [NPY](tensors/0004388.npy) |
| 4389 | `model.layers.11.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -46.5 / 57.75 / 0.15643572807312012 / 5.063365883821647 | [NPY](tensors/0004389.npy) |
| 4390 | `model.layers.11.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -113.0 / 79.0 / 0.02381594909562005 / 3.288338787168057 | [NPY](tensors/0004390.npy) |
| 4391 | `model.layers.11.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.21875 / 6.09375 / 0.0010546445846557617 / 1.9747628269640014 | [NPY](tensors/0004391.npy) |
| 4392 | `model.layers.11.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.71875 / 7.4375 / 0.008266325923614204 / 1.315613355583922 | [NPY](tensors/0004392.npy) |
| 4393 | `model.layers.11.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.0 / 129.0 / 0.10872628026538425 / 5.736000571243284 | [NPY](tensors/0004393.npy) |
| 4394 | `model.layers.11.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.0 / 129.0 / 0.10872628026538425 / 5.736000571243284 | [NPY](tensors/0004394.npy) |
| 4395 | `model.layers.11.self_attn` | 37 | `output[1]` | [1, 64, 1, 910] | torch.bfloat16 → float32 | 3.7969627442180354e-14 / 0.90234375 / 0.0010278799031164616 / 0.008442610277135706 | [NPY](tensors/0004395.npy) |
| 4396 | `model.layers.11.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -478.0 / 428.0 / 0.3339825100368924 / 21.316173844193496 | [NPY](tensors/0004396.npy) |
| 4397 | `model.layers.11.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.984375 / 3.921875 / 0.005261242389678955 / 0.6000857506499168 | [NPY](tensors/0004397.npy) |
| 4398 | `model.layers.11.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.984375 / 3.921875 / 0.005261242389678955 / 0.6000857506499168 | [NPY](tensors/0004398.npy) |
| 4399 | `model.layers.11.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.984375 / 3.921875 / 0.005261242389678955 / 0.6000857506499168 | [NPY](tensors/0004399.npy) |
| 4400 | `model.layers.11.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4401 | `model.layers.11.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4402 | `model.layers.11.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4403 | `model.layers.11.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -126.0 / 153.0 / 0.12210817270808749 / 5.571524056305457 | [NPY](tensors/0004403.npy) |
| 4404 | `model.layers.11.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -126.0 / 153.0 / 0.12210817270808749 / 5.571524056305457 | [NPY](tensors/0004404.npy) |
| 4405 | `model.layers.11.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.09375 / 0.83984375 / -0.16617298126220703 / 0.6224935199868254 | [NPY](tensors/0004405.npy) |
| 4406 | `model.layers.11` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -604.0 / 536.0 / 0.4553097195095486 / 25.133165224246174 | [NPY](tensors/0004406.npy) |
| 4485 | `model.layers.11` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -352.0 / 368.0 / 0.42422188652886283 / 17.92671616121019 | [NPY](tensors/0004485.npy) |
| 4486 | `model.layers.11` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 911] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004486.npy) |
| 4487 | `model.layers.11` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.49200439453125 / 1.0259755074121442 | [NPY](tensors/0004487.npy) |
| 4488 | `model.layers.11` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.14840924739837646 / 0.7028633553324986 | [NPY](tensors/0004488.npy) |
| 4489 | `model.layers.11` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 910.0 / 910.0 / 910.0 / 0.0 | [NPY](tensors/0004489.npy) |
| 4490 | `model.layers.11` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4491 | `model.layers.11` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4492 | `model.layers.11` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4493 | `model.layers.11.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -352.0 / 368.0 / 0.42422188652886283 / 17.92671616121019 | [NPY](tensors/0004493.npy) |
| 4494 | `model.layers.11.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 96.0 / 0.048164943854014076 / 3.2866170553505274 | [NPY](tensors/0004494.npy) |
| 4495 | `model.layers.11.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 96.0 / 0.048164943854014076 / 3.2866170553505274 | [NPY](tensors/0004495.npy) |
| 4496 | `model.layers.11.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 911] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004496.npy) |
| 4497 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 910.0 / 910.0 / 910.0 / 0.0 | [NPY](tensors/0004497.npy) |
| 4498 | `model.layers.11.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4499 | `model.layers.11.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4500 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.49200439453125 / 1.0259755074121442 | [NPY](tensors/0004500.npy) |
| 4501 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.14840924739837646 / 0.7028633553324986 | [NPY](tensors/0004501.npy) |
| 4502 | `model.layers.11.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4503 | `model.layers.11.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 96.0 / 0.048164943854014076 / 3.2866170553505274 | [NPY](tensors/0004503.npy) |
| 4504 | `model.layers.11.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.4375 / 9.0625 / 0.06869550351984799 / 1.2159116735352486 | [NPY](tensors/0004504.npy) |
| 4505 | `model.layers.11.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 96.0 / 0.048164943854014076 / 3.2866170553505274 | [NPY](tensors/0004505.npy) |
| 4506 | `model.layers.11.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -46.75 / 53.25 / 0.09693631529808044 / 4.81976028915012 | [NPY](tensors/0004506.npy) |
| 4507 | `model.layers.11.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 96.0 / 0.048164943854014076 / 3.2866170553505274 | [NPY](tensors/0004507.npy) |
| 4508 | `model.layers.11.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.28125 / 5.25 / -0.008497804403305054 / 1.9036270641830306 | [NPY](tensors/0004508.npy) |
| 4509 | `model.layers.11.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.6875 / 7.875 / 0.017213300336152315 / 1.2834141016254288 | [NPY](tensors/0004509.npy) |
| 4510 | `model.layers.11.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -123.0 / 138.0 / 0.13083095285627577 / 5.531745073351441 | [NPY](tensors/0004510.npy) |
| 4511 | `model.layers.11.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -123.0 / 138.0 / 0.13083095285627577 / 5.531745073351441 | [NPY](tensors/0004511.npy) |
| 4512 | `model.layers.11.self_attn` | 38 | `output[1]` | [1, 64, 1, 911] | torch.bfloat16 → float32 | 4.6629367034256575e-15 / 0.9453125 / 0.0010114874832233792 / 0.0076042295252179495 | [NPY](tensors/0004512.npy) |
| 4513 | `model.layers.11.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -476.0 / 480.0 / 0.5549385918511285 / 21.48343202948969 | [NPY](tensors/0004513.npy) |
| 4514 | `model.layers.11.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.796875 / 2.6875 / 0.013616298966937595 / 0.5874198143354066 | [NPY](tensors/0004514.npy) |
| 4515 | `model.layers.11.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.796875 / 2.6875 / 0.013616298966937595 / 0.5874198143354066 | [NPY](tensors/0004515.npy) |
| 4516 | `model.layers.11.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.796875 / 2.6875 / 0.013616298966937595 / 0.5874198143354066 | [NPY](tensors/0004516.npy) |
| 4517 | `model.layers.11.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4518 | `model.layers.11.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4519 | `model.layers.11.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4520 | `model.layers.11.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -46.0 / 58.25 / 0.04048760732014974 / 3.1698772284348915 | [NPY](tensors/0004520.npy) |
| 4521 | `model.layers.11.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 58.25 / 0.04048760732014974 / 3.1698772284348915 | [NPY](tensors/0004521.npy) |
| 4522 | `model.layers.11.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.1796875 / 0.80859375 / -0.12268871068954468 / 0.4278438966065448 | [NPY](tensors/0004522.npy) |
| 4523 | `model.layers.11` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -504.0 / 540.0 / 0.5957926432291667 / 23.162445175391994 | [NPY](tensors/0004523.npy) |
| 4602 | `model.layers.11` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -288.0 / 312.0 / 0.5063483344184028 / 17.376876452679152 | [NPY](tensors/0004602.npy) |
| 4603 | `model.layers.11` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 912] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004603.npy) |
| 4604 | `model.layers.11` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.559814453125 / 1.0371191164410525 | [NPY](tensors/0004604.npy) |
| 4605 | `model.layers.11` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2734375 / -0.12162959575653076 / 0.636397050487149 | [NPY](tensors/0004605.npy) |
| 4606 | `model.layers.11` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 911.0 / 911.0 / 911.0 / 0.0 | [NPY](tensors/0004606.npy) |
| 4607 | `model.layers.11` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4608 | `model.layers.11` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4609 | `model.layers.11` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4610 | `model.layers.11.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -288.0 / 312.0 / 0.5063483344184028 / 17.376876452679152 | [NPY](tensors/0004610.npy) |
| 4611 | `model.layers.11.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 84.0 / 0.05364076644182205 / 2.884934473131436 | [NPY](tensors/0004611.npy) |
| 4612 | `model.layers.11.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 84.0 / 0.05364076644182205 / 2.884934473131436 | [NPY](tensors/0004612.npy) |
| 4613 | `model.layers.11.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 912] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004613.npy) |
| 4614 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 911.0 / 911.0 / 911.0 / 0.0 | [NPY](tensors/0004614.npy) |
| 4615 | `model.layers.11.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4616 | `model.layers.11.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4617 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.559814453125 / 1.0371191164410525 | [NPY](tensors/0004617.npy) |
| 4618 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2734375 / -0.12162959575653076 / 0.636397050487149 | [NPY](tensors/0004618.npy) |
| 4619 | `model.layers.11.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4620 | `model.layers.11.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 84.0 / 0.05364076644182205 / 2.884934473131436 | [NPY](tensors/0004620.npy) |
| 4621 | `model.layers.11.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.9375 / 9.6875 / 0.09493003637180664 / 1.3627019709116386 | [NPY](tensors/0004621.npy) |
| 4622 | `model.layers.11.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 84.0 / 0.05364076644182205 / 2.884934473131436 | [NPY](tensors/0004622.npy) |
| 4623 | `model.layers.11.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.75 / 48.75 / 0.14886999130249023 / 4.749101613111635 | [NPY](tensors/0004623.npy) |
| 4624 | `model.layers.11.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 84.0 / 0.05364076644182205 / 2.884934473131436 | [NPY](tensors/0004624.npy) |
| 4625 | `model.layers.11.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -10.1875 / 7.21875 / -0.035479605197906494 / 2.211326072450147 | [NPY](tensors/0004625.npy) |
| 4626 | `model.layers.11.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 5.9375 / -0.01217983290553093 / 1.3961528291305827 | [NPY](tensors/0004626.npy) |
| 4627 | `model.layers.11.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -130.0 / 157.0 / 0.06493263774447972 / 5.417452302595949 | [NPY](tensors/0004627.npy) |
| 4628 | `model.layers.11.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -130.0 / 157.0 / 0.06493263774447972 / 5.417452302595949 | [NPY](tensors/0004628.npy) |
| 4629 | `model.layers.11.self_attn` | 39 | `output[1]` | [1, 64, 1, 912] | torch.bfloat16 → float32 | 8.782037597132586e-18 / 0.92578125 / 0.0009969311512085537 / 0.009770056060815543 | [NPY](tensors/0004629.npy) |
| 4630 | `model.layers.11.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -418.0 / 398.0 / 0.5706366644965277 / 20.483071325076754 | [NPY](tensors/0004630.npy) |
| 4631 | `model.layers.11.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.703125 / 2.796875 / 0.017049880822499593 / 0.6597949235091906 | [NPY](tensors/0004631.npy) |
| 4632 | `model.layers.11.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.703125 / 2.796875 / 0.017049880822499593 / 0.6597949235091906 | [NPY](tensors/0004632.npy) |
| 4633 | `model.layers.11.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.703125 / 2.796875 / 0.017049880822499593 / 0.6597949235091906 | [NPY](tensors/0004633.npy) |
| 4634 | `model.layers.11.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4635 | `model.layers.11.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4636 | `model.layers.11.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4637 | `model.layers.11.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -47.0 / 69.5 / 0.016329662005106608 / 3.4745576762353347 | [NPY](tensors/0004637.npy) |
| 4638 | `model.layers.11.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 69.5 / 0.016329662005106608 / 3.4745576762353347 | [NPY](tensors/0004638.npy) |
| 4639 | `model.layers.11.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.9453125 / 0.74609375 / -0.1213226318359375 / 0.42769217146860145 | [NPY](tensors/0004639.npy) |
| 4640 | `model.layers.11` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -464.0 / 468.0 / 0.5874884711371527 / 21.99836886483649 | [NPY](tensors/0004640.npy) |
| 4719 | `model.layers.11` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -232.0 / 274.0 / 0.5300279193454318 / 14.469000449842229 | [NPY](tensors/0004719.npy) |
| 4720 | `model.layers.11` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 913] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004720.npy) |
| 4721 | `model.layers.11` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.57440185546875 / 1.030810795441952 | [NPY](tensors/0004721.npy) |
| 4722 | `model.layers.11` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.2734375 / -0.07393771409988403 / 0.6426875034418209 | [NPY](tensors/0004722.npy) |
| 4723 | `model.layers.11` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 912.0 / 912.0 / 912.0 / 0.0 | [NPY](tensors/0004723.npy) |
| 4724 | `model.layers.11` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4725 | `model.layers.11` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4726 | `model.layers.11` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4727 | `model.layers.11.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -232.0 / 274.0 / 0.5300279193454318 / 14.469000449842229 | [NPY](tensors/0004727.npy) |
| 4728 | `model.layers.11.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 85.0 / 0.07627159886889988 / 3.0721895711824323 | [NPY](tensors/0004728.npy) |
| 4729 | `model.layers.11.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 85.0 / 0.07627159886889988 / 3.0721895711824323 | [NPY](tensors/0004729.npy) |
| 4730 | `model.layers.11.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 913] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004730.npy) |
| 4731 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 912.0 / 912.0 / 912.0 / 0.0 | [NPY](tensors/0004731.npy) |
| 4732 | `model.layers.11.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4733 | `model.layers.11.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4734 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.57440185546875 / 1.030810795441952 | [NPY](tensors/0004734.npy) |
| 4735 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.2734375 / -0.07393771409988403 / 0.6426875034418209 | [NPY](tensors/0004735.npy) |
| 4736 | `model.layers.11.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4737 | `model.layers.11.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 85.0 / 0.07627159886889988 / 3.0721895711824323 | [NPY](tensors/0004737.npy) |
| 4738 | `model.layers.11.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.6875 / 8.1875 / 0.026551219867542386 / 1.347546782284492 | [NPY](tensors/0004738.npy) |
| 4739 | `model.layers.11.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 85.0 / 0.07627159886889988 / 3.0721895711824323 | [NPY](tensors/0004739.npy) |
| 4740 | `model.layers.11.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -46.25 / 57.25 / 0.19963940978050232 / 5.032046445640363 | [NPY](tensors/0004740.npy) |
| 4741 | `model.layers.11.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 85.0 / 0.07627159886889988 / 3.0721895711824323 | [NPY](tensors/0004741.npy) |
| 4742 | `model.layers.11.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.40625 / 7.3125 / 0.02093052864074707 / 1.9382087832868462 | [NPY](tensors/0004742.npy) |
| 4743 | `model.layers.11.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.59375 / 6.28125 / -0.03091915976256132 / 1.4429761198012587 | [NPY](tensors/0004743.npy) |
| 4744 | `model.layers.11.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.625 / 111.5 / 0.09879801803165011 / 3.840951792791987 | [NPY](tensors/0004744.npy) |
| 4745 | `model.layers.11.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.625 / 111.5 / 0.09879801803165011 / 3.840951792791987 | [NPY](tensors/0004745.npy) |
| 4746 | `model.layers.11.self_attn` | 40 | `output[1]` | [1, 64, 1, 913] | torch.bfloat16 → float32 | 9.049472282640636e-11 / 0.77734375 / 0.0010035062770518575 / 0.005757665771899323 | [NPY](tensors/0004746.npy) |
| 4747 | `model.layers.11.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -239.0 / 292.0 / 0.6288128323025174 / 15.942087225719229 | [NPY](tensors/0004747.npy) |
| 4748 | `model.layers.11.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.46875 / 2.6875 / 0.02200338509347704 / 0.6324895780114175 | [NPY](tensors/0004748.npy) |
| 4749 | `model.layers.11.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.46875 / 2.6875 / 0.02200338509347704 / 0.6324895780114175 | [NPY](tensors/0004749.npy) |
| 4750 | `model.layers.11.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.46875 / 2.6875 / 0.02200338509347704 / 0.6324895780114175 | [NPY](tensors/0004750.npy) |
| 4751 | `model.layers.11.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4752 | `model.layers.11.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4753 | `model.layers.11.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4754 | `model.layers.11.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -13.3125 / 34.5 / -0.03429642783270942 / 3.2471559760464235 | [NPY](tensors/0004754.npy) |
| 4755 | `model.layers.11.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.3125 / 34.5 / -0.03429642783270942 / 3.2471559760464235 | [NPY](tensors/0004755.npy) |
| 4756 | `model.layers.11.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.546875 / 0.859375 / -0.14984893798828125 / 0.6658196866789109 | [NPY](tensors/0004756.npy) |
| 4757 | `model.layers.11` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -221.0 / 298.0 / 0.5939409044053819 / 16.83116443674062 | [NPY](tensors/0004757.npy) |
| 4836 | `model.layers.11` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -274.0 / 290.0 / 0.3831444634331597 / 16.793808630504564 | [NPY](tensors/0004836.npy) |
| 4837 | `model.layers.11` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 914] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004837.npy) |
| 4838 | `model.layers.11` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.5457305908203125 / 1.0267502307475864 | [NPY](tensors/0004838.npy) |
| 4839 | `model.layers.11` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.051917850971221924 / 0.6740142912053045 | [NPY](tensors/0004839.npy) |
| 4840 | `model.layers.11` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 913.0 / 913.0 / 913.0 / 0.0 | [NPY](tensors/0004840.npy) |
| 4841 | `model.layers.11` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4842 | `model.layers.11` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4843 | `model.layers.11` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4844 | `model.layers.11.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -274.0 / 290.0 / 0.3831444634331597 / 16.793808630504564 | [NPY](tensors/0004844.npy) |
| 4845 | `model.layers.11.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 81.0 / 0.04917260805765788 / 2.9376748823963164 | [NPY](tensors/0004845.npy) |
| 4846 | `model.layers.11.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 81.0 / 0.04917260805765788 / 2.9376748823963164 | [NPY](tensors/0004846.npy) |
| 4847 | `model.layers.11.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 914] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004847.npy) |
| 4848 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 913.0 / 913.0 / 913.0 / 0.0 | [NPY](tensors/0004848.npy) |
| 4849 | `model.layers.11.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4850 | `model.layers.11.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4851 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.5457305908203125 / 1.0267502307475864 | [NPY](tensors/0004851.npy) |
| 4852 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.051917850971221924 / 0.6740142912053045 | [NPY](tensors/0004852.npy) |
| 4853 | `model.layers.11.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4854 | `model.layers.11.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 81.0 / 0.04917260805765788 / 2.9376748823963164 | [NPY](tensors/0004854.npy) |
| 4855 | `model.layers.11.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.1875 / 10.125 / 0.08602095977403224 / 1.3530793678478579 | [NPY](tensors/0004855.npy) |
| 4856 | `model.layers.11.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 81.0 / 0.04917260805765788 / 2.9376748823963164 | [NPY](tensors/0004856.npy) |
| 4857 | `model.layers.11.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.25 / 56.25 / 0.17280417680740356 / 5.110166418427866 | [NPY](tensors/0004857.npy) |
| 4858 | `model.layers.11.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 81.0 / 0.04917260805765788 / 2.9376748823963164 | [NPY](tensors/0004858.npy) |
| 4859 | `model.layers.11.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.71875 / 6.28125 / -0.024688661098480225 / 2.1293613001570524 | [NPY](tensors/0004859.npy) |
| 4860 | `model.layers.11.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.46875 / 6.1875 / -0.02032027766108513 / 1.3825658018426044 | [NPY](tensors/0004860.npy) |
| 4861 | `model.layers.11.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -127.0 / 177.0 / 0.032457923889160155 / 6.136999041462904 | [NPY](tensors/0004861.npy) |
| 4862 | `model.layers.11.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -127.0 / 177.0 / 0.032457923889160155 / 6.136999041462904 | [NPY](tensors/0004862.npy) |
| 4863 | `model.layers.11.self_attn` | 41 | `output[1]` | [1, 64, 1, 914] | torch.bfloat16 → float32 | 1.0200174038743626e-15 / 0.953125 / 0.0010267703513677914 / 0.008396670814979447 | [NPY](tensors/0004863.npy) |
| 4864 | `model.layers.11.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -400.0 / 410.0 / 0.4170596652560764 / 20.531501108486225 | [NPY](tensors/0004864.npy) |
| 4865 | `model.layers.11.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.6875 / 2.6875 / 0.006556359926859537 / 0.6114907458510281 | [NPY](tensors/0004865.npy) |
| 4866 | `model.layers.11.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.6875 / 2.6875 / 0.006556359926859537 / 0.6114907458510281 | [NPY](tensors/0004866.npy) |
| 4867 | `model.layers.11.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.6875 / 2.6875 / 0.006556359926859537 / 0.6114907458510281 | [NPY](tensors/0004867.npy) |
| 4868 | `model.layers.11.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4869 | `model.layers.11.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4870 | `model.layers.11.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4871 | `model.layers.11.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -44.25 / 41.5 / 0.010047324498494466 / 3.085789537641484 | [NPY](tensors/0004871.npy) |
| 4872 | `model.layers.11.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 41.5 / 0.010047324498494466 / 3.085789537641484 | [NPY](tensors/0004872.npy) |
| 4873 | `model.layers.11.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.9765625 / 0.73828125 / -0.09309816360473633 / 0.37518771266005846 | [NPY](tensors/0004873.npy) |
| 4874 | `model.layers.11` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -426.0 / 452.0 / 0.4262049357096354 / 21.67006727029667 | [NPY](tensors/0004874.npy) |
| 4953 | `model.layers.11` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -236.0 / 266.0 / 0.32493828667534724 / 16.67730176633392 | [NPY](tensors/0004953.npy) |
| 4954 | `model.layers.11` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 915] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004954.npy) |
| 4955 | `model.layers.11` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.513641357421875 / 1.0381515204992577 | [NPY](tensors/0004955.npy) |
| 4956 | `model.layers.11` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / -0.07546013593673706 / 0.6806294351122038 | [NPY](tensors/0004956.npy) |
| 4957 | `model.layers.11` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 914.0 / 914.0 / 914.0 / 0.0 | [NPY](tensors/0004957.npy) |
| 4958 | `model.layers.11` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4959 | `model.layers.11` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4960 | `model.layers.11` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4961 | `model.layers.11.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -236.0 / 266.0 / 0.32493828667534724 / 16.67730176633392 | [NPY](tensors/0004961.npy) |
| 4962 | `model.layers.11.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 66.0 / 0.0506663892004225 / 2.7006350326559114 | [NPY](tensors/0004962.npy) |
| 4963 | `model.layers.11.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 66.0 / 0.0506663892004225 / 2.7006350326559114 | [NPY](tensors/0004963.npy) |
| 4964 | `model.layers.11.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 915] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004964.npy) |
| 4965 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 914.0 / 914.0 / 914.0 / 0.0 | [NPY](tensors/0004965.npy) |
| 4966 | `model.layers.11.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4967 | `model.layers.11.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4968 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.513641357421875 / 1.0381515204992577 | [NPY](tensors/0004968.npy) |
| 4969 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / -0.07546013593673706 / 0.6806294351122038 | [NPY](tensors/0004969.npy) |
| 4970 | `model.layers.11.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4971 | `model.layers.11.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 66.0 / 0.0506663892004225 / 2.7006350326559114 | [NPY](tensors/0004971.npy) |
| 4972 | `model.layers.11.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.8125 / 10.625 / 0.05283249414060265 / 1.4091447626607712 | [NPY](tensors/0004972.npy) |
| 4973 | `model.layers.11.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 66.0 / 0.0506663892004225 / 2.7006350326559114 | [NPY](tensors/0004973.npy) |
| 4974 | `model.layers.11.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.75 / 52.5 / 0.17065292596817017 / 4.863132563200198 | [NPY](tensors/0004974.npy) |
| 4975 | `model.layers.11.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 66.0 / 0.0506663892004225 / 2.7006350326559114 | [NPY](tensors/0004975.npy) |
| 4976 | `model.layers.11.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -11.4375 / 12.0 / -0.09072333574295044 / 2.666427697628904 | [NPY](tensors/0004976.npy) |
| 4977 | `model.layers.11.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.8125 / 9.9375 / -0.03529895329847932 / 1.6709896679617955 | [NPY](tensors/0004977.npy) |
| 4978 | `model.layers.11.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 163.0 / -0.0034070064624150596 / 6.188567454110086 | [NPY](tensors/0004978.npy) |
| 4979 | `model.layers.11.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 163.0 / -0.0034070064624150596 / 6.188567454110086 | [NPY](tensors/0004979.npy) |
| 4980 | `model.layers.11.self_attn` | 42 | `output[1]` | [1, 64, 1, 915] | torch.bfloat16 → float32 | 4.241051954068098e-14 / 0.78125 / 0.0009817247583174963 / 0.008737545161342957 | [NPY](tensors/0004980.npy) |
| 4981 | `model.layers.11.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -294.0 / 366.0 / 0.3216847631666395 / 20.234541444869354 | [NPY](tensors/0004981.npy) |
| 4982 | `model.layers.11.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.09375 / 2.46875 / 0.01037524143854777 / 0.6900657977529039 | [NPY](tensors/0004982.npy) |
| 4983 | `model.layers.11.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.09375 / 2.46875 / 0.01037524143854777 / 0.6900657977529039 | [NPY](tensors/0004983.npy) |
| 4984 | `model.layers.11.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.09375 / 2.46875 / 0.01037524143854777 / 0.6900657977529039 | [NPY](tensors/0004984.npy) |
| 4985 | `model.layers.11.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4986 | `model.layers.11.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4987 | `model.layers.11.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4988 | `model.layers.11.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -91.0 / 86.0 / -0.0059026559193929035 / 5.214480508988284 | [NPY](tensors/0004988.npy) |
| 4989 | `model.layers.11.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.0 / 86.0 / -0.0059026559193929035 / 5.214480508988284 | [NPY](tensors/0004989.npy) |
| 4990 | `model.layers.11.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.0 / 1.234375 / -0.07118797302246094 / 0.6342283709052134 | [NPY](tensors/0004990.npy) |
| 4991 | `model.layers.11` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -384.0 / 450.0 / 0.31606920030381946 / 23.129156595287952 | [NPY](tensors/0004991.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -12672.0 / 14208.0 / -0.5974490452771639 / 414.82675565829504 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 873, 873] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6928243822607898e+38 / 1.694764582762651e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 873, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7211662215764238 / 0.9199891152809843 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 873, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10053101652705901 / 0.6581213818663489 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 873] | torch.int64 → int64 | 0.0 / 872.0 / 436.0 / 252.01322716608877 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -12672.0 / 14208.0 / -0.5974490452771639 / 414.82675565829504 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 873, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010854286986391433 / 1.7616385687671088 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 873, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010854286986391433 / 1.7616385687671088 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 873, 873] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6928243822607898e+38 / 1.694764582762651e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 873] | torch.int64 → int64 | 0.0 / 872.0 / 436.0 / 252.01322716608877 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 873, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7211662215764238 / 0.9199891152809843 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 873, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10053101652705901 / 0.6581213818663489 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010854286986391433 / 1.7616385687671088 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 873, 4096] | torch.bfloat16 → float32 | -19.75 / 24.75 / 0.033664049768494256 / 1.6316527338096347 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010854286986391433 / 1.7616385687671088 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 873, 512] | torch.bfloat16 → float32 | -102.5 / 68.0 / -0.09398149507069944 / 5.169082565782344 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010854286986391433 / 1.7616385687671088 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 873, 512] | torch.bfloat16 → float32 | -30.75 / 20.25 / -0.034361300633805256 / 3.240373047871329 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 873, 4096] | torch.bfloat16 → float32 | -26.625 / 14.3125 / -0.012544475694118982 / 1.1816465667326947 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 873, 2880] | torch.bfloat16 → float32 | -7552.0 / 7840.0 / 3.240936793373281 / 169.35834566111393 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -7552.0 / 7840.0 / 3.240936793373281 / 169.35834566111393 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 873, 873] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0006529199537450743 / 0.007383469499550489 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -11328.0 / 11520.0 / 2.642857840917819 / 399.16047834807785 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 873, 2880] | torch.bfloat16 → float32 | -52.75 / 22.5 / -0.011819357807318095 / 1.174083123299406 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -52.75 / 22.5 / -0.011819357807318095 / 1.174083123299406 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [873, 2880] | torch.bfloat16 → float32 | -52.75 / 22.5 / -0.011819357807318095 / 1.174083123299406 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [873, 2880] | torch.bfloat16 → float32 | -7328.0 / 6400.0 / -1.3298532666771017 / 161.75279658823675 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 873, 2880] | torch.bfloat16 → float32 | -7328.0 / 6400.0 / -1.3298532666771017 / 161.75279658823675 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [873, 32] | torch.bfloat16 → float32 | -8.0625 / 4.21875 / 0.2249495821993239 / 2.220798038499347 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 873, 2880] | torch.bfloat16 → float32 | -11840.0 / 11968.0 / 1.3132904079923255 / 434.6433685240814 | [NPY](tensors/0000116.npy) |
| 195 | `model.layers.23` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 9536.0 / 2.9911451551649306 / 427.97984110068865 | [NPY](tensors/0000195.npy) |
| 196 | `model.layers.23` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 874] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000196.npy) |
| 197 | `model.layers.23` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.649322509765625 / 0.9833264324529841 | [NPY](tensors/0000197.npy) |
| 198 | `model.layers.23` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.024361848831176758 / 0.6489880782497579 | [NPY](tensors/0000198.npy) |
| 199 | `model.layers.23` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 873.0 / 873.0 / 873.0 / 0.0 | [NPY](tensors/0000199.npy) |
| 200 | `model.layers.23` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 201 | `model.layers.23` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 202 | `model.layers.23` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 203 | `model.layers.23.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 9536.0 / 2.9911451551649306 / 427.97984110068865 | [NPY](tensors/0000203.npy) |
| 204 | `model.layers.23.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 60.0 / 0.024254736635420056 / 1.7979648813218645 | [NPY](tensors/0000204.npy) |
| 205 | `model.layers.23.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 60.0 / 0.024254736635420056 / 1.7979648813218645 | [NPY](tensors/0000205.npy) |
| 206 | `model.layers.23.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 874] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000206.npy) |
| 207 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 873.0 / 873.0 / 873.0 / 0.0 | [NPY](tensors/0000207.npy) |
| 208 | `model.layers.23.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 209 | `model.layers.23.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 210 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.649322509765625 / 0.9833264324529841 | [NPY](tensors/0000210.npy) |
| 211 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.024361848831176758 / 0.6489880782497579 | [NPY](tensors/0000211.npy) |
| 212 | `model.layers.23.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 213 | `model.layers.23.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 60.0 / 0.024254736635420056 / 1.7979648813218645 | [NPY](tensors/0000213.npy) |
| 214 | `model.layers.23.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.375 / 12.1875 / 0.050855324108852074 / 1.5418863414900963 | [NPY](tensors/0000214.npy) |
| 215 | `model.layers.23.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 60.0 / 0.024254736635420056 / 1.7979648813218645 | [NPY](tensors/0000215.npy) |
| 216 | `model.layers.23.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -57.5 / 49.75 / -0.01800122857093811 / 6.022131428207291 | [NPY](tensors/0000216.npy) |
| 217 | `model.layers.23.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 60.0 / 0.024254736635420056 / 1.7979648813218645 | [NPY](tensors/0000217.npy) |
| 218 | `model.layers.23.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.375 / 10.8125 / 0.04034191370010376 / 3.494312755751379 | [NPY](tensors/0000218.npy) |
| 219 | `model.layers.23.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.875 / 7.375 / -0.020832371432334185 / 1.72153354881929 | [NPY](tensors/0000219.npy) |
| 220 | `model.layers.23.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4704.0 / 4864.0 / 3.3735070758395724 / 213.47088011652545 | [NPY](tensors/0000220.npy) |
| 221 | `model.layers.23.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4704.0 / 4864.0 / 3.3735070758395724 / 213.47088011652545 | [NPY](tensors/0000221.npy) |
| 222 | `model.layers.23.self_attn` | 1 | `output[1]` | [1, 64, 1, 874] | torch.bfloat16 → float32 | 3.9745984281580604e-14 / 0.8984375 / 0.0009673841509394274 / 0.011372891706068212 | [NPY](tensors/0000222.npy) |
| 223 | `model.layers.23.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9280.0 / 9152.0 / 6.360915798611111 / 489.5979047224158 | [NPY](tensors/0000223.npy) |
| 224 | `model.layers.23.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 7.375 / 0.0016205939981672498 / 1.117998433344935 | [NPY](tensors/0000224.npy) |
| 225 | `model.layers.23.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 7.375 / 0.0016205939981672498 / 1.117998433344935 | [NPY](tensors/0000225.npy) |
| 226 | `model.layers.23.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.5 / 7.375 / 0.0016205939981672498 / 1.117998433344935 | [NPY](tensors/0000226.npy) |
| 227 | `model.layers.23.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 228 | `model.layers.23.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 229 | `model.layers.23.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 230 | `model.layers.23.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3168.0 / 2816.0 / -1.1399752298990886 / 163.84847140584856 | [NPY](tensors/0000230.npy) |
| 231 | `model.layers.23.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3168.0 / 2816.0 / -1.1399752298990886 / 163.84847140584856 | [NPY](tensors/0000231.npy) |
| 232 | `model.layers.23.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.28125 / 1.4921875 / -0.05844879150390625 / 0.702192402921898 | [NPY](tensors/0000232.npy) |
| 233 | `model.layers.23` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6464.0 / 5984.0 / 5.215831163194444 / 384.74650424495326 | [NPY](tensors/0000233.npy) |
| 312 | `model.layers.23` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8256.0 / 7872.0 / 9.41960720486111 / 397.2425339755304 | [NPY](tensors/0000312.npy) |
| 313 | `model.layers.23` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 875] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000313.npy) |
| 314 | `model.layers.23` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.663970947265625 / 0.9817896713297021 | [NPY](tensors/0000314.npy) |
| 315 | `model.layers.23` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.25 / 1.34375 / 0.07146221399307251 / 0.6328787006162191 | [NPY](tensors/0000315.npy) |
| 316 | `model.layers.23` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 874.0 / 874.0 / 874.0 / 0.0 | [NPY](tensors/0000316.npy) |
| 317 | `model.layers.23` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 318 | `model.layers.23` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 319 | `model.layers.23` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 320 | `model.layers.23.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8256.0 / 7872.0 / 9.41960720486111 / 397.2425339755304 | [NPY](tensors/0000320.npy) |
| 321 | `model.layers.23.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 53.25 / 0.04796025090747409 / 1.7331404796843874 | [NPY](tensors/0000321.npy) |
| 322 | `model.layers.23.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 53.25 / 0.04796025090747409 / 1.7331404796843874 | [NPY](tensors/0000322.npy) |
| 323 | `model.layers.23.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 875] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000323.npy) |
| 324 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 874.0 / 874.0 / 874.0 / 0.0 | [NPY](tensors/0000324.npy) |
| 325 | `model.layers.23.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 326 | `model.layers.23.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 327 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.663970947265625 / 0.9817896713297021 | [NPY](tensors/0000327.npy) |
| 328 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.25 / 1.34375 / 0.07146221399307251 / 0.6328787006162191 | [NPY](tensors/0000328.npy) |
| 329 | `model.layers.23.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 330 | `model.layers.23.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 53.25 / 0.04796025090747409 / 1.7331404796843874 | [NPY](tensors/0000330.npy) |
| 331 | `model.layers.23.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.1875 / 14.125 / 0.03919464768841863 / 1.6180092185547443 | [NPY](tensors/0000331.npy) |
| 332 | `model.layers.23.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 53.25 / 0.04796025090747409 / 1.7331404796843874 | [NPY](tensors/0000332.npy) |
| 333 | `model.layers.23.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.25 / 38.5 / 0.07258680509403348 / 5.623662496336176 | [NPY](tensors/0000333.npy) |
| 334 | `model.layers.23.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 53.25 / 0.04796025090747409 / 1.7331404796843874 | [NPY](tensors/0000334.npy) |
| 335 | `model.layers.23.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.8125 / 12.375 / -0.11531782150268555 / 3.641384883614422 | [NPY](tensors/0000335.npy) |
| 336 | `model.layers.23.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.25 / 9.6875 / 0.03147798404097557 / 1.5422500818795362 | [NPY](tensors/0000336.npy) |
| 337 | `model.layers.23.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4640.0 / 4704.0 / 5.057539706759982 / 220.9288690996285 | [NPY](tensors/0000337.npy) |
| 338 | `model.layers.23.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4640.0 / 4704.0 / 5.057539706759982 / 220.9288690996285 | [NPY](tensors/0000338.npy) |
| 339 | `model.layers.23.self_attn` | 2 | `output[1]` | [1, 64, 1, 875] | torch.bfloat16 → float32 | 1.3358203432289883e-12 / 0.8046875 / 0.0008070705399350512 / 0.008387909310786024 | [NPY](tensors/0000339.npy) |
| 340 | `model.layers.23.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8384.0 / 8032.0 / 14.497634548611112 / 480.75480213390864 | [NPY](tensors/0000340.npy) |
| 341 | `model.layers.23.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.125 / 9.375 / 0.024483548270331487 / 1.1885994560147661 | [NPY](tensors/0000341.npy) |
| 342 | `model.layers.23.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.125 / 9.375 / 0.024483548270331487 / 1.1885994560147661 | [NPY](tensors/0000342.npy) |
| 343 | `model.layers.23.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -23.125 / 9.375 / 0.024483548270331487 / 1.1885994560147661 | [NPY](tensors/0000343.npy) |
| 344 | `model.layers.23.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 345 | `model.layers.23.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 346 | `model.layers.23.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 347 | `model.layers.23.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2912.0 / 2672.0 / -1.0286546919080946 / 227.45963909290356 | [NPY](tensors/0000347.npy) |
| 348 | `model.layers.23.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2912.0 / 2672.0 / -1.0286546919080946 / 227.45963909290356 | [NPY](tensors/0000348.npy) |
| 349 | `model.layers.23.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.78125 / 0.01050567626953125 / 0.5698107559600345 | [NPY](tensors/0000349.npy) |
| 350 | `model.layers.23` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5824.0 / 5120.0 / 13.450455729166666 / 437.5342253807265 | [NPY](tensors/0000350.npy) |
| 429 | `model.layers.23` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9472.0 / 9344.0 / -3.199435763888889 / 412.13857283919805 | [NPY](tensors/0000429.npy) |
| 430 | `model.layers.23` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 876] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000430.npy) |
| 431 | `model.layers.23` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.6338043212890625 / 0.990232497628255 | [NPY](tensors/0000431.npy) |
| 432 | `model.layers.23` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.10754281282424927 / 0.6458776678737284 | [NPY](tensors/0000432.npy) |
| 433 | `model.layers.23` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 875.0 / 875.0 / 875.0 / 0.0 | [NPY](tensors/0000433.npy) |
| 434 | `model.layers.23` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 435 | `model.layers.23` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 436 | `model.layers.23` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 437 | `model.layers.23.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9472.0 / 9344.0 / -3.199435763888889 / 412.13857283919805 | [NPY](tensors/0000437.npy) |
| 438 | `model.layers.23.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 60.0 / 0.004283374879095289 / 1.8020947220656425 | [NPY](tensors/0000438.npy) |
| 439 | `model.layers.23.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 60.0 / 0.004283374879095289 / 1.8020947220656425 | [NPY](tensors/0000439.npy) |
| 440 | `model.layers.23.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 876] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000440.npy) |
| 441 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 875.0 / 875.0 / 875.0 / 0.0 | [NPY](tensors/0000441.npy) |
| 442 | `model.layers.23.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 443 | `model.layers.23.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 444 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.6338043212890625 / 0.990232497628255 | [NPY](tensors/0000444.npy) |
| 445 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.10754281282424927 / 0.6458776678737284 | [NPY](tensors/0000445.npy) |
| 446 | `model.layers.23.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 447 | `model.layers.23.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 60.0 / 0.004283374879095289 / 1.8020947220656425 | [NPY](tensors/0000447.npy) |
| 448 | `model.layers.23.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.8125 / 14.5 / 0.04835582443047315 / 1.456825048203124 | [NPY](tensors/0000448.npy) |
| 449 | `model.layers.23.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 60.0 / 0.004283374879095289 / 1.8020947220656425 | [NPY](tensors/0000449.npy) |
| 450 | `model.layers.23.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.5 / 41.75 / -0.05741691589355469 / 5.435071543159168 | [NPY](tensors/0000450.npy) |
| 451 | `model.layers.23.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 60.0 / 0.004283374879095289 / 1.8020947220656425 | [NPY](tensors/0000451.npy) |
| 452 | `model.layers.23.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.75 / 11.75 / 0.0774836540222168 / 3.5585505296923277 | [NPY](tensors/0000452.npy) |
| 453 | `model.layers.23.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.75 / 6.34375 / -0.04625261202454567 / 1.1728839340791917 | [NPY](tensors/0000453.npy) |
| 454 | `model.layers.23.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 5856.0 / 6.362959840562609 / 251.78702491456406 | [NPY](tensors/0000454.npy) |
| 455 | `model.layers.23.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 5856.0 / 6.362959840562609 / 251.78702491456406 | [NPY](tensors/0000455.npy) |
| 456 | `model.layers.23.self_attn` | 3 | `output[1]` | [1, 64, 1, 876] | torch.bfloat16 → float32 | 3.219646771412954e-14 / 0.828125 / 0.0008106344364283689 / 0.0061702992542647635 | [NPY](tensors/0000456.npy) |
| 457 | `model.layers.23.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9408.0 / 9408.0 / 3.139956325954861 / 499.2554829387853 | [NPY](tensors/0000457.npy) |
| 458 | `model.layers.23.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.375 / 8.5 / -0.00935007996029324 / 0.9277181931023745 | [NPY](tensors/0000458.npy) |
| 459 | `model.layers.23.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.375 / 8.5 / -0.00935007996029324 / 0.9277181931023745 | [NPY](tensors/0000459.npy) |
| 460 | `model.layers.23.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -26.375 / 8.5 / -0.00935007996029324 / 0.9277181931023745 | [NPY](tensors/0000460.npy) |
| 461 | `model.layers.23.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 462 | `model.layers.23.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 463 | `model.layers.23.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 464 | `model.layers.23.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1168.0 / 1112.0 / -1.3130272017584907 / 74.66050352765991 | [NPY](tensors/0000464.npy) |
| 465 | `model.layers.23.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1168.0 / 1112.0 / -1.3130272017584907 / 74.66050352765991 | [NPY](tensors/0000465.npy) |
| 466 | `model.layers.23.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.78515625 / 1.234375 / 0.04578876495361328 / 0.37478967180609046 | [NPY](tensors/0000466.npy) |
| 467 | `model.layers.23` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8640.0 / 8576.0 / 1.8137498643663195 / 455.28647700534634 | [NPY](tensors/0000467.npy) |
| 546 | `model.layers.23` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 10240.0 / -2.9478936089409724 / 470.85018209498395 | [NPY](tensors/0000546.npy) |
| 547 | `model.layers.23` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 877] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000547.npy) |
| 548 | `model.layers.23` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.58746337890625 / 1.0206486490707742 | [NPY](tensors/0000548.npy) |
| 549 | `model.layers.23` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.3203125 / 0.10449105501174927 / 0.6417963143458147 | [NPY](tensors/0000549.npy) |
| 550 | `model.layers.23` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 876.0 / 876.0 / 876.0 / 0.0 | [NPY](tensors/0000550.npy) |
| 551 | `model.layers.23` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 552 | `model.layers.23` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 553 | `model.layers.23` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 554 | `model.layers.23.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 10240.0 / -2.9478936089409724 / 470.85018209498395 | [NPY](tensors/0000554.npy) |
| 555 | `model.layers.23.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 58.5 / 0.002517158455318875 / 1.7817750286821759 | [NPY](tensors/0000555.npy) |
| 556 | `model.layers.23.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 58.5 / 0.002517158455318875 / 1.7817750286821759 | [NPY](tensors/0000556.npy) |
| 557 | `model.layers.23.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 877] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000557.npy) |
| 558 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 876.0 / 876.0 / 876.0 / 0.0 | [NPY](tensors/0000558.npy) |
| 559 | `model.layers.23.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 560 | `model.layers.23.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 561 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.58746337890625 / 1.0206486490707742 | [NPY](tensors/0000561.npy) |
| 562 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.3203125 / 0.10449105501174927 / 0.6417963143458147 | [NPY](tensors/0000562.npy) |
| 563 | `model.layers.23.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 564 | `model.layers.23.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 58.5 / 0.002517158455318875 / 1.7817750286821759 | [NPY](tensors/0000564.npy) |
| 565 | `model.layers.23.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.75 / 18.125 / 0.03871876292396337 / 1.413264605720748 | [NPY](tensors/0000565.npy) |
| 566 | `model.layers.23.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 58.5 / 0.002517158455318875 / 1.7817750286821759 | [NPY](tensors/0000566.npy) |
| 567 | `model.layers.23.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -41.75 / 35.25 / -0.16871541738510132 / 5.384542818540988 | [NPY](tensors/0000567.npy) |
| 568 | `model.layers.23.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 58.5 / 0.002517158455318875 / 1.7817750286821759 | [NPY](tensors/0000568.npy) |
| 569 | `model.layers.23.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.5625 / 6.15625 / -0.10464173555374146 / 2.1004316701523034 | [NPY](tensors/0000569.npy) |
| 570 | `model.layers.23.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.625 / 5.78125 / -0.04985655099153519 / 0.8608619625517359 | [NPY](tensors/0000570.npy) |
| 571 | `model.layers.23.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5664.0 / 5.581386905246311 / 239.44516714915846 | [NPY](tensors/0000571.npy) |
| 572 | `model.layers.23.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5664.0 / 5.581386905246311 / 239.44516714915846 | [NPY](tensors/0000572.npy) |
| 573 | `model.layers.23.self_attn` | 4 | `output[1]` | [1, 64, 1, 877] | torch.bfloat16 → float32 | 7.251144129583054e-16 / 0.89453125 / 0.0006073172994528064 / 0.006001296003441093 | [NPY](tensors/0000573.npy) |
| 574 | `model.layers.23.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 10112.0 / 2.615048556857639 / 543.768922713757 | [NPY](tensors/0000574.npy) |
| 575 | `model.layers.23.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.625 / 7.9375 / -0.01591902838812934 / 0.9292677384516416 | [NPY](tensors/0000575.npy) |
| 576 | `model.layers.23.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.625 / 7.9375 / -0.01591902838812934 / 0.9292677384516416 | [NPY](tensors/0000576.npy) |
| 577 | `model.layers.23.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.625 / 7.9375 / -0.01591902838812934 / 0.9292677384516416 | [NPY](tensors/0000577.npy) |
| 578 | `model.layers.23.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 579 | `model.layers.23.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 580 | `model.layers.23.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 581 | `model.layers.23.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1120.0 / 1064.0 / -1.6284146732754177 / 72.87049961807277 | [NPY](tensors/0000581.npy) |
| 582 | `model.layers.23.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1120.0 / 1064.0 / -1.6284146732754177 / 72.87049961807277 | [NPY](tensors/0000582.npy) |
| 583 | `model.layers.23.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.3828125 / 1.2578125 / 0.07655906677246094 / 0.32416133939977926 | [NPY](tensors/0000583.npy) |
| 584 | `model.layers.23` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 9152.0 / 0.9710259331597222 / 493.28302415719753 | [NPY](tensors/0000584.npy) |
| 663 | `model.layers.23` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9408.0 / 9472.0 / -2.8879489474826388 / 444.13984395562295 | [NPY](tensors/0000663.npy) |
| 664 | `model.layers.23` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 878] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000664.npy) |
| 665 | `model.layers.23` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.558441162109375 / 1.0101761449217725 | [NPY](tensors/0000665.npy) |
| 666 | `model.layers.23` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3359375 / 0.06921488046646118 / 0.6876239253025267 | [NPY](tensors/0000666.npy) |
| 667 | `model.layers.23` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 877.0 / 877.0 / 877.0 / 0.0 | [NPY](tensors/0000667.npy) |
| 668 | `model.layers.23` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 669 | `model.layers.23` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 670 | `model.layers.23` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 671 | `model.layers.23.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9408.0 / 9472.0 / -2.8879489474826388 / 444.13984395562295 | [NPY](tensors/0000671.npy) |
| 672 | `model.layers.23.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 57.25 / -0.0005243712001376682 / 1.7432840582915943 | [NPY](tensors/0000672.npy) |
| 673 | `model.layers.23.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 57.25 / -0.0005243712001376682 / 1.7432840582915943 | [NPY](tensors/0000673.npy) |
| 674 | `model.layers.23.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 878] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000674.npy) |
| 675 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 877.0 / 877.0 / 877.0 / 0.0 | [NPY](tensors/0000675.npy) |
| 676 | `model.layers.23.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 677 | `model.layers.23.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 678 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.558441162109375 / 1.0101761449217725 | [NPY](tensors/0000678.npy) |
| 679 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3359375 / 0.06921488046646118 / 0.6876239253025267 | [NPY](tensors/0000679.npy) |
| 680 | `model.layers.23.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 681 | `model.layers.23.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 57.25 / -0.0005243712001376682 / 1.7432840582915943 | [NPY](tensors/0000681.npy) |
| 682 | `model.layers.23.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.59375 / 15.3125 / 0.03557474014814943 / 1.3801186934688665 | [NPY](tensors/0000682.npy) |
| 683 | `model.layers.23.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 57.25 / -0.0005243712001376682 / 1.7432840582915943 | [NPY](tensors/0000683.npy) |
| 684 | `model.layers.23.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.75 / 38.25 / -0.10232632234692574 / 5.3673453478017485 | [NPY](tensors/0000684.npy) |
| 685 | `model.layers.23.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 57.25 / -0.0005243712001376682 / 1.7432840582915943 | [NPY](tensors/0000685.npy) |
| 686 | `model.layers.23.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.9375 / 7.84375 / -0.15643680095672607 / 2.6894774166738933 | [NPY](tensors/0000686.npy) |
| 687 | `model.layers.23.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.3125 / 5.59375 / -0.07590298284776509 / 1.106591683321661 | [NPY](tensors/0000687.npy) |
| 688 | `model.layers.23.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5408.0 / 5696.0 / 5.854394170973036 / 240.49690645934098 | [NPY](tensors/0000688.npy) |
| 689 | `model.layers.23.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5408.0 / 5696.0 / 5.854394170973036 / 240.49690645934098 | [NPY](tensors/0000689.npy) |
| 690 | `model.layers.23.self_attn` | 5 | `output[1]` | [1, 64, 1, 878] | torch.bfloat16 → float32 | 5.245803791353865e-15 / 0.87890625 / 0.0008502862869998674 / 0.006186536050655819 | [NPY](tensors/0000690.npy) |
| 691 | `model.layers.23.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 9280.0 / 2.9682861328125 / 515.650081650668 | [NPY](tensors/0000691.npy) |
| 692 | `model.layers.23.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 8.4375 / -0.017815037568410238 / 0.9116807307428423 | [NPY](tensors/0000692.npy) |
| 693 | `model.layers.23.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 8.4375 / -0.017815037568410238 / 0.9116807307428423 | [NPY](tensors/0000693.npy) |
| 694 | `model.layers.23.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -29.875 / 8.4375 / -0.017815037568410238 / 0.9116807307428423 | [NPY](tensors/0000694.npy) |
| 695 | `model.layers.23.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 696 | `model.layers.23.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 697 | `model.layers.23.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 698 | `model.layers.23.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1240.0 / 880.0 / -1.6254309760199652 / 69.13343041490731 | [NPY](tensors/0000698.npy) |
| 699 | `model.layers.23.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1240.0 / 880.0 / -1.6254309760199652 / 69.13343041490731 | [NPY](tensors/0000699.npy) |
| 700 | `model.layers.23.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.6953125 / 1.125 / 0.09420859813690186 / 0.37395821479940805 | [NPY](tensors/0000700.npy) |
| 701 | `model.layers.23` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8256.0 / 8576.0 / 1.3388726128472221 / 483.4823680094409 | [NPY](tensors/0000701.npy) |
| 780 | `model.layers.23` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 10240.0 / -6.1183837890625 / 489.8189236667184 | [NPY](tensors/0000780.npy) |
| 781 | `model.layers.23` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 879] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000781.npy) |
| 782 | `model.layers.23` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5615997314453125 / 0.9848671705266577 | [NPY](tensors/0000782.npy) |
| 783 | `model.layers.23` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.030482351779937744 / 0.7236419726526301 | [NPY](tensors/0000783.npy) |
| 784 | `model.layers.23` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 878.0 / 878.0 / 878.0 / 0.0 | [NPY](tensors/0000784.npy) |
| 785 | `model.layers.23` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 786 | `model.layers.23` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 787 | `model.layers.23` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 788 | `model.layers.23.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 10240.0 / -6.1183837890625 / 489.8189236667184 | [NPY](tensors/0000788.npy) |
| 789 | `model.layers.23.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.25 / -0.007300288147396512 / 1.737385430793795 | [NPY](tensors/0000789.npy) |
| 790 | `model.layers.23.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.25 / -0.007300288147396512 / 1.737385430793795 | [NPY](tensors/0000790.npy) |
| 791 | `model.layers.23.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 879] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000791.npy) |
| 792 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 878.0 / 878.0 / 878.0 / 0.0 | [NPY](tensors/0000792.npy) |
| 793 | `model.layers.23.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 794 | `model.layers.23.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 795 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5615997314453125 / 0.9848671705266577 | [NPY](tensors/0000795.npy) |
| 796 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.030482351779937744 / 0.7236419726526301 | [NPY](tensors/0000796.npy) |
| 797 | `model.layers.23.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 798 | `model.layers.23.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.25 / -0.007300288147396512 / 1.737385430793795 | [NPY](tensors/0000798.npy) |
| 799 | `model.layers.23.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 16.375 / 0.03841289598494768 / 1.4185357100742384 | [NPY](tensors/0000799.npy) |
| 800 | `model.layers.23.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.25 / -0.007300288147396512 / 1.737385430793795 | [NPY](tensors/0000800.npy) |
| 801 | `model.layers.23.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 39.25 / -0.0704461932182312 / 5.218524778221689 | [NPY](tensors/0000801.npy) |
| 802 | `model.layers.23.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.25 / -0.007300288147396512 / 1.737385430793795 | [NPY](tensors/0000802.npy) |
| 803 | `model.layers.23.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.75 / 6.875 / -0.1365263517946005 / 1.9599532454676845 | [NPY](tensors/0000803.npy) |
| 804 | `model.layers.23.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.0625 / 6.125 / -0.05502225802047178 / 0.9112729672191443 | [NPY](tensors/0000804.npy) |
| 805 | `model.layers.23.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5664.0 / 5.792224566141765 / 237.67175564713506 | [NPY](tensors/0000805.npy) |
| 806 | `model.layers.23.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5664.0 / 5.792224566141765 / 237.67175564713506 | [NPY](tensors/0000806.npy) |
| 807 | `model.layers.23.self_attn` | 6 | `output[1]` | [1, 64, 1, 879] | torch.bfloat16 → float32 | 4.440892098500626e-16 / 0.90234375 / 0.0006554505959233641 / 0.006244589750285903 | [NPY](tensors/0000807.npy) |
| 808 | `model.layers.23.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 10112.0 / -0.3149441189236111 / 562.003913561134 | [NPY](tensors/0000808.npy) |
| 809 | `model.layers.23.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 8.125 / -0.025025451183319093 / 0.9855514725995013 | [NPY](tensors/0000809.npy) |
| 810 | `model.layers.23.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 8.125 / -0.025025451183319093 / 0.9855514725995013 | [NPY](tensors/0000810.npy) |
| 811 | `model.layers.23.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.25 / 8.125 / -0.025025451183319093 / 0.9855514725995013 | [NPY](tensors/0000811.npy) |
| 812 | `model.layers.23.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 813 | `model.layers.23.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 814 | `model.layers.23.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 815 | `model.layers.23.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1224.0 / 876.0 / -1.6635841793484158 / 61.89723417886158 | [NPY](tensors/0000815.npy) |
| 816 | `model.layers.23.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1224.0 / 876.0 / -1.6635841793484158 / 61.89723417886158 | [NPY](tensors/0000816.npy) |
| 817 | `model.layers.23.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.59765625 / 1.15625 / 0.017789840698242188 / 0.3519502461779461 | [NPY](tensors/0000817.npy) |
| 818 | `model.layers.23` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9792.0 / 9664.0 / -1.9445366753472222 / 539.5398378494357 | [NPY](tensors/0000818.npy) |
| 897 | `model.layers.23` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9920.0 / 1.5191487630208333 / 448.9820076583929 | [NPY](tensors/0000897.npy) |
| 898 | `model.layers.23` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 880] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000898.npy) |
| 899 | `model.layers.23` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.5797119140625 / 1.0186800490978136 | [NPY](tensors/0000899.npy) |
| 900 | `model.layers.23` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.296875 / 0.009048700332641602 / 0.6598895155407865 | [NPY](tensors/0000900.npy) |
| 901 | `model.layers.23` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 879.0 / 879.0 / 879.0 / 0.0 | [NPY](tensors/0000901.npy) |
| 902 | `model.layers.23` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 903 | `model.layers.23` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 904 | `model.layers.23` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 905 | `model.layers.23.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9920.0 / 1.5191487630208333 / 448.9820076583929 | [NPY](tensors/0000905.npy) |
| 906 | `model.layers.23.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 59.5 / 0.013990681701236301 / 1.766267062655799 | [NPY](tensors/0000906.npy) |
| 907 | `model.layers.23.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 59.5 / 0.013990681701236301 / 1.766267062655799 | [NPY](tensors/0000907.npy) |
| 908 | `model.layers.23.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 880] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000908.npy) |
| 909 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 879.0 / 879.0 / 879.0 / 0.0 | [NPY](tensors/0000909.npy) |
| 910 | `model.layers.23.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 911 | `model.layers.23.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 912 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.5797119140625 / 1.0186800490978136 | [NPY](tensors/0000912.npy) |
| 913 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.296875 / 0.009048700332641602 / 0.6598895155407865 | [NPY](tensors/0000913.npy) |
| 914 | `model.layers.23.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 915 | `model.layers.23.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 59.5 / 0.013990681701236301 / 1.766267062655799 | [NPY](tensors/0000915.npy) |
| 916 | `model.layers.23.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.21875 / 13.875 / 0.033629737386945635 / 1.3693023497475023 | [NPY](tensors/0000916.npy) |
| 917 | `model.layers.23.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 59.5 / 0.013990681701236301 / 1.766267062655799 | [NPY](tensors/0000917.npy) |
| 918 | `model.layers.23.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.5 / 42.5 / -0.16648823022842407 / 5.560454069873513 | [NPY](tensors/0000918.npy) |
| 919 | `model.layers.23.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 59.5 / 0.013990681701236301 / 1.766267062655799 | [NPY](tensors/0000919.npy) |
| 920 | `model.layers.23.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.8125 / 10.4375 / -0.16226017475128174 / 3.015389721188541 | [NPY](tensors/0000920.npy) |
| 921 | `model.layers.23.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.75 / 5.6875 / -0.07000571640674025 / 1.2698530643495451 | [NPY](tensors/0000921.npy) |
| 922 | `model.layers.23.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5760.0 / 6048.0 / 6.132992299397786 / 257.93171795138284 | [NPY](tensors/0000922.npy) |
| 923 | `model.layers.23.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5760.0 / 6048.0 / 6.132992299397786 / 257.93171795138284 | [NPY](tensors/0000923.npy) |
| 924 | `model.layers.23.self_attn` | 7 | `output[1]` | [1, 64, 1, 880] | torch.bfloat16 → float32 | 6.439293542825908e-14 / 0.8828125 / 0.000901014350609091 / 0.006630592317059189 | [NPY](tensors/0000924.npy) |
| 925 | `model.layers.23.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9280.0 / 9728.0 / 7.658951822916666 / 531.284571835634 | [NPY](tensors/0000925.npy) |
| 926 | `model.layers.23.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.5 / 9.0625 / -0.007590542236963908 / 0.9349387679433899 | [NPY](tensors/0000926.npy) |
| 927 | `model.layers.23.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.5 / 9.0625 / -0.007590542236963908 / 0.9349387679433899 | [NPY](tensors/0000927.npy) |
| 928 | `model.layers.23.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.5 / 9.0625 / -0.007590542236963908 / 0.9349387679433899 | [NPY](tensors/0000928.npy) |
| 929 | `model.layers.23.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 930 | `model.layers.23.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 931 | `model.layers.23.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 932 | `model.layers.23.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1472.0 / 1080.0 / -1.1136066224839953 / 62.09953396617949 | [NPY](tensors/0000932.npy) |
| 933 | `model.layers.23.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1472.0 / 1080.0 / -1.1136066224839953 / 62.09953396617949 | [NPY](tensors/0000933.npy) |
| 934 | `model.layers.23.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.703125 / 1.2265625 / 0.09021949768066406 / 0.3916021428226915 | [NPY](tensors/0000934.npy) |
| 935 | `model.layers.23` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 9664.0 / 6.513929578993055 / 527.1160261802222 | [NPY](tensors/0000935.npy) |
| 1014 | `model.layers.23` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 10432.0 / 2.3680921766493057 / 468.0520962631843 | [NPY](tensors/0001014.npy) |
| 1015 | `model.layers.23` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 881] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001015.npy) |
| 1016 | `model.layers.23` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5914459228515625 / 1.036270522436494 | [NPY](tensors/0001016.npy) |
| 1017 | `model.layers.23` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.0005860328674316406 / 0.6206299087009224 | [NPY](tensors/0001017.npy) |
| 1018 | `model.layers.23` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 880.0 / 880.0 / 880.0 / 0.0 | [NPY](tensors/0001018.npy) |
| 1019 | `model.layers.23` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1020 | `model.layers.23` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1021 | `model.layers.23` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1022 | `model.layers.23.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 10432.0 / 2.3680921766493057 / 468.0520962631843 | [NPY](tensors/0001022.npy) |
| 1023 | `model.layers.23.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 60.0 / 0.01946547163857354 / 1.7596763876502883 | [NPY](tensors/0001023.npy) |
| 1024 | `model.layers.23.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 60.0 / 0.01946547163857354 / 1.7596763876502883 | [NPY](tensors/0001024.npy) |
| 1025 | `model.layers.23.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 881] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001025.npy) |
| 1026 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 880.0 / 880.0 / 880.0 / 0.0 | [NPY](tensors/0001026.npy) |
| 1027 | `model.layers.23.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1028 | `model.layers.23.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1029 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5914459228515625 / 1.036270522436494 | [NPY](tensors/0001029.npy) |
| 1030 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.0005860328674316406 / 0.6206299087009224 | [NPY](tensors/0001030.npy) |
| 1031 | `model.layers.23.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1032 | `model.layers.23.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 60.0 / 0.01946547163857354 / 1.7596763876502883 | [NPY](tensors/0001032.npy) |
| 1033 | `model.layers.23.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.53125 / 14.375 / 0.020536598065518774 / 1.3894148221481504 | [NPY](tensors/0001033.npy) |
| 1034 | `model.layers.23.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 60.0 / 0.01946547163857354 / 1.7596763876502883 | [NPY](tensors/0001034.npy) |
| 1035 | `model.layers.23.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -46.0 / 43.25 / -0.07357113063335419 / 5.556590064179935 | [NPY](tensors/0001035.npy) |
| 1036 | `model.layers.23.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 60.0 / 0.01946547163857354 / 1.7596763876502883 | [NPY](tensors/0001036.npy) |
| 1037 | `model.layers.23.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.625 / 6.53125 / -0.03156858682632446 / 2.0541679631557646 | [NPY](tensors/0001037.npy) |
| 1038 | `model.layers.23.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.1875 / 6.5625 / -0.05728517426177859 / 1.4739754976483603 | [NPY](tensors/0001038.npy) |
| 1039 | `model.layers.23.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5952.0 / 6208.0 / 5.1939559247758655 / 266.62321122021876 | [NPY](tensors/0001039.npy) |
| 1040 | `model.layers.23.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5952.0 / 6208.0 / 5.1939559247758655 / 266.62321122021876 | [NPY](tensors/0001040.npy) |
| 1041 | `model.layers.23.self_attn` | 8 | `output[1]` | [1, 64, 1, 881] | torch.bfloat16 → float32 | 6.616929226765933e-14 / 0.91015625 / 0.0009281643482842982 / 0.008183795380777147 | [NPY](tensors/0001041.npy) |
| 1042 | `model.layers.23.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9664.0 / 10368.0 / 7.525965711805555 / 560.2302273671904 | [NPY](tensors/0001042.npy) |
| 1043 | `model.layers.23.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 7.71875 / -0.00797493921385871 / 0.9652074543383329 | [NPY](tensors/0001043.npy) |
| 1044 | `model.layers.23.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 7.71875 / -0.00797493921385871 / 0.9652074543383329 | [NPY](tensors/0001044.npy) |
| 1045 | `model.layers.23.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.75 / 7.71875 / -0.00797493921385871 / 0.9652074543383329 | [NPY](tensors/0001045.npy) |
| 1046 | `model.layers.23.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1047 | `model.layers.23.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1048 | `model.layers.23.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1049 | `model.layers.23.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1328.0 / 1088.0 / -2.3299014621310765 / 75.04708641263088 | [NPY](tensors/0001049.npy) |
| 1050 | `model.layers.23.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1328.0 / 1088.0 / -2.3299014621310765 / 75.04708641263088 | [NPY](tensors/0001050.npy) |
| 1051 | `model.layers.23.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.85546875 / 1.375 / 0.04605865478515625 / 0.46255778208427717 | [NPY](tensors/0001051.npy) |
| 1052 | `model.layers.23` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9024.0 / 9856.0 / 5.177182006835937 / 534.523961482367 | [NPY](tensors/0001052.npy) |
| 1131 | `model.layers.23` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 9088.0 / -0.6634969075520833 / 439.65090189120195 | [NPY](tensors/0001131.npy) |
| 1132 | `model.layers.23` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 882] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001132.npy) |
| 1133 | `model.layers.23` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.594635009765625 / 0.998380462956763 | [NPY](tensors/0001133.npy) |
| 1134 | `model.layers.23` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3125 / -0.016051054000854492 / 0.6776192851250942 | [NPY](tensors/0001134.npy) |
| 1135 | `model.layers.23` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 881.0 / 881.0 / 881.0 / 0.0 | [NPY](tensors/0001135.npy) |
| 1136 | `model.layers.23` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1137 | `model.layers.23` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1138 | `model.layers.23` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1139 | `model.layers.23.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 9088.0 / -0.6634969075520833 / 439.65090189120195 | [NPY](tensors/0001139.npy) |
| 1140 | `model.layers.23.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 54.0 / 0.0025993693206045362 / 1.7290803073626881 | [NPY](tensors/0001140.npy) |
| 1141 | `model.layers.23.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 54.0 / 0.0025993693206045362 / 1.7290803073626881 | [NPY](tensors/0001141.npy) |
| 1142 | `model.layers.23.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 882] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001142.npy) |
| 1143 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 881.0 / 881.0 / 881.0 / 0.0 | [NPY](tensors/0001143.npy) |
| 1144 | `model.layers.23.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1145 | `model.layers.23.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1146 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.594635009765625 / 0.998380462956763 | [NPY](tensors/0001146.npy) |
| 1147 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3125 / -0.016051054000854492 / 0.6776192851250942 | [NPY](tensors/0001147.npy) |
| 1148 | `model.layers.23.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1149 | `model.layers.23.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 54.0 / 0.0025993693206045362 / 1.7290803073626881 | [NPY](tensors/0001149.npy) |
| 1150 | `model.layers.23.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.125 / 16.0 / 0.029451290611177683 / 1.4767952337557457 | [NPY](tensors/0001150.npy) |
| 1151 | `model.layers.23.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 54.0 / 0.0025993693206045362 / 1.7290803073626881 | [NPY](tensors/0001151.npy) |
| 1152 | `model.layers.23.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -67.5 / 45.0 / -0.05312567949295044 / 6.47337451742646 | [NPY](tensors/0001152.npy) |
| 1153 | `model.layers.23.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 54.0 / 0.0025993693206045362 / 1.7290803073626881 | [NPY](tensors/0001153.npy) |
| 1154 | `model.layers.23.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.25 / 16.125 / -0.5036933124065399 / 3.597864111698096 | [NPY](tensors/0001154.npy) |
| 1155 | `model.layers.23.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.6875 / 5.59375 / -0.040945509099401534 / 1.290740704829559 | [NPY](tensors/0001155.npy) |
| 1156 | `model.layers.23.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5760.0 / 6016.0 / 4.903620613945855 / 256.9836673851485 | [NPY](tensors/0001156.npy) |
| 1157 | `model.layers.23.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5760.0 / 6016.0 / 4.903620613945855 / 256.9836673851485 | [NPY](tensors/0001157.npy) |
| 1158 | `model.layers.23.self_attn` | 9 | `output[1]` | [1, 64, 1, 882] | torch.bfloat16 → float32 | 8.038014698286133e-14 / 0.859375 / 0.0008786244649048172 / 0.007275021329386836 | [NPY](tensors/0001158.npy) |
| 1159 | `model.layers.23.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9984.0 / 9344.0 / 4.229568142361111 / 540.709049291769 | [NPY](tensors/0001159.npy) |
| 1160 | `model.layers.23.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 8.25 / -0.0187417295244005 / 1.0149617313402617 | [NPY](tensors/0001160.npy) |
| 1161 | `model.layers.23.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 8.25 / -0.0187417295244005 / 1.0149617313402617 | [NPY](tensors/0001161.npy) |
| 1162 | `model.layers.23.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.5 / 8.25 / -0.0187417295244005 / 1.0149617313402617 | [NPY](tensors/0001162.npy) |
| 1163 | `model.layers.23.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1164 | `model.layers.23.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1165 | `model.layers.23.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1166 | `model.layers.23.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1584.0 / 1552.0 / -0.7220613585578071 / 94.24818527456917 | [NPY](tensors/0001166.npy) |
| 1167 | `model.layers.23.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1584.0 / 1552.0 / -0.7220613585578071 / 94.24818527456917 | [NPY](tensors/0001167.npy) |
| 1168 | `model.layers.23.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0625 / 1.046875 / 0.07625198364257812 / 0.45795819598325915 | [NPY](tensors/0001168.npy) |
| 1169 | `model.layers.23` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8896.0 / 8320.0 / 3.5048529730902778 / 474.56181775034497 | [NPY](tensors/0001169.npy) |
| 1248 | `model.layers.23` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9216.0 / 8960.0 / -3.871434529622396 / 422.56007833109396 | [NPY](tensors/0001248.npy) |
| 1249 | `model.layers.23` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 883] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001249.npy) |
| 1250 | `model.layers.23` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.611114501953125 / 0.9771971733502269 | [NPY](tensors/0001250.npy) |
| 1251 | `model.layers.23` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / -0.047824978828430176 / 0.6921356554670257 | [NPY](tensors/0001251.npy) |
| 1252 | `model.layers.23` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 882.0 / 882.0 / 882.0 / 0.0 | [NPY](tensors/0001252.npy) |
| 1253 | `model.layers.23` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1254 | `model.layers.23` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1255 | `model.layers.23` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1256 | `model.layers.23.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9216.0 / 8960.0 / -3.871434529622396 / 422.56007833109396 | [NPY](tensors/0001256.npy) |
| 1257 | `model.layers.23.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 53.25 / -0.00977051854133606 / 1.731947241116189 | [NPY](tensors/0001257.npy) |
| 1258 | `model.layers.23.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 53.25 / -0.00977051854133606 / 1.731947241116189 | [NPY](tensors/0001258.npy) |
| 1259 | `model.layers.23.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 883] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001259.npy) |
| 1260 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 882.0 / 882.0 / 882.0 / 0.0 | [NPY](tensors/0001260.npy) |
| 1261 | `model.layers.23.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1262 | `model.layers.23.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1263 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.611114501953125 / 0.9771971733502269 | [NPY](tensors/0001263.npy) |
| 1264 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / -0.047824978828430176 / 0.6921356554670257 | [NPY](tensors/0001264.npy) |
| 1265 | `model.layers.23.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1266 | `model.layers.23.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 53.25 / -0.00977051854133606 / 1.731947241116189 | [NPY](tensors/0001266.npy) |
| 1267 | `model.layers.23.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.75 / 14.9375 / 0.03905343945370987 / 1.4923463846320946 | [NPY](tensors/0001267.npy) |
| 1268 | `model.layers.23.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 53.25 / -0.00977051854133606 / 1.731947241116189 | [NPY](tensors/0001268.npy) |
| 1269 | `model.layers.23.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.75 / 41.75 / -0.07778824865818024 / 5.975315253344763 | [NPY](tensors/0001269.npy) |
| 1270 | `model.layers.23.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 53.25 / -0.00977051854133606 / 1.731947241116189 | [NPY](tensors/0001270.npy) |
| 1271 | `model.layers.23.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.25 / 11.9375 / -0.03537851572036743 / 3.172705721698562 | [NPY](tensors/0001271.npy) |
| 1272 | `model.layers.23.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.0625 / 6.6875 / -0.04796229908242822 / 1.0888225287670759 | [NPY](tensors/0001272.npy) |
| 1273 | `model.layers.23.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 5856.0 / 5.097936534881592 / 249.4580125347972 | [NPY](tensors/0001273.npy) |
| 1274 | `model.layers.23.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 5856.0 / 5.097936534881592 / 249.4580125347972 | [NPY](tensors/0001274.npy) |
| 1275 | `model.layers.23.self_attn` | 10 | `output[1]` | [1, 64, 1, 883] | torch.bfloat16 → float32 | 6.52811138479592e-14 / 0.89453125 / 0.0007930831591513571 / 0.006399901597172269 | [NPY](tensors/0001275.npy) |
| 1276 | `model.layers.23.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9280.0 / 9088.0 / 1.2294013129340278 / 510.6457897084838 | [NPY](tensors/0001276.npy) |
| 1277 | `model.layers.23.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 9.4375 / -0.02458149856991238 / 0.9839124458612557 | [NPY](tensors/0001277.npy) |
| 1278 | `model.layers.23.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 9.4375 / -0.02458149856991238 / 0.9839124458612557 | [NPY](tensors/0001278.npy) |
| 1279 | `model.layers.23.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.0 / 9.4375 / -0.02458149856991238 / 0.9839124458612557 | [NPY](tensors/0001279.npy) |
| 1280 | `model.layers.23.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1281 | `model.layers.23.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1282 | `model.layers.23.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1283 | `model.layers.23.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -680.0 / 700.0 / -0.692913085884518 / 52.24278306153328 | [NPY](tensors/0001283.npy) |
| 1284 | `model.layers.23.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -680.0 / 700.0 / -0.692913085884518 / 52.24278306153328 | [NPY](tensors/0001284.npy) |
| 1285 | `model.layers.23.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.4453125 / 1.3671875 / 0.08797454833984375 / 0.38858471597332434 | [NPY](tensors/0001285.npy) |
| 1286 | `model.layers.23` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 8448.0 / 0.5315945095486111 / 483.4777126070049 | [NPY](tensors/0001286.npy) |
| 1365 | `model.layers.23` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9920.0 / -4.009266493055556 / 453.03091610759674 | [NPY](tensors/0001365.npy) |
| 1366 | `model.layers.23` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 884] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001366.npy) |
| 1367 | `model.layers.23` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.659881591796875 / 0.9579637378310449 | [NPY](tensors/0001367.npy) |
| 1368 | `model.layers.23` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / -0.07649624347686768 / 0.6710666469829912 | [NPY](tensors/0001368.npy) |
| 1369 | `model.layers.23` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 883.0 / 883.0 / 883.0 / 0.0 | [NPY](tensors/0001369.npy) |
| 1370 | `model.layers.23` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1371 | `model.layers.23` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1372 | `model.layers.23` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1373 | `model.layers.23.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9920.0 / -4.009266493055556 / 453.03091610759674 | [NPY](tensors/0001373.npy) |
| 1374 | `model.layers.23.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 55.0 / 0.0010252594947814941 / 1.7613215388664132 | [NPY](tensors/0001374.npy) |
| 1375 | `model.layers.23.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 55.0 / 0.0010252594947814941 / 1.7613215388664132 | [NPY](tensors/0001375.npy) |
| 1376 | `model.layers.23.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 884] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001376.npy) |
| 1377 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 883.0 / 883.0 / 883.0 / 0.0 | [NPY](tensors/0001377.npy) |
| 1378 | `model.layers.23.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1379 | `model.layers.23.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1380 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.659881591796875 / 0.9579637378310449 | [NPY](tensors/0001380.npy) |
| 1381 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / -0.07649624347686768 / 0.6710666469829912 | [NPY](tensors/0001381.npy) |
| 1382 | `model.layers.23.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1383 | `model.layers.23.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 55.0 / 0.0010252594947814941 / 1.7613215388664132 | [NPY](tensors/0001383.npy) |
| 1384 | `model.layers.23.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.15625 / 13.4375 / 0.03798874840140343 / 1.3732968110515218 | [NPY](tensors/0001384.npy) |
| 1385 | `model.layers.23.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 55.0 / 0.0010252594947814941 / 1.7613215388664132 | [NPY](tensors/0001385.npy) |
| 1386 | `model.layers.23.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.75 / 45.5 / -0.049983084201812744 / 5.7947107858946065 | [NPY](tensors/0001386.npy) |
| 1387 | `model.layers.23.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 55.0 / 0.0010252594947814941 / 1.7613215388664132 | [NPY](tensors/0001387.npy) |
| 1388 | `model.layers.23.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.875 / 6.625 / -0.07860782742500305 / 2.2693618540071636 | [NPY](tensors/0001388.npy) |
| 1389 | `model.layers.23.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.9375 / 11.1875 / -0.020341204944998026 / 1.5074019581876639 | [NPY](tensors/0001389.npy) |
| 1390 | `model.layers.23.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5824.0 / 5952.0 / 6.513922288682726 / 262.24736581260044 | [NPY](tensors/0001390.npy) |
| 1391 | `model.layers.23.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5824.0 / 5952.0 / 6.513922288682726 / 262.24736581260044 | [NPY](tensors/0001391.npy) |
| 1392 | `model.layers.23.self_attn` | 11 | `output[1]` | [1, 64, 1, 884] | torch.bfloat16 → float32 | 7.667477763817487e-16 / 0.9453125 / 0.0009289134264134474 / 0.007464702613513913 | [NPY](tensors/0001392.npy) |
| 1393 | `model.layers.23.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 9536.0 / 2.5360107421875 / 525.1963017594138 | [NPY](tensors/0001393.npy) |
| 1394 | `model.layers.23.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.625 / 10.5625 / -0.013588660293155246 / 1.027963858336681 | [NPY](tensors/0001394.npy) |
| 1395 | `model.layers.23.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.625 / 10.5625 / -0.013588660293155246 / 1.027963858336681 | [NPY](tensors/0001395.npy) |
| 1396 | `model.layers.23.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -25.625 / 10.5625 / -0.013588660293155246 / 1.027963858336681 | [NPY](tensors/0001396.npy) |
| 1397 | `model.layers.23.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1398 | `model.layers.23.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1399 | `model.layers.23.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1400 | `model.layers.23.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1680.0 / 1640.0 / -2.690755081176758 / 93.5438052085856 | [NPY](tensors/0001400.npy) |
| 1401 | `model.layers.23.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1680.0 / 1640.0 / -2.690755081176758 / 93.5438052085856 | [NPY](tensors/0001401.npy) |
| 1402 | `model.layers.23.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.78515625 / 1.546875 / -0.016448974609375 / 0.4268559565614432 | [NPY](tensors/0001402.npy) |
| 1403 | `model.layers.23` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9792.0 / -0.151318359375 / 554.2212327228145 | [NPY](tensors/0001403.npy) |
| 1482 | `model.layers.23` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 8960.0 / -3.5855821397569443 / 411.04868690867204 | [NPY](tensors/0001482.npy) |
| 1483 | `model.layers.23` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 885] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001483.npy) |
| 1484 | `model.layers.23` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.734130859375 / 0.896956143048102 | [NPY](tensors/0001484.npy) |
| 1485 | `model.layers.23` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.296875 / -0.06761544942855835 / 0.6796756860615183 | [NPY](tensors/0001485.npy) |
| 1486 | `model.layers.23` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 884.0 / 884.0 / 884.0 / 0.0 | [NPY](tensors/0001486.npy) |
| 1487 | `model.layers.23` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1488 | `model.layers.23` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1489 | `model.layers.23` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1490 | `model.layers.23.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 8960.0 / -3.5855821397569443 / 411.04868690867204 | [NPY](tensors/0001490.npy) |
| 1491 | `model.layers.23.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 58.5 / 0.009234095944298639 / 1.7882282362570774 | [NPY](tensors/0001491.npy) |
| 1492 | `model.layers.23.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 58.5 / 0.009234095944298639 / 1.7882282362570774 | [NPY](tensors/0001492.npy) |
| 1493 | `model.layers.23.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 885] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001493.npy) |
| 1494 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 884.0 / 884.0 / 884.0 / 0.0 | [NPY](tensors/0001494.npy) |
| 1495 | `model.layers.23.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1496 | `model.layers.23.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1497 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.734130859375 / 0.896956143048102 | [NPY](tensors/0001497.npy) |
| 1498 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.296875 / -0.06761544942855835 / 0.6796756860615183 | [NPY](tensors/0001498.npy) |
| 1499 | `model.layers.23.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1500 | `model.layers.23.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 58.5 / 0.009234095944298639 / 1.7882282362570774 | [NPY](tensors/0001500.npy) |
| 1501 | `model.layers.23.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.6875 / 16.375 / 0.052954527898691595 / 1.7122463621768975 | [NPY](tensors/0001501.npy) |
| 1502 | `model.layers.23.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 58.5 / 0.009234095944298639 / 1.7882282362570774 | [NPY](tensors/0001502.npy) |
| 1503 | `model.layers.23.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.5 / 41.0 / -0.06767874956130981 / 5.40616720630256 | [NPY](tensors/0001503.npy) |
| 1504 | `model.layers.23.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 58.5 / 0.009234095944298639 / 1.7882282362570774 | [NPY](tensors/0001504.npy) |
| 1505 | `model.layers.23.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.6875 / 12.4375 / 0.08962391316890717 / 3.7143058684928127 | [NPY](tensors/0001505.npy) |
| 1506 | `model.layers.23.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.875 / 11.625 / 0.05097548337653279 / 2.0114978535188643 | [NPY](tensors/0001506.npy) |
| 1507 | `model.layers.23.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3280.0 / 3008.0 / 1.147975789176093 / 173.91776723973996 | [NPY](tensors/0001507.npy) |
| 1508 | `model.layers.23.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3280.0 / 3008.0 / 1.147975789176093 / 173.91776723973996 | [NPY](tensors/0001508.npy) |
| 1509 | `model.layers.23.self_attn` | 12 | `output[1]` | [1, 64, 1, 885] | torch.bfloat16 → float32 | 2.220446049250313e-16 / 0.9609375 / 0.0008702986049093938 / 0.009220632724529124 | [NPY](tensors/0001509.npy) |
| 1510 | `model.layers.23.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7200.0 / 7200.0 / -2.429581705729167 / 416.8809947333147 | [NPY](tensors/0001510.npy) |
| 1511 | `model.layers.23.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 10.125 / -0.02579289542304145 / 1.3672123824650593 | [NPY](tensors/0001511.npy) |
| 1512 | `model.layers.23.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 10.125 / -0.02579289542304145 / 1.3672123824650593 | [NPY](tensors/0001512.npy) |
| 1513 | `model.layers.23.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.0 / 10.125 / -0.02579289542304145 / 1.3672123824650593 | [NPY](tensors/0001513.npy) |
| 1514 | `model.layers.23.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1515 | `model.layers.23.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1516 | `model.layers.23.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1517 | `model.layers.23.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5952.0 / 5696.0 / -3.499983384874132 / 285.35649403636995 | [NPY](tensors/0001517.npy) |
| 1518 | `model.layers.23.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5952.0 / 5696.0 / -3.499983384874132 / 285.35649403636995 | [NPY](tensors/0001518.npy) |
| 1519 | `model.layers.23.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.984375 / 1.390625 / 0.01184844970703125 / 1.2103817094738685 | [NPY](tensors/0001519.npy) |
| 1520 | `model.layers.23` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1840.0 / 1608.0 / -5.916824001736111 / 304.6007756503996 | [NPY](tensors/0001520.npy) |
| 1599 | `model.layers.23` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8896.0 / 10176.0 / 0.28838161892361114 / 429.11038004299144 | [NPY](tensors/0001599.npy) |
| 1600 | `model.layers.23` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 886] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001600.npy) |
| 1601 | `model.layers.23` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.7958755493164062 / 0.858839493189722 | [NPY](tensors/0001601.npy) |
| 1602 | `model.layers.23` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.005351245403289795 / 0.6623439987299442 | [NPY](tensors/0001602.npy) |
| 1603 | `model.layers.23` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 885.0 / 885.0 / 885.0 / 0.0 | [NPY](tensors/0001603.npy) |
| 1604 | `model.layers.23` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1605 | `model.layers.23` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1606 | `model.layers.23` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1607 | `model.layers.23.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8896.0 / 10176.0 / 0.28838161892361114 / 429.11038004299144 | [NPY](tensors/0001607.npy) |
| 1608 | `model.layers.23.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 63.75 / 0.021376648214128283 / 1.8350315708827092 | [NPY](tensors/0001608.npy) |
| 1609 | `model.layers.23.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 63.75 / 0.021376648214128283 / 1.8350315708827092 | [NPY](tensors/0001609.npy) |
| 1610 | `model.layers.23.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 886] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001610.npy) |
| 1611 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 885.0 / 885.0 / 885.0 / 0.0 | [NPY](tensors/0001611.npy) |
| 1612 | `model.layers.23.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1613 | `model.layers.23.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1614 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.7958755493164062 / 0.858839493189722 | [NPY](tensors/0001614.npy) |
| 1615 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.005351245403289795 / 0.6623439987299442 | [NPY](tensors/0001615.npy) |
| 1616 | `model.layers.23.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1617 | `model.layers.23.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 63.75 / 0.021376648214128283 / 1.8350315708827092 | [NPY](tensors/0001617.npy) |
| 1618 | `model.layers.23.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.125 / 14.1875 / 0.061751447356073186 / 1.6624859050058962 | [NPY](tensors/0001618.npy) |
| 1619 | `model.layers.23.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 63.75 / 0.021376648214128283 / 1.8350315708827092 | [NPY](tensors/0001619.npy) |
| 1620 | `model.layers.23.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -41.5 / 34.25 / -0.014479070901870728 / 5.609616070515337 | [NPY](tensors/0001620.npy) |
| 1621 | `model.layers.23.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 63.75 / 0.021376648214128283 / 1.8350315708827092 | [NPY](tensors/0001621.npy) |
| 1622 | `model.layers.23.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.3125 / 15.625 / 0.0030727386474609375 / 4.356374429724615 | [NPY](tensors/0001622.npy) |
| 1623 | `model.layers.23.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.1875 / 9.25 / 0.02383178286254406 / 1.8345137825334898 | [NPY](tensors/0001623.npy) |
| 1624 | `model.layers.23.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3616.0 / 3488.0 / 3.726717970106337 / 176.59589670507745 | [NPY](tensors/0001624.npy) |
| 1625 | `model.layers.23.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3616.0 / 3488.0 / 3.726717970106337 / 176.59589670507745 | [NPY](tensors/0001625.npy) |
| 1626 | `model.layers.23.self_attn` | 13 | `output[1]` | [1, 64, 1, 886] | torch.bfloat16 → float32 | 2.4702462297909733e-15 / 0.875 / 0.0008282244117517845 / 0.009280149256646733 | [NPY](tensors/0001626.npy) |
| 1627 | `model.layers.23.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7840.0 / 9280.0 / 3.9929741753472223 / 445.3785375697409 | [NPY](tensors/0001627.npy) |
| 1628 | `model.layers.23.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 10.375 / -0.0037637816535102 / 1.2875351682557103 | [NPY](tensors/0001628.npy) |
| 1629 | `model.layers.23.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 10.375 / -0.0037637816535102 / 1.2875351682557103 | [NPY](tensors/0001629.npy) |
| 1630 | `model.layers.23.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -40.0 / 10.375 / -0.0037637816535102 / 1.2875351682557103 | [NPY](tensors/0001630.npy) |
| 1631 | `model.layers.23.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1632 | `model.layers.23.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1633 | `model.layers.23.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1634 | `model.layers.23.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4096.0 / 3888.0 / -2.2849499914381237 / 198.79836218338093 | [NPY](tensors/0001634.npy) |
| 1635 | `model.layers.23.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4096.0 / 3888.0 / -2.2849499914381237 / 198.79836218338093 | [NPY](tensors/0001635.npy) |
| 1636 | `model.layers.23.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.59375 / 1.65625 / 0.06304931640625 / 1.3809292342604809 | [NPY](tensors/0001636.npy) |
| 1637 | `model.layers.23` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4032.0 / 5184.0 / 1.687863498263889 / 335.9123435367797 | [NPY](tensors/0001637.npy) |
| 1716 | `model.layers.23` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9088.0 / 2.3028971354166665 / 421.8465458684287 | [NPY](tensors/0001716.npy) |
| 1717 | `model.layers.23` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 887] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001717.npy) |
| 1718 | `model.layers.23` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.805328369140625 / 0.858282942374398 | [NPY](tensors/0001718.npy) |
| 1719 | `model.layers.23` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.2890625 / 0.08753019571304321 / 0.6450265564714699 | [NPY](tensors/0001719.npy) |
| 1720 | `model.layers.23` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 886.0 / 886.0 / 886.0 / 0.0 | [NPY](tensors/0001720.npy) |
| 1721 | `model.layers.23` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1722 | `model.layers.23` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1723 | `model.layers.23` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1724 | `model.layers.23.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9088.0 / 2.3028971354166665 / 421.8465458684287 | [NPY](tensors/0001724.npy) |
| 1725 | `model.layers.23.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.0 / 0.02537495493888855 / 1.8052121386919524 | [NPY](tensors/0001725.npy) |
| 1726 | `model.layers.23.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.0 / 0.02537495493888855 / 1.8052121386919524 | [NPY](tensors/0001726.npy) |
| 1727 | `model.layers.23.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 887] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001727.npy) |
| 1728 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 886.0 / 886.0 / 886.0 / 0.0 | [NPY](tensors/0001728.npy) |
| 1729 | `model.layers.23.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1730 | `model.layers.23.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1731 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.805328369140625 / 0.858282942374398 | [NPY](tensors/0001731.npy) |
| 1732 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.2890625 / 0.08753019571304321 / 0.6450265564714699 | [NPY](tensors/0001732.npy) |
| 1733 | `model.layers.23.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1734 | `model.layers.23.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.0 / 0.02537495493888855 / 1.8052121386919524 | [NPY](tensors/0001734.npy) |
| 1735 | `model.layers.23.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.5625 / 12.875 / 0.038192376028746367 / 1.6594895505635636 | [NPY](tensors/0001735.npy) |
| 1736 | `model.layers.23.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.0 / 0.02537495493888855 / 1.8052121386919524 | [NPY](tensors/0001736.npy) |
| 1737 | `model.layers.23.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 42.25 / 0.036311179399490356 / 6.000983934489769 | [NPY](tensors/0001737.npy) |
| 1738 | `model.layers.23.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.0 / 0.02537495493888855 / 1.8052121386919524 | [NPY](tensors/0001738.npy) |
| 1739 | `model.layers.23.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.375 / 10.0 / 0.10584688186645508 / 3.548613856969995 | [NPY](tensors/0001739.npy) |
| 1740 | `model.layers.23.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.0 / 9.6875 / 0.056062540505081415 / 1.7970239678598035 | [NPY](tensors/0001740.npy) |
| 1741 | `model.layers.23.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3984.0 / 3712.0 / 3.825120544433594 / 187.69509876585224 | [NPY](tensors/0001741.npy) |
| 1742 | `model.layers.23.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3984.0 / 3712.0 / 3.825120544433594 / 187.69509876585224 | [NPY](tensors/0001742.npy) |
| 1743 | `model.layers.23.self_attn` | 14 | `output[1]` | [1, 64, 1, 887] | torch.bfloat16 → float32 | 6.794564910705958e-14 / 0.96484375 / 0.0009720003187031996 / 0.009828896942112201 | [NPY](tensors/0001743.npy) |
| 1744 | `model.layers.23.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 8960.0 / 6.122281901041666 / 474.5668432279686 | [NPY](tensors/0001744.npy) |
| 1745 | `model.layers.23.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 7.71875 / -0.0007989618513319228 / 1.1757816460225003 | [NPY](tensors/0001745.npy) |
| 1746 | `model.layers.23.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 7.71875 / -0.0007989618513319228 / 1.1757816460225003 | [NPY](tensors/0001746.npy) |
| 1747 | `model.layers.23.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -29.625 / 7.71875 / -0.0007989618513319228 / 1.1757816460225003 | [NPY](tensors/0001747.npy) |
| 1748 | `model.layers.23.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1749 | `model.layers.23.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1750 | `model.layers.23.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1751 | `model.layers.23.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6464.0 / 5824.0 / -1.5783163494533963 / 333.21214354863366 | [NPY](tensors/0001751.npy) |
| 1752 | `model.layers.23.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6464.0 / 5824.0 / -1.5783163494533963 / 333.21214354863366 | [NPY](tensors/0001752.npy) |
| 1753 | `model.layers.23.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.140625 / 1.84375 / -0.060764312744140625 / 0.787585118102541 | [NPY](tensors/0001753.npy) |
| 1754 | `model.layers.23` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3328.0 / 2720.0 / 4.540863715277778 / 358.65087490742695 | [NPY](tensors/0001754.npy) |
| 1833 | `model.layers.23` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9984.0 / 4.936797417534722 / 432.65652653327135 | [NPY](tensors/0001833.npy) |
| 1834 | `model.layers.23` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 888] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001834.npy) |
| 1835 | `model.layers.23` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.752716064453125 / 0.8717363915407874 | [NPY](tensors/0001835.npy) |
| 1836 | `model.layers.23` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / 0.1641445755958557 / 0.6760071928531548 | [NPY](tensors/0001836.npy) |
| 1837 | `model.layers.23` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 887.0 / 887.0 / 887.0 / 0.0 | [NPY](tensors/0001837.npy) |
| 1838 | `model.layers.23` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1839 | `model.layers.23` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1840 | `model.layers.23` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1841 | `model.layers.23.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9984.0 / 4.936797417534722 / 432.65652653327135 | [NPY](tensors/0001841.npy) |
| 1842 | `model.layers.23.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 62.0 / 0.03175202873018053 / 1.8108129250549847 | [NPY](tensors/0001842.npy) |
| 1843 | `model.layers.23.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 62.0 / 0.03175202873018053 / 1.8108129250549847 | [NPY](tensors/0001843.npy) |
| 1844 | `model.layers.23.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 888] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001844.npy) |
| 1845 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 887.0 / 887.0 / 887.0 / 0.0 | [NPY](tensors/0001845.npy) |
| 1846 | `model.layers.23.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1847 | `model.layers.23.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1848 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.752716064453125 / 0.8717363915407874 | [NPY](tensors/0001848.npy) |
| 1849 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / 0.1641445755958557 / 0.6760071928531548 | [NPY](tensors/0001849.npy) |
| 1850 | `model.layers.23.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1851 | `model.layers.23.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 62.0 / 0.03175202873018053 / 1.8108129250549847 | [NPY](tensors/0001851.npy) |
| 1852 | `model.layers.23.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.5 / 13.5 / 0.03975640702992678 / 1.5334733253013555 | [NPY](tensors/0001852.npy) |
| 1853 | `model.layers.23.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 62.0 / 0.03175202873018053 / 1.8108129250549847 | [NPY](tensors/0001853.npy) |
| 1854 | `model.layers.23.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.75 / 46.75 / -0.006932251155376434 / 6.034204629681617 | [NPY](tensors/0001854.npy) |
| 1855 | `model.layers.23.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 62.0 / 0.03175202873018053 / 1.8108129250549847 | [NPY](tensors/0001855.npy) |
| 1856 | `model.layers.23.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.625 / 11.6875 / -0.0625998005270958 / 3.642049025440081 | [NPY](tensors/0001856.npy) |
| 1857 | `model.layers.23.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.625 / 7.0625 / -0.019419074873439968 / 1.693985126291946 | [NPY](tensors/0001857.npy) |
| 1858 | `model.layers.23.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3744.0 / 3728.0 / 2.9160905838012696 / 170.04171198773457 | [NPY](tensors/0001858.npy) |
| 1859 | `model.layers.23.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3744.0 / 3728.0 / 2.9160905838012696 / 170.04171198773457 | [NPY](tensors/0001859.npy) |
| 1860 | `model.layers.23.self_attn` | 15 | `output[1]` | [1, 64, 1, 888] | torch.bfloat16 → float32 | 9.048317650695026e-15 / 0.91796875 / 0.0009667544761725712 / 0.010430286169047573 | [NPY](tensors/0001860.npy) |
| 1861 | `model.layers.23.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8384.0 / 9088.0 / 7.8675347222222225 / 452.02219469578483 | [NPY](tensors/0001861.npy) |
| 1862 | `model.layers.23.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.0 / 10.0625 / 0.00914739105436537 / 1.206633586764566 | [NPY](tensors/0001862.npy) |
| 1863 | `model.layers.23.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.0 / 10.0625 / 0.00914739105436537 / 1.206633586764566 | [NPY](tensors/0001863.npy) |
| 1864 | `model.layers.23.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -39.0 / 10.0625 / 0.00914739105436537 / 1.206633586764566 | [NPY](tensors/0001864.npy) |
| 1865 | `model.layers.23.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1866 | `model.layers.23.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1867 | `model.layers.23.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1868 | `model.layers.23.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4448.0 / 4160.0 / -3.624023267957899 / 222.13236607337117 | [NPY](tensors/0001868.npy) |
| 1869 | `model.layers.23.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4448.0 / 4160.0 / -3.624023267957899 / 222.13236607337117 | [NPY](tensors/0001869.npy) |
| 1870 | `model.layers.23.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.390625 / 2.140625 / 0.0825653076171875 / 1.2635490992207548 | [NPY](tensors/0001870.npy) |
| 1871 | `model.layers.23` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4224.0 / 4640.0 / 4.250070529513889 / 335.2764054794689 | [NPY](tensors/0001871.npy) |
| 1950 | `model.layers.23` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6464.0 / 6304.0 / 4.024283854166667 / 388.4588468780227 | [NPY](tensors/0001950.npy) |
| 1951 | `model.layers.23` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 889] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001951.npy) |
| 1952 | `model.layers.23` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6714019775390625 / 0.9432200886540145 | [NPY](tensors/0001952.npy) |
| 1953 | `model.layers.23` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.18380916118621826 / 0.659819262490622 | [NPY](tensors/0001953.npy) |
| 1954 | `model.layers.23` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 888.0 / 888.0 / 888.0 / 0.0 | [NPY](tensors/0001954.npy) |
| 1955 | `model.layers.23` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1956 | `model.layers.23` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1957 | `model.layers.23` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1958 | `model.layers.23.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6464.0 / 6304.0 / 4.024283854166667 / 388.4588468780227 | [NPY](tensors/0001958.npy) |
| 1959 | `model.layers.23.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.0 / 43.5 / 0.03023260169559055 / 1.6689060992528977 | [NPY](tensors/0001959.npy) |
| 1960 | `model.layers.23.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.0 / 43.5 / 0.03023260169559055 / 1.6689060992528977 | [NPY](tensors/0001960.npy) |
| 1961 | `model.layers.23.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 889] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001961.npy) |
| 1962 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 888.0 / 888.0 / 888.0 / 0.0 | [NPY](tensors/0001962.npy) |
| 1963 | `model.layers.23.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1964 | `model.layers.23.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1965 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6714019775390625 / 0.9432200886540145 | [NPY](tensors/0001965.npy) |
| 1966 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.18380916118621826 / 0.659819262490622 | [NPY](tensors/0001966.npy) |
| 1967 | `model.layers.23.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1968 | `model.layers.23.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.0 / 43.5 / 0.03023260169559055 / 1.6689060992528977 | [NPY](tensors/0001968.npy) |
| 1969 | `model.layers.23.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.0 / 14.0625 / 0.024562276375945657 / 1.7389306391538195 | [NPY](tensors/0001969.npy) |
| 1970 | `model.layers.23.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.0 / 43.5 / 0.03023260169559055 / 1.6689060992528977 | [NPY](tensors/0001970.npy) |
| 1971 | `model.layers.23.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -63.5 / 47.25 / -0.007378235459327698 / 6.83540187099904 | [NPY](tensors/0001971.npy) |
| 1972 | `model.layers.23.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.0 / 43.5 / 0.03023260169559055 / 1.6689060992528977 | [NPY](tensors/0001972.npy) |
| 1973 | `model.layers.23.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.0 / 14.25 / -0.12739145755767822 / 4.065132428979553 | [NPY](tensors/0001973.npy) |
| 1974 | `model.layers.23.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.375 / 13.25 / 0.057306106347823516 / 1.7505392860145077 | [NPY](tensors/0001974.npy) |
| 1975 | `model.layers.23.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3936.0 / 4000.0 / 3.3996511671278213 / 195.38110705785414 | [NPY](tensors/0001975.npy) |
| 1976 | `model.layers.23.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3936.0 / 4000.0 / 3.3996511671278213 / 195.38110705785414 | [NPY](tensors/0001976.npy) |
| 1977 | `model.layers.23.self_attn` | 16 | `output[1]` | [1, 64, 1, 889] | torch.bfloat16 → float32 | 2.5224267119483557e-13 / 0.97265625 / 0.0008983773572257002 / 0.010091094698246332 | [NPY](tensors/0001977.npy) |
| 1978 | `model.layers.23.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7200.0 / 7296.0 / 7.451985677083333 / 465.9773746919805 | [NPY](tensors/0001978.npy) |
| 1979 | `model.layers.23.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.375 / 8.25 / 0.0031326353549957276 / 1.3779519506829865 | [NPY](tensors/0001979.npy) |
| 1980 | `model.layers.23.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.375 / 8.25 / 0.0031326353549957276 / 1.3779519506829865 | [NPY](tensors/0001980.npy) |
| 1981 | `model.layers.23.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -28.375 / 8.25 / 0.0031326353549957276 / 1.3779519506829865 | [NPY](tensors/0001981.npy) |
| 1982 | `model.layers.23.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1983 | `model.layers.23.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1984 | `model.layers.23.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1985 | `model.layers.23.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7648.0 / 6784.0 / -5.696259583367242 / 463.85134732229744 | [NPY](tensors/0001985.npy) |
| 1986 | `model.layers.23.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7648.0 / 6784.0 / -5.696259583367242 / 463.85134732229744 | [NPY](tensors/0001986.npy) |
| 1987 | `model.layers.23.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.0625 / 2.28125 / 0.02449941635131836 / 1.076907896631842 | [NPY](tensors/0001987.npy) |
| 1988 | `model.layers.23` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1680.0 / 2240.0 / 1.7730034722222223 / 467.8943375727303 | [NPY](tensors/0001988.npy) |
| 2067 | `model.layers.23` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8960.0 / 9216.0 / 1.6174913194444445 / 420.4659067676104 | [NPY](tensors/0002067.npy) |
| 2068 | `model.layers.23` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 890] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002068.npy) |
| 2069 | `model.layers.23` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.61199951171875 / 1.0116022827243683 | [NPY](tensors/0002069.npy) |
| 2070 | `model.layers.23` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14778363704681396 / 0.6247390563478729 | [NPY](tensors/0002070.npy) |
| 2071 | `model.layers.23` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 889.0 / 889.0 / 889.0 / 0.0 | [NPY](tensors/0002071.npy) |
| 2072 | `model.layers.23` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2073 | `model.layers.23` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2074 | `model.layers.23` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2075 | `model.layers.23.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8960.0 / 9216.0 / 1.6174913194444445 / 420.4659067676104 | [NPY](tensors/0002075.npy) |
| 2076 | `model.layers.23.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 59.0 / 0.01906416548622979 / 1.7871405916252445 | [NPY](tensors/0002076.npy) |
| 2077 | `model.layers.23.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 59.0 / 0.01906416548622979 / 1.7871405916252445 | [NPY](tensors/0002077.npy) |
| 2078 | `model.layers.23.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 890] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002078.npy) |
| 2079 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 889.0 / 889.0 / 889.0 / 0.0 | [NPY](tensors/0002079.npy) |
| 2080 | `model.layers.23.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2081 | `model.layers.23.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2082 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.61199951171875 / 1.0116022827243683 | [NPY](tensors/0002082.npy) |
| 2083 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14778363704681396 / 0.6247390563478729 | [NPY](tensors/0002083.npy) |
| 2084 | `model.layers.23.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2085 | `model.layers.23.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 59.0 / 0.01906416548622979 / 1.7871405916252445 | [NPY](tensors/0002085.npy) |
| 2086 | `model.layers.23.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.5 / 12.375 / 0.01941612781956792 / 1.4702211856199858 | [NPY](tensors/0002086.npy) |
| 2087 | `model.layers.23.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 59.0 / 0.01906416548622979 / 1.7871405916252445 | [NPY](tensors/0002087.npy) |
| 2088 | `model.layers.23.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -64.0 / 45.75 / -0.11313748359680176 / 5.956727426645164 | [NPY](tensors/0002088.npy) |
| 2089 | `model.layers.23.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 59.0 / 0.01906416548622979 / 1.7871405916252445 | [NPY](tensors/0002089.npy) |
| 2090 | `model.layers.23.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.125 / 11.6875 / 0.14028191566467285 / 3.5201560544722335 | [NPY](tensors/0002090.npy) |
| 2091 | `model.layers.23.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.75 / 7.71875 / 0.01493249204941094 / 1.5306942243004478 | [NPY](tensors/0002091.npy) |
| 2092 | `model.layers.23.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 5664.0 / 3.0962204827202693 / 255.72179706716798 | [NPY](tensors/0002092.npy) |
| 2093 | `model.layers.23.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 5664.0 / 3.0962204827202693 / 255.72179706716798 | [NPY](tensors/0002093.npy) |
| 2094 | `model.layers.23.self_attn` | 17 | `output[1]` | [1, 64, 1, 890] | torch.bfloat16 → float32 | 7.945033519973776e-16 / 0.82421875 / 0.0008556270007712264 / 0.008071331525310206 | [NPY](tensors/0002094.npy) |
| 2095 | `model.layers.23.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9280.0 / 9600.0 / 4.70771484375 / 526.5223952611883 | [NPY](tensors/0002095.npy) |
| 2096 | `model.layers.23.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.75 / 6.8125 / -0.005014682478374905 / 1.0682625874288667 | [NPY](tensors/0002096.npy) |
| 2097 | `model.layers.23.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.75 / 6.8125 / -0.005014682478374905 / 1.0682625874288667 | [NPY](tensors/0002097.npy) |
| 2098 | `model.layers.23.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.75 / 6.8125 / -0.005014682478374905 / 1.0682625874288667 | [NPY](tensors/0002098.npy) |
| 2099 | `model.layers.23.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2100 | `model.layers.23.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2101 | `model.layers.23.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2102 | `model.layers.23.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3360.0 / 3200.0 / -2.947219509548611 / 193.70838519394022 | [NPY](tensors/0002102.npy) |
| 2103 | `model.layers.23.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3360.0 / 3200.0 / -2.947219509548611 / 193.70838519394022 | [NPY](tensors/0002103.npy) |
| 2104 | `model.layers.23.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.296875 / 1.3984375 / 0.01465606689453125 / 0.8299022274668021 | [NPY](tensors/0002104.npy) |
| 2105 | `model.layers.23` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6080.0 / 6240.0 / 1.763180881076389 / 398.5804767043196 | [NPY](tensors/0002105.npy) |
| 2184 | `model.layers.23` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9664.0 / 9792.0 / 0.37449544270833335 / 433.83742551550336 | [NPY](tensors/0002184.npy) |
| 2185 | `model.layers.23` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 891] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002185.npy) |
| 2186 | `model.layers.23` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6052932739257812 / 0.9920321858005083 | [NPY](tensors/0002186.npy) |
| 2187 | `model.layers.23` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.0962597131729126 / 0.670037121922543 | [NPY](tensors/0002187.npy) |
| 2188 | `model.layers.23` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 890.0 / 890.0 / 890.0 / 0.0 | [NPY](tensors/0002188.npy) |
| 2189 | `model.layers.23` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2190 | `model.layers.23` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2191 | `model.layers.23` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2192 | `model.layers.23.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9664.0 / 9792.0 / 0.37449544270833335 / 433.83742551550336 | [NPY](tensors/0002192.npy) |
| 2193 | `model.layers.23.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 60.75 / 0.018184414174821643 / 1.8026130642387936 | [NPY](tensors/0002193.npy) |
| 2194 | `model.layers.23.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 60.75 / 0.018184414174821643 / 1.8026130642387936 | [NPY](tensors/0002194.npy) |
| 2195 | `model.layers.23.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 891] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002195.npy) |
| 2196 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 890.0 / 890.0 / 890.0 / 0.0 | [NPY](tensors/0002196.npy) |
| 2197 | `model.layers.23.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2198 | `model.layers.23.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2199 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6052932739257812 / 0.9920321858005083 | [NPY](tensors/0002199.npy) |
| 2200 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.0962597131729126 / 0.670037121922543 | [NPY](tensors/0002200.npy) |
| 2201 | `model.layers.23.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2202 | `model.layers.23.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 60.75 / 0.018184414174821643 / 1.8026130642387936 | [NPY](tensors/0002202.npy) |
| 2203 | `model.layers.23.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.3125 / 14.875 / 0.013321679034561384 / 1.4555379517486318 | [NPY](tensors/0002203.npy) |
| 2204 | `model.layers.23.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 60.75 / 0.018184414174821643 / 1.8026130642387936 | [NPY](tensors/0002204.npy) |
| 2205 | `model.layers.23.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -69.0 / 50.25 / -0.009530238807201385 / 6.397335768745159 | [NPY](tensors/0002205.npy) |
| 2206 | `model.layers.23.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 60.75 / 0.018184414174821643 / 1.8026130642387936 | [NPY](tensors/0002206.npy) |
| 2207 | `model.layers.23.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.75 / 8.6875 / 0.36053478717803955 / 3.1253908915111697 | [NPY](tensors/0002207.npy) |
| 2208 | `model.layers.23.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.125 / 6.5625 / -0.03030421258881688 / 1.4973952666389567 | [NPY](tensors/0002208.npy) |
| 2209 | `model.layers.23.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4544.0 / 4576.0 / 2.6180135938856335 / 199.08732535174295 | [NPY](tensors/0002209.npy) |
| 2210 | `model.layers.23.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4544.0 / 4576.0 / 2.6180135938856335 / 199.08732535174295 | [NPY](tensors/0002210.npy) |
| 2211 | `model.layers.23.self_attn` | 18 | `output[1]` | [1, 64, 1, 891] | torch.bfloat16 → float32 | 4.128641872824801e-16 / 0.83984375 / 0.000811967695034796 / 0.008412859664075935 | [NPY](tensors/0002211.npy) |
| 2212 | `model.layers.23.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9408.0 / 9664.0 / 2.9728162977430554 / 489.4062405760701 | [NPY](tensors/0002212.npy) |
| 2213 | `model.layers.23.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 8.375 / -0.007465593020121257 / 1.0962988445523558 | [NPY](tensors/0002213.npy) |
| 2214 | `model.layers.23.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 8.375 / -0.007465593020121257 / 1.0962988445523558 | [NPY](tensors/0002214.npy) |
| 2215 | `model.layers.23.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.75 / 8.375 / -0.007465593020121257 / 1.0962988445523558 | [NPY](tensors/0002215.npy) |
| 2216 | `model.layers.23.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2217 | `model.layers.23.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2218 | `model.layers.23.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2219 | `model.layers.23.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2544.0 / 2464.0 / -4.410369427998861 / 154.13073037235725 | [NPY](tensors/0002219.npy) |
| 2220 | `model.layers.23.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2544.0 / 2464.0 / -4.410369427998861 / 154.13073037235725 | [NPY](tensors/0002220.npy) |
| 2221 | `model.layers.23.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.890625 / 1.9296875 / 0.078277587890625 / 1.1635557802334586 | [NPY](tensors/0002221.npy) |
| 2222 | `model.layers.23` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6944.0 / 7104.0 / -1.44951171875 / 406.64979282558596 | [NPY](tensors/0002222.npy) |
| 2301 | `model.layers.23` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8512.0 / 8128.0 / 0.4792263454861111 / 391.34119012412447 | [NPY](tensors/0002301.npy) |
| 2302 | `model.layers.23` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 892] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002302.npy) |
| 2303 | `model.layers.23` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6360321044921875 / 0.965021007945482 | [NPY](tensors/0002303.npy) |
| 2304 | `model.layers.23` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.07508242130279541 / 0.6832161663666542 | [NPY](tensors/0002304.npy) |
| 2305 | `model.layers.23` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 891.0 / 891.0 / 891.0 / 0.0 | [NPY](tensors/0002305.npy) |
| 2306 | `model.layers.23` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2307 | `model.layers.23` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2308 | `model.layers.23` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2309 | `model.layers.23.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8512.0 / 8128.0 / 0.4792263454861111 / 391.34119012412447 | [NPY](tensors/0002309.npy) |
| 2310 | `model.layers.23.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 55.75 / 0.008987634711795383 / 1.7570839032593426 | [NPY](tensors/0002310.npy) |
| 2311 | `model.layers.23.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 55.75 / 0.008987634711795383 / 1.7570839032593426 | [NPY](tensors/0002311.npy) |
| 2312 | `model.layers.23.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 892] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002312.npy) |
| 2313 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 891.0 / 891.0 / 891.0 / 0.0 | [NPY](tensors/0002313.npy) |
| 2314 | `model.layers.23.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2315 | `model.layers.23.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2316 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6360321044921875 / 0.965021007945482 | [NPY](tensors/0002316.npy) |
| 2317 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.07508242130279541 / 0.6832161663666542 | [NPY](tensors/0002317.npy) |
| 2318 | `model.layers.23.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2319 | `model.layers.23.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 55.75 / 0.008987634711795383 / 1.7570839032593426 | [NPY](tensors/0002319.npy) |
| 2320 | `model.layers.23.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.5625 / 15.75 / 0.011349601089023054 / 1.5479959576078195 | [NPY](tensors/0002320.npy) |
| 2321 | `model.layers.23.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 55.75 / 0.008987634711795383 / 1.7570839032593426 | [NPY](tensors/0002321.npy) |
| 2322 | `model.layers.23.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -72.5 / 42.0 / -0.05773725057952106 / 6.31923969816084 | [NPY](tensors/0002322.npy) |
| 2323 | `model.layers.23.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 55.75 / 0.008987634711795383 / 1.7570839032593426 | [NPY](tensors/0002323.npy) |
| 2324 | `model.layers.23.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.375 / 14.0625 / -0.37476253509521484 / 3.5880008875444758 | [NPY](tensors/0002324.npy) |
| 2325 | `model.layers.23.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.375 / 5.84375 / -0.008492639986798167 / 1.1975095285529043 | [NPY](tensors/0002325.npy) |
| 2326 | `model.layers.23.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4544.0 / 4608.0 / 5.030782919459873 / 199.26050169729297 | [NPY](tensors/0002326.npy) |
| 2327 | `model.layers.23.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4544.0 / 4608.0 / 5.030782919459873 / 199.26050169729297 | [NPY](tensors/0002327.npy) |
| 2328 | `model.layers.23.self_attn` | 19 | `output[1]` | [1, 64, 1, 892] | torch.bfloat16 → float32 | 2.400857290751901e-15 / 0.8515625 / 0.0008443988431323541 / 0.006806282900420736 | [NPY](tensors/0002328.npy) |
| 2329 | `model.layers.23.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8320.0 / 8064.0 / 5.50738525390625 / 450.6735163652156 | [NPY](tensors/0002329.npy) |
| 2330 | `model.layers.23.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.25 / 9.125 / -0.00527341365814209 / 1.0803167609962678 | [NPY](tensors/0002330.npy) |
| 2331 | `model.layers.23.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.25 / 9.125 / -0.00527341365814209 / 1.0803167609962678 | [NPY](tensors/0002331.npy) |
| 2332 | `model.layers.23.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.25 / 9.125 / -0.00527341365814209 / 1.0803167609962678 | [NPY](tensors/0002332.npy) |
| 2333 | `model.layers.23.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2334 | `model.layers.23.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2335 | `model.layers.23.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2336 | `model.layers.23.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2160.0 / 1936.0 / -1.4121821297539605 / 131.55754791149332 | [NPY](tensors/0002336.npy) |
| 2337 | `model.layers.23.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2160.0 / 1936.0 / -1.4121821297539605 / 131.55754791149332 | [NPY](tensors/0002337.npy) |
| 2338 | `model.layers.23.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.9375 / 1.34375 / 0.09649658203125 / 1.053593483177648 | [NPY](tensors/0002338.npy) |
| 2339 | `model.layers.23` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6464.0 / 5888.0 / 4.100336371527778 / 371.7130999512341 | [NPY](tensors/0002339.npy) |
| 2418 | `model.layers.23` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9216.0 / 2.4580864800347224 / 402.4282193488971 | [NPY](tensors/0002418.npy) |
| 2419 | `model.layers.23` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 893] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002419.npy) |
| 2420 | `model.layers.23` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.66259765625 / 0.9932594816118745 | [NPY](tensors/0002420.npy) |
| 2421 | `model.layers.23` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.09707069396972656 / 0.6118488978099847 | [NPY](tensors/0002421.npy) |
| 2422 | `model.layers.23` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 892.0 / 892.0 / 892.0 / 0.0 | [NPY](tensors/0002422.npy) |
| 2423 | `model.layers.23` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2424 | `model.layers.23` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2425 | `model.layers.23` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2426 | `model.layers.23.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9216.0 / 2.4580864800347224 / 402.4282193488971 | [NPY](tensors/0002426.npy) |
| 2427 | `model.layers.23.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 61.5 / 0.019377028942108153 / 1.8054889972720223 | [NPY](tensors/0002427.npy) |
| 2428 | `model.layers.23.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 61.5 / 0.019377028942108153 / 1.8054889972720223 | [NPY](tensors/0002428.npy) |
| 2429 | `model.layers.23.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 893] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002429.npy) |
| 2430 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 892.0 / 892.0 / 892.0 / 0.0 | [NPY](tensors/0002430.npy) |
| 2431 | `model.layers.23.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2432 | `model.layers.23.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2433 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.66259765625 / 0.9932594816118745 | [NPY](tensors/0002433.npy) |
| 2434 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.09707069396972656 / 0.6118488978099847 | [NPY](tensors/0002434.npy) |
| 2435 | `model.layers.23.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2436 | `model.layers.23.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 61.5 / 0.019377028942108153 / 1.8054889972720223 | [NPY](tensors/0002436.npy) |
| 2437 | `model.layers.23.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.5625 / 10.5625 / 0.026164115872234106 / 1.3588617886520518 | [NPY](tensors/0002437.npy) |
| 2438 | `model.layers.23.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 61.5 / 0.019377028942108153 / 1.8054889972720223 | [NPY](tensors/0002438.npy) |
| 2439 | `model.layers.23.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -59.25 / 44.25 / -0.04943712800741196 / 5.419063909884104 | [NPY](tensors/0002439.npy) |
| 2440 | `model.layers.23.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 61.5 / 0.019377028942108153 / 1.8054889972720223 | [NPY](tensors/0002440.npy) |
| 2441 | `model.layers.23.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.5 / 7.28125 / -0.0677376389503479 / 2.213523673549124 | [NPY](tensors/0002441.npy) |
| 2442 | `model.layers.23.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.4375 / 9.5 / -0.03199302090797573 / 1.4220562534028158 | [NPY](tensors/0002442.npy) |
| 2443 | `model.layers.23.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5472.0 / 5.456220160590278 / 236.5585908438901 | [NPY](tensors/0002443.npy) |
| 2444 | `model.layers.23.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5472.0 / 5.456220160590278 / 236.5585908438901 | [NPY](tensors/0002444.npy) |
| 2445 | `model.layers.23.self_attn` | 20 | `output[1]` | [1, 64, 1, 893] | torch.bfloat16 → float32 | 8.242295734817162e-13 / 0.8203125 / 0.0009235194020121563 / 0.008726173844327993 | [NPY](tensors/0002445.npy) |
| 2446 | `model.layers.23.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9216.0 / 8832.0 / 7.905794270833334 / 474.8270969861523 | [NPY](tensors/0002446.npy) |
| 2447 | `model.layers.23.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 8.3125 / 0.00842742191420661 / 0.9680643512877184 | [NPY](tensors/0002447.npy) |
| 2448 | `model.layers.23.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 8.3125 / 0.00842742191420661 / 0.9680643512877184 | [NPY](tensors/0002448.npy) |
| 2449 | `model.layers.23.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -29.0 / 8.3125 / 0.00842742191420661 / 0.9680643512877184 | [NPY](tensors/0002449.npy) |
| 2450 | `model.layers.23.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2451 | `model.layers.23.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2452 | `model.layers.23.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2453 | `model.layers.23.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1600.0 / 1552.0 / -1.0485011842515735 / 103.64186023387387 | [NPY](tensors/0002453.npy) |
| 2454 | `model.layers.23.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1600.0 / 1552.0 / -1.0485011842515735 / 103.64186023387387 | [NPY](tensors/0002454.npy) |
| 2455 | `model.layers.23.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.4296875 / 0.8671875 / -0.020076751708984375 / 0.5260744846743902 | [NPY](tensors/0002455.npy) |
| 2456 | `model.layers.23` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7808.0 / 7360.0 / 6.863069661458334 / 406.2172560903921 | [NPY](tensors/0002456.npy) |
| 2535 | `model.layers.23` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 10624.0 / -6.020271809895833 / 484.9207772011643 | [NPY](tensors/0002535.npy) |
| 2536 | `model.layers.23` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 894] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002536.npy) |
| 2537 | `model.layers.23` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6520881652832031 / 1.010377882001008 | [NPY](tensors/0002537.npy) |
| 2538 | `model.layers.23` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.328125 / 0.13654857873916626 / 0.5864893104951562 | [NPY](tensors/0002538.npy) |
| 2539 | `model.layers.23` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 893.0 / 893.0 / 893.0 / 0.0 | [NPY](tensors/0002539.npy) |
| 2540 | `model.layers.23` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2541 | `model.layers.23` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2542 | `model.layers.23` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2543 | `model.layers.23.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 10624.0 / -6.020271809895833 / 484.9207772011643 | [NPY](tensors/0002543.npy) |
| 2544 | `model.layers.23.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 59.0 / -0.005668106344011095 / 1.7513255495668032 | [NPY](tensors/0002544.npy) |
| 2545 | `model.layers.23.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 59.0 / -0.005668106344011095 / 1.7513255495668032 | [NPY](tensors/0002545.npy) |
| 2546 | `model.layers.23.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 894] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002546.npy) |
| 2547 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 893.0 / 893.0 / 893.0 / 0.0 | [NPY](tensors/0002547.npy) |
| 2548 | `model.layers.23.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2549 | `model.layers.23.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2550 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6520881652832031 / 1.010377882001008 | [NPY](tensors/0002550.npy) |
| 2551 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.328125 / 0.13654857873916626 / 0.5864893104951562 | [NPY](tensors/0002551.npy) |
| 2552 | `model.layers.23.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2553 | `model.layers.23.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 59.0 / -0.005668106344011095 / 1.7513255495668032 | [NPY](tensors/0002553.npy) |
| 2554 | `model.layers.23.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.625 / 14.25 / 0.019305758643895388 / 1.3576386183360267 | [NPY](tensors/0002554.npy) |
| 2555 | `model.layers.23.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 59.0 / -0.005668106344011095 / 1.7513255495668032 | [NPY](tensors/0002555.npy) |
| 2556 | `model.layers.23.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -60.5 / 38.5 / -0.117056705057621 / 5.414818121867046 | [NPY](tensors/0002556.npy) |
| 2557 | `model.layers.23.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 59.0 / -0.005668106344011095 / 1.7513255495668032 | [NPY](tensors/0002557.npy) |
| 2558 | `model.layers.23.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.875 / 5.875 / -0.1525413990020752 / 2.2051127183419887 | [NPY](tensors/0002558.npy) |
| 2559 | `model.layers.23.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.625 / 7.1875 / -0.014309475664049387 / 1.3523773485820492 | [NPY](tensors/0002559.npy) |
| 2560 | `model.layers.23.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5920.0 / 6240.0 / 7.186094644334581 / 268.16781529128804 | [NPY](tensors/0002560.npy) |
| 2561 | `model.layers.23.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5920.0 / 6240.0 / 7.186094644334581 / 268.16781529128804 | [NPY](tensors/0002561.npy) |
| 2562 | `model.layers.23.self_attn` | 21 | `output[1]` | [1, 64, 1, 894] | torch.bfloat16 → float32 | 4.121147867408581e-13 / 0.765625 / 0.0007855641064180931 / 0.008160225817362707 | [NPY](tensors/0002562.npy) |
| 2563 | `model.layers.23.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 10880.0 / 1.183056640625 / 588.4123349502787 | [NPY](tensors/0002563.npy) |
| 2564 | `model.layers.23.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 8.0 / -0.024985972377989028 / 0.965449219842364 | [NPY](tensors/0002564.npy) |
| 2565 | `model.layers.23.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 8.0 / -0.024985972377989028 / 0.965449219842364 | [NPY](tensors/0002565.npy) |
| 2566 | `model.layers.23.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.5 / 8.0 / -0.024985972377989028 / 0.965449219842364 | [NPY](tensors/0002566.npy) |
| 2567 | `model.layers.23.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2568 | `model.layers.23.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2569 | `model.layers.23.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2570 | `model.layers.23.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1208.0 / 1192.0 / -1.7985723707411023 / 83.14709767492255 | [NPY](tensors/0002570.npy) |
| 2571 | `model.layers.23.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1208.0 / 1192.0 / -1.7985723707411023 / 83.14709767492255 | [NPY](tensors/0002571.npy) |
| 2572 | `model.layers.23.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.4609375 / 1.1484375 / 0.118896484375 / 0.5562578457911231 | [NPY](tensors/0002572.npy) |
| 2573 | `model.layers.23` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9472.0 / 9984.0 / -0.5958143446180556 / 543.0746256473365 | [NPY](tensors/0002573.npy) |
| 2652 | `model.layers.23` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8704.0 / 9024.0 / -4.537101236979167 / 423.42403931764846 | [NPY](tensors/0002652.npy) |
| 2653 | `model.layers.23` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 895] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002653.npy) |
| 2654 | `model.layers.23` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6077041625976562 / 1.0143983018780602 | [NPY](tensors/0002654.npy) |
| 2655 | `model.layers.23` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.15405970811843872 / 0.6224309502943564 | [NPY](tensors/0002655.npy) |
| 2656 | `model.layers.23` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 894.0 / 894.0 / 894.0 / 0.0 | [NPY](tensors/0002656.npy) |
| 2657 | `model.layers.23` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2658 | `model.layers.23` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2659 | `model.layers.23` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2660 | `model.layers.23.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8704.0 / 9024.0 / -4.537101236979167 / 423.42403931764846 | [NPY](tensors/0002660.npy) |
| 2661 | `model.layers.23.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 57.25 / -0.004973476462894016 / 1.7343584998249861 | [NPY](tensors/0002661.npy) |
| 2662 | `model.layers.23.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 57.25 / -0.004973476462894016 / 1.7343584998249861 | [NPY](tensors/0002662.npy) |
| 2663 | `model.layers.23.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 895] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002663.npy) |
| 2664 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 894.0 / 894.0 / 894.0 / 0.0 | [NPY](tensors/0002664.npy) |
| 2665 | `model.layers.23.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2666 | `model.layers.23.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2667 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6077041625976562 / 1.0143983018780602 | [NPY](tensors/0002667.npy) |
| 2668 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.15405970811843872 / 0.6224309502943564 | [NPY](tensors/0002668.npy) |
| 2669 | `model.layers.23.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2670 | `model.layers.23.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 57.25 / -0.004973476462894016 / 1.7343584998249861 | [NPY](tensors/0002670.npy) |
| 2671 | `model.layers.23.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.5 / 15.9375 / 0.022440363187342882 / 1.4637451404624378 | [NPY](tensors/0002671.npy) |
| 2672 | `model.layers.23.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 57.25 / -0.004973476462894016 / 1.7343584998249861 | [NPY](tensors/0002672.npy) |
| 2673 | `model.layers.23.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -59.5 / 40.5 / -0.2129548192024231 / 5.95688715366958 | [NPY](tensors/0002673.npy) |
| 2674 | `model.layers.23.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 57.25 / -0.004973476462894016 / 1.7343584998249861 | [NPY](tensors/0002674.npy) |
| 2675 | `model.layers.23.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.75 / 12.0625 / -0.008285075426101685 / 3.4381134794025416 | [NPY](tensors/0002675.npy) |
| 2676 | `model.layers.23.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.25 / 7.96875 / 0.006117558339610696 / 1.4683901137758912 | [NPY](tensors/0002676.npy) |
| 2677 | `model.layers.23.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5216.0 / 5504.0 / 7.190899933709039 / 232.7009225874672 | [NPY](tensors/0002677.npy) |
| 2678 | `model.layers.23.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5216.0 / 5504.0 / 7.190899933709039 / 232.7009225874672 | [NPY](tensors/0002678.npy) |
| 2679 | `model.layers.23.self_attn` | 22 | `output[1]` | [1, 64, 1, 895] | torch.bfloat16 → float32 | 5.897504706808832e-13 / 0.76171875 / 0.0007775899127870375 / 0.008274144127246225 | [NPY](tensors/0002679.npy) |
| 2680 | `model.layers.23.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 9728.0 / 2.667366536458333 / 515.2960392734931 | [NPY](tensors/0002680.npy) |
| 2681 | `model.layers.23.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 7.59375 / -0.021407673094007703 / 1.0634712782531002 | [NPY](tensors/0002681.npy) |
| 2682 | `model.layers.23.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 7.59375 / -0.021407673094007703 / 1.0634712782531002 | [NPY](tensors/0002682.npy) |
| 2683 | `model.layers.23.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -39.5 / 7.59375 / -0.021407673094007703 / 1.0634712782531002 | [NPY](tensors/0002683.npy) |
| 2684 | `model.layers.23.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2685 | `model.layers.23.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2686 | `model.layers.23.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2687 | `model.layers.23.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2160.0 / 1984.0 / -2.1057884428236218 / 96.86710221953633 | [NPY](tensors/0002687.npy) |
| 2688 | `model.layers.23.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2160.0 / 1984.0 / -2.1057884428236218 / 96.86710221953633 | [NPY](tensors/0002688.npy) |
| 2689 | `model.layers.23.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.875 / 0.9296875 / 0.170867919921875 / 0.7603518809384753 | [NPY](tensors/0002689.npy) |
| 2690 | `model.layers.23` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8896.0 / 9408.0 / 0.5603542751736111 / 533.2314252306944 | [NPY](tensors/0002690.npy) |
| 2769 | `model.layers.23` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9088.0 / 1.6104410807291667 / 433.13887784716275 | [NPY](tensors/0002769.npy) |
| 2770 | `model.layers.23` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 896] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002770.npy) |
| 2771 | `model.layers.23` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5635757446289062 / 1.0167091376095412 | [NPY](tensors/0002771.npy) |
| 2772 | `model.layers.23` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.13094085454940796 / 0.6637995182317289 | [NPY](tensors/0002772.npy) |
| 2773 | `model.layers.23` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 895.0 / 895.0 / 895.0 / 0.0 | [NPY](tensors/0002773.npy) |
| 2774 | `model.layers.23` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2775 | `model.layers.23` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2776 | `model.layers.23` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2777 | `model.layers.23.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9088.0 / 1.6104410807291667 / 433.13887784716275 | [NPY](tensors/0002777.npy) |
| 2778 | `model.layers.23.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 56.5 / 0.012978867027494642 / 1.7394132513858938 | [NPY](tensors/0002778.npy) |
| 2779 | `model.layers.23.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 56.5 / 0.012978867027494642 / 1.7394132513858938 | [NPY](tensors/0002779.npy) |
| 2780 | `model.layers.23.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 896] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002780.npy) |
| 2781 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 895.0 / 895.0 / 895.0 / 0.0 | [NPY](tensors/0002781.npy) |
| 2782 | `model.layers.23.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2783 | `model.layers.23.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2784 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.5635757446289062 / 1.0167091376095412 | [NPY](tensors/0002784.npy) |
| 2785 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.13094085454940796 / 0.6637995182317289 | [NPY](tensors/0002785.npy) |
| 2786 | `model.layers.23.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2787 | `model.layers.23.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 56.5 / 0.012978867027494642 / 1.7394132513858938 | [NPY](tensors/0002787.npy) |
| 2788 | `model.layers.23.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.375 / 16.625 / 0.012934854323248146 / 1.428650498628752 | [NPY](tensors/0002788.npy) |
| 2789 | `model.layers.23.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 56.5 / 0.012978867027494642 / 1.7394132513858938 | [NPY](tensors/0002789.npy) |
| 2790 | `model.layers.23.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -71.5 / 44.25 / -0.13918083161115646 / 6.469135050798463 | [NPY](tensors/0002790.npy) |
| 2791 | `model.layers.23.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 56.5 / 0.012978867027494642 / 1.7394132513858938 | [NPY](tensors/0002791.npy) |
| 2792 | `model.layers.23.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.0 / 11.0625 / 0.1407318264245987 / 2.9587224692395226 | [NPY](tensors/0002792.npy) |
| 2793 | `model.layers.23.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.125 / 6.03125 / -0.021046277892310172 / 1.1522205019395186 | [NPY](tensors/0002793.npy) |
| 2794 | `model.layers.23.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4480.0 / 4640.0 / 5.142247687445747 / 194.85401408711596 | [NPY](tensors/0002794.npy) |
| 2795 | `model.layers.23.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4480.0 / 4640.0 / 5.142247687445747 / 194.85401408711596 | [NPY](tensors/0002795.npy) |
| 2796 | `model.layers.23.self_attn` | 23 | `output[1]` | [1, 64, 1, 896] | torch.bfloat16 → float32 | 1.226796442210798e-14 / 0.859375 / 0.0006193547263351416 / 0.006762643047362304 | [NPY](tensors/0002796.npy) |
| 2797 | `model.layers.23.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8768.0 / 8576.0 / 6.773342556423611 / 471.41798773677226 | [NPY](tensors/0002797.npy) |
| 2798 | `model.layers.23.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 7.03125 / -0.003065864576233758 / 1.1252583117586459 | [NPY](tensors/0002798.npy) |
| 2799 | `model.layers.23.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 7.03125 / -0.003065864576233758 / 1.1252583117586459 | [NPY](tensors/0002799.npy) |
| 2800 | `model.layers.23.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -42.25 / 7.03125 / -0.003065864576233758 / 1.1252583117586459 | [NPY](tensors/0002800.npy) |
| 2801 | `model.layers.23.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2802 | `model.layers.23.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2803 | `model.layers.23.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2804 | `model.layers.23.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1776.0 / 1592.0 / 0.6193267822265625 / 84.28891284065037 | [NPY](tensors/0002804.npy) |
| 2805 | `model.layers.23.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1776.0 / 1592.0 / 0.6193267822265625 / 84.28891284065037 | [NPY](tensors/0002805.npy) |
| 2806 | `model.layers.23.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.78125 / 1.28125 / 0.253692626953125 / 1.1028135442032956 | [NPY](tensors/0002806.npy) |
| 2807 | `model.layers.23` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8512.0 / 8192.0 / 7.378841145833333 / 473.93585713951364 | [NPY](tensors/0002807.npy) |
| 2886 | `model.layers.23` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9216.0 / 0.8369547526041666 / 453.81679712733705 | [NPY](tensors/0002886.npy) |
| 2887 | `model.layers.23` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 897] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002887.npy) |
| 2888 | `model.layers.23` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5521621704101562 / 0.9747722822304562 | [NPY](tensors/0002888.npy) |
| 2889 | `model.layers.23` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.08557838201522827 / 0.7397982213081387 | [NPY](tensors/0002889.npy) |
| 2890 | `model.layers.23` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 896.0 / 896.0 / 896.0 / 0.0 | [NPY](tensors/0002890.npy) |
| 2891 | `model.layers.23` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2892 | `model.layers.23` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2893 | `model.layers.23` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2894 | `model.layers.23.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9216.0 / 0.8369547526041666 / 453.81679712733705 | [NPY](tensors/0002894.npy) |
| 2895 | `model.layers.23.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 53.5 / 0.017931636174519858 / 1.7001372899630394 | [NPY](tensors/0002895.npy) |
| 2896 | `model.layers.23.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 53.5 / 0.017931636174519858 / 1.7001372899630394 | [NPY](tensors/0002896.npy) |
| 2897 | `model.layers.23.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 897] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002897.npy) |
| 2898 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 896.0 / 896.0 / 896.0 / 0.0 | [NPY](tensors/0002898.npy) |
| 2899 | `model.layers.23.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2900 | `model.layers.23.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2901 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5521621704101562 / 0.9747722822304562 | [NPY](tensors/0002901.npy) |
| 2902 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.08557838201522827 / 0.7397982213081387 | [NPY](tensors/0002902.npy) |
| 2903 | `model.layers.23.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2904 | `model.layers.23.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 53.5 / 0.017931636174519858 / 1.7001372899630394 | [NPY](tensors/0002904.npy) |
| 2905 | `model.layers.23.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.875 / 14.5625 / 0.02154853963293135 / 1.445105017098425 | [NPY](tensors/0002905.npy) |
| 2906 | `model.layers.23.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 53.5 / 0.017931636174519858 / 1.7001372899630394 | [NPY](tensors/0002906.npy) |
| 2907 | `model.layers.23.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -71.0 / 45.0 / -0.1250169426202774 / 5.994155638535298 | [NPY](tensors/0002907.npy) |
| 2908 | `model.layers.23.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 53.5 / 0.017931636174519858 / 1.7001372899630394 | [NPY](tensors/0002908.npy) |
| 2909 | `model.layers.23.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.25 / 7.9375 / -0.040638864040374756 / 2.5620286675591744 | [NPY](tensors/0002909.npy) |
| 2910 | `model.layers.23.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.625 / 9.25 / 0.039246026397449896 / 1.8650031711928732 | [NPY](tensors/0002910.npy) |
| 2911 | `model.layers.23.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4480.0 / 4608.0 / 4.771645016140408 / 203.4124536304017 | [NPY](tensors/0002911.npy) |
| 2912 | `model.layers.23.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4480.0 / 4608.0 / 4.771645016140408 / 203.4124536304017 | [NPY](tensors/0002912.npy) |
| 2913 | `model.layers.23.self_attn` | 24 | `output[1]` | [1, 64, 1, 897] | torch.bfloat16 → float32 | 6.411537967210279e-15 / 0.8671875 / 0.0007297935940528818 / 0.009305885730292908 | [NPY](tensors/0002913.npy) |
| 2914 | `model.layers.23.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9216.0 / 5.628173828125 / 518.8196008482778 | [NPY](tensors/0002914.npy) |
| 2915 | `model.layers.23.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 10.6875 / 0.0033113267686631946 / 1.1488384878520785 | [NPY](tensors/0002915.npy) |
| 2916 | `model.layers.23.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 10.6875 / 0.0033113267686631946 / 1.1488384878520785 | [NPY](tensors/0002916.npy) |
| 2917 | `model.layers.23.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.25 / 10.6875 / 0.0033113267686631946 / 1.1488384878520785 | [NPY](tensors/0002917.npy) |
| 2918 | `model.layers.23.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2919 | `model.layers.23.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2920 | `model.layers.23.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2921 | `model.layers.23.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3696.0 / 3504.0 / 0.3866936577690972 / 211.11354524642806 | [NPY](tensors/0002921.npy) |
| 2922 | `model.layers.23.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3696.0 / 3504.0 / 0.3866936577690972 / 211.11354524642806 | [NPY](tensors/0002922.npy) |
| 2923 | `model.layers.23.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.625 / 1.8671875 / 0.0934906005859375 / 1.4576859319290605 | [NPY](tensors/0002923.npy) |
| 2924 | `model.layers.23` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6144.0 / 5728.0 / 6.030924479166667 / 415.46915000467476 | [NPY](tensors/0002924.npy) |
| 3003 | `model.layers.23` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7744.0 / 7456.0 / 1.2451348198784722 / 387.7123841886352 | [NPY](tensors/0003003.npy) |
| 3004 | `model.layers.23` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 898] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003004.npy) |
| 3005 | `model.layers.23` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.576171875 / 0.9367379826853268 | [NPY](tensors/0003005.npy) |
| 3006 | `model.layers.23` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05449014902114868 / 0.7727124058266066 | [NPY](tensors/0003006.npy) |
| 3007 | `model.layers.23` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 897.0 / 897.0 / 897.0 / 0.0 | [NPY](tensors/0003007.npy) |
| 3008 | `model.layers.23` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3009 | `model.layers.23` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3010 | `model.layers.23` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3011 | `model.layers.23.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7744.0 / 7456.0 / 1.2451348198784722 / 387.7123841886352 | [NPY](tensors/0003011.npy) |
| 3012 | `model.layers.23.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 51.75 / 0.018063818083869088 / 1.7394738375964194 | [NPY](tensors/0003012.npy) |
| 3013 | `model.layers.23.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 51.75 / 0.018063818083869088 / 1.7394738375964194 | [NPY](tensors/0003013.npy) |
| 3014 | `model.layers.23.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 898] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003014.npy) |
| 3015 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 897.0 / 897.0 / 897.0 / 0.0 | [NPY](tensors/0003015.npy) |
| 3016 | `model.layers.23.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3017 | `model.layers.23.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3018 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.576171875 / 0.9367379826853268 | [NPY](tensors/0003018.npy) |
| 3019 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05449014902114868 / 0.7727124058266066 | [NPY](tensors/0003019.npy) |
| 3020 | `model.layers.23.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3021 | `model.layers.23.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 51.75 / 0.018063818083869088 / 1.7394738375964194 | [NPY](tensors/0003021.npy) |
| 3022 | `model.layers.23.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.9375 / 18.375 / 0.03257523488719016 / 1.6728373212051957 | [NPY](tensors/0003022.npy) |
| 3023 | `model.layers.23.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 51.75 / 0.018063818083869088 / 1.7394738375964194 | [NPY](tensors/0003023.npy) |
| 3024 | `model.layers.23.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -85.5 / 54.5 / -0.09332600235939026 / 7.145170306066662 | [NPY](tensors/0003024.npy) |
| 3025 | `model.layers.23.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 51.75 / 0.018063818083869088 / 1.7394738375964194 | [NPY](tensors/0003025.npy) |
| 3026 | `model.layers.23.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.625 / 15.6875 / 0.10112690925598145 / 4.244569861626346 | [NPY](tensors/0003026.npy) |
| 3027 | `model.layers.23.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.125 / 9.25 / 0.038022235268726945 / 1.529698305859711 | [NPY](tensors/0003027.npy) |
| 3028 | `model.layers.23.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3728.0 / 3824.0 / 4.45182236565484 / 171.83346333611377 | [NPY](tensors/0003028.npy) |
| 3029 | `model.layers.23.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3728.0 / 3824.0 / 4.45182236565484 / 171.83346333611377 | [NPY](tensors/0003029.npy) |
| 3030 | `model.layers.23.self_attn` | 25 | `output[1]` | [1, 64, 1, 898] | torch.bfloat16 → float32 | 1.2628786905111156e-15 / 0.79296875 / 0.0005343453447326161 / 0.009131701981403053 | [NPY](tensors/0003030.npy) |
| 3031 | `model.layers.23.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8320.0 / 8320.0 / 5.679254828559028 / 452.0429831042097 | [NPY](tensors/0003031.npy) |
| 3032 | `model.layers.23.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.75 / 13.625 / 0.006035258372624715 / 1.1905184592761804 | [NPY](tensors/0003032.npy) |
| 3033 | `model.layers.23.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.75 / 13.625 / 0.006035258372624715 / 1.1905184592761804 | [NPY](tensors/0003033.npy) |
| 3034 | `model.layers.23.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -28.75 / 13.625 / 0.006035258372624715 / 1.1905184592761804 | [NPY](tensors/0003034.npy) |
| 3035 | `model.layers.23.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3036 | `model.layers.23.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3037 | `model.layers.23.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3038 | `model.layers.23.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5280.0 / 5312.0 / 0.3286673651801215 / 329.46035444946335 | [NPY](tensors/0003038.npy) |
| 3039 | `model.layers.23.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5280.0 / 5312.0 / 0.3286673651801215 / 329.46035444946335 | [NPY](tensors/0003039.npy) |
| 3040 | `model.layers.23.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.125 / 2.46875 / 0.0419921875 / 1.8310741535423611 | [NPY](tensors/0003040.npy) |
| 3041 | `model.layers.23` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3008.0 / 3040.0 / 5.9996527777777775 / 385.5048711216456 | [NPY](tensors/0003041.npy) |
| 3120 | `model.layers.23` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7264.0 / 7744.0 / 7.014889865451389 / 360.23295888886 | [NPY](tensors/0003120.npy) |
| 3121 | `model.layers.23` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 899] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003121.npy) |
| 3122 | `model.layers.23` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.60968017578125 / 0.9551838287803889 | [NPY](tensors/0003122.npy) |
| 3123 | `model.layers.23` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05779397487640381 / 0.7235452926755772 | [NPY](tensors/0003123.npy) |
| 3124 | `model.layers.23` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 898.0 / 898.0 / 898.0 / 0.0 | [NPY](tensors/0003124.npy) |
| 3125 | `model.layers.23` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3126 | `model.layers.23` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3127 | `model.layers.23` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3128 | `model.layers.23.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7264.0 / 7744.0 / 7.014889865451389 / 360.23295888886 | [NPY](tensors/0003128.npy) |
| 3129 | `model.layers.23.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 57.75 / 0.04050172633594937 / 1.7696485964774995 | [NPY](tensors/0003129.npy) |
| 3130 | `model.layers.23.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 57.75 / 0.04050172633594937 / 1.7696485964774995 | [NPY](tensors/0003130.npy) |
| 3131 | `model.layers.23.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 899] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003131.npy) |
| 3132 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 898.0 / 898.0 / 898.0 / 0.0 | [NPY](tensors/0003132.npy) |
| 3133 | `model.layers.23.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3134 | `model.layers.23.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3135 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.60968017578125 / 0.9551838287803889 | [NPY](tensors/0003135.npy) |
| 3136 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05779397487640381 / 0.7235452926755772 | [NPY](tensors/0003136.npy) |
| 3137 | `model.layers.23.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3138 | `model.layers.23.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 57.75 / 0.04050172633594937 / 1.7696485964774995 | [NPY](tensors/0003138.npy) |
| 3139 | `model.layers.23.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.25 / 16.5 / 0.03146274876780808 / 1.63861206903495 | [NPY](tensors/0003139.npy) |
| 3140 | `model.layers.23.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 57.75 / 0.04050172633594937 / 1.7696485964774995 | [NPY](tensors/0003140.npy) |
| 3141 | `model.layers.23.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -93.5 / 60.75 / -0.21172668039798737 / 7.914229244067174 | [NPY](tensors/0003141.npy) |
| 3142 | `model.layers.23.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 57.75 / 0.04050172633594937 / 1.7696485964774995 | [NPY](tensors/0003142.npy) |
| 3143 | `model.layers.23.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.5 / 15.0625 / 0.2448101043701172 / 3.5854455186977376 | [NPY](tensors/0003143.npy) |
| 3144 | `model.layers.23.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.875 / 6.625 / -0.015850730240345 / 1.283412280451943 | [NPY](tensors/0003144.npy) |
| 3145 | `model.layers.23.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4608.0 / 4768.0 / 4.70847225189209 / 204.49037915264495 | [NPY](tensors/0003145.npy) |
| 3146 | `model.layers.23.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4608.0 / 4768.0 / 4.70847225189209 / 204.49037915264495 | [NPY](tensors/0003146.npy) |
| 3147 | `model.layers.23.self_attn` | 26 | `output[1]` | [1, 64, 1, 899] | torch.bfloat16 → float32 | 8.118505867571457e-16 / 0.828125 / 0.0005531224346332325 / 0.00788935430007009 | [NPY](tensors/0003147.npy) |
| 3148 | `model.layers.23.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7296.0 / 7968.0 / 11.713346354166667 / 425.06985498585834 | [NPY](tensors/0003148.npy) |
| 3149 | `model.layers.23.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 9.1875 / 0.024184838930765788 / 1.1749600784840986 | [NPY](tensors/0003149.npy) |
| 3150 | `model.layers.23.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 9.1875 / 0.024184838930765788 / 1.1749600784840986 | [NPY](tensors/0003150.npy) |
| 3151 | `model.layers.23.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.5 / 9.1875 / 0.024184838930765788 / 1.1749600784840986 | [NPY](tensors/0003151.npy) |
| 3152 | `model.layers.23.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3153 | `model.layers.23.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3154 | `model.layers.23.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3155 | `model.layers.23.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1544.0 / 1536.0 / -0.5819256729549832 / 90.23111534459024 | [NPY](tensors/0003155.npy) |
| 3156 | `model.layers.23.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1544.0 / 1536.0 / -0.5819256729549832 / 90.23111534459024 | [NPY](tensors/0003156.npy) |
| 3157 | `model.layers.23.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.71875 / 2.28125 / 0.4322509765625 / 2.1577926556104945 | [NPY](tensors/0003157.npy) |
| 3158 | `model.layers.23` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5760.0 / 6432.0 / 11.13251953125 / 385.5556146728158 | [NPY](tensors/0003158.npy) |
| 3237 | `model.layers.23` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9024.0 / 8448.0 / 1.8008368598090279 / 431.5652087454492 | [NPY](tensors/0003237.npy) |
| 3238 | `model.layers.23` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 900] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003238.npy) |
| 3239 | `model.layers.23` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.6215248107910156 / 0.953261420864228 | [NPY](tensors/0003239.npy) |
| 3240 | `model.layers.23` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.08504927158355713 / 0.7123271249161985 | [NPY](tensors/0003240.npy) |
| 3241 | `model.layers.23` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 899.0 / 899.0 / 899.0 / 0.0 | [NPY](tensors/0003241.npy) |
| 3242 | `model.layers.23` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3243 | `model.layers.23` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3244 | `model.layers.23` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3245 | `model.layers.23.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9024.0 / 8448.0 / 1.8008368598090279 / 431.5652087454492 | [NPY](tensors/0003245.npy) |
| 3246 | `model.layers.23.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 52.5 / 0.012811517715454102 / 1.7123187516134715 | [NPY](tensors/0003246.npy) |
| 3247 | `model.layers.23.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 52.5 / 0.012811517715454102 / 1.7123187516134715 | [NPY](tensors/0003247.npy) |
| 3248 | `model.layers.23.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 900] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003248.npy) |
| 3249 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 899.0 / 899.0 / 899.0 / 0.0 | [NPY](tensors/0003249.npy) |
| 3250 | `model.layers.23.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3251 | `model.layers.23.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3252 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.6215248107910156 / 0.953261420864228 | [NPY](tensors/0003252.npy) |
| 3253 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.08504927158355713 / 0.7123271249161985 | [NPY](tensors/0003253.npy) |
| 3254 | `model.layers.23.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3255 | `model.layers.23.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 52.5 / 0.012811517715454102 / 1.7123187516134715 | [NPY](tensors/0003255.npy) |
| 3256 | `model.layers.23.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.0625 / 17.0 / 0.01593030896037817 / 1.4913858158650428 | [NPY](tensors/0003256.npy) |
| 3257 | `model.layers.23.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 52.5 / 0.012811517715454102 / 1.7123187516134715 | [NPY](tensors/0003257.npy) |
| 3258 | `model.layers.23.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -77.5 / 54.0 / -0.16605126857757568 / 6.77130590821267 | [NPY](tensors/0003258.npy) |
| 3259 | `model.layers.23.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 52.5 / 0.012811517715454102 / 1.7123187516134715 | [NPY](tensors/0003259.npy) |
| 3260 | `model.layers.23.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.625 / 6.625 / 0.026498079299926758 / 2.503421986824844 | [NPY](tensors/0003260.npy) |
| 3261 | `model.layers.23.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.625 / 5.46875 / -0.033704635221511126 / 1.0992685183827928 | [NPY](tensors/0003261.npy) |
| 3262 | `model.layers.23.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4960.0 / 5056.0 / 5.356567827860514 / 216.94680000731347 | [NPY](tensors/0003262.npy) |
| 3263 | `model.layers.23.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4960.0 / 5056.0 / 5.356567827860514 / 216.94680000731347 | [NPY](tensors/0003263.npy) |
| 3264 | `model.layers.23.self_attn` | 27 | `output[1]` | [1, 64, 1, 900] | torch.bfloat16 → float32 | 1.1157741397482823e-14 / 0.77734375 / 0.0005536125751848752 / 0.0064426609946194304 | [NPY](tensors/0003264.npy) |
| 3265 | `model.layers.23.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9408.0 / 9024.0 / 7.168402777777778 / 508.17546410813776 | [NPY](tensors/0003265.npy) |
| 3266 | `model.layers.23.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 8.4375 / -0.003402384122212728 / 1.1621668252628723 | [NPY](tensors/0003266.npy) |
| 3267 | `model.layers.23.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 8.4375 / -0.003402384122212728 / 1.1621668252628723 | [NPY](tensors/0003267.npy) |
| 3268 | `model.layers.23.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -42.25 / 8.4375 / -0.003402384122212728 / 1.1621668252628723 | [NPY](tensors/0003268.npy) |
| 3269 | `model.layers.23.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3270 | `model.layers.23.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3271 | `model.layers.23.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3272 | `model.layers.23.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1296.0 / 1248.0 / -1.6113464991251627 / 77.93746222563601 | [NPY](tensors/0003272.npy) |
| 3273 | `model.layers.23.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1296.0 / 1248.0 / -1.6113464991251627 / 77.93746222563601 | [NPY](tensors/0003273.npy) |
| 3274 | `model.layers.23.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8359375 / 1.0 / 0.259124755859375 / 0.7513182344000827 | [NPY](tensors/0003274.npy) |
| 3275 | `model.layers.23` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8160.0 / 7744.0 / 5.574252658420139 / 476.6673850114717 | [NPY](tensors/0003275.npy) |
| 3354 | `model.layers.23` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6400.0 / 5664.0 / 1.251901584201389 / 327.16721159666866 | [NPY](tensors/0003354.npy) |
| 3355 | `model.layers.23` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 901] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003355.npy) |
| 3356 | `model.layers.23` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.6053333282470703 / 0.9378499631722268 | [NPY](tensors/0003356.npy) |
| 3357 | `model.layers.23` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.10818588733673096 / 0.7432403804988892 | [NPY](tensors/0003357.npy) |
| 3358 | `model.layers.23` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 900.0 / 900.0 / 900.0 / 0.0 | [NPY](tensors/0003358.npy) |
| 3359 | `model.layers.23` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3360 | `model.layers.23` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3361 | `model.layers.23` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3362 | `model.layers.23.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6400.0 / 5664.0 / 1.251901584201389 / 327.16721159666866 | [NPY](tensors/0003362.npy) |
| 3363 | `model.layers.23.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 44.5 / 0.02248508930206299 / 1.6637377035983458 | [NPY](tensors/0003363.npy) |
| 3364 | `model.layers.23.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 44.5 / 0.02248508930206299 / 1.6637377035983458 | [NPY](tensors/0003364.npy) |
| 3365 | `model.layers.23.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 901] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003365.npy) |
| 3366 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 900.0 / 900.0 / 900.0 / 0.0 | [NPY](tensors/0003366.npy) |
| 3367 | `model.layers.23.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3368 | `model.layers.23.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3369 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.6053333282470703 / 0.9378499631722268 | [NPY](tensors/0003369.npy) |
| 3370 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.10818588733673096 / 0.7432403804988892 | [NPY](tensors/0003370.npy) |
| 3371 | `model.layers.23.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3372 | `model.layers.23.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 44.5 / 0.02248508930206299 / 1.6637377035983458 | [NPY](tensors/0003372.npy) |
| 3373 | `model.layers.23.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.75 / 19.875 / 0.002245848998427391 / 1.8185103664397406 | [NPY](tensors/0003373.npy) |
| 3374 | `model.layers.23.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 44.5 / 0.02248508930206299 / 1.6637377035983458 | [NPY](tensors/0003374.npy) |
| 3375 | `model.layers.23.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -106.0 / 69.0 / -0.2428586781024933 / 8.065091653759007 | [NPY](tensors/0003375.npy) |
| 3376 | `model.layers.23.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 44.5 / 0.02248508930206299 / 1.6637377035983458 | [NPY](tensors/0003376.npy) |
| 3377 | `model.layers.23.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.0 / 12.0 / -0.18143153190612793 / 3.9799888247800532 | [NPY](tensors/0003377.npy) |
| 3378 | `model.layers.23.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -18.125 / 6.875 / -0.03455240436596796 / 1.1993299283913403 | [NPY](tensors/0003378.npy) |
| 3379 | `model.layers.23.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4160.0 / 4288.0 / 4.6395966000027125 / 188.82616217742614 | [NPY](tensors/0003379.npy) |
| 3380 | `model.layers.23.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4160.0 / 4288.0 / 4.6395966000027125 / 188.82616217742614 | [NPY](tensors/0003380.npy) |
| 3381 | `model.layers.23.self_attn` | 28 | `output[1]` | [1, 64, 1, 901] | torch.bfloat16 → float32 | 1.2576745200831851e-17 / 0.859375 / 0.0005651349752314459 / 0.009240814300182853 | [NPY](tensors/0003381.npy) |
| 3382 | `model.layers.23.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6976.0 / 6400.0 / 5.898177083333334 / 404.62414895445164 | [NPY](tensors/0003382.npy) |
| 3383 | `model.layers.23.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 10.0 / 0.002387107743157281 / 1.267545844788771 | [NPY](tensors/0003383.npy) |
| 3384 | `model.layers.23.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 10.0 / 0.002387107743157281 / 1.267545844788771 | [NPY](tensors/0003384.npy) |
| 3385 | `model.layers.23.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.75 / 10.0 / 0.002387107743157281 / 1.267545844788771 | [NPY](tensors/0003385.npy) |
| 3386 | `model.layers.23.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3387 | `model.layers.23.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3388 | `model.layers.23.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3389 | `model.layers.23.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1984.0 / 1920.0 / -1.2655086305406358 / 126.9840228148535 | [NPY](tensors/0003389.npy) |
| 3390 | `model.layers.23.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1984.0 / 1920.0 / -1.2655086305406358 / 126.9840228148535 | [NPY](tensors/0003390.npy) |
| 3391 | `model.layers.23.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.03125 / 2.015625 / 0.34112548828125 / 1.8668582647941285 | [NPY](tensors/0003391.npy) |
| 3392 | `model.layers.23` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5056.0 / 4416.0 / 4.646006944444444 / 373.49786285854685 | [NPY](tensors/0003392.npy) |
| 3471 | `model.layers.23` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8000.0 / 7872.0 / -2.765036349826389 / 396.32553571898393 | [NPY](tensors/0003471.npy) |
| 3472 | `model.layers.23` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 902] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003472.npy) |
| 3473 | `model.layers.23` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.58184814453125 / 0.9804601915905449 | [NPY](tensors/0003473.npy) |
| 3474 | `model.layers.23` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / 0.11050879955291748 / 0.7066672716698735 | [NPY](tensors/0003474.npy) |
| 3475 | `model.layers.23` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 901.0 / 901.0 / 901.0 / 0.0 | [NPY](tensors/0003475.npy) |
| 3476 | `model.layers.23` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3477 | `model.layers.23` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3478 | `model.layers.23` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3479 | `model.layers.23.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8000.0 / 7872.0 / -2.765036349826389 / 396.32553571898393 | [NPY](tensors/0003479.npy) |
| 3480 | `model.layers.23.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 53.5 / 0.00018821292453342014 / 1.708663551257702 | [NPY](tensors/0003480.npy) |
| 3481 | `model.layers.23.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 53.5 / 0.00018821292453342014 / 1.708663551257702 | [NPY](tensors/0003481.npy) |
| 3482 | `model.layers.23.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 902] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003482.npy) |
| 3483 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 901.0 / 901.0 / 901.0 / 0.0 | [NPY](tensors/0003483.npy) |
| 3484 | `model.layers.23.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3485 | `model.layers.23.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3486 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.58184814453125 / 0.9804601915905449 | [NPY](tensors/0003486.npy) |
| 3487 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / 0.11050879955291748 / 0.7066672716698735 | [NPY](tensors/0003487.npy) |
| 3488 | `model.layers.23.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3489 | `model.layers.23.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 53.5 / 0.00018821292453342014 / 1.708663551257702 | [NPY](tensors/0003489.npy) |
| 3490 | `model.layers.23.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.8125 / 15.625 / 0.01678073708899319 / 1.584578191330822 | [NPY](tensors/0003490.npy) |
| 3491 | `model.layers.23.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 53.5 / 0.00018821292453342014 / 1.708663551257702 | [NPY](tensors/0003491.npy) |
| 3492 | `model.layers.23.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -80.5 / 55.25 / -0.2623964287340641 / 6.9026014669261775 | [NPY](tensors/0003492.npy) |
| 3493 | `model.layers.23.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 53.5 / 0.00018821292453342014 / 1.708663551257702 | [NPY](tensors/0003493.npy) |
| 3494 | `model.layers.23.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.5 / 9.9375 / -0.26951372623443604 / 3.3460293116355735 | [NPY](tensors/0003494.npy) |
| 3495 | `model.layers.23.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.75 / 6.9375 / -0.027202676457818598 / 1.234126630280957 | [NPY](tensors/0003495.npy) |
| 3496 | `model.layers.23.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4512.0 / 4640.0 / 5.343810780843099 / 198.94943163291887 | [NPY](tensors/0003496.npy) |
| 3497 | `model.layers.23.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4512.0 / 4640.0 / 5.343810780843099 / 198.94943163291887 | [NPY](tensors/0003497.npy) |
| 3498 | `model.layers.23.self_attn` | 29 | `output[1]` | [1, 64, 1, 902] | torch.bfloat16 → float32 | 1.2420620087993939e-15 / 0.8515625 / 0.0005826914868350487 / 0.008133878864258566 | [NPY](tensors/0003498.npy) |
| 3499 | `model.layers.23.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7744.0 / 7808.0 / 2.5612060546875 / 456.76592447195105 | [NPY](tensors/0003499.npy) |
| 3500 | `model.layers.23.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 9.125 / -0.013045052687327066 / 1.2884509983490409 | [NPY](tensors/0003500.npy) |
| 3501 | `model.layers.23.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 9.125 / -0.013045052687327066 / 1.2884509983490409 | [NPY](tensors/0003501.npy) |
| 3502 | `model.layers.23.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -45.0 / 9.125 / -0.013045052687327066 / 1.2884509983490409 | [NPY](tensors/0003502.npy) |
| 3503 | `model.layers.23.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3504 | `model.layers.23.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3505 | `model.layers.23.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3506 | `model.layers.23.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1616.0 / 1728.0 / -0.4097110748291016 / 105.02305477091836 | [NPY](tensors/0003506.npy) |
| 3507 | `model.layers.23.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1616.0 / 1728.0 / -0.4097110748291016 / 105.02305477091836 | [NPY](tensors/0003507.npy) |
| 3508 | `model.layers.23.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.734375 / 1.53125 / 0.3719749450683594 / 1.3864362263440129 | [NPY](tensors/0003508.npy) |
| 3509 | `model.layers.23` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6016.0 / 6208.0 / 2.157101779513889 / 418.122614763664 | [NPY](tensors/0003509.npy) |
| 3588 | `model.layers.23` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8768.0 / 8448.0 / -4.967865668402778 / 411.07864478399733 | [NPY](tensors/0003588.npy) |
| 3589 | `model.layers.23` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 903] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003589.npy) |
| 3590 | `model.layers.23` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.57342529296875 / 1.011353752766297 | [NPY](tensors/0003590.npy) |
| 3591 | `model.layers.23` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.10230749845504761 / 0.668999264851671 | [NPY](tensors/0003591.npy) |
| 3592 | `model.layers.23` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 902.0 / 902.0 / 902.0 / 0.0 | [NPY](tensors/0003592.npy) |
| 3593 | `model.layers.23` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3594 | `model.layers.23` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3595 | `model.layers.23` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3596 | `model.layers.23.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8768.0 / 8448.0 / -4.967865668402778 / 411.07864478399733 | [NPY](tensors/0003596.npy) |
| 3597 | `model.layers.23.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 55.25 / -0.008423746956719293 / 1.7362230360336557 | [NPY](tensors/0003597.npy) |
| 3598 | `model.layers.23.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 55.25 / -0.008423746956719293 / 1.7362230360336557 | [NPY](tensors/0003598.npy) |
| 3599 | `model.layers.23.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 903] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003599.npy) |
| 3600 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 902.0 / 902.0 / 902.0 / 0.0 | [NPY](tensors/0003600.npy) |
| 3601 | `model.layers.23.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3602 | `model.layers.23.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3603 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.57342529296875 / 1.011353752766297 | [NPY](tensors/0003603.npy) |
| 3604 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.10230749845504761 / 0.668999264851671 | [NPY](tensors/0003604.npy) |
| 3605 | `model.layers.23.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3606 | `model.layers.23.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 55.25 / -0.008423746956719293 / 1.7362230360336557 | [NPY](tensors/0003606.npy) |
| 3607 | `model.layers.23.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.875 / 15.25 / 0.0031781569123268127 / 1.4789482828300538 | [NPY](tensors/0003607.npy) |
| 3608 | `model.layers.23.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 55.25 / -0.008423746956719293 / 1.7362230360336557 | [NPY](tensors/0003608.npy) |
| 3609 | `model.layers.23.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -73.0 / 52.25 / -0.18699979688972235 / 6.895049114701866 | [NPY](tensors/0003609.npy) |
| 3610 | `model.layers.23.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 55.25 / -0.008423746956719293 / 1.7362230360336557 | [NPY](tensors/0003610.npy) |
| 3611 | `model.layers.23.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.0 / 8.875 / -0.056473493576049805 / 2.926333600055371 | [NPY](tensors/0003611.npy) |
| 3612 | `model.layers.23.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.75 / 4.3125 / -0.020065943390363827 / 0.8295430215309929 | [NPY](tensors/0003612.npy) |
| 3613 | `model.layers.23.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4928.0 / 5152.0 / 5.60912102593316 / 217.62520060407297 | [NPY](tensors/0003613.npy) |
| 3614 | `model.layers.23.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4928.0 / 5152.0 / 5.60912102593316 / 217.62520060407297 | [NPY](tensors/0003614.npy) |
| 3615 | `model.layers.23.self_attn` | 30 | `output[1]` | [1, 64, 1, 903] | torch.bfloat16 → float32 | 6.52811138479592e-14 / 0.76953125 / 0.0004450639031958542 / 0.005265217534429845 | [NPY](tensors/0003615.npy) |
| 3616 | `model.layers.23.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 8960.0 / 0.6153903537326388 / 493.82765012247785 | [NPY](tensors/0003616.npy) |
| 3617 | `model.layers.23.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 7.96875 / -0.021770233578152127 / 1.058825299115255 | [NPY](tensors/0003617.npy) |
| 3618 | `model.layers.23.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 7.96875 / -0.021770233578152127 / 1.058825299115255 | [NPY](tensors/0003618.npy) |
| 3619 | `model.layers.23.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.75 / 7.96875 / -0.021770233578152127 / 1.058825299115255 | [NPY](tensors/0003619.npy) |
| 3620 | `model.layers.23.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3621 | `model.layers.23.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3622 | `model.layers.23.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3623 | `model.layers.23.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1208.0 / 1048.0 / -0.7026296827528212 / 66.51098937149811 | [NPY](tensors/0003623.npy) |
| 3624 | `model.layers.23.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1208.0 / 1048.0 / -0.7026296827528212 / 66.51098937149811 | [NPY](tensors/0003624.npy) |
| 3625 | `model.layers.23.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8515625 / 1.234375 / 0.175079345703125 / 0.723156986863394 | [NPY](tensors/0003625.npy) |
| 3626 | `model.layers.23` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8128.0 / 7968.0 / -0.11520182291666667 / 446.29269406473304 | [NPY](tensors/0003626.npy) |
| 3705 | `model.layers.23` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9472.0 / 9088.0 / 8.896671549479167 / 441.8203988793093 | [NPY](tensors/0003705.npy) |
| 3706 | `model.layers.23` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 904] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003706.npy) |
| 3707 | `model.layers.23` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.576141357421875 / 0.9960825148117132 | [NPY](tensors/0003707.npy) |
| 3708 | `model.layers.23` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.10725325345993042 / 0.6890912510284947 | [NPY](tensors/0003708.npy) |
| 3709 | `model.layers.23` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 903.0 / 903.0 / 903.0 / 0.0 | [NPY](tensors/0003709.npy) |
| 3710 | `model.layers.23` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3711 | `model.layers.23` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3712 | `model.layers.23` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3713 | `model.layers.23.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9472.0 / 9088.0 / 8.896671549479167 / 441.8203988793093 | [NPY](tensors/0003713.npy) |
| 3714 | `model.layers.23.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 55.25 / 0.03761077788141039 / 1.7288349874872555 | [NPY](tensors/0003714.npy) |
| 3715 | `model.layers.23.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 55.25 / 0.03761077788141039 / 1.7288349874872555 | [NPY](tensors/0003715.npy) |
| 3716 | `model.layers.23.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 904] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003716.npy) |
| 3717 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 903.0 / 903.0 / 903.0 / 0.0 | [NPY](tensors/0003717.npy) |
| 3718 | `model.layers.23.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3719 | `model.layers.23.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3720 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.576141357421875 / 0.9960825148117132 | [NPY](tensors/0003720.npy) |
| 3721 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.10725325345993042 / 0.6890912510284947 | [NPY](tensors/0003721.npy) |
| 3722 | `model.layers.23.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3723 | `model.layers.23.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 55.25 / 0.03761077788141039 / 1.7288349874872555 | [NPY](tensors/0003723.npy) |
| 3724 | `model.layers.23.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.75 / 13.8125 / -0.003124286886304617 / 1.3908323326933139 | [NPY](tensors/0003724.npy) |
| 3725 | `model.layers.23.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 55.25 / 0.03761077788141039 / 1.7288349874872555 | [NPY](tensors/0003725.npy) |
| 3726 | `model.layers.23.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -65.0 / 48.25 / -0.3243883103132248 / 6.266806035976738 | [NPY](tensors/0003726.npy) |
| 3727 | `model.layers.23.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 55.25 / 0.03761077788141039 / 1.7288349874872555 | [NPY](tensors/0003727.npy) |
| 3728 | `model.layers.23.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.5 / 5.96875 / 0.021654784679412842 / 2.1831711012228703 | [NPY](tensors/0003728.npy) |
| 3729 | `model.layers.23.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.625 / 6.0 / -0.00959942136250902 / 1.0698354064798334 | [NPY](tensors/0003729.npy) |
| 3730 | `model.layers.23.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3808.0 / 4000.0 / 4.478317313724094 / 170.61073290881555 | [NPY](tensors/0003730.npy) |
| 3731 | `model.layers.23.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3808.0 / 4000.0 / 4.478317313724094 / 170.61073290881555 | [NPY](tensors/0003731.npy) |
| 3732 | `model.layers.23.self_attn` | 31 | `output[1]` | [1, 64, 1, 904] | torch.bfloat16 → float32 | 1.5543122344752192e-13 / 0.859375 / 0.0006532960789758779 / 0.0067844644858885295 | [NPY](tensors/0003732.npy) |
| 3733 | `model.layers.23.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8160.0 / 7776.0 / 13.354302300347221 / 437.64897403942774 | [NPY](tensors/0003733.npy) |
| 3734 | `model.layers.23.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 9.125 / 0.021035702029863993 / 1.161186164813637 | [NPY](tensors/0003734.npy) |
| 3735 | `model.layers.23.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 9.125 / 0.021035702029863993 / 1.161186164813637 | [NPY](tensors/0003735.npy) |
| 3736 | `model.layers.23.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -42.0 / 9.125 / 0.021035702029863993 / 1.161186164813637 | [NPY](tensors/0003736.npy) |
| 3737 | `model.layers.23.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3738 | `model.layers.23.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3739 | `model.layers.23.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3740 | `model.layers.23.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2024.0 / 1824.0 / -0.13158333831363253 / 94.2456135042696 | [NPY](tensors/0003740.npy) |
| 3741 | `model.layers.23.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2024.0 / 1824.0 / -0.13158333831363253 / 94.2456135042696 | [NPY](tensors/0003741.npy) |
| 3742 | `model.layers.23.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.734375 / 1.6953125 / 0.22802734375 / 1.1948076565821868 | [NPY](tensors/0003742.npy) |
| 3743 | `model.layers.23` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8064.0 / 7680.0 / 13.235774739583333 / 461.45641801978377 | [NPY](tensors/0003743.npy) |
| 3822 | `model.layers.23` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10816.0 / -1.4232896592881945 / 481.48824163425525 | [NPY](tensors/0003822.npy) |
| 3823 | `model.layers.23` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 905] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003823.npy) |
| 3824 | `model.layers.23` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.56591796875 / 1.009767041675747 | [NPY](tensors/0003824.npy) |
| 3825 | `model.layers.23` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.28125 / 0.13484972715377808 / 0.6728120153629138 | [NPY](tensors/0003825.npy) |
| 3826 | `model.layers.23` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 904.0 / 904.0 / 904.0 / 0.0 | [NPY](tensors/0003826.npy) |
| 3827 | `model.layers.23` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3828 | `model.layers.23` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3829 | `model.layers.23` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3830 | `model.layers.23.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10816.0 / -1.4232896592881945 / 481.48824163425525 | [NPY](tensors/0003830.npy) |
| 3831 | `model.layers.23.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 60.25 / 0.006949197583728367 / 1.7698081581476026 | [NPY](tensors/0003831.npy) |
| 3832 | `model.layers.23.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 60.25 / 0.006949197583728367 / 1.7698081581476026 | [NPY](tensors/0003832.npy) |
| 3833 | `model.layers.23.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 905] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003833.npy) |
| 3834 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 904.0 / 904.0 / 904.0 / 0.0 | [NPY](tensors/0003834.npy) |
| 3835 | `model.layers.23.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3836 | `model.layers.23.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3837 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.56591796875 / 1.009767041675747 | [NPY](tensors/0003837.npy) |
| 3838 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.28125 / 0.13484972715377808 / 0.6728120153629138 | [NPY](tensors/0003838.npy) |
| 3839 | `model.layers.23.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3840 | `model.layers.23.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 60.25 / 0.006949197583728367 / 1.7698081581476026 | [NPY](tensors/0003840.npy) |
| 3841 | `model.layers.23.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.0 / 15.0 / 0.005489686969667673 / 1.4519267846985058 | [NPY](tensors/0003841.npy) |
| 3842 | `model.layers.23.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 60.25 / 0.006949197583728367 / 1.7698081581476026 | [NPY](tensors/0003842.npy) |
| 3843 | `model.layers.23.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.5 / 47.25 / -0.2518894225358963 / 5.714526535203894 | [NPY](tensors/0003843.npy) |
| 3844 | `model.layers.23.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 60.25 / 0.006949197583728367 / 1.7698081581476026 | [NPY](tensors/0003844.npy) |
| 3845 | `model.layers.23.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.625 / 6.625 / 0.014093875885009766 / 2.1076552037919973 | [NPY](tensors/0003845.npy) |
| 3846 | `model.layers.23.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.875 / 7.71875 / -0.01193896122276783 / 1.2869831757780845 | [NPY](tensors/0003846.npy) |
| 3847 | `model.layers.23.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5120.0 / 5280.0 / 7.327780787150065 / 225.1482904968546 | [NPY](tensors/0003847.npy) |
| 3848 | `model.layers.23.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5120.0 / 5280.0 / 7.327780787150065 / 225.1482904968546 | [NPY](tensors/0003848.npy) |
| 3849 | `model.layers.23.self_attn` | 32 | `output[1]` | [1, 64, 1, 905] | torch.bfloat16 → float32 | 3.885780586188048e-15 / 0.8359375 / 0.0006899353226167947 / 0.008050870412856776 | [NPY](tensors/0003849.npy) |
| 3850 | `model.layers.23.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 10496.0 / 5.87607421875 / 542.1424679103168 | [NPY](tensors/0003850.npy) |
| 3851 | `model.layers.23.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 6.6875 / -0.010057710276709663 / 1.0852482267457737 | [NPY](tensors/0003851.npy) |
| 3852 | `model.layers.23.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 6.6875 / -0.010057710276709663 / 1.0852482267457737 | [NPY](tensors/0003852.npy) |
| 3853 | `model.layers.23.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -40.25 / 6.6875 / -0.010057710276709663 / 1.0852482267457737 | [NPY](tensors/0003853.npy) |
| 3854 | `model.layers.23.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3855 | `model.layers.23.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3856 | `model.layers.23.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3857 | `model.layers.23.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1680.0 / 1656.0 / 0.2708060370551215 / 109.22846653793452 | [NPY](tensors/0003857.npy) |
| 3858 | `model.layers.23.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1680.0 / 1656.0 / 0.2708060370551215 / 109.22846653793452 | [NPY](tensors/0003858.npy) |
| 3859 | `model.layers.23.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.0390625 / 0.09131240844726562 / 0.5378337591840581 | [NPY](tensors/0003859.npy) |
| 3860 | `model.layers.23` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8576.0 / 8832.0 / 6.140489366319445 / 484.6781882149074 | [NPY](tensors/0003860.npy) |
| 3939 | `model.layers.23` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8512.0 / 7648.0 / -4.624099392361111 / 399.4545451647625 | [NPY](tensors/0003939.npy) |
| 3940 | `model.layers.23` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 906] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003940.npy) |
| 3941 | `model.layers.23` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.517730712890625 / 1.0482222047318746 | [NPY](tensors/0003941.npy) |
| 3942 | `model.layers.23` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.1620463728904724 / 0.645396390931362 | [NPY](tensors/0003942.npy) |
| 3943 | `model.layers.23` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 905.0 / 905.0 / 905.0 / 0.0 | [NPY](tensors/0003943.npy) |
| 3944 | `model.layers.23` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3945 | `model.layers.23` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3946 | `model.layers.23` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3947 | `model.layers.23.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8512.0 / 7648.0 / -4.624099392361111 / 399.4545451647625 | [NPY](tensors/0003947.npy) |
| 3948 | `model.layers.23.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 51.5 / -0.01214753786722819 / 1.7179608569063742 | [NPY](tensors/0003948.npy) |
| 3949 | `model.layers.23.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 51.5 / -0.01214753786722819 / 1.7179608569063742 | [NPY](tensors/0003949.npy) |
| 3950 | `model.layers.23.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 906] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003950.npy) |
| 3951 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 905.0 / 905.0 / 905.0 / 0.0 | [NPY](tensors/0003951.npy) |
| 3952 | `model.layers.23.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3953 | `model.layers.23.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3954 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.517730712890625 / 1.0482222047318746 | [NPY](tensors/0003954.npy) |
| 3955 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.1620463728904724 / 0.645396390931362 | [NPY](tensors/0003955.npy) |
| 3956 | `model.layers.23.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3957 | `model.layers.23.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 51.5 / -0.01214753786722819 / 1.7179608569063742 | [NPY](tensors/0003957.npy) |
| 3958 | `model.layers.23.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.625 / 15.875 / 0.01661478402093053 / 1.60800421261157 | [NPY](tensors/0003958.npy) |
| 3959 | `model.layers.23.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 51.5 / -0.01214753786722819 / 1.7179608569063742 | [NPY](tensors/0003959.npy) |
| 3960 | `model.layers.23.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.5 / 37.5 / -0.21866366267204285 / 5.935416030141979 | [NPY](tensors/0003960.npy) |
| 3961 | `model.layers.23.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 51.5 / -0.01214753786722819 / 1.7179608569063742 | [NPY](tensors/0003961.npy) |
| 3962 | `model.layers.23.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.4375 / 15.0625 / -0.032169342041015625 / 3.348652859631813 | [NPY](tensors/0003962.npy) |
| 3963 | `model.layers.23.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.25 / 5.4375 / -0.01000345905777067 / 1.1148710265801065 | [NPY](tensors/0003963.npy) |
| 3964 | `model.layers.23.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4000.0 / 4224.0 / 5.596388583713107 / 176.22797562867828 | [NPY](tensors/0003964.npy) |
| 3965 | `model.layers.23.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4000.0 / 4224.0 / 5.596388583713107 / 176.22797562867828 | [NPY](tensors/0003965.npy) |
| 3966 | `model.layers.23.self_attn` | 33 | `output[1]` | [1, 64, 1, 906] | torch.bfloat16 → float32 | 3.066991105526995e-15 / 0.84765625 / 0.0005861480114494506 / 0.007686317741716878 | [NPY](tensors/0003966.npy) |
| 3967 | `model.layers.23.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8064.0 / 7424.0 / 0.9729736328125 / 434.4175638720788 | [NPY](tensors/0003967.npy) |
| 3968 | `model.layers.23.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 6.59375 / -0.01771427525414361 / 1.197704212855445 | [NPY](tensors/0003968.npy) |
| 3969 | `model.layers.23.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 6.59375 / -0.01771427525414361 / 1.197704212855445 | [NPY](tensors/0003969.npy) |
| 3970 | `model.layers.23.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -41.25 / 6.59375 / -0.01771427525414361 / 1.197704212855445 | [NPY](tensors/0003970.npy) |
| 3971 | `model.layers.23.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3972 | `model.layers.23.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3973 | `model.layers.23.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3974 | `model.layers.23.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1736.0 / 1512.0 / -0.060762850443522136 / 80.31503077506333 | [NPY](tensors/0003974.npy) |
| 3975 | `model.layers.23.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1736.0 / 1512.0 / -0.060762850443522136 / 80.31503077506333 | [NPY](tensors/0003975.npy) |
| 3976 | `model.layers.23.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.65625 / 1.390625 / 0.31036376953125 / 1.1221675565063367 | [NPY](tensors/0003976.npy) |
| 3977 | `model.layers.23` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7936.0 / 7296.0 / 0.8885389539930556 / 450.31115371284403 | [NPY](tensors/0003977.npy) |
| 4056 | `model.layers.23` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 9344.0 / 4.618660481770833 / 431.612691356808 | [NPY](tensors/0004056.npy) |
| 4057 | `model.layers.23` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 907] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004057.npy) |
| 4058 | `model.layers.23` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.439208984375 / 1.0785913702628929 | [NPY](tensors/0004058.npy) |
| 4059 | `model.layers.23` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.15223175287246704 / 0.6555427416634236 | [NPY](tensors/0004059.npy) |
| 4060 | `model.layers.23` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 906.0 / 906.0 / 906.0 / 0.0 | [NPY](tensors/0004060.npy) |
| 4061 | `model.layers.23` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4062 | `model.layers.23` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4063 | `model.layers.23` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4064 | `model.layers.23.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 9344.0 / 4.618660481770833 / 431.612691356808 | [NPY](tensors/0004064.npy) |
| 4065 | `model.layers.23.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 58.25 / 0.023695287770695156 / 1.7533252327664615 | [NPY](tensors/0004065.npy) |
| 4066 | `model.layers.23.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 58.25 / 0.023695287770695156 / 1.7533252327664615 | [NPY](tensors/0004066.npy) |
| 4067 | `model.layers.23.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 907] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004067.npy) |
| 4068 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 906.0 / 906.0 / 906.0 / 0.0 | [NPY](tensors/0004068.npy) |
| 4069 | `model.layers.23.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4070 | `model.layers.23.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4071 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.439208984375 / 1.0785913702628929 | [NPY](tensors/0004071.npy) |
| 4072 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.15223175287246704 / 0.6555427416634236 | [NPY](tensors/0004072.npy) |
| 4073 | `model.layers.23.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4074 | `model.layers.23.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 58.25 / 0.023695287770695156 / 1.7533252327664615 | [NPY](tensors/0004074.npy) |
| 4075 | `model.layers.23.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.96875 / 15.5 / 0.002605456975288689 / 1.4653834497083749 | [NPY](tensors/0004075.npy) |
| 4076 | `model.layers.23.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 58.25 / 0.023695287770695156 / 1.7533252327664615 | [NPY](tensors/0004076.npy) |
| 4077 | `model.layers.23.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -64.5 / 51.5 / -0.15275169909000397 / 6.232230832272731 | [NPY](tensors/0004077.npy) |
| 4078 | `model.layers.23.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 58.25 / 0.023695287770695156 / 1.7533252327664615 | [NPY](tensors/0004078.npy) |
| 4079 | `model.layers.23.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.625 / 6.9375 / -0.2255062460899353 / 2.1393960709410793 | [NPY](tensors/0004079.npy) |
| 4080 | `model.layers.23.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.25 / 5.3125 / -0.04081094181674416 / 0.9548499808562817 | [NPY](tensors/0004080.npy) |
| 4081 | `model.layers.23.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5568.0 / 5.467850960625542 / 237.795638864074 | [NPY](tensors/0004081.npy) |
| 4082 | `model.layers.23.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5568.0 / 5.467850960625542 / 237.795638864074 | [NPY](tensors/0004082.npy) |
| 4083 | `model.layers.23.self_attn` | 34 | `output[1]` | [1, 64, 1, 907] | torch.bfloat16 → float32 | 6.439293542825908e-15 / 0.83984375 / 0.0006378255945847079 / 0.00668711109713901 | [NPY](tensors/0004083.npy) |
| 4084 | `model.layers.23.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9984.0 / 10.126022677951388 / 530.3837353728171 | [NPY](tensors/0004084.npy) |
| 4085 | `model.layers.23.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 7.96875 / -0.002544489171769884 / 1.0357471514312728 | [NPY](tensors/0004085.npy) |
| 4086 | `model.layers.23.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 7.96875 / -0.002544489171769884 / 1.0357471514312728 | [NPY](tensors/0004086.npy) |
| 4087 | `model.layers.23.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.0 / 7.96875 / -0.002544489171769884 / 1.0357471514312728 | [NPY](tensors/0004087.npy) |
| 4088 | `model.layers.23.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4089 | `model.layers.23.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4090 | `model.layers.23.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4091 | `model.layers.23.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -892.0 / 944.0 / -0.2523994657728407 / 61.138750583153474 | [NPY](tensors/0004091.npy) |
| 4092 | `model.layers.23.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -892.0 / 944.0 / -0.2523994657728407 / 61.138750583153474 | [NPY](tensors/0004092.npy) |
| 4093 | `model.layers.23.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.9140625 / 0.72265625 / 0.19989013671875 / 0.43700445158472956 | [NPY](tensors/0004093.npy) |
| 4094 | `model.layers.23` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 9088.0 / 9.867173936631945 / 494.7593969941319 | [NPY](tensors/0004094.npy) |
| 4173 | `model.layers.23` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9472.0 / 9472.0 / 4.613087293836806 / 436.9686792555058 | [NPY](tensors/0004173.npy) |
| 4174 | `model.layers.23` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 908] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004174.npy) |
| 4175 | `model.layers.23` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.369232177734375 / 1.1234051302987014 | [NPY](tensors/0004175.npy) |
| 4176 | `model.layers.23` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.328125 / 0.08310973644256592 / 0.636302055198959 | [NPY](tensors/0004176.npy) |
| 4177 | `model.layers.23` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 907.0 / 907.0 / 907.0 / 0.0 | [NPY](tensors/0004177.npy) |
| 4178 | `model.layers.23` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4179 | `model.layers.23` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4180 | `model.layers.23` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4181 | `model.layers.23.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9472.0 / 9472.0 / 4.613087293836806 / 436.9686792555058 | [NPY](tensors/0004181.npy) |
| 4182 | `model.layers.23.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 58.25 / 0.026794335577223036 / 1.7613014033534973 | [NPY](tensors/0004182.npy) |
| 4183 | `model.layers.23.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 58.25 / 0.026794335577223036 / 1.7613014033534973 | [NPY](tensors/0004183.npy) |
| 4184 | `model.layers.23.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 908] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004184.npy) |
| 4185 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 907.0 / 907.0 / 907.0 / 0.0 | [NPY](tensors/0004185.npy) |
| 4186 | `model.layers.23.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4187 | `model.layers.23.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4188 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.369232177734375 / 1.1234051302987014 | [NPY](tensors/0004188.npy) |
| 4189 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.328125 / 0.08310973644256592 / 0.636302055198959 | [NPY](tensors/0004189.npy) |
| 4190 | `model.layers.23.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4191 | `model.layers.23.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 58.25 / 0.026794335577223036 / 1.7613014033534973 | [NPY](tensors/0004191.npy) |
| 4192 | `model.layers.23.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.53125 / 15.6875 / 0.006262163631618023 / 1.4689304338637492 | [NPY](tensors/0004192.npy) |
| 4193 | `model.layers.23.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 58.25 / 0.026794335577223036 / 1.7613014033534973 | [NPY](tensors/0004193.npy) |
| 4194 | `model.layers.23.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -67.0 / 50.25 / -0.1973706940189004 / 6.13169698397154 | [NPY](tensors/0004194.npy) |
| 4195 | `model.layers.23.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 58.25 / 0.026794335577223036 / 1.7613014033534973 | [NPY](tensors/0004195.npy) |
| 4196 | `model.layers.23.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.625 / 9.9375 / -0.09206622838973999 / 2.7009869931510027 | [NPY](tensors/0004196.npy) |
| 4197 | `model.layers.23.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.0 / 7.78125 / -0.029674138146219775 / 1.1795586401437597 | [NPY](tensors/0004197.npy) |
| 4198 | `model.layers.23.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5728.0 / 5920.0 / 6.793876859876844 / 255.20104206375947 | [NPY](tensors/0004198.npy) |
| 4199 | `model.layers.23.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5728.0 / 5920.0 / 6.793876859876844 / 255.20104206375947 | [NPY](tensors/0004199.npy) |
| 4200 | `model.layers.23.self_attn` | 35 | `output[1]` | [1, 64, 1, 908] | torch.bfloat16 → float32 | 1.0658141036401503e-14 / 0.80859375 / 0.0007986160411395642 / 0.0072608095288030665 | [NPY](tensors/0004200.npy) |
| 4201 | `model.layers.23.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9856.0 / 9984.0 / 11.390692816840279 / 539.8557445050151 | [NPY](tensors/0004201.npy) |
| 4202 | `model.layers.23.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 7.71875 / 0.004519863923390707 / 0.9493564401121918 | [NPY](tensors/0004202.npy) |
| 4203 | `model.layers.23.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 7.71875 / 0.004519863923390707 / 0.9493564401121918 | [NPY](tensors/0004203.npy) |
| 4204 | `model.layers.23.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.25 / 7.71875 / 0.004519863923390707 / 0.9493564401121918 | [NPY](tensors/0004204.npy) |
| 4205 | `model.layers.23.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4206 | `model.layers.23.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4207 | `model.layers.23.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4208 | `model.layers.23.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1416.0 / 1416.0 / 0.1913614061143663 / 82.72777675060149 | [NPY](tensors/0004208.npy) |
| 4209 | `model.layers.23.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1416.0 / 1416.0 / 0.1913614061143663 / 82.72777675060149 | [NPY](tensors/0004209.npy) |
| 4210 | `model.layers.23.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.140625 / 0.6953125 / 0.1688995361328125 / 0.43855903987189243 | [NPY](tensors/0004210.npy) |
| 4211 | `model.layers.23` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8640.0 / 8640.0 / 11.577389865451389 / 478.3936308466106 | [NPY](tensors/0004211.npy) |
| 4290 | `model.layers.23` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 9344.0 / 2.018857150607639 / 455.1572582776946 | [NPY](tensors/0004290.npy) |
| 4291 | `model.layers.23` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 909] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004291.npy) |
| 4292 | `model.layers.23` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.353973388671875 / 1.129845910800914 | [NPY](tensors/0004292.npy) |
| 4293 | `model.layers.23` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.328125 / -0.02260303497314453 / 0.6391623929271725 | [NPY](tensors/0004293.npy) |
| 4294 | `model.layers.23` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 908.0 / 908.0 / 908.0 / 0.0 | [NPY](tensors/0004294.npy) |
| 4295 | `model.layers.23` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4296 | `model.layers.23` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4297 | `model.layers.23` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4298 | `model.layers.23.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 9344.0 / 2.018857150607639 / 455.1572582776946 | [NPY](tensors/0004298.npy) |
| 4299 | `model.layers.23.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 55.25 / 0.017295326126946342 / 1.7367963622225613 | [NPY](tensors/0004299.npy) |
| 4300 | `model.layers.23.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 55.25 / 0.017295326126946342 / 1.7367963622225613 | [NPY](tensors/0004300.npy) |
| 4301 | `model.layers.23.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 909] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004301.npy) |
| 4302 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 908.0 / 908.0 / 908.0 / 0.0 | [NPY](tensors/0004302.npy) |
| 4303 | `model.layers.23.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4304 | `model.layers.23.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4305 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.353973388671875 / 1.129845910800914 | [NPY](tensors/0004305.npy) |
| 4306 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.328125 / -0.02260303497314453 / 0.6391623929271725 | [NPY](tensors/0004306.npy) |
| 4307 | `model.layers.23.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4308 | `model.layers.23.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 55.25 / 0.017295326126946342 / 1.7367963622225613 | [NPY](tensors/0004308.npy) |
| 4309 | `model.layers.23.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.6875 / 16.625 / -0.00402691843919456 / 1.4197258363093006 | [NPY](tensors/0004309.npy) |
| 4310 | `model.layers.23.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 55.25 / 0.017295326126946342 / 1.7367963622225613 | [NPY](tensors/0004310.npy) |
| 4311 | `model.layers.23.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -64.5 / 49.5 / -0.18483924865722656 / 6.299019864067312 | [NPY](tensors/0004311.npy) |
| 4312 | `model.layers.23.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 55.25 / 0.017295326126946342 / 1.7367963622225613 | [NPY](tensors/0004312.npy) |
| 4313 | `model.layers.23.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.25 / 8.4375 / -0.1279597282409668 / 2.7360501580379872 | [NPY](tensors/0004313.npy) |
| 4314 | `model.layers.23.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.75 / 6.09375 / 0.01719369867350906 / 1.3005436949703861 | [NPY](tensors/0004314.npy) |
| 4315 | `model.layers.23.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5248.0 / 5632.0 / 7.189081531100803 / 240.49466708160938 | [NPY](tensors/0004315.npy) |
| 4316 | `model.layers.23.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5248.0 / 5632.0 / 7.189081531100803 / 240.49466708160938 | [NPY](tensors/0004316.npy) |
| 4317 | `model.layers.23.self_attn` | 36 | `output[1]` | [1, 64, 1, 909] | torch.bfloat16 → float32 | 2.0095036745715333e-14 / 0.77734375 / 0.0006659361032483274 / 0.007750862937595161 | [NPY](tensors/0004317.npy) |
| 4318 | `model.layers.23.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 9664.0 / 9.20490451388889 / 542.6069316752813 | [NPY](tensors/0004318.npy) |
| 4319 | `model.layers.23.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.75 / 7.375 / 0.0023104720645480688 / 0.9720432343250721 | [NPY](tensors/0004319.npy) |
| 4320 | `model.layers.23.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.75 / 7.375 / 0.0023104720645480688 / 0.9720432343250721 | [NPY](tensors/0004320.npy) |
| 4321 | `model.layers.23.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.75 / 7.375 / 0.0023104720645480688 / 0.9720432343250721 | [NPY](tensors/0004321.npy) |
| 4322 | `model.layers.23.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4323 | `model.layers.23.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4324 | `model.layers.23.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4325 | `model.layers.23.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2096.0 / 2144.0 / -0.06166373358832465 / 124.12680033478006 | [NPY](tensors/0004325.npy) |
| 4326 | `model.layers.23.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2096.0 / 2144.0 / -0.06166373358832465 / 124.12680033478006 | [NPY](tensors/0004326.npy) |
| 4327 | `model.layers.23.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3984375 / 0.7109375 / 0.1688079833984375 / 0.5788469219100134 | [NPY](tensors/0004327.npy) |
| 4328 | `model.layers.23` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8576.0 / 8128.0 / 9.149896918402778 / 454.083968439858 | [NPY](tensors/0004328.npy) |
| 4407 | `model.layers.23` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 8448.0 / 1.0755154079861111 / 432.7364542841246 | [NPY](tensors/0004407.npy) |
| 4408 | `model.layers.23` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 910] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004408.npy) |
| 4409 | `model.layers.23` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.40557861328125 / 1.0657613414649296 | [NPY](tensors/0004409.npy) |
| 4410 | `model.layers.23` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.2734375 / -0.11394071578979492 / 0.7046058830066726 | [NPY](tensors/0004410.npy) |
| 4411 | `model.layers.23` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 909.0 / 909.0 / 909.0 / 0.0 | [NPY](tensors/0004411.npy) |
| 4412 | `model.layers.23` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4413 | `model.layers.23` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4414 | `model.layers.23` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4415 | `model.layers.23.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 8448.0 / 1.0755154079861111 / 432.7364542841246 | [NPY](tensors/0004415.npy) |
| 4416 | `model.layers.23.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 51.25 / 0.009557699163754782 / 1.7007700631533957 | [NPY](tensors/0004416.npy) |
| 4417 | `model.layers.23.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 51.25 / 0.009557699163754782 / 1.7007700631533957 | [NPY](tensors/0004417.npy) |
| 4418 | `model.layers.23.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 910] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004418.npy) |
| 4419 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 909.0 / 909.0 / 909.0 / 0.0 | [NPY](tensors/0004419.npy) |
| 4420 | `model.layers.23.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4421 | `model.layers.23.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4422 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.40557861328125 / 1.0657613414649296 | [NPY](tensors/0004422.npy) |
| 4423 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.2734375 / -0.11394071578979492 / 0.7046058830066726 | [NPY](tensors/0004423.npy) |
| 4424 | `model.layers.23.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4425 | `model.layers.23.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 51.25 / 0.009557699163754782 / 1.7007700631533957 | [NPY](tensors/0004425.npy) |
| 4426 | `model.layers.23.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.5 / 18.75 / 0.013377608265727758 / 1.5197010367547137 | [NPY](tensors/0004426.npy) |
| 4427 | `model.layers.23.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 51.25 / 0.009557699163754782 / 1.7007700631533957 | [NPY](tensors/0004427.npy) |
| 4428 | `model.layers.23.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -76.0 / 50.75 / -0.06884072348475456 / 6.83490138762806 | [NPY](tensors/0004428.npy) |
| 4429 | `model.layers.23.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 51.25 / 0.009557699163754782 / 1.7007700631533957 | [NPY](tensors/0004429.npy) |
| 4430 | `model.layers.23.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.5 / 13.625 / 0.015426456928253174 / 3.217011948397207 | [NPY](tensors/0004430.npy) |
| 4431 | `model.layers.23.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.25 / 6.3125 / -0.004665422486141324 / 1.1795396207047757 | [NPY](tensors/0004431.npy) |
| 4432 | `model.layers.23.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4192.0 / 4512.0 / 4.366183725992839 / 188.50562894116743 | [NPY](tensors/0004432.npy) |
| 4433 | `model.layers.23.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4192.0 / 4512.0 / 4.366183725992839 / 188.50562894116743 | [NPY](tensors/0004433.npy) |
| 4434 | `model.layers.23.self_attn` | 37 | `output[1]` | [1, 64, 1, 910] | torch.bfloat16 → float32 | 3.58046925441613e-15 / 0.76953125 / 0.0006316403807202953 / 0.006917657871164768 | [NPY](tensors/0004434.npy) |
| 4435 | `model.layers.23.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9024.0 / 8256.0 / 5.426529947916666 / 476.1985824975069 | [NPY](tensors/0004435.npy) |
| 4436 | `model.layers.23.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 8.0625 / -0.007477218574947781 / 1.1613306741461198 | [NPY](tensors/0004436.npy) |
| 4437 | `model.layers.23.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 8.0625 / -0.007477218574947781 / 1.1613306741461198 | [NPY](tensors/0004437.npy) |
| 4438 | `model.layers.23.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -42.25 / 8.0625 / -0.007477218574947781 / 1.1613306741461198 | [NPY](tensors/0004438.npy) |
| 4439 | `model.layers.23.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4440 | `model.layers.23.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4441 | `model.layers.23.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4442 | `model.layers.23.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1816.0 / 1520.0 / -0.36313001844618054 / 81.10808493496636 | [NPY](tensors/0004442.npy) |
| 4443 | `model.layers.23.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1816.0 / 1520.0 / -0.36313001844618054 / 81.10808493496636 | [NPY](tensors/0004443.npy) |
| 4444 | `model.layers.23.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.5 / 1.25 / 0.2402496337890625 / 1.0026968746831852 | [NPY](tensors/0004444.npy) |
| 4445 | `model.layers.23` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 8032.0 / 5.071565755208334 / 485.9750735329539 | [NPY](tensors/0004445.npy) |
| 4524 | `model.layers.23` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8512.0 / 8096.0 / 4.000566948784722 / 415.90837294952655 | [NPY](tensors/0004524.npy) |
| 4525 | `model.layers.23` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 911] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004525.npy) |
| 4526 | `model.layers.23` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.49200439453125 / 1.0259755074121442 | [NPY](tensors/0004526.npy) |
| 4527 | `model.layers.23` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.14840924739837646 / 0.7028633553324986 | [NPY](tensors/0004527.npy) |
| 4528 | `model.layers.23` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 910.0 / 910.0 / 910.0 / 0.0 | [NPY](tensors/0004528.npy) |
| 4529 | `model.layers.23` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4530 | `model.layers.23` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4531 | `model.layers.23` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4532 | `model.layers.23.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8512.0 / 8096.0 / 4.000566948784722 / 415.90837294952655 | [NPY](tensors/0004532.npy) |
| 4533 | `model.layers.23.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 52.25 / 0.017788036002053156 / 1.7038875522159926 | [NPY](tensors/0004533.npy) |
| 4534 | `model.layers.23.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 52.25 / 0.017788036002053156 / 1.7038875522159926 | [NPY](tensors/0004534.npy) |
| 4535 | `model.layers.23.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 911] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004535.npy) |
| 4536 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 910.0 / 910.0 / 910.0 / 0.0 | [NPY](tensors/0004536.npy) |
| 4537 | `model.layers.23.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4538 | `model.layers.23.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4539 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.49200439453125 / 1.0259755074121442 | [NPY](tensors/0004539.npy) |
| 4540 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.14840924739837646 / 0.7028633553324986 | [NPY](tensors/0004540.npy) |
| 4541 | `model.layers.23.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4542 | `model.layers.23.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 52.25 / 0.017788036002053156 / 1.7038875522159926 | [NPY](tensors/0004542.npy) |
| 4543 | `model.layers.23.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.3125 / 16.25 / -0.005621067248284817 / 1.60850520313055 | [NPY](tensors/0004543.npy) |
| 4544 | `model.layers.23.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 52.25 / 0.017788036002053156 / 1.7038875522159926 | [NPY](tensors/0004544.npy) |
| 4545 | `model.layers.23.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -72.0 / 52.75 / -0.10505033214576542 / 6.785915285930042 | [NPY](tensors/0004545.npy) |
| 4546 | `model.layers.23.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 52.25 / 0.017788036002053156 / 1.7038875522159926 | [NPY](tensors/0004546.npy) |
| 4547 | `model.layers.23.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.5 / 9.3125 / -0.004853039979934692 / 2.9844237812949372 | [NPY](tensors/0004547.npy) |
| 4548 | `model.layers.23.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.75 / 7.375 / -0.025977766141295433 / 1.3092202585775894 | [NPY](tensors/0004548.npy) |
| 4549 | `model.layers.23.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5856.0 / 6016.0 / 6.554680633544922 / 265.10014260993853 | [NPY](tensors/0004549.npy) |
| 4550 | `model.layers.23.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5856.0 / 6016.0 / 6.554680633544922 / 265.10014260993853 | [NPY](tensors/0004550.npy) |
| 4551 | `model.layers.23.self_attn` | 38 | `output[1]` | [1, 64, 1, 911] | torch.bfloat16 → float32 | 5.1736392947532295e-14 / 0.8359375 / 0.0006193532612386407 / 0.008879133370231943 | [NPY](tensors/0004551.npy) |
| 4552 | `model.layers.23.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9216.0 / 8896.0 / 10.511176215277779 / 535.2489291132551 | [NPY](tensors/0004552.npy) |
| 4553 | `model.layers.23.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.0 / 9.4375 / 0.005122854974534776 / 1.1081356580539188 | [NPY](tensors/0004553.npy) |
| 4554 | `model.layers.23.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.0 / 9.4375 / 0.005122854974534776 / 1.1081356580539188 | [NPY](tensors/0004554.npy) |
| 4555 | `model.layers.23.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -39.0 / 9.4375 / 0.005122854974534776 / 1.1081356580539188 | [NPY](tensors/0004555.npy) |
| 4556 | `model.layers.23.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4557 | `model.layers.23.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4558 | `model.layers.23.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4559 | `model.layers.23.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1936.0 / 1768.0 / -1.7993544684516058 / 109.21491216356834 | [NPY](tensors/0004559.npy) |
| 4560 | `model.layers.23.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1936.0 / 1768.0 / -1.7993544684516058 / 109.21491216356834 | [NPY](tensors/0004560.npy) |
| 4561 | `model.layers.23.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.6875 / 0.91015625 / 0.170166015625 / 0.36339520133639175 | [NPY](tensors/0004561.npy) |
| 4562 | `model.layers.23` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7648.0 / 6976.0 / 8.719437662760416 / 456.0968339670284 | [NPY](tensors/0004562.npy) |
| 4641 | `model.layers.23` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 8832.0 / -0.8373494466145833 / 424.23460441643766 | [NPY](tensors/0004641.npy) |
| 4642 | `model.layers.23` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 912] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004642.npy) |
| 4643 | `model.layers.23` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.559814453125 / 1.0371191164410525 | [NPY](tensors/0004643.npy) |
| 4644 | `model.layers.23` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2734375 / -0.12162959575653076 / 0.636397050487149 | [NPY](tensors/0004644.npy) |
| 4645 | `model.layers.23` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 911.0 / 911.0 / 911.0 / 0.0 | [NPY](tensors/0004645.npy) |
| 4646 | `model.layers.23` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4647 | `model.layers.23` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4648 | `model.layers.23` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4649 | `model.layers.23.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 8832.0 / -0.8373494466145833 / 424.23460441643766 | [NPY](tensors/0004649.npy) |
| 4650 | `model.layers.23.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / 0.003354736665884654 / 1.7409508281453034 | [NPY](tensors/0004650.npy) |
| 4651 | `model.layers.23.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / 0.003354736665884654 / 1.7409508281453034 | [NPY](tensors/0004651.npy) |
| 4652 | `model.layers.23.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 912] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004652.npy) |
| 4653 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 911.0 / 911.0 / 911.0 / 0.0 | [NPY](tensors/0004653.npy) |
| 4654 | `model.layers.23.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4655 | `model.layers.23.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4656 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.559814453125 / 1.0371191164410525 | [NPY](tensors/0004656.npy) |
| 4657 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2734375 / -0.12162959575653076 / 0.636397050487149 | [NPY](tensors/0004657.npy) |
| 4658 | `model.layers.23.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4659 | `model.layers.23.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / 0.003354736665884654 / 1.7409508281453034 | [NPY](tensors/0004659.npy) |
| 4660 | `model.layers.23.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.375 / 17.0 / 0.006741751451045275 / 1.5119363566493587 | [NPY](tensors/0004660.npy) |
| 4661 | `model.layers.23.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / 0.003354736665884654 / 1.7409508281453034 | [NPY](tensors/0004661.npy) |
| 4662 | `model.layers.23.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -65.0 / 53.25 / -0.12458433269057423 / 6.242633231247148 | [NPY](tensors/0004662.npy) |
| 4663 | `model.layers.23.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / 0.003354736665884654 / 1.7409508281453034 | [NPY](tensors/0004663.npy) |
| 4664 | `model.layers.23.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.3125 / 8.0 / -0.09152507781982422 / 3.017494531430289 | [NPY](tensors/0004664.npy) |
| 4665 | `model.layers.23.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.25 / 6.375 / -0.04213536251336336 / 1.057418904210003 | [NPY](tensors/0004665.npy) |
| 4666 | `model.layers.23.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4224.0 / 4352.0 / 3.5605245378282335 / 182.4621193513401 | [NPY](tensors/0004666.npy) |
| 4667 | `model.layers.23.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4224.0 / 4352.0 / 3.5605245378282335 / 182.4621193513401 | [NPY](tensors/0004667.npy) |
| 4668 | `model.layers.23.self_attn` | 39 | `output[1]` | [1, 64, 1, 912] | torch.bfloat16 → float32 | 9.020562075079397e-16 / 0.8671875 / 0.0005564617832432849 / 0.007525416006884807 | [NPY](tensors/0004668.npy) |
| 4669 | `model.layers.23.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8704.0 / 8640.0 / 2.724509006076389 / 462.1342158027758 | [NPY](tensors/0004669.npy) |
| 4670 | `model.layers.23.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 8.9375 / -0.015493374400668674 / 1.2355538125258076 | [NPY](tensors/0004670.npy) |
| 4671 | `model.layers.23.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 8.9375 / -0.015493374400668674 / 1.2355538125258076 | [NPY](tensors/0004671.npy) |
| 4672 | `model.layers.23.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -45.0 / 8.9375 / -0.015493374400668674 / 1.2355538125258076 | [NPY](tensors/0004672.npy) |
| 4673 | `model.layers.23.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4674 | `model.layers.23.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4675 | `model.layers.23.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4676 | `model.layers.23.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1512.0 / 1328.0 / -0.1652212447590298 / 74.63514410572692 | [NPY](tensors/0004676.npy) |
| 4677 | `model.layers.23.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1512.0 / 1328.0 / -0.1652212447590298 / 74.63514410572692 | [NPY](tensors/0004677.npy) |
| 4678 | `model.layers.23.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.84375 / 1.421875 / 0.339080810546875 / 1.3150639407848366 | [NPY](tensors/0004678.npy) |
| 4679 | `model.layers.23` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8064.0 / 8000.0 / 2.5630208333333333 / 460.144507864999 | [NPY](tensors/0004679.npy) |
| 4758 | `model.layers.23` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8960.0 / 8448.0 / -1.4887776692708334 / 422.46956982244336 | [NPY](tensors/0004758.npy) |
| 4759 | `model.layers.23` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 913] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004759.npy) |
| 4760 | `model.layers.23` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.57440185546875 / 1.030810795441952 | [NPY](tensors/0004760.npy) |
| 4761 | `model.layers.23` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.2734375 / -0.07393771409988403 / 0.6426875034418209 | [NPY](tensors/0004761.npy) |
| 4762 | `model.layers.23` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 912.0 / 912.0 / 912.0 / 0.0 | [NPY](tensors/0004762.npy) |
| 4763 | `model.layers.23` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4764 | `model.layers.23` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4765 | `model.layers.23` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4766 | `model.layers.23.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8960.0 / 8448.0 / -1.4887776692708334 / 422.46956982244336 | [NPY](tensors/0004766.npy) |
| 4767 | `model.layers.23.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 52.0 / 0.0057711044947306315 / 1.6952453180534452 | [NPY](tensors/0004767.npy) |
| 4768 | `model.layers.23.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 52.0 / 0.0057711044947306315 / 1.6952453180534452 | [NPY](tensors/0004768.npy) |
| 4769 | `model.layers.23.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 913] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004769.npy) |
| 4770 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 912.0 / 912.0 / 912.0 / 0.0 | [NPY](tensors/0004770.npy) |
| 4771 | `model.layers.23.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4772 | `model.layers.23.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4773 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.57440185546875 / 1.030810795441952 | [NPY](tensors/0004773.npy) |
| 4774 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.2734375 / -0.07393771409988403 / 0.6426875034418209 | [NPY](tensors/0004774.npy) |
| 4775 | `model.layers.23.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4776 | `model.layers.23.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 52.0 / 0.0057711044947306315 / 1.6952453180534452 | [NPY](tensors/0004776.npy) |
| 4777 | `model.layers.23.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.9375 / 14.5 / -0.004996765004761983 / 1.4950515020444917 | [NPY](tensors/0004777.npy) |
| 4778 | `model.layers.23.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 52.0 / 0.0057711044947306315 / 1.6952453180534452 | [NPY](tensors/0004778.npy) |
| 4779 | `model.layers.23.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -68.5 / 54.0 / -0.1495083011686802 / 6.77890782800174 | [NPY](tensors/0004779.npy) |
| 4780 | `model.layers.23.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 52.0 / 0.0057711044947306315 / 1.6952453180534452 | [NPY](tensors/0004780.npy) |
| 4781 | `model.layers.23.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.25 / 6.9375 / -0.07378721237182617 / 2.2108029575169286 | [NPY](tensors/0004781.npy) |
| 4782 | `model.layers.23.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.25 / 5.125 / -0.017846912844106555 / 1.0876689933550057 | [NPY](tensors/0004782.npy) |
| 4783 | `model.layers.23.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5152.0 / 5280.0 / 5.324278598361545 / 226.4088287400109 | [NPY](tensors/0004783.npy) |
| 4784 | `model.layers.23.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5152.0 / 5280.0 / 5.324278598361545 / 226.4088287400109 | [NPY](tensors/0004784.npy) |
| 4785 | `model.layers.23.self_attn` | 40 | `output[1]` | [1, 64, 1, 913] | torch.bfloat16 → float32 | 2.4147350785597155e-15 / 0.73828125 / 0.0006348814116122779 / 0.007100474075595577 | [NPY](tensors/0004785.npy) |
| 4786 | `model.layers.23.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 8960.0 / 3.833972846137153 / 514.8487170095317 | [NPY](tensors/0004786.npy) |
| 4787 | `model.layers.23.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 7.34375 / -0.013248509168624878 / 1.1114784033771374 | [NPY](tensors/0004787.npy) |
| 4788 | `model.layers.23.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 7.34375 / -0.013248509168624878 / 1.1114784033771374 | [NPY](tensors/0004788.npy) |
| 4789 | `model.layers.23.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -42.25 / 7.34375 / -0.013248509168624878 / 1.1114784033771374 | [NPY](tensors/0004789.npy) |
| 4790 | `model.layers.23.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4791 | `model.layers.23.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4792 | `model.layers.23.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4793 | `model.layers.23.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1864.0 / 1728.0 / -1.1782230377197265 / 96.08371383332404 | [NPY](tensors/0004793.npy) |
| 4794 | `model.layers.23.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1864.0 / 1728.0 / -1.1782230377197265 / 96.08371383332404 | [NPY](tensors/0004794.npy) |
| 4795 | `model.layers.23.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.5234375 / 0.6953125 / 0.16736602783203125 / 0.526678722047897 | [NPY](tensors/0004795.npy) |
| 4796 | `model.layers.23` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7616.0 / 7168.0 / 2.6744818793402776 / 453.5274297508862 | [NPY](tensors/0004796.npy) |
| 4875 | `model.layers.23` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7936.0 / 7424.0 / 0.5629069010416666 / 381.5289409439769 | [NPY](tensors/0004875.npy) |
| 4876 | `model.layers.23` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 914] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004876.npy) |
| 4877 | `model.layers.23` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.5457305908203125 / 1.0267502307475864 | [NPY](tensors/0004877.npy) |
| 4878 | `model.layers.23` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.051917850971221924 / 0.6740142912053045 | [NPY](tensors/0004878.npy) |
| 4879 | `model.layers.23` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 913.0 / 913.0 / 913.0 / 0.0 | [NPY](tensors/0004879.npy) |
| 4880 | `model.layers.23` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4881 | `model.layers.23` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4882 | `model.layers.23` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4883 | `model.layers.23.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7936.0 / 7424.0 / 0.5629069010416666 / 381.5289409439769 | [NPY](tensors/0004883.npy) |
| 4884 | `model.layers.23.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 52.25 / 0.0074068837695651585 / 1.7096641949125266 | [NPY](tensors/0004884.npy) |
| 4885 | `model.layers.23.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 52.25 / 0.0074068837695651585 / 1.7096641949125266 | [NPY](tensors/0004885.npy) |
| 4886 | `model.layers.23.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 914] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004886.npy) |
| 4887 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 913.0 / 913.0 / 913.0 / 0.0 | [NPY](tensors/0004887.npy) |
| 4888 | `model.layers.23.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4889 | `model.layers.23.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4890 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.5457305908203125 / 1.0267502307475864 | [NPY](tensors/0004890.npy) |
| 4891 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.051917850971221924 / 0.6740142912053045 | [NPY](tensors/0004891.npy) |
| 4892 | `model.layers.23.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4893 | `model.layers.23.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 52.25 / 0.0074068837695651585 / 1.7096641949125266 | [NPY](tensors/0004893.npy) |
| 4894 | `model.layers.23.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.0625 / 16.125 / -0.004142407531617209 / 1.5992498993343647 | [NPY](tensors/0004894.npy) |
| 4895 | `model.layers.23.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 52.25 / 0.0074068837695651585 / 1.7096641949125266 | [NPY](tensors/0004895.npy) |
| 4896 | `model.layers.23.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.0 / 54.75 / -0.10655401460826397 / 6.452491276550471 | [NPY](tensors/0004896.npy) |
| 4897 | `model.layers.23.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 52.25 / 0.0074068837695651585 / 1.7096641949125266 | [NPY](tensors/0004897.npy) |
| 4898 | `model.layers.23.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -21.375 / 9.375 / -0.061418771743774414 / 3.280096155243122 | [NPY](tensors/0004898.npy) |
| 4899 | `model.layers.23.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -18.375 / 5.59375 / -0.026705270633101463 / 1.0146817193693642 | [NPY](tensors/0004899.npy) |
| 4900 | `model.layers.23.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5248.0 / 5440.0 / 5.49518068101671 / 238.07926488235933 | [NPY](tensors/0004900.npy) |
| 4901 | `model.layers.23.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5248.0 / 5440.0 / 5.49518068101671 / 238.07926488235933 | [NPY](tensors/0004901.npy) |
| 4902 | `model.layers.23.self_attn` | 41 | `output[1]` | [1, 64, 1, 914] | torch.bfloat16 → float32 | 2.0469737016526324e-16 / 0.85546875 / 0.0004449789520878549 / 0.005936869370505127 | [NPY](tensors/0004902.npy) |
| 4903 | `model.layers.23.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8512.0 / 8256.0 / 6.060991753472222 / 484.323996706513 | [NPY](tensors/0004903.npy) |
| 4904 | `model.layers.23.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 8.1875 / -0.0004618848363558451 / 1.0790628438463299 | [NPY](tensors/0004904.npy) |
| 4905 | `model.layers.23.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 8.1875 / -0.0004618848363558451 / 1.0790628438463299 | [NPY](tensors/0004905.npy) |
| 4906 | `model.layers.23.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.0 / 8.1875 / -0.0004618848363558451 / 1.0790628438463299 | [NPY](tensors/0004906.npy) |
| 4907 | `model.layers.23.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4908 | `model.layers.23.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4909 | `model.layers.23.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4910 | `model.layers.23.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1568.0 / 1560.0 / -2.335954793294271 / 107.40115496593157 | [NPY](tensors/0004910.npy) |
| 4911 | `model.layers.23.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1568.0 / 1560.0 / -2.335954793294271 / 107.40115496593157 | [NPY](tensors/0004911.npy) |
| 4912 | `model.layers.23.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.453125 / 1.265625 / 0.2525787353515625 / 0.9588479237051691 | [NPY](tensors/0004912.npy) |
| 4913 | `model.layers.23` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6944.0 / 6688.0 / 3.7210286458333335 / 420.1176921495802 | [NPY](tensors/0004913.npy) |
| 4992 | `model.layers.23` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 9088.0 / 1.8179195827907986 / 437.5866189267489 | [NPY](tensors/0004992.npy) |
| 4993 | `model.layers.23` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 915] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004993.npy) |
| 4994 | `model.layers.23` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.513641357421875 / 1.0381515204992577 | [NPY](tensors/0004994.npy) |
| 4995 | `model.layers.23` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / -0.07546013593673706 / 0.6806294351122038 | [NPY](tensors/0004995.npy) |
| 4996 | `model.layers.23` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 914.0 / 914.0 / 914.0 / 0.0 | [NPY](tensors/0004996.npy) |
| 4997 | `model.layers.23` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4998 | `model.layers.23` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4999 | `model.layers.23` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5000 | `model.layers.23.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 9088.0 / 1.8179195827907986 / 437.5866189267489 | [NPY](tensors/0005000.npy) |
| 5001 | `model.layers.23.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 55.75 / 0.0169583883550432 / 1.7692407801368242 | [NPY](tensors/0005001.npy) |
| 5002 | `model.layers.23.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 55.75 / 0.0169583883550432 / 1.7692407801368242 | [NPY](tensors/0005002.npy) |
| 5003 | `model.layers.23.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 915] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005003.npy) |
| 5004 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 914.0 / 914.0 / 914.0 / 0.0 | [NPY](tensors/0005004.npy) |
| 5005 | `model.layers.23.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5006 | `model.layers.23.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5007 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.513641357421875 / 1.0381515204992577 | [NPY](tensors/0005007.npy) |
| 5008 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3359375 / -0.07546013593673706 / 0.6806294351122038 | [NPY](tensors/0005008.npy) |
| 5009 | `model.layers.23.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5010 | `model.layers.23.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 55.75 / 0.0169583883550432 / 1.7692407801368242 | [NPY](tensors/0005010.npy) |
| 5011 | `model.layers.23.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.4375 / 17.125 / 0.0022795083932578564 / 1.4961111637934255 | [NPY](tensors/0005011.npy) |
| 5012 | `model.layers.23.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 55.75 / 0.0169583883550432 / 1.7692407801368242 | [NPY](tensors/0005012.npy) |
| 5013 | `model.layers.23.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -60.75 / 49.75 / -0.06882314383983612 / 6.024540100805477 | [NPY](tensors/0005013.npy) |
| 5014 | `model.layers.23.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 55.75 / 0.0169583883550432 / 1.7692407801368242 | [NPY](tensors/0005014.npy) |
| 5015 | `model.layers.23.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.75 / 7.21875 / 0.04429319500923157 / 2.598564159596683 | [NPY](tensors/0005015.npy) |
| 5016 | `model.layers.23.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.25 / 6.375 / 0.005607586121186614 / 1.1987053862769166 | [NPY](tensors/0005016.npy) |
| 5017 | `model.layers.23.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5184.0 / 5184.0 / 4.6176641252305775 / 227.27203023215563 | [NPY](tensors/0005017.npy) |
| 5018 | `model.layers.23.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5184.0 / 5184.0 / 4.6176641252305775 / 227.27203023215563 | [NPY](tensors/0005018.npy) |
| 5019 | `model.layers.23.self_attn` | 42 | `output[1]` | [1, 64, 1, 915] | torch.bfloat16 → float32 | 6.830473686658678e-18 / 0.97265625 / 0.0005225595859168778 / 0.006448660186234461 | [NPY](tensors/0005019.npy) |
| 5020 | `model.layers.23.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 8832.0 / 6.4361328125 / 509.47921620542684 | [NPY](tensors/0005020.npy) |
| 5021 | `model.layers.23.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 5.59375 / -0.0010348677635192872 / 1.070767780058753 | [NPY](tensors/0005021.npy) |
| 5022 | `model.layers.23.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 5.59375 / -0.0010348677635192872 / 1.070767780058753 | [NPY](tensors/0005022.npy) |
| 5023 | `model.layers.23.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.0 / 5.59375 / -0.0010348677635192872 / 1.070767780058753 | [NPY](tensors/0005023.npy) |
| 5024 | `model.layers.23.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5025 | `model.layers.23.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5026 | `model.layers.23.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5027 | `model.layers.23.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2224.0 / 1888.0 / -0.018019315931532116 / 137.08046792476551 | [NPY](tensors/0005027.npy) |
| 5028 | `model.layers.23.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2224.0 / 1888.0 / -0.018019315931532116 / 137.08046792476551 | [NPY](tensors/0005028.npy) |
| 5029 | `model.layers.23.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.125 / 1.3125 / 0.025997161865234375 / 0.7344620211031081 | [NPY](tensors/0005029.npy) |
| 5030 | `model.layers.23` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8192.0 / 6592.0 / 6.419406467013889 / 439.0499802407391 | [NPY](tensors/0005030.npy) |

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
