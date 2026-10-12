# Hook inspection: generation

Status: **complete**. 3870 full tensors; 5031 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -2.1646103764312276e-05 / 2.735240602027808 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 321, 321] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.305312926797458e+38 / 1.580968955092999e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 321, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7882230712617297 / 0.8876106672141242 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 321, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.1173851026170974 / 0.6217412290332741 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 321] | torch.int64 → int64 | 0.0 / 320.0 / 160.0 / 92.66426855410162 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -2.1646103764312276e-05 / 2.735240602027808 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 321, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.002088569955772653 / 0.7617013932325184 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 321, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.002088569955772653 / 0.7617013932325184 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 321, 321] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.305312926797458e+38 / 1.580968955092999e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 321] | torch.int64 → int64 | 0.0 / 320.0 / 160.0 / 92.66426855410162 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 321, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7882230712617297 / 0.8876106672141242 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 321, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.1173851026170974 / 0.6217412290332741 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.002088569955772653 / 0.7617013932325184 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 321, 4096] | torch.bfloat16 → float32 | -10.25 / 12.8125 / 0.02319542564791534 / 1.0565484307285995 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.002088569955772653 / 0.7617013932325184 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 321, 512] | torch.bfloat16 → float32 | -65.5 / 66.0 / 0.033363847532004956 / 5.7527441168162525 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.002088569955772653 / 0.7617013932325184 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 321, 512] | torch.bfloat16 → float32 | -8.125 / 7.75 / -0.015592737848699278 / 1.2437954848574129 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 321, 4096] | torch.bfloat16 → float32 | -8.125 / 7.75 / -0.007331685550100644 / 0.5608300014878052 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 321, 2880] | torch.bfloat16 → float32 | -34.5 / 52.75 / 0.030612033498946138 / 1.1894064333465812 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -34.5 / 52.75 / 0.030612033498946138 / 1.1894064333465812 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 321, 321] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0011616085078244292 / 0.02257488792848887 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -87.5 / 70.5 / 0.030596308643304582 / 2.929530719647362 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 321, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0015944900950523304 / 0.3535882220090854 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0015944900950523304 / 0.3535882220090854 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [321, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0015944900950523304 / 0.3535882220090854 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [321, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.020223247953205424 / 0.9367653738392923 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.020223247953205424 / 0.9367653738392923 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [321, 32] | torch.bfloat16 → float32 | -4.90625 / 3.4375 / -0.10854729387990411 / 1.000574141048501 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 321, 2880] | torch.bfloat16 → float32 | -93.0 / 105.5 / 0.05081248666721053 / 3.236226789623089 | [NPY](tensors/0000038.npy) |
| 117 | `model.layers.0` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 43.75 / 0.02880006796783871 / 2.9013049797239288 | [NPY](tensors/0000117.npy) |
| 118 | `model.layers.0` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000118.npy) |
| 119 | `model.layers.0` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0000119.npy) |
| 120 | `model.layers.0` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0000120.npy) |
| 121 | `model.layers.0` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0000121.npy) |
| 122 | `model.layers.0` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 123 | `model.layers.0` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 124 | `model.layers.0` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 125 | `model.layers.0.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 43.75 / 0.02880006796783871 / 2.9013049797239288 | [NPY](tensors/0000125.npy) |
| 126 | `model.layers.0.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000126.npy) |
| 127 | `model.layers.0.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000127.npy) |
| 128 | `model.layers.0.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000128.npy) |
| 129 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0000129.npy) |
| 130 | `model.layers.0.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 131 | `model.layers.0.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 132 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0000132.npy) |
| 133 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0000133.npy) |
| 134 | `model.layers.0.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 135 | `model.layers.0.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000135.npy) |
| 136 | `model.layers.0.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 7.4375 / 0.039632019703276455 / 0.9975220123045838 | [NPY](tensors/0000136.npy) |
| 137 | `model.layers.0.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000137.npy) |
| 138 | `model.layers.0.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.5 / 41.25 / 0.060565054416656494 / 4.792407804689708 | [NPY](tensors/0000138.npy) |
| 139 | `model.layers.0.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000139.npy) |
| 140 | `model.layers.0.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.9375 / 3.90625 / 0.001153320074081421 / 1.2325447380756387 | [NPY](tensors/0000140.npy) |
| 141 | `model.layers.0.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.21875 / 2.859375 / -0.0005697528104064986 / 0.4649810995564979 | [NPY](tensors/0000141.npy) |
| 142 | `model.layers.0.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.8125 / 40.25 / 0.02807587484518687 / 1.1987142168986538 | [NPY](tensors/0000142.npy) |
| 143 | `model.layers.0.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.8125 / 40.25 / 0.02807587484518687 / 1.1987142168986538 | [NPY](tensors/0000143.npy) |
| 144 | `model.layers.0.self_attn` | 1 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0033853745637709197 / 0.038120914753074685 | [NPY](tensors/0000144.npy) |
| 145 | `model.layers.0.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.25 / 43.5 / 0.0568189091152615 / 3.0801988859357365 | [NPY](tensors/0000145.npy) |
| 146 | `model.layers.0.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8359375 / 2.09375 / 0.003103089994854397 / 0.31291787006451516 | [NPY](tensors/0000146.npy) |
| 147 | `model.layers.0.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8359375 / 2.09375 / 0.003103089994854397 / 0.31291787006451516 | [NPY](tensors/0000147.npy) |
| 148 | `model.layers.0.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.8359375 / 2.09375 / 0.003103089994854397 / 0.31291787006451516 | [NPY](tensors/0000148.npy) |
| 149 | `model.layers.0.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 150 | `model.layers.0.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 151 | `model.layers.0.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 152 | `model.layers.0.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.28125 / 28.25 / 0.003325812394420306 / 0.8326241361348675 | [NPY](tensors/0000152.npy) |
| 153 | `model.layers.0.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.28125 / 28.25 / 0.003325812394420306 / 0.8326241361348675 | [NPY](tensors/0000153.npy) |
| 154 | `model.layers.0.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.5078125 / 2.234375 / -0.0728607177734375 / 0.9013503124469711 | [NPY](tensors/0000154.npy) |
| 155 | `model.layers.0` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.0 / 54.0 / 0.06005382935206095 / 3.2427998555307034 | [NPY](tensors/0000155.npy) |
| 234 | `model.layers.0` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 45.75 / 0.04227736194928487 / 3.1518798398795616 | [NPY](tensors/0000234.npy) |
| 235 | `model.layers.0` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000235.npy) |
| 236 | `model.layers.0` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0000236.npy) |
| 237 | `model.layers.0` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0000237.npy) |
| 238 | `model.layers.0` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0000238.npy) |
| 239 | `model.layers.0` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 240 | `model.layers.0` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 241 | `model.layers.0` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 242 | `model.layers.0.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 45.75 / 0.04227736194928487 / 3.1518798398795616 | [NPY](tensors/0000242.npy) |
| 243 | `model.layers.0.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000243.npy) |
| 244 | `model.layers.0.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000244.npy) |
| 245 | `model.layers.0.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000245.npy) |
| 246 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0000246.npy) |
| 247 | `model.layers.0.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 248 | `model.layers.0.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 249 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0000249.npy) |
| 250 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0000250.npy) |
| 251 | `model.layers.0.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 252 | `model.layers.0.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000252.npy) |
| 253 | `model.layers.0.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5 / 8.1875 / 0.022865560371428728 / 0.9733268065645532 | [NPY](tensors/0000253.npy) |
| 254 | `model.layers.0.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000254.npy) |
| 255 | `model.layers.0.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.75 / 47.0 / 0.09419560432434082 / 4.904277940788795 | [NPY](tensors/0000255.npy) |
| 256 | `model.layers.0.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000256.npy) |
| 257 | `model.layers.0.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 4.34375 / -0.08974748849868774 / 1.1126171556291353 | [NPY](tensors/0000257.npy) |
| 258 | `model.layers.0.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.25 / 3.796875 / -0.00925096247010515 / 0.5528710691885688 | [NPY](tensors/0000258.npy) |
| 259 | `model.layers.0.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.9375 / 37.75 / 0.023739319874180688 / 1.1827334401792426 | [NPY](tensors/0000259.npy) |
| 260 | `model.layers.0.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.9375 / 37.75 / 0.023739319874180688 / 1.1827334401792426 | [NPY](tensors/0000260.npy) |
| 261 | `model.layers.0.self_attn` | 2 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0038709860111687065 / 0.04214823716190571 | [NPY](tensors/0000261.npy) |
| 262 | `model.layers.0.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 45.25 / 0.06584057278103299 / 3.356731843728876 | [NPY](tensors/0000262.npy) |
| 263 | `model.layers.0.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.109375 / 2.015625 / 0.005575017134348551 / 0.31284158262903183 | [NPY](tensors/0000263.npy) |
| 264 | `model.layers.0.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.109375 / 2.015625 / 0.005575017134348551 / 0.31284158262903183 | [NPY](tensors/0000264.npy) |
| 265 | `model.layers.0.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.109375 / 2.015625 / 0.005575017134348551 / 0.31284158262903183 | [NPY](tensors/0000265.npy) |
| 266 | `model.layers.0.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 267 | `model.layers.0.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 268 | `model.layers.0.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 269 | `model.layers.0.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.5 / 23.0 / 0.027629189276032976 / 0.7623021086711805 | [NPY](tensors/0000269.npy) |
| 270 | `model.layers.0.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.5 / 23.0 / 0.027629189276032976 / 0.7623021086711805 | [NPY](tensors/0000270.npy) |
| 271 | `model.layers.0.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.5625 / 1.8359375 / -0.15050506591796875 / 1.0028062612335176 | [NPY](tensors/0000271.npy) |
| 272 | `model.layers.0` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 65.5 / 0.0934246646033393 / 3.5668614448346307 | [NPY](tensors/0000272.npy) |
| 351 | `model.layers.0` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0000351.npy) |
| 352 | `model.layers.0` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000352.npy) |
| 353 | `model.layers.0` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0000353.npy) |
| 354 | `model.layers.0` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0000354.npy) |
| 355 | `model.layers.0` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0000355.npy) |
| 356 | `model.layers.0` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 357 | `model.layers.0` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 358 | `model.layers.0` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 359 | `model.layers.0.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0000359.npy) |
| 360 | `model.layers.0.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000360.npy) |
| 361 | `model.layers.0.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000361.npy) |
| 362 | `model.layers.0.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000362.npy) |
| 363 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0000363.npy) |
| 364 | `model.layers.0.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 365 | `model.layers.0.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 366 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0000366.npy) |
| 367 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0000367.npy) |
| 368 | `model.layers.0.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 369 | `model.layers.0.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000369.npy) |
| 370 | `model.layers.0.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 9.25 / 0.06582052947487682 / 1.0317253511582722 | [NPY](tensors/0000370.npy) |
| 371 | `model.layers.0.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000371.npy) |
| 372 | `model.layers.0.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.5 / 59.75 / -0.027341485023498535 / 6.496414800406944 | [NPY](tensors/0000372.npy) |
| 373 | `model.layers.0.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000373.npy) |
| 374 | `model.layers.0.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.453125 / 4.6875 / 0.06333106756210327 / 0.9556167387162166 | [NPY](tensors/0000374.npy) |
| 375 | `model.layers.0.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.25 / 4.34375 / -0.010686465211620089 / 0.5544089016070174 | [NPY](tensors/0000375.npy) |
| 376 | `model.layers.0.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.1875 / 39.5 / 0.031500537693500516 / 1.203638276115619 | [NPY](tensors/0000376.npy) |
| 377 | `model.layers.0.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.1875 / 39.5 / 0.031500537693500516 / 1.203638276115619 | [NPY](tensors/0000377.npy) |
| 378 | `model.layers.0.self_attn` | 3 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003560383620136663 / 0.03959858213996353 | [NPY](tensors/0000378.npy) |
| 379 | `model.layers.0.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 39.25 / 0.08046215375264486 / 2.6641483263224317 | [NPY](tensors/0000379.npy) |
| 380 | `model.layers.0.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.375 / 1.875 / 0.006489267283015781 / 0.326908881906782 | [NPY](tensors/0000380.npy) |
| 381 | `model.layers.0.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.375 / 1.875 / 0.006489267283015781 / 0.326908881906782 | [NPY](tensors/0000381.npy) |
| 382 | `model.layers.0.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.375 / 1.875 / 0.006489267283015781 / 0.326908881906782 | [NPY](tensors/0000382.npy) |
| 383 | `model.layers.0.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 384 | `model.layers.0.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 385 | `model.layers.0.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 386 | `model.layers.0.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -16.0 / 51.75 / 0.0446285051604112 / 1.6583677591153403 | [NPY](tensors/0000386.npy) |
| 387 | `model.layers.0.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.0 / 51.75 / 0.0446285051604112 / 1.6583677591153403 | [NPY](tensors/0000387.npy) |
| 388 | `model.layers.0.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.328125 / 2.421875 / -0.124298095703125 / 1.2675718529961917 | [NPY](tensors/0000388.npy) |
| 389 | `model.layers.0` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 88.5 / 0.12485212220085992 / 3.422144756853717 | [NPY](tensors/0000389.npy) |
| 468 | `model.layers.0` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 34.5 / -0.00621017747455173 / 2.9689713325199563 | [NPY](tensors/0000468.npy) |
| 469 | `model.layers.0` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000469.npy) |
| 470 | `model.layers.0` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0000470.npy) |
| 471 | `model.layers.0` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0000471.npy) |
| 472 | `model.layers.0` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0000472.npy) |
| 473 | `model.layers.0` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 474 | `model.layers.0` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 475 | `model.layers.0` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 476 | `model.layers.0.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 34.5 / -0.00621017747455173 / 2.9689713325199563 | [NPY](tensors/0000476.npy) |
| 477 | `model.layers.0.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 8.75 / -0.004585133658515083 / 0.7492337618014016 | [NPY](tensors/0000477.npy) |
| 478 | `model.layers.0.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 8.75 / -0.004585133658515083 / 0.7492337618014016 | [NPY](tensors/0000478.npy) |
| 479 | `model.layers.0.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000479.npy) |
| 480 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0000480.npy) |
| 481 | `model.layers.0.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 482 | `model.layers.0.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 483 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0000483.npy) |
| 484 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0000484.npy) |
| 485 | `model.layers.0.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 486 | `model.layers.0.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 8.75 / -0.004585133658515083 / 0.7492337618014016 | [NPY](tensors/0000486.npy) |
| 487 | `model.layers.0.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.625 / 10.125 / 0.029261586867505684 / 1.0112363812461085 | [NPY](tensors/0000487.npy) |
| 488 | `model.layers.0.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 8.75 / -0.004585133658515083 / 0.7492337618014016 | [NPY](tensors/0000488.npy) |
| 489 | `model.layers.0.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -56.75 / 46.75 / -0.0824456587433815 / 5.565340349748302 | [NPY](tensors/0000489.npy) |
| 490 | `model.layers.0.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 8.75 / -0.004585133658515083 / 0.7492337618014016 | [NPY](tensors/0000490.npy) |
| 491 | `model.layers.0.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.5625 / 5.90625 / -0.08182156085968018 / 1.2309353697889387 | [NPY](tensors/0000491.npy) |
| 492 | `model.layers.0.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.21875 / 3.484375 / -0.0014971389828133397 / 0.5516500578036508 | [NPY](tensors/0000492.npy) |
| 493 | `model.layers.0.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.3125 / 42.75 / 0.03154841040571531 / 1.2572727534258015 | [NPY](tensors/0000493.npy) |
| 494 | `model.layers.0.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.3125 / 42.75 / 0.03154841040571531 / 1.2572727534258015 | [NPY](tensors/0000494.npy) |
| 495 | `model.layers.0.self_attn` | 4 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0030734501510067506 / 0.036523477487472596 | [NPY](tensors/0000495.npy) |
| 496 | `model.layers.0.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 40.5 / 0.025393443637424046 / 3.12274286583601 | [NPY](tensors/0000496.npy) |
| 497 | `model.layers.0.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.71875 / 1.9296875 / -0.003479789694150289 / 0.3043131469730198 | [NPY](tensors/0000497.npy) |
| 498 | `model.layers.0.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.71875 / 1.9296875 / -0.003479789694150289 / 0.3043131469730198 | [NPY](tensors/0000498.npy) |
| 499 | `model.layers.0.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.71875 / 1.9296875 / -0.003479789694150289 / 0.3043131469730198 | [NPY](tensors/0000499.npy) |
| 500 | `model.layers.0.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 501 | `model.layers.0.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 502 | `model.layers.0.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 503 | `model.layers.0.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.875 / 27.375 / 0.0354476981692844 / 1.0206028393989075 | [NPY](tensors/0000503.npy) |
| 504 | `model.layers.0.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.875 / 27.375 / 0.0354476981692844 / 1.0206028393989075 | [NPY](tensors/0000504.npy) |
| 505 | `model.layers.0.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.6875 / 1.265625 / -0.23114776611328125 / 0.7339425151027313 | [NPY](tensors/0000505.npy) |
| 506 | `model.layers.0` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.875 / 68.0 / 0.060712464650472 / 3.358377785435434 | [NPY](tensors/0000506.npy) |
| 585 | `model.layers.0` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.75 / 35.0 / 0.029632277372810576 / 3.0790713420157756 | [NPY](tensors/0000585.npy) |
| 586 | `model.layers.0` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000586.npy) |
| 587 | `model.layers.0` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0000587.npy) |
| 588 | `model.layers.0` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0000588.npy) |
| 589 | `model.layers.0` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0000589.npy) |
| 590 | `model.layers.0` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 591 | `model.layers.0` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 592 | `model.layers.0` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 593 | `model.layers.0.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.75 / 35.0 / 0.029632277372810576 / 3.0790713420157756 | [NPY](tensors/0000593.npy) |
| 594 | `model.layers.0.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0000594.npy) |
| 595 | `model.layers.0.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0000595.npy) |
| 596 | `model.layers.0.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000596.npy) |
| 597 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0000597.npy) |
| 598 | `model.layers.0.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 599 | `model.layers.0.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 600 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0000600.npy) |
| 601 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0000601.npy) |
| 602 | `model.layers.0.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 603 | `model.layers.0.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0000603.npy) |
| 604 | `model.layers.0.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.25 / 10.1875 / 0.01786483358591795 / 0.975573086522404 | [NPY](tensors/0000604.npy) |
| 605 | `model.layers.0.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0000605.npy) |
| 606 | `model.layers.0.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -55.5 / 43.25 / -0.043908245861530304 / 5.450620468537411 | [NPY](tensors/0000606.npy) |
| 607 | `model.layers.0.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.5 / 0.002124585707982381 / 0.7293914899189831 | [NPY](tensors/0000607.npy) |
| 608 | `model.layers.0.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.84375 / 5.65625 / -0.12457606196403503 / 1.1890564225679914 | [NPY](tensors/0000608.npy) |
| 609 | `model.layers.0.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.28125 / 4.71875 / -0.01445389762375271 / 0.5982222928729015 | [NPY](tensors/0000609.npy) |
| 610 | `model.layers.0.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.5625 / 42.5 / 0.027975874808099536 / 1.2721949027057924 | [NPY](tensors/0000610.npy) |
| 611 | `model.layers.0.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.5625 / 42.5 / 0.027975874808099536 / 1.2721949027057924 | [NPY](tensors/0000611.npy) |
| 612 | `model.layers.0.self_attn` | 5 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98046875 / 0.003359520551419132 / 0.035611531804170725 | [NPY](tensors/0000612.npy) |
| 613 | `model.layers.0.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 43.25 / 0.05770698123508029 / 3.3591969234996593 | [NPY](tensors/0000613.npy) |
| 614 | `model.layers.0.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.140625 / 1.4609375 / -0.003110043207804362 / 0.29021550309903354 | [NPY](tensors/0000614.npy) |
| 615 | `model.layers.0.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.140625 / 1.4609375 / -0.003110043207804362 / 0.29021550309903354 | [NPY](tensors/0000615.npy) |
| 616 | `model.layers.0.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.140625 / 1.4609375 / -0.003110043207804362 / 0.29021550309903354 | [NPY](tensors/0000616.npy) |
| 617 | `model.layers.0.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 618 | `model.layers.0.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 619 | `model.layers.0.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 620 | `model.layers.0.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -16.75 / 22.875 / 0.004789750691917207 / 0.7488338365158033 | [NPY](tensors/0000620.npy) |
| 621 | `model.layers.0.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.75 / 22.875 / 0.004789750691917207 / 0.7488338365158033 | [NPY](tensors/0000621.npy) |
| 622 | `model.layers.0.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.21875 / 1.5703125 / -0.17045974731445312 / 0.6422271790939839 | [NPY](tensors/0000622.npy) |
| 623 | `model.layers.0` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 64.5 / 0.06256370544433594 / 3.7157225848519904 | [NPY](tensors/0000623.npy) |
| 702 | `model.layers.0` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0000702.npy) |
| 703 | `model.layers.0` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000703.npy) |
| 704 | `model.layers.0` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0000704.npy) |
| 705 | `model.layers.0` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0000705.npy) |
| 706 | `model.layers.0` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0000706.npy) |
| 707 | `model.layers.0` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 708 | `model.layers.0` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 709 | `model.layers.0` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 710 | `model.layers.0.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0000710.npy) |
| 711 | `model.layers.0.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0000711.npy) |
| 712 | `model.layers.0.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0000712.npy) |
| 713 | `model.layers.0.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000713.npy) |
| 714 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0000714.npy) |
| 715 | `model.layers.0.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 716 | `model.layers.0.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 717 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0000717.npy) |
| 718 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0000718.npy) |
| 719 | `model.layers.0.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 720 | `model.layers.0.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0000720.npy) |
| 721 | `model.layers.0.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.84375 / 8.5625 / 0.0153301190584898 / 1.0113524420299036 | [NPY](tensors/0000721.npy) |
| 722 | `model.layers.0.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0000722.npy) |
| 723 | `model.layers.0.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.0 / 65.5 / 0.032654017210006714 / 6.89507515667232 | [NPY](tensors/0000723.npy) |
| 724 | `model.layers.0.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0000724.npy) |
| 725 | `model.layers.0.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.28125 / 3.390625 / -0.002120666205883026 / 0.8566653376613583 | [NPY](tensors/0000725.npy) |
| 726 | `model.layers.0.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.1875 / 3.609375 / 0.007038937861125305 / 0.46620829611733977 | [NPY](tensors/0000726.npy) |
| 727 | `model.layers.0.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 29.625 / 0.03504402736822764 / 0.9998362746790631 | [NPY](tensors/0000727.npy) |
| 728 | `model.layers.0.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 29.625 / 0.03504402736822764 / 0.9998362746790631 | [NPY](tensors/0000728.npy) |
| 729 | `model.layers.0.self_attn` | 6 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0029440953717275705 / 0.03107522445918853 | [NPY](tensors/0000729.npy) |
| 730 | `model.layers.0.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.0 / 33.0 / 0.03295380406909519 / 3.0125391112418125 | [NPY](tensors/0000730.npy) |
| 731 | `model.layers.0.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.546875 / 1.3828125 / 0.0010026176770528159 / 0.2900540245021064 | [NPY](tensors/0000731.npy) |
| 732 | `model.layers.0.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.546875 / 1.3828125 / 0.0010026176770528159 / 0.2900540245021064 | [NPY](tensors/0000732.npy) |
| 733 | `model.layers.0.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.546875 / 1.3828125 / 0.0010026176770528159 / 0.2900540245021064 | [NPY](tensors/0000733.npy) |
| 734 | `model.layers.0.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 735 | `model.layers.0.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 736 | `model.layers.0.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 737 | `model.layers.0.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.625 / 17.25 / 0.021852132678031922 / 0.7212352724671609 | [NPY](tensors/0000737.npy) |
| 738 | `model.layers.0.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.625 / 17.25 / 0.021852132678031922 / 0.7212352724671609 | [NPY](tensors/0000738.npy) |
| 739 | `model.layers.0.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.90625 / 2.859375 / -0.028961181640625 / 1.4157500468507656 | [NPY](tensors/0000739.npy) |
| 740 | `model.layers.0` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.375 / 50.25 / 0.05474133491516113 / 3.0189534155835474 | [NPY](tensors/0000740.npy) |
| 819 | `model.layers.0` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 35.5 / 0.025291162646479078 / 2.9024239561028407 | [NPY](tensors/0000819.npy) |
| 820 | `model.layers.0` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000820.npy) |
| 821 | `model.layers.0` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0000821.npy) |
| 822 | `model.layers.0` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0000822.npy) |
| 823 | `model.layers.0` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0000823.npy) |
| 824 | `model.layers.0` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 825 | `model.layers.0` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 826 | `model.layers.0` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 827 | `model.layers.0.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 35.5 / 0.025291162646479078 / 2.9024239561028407 | [NPY](tensors/0000827.npy) |
| 828 | `model.layers.0.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.0 / 9.625 / 0.00490583587023947 / 0.7960603038325479 | [NPY](tensors/0000828.npy) |
| 829 | `model.layers.0.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.0 / 9.625 / 0.00490583587023947 / 0.7960603038325479 | [NPY](tensors/0000829.npy) |
| 830 | `model.layers.0.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000830.npy) |
| 831 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0000831.npy) |
| 832 | `model.layers.0.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 833 | `model.layers.0.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 834 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0000834.npy) |
| 835 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0000835.npy) |
| 836 | `model.layers.0.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 837 | `model.layers.0.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.0 / 9.625 / 0.00490583587023947 / 0.7960603038325479 | [NPY](tensors/0000837.npy) |
| 838 | `model.layers.0.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0625 / 8.5 / 0.030272164847701788 / 0.9853703337645039 | [NPY](tensors/0000838.npy) |
| 839 | `model.layers.0.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.0 / 9.625 / 0.00490583587023947 / 0.7960603038325479 | [NPY](tensors/0000839.npy) |
| 840 | `model.layers.0.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.5 / 50.75 / 0.08591138012707233 / 5.104874768475402 | [NPY](tensors/0000840.npy) |
| 841 | `model.layers.0.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.0 / 9.625 / 0.00490583587023947 / 0.7960603038325479 | [NPY](tensors/0000841.npy) |
| 842 | `model.layers.0.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.65625 / 3.640625 / -0.019169986248016357 / 1.1832823689364846 | [NPY](tensors/0000842.npy) |
| 843 | `model.layers.0.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.34375 / 2.84375 / -0.003967520944115677 / 0.4026698105282072 | [NPY](tensors/0000843.npy) |
| 844 | `model.layers.0.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5 / 42.75 / 0.03646695282724169 / 1.258394133734146 | [NPY](tensors/0000844.npy) |
| 845 | `model.layers.0.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5 / 42.75 / 0.03646695282724169 / 1.258394133734146 | [NPY](tensors/0000845.npy) |
| 846 | `model.layers.0.self_attn` | 7 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0027282453530723867 / 0.029530825060507953 | [NPY](tensors/0000846.npy) |
| 847 | `model.layers.0.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 45.0 / 0.06152243614196777 / 3.2004180556805095 | [NPY](tensors/0000847.npy) |
| 848 | `model.layers.0.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.3125 / 2.046875 / 0.0074341098467508955 / 0.3237872546847889 | [NPY](tensors/0000848.npy) |
| 849 | `model.layers.0.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.3125 / 2.046875 / 0.0074341098467508955 / 0.3237872546847889 | [NPY](tensors/0000849.npy) |
| 850 | `model.layers.0.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.3125 / 2.046875 / 0.0074341098467508955 / 0.3237872546847889 | [NPY](tensors/0000850.npy) |
| 851 | `model.layers.0.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 852 | `model.layers.0.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 853 | `model.layers.0.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 854 | `model.layers.0.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.03125 / 26.25 / 0.024777839539779557 / 0.7799712298067293 | [NPY](tensors/0000854.npy) |
| 855 | `model.layers.0.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.03125 / 26.25 / 0.024777839539779557 / 0.7799712298067293 | [NPY](tensors/0000855.npy) |
| 856 | `model.layers.0.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.296875 / 1.6328125 / -0.13964462280273438 / 0.8215715694024243 | [NPY](tensors/0000856.npy) |
| 857 | `model.layers.0` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 71.0 / 0.08645990689595541 / 3.57130297671818 | [NPY](tensors/0000857.npy) |
| 936 | `model.layers.0` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 33.25 / -0.00010735144217809042 / 2.523605988577484 | [NPY](tensors/0000936.npy) |
| 937 | `model.layers.0` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000937.npy) |
| 938 | `model.layers.0` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0000938.npy) |
| 939 | `model.layers.0` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0000939.npy) |
| 940 | `model.layers.0` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0000940.npy) |
| 941 | `model.layers.0` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 942 | `model.layers.0` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 943 | `model.layers.0` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 944 | `model.layers.0.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 33.25 / -0.00010735144217809042 / 2.523605988577484 | [NPY](tensors/0000944.npy) |
| 945 | `model.layers.0.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.125 / 9.3125 / 0.0025687262415885924 / 0.7612925106543675 | [NPY](tensors/0000945.npy) |
| 946 | `model.layers.0.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.125 / 9.3125 / 0.0025687262415885924 / 0.7612925106543675 | [NPY](tensors/0000946.npy) |
| 947 | `model.layers.0.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000947.npy) |
| 948 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0000948.npy) |
| 949 | `model.layers.0.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 950 | `model.layers.0.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 951 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0000951.npy) |
| 952 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0000952.npy) |
| 953 | `model.layers.0.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 954 | `model.layers.0.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.125 / 9.3125 / 0.0025687262415885924 / 0.7612925106543675 | [NPY](tensors/0000954.npy) |
| 955 | `model.layers.0.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.03125 / 9.125 / 0.002232139930129051 / 0.9922704412933107 | [NPY](tensors/0000955.npy) |
| 956 | `model.layers.0.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.125 / 9.3125 / 0.0025687262415885924 / 0.7612925106543675 | [NPY](tensors/0000956.npy) |
| 957 | `model.layers.0.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.0 / 43.25 / 0.006416738033294678 / 5.075484743629722 | [NPY](tensors/0000957.npy) |
| 958 | `model.layers.0.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.125 / 9.3125 / 0.0025687262415885924 / 0.7612925106543675 | [NPY](tensors/0000958.npy) |
| 959 | `model.layers.0.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.125 / 5.84375 / -0.09414148330688477 / 1.346493210012572 | [NPY](tensors/0000959.npy) |
| 960 | `model.layers.0.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.3125 / 5.6875 / -0.018865563988583745 / 0.48776581306216915 | [NPY](tensors/0000960.npy) |
| 961 | `model.layers.0.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.375 / 48.75 / 0.029439995975957978 / 1.5015177594897642 | [NPY](tensors/0000961.npy) |
| 962 | `model.layers.0.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.375 / 48.75 / 0.029439995975957978 / 1.5015177594897642 | [NPY](tensors/0000962.npy) |
| 963 | `model.layers.0.self_attn` | 8 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9765625 / 0.0024578816021090825 / 0.031187112254550585 | [NPY](tensors/0000963.npy) |
| 964 | `model.layers.0.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -60.0 / 50.0 / 0.02924318313598633 / 3.06166497697477 | [NPY](tensors/0000964.npy) |
| 965 | `model.layers.0.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9921875 / 1.6796875 / 0.006831784380806817 / 0.3419121922065125 | [NPY](tensors/0000965.npy) |
| 966 | `model.layers.0.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9921875 / 1.6796875 / 0.006831784380806817 / 0.3419121922065125 | [NPY](tensors/0000966.npy) |
| 967 | `model.layers.0.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.9921875 / 1.6796875 / 0.006831784380806817 / 0.3419121922065125 | [NPY](tensors/0000967.npy) |
| 968 | `model.layers.0.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 969 | `model.layers.0.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 970 | `model.layers.0.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 971 | `model.layers.0.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -19.25 / 26.125 / 0.019034819056590397 / 0.8591261609003324 | [NPY](tensors/0000971.npy) |
| 972 | `model.layers.0.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.25 / 26.125 / 0.019034819056590397 / 0.8591261609003324 | [NPY](tensors/0000972.npy) |
| 973 | `model.layers.0.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.484375 / 1.3515625 / -0.1159205436706543 / 0.5540636549777094 | [NPY](tensors/0000973.npy) |
| 974 | `model.layers.0` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -79.0 / 76.0 / 0.048375611835055884 / 3.6614364286910823 | [NPY](tensors/0000974.npy) |
| 1053 | `model.layers.0` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 89.0 / 0.026544343266222212 / 4.541275344485995 | [NPY](tensors/0001053.npy) |
| 1054 | `model.layers.0` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001054.npy) |
| 1055 | `model.layers.0` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0001055.npy) |
| 1056 | `model.layers.0` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0001056.npy) |
| 1057 | `model.layers.0` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0001057.npy) |
| 1058 | `model.layers.0` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1059 | `model.layers.0` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1060 | `model.layers.0` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1061 | `model.layers.0.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 89.0 / 0.026544343266222212 / 4.541275344485995 | [NPY](tensors/0001061.npy) |
| 1062 | `model.layers.0.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0001062.npy) |
| 1063 | `model.layers.0.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0001063.npy) |
| 1064 | `model.layers.0.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001064.npy) |
| 1065 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0001065.npy) |
| 1066 | `model.layers.0.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1067 | `model.layers.0.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1068 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0001068.npy) |
| 1069 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0001069.npy) |
| 1070 | `model.layers.0.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1071 | `model.layers.0.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0001071.npy) |
| 1072 | `model.layers.0.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.875 / 7.84375 / 0.015290047216694802 / 0.914624676971129 | [NPY](tensors/0001072.npy) |
| 1073 | `model.layers.0.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0001073.npy) |
| 1074 | `model.layers.0.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.25 / 34.5 / -0.11417865753173828 / 4.434976879466014 | [NPY](tensors/0001074.npy) |
| 1075 | `model.layers.0.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0001075.npy) |
| 1076 | `model.layers.0.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.03125 / 4.8125 / -0.07233588397502899 / 1.0561324517062678 | [NPY](tensors/0001076.npy) |
| 1077 | `model.layers.0.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.875 / 4.375 / -0.03969653690000996 / 0.7433280530189555 | [NPY](tensors/0001077.npy) |
| 1078 | `model.layers.0.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.5 / 38.0 / 0.02264210648006863 / 1.3273994639390105 | [NPY](tensors/0001078.npy) |
| 1079 | `model.layers.0.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.5 / 38.0 / 0.02264210648006863 / 1.3273994639390105 | [NPY](tensors/0001079.npy) |
| 1080 | `model.layers.0.self_attn` | 9 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004242814425150409 / 0.046187654371144096 | [NPY](tensors/0001080.npy) |
| 1081 | `model.layers.0.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.5 / 70.5 / 0.049183636241488984 / 4.132915036244379 | [NPY](tensors/0001081.npy) |
| 1082 | `model.layers.0.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0 / 2.125 / -0.0003084606594509549 / 0.26950863897328226 | [NPY](tensors/0001082.npy) |
| 1083 | `model.layers.0.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0 / 2.125 / -0.0003084606594509549 / 0.26950863897328226 | [NPY](tensors/0001083.npy) |
| 1084 | `model.layers.0.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.0 / 2.125 / -0.0003084606594509549 / 0.26950863897328226 | [NPY](tensors/0001084.npy) |
| 1085 | `model.layers.0.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1086 | `model.layers.0.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1087 | `model.layers.0.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1088 | `model.layers.0.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -30.0 / 30.75 / 0.033131406795130006 / 1.3424740457327187 | [NPY](tensors/0001088.npy) |
| 1089 | `model.layers.0.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.0 / 30.75 / 0.033131406795130006 / 1.3424740457327187 | [NPY](tensors/0001089.npy) |
| 1090 | `model.layers.0.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.765625 / 2.890625 / -0.1683502197265625 / 0.8609623790681838 | [NPY](tensors/0001090.npy) |
| 1091 | `model.layers.0` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 72.0 / 0.08222315046522352 / 3.8593962467038363 | [NPY](tensors/0001091.npy) |
| 1170 | `model.layers.0` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.625 / 47.5 / 0.005106970005565219 / 2.6215914903750863 | [NPY](tensors/0001170.npy) |
| 1171 | `model.layers.0` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001171.npy) |
| 1172 | `model.layers.0` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0001172.npy) |
| 1173 | `model.layers.0` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0001173.npy) |
| 1174 | `model.layers.0` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0001174.npy) |
| 1175 | `model.layers.0` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1176 | `model.layers.0` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1177 | `model.layers.0` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1178 | `model.layers.0.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.625 / 47.5 / 0.005106970005565219 / 2.6215914903750863 | [NPY](tensors/0001178.npy) |
| 1179 | `model.layers.0.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 14.125 / 0.0005866729550891452 / 0.7554183234523332 | [NPY](tensors/0001179.npy) |
| 1180 | `model.layers.0.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 14.125 / 0.0005866729550891452 / 0.7554183234523332 | [NPY](tensors/0001180.npy) |
| 1181 | `model.layers.0.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001181.npy) |
| 1182 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0001182.npy) |
| 1183 | `model.layers.0.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1184 | `model.layers.0.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1185 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0001185.npy) |
| 1186 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0001186.npy) |
| 1187 | `model.layers.0.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1188 | `model.layers.0.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 14.125 / 0.0005866729550891452 / 0.7554183234523332 | [NPY](tensors/0001188.npy) |
| 1189 | `model.layers.0.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.21875 / 11.25 / 0.010708235728088766 / 1.060515732660661 | [NPY](tensors/0001189.npy) |
| 1190 | `model.layers.0.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 14.125 / 0.0005866729550891452 / 0.7554183234523332 | [NPY](tensors/0001190.npy) |
| 1191 | `model.layers.0.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -58.75 / 50.25 / -0.06230086088180542 / 6.016812680413199 | [NPY](tensors/0001191.npy) |
| 1192 | `model.layers.0.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 14.125 / 0.0005866729550891452 / 0.7554183234523332 | [NPY](tensors/0001192.npy) |
| 1193 | `model.layers.0.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.65625 / 5.46875 / -0.0845739059150219 / 1.4068414576152921 | [NPY](tensors/0001193.npy) |
| 1194 | `model.layers.0.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.21875 / 4.21875 / -0.026666834659408778 / 0.5762536107102212 | [NPY](tensors/0001194.npy) |
| 1195 | `model.layers.0.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.875 / 44.5 / 0.031938090009821785 / 1.3385382775782682 | [NPY](tensors/0001195.npy) |
| 1196 | `model.layers.0.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.875 / 44.5 / 0.031938090009821785 / 1.3385382775782682 | [NPY](tensors/0001196.npy) |
| 1197 | `model.layers.0.self_attn` | 10 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0034666664587482314 / 0.038128753371809834 | [NPY](tensors/0001197.npy) |
| 1198 | `model.layers.0.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 47.25 / 0.0368962287902832 / 3.0411125273503865 | [NPY](tensors/0001198.npy) |
| 1199 | `model.layers.0.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.203125 / 2.5 / -0.002200341886944241 / 0.3266438300992516 | [NPY](tensors/0001199.npy) |
| 1200 | `model.layers.0.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.203125 / 2.5 / -0.002200341886944241 / 0.3266438300992516 | [NPY](tensors/0001200.npy) |
| 1201 | `model.layers.0.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.203125 / 2.5 / -0.002200341886944241 / 0.3266438300992516 | [NPY](tensors/0001201.npy) |
| 1202 | `model.layers.0.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1203 | `model.layers.0.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1204 | `model.layers.0.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1205 | `model.layers.0.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.125 / 24.125 / 0.0251141670677397 / 0.7359608037929202 | [NPY](tensors/0001205.npy) |
| 1206 | `model.layers.0.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.125 / 24.125 / 0.0251141670677397 / 0.7359608037929202 | [NPY](tensors/0001206.npy) |
| 1207 | `model.layers.0.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.546875 / 1.34375 / -0.15941619873046875 / 0.6916964010611172 | [NPY](tensors/0001207.npy) |
| 1208 | `model.layers.0` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 71.5 / 0.06199039883083767 / 3.396404684964956 | [NPY](tensors/0001208.npy) |
| 1287 | `model.layers.0` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001287.npy) |
| 1288 | `model.layers.0` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001288.npy) |
| 1289 | `model.layers.0` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0001289.npy) |
| 1290 | `model.layers.0` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0001290.npy) |
| 1291 | `model.layers.0` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0001291.npy) |
| 1292 | `model.layers.0` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1293 | `model.layers.0` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1294 | `model.layers.0` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1295 | `model.layers.0.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001295.npy) |
| 1296 | `model.layers.0.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001296.npy) |
| 1297 | `model.layers.0.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001297.npy) |
| 1298 | `model.layers.0.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001298.npy) |
| 1299 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0001299.npy) |
| 1300 | `model.layers.0.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1301 | `model.layers.0.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1302 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0001302.npy) |
| 1303 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0001303.npy) |
| 1304 | `model.layers.0.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1305 | `model.layers.0.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001305.npy) |
| 1306 | `model.layers.0.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.84375 / 8.5625 / 0.0153301190584898 / 1.0113524420299036 | [NPY](tensors/0001306.npy) |
| 1307 | `model.layers.0.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001307.npy) |
| 1308 | `model.layers.0.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.0 / 65.5 / 0.032654017210006714 / 6.89507515667232 | [NPY](tensors/0001308.npy) |
| 1309 | `model.layers.0.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001309.npy) |
| 1310 | `model.layers.0.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.28125 / 3.390625 / -0.002120666205883026 / 0.8566653376613583 | [NPY](tensors/0001310.npy) |
| 1311 | `model.layers.0.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.1875 / 3.390625 / -0.0022074446587794228 / 0.4773790409275267 | [NPY](tensors/0001311.npy) |
| 1312 | `model.layers.0.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.5 / 29.5 / 0.02722140004237493 / 0.9969757994350864 | [NPY](tensors/0001312.npy) |
| 1313 | `model.layers.0.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.5 / 29.5 / 0.02722140004237493 / 0.9969757994350864 | [NPY](tensors/0001313.npy) |
| 1314 | `model.layers.0.self_attn` | 11 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003079303131349984 / 0.030888044314343995 | [NPY](tensors/0001314.npy) |
| 1315 | `model.layers.0.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.125 / 32.75 / 0.025291397836473252 / 2.9888811379744724 | [NPY](tensors/0001315.npy) |
| 1316 | `model.layers.0.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.3984375 / -0.002899119589063856 / 0.2919847649025277 | [NPY](tensors/0001316.npy) |
| 1317 | `model.layers.0.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.3984375 / -0.002899119589063856 / 0.2919847649025277 | [NPY](tensors/0001317.npy) |
| 1318 | `model.layers.0.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.3984375 / -0.002899119589063856 / 0.2919847649025277 | [NPY](tensors/0001318.npy) |
| 1319 | `model.layers.0.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1320 | `model.layers.0.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1321 | `model.layers.0.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1322 | `model.layers.0.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.75 / 16.625 / 0.02217928957866712 / 0.7275589090515336 | [NPY](tensors/0001322.npy) |
| 1323 | `model.layers.0.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.75 / 16.625 / 0.02217928957866712 / 0.7275589090515336 | [NPY](tensors/0001323.npy) |
| 1324 | `model.layers.0.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.984375 / 2.828125 / -0.03392791748046875 / 1.4394484452392498 | [NPY](tensors/0001324.npy) |
| 1325 | `model.layers.0` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.375 / 49.5 / 0.047446685367160374 / 2.9964810788701626 | [NPY](tensors/0001325.npy) |
| 1404 | `model.layers.0` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 49.25 / -0.03481262918147776 / 3.3040972398817177 | [NPY](tensors/0001404.npy) |
| 1405 | `model.layers.0` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001405.npy) |
| 1406 | `model.layers.0` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0001406.npy) |
| 1407 | `model.layers.0` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0001407.npy) |
| 1408 | `model.layers.0` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0001408.npy) |
| 1409 | `model.layers.0` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1410 | `model.layers.0` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1411 | `model.layers.0` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1412 | `model.layers.0.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 49.25 / -0.03481262918147776 / 3.3040972398817177 | [NPY](tensors/0001412.npy) |
| 1413 | `model.layers.0.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001413.npy) |
| 1414 | `model.layers.0.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001414.npy) |
| 1415 | `model.layers.0.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001415.npy) |
| 1416 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0001416.npy) |
| 1417 | `model.layers.0.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1418 | `model.layers.0.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1419 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0001419.npy) |
| 1420 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0001420.npy) |
| 1421 | `model.layers.0.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1422 | `model.layers.0.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001422.npy) |
| 1423 | `model.layers.0.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 6.25 / 0.025897369312588125 / 0.9110042125091211 | [NPY](tensors/0001423.npy) |
| 1424 | `model.layers.0.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001424.npy) |
| 1425 | `model.layers.0.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.75 / 46.25 / 0.08283017575740814 / 5.101942263816244 | [NPY](tensors/0001425.npy) |
| 1426 | `model.layers.0.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001426.npy) |
| 1427 | `model.layers.0.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.765625 / 3.28125 / 0.0731726735830307 / 0.9884409409989561 | [NPY](tensors/0001427.npy) |
| 1428 | `model.layers.0.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.125 / 2.875 / 0.0035866202881607023 / 0.44377185496543475 | [NPY](tensors/0001428.npy) |
| 1429 | `model.layers.0.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.84375 / 36.0 / 0.030840444399250877 / 1.0648759231925602 | [NPY](tensors/0001429.npy) |
| 1430 | `model.layers.0.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.84375 / 36.0 / 0.030840444399250877 / 1.0648759231925602 | [NPY](tensors/0001430.npy) |
| 1431 | `model.layers.0.self_attn` | 12 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0033121949075832994 / 0.03333152629991977 | [NPY](tensors/0001431.npy) |
| 1432 | `model.layers.0.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 49.0 / -0.004030725691053602 / 3.390073857404087 | [NPY](tensors/0001432.npy) |
| 1433 | `model.layers.0.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 2.015625 / -0.0031744619210561115 / 0.2930595884081759 | [NPY](tensors/0001433.npy) |
| 1434 | `model.layers.0.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 2.015625 / -0.0031744619210561115 / 0.2930595884081759 | [NPY](tensors/0001434.npy) |
| 1435 | `model.layers.0.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.09375 / 2.015625 / -0.0031744619210561115 / 0.2930595884081759 | [NPY](tensors/0001435.npy) |
| 1436 | `model.layers.0.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1437 | `model.layers.0.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1438 | `model.layers.0.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1439 | `model.layers.0.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.65625 / 19.75 / 0.029970933496952058 / 0.6509264260178661 | [NPY](tensors/0001439.npy) |
| 1440 | `model.layers.0.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.65625 / 19.75 / 0.029970933496952058 / 0.6509264260178661 | [NPY](tensors/0001440.npy) |
| 1441 | `model.layers.0.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.46875 / 1.6015625 / -0.06350994110107422 / 0.8760599719187877 | [NPY](tensors/0001441.npy) |
| 1442 | `model.layers.0` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 48.75 / 0.025962818993462457 / 3.438249487474792 | [NPY](tensors/0001442.npy) |
| 1521 | `model.layers.0` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 23.0 / -0.06670066184467739 / 2.312253441767413 | [NPY](tensors/0001521.npy) |
| 1522 | `model.layers.0` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001522.npy) |
| 1523 | `model.layers.0` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0001523.npy) |
| 1524 | `model.layers.0` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0001524.npy) |
| 1525 | `model.layers.0` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0001525.npy) |
| 1526 | `model.layers.0` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1527 | `model.layers.0` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1528 | `model.layers.0` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1529 | `model.layers.0.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 23.0 / -0.06670066184467739 / 2.312253441767413 | [NPY](tensors/0001529.npy) |
| 1530 | `model.layers.0.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.8125 / 5.59375 / -0.020342383119795058 / 0.704412340044763 | [NPY](tensors/0001530.npy) |
| 1531 | `model.layers.0.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.8125 / 5.59375 / -0.020342383119795058 / 0.704412340044763 | [NPY](tensors/0001531.npy) |
| 1532 | `model.layers.0.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001532.npy) |
| 1533 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0001533.npy) |
| 1534 | `model.layers.0.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1535 | `model.layers.0.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1536 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0001536.npy) |
| 1537 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0001537.npy) |
| 1538 | `model.layers.0.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1539 | `model.layers.0.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.8125 / 5.59375 / -0.020342383119795058 / 0.704412340044763 | [NPY](tensors/0001539.npy) |
| 1540 | `model.layers.0.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 9.4375 / 0.047403842909261584 / 1.0481627444526902 | [NPY](tensors/0001540.npy) |
| 1541 | `model.layers.0.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.8125 / 5.59375 / -0.020342383119795058 / 0.704412340044763 | [NPY](tensors/0001541.npy) |
| 1542 | `model.layers.0.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.5 / 52.75 / 0.1424560248851776 / 5.693084799587338 | [NPY](tensors/0001542.npy) |
| 1543 | `model.layers.0.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.8125 / 5.59375 / -0.020342383119795058 / 0.704412340044763 | [NPY](tensors/0001543.npy) |
| 1544 | `model.layers.0.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.9375 / 4.59375 / 0.0357738733291626 / 1.29216792750665 | [NPY](tensors/0001544.npy) |
| 1545 | `model.layers.0.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.09375 / 3.078125 / 0.030558040583855473 / 0.5312084766104387 | [NPY](tensors/0001545.npy) |
| 1546 | `model.layers.0.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5 / 39.0 / 0.041854896603359115 / 1.2117566932664863 | [NPY](tensors/0001546.npy) |
| 1547 | `model.layers.0.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5 / 39.0 / 0.041854896603359115 / 1.2117566932664863 | [NPY](tensors/0001547.npy) |
| 1548 | `model.layers.0.self_attn` | 13 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003552903424880673 / 0.04199100195717139 | [NPY](tensors/0001548.npy) |
| 1549 | `model.layers.0.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 41.5 / -0.024747308095296225 / 2.6144411451120417 | [NPY](tensors/0001549.npy) |
| 1550 | `model.layers.0.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 1.703125 / -0.0021214710341559517 / 0.3344338050900628 | [NPY](tensors/0001550.npy) |
| 1551 | `model.layers.0.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 1.703125 / -0.0021214710341559517 / 0.3344338050900628 | [NPY](tensors/0001551.npy) |
| 1552 | `model.layers.0.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.8125 / 1.703125 / -0.0021214710341559517 / 0.3344338050900628 | [NPY](tensors/0001552.npy) |
| 1553 | `model.layers.0.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1554 | `model.layers.0.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1555 | `model.layers.0.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1556 | `model.layers.0.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.28125 / 34.25 / 0.030976316125856506 / 1.2353424595704119 | [NPY](tensors/0001556.npy) |
| 1557 | `model.layers.0.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.28125 / 34.25 / 0.030976316125856506 / 1.2353424595704119 | [NPY](tensors/0001557.npy) |
| 1558 | `model.layers.0.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.078125 / 1.9453125 / -0.05228233337402344 / 1.0452363413220325 | [NPY](tensors/0001558.npy) |
| 1559 | `model.layers.0` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 74.0 / 0.006294896867540148 / 3.3245140998135576 | [NPY](tensors/0001559.npy) |
| 1638 | `model.layers.0` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.0 / 44.25 / -0.05639152005314827 / 3.20644216139137 | [NPY](tensors/0001638.npy) |
| 1639 | `model.layers.0` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001639.npy) |
| 1640 | `model.layers.0` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0001640.npy) |
| 1641 | `model.layers.0` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0001641.npy) |
| 1642 | `model.layers.0` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0001642.npy) |
| 1643 | `model.layers.0` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1644 | `model.layers.0` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1645 | `model.layers.0` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1646 | `model.layers.0.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.0 / 44.25 / -0.05639152005314827 / 3.20644216139137 | [NPY](tensors/0001646.npy) |
| 1647 | `model.layers.0.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.1875 / 7.46875 / -0.013263263139459821 / 0.6714411594858319 | [NPY](tensors/0001647.npy) |
| 1648 | `model.layers.0.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.1875 / 7.46875 / -0.013263263139459821 / 0.6714411594858319 | [NPY](tensors/0001648.npy) |
| 1649 | `model.layers.0.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001649.npy) |
| 1650 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0001650.npy) |
| 1651 | `model.layers.0.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1652 | `model.layers.0.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1653 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0001653.npy) |
| 1654 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0001654.npy) |
| 1655 | `model.layers.0.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1656 | `model.layers.0.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.1875 / 7.46875 / -0.013263263139459821 / 0.6714411594858319 | [NPY](tensors/0001656.npy) |
| 1657 | `model.layers.0.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0 / 8.0625 / 0.007593905087560415 / 0.9356202666603853 | [NPY](tensors/0001657.npy) |
| 1658 | `model.layers.0.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.1875 / 7.46875 / -0.013263263139459821 / 0.6714411594858319 | [NPY](tensors/0001658.npy) |
| 1659 | `model.layers.0.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.5 / 54.25 / -0.0055768489837646484 / 5.816745508909234 | [NPY](tensors/0001659.npy) |
| 1660 | `model.layers.0.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.1875 / 7.46875 / -0.013263263139459821 / 0.6714411594858319 | [NPY](tensors/0001660.npy) |
| 1661 | `model.layers.0.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -2.890625 / 3.5 / 0.058073386549949646 / 0.8870191240100074 | [NPY](tensors/0001661.npy) |
| 1662 | `model.layers.0.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.5 / 4.40625 / 0.011771371373470174 / 0.623967411597386 | [NPY](tensors/0001662.npy) |
| 1663 | `model.layers.0.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.6875 / 41.5 / 0.041643866399923964 / 1.278701414145709 | [NPY](tensors/0001663.npy) |
| 1664 | `model.layers.0.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.6875 / 41.5 / 0.041643866399923964 / 1.278701414145709 | [NPY](tensors/0001664.npy) |
| 1665 | `model.layers.0.self_attn` | 14 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003219215982775263 / 0.03560073537879268 | [NPY](tensors/0001665.npy) |
| 1666 | `model.layers.0.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 39.75 / -0.014815356996324327 / 3.0642252802989645 | [NPY](tensors/0001666.npy) |
| 1667 | `model.layers.0.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.234375 / 2.09375 / -0.004642265372806125 / 0.28337115783255856 | [NPY](tensors/0001667.npy) |
| 1668 | `model.layers.0.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.234375 / 2.09375 / -0.004642265372806125 / 0.28337115783255856 | [NPY](tensors/0001668.npy) |
| 1669 | `model.layers.0.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.234375 / 2.09375 / -0.004642265372806125 / 0.28337115783255856 | [NPY](tensors/0001669.npy) |
| 1670 | `model.layers.0.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1671 | `model.layers.0.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1672 | `model.layers.0.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1673 | `model.layers.0.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -10.125 / 31.625 / 0.03623481525315179 / 1.0234820320339837 | [NPY](tensors/0001673.npy) |
| 1674 | `model.layers.0.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 31.625 / 0.03623481525315179 / 1.0234820320339837 | [NPY](tensors/0001674.npy) |
| 1675 | `model.layers.0.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.25 / 2.09375 / -0.07812118530273438 / 0.9887151794963037 | [NPY](tensors/0001675.npy) |
| 1676 | `model.layers.0` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 61.5 / 0.021569686465793186 / 3.2085741697009307 | [NPY](tensors/0001676.npy) |
| 1755 | `model.layers.0` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.75 / 32.0 / 0.02612974349823263 / 2.3052590463349314 | [NPY](tensors/0001755.npy) |
| 1756 | `model.layers.0` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001756.npy) |
| 1757 | `model.layers.0` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0001757.npy) |
| 1758 | `model.layers.0` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0001758.npy) |
| 1759 | `model.layers.0` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0001759.npy) |
| 1760 | `model.layers.0` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1761 | `model.layers.0` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1762 | `model.layers.0` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1763 | `model.layers.0.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.75 / 32.0 / 0.02612974349823263 / 2.3052590463349314 | [NPY](tensors/0001763.npy) |
| 1764 | `model.layers.0.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0001764.npy) |
| 1765 | `model.layers.0.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0001765.npy) |
| 1766 | `model.layers.0.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001766.npy) |
| 1767 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0001767.npy) |
| 1768 | `model.layers.0.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1769 | `model.layers.0.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1770 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0001770.npy) |
| 1771 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0001771.npy) |
| 1772 | `model.layers.0.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1773 | `model.layers.0.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0001773.npy) |
| 1774 | `model.layers.0.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.375 / 10.0625 / -0.0011312136193737388 / 1.2762524673806912 | [NPY](tensors/0001774.npy) |
| 1775 | `model.layers.0.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0001775.npy) |
| 1776 | `model.layers.0.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.5 / 51.25 / 0.02611599490046501 / 5.9708322691785325 | [NPY](tensors/0001776.npy) |
| 1777 | `model.layers.0.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0001777.npy) |
| 1778 | `model.layers.0.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / 0.016116023063659668 / 1.5717161949904705 | [NPY](tensors/0001778.npy) |
| 1779 | `model.layers.0.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.0 / 3.140625 / -0.006344530236674473 / 0.43310069653119915 | [NPY](tensors/0001779.npy) |
| 1780 | `model.layers.0.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.75 / 41.0 / 0.01436940510239866 / 1.256544902070688 | [NPY](tensors/0001780.npy) |
| 1781 | `model.layers.0.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.75 / 41.0 / 0.01436940510239866 / 1.256544902070688 | [NPY](tensors/0001781.npy) |
| 1782 | `model.layers.0.self_attn` | 15 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0026026702697701572 / 0.035841075111788474 | [NPY](tensors/0001782.npy) |
| 1783 | `model.layers.0.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.5 / 43.75 / 0.040428574879964194 / 2.737762257774649 | [NPY](tensors/0001783.npy) |
| 1784 | `model.layers.0.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.640625 / 1.546875 / 0.004711990886264377 / 0.35223652000863015 | [NPY](tensors/0001784.npy) |
| 1785 | `model.layers.0.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.640625 / 1.546875 / 0.004711990886264377 / 0.35223652000863015 | [NPY](tensors/0001785.npy) |
| 1786 | `model.layers.0.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.640625 / 1.546875 / 0.004711990886264377 / 0.35223652000863015 | [NPY](tensors/0001786.npy) |
| 1787 | `model.layers.0.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1788 | `model.layers.0.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1789 | `model.layers.0.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1790 | `model.layers.0.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.125 / 27.125 / 0.026367776178651384 / 1.0006696555295773 | [NPY](tensors/0001790.npy) |
| 1791 | `model.layers.0.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.125 / 27.125 / 0.026367776178651384 / 1.0006696555295773 | [NPY](tensors/0001791.npy) |
| 1792 | `model.layers.0.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.7578125 / 2.75 / -0.274322509765625 / 1.1130689280472563 | [NPY](tensors/0001792.npy) |
| 1793 | `model.layers.0` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -60.25 / 71.0 / 0.06667259799109565 / 3.3131680140839204 | [NPY](tensors/0001793.npy) |
| 1872 | `model.layers.0` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 38.75 / -0.019637677404615615 / 2.869533421530457 | [NPY](tensors/0001872.npy) |
| 1873 | `model.layers.0` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001873.npy) |
| 1874 | `model.layers.0` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0001874.npy) |
| 1875 | `model.layers.0` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0001875.npy) |
| 1876 | `model.layers.0` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0001876.npy) |
| 1877 | `model.layers.0` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1878 | `model.layers.0` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1879 | `model.layers.0` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1880 | `model.layers.0.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 38.75 / -0.019637677404615615 / 2.869533421530457 | [NPY](tensors/0001880.npy) |
| 1881 | `model.layers.0.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0001881.npy) |
| 1882 | `model.layers.0.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0001882.npy) |
| 1883 | `model.layers.0.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001883.npy) |
| 1884 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0001884.npy) |
| 1885 | `model.layers.0.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1886 | `model.layers.0.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1887 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0001887.npy) |
| 1888 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0001888.npy) |
| 1889 | `model.layers.0.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1890 | `model.layers.0.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0001890.npy) |
| 1891 | `model.layers.0.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0 / 9.4375 / 0.009774616220965981 / 1.008080585961609 | [NPY](tensors/0001891.npy) |
| 1892 | `model.layers.0.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0001892.npy) |
| 1893 | `model.layers.0.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.5 / 52.0 / -0.04840673506259918 / 6.119228313490181 | [NPY](tensors/0001893.npy) |
| 1894 | `model.layers.0.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0001894.npy) |
| 1895 | `model.layers.0.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.34375 / 3.625 / -0.03821904957294464 / 0.9543836895451787 | [NPY](tensors/0001895.npy) |
| 1896 | `model.layers.0.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.125 / 4.34375 / 0.00851356858811414 / 0.5393030027298731 | [NPY](tensors/0001896.npy) |
| 1897 | `model.layers.0.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.6875 / 32.0 / 0.03533158600330353 / 1.0285062318329692 | [NPY](tensors/0001897.npy) |
| 1898 | `model.layers.0.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.6875 / 32.0 / 0.03533158600330353 / 1.0285062318329692 | [NPY](tensors/0001898.npy) |
| 1899 | `model.layers.0.self_attn` | 16 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003094246358820787 / 0.032006485657569174 | [NPY](tensors/0001899.npy) |
| 1900 | `model.layers.0.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 39.0 / 0.01547790633307563 / 2.834312745770847 | [NPY](tensors/0001900.npy) |
| 1901 | `model.layers.0.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.4375 / 2.078125 / -0.0026524947749243842 / 0.29211574106516064 | [NPY](tensors/0001901.npy) |
| 1902 | `model.layers.0.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.4375 / 2.078125 / -0.0026524947749243842 / 0.29211574106516064 | [NPY](tensors/0001902.npy) |
| 1903 | `model.layers.0.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.4375 / 2.078125 / -0.0026524947749243842 / 0.29211574106516064 | [NPY](tensors/0001903.npy) |
| 1904 | `model.layers.0.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1905 | `model.layers.0.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1906 | `model.layers.0.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1907 | `model.layers.0.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -12.9375 / 21.875 / 0.020777117543750338 / 0.9342717413094238 | [NPY](tensors/0001907.npy) |
| 1908 | `model.layers.0.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.9375 / 21.875 / 0.020777117543750338 / 0.9342717413094238 | [NPY](tensors/0001908.npy) |
| 1909 | `model.layers.0.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.78125 / 1.8125 / -0.03012847900390625 / 1.1743664686977981 | [NPY](tensors/0001909.npy) |
| 1910 | `model.layers.0` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 51.5 / 0.036257399453057185 / 3.0342316368272524 | [NPY](tensors/0001910.npy) |
| 1989 | `model.layers.0` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 25.0 / 0.01804563016113308 / 2.3323165527333782 | [NPY](tensors/0001989.npy) |
| 1990 | `model.layers.0` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001990.npy) |
| 1991 | `model.layers.0` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0001991.npy) |
| 1992 | `model.layers.0` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0001992.npy) |
| 1993 | `model.layers.0` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0001993.npy) |
| 1994 | `model.layers.0` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1995 | `model.layers.0` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1996 | `model.layers.0` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1997 | `model.layers.0.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 25.0 / 0.01804563016113308 / 2.3323165527333782 | [NPY](tensors/0001997.npy) |
| 1998 | `model.layers.0.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0001998.npy) |
| 1999 | `model.layers.0.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0001999.npy) |
| 2000 | `model.layers.0.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002000.npy) |
| 2001 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0002001.npy) |
| 2002 | `model.layers.0.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2003 | `model.layers.0.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2004 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0002004.npy) |
| 2005 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0002005.npy) |
| 2006 | `model.layers.0.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2007 | `model.layers.0.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0002007.npy) |
| 2008 | `model.layers.0.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 8.75 / 0.005578655982390046 / 1.1564340991725837 | [NPY](tensors/0002008.npy) |
| 2009 | `model.layers.0.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0002009.npy) |
| 2010 | `model.layers.0.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -56.25 / 41.75 / -0.16974663734436035 / 5.496621344446725 | [NPY](tensors/0002010.npy) |
| 2011 | `model.layers.0.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0002011.npy) |
| 2012 | `model.layers.0.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.6875 / 4.5 / 0.06943026185035706 / 1.339855997999367 | [NPY](tensors/0002012.npy) |
| 2013 | `model.layers.0.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.28125 / 4.375 / 0.00028455246501835063 / 0.5180289245376569 | [NPY](tensors/0002013.npy) |
| 2014 | `model.layers.0.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.375 / 42.0 / 0.021802772829929987 / 1.300635444183617 | [NPY](tensors/0002014.npy) |
| 2015 | `model.layers.0.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.375 / 42.0 / 0.021802772829929987 / 1.300635444183617 | [NPY](tensors/0002015.npy) |
| 2016 | `model.layers.0.self_attn` | 17 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0029579222875343297 / 0.03630511585359859 | [NPY](tensors/0002016.npy) |
| 2017 | `model.layers.0.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.0 / 47.5 / 0.03999474843343099 / 2.8411506892828404 | [NPY](tensors/0002017.npy) |
| 2018 | `model.layers.0.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0625 / 1.578125 / 0.003335588508182102 / 0.2944492787626355 | [NPY](tensors/0002018.npy) |
| 2019 | `model.layers.0.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0625 / 1.578125 / 0.003335588508182102 / 0.2944492787626355 | [NPY](tensors/0002019.npy) |
| 2020 | `model.layers.0.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.0625 / 1.578125 / 0.003335588508182102 / 0.2944492787626355 | [NPY](tensors/0002020.npy) |
| 2021 | `model.layers.0.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2022 | `model.layers.0.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2023 | `model.layers.0.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2024 | `model.layers.0.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.875 / 25.75 / 0.020715664285752507 / 0.8982506110018865 | [NPY](tensors/0002024.npy) |
| 2025 | `model.layers.0.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.875 / 25.75 / 0.020715664285752507 / 0.8982506110018865 | [NPY](tensors/0002025.npy) |
| 2026 | `model.layers.0.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.40625 / 1.9921875 / -0.15587615966796875 / 0.728914218258963 | [NPY](tensors/0002026.npy) |
| 2027 | `model.layers.0` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -56.5 / 71.0 / 0.06083253224690755 / 3.292076677124979 | [NPY](tensors/0002027.npy) |
| 2106 | `model.layers.0` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 32.5 / -0.010988011221504874 / 2.8100849975485342 | [NPY](tensors/0002106.npy) |
| 2107 | `model.layers.0` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002107.npy) |
| 2108 | `model.layers.0` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0002108.npy) |
| 2109 | `model.layers.0` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0002109.npy) |
| 2110 | `model.layers.0` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0002110.npy) |
| 2111 | `model.layers.0` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2112 | `model.layers.0` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2113 | `model.layers.0` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2114 | `model.layers.0.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 32.5 / -0.010988011221504874 / 2.8100849975485342 | [NPY](tensors/0002114.npy) |
| 2115 | `model.layers.0.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 9.4375 / -0.006889543920341465 / 0.7635197371874709 | [NPY](tensors/0002115.npy) |
| 2116 | `model.layers.0.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 9.4375 / -0.006889543920341465 / 0.7635197371874709 | [NPY](tensors/0002116.npy) |
| 2117 | `model.layers.0.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002117.npy) |
| 2118 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0002118.npy) |
| 2119 | `model.layers.0.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2120 | `model.layers.0.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2121 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0002121.npy) |
| 2122 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0002122.npy) |
| 2123 | `model.layers.0.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2124 | `model.layers.0.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 9.4375 / -0.006889543920341465 / 0.7635197371874709 | [NPY](tensors/0002124.npy) |
| 2125 | `model.layers.0.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5625 / 8.125 / 0.016898621805012226 / 1.0047983616456486 | [NPY](tensors/0002125.npy) |
| 2126 | `model.layers.0.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 9.4375 / -0.006889543920341465 / 0.7635197371874709 | [NPY](tensors/0002126.npy) |
| 2127 | `model.layers.0.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.0 / 58.25 / 0.02473968267440796 / 6.1681818782782605 | [NPY](tensors/0002127.npy) |
| 2128 | `model.layers.0.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 9.4375 / -0.006889543920341465 / 0.7635197371874709 | [NPY](tensors/0002128.npy) |
| 2129 | `model.layers.0.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.03125 / 3.515625 / -0.009867578744888306 / 0.9141301384289886 | [NPY](tensors/0002129.npy) |
| 2130 | `model.layers.0.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.25 / 3.5625 / 0.016748439039702134 / 0.5047135445420462 | [NPY](tensors/0002130.npy) |
| 2131 | `model.layers.0.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.5 / 35.0 / 0.032329250934223334 / 1.0231908458432155 | [NPY](tensors/0002131.npy) |
| 2132 | `model.layers.0.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.5 / 35.0 / 0.032329250934223334 / 1.0231908458432155 | [NPY](tensors/0002132.npy) |
| 2133 | `model.layers.0.self_attn` | 18 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.96484375 / 0.0028842561452166737 / 0.03086735488708723 | [NPY](tensors/0002133.npy) |
| 2134 | `model.layers.0.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 39.25 / 0.021283234490288627 / 2.967652744181512 | [NPY](tensors/0002134.npy) |
| 2135 | `model.layers.0.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.296875 / 2.203125 / 0.0015206495920817057 / 0.27718030841139657 | [NPY](tensors/0002135.npy) |
| 2136 | `model.layers.0.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.296875 / 2.203125 / 0.0015206495920817057 / 0.27718030841139657 | [NPY](tensors/0002136.npy) |
| 2137 | `model.layers.0.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.296875 / 2.203125 / 0.0015206495920817057 / 0.27718030841139657 | [NPY](tensors/0002137.npy) |
| 2138 | `model.layers.0.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2139 | `model.layers.0.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2140 | `model.layers.0.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2141 | `model.layers.0.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.671875 / 13.8125 / 0.02821919090218014 / 0.545333475134223 | [NPY](tensors/0002141.npy) |
| 2142 | `model.layers.0.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.671875 / 13.8125 / 0.02821919090218014 / 0.545333475134223 | [NPY](tensors/0002142.npy) |
| 2143 | `model.layers.0.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.40625 / 2.03125 / -0.05591583251953125 / 1.3156732412806973 | [NPY](tensors/0002143.npy) |
| 2144 | `model.layers.0` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.0 / 53.0 / 0.04934759669833713 / 2.9868052165620367 | [NPY](tensors/0002144.npy) |
| 2223 | `model.layers.0` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 32.75 / 0.03959848284721375 / 2.636727096419094 | [NPY](tensors/0002223.npy) |
| 2224 | `model.layers.0` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002224.npy) |
| 2225 | `model.layers.0` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0002225.npy) |
| 2226 | `model.layers.0` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0002226.npy) |
| 2227 | `model.layers.0` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0002227.npy) |
| 2228 | `model.layers.0` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2229 | `model.layers.0` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2230 | `model.layers.0` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2231 | `model.layers.0.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 32.75 / 0.03959848284721375 / 2.636727096419094 | [NPY](tensors/0002231.npy) |
| 2232 | `model.layers.0.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002232.npy) |
| 2233 | `model.layers.0.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002233.npy) |
| 2234 | `model.layers.0.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002234.npy) |
| 2235 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0002235.npy) |
| 2236 | `model.layers.0.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2237 | `model.layers.0.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2238 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0002238.npy) |
| 2239 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0002239.npy) |
| 2240 | `model.layers.0.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2241 | `model.layers.0.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002241.npy) |
| 2242 | `model.layers.0.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.0625 / 6.78125 / -0.006842018279712647 / 0.8517376388261615 | [NPY](tensors/0002242.npy) |
| 2243 | `model.layers.0.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002243.npy) |
| 2244 | `model.layers.0.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.25 / 35.75 / 0.051442623138427734 / 3.999531927842787 | [NPY](tensors/0002244.npy) |
| 2245 | `model.layers.0.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002245.npy) |
| 2246 | `model.layers.0.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 4.625 / 0.04163137078285217 / 1.1435466539669636 | [NPY](tensors/0002246.npy) |
| 2247 | `model.layers.0.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.0625 / 2.703125 / 0.0028175271218060516 / 0.40646585788684986 | [NPY](tensors/0002247.npy) |
| 2248 | `model.layers.0.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 44.25 / 0.03434218991961744 / 1.3111398795469011 | [NPY](tensors/0002248.npy) |
| 2249 | `model.layers.0.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 44.25 / 0.03434218991961744 / 1.3111398795469011 | [NPY](tensors/0002249.npy) |
| 2250 | `model.layers.0.self_attn` | 19 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9453125 / 0.0028352139505165544 / 0.028244721794518528 | [NPY](tensors/0002250.npy) |
| 2251 | `model.layers.0.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 43.5 / 0.07408773634168837 / 2.957029563449283 | [NPY](tensors/0002251.npy) |
| 2252 | `model.layers.0.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.25 / 1.703125 / -0.0005095627572801378 / 0.37122921170492695 | [NPY](tensors/0002252.npy) |
| 2253 | `model.layers.0.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.25 / 1.703125 / -0.0005095627572801378 / 0.37122921170492695 | [NPY](tensors/0002253.npy) |
| 2254 | `model.layers.0.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.25 / 1.703125 / -0.0005095627572801378 / 0.37122921170492695 | [NPY](tensors/0002254.npy) |
| 2255 | `model.layers.0.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2256 | `model.layers.0.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2257 | `model.layers.0.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2258 | `model.layers.0.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.75 / 22.625 / 0.03586874900178777 / 0.8632872860965066 | [NPY](tensors/0002258.npy) |
| 2259 | `model.layers.0.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.75 / 22.625 / 0.03586874900178777 / 0.8632872860965066 | [NPY](tensors/0002259.npy) |
| 2260 | `model.layers.0.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.609375 / 1.6328125 / -0.202392578125 / 0.772516080453046 | [NPY](tensors/0002260.npy) |
| 2261 | `model.layers.0` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 66.0 / 0.1098794937133789 / 3.4468623041990085 | [NPY](tensors/0002261.npy) |
| 2340 | `model.layers.0` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 32.5 / 0.02340112761594355 / 2.5180141341639093 | [NPY](tensors/0002340.npy) |
| 2341 | `model.layers.0` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002341.npy) |
| 2342 | `model.layers.0` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.34375 / 0.7532014846801758 / 0.8246045706539666 | [NPY](tensors/0002342.npy) |
| 2343 | `model.layers.0` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.03213447332382202 / 0.7489573739100013 | [NPY](tensors/0002343.npy) |
| 2344 | `model.layers.0` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 340.0 / 340.0 / 340.0 / 0.0 | [NPY](tensors/0002344.npy) |
| 2345 | `model.layers.0` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2346 | `model.layers.0` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2347 | `model.layers.0` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2348 | `model.layers.0.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 32.5 / 0.02340112761594355 / 2.5180141341639093 | [NPY](tensors/0002348.npy) |
| 2349 | `model.layers.0.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002349.npy) |
| 2350 | `model.layers.0.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002350.npy) |
| 2351 | `model.layers.0.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002351.npy) |
| 2352 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 340.0 / 340.0 / 340.0 / 0.0 | [NPY](tensors/0002352.npy) |
| 2353 | `model.layers.0.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2354 | `model.layers.0.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2355 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.34375 / 0.7532014846801758 / 0.8246045706539666 | [NPY](tensors/0002355.npy) |
| 2356 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.03213447332382202 / 0.7489573739100013 | [NPY](tensors/0002356.npy) |
| 2357 | `model.layers.0.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2358 | `model.layers.0.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002358.npy) |
| 2359 | `model.layers.0.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.4375 / 5.40625 / -0.007190447126049548 / 0.8410779943508924 | [NPY](tensors/0002359.npy) |
| 2360 | `model.layers.0.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002360.npy) |
| 2361 | `model.layers.0.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.375 / 29.25 / -0.0019535720348358154 / 3.219451134212101 | [NPY](tensors/0002361.npy) |
| 2362 | `model.layers.0.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002362.npy) |
| 2363 | `model.layers.0.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.71875 / 3.5625 / -0.03649583458900452 / 1.2017397564519863 | [NPY](tensors/0002363.npy) |
| 2364 | `model.layers.0.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.0625 / 3.859375 / 0.015764601368573494 / 0.5138974664733622 | [NPY](tensors/0002364.npy) |
| 2365 | `model.layers.0.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 48.25 / 0.02935652250630988 / 1.5011795630910192 | [NPY](tensors/0002365.npy) |
| 2366 | `model.layers.0.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 48.25 / 0.02935652250630988 / 1.5011795630910192 | [NPY](tensors/0002366.npy) |
| 2367 | `model.layers.0.self_attn` | 20 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.94921875 / 0.0035248219721445676 / 0.03275886378774158 | [NPY](tensors/0002367.npy) |
| 2368 | `model.layers.0.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.0 / 50.25 / 0.052651760313245984 / 2.999843521420697 | [NPY](tensors/0002368.npy) |
| 2369 | `model.layers.0.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.0625 / 1.6015625 / -0.006309845712449816 / 0.3713762854727187 | [NPY](tensors/0002369.npy) |
| 2370 | `model.layers.0.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.0625 / 1.6015625 / -0.006309845712449816 / 0.3713762854727187 | [NPY](tensors/0002370.npy) |
| 2371 | `model.layers.0.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.0625 / 1.6015625 / -0.006309845712449816 / 0.3713762854727187 | [NPY](tensors/0002371.npy) |
| 2372 | `model.layers.0.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2373 | `model.layers.0.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2374 | `model.layers.0.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2375 | `model.layers.0.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.03125 / 5.46875 / 0.015561096238282819 / 0.4554620644728799 | [NPY](tensors/0002375.npy) |
| 2376 | `model.layers.0.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.03125 / 5.46875 / 0.015561096238282819 / 0.4554620644728799 | [NPY](tensors/0002376.npy) |
| 2377 | `model.layers.0.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6875 / 1.28125 / -0.1855621337890625 / 0.6970177269548732 | [NPY](tensors/0002377.npy) |
| 2378 | `model.layers.0` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 52.75 / 0.06820997662014432 / 3.185076788171217 | [NPY](tensors/0002378.npy) |
| 2457 | `model.layers.0` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.25 / 32.0 / 0.061791101429197526 / 2.238756913453412 | [NPY](tensors/0002457.npy) |
| 2458 | `model.layers.0` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002458.npy) |
| 2459 | `model.layers.0` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.7198410034179688 / 0.8503804730267482 | [NPY](tensors/0002459.npy) |
| 2460 | `model.layers.0` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.027828902006149292 / 0.7525043584225227 | [NPY](tensors/0002460.npy) |
| 2461 | `model.layers.0` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 341.0 / 341.0 / 341.0 / 0.0 | [NPY](tensors/0002461.npy) |
| 2462 | `model.layers.0` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2463 | `model.layers.0` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2464 | `model.layers.0` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2465 | `model.layers.0.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.25 / 32.0 / 0.061791101429197526 / 2.238756913453412 | [NPY](tensors/0002465.npy) |
| 2466 | `model.layers.0.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002466.npy) |
| 2467 | `model.layers.0.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002467.npy) |
| 2468 | `model.layers.0.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002468.npy) |
| 2469 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 341.0 / 341.0 / 341.0 / 0.0 | [NPY](tensors/0002469.npy) |
| 2470 | `model.layers.0.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2471 | `model.layers.0.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2472 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.7198410034179688 / 0.8503804730267482 | [NPY](tensors/0002472.npy) |
| 2473 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.027828902006149292 / 0.7525043584225227 | [NPY](tensors/0002473.npy) |
| 2474 | `model.layers.0.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2475 | `model.layers.0.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002475.npy) |
| 2476 | `model.layers.0.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.375 / 8.125 / 0.007972375839017332 / 1.0483744761991842 | [NPY](tensors/0002476.npy) |
| 2477 | `model.layers.0.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002477.npy) |
| 2478 | `model.layers.0.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.0 / 52.0 / -0.06352853029966354 / 5.834851084637073 | [NPY](tensors/0002478.npy) |
| 2479 | `model.layers.0.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002479.npy) |
| 2480 | `model.layers.0.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.75 / 4.5 / 0.031710169510915875 / 1.4942407070139319 | [NPY](tensors/0002480.npy) |
| 2481 | `model.layers.0.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.6875 / 3.546875 / -0.012284851080039516 / 0.7028898139903671 | [NPY](tensors/0002481.npy) |
| 2482 | `model.layers.0.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.75 / 41.5 / 0.013730724779371586 / 1.3016987573602026 | [NPY](tensors/0002482.npy) |
| 2483 | `model.layers.0.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.75 / 41.5 / 0.013730724779371586 / 1.3016987573602026 | [NPY](tensors/0002483.npy) |
| 2484 | `model.layers.0.self_attn` | 21 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0042202489524684784 / 0.04442281497725351 | [NPY](tensors/0002484.npy) |
| 2485 | `model.layers.0.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 41.25 / 0.07569376892513699 / 2.6279388058496735 | [NPY](tensors/0002485.npy) |
| 2486 | `model.layers.0.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.4375 / 1.8515625 / 0.004827430182033115 / 0.45078643661911905 | [NPY](tensors/0002486.npy) |
| 2487 | `model.layers.0.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.4375 / 1.8515625 / 0.004827430182033115 / 0.45078643661911905 | [NPY](tensors/0002487.npy) |
| 2488 | `model.layers.0.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.4375 / 1.8515625 / 0.004827430182033115 / 0.45078643661911905 | [NPY](tensors/0002488.npy) |
| 2489 | `model.layers.0.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2490 | `model.layers.0.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2491 | `model.layers.0.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2492 | `model.layers.0.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.9375 / 38.5 / 0.0195451483130455 / 1.180899527447691 | [NPY](tensors/0002492.npy) |
| 2493 | `model.layers.0.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.9375 / 38.5 / 0.0195451483130455 / 1.180899527447691 | [NPY](tensors/0002493.npy) |
| 2494 | `model.layers.0.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.25 / 1.7421875 / -0.16830825805664062 / 0.7884684398639857 | [NPY](tensors/0002494.npy) |
| 2495 | `model.layers.0` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.125 / 79.0 / 0.09524377716912164 / 3.3252432024455714 | [NPY](tensors/0002495.npy) |
| 2574 | `model.layers.0` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0002574.npy) |
| 2575 | `model.layers.0` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002575.npy) |
| 2576 | `model.layers.0` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.70660400390625 / 0.91681783844784 | [NPY](tensors/0002576.npy) |
| 2577 | `model.layers.0` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / -0.014852643013000488 / 0.6845543139796254 | [NPY](tensors/0002577.npy) |
| 2578 | `model.layers.0` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 342.0 / 342.0 / 342.0 / 0.0 | [NPY](tensors/0002578.npy) |
| 2579 | `model.layers.0` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2580 | `model.layers.0` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2581 | `model.layers.0` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2582 | `model.layers.0.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0002582.npy) |
| 2583 | `model.layers.0.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002583.npy) |
| 2584 | `model.layers.0.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002584.npy) |
| 2585 | `model.layers.0.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002585.npy) |
| 2586 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 342.0 / 342.0 / 342.0 / 0.0 | [NPY](tensors/0002586.npy) |
| 2587 | `model.layers.0.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2588 | `model.layers.0.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2589 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.70660400390625 / 0.91681783844784 | [NPY](tensors/0002589.npy) |
| 2590 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / -0.014852643013000488 / 0.6845543139796254 | [NPY](tensors/0002590.npy) |
| 2591 | `model.layers.0.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2592 | `model.layers.0.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002592.npy) |
| 2593 | `model.layers.0.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.34375 / 8.125 / 0.009809806477278471 / 1.0602451281469458 | [NPY](tensors/0002593.npy) |
| 2594 | `model.layers.0.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002594.npy) |
| 2595 | `model.layers.0.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.5 / 52.75 / 0.05987404379993677 / 5.486411371880323 | [NPY](tensors/0002595.npy) |
| 2596 | `model.layers.0.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002596.npy) |
| 2597 | `model.layers.0.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.125 / 3.75 / 0.02330493927001953 / 1.1486258589347933 | [NPY](tensors/0002597.npy) |
| 2598 | `model.layers.0.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0625 / 3.96875 / 0.002689556422410533 / 0.7149478472224937 | [NPY](tensors/0002598.npy) |
| 2599 | `model.layers.0.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.875 / 44.0 / 0.035416124016046525 / 1.3381285028077492 | [NPY](tensors/0002599.npy) |
| 2600 | `model.layers.0.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.875 / 44.0 / 0.035416124016046525 / 1.3381285028077492 | [NPY](tensors/0002600.npy) |
| 2601 | `model.layers.0.self_attn` | 22 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.004489446830278222 / 0.04466046543038893 | [NPY](tensors/0002601.npy) |
| 2602 | `model.layers.0.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 48.5 / -0.028693011071946887 / 2.8432189392565492 | [NPY](tensors/0002602.npy) |
| 2603 | `model.layers.0.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9765625 / 1.6328125 / 0.0003039995829264323 / 0.39803498826503103 | [NPY](tensors/0002603.npy) |
| 2604 | `model.layers.0.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9765625 / 1.6328125 / 0.0003039995829264323 / 0.39803498826503103 | [NPY](tensors/0002604.npy) |
| 2605 | `model.layers.0.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.9765625 / 1.6328125 / 0.0003039995829264323 / 0.39803498826503103 | [NPY](tensors/0002605.npy) |
| 2606 | `model.layers.0.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2607 | `model.layers.0.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2608 | `model.layers.0.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2609 | `model.layers.0.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.703125 / 23.75 / 0.01864103058146106 / 0.7144472478397602 | [NPY](tensors/0002609.npy) |
| 2610 | `model.layers.0.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.703125 / 23.75 / 0.01864103058146106 / 0.7144472478397602 | [NPY](tensors/0002610.npy) |
| 2611 | `model.layers.0.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.875 / 1.890625 / -0.0557403564453125 / 0.8006475021445933 | [NPY](tensors/0002611.npy) |
| 2612 | `model.layers.0` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 72.0 / -0.010155932108561198 / 3.178025765890585 | [NPY](tensors/0002612.npy) |
| 2691 | `model.layers.0` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 34.75 / 0.06460592945416768 / 2.603620301499426 | [NPY](tensors/0002691.npy) |
| 2692 | `model.layers.0` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002692.npy) |
| 2693 | `model.layers.0` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.740966796875 / 0.9022817549113021 | [NPY](tensors/0002693.npy) |
| 2694 | `model.layers.0` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3046875 / -0.06294980645179749 / 0.6646640154085409 | [NPY](tensors/0002694.npy) |
| 2695 | `model.layers.0` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 343.0 / 343.0 / 343.0 / 0.0 | [NPY](tensors/0002695.npy) |
| 2696 | `model.layers.0` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2697 | `model.layers.0` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2698 | `model.layers.0` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2699 | `model.layers.0.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 34.75 / 0.06460592945416768 / 2.603620301499426 | [NPY](tensors/0002699.npy) |
| 2700 | `model.layers.0.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0002700.npy) |
| 2701 | `model.layers.0.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0002701.npy) |
| 2702 | `model.layers.0.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002702.npy) |
| 2703 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 343.0 / 343.0 / 343.0 / 0.0 | [NPY](tensors/0002703.npy) |
| 2704 | `model.layers.0.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2705 | `model.layers.0.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2706 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.740966796875 / 0.9022817549113021 | [NPY](tensors/0002706.npy) |
| 2707 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3046875 / -0.06294980645179749 / 0.6646640154085409 | [NPY](tensors/0002707.npy) |
| 2708 | `model.layers.0.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2709 | `model.layers.0.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0002709.npy) |
| 2710 | `model.layers.0.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.71875 / 8.4375 / 0.008836216118652374 / 1.127863321857116 | [NPY](tensors/0002710.npy) |
| 2711 | `model.layers.0.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0002711.npy) |
| 2712 | `model.layers.0.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -47.25 / 52.5 / -0.01974540948867798 / 5.528074362257702 | [NPY](tensors/0002712.npy) |
| 2713 | `model.layers.0.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0002713.npy) |
| 2714 | `model.layers.0.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.34375 / 5.1875 / 0.04988500475883484 / 1.3788012115777875 | [NPY](tensors/0002714.npy) |
| 2715 | `model.layers.0.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.09375 / 4.0 / -0.0026160247580264695 / 0.6022272417148133 | [NPY](tensors/0002715.npy) |
| 2716 | `model.layers.0.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.9375 / 44.0 / 0.031478928153713545 / 1.292029120107135 | [NPY](tensors/0002716.npy) |
| 2717 | `model.layers.0.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.9375 / 44.0 / 0.031478928153713545 / 1.292029120107135 | [NPY](tensors/0002717.npy) |
| 2718 | `model.layers.0.self_attn` | 23 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003154787750528516 / 0.03748750355058938 | [NPY](tensors/0002718.npy) |
| 2719 | `model.layers.0.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 43.0 / 0.09600966771443685 / 2.91433649533637 | [NPY](tensors/0002719.npy) |
| 2720 | `model.layers.0.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.75 / 1.546875 / 0.002609202596876356 / 0.38412091915360724 | [NPY](tensors/0002720.npy) |
| 2721 | `model.layers.0.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.75 / 1.546875 / 0.002609202596876356 / 0.38412091915360724 | [NPY](tensors/0002721.npy) |
| 2722 | `model.layers.0.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.75 / 1.546875 / 0.002609202596876356 / 0.38412091915360724 | [NPY](tensors/0002722.npy) |
| 2723 | `model.layers.0.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2724 | `model.layers.0.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2725 | `model.layers.0.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2726 | `model.layers.0.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.46875 / 24.875 / 0.024521939415070745 / 0.725375343971687 | [NPY](tensors/0002726.npy) |
| 2727 | `model.layers.0.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.46875 / 24.875 / 0.024521939415070745 / 0.725375343971687 | [NPY](tensors/0002727.npy) |
| 2728 | `model.layers.0.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.421875 / 1.90625 / -0.21526145935058594 / 0.8419869366433991 | [NPY](tensors/0002728.npy) |
| 2729 | `model.layers.0` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 65.0 / 0.12057827843560112 / 3.237818468252893 | [NPY](tensors/0002729.npy) |
| 2808 | `model.layers.0` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0002808.npy) |
| 2809 | `model.layers.0` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002809.npy) |
| 2810 | `model.layers.0` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8131542205810547 / 0.8233916239555151 | [NPY](tensors/0002810.npy) |
| 2811 | `model.layers.0` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.07140964269638062 / 0.6820182328303498 | [NPY](tensors/0002811.npy) |
| 2812 | `model.layers.0` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 344.0 / 344.0 / 344.0 / 0.0 | [NPY](tensors/0002812.npy) |
| 2813 | `model.layers.0` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2814 | `model.layers.0` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2815 | `model.layers.0` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2816 | `model.layers.0.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0002816.npy) |
| 2817 | `model.layers.0.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002817.npy) |
| 2818 | `model.layers.0.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002818.npy) |
| 2819 | `model.layers.0.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002819.npy) |
| 2820 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 344.0 / 344.0 / 344.0 / 0.0 | [NPY](tensors/0002820.npy) |
| 2821 | `model.layers.0.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2822 | `model.layers.0.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2823 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8131542205810547 / 0.8233916239555151 | [NPY](tensors/0002823.npy) |
| 2824 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.07140964269638062 / 0.6820182328303498 | [NPY](tensors/0002824.npy) |
| 2825 | `model.layers.0.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2826 | `model.layers.0.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002826.npy) |
| 2827 | `model.layers.0.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 9.25 / 0.06582052947487682 / 1.0317253511582722 | [NPY](tensors/0002827.npy) |
| 2828 | `model.layers.0.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002828.npy) |
| 2829 | `model.layers.0.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.5 / 59.75 / -0.027341485023498535 / 6.496414800406944 | [NPY](tensors/0002829.npy) |
| 2830 | `model.layers.0.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002830.npy) |
| 2831 | `model.layers.0.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.453125 / 4.6875 / 0.06333106756210327 / 0.9556167387162166 | [NPY](tensors/0002831.npy) |
| 2832 | `model.layers.0.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.9375 / 4.53125 / 0.007079346868522407 / 0.4681439429063608 | [NPY](tensors/0002832.npy) |
| 2833 | `model.layers.0.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.4375 / 38.0 / 0.027925605637331805 / 1.1111484332186432 | [NPY](tensors/0002833.npy) |
| 2834 | `model.layers.0.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.4375 / 38.0 / 0.027925605637331805 / 1.1111484332186432 | [NPY](tensors/0002834.npy) |
| 2835 | `model.layers.0.self_attn` | 24 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002823330514670117 / 0.030437457216273032 | [NPY](tensors/0002835.npy) |
| 2836 | `model.layers.0.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.0 / 39.25 / 0.07704846064249675 / 2.697216101087651 | [NPY](tensors/0002836.npy) |
| 2837 | `model.layers.0.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.4375 / 1.78125 / 0.005350671874152289 / 0.3169708407994292 | [NPY](tensors/0002837.npy) |
| 2838 | `model.layers.0.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.4375 / 1.78125 / 0.005350671874152289 / 0.3169708407994292 | [NPY](tensors/0002838.npy) |
| 2839 | `model.layers.0.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.4375 / 1.78125 / 0.005350671874152289 / 0.3169708407994292 | [NPY](tensors/0002839.npy) |
| 2840 | `model.layers.0.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2841 | `model.layers.0.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2842 | `model.layers.0.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2843 | `model.layers.0.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.71875 / 6.625 / -0.0022921439674165513 / 0.4590806391818679 | [NPY](tensors/0002843.npy) |
| 2844 | `model.layers.0.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.71875 / 6.625 / -0.0022921439674165513 / 0.4590806391818679 | [NPY](tensors/0002844.npy) |
| 2845 | `model.layers.0.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.859375 / 2.78125 / -0.14240264892578125 / 1.2046911527686752 | [NPY](tensors/0002845.npy) |
| 2846 | `model.layers.0` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.75 / 43.25 / 0.07488434977001614 / 2.699577437345663 | [NPY](tensors/0002846.npy) |
| 2925 | `model.layers.0` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.75 / 36.5 / -0.03277786038815975 / 2.7829041357151567 | [NPY](tensors/0002925.npy) |
| 2926 | `model.layers.0` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002926.npy) |
| 2927 | `model.layers.0` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.8764495849609375 / 0.8009113437243138 | [NPY](tensors/0002927.npy) |
| 2928 | `model.layers.0` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.020697563886642456 / 0.632324519915983 | [NPY](tensors/0002928.npy) |
| 2929 | `model.layers.0` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 345.0 / 345.0 / 345.0 / 0.0 | [NPY](tensors/0002929.npy) |
| 2930 | `model.layers.0` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2931 | `model.layers.0` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2932 | `model.layers.0` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2933 | `model.layers.0.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.75 / 36.5 / -0.03277786038815975 / 2.7829041357151567 | [NPY](tensors/0002933.npy) |
| 2934 | `model.layers.0.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002934.npy) |
| 2935 | `model.layers.0.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002935.npy) |
| 2936 | `model.layers.0.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002936.npy) |
| 2937 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 345.0 / 345.0 / 345.0 / 0.0 | [NPY](tensors/0002937.npy) |
| 2938 | `model.layers.0.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2939 | `model.layers.0.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2940 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.8764495849609375 / 0.8009113437243138 | [NPY](tensors/0002940.npy) |
| 2941 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.020697563886642456 / 0.632324519915983 | [NPY](tensors/0002941.npy) |
| 2942 | `model.layers.0.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2943 | `model.layers.0.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002943.npy) |
| 2944 | `model.layers.0.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0625 / 8.75 / 0.007699438836425543 / 0.9554901933770389 | [NPY](tensors/0002944.npy) |
| 2945 | `model.layers.0.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002945.npy) |
| 2946 | `model.layers.0.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.5 / 55.25 / -0.05697989463806152 / 6.049655579159513 | [NPY](tensors/0002946.npy) |
| 2947 | `model.layers.0.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002947.npy) |
| 2948 | `model.layers.0.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -2.703125 / 3.4375 / 0.04050885885953903 / 0.8799544405823716 | [NPY](tensors/0002948.npy) |
| 2949 | `model.layers.0.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.78125 / 4.5625 / 0.007962974421388935 / 0.4981852080089831 | [NPY](tensors/0002949.npy) |
| 2950 | `model.layers.0.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.40625 / 30.875 / 0.02937899430592855 / 0.929067854119628 | [NPY](tensors/0002950.npy) |
| 2951 | `model.layers.0.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.40625 / 30.875 / 0.02937899430592855 / 0.929067854119628 | [NPY](tensors/0002951.npy) |
| 2952 | `model.layers.0.self_attn` | 25 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0033020909764750242 / 0.03320779721223605 | [NPY](tensors/0002952.npy) |
| 2953 | `model.layers.0.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.0 / 36.75 / -0.0031560950809054905 / 2.8583007977224812 | [NPY](tensors/0002953.npy) |
| 2954 | `model.layers.0.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.109375 / 2.765625 / 0.003915629784266154 / 0.28568212139462074 | [NPY](tensors/0002954.npy) |
| 2955 | `model.layers.0.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.109375 / 2.765625 / 0.003915629784266154 / 0.28568212139462074 | [NPY](tensors/0002955.npy) |
| 2956 | `model.layers.0.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.109375 / 2.765625 / 0.003915629784266154 / 0.28568212139462074 | [NPY](tensors/0002956.npy) |
| 2957 | `model.layers.0.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2958 | `model.layers.0.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2959 | `model.layers.0.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2960 | `model.layers.0.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.3125 / 8.5 / 0.010801531540022957 / 0.5063587357677939 | [NPY](tensors/0002960.npy) |
| 2961 | `model.layers.0.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.3125 / 8.5 / 0.010801531540022957 / 0.5063587357677939 | [NPY](tensors/0002961.npy) |
| 2962 | `model.layers.0.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.40625 / 1.65625 / -0.05484962463378906 / 1.0418141537861254 | [NPY](tensors/0002962.npy) |
| 2963 | `model.layers.0` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 36.25 / 0.007601886325412326 / 2.7699193407003406 | [NPY](tensors/0002963.npy) |
| 3042 | `model.layers.0` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 25.375 / 0.03148116301745176 / 2.4913610061559237 | [NPY](tensors/0003042.npy) |
| 3043 | `model.layers.0` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003043.npy) |
| 3044 | `model.layers.0` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.887237548828125 / 0.808167570442007 | [NPY](tensors/0003044.npy) |
| 3045 | `model.layers.0` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.06384772062301636 / 0.6046658936992718 | [NPY](tensors/0003045.npy) |
| 3046 | `model.layers.0` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 346.0 / 346.0 / 346.0 / 0.0 | [NPY](tensors/0003046.npy) |
| 3047 | `model.layers.0` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3048 | `model.layers.0` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3049 | `model.layers.0` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3050 | `model.layers.0.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 25.375 / 0.03148116301745176 / 2.4913610061559237 | [NPY](tensors/0003050.npy) |
| 3051 | `model.layers.0.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003051.npy) |
| 3052 | `model.layers.0.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003052.npy) |
| 3053 | `model.layers.0.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003053.npy) |
| 3054 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 346.0 / 346.0 / 346.0 / 0.0 | [NPY](tensors/0003054.npy) |
| 3055 | `model.layers.0.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3056 | `model.layers.0.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3057 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.887237548828125 / 0.808167570442007 | [NPY](tensors/0003057.npy) |
| 3058 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.06384772062301636 / 0.6046658936992718 | [NPY](tensors/0003058.npy) |
| 3059 | `model.layers.0.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3060 | `model.layers.0.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003060.npy) |
| 3061 | `model.layers.0.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.8125 / 9.875 / 0.001175960642285645 / 1.0708778134614567 | [NPY](tensors/0003061.npy) |
| 3062 | `model.layers.0.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003062.npy) |
| 3063 | `model.layers.0.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.0 / 46.0 / -0.07610408216714859 / 5.694328378141193 | [NPY](tensors/0003063.npy) |
| 3064 | `model.layers.0.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003064.npy) |
| 3065 | `model.layers.0.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.46875 / 6.09375 / -0.02648264169692993 / 1.4472391438112524 | [NPY](tensors/0003065.npy) |
| 3066 | `model.layers.0.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.25 / 3.1875 / 0.006061712236260064 / 0.45414402757158584 | [NPY](tensors/0003066.npy) |
| 3067 | `model.layers.0.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.625 / 43.5 / 0.022009402099582884 / 1.33817107234205 | [NPY](tensors/0003067.npy) |
| 3068 | `model.layers.0.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.625 / 43.5 / 0.022009402099582884 / 1.33817107234205 | [NPY](tensors/0003068.npy) |
| 3069 | `model.layers.0.self_attn` | 26 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002945088403850273 / 0.03450351078599666 | [NPY](tensors/0003069.npy) |
| 3070 | `model.layers.0.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 44.5 / 0.05345279905531142 / 2.935847094557859 | [NPY](tensors/0003070.npy) |
| 3071 | `model.layers.0.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.21875 / 1.46875 / 0.0060400293933020694 / 0.3606188510168371 | [NPY](tensors/0003071.npy) |
| 3072 | `model.layers.0.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.21875 / 1.46875 / 0.0060400293933020694 / 0.3606188510168371 | [NPY](tensors/0003072.npy) |
| 3073 | `model.layers.0.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -5.21875 / 1.46875 / 0.0060400293933020694 / 0.3606188510168371 | [NPY](tensors/0003073.npy) |
| 3074 | `model.layers.0.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3075 | `model.layers.0.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3076 | `model.layers.0.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3077 | `model.layers.0.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.5625 / 15.6875 / 0.019439181726839807 / 0.5427952192866303 | [NPY](tensors/0003077.npy) |
| 3078 | `model.layers.0.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.5625 / 15.6875 / 0.019439181726839807 / 0.5427952192866303 | [NPY](tensors/0003078.npy) |
| 3079 | `model.layers.0.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.25 / 2.09375 / -0.20333480834960938 / 0.8210190484699318 | [NPY](tensors/0003079.npy) |
| 3080 | `model.layers.0` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.0 / 59.25 / 0.07287891176011828 / 3.256155042276669 | [NPY](tensors/0003080.npy) |
| 3159 | `model.layers.0` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.25 / 22.875 / 0.02578953950562411 / 2.1256093624936447 | [NPY](tensors/0003159.npy) |
| 3160 | `model.layers.0` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003160.npy) |
| 3161 | `model.layers.0` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.8368129730224609 / 0.8204651963806046 | [NPY](tensors/0003161.npy) |
| 3162 | `model.layers.0` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.1309933364391327 / 0.6478045244450656 | [NPY](tensors/0003162.npy) |
| 3163 | `model.layers.0` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 347.0 / 347.0 / 347.0 / 0.0 | [NPY](tensors/0003163.npy) |
| 3164 | `model.layers.0` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3165 | `model.layers.0` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3166 | `model.layers.0` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3167 | `model.layers.0.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.25 / 22.875 / 0.02578953950562411 / 2.1256093624936447 | [NPY](tensors/0003167.npy) |
| 3168 | `model.layers.0.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003168.npy) |
| 3169 | `model.layers.0.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003169.npy) |
| 3170 | `model.layers.0.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003170.npy) |
| 3171 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 347.0 / 347.0 / 347.0 / 0.0 | [NPY](tensors/0003171.npy) |
| 3172 | `model.layers.0.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3173 | `model.layers.0.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3174 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.8368129730224609 / 0.8204651963806046 | [NPY](tensors/0003174.npy) |
| 3175 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.1309933364391327 / 0.6478045244450656 | [NPY](tensors/0003175.npy) |
| 3176 | `model.layers.0.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3177 | `model.layers.0.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003177.npy) |
| 3178 | `model.layers.0.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.8125 / 7.9375 / -0.014699231367558241 / 1.1007098219776468 | [NPY](tensors/0003178.npy) |
| 3179 | `model.layers.0.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003179.npy) |
| 3180 | `model.layers.0.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.25 / 55.25 / 0.1305762529373169 / 5.5847358405435745 | [NPY](tensors/0003180.npy) |
| 3181 | `model.layers.0.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003181.npy) |
| 3182 | `model.layers.0.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.21875 / 5.84375 / -0.07473260164260864 / 1.5255124313159032 | [NPY](tensors/0003182.npy) |
| 3183 | `model.layers.0.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.4375 / 6.09375 / -0.001994971535168588 / 0.816236499424558 | [NPY](tensors/0003183.npy) |
| 3184 | `model.layers.0.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.125 / 46.75 / 0.040053828557332354 / 1.5172365176101061 | [NPY](tensors/0003184.npy) |
| 3185 | `model.layers.0.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.125 / 46.75 / 0.040053828557332354 / 1.5172365176101061 | [NPY](tensors/0003185.npy) |
| 3186 | `model.layers.0.self_attn` | 27 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0038624389724471815 / 0.0459016196302767 | [NPY](tensors/0003186.npy) |
| 3187 | `model.layers.0.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 49.5 / 0.06576600604587131 / 2.7302925787733394 | [NPY](tensors/0003187.npy) |
| 3188 | `model.layers.0.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6171875 / 1.734375 / 0.010078529516855875 / 0.4606982134930246 | [NPY](tensors/0003188.npy) |
| 3189 | `model.layers.0.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6171875 / 1.734375 / 0.010078529516855875 / 0.4606982134930246 | [NPY](tensors/0003189.npy) |
| 3190 | `model.layers.0.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.6171875 / 1.734375 / 0.010078529516855875 / 0.4606982134930246 | [NPY](tensors/0003190.npy) |
| 3191 | `model.layers.0.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3192 | `model.layers.0.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3193 | `model.layers.0.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3194 | `model.layers.0.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -20.5 / 39.25 / 0.010812244067589441 / 1.3699409293905034 | [NPY](tensors/0003194.npy) |
| 3195 | `model.layers.0.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.5 / 39.25 / 0.010812244067589441 / 1.3699409293905034 | [NPY](tensors/0003195.npy) |
| 3196 | `model.layers.0.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9765625 / 2.453125 / -0.05680084228515625 / 0.8114269709015973 | [NPY](tensors/0003196.npy) |
| 3197 | `model.layers.0` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.25 / 89.0 / 0.07678239610460069 / 3.551813874062127 | [NPY](tensors/0003197.npy) |
| 3276 | `model.layers.0` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 89.0 / 0.026544343266222212 / 4.541275344485995 | [NPY](tensors/0003276.npy) |
| 3277 | `model.layers.0` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003277.npy) |
| 3278 | `model.layers.0` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7588653564453125 / 0.8828955932720353 | [NPY](tensors/0003278.npy) |
| 3279 | `model.layers.0` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14290890097618103 / 0.6590419455082627 | [NPY](tensors/0003279.npy) |
| 3280 | `model.layers.0` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 348.0 / 348.0 / 348.0 / 0.0 | [NPY](tensors/0003280.npy) |
| 3281 | `model.layers.0` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3282 | `model.layers.0` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3283 | `model.layers.0` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3284 | `model.layers.0.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 89.0 / 0.026544343266222212 / 4.541275344485995 | [NPY](tensors/0003284.npy) |
| 3285 | `model.layers.0.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003285.npy) |
| 3286 | `model.layers.0.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003286.npy) |
| 3287 | `model.layers.0.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003287.npy) |
| 3288 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 348.0 / 348.0 / 348.0 / 0.0 | [NPY](tensors/0003288.npy) |
| 3289 | `model.layers.0.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3290 | `model.layers.0.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3291 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7588653564453125 / 0.8828955932720353 | [NPY](tensors/0003291.npy) |
| 3292 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14290890097618103 / 0.6590419455082627 | [NPY](tensors/0003292.npy) |
| 3293 | `model.layers.0.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3294 | `model.layers.0.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003294.npy) |
| 3295 | `model.layers.0.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.875 / 7.84375 / 0.015290047216694802 / 0.914624676971129 | [NPY](tensors/0003295.npy) |
| 3296 | `model.layers.0.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003296.npy) |
| 3297 | `model.layers.0.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.25 / 34.5 / -0.11417865753173828 / 4.434976879466014 | [NPY](tensors/0003297.npy) |
| 3298 | `model.layers.0.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003298.npy) |
| 3299 | `model.layers.0.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.03125 / 4.8125 / -0.07233588397502899 / 1.0561324517062678 | [NPY](tensors/0003299.npy) |
| 3300 | `model.layers.0.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.09375 / 5.71875 / -0.042821906972676516 / 0.8068173231211933 | [NPY](tensors/0003300.npy) |
| 3301 | `model.layers.0.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.625 / 28.5 / 0.03120114869541592 / 1.1796443220997896 | [NPY](tensors/0003301.npy) |
| 3302 | `model.layers.0.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.625 / 28.5 / 0.03120114869541592 / 1.1796443220997896 | [NPY](tensors/0003302.npy) |
| 3303 | `model.layers.0.self_attn` | 28 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004200770805850903 / 0.044327192670177235 | [NPY](tensors/0003303.npy) |
| 3304 | `model.layers.0.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -60.25 / 66.5 / 0.05790104336208767 / 4.069501006722114 | [NPY](tensors/0003304.npy) |
| 3305 | `model.layers.0.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0 / 2.125 / 0.009295962916480171 / 0.2847601184534186 | [NPY](tensors/0003305.npy) |
| 3306 | `model.layers.0.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0 / 2.125 / 0.009295962916480171 / 0.2847601184534186 | [NPY](tensors/0003306.npy) |
| 3307 | `model.layers.0.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.0 / 2.125 / 0.009295962916480171 / 0.2847601184534186 | [NPY](tensors/0003307.npy) |
| 3308 | `model.layers.0.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3309 | `model.layers.0.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3310 | `model.layers.0.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3311 | `model.layers.0.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -28.875 / 24.75 / 0.022375789574450917 / 1.2774911247764087 | [NPY](tensors/0003311.npy) |
| 3312 | `model.layers.0.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.875 / 24.75 / 0.022375789574450917 / 1.2774911247764087 | [NPY](tensors/0003312.npy) |
| 3313 | `model.layers.0.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.75 / 2.875 / -0.17864227294921875 / 0.867467631454446 | [NPY](tensors/0003313.npy) |
| 3314 | `model.layers.0` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.0 / 57.25 / 0.08021535873413085 / 3.5979895830906345 | [NPY](tensors/0003314.npy) |
| 3393 | `model.layers.0` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0003393.npy) |
| 3394 | `model.layers.0` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003394.npy) |
| 3395 | `model.layers.0` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.701873779296875 / 0.9298159802037973 | [NPY](tensors/0003395.npy) |
| 3396 | `model.layers.0` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.10132250189781189 / 0.6650396518932735 | [NPY](tensors/0003396.npy) |
| 3397 | `model.layers.0` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 349.0 / 349.0 / 349.0 / 0.0 | [NPY](tensors/0003397.npy) |
| 3398 | `model.layers.0` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3399 | `model.layers.0` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3400 | `model.layers.0` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3401 | `model.layers.0.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0003401.npy) |
| 3402 | `model.layers.0.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003402.npy) |
| 3403 | `model.layers.0.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003403.npy) |
| 3404 | `model.layers.0.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003404.npy) |
| 3405 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 349.0 / 349.0 / 349.0 / 0.0 | [NPY](tensors/0003405.npy) |
| 3406 | `model.layers.0.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3407 | `model.layers.0.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3408 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.701873779296875 / 0.9298159802037973 | [NPY](tensors/0003408.npy) |
| 3409 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.10132250189781189 / 0.6650396518932735 | [NPY](tensors/0003409.npy) |
| 3410 | `model.layers.0.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3411 | `model.layers.0.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003411.npy) |
| 3412 | `model.layers.0.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 7.625 / 0.011268170550465584 / 0.9167789321734896 | [NPY](tensors/0003412.npy) |
| 3413 | `model.layers.0.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003413.npy) |
| 3414 | `model.layers.0.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 43.75 / 0.046514674089848995 / 4.791095594233786 | [NPY](tensors/0003414.npy) |
| 3415 | `model.layers.0.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003415.npy) |
| 3416 | `model.layers.0.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.84375 / 4.125 / -0.01808762550354004 / 1.3178383551916408 | [NPY](tensors/0003416.npy) |
| 3417 | `model.layers.0.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.15625 / 4.34375 / -0.009857212222414091 / 0.49563968700741584 | [NPY](tensors/0003417.npy) |
| 3418 | `model.layers.0.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.125 / 38.0 / 0.030097500855724015 / 1.0950935168772022 | [NPY](tensors/0003418.npy) |
| 3419 | `model.layers.0.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.125 / 38.0 / 0.030097500855724015 / 1.0950935168772022 | [NPY](tensors/0003419.npy) |
| 3420 | `model.layers.0.self_attn` | 29 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.0031851582671357363 / 0.0283683703639052 | [NPY](tensors/0003420.npy) |
| 3421 | `model.layers.0.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 39.0 / 0.019421090020073785 / 2.8496651801559203 | [NPY](tensors/0003421.npy) |
| 3422 | `model.layers.0.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.15625 / 1.96875 / 0.008181229896015592 / 0.37756827531804693 | [NPY](tensors/0003422.npy) |
| 3423 | `model.layers.0.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.15625 / 1.96875 / 0.008181229896015592 / 0.37756827531804693 | [NPY](tensors/0003423.npy) |
| 3424 | `model.layers.0.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.15625 / 1.96875 / 0.008181229896015592 / 0.37756827531804693 | [NPY](tensors/0003424.npy) |
| 3425 | `model.layers.0.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3426 | `model.layers.0.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3427 | `model.layers.0.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3428 | `model.layers.0.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.0 / 16.625 / 0.020786520755953258 / 0.5728848050135633 | [NPY](tensors/0003428.npy) |
| 3429 | `model.layers.0.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.0 / 16.625 / 0.020786520755953258 / 0.5728848050135633 | [NPY](tensors/0003429.npy) |
| 3430 | `model.layers.0.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0546875 / 1.890625 / -0.07280540466308594 / 0.6352043911604794 | [NPY](tensors/0003430.npy) |
| 3431 | `model.layers.0` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.75 / 55.5 / 0.04002140892876519 / 3.0960170909334344 | [NPY](tensors/0003431.npy) |
| 3510 | `model.layers.0` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 30.875 / -0.03053326966861884 / 2.629557572976096 | [NPY](tensors/0003510.npy) |
| 3511 | `model.layers.0` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003511.npy) |
| 3512 | `model.layers.0` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.690826416015625 / 0.927895842605205 | [NPY](tensors/0003512.npy) |
| 3513 | `model.layers.0` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.04170632362365723 / 0.685352030153117 | [NPY](tensors/0003513.npy) |
| 3514 | `model.layers.0` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 350.0 / 350.0 / 350.0 / 0.0 | [NPY](tensors/0003514.npy) |
| 3515 | `model.layers.0` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3516 | `model.layers.0` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3517 | `model.layers.0` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3518 | `model.layers.0.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 30.875 / -0.03053326966861884 / 2.629557572976096 | [NPY](tensors/0003518.npy) |
| 3519 | `model.layers.0.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003519.npy) |
| 3520 | `model.layers.0.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003520.npy) |
| 3521 | `model.layers.0.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003521.npy) |
| 3522 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 350.0 / 350.0 / 350.0 / 0.0 | [NPY](tensors/0003522.npy) |
| 3523 | `model.layers.0.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3524 | `model.layers.0.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3525 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.690826416015625 / 0.927895842605205 | [NPY](tensors/0003525.npy) |
| 3526 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.04170632362365723 / 0.685352030153117 | [NPY](tensors/0003526.npy) |
| 3527 | `model.layers.0.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3528 | `model.layers.0.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003528.npy) |
| 3529 | `model.layers.0.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 9.375 / -0.0057218477595597506 / 1.0817809599468158 | [NPY](tensors/0003529.npy) |
| 3530 | `model.layers.0.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003530.npy) |
| 3531 | `model.layers.0.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.75 / 60.25 / 0.21187177300453186 / 5.623456193541793 | [NPY](tensors/0003531.npy) |
| 3532 | `model.layers.0.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003532.npy) |
| 3533 | `model.layers.0.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.15625 / 3.484375 / -0.04266364127397537 / 1.132992277020041 | [NPY](tensors/0003533.npy) |
| 3534 | `model.layers.0.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.78125 / 4.09375 / -4.247833203407936e-05 / 0.8101508735045365 | [NPY](tensors/0003534.npy) |
| 3535 | `model.layers.0.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 47.75 / 0.03710534299413363 / 1.4262792429465467 | [NPY](tensors/0003535.npy) |
| 3536 | `model.layers.0.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.0625 / 47.75 / 0.03710534299413363 / 1.4262792429465467 | [NPY](tensors/0003536.npy) |
| 3537 | `model.layers.0.self_attn` | 30 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004699212439963242 / 0.0502982971292184 | [NPY](tensors/0003537.npy) |
| 3538 | `model.layers.0.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 51.75 / 0.006581269370185004 / 3.04051912742466 | [NPY](tensors/0003538.npy) |
| 3539 | `model.layers.0.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 1.625 / 0.0051869885789023506 / 0.3931295940363556 | [NPY](tensors/0003539.npy) |
| 3540 | `model.layers.0.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 1.625 / 0.0051869885789023506 / 0.3931295940363556 | [NPY](tensors/0003540.npy) |
| 3541 | `model.layers.0.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.8125 / 1.625 / 0.0051869885789023506 / 0.3931295940363556 | [NPY](tensors/0003541.npy) |
| 3542 | `model.layers.0.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3543 | `model.layers.0.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3544 | `model.layers.0.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3545 | `model.layers.0.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.5625 / 39.25 / 0.05383943849139743 / 1.2327717608963815 | [NPY](tensors/0003545.npy) |
| 3546 | `model.layers.0.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 39.25 / 0.05383943849139743 / 1.2327717608963815 | [NPY](tensors/0003546.npy) |
| 3547 | `model.layers.0.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.5390625 / -0.13469696044921875 / 0.6148333718103032 | [NPY](tensors/0003547.npy) |
| 3548 | `model.layers.0` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 91.0 / 0.06033727857801649 / 3.6994507591289256 | [NPY](tensors/0003548.npy) |
| 3627 | `model.layers.0` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 29.875 / -0.024451741410626306 / 2.4041472308375256 | [NPY](tensors/0003627.npy) |
| 3628 | `model.layers.0` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003628.npy) |
| 3629 | `model.layers.0` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.715423583984375 / 0.9264461804361078 | [NPY](tensors/0003629.npy) |
| 3630 | `model.layers.0` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.0011060535907745361 / 0.6627134184873914 | [NPY](tensors/0003630.npy) |
| 3631 | `model.layers.0` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 351.0 / 351.0 / 351.0 / 0.0 | [NPY](tensors/0003631.npy) |
| 3632 | `model.layers.0` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3633 | `model.layers.0` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3634 | `model.layers.0` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3635 | `model.layers.0.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 29.875 / -0.024451741410626306 / 2.4041472308375256 | [NPY](tensors/0003635.npy) |
| 3636 | `model.layers.0.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003636.npy) |
| 3637 | `model.layers.0.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003637.npy) |
| 3638 | `model.layers.0.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003638.npy) |
| 3639 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 351.0 / 351.0 / 351.0 / 0.0 | [NPY](tensors/0003639.npy) |
| 3640 | `model.layers.0.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3641 | `model.layers.0.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3642 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.715423583984375 / 0.9264461804361078 | [NPY](tensors/0003642.npy) |
| 3643 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.0011060535907745361 / 0.6627134184873914 | [NPY](tensors/0003643.npy) |
| 3644 | `model.layers.0.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3645 | `model.layers.0.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003645.npy) |
| 3646 | `model.layers.0.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.96875 / 9.3125 / 0.013412588275969028 / 1.162217466520388 | [NPY](tensors/0003646.npy) |
| 3647 | `model.layers.0.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003647.npy) |
| 3648 | `model.layers.0.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.5 / 52.75 / 0.024785220623016357 / 5.9833002218429145 | [NPY](tensors/0003648.npy) |
| 3649 | `model.layers.0.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003649.npy) |
| 3650 | `model.layers.0.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.8125 / 6.03125 / -0.03467495460063219 / 1.460652286605354 | [NPY](tensors/0003650.npy) |
| 3651 | `model.layers.0.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.125 / 2.796875 / -0.033418352049011446 / 0.576802663687985 | [NPY](tensors/0003651.npy) |
| 3652 | `model.layers.0.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.625 / 46.25 / 0.022698120234741104 / 1.3669315209397983 | [NPY](tensors/0003652.npy) |
| 3653 | `model.layers.0.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.625 / 46.25 / 0.022698120234741104 / 1.3669315209397983 | [NPY](tensors/0003653.npy) |
| 3654 | `model.layers.0.self_attn` | 31 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003090119309823958 / 0.03780392217302368 | [NPY](tensors/0003654.npy) |
| 3655 | `model.layers.0.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 45.25 / -0.0017683400048149956 / 2.832224263190073 | [NPY](tensors/0003655.npy) |
| 3656 | `model.layers.0.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.953125 / 1.8984375 / 0.006985567675696479 / 0.3734048396708585 | [NPY](tensors/0003656.npy) |
| 3657 | `model.layers.0.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.953125 / 1.8984375 / 0.006985567675696479 / 0.3734048396708585 | [NPY](tensors/0003657.npy) |
| 3658 | `model.layers.0.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.953125 / 1.8984375 / 0.006985567675696479 / 0.3734048396708585 | [NPY](tensors/0003658.npy) |
| 3659 | `model.layers.0.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3660 | `model.layers.0.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3661 | `model.layers.0.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3662 | `model.layers.0.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.75 / 30.25 / 0.030362319035662545 / 0.9609129627226145 | [NPY](tensors/0003662.npy) |
| 3663 | `model.layers.0.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.75 / 30.25 / 0.030362319035662545 / 0.9609129627226145 | [NPY](tensors/0003663.npy) |
| 3664 | `model.layers.0.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9453125 / 1.9140625 / -0.15657424926757812 / 0.7879083908546749 | [NPY](tensors/0003664.npy) |
| 3665 | `model.layers.0` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 75.0 / 0.02880396048227946 / 3.3426978820276134 | [NPY](tensors/0003665.npy) |
| 3744 | `model.layers.0` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 35.0 / -0.0015044911040200128 / 2.4601390841825688 | [NPY](tensors/0003744.npy) |
| 3745 | `model.layers.0` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003745.npy) |
| 3746 | `model.layers.0` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.09375 / 1.34375 / 0.7454833984375 / 0.8931286656122284 | [NPY](tensors/0003746.npy) |
| 3747 | `model.layers.0` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3203125 / -0.0122755765914917 / 0.6751613260908969 | [NPY](tensors/0003747.npy) |
| 3748 | `model.layers.0` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 352.0 / 352.0 / 352.0 / 0.0 | [NPY](tensors/0003748.npy) |
| 3749 | `model.layers.0` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3750 | `model.layers.0` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3751 | `model.layers.0` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3752 | `model.layers.0.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 35.0 / -0.0015044911040200128 / 2.4601390841825688 | [NPY](tensors/0003752.npy) |
| 3753 | `model.layers.0.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003753.npy) |
| 3754 | `model.layers.0.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003754.npy) |
| 3755 | `model.layers.0.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003755.npy) |
| 3756 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 352.0 / 352.0 / 352.0 / 0.0 | [NPY](tensors/0003756.npy) |
| 3757 | `model.layers.0.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3758 | `model.layers.0.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3759 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.09375 / 1.34375 / 0.7454833984375 / 0.8931286656122284 | [NPY](tensors/0003759.npy) |
| 3760 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3203125 / -0.0122755765914917 / 0.6751613260908969 | [NPY](tensors/0003760.npy) |
| 3761 | `model.layers.0.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3762 | `model.layers.0.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003762.npy) |
| 3763 | `model.layers.0.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 6.875 / 0.0073078901041299105 / 1.018639785574501 | [NPY](tensors/0003763.npy) |
| 3764 | `model.layers.0.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003764.npy) |
| 3765 | `model.layers.0.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.0 / 49.0 / 0.1723565487191081 / 4.808040616212344 | [NPY](tensors/0003765.npy) |
| 3766 | `model.layers.0.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003766.npy) |
| 3767 | `model.layers.0.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.8125 / 3.265625 / 0.014979145489633083 / 1.106498243297265 | [NPY](tensors/0003767.npy) |
| 3768 | `model.layers.0.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.65625 / 5.84375 / -0.008692445982887875 / 0.7599063284986969 | [NPY](tensors/0003768.npy) |
| 3769 | `model.layers.0.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.625 / 44.25 / 0.028286063174406687 / 1.3446089313510907 | [NPY](tensors/0003769.npy) |
| 3770 | `model.layers.0.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.625 / 44.25 / 0.028286063174406687 / 1.3446089313510907 | [NPY](tensors/0003770.npy) |
| 3771 | `model.layers.0.self_attn` | 32 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.004142394581286962 / 0.0430943217055262 | [NPY](tensors/0003771.npy) |
| 3772 | `model.layers.0.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 42.25 / 0.02676053179634942 / 2.8266047124899494 | [NPY](tensors/0003772.npy) |
| 3773 | `model.layers.0.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.09375 / 2.25 / -0.0013112425804138184 / 0.4276656221919784 | [NPY](tensors/0003773.npy) |
| 3774 | `model.layers.0.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.09375 / 2.25 / -0.0013112425804138184 / 0.4276656221919784 | [NPY](tensors/0003774.npy) |
| 3775 | `model.layers.0.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.09375 / 2.25 / -0.0013112425804138184 / 0.4276656221919784 | [NPY](tensors/0003775.npy) |
| 3776 | `model.layers.0.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3777 | `model.layers.0.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3778 | `model.layers.0.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3779 | `model.layers.0.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.8125 / 25.25 / 0.022691998879114786 / 1.0830930846654747 | [NPY](tensors/0003779.npy) |
| 3780 | `model.layers.0.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 25.25 / 0.022691998879114786 / 1.0830930846654747 | [NPY](tensors/0003780.npy) |
| 3781 | `model.layers.0.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.28125 / 2.0 / -0.00951385498046875 / 1.2930145651493496 | [NPY](tensors/0003781.npy) |
| 3782 | `model.layers.0` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 66.0 / 0.0493310292561849 / 3.2497391898255303 | [NPY](tensors/0003782.npy) |
| 3861 | `model.layers.0` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 22.625 / -0.02912892893784576 / 2.1983857303463927 | [NPY](tensors/0003861.npy) |
| 3862 | `model.layers.0` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003862.npy) |
| 3863 | `model.layers.0` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.9921875 / 1.34375 / 0.763092041015625 / 0.8164851998069582 | [NPY](tensors/0003863.npy) |
| 3864 | `model.layers.0` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3203125 / -0.015299439430236816 / 0.7488356747498943 | [NPY](tensors/0003864.npy) |
| 3865 | `model.layers.0` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 353.0 / 353.0 / 353.0 / 0.0 | [NPY](tensors/0003865.npy) |
| 3866 | `model.layers.0` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3867 | `model.layers.0` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3868 | `model.layers.0` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3869 | `model.layers.0.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 22.625 / -0.02912892893784576 / 2.1983857303463927 | [NPY](tensors/0003869.npy) |
| 3870 | `model.layers.0.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003870.npy) |
| 3871 | `model.layers.0.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003871.npy) |
| 3872 | `model.layers.0.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003872.npy) |
| 3873 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 353.0 / 353.0 / 353.0 / 0.0 | [NPY](tensors/0003873.npy) |
| 3874 | `model.layers.0.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3875 | `model.layers.0.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3876 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.9921875 / 1.34375 / 0.763092041015625 / 0.8164851998069582 | [NPY](tensors/0003876.npy) |
| 3877 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3203125 / -0.015299439430236816 / 0.7488356747498943 | [NPY](tensors/0003877.npy) |
| 3878 | `model.layers.0.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3879 | `model.layers.0.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003879.npy) |
| 3880 | `model.layers.0.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.78125 / 0.008440272184088826 / 1.120452857679885 | [NPY](tensors/0003880.npy) |
| 3881 | `model.layers.0.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003881.npy) |
| 3882 | `model.layers.0.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.5 / 51.5 / 0.1618337631225586 / 5.774741101565946 | [NPY](tensors/0003882.npy) |
| 3883 | `model.layers.0.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003883.npy) |
| 3884 | `model.layers.0.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.9375 / 4.875 / -0.08827418088912964 / 1.3724833169271258 | [NPY](tensors/0003884.npy) |
| 3885 | `model.layers.0.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.34375 / 5.3125 / -0.01765729514954728 / 0.6711253785102177 | [NPY](tensors/0003885.npy) |
| 3886 | `model.layers.0.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 49.75 / 0.027496276961432562 / 1.5843518359215785 | [NPY](tensors/0003886.npy) |
| 3887 | `model.layers.0.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 49.75 / 0.027496276961432562 / 1.5843518359215785 | [NPY](tensors/0003887.npy) |
| 3888 | `model.layers.0.self_attn` | 33 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0038165453560175754 / 0.04208283783843969 | [NPY](tensors/0003888.npy) |
| 3889 | `model.layers.0.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -56.5 / 56.75 / -0.001659165488349067 / 2.9047764391153 | [NPY](tensors/0003889.npy) |
| 3890 | `model.layers.0.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6640625 / 1.8671875 / 0.004910359117719862 / 0.3601395722809383 | [NPY](tensors/0003890.npy) |
| 3891 | `model.layers.0.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6640625 / 1.8671875 / 0.004910359117719862 / 0.3601395722809383 | [NPY](tensors/0003891.npy) |
| 3892 | `model.layers.0.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.6640625 / 1.8671875 / 0.004910359117719862 / 0.3601395722809383 | [NPY](tensors/0003892.npy) |
| 3893 | `model.layers.0.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3894 | `model.layers.0.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3895 | `model.layers.0.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3896 | `model.layers.0.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.25 / 24.625 / 0.027847994036144682 / 0.8626203132937068 | [NPY](tensors/0003896.npy) |
| 3897 | `model.layers.0.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.25 / 24.625 / 0.027847994036144682 / 0.8626203132937068 | [NPY](tensors/0003897.npy) |
| 3898 | `model.layers.0.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.171875 / 1.6015625 / -0.07268905639648438 / 0.7123982022058369 | [NPY](tensors/0003898.npy) |
| 3899 | `model.layers.0` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 76.5 / 0.02623487909634908 / 3.154099218055261 | [NPY](tensors/0003899.npy) |
| 3978 | `model.layers.0` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0003978.npy) |
| 3979 | `model.layers.0` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003979.npy) |
| 3980 | `model.layers.0` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2265625 / 1.34375 / 0.7769069671630859 / 0.8058280923944267 | [NPY](tensors/0003980.npy) |
| 3981 | `model.layers.0` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / -0.027683675289154053 / 0.7450244855303801 | [NPY](tensors/0003981.npy) |
| 3982 | `model.layers.0` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 354.0 / 354.0 / 354.0 / 0.0 | [NPY](tensors/0003982.npy) |
| 3983 | `model.layers.0` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3984 | `model.layers.0` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3985 | `model.layers.0` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3986 | `model.layers.0.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0003986.npy) |
| 3987 | `model.layers.0.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003987.npy) |
| 3988 | `model.layers.0.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003988.npy) |
| 3989 | `model.layers.0.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003989.npy) |
| 3990 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 354.0 / 354.0 / 354.0 / 0.0 | [NPY](tensors/0003990.npy) |
| 3991 | `model.layers.0.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3992 | `model.layers.0.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3993 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2265625 / 1.34375 / 0.7769069671630859 / 0.8058280923944267 | [NPY](tensors/0003993.npy) |
| 3994 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / -0.027683675289154053 / 0.7450244855303801 | [NPY](tensors/0003994.npy) |
| 3995 | `model.layers.0.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3996 | `model.layers.0.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003996.npy) |
| 3997 | `model.layers.0.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 8.0 / 0.0014486645814031363 / 1.027321203413773 | [NPY](tensors/0003997.npy) |
| 3998 | `model.layers.0.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003998.npy) |
| 3999 | `model.layers.0.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.75 / 53.75 / 0.06940409168601036 / 5.734687316339554 | [NPY](tensors/0003999.npy) |
| 4000 | `model.layers.0.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004000.npy) |
| 4001 | `model.layers.0.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.8125 / 3.75 / -0.006423294544219971 / 0.9290448609736645 | [NPY](tensors/0004001.npy) |
| 4002 | `model.layers.0.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.125 / 4.59375 / -0.0026454693879713886 / 0.6701349367771199 | [NPY](tensors/0004002.npy) |
| 4003 | `model.layers.0.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.5625 / 36.75 / 0.029067450679010814 / 1.156196698611806 | [NPY](tensors/0004003.npy) |
| 4004 | `model.layers.0.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.5625 / 36.75 / 0.029067450679010814 / 1.156196698611806 | [NPY](tensors/0004004.npy) |
| 4005 | `model.layers.0.self_attn` | 34 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004232354179302396 / 0.04460824055001455 | [NPY](tensors/0004005.npy) |
| 4006 | `model.layers.0.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.75 / 37.25 / -0.06186356014675564 / 2.963220274399975 | [NPY](tensors/0004006.npy) |
| 4007 | `model.layers.0.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8125 / 1.6328125 / 0.0012973142994774712 / 0.3440154058438926 | [NPY](tensors/0004007.npy) |
| 4008 | `model.layers.0.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8125 / 1.6328125 / 0.0012973142994774712 / 0.3440154058438926 | [NPY](tensors/0004008.npy) |
| 4009 | `model.layers.0.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.8125 / 1.6328125 / 0.0012973142994774712 / 0.3440154058438926 | [NPY](tensors/0004009.npy) |
| 4010 | `model.layers.0.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4011 | `model.layers.0.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4012 | `model.layers.0.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4013 | `model.layers.0.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.03125 / 12.875 / 0.020540873871909247 / 0.5190760716816629 | [NPY](tensors/0004013.npy) |
| 4014 | `model.layers.0.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.03125 / 12.875 / 0.020540873871909247 / 0.5190760716816629 | [NPY](tensors/0004014.npy) |
| 4015 | `model.layers.0.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.5625 / 1.53125 / 0.02207183837890625 / 1.3914812054160473 | [NPY](tensors/0004015.npy) |
| 4016 | `model.layers.0` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 40.5 / -0.041115824381510416 / 2.9246697620757813 | [NPY](tensors/0004016.npy) |
| 4095 | `model.layers.0` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 30.0 / -0.032196171374784574 / 2.820171892718441 | [NPY](tensors/0004095.npy) |
| 4096 | `model.layers.0` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004096.npy) |
| 4097 | `model.layers.0` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.80755615234375 / 0.8303206482187034 | [NPY](tensors/0004097.npy) |
| 4098 | `model.layers.0` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / -0.04510064423084259 / 0.6824180444259353 | [NPY](tensors/0004098.npy) |
| 4099 | `model.layers.0` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 355.0 / 355.0 / 355.0 / 0.0 | [NPY](tensors/0004099.npy) |
| 4100 | `model.layers.0` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4101 | `model.layers.0` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4102 | `model.layers.0` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4103 | `model.layers.0.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 30.0 / -0.032196171374784574 / 2.820171892718441 | [NPY](tensors/0004103.npy) |
| 4104 | `model.layers.0.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004104.npy) |
| 4105 | `model.layers.0.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004105.npy) |
| 4106 | `model.layers.0.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004106.npy) |
| 4107 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 355.0 / 355.0 / 355.0 / 0.0 | [NPY](tensors/0004107.npy) |
| 4108 | `model.layers.0.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4109 | `model.layers.0.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4110 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.80755615234375 / 0.8303206482187034 | [NPY](tensors/0004110.npy) |
| 4111 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / -0.04510064423084259 / 0.6824180444259353 | [NPY](tensors/0004111.npy) |
| 4112 | `model.layers.0.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4113 | `model.layers.0.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004113.npy) |
| 4114 | `model.layers.0.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.6875 / 10.0625 / 0.016296769957989454 / 1.0275877120532655 | [NPY](tensors/0004114.npy) |
| 4115 | `model.layers.0.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004115.npy) |
| 4116 | `model.layers.0.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -57.0 / 59.0 / -0.06925755739212036 / 5.9291873125568 | [NPY](tensors/0004116.npy) |
| 4117 | `model.layers.0.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004117.npy) |
| 4118 | `model.layers.0.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.0625 / 3.890625 / -0.020120687782764435 / 1.0179532107822138 | [NPY](tensors/0004118.npy) |
| 4119 | `model.layers.0.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.75 / 3.421875 / -0.023336830403422937 / 0.568673030353658 | [NPY](tensors/0004119.npy) |
| 4120 | `model.layers.0.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 36.0 / 0.02116073055399789 / 1.1172220378554807 | [NPY](tensors/0004120.npy) |
| 4121 | `model.layers.0.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 36.0 / 0.02116073055399789 / 1.1172220378554807 | [NPY](tensors/0004121.npy) |
| 4122 | `model.layers.0.self_attn` | 35 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.003713882925427099 / 0.041206493832378906 | [NPY](tensors/0004122.npy) |
| 4123 | `model.layers.0.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 37.25 / -0.011016967561509874 / 2.8911886302833065 | [NPY](tensors/0004123.npy) |
| 4124 | `model.layers.0.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.96875 / 1.6484375 / 0.0022626650002267627 / 0.2748398801213969 | [NPY](tensors/0004124.npy) |
| 4125 | `model.layers.0.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.96875 / 1.6484375 / 0.0022626650002267627 / 0.2748398801213969 | [NPY](tensors/0004125.npy) |
| 4126 | `model.layers.0.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.96875 / 1.6484375 / 0.0022626650002267627 / 0.2748398801213969 | [NPY](tensors/0004126.npy) |
| 4127 | `model.layers.0.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4128 | `model.layers.0.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4129 | `model.layers.0.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4130 | `model.layers.0.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.375 / 10.375 / 0.009786853194236755 / 0.5690847756834704 | [NPY](tensors/0004130.npy) |
| 4131 | `model.layers.0.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.375 / 10.375 / 0.009786853194236755 / 0.5690847756834704 | [NPY](tensors/0004131.npy) |
| 4132 | `model.layers.0.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.578125 / 1.7734375 / -0.026149749755859375 / 1.0352972590179188 | [NPY](tensors/0004132.npy) |
| 4133 | `model.layers.0` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 47.5 / -0.001251999537150065 / 2.863881457699113 | [NPY](tensors/0004133.npy) |
| 4212 | `model.layers.0` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.5 / 30.625 / 0.03435131601161427 / 2.148670063069294 | [NPY](tensors/0004212.npy) |
| 4213 | `model.layers.0` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004213.npy) |
| 4214 | `model.layers.0` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.85931396484375 / 0.7701579969072487 | [NPY](tensors/0004214.npy) |
| 4215 | `model.layers.0` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3203125 / -0.04313334822654724 / 0.6902819775762118 | [NPY](tensors/0004215.npy) |
| 4216 | `model.layers.0` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 356.0 / 356.0 / 356.0 / 0.0 | [NPY](tensors/0004216.npy) |
| 4217 | `model.layers.0` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4218 | `model.layers.0` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4219 | `model.layers.0` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4220 | `model.layers.0.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.5 / 30.625 / 0.03435131601161427 / 2.148670063069294 | [NPY](tensors/0004220.npy) |
| 4221 | `model.layers.0.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004221.npy) |
| 4222 | `model.layers.0.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004222.npy) |
| 4223 | `model.layers.0.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004223.npy) |
| 4224 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 356.0 / 356.0 / 356.0 / 0.0 | [NPY](tensors/0004224.npy) |
| 4225 | `model.layers.0.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4226 | `model.layers.0.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4227 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.85931396484375 / 0.7701579969072487 | [NPY](tensors/0004227.npy) |
| 4228 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3203125 / -0.04313334822654724 / 0.6902819775762118 | [NPY](tensors/0004228.npy) |
| 4229 | `model.layers.0.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4230 | `model.layers.0.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004230.npy) |
| 4231 | `model.layers.0.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.59375 / 8.875 / -0.01820482179755345 / 1.2112680722654519 | [NPY](tensors/0004231.npy) |
| 4232 | `model.layers.0.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004232.npy) |
| 4233 | `model.layers.0.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -47.25 / 51.0 / 0.04916292428970337 / 5.661126585935481 | [NPY](tensors/0004233.npy) |
| 4234 | `model.layers.0.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004234.npy) |
| 4235 | `model.layers.0.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.59375 / 4.9375 / -0.02149730920791626 / 1.5738961772339104 | [NPY](tensors/0004235.npy) |
| 4236 | `model.layers.0.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.03125 / 3.03125 / -0.017957830314117018 / 0.4599592432583556 | [NPY](tensors/0004236.npy) |
| 4237 | `model.layers.0.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.25 / 31.875 / 0.010058176724447145 / 1.0310315211446077 | [NPY](tensors/0004237.npy) |
| 4238 | `model.layers.0.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.25 / 31.875 / 0.010058176724447145 / 1.0310315211446077 | [NPY](tensors/0004238.npy) |
| 4239 | `model.layers.0.self_attn` | 36 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.002167261569140601 / 0.03393176994173062 | [NPY](tensors/0004239.npy) |
| 4240 | `model.layers.0.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 32.25 / 0.04442010985480414 / 2.470572792054532 | [NPY](tensors/0004240.npy) |
| 4241 | `model.layers.0.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.765625 / 2.4375 / 0.005042125781377156 / 0.41973537457155685 | [NPY](tensors/0004241.npy) |
| 4242 | `model.layers.0.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.765625 / 2.4375 / 0.005042125781377156 / 0.41973537457155685 | [NPY](tensors/0004242.npy) |
| 4243 | `model.layers.0.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.765625 / 2.4375 / 0.005042125781377156 / 0.41973537457155685 | [NPY](tensors/0004243.npy) |
| 4244 | `model.layers.0.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4245 | `model.layers.0.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4246 | `model.layers.0.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4247 | `model.layers.0.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.125 / 46.75 / 0.03337997893492381 / 1.4589691520024404 | [NPY](tensors/0004247.npy) |
| 4248 | `model.layers.0.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.125 / 46.75 / 0.03337997893492381 / 1.4589691520024404 | [NPY](tensors/0004248.npy) |
| 4249 | `model.layers.0.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.9296875 / -0.135650634765625 / 0.8457597571522174 | [NPY](tensors/0004249.npy) |
| 4250 | `model.layers.0` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.75 / 75.5 / 0.07767925262451172 / 3.289671374466639 | [NPY](tensors/0004250.npy) |
| 4329 | `model.layers.0` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0004329.npy) |
| 4330 | `model.layers.0` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004330.npy) |
| 4331 | `model.layers.0` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.9085693359375 / 0.6912552727986224 | [NPY](tensors/0004331.npy) |
| 4332 | `model.layers.0` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.3203125 / -0.004209965467453003 / 0.711058024090348 | [NPY](tensors/0004332.npy) |
| 4333 | `model.layers.0` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 357.0 / 357.0 / 357.0 / 0.0 | [NPY](tensors/0004333.npy) |
| 4334 | `model.layers.0` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4335 | `model.layers.0` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4336 | `model.layers.0` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4337 | `model.layers.0.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0004337.npy) |
| 4338 | `model.layers.0.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004338.npy) |
| 4339 | `model.layers.0.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004339.npy) |
| 4340 | `model.layers.0.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004340.npy) |
| 4341 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 357.0 / 357.0 / 357.0 / 0.0 | [NPY](tensors/0004341.npy) |
| 4342 | `model.layers.0.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4343 | `model.layers.0.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4344 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.9085693359375 / 0.6912552727986224 | [NPY](tensors/0004344.npy) |
| 4345 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.3203125 / -0.004209965467453003 / 0.711058024090348 | [NPY](tensors/0004345.npy) |
| 4346 | `model.layers.0.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4347 | `model.layers.0.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004347.npy) |
| 4348 | `model.layers.0.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 8.0 / 0.0014486645814031363 / 1.027321203413773 | [NPY](tensors/0004348.npy) |
| 4349 | `model.layers.0.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004349.npy) |
| 4350 | `model.layers.0.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.75 / 53.75 / 0.06940409168601036 / 5.734687316339554 | [NPY](tensors/0004350.npy) |
| 4351 | `model.layers.0.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004351.npy) |
| 4352 | `model.layers.0.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.8125 / 3.75 / -0.006423294544219971 / 0.9290448609736645 | [NPY](tensors/0004352.npy) |
| 4353 | `model.layers.0.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.28125 / 3.734375 / -0.003935688430829032 / 0.6258574716574457 | [NPY](tensors/0004353.npy) |
| 4354 | `model.layers.0.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 33.25 / 0.029207546512285867 / 1.052140201003866 | [NPY](tensors/0004354.npy) |
| 4355 | `model.layers.0.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 33.25 / 0.029207546512285867 / 1.052140201003866 | [NPY](tensors/0004355.npy) |
| 4356 | `model.layers.0.self_attn` | 37 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0037157217041494037 / 0.04039990901531398 | [NPY](tensors/0004356.npy) |
| 4357 | `model.layers.0.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.0 / 33.75 / -0.06175657908121745 / 2.952181369808618 | [NPY](tensors/0004357.npy) |
| 4358 | `model.layers.0.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8515625 / 1.6328125 / 0.0030200097295973037 / 0.3334192612153699 | [NPY](tensors/0004358.npy) |
| 4359 | `model.layers.0.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8515625 / 1.6328125 / 0.0030200097295973037 / 0.3334192612153699 | [NPY](tensors/0004359.npy) |
| 4360 | `model.layers.0.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.8515625 / 1.6328125 / 0.0030200097295973037 / 0.3334192612153699 | [NPY](tensors/0004360.npy) |
| 4361 | `model.layers.0.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4362 | `model.layers.0.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4363 | `model.layers.0.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4364 | `model.layers.0.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.328125 / 10.8125 / 0.014385123136970731 / 0.5222198769469043 | [NPY](tensors/0004364.npy) |
| 4365 | `model.layers.0.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.328125 / 10.8125 / 0.014385123136970731 / 0.5222198769469043 | [NPY](tensors/0004365.npy) |
| 4366 | `model.layers.0.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.5625 / 1.4375 / -0.016582489013671875 / 1.3236930396204643 | [NPY](tensors/0004366.npy) |
| 4367 | `model.layers.0` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.25 / 44.0 / -0.04745133188035753 / 2.9890275074432457 | [NPY](tensors/0004367.npy) |
| 4446 | `model.layers.0` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.75 / 32.0 / 0.02612974349823263 / 2.3052590463349314 | [NPY](tensors/0004446.npy) |
| 4447 | `model.layers.0` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004447.npy) |
| 4448 | `model.layers.0` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0234375 / 1.34375 / 0.9233245849609375 / 0.6835210214822701 | [NPY](tensors/0004448.npy) |
| 4449 | `model.layers.0` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.060156017541885376 / 0.6978118882257907 | [NPY](tensors/0004449.npy) |
| 4450 | `model.layers.0` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 358.0 / 358.0 / 358.0 / 0.0 | [NPY](tensors/0004450.npy) |
| 4451 | `model.layers.0` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4452 | `model.layers.0` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4453 | `model.layers.0` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4454 | `model.layers.0.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.75 / 32.0 / 0.02612974349823263 / 2.3052590463349314 | [NPY](tensors/0004454.npy) |
| 4455 | `model.layers.0.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004455.npy) |
| 4456 | `model.layers.0.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004456.npy) |
| 4457 | `model.layers.0.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004457.npy) |
| 4458 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 358.0 / 358.0 / 358.0 / 0.0 | [NPY](tensors/0004458.npy) |
| 4459 | `model.layers.0.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4460 | `model.layers.0.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4461 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0234375 / 1.34375 / 0.9233245849609375 / 0.6835210214822701 | [NPY](tensors/0004461.npy) |
| 4462 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.060156017541885376 / 0.6978118882257907 | [NPY](tensors/0004462.npy) |
| 4463 | `model.layers.0.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4464 | `model.layers.0.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004464.npy) |
| 4465 | `model.layers.0.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.375 / 10.0625 / -0.0011312136193737388 / 1.2762524673806912 | [NPY](tensors/0004465.npy) |
| 4466 | `model.layers.0.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004466.npy) |
| 4467 | `model.layers.0.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.5 / 51.25 / 0.02611599490046501 / 5.9708322691785325 | [NPY](tensors/0004467.npy) |
| 4468 | `model.layers.0.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004468.npy) |
| 4469 | `model.layers.0.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / 0.016116023063659668 / 1.5717161949904705 | [NPY](tensors/0004469.npy) |
| 4470 | `model.layers.0.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.125 / 3.90625 / -0.017357731936499476 / 0.6490590286227359 | [NPY](tensors/0004470.npy) |
| 4471 | `model.layers.0.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.25 / 36.25 / 0.024702034890651703 / 1.1340410136403711 | [NPY](tensors/0004471.npy) |
| 4472 | `model.layers.0.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.25 / 36.25 / 0.024702034890651703 / 1.1340410136403711 | [NPY](tensors/0004472.npy) |
| 4473 | `model.layers.0.self_attn` | 38 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003933037900309023 / 0.049359107322851974 | [NPY](tensors/0004473.npy) |
| 4474 | `model.layers.0.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 39.0 / 0.050742144054836694 / 2.672851369792594 | [NPY](tensors/0004474.npy) |
| 4475 | `model.layers.0.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.578125 / 1.6796875 / 0.014842575788497925 / 0.400123463754498 | [NPY](tensors/0004475.npy) |
| 4476 | `model.layers.0.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.578125 / 1.6796875 / 0.014842575788497925 / 0.400123463754498 | [NPY](tensors/0004476.npy) |
| 4477 | `model.layers.0.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.578125 / 1.6796875 / 0.014842575788497925 / 0.400123463754498 | [NPY](tensors/0004477.npy) |
| 4478 | `model.layers.0.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4479 | `model.layers.0.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4480 | `model.layers.0.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4481 | `model.layers.0.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -12.5625 / 26.0 / 0.0182185634970665 / 1.064938104155346 | [NPY](tensors/0004481.npy) |
| 4482 | `model.layers.0.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.5625 / 26.0 / 0.0182185634970665 / 1.064938104155346 | [NPY](tensors/0004482.npy) |
| 4483 | `model.layers.0.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.640625 / 3.25 / -0.275115966796875 / 1.149920776851178 | [NPY](tensors/0004483.npy) |
| 4484 | `model.layers.0` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.5 / 62.75 / 0.06888033548990885 / 3.1554597087612315 | [NPY](tensors/0004484.npy) |
| 4563 | `model.layers.0` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 38.75 / -0.019637677404615615 / 2.869533421530457 | [NPY](tensors/0004563.npy) |
| 4564 | `model.layers.0` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004564.npy) |
| 4565 | `model.layers.0` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.8929443359375 / 0.7026515532326651 | [NPY](tensors/0004565.npy) |
| 4566 | `model.layers.0` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3203125 / 0.11357763409614563 / 0.7110437810662014 | [NPY](tensors/0004566.npy) |
| 4567 | `model.layers.0` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 359.0 / 359.0 / 359.0 / 0.0 | [NPY](tensors/0004567.npy) |
| 4568 | `model.layers.0` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4569 | `model.layers.0` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4570 | `model.layers.0` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4571 | `model.layers.0.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 38.75 / -0.019637677404615615 / 2.869533421530457 | [NPY](tensors/0004571.npy) |
| 4572 | `model.layers.0.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0004572.npy) |
| 4573 | `model.layers.0.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0004573.npy) |
| 4574 | `model.layers.0.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004574.npy) |
| 4575 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 359.0 / 359.0 / 359.0 / 0.0 | [NPY](tensors/0004575.npy) |
| 4576 | `model.layers.0.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4577 | `model.layers.0.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4578 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.8929443359375 / 0.7026515532326651 | [NPY](tensors/0004578.npy) |
| 4579 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3203125 / 0.11357763409614563 / 0.7110437810662014 | [NPY](tensors/0004579.npy) |
| 4580 | `model.layers.0.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4581 | `model.layers.0.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0004581.npy) |
| 4582 | `model.layers.0.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0 / 9.4375 / 0.009774616220965981 / 1.008080585961609 | [NPY](tensors/0004582.npy) |
| 4583 | `model.layers.0.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0004583.npy) |
| 4584 | `model.layers.0.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.5 / 52.0 / -0.04840673506259918 / 6.119228313490181 | [NPY](tensors/0004584.npy) |
| 4585 | `model.layers.0.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0004585.npy) |
| 4586 | `model.layers.0.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.34375 / 3.625 / -0.03821904957294464 / 0.9543836895451787 | [NPY](tensors/0004586.npy) |
| 4587 | `model.layers.0.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.1875 / 4.15625 / -0.007929348048492102 / 0.5710082508910348 | [NPY](tensors/0004587.npy) |
| 4588 | `model.layers.0.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.46875 / 34.25 / 0.034088687681489524 / 1.0663825381552745 | [NPY](tensors/0004588.npy) |
| 4589 | `model.layers.0.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.46875 / 34.25 / 0.034088687681489524 / 1.0663825381552745 | [NPY](tensors/0004589.npy) |
| 4590 | `model.layers.0.self_attn` | 39 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0034898518800559088 / 0.037211416661364856 | [NPY](tensors/0004590.npy) |
| 4591 | `model.layers.0.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 37.75 / 0.014561385578579373 / 2.857515717660268 | [NPY](tensors/0004591.npy) |
| 4592 | `model.layers.0.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.453125 / 2.109375 / 0.0031276451216803655 / 0.2830868428761776 | [NPY](tensors/0004592.npy) |
| 4593 | `model.layers.0.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.453125 / 2.109375 / 0.0031276451216803655 / 0.2830868428761776 | [NPY](tensors/0004593.npy) |
| 4594 | `model.layers.0.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.453125 / 2.109375 / 0.0031276451216803655 / 0.2830868428761776 | [NPY](tensors/0004594.npy) |
| 4595 | `model.layers.0.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4596 | `model.layers.0.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4597 | `model.layers.0.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4598 | `model.layers.0.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -11.625 / 16.875 / 0.01750413796140088 / 0.7896732580004091 | [NPY](tensors/0004598.npy) |
| 4599 | `model.layers.0.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.625 / 16.875 / 0.01750413796140088 / 0.7896732580004091 | [NPY](tensors/0004599.npy) |
| 4600 | `model.layers.0.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.25 / 1.734375 / -0.015918731689453125 / 1.2442337678942321 | [NPY](tensors/0004600.npy) |
| 4601 | `model.layers.0` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 49.0 / 0.032141400708092585 / 2.980825245341459 | [NPY](tensors/0004601.npy) |
| 4680 | `model.layers.0` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 25.0 / 0.01804563016113308 / 2.3323165527333782 | [NPY](tensors/0004680.npy) |
| 4681 | `model.layers.0` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004681.npy) |
| 4682 | `model.layers.0` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.8425521850585938 / 0.7592463038913561 | [NPY](tensors/0004682.npy) |
| 4683 | `model.layers.0` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.328125 / 0.12352868914604187 / 0.7124125188030568 | [NPY](tensors/0004683.npy) |
| 4684 | `model.layers.0` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 360.0 / 360.0 / 360.0 / 0.0 | [NPY](tensors/0004684.npy) |
| 4685 | `model.layers.0` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4686 | `model.layers.0` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4687 | `model.layers.0` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4688 | `model.layers.0.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 25.0 / 0.01804563016113308 / 2.3323165527333782 | [NPY](tensors/0004688.npy) |
| 4689 | `model.layers.0.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0004689.npy) |
| 4690 | `model.layers.0.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0004690.npy) |
| 4691 | `model.layers.0.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004691.npy) |
| 4692 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 360.0 / 360.0 / 360.0 / 0.0 | [NPY](tensors/0004692.npy) |
| 4693 | `model.layers.0.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4694 | `model.layers.0.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4695 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.8425521850585938 / 0.7592463038913561 | [NPY](tensors/0004695.npy) |
| 4696 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.328125 / 0.12352868914604187 / 0.7124125188030568 | [NPY](tensors/0004696.npy) |
| 4697 | `model.layers.0.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4698 | `model.layers.0.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0004698.npy) |
| 4699 | `model.layers.0.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 8.75 / 0.005578655982390046 / 1.1564340991725837 | [NPY](tensors/0004699.npy) |
| 4700 | `model.layers.0.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0004700.npy) |
| 4701 | `model.layers.0.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -56.25 / 41.75 / -0.16974663734436035 / 5.496621344446725 | [NPY](tensors/0004701.npy) |
| 4702 | `model.layers.0.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0004702.npy) |
| 4703 | `model.layers.0.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.6875 / 4.5 / 0.06943026185035706 / 1.339855997999367 | [NPY](tensors/0004703.npy) |
| 4704 | `model.layers.0.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.3125 / 4.28125 / -0.004713373695267364 / 0.5454579372790479 | [NPY](tensors/0004704.npy) |
| 4705 | `model.layers.0.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.0 / 39.75 / 0.02163189285331302 / 1.289530171265261 | [NPY](tensors/0004705.npy) |
| 4706 | `model.layers.0.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.0 / 39.75 / 0.02163189285331302 / 1.289530171265261 | [NPY](tensors/0004706.npy) |
| 4707 | `model.layers.0.self_attn` | 40 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003124280084725474 / 0.03902725148758927 | [NPY](tensors/0004707.npy) |
| 4708 | `model.layers.0.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.75 / 45.0 / 0.039587110943264434 / 2.8600153828032817 | [NPY](tensors/0004708.npy) |
| 4709 | `model.layers.0.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0625 / 1.484375 / 0.006135178274578519 / 0.2894130043294413 | [NPY](tensors/0004709.npy) |
| 4710 | `model.layers.0.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0625 / 1.484375 / 0.006135178274578519 / 0.2894130043294413 | [NPY](tensors/0004710.npy) |
| 4711 | `model.layers.0.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.0625 / 1.484375 / 0.006135178274578519 / 0.2894130043294413 | [NPY](tensors/0004711.npy) |
| 4712 | `model.layers.0.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4713 | `model.layers.0.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4714 | `model.layers.0.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4715 | `model.layers.0.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.65625 / 21.875 / 0.016914829115072885 / 0.8121232056599926 | [NPY](tensors/0004715.npy) |
| 4716 | `model.layers.0.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.65625 / 21.875 / 0.016914829115072885 / 0.8121232056599926 | [NPY](tensors/0004716.npy) |
| 4717 | `model.layers.0.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.375 / 1.9765625 / -0.15046310424804688 / 0.7054152877032346 | [NPY](tensors/0004717.npy) |
| 4718 | `model.layers.0` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -59.25 / 65.5 / 0.05652949015299479 / 3.225343798338294 | [NPY](tensors/0004718.npy) |
| 4797 | `model.layers.0` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 40.25 / -0.06394515766037835 / 2.6467228965831135 | [NPY](tensors/0004797.npy) |
| 4798 | `model.layers.0` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004798.npy) |
| 4799 | `model.layers.0` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.8165130615234375 / 0.8162570957147703 | [NPY](tensors/0004799.npy) |
| 4800 | `model.layers.0` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.09044128656387329 / 0.6843655856400834 | [NPY](tensors/0004800.npy) |
| 4801 | `model.layers.0` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 361.0 / 361.0 / 361.0 / 0.0 | [NPY](tensors/0004801.npy) |
| 4802 | `model.layers.0` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4803 | `model.layers.0` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4804 | `model.layers.0` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4805 | `model.layers.0.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 40.25 / -0.06394515766037835 / 2.6467228965831135 | [NPY](tensors/0004805.npy) |
| 4806 | `model.layers.0.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004806.npy) |
| 4807 | `model.layers.0.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004807.npy) |
| 4808 | `model.layers.0.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004808.npy) |
| 4809 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 361.0 / 361.0 / 361.0 / 0.0 | [NPY](tensors/0004809.npy) |
| 4810 | `model.layers.0.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4811 | `model.layers.0.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4812 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.8165130615234375 / 0.8162570957147703 | [NPY](tensors/0004812.npy) |
| 4813 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.09044128656387329 / 0.6843655856400834 | [NPY](tensors/0004813.npy) |
| 4814 | `model.layers.0.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4815 | `model.layers.0.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004815.npy) |
| 4816 | `model.layers.0.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.6875 / 7.625 / -0.005639673676341772 / 1.046891081389267 | [NPY](tensors/0004816.npy) |
| 4817 | `model.layers.0.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004817.npy) |
| 4818 | `model.layers.0.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.75 / 51.5 / 0.029395833611488342 / 5.690317737756353 | [NPY](tensors/0004818.npy) |
| 4819 | `model.layers.0.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004819.npy) |
| 4820 | `model.layers.0.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.5625 / 4.03125 / 0.016885966062545776 / 1.1800325387513315 | [NPY](tensors/0004820.npy) |
| 4821 | `model.layers.0.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.40625 / 3.65625 / 0.007604098129377235 / 0.5382079462556537 | [NPY](tensors/0004821.npy) |
| 4822 | `model.layers.0.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.4375 / 39.5 / 0.030327772514687643 / 1.1597167899824763 | [NPY](tensors/0004822.npy) |
| 4823 | `model.layers.0.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.4375 / 39.5 / 0.030327772514687643 / 1.1597167899824763 | [NPY](tensors/0004823.npy) |
| 4824 | `model.layers.0.self_attn` | 41 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003268981403153269 / 0.0337721880677664 | [NPY](tensors/0004824.npy) |
| 4825 | `model.layers.0.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 41.25 / -0.03362155490451389 / 2.9663504750269367 | [NPY](tensors/0004825.npy) |
| 4826 | `model.layers.0.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.859375 / 2.984375 / 0.004317553175820245 / 0.3152066348381209 | [NPY](tensors/0004826.npy) |
| 4827 | `model.layers.0.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.859375 / 2.984375 / 0.004317553175820245 / 0.3152066348381209 | [NPY](tensors/0004827.npy) |
| 4828 | `model.layers.0.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.859375 / 2.984375 / 0.004317553175820245 / 0.3152066348381209 | [NPY](tensors/0004828.npy) |
| 4829 | `model.layers.0.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4830 | `model.layers.0.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4831 | `model.layers.0.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4832 | `model.layers.0.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.28125 / 17.625 / 0.014503641136818462 / 0.7237589071760371 | [NPY](tensors/0004832.npy) |
| 4833 | `model.layers.0.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.28125 / 17.625 / 0.014503641136818462 / 0.7237589071760371 | [NPY](tensors/0004833.npy) |
| 4834 | `model.layers.0.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.703125 / 1.9765625 / -0.05474090576171875 / 1.166707793077389 | [NPY](tensors/0004834.npy) |
| 4835 | `model.layers.0` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 58.5 / -0.01927355130513509 / 3.0822986733519717 | [NPY](tensors/0004835.npy) |
| 4914 | `model.layers.0` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 50.75 / -0.03880806507335769 / 2.8720089898153187 | [NPY](tensors/0004914.npy) |
| 4915 | `model.layers.0` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004915.npy) |
| 4916 | `model.layers.0` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.046875 / 1.34375 / 0.8409137725830078 / 0.7828598309066966 | [NPY](tensors/0004916.npy) |
| 4917 | `model.layers.0` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.05170133709907532 / 0.6983318090469743 | [NPY](tensors/0004917.npy) |
| 4918 | `model.layers.0` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 362.0 / 362.0 / 362.0 / 0.0 | [NPY](tensors/0004918.npy) |
| 4919 | `model.layers.0` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4920 | `model.layers.0` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4921 | `model.layers.0` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4922 | `model.layers.0.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 50.75 / -0.03880806507335769 / 2.8720089898153187 | [NPY](tensors/0004922.npy) |
| 4923 | `model.layers.0.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0004923.npy) |
| 4924 | `model.layers.0.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0004924.npy) |
| 4925 | `model.layers.0.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004925.npy) |
| 4926 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 362.0 / 362.0 / 362.0 / 0.0 | [NPY](tensors/0004926.npy) |
| 4927 | `model.layers.0.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4928 | `model.layers.0.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4929 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.046875 / 1.34375 / 0.8409137725830078 / 0.7828598309066966 | [NPY](tensors/0004929.npy) |
| 4930 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.05170133709907532 / 0.6983318090469743 | [NPY](tensors/0004930.npy) |
| 4931 | `model.layers.0.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4932 | `model.layers.0.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0004932.npy) |
| 4933 | `model.layers.0.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.15625 / 6.84375 / 0.0022307498147711158 / 0.9416562142053898 | [NPY](tensors/0004933.npy) |
| 4934 | `model.layers.0.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0004934.npy) |
| 4935 | `model.layers.0.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.0 / 42.75 / -0.03451061248779297 / 5.165071669827751 | [NPY](tensors/0004935.npy) |
| 4936 | `model.layers.0.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0004936.npy) |
| 4937 | `model.layers.0.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.5625 / 3.5 / 0.010839223861694336 / 0.9793238812790538 | [NPY](tensors/0004937.npy) |
| 4938 | `model.layers.0.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.34375 / 3.75 / 0.006801969197113067 / 0.5868036819292927 | [NPY](tensors/0004938.npy) |
| 4939 | `model.layers.0.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.1875 / 34.0 / 0.04034283885007931 / 1.0462113882399118 | [NPY](tensors/0004939.npy) |
| 4940 | `model.layers.0.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.1875 / 34.0 / 0.04034283885007931 / 1.0462113882399118 | [NPY](tensors/0004940.npy) |
| 4941 | `model.layers.0.self_attn` | 42 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.003624759418872068 / 0.03815890374748309 | [NPY](tensors/0004941.npy) |
| 4942 | `model.layers.0.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 52.5 / 0.0015328566233317057 / 2.9549073667140364 | [NPY](tensors/0004942.npy) |
| 4943 | `model.layers.0.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.671875 / 3.8125 / -0.0016372309790717232 / 0.3019805410379754 | [NPY](tensors/0004943.npy) |
| 4944 | `model.layers.0.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.671875 / 3.8125 / -0.0016372309790717232 / 0.3019805410379754 | [NPY](tensors/0004944.npy) |
| 4945 | `model.layers.0.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.671875 / 3.8125 / -0.0016372309790717232 / 0.3019805410379754 | [NPY](tensors/0004945.npy) |
| 4946 | `model.layers.0.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4947 | `model.layers.0.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4948 | `model.layers.0.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4949 | `model.layers.0.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.4375 / 30.875 / 0.0215025998522631 / 0.9651891012530233 | [NPY](tensors/0004949.npy) |
| 4950 | `model.layers.0.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.4375 / 30.875 / 0.0215025998522631 / 0.9651891012530233 | [NPY](tensors/0004950.npy) |
| 4951 | `model.layers.0.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.21875 / 2.359375 / -0.07779717445373535 / 1.0784154336350622 | [NPY](tensors/0004951.npy) |
| 4952 | `model.layers.0` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 66.5 / 0.023074248101976183 / 3.1453802949924627 | [NPY](tensors/0004952.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -41216.0 / 992.0 / 0.5215798484614748 / 48.15308405959803 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 321, 321] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6894860507172763e+38 / 1.6947574708614093e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 321, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7882230712617297 / 0.8876106672141242 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 321, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.1173851026170974 / 0.6217412290332741 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 321] | torch.int64 → int64 | 0.0 / 320.0 / 160.0 / 92.66426855410162 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -41216.0 / 992.0 / 0.5215798484614748 / 48.15308405959803 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 321, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.06893414784623869 / 3.1586577857453624 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 321, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.06893414784623869 / 3.1586577857453624 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 321, 321] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6894860507172763e+38 / 1.6947574708614093e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 321] | torch.int64 → int64 | 0.0 / 320.0 / 160.0 / 92.66426855410162 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 321, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7882230712617297 / 0.8876106672141242 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 321, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.1173851026170974 / 0.6217412290332741 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.06893414784623869 / 3.1586577857453624 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 321, 4096] | torch.bfloat16 → float32 | -13.0625 / 13.3125 / 0.03622006454415584 / 1.3602279838928002 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.06893414784623869 / 3.1586577857453624 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 321, 512] | torch.bfloat16 → float32 | -41.5 / 45.5 / 0.06888217193501019 / 3.7102619118509166 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.06893414784623869 / 3.1586577857453624 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 321, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.03555568282106584 / 2.5089837265558432 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 321, 4096] | torch.bfloat16 → float32 | -11.75 / 11.3125 / -0.03200253358712264 / 1.5105883187734521 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 321, 2880] | torch.bfloat16 → float32 | -464.0 / 496.0 / -0.038162981728320715 / 6.472189619640965 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -464.0 / 496.0 / -0.038162981728320715 / 6.472189619640965 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 321, 321] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002661644942392659 / 0.016586083845703845 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -41216.0 / 708.0 / 0.48338756401178207 / 47.44937307637045 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 321, 2880] | torch.bfloat16 → float32 | -78.5 / 6.0625 / 0.01038871365549367 / 0.789083436976707 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -78.5 / 6.0625 / 0.01038871365549367 / 0.789083436976707 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [321, 2880] | torch.bfloat16 → float32 | -78.5 / 6.0625 / 0.01038871365549367 / 0.789083436976707 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [321, 2880] | torch.bfloat16 → float32 | -548.0 / 458.0 / 0.11661833702135599 / 9.147674431455835 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -548.0 / 458.0 / 0.11661833702135599 / 9.147674431455835 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [321, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.15515426683277356 / 0.7603005097298884 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 321, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.6000157996336454 / 49.930657709097005 | [NPY](tensors/0000077.npy) |
| 156 | `model.layers.11` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -190.0 / 266.0 / 0.34816758897569444 / 16.37665792224951 | [NPY](tensors/0000156.npy) |
| 157 | `model.layers.11` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000157.npy) |
| 158 | `model.layers.11` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0000158.npy) |
| 159 | `model.layers.11` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0000159.npy) |
| 160 | `model.layers.11` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0000160.npy) |
| 161 | `model.layers.11` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 162 | `model.layers.11` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 163 | `model.layers.11` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 164 | `model.layers.11.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -190.0 / 266.0 / 0.34816758897569444 / 16.37665792224951 | [NPY](tensors/0000164.npy) |
| 165 | `model.layers.11.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.0 / 66.0 / 0.06408125029669867 / 2.512945761441842 | [NPY](tensors/0000165.npy) |
| 166 | `model.layers.11.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.0 / 66.0 / 0.06408125029669867 / 2.512945761441842 | [NPY](tensors/0000166.npy) |
| 167 | `model.layers.11.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000167.npy) |
| 168 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0000168.npy) |
| 169 | `model.layers.11.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 170 | `model.layers.11.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 171 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0000171.npy) |
| 172 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0000172.npy) |
| 173 | `model.layers.11.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 174 | `model.layers.11.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.0 / 66.0 / 0.06408125029669867 / 2.512945761441842 | [NPY](tensors/0000174.npy) |
| 175 | `model.layers.11.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.0 / 11.375 / 0.05902530130697414 / 1.2666047361621133 | [NPY](tensors/0000175.npy) |
| 176 | `model.layers.11.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.0 / 66.0 / 0.06408125029669867 / 2.512945761441842 | [NPY](tensors/0000176.npy) |
| 177 | `model.layers.11.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.625 / 31.625 / 0.08040429651737213 / 3.5430250688405427 | [NPY](tensors/0000177.npy) |
| 178 | `model.layers.11.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.0 / 66.0 / 0.06408125029669867 / 2.512945761441842 | [NPY](tensors/0000178.npy) |
| 179 | `model.layers.11.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.1875 / 9.125 / -0.05340856313705444 / 2.433200375448113 | [NPY](tensors/0000179.npy) |
| 180 | `model.layers.11.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.59375 / 7.03125 / -0.031965481117367744 / 1.4578626965271804 | [NPY](tensors/0000180.npy) |
| 181 | `model.layers.11.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -76.0 / 84.5 / -0.006338728798760308 / 4.163023913737638 | [NPY](tensors/0000181.npy) |
| 182 | `model.layers.11.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -76.0 / 84.5 / -0.006338728798760308 / 4.163023913737638 | [NPY](tensors/0000182.npy) |
| 183 | `model.layers.11.self_attn` | 1 | `output[1]` | [1, 64, 1, 322] | torch.bfloat16 → float32 | 4.547473508864641e-11 / 0.82421875 / 0.002740356221195265 / 0.010534786193776246 | [NPY](tensors/0000183.npy) |
| 184 | `model.layers.11.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -266.0 / 316.0 / 0.3422393798828125 / 18.480843733272245 | [NPY](tensors/0000184.npy) |
| 185 | `model.layers.11.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.0625 / 3.359375 / -0.004651800791422526 / 0.7637277719251336 | [NPY](tensors/0000185.npy) |
| 186 | `model.layers.11.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.0625 / 3.359375 / -0.004651800791422526 / 0.7637277719251336 | [NPY](tensors/0000186.npy) |
| 187 | `model.layers.11.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.0625 / 3.359375 / -0.004651800791422526 / 0.7637277719251336 | [NPY](tensors/0000187.npy) |
| 188 | `model.layers.11.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 189 | `model.layers.11.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 190 | `model.layers.11.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 191 | `model.layers.11.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -47.5 / 110.5 / 0.20532939698961045 / 5.8198421330338475 | [NPY](tensors/0000191.npy) |
| 192 | `model.layers.11.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 110.5 / 0.20532939698961045 / 5.8198421330338475 | [NPY](tensors/0000192.npy) |
| 193 | `model.layers.11.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3828125 / 1.671875 / -0.06954574584960938 / 0.7053602869477814 | [NPY](tensors/0000193.npy) |
| 194 | `model.layers.11` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -308.0 / 424.0 / 0.5470835367838541 / 21.645233141705237 | [NPY](tensors/0000194.npy) |
| 273 | `model.layers.11` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 428.0 / 0.4514492458767361 / 19.381434488257042 | [NPY](tensors/0000273.npy) |
| 274 | `model.layers.11` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000274.npy) |
| 275 | `model.layers.11` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0000275.npy) |
| 276 | `model.layers.11` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0000276.npy) |
| 277 | `model.layers.11` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0000277.npy) |
| 278 | `model.layers.11` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 279 | `model.layers.11` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 280 | `model.layers.11` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 281 | `model.layers.11.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 428.0 / 0.4514492458767361 / 19.381434488257042 | [NPY](tensors/0000281.npy) |
| 282 | `model.layers.11.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 103.5 / 0.06816724605030483 / 3.1383835012002894 | [NPY](tensors/0000282.npy) |
| 283 | `model.layers.11.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 103.5 / 0.06816724605030483 / 3.1383835012002894 | [NPY](tensors/0000283.npy) |
| 284 | `model.layers.11.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000284.npy) |
| 285 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0000285.npy) |
| 286 | `model.layers.11.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 287 | `model.layers.11.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 288 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0000288.npy) |
| 289 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0000289.npy) |
| 290 | `model.layers.11.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 291 | `model.layers.11.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 103.5 / 0.06816724605030483 / 3.1383835012002894 | [NPY](tensors/0000291.npy) |
| 292 | `model.layers.11.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.59375 / 10.375 / 0.048495738534256816 / 1.1970528733146235 | [NPY](tensors/0000292.npy) |
| 293 | `model.layers.11.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 103.5 / 0.06816724605030483 / 3.1383835012002894 | [NPY](tensors/0000293.npy) |
| 294 | `model.layers.11.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.0 / 33.75 / 0.11315283179283142 / 3.383082106742162 | [NPY](tensors/0000294.npy) |
| 295 | `model.layers.11.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 103.5 / 0.06816724605030483 / 3.1383835012002894 | [NPY](tensors/0000295.npy) |
| 296 | `model.layers.11.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.21875 / 5.46875 / -0.026867657899856567 / 1.8687342195659444 | [NPY](tensors/0000296.npy) |
| 297 | `model.layers.11.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.375 / 6.875 / -0.023040420637698844 / 1.4143094064767336 | [NPY](tensors/0000297.npy) |
| 298 | `model.layers.11.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 36.25 / -0.09102261530028449 / 3.737872504523284 | [NPY](tensors/0000298.npy) |
| 299 | `model.layers.11.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -68.0 / 36.25 / -0.09102261530028449 / 3.737872504523284 | [NPY](tensors/0000299.npy) |
| 300 | `model.layers.11.self_attn` | 2 | `output[1]` | [1, 64, 1, 323] | torch.bfloat16 → float32 | 8.185452315956354e-12 / 0.96875 / 0.002895890314299205 / 0.013029193603535043 | [NPY](tensors/0000300.npy) |
| 301 | `model.layers.11.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -276.0 / 360.0 / 0.36028552585177953 / 19.24000554174118 | [NPY](tensors/0000301.npy) |
| 302 | `model.layers.11.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.875 / 3.5 / -0.014519780211978488 / 0.7033623654429434 | [NPY](tensors/0000302.npy) |
| 303 | `model.layers.11.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.875 / 3.5 / -0.014519780211978488 / 0.7033623654429434 | [NPY](tensors/0000303.npy) |
| 304 | `model.layers.11.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.875 / 3.5 / -0.014519780211978488 / 0.7033623654429434 | [NPY](tensors/0000304.npy) |
| 305 | `model.layers.11.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 306 | `model.layers.11.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 307 | `model.layers.11.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 308 | `model.layers.11.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -113.5 / 182.0 / 0.11945957872602675 / 6.83589637661563 | [NPY](tensors/0000308.npy) |
| 309 | `model.layers.11.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -113.5 / 182.0 / 0.11945957872602675 / 6.83589637661563 | [NPY](tensors/0000309.npy) |
| 310 | `model.layers.11.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.546875 / 1.2421875 / -0.07632637023925781 / 0.6548172765402543 | [NPY](tensors/0000310.npy) |
| 311 | `model.layers.11` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -390.0 / 508.0 / 0.4786800808376736 / 23.724884418450962 | [NPY](tensors/0000311.npy) |
| 390 | `model.layers.11` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -251.0 / 354.0 / 0.5759571499294704 / 15.699281871251701 | [NPY](tensors/0000390.npy) |
| 391 | `model.layers.11` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000391.npy) |
| 392 | `model.layers.11` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0000392.npy) |
| 393 | `model.layers.11` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0000393.npy) |
| 394 | `model.layers.11` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0000394.npy) |
| 395 | `model.layers.11` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 396 | `model.layers.11` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 397 | `model.layers.11` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 398 | `model.layers.11.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -251.0 / 354.0 / 0.5759571499294704 / 15.699281871251701 | [NPY](tensors/0000398.npy) |
| 399 | `model.layers.11.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 105.5 / 0.08967484633127848 / 3.218037245006722 | [NPY](tensors/0000399.npy) |
| 400 | `model.layers.11.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 105.5 / 0.08967484633127848 / 3.218037245006722 | [NPY](tensors/0000400.npy) |
| 401 | `model.layers.11.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000401.npy) |
| 402 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0000402.npy) |
| 403 | `model.layers.11.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 404 | `model.layers.11.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 405 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0000405.npy) |
| 406 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0000406.npy) |
| 407 | `model.layers.11.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 408 | `model.layers.11.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 105.5 / 0.08967484633127848 / 3.218037245006722 | [NPY](tensors/0000408.npy) |
| 409 | `model.layers.11.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.15625 / 7.375 / 0.05622295098146424 / 1.2061038160595723 | [NPY](tensors/0000409.npy) |
| 410 | `model.layers.11.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 105.5 / 0.08967484633127848 / 3.218037245006722 | [NPY](tensors/0000410.npy) |
| 411 | `model.layers.11.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 36.5 / 0.11366719007492065 / 3.7687332871071733 | [NPY](tensors/0000411.npy) |
| 412 | `model.layers.11.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 105.5 / 0.08967484633127848 / 3.218037245006722 | [NPY](tensors/0000412.npy) |
| 413 | `model.layers.11.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.125 / 6.78125 / -0.023620426654815674 / 1.8641467023867213 | [NPY](tensors/0000413.npy) |
| 414 | `model.layers.11.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.71875 / 6.46875 / -0.0027239457704126835 / 1.3579320486575854 | [NPY](tensors/0000414.npy) |
| 415 | `model.layers.11.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 20.375 / 0.0024639586607615154 / 3.261257089130993 | [NPY](tensors/0000415.npy) |
| 416 | `model.layers.11.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 20.375 / 0.0024639586607615154 / 3.261257089130993 | [NPY](tensors/0000416.npy) |
| 417 | `model.layers.11.self_attn` | 3 | `output[1]` | [1, 64, 1, 324] | torch.bfloat16 → float32 | 1.8530954548623413e-11 / 0.91796875 / 0.002925774632381162 / 0.01226711962722349 | [NPY](tensors/0000417.npy) |
| 418 | `model.layers.11.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -235.0 / 316.0 / 0.5781032562255859 / 16.178988163455653 | [NPY](tensors/0000418.npy) |
| 419 | `model.layers.11.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 3.046875 / 0.010875085989634195 / 0.6677710116536332 | [NPY](tensors/0000419.npy) |
| 420 | `model.layers.11.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 3.046875 / 0.010875085989634195 / 0.6677710116536332 | [NPY](tensors/0000420.npy) |
| 421 | `model.layers.11.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.8125 / 3.046875 / 0.010875085989634195 / 0.6677710116536332 | [NPY](tensors/0000421.npy) |
| 422 | `model.layers.11.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 423 | `model.layers.11.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 424 | `model.layers.11.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 425 | `model.layers.11.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -76.0 / 92.5 / 0.12842438750796847 / 4.609490614186081 | [NPY](tensors/0000425.npy) |
| 426 | `model.layers.11.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -76.0 / 92.5 / 0.12842438750796847 / 4.609490614186081 | [NPY](tensors/0000426.npy) |
| 427 | `model.layers.11.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3203125 / 0.72265625 / -0.07007980346679688 / 0.5023281670086108 | [NPY](tensors/0000427.npy) |
| 428 | `model.layers.11` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 384.0 / 0.7056458367241754 / 18.819137482513476 | [NPY](tensors/0000428.npy) |
| 507 | `model.layers.11` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -462.0 / 548.0 / 0.666340806749132 / 21.995838145414208 | [NPY](tensors/0000507.npy) |
| 508 | `model.layers.11` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000508.npy) |
| 509 | `model.layers.11` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0000509.npy) |
| 510 | `model.layers.11` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0000510.npy) |
| 511 | `model.layers.11` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0000511.npy) |
| 512 | `model.layers.11` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 513 | `model.layers.11` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 514 | `model.layers.11` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 515 | `model.layers.11.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -462.0 / 548.0 / 0.666340806749132 / 21.995838145414208 | [NPY](tensors/0000515.npy) |
| 516 | `model.layers.11.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -110.0 / 116.0 / 0.0719241061144405 / 3.6079361171799227 | [NPY](tensors/0000516.npy) |
| 517 | `model.layers.11.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -110.0 / 116.0 / 0.0719241061144405 / 3.6079361171799227 | [NPY](tensors/0000517.npy) |
| 518 | `model.layers.11.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000518.npy) |
| 519 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0000519.npy) |
| 520 | `model.layers.11.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 521 | `model.layers.11.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 522 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0000522.npy) |
| 523 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0000523.npy) |
| 524 | `model.layers.11.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 525 | `model.layers.11.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -110.0 / 116.0 / 0.0719241061144405 / 3.6079361171799227 | [NPY](tensors/0000525.npy) |
| 526 | `model.layers.11.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5625 / 7.09375 / 0.031810306711122394 / 1.1171160562686873 | [NPY](tensors/0000526.npy) |
| 527 | `model.layers.11.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -110.0 / 116.0 / 0.0719241061144405 / 3.6079361171799227 | [NPY](tensors/0000527.npy) |
| 528 | `model.layers.11.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.125 / 43.0 / 0.016645312309265137 / 3.8725432744818584 | [NPY](tensors/0000528.npy) |
| 529 | `model.layers.11.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -110.0 / 116.0 / 0.0719241061144405 / 3.6079361171799227 | [NPY](tensors/0000529.npy) |
| 530 | `model.layers.11.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.6875 / 6.0 / -0.00707089900970459 / 2.063780866387819 | [NPY](tensors/0000530.npy) |
| 531 | `model.layers.11.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.6875 / 6.53125 / 0.013981439522467554 / 1.3489028903097808 | [NPY](tensors/0000531.npy) |
| 532 | `model.layers.11.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.0 / 138.0 / 0.0535073889626397 / 4.904563967919153 | [NPY](tensors/0000532.npy) |
| 533 | `model.layers.11.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.0 / 138.0 / 0.0535073889626397 / 4.904563967919153 | [NPY](tensors/0000533.npy) |
| 534 | `model.layers.11.self_attn` | 4 | `output[1]` | [1, 64, 1, 325] | torch.bfloat16 → float32 | 3.865352482534945e-12 / 0.96875 / 0.0027902183333907505 / 0.015509670260810808 | [NPY](tensors/0000534.npy) |
| 535 | `model.layers.11.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -324.0 / 482.0 / 0.7204477945963542 / 20.662773332066518 | [NPY](tensors/0000535.npy) |
| 536 | `model.layers.11.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.90625 / 3.0625 / 0.02125250630908542 / 0.6718973814631312 | [NPY](tensors/0000536.npy) |
| 537 | `model.layers.11.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.90625 / 3.0625 / 0.02125250630908542 / 0.6718973814631312 | [NPY](tensors/0000537.npy) |
| 538 | `model.layers.11.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.90625 / 3.0625 / 0.02125250630908542 / 0.6718973814631312 | [NPY](tensors/0000538.npy) |
| 539 | `model.layers.11.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 540 | `model.layers.11.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 541 | `model.layers.11.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 542 | `model.layers.11.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -274.0 / 210.0 / 0.2160838418536716 / 8.690638561943638 | [NPY](tensors/0000542.npy) |
| 543 | `model.layers.11.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -274.0 / 210.0 / 0.2160838418536716 / 8.690638561943638 | [NPY](tensors/0000543.npy) |
| 544 | `model.layers.11.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.1640625 / 1.078125 / -0.0463104248046875 / 0.5186366985775515 | [NPY](tensors/0000544.npy) |
| 545 | `model.layers.11` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -600.0 / 656.0 / 0.9367574055989584 / 26.79598714509143 | [NPY](tensors/0000545.npy) |
| 624 | `model.layers.11` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -560.0 / 544.0 / 0.5602288987901476 / 22.809622552099817 | [NPY](tensors/0000624.npy) |
| 625 | `model.layers.11` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000625.npy) |
| 626 | `model.layers.11` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0000626.npy) |
| 627 | `model.layers.11` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0000627.npy) |
| 628 | `model.layers.11` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0000628.npy) |
| 629 | `model.layers.11` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 630 | `model.layers.11` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 631 | `model.layers.11` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 632 | `model.layers.11.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -560.0 / 544.0 / 0.5602288987901476 / 22.809622552099817 | [NPY](tensors/0000632.npy) |
| 633 | `model.layers.11.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -129.0 / 112.0 / 0.05051686763763428 / 3.683390069992614 | [NPY](tensors/0000633.npy) |
| 634 | `model.layers.11.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -129.0 / 112.0 / 0.05051686763763428 / 3.683390069992614 | [NPY](tensors/0000634.npy) |
| 635 | `model.layers.11.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000635.npy) |
| 636 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0000636.npy) |
| 637 | `model.layers.11.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 638 | `model.layers.11.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 639 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0000639.npy) |
| 640 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0000640.npy) |
| 641 | `model.layers.11.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 642 | `model.layers.11.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -129.0 / 112.0 / 0.05051686763763428 / 3.683390069992614 | [NPY](tensors/0000642.npy) |
| 643 | `model.layers.11.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.84375 / 7.28125 / 0.03095873584970832 / 1.1046515414607316 | [NPY](tensors/0000643.npy) |
| 644 | `model.layers.11.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -129.0 / 112.0 / 0.05051686763763428 / 3.683390069992614 | [NPY](tensors/0000644.npy) |
| 645 | `model.layers.11.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.625 / 43.25 / -0.01363229751586914 / 3.9010650440550023 | [NPY](tensors/0000645.npy) |
| 646 | `model.layers.11.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -129.0 / 112.0 / 0.05051686763763428 / 3.683390069992614 | [NPY](tensors/0000646.npy) |
| 647 | `model.layers.11.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.96875 / 7.0 / -0.02093517780303955 / 2.0992159884161503 | [NPY](tensors/0000647.npy) |
| 648 | `model.layers.11.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.6875 / 6.40625 / 0.002561355708166957 / 1.26396727302133 | [NPY](tensors/0000648.npy) |
| 649 | `model.layers.11.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -194.0 / 216.0 / -0.07250506348080105 / 6.54339599443339 | [NPY](tensors/0000649.npy) |
| 650 | `model.layers.11.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -194.0 / 216.0 / -0.07250506348080105 / 6.54339599443339 | [NPY](tensors/0000650.npy) |
| 651 | `model.layers.11.self_attn` | 5 | `output[1]` | [1, 64, 1, 326] | torch.bfloat16 → float32 | 1.5654144647214707e-14 / 0.96484375 / 0.0026623842660563543 / 0.01679134780088106 | [NPY](tensors/0000651.npy) |
| 652 | `model.layers.11.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -344.0 / 372.0 / 0.4873361375596788 / 19.461231140794407 | [NPY](tensors/0000652.npy) |
| 653 | `model.layers.11.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.921875 / 3.671875 / 0.01983743906021118 / 0.7051836695361422 | [NPY](tensors/0000653.npy) |
| 654 | `model.layers.11.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.921875 / 3.671875 / 0.01983743906021118 / 0.7051836695361422 | [NPY](tensors/0000654.npy) |
| 655 | `model.layers.11.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.921875 / 3.671875 / 0.01983743906021118 / 0.7051836695361422 | [NPY](tensors/0000655.npy) |
| 656 | `model.layers.11.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 657 | `model.layers.11.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 658 | `model.layers.11.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 659 | `model.layers.11.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -372.0 / 264.0 / 0.014748483233981662 / 11.003058531846786 | [NPY](tensors/0000659.npy) |
| 660 | `model.layers.11.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -372.0 / 264.0 / 0.014748483233981662 / 11.003058531846786 | [NPY](tensors/0000660.npy) |
| 661 | `model.layers.11.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.671875 / 1.390625 / -0.15509986877441406 / 0.7594946276082406 | [NPY](tensors/0000661.npy) |
| 662 | `model.layers.11` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -716.0 / 616.0 / 0.5030841403537326 / 27.41118699689867 | [NPY](tensors/0000662.npy) |
| 741 | `model.layers.11` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -272.0 / 424.0 / 0.8311570909288194 / 17.630941342675772 | [NPY](tensors/0000741.npy) |
| 742 | `model.layers.11` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000742.npy) |
| 743 | `model.layers.11` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0000743.npy) |
| 744 | `model.layers.11` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0000744.npy) |
| 745 | `model.layers.11` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0000745.npy) |
| 746 | `model.layers.11` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 747 | `model.layers.11` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 748 | `model.layers.11` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 749 | `model.layers.11.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -272.0 / 424.0 / 0.8311570909288194 / 17.630941342675772 | [NPY](tensors/0000749.npy) |
| 750 | `model.layers.11.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -81.0 / 106.0 / 0.10892839034398397 / 3.2761266246969196 | [NPY](tensors/0000750.npy) |
| 751 | `model.layers.11.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -81.0 / 106.0 / 0.10892839034398397 / 3.2761266246969196 | [NPY](tensors/0000751.npy) |
| 752 | `model.layers.11.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000752.npy) |
| 753 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0000753.npy) |
| 754 | `model.layers.11.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 755 | `model.layers.11.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 756 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0000756.npy) |
| 757 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0000757.npy) |
| 758 | `model.layers.11.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 759 | `model.layers.11.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -81.0 / 106.0 / 0.10892839034398397 / 3.2761266246969196 | [NPY](tensors/0000759.npy) |
| 760 | `model.layers.11.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.46875 / 7.53125 / 0.047103270335355774 / 1.1883922346223632 | [NPY](tensors/0000760.npy) |
| 761 | `model.layers.11.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -81.0 / 106.0 / 0.10892839034398397 / 3.2761266246969196 | [NPY](tensors/0000761.npy) |
| 762 | `model.layers.11.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.5 / 43.5 / 0.08063486218452454 / 4.176664468562635 | [NPY](tensors/0000762.npy) |
| 763 | `model.layers.11.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -81.0 / 106.0 / 0.10892839034398397 / 3.2761266246969196 | [NPY](tensors/0000763.npy) |
| 764 | `model.layers.11.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.8125 / 8.5 / 0.048418402671813965 / 2.1302096309656977 | [NPY](tensors/0000764.npy) |
| 765 | `model.layers.11.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.625 / 6.0 / 0.0011467430740594864 / 1.3110342129690926 | [NPY](tensors/0000765.npy) |
| 766 | `model.layers.11.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.25 / 96.5 / 0.0661834822760688 / 3.964360165623321 | [NPY](tensors/0000766.npy) |
| 767 | `model.layers.11.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.25 / 96.5 / 0.0661834822760688 / 3.964360165623321 | [NPY](tensors/0000767.npy) |
| 768 | `model.layers.11.self_attn` | 6 | `output[1]` | [1, 64, 1, 327] | torch.bfloat16 → float32 | 6.0822458181064576e-12 / 0.92578125 / 0.002836998535199312 / 0.011567810234094537 | [NPY](tensors/0000768.npy) |
| 769 | `model.layers.11.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -256.0 / 436.0 / 0.8976126776801215 / 18.97597939503545 | [NPY](tensors/0000769.npy) |
| 770 | `model.layers.11.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.21875 / 2.46875 / 0.020004271136389837 / 0.6530003791223326 | [NPY](tensors/0000770.npy) |
| 771 | `model.layers.11.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.21875 / 2.46875 / 0.020004271136389837 / 0.6530003791223326 | [NPY](tensors/0000771.npy) |
| 772 | `model.layers.11.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.21875 / 2.46875 / 0.020004271136389837 / 0.6530003791223326 | [NPY](tensors/0000772.npy) |
| 773 | `model.layers.11.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 774 | `model.layers.11.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 775 | `model.layers.11.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 776 | `model.layers.11.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -90.5 / 118.0 / 0.1771842810842726 / 5.0459632966224275 | [NPY](tensors/0000776.npy) |
| 777 | `model.layers.11.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 118.0 / 0.1771842810842726 / 5.0459632966224275 | [NPY](tensors/0000777.npy) |
| 778 | `model.layers.11.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.875 / 1.0078125 / -0.019571304321289062 / 0.40836173026948464 | [NPY](tensors/0000778.npy) |
| 779 | `model.layers.11` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -346.0 / 524.0 / 1.0757975260416666 / 22.024705624396244 | [NPY](tensors/0000779.npy) |
| 858 | `model.layers.11` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -330.0 / 472.0 / 0.6089832941691081 / 20.605328937280873 | [NPY](tensors/0000858.npy) |
| 859 | `model.layers.11` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000859.npy) |
| 860 | `model.layers.11` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0000860.npy) |
| 861 | `model.layers.11` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0000861.npy) |
| 862 | `model.layers.11` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0000862.npy) |
| 863 | `model.layers.11` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 864 | `model.layers.11` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 865 | `model.layers.11` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 866 | `model.layers.11.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -330.0 / 472.0 / 0.6089832941691081 / 20.605328937280873 | [NPY](tensors/0000866.npy) |
| 867 | `model.layers.11.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 107.5 / 0.0764281474881702 / 3.30136574191531 | [NPY](tensors/0000867.npy) |
| 868 | `model.layers.11.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 107.5 / 0.0764281474881702 / 3.30136574191531 | [NPY](tensors/0000868.npy) |
| 869 | `model.layers.11.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000869.npy) |
| 870 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0000870.npy) |
| 871 | `model.layers.11.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 872 | `model.layers.11.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 873 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0000873.npy) |
| 874 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0000874.npy) |
| 875 | `model.layers.11.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 876 | `model.layers.11.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 107.5 / 0.0764281474881702 / 3.30136574191531 | [NPY](tensors/0000876.npy) |
| 877 | `model.layers.11.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.71875 / 7.59375 / 0.032366417115554214 / 1.1768123000564676 | [NPY](tensors/0000877.npy) |
| 878 | `model.layers.11.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 107.5 / 0.0764281474881702 / 3.30136574191531 | [NPY](tensors/0000878.npy) |
| 879 | `model.layers.11.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 36.5 / 0.16237892396748066 / 3.646524463616039 | [NPY](tensors/0000879.npy) |
| 880 | `model.layers.11.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.0 / 107.5 / 0.0764281474881702 / 3.30136574191531 | [NPY](tensors/0000880.npy) |
| 881 | `model.layers.11.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.90625 / 4.90625 / -0.15166109800338745 / 1.7496844511455503 | [NPY](tensors/0000881.npy) |
| 882 | `model.layers.11.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.59375 / 7.875 / -0.03522326401434839 / 1.418888599294929 | [NPY](tensors/0000882.npy) |
| 883 | `model.layers.11.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -74.0 / 63.75 / 0.017084370719061957 / 4.234064431992024 | [NPY](tensors/0000883.npy) |
| 884 | `model.layers.11.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -74.0 / 63.75 / 0.017084370719061957 / 4.234064431992024 | [NPY](tensors/0000884.npy) |
| 885 | `model.layers.11.self_attn` | 7 | `output[1]` | [1, 64, 1, 328] | torch.bfloat16 → float32 | 4.014566457044566e-13 / 0.95703125 / 0.0028210982080113787 / 0.011310868227604836 | [NPY](tensors/0000885.npy) |
| 886 | `model.layers.11.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -296.0 / 428.0 / 0.625496588812934 / 20.954480424722274 | [NPY](tensors/0000886.npy) |
| 887 | `model.layers.11.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.96875 / 2.984375 / 0.005937997500101725 / 0.6602637572563502 | [NPY](tensors/0000887.npy) |
| 888 | `model.layers.11.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.96875 / 2.984375 / 0.005937997500101725 / 0.6602637572563502 | [NPY](tensors/0000888.npy) |
| 889 | `model.layers.11.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.96875 / 2.984375 / 0.005937997500101725 / 0.6602637572563502 | [NPY](tensors/0000889.npy) |
| 890 | `model.layers.11.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 891 | `model.layers.11.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 892 | `model.layers.11.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 893 | `model.layers.11.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -119.0 / 201.0 / 0.10619206958346897 / 6.156416803970403 | [NPY](tensors/0000893.npy) |
| 894 | `model.layers.11.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -119.0 / 201.0 / 0.10619206958346897 / 6.156416803970403 | [NPY](tensors/0000894.npy) |
| 895 | `model.layers.11.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3671875 / 0.84765625 / -0.07039451599121094 / 0.513148644300153 | [NPY](tensors/0000895.npy) |
| 896 | `model.layers.11` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -416.0 / 600.0 / 0.7314785427517361 / 25.104657461588697 | [NPY](tensors/0000896.npy) |
| 975 | `model.layers.11` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -436.0 / 480.0 / 0.3712683783637153 / 20.941805571483233 | [NPY](tensors/0000975.npy) |
| 976 | `model.layers.11` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000976.npy) |
| 977 | `model.layers.11` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0000977.npy) |
| 978 | `model.layers.11` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0000978.npy) |
| 979 | `model.layers.11` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0000979.npy) |
| 980 | `model.layers.11` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 981 | `model.layers.11` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 982 | `model.layers.11` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 983 | `model.layers.11.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -436.0 / 480.0 / 0.3712683783637153 / 20.941805571483233 | [NPY](tensors/0000983.npy) |
| 984 | `model.layers.11.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.5 / 107.5 / 0.04843082163068983 / 3.484291102787908 | [NPY](tensors/0000984.npy) |
| 985 | `model.layers.11.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.5 / 107.5 / 0.04843082163068983 / 3.484291102787908 | [NPY](tensors/0000985.npy) |
| 986 | `model.layers.11.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000986.npy) |
| 987 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0000987.npy) |
| 988 | `model.layers.11.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 989 | `model.layers.11.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 990 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0000990.npy) |
| 991 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0000991.npy) |
| 992 | `model.layers.11.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 993 | `model.layers.11.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.5 / 107.5 / 0.04843082163068983 / 3.484291102787908 | [NPY](tensors/0000993.npy) |
| 994 | `model.layers.11.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 7.5625 / 0.013527132105082273 / 1.210181186270146 | [NPY](tensors/0000994.npy) |
| 995 | `model.layers.11.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.5 / 107.5 / 0.04843082163068983 / 3.484291102787908 | [NPY](tensors/0000995.npy) |
| 996 | `model.layers.11.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.5 / 39.75 / -0.005795717239379883 / 4.087032215724055 | [NPY](tensors/0000996.npy) |
| 997 | `model.layers.11.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.5 / 107.5 / 0.04843082163068983 / 3.484291102787908 | [NPY](tensors/0000997.npy) |
| 998 | `model.layers.11.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.375 / 7.125 / 0.03422504663467407 / 1.9721740669854062 | [NPY](tensors/0000998.npy) |
| 999 | `model.layers.11.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.03125 / 6.09375 / -0.006260526366531849 / 1.287399508939904 | [NPY](tensors/0000999.npy) |
| 1000 | `model.layers.11.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.0 / 151.0 / 0.043493449687957764 / 4.752916073419127 | [NPY](tensors/0001000.npy) |
| 1001 | `model.layers.11.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.0 / 151.0 / 0.043493449687957764 / 4.752916073419127 | [NPY](tensors/0001001.npy) |
| 1002 | `model.layers.11.self_attn` | 8 | `output[1]` | [1, 64, 1, 329] | torch.bfloat16 → float32 | 2.362554596402333e-13 / 0.9296875 / 0.0027739439332694705 / 0.013120198621315093 | [NPY](tensors/0001002.npy) |
| 1003 | `model.layers.11.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -284.0 / 396.0 / 0.41556040445963544 / 20.06444008624151 | [NPY](tensors/0001003.npy) |
| 1004 | `model.layers.11.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.21875 / 2.84375 / 0.010349573691685994 / 0.6748278194088418 | [NPY](tensors/0001004.npy) |
| 1005 | `model.layers.11.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.21875 / 2.84375 / 0.010349573691685994 / 0.6748278194088418 | [NPY](tensors/0001005.npy) |
| 1006 | `model.layers.11.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.21875 / 2.84375 / 0.010349573691685994 / 0.6748278194088418 | [NPY](tensors/0001006.npy) |
| 1007 | `model.layers.11.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1008 | `model.layers.11.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1009 | `model.layers.11.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1010 | `model.layers.11.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -195.0 / 181.0 / 0.09680116441514756 / 6.924262955401076 | [NPY](tensors/0001010.npy) |
| 1011 | `model.layers.11.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -195.0 / 181.0 / 0.09680116441514756 / 6.924262955401076 | [NPY](tensors/0001011.npy) |
| 1012 | `model.layers.11.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8203125 / 1.140625 / -0.132415771484375 / 0.6255110253361296 | [NPY](tensors/0001012.npy) |
| 1013 | `model.layers.11` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -480.0 / 576.0 / 0.5123606363932292 / 24.734500631801655 | [NPY](tensors/0001013.npy) |
| 1092 | `model.layers.11` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -280.0 / 504.0 / 0.387506103515625 / 19.64666762972169 | [NPY](tensors/0001092.npy) |
| 1093 | `model.layers.11` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 330] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001093.npy) |
| 1094 | `model.layers.11` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0001094.npy) |
| 1095 | `model.layers.11` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0001095.npy) |
| 1096 | `model.layers.11` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0001096.npy) |
| 1097 | `model.layers.11` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1098 | `model.layers.11` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1099 | `model.layers.11` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1100 | `model.layers.11.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -280.0 / 504.0 / 0.387506103515625 / 19.64666762972169 | [NPY](tensors/0001100.npy) |
| 1101 | `model.layers.11.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.0 / 120.0 / 0.06833715306388008 / 3.3564816807247717 | [NPY](tensors/0001101.npy) |
| 1102 | `model.layers.11.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.0 / 120.0 / 0.06833715306388008 / 3.3564816807247717 | [NPY](tensors/0001102.npy) |
| 1103 | `model.layers.11.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 330] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001103.npy) |
| 1104 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0001104.npy) |
| 1105 | `model.layers.11.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1106 | `model.layers.11.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1107 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0001107.npy) |
| 1108 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0001108.npy) |
| 1109 | `model.layers.11.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1110 | `model.layers.11.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.0 / 120.0 / 0.06833715306388008 / 3.3564816807247717 | [NPY](tensors/0001110.npy) |
| 1111 | `model.layers.11.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.5 / 7.46875 / 0.024661932606250048 / 1.253297401795589 | [NPY](tensors/0001111.npy) |
| 1112 | `model.layers.11.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.0 / 120.0 / 0.06833715306388008 / 3.3564816807247717 | [NPY](tensors/0001112.npy) |
| 1113 | `model.layers.11.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.5 / 35.0 / 0.0984429121017456 / 3.8965209915075167 | [NPY](tensors/0001113.npy) |
| 1114 | `model.layers.11.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.0 / 120.0 / 0.06833715306388008 / 3.3564816807247717 | [NPY](tensors/0001114.npy) |
| 1115 | `model.layers.11.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.625 / 6.21875 / -0.09012532234191895 / 2.1611247848252604 | [NPY](tensors/0001115.npy) |
| 1116 | `model.layers.11.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.09375 / 6.34375 / -0.04296604450792074 / 1.5002548603718568 | [NPY](tensors/0001116.npy) |
| 1117 | `model.layers.11.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -59.5 / 66.5 / 0.013945515950520833 / 4.1731230548004135 | [NPY](tensors/0001117.npy) |
| 1118 | `model.layers.11.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -59.5 / 66.5 / 0.013945515950520833 / 4.1731230548004135 | [NPY](tensors/0001118.npy) |
| 1119 | `model.layers.11.self_attn` | 9 | `output[1]` | [1, 64, 1, 330] | torch.bfloat16 → float32 | 6.30961949354969e-12 / 0.9609375 / 0.0028492338368239626 / 0.012220773638428441 | [NPY](tensors/0001119.npy) |
| 1120 | `model.layers.11.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -241.0 / 444.0 / 0.4006477355957031 / 20.33975627660439 | [NPY](tensors/0001120.npy) |
| 1121 | `model.layers.11.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5625 / 2.4375 / 0.003032799230681525 / 0.6744868578749621 | [NPY](tensors/0001121.npy) |
| 1122 | `model.layers.11.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5625 / 2.4375 / 0.003032799230681525 / 0.6744868578749621 | [NPY](tensors/0001122.npy) |
| 1123 | `model.layers.11.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.5625 / 2.4375 / 0.003032799230681525 / 0.6744868578749621 | [NPY](tensors/0001123.npy) |
| 1124 | `model.layers.11.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1125 | `model.layers.11.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1126 | `model.layers.11.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1127 | `model.layers.11.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -158.0 / 216.0 / 0.13471044964260526 / 7.280466329901417 | [NPY](tensors/0001127.npy) |
| 1128 | `model.layers.11.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -158.0 / 216.0 / 0.13471044964260526 / 7.280466329901417 | [NPY](tensors/0001128.npy) |
| 1129 | `model.layers.11.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.96484375 / 0.875 / -0.09901022911071777 / 0.4610210281124945 | [NPY](tensors/0001129.npy) |
| 1130 | `model.layers.11` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -400.0 / 660.0 / 0.5346015082465277 / 25.33367425618767 | [NPY](tensors/0001130.npy) |
| 1209 | `model.layers.11` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -358.0 / 564.0 / 0.4384702894422743 / 21.784699520530186 | [NPY](tensors/0001209.npy) |
| 1210 | `model.layers.11` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 331] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001210.npy) |
| 1211 | `model.layers.11` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0001211.npy) |
| 1212 | `model.layers.11` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0001212.npy) |
| 1213 | `model.layers.11` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0001213.npy) |
| 1214 | `model.layers.11` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1215 | `model.layers.11` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1216 | `model.layers.11` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1217 | `model.layers.11.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -358.0 / 564.0 / 0.4384702894422743 / 21.784699520530186 | [NPY](tensors/0001217.npy) |
| 1218 | `model.layers.11.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 121.5 / 0.07030158042907715 / 3.447666114941362 | [NPY](tensors/0001218.npy) |
| 1219 | `model.layers.11.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 121.5 / 0.07030158042907715 / 3.447666114941362 | [NPY](tensors/0001219.npy) |
| 1220 | `model.layers.11.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 331] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001220.npy) |
| 1221 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0001221.npy) |
| 1222 | `model.layers.11.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1223 | `model.layers.11.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1224 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0001224.npy) |
| 1225 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0001225.npy) |
| 1226 | `model.layers.11.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1227 | `model.layers.11.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 121.5 / 0.07030158042907715 / 3.447666114941362 | [NPY](tensors/0001227.npy) |
| 1228 | `model.layers.11.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.375 / 8.0625 / 0.018910238437456428 / 1.3048531435181445 | [NPY](tensors/0001228.npy) |
| 1229 | `model.layers.11.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 121.5 / 0.07030158042907715 / 3.447666114941362 | [NPY](tensors/0001229.npy) |
| 1230 | `model.layers.11.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 38.75 / 0.014514684677124023 / 4.175206668090403 | [NPY](tensors/0001230.npy) |
| 1231 | `model.layers.11.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 121.5 / 0.07030158042907715 / 3.447666114941362 | [NPY](tensors/0001231.npy) |
| 1232 | `model.layers.11.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.8125 / 9.6875 / -0.08068738877773285 / 2.4114618585600134 | [NPY](tensors/0001232.npy) |
| 1233 | `model.layers.11.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.4375 / 7.125 / -0.05474944703746587 / 1.7394698952807512 | [NPY](tensors/0001233.npy) |
| 1234 | `model.layers.11.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 97.5 / 0.04376859101984236 / 4.517686186628403 | [NPY](tensors/0001234.npy) |
| 1235 | `model.layers.11.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 97.5 / 0.04376859101984236 / 4.517686186628403 | [NPY](tensors/0001235.npy) |
| 1236 | `model.layers.11.self_attn` | 10 | `output[1]` | [1, 64, 1, 331] | torch.bfloat16 → float32 | 3.8546943414985435e-13 / 0.9609375 / 0.002832870995135972 / 0.013172495637490051 | [NPY](tensors/0001236.npy) |
| 1237 | `model.layers.11.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -340.0 / 528.0 / 0.48385365804036456 / 23.084503465658308 | [NPY](tensors/0001237.npy) |
| 1238 | `model.layers.11.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 3.171875 / 0.006977510452270508 / 0.655862503464481 | [NPY](tensors/0001238.npy) |
| 1239 | `model.layers.11.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 3.171875 / 0.006977510452270508 / 0.655862503464481 | [NPY](tensors/0001239.npy) |
| 1240 | `model.layers.11.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.8125 / 3.171875 / 0.006977510452270508 / 0.655862503464481 | [NPY](tensors/0001240.npy) |
| 1241 | `model.layers.11.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1242 | `model.layers.11.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1243 | `model.layers.11.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1244 | `model.layers.11.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -129.0 / 228.0 / 0.04163855181799995 / 7.325648277246264 | [NPY](tensors/0001244.npy) |
| 1245 | `model.layers.11.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -129.0 / 228.0 / 0.04163855181799995 / 7.325648277246264 | [NPY](tensors/0001245.npy) |
| 1246 | `model.layers.11.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.88671875 / 0.99609375 / -0.0772702693939209 / 0.4703156860168346 | [NPY](tensors/0001246.npy) |
| 1247 | `model.layers.11` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -468.0 / 756.0 / 0.5262488471137152 / 28.108790276720427 | [NPY](tensors/0001247.npy) |
| 1326 | `model.layers.11` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -181.0 / 334.0 / 0.5775766160753039 / 17.004766822138542 | [NPY](tensors/0001326.npy) |
| 1327 | `model.layers.11` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 332] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001327.npy) |
| 1328 | `model.layers.11` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0001328.npy) |
| 1329 | `model.layers.11` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0001329.npy) |
| 1330 | `model.layers.11` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0001330.npy) |
| 1331 | `model.layers.11` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1332 | `model.layers.11` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1333 | `model.layers.11` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1334 | `model.layers.11.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -181.0 / 334.0 / 0.5775766160753039 / 17.004766822138542 | [NPY](tensors/0001334.npy) |
| 1335 | `model.layers.11.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.75 / 92.0 / 0.09405488636758592 / 2.9632254674961205 | [NPY](tensors/0001335.npy) |
| 1336 | `model.layers.11.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.75 / 92.0 / 0.09405488636758592 / 2.9632254674961205 | [NPY](tensors/0001336.npy) |
| 1337 | `model.layers.11.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 332] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001337.npy) |
| 1338 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0001338.npy) |
| 1339 | `model.layers.11.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1340 | `model.layers.11.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1341 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0001341.npy) |
| 1342 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0001342.npy) |
| 1343 | `model.layers.11.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1344 | `model.layers.11.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.75 / 92.0 / 0.09405488636758592 / 2.9632254674961205 | [NPY](tensors/0001344.npy) |
| 1345 | `model.layers.11.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.125 / 8.3125 / 0.03633511671796441 / 1.2838215433995013 | [NPY](tensors/0001345.npy) |
| 1346 | `model.layers.11.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.75 / 92.0 / 0.09405488636758592 / 2.9632254674961205 | [NPY](tensors/0001346.npy) |
| 1347 | `model.layers.11.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.5 / 39.75 / 0.10272838175296783 / 4.243615852238104 | [NPY](tensors/0001347.npy) |
| 1348 | `model.layers.11.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.75 / 92.0 / 0.09405488636758592 / 2.9632254674961205 | [NPY](tensors/0001348.npy) |
| 1349 | `model.layers.11.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.09375 / 7.0 / -0.11705073714256287 / 2.3592060845296308 | [NPY](tensors/0001349.npy) |
| 1350 | `model.layers.11.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.46875 / 7.71875 / -0.03768169041723013 / 1.585638418007353 | [NPY](tensors/0001350.npy) |
| 1351 | `model.layers.11.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 127.5 / 0.07707810931735569 / 4.781410835431467 | [NPY](tensors/0001351.npy) |
| 1352 | `model.layers.11.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 127.5 / 0.07707810931735569 / 4.781410835431467 | [NPY](tensors/0001352.npy) |
| 1353 | `model.layers.11.self_attn` | 11 | `output[1]` | [1, 64, 1, 332] | torch.bfloat16 → float32 | 1.5825207810848951e-10 / 0.9375 / 0.0028350405270027162 / 0.012756467264578651 | [NPY](tensors/0001353.npy) |
| 1354 | `model.layers.11.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -264.0 / 366.0 / 0.6547247992621528 / 19.472893631973076 | [NPY](tensors/0001354.npy) |
| 1355 | `model.layers.11.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.484375 / 3.28125 / 0.008054200808207195 / 0.68498983455963 | [NPY](tensors/0001355.npy) |
| 1356 | `model.layers.11.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.484375 / 3.28125 / 0.008054200808207195 / 0.68498983455963 | [NPY](tensors/0001356.npy) |
| 1357 | `model.layers.11.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.484375 / 3.28125 / 0.008054200808207195 / 0.68498983455963 | [NPY](tensors/0001357.npy) |
| 1358 | `model.layers.11.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1359 | `model.layers.11.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1360 | `model.layers.11.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1361 | `model.layers.11.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -55.75 / 165.0 / 0.19489903979831272 / 5.728049923310617 | [NPY](tensors/0001361.npy) |
| 1362 | `model.layers.11.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.75 / 165.0 / 0.19489903979831272 / 5.728049923310617 | [NPY](tensors/0001362.npy) |
| 1363 | `model.layers.11.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.4296875 / -0.022747039794921875 / 0.5392738715779937 | [NPY](tensors/0001363.npy) |
| 1364 | `model.layers.11` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -320.0 / 532.0 / 0.8499494764539931 / 23.19428785047984 | [NPY](tensors/0001364.npy) |
| 1443 | `model.layers.11` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -207.0 / 336.0 / 0.47272830539279515 / 16.920848709678594 | [NPY](tensors/0001443.npy) |
| 1444 | `model.layers.11` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 333] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001444.npy) |
| 1445 | `model.layers.11` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0001445.npy) |
| 1446 | `model.layers.11` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0001446.npy) |
| 1447 | `model.layers.11` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0001447.npy) |
| 1448 | `model.layers.11` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1449 | `model.layers.11` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1450 | `model.layers.11` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1451 | `model.layers.11.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -207.0 / 336.0 / 0.47272830539279515 / 16.920848709678594 | [NPY](tensors/0001451.npy) |
| 1452 | `model.layers.11.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.0 / 93.0 / 0.07750007443957858 / 2.9575755342915504 | [NPY](tensors/0001452.npy) |
| 1453 | `model.layers.11.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.0 / 93.0 / 0.07750007443957858 / 2.9575755342915504 | [NPY](tensors/0001453.npy) |
| 1454 | `model.layers.11.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 333] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001454.npy) |
| 1455 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0001455.npy) |
| 1456 | `model.layers.11.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1457 | `model.layers.11.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1458 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0001458.npy) |
| 1459 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0001459.npy) |
| 1460 | `model.layers.11.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1461 | `model.layers.11.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.0 / 93.0 / 0.07750007443957858 / 2.9575755342915504 | [NPY](tensors/0001461.npy) |
| 1462 | `model.layers.11.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.65625 / 9.75 / 0.04795001563616097 / 1.2207643710394602 | [NPY](tensors/0001462.npy) |
| 1463 | `model.layers.11.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.0 / 93.0 / 0.07750007443957858 / 2.9575755342915504 | [NPY](tensors/0001463.npy) |
| 1464 | `model.layers.11.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.5 / 38.0 / 0.1208762377500534 / 3.8138963735418687 | [NPY](tensors/0001464.npy) |
| 1465 | `model.layers.11.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.0 / 93.0 / 0.07750007443957858 / 2.9575755342915504 | [NPY](tensors/0001465.npy) |
| 1466 | `model.layers.11.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.28125 / 5.40625 / 0.0023657679557800293 / 1.946647745935913 | [NPY](tensors/0001466.npy) |
| 1467 | `model.layers.11.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.75 / 6.4375 / -0.03903893381357193 / 1.3581095678944524 | [NPY](tensors/0001467.npy) |
| 1468 | `model.layers.11.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 62.75 / -0.001437491840786404 / 3.491136427525789 | [NPY](tensors/0001468.npy) |
| 1469 | `model.layers.11.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 62.75 / -0.001437491840786404 / 3.491136427525789 | [NPY](tensors/0001469.npy) |
| 1470 | `model.layers.11.self_attn` | 12 | `output[1]` | [1, 64, 1, 333] | torch.bfloat16 → float32 | 5.7696070143720135e-12 / 0.8828125 / 0.0027569333016233427 / 0.0122307653158094 | [NPY](tensors/0001470.npy) |
| 1471 | `model.layers.11.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -242.0 / 342.0 / 0.47103949652777777 / 18.244897771172614 | [NPY](tensors/0001471.npy) |
| 1472 | `model.layers.11.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.375 / -0.0015661981370713976 / 0.6906746935696684 | [NPY](tensors/0001472.npy) |
| 1473 | `model.layers.11.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.375 / -0.0015661981370713976 / 0.6906746935696684 | [NPY](tensors/0001473.npy) |
| 1474 | `model.layers.11.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.375 / -0.0015661981370713976 / 0.6906746935696684 | [NPY](tensors/0001474.npy) |
| 1475 | `model.layers.11.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1476 | `model.layers.11.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1477 | `model.layers.11.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1478 | `model.layers.11.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -89.0 / 129.0 / 0.10309024122026232 / 5.426243297833002 | [NPY](tensors/0001478.npy) |
| 1479 | `model.layers.11.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.0 / 129.0 / 0.10309024122026232 / 5.426243297833002 | [NPY](tensors/0001479.npy) |
| 1480 | `model.layers.11.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6875 / 1.6171875 / -0.031019210815429688 / 0.6790664523436877 | [NPY](tensors/0001480.npy) |
| 1481 | `model.layers.11` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -332.0 / 468.0 / 0.573085700141059 / 21.742060085991216 | [NPY](tensors/0001481.npy) |
| 1560 | `model.layers.11` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -400.0 / 476.0 / 0.4309861924913194 / 20.90770855037219 | [NPY](tensors/0001560.npy) |
| 1561 | `model.layers.11` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 334] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001561.npy) |
| 1562 | `model.layers.11` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0001562.npy) |
| 1563 | `model.layers.11` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0001563.npy) |
| 1564 | `model.layers.11` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0001564.npy) |
| 1565 | `model.layers.11` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1566 | `model.layers.11` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1567 | `model.layers.11` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1568 | `model.layers.11.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -400.0 / 476.0 / 0.4309861924913194 / 20.90770855037219 | [NPY](tensors/0001568.npy) |
| 1569 | `model.layers.11.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 106.5 / 0.058842221895853676 / 3.430009634292026 | [NPY](tensors/0001569.npy) |
| 1570 | `model.layers.11.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 106.5 / 0.058842221895853676 / 3.430009634292026 | [NPY](tensors/0001570.npy) |
| 1571 | `model.layers.11.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 334] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001571.npy) |
| 1572 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0001572.npy) |
| 1573 | `model.layers.11.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1574 | `model.layers.11.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1575 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0001575.npy) |
| 1576 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0001576.npy) |
| 1577 | `model.layers.11.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1578 | `model.layers.11.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 106.5 / 0.058842221895853676 / 3.430009634292026 | [NPY](tensors/0001578.npy) |
| 1579 | `model.layers.11.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.75 / 7.84375 / 0.03642031503841281 / 1.124358206286871 | [NPY](tensors/0001579.npy) |
| 1580 | `model.layers.11.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 106.5 / 0.058842221895853676 / 3.430009634292026 | [NPY](tensors/0001580.npy) |
| 1581 | `model.layers.11.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.75 / 39.0 / 0.14683330059051514 / 3.6214214460759426 | [NPY](tensors/0001581.npy) |
| 1582 | `model.layers.11.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 106.5 / 0.058842221895853676 / 3.430009634292026 | [NPY](tensors/0001582.npy) |
| 1583 | `model.layers.11.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.96875 / 6.21875 / 0.019381878897547722 / 1.6378319929008707 | [NPY](tensors/0001583.npy) |
| 1584 | `model.layers.11.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.4375 / 6.0 / -0.014845737256109715 / 1.2150161400334327 | [NPY](tensors/0001584.npy) |
| 1585 | `model.layers.11.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 102.5 / 0.01944253577126397 / 4.359114091786323 | [NPY](tensors/0001585.npy) |
| 1586 | `model.layers.11.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 102.5 / 0.01944253577126397 / 4.359114091786323 | [NPY](tensors/0001586.npy) |
| 1587 | `model.layers.11.self_attn` | 13 | `output[1]` | [1, 64, 1, 334] | torch.bfloat16 → float32 | 7.133849067031406e-12 / 0.9609375 / 0.0026992734819266634 / 0.010976477066554538 | [NPY](tensors/0001587.npy) |
| 1588 | `model.layers.11.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -298.0 / 420.0 / 0.4501849704318576 / 20.25066419643366 | [NPY](tensors/0001588.npy) |
| 1589 | `model.layers.11.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.03125 / 3.0625 / 0.0014674968189663357 / 0.6791258911361638 | [NPY](tensors/0001589.npy) |
| 1590 | `model.layers.11.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.03125 / 3.0625 / 0.0014674968189663357 / 0.6791258911361638 | [NPY](tensors/0001590.npy) |
| 1591 | `model.layers.11.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.03125 / 3.0625 / 0.0014674968189663357 / 0.6791258911361638 | [NPY](tensors/0001591.npy) |
| 1592 | `model.layers.11.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1593 | `model.layers.11.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1594 | `model.layers.11.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1595 | `model.layers.11.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -189.0 / 158.0 / 0.011085330115424261 / 6.421478709179719 | [NPY](tensors/0001595.npy) |
| 1596 | `model.layers.11.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -189.0 / 158.0 / 0.011085330115424261 / 6.421478709179719 | [NPY](tensors/0001596.npy) |
| 1597 | `model.layers.11.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.859375 / 1.015625 / -0.033172607421875 / 0.5857621908190733 | [NPY](tensors/0001597.npy) |
| 1598 | `model.layers.11` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -488.0 / 544.0 / 0.45927327473958335 / 24.43661360759118 | [NPY](tensors/0001598.npy) |
| 1677 | `model.layers.11` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -446.0 / 540.0 / 0.5719509548611111 / 20.995044304529273 | [NPY](tensors/0001677.npy) |
| 1678 | `model.layers.11` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 335] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001678.npy) |
| 1679 | `model.layers.11` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0001679.npy) |
| 1680 | `model.layers.11` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0001680.npy) |
| 1681 | `model.layers.11` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0001681.npy) |
| 1682 | `model.layers.11` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1683 | `model.layers.11` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1684 | `model.layers.11` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1685 | `model.layers.11.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -446.0 / 540.0 / 0.5719509548611111 / 20.995044304529273 | [NPY](tensors/0001685.npy) |
| 1686 | `model.layers.11.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -111.5 / 120.5 / 0.0717684461010827 / 3.648545129763482 | [NPY](tensors/0001686.npy) |
| 1687 | `model.layers.11.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -111.5 / 120.5 / 0.0717684461010827 / 3.648545129763482 | [NPY](tensors/0001687.npy) |
| 1688 | `model.layers.11.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 335] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001688.npy) |
| 1689 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0001689.npy) |
| 1690 | `model.layers.11.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1691 | `model.layers.11.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1692 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0001692.npy) |
| 1693 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0001693.npy) |
| 1694 | `model.layers.11.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1695 | `model.layers.11.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -111.5 / 120.5 / 0.0717684461010827 / 3.648545129763482 | [NPY](tensors/0001695.npy) |
| 1696 | `model.layers.11.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 7.4375 / 0.02534646971616894 / 1.0890624518800722 | [NPY](tensors/0001696.npy) |
| 1697 | `model.layers.11.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -111.5 / 120.5 / 0.0717684461010827 / 3.648545129763482 | [NPY](tensors/0001697.npy) |
| 1698 | `model.layers.11.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.25 / 41.0 / 0.0716957151889801 / 3.705441575460919 | [NPY](tensors/0001698.npy) |
| 1699 | `model.layers.11.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -111.5 / 120.5 / 0.0717684461010827 / 3.648545129763482 | [NPY](tensors/0001699.npy) |
| 1700 | `model.layers.11.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.0 / 6.21875 / 0.04010117053985596 / 1.719220491945295 | [NPY](tensors/0001700.npy) |
| 1701 | `model.layers.11.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.15625 / 5.84375 / -0.002449062652885914 / 1.216454800401939 | [NPY](tensors/0001701.npy) |
| 1702 | `model.layers.11.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 123.5 / 0.06604136493470934 / 4.637745541635558 | [NPY](tensors/0001702.npy) |
| 1703 | `model.layers.11.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 123.5 / 0.06604136493470934 / 4.637745541635558 | [NPY](tensors/0001703.npy) |
| 1704 | `model.layers.11.self_attn` | 14 | `output[1]` | [1, 64, 1, 335] | torch.bfloat16 → float32 | 1.0231815394945443e-11 / 0.9453125 / 0.0027282834001030555 / 0.011976221628879789 | [NPY](tensors/0001704.npy) |
| 1705 | `model.layers.11.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -322.0 / 454.0 / 0.6379859076605903 / 20.086295379413812 | [NPY](tensors/0001705.npy) |
| 1706 | `model.layers.11.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.609375 / 2.8125 / 0.015591843922932943 / 0.6727333126675522 | [NPY](tensors/0001706.npy) |
| 1707 | `model.layers.11.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.609375 / 2.8125 / 0.015591843922932943 / 0.6727333126675522 | [NPY](tensors/0001707.npy) |
| 1708 | `model.layers.11.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.609375 / 2.8125 / 0.015591843922932943 / 0.6727333126675522 | [NPY](tensors/0001708.npy) |
| 1709 | `model.layers.11.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1710 | `model.layers.11.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1711 | `model.layers.11.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1712 | `model.layers.11.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -147.0 / 151.0 / 0.08260856734381782 / 6.473222906236268 | [NPY](tensors/0001712.npy) |
| 1713 | `model.layers.11.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -147.0 / 151.0 / 0.08260856734381782 / 6.473222906236268 | [NPY](tensors/0001713.npy) |
| 1714 | `model.layers.11.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.015625 / 1.0234375 / -0.05163764953613281 / 0.5116630995507867 | [NPY](tensors/0001714.npy) |
| 1715 | `model.layers.11` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -468.0 / 604.0 / 0.7208089192708333 / 24.18911126150777 | [NPY](tensors/0001715.npy) |
| 1794 | `model.layers.11` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -544.0 / 600.0 / 0.49075893825954864 / 24.362373288635176 | [NPY](tensors/0001794.npy) |
| 1795 | `model.layers.11` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 336] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001795.npy) |
| 1796 | `model.layers.11` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0001796.npy) |
| 1797 | `model.layers.11` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0001797.npy) |
| 1798 | `model.layers.11` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0001798.npy) |
| 1799 | `model.layers.11` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1800 | `model.layers.11` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1801 | `model.layers.11` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1802 | `model.layers.11.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -544.0 / 600.0 / 0.49075893825954864 / 24.362373288635176 | [NPY](tensors/0001802.npy) |
| 1803 | `model.layers.11.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 115.5 / 0.05466568867365519 / 3.5980503952157017 | [NPY](tensors/0001803.npy) |
| 1804 | `model.layers.11.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 115.5 / 0.05466568867365519 / 3.5980503952157017 | [NPY](tensors/0001804.npy) |
| 1805 | `model.layers.11.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 336] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001805.npy) |
| 1806 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0001806.npy) |
| 1807 | `model.layers.11.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1808 | `model.layers.11.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1809 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0001809.npy) |
| 1810 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0001810.npy) |
| 1811 | `model.layers.11.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1812 | `model.layers.11.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 115.5 / 0.05466568867365519 / 3.5980503952157017 | [NPY](tensors/0001812.npy) |
| 1813 | `model.layers.11.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.34375 / 7.1875 / 0.036315991543233395 / 1.100330829617642 | [NPY](tensors/0001813.npy) |
| 1814 | `model.layers.11.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 115.5 / 0.05466568867365519 / 3.5980503952157017 | [NPY](tensors/0001814.npy) |
| 1815 | `model.layers.11.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.625 / 45.0 / 0.00027233362197875977 / 3.979898841682803 | [NPY](tensors/0001815.npy) |
| 1816 | `model.layers.11.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 115.5 / 0.05466568867365519 / 3.5980503952157017 | [NPY](tensors/0001816.npy) |
| 1817 | `model.layers.11.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.375 / 6.84375 / -0.0319904088973999 / 2.2894806386210296 | [NPY](tensors/0001817.npy) |
| 1818 | `model.layers.11.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.875 / 6.40625 / 0.004023216664791107 / 1.339907526543857 | [NPY](tensors/0001818.npy) |
| 1819 | `model.layers.11.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -218.0 / 185.0 / -0.0801584243774414 / 6.79926779543821 | [NPY](tensors/0001819.npy) |
| 1820 | `model.layers.11.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -218.0 / 185.0 / -0.0801584243774414 / 6.79926779543821 | [NPY](tensors/0001820.npy) |
| 1821 | `model.layers.11.self_attn` | 15 | `output[1]` | [1, 64, 1, 336] | torch.bfloat16 → float32 | 1.1723955140041653e-13 / 0.97265625 / 0.0026538138353183155 / 0.016141661441462413 | [NPY](tensors/0001821.npy) |
| 1822 | `model.layers.11.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -360.0 / 388.0 / 0.40972425672743057 / 21.330164994885944 | [NPY](tensors/0001822.npy) |
| 1823 | `model.layers.11.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.734375 / 3.8125 / 0.013245234886805216 / 0.7433339789110517 | [NPY](tensors/0001823.npy) |
| 1824 | `model.layers.11.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.734375 / 3.8125 / 0.013245234886805216 / 0.7433339789110517 | [NPY](tensors/0001824.npy) |
| 1825 | `model.layers.11.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.734375 / 3.8125 / 0.013245234886805216 / 0.7433339789110517 | [NPY](tensors/0001825.npy) |
| 1826 | `model.layers.11.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1827 | `model.layers.11.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1828 | `model.layers.11.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1829 | `model.layers.11.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -318.0 / 195.0 / 0.16606898837619358 / 9.514576384001305 | [NPY](tensors/0001829.npy) |
| 1830 | `model.layers.11.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -318.0 / 195.0 / 0.16606898837619358 / 9.514576384001305 | [NPY](tensors/0001830.npy) |
| 1831 | `model.layers.11.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.421875 / 1.3984375 / -0.12858819961547852 / 0.8273938408588072 | [NPY](tensors/0001831.npy) |
| 1832 | `model.layers.11` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -680.0 / 576.0 / 0.5751091851128473 / 27.72135629153478 | [NPY](tensors/0001832.npy) |
| 1911 | `model.layers.11` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -532.0 / 508.0 / 0.09084548950195312 / 22.102031660043885 | [NPY](tensors/0001911.npy) |
| 1912 | `model.layers.11` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 337] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001912.npy) |
| 1913 | `model.layers.11` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0001913.npy) |
| 1914 | `model.layers.11` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0001914.npy) |
| 1915 | `model.layers.11` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0001915.npy) |
| 1916 | `model.layers.11` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1917 | `model.layers.11` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1918 | `model.layers.11` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1919 | `model.layers.11.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -532.0 / 508.0 / 0.09084548950195312 / 22.102031660043885 | [NPY](tensors/0001919.npy) |
| 1920 | `model.layers.11.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -126.5 / 107.5 / 0.033172245820363364 / 3.6170049992461095 | [NPY](tensors/0001920.npy) |
| 1921 | `model.layers.11.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -126.5 / 107.5 / 0.033172245820363364 / 3.6170049992461095 | [NPY](tensors/0001921.npy) |
| 1922 | `model.layers.11.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 337] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001922.npy) |
| 1923 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0001923.npy) |
| 1924 | `model.layers.11.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1925 | `model.layers.11.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1926 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0001926.npy) |
| 1927 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0001927.npy) |
| 1928 | `model.layers.11.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1929 | `model.layers.11.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -126.5 / 107.5 / 0.033172245820363364 / 3.6170049992461095 | [NPY](tensors/0001929.npy) |
| 1930 | `model.layers.11.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.84375 / 6.65625 / 0.029480207711458206 / 1.1133898982402148 | [NPY](tensors/0001930.npy) |
| 1931 | `model.layers.11.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -126.5 / 107.5 / 0.033172245820363364 / 3.6170049992461095 | [NPY](tensors/0001931.npy) |
| 1932 | `model.layers.11.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.5 / 40.5 / 0.030614051967859268 / 3.8362691772890525 | [NPY](tensors/0001932.npy) |
| 1933 | `model.layers.11.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -126.5 / 107.5 / 0.033172245820363364 / 3.6170049992461095 | [NPY](tensors/0001933.npy) |
| 1934 | `model.layers.11.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.78125 / 6.25 / -0.07838141918182373 / 2.034259259682985 | [NPY](tensors/0001934.npy) |
| 1935 | `model.layers.11.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.21875 / 6.5 / -0.00998975127004087 / 1.377009938287968 | [NPY](tensors/0001935.npy) |
| 1936 | `model.layers.11.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 132.0 / -0.022162919574313693 / 5.678855196132521 | [NPY](tensors/0001936.npy) |
| 1937 | `model.layers.11.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 132.0 / -0.022162919574313693 / 5.678855196132521 | [NPY](tensors/0001937.npy) |
| 1938 | `model.layers.11.self_attn` | 16 | `output[1]` | [1, 64, 1, 337] | torch.bfloat16 → float32 | 1.7834622667578515e-12 / 0.94921875 / 0.0027104596047491714 / 0.016896451015317445 | [NPY](tensors/0001938.npy) |
| 1939 | `model.layers.11.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -400.0 / 416.0 / 0.06954888237847222 / 21.21056323846715 | [NPY](tensors/0001939.npy) |
| 1940 | `model.layers.11.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.8125 / 3.53125 / -0.0038885098364618087 / 0.7526930161642695 | [NPY](tensors/0001940.npy) |
| 1941 | `model.layers.11.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.8125 / 3.53125 / -0.0038885098364618087 / 0.7526930161642695 | [NPY](tensors/0001941.npy) |
| 1942 | `model.layers.11.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.8125 / 3.53125 / -0.0038885098364618087 / 0.7526930161642695 | [NPY](tensors/0001942.npy) |
| 1943 | `model.layers.11.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1944 | `model.layers.11.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1945 | `model.layers.11.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1946 | `model.layers.11.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -240.0 / 170.0 / 0.06091029312875536 / 8.03697605479172 | [NPY](tensors/0001946.npy) |
| 1947 | `model.layers.11.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -240.0 / 170.0 / 0.06091029312875536 / 8.03697605479172 | [NPY](tensors/0001947.npy) |
| 1948 | `model.layers.11.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.5390625 / 1.1484375 / -0.12717437744140625 / 0.6374652247649532 | [NPY](tensors/0001948.npy) |
| 1949 | `model.layers.11` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -640.0 / 568.0 / 0.13073933919270833 / 26.249713849827174 | [NPY](tensors/0001949.npy) |
| 2028 | `model.layers.11` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -664.0 / 608.0 / 0.8100963168674045 / 26.79180668155576 | [NPY](tensors/0002028.npy) |
| 2029 | `model.layers.11` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 338] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002029.npy) |
| 2030 | `model.layers.11` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0002030.npy) |
| 2031 | `model.layers.11` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0002031.npy) |
| 2032 | `model.layers.11` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0002032.npy) |
| 2033 | `model.layers.11` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2034 | `model.layers.11` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2035 | `model.layers.11` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2036 | `model.layers.11.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -664.0 / 608.0 / 0.8100963168674045 / 26.79180668155576 | [NPY](tensors/0002036.npy) |
| 2037 | `model.layers.11.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -130.0 / 106.5 / 0.06603478193283081 / 3.620019701053057 | [NPY](tensors/0002037.npy) |
| 2038 | `model.layers.11.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -130.0 / 106.5 / 0.06603478193283081 / 3.620019701053057 | [NPY](tensors/0002038.npy) |
| 2039 | `model.layers.11.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 338] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002039.npy) |
| 2040 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0002040.npy) |
| 2041 | `model.layers.11.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2042 | `model.layers.11.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2043 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0002043.npy) |
| 2044 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0002044.npy) |
| 2045 | `model.layers.11.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2046 | `model.layers.11.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -130.0 / 106.5 / 0.06603478193283081 / 3.620019701053057 | [NPY](tensors/0002046.npy) |
| 2047 | `model.layers.11.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.1875 / 8.625 / 0.06508930213749409 / 1.175210404177035 | [NPY](tensors/0002047.npy) |
| 2048 | `model.layers.11.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -130.0 / 106.5 / 0.06603478193283081 / 3.620019701053057 | [NPY](tensors/0002048.npy) |
| 2049 | `model.layers.11.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 37.0 / 0.14672096073627472 / 3.683235666122967 | [NPY](tensors/0002049.npy) |
| 2050 | `model.layers.11.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -130.0 / 106.5 / 0.06603478193283081 / 3.620019701053057 | [NPY](tensors/0002050.npy) |
| 2051 | `model.layers.11.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.40625 / 7.96875 / 0.048296213150024414 / 2.4488000465607347 | [NPY](tensors/0002051.npy) |
| 2052 | `model.layers.11.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.75 / 6.40625 / -0.004701587837189436 / 1.2338438075628069 | [NPY](tensors/0002052.npy) |
| 2053 | `model.layers.11.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -200.0 / 268.0 / -0.07991937200228373 / 7.437959720088514 | [NPY](tensors/0002053.npy) |
| 2054 | `model.layers.11.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -200.0 / 268.0 / -0.07991937200228373 / 7.437959720088514 | [NPY](tensors/0002054.npy) |
| 2055 | `model.layers.11.self_attn` | 17 | `output[1]` | [1, 64, 1, 338] | torch.bfloat16 → float32 | 8.881784197001252e-14 / 0.9765625 / 0.0024935385546134086 / 0.018198769675331173 | [NPY](tensors/0002055.npy) |
| 2056 | `model.layers.11.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -396.0 / 434.0 / 0.7302988688151042 / 23.229099828269316 | [NPY](tensors/0002056.npy) |
| 2057 | `model.layers.11.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.84375 / 3.875 / 0.013946244451734756 / 0.7583789943342429 | [NPY](tensors/0002057.npy) |
| 2058 | `model.layers.11.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.84375 / 3.875 / 0.013946244451734756 / 0.7583789943342429 | [NPY](tensors/0002058.npy) |
| 2059 | `model.layers.11.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.84375 / 3.875 / 0.013946244451734756 / 0.7583789943342429 | [NPY](tensors/0002059.npy) |
| 2060 | `model.layers.11.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2061 | `model.layers.11.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2062 | `model.layers.11.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2063 | `model.layers.11.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -400.0 / 306.0 / 0.10413950284322103 / 11.930359698039453 | [NPY](tensors/0002063.npy) |
| 2064 | `model.layers.11.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -400.0 / 306.0 / 0.10413950284322103 / 11.930359698039453 | [NPY](tensors/0002064.npy) |
| 2065 | `model.layers.11.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.203125 / 1.296875 / -0.15143966674804688 / 0.7815774272352596 | [NPY](tensors/0002065.npy) |
| 2066 | `model.layers.11` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -796.0 / 712.0 / 0.8344824896918402 / 31.27284272235647 | [NPY](tensors/0002066.npy) |
| 2145 | `model.layers.11` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -360.0 / 464.0 / 0.7700385199652777 / 19.010481389230883 | [NPY](tensors/0002145.npy) |
| 2146 | `model.layers.11` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 339] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002146.npy) |
| 2147 | `model.layers.11` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0002147.npy) |
| 2148 | `model.layers.11` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0002148.npy) |
| 2149 | `model.layers.11` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0002149.npy) |
| 2150 | `model.layers.11` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2151 | `model.layers.11` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2152 | `model.layers.11` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2153 | `model.layers.11.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -360.0 / 464.0 / 0.7700385199652777 / 19.010481389230883 | [NPY](tensors/0002153.npy) |
| 2154 | `model.layers.11.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.5 / 97.0 / 0.091320976946089 / 3.4290510394293325 | [NPY](tensors/0002154.npy) |
| 2155 | `model.layers.11.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.5 / 97.0 / 0.091320976946089 / 3.4290510394293325 | [NPY](tensors/0002155.npy) |
| 2156 | `model.layers.11.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 339] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002156.npy) |
| 2157 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0002157.npy) |
| 2158 | `model.layers.11.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2159 | `model.layers.11.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2160 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0002160.npy) |
| 2161 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0002161.npy) |
| 2162 | `model.layers.11.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2163 | `model.layers.11.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.5 / 97.0 / 0.091320976946089 / 3.4290510394293325 | [NPY](tensors/0002163.npy) |
| 2164 | `model.layers.11.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.40625 / 6.34375 / 0.05484036426059902 / 1.1367790868308572 | [NPY](tensors/0002164.npy) |
| 2165 | `model.layers.11.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.5 / 97.0 / 0.091320976946089 / 3.4290510394293325 | [NPY](tensors/0002165.npy) |
| 2166 | `model.layers.11.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.375 / 38.25 / 0.09560245275497437 / 3.9662806436544704 | [NPY](tensors/0002166.npy) |
| 2167 | `model.layers.11.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.5 / 97.0 / 0.091320976946089 / 3.4290510394293325 | [NPY](tensors/0002167.npy) |
| 2168 | `model.layers.11.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.96875 / 6.96875 / 0.022305011749267578 / 2.1320358505053463 | [NPY](tensors/0002168.npy) |
| 2169 | `model.layers.11.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.25 / 6.0625 / -0.00867041340097785 / 1.175805846447194 | [NPY](tensors/0002169.npy) |
| 2170 | `model.layers.11.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.25 / 94.0 / 0.057303176985846624 / 3.753615878850926 | [NPY](tensors/0002170.npy) |
| 2171 | `model.layers.11.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.25 / 94.0 / 0.057303176985846624 / 3.753615878850926 | [NPY](tensors/0002171.npy) |
| 2172 | `model.layers.11.self_attn` | 18 | `output[1]` | [1, 64, 1, 339] | torch.bfloat16 → float32 | 5.201172825763933e-12 / 0.8984375 / 0.0026297099041015025 / 0.012999206199442889 | [NPY](tensors/0002172.npy) |
| 2173 | `model.layers.11.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 468.0 / 0.8267957899305556 / 19.69618296287811 | [NPY](tensors/0002173.npy) |
| 2174 | `model.layers.11.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.109375 / 3.296875 / 0.014299688074323866 / 0.6242162133172768 | [NPY](tensors/0002174.npy) |
| 2175 | `model.layers.11.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.109375 / 3.296875 / 0.014299688074323866 / 0.6242162133172768 | [NPY](tensors/0002175.npy) |
| 2176 | `model.layers.11.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.109375 / 3.296875 / 0.014299688074323866 / 0.6242162133172768 | [NPY](tensors/0002176.npy) |
| 2177 | `model.layers.11.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2178 | `model.layers.11.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2179 | `model.layers.11.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2180 | `model.layers.11.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -120.5 / 108.5 / 0.03618311087290446 / 4.622482820977699 | [NPY](tensors/0002180.npy) |
| 2181 | `model.layers.11.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -120.5 / 108.5 / 0.03618311087290446 / 4.622482820977699 | [NPY](tensors/0002181.npy) |
| 2182 | `model.layers.11.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.7265625 / 0.9609375 / -0.023983001708984375 / 0.39648749085359447 | [NPY](tensors/0002182.npy) |
| 2183 | `model.layers.11` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -432.0 / 536.0 / 0.8616502549913194 / 22.593062986914852 | [NPY](tensors/0002183.npy) |
| 2262 | `model.layers.11` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -368.0 / 380.0 / 0.8504116482204861 / 21.92204540483022 | [NPY](tensors/0002262.npy) |
| 2263 | `model.layers.11` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 340] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002263.npy) |
| 2264 | `model.layers.11` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0002264.npy) |
| 2265 | `model.layers.11` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0002265.npy) |
| 2266 | `model.layers.11` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0002266.npy) |
| 2267 | `model.layers.11` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2268 | `model.layers.11` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2269 | `model.layers.11` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2270 | `model.layers.11.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -368.0 / 380.0 / 0.8504116482204861 / 21.92204540483022 | [NPY](tensors/0002270.npy) |
| 2271 | `model.layers.11.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 81.0 / 0.08319412734773424 / 2.9125387504360405 | [NPY](tensors/0002271.npy) |
| 2272 | `model.layers.11.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 81.0 / 0.08319412734773424 / 2.9125387504360405 | [NPY](tensors/0002272.npy) |
| 2273 | `model.layers.11.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 340] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002273.npy) |
| 2274 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0002274.npy) |
| 2275 | `model.layers.11.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2276 | `model.layers.11.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2277 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0002277.npy) |
| 2278 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0002278.npy) |
| 2279 | `model.layers.11.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2280 | `model.layers.11.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 81.0 / 0.08319412734773424 / 2.9125387504360405 | [NPY](tensors/0002280.npy) |
| 2281 | `model.layers.11.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.5625 / 9.5 / 0.027045269031077623 / 1.3081590441416937 | [NPY](tensors/0002281.npy) |
| 2282 | `model.layers.11.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 81.0 / 0.08319412734773424 / 2.9125387504360405 | [NPY](tensors/0002282.npy) |
| 2283 | `model.layers.11.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -37.25 / 41.0 / 0.03758350759744644 / 4.0649324893022465 | [NPY](tensors/0002283.npy) |
| 2284 | `model.layers.11.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 81.0 / 0.08319412734773424 / 2.9125387504360405 | [NPY](tensors/0002284.npy) |
| 2285 | `model.layers.11.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.46875 / 7.625 / -0.021632790565490723 / 2.268839725659476 | [NPY](tensors/0002285.npy) |
| 2286 | `model.layers.11.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5625 / 6.875 / -0.03223129268735647 / 1.3966655791210025 | [NPY](tensors/0002286.npy) |
| 2287 | `model.layers.11.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.0 / 77.0 / -0.05446392165289985 / 3.380006347619954 | [NPY](tensors/0002287.npy) |
| 2288 | `model.layers.11.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.0 / 77.0 / -0.05446392165289985 / 3.380006347619954 | [NPY](tensors/0002288.npy) |
| 2289 | `model.layers.11.self_attn` | 19 | `output[1]` | [1, 64, 1, 340] | torch.bfloat16 → float32 | 7.105427357601002e-12 / 0.8515625 / 0.0024050752233360866 / 0.013299407769001348 | [NPY](tensors/0002289.npy) |
| 2290 | `model.layers.11.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -292.0 / 360.0 / 0.7961910671657986 / 22.148400279870323 | [NPY](tensors/0002290.npy) |
| 2291 | `model.layers.11.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.1875 / 5.25 / 0.012205862998962402 / 0.7335237813692413 | [NPY](tensors/0002291.npy) |
| 2292 | `model.layers.11.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.1875 / 5.25 / 0.012205862998962402 / 0.7335237813692413 | [NPY](tensors/0002292.npy) |
| 2293 | `model.layers.11.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.1875 / 5.25 / 0.012205862998962402 / 0.7335237813692413 | [NPY](tensors/0002293.npy) |
| 2294 | `model.layers.11.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2295 | `model.layers.11.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2296 | `model.layers.11.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2297 | `model.layers.11.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -167.0 / 152.0 / 0.11754017935858832 / 6.8272364170273505 | [NPY](tensors/0002297.npy) |
| 2298 | `model.layers.11.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -167.0 / 152.0 / 0.11754017935858832 / 6.8272364170273505 | [NPY](tensors/0002298.npy) |
| 2299 | `model.layers.11.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6015625 / 1.5078125 / -0.11406326293945312 / 0.6171596163621007 | [NPY](tensors/0002299.npy) |
| 2300 | `model.layers.11` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -460.0 / 512.0 / 0.9130018446180556 / 26.466704508216313 | [NPY](tensors/0002300.npy) |
| 2379 | `model.layers.11` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -346.0 / 486.0 / 0.7783799913194445 / 24.103810226093458 | [NPY](tensors/0002379.npy) |
| 2380 | `model.layers.11` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 341] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002380.npy) |
| 2381 | `model.layers.11` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.34375 / 0.7532014846801758 / 0.8246045706539666 | [NPY](tensors/0002381.npy) |
| 2382 | `model.layers.11` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.03213447332382202 / 0.7489573739100013 | [NPY](tensors/0002382.npy) |
| 2383 | `model.layers.11` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 340.0 / 340.0 / 340.0 / 0.0 | [NPY](tensors/0002383.npy) |
| 2384 | `model.layers.11` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2385 | `model.layers.11` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2386 | `model.layers.11` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2387 | `model.layers.11.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -346.0 / 486.0 / 0.7783799913194445 / 24.103810226093458 | [NPY](tensors/0002387.npy) |
| 2388 | `model.layers.11.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 94.5 / 0.07778946823543972 / 2.9237419799225592 | [NPY](tensors/0002388.npy) |
| 2389 | `model.layers.11.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 94.5 / 0.07778946823543972 / 2.9237419799225592 | [NPY](tensors/0002389.npy) |
| 2390 | `model.layers.11.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 341] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002390.npy) |
| 2391 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 340.0 / 340.0 / 340.0 / 0.0 | [NPY](tensors/0002391.npy) |
| 2392 | `model.layers.11.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2393 | `model.layers.11.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2394 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.34375 / 0.7532014846801758 / 0.8246045706539666 | [NPY](tensors/0002394.npy) |
| 2395 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.03213447332382202 / 0.7489573739100013 | [NPY](tensors/0002395.npy) |
| 2396 | `model.layers.11.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2397 | `model.layers.11.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 94.5 / 0.07778946823543972 / 2.9237419799225592 | [NPY](tensors/0002397.npy) |
| 2398 | `model.layers.11.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.125 / 10.3125 / 0.009363432880491018 / 1.3520142179435626 | [NPY](tensors/0002398.npy) |
| 2399 | `model.layers.11.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 94.5 / 0.07778946823543972 / 2.9237419799225592 | [NPY](tensors/0002399.npy) |
| 2400 | `model.layers.11.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 39.5 / 0.007030412554740906 / 3.9344493055454137 | [NPY](tensors/0002400.npy) |
| 2401 | `model.layers.11.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 94.5 / 0.07778946823543972 / 2.9237419799225592 | [NPY](tensors/0002401.npy) |
| 2402 | `model.layers.11.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.84375 / 8.125 / 0.03073662519454956 / 2.3820382037280683 | [NPY](tensors/0002402.npy) |
| 2403 | `model.layers.11.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.65625 / 6.78125 / -0.026397929061204195 / 1.497451373969631 | [NPY](tensors/0002403.npy) |
| 2404 | `model.layers.11.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 43.75 / -0.019672258694966634 / 3.381680251676582 | [NPY](tensors/0002404.npy) |
| 2405 | `model.layers.11.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 43.75 / -0.019672258694966634 / 3.381680251676582 | [NPY](tensors/0002405.npy) |
| 2406 | `model.layers.11.self_attn` | 20 | `output[1]` | [1, 64, 1, 341] | torch.bfloat16 → float32 | 2.5579538487363607e-11 / 0.87109375 / 0.002493265168562487 / 0.015678563468515993 | [NPY](tensors/0002406.npy) |
| 2407 | `model.layers.11.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -302.0 / 446.0 / 0.7590128580729166 / 24.479284145051345 | [NPY](tensors/0002407.npy) |
| 2408 | `model.layers.11.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.828125 / 4.28125 / 0.0056052433119879825 / 0.7410570738898754 | [NPY](tensors/0002408.npy) |
| 2409 | `model.layers.11.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.828125 / 4.28125 / 0.0056052433119879825 / 0.7410570738898754 | [NPY](tensors/0002409.npy) |
| 2410 | `model.layers.11.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.828125 / 4.28125 / 0.0056052433119879825 / 0.7410570738898754 | [NPY](tensors/0002410.npy) |
| 2411 | `model.layers.11.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2412 | `model.layers.11.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2413 | `model.layers.11.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2414 | `model.layers.11.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -168.0 / 181.0 / 0.024629688262939452 / 7.505152288909923 | [NPY](tensors/0002414.npy) |
| 2415 | `model.layers.11.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -168.0 / 181.0 / 0.024629688262939452 / 7.505152288909923 | [NPY](tensors/0002415.npy) |
| 2416 | `model.layers.11.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9375 / 1.6484375 / -0.1534576416015625 / 0.650417536208853 | [NPY](tensors/0002416.npy) |
| 2417 | `model.layers.11` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -470.0 / 628.0 / 0.7836340586344401 / 29.055566711069286 | [NPY](tensors/0002417.npy) |
| 2496 | `model.layers.11` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -364.0 / 580.0 / 0.8924860636393229 / 26.67466758300146 | [NPY](tensors/0002496.npy) |
| 2497 | `model.layers.11` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 342] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002497.npy) |
| 2498 | `model.layers.11` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.7198410034179688 / 0.8503804730267482 | [NPY](tensors/0002498.npy) |
| 2499 | `model.layers.11` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.027828902006149292 / 0.7525043584225227 | [NPY](tensors/0002499.npy) |
| 2500 | `model.layers.11` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 341.0 / 341.0 / 341.0 / 0.0 | [NPY](tensors/0002500.npy) |
| 2501 | `model.layers.11` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2502 | `model.layers.11` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2503 | `model.layers.11` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2504 | `model.layers.11.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -364.0 / 580.0 / 0.8924860636393229 / 26.67466758300146 | [NPY](tensors/0002504.npy) |
| 2505 | `model.layers.11.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -71.5 / 102.0 / 0.08356733289029863 / 2.97341312364948 | [NPY](tensors/0002505.npy) |
| 2506 | `model.layers.11.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -71.5 / 102.0 / 0.08356733289029863 / 2.97341312364948 | [NPY](tensors/0002506.npy) |
| 2507 | `model.layers.11.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 342] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002507.npy) |
| 2508 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 341.0 / 341.0 / 341.0 / 0.0 | [NPY](tensors/0002508.npy) |
| 2509 | `model.layers.11.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2510 | `model.layers.11.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2511 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.7198410034179688 / 0.8503804730267482 | [NPY](tensors/0002511.npy) |
| 2512 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.027828902006149292 / 0.7525043584225227 | [NPY](tensors/0002512.npy) |
| 2513 | `model.layers.11.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2514 | `model.layers.11.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -71.5 / 102.0 / 0.08356733289029863 / 2.97341312364948 | [NPY](tensors/0002514.npy) |
| 2515 | `model.layers.11.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.6875 / 9.9375 / 0.012741353828459978 / 1.3537635531457723 | [NPY](tensors/0002515.npy) |
| 2516 | `model.layers.11.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -71.5 / 102.0 / 0.08356733289029863 / 2.97341312364948 | [NPY](tensors/0002516.npy) |
| 2517 | `model.layers.11.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.25 / 38.25 / 0.025112628936767578 / 3.7339508746280408 | [NPY](tensors/0002517.npy) |
| 2518 | `model.layers.11.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -71.5 / 102.0 / 0.08356733289029863 / 2.97341312364948 | [NPY](tensors/0002518.npy) |
| 2519 | `model.layers.11.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.0 / 9.6875 / -0.08219170570373535 / 2.770490946177784 | [NPY](tensors/0002519.npy) |
| 2520 | `model.layers.11.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.59375 / 8.9375 / -0.0339372493326664 / 1.673702045172663 | [NPY](tensors/0002520.npy) |
| 2521 | `model.layers.11.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 65.0 / 0.060784371693929036 / 4.394003569385762 | [NPY](tensors/0002521.npy) |
| 2522 | `model.layers.11.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 65.0 / 0.060784371693929036 / 4.394003569385762 | [NPY](tensors/0002522.npy) |
| 2523 | `model.layers.11.self_attn` | 21 | `output[1]` | [1, 64, 1, 342] | torch.bfloat16 → float32 | 1.9895196601282805e-11 / 0.87109375 / 0.0027303190305671874 / 0.015105384648590825 | [NPY](tensors/0002523.npy) |
| 2524 | `model.layers.11.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -366.0 / 544.0 / 0.9530615912543403 / 27.76288097351527 | [NPY](tensors/0002524.npy) |
| 2525 | `model.layers.11.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.859375 / 4.0625 / 0.017949832810295954 / 0.7482813406785576 | [NPY](tensors/0002525.npy) |
| 2526 | `model.layers.11.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.859375 / 4.0625 / 0.017949832810295954 / 0.7482813406785576 | [NPY](tensors/0002526.npy) |
| 2527 | `model.layers.11.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.859375 / 4.0625 / 0.017949832810295954 / 0.7482813406785576 | [NPY](tensors/0002527.npy) |
| 2528 | `model.layers.11.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2529 | `model.layers.11.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2530 | `model.layers.11.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2531 | `model.layers.11.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -126.5 / 227.0 / 0.27201696501837835 / 8.200189493710825 | [NPY](tensors/0002531.npy) |
| 2532 | `model.layers.11.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -126.5 / 227.0 / 0.27201696501837835 / 8.200189493710825 | [NPY](tensors/0002532.npy) |
| 2533 | `model.layers.11.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.046875 / 1.015625 / -0.12500762939453125 / 0.5741279192756579 | [NPY](tensors/0002533.npy) |
| 2534 | `model.layers.11` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -492.0 / 772.0 / 1.2255706787109375 / 33.16875250944291 | [NPY](tensors/0002534.npy) |
| 2613 | `model.layers.11` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -132.0 / 272.0 / 0.6846042844984267 / 15.391546452347763 | [NPY](tensors/0002613.npy) |
| 2614 | `model.layers.11` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 343] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002614.npy) |
| 2615 | `model.layers.11` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.70660400390625 / 0.91681783844784 | [NPY](tensors/0002615.npy) |
| 2616 | `model.layers.11` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / -0.014852643013000488 / 0.6845543139796254 | [NPY](tensors/0002616.npy) |
| 2617 | `model.layers.11` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 342.0 / 342.0 / 342.0 / 0.0 | [NPY](tensors/0002617.npy) |
| 2618 | `model.layers.11` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2619 | `model.layers.11` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2620 | `model.layers.11` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2621 | `model.layers.11.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -132.0 / 272.0 / 0.6846042844984267 / 15.391546452347763 | [NPY](tensors/0002621.npy) |
| 2622 | `model.layers.11.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 83.0 / 0.10277244514889187 / 2.703063914412773 | [NPY](tensors/0002622.npy) |
| 2623 | `model.layers.11.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 83.0 / 0.10277244514889187 / 2.703063914412773 | [NPY](tensors/0002623.npy) |
| 2624 | `model.layers.11.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 343] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002624.npy) |
| 2625 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 342.0 / 342.0 / 342.0 / 0.0 | [NPY](tensors/0002625.npy) |
| 2626 | `model.layers.11.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2627 | `model.layers.11.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2628 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.70660400390625 / 0.91681783844784 | [NPY](tensors/0002628.npy) |
| 2629 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / -0.014852643013000488 / 0.6845543139796254 | [NPY](tensors/0002629.npy) |
| 2630 | `model.layers.11.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2631 | `model.layers.11.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 83.0 / 0.10277244514889187 / 2.703063914412773 | [NPY](tensors/0002631.npy) |
| 2632 | `model.layers.11.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 11.0625 / 0.01844030275242403 / 1.380086146289399 | [NPY](tensors/0002632.npy) |
| 2633 | `model.layers.11.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 83.0 / 0.10277244514889187 / 2.703063914412773 | [NPY](tensors/0002633.npy) |
| 2634 | `model.layers.11.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 43.75 / 0.0623587891459465 / 4.569827625839678 | [NPY](tensors/0002634.npy) |
| 2635 | `model.layers.11.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 83.0 / 0.10277244514889187 / 2.703063914412773 | [NPY](tensors/0002635.npy) |
| 2636 | `model.layers.11.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.40625 / 8.9375 / -0.00345766544342041 / 2.5015387463044116 | [NPY](tensors/0002636.npy) |
| 2637 | `model.layers.11.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.21875 / 6.78125 / -0.033466501627117395 / 1.4933349359020087 | [NPY](tensors/0002637.npy) |
| 2638 | `model.layers.11.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 95.5 / 0.05464618007342021 / 4.37533219960105 | [NPY](tensors/0002638.npy) |
| 2639 | `model.layers.11.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 95.5 / 0.05464618007342021 / 4.37533219960105 | [NPY](tensors/0002639.npy) |
| 2640 | `model.layers.11.self_attn` | 22 | `output[1]` | [1, 64, 1, 343] | torch.bfloat16 → float32 | 3.1104718800634146e-10 / 0.87109375 / 0.0025597944468832754 / 0.014504666941897709 | [NPY](tensors/0002640.npy) |
| 2641 | `model.layers.11.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -208.0 / 364.0 / 0.7393686930338542 / 17.741215975363172 | [NPY](tensors/0002641.npy) |
| 2642 | `model.layers.11.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.5 / 3.828125 / 0.016506888469060264 / 0.7131275365709303 | [NPY](tensors/0002642.npy) |
| 2643 | `model.layers.11.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.5 / 3.828125 / 0.016506888469060264 / 0.7131275365709303 | [NPY](tensors/0002643.npy) |
| 2644 | `model.layers.11.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.5 / 3.828125 / 0.016506888469060264 / 0.7131275365709303 | [NPY](tensors/0002644.npy) |
| 2645 | `model.layers.11.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2646 | `model.layers.11.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2647 | `model.layers.11.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2648 | `model.layers.11.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -101.5 / 70.5 / 0.09209059609307182 / 4.400498495763484 | [NPY](tensors/0002648.npy) |
| 2649 | `model.layers.11.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 70.5 / 0.09209059609307182 / 4.400498495763484 | [NPY](tensors/0002649.npy) |
| 2650 | `model.layers.11.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.734375 / 1.484375 / -0.093231201171875 / 0.6663501261671411 | [NPY](tensors/0002650.npy) |
| 2651 | `model.layers.11` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -310.0 / 394.0 / 0.8303571912977431 / 19.921531199144578 | [NPY](tensors/0002651.npy) |
| 2730 | `model.layers.11` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -452.0 / 632.0 / 0.7140652126736111 / 26.331082274839922 | [NPY](tensors/0002730.npy) |
| 2731 | `model.layers.11` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 344] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002731.npy) |
| 2732 | `model.layers.11` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.740966796875 / 0.9022817549113021 | [NPY](tensors/0002732.npy) |
| 2733 | `model.layers.11` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3046875 / -0.06294980645179749 / 0.6646640154085409 | [NPY](tensors/0002733.npy) |
| 2734 | `model.layers.11` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 343.0 / 343.0 / 343.0 / 0.0 | [NPY](tensors/0002734.npy) |
| 2735 | `model.layers.11` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2736 | `model.layers.11` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2737 | `model.layers.11` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2738 | `model.layers.11.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -452.0 / 632.0 / 0.7140652126736111 / 26.331082274839922 | [NPY](tensors/0002738.npy) |
| 2739 | `model.layers.11.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.0 / 112.5 / 0.0627029922273424 / 3.169262073212285 | [NPY](tensors/0002739.npy) |
| 2740 | `model.layers.11.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.0 / 112.5 / 0.0627029922273424 / 3.169262073212285 | [NPY](tensors/0002740.npy) |
| 2741 | `model.layers.11.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 344] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002741.npy) |
| 2742 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 343.0 / 343.0 / 343.0 / 0.0 | [NPY](tensors/0002742.npy) |
| 2743 | `model.layers.11.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2744 | `model.layers.11.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2745 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.740966796875 / 0.9022817549113021 | [NPY](tensors/0002745.npy) |
| 2746 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3046875 / -0.06294980645179749 / 0.6646640154085409 | [NPY](tensors/0002746.npy) |
| 2747 | `model.layers.11.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2748 | `model.layers.11.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.0 / 112.5 / 0.0627029922273424 / 3.169262073212285 | [NPY](tensors/0002748.npy) |
| 2749 | `model.layers.11.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.0625 / 9.25 / -0.002084717038087547 / 1.3142634249986747 | [NPY](tensors/0002749.npy) |
| 2750 | `model.layers.11.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.0 / 112.5 / 0.0627029922273424 / 3.169262073212285 | [NPY](tensors/0002750.npy) |
| 2751 | `model.layers.11.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.125 / 30.5 / -0.02939373254776001 / 3.5281955892981585 | [NPY](tensors/0002751.npy) |
| 2752 | `model.layers.11.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.0 / 112.5 / 0.0627029922273424 / 3.169262073212285 | [NPY](tensors/0002752.npy) |
| 2753 | `model.layers.11.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.0625 / 9.375 / 0.005947113037109375 / 2.809465570661068 | [NPY](tensors/0002753.npy) |
| 2754 | `model.layers.11.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.8125 / 8.25 / -0.010407880647107959 / 1.5064390593238068 | [NPY](tensors/0002754.npy) |
| 2755 | `model.layers.11.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 71.5 / -0.09260024544265535 / 4.390740179635755 | [NPY](tensors/0002755.npy) |
| 2756 | `model.layers.11.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 71.5 / -0.09260024544265535 / 4.390740179635755 | [NPY](tensors/0002756.npy) |
| 2757 | `model.layers.11.self_attn` | 23 | `output[1]` | [1, 64, 1, 344] | torch.bfloat16 → float32 | 4.547473508864641e-11 / 0.9375 / 0.0024412326317263815 / 0.015916346814196954 | [NPY](tensors/0002757.npy) |
| 2758 | `model.layers.11.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -380.0 / 516.0 / 0.6214504665798611 / 25.483788542030474 | [NPY](tensors/0002758.npy) |
| 2759 | `model.layers.11.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.125 / 3.609375 / 0.004432291454739041 / 0.7793070858416011 | [NPY](tensors/0002759.npy) |
| 2760 | `model.layers.11.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.125 / 3.609375 / 0.004432291454739041 / 0.7793070858416011 | [NPY](tensors/0002760.npy) |
| 2761 | `model.layers.11.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.125 / 3.609375 / 0.004432291454739041 / 0.7793070858416011 | [NPY](tensors/0002761.npy) |
| 2762 | `model.layers.11.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2763 | `model.layers.11.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2764 | `model.layers.11.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2765 | `model.layers.11.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -300.0 / 270.0 / 0.18228092193603515 / 10.278058072721066 | [NPY](tensors/0002765.npy) |
| 2766 | `model.layers.11.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -300.0 / 270.0 / 0.18228092193603515 / 10.278058072721066 | [NPY](tensors/0002766.npy) |
| 2767 | `model.layers.11.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.125 / 1.28125 / -0.11540985107421875 / 0.6870427215737802 | [NPY](tensors/0002767.npy) |
| 2768 | `model.layers.11` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -680.0 / 784.0 / 0.8028401692708333 / 32.669342467087475 | [NPY](tensors/0002768.npy) |
| 2847 | `model.layers.11` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -404.0 / 556.0 / 0.3960210164388021 / 24.241674428592177 | [NPY](tensors/0002847.npy) |
| 2848 | `model.layers.11` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 345] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002848.npy) |
| 2849 | `model.layers.11` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8131542205810547 / 0.8233916239555151 | [NPY](tensors/0002849.npy) |
| 2850 | `model.layers.11` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.07140964269638062 / 0.6820182328303498 | [NPY](tensors/0002850.npy) |
| 2851 | `model.layers.11` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 344.0 / 344.0 / 344.0 / 0.0 | [NPY](tensors/0002851.npy) |
| 2852 | `model.layers.11` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2853 | `model.layers.11` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2854 | `model.layers.11` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2855 | `model.layers.11.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -404.0 / 556.0 / 0.3960210164388021 / 24.241674428592177 | [NPY](tensors/0002855.npy) |
| 2856 | `model.layers.11.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 107.5 / 0.0523564272456699 / 3.1116583036311005 | [NPY](tensors/0002856.npy) |
| 2857 | `model.layers.11.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 107.5 / 0.0523564272456699 / 3.1116583036311005 | [NPY](tensors/0002857.npy) |
| 2858 | `model.layers.11.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 345] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002858.npy) |
| 2859 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 344.0 / 344.0 / 344.0 / 0.0 | [NPY](tensors/0002859.npy) |
| 2860 | `model.layers.11.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2861 | `model.layers.11.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2862 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8131542205810547 / 0.8233916239555151 | [NPY](tensors/0002862.npy) |
| 2863 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.07140964269638062 / 0.6820182328303498 | [NPY](tensors/0002863.npy) |
| 2864 | `model.layers.11.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2865 | `model.layers.11.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 107.5 / 0.0523564272456699 / 3.1116583036311005 | [NPY](tensors/0002865.npy) |
| 2866 | `model.layers.11.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 10.25 / 0.011482009664177895 / 1.290400064925688 | [NPY](tensors/0002866.npy) |
| 2867 | `model.layers.11.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 107.5 / 0.0523564272456699 / 3.1116583036311005 | [NPY](tensors/0002867.npy) |
| 2868 | `model.layers.11.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.25 / 33.0 / 0.06894755363464355 / 3.541230642203684 | [NPY](tensors/0002868.npy) |
| 2869 | `model.layers.11.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 107.5 / 0.0523564272456699 / 3.1116583036311005 | [NPY](tensors/0002869.npy) |
| 2870 | `model.layers.11.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.0625 / 7.6875 / -0.025888025760650635 / 2.2042536042018113 | [NPY](tensors/0002870.npy) |
| 2871 | `model.layers.11.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0 / 7.6875 / -0.026772255077958107 / 1.437880970422007 | [NPY](tensors/0002871.npy) |
| 2872 | `model.layers.11.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.5 / 76.0 / -0.001514895757039388 / 4.006609379860143 | [NPY](tensors/0002872.npy) |
| 2873 | `model.layers.11.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.5 / 76.0 / -0.001514895757039388 / 4.006609379860143 | [NPY](tensors/0002873.npy) |
| 2874 | `model.layers.11.self_attn` | 24 | `output[1]` | [1, 64, 1, 345] | torch.bfloat16 → float32 | 4.4792614062316716e-11 / 0.92578125 / 0.0024601815211998876 / 0.015021618166746973 | [NPY](tensors/0002874.npy) |
| 2875 | `model.layers.11.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -328.0 / 454.0 / 0.3943803575303819 / 23.66338772933255 | [NPY](tensors/0002875.npy) |
| 2876 | `model.layers.11.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.984375 / 4.34375 / -0.003874446948369344 / 0.7541879588962265 | [NPY](tensors/0002876.npy) |
| 2877 | `model.layers.11.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.984375 / 4.34375 / -0.003874446948369344 / 0.7541879588962265 | [NPY](tensors/0002877.npy) |
| 2878 | `model.layers.11.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.984375 / 4.34375 / -0.003874446948369344 / 0.7541879588962265 | [NPY](tensors/0002878.npy) |
| 2879 | `model.layers.11.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2880 | `model.layers.11.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2881 | `model.layers.11.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2882 | `model.layers.11.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -126.5 / 130.0 / 0.04227291742960612 / 6.219996143611638 | [NPY](tensors/0002882.npy) |
| 2883 | `model.layers.11.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -126.5 / 130.0 / 0.04227291742960612 / 6.219996143611638 | [NPY](tensors/0002883.npy) |
| 2884 | `model.layers.11.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.1796875 / -0.06839478015899658 / 0.552970213206567 | [NPY](tensors/0002884.npy) |
| 2885 | `model.layers.11` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -454.0 / 576.0 / 0.43709852430555557 / 27.29111921619929 | [NPY](tensors/0002885.npy) |
| 2964 | `model.layers.11` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -488.0 / 616.0 / 0.2495763142903646 / 25.990230398020362 | [NPY](tensors/0002964.npy) |
| 2965 | `model.layers.11` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 346] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002965.npy) |
| 2966 | `model.layers.11` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.8764495849609375 / 0.8009113437243138 | [NPY](tensors/0002966.npy) |
| 2967 | `model.layers.11` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.020697563886642456 / 0.632324519915983 | [NPY](tensors/0002967.npy) |
| 2968 | `model.layers.11` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 345.0 / 345.0 / 345.0 / 0.0 | [NPY](tensors/0002968.npy) |
| 2969 | `model.layers.11` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2970 | `model.layers.11` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2971 | `model.layers.11` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2972 | `model.layers.11.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -488.0 / 616.0 / 0.2495763142903646 / 25.990230398020362 | [NPY](tensors/0002972.npy) |
| 2973 | `model.layers.11.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 111.0 / 0.03811285230848524 / 3.2185479191084645 | [NPY](tensors/0002973.npy) |
| 2974 | `model.layers.11.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 111.0 / 0.03811285230848524 / 3.2185479191084645 | [NPY](tensors/0002974.npy) |
| 2975 | `model.layers.11.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 346] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002975.npy) |
| 2976 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 345.0 / 345.0 / 345.0 / 0.0 | [NPY](tensors/0002976.npy) |
| 2977 | `model.layers.11.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2978 | `model.layers.11.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2979 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.8764495849609375 / 0.8009113437243138 | [NPY](tensors/0002979.npy) |
| 2980 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.020697563886642456 / 0.632324519915983 | [NPY](tensors/0002980.npy) |
| 2981 | `model.layers.11.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2982 | `model.layers.11.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 111.0 / 0.03811285230848524 / 3.2185479191084645 | [NPY](tensors/0002982.npy) |
| 2983 | `model.layers.11.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.375 / 9.1875 / 0.005548528861254454 / 1.3036706919453025 | [NPY](tensors/0002983.npy) |
| 2984 | `model.layers.11.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 111.0 / 0.03811285230848524 / 3.2185479191084645 | [NPY](tensors/0002984.npy) |
| 2985 | `model.layers.11.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.375 / 32.25 / 0.011498495936393738 / 3.4026529129442724 | [NPY](tensors/0002985.npy) |
| 2986 | `model.layers.11.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 111.0 / 0.03811285230848524 / 3.2185479191084645 | [NPY](tensors/0002986.npy) |
| 2987 | `model.layers.11.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.4375 / 8.3125 / 0.028599292039871216 / 2.291570370005751 | [NPY](tensors/0002987.npy) |
| 2988 | `model.layers.11.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.09375 / 8.1875 / -0.021326571208192036 / 1.4282667295111275 | [NPY](tensors/0002988.npy) |
| 2989 | `model.layers.11.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -229.0 / 202.0 / -0.05678979539208942 / 6.763657460152531 | [NPY](tensors/0002989.npy) |
| 2990 | `model.layers.11.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -229.0 / 202.0 / -0.05678979539208942 / 6.763657460152531 | [NPY](tensors/0002990.npy) |
| 2991 | `model.layers.11.self_attn` | 25 | `output[1]` | [1, 64, 1, 346] | torch.bfloat16 → float32 | 9.549694368615746e-11 / 0.9296875 / 0.002122643651562136 / 0.018500012656262887 | [NPY](tensors/0002991.npy) |
| 2992 | `model.layers.11.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -286.0 / 388.0 / 0.19371422661675347 / 23.118809731795697 | [NPY](tensors/0002992.npy) |
| 2993 | `model.layers.11.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.703125 / 4.1875 / -0.005944985813564724 / 0.8186889597603328 | [NPY](tensors/0002993.npy) |
| 2994 | `model.layers.11.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.703125 / 4.1875 / -0.005944985813564724 / 0.8186889597603328 | [NPY](tensors/0002994.npy) |
| 2995 | `model.layers.11.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.703125 / 4.1875 / -0.005944985813564724 / 0.8186889597603328 | [NPY](tensors/0002995.npy) |
| 2996 | `model.layers.11.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2997 | `model.layers.11.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2998 | `model.layers.11.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2999 | `model.layers.11.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -296.0 / 216.0 / 0.13165514204237197 / 9.35559439701744 | [NPY](tensors/0002999.npy) |
| 3000 | `model.layers.11.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -296.0 / 216.0 / 0.13165514204237197 / 9.35559439701744 | [NPY](tensors/0003000.npy) |
| 3001 | `model.layers.11.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.203125 / 1.5078125 / -0.21320724487304688 / 0.8181188958724865 | [NPY](tensors/0003001.npy) |
| 3002 | `model.layers.11` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -584.0 / 604.0 / 0.32392679850260414 / 28.895132558536993 | [NPY](tensors/0003002.npy) |
| 3081 | `model.layers.11` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -416.0 / 560.0 / 0.3901775783962674 / 23.35131374277619 | [NPY](tensors/0003081.npy) |
| 3082 | `model.layers.11` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 347] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003082.npy) |
| 3083 | `model.layers.11` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.887237548828125 / 0.808167570442007 | [NPY](tensors/0003083.npy) |
| 3084 | `model.layers.11` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.06384772062301636 / 0.6046658936992718 | [NPY](tensors/0003084.npy) |
| 3085 | `model.layers.11` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 346.0 / 346.0 / 346.0 / 0.0 | [NPY](tensors/0003085.npy) |
| 3086 | `model.layers.11` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3087 | `model.layers.11` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3088 | `model.layers.11` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3089 | `model.layers.11.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -416.0 / 560.0 / 0.3901775783962674 / 23.35131374277619 | [NPY](tensors/0003089.npy) |
| 3090 | `model.layers.11.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 112.5 / 0.05427056286070082 / 3.274342651248588 | [NPY](tensors/0003090.npy) |
| 3091 | `model.layers.11.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 112.5 / 0.05427056286070082 / 3.274342651248588 | [NPY](tensors/0003091.npy) |
| 3092 | `model.layers.11.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 347] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003092.npy) |
| 3093 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 346.0 / 346.0 / 346.0 / 0.0 | [NPY](tensors/0003093.npy) |
| 3094 | `model.layers.11.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3095 | `model.layers.11.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3096 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.887237548828125 / 0.808167570442007 | [NPY](tensors/0003096.npy) |
| 3097 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.06384772062301636 / 0.6046658936992718 | [NPY](tensors/0003097.npy) |
| 3098 | `model.layers.11.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3099 | `model.layers.11.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 112.5 / 0.05427056286070082 / 3.274342651248588 | [NPY](tensors/0003099.npy) |
| 3100 | `model.layers.11.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.03125 / 10.0625 / 0.017078568460419774 / 1.321259395906015 | [NPY](tensors/0003100.npy) |
| 3101 | `model.layers.11.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 112.5 / 0.05427056286070082 / 3.274342651248588 | [NPY](tensors/0003101.npy) |
| 3102 | `model.layers.11.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.875 / 33.5 / 0.0004024878144264221 / 3.6166428701707902 | [NPY](tensors/0003102.npy) |
| 3103 | `model.layers.11.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 112.5 / 0.05427056286070082 / 3.274342651248588 | [NPY](tensors/0003103.npy) |
| 3104 | `model.layers.11.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.59375 / 8.625 / 0.054465413093566895 / 2.4786740614087326 | [NPY](tensors/0003104.npy) |
| 3105 | `model.layers.11.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.90625 / 7.46875 / 0.0048778303898870945 / 1.386922069421499 | [NPY](tensors/0003105.npy) |
| 3106 | `model.layers.11.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -181.0 / 180.0 / -0.06518741183810764 / 5.784333614098425 | [NPY](tensors/0003106.npy) |
| 3107 | `model.layers.11.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -181.0 / 180.0 / -0.06518741183810764 / 5.784333614098425 | [NPY](tensors/0003107.npy) |
| 3108 | `model.layers.11.self_attn` | 26 | `output[1]` | [1, 64, 1, 347] | torch.bfloat16 → float32 | 2.5920599000528455e-11 / 0.8828125 / 0.002252659870340119 / 0.01785726445790764 | [NPY](tensors/0003108.npy) |
| 3109 | `model.layers.11.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -236.0 / 380.0 / 0.3256622314453125 / 21.31297548579224 | [NPY](tensors/0003109.npy) |
| 3110 | `model.layers.11.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.09375 / 3.71875 / 0.007694138752089606 / 0.7347869903505285 | [NPY](tensors/0003110.npy) |
| 3111 | `model.layers.11.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.09375 / 3.71875 / 0.007694138752089606 / 0.7347869903505285 | [NPY](tensors/0003111.npy) |
| 3112 | `model.layers.11.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.09375 / 3.71875 / 0.007694138752089606 / 0.7347869903505285 | [NPY](tensors/0003112.npy) |
| 3113 | `model.layers.11.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3114 | `model.layers.11.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3115 | `model.layers.11.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3116 | `model.layers.11.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -278.0 / 191.0 / 0.07578139040205213 / 8.904846182601744 | [NPY](tensors/0003116.npy) |
| 3117 | `model.layers.11.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -278.0 / 191.0 / 0.07578139040205213 / 8.904846182601744 | [NPY](tensors/0003117.npy) |
| 3118 | `model.layers.11.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.140625 / 1.515625 / -0.2126922607421875 / 0.9170885054517927 | [NPY](tensors/0003118.npy) |
| 3119 | `model.layers.11` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -512.0 / 560.0 / 0.40061747233072914 / 26.795473013451144 | [NPY](tensors/0003119.npy) |
| 3198 | `model.layers.11` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -462.0 / 520.0 / 0.601454332139757 / 23.762690510372042 | [NPY](tensors/0003198.npy) |
| 3199 | `model.layers.11` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 348] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003199.npy) |
| 3200 | `model.layers.11` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.8368129730224609 / 0.8204651963806046 | [NPY](tensors/0003200.npy) |
| 3201 | `model.layers.11` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.1309933364391327 / 0.6478045244450656 | [NPY](tensors/0003201.npy) |
| 3202 | `model.layers.11` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 347.0 / 347.0 / 347.0 / 0.0 | [NPY](tensors/0003202.npy) |
| 3203 | `model.layers.11` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3204 | `model.layers.11` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3205 | `model.layers.11` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3206 | `model.layers.11.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -462.0 / 520.0 / 0.601454332139757 / 23.762690510372042 | [NPY](tensors/0003206.npy) |
| 3207 | `model.layers.11.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.0 / 102.5 / 0.06510425143771702 / 3.2717186100580973 | [NPY](tensors/0003207.npy) |
| 3208 | `model.layers.11.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.0 / 102.5 / 0.06510425143771702 / 3.2717186100580973 | [NPY](tensors/0003208.npy) |
| 3209 | `model.layers.11.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 348] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003209.npy) |
| 3210 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 347.0 / 347.0 / 347.0 / 0.0 | [NPY](tensors/0003210.npy) |
| 3211 | `model.layers.11.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3212 | `model.layers.11.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3213 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.8368129730224609 / 0.8204651963806046 | [NPY](tensors/0003213.npy) |
| 3214 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.1309933364391327 / 0.6478045244450656 | [NPY](tensors/0003214.npy) |
| 3215 | `model.layers.11.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3216 | `model.layers.11.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.0 / 102.5 / 0.06510425143771702 / 3.2717186100580973 | [NPY](tensors/0003216.npy) |
| 3217 | `model.layers.11.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 9.0625 / 0.011899820994585752 / 1.3584932134857317 | [NPY](tensors/0003217.npy) |
| 3218 | `model.layers.11.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.0 / 102.5 / 0.06510425143771702 / 3.2717186100580973 | [NPY](tensors/0003218.npy) |
| 3219 | `model.layers.11.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.875 / 37.75 / 0.025661781430244446 / 3.779020120054823 | [NPY](tensors/0003219.npy) |
| 3220 | `model.layers.11.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.0 / 102.5 / 0.06510425143771702 / 3.2717186100580973 | [NPY](tensors/0003220.npy) |
| 3221 | `model.layers.11.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.59375 / 7.03125 / 0.01025363802909851 / 2.4502070849511255 | [NPY](tensors/0003221.npy) |
| 3222 | `model.layers.11.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 7.25 / -0.0004387805820442736 / 1.4338714627255804 | [NPY](tensors/0003222.npy) |
| 3223 | `model.layers.11.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -155.0 / 153.0 / 0.007792321178648207 / 5.1808444507687925 | [NPY](tensors/0003223.npy) |
| 3224 | `model.layers.11.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -155.0 / 153.0 / 0.007792321178648207 / 5.1808444507687925 | [NPY](tensors/0003224.npy) |
| 3225 | `model.layers.11.self_attn` | 27 | `output[1]` | [1, 64, 1, 348] | torch.bfloat16 → float32 | 1.7053025658242404e-12 / 0.90625 / 0.00228592784429994 / 0.017214771011641865 | [NPY](tensors/0003225.npy) |
| 3226 | `model.layers.11.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -308.0 / 364.0 / 0.609969245062934 / 22.68245447882037 | [NPY](tensors/0003226.npy) |
| 3227 | `model.layers.11.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.703125 / 3.171875 / 0.015875246789720323 / 0.7304727794100172 | [NPY](tensors/0003227.npy) |
| 3228 | `model.layers.11.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.703125 / 3.171875 / 0.015875246789720323 / 0.7304727794100172 | [NPY](tensors/0003228.npy) |
| 3229 | `model.layers.11.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.703125 / 3.171875 / 0.015875246789720323 / 0.7304727794100172 | [NPY](tensors/0003229.npy) |
| 3230 | `model.layers.11.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3231 | `model.layers.11.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3232 | `model.layers.11.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3233 | `model.layers.11.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -256.0 / 224.0 / 0.14212100240919326 / 8.94120890684358 | [NPY](tensors/0003233.npy) |
| 3234 | `model.layers.11.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -256.0 / 224.0 / 0.14212100240919326 / 8.94120890684358 | [NPY](tensors/0003234.npy) |
| 3235 | `model.layers.11.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.9375 / 1.515625 / -0.17830657958984375 / 0.8868454758783788 | [NPY](tensors/0003235.npy) |
| 3236 | `model.layers.11` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -564.0 / 588.0 / 0.7520331488715277 / 28.396438717754044 | [NPY](tensors/0003236.npy) |
| 3315 | `model.layers.11` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -386.0 / 494.0 / 0.6112438625759549 / 23.286805365428258 | [NPY](tensors/0003315.npy) |
| 3316 | `model.layers.11` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 349] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003316.npy) |
| 3317 | `model.layers.11` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7588653564453125 / 0.8828955932720353 | [NPY](tensors/0003317.npy) |
| 3318 | `model.layers.11` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14290890097618103 / 0.6590419455082627 | [NPY](tensors/0003318.npy) |
| 3319 | `model.layers.11` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 348.0 / 348.0 / 348.0 / 0.0 | [NPY](tensors/0003319.npy) |
| 3320 | `model.layers.11` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3321 | `model.layers.11` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3322 | `model.layers.11` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3323 | `model.layers.11.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -386.0 / 494.0 / 0.6112438625759549 / 23.286805365428258 | [NPY](tensors/0003323.npy) |
| 3324 | `model.layers.11.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 99.5 / 0.0638402541478475 / 3.0763609054612115 | [NPY](tensors/0003324.npy) |
| 3325 | `model.layers.11.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 99.5 / 0.0638402541478475 / 3.0763609054612115 | [NPY](tensors/0003325.npy) |
| 3326 | `model.layers.11.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 349] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003326.npy) |
| 3327 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 348.0 / 348.0 / 348.0 / 0.0 | [NPY](tensors/0003327.npy) |
| 3328 | `model.layers.11.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3329 | `model.layers.11.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3330 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7588653564453125 / 0.8828955932720353 | [NPY](tensors/0003330.npy) |
| 3331 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14290890097618103 / 0.6590419455082627 | [NPY](tensors/0003331.npy) |
| 3332 | `model.layers.11.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3333 | `model.layers.11.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 99.5 / 0.0638402541478475 / 3.0763609054612115 | [NPY](tensors/0003333.npy) |
| 3334 | `model.layers.11.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.9375 / 8.75 / -0.0034069321118295193 / 1.4122154938232256 | [NPY](tensors/0003334.npy) |
| 3335 | `model.layers.11.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 99.5 / 0.0638402541478475 / 3.0763609054612115 | [NPY](tensors/0003335.npy) |
| 3336 | `model.layers.11.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.0 / 37.5 / 0.0016104131937026978 / 3.745081165106873 | [NPY](tensors/0003336.npy) |
| 3337 | `model.layers.11.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 99.5 / 0.0638402541478475 / 3.0763609054612115 | [NPY](tensors/0003337.npy) |
| 3338 | `model.layers.11.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.8125 / 6.71875 / -0.17548763751983643 / 2.389205254011513 | [NPY](tensors/0003338.npy) |
| 3339 | `model.layers.11.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.90625 / 7.84375 / -0.028779928805306554 / 1.5269759913735101 | [NPY](tensors/0003339.npy) |
| 3340 | `model.layers.11.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -178.0 / 159.0 / 0.023910607231987846 / 5.884140259989764 | [NPY](tensors/0003340.npy) |
| 3341 | `model.layers.11.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -178.0 / 159.0 / 0.023910607231987846 / 5.884140259989764 | [NPY](tensors/0003341.npy) |
| 3342 | `model.layers.11.self_attn` | 28 | `output[1]` | [1, 64, 1, 349] | torch.bfloat16 → float32 | 8.384404281969182e-13 / 0.9453125 / 0.002300221985231988 / 0.018743001195278122 | [NPY](tensors/0003342.npy) |
| 3343 | `model.layers.11.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -227.0 / 316.0 / 0.6350857204861111 / 21.99521720584014 | [NPY](tensors/0003343.npy) |
| 3344 | `model.layers.11.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.1875 / 0.013581629594167073 / 0.7998092862282793 | [NPY](tensors/0003344.npy) |
| 3345 | `model.layers.11.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.1875 / 0.013581629594167073 / 0.7998092862282793 | [NPY](tensors/0003345.npy) |
| 3346 | `model.layers.11.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.1875 / 0.013581629594167073 / 0.7998092862282793 | [NPY](tensors/0003346.npy) |
| 3347 | `model.layers.11.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3348 | `model.layers.11.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3349 | `model.layers.11.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3350 | `model.layers.11.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -310.0 / 338.0 / 0.12959445317586263 / 11.223154576120253 | [NPY](tensors/0003350.npy) |
| 3351 | `model.layers.11.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -310.0 / 338.0 / 0.12959445317586263 / 11.223154576120253 | [NPY](tensors/0003351.npy) |
| 3352 | `model.layers.11.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.28125 / 1.8046875 / -0.17237234115600586 / 0.8671953665596578 | [NPY](tensors/0003352.npy) |
| 3353 | `model.layers.11` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -536.0 / 656.0 / 0.7659267849392362 / 29.046944468452985 | [NPY](tensors/0003353.npy) |
| 3432 | `model.layers.11` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -244.0 / 388.0 / 0.5853161282009549 / 18.977355774906815 | [NPY](tensors/0003432.npy) |
| 3433 | `model.layers.11` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 350] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003433.npy) |
| 3434 | `model.layers.11` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.701873779296875 / 0.9298159802037973 | [NPY](tensors/0003434.npy) |
| 3435 | `model.layers.11` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.10132250189781189 / 0.6650396518932735 | [NPY](tensors/0003435.npy) |
| 3436 | `model.layers.11` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 349.0 / 349.0 / 349.0 / 0.0 | [NPY](tensors/0003436.npy) |
| 3437 | `model.layers.11` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3438 | `model.layers.11` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3439 | `model.layers.11` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3440 | `model.layers.11.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -244.0 / 388.0 / 0.5853161282009549 / 18.977355774906815 | [NPY](tensors/0003440.npy) |
| 3441 | `model.layers.11.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -67.5 / 96.0 / 0.08245269457499187 / 2.927457179302215 | [NPY](tensors/0003441.npy) |
| 3442 | `model.layers.11.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -67.5 / 96.0 / 0.08245269457499187 / 2.927457179302215 | [NPY](tensors/0003442.npy) |
| 3443 | `model.layers.11.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 350] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003443.npy) |
| 3444 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 349.0 / 349.0 / 349.0 / 0.0 | [NPY](tensors/0003444.npy) |
| 3445 | `model.layers.11.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3446 | `model.layers.11.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3447 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.701873779296875 / 0.9298159802037973 | [NPY](tensors/0003447.npy) |
| 3448 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.10132250189781189 / 0.6650396518932735 | [NPY](tensors/0003448.npy) |
| 3449 | `model.layers.11.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3450 | `model.layers.11.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -67.5 / 96.0 / 0.08245269457499187 / 2.927457179302215 | [NPY](tensors/0003450.npy) |
| 3451 | `model.layers.11.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 9.3125 / 0.023403017432428896 / 1.4066357097456914 | [NPY](tensors/0003451.npy) |
| 3452 | `model.layers.11.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -67.5 / 96.0 / 0.08245269457499187 / 2.927457179302215 | [NPY](tensors/0003452.npy) |
| 3453 | `model.layers.11.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.75 / 44.25 / 0.07736878097057343 / 4.428592099415412 | [NPY](tensors/0003453.npy) |
| 3454 | `model.layers.11.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -67.5 / 96.0 / 0.08245269457499187 / 2.927457179302215 | [NPY](tensors/0003454.npy) |
| 3455 | `model.layers.11.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.71875 / 7.1875 / -0.004553079605102539 / 2.279498856955311 | [NPY](tensors/0003455.npy) |
| 3456 | `model.layers.11.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.65625 / 6.125 / -0.03794386109802872 / 1.5129353871223148 | [NPY](tensors/0003456.npy) |
| 3457 | `model.layers.11.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.625 / 28.25 / -0.005506151252322727 / 3.7675161075003087 | [NPY](tensors/0003457.npy) |
| 3458 | `model.layers.11.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.625 / 28.25 / -0.005506151252322727 / 3.7675161075003087 | [NPY](tensors/0003458.npy) |
| 3459 | `model.layers.11.self_attn` | 29 | `output[1]` | [1, 64, 1, 350] | torch.bfloat16 → float32 | 2.2879476091475226e-12 / 0.9453125 / 0.002629419451972883 / 0.013594970807479756 | [NPY](tensors/0003459.npy) |
| 3460 | `model.layers.11.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -220.0 / 362.0 / 0.5796978844536675 / 19.878451317273033 | [NPY](tensors/0003460.npy) |
| 3461 | `model.layers.11.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.53125 / 3.59375 / 0.007829873429404364 / 0.7239411512214586 | [NPY](tensors/0003461.npy) |
| 3462 | `model.layers.11.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.53125 / 3.59375 / 0.007829873429404364 / 0.7239411512214586 | [NPY](tensors/0003462.npy) |
| 3463 | `model.layers.11.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.53125 / 3.59375 / 0.007829873429404364 / 0.7239411512214586 | [NPY](tensors/0003463.npy) |
| 3464 | `model.layers.11.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3465 | `model.layers.11.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3466 | `model.layers.11.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3467 | `model.layers.11.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -247.0 / 158.0 / 0.21040366490681967 / 7.943840460461842 | [NPY](tensors/0003467.npy) |
| 3468 | `model.layers.11.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -247.0 / 158.0 / 0.21040366490681967 / 7.943840460461842 | [NPY](tensors/0003468.npy) |
| 3469 | `model.layers.11.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8828125 / 1.984375 / -0.10319089889526367 / 0.7665958082596112 | [NPY](tensors/0003469.npy) |
| 3470 | `model.layers.11` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -468.0 / 520.0 / 0.7889477199978299 / 24.59632576770307 | [NPY](tensors/0003470.npy) |
| 3549 | `model.layers.11` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -288.0 / 440.0 / 0.2888341267903646 / 19.672422503234152 | [NPY](tensors/0003549.npy) |
| 3550 | `model.layers.11` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 351] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003550.npy) |
| 3551 | `model.layers.11` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.690826416015625 / 0.927895842605205 | [NPY](tensors/0003551.npy) |
| 3552 | `model.layers.11` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.04170632362365723 / 0.685352030153117 | [NPY](tensors/0003552.npy) |
| 3553 | `model.layers.11` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 350.0 / 350.0 / 350.0 / 0.0 | [NPY](tensors/0003553.npy) |
| 3554 | `model.layers.11` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3555 | `model.layers.11` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3556 | `model.layers.11` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3557 | `model.layers.11.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -288.0 / 440.0 / 0.2888341267903646 / 19.672422503234152 | [NPY](tensors/0003557.npy) |
| 3558 | `model.layers.11.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 105.0 / 0.04858560429679023 / 3.111044507925663 | [NPY](tensors/0003558.npy) |
| 3559 | `model.layers.11.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 105.0 / 0.04858560429679023 / 3.111044507925663 | [NPY](tensors/0003559.npy) |
| 3560 | `model.layers.11.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 351] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003560.npy) |
| 3561 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 350.0 / 350.0 / 350.0 / 0.0 | [NPY](tensors/0003561.npy) |
| 3562 | `model.layers.11.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3563 | `model.layers.11.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3564 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.690826416015625 / 0.927895842605205 | [NPY](tensors/0003564.npy) |
| 3565 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.04170632362365723 / 0.685352030153117 | [NPY](tensors/0003565.npy) |
| 3566 | `model.layers.11.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3567 | `model.layers.11.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 105.0 / 0.04858560429679023 / 3.111044507925663 | [NPY](tensors/0003567.npy) |
| 3568 | `model.layers.11.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.0 / 8.375 / 0.019275844329968095 / 1.3592789682639845 | [NPY](tensors/0003568.npy) |
| 3569 | `model.layers.11.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 105.0 / 0.04858560429679023 / 3.111044507925663 | [NPY](tensors/0003569.npy) |
| 3570 | `model.layers.11.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.5 / 36.25 / 0.1205344870686531 / 3.927302269672066 | [NPY](tensors/0003570.npy) |
| 3571 | `model.layers.11.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 105.0 / 0.04858560429679023 / 3.111044507925663 | [NPY](tensors/0003571.npy) |
| 3572 | `model.layers.11.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.46875 / 7.15625 / -0.11971497535705566 / 2.266486871694458 | [NPY](tensors/0003572.npy) |
| 3573 | `model.layers.11.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.34375 / 7.125 / -0.0055848173797130585 / 1.4751763803130102 | [NPY](tensors/0003573.npy) |
| 3574 | `model.layers.11.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -158.0 / 156.0 / -0.07194579972161187 / 5.8161370132168235 | [NPY](tensors/0003574.npy) |
| 3575 | `model.layers.11.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -158.0 / 156.0 / -0.07194579972161187 / 5.8161370132168235 | [NPY](tensors/0003575.npy) |
| 3576 | `model.layers.11.self_attn` | 30 | `output[1]` | [1, 64, 1, 351] | torch.bfloat16 → float32 | 1.0516032489249483e-12 / 0.96484375 / 0.0025112426083962547 / 0.016326159322434405 | [NPY](tensors/0003576.npy) |
| 3577 | `model.layers.11.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -233.0 / 282.0 / 0.2170901828342014 / 18.95642513846845 | [NPY](tensors/0003577.npy) |
| 3578 | `model.layers.11.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.90625 / 3.890625 / -0.001967691050635444 / 0.7960599035081337 | [NPY](tensors/0003578.npy) |
| 3579 | `model.layers.11.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.90625 / 3.890625 / -0.001967691050635444 / 0.7960599035081337 | [NPY](tensors/0003579.npy) |
| 3580 | `model.layers.11.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.90625 / 3.890625 / -0.001967691050635444 / 0.7960599035081337 | [NPY](tensors/0003580.npy) |
| 3581 | `model.layers.11.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3582 | `model.layers.11.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3583 | `model.layers.11.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3584 | `model.layers.11.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -274.0 / 286.0 / 0.19381402598487008 / 9.9925010768168 | [NPY](tensors/0003584.npy) |
| 3585 | `model.layers.11.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -274.0 / 286.0 / 0.19381402598487008 / 9.9925010768168 | [NPY](tensors/0003585.npy) |
| 3586 | `model.layers.11.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.5 / 1.6171875 / -0.1571812629699707 / 0.8430670676490287 | [NPY](tensors/0003586.npy) |
| 3587 | `model.layers.11` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -406.0 / 568.0 / 0.41074015299479166 / 24.66614768652099 | [NPY](tensors/0003587.npy) |
| 3666 | `model.layers.11` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -376.0 / 572.0 / 0.3623540242513021 / 21.2788807189857 | [NPY](tensors/0003666.npy) |
| 3667 | `model.layers.11` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 352] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003667.npy) |
| 3668 | `model.layers.11` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.715423583984375 / 0.9264461804361078 | [NPY](tensors/0003668.npy) |
| 3669 | `model.layers.11` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.0011060535907745361 / 0.6627134184873914 | [NPY](tensors/0003669.npy) |
| 3670 | `model.layers.11` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 351.0 / 351.0 / 351.0 / 0.0 | [NPY](tensors/0003670.npy) |
| 3671 | `model.layers.11` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3672 | `model.layers.11` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3673 | `model.layers.11` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3674 | `model.layers.11.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -376.0 / 572.0 / 0.3623540242513021 / 21.2788807189857 | [NPY](tensors/0003674.npy) |
| 3675 | `model.layers.11.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 126.0 / 0.057827981975343494 / 3.4503367425125107 | [NPY](tensors/0003675.npy) |
| 3676 | `model.layers.11.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 126.0 / 0.057827981975343494 / 3.4503367425125107 | [NPY](tensors/0003676.npy) |
| 3677 | `model.layers.11.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 352] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003677.npy) |
| 3678 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 351.0 / 351.0 / 351.0 / 0.0 | [NPY](tensors/0003678.npy) |
| 3679 | `model.layers.11.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3680 | `model.layers.11.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3681 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.715423583984375 / 0.9264461804361078 | [NPY](tensors/0003681.npy) |
| 3682 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.0011060535907745361 / 0.6627134184873914 | [NPY](tensors/0003682.npy) |
| 3683 | `model.layers.11.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3684 | `model.layers.11.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 126.0 / 0.057827981975343494 / 3.4503367425125107 | [NPY](tensors/0003684.npy) |
| 3685 | `model.layers.11.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 7.8125 / -0.0029004374518990517 / 1.285897290523397 | [NPY](tensors/0003685.npy) |
| 3686 | `model.layers.11.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 126.0 / 0.057827981975343494 / 3.4503367425125107 | [NPY](tensors/0003686.npy) |
| 3687 | `model.layers.11.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.375 / 35.25 / -0.024305343627929688 / 3.6568334696709095 | [NPY](tensors/0003687.npy) |
| 3688 | `model.layers.11.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 126.0 / 0.057827981975343494 / 3.4503367425125107 | [NPY](tensors/0003688.npy) |
| 3689 | `model.layers.11.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.03125 / 7.84375 / -0.10912388563156128 / 2.3142637205653225 | [NPY](tensors/0003689.npy) |
| 3690 | `model.layers.11.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.90625 / 6.375 / -0.008106344252155395 / 1.376612089675874 | [NPY](tensors/0003690.npy) |
| 3691 | `model.layers.11.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -222.0 / 188.0 / -0.1133514232105679 / 6.463697440623471 | [NPY](tensors/0003691.npy) |
| 3692 | `model.layers.11.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -222.0 / 188.0 / -0.1133514232105679 / 6.463697440623471 | [NPY](tensors/0003692.npy) |
| 3693 | `model.layers.11.self_attn` | 31 | `output[1]` | [1, 64, 1, 352] | torch.bfloat16 → float32 | 3.241851231905457e-14 / 0.9453125 / 0.0023824289060299275 / 0.015945762544371703 | [NPY](tensors/0003693.npy) |
| 3694 | `model.layers.11.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -188.0 / 350.0 / 0.24904344346788193 / 18.693879867913147 | [NPY](tensors/0003694.npy) |
| 3695 | `model.layers.11.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.984375 / 5.21875 / 0.006008876694573296 / 0.745037172301206 | [NPY](tensors/0003695.npy) |
| 3696 | `model.layers.11.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.984375 / 5.21875 / 0.006008876694573296 / 0.745037172301206 | [NPY](tensors/0003696.npy) |
| 3697 | `model.layers.11.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.984375 / 5.21875 / 0.006008876694573296 / 0.745037172301206 | [NPY](tensors/0003697.npy) |
| 3698 | `model.layers.11.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3699 | `model.layers.11.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3700 | `model.layers.11.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3701 | `model.layers.11.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -370.0 / 344.0 / 0.22400663163926865 / 13.0653191817724 | [NPY](tensors/0003701.npy) |
| 3702 | `model.layers.11.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -370.0 / 344.0 / 0.22400663163926865 / 13.0653191817724 | [NPY](tensors/0003702.npy) |
| 3703 | `model.layers.11.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.328125 / 1.890625 / -0.19774436950683594 / 1.0932269156971681 | [NPY](tensors/0003703.npy) |
| 3704 | `model.layers.11` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -560.0 / 696.0 / 0.47342037624782984 / 27.281364148501638 | [NPY](tensors/0003704.npy) |
| 3783 | `model.layers.11` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -264.0 / 416.0 / 0.5359645419650607 / 16.643869142064773 | [NPY](tensors/0003783.npy) |
| 3784 | `model.layers.11` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 353] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003784.npy) |
| 3785 | `model.layers.11` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.09375 / 1.34375 / 0.7454833984375 / 0.8931286656122284 | [NPY](tensors/0003785.npy) |
| 3786 | `model.layers.11` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3203125 / -0.0122755765914917 / 0.6751613260908969 | [NPY](tensors/0003786.npy) |
| 3787 | `model.layers.11` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 352.0 / 352.0 / 352.0 / 0.0 | [NPY](tensors/0003787.npy) |
| 3788 | `model.layers.11` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3789 | `model.layers.11` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3790 | `model.layers.11` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3791 | `model.layers.11.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -264.0 / 416.0 / 0.5359645419650607 / 16.643869142064773 | [NPY](tensors/0003791.npy) |
| 3792 | `model.layers.11.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.0 / 117.0 / 0.08452839454015096 / 3.3618681574716516 | [NPY](tensors/0003792.npy) |
| 3793 | `model.layers.11.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.0 / 117.0 / 0.08452839454015096 / 3.3618681574716516 | [NPY](tensors/0003793.npy) |
| 3794 | `model.layers.11.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 353] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003794.npy) |
| 3795 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 352.0 / 352.0 / 352.0 / 0.0 | [NPY](tensors/0003795.npy) |
| 3796 | `model.layers.11.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3797 | `model.layers.11.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3798 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.09375 / 1.34375 / 0.7454833984375 / 0.8931286656122284 | [NPY](tensors/0003798.npy) |
| 3799 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3203125 / -0.0122755765914917 / 0.6751613260908969 | [NPY](tensors/0003799.npy) |
| 3800 | `model.layers.11.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3801 | `model.layers.11.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.0 / 117.0 / 0.08452839454015096 / 3.3618681574716516 | [NPY](tensors/0003801.npy) |
| 3802 | `model.layers.11.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.84375 / 8.3125 / 0.028497630963101983 / 1.2663216158251682 | [NPY](tensors/0003802.npy) |
| 3803 | `model.layers.11.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.0 / 117.0 / 0.08452839454015096 / 3.3618681574716516 | [NPY](tensors/0003803.npy) |
| 3804 | `model.layers.11.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.0 / 45.5 / 0.14150047302246094 / 4.2512427303365765 | [NPY](tensors/0003804.npy) |
| 3805 | `model.layers.11.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.0 / 117.0 / 0.08452839454015096 / 3.3618681574716516 | [NPY](tensors/0003805.npy) |
| 3806 | `model.layers.11.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.40625 / 6.5625 / -0.02834033966064453 / 1.9947001943652656 | [NPY](tensors/0003806.npy) |
| 3807 | `model.layers.11.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.625 / 5.75 / -0.03102114546345547 / 1.3412096060306107 | [NPY](tensors/0003807.npy) |
| 3808 | `model.layers.11.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -110.5 / 91.5 / -0.0528495709101359 / 3.9439342144199125 | [NPY](tensors/0003808.npy) |
| 3809 | `model.layers.11.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -110.5 / 91.5 / -0.0528495709101359 / 3.9439342144199125 | [NPY](tensors/0003809.npy) |
| 3810 | `model.layers.11.self_attn` | 32 | `output[1]` | [1, 64, 1, 353] | torch.bfloat16 → float32 | 7.412381819449365e-11 / 0.92578125 / 0.002620766467875464 / 0.011162029393765873 | [NPY](tensors/0003810.npy) |
| 3811 | `model.layers.11.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -172.0 / 312.0 / 0.48336749606662327 / 15.971713708345327 | [NPY](tensors/0003811.npy) |
| 3812 | `model.layers.11.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.671875 / 2.84375 / 0.009364475144280328 / 0.6905074365940603 | [NPY](tensors/0003812.npy) |
| 3813 | `model.layers.11.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.671875 / 2.84375 / 0.009364475144280328 / 0.6905074365940603 | [NPY](tensors/0003813.npy) |
| 3814 | `model.layers.11.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.671875 / 2.84375 / 0.009364475144280328 / 0.6905074365940603 | [NPY](tensors/0003814.npy) |
| 3815 | `model.layers.11.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3816 | `model.layers.11.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3817 | `model.layers.11.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3818 | `model.layers.11.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -185.0 / 152.0 / 0.0033398138152228463 / 6.3603589592133485 | [NPY](tensors/0003818.npy) |
| 3819 | `model.layers.11.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -185.0 / 152.0 / 0.0033398138152228463 / 6.3603589592133485 | [NPY](tensors/0003819.npy) |
| 3820 | `model.layers.11.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8046875 / 1.1796875 / -0.1107635498046875 / 0.6748292353687794 | [NPY](tensors/0003820.npy) |
| 3821 | `model.layers.11` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -356.0 / 458.0 / 0.4869672987196181 / 19.809135214141733 | [NPY](tensors/0003821.npy) |
| 3900 | `model.layers.11` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -392.0 / 466.0 / 0.25310372246636287 / 20.003226972676178 | [NPY](tensors/0003900.npy) |
| 3901 | `model.layers.11` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 354] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003901.npy) |
| 3902 | `model.layers.11` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.9921875 / 1.34375 / 0.763092041015625 / 0.8164851998069582 | [NPY](tensors/0003902.npy) |
| 3903 | `model.layers.11` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3203125 / -0.015299439430236816 / 0.7488356747498943 | [NPY](tensors/0003903.npy) |
| 3904 | `model.layers.11` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 353.0 / 353.0 / 353.0 / 0.0 | [NPY](tensors/0003904.npy) |
| 3905 | `model.layers.11` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3906 | `model.layers.11` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3907 | `model.layers.11` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3908 | `model.layers.11.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -392.0 / 466.0 / 0.25310372246636287 / 20.003226972676178 | [NPY](tensors/0003908.npy) |
| 3909 | `model.layers.11.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 109.0 / 0.04156473610136244 / 3.3436615029061585 | [NPY](tensors/0003909.npy) |
| 3910 | `model.layers.11.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 109.0 / 0.04156473610136244 / 3.3436615029061585 | [NPY](tensors/0003910.npy) |
| 3911 | `model.layers.11.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 354] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003911.npy) |
| 3912 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 353.0 / 353.0 / 353.0 / 0.0 | [NPY](tensors/0003912.npy) |
| 3913 | `model.layers.11.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3914 | `model.layers.11.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3915 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.9921875 / 1.34375 / 0.763092041015625 / 0.8164851998069582 | [NPY](tensors/0003915.npy) |
| 3916 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3203125 / -0.015299439430236816 / 0.7488356747498943 | [NPY](tensors/0003916.npy) |
| 3917 | `model.layers.11.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3918 | `model.layers.11.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 109.0 / 0.04156473610136244 / 3.3436615029061585 | [NPY](tensors/0003918.npy) |
| 3919 | `model.layers.11.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 9.9375 / 0.01564984762808308 / 1.2660463054782167 | [NPY](tensors/0003919.npy) |
| 3920 | `model.layers.11.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 109.0 / 0.04156473610136244 / 3.3436615029061585 | [NPY](tensors/0003920.npy) |
| 3921 | `model.layers.11.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.625 / 36.5 / -0.04873955249786377 / 3.9004653419699635 | [NPY](tensors/0003921.npy) |
| 3922 | `model.layers.11.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 109.0 / 0.04156473610136244 / 3.3436615029061585 | [NPY](tensors/0003922.npy) |
| 3923 | `model.layers.11.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.6875 / 7.84375 / 0.01109883189201355 / 2.2428755096264683 | [NPY](tensors/0003923.npy) |
| 3924 | `model.layers.11.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.375 / 6.875 / -0.006621728651225567 / 1.3680384370525331 | [NPY](tensors/0003924.npy) |
| 3925 | `model.layers.11.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 110.0 / -0.027264616224500868 / 4.152490478609747 | [NPY](tensors/0003925.npy) |
| 3926 | `model.layers.11.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 110.0 / -0.027264616224500868 / 4.152490478609747 | [NPY](tensors/0003926.npy) |
| 3927 | `model.layers.11.self_attn` | 33 | `output[1]` | [1, 64, 1, 354] | torch.bfloat16 → float32 | 3.9612757518625585e-13 / 0.9453125 / 0.002491458945443931 / 0.013816243327367375 | [NPY](tensors/0003927.npy) |
| 3928 | `model.layers.11.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -282.0 / 382.0 / 0.22635023328993056 / 19.543172252868334 | [NPY](tensors/0003928.npy) |
| 3929 | `model.layers.11.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.046875 / 3.390625 / 0.0037867042753431533 / 0.6977046266652325 | [NPY](tensors/0003929.npy) |
| 3930 | `model.layers.11.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.046875 / 3.390625 / 0.0037867042753431533 / 0.6977046266652325 | [NPY](tensors/0003930.npy) |
| 3931 | `model.layers.11.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.046875 / 3.390625 / 0.0037867042753431533 / 0.6977046266652325 | [NPY](tensors/0003931.npy) |
| 3932 | `model.layers.11.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3933 | `model.layers.11.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3934 | `model.layers.11.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3935 | `model.layers.11.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -244.0 / 214.0 / 0.15041533841027155 / 8.199263352015986 | [NPY](tensors/0003935.npy) |
| 3936 | `model.layers.11.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -244.0 / 214.0 / 0.15041533841027155 / 8.199263352015986 | [NPY](tensors/0003936.npy) |
| 3937 | `model.layers.11.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.46875 / 1.5390625 / -0.19194793701171875 / 0.9407680269948385 | [NPY](tensors/0003937.npy) |
| 3938 | `model.layers.11` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -528.0 / 596.0 / 0.37518564860026044 / 24.981151448654277 | [NPY](tensors/0003938.npy) |
| 4017 | `model.layers.11` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -227.0 / 356.0 / 0.3665179782443576 / 15.115484270263407 | [NPY](tensors/0004017.npy) |
| 4018 | `model.layers.11` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 355] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004018.npy) |
| 4019 | `model.layers.11` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2265625 / 1.34375 / 0.7769069671630859 / 0.8058280923944267 | [NPY](tensors/0004019.npy) |
| 4020 | `model.layers.11` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / -0.027683675289154053 / 0.7450244855303801 | [NPY](tensors/0004020.npy) |
| 4021 | `model.layers.11` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 354.0 / 354.0 / 354.0 / 0.0 | [NPY](tensors/0004021.npy) |
| 4022 | `model.layers.11` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4023 | `model.layers.11` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4024 | `model.layers.11` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4025 | `model.layers.11.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -227.0 / 356.0 / 0.3665179782443576 / 15.115484270263407 | [NPY](tensors/0004025.npy) |
| 4026 | `model.layers.11.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -79.0 / 110.5 / 0.06958610084321763 / 3.230249002117842 | [NPY](tensors/0004026.npy) |
| 4027 | `model.layers.11.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -79.0 / 110.5 / 0.06958610084321763 / 3.230249002117842 | [NPY](tensors/0004027.npy) |
| 4028 | `model.layers.11.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 355] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004028.npy) |
| 4029 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 354.0 / 354.0 / 354.0 / 0.0 | [NPY](tensors/0004029.npy) |
| 4030 | `model.layers.11.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4031 | `model.layers.11.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4032 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2265625 / 1.34375 / 0.7769069671630859 / 0.8058280923944267 | [NPY](tensors/0004032.npy) |
| 4033 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / -0.027683675289154053 / 0.7450244855303801 | [NPY](tensors/0004033.npy) |
| 4034 | `model.layers.11.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4035 | `model.layers.11.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -79.0 / 110.5 / 0.06958610084321763 / 3.230249002117842 | [NPY](tensors/0004035.npy) |
| 4036 | `model.layers.11.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.6875 / 9.375 / 0.009074829053133726 / 1.359782136904059 | [NPY](tensors/0004036.npy) |
| 4037 | `model.layers.11.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -79.0 / 110.5 / 0.06958610084321763 / 3.230249002117842 | [NPY](tensors/0004037.npy) |
| 4038 | `model.layers.11.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.5 / 42.5 / 0.07595506310462952 / 4.347737221824477 | [NPY](tensors/0004038.npy) |
| 4039 | `model.layers.11.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -79.0 / 110.5 / 0.06958610084321763 / 3.230249002117842 | [NPY](tensors/0004039.npy) |
| 4040 | `model.layers.11.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.75 / 9.0625 / -0.026853829622268677 / 2.2984576282232156 | [NPY](tensors/0004040.npy) |
| 4041 | `model.layers.11.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.8125 / 6.375 / -0.026526628294959664 / 1.4492668679985958 | [NPY](tensors/0004041.npy) |
| 4042 | `model.layers.11.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -76.5 / 55.0 / -0.019661797417534724 / 3.862102768829371 | [NPY](tensors/0004042.npy) |
| 4043 | `model.layers.11.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -76.5 / 55.0 / -0.019661797417534724 / 3.862102768829371 | [NPY](tensors/0004043.npy) |
| 4044 | `model.layers.11.self_attn` | 34 | `output[1]` | [1, 64, 1, 355] | torch.bfloat16 → float32 | 7.105427357601002e-12 / 0.890625 / 0.00247245309099844 / 0.01478616193763604 | [NPY](tensors/0004044.npy) |
| 4045 | `model.layers.11.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -210.0 / 280.0 / 0.3473659939236111 / 15.79364601775362 | [NPY](tensors/0004045.npy) |
| 4046 | `model.layers.11.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.625 / 3.21875 / 0.01259517404768202 / 0.7102756903781166 | [NPY](tensors/0004046.npy) |
| 4047 | `model.layers.11.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.625 / 3.21875 / 0.01259517404768202 / 0.7102756903781166 | [NPY](tensors/0004047.npy) |
| 4048 | `model.layers.11.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.625 / 3.21875 / 0.01259517404768202 / 0.7102756903781166 | [NPY](tensors/0004048.npy) |
| 4049 | `model.layers.11.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4050 | `model.layers.11.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4051 | `model.layers.11.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4052 | `model.layers.11.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -237.0 / 241.0 / 0.14922468794716728 / 8.143033766938503 | [NPY](tensors/0004052.npy) |
| 4053 | `model.layers.11.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -237.0 / 241.0 / 0.14922468794716728 / 8.143033766938503 | [NPY](tensors/0004053.npy) |
| 4054 | `model.layers.11.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.953125 / 1.0859375 / -0.17412567138671875 / 0.8050182360380749 | [NPY](tensors/0004054.npy) |
| 4055 | `model.layers.11` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -448.0 / 520.0 / 0.4952716403537326 / 21.145756405009323 | [NPY](tensors/0004055.npy) |
| 4134 | `model.layers.11` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -294.0 / 424.0 / 0.6001329210069445 / 16.708086549684054 | [NPY](tensors/0004134.npy) |
| 4135 | `model.layers.11` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 356] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004135.npy) |
| 4136 | `model.layers.11` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.80755615234375 / 0.8303206482187034 | [NPY](tensors/0004136.npy) |
| 4137 | `model.layers.11` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / -0.04510064423084259 / 0.6824180444259353 | [NPY](tensors/0004137.npy) |
| 4138 | `model.layers.11` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 355.0 / 355.0 / 355.0 / 0.0 | [NPY](tensors/0004138.npy) |
| 4139 | `model.layers.11` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4140 | `model.layers.11` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4141 | `model.layers.11` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4142 | `model.layers.11.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -294.0 / 424.0 / 0.6001329210069445 / 16.708086549684054 | [NPY](tensors/0004142.npy) |
| 4143 | `model.layers.11.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 104.5 / 0.08074160681830513 / 3.327458886478887 | [NPY](tensors/0004143.npy) |
| 4144 | `model.layers.11.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 104.5 / 0.08074160681830513 / 3.327458886478887 | [NPY](tensors/0004144.npy) |
| 4145 | `model.layers.11.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 356] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004145.npy) |
| 4146 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 355.0 / 355.0 / 355.0 / 0.0 | [NPY](tensors/0004146.npy) |
| 4147 | `model.layers.11.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4148 | `model.layers.11.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4149 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.80755615234375 / 0.8303206482187034 | [NPY](tensors/0004149.npy) |
| 4150 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / -0.04510064423084259 / 0.6824180444259353 | [NPY](tensors/0004150.npy) |
| 4151 | `model.layers.11.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4152 | `model.layers.11.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 104.5 / 0.08074160681830513 / 3.327458886478887 | [NPY](tensors/0004152.npy) |
| 4153 | `model.layers.11.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.8125 / 7.3125 / 0.06667474284768105 / 1.2052498149831412 | [NPY](tensors/0004153.npy) |
| 4154 | `model.layers.11.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 104.5 / 0.08074160681830513 / 3.327458886478887 | [NPY](tensors/0004154.npy) |
| 4155 | `model.layers.11.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.375 / 36.75 / 0.12305338308215141 / 3.826899175334925 | [NPY](tensors/0004155.npy) |
| 4156 | `model.layers.11.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 104.5 / 0.08074160681830513 / 3.327458886478887 | [NPY](tensors/0004156.npy) |
| 4157 | `model.layers.11.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.03125 / 5.78125 / 0.11883211135864258 / 2.0509901192403044 | [NPY](tensors/0004157.npy) |
| 4158 | `model.layers.11.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0 / 6.5625 / 0.028000189806334674 / 1.4094379405765953 | [NPY](tensors/0004158.npy) |
| 4159 | `model.layers.11.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.375 / 43.5 / 0.009198604689704046 / 3.6087275112090977 | [NPY](tensors/0004159.npy) |
| 4160 | `model.layers.11.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.375 / 43.5 / 0.009198604689704046 / 3.6087275112090977 | [NPY](tensors/0004160.npy) |
| 4161 | `model.layers.11.self_attn` | 35 | `output[1]` | [1, 64, 1, 356] | torch.bfloat16 → float32 | 6.639311322942376e-11 / 0.9453125 / 0.002645310409819158 / 0.014709653860666978 | [NPY](tensors/0004161.npy) |
| 4162 | `model.layers.11.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -251.0 / 418.0 / 0.6087831285264756 / 17.35392000895219 | [NPY](tensors/0004162.npy) |
| 4163 | `model.layers.11.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 2.703125 / 0.021659113301171196 / 0.6531526065773258 | [NPY](tensors/0004163.npy) |
| 4164 | `model.layers.11.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 2.703125 / 0.021659113301171196 / 0.6531526065773258 | [NPY](tensors/0004164.npy) |
| 4165 | `model.layers.11.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.8125 / 2.703125 / 0.021659113301171196 / 0.6531526065773258 | [NPY](tensors/0004165.npy) |
| 4166 | `model.layers.11.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4167 | `model.layers.11.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4168 | `model.layers.11.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4169 | `model.layers.11.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -177.0 / 140.0 / 0.07954311635759141 / 6.205873559117569 | [NPY](tensors/0004169.npy) |
| 4170 | `model.layers.11.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -177.0 / 140.0 / 0.07954311635759141 / 6.205873559117569 | [NPY](tensors/0004170.npy) |
| 4171 | `model.layers.11.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3671875 / 0.63671875 / -0.07025146484375 / 0.40017856006177893 | [NPY](tensors/0004171.npy) |
| 4172 | `model.layers.11` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -428.0 / 508.0 / 0.6887144459618463 / 21.4673698645718 | [NPY](tensors/0004172.npy) |
| 4251 | `model.layers.11` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -394.0 / 536.0 / 0.6167365180121528 / 22.047977085985035 | [NPY](tensors/0004251.npy) |
| 4252 | `model.layers.11` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 357] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004252.npy) |
| 4253 | `model.layers.11` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.85931396484375 / 0.7701579969072487 | [NPY](tensors/0004253.npy) |
| 4254 | `model.layers.11` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3203125 / -0.04313334822654724 / 0.6902819775762118 | [NPY](tensors/0004254.npy) |
| 4255 | `model.layers.11` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 356.0 / 356.0 / 356.0 / 0.0 | [NPY](tensors/0004255.npy) |
| 4256 | `model.layers.11` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4257 | `model.layers.11` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4258 | `model.layers.11` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4259 | `model.layers.11.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -394.0 / 536.0 / 0.6167365180121528 / 22.047977085985035 | [NPY](tensors/0004259.npy) |
| 4260 | `model.layers.11.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 114.0 / 0.07579240136676364 / 3.3255506030715765 | [NPY](tensors/0004260.npy) |
| 4261 | `model.layers.11.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 114.0 / 0.07579240136676364 / 3.3255506030715765 | [NPY](tensors/0004261.npy) |
| 4262 | `model.layers.11.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 357] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004262.npy) |
| 4263 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 356.0 / 356.0 / 356.0 / 0.0 | [NPY](tensors/0004263.npy) |
| 4264 | `model.layers.11.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4265 | `model.layers.11.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4266 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.85931396484375 / 0.7701579969072487 | [NPY](tensors/0004266.npy) |
| 4267 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3203125 / -0.04313334822654724 / 0.6902819775762118 | [NPY](tensors/0004267.npy) |
| 4268 | `model.layers.11.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4269 | `model.layers.11.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 114.0 / 0.07579240136676364 / 3.3255506030715765 | [NPY](tensors/0004269.npy) |
| 4270 | `model.layers.11.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.03125 / 8.4375 / 0.04180290654767305 / 1.2756345354782221 | [NPY](tensors/0004270.npy) |
| 4271 | `model.layers.11.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 114.0 / 0.07579240136676364 / 3.3255506030715765 | [NPY](tensors/0004271.npy) |
| 4272 | `model.layers.11.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.25 / 36.5 / 0.04508376121520996 / 3.804885140046374 | [NPY](tensors/0004272.npy) |
| 4273 | `model.layers.11.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 114.0 / 0.07579240136676364 / 3.3255506030715765 | [NPY](tensors/0004273.npy) |
| 4274 | `model.layers.11.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.6875 / 9.9375 / -0.029628634452819824 / 2.379660786284663 | [NPY](tensors/0004274.npy) |
| 4275 | `model.layers.11.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.46875 / 5.59375 / -0.010109563285368495 / 1.2537970205189841 | [NPY](tensors/0004275.npy) |
| 4276 | `model.layers.11.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -192.0 / 185.0 / -0.05300847821765476 / 6.023676578560925 | [NPY](tensors/0004276.npy) |
| 4277 | `model.layers.11.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -192.0 / 185.0 / -0.05300847821765476 / 6.023676578560925 | [NPY](tensors/0004277.npy) |
| 4278 | `model.layers.11.self_attn` | 36 | `output[1]` | [1, 64, 1, 357] | torch.bfloat16 → float32 | 2.0804691303055733e-11 / 0.91015625 / 0.002423672969115307 / 0.010796194768198507 | [NPY](tensors/0004278.npy) |
| 4279 | `model.layers.11.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -209.0 / 344.0 / 0.564357672797309 / 19.511873281435566 | [NPY](tensors/0004279.npy) |
| 4280 | `model.layers.11.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.84375 / 5.0 / 0.011551866928736368 / 0.722402398748117 | [NPY](tensors/0004280.npy) |
| 4281 | `model.layers.11.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.84375 / 5.0 / 0.011551866928736368 / 0.722402398748117 | [NPY](tensors/0004281.npy) |
| 4282 | `model.layers.11.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.84375 / 5.0 / 0.011551866928736368 / 0.722402398748117 | [NPY](tensors/0004282.npy) |
| 4283 | `model.layers.11.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4284 | `model.layers.11.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4285 | `model.layers.11.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4286 | `model.layers.11.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -290.0 / 262.0 / 0.30530419879489473 / 9.534793687145328 | [NPY](tensors/0004286.npy) |
| 4287 | `model.layers.11.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -290.0 / 262.0 / 0.30530419879489473 / 9.534793687145328 | [NPY](tensors/0004287.npy) |
| 4288 | `model.layers.11.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.328125 / 1.8046875 / -0.18613052368164062 / 0.9629410904270219 | [NPY](tensors/0004288.npy) |
| 4289 | `model.layers.11` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -500.0 / 608.0 / 0.8697723388671875 / 25.806274296799703 | [NPY](tensors/0004289.npy) |
| 4368 | `model.layers.11` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -404.0 / 478.0 / 0.6146103752983941 / 20.065278972426526 | [NPY](tensors/0004368.npy) |
| 4369 | `model.layers.11` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 358] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004369.npy) |
| 4370 | `model.layers.11` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.9085693359375 / 0.6912552727986224 | [NPY](tensors/0004370.npy) |
| 4371 | `model.layers.11` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.3203125 / -0.004209965467453003 / 0.711058024090348 | [NPY](tensors/0004371.npy) |
| 4372 | `model.layers.11` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 357.0 / 357.0 / 357.0 / 0.0 | [NPY](tensors/0004372.npy) |
| 4373 | `model.layers.11` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4374 | `model.layers.11` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4375 | `model.layers.11` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4376 | `model.layers.11.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -404.0 / 478.0 / 0.6146103752983941 / 20.065278972426526 | [NPY](tensors/0004376.npy) |
| 4377 | `model.layers.11.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.5 / 111.5 / 0.0768938660621643 / 3.4882220307977976 | [NPY](tensors/0004377.npy) |
| 4378 | `model.layers.11.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.5 / 111.5 / 0.0768938660621643 / 3.4882220307977976 | [NPY](tensors/0004378.npy) |
| 4379 | `model.layers.11.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 358] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004379.npy) |
| 4380 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 357.0 / 357.0 / 357.0 / 0.0 | [NPY](tensors/0004380.npy) |
| 4381 | `model.layers.11.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4382 | `model.layers.11.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4383 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.9085693359375 / 0.6912552727986224 | [NPY](tensors/0004383.npy) |
| 4384 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.3203125 / -0.004209965467453003 / 0.711058024090348 | [NPY](tensors/0004384.npy) |
| 4385 | `model.layers.11.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4386 | `model.layers.11.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.5 / 111.5 / 0.0768938660621643 / 3.4882220307977976 | [NPY](tensors/0004386.npy) |
| 4387 | `model.layers.11.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.65625 / 6.59375 / 0.02168801403604448 / 1.1654122800418203 | [NPY](tensors/0004387.npy) |
| 4388 | `model.layers.11.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.5 / 111.5 / 0.0768938660621643 / 3.4882220307977976 | [NPY](tensors/0004388.npy) |
| 4389 | `model.layers.11.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.5 / 37.75 / 0.07957959175109863 / 3.6112857706962713 | [NPY](tensors/0004389.npy) |
| 4390 | `model.layers.11.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.5 / 111.5 / 0.0768938660621643 / 3.4882220307977976 | [NPY](tensors/0004390.npy) |
| 4391 | `model.layers.11.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.9375 / 5.75 / 0.031861208379268646 / 1.771756230237349 | [NPY](tensors/0004391.npy) |
| 4392 | `model.layers.11.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.875 / 5.4375 / -0.015391291584819555 / 1.2423265234906262 | [NPY](tensors/0004392.npy) |
| 4393 | `model.layers.11.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -162.0 / 155.0 / -0.035949055353800455 / 5.31866284406107 | [NPY](tensors/0004393.npy) |
| 4394 | `model.layers.11.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -162.0 / 155.0 / -0.035949055353800455 / 5.31866284406107 | [NPY](tensors/0004394.npy) |
| 4395 | `model.layers.11.self_attn` | 37 | `output[1]` | [1, 64, 1, 358] | torch.bfloat16 → float32 | 5.206857167650014e-11 / 0.94921875 / 0.0025655268207410713 / 0.01041831548435353 | [NPY](tensors/0004395.npy) |
| 4396 | `model.layers.11.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -249.0 / 364.0 / 0.5789601643880208 / 18.159209009412212 | [NPY](tensors/0004396.npy) |
| 4397 | `model.layers.11.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.265625 / 4.3125 / 0.01774337821536594 / 0.6876622150733376 | [NPY](tensors/0004397.npy) |
| 4398 | `model.layers.11.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.265625 / 4.3125 / 0.01774337821536594 / 0.6876622150733376 | [NPY](tensors/0004398.npy) |
| 4399 | `model.layers.11.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.265625 / 4.3125 / 0.01774337821536594 / 0.6876622150733376 | [NPY](tensors/0004399.npy) |
| 4400 | `model.layers.11.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4401 | `model.layers.11.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4402 | `model.layers.11.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4403 | `model.layers.11.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -235.0 / 154.0 / 0.10915546947055393 / 7.504204032750219 | [NPY](tensors/0004403.npy) |
| 4404 | `model.layers.11.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -235.0 / 154.0 / 0.10915546947055393 / 7.504204032750219 | [NPY](tensors/0004404.npy) |
| 4405 | `model.layers.11.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.0 / 1.515625 / -0.13048553466796875 / 0.7618500595971973 | [NPY](tensors/0004405.npy) |
| 4406 | `model.layers.11` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -484.0 / 470.0 / 0.6885409884982638 / 22.93149688526245 | [NPY](tensors/0004406.npy) |
| 4485 | `model.layers.11` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -476.0 / 584.0 / 0.5698250664605035 / 23.134404390302464 | [NPY](tensors/0004485.npy) |
| 4486 | `model.layers.11` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 359] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004486.npy) |
| 4487 | `model.layers.11` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0234375 / 1.34375 / 0.9233245849609375 / 0.6835210214822701 | [NPY](tensors/0004487.npy) |
| 4488 | `model.layers.11` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.060156017541885376 / 0.6978118882257907 | [NPY](tensors/0004488.npy) |
| 4489 | `model.layers.11` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 358.0 / 358.0 / 358.0 / 0.0 | [NPY](tensors/0004489.npy) |
| 4490 | `model.layers.11` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4491 | `model.layers.11` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4492 | `model.layers.11` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4493 | `model.layers.11.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -476.0 / 584.0 / 0.5698250664605035 / 23.134404390302464 | [NPY](tensors/0004493.npy) |
| 4494 | `model.layers.11.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.0 / 118.5 / 0.06231247468127145 / 3.502796177464613 | [NPY](tensors/0004494.npy) |
| 4495 | `model.layers.11.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.0 / 118.5 / 0.06231247468127145 / 3.502796177464613 | [NPY](tensors/0004495.npy) |
| 4496 | `model.layers.11.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 359] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004496.npy) |
| 4497 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 358.0 / 358.0 / 358.0 / 0.0 | [NPY](tensors/0004497.npy) |
| 4498 | `model.layers.11.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4499 | `model.layers.11.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4500 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0234375 / 1.34375 / 0.9233245849609375 / 0.6835210214822701 | [NPY](tensors/0004500.npy) |
| 4501 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.060156017541885376 / 0.6978118882257907 | [NPY](tensors/0004501.npy) |
| 4502 | `model.layers.11.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4503 | `model.layers.11.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.0 / 118.5 / 0.06231247468127145 / 3.502796177464613 | [NPY](tensors/0004503.npy) |
| 4504 | `model.layers.11.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.28125 / 7.21875 / 0.032520203618332744 / 1.1437361915244408 | [NPY](tensors/0004504.npy) |
| 4505 | `model.layers.11.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.0 / 118.5 / 0.06231247468127145 / 3.502796177464613 | [NPY](tensors/0004505.npy) |
| 4506 | `model.layers.11.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.25 / 43.75 / 0.0005198121070861816 / 3.933457470581829 | [NPY](tensors/0004506.npy) |
| 4507 | `model.layers.11.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.0 / 118.5 / 0.06231247468127145 / 3.502796177464613 | [NPY](tensors/0004507.npy) |
| 4508 | `model.layers.11.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.78125 / 6.875 / -0.08479005098342896 / 2.1971100733946023 | [NPY](tensors/0004508.npy) |
| 4509 | `model.layers.11.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5625 / 6.375 / 0.00023569096811115742 / 1.2957150154588686 | [NPY](tensors/0004509.npy) |
| 4510 | `model.layers.11.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -180.0 / 156.0 / 0.022171067943175634 / 5.7809091996385815 | [NPY](tensors/0004510.npy) |
| 4511 | `model.layers.11.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -180.0 / 156.0 / 0.022171067943175634 / 5.7809091996385815 | [NPY](tensors/0004511.npy) |
| 4512 | `model.layers.11.self_attn` | 38 | `output[1]` | [1, 64, 1, 359] | torch.bfloat16 → float32 | 2.1760371282653068e-13 / 0.96875 / 0.0024972773540928436 / 0.015296004641666241 | [NPY](tensors/0004512.npy) |
| 4513 | `model.layers.11.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -320.0 / 404.0 / 0.5921585083007812 / 21.07733663805607 | [NPY](tensors/0004513.npy) |
| 4514 | `model.layers.11.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.90625 / 4.21875 / 0.019597776730855308 / 0.7332048489832613 | [NPY](tensors/0004514.npy) |
| 4515 | `model.layers.11.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.90625 / 4.21875 / 0.019597776730855308 / 0.7332048489832613 | [NPY](tensors/0004515.npy) |
| 4516 | `model.layers.11.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.90625 / 4.21875 / 0.019597776730855308 / 0.7332048489832613 | [NPY](tensors/0004516.npy) |
| 4517 | `model.layers.11.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4518 | `model.layers.11.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4519 | `model.layers.11.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4520 | `model.layers.11.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -256.0 / 207.0 / 0.031073083480199177 / 8.497370775434772 | [NPY](tensors/0004520.npy) |
| 4521 | `model.layers.11.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -256.0 / 207.0 / 0.031073083480199177 / 8.497370775434772 | [NPY](tensors/0004521.npy) |
| 4522 | `model.layers.11.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.609375 / 1.40625 / -0.14312362670898438 / 0.8945743459750232 | [NPY](tensors/0004522.npy) |
| 4523 | `model.layers.11` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -576.0 / 612.0 / 0.6238064236111112 / 26.63009306250391 | [NPY](tensors/0004523.npy) |
| 4602 | `model.layers.11` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -452.0 / 544.0 / 0.3319639417860243 / 20.95198539942541 | [NPY](tensors/0004602.npy) |
| 4603 | `model.layers.11` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 360] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004603.npy) |
| 4604 | `model.layers.11` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.8929443359375 / 0.7026515532326651 | [NPY](tensors/0004604.npy) |
| 4605 | `model.layers.11` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3203125 / 0.11357763409614563 / 0.7110437810662014 | [NPY](tensors/0004605.npy) |
| 4606 | `model.layers.11` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 359.0 / 359.0 / 359.0 / 0.0 | [NPY](tensors/0004606.npy) |
| 4607 | `model.layers.11` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4608 | `model.layers.11` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4609 | `model.layers.11` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4610 | `model.layers.11.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -452.0 / 544.0 / 0.3319639417860243 / 20.95198539942541 | [NPY](tensors/0004610.npy) |
| 4611 | `model.layers.11.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -113.0 / 121.5 / 0.054689481523301865 / 3.601830112276354 | [NPY](tensors/0004611.npy) |
| 4612 | `model.layers.11.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -113.0 / 121.5 / 0.054689481523301865 / 3.601830112276354 | [NPY](tensors/0004612.npy) |
| 4613 | `model.layers.11.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 360] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004613.npy) |
| 4614 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 359.0 / 359.0 / 359.0 / 0.0 | [NPY](tensors/0004614.npy) |
| 4615 | `model.layers.11.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4616 | `model.layers.11.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4617 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.8929443359375 / 0.7026515532326651 | [NPY](tensors/0004617.npy) |
| 4618 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3203125 / 0.11357763409614563 / 0.7110437810662014 | [NPY](tensors/0004618.npy) |
| 4619 | `model.layers.11.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4620 | `model.layers.11.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -113.0 / 121.5 / 0.054689481523301865 / 3.601830112276354 | [NPY](tensors/0004620.npy) |
| 4621 | `model.layers.11.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5 / 6.71875 / 0.037084372946992517 / 1.1335270455802635 | [NPY](tensors/0004621.npy) |
| 4622 | `model.layers.11.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -113.0 / 121.5 / 0.054689481523301865 / 3.601830112276354 | [NPY](tensors/0004622.npy) |
| 4623 | `model.layers.11.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.25 / 40.5 / 0.02867383323609829 / 3.860485851196034 | [NPY](tensors/0004623.npy) |
| 4624 | `model.layers.11.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -113.0 / 121.5 / 0.054689481523301865 / 3.601830112276354 | [NPY](tensors/0004624.npy) |
| 4625 | `model.layers.11.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.5625 / 6.15625 / -0.06199240684509277 / 1.880624444029812 | [NPY](tensors/0004625.npy) |
| 4626 | `model.layers.11.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.625 / 6.34375 / -0.015001320280134678 / 1.2714001745217742 | [NPY](tensors/0004626.npy) |
| 4627 | `model.layers.11.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -145.0 / 143.0 / 0.06805685891045464 / 5.285074337606384 | [NPY](tensors/0004627.npy) |
| 4628 | `model.layers.11.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -145.0 / 143.0 / 0.06805685891045464 / 5.285074337606384 | [NPY](tensors/0004628.npy) |
| 4629 | `model.layers.11.self_attn` | 39 | `output[1]` | [1, 64, 1, 360] | torch.bfloat16 → float32 | 2.5437429940211587e-12 / 0.9296875 / 0.0024791659924350076 / 0.015675657973709158 | [NPY](tensors/0004629.npy) |
| 4630 | `model.layers.11.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -308.0 / 400.0 / 0.4008265177408854 / 19.38219218929506 | [NPY](tensors/0004630.npy) |
| 4631 | `model.layers.11.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.1875 / 3.671875 / 0.013316529326968723 / 0.7335262267562414 | [NPY](tensors/0004631.npy) |
| 4632 | `model.layers.11.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.1875 / 3.671875 / 0.013316529326968723 / 0.7335262267562414 | [NPY](tensors/0004632.npy) |
| 4633 | `model.layers.11.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.1875 / 3.671875 / 0.013316529326968723 / 0.7335262267562414 | [NPY](tensors/0004633.npy) |
| 4634 | `model.layers.11.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4635 | `model.layers.11.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4636 | `model.layers.11.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4637 | `model.layers.11.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -276.0 / 193.0 / -0.0001792397763994005 / 8.521370900932366 | [NPY](tensors/0004637.npy) |
| 4638 | `model.layers.11.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -276.0 / 193.0 / -0.0001792397763994005 / 8.521370900932366 | [NPY](tensors/0004638.npy) |
| 4639 | `model.layers.11.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.21875 / 1.2265625 / -0.13660240173339844 / 0.7205846634882804 | [NPY](tensors/0004639.npy) |
| 4640 | `model.layers.11` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -584.0 / 592.0 / 0.40113355848524307 / 25.04206279380874 | [NPY](tensors/0004640.npy) |
| 4719 | `model.layers.11` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -560.0 / 604.0 / 0.7314791361490885 / 25.13999802568866 | [NPY](tensors/0004719.npy) |
| 4720 | `model.layers.11` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 361] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004720.npy) |
| 4721 | `model.layers.11` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.8425521850585938 / 0.7592463038913561 | [NPY](tensors/0004721.npy) |
| 4722 | `model.layers.11` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.328125 / 0.12352868914604187 / 0.7124125188030568 | [NPY](tensors/0004722.npy) |
| 4723 | `model.layers.11` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 360.0 / 360.0 / 360.0 / 0.0 | [NPY](tensors/0004723.npy) |
| 4724 | `model.layers.11` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4725 | `model.layers.11` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4726 | `model.layers.11` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4727 | `model.layers.11.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -560.0 / 604.0 / 0.7314791361490885 / 25.13999802568866 | [NPY](tensors/0004727.npy) |
| 4728 | `model.layers.11.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 112.5 / 0.06815722154246437 / 3.4965409614872476 | [NPY](tensors/0004728.npy) |
| 4729 | `model.layers.11.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 112.5 / 0.06815722154246437 / 3.4965409614872476 | [NPY](tensors/0004729.npy) |
| 4730 | `model.layers.11.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 361] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004730.npy) |
| 4731 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 360.0 / 360.0 / 360.0 / 0.0 | [NPY](tensors/0004731.npy) |
| 4732 | `model.layers.11.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4733 | `model.layers.11.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4734 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.8425521850585938 / 0.7592463038913561 | [NPY](tensors/0004734.npy) |
| 4735 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.328125 / 0.12352868914604187 / 0.7124125188030568 | [NPY](tensors/0004735.npy) |
| 4736 | `model.layers.11.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4737 | `model.layers.11.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 112.5 / 0.06815722154246437 / 3.4965409614872476 | [NPY](tensors/0004737.npy) |
| 4738 | `model.layers.11.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.625 / 8.0 / 0.049224521266296506 / 1.2175948662636147 | [NPY](tensors/0004738.npy) |
| 4739 | `model.layers.11.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 112.5 / 0.06815722154246437 / 3.4965409614872476 | [NPY](tensors/0004739.npy) |
| 4740 | `model.layers.11.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.25 / 38.0 / 0.15354205667972565 / 3.9285245446023334 | [NPY](tensors/0004740.npy) |
| 4741 | `model.layers.11.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 112.5 / 0.06815722154246437 / 3.4965409614872476 | [NPY](tensors/0004741.npy) |
| 4742 | `model.layers.11.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.65625 / 8.375 / 0.09151962399482727 / 2.550643253377088 | [NPY](tensors/0004742.npy) |
| 4743 | `model.layers.11.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 6.25 / -0.007582780905067921 / 1.3299016421122738 | [NPY](tensors/0004743.npy) |
| 4744 | `model.layers.11.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -182.0 / 228.0 / -0.06490223275290595 / 6.646641784511485 | [NPY](tensors/0004744.npy) |
| 4745 | `model.layers.11.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -182.0 / 228.0 / -0.06490223275290595 / 6.646641784511485 | [NPY](tensors/0004745.npy) |
| 4746 | `model.layers.11.self_attn` | 40 | `output[1]` | [1, 64, 1, 361] | torch.bfloat16 → float32 | 1.2836953722228372e-15 / 0.9609375 / 0.002410846332210603 / 0.018370027051787363 | [NPY](tensors/0004746.npy) |
| 4747 | `model.layers.11.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -332.0 / 422.0 / 0.6675501505533854 / 22.543015804825092 | [NPY](tensors/0004747.npy) |
| 4748 | `model.layers.11.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.078125 / 3.734375 / 0.018000136646959517 / 0.7895121170610649 | [NPY](tensors/0004748.npy) |
| 4749 | `model.layers.11.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.078125 / 3.734375 / 0.018000136646959517 / 0.7895121170610649 | [NPY](tensors/0004749.npy) |
| 4750 | `model.layers.11.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.078125 / 3.734375 / 0.018000136646959517 / 0.7895121170610649 | [NPY](tensors/0004750.npy) |
| 4751 | `model.layers.11.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4752 | `model.layers.11.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4753 | `model.layers.11.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4754 | `model.layers.11.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -328.0 / 282.0 / 0.07403584586249458 / 10.942276730298195 | [NPY](tensors/0004754.npy) |
| 4755 | `model.layers.11.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -328.0 / 282.0 / 0.07403584586249458 / 10.942276730298195 | [NPY](tensors/0004755.npy) |
| 4756 | `model.layers.11.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.5 / 1.3515625 / -0.14377307891845703 / 0.8381094254065949 | [NPY](tensors/0004756.npy) |
| 4757 | `model.layers.11` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -660.0 / 704.0 / 0.7427571614583334 / 29.43294140932182 | [NPY](tensors/0004757.npy) |
| 4836 | `model.layers.11` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -328.0 / 472.0 / 0.9074164496527778 / 19.647143532059985 | [NPY](tensors/0004836.npy) |
| 4837 | `model.layers.11` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 362] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004837.npy) |
| 4838 | `model.layers.11` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.8165130615234375 / 0.8162570957147703 | [NPY](tensors/0004838.npy) |
| 4839 | `model.layers.11` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.09044128656387329 / 0.6843655856400834 | [NPY](tensors/0004839.npy) |
| 4840 | `model.layers.11` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 361.0 / 361.0 / 361.0 / 0.0 | [NPY](tensors/0004840.npy) |
| 4841 | `model.layers.11` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4842 | `model.layers.11` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4843 | `model.layers.11` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4844 | `model.layers.11.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -328.0 / 472.0 / 0.9074164496527778 / 19.647143532059985 | [NPY](tensors/0004844.npy) |
| 4845 | `model.layers.11.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 112.5 / 0.10913037723965115 / 3.3464348418976004 | [NPY](tensors/0004845.npy) |
| 4846 | `model.layers.11.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 112.5 / 0.10913037723965115 / 3.3464348418976004 | [NPY](tensors/0004846.npy) |
| 4847 | `model.layers.11.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 362] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004847.npy) |
| 4848 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 361.0 / 361.0 / 361.0 / 0.0 | [NPY](tensors/0004848.npy) |
| 4849 | `model.layers.11.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4850 | `model.layers.11.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4851 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.8165130615234375 / 0.8162570957147703 | [NPY](tensors/0004851.npy) |
| 4852 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.09044128656387329 / 0.6843655856400834 | [NPY](tensors/0004852.npy) |
| 4853 | `model.layers.11.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4854 | `model.layers.11.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 112.5 / 0.10913037723965115 / 3.3464348418976004 | [NPY](tensors/0004854.npy) |
| 4855 | `model.layers.11.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 7.375 / 0.0585437323898077 / 1.2146734988310246 | [NPY](tensors/0004855.npy) |
| 4856 | `model.layers.11.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 112.5 / 0.10913037723965115 / 3.3464348418976004 | [NPY](tensors/0004856.npy) |
| 4857 | `model.layers.11.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.0 / 35.75 / 0.11664905399084091 / 3.9401955379059053 | [NPY](tensors/0004857.npy) |
| 4858 | `model.layers.11.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 112.5 / 0.10913037723965115 / 3.3464348418976004 | [NPY](tensors/0004858.npy) |
| 4859 | `model.layers.11.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.0625 / 8.0625 / -0.007724776864051819 / 2.4092229044624043 | [NPY](tensors/0004859.npy) |
| 4860 | `model.layers.11.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.40625 / 7.625 / -0.0011162473820149899 / 1.3298426446103735 | [NPY](tensors/0004860.npy) |
| 4861 | `model.layers.11.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -104.5 / 106.0 / 0.014039883348676894 / 4.539465994421369 | [NPY](tensors/0004861.npy) |
| 4862 | `model.layers.11.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -104.5 / 106.0 / 0.014039883348676894 / 4.539465994421369 | [NPY](tensors/0004862.npy) |
| 4863 | `model.layers.11.self_attn` | 41 | `output[1]` | [1, 64, 1, 362] | torch.bfloat16 → float32 | 3.979039320256561e-13 / 0.94921875 / 0.00258792306480625 / 0.013263586160052231 | [NPY](tensors/0004863.npy) |
| 4864 | `model.layers.11.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -222.0 / 410.0 / 0.9213416205512153 / 19.11601548342902 | [NPY](tensors/0004864.npy) |
| 4865 | `model.layers.11.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.578125 / 3.65625 / 0.03770307699839274 / 0.7332281833982864 | [NPY](tensors/0004865.npy) |
| 4866 | `model.layers.11.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.578125 / 3.65625 / 0.03770307699839274 / 0.7332281833982864 | [NPY](tensors/0004866.npy) |
| 4867 | `model.layers.11.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.578125 / 3.65625 / 0.03770307699839274 / 0.7332281833982864 | [NPY](tensors/0004867.npy) |
| 4868 | `model.layers.11.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4869 | `model.layers.11.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4870 | `model.layers.11.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4871 | `model.layers.11.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -199.0 / 218.0 / -0.009986137019263373 / 8.53323888968174 | [NPY](tensors/0004871.npy) |
| 4872 | `model.layers.11.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -199.0 / 218.0 / -0.009986137019263373 / 8.53323888968174 | [NPY](tensors/0004872.npy) |
| 4873 | `model.layers.11.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.7421875 / 1.078125 / -0.08351516723632812 / 0.5697903350174717 | [NPY](tensors/0004873.npy) |
| 4874 | `model.layers.11` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -420.0 / 584.0 / 0.9118489583333333 / 24.618081994215725 | [NPY](tensors/0004874.npy) |
| 4953 | `model.layers.11` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -256.0 / 408.0 / 0.6601902431911892 / 18.438255281135167 | [NPY](tensors/0004953.npy) |
| 4954 | `model.layers.11` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 363] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004954.npy) |
| 4955 | `model.layers.11` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.046875 / 1.34375 / 0.8409137725830078 / 0.7828598309066966 | [NPY](tensors/0004955.npy) |
| 4956 | `model.layers.11` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.05170133709907532 / 0.6983318090469743 | [NPY](tensors/0004956.npy) |
| 4957 | `model.layers.11` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 362.0 / 362.0 / 362.0 / 0.0 | [NPY](tensors/0004957.npy) |
| 4958 | `model.layers.11` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4959 | `model.layers.11` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4960 | `model.layers.11` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4961 | `model.layers.11.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -256.0 / 408.0 / 0.6601902431911892 / 18.438255281135167 | [NPY](tensors/0004961.npy) |
| 4962 | `model.layers.11.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 103.5 / 0.09626813199785021 / 3.098529666549039 | [NPY](tensors/0004962.npy) |
| 4963 | `model.layers.11.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 103.5 / 0.09626813199785021 / 3.098529666549039 | [NPY](tensors/0004963.npy) |
| 4964 | `model.layers.11.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 363] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004964.npy) |
| 4965 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 362.0 / 362.0 / 362.0 / 0.0 | [NPY](tensors/0004965.npy) |
| 4966 | `model.layers.11.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4967 | `model.layers.11.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4968 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.046875 / 1.34375 / 0.8409137725830078 / 0.7828598309066966 | [NPY](tensors/0004968.npy) |
| 4969 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.05170133709907532 / 0.6983318090469743 | [NPY](tensors/0004969.npy) |
| 4970 | `model.layers.11.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4971 | `model.layers.11.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 103.5 / 0.09626813199785021 / 3.098529666549039 | [NPY](tensors/0004971.npy) |
| 4972 | `model.layers.11.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.75 / 8.6875 / 0.03720608726143837 / 1.3476264596494674 | [NPY](tensors/0004972.npy) |
| 4973 | `model.layers.11.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 103.5 / 0.09626813199785021 / 3.098529666549039 | [NPY](tensors/0004973.npy) |
| 4974 | `model.layers.11.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.875 / 40.25 / 0.10903036594390869 / 4.175704847202968 | [NPY](tensors/0004974.npy) |
| 4975 | `model.layers.11.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 103.5 / 0.09626813199785021 / 3.098529666549039 | [NPY](tensors/0004975.npy) |
| 4976 | `model.layers.11.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.25 / 11.0625 / 0.030684873461723328 / 2.5492092496536407 | [NPY](tensors/0004976.npy) |
| 4977 | `model.layers.11.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 6.03125 / -0.015283448999980465 / 1.441848026203781 | [NPY](tensors/0004977.npy) |
| 4978 | `model.layers.11.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.5 / 122.5 / -0.020641949441697862 / 4.370117504689474 | [NPY](tensors/0004978.npy) |
| 4979 | `model.layers.11.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.5 / 122.5 / -0.020641949441697862 / 4.370117504689474 | [NPY](tensors/0004979.npy) |
| 4980 | `model.layers.11.self_attn` | 42 | `output[1]` | [1, 64, 1, 363] | torch.bfloat16 → float32 | 5.7980287238024175e-11 / 0.9296875 / 0.0025455407616177934 / 0.012701896776439051 | [NPY](tensors/0004980.npy) |
| 4981 | `model.layers.11.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -169.0 / 306.0 / 0.639684549967448 / 18.153872076882237 | [NPY](tensors/0004981.npy) |
| 4982 | `model.layers.11.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.96875 / 3.0625 / 0.02389694849650065 / 0.7461693648865724 | [NPY](tensors/0004982.npy) |
| 4983 | `model.layers.11.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.96875 / 3.0625 / 0.02389694849650065 / 0.7461693648865724 | [NPY](tensors/0004983.npy) |
| 4984 | `model.layers.11.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.96875 / 3.0625 / 0.02389694849650065 / 0.7461693648865724 | [NPY](tensors/0004984.npy) |
| 4985 | `model.layers.11.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4986 | `model.layers.11.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4987 | `model.layers.11.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4988 | `model.layers.11.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -223.0 / 225.0 / 0.07830369803640577 / 8.344900592618112 | [NPY](tensors/0004988.npy) |
| 4989 | `model.layers.11.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -223.0 / 225.0 / 0.07830369803640577 / 8.344900592618112 | [NPY](tensors/0004989.npy) |
| 4990 | `model.layers.11.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.09375 / 1.0625 / -0.12255382537841797 / 0.6872017347910668 | [NPY](tensors/0004990.npy) |
| 4991 | `model.layers.11` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -356.0 / 532.0 / 0.7177308824327256 / 23.370417770043723 | [NPY](tensors/0004991.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -2.368123964736849 / 408.59429495958534 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 321, 321] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6894860507172763e+38 / 1.6947574708614093e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 321, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7882230712617297 / 0.8876106672141242 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 321, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.1173851026170974 / 0.6217412290332741 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 321] | torch.int64 → int64 | 0.0 / 320.0 / 160.0 / 92.66426855410162 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -2.368123964736849 / 408.59429495958534 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 321, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.006824704367949831 / 1.7512628427739052 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 321, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.006824704367949831 / 1.7512628427739052 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 321, 321] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6894860507172763e+38 / 1.6947574708614093e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 321] | torch.int64 → int64 | 0.0 / 320.0 / 160.0 / 92.66426855410162 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 321, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7882230712617297 / 0.8876106672141242 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 321, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.1173851026170974 / 0.6217412290332741 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.006824704367949831 / 1.7512628427739052 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 321, 4096] | torch.bfloat16 → float32 | -19.0 / 24.25 / 0.028656292075589652 / 1.6658098275665216 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.006824704367949831 / 1.7512628427739052 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 321, 512] | torch.bfloat16 → float32 | -82.0 / 59.0 / -0.08784475300542291 / 5.049200854749734 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.006824704367949831 / 1.7512628427739052 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 321, 512] | torch.bfloat16 → float32 | -27.25 / 24.25 / 0.026860563647338534 / 3.2131446528773155 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 321, 4096] | torch.bfloat16 → float32 | -25.625 / 12.9375 / 0.003755584291949981 / 1.151192221507995 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 321, 2880] | torch.bfloat16 → float32 | -6656.0 / 6880.0 / 2.473295246453053 / 163.104061090178 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -6656.0 / 6880.0 / 2.473295246453053 / 163.104061090178 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 321, 321] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0015606369175691047 / 0.011644410847680654 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -10496.0 / 11264.0 / 0.10475843204433585 / 358.4300581992605 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 321, 2880] | torch.bfloat16 → float32 | -46.75 / 26.75 / -0.018184728677007062 / 1.2603643104904454 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -46.75 / 26.75 / -0.018184728677007062 / 1.2603643104904454 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [321, 2880] | torch.bfloat16 → float32 | -46.75 / 26.75 / -0.018184728677007062 / 1.2603643104904454 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [321, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.7661476833756797 / 148.23173991768323 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 321, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.7661476833756797 / 148.23173991768323 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [321, 32] | torch.bfloat16 → float32 | -7.84375 / 4.625 / 0.2465937858058656 / 2.6420576053758316 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 321, 2880] | torch.bfloat16 → float32 | -10752.0 / 10944.0 / -1.66168034792194 / 393.87290975941886 | [NPY](tensors/0000116.npy) |
| 195 | `model.layers.23` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 10048.0 / -2.1124565972222222 / 439.75497207649795 | [NPY](tensors/0000195.npy) |
| 196 | `model.layers.23` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000196.npy) |
| 197 | `model.layers.23` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0000197.npy) |
| 198 | `model.layers.23` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0000198.npy) |
| 199 | `model.layers.23` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0000199.npy) |
| 200 | `model.layers.23` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 201 | `model.layers.23` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 202 | `model.layers.23` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 203 | `model.layers.23.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 10048.0 / -2.1124565972222222 / 439.75497207649795 | [NPY](tensors/0000203.npy) |
| 204 | `model.layers.23.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 61.5 / 0.005684920152028402 / 1.790250296503596 | [NPY](tensors/0000204.npy) |
| 205 | `model.layers.23.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 61.5 / 0.005684920152028402 / 1.790250296503596 | [NPY](tensors/0000205.npy) |
| 206 | `model.layers.23.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000206.npy) |
| 207 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0000207.npy) |
| 208 | `model.layers.23.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 209 | `model.layers.23.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 210 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0000210.npy) |
| 211 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0000211.npy) |
| 212 | `model.layers.23.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 213 | `model.layers.23.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 61.5 / 0.005684920152028402 / 1.790250296503596 | [NPY](tensors/0000213.npy) |
| 214 | `model.layers.23.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.375 / 18.5 / 0.03419799916446209 / 1.40301921428332 | [NPY](tensors/0000214.npy) |
| 215 | `model.layers.23.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 61.5 / 0.005684920152028402 / 1.790250296503596 | [NPY](tensors/0000215.npy) |
| 216 | `model.layers.23.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.5 / 40.75 / -0.20857228804379702 / 5.184263418658333 | [NPY](tensors/0000216.npy) |
| 217 | `model.layers.23.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 61.5 / 0.005684920152028402 / 1.790250296503596 | [NPY](tensors/0000217.npy) |
| 218 | `model.layers.23.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.625 / 9.3125 / -0.03755831718444824 / 2.493353622837025 | [NPY](tensors/0000218.npy) |
| 219 | `model.layers.23.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.625 / 5.71875 / -0.00968107257176598 / 0.955293700294944 | [NPY](tensors/0000219.npy) |
| 220 | `model.layers.23.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5312.0 / 5600.0 / 5.396758376227485 / 236.64284473835622 | [NPY](tensors/0000220.npy) |
| 221 | `model.layers.23.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5312.0 / 5600.0 / 5.396758376227485 / 236.64284473835622 | [NPY](tensors/0000221.npy) |
| 222 | `model.layers.23.self_attn` | 1 | `output[1]` | [1, 64, 1, 322] | torch.bfloat16 → float32 | 1.7053025658242404e-13 / 0.86328125 / 0.0017511356364803552 / 0.011178164386227606 | [NPY](tensors/0000222.npy) |
| 223 | `model.layers.23.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9856.0 / 10176.0 / 3.2856987847222223 / 522.9698233156281 | [NPY](tensors/0000223.npy) |
| 224 | `model.layers.23.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.875 / 7.96875 / -0.01339853670861986 / 0.9445594862567097 | [NPY](tensors/0000224.npy) |
| 225 | `model.layers.23.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.875 / 7.96875 / -0.01339853670861986 / 0.9445594862567097 | [NPY](tensors/0000225.npy) |
| 226 | `model.layers.23.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -30.875 / 7.96875 / -0.01339853670861986 / 0.9445594862567097 | [NPY](tensors/0000226.npy) |
| 227 | `model.layers.23.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 228 | `model.layers.23.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 229 | `model.layers.23.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 230 | `model.layers.23.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1040.0 / 796.0 / -1.642236434088813 / 66.4614191642403 | [NPY](tensors/0000230.npy) |
| 231 | `model.layers.23.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1040.0 / 796.0 / -1.642236434088813 / 66.4614191642403 | [NPY](tensors/0000231.npy) |
| 232 | `model.layers.23.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.6484375 / 1.1484375 / 0.08960723876953125 / 0.3348101367334242 | [NPY](tensors/0000232.npy) |
| 233 | `model.layers.23` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9280.0 / 9600.0 / 1.641427951388889 / 489.8997124363708 | [NPY](tensors/0000233.npy) |
| 312 | `model.layers.23` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9600.0 / -1.8402913411458333 / 444.5628010379403 | [NPY](tensors/0000312.npy) |
| 313 | `model.layers.23` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000313.npy) |
| 314 | `model.layers.23` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0000314.npy) |
| 315 | `model.layers.23` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0000315.npy) |
| 316 | `model.layers.23` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0000316.npy) |
| 317 | `model.layers.23` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 318 | `model.layers.23` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 319 | `model.layers.23` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 320 | `model.layers.23.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9600.0 / -1.8402913411458333 / 444.5628010379403 | [NPY](tensors/0000320.npy) |
| 321 | `model.layers.23.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 58.0 / 0.0018160508738623725 / 1.7388709983289772 | [NPY](tensors/0000321.npy) |
| 322 | `model.layers.23.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 58.0 / 0.0018160508738623725 / 1.7388709983289772 | [NPY](tensors/0000322.npy) |
| 323 | `model.layers.23.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000323.npy) |
| 324 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0000324.npy) |
| 325 | `model.layers.23.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 326 | `model.layers.23.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 327 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0000327.npy) |
| 328 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0000328.npy) |
| 329 | `model.layers.23.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 330 | `model.layers.23.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 58.0 / 0.0018160508738623725 / 1.7388709983289772 | [NPY](tensors/0000330.npy) |
| 331 | `model.layers.23.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.875 / 16.25 / 0.030419896356761456 / 1.3280486385659749 | [NPY](tensors/0000331.npy) |
| 332 | `model.layers.23.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 58.0 / 0.0018160508738623725 / 1.7388709983289772 | [NPY](tensors/0000332.npy) |
| 333 | `model.layers.23.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -37.25 / 37.75 / -0.08815270895138383 / 4.744750456234467 | [NPY](tensors/0000333.npy) |
| 334 | `model.layers.23.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 58.0 / 0.0018160508738623725 / 1.7388709983289772 | [NPY](tensors/0000334.npy) |
| 335 | `model.layers.23.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.0625 / 7.96875 / -0.032529864460229874 / 2.8589475422793997 | [NPY](tensors/0000335.npy) |
| 336 | `model.layers.23.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.4375 / 7.0 / 0.011099936906248331 / 1.2405360596237107 | [NPY](tensors/0000336.npy) |
| 337 | `model.layers.23.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5216.0 / 5536.0 / 5.437964810265435 / 231.81376564802122 | [NPY](tensors/0000337.npy) |
| 338 | `model.layers.23.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5216.0 / 5536.0 / 5.437964810265435 / 231.81376564802122 | [NPY](tensors/0000338.npy) |
| 339 | `model.layers.23.self_attn` | 2 | `output[1]` | [1, 64, 1, 323] | torch.bfloat16 → float32 | 8.215650382226158e-14 / 0.875 / 0.0022993535659296986 / 0.011899917537593552 | [NPY](tensors/0000339.npy) |
| 340 | `model.layers.23.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 9216.0 / 3.5986029730902778 / 502.49087662160986 | [NPY](tensors/0000340.npy) |
| 341 | `model.layers.23.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.25 / 8.5625 / -0.015226441621780395 / 0.9363352922203202 | [NPY](tensors/0000341.npy) |
| 342 | `model.layers.23.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.25 / 8.5625 / -0.015226441621780395 / 0.9363352922203202 | [NPY](tensors/0000342.npy) |
| 343 | `model.layers.23.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -29.25 / 8.5625 / -0.015226441621780395 / 0.9363352922203202 | [NPY](tensors/0000343.npy) |
| 344 | `model.layers.23.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 345 | `model.layers.23.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 346 | `model.layers.23.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 347 | `model.layers.23.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1128.0 / 876.0 / -2.2344920052422417 / 63.44286033709019 | [NPY](tensors/0000347.npy) |
| 348 | `model.layers.23.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1128.0 / 876.0 / -2.2344920052422417 / 63.44286033709019 | [NPY](tensors/0000348.npy) |
| 349 | `model.layers.23.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.09375 / 0.12988704442977905 / 0.4658429799908829 | [NPY](tensors/0000349.npy) |
| 350 | `model.layers.23` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8512.0 / 8768.0 / 1.354562717013889 / 482.4814069270919 | [NPY](tensors/0000350.npy) |
| 429 | `model.layers.23` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9856.0 / 9920.0 / -8.009088812934028 / 477.76900254978665 | [NPY](tensors/0000429.npy) |
| 430 | `model.layers.23` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000430.npy) |
| 431 | `model.layers.23` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0000431.npy) |
| 432 | `model.layers.23` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0000432.npy) |
| 433 | `model.layers.23` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0000433.npy) |
| 434 | `model.layers.23` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 435 | `model.layers.23` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 436 | `model.layers.23` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 437 | `model.layers.23.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9856.0 / 9920.0 / -8.009088812934028 / 477.76900254978665 | [NPY](tensors/0000437.npy) |
| 438 | `model.layers.23.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 55.75 / -0.012326810095045302 / 1.7172204135517226 | [NPY](tensors/0000438.npy) |
| 439 | `model.layers.23.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 55.75 / -0.012326810095045302 / 1.7172204135517226 | [NPY](tensors/0000439.npy) |
| 440 | `model.layers.23.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000440.npy) |
| 441 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0000441.npy) |
| 442 | `model.layers.23.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 443 | `model.layers.23.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 444 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0000444.npy) |
| 445 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0000445.npy) |
| 446 | `model.layers.23.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 447 | `model.layers.23.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 55.75 / -0.012326810095045302 / 1.7172204135517226 | [NPY](tensors/0000447.npy) |
| 448 | `model.layers.23.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.0625 / 16.0 / 0.0284326117252931 / 1.3951799046828712 | [NPY](tensors/0000448.npy) |
| 449 | `model.layers.23.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 55.75 / -0.012326810095045302 / 1.7172204135517226 | [NPY](tensors/0000449.npy) |
| 450 | `model.layers.23.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.5 / 39.25 / -0.07417012378573418 / 4.9643761351850095 | [NPY](tensors/0000450.npy) |
| 451 | `model.layers.23.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 55.75 / -0.012326810095045302 / 1.7172204135517226 | [NPY](tensors/0000451.npy) |
| 452 | `model.layers.23.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.75 / 7.5 / -0.047381460666656494 / 2.2395035144874362 | [NPY](tensors/0000452.npy) |
| 453 | `model.layers.23.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.125 / 6.84375 / 0.002892673946917057 / 1.0317309157726315 | [NPY](tensors/0000453.npy) |
| 454 | `model.layers.23.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5312.0 / 5632.0 / 5.821437072753906 / 236.35023227110378 | [NPY](tensors/0000454.npy) |
| 455 | `model.layers.23.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5312.0 / 5632.0 / 5.821437072753906 / 236.35023227110378 | [NPY](tensors/0000455.npy) |
| 456 | `model.layers.23.self_attn` | 3 | `output[1]` | [1, 64, 1, 324] | torch.bfloat16 → float32 | 4.163336342344337e-15 / 0.89453125 / 0.0018677983014344722 / 0.01125074401104323 | [NPY](tensors/0000456.npy) |
| 457 | `model.layers.23.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 9984.0 / -2.2104926215277776 / 554.0472502750881 | [NPY](tensors/0000457.npy) |
| 458 | `model.layers.23.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 8.75 / -0.029278996255662708 / 1.0100876104099887 | [NPY](tensors/0000458.npy) |
| 459 | `model.layers.23.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 8.75 / -0.029278996255662708 / 1.0100876104099887 | [NPY](tensors/0000459.npy) |
| 460 | `model.layers.23.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.5 / 8.75 / -0.029278996255662708 / 1.0100876104099887 | [NPY](tensors/0000460.npy) |
| 461 | `model.layers.23.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 462 | `model.layers.23.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 463 | `model.layers.23.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 464 | `model.layers.23.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1136.0 / 832.0 / -1.3177804734971788 / 56.60273414817991 | [NPY](tensors/0000464.npy) |
| 465 | `model.layers.23.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1136.0 / 832.0 / -1.3177804734971788 / 56.60273414817991 | [NPY](tensors/0000465.npy) |
| 466 | `model.layers.23.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.87109375 / 1.2265625 / 0.008508682250976562 / 0.4331486743471824 | [NPY](tensors/0000466.npy) |
| 467 | `model.layers.23` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9728.0 / -3.560677083333333 / 542.0239212327479 | [NPY](tensors/0000467.npy) |
| 546 | `model.layers.23` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11264.0 / 11136.0 / 2.7078070746527776 / 502.8003642401231 | [NPY](tensors/0000546.npy) |
| 547 | `model.layers.23` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000547.npy) |
| 548 | `model.layers.23` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0000548.npy) |
| 549 | `model.layers.23` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0000549.npy) |
| 550 | `model.layers.23` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0000550.npy) |
| 551 | `model.layers.23` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 552 | `model.layers.23` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 553 | `model.layers.23` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 554 | `model.layers.23.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11264.0 / 11136.0 / 2.7078070746527776 / 502.8003642401231 | [NPY](tensors/0000554.npy) |
| 555 | `model.layers.23.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 59.5 / 0.016104778978559706 / 1.765538127798798 | [NPY](tensors/0000555.npy) |
| 556 | `model.layers.23.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 59.5 / 0.016104778978559706 / 1.765538127798798 | [NPY](tensors/0000556.npy) |
| 557 | `model.layers.23.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000557.npy) |
| 558 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0000558.npy) |
| 559 | `model.layers.23.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 560 | `model.layers.23.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 561 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0000561.npy) |
| 562 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0000562.npy) |
| 563 | `model.layers.23.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 564 | `model.layers.23.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 59.5 / 0.016104778978559706 / 1.765538127798798 | [NPY](tensors/0000564.npy) |
| 565 | `model.layers.23.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.75 / 14.5625 / 0.027590783312916756 / 1.394111597130874 | [NPY](tensors/0000565.npy) |
| 566 | `model.layers.23.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 59.5 / 0.016104778978559706 / 1.765538127798798 | [NPY](tensors/0000566.npy) |
| 567 | `model.layers.23.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.75 / 46.0 / -0.1053767055273056 / 5.303365306513238 | [NPY](tensors/0000567.npy) |
| 568 | `model.layers.23.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 59.5 / 0.016104778978559706 / 1.765538127798798 | [NPY](tensors/0000568.npy) |
| 569 | `model.layers.23.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.75 / 9.375 / 0.09432411193847656 / 3.2825974513487015 | [NPY](tensors/0000569.npy) |
| 570 | `model.layers.23.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.9375 / 6.8125 / 0.0006463667377829552 / 1.3194420945365997 | [NPY](tensors/0000570.npy) |
| 571 | `model.layers.23.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5568.0 / 5888.0 / 7.666418446434869 / 249.49304753932523 | [NPY](tensors/0000571.npy) |
| 572 | `model.layers.23.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5568.0 / 5888.0 / 7.666418446434869 / 249.49304753932523 | [NPY](tensors/0000572.npy) |
| 573 | `model.layers.23.self_attn` | 4 | `output[1]` | [1, 64, 1, 325] | torch.bfloat16 → float32 | 9.414691248821327e-14 / 0.88671875 / 0.0020989123762965747 / 0.014211660366097553 | [NPY](tensors/0000573.npy) |
| 574 | `model.layers.23.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11264.0 / 11136.0 / 10.378801812065973 / 583.3653019227285 | [NPY](tensors/0000574.npy) |
| 575 | `model.layers.23.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 9.4375 / 0.001994903220070733 / 1.0149719910479986 | [NPY](tensors/0000575.npy) |
| 576 | `model.layers.23.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 9.4375 / 0.001994903220070733 / 1.0149719910479986 | [NPY](tensors/0000576.npy) |
| 577 | `model.layers.23.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.25 / 9.4375 / 0.001994903220070733 / 1.0149719910479986 | [NPY](tensors/0000577.npy) |
| 578 | `model.layers.23.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 579 | `model.layers.23.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 580 | `model.layers.23.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 581 | `model.layers.23.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1528.0 / 1056.0 / -0.7310768127441406 / 74.69007103459005 | [NPY](tensors/0000581.npy) |
| 582 | `model.layers.23.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1528.0 / 1056.0 / -0.7310768127441406 / 74.69007103459005 | [NPY](tensors/0000582.npy) |
| 583 | `model.layers.23.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.140625 / 1.140625 / 0.13389670848846436 / 0.46923375098413544 | [NPY](tensors/0000583.npy) |
| 584 | `model.layers.23` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10560.0 / 9.634932454427084 / 557.7512785424593 | [NPY](tensors/0000584.npy) |
| 663 | `model.layers.23` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 9728.0 / -2.0115451388888888 / 464.50541797559606 | [NPY](tensors/0000663.npy) |
| 664 | `model.layers.23` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000664.npy) |
| 665 | `model.layers.23` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0000665.npy) |
| 666 | `model.layers.23` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0000666.npy) |
| 667 | `model.layers.23` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0000667.npy) |
| 668 | `model.layers.23` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 669 | `model.layers.23` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 670 | `model.layers.23` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 671 | `model.layers.23.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 9728.0 / -2.0115451388888888 / 464.50541797559606 | [NPY](tensors/0000671.npy) |
| 672 | `model.layers.23.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 56.25 / -0.0036696910858154295 / 1.7456270538762155 | [NPY](tensors/0000672.npy) |
| 673 | `model.layers.23.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 56.25 / -0.0036696910858154295 / 1.7456270538762155 | [NPY](tensors/0000673.npy) |
| 674 | `model.layers.23.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000674.npy) |
| 675 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0000675.npy) |
| 676 | `model.layers.23.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 677 | `model.layers.23.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 678 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0000678.npy) |
| 679 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0000679.npy) |
| 680 | `model.layers.23.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 681 | `model.layers.23.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 56.25 / -0.0036696910858154295 / 1.7456270538762155 | [NPY](tensors/0000681.npy) |
| 682 | `model.layers.23.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.875 / 17.25 / 0.029835569839633536 / 1.4646930473495097 | [NPY](tensors/0000682.npy) |
| 683 | `model.layers.23.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 56.25 / -0.0036696910858154295 / 1.7456270538762155 | [NPY](tensors/0000683.npy) |
| 684 | `model.layers.23.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -59.25 / 48.0 / -0.08199749514460564 / 5.368835527136233 | [NPY](tensors/0000684.npy) |
| 685 | `model.layers.23.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 56.25 / -0.0036696910858154295 / 1.7456270538762155 | [NPY](tensors/0000685.npy) |
| 686 | `model.layers.23.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -12.75 / 11.8125 / 0.059237003326416016 / 3.2614586157314336 | [NPY](tensors/0000686.npy) |
| 687 | `model.layers.23.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.875 / 7.3125 / -0.010334512451663613 / 1.1879109478198708 | [NPY](tensors/0000687.npy) |
| 688 | `model.layers.23.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5280.0 / 5472.0 / 7.091273795233833 / 230.30435173072786 | [NPY](tensors/0000688.npy) |
| 689 | `model.layers.23.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5280.0 / 5472.0 / 7.091273795233833 / 230.30435173072786 | [NPY](tensors/0000689.npy) |
| 690 | `model.layers.23.self_attn` | 5 | `output[1]` | [1, 64, 1, 326] | torch.bfloat16 → float32 | 8.93729534823251e-15 / 0.90625 / 0.002007099858750428 / 0.012583327770328175 | [NPY](tensors/0000690.npy) |
| 691 | `model.layers.23.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 9792.0 / 5.095077853732639 / 533.332127905756 | [NPY](tensors/0000691.npy) |
| 692 | `model.layers.23.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 7.6875 / -0.011463790469699435 / 0.9852033482668996 | [NPY](tensors/0000692.npy) |
| 693 | `model.layers.23.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 7.6875 / -0.011463790469699435 / 0.9852033482668996 | [NPY](tensors/0000693.npy) |
| 694 | `model.layers.23.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.5 / 7.6875 / -0.011463790469699435 / 0.9852033482668996 | [NPY](tensors/0000694.npy) |
| 695 | `model.layers.23.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 696 | `model.layers.23.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 697 | `model.layers.23.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 698 | `model.layers.23.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -952.0 / 656.0 / -0.946894359588623 / 47.745452505390155 | [NPY](tensors/0000698.npy) |
| 699 | `model.layers.23.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -952.0 / 656.0 / -0.946894359588623 / 47.745452505390155 | [NPY](tensors/0000699.npy) |
| 700 | `model.layers.23.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.80859375 / 1.265625 / 0.14108943939208984 / 0.42123937798619887 | [NPY](tensors/0000700.npy) |
| 701 | `model.layers.23` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9536.0 / 4.167892795138889 / 523.6879884073588 | [NPY](tensors/0000701.npy) |
| 780 | `model.layers.23` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 9920.0 / -7.559138997395833 / 451.78661050997164 | [NPY](tensors/0000780.npy) |
| 781 | `model.layers.23` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000781.npy) |
| 782 | `model.layers.23` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0000782.npy) |
| 783 | `model.layers.23` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0000783.npy) |
| 784 | `model.layers.23` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0000784.npy) |
| 785 | `model.layers.23` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 786 | `model.layers.23` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 787 | `model.layers.23` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 788 | `model.layers.23.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 9920.0 / -7.559138997395833 / 451.78661050997164 | [NPY](tensors/0000788.npy) |
| 789 | `model.layers.23.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 58.5 / -0.009372463822364807 / 1.7781854880368693 | [NPY](tensors/0000789.npy) |
| 790 | `model.layers.23.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 58.5 / -0.009372463822364807 / 1.7781854880368693 | [NPY](tensors/0000790.npy) |
| 791 | `model.layers.23.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000791.npy) |
| 792 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0000792.npy) |
| 793 | `model.layers.23.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 794 | `model.layers.23.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 795 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0000795.npy) |
| 796 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0000796.npy) |
| 797 | `model.layers.23.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 798 | `model.layers.23.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 58.5 / -0.009372463822364807 / 1.7781854880368693 | [NPY](tensors/0000798.npy) |
| 799 | `model.layers.23.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.5 / 13.6875 / 0.028083962621167302 / 1.381742337987122 | [NPY](tensors/0000799.npy) |
| 800 | `model.layers.23.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 58.5 / -0.009372463822364807 / 1.7781854880368693 | [NPY](tensors/0000800.npy) |
| 801 | `model.layers.23.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.5 / 50.0 / -0.08103248849511147 / 5.525016174530262 | [NPY](tensors/0000801.npy) |
| 802 | `model.layers.23.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 58.5 / -0.009372463822364807 / 1.7781854880368693 | [NPY](tensors/0000802.npy) |
| 803 | `model.layers.23.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.625 / 9.1875 / -0.017035067081451416 / 2.1144321197520095 | [NPY](tensors/0000803.npy) |
| 804 | `model.layers.23.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.6875 / 8.6875 / 0.0010456782765686512 / 1.3979202006442872 | [NPY](tensors/0000804.npy) |
| 805 | `model.layers.23.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5568.0 / 5760.0 / 5.376691950692071 / 245.91409545102124 | [NPY](tensors/0000805.npy) |
| 806 | `model.layers.23.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5568.0 / 5760.0 / 5.376691950692071 / 245.91409545102124 | [NPY](tensors/0000806.npy) |
| 807 | `model.layers.23.self_attn` | 6 | `output[1]` | [1, 64, 1, 327] | torch.bfloat16 → float32 | 1.9761969838327786e-14 / 0.9453125 / 0.0024621621698449566 / 0.013113930796107552 | [NPY](tensors/0000807.npy) |
| 808 | `model.layers.23.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 9792.0 / -2.127080620659722 / 526.6033477324236 | [NPY](tensors/0000808.npy) |
| 809 | `model.layers.23.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.125 / 7.5625 / -0.030136238866382174 / 0.9609503853122489 | [NPY](tensors/0000809.npy) |
| 810 | `model.layers.23.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.125 / 7.5625 / -0.030136238866382174 / 0.9609503853122489 | [NPY](tensors/0000810.npy) |
| 811 | `model.layers.23.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -28.125 / 7.5625 / -0.030136238866382174 / 0.9609503853122489 | [NPY](tensors/0000811.npy) |
| 812 | `model.layers.23.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 813 | `model.layers.23.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 814 | `model.layers.23.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 815 | `model.layers.23.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -876.0 / 848.0 / -2.381175316704644 / 64.25833794931371 | [NPY](tensors/0000815.npy) |
| 816 | `model.layers.23.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -876.0 / 848.0 / -2.381175316704644 / 64.25833794931371 | [NPY](tensors/0000816.npy) |
| 817 | `model.layers.23.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.73046875 / 1.171875 / 0.03455018997192383 / 0.43573940795693844 | [NPY](tensors/0000817.npy) |
| 818 | `model.layers.23` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 9152.0 / -4.521271430121528 / 495.9362141913803 | [NPY](tensors/0000818.npy) |
| 897 | `model.layers.23` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 10240.0 / 2.0784654405381944 / 473.3889893054129 | [NPY](tensors/0000897.npy) |
| 898 | `model.layers.23` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000898.npy) |
| 899 | `model.layers.23` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0000899.npy) |
| 900 | `model.layers.23` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0000900.npy) |
| 901 | `model.layers.23` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0000901.npy) |
| 902 | `model.layers.23` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 903 | `model.layers.23` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 904 | `model.layers.23` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 905 | `model.layers.23.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 10240.0 / 2.0784654405381944 / 473.3889893054129 | [NPY](tensors/0000905.npy) |
| 906 | `model.layers.23.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.25 / 0.017003687222798665 / 1.7459387621098224 | [NPY](tensors/0000906.npy) |
| 907 | `model.layers.23.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.25 / 0.017003687222798665 / 1.7459387621098224 | [NPY](tensors/0000907.npy) |
| 908 | `model.layers.23.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000908.npy) |
| 909 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0000909.npy) |
| 910 | `model.layers.23.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 911 | `model.layers.23.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 912 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0000912.npy) |
| 913 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0000913.npy) |
| 914 | `model.layers.23.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 915 | `model.layers.23.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.25 / 0.017003687222798665 / 1.7459387621098224 | [NPY](tensors/0000915.npy) |
| 916 | `model.layers.23.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.8125 / 14.3125 / 0.017722707241773605 / 1.3647464608351978 | [NPY](tensors/0000916.npy) |
| 917 | `model.layers.23.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.25 / 0.017003687222798665 / 1.7459387621098224 | [NPY](tensors/0000917.npy) |
| 918 | `model.layers.23.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.25 / 45.25 / -0.19241394102573395 / 5.115723337433457 | [NPY](tensors/0000918.npy) |
| 919 | `model.layers.23.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.25 / 0.017003687222798665 / 1.7459387621098224 | [NPY](tensors/0000919.npy) |
| 920 | `model.layers.23.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.6875 / 8.25 / 0.014055311679840088 / 3.0051709047873696 | [NPY](tensors/0000920.npy) |
| 921 | `model.layers.23.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.5 / 7.5625 / 0.07367038447409868 / 1.4245768306223665 | [NPY](tensors/0000921.npy) |
| 922 | `model.layers.23.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5312.0 / 5600.0 / 4.887033165825738 / 234.99016412333194 | [NPY](tensors/0000922.npy) |
| 923 | `model.layers.23.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5312.0 / 5600.0 / 4.887033165825738 / 234.99016412333194 | [NPY](tensors/0000923.npy) |
| 924 | `model.layers.23.self_attn` | 7 | `output[1]` | [1, 64, 1, 328] | torch.bfloat16 → float32 | 2.646771690706373e-13 / 0.921875 / 0.0023119867629061166 / 0.013416070702075312 | [NPY](tensors/0000924.npy) |
| 925 | `model.layers.23.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9856.0 / 10176.0 / 6.961924913194444 / 537.7490645623899 | [NPY](tensors/0000925.npy) |
| 926 | `model.layers.23.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 8.5 / -0.011627939012315538 / 1.0081010186694999 | [NPY](tensors/0000926.npy) |
| 927 | `model.layers.23.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 8.5 / -0.011627939012315538 / 1.0081010186694999 | [NPY](tensors/0000927.npy) |
| 928 | `model.layers.23.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.0 / 8.5 / -0.011627939012315538 / 1.0081010186694999 | [NPY](tensors/0000928.npy) |
| 929 | `model.layers.23.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 930 | `model.layers.23.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 931 | `model.layers.23.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 932 | `model.layers.23.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1712.0 / 1472.0 / -2.777138026555379 / 78.42337907337587 | [NPY](tensors/0000932.npy) |
| 933 | `model.layers.23.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1712.0 / 1472.0 / -2.777138026555379 / 78.42337907337587 | [NPY](tensors/0000933.npy) |
| 934 | `model.layers.23.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.125 / 1.1875 / 0.11432647705078125 / 0.5168693844623047 | [NPY](tensors/0000934.npy) |
| 935 | `model.layers.23` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9792.0 / 10240.0 / 4.203485785590278 / 549.3746300797436 | [NPY](tensors/0000935.npy) |
| 1014 | `model.layers.23` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 10176.0 / 0.7060804578993055 / 478.3375717241384 | [NPY](tensors/0001014.npy) |
| 1015 | `model.layers.23` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001015.npy) |
| 1016 | `model.layers.23` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0001016.npy) |
| 1017 | `model.layers.23` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0001017.npy) |
| 1018 | `model.layers.23` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0001018.npy) |
| 1019 | `model.layers.23` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1020 | `model.layers.23` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1021 | `model.layers.23` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1022 | `model.layers.23.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 10176.0 / 0.7060804578993055 / 478.3375717241384 | [NPY](tensors/0001022.npy) |
| 1023 | `model.layers.23.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 57.25 / 0.009009997049967447 / 1.7472545941784907 | [NPY](tensors/0001023.npy) |
| 1024 | `model.layers.23.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 57.25 / 0.009009997049967447 / 1.7472545941784907 | [NPY](tensors/0001024.npy) |
| 1025 | `model.layers.23.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001025.npy) |
| 1026 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0001026.npy) |
| 1027 | `model.layers.23.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1028 | `model.layers.23.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1029 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0001029.npy) |
| 1030 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0001030.npy) |
| 1031 | `model.layers.23.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1032 | `model.layers.23.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 57.25 / 0.009009997049967447 / 1.7472545941784907 | [NPY](tensors/0001032.npy) |
| 1033 | `model.layers.23.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.4375 / 16.75 / 0.02520619099959731 / 1.4974538499206385 | [NPY](tensors/0001033.npy) |
| 1034 | `model.layers.23.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 57.25 / 0.009009997049967447 / 1.7472545941784907 | [NPY](tensors/0001034.npy) |
| 1035 | `model.layers.23.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.0 / 40.5 / -0.021976396441459656 / 5.463240367940199 | [NPY](tensors/0001035.npy) |
| 1036 | `model.layers.23.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 57.25 / 0.009009997049967447 / 1.7472545941784907 | [NPY](tensors/0001036.npy) |
| 1037 | `model.layers.23.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.5625 / 13.5625 / 0.33293038606643677 / 3.464371710404605 | [NPY](tensors/0001037.npy) |
| 1038 | `model.layers.23.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.5625 / 7.21875 / 0.04428168945014477 / 1.342919012742134 | [NPY](tensors/0001038.npy) |
| 1039 | `model.layers.23.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5664.0 / 5.844649855295817 / 238.2922586879232 | [NPY](tensors/0001039.npy) |
| 1040 | `model.layers.23.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5664.0 / 5.844649855295817 / 238.2922586879232 | [NPY](tensors/0001040.npy) |
| 1041 | `model.layers.23.self_attn` | 8 | `output[1]` | [1, 64, 1, 329] | torch.bfloat16 → float32 | 3.446132268436486e-13 / 0.93359375 / 0.002196461369857771 / 0.013711770400431188 | [NPY](tensors/0001041.npy) |
| 1042 | `model.layers.23.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 10176.0 / 6.528038194444444 / 547.930070026824 | [NPY](tensors/0001042.npy) |
| 1043 | `model.layers.23.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 8.375 / -0.007522956530253092 / 1.0374192919980452 | [NPY](tensors/0001043.npy) |
| 1044 | `model.layers.23.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 8.375 / -0.007522956530253092 / 1.0374192919980452 | [NPY](tensors/0001044.npy) |
| 1045 | `model.layers.23.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.75 / 8.375 / -0.007522956530253092 / 1.0374192919980452 | [NPY](tensors/0001045.npy) |
| 1046 | `model.layers.23.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1047 | `model.layers.23.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1048 | `model.layers.23.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1049 | `model.layers.23.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1056.0 / 744.0 / -1.2248940573798286 / 58.03359348567735 | [NPY](tensors/0001049.npy) |
| 1050 | `model.layers.23.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1056.0 / 744.0 / -1.2248940573798286 / 58.03359348567735 | [NPY](tensors/0001050.npy) |
| 1051 | `model.layers.23.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.125 / 1.28125 / 0.10275793075561523 / 0.5081495681498245 | [NPY](tensors/0001051.npy) |
| 1052 | `model.layers.23` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 9856.0 / 5.31455078125 / 530.5980914889701 | [NPY](tensors/0001052.npy) |
| 1131 | `model.layers.23` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10752.0 / 9856.0 / -1.7229871961805556 / 479.0068175764193 | [NPY](tensors/0001131.npy) |
| 1132 | `model.layers.23` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 330] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001132.npy) |
| 1133 | `model.layers.23` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0001133.npy) |
| 1134 | `model.layers.23` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0001134.npy) |
| 1135 | `model.layers.23` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0001135.npy) |
| 1136 | `model.layers.23` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1137 | `model.layers.23` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1138 | `model.layers.23` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1139 | `model.layers.23.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10752.0 / 9856.0 / -1.7229871961805556 / 479.0068175764193 | [NPY](tensors/0001139.npy) |
| 1140 | `model.layers.23.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 55.25 / 0.0013665649625990127 / 1.7427605002556754 | [NPY](tensors/0001140.npy) |
| 1141 | `model.layers.23.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 55.25 / 0.0013665649625990127 / 1.7427605002556754 | [NPY](tensors/0001141.npy) |
| 1142 | `model.layers.23.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 330] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001142.npy) |
| 1143 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0001143.npy) |
| 1144 | `model.layers.23.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1145 | `model.layers.23.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1146 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0001146.npy) |
| 1147 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0001147.npy) |
| 1148 | `model.layers.23.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1149 | `model.layers.23.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 55.25 / 0.0013665649625990127 / 1.7427605002556754 | [NPY](tensors/0001149.npy) |
| 1150 | `model.layers.23.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.375 / 17.125 / 0.019977983844000846 / 1.5013773900923655 | [NPY](tensors/0001150.npy) |
| 1151 | `model.layers.23.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 55.25 / 0.0013665649625990127 / 1.7427605002556754 | [NPY](tensors/0001151.npy) |
| 1152 | `model.layers.23.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.75 / 52.75 / -0.05944763123989105 / 5.658474199748716 | [NPY](tensors/0001152.npy) |
| 1153 | `model.layers.23.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 55.25 / 0.0013665649625990127 / 1.7427605002556754 | [NPY](tensors/0001153.npy) |
| 1154 | `model.layers.23.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.375 / 15.0 / 0.08036178350448608 / 3.9794810557206217 | [NPY](tensors/0001154.npy) |
| 1155 | `model.layers.23.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.03348132409155369 / 1.332858248680032 | [NPY](tensors/0001155.npy) |
| 1156 | `model.layers.23.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5440.0 / 5664.0 / 5.75396908654107 / 237.66035120015272 | [NPY](tensors/0001156.npy) |
| 1157 | `model.layers.23.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5440.0 / 5664.0 / 5.75396908654107 / 237.66035120015272 | [NPY](tensors/0001157.npy) |
| 1158 | `model.layers.23.self_attn` | 9 | `output[1]` | [1, 64, 1, 330] | torch.bfloat16 → float32 | 9.903189379656396e-14 / 0.93359375 / 0.0022642172632003 / 0.012396827876820017 | [NPY](tensors/0001158.npy) |
| 1159 | `model.layers.23.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 9664.0 / 4.038319227430556 / 539.960344515423 | [NPY](tensors/0001159.npy) |
| 1160 | `model.layers.23.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 8.0625 / -0.015306176741917928 / 1.0657032505156756 | [NPY](tensors/0001160.npy) |
| 1161 | `model.layers.23.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 8.0625 / -0.015306176741917928 / 1.0657032505156756 | [NPY](tensors/0001161.npy) |
| 1162 | `model.layers.23.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.25 / 8.0625 / -0.015306176741917928 / 1.0657032505156756 | [NPY](tensors/0001162.npy) |
| 1163 | `model.layers.23.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1164 | `model.layers.23.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1165 | `model.layers.23.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1166 | `model.layers.23.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1384.0 / 1136.0 / -0.3020036061604818 / 65.80969822672087 | [NPY](tensors/0001166.npy) |
| 1167 | `model.layers.23.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1384.0 / 1136.0 / -0.3020036061604818 / 65.80969822672087 | [NPY](tensors/0001167.npy) |
| 1168 | `model.layers.23.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0234375 / 1.296875 / 0.1247553825378418 / 0.5083720826496042 | [NPY](tensors/0001168.npy) |
| 1169 | `model.layers.23` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10752.0 / 9984.0 / 3.776961263020833 / 559.733736065178 | [NPY](tensors/0001169.npy) |
| 1248 | `model.layers.23` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9856.0 / 9344.0 / -3.5182508680555555 / 454.1930255086918 | [NPY](tensors/0001248.npy) |
| 1249 | `model.layers.23` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 331] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001249.npy) |
| 1250 | `model.layers.23` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0001250.npy) |
| 1251 | `model.layers.23` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0001251.npy) |
| 1252 | `model.layers.23` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0001252.npy) |
| 1253 | `model.layers.23` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1254 | `model.layers.23` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1255 | `model.layers.23` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1256 | `model.layers.23.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9856.0 / 9344.0 / -3.5182508680555555 / 454.1930255086918 | [NPY](tensors/0001256.npy) |
| 1257 | `model.layers.23.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 55.25 / -0.005464350514941745 / 1.7317375178006944 | [NPY](tensors/0001257.npy) |
| 1258 | `model.layers.23.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 55.25 / -0.005464350514941745 / 1.7317375178006944 | [NPY](tensors/0001258.npy) |
| 1259 | `model.layers.23.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 331] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001259.npy) |
| 1260 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0001260.npy) |
| 1261 | `model.layers.23.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1262 | `model.layers.23.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1263 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0001263.npy) |
| 1264 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0001264.npy) |
| 1265 | `model.layers.23.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1266 | `model.layers.23.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 55.25 / -0.005464350514941745 / 1.7317375178006944 | [NPY](tensors/0001266.npy) |
| 1267 | `model.layers.23.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.4375 / 15.375 / 0.028873696603113785 / 1.486467434372007 | [NPY](tensors/0001267.npy) |
| 1268 | `model.layers.23.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 55.25 / -0.005464350514941745 / 1.7317375178006944 | [NPY](tensors/0001268.npy) |
| 1269 | `model.layers.23.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.75 / 50.25 / -0.048138976097106934 / 5.637562958871481 | [NPY](tensors/0001269.npy) |
| 1270 | `model.layers.23.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 55.25 / -0.005464350514941745 / 1.7317375178006944 | [NPY](tensors/0001270.npy) |
| 1271 | `model.layers.23.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.125 / 10.9375 / 0.07825815677642822 / 3.1870918698806023 | [NPY](tensors/0001271.npy) |
| 1272 | `model.layers.23.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.8125 / 8.25 / 0.01889723155181855 / 1.3138582158091408 | [NPY](tensors/0001272.npy) |
| 1273 | `model.layers.23.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5120.0 / 5376.0 / 5.696182674831814 / 225.98367434255798 | [NPY](tensors/0001273.npy) |
| 1274 | `model.layers.23.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5120.0 / 5376.0 / 5.696182674831814 / 225.98367434255798 | [NPY](tensors/0001274.npy) |
| 1275 | `model.layers.23.self_attn` | 10 | `output[1]` | [1, 64, 1, 331] | torch.bfloat16 → float32 | 2.682298827494378e-13 / 0.9296875 / 0.002122422110891379 / 0.012372150076459771 | [NPY](tensors/0001275.npy) |
| 1276 | `model.layers.23.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 9152.0 / 2.150873480902778 / 510.84192353236836 | [NPY](tensors/0001276.npy) |
| 1277 | `model.layers.23.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.75 / 9.125 / -0.021705394321017795 / 1.0700857122595078 | [NPY](tensors/0001277.npy) |
| 1278 | `model.layers.23.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.75 / 9.125 / -0.021705394321017795 / 1.0700857122595078 | [NPY](tensors/0001278.npy) |
| 1279 | `model.layers.23.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -35.75 / 9.125 / -0.021705394321017795 / 1.0700857122595078 | [NPY](tensors/0001279.npy) |
| 1280 | `model.layers.23.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1281 | `model.layers.23.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1282 | `model.layers.23.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1283 | `model.layers.23.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1728.0 / 1384.0 / -0.6269576907157898 / 77.13087196230835 | [NPY](tensors/0001283.npy) |
| 1284 | `model.layers.23.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1728.0 / 1384.0 / -0.6269576907157898 / 77.13087196230835 | [NPY](tensors/0001284.npy) |
| 1285 | `model.layers.23.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.98046875 / 1.3203125 / 0.1582813262939453 / 0.49913736017078786 | [NPY](tensors/0001285.npy) |
| 1286 | `model.layers.23` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9856.0 / 9280.0 / 1.5207899305555554 / 532.8134201926111 | [NPY](tensors/0001286.npy) |
| 1365 | `model.layers.23` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9600.0 / -7.628786892361111 / 445.38192194570075 | [NPY](tensors/0001365.npy) |
| 1366 | `model.layers.23` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 332] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001366.npy) |
| 1367 | `model.layers.23` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0001367.npy) |
| 1368 | `model.layers.23` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0001368.npy) |
| 1369 | `model.layers.23` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0001369.npy) |
| 1370 | `model.layers.23` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1371 | `model.layers.23` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1372 | `model.layers.23` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1373 | `model.layers.23.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9600.0 / -7.628786892361111 / 445.38192194570075 | [NPY](tensors/0001373.npy) |
| 1374 | `model.layers.23.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 58.0 / -0.00917735927634769 / 1.785349523113161 | [NPY](tensors/0001374.npy) |
| 1375 | `model.layers.23.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 58.0 / -0.00917735927634769 / 1.785349523113161 | [NPY](tensors/0001375.npy) |
| 1376 | `model.layers.23.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 332] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001376.npy) |
| 1377 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0001377.npy) |
| 1378 | `model.layers.23.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1379 | `model.layers.23.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1380 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0001380.npy) |
| 1381 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0001381.npy) |
| 1382 | `model.layers.23.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1383 | `model.layers.23.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 58.0 / -0.00917735927634769 / 1.785349523113161 | [NPY](tensors/0001383.npy) |
| 1384 | `model.layers.23.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 14.625 / 0.021795323584228754 / 1.409207422991659 | [NPY](tensors/0001384.npy) |
| 1385 | `model.layers.23.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 58.0 / -0.00917735927634769 / 1.785349523113161 | [NPY](tensors/0001385.npy) |
| 1386 | `model.layers.23.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.0 / 49.75 / -0.09064484015107155 / 5.6517546120885225 | [NPY](tensors/0001386.npy) |
| 1387 | `model.layers.23.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 58.0 / -0.00917735927634769 / 1.785349523113161 | [NPY](tensors/0001387.npy) |
| 1388 | `model.layers.23.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.5 / 7.9375 / -0.016949623823165894 / 2.265060310292581 | [NPY](tensors/0001388.npy) |
| 1389 | `model.layers.23.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.75 / 7.625 / -0.012126833666116 / 1.3929853294427332 | [NPY](tensors/0001389.npy) |
| 1390 | `model.layers.23.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5984.0 / 6208.0 / 6.039788394504123 / 269.65847147209905 | [NPY](tensors/0001390.npy) |
| 1391 | `model.layers.23.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5984.0 / 6208.0 / 6.039788394504123 / 269.65847147209905 | [NPY](tensors/0001391.npy) |
| 1392 | `model.layers.23.self_attn` | 11 | `output[1]` | [1, 64, 1, 332] | torch.bfloat16 → float32 | 2.7711166694643907e-13 / 0.9609375 / 0.002314116507437378 / 0.012336750579950453 | [NPY](tensors/0001392.npy) |
| 1393 | `model.layers.23.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11072.0 / 9920.0 / -1.5605143229166667 / 551.9228740891192 | [NPY](tensors/0001393.npy) |
| 1394 | `model.layers.23.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.25 / 7.59375 / -0.027376840511957806 / 0.9227288505971389 | [NPY](tensors/0001394.npy) |
| 1395 | `model.layers.23.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.25 / 7.59375 / -0.027376840511957806 / 0.9227288505971389 | [NPY](tensors/0001395.npy) |
| 1396 | `model.layers.23.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -24.25 / 7.59375 / -0.027376840511957806 / 0.9227288505971389 | [NPY](tensors/0001396.npy) |
| 1397 | `model.layers.23.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1398 | `model.layers.23.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1399 | `model.layers.23.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1400 | `model.layers.23.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -856.0 / 832.0 / -2.232988272772895 / 64.51036986702746 | [NPY](tensors/0001400.npy) |
| 1401 | `model.layers.23.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -856.0 / 832.0 / -2.232988272772895 / 64.51036986702746 | [NPY](tensors/0001401.npy) |
| 1402 | `model.layers.23.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.66015625 / 1.203125 / 0.025836944580078125 / 0.4263965537702102 | [NPY](tensors/0001402.npy) |
| 1403 | `model.layers.23` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 9280.0 / -3.7755262586805554 / 520.0329127226959 | [NPY](tensors/0001403.npy) |
| 1482 | `model.layers.23` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 10304.0 / -4.864634195963542 / 476.6909124993324 | [NPY](tensors/0001482.npy) |
| 1483 | `model.layers.23` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 333] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001483.npy) |
| 1484 | `model.layers.23` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0001484.npy) |
| 1485 | `model.layers.23` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0001485.npy) |
| 1486 | `model.layers.23` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0001486.npy) |
| 1487 | `model.layers.23` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1488 | `model.layers.23` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1489 | `model.layers.23` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1490 | `model.layers.23.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 10304.0 / -4.864634195963542 / 476.6909124993324 | [NPY](tensors/0001490.npy) |
| 1491 | `model.layers.23.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 58.0 / -0.003097734848658244 / 1.7561832018340544 | [NPY](tensors/0001491.npy) |
| 1492 | `model.layers.23.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 58.0 / -0.003097734848658244 / 1.7561832018340544 | [NPY](tensors/0001492.npy) |
| 1493 | `model.layers.23.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 333] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001493.npy) |
| 1494 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0001494.npy) |
| 1495 | `model.layers.23.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1496 | `model.layers.23.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1497 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0001497.npy) |
| 1498 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0001498.npy) |
| 1499 | `model.layers.23.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1500 | `model.layers.23.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 58.0 / -0.003097734848658244 / 1.7561832018340544 | [NPY](tensors/0001500.npy) |
| 1501 | `model.layers.23.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.3125 / 17.25 / 0.02603066304436652 / 1.3819129829487053 | [NPY](tensors/0001501.npy) |
| 1502 | `model.layers.23.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 58.0 / -0.003097734848658244 / 1.7561832018340544 | [NPY](tensors/0001502.npy) |
| 1503 | `model.layers.23.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.25 / 43.0 / -0.13816431164741516 / 4.8852955390955595 | [NPY](tensors/0001503.npy) |
| 1504 | `model.layers.23.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 58.0 / -0.003097734848658244 / 1.7561832018340544 | [NPY](tensors/0001504.npy) |
| 1505 | `model.layers.23.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.875 / 8.25 / -0.0022149458527565002 / 2.7454749840317025 | [NPY](tensors/0001505.npy) |
| 1506 | `model.layers.23.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.25 / 7.40625 / 0.0030892996583133936 / 1.0598884242475697 | [NPY](tensors/0001506.npy) |
| 1507 | `model.layers.23.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5664.0 / 5.6636957698398165 / 239.01016104925304 | [NPY](tensors/0001507.npy) |
| 1508 | `model.layers.23.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5664.0 / 5.6636957698398165 / 239.01016104925304 | [NPY](tensors/0001508.npy) |
| 1509 | `model.layers.23.self_attn` | 12 | `output[1]` | [1, 64, 1, 333] | torch.bfloat16 → float32 | 1.1379786002407855e-14 / 0.8984375 / 0.0018271066242218365 / 0.010151477474207343 | [NPY](tensors/0001509.npy) |
| 1510 | `model.layers.23.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 10368.0 / 0.7875257703993056 / 551.8550481357519 | [NPY](tensors/0001510.npy) |
| 1511 | `model.layers.23.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 8.4375 / -0.021414559417300753 / 0.9936568399157131 | [NPY](tensors/0001511.npy) |
| 1512 | `model.layers.23.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 8.4375 / -0.021414559417300753 / 0.9936568399157131 | [NPY](tensors/0001512.npy) |
| 1513 | `model.layers.23.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.5 / 8.4375 / -0.021414559417300753 / 0.9936568399157131 | [NPY](tensors/0001513.npy) |
| 1514 | `model.layers.23.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1515 | `model.layers.23.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1516 | `model.layers.23.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1517 | `model.layers.23.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1048.0 / 640.0 / -1.9223952187432183 / 56.76609196293658 | [NPY](tensors/0001517.npy) |
| 1518 | `model.layers.23.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1048.0 / 640.0 / -1.9223952187432183 / 56.76609196293658 | [NPY](tensors/0001518.npy) |
| 1519 | `model.layers.23.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.94140625 / 1.3515625 / 0.02528667449951172 / 0.46559012727041943 | [NPY](tensors/0001519.npy) |
| 1520 | `model.layers.23` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9984.0 / 9984.0 / -1.1064290364583333 / 532.1921993854373 | [NPY](tensors/0001520.npy) |
| 1599 | `model.layers.23` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10944.0 / 10240.0 / 5.382240125868056 / 494.6127505229684 | [NPY](tensors/0001599.npy) |
| 1600 | `model.layers.23` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 334] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001600.npy) |
| 1601 | `model.layers.23` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0001601.npy) |
| 1602 | `model.layers.23` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0001602.npy) |
| 1603 | `model.layers.23` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0001603.npy) |
| 1604 | `model.layers.23` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1605 | `model.layers.23` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1606 | `model.layers.23` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1607 | `model.layers.23.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10944.0 / 10240.0 / 5.382240125868056 / 494.6127505229684 | [NPY](tensors/0001607.npy) |
| 1608 | `model.layers.23.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 55.75 / 0.023141580157809788 / 1.7350463111464571 | [NPY](tensors/0001608.npy) |
| 1609 | `model.layers.23.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 55.75 / 0.023141580157809788 / 1.7350463111464571 | [NPY](tensors/0001609.npy) |
| 1610 | `model.layers.23.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 334] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001610.npy) |
| 1611 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0001611.npy) |
| 1612 | `model.layers.23.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1613 | `model.layers.23.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1614 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0001614.npy) |
| 1615 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0001615.npy) |
| 1616 | `model.layers.23.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1617 | `model.layers.23.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 55.75 / 0.023141580157809788 / 1.7350463111464571 | [NPY](tensors/0001617.npy) |
| 1618 | `model.layers.23.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.1875 / 16.0 / 0.02491606498369947 / 1.3334571723316366 | [NPY](tensors/0001618.npy) |
| 1619 | `model.layers.23.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 55.75 / 0.023141580157809788 / 1.7350463111464571 | [NPY](tensors/0001619.npy) |
| 1620 | `model.layers.23.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.25 / 46.0 / -0.16026020050048828 / 4.916628258189115 | [NPY](tensors/0001620.npy) |
| 1621 | `model.layers.23.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 55.75 / 0.023141580157809788 / 1.7350463111464571 | [NPY](tensors/0001621.npy) |
| 1622 | `model.layers.23.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.375 / 10.125 / 0.0004153028130531311 / 2.993546349981601 | [NPY](tensors/0001622.npy) |
| 1623 | `model.layers.23.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.0 / 8.25 / 0.021622725733323023 / 1.193834674899954 | [NPY](tensors/0001623.npy) |
| 1624 | `model.layers.23.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5056.0 / 5280.0 / 5.219364537133111 / 220.12888277178732 | [NPY](tensors/0001624.npy) |
| 1625 | `model.layers.23.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5056.0 / 5280.0 / 5.219364537133111 / 220.12888277178732 | [NPY](tensors/0001625.npy) |
| 1626 | `model.layers.23.self_attn` | 13 | `output[1]` | [1, 64, 1, 334] | torch.bfloat16 → float32 | 6.716849298982197e-15 / 0.875 / 0.0018802771809547814 / 0.01162708453330923 | [NPY](tensors/0001626.npy) |
| 1627 | `model.layers.23.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 9920.0 / 10.604380967881944 / 545.6954421010774 | [NPY](tensors/0001627.npy) |
| 1628 | `model.layers.23.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 8.3125 / 0.005397915674580468 / 1.1069572171299276 | [NPY](tensors/0001628.npy) |
| 1629 | `model.layers.23.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 8.3125 / 0.005397915674580468 / 1.1069572171299276 | [NPY](tensors/0001629.npy) |
| 1630 | `model.layers.23.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.75 / 8.3125 / 0.005397915674580468 / 1.1069572171299276 | [NPY](tensors/0001630.npy) |
| 1631 | `model.layers.23.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1632 | `model.layers.23.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1633 | `model.layers.23.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1634 | `model.layers.23.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1208.0 / 956.0 / -1.6017804357740615 / 76.43996958080426 | [NPY](tensors/0001634.npy) |
| 1635 | `model.layers.23.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1208.0 / 956.0 / -1.6017804357740615 / 76.43996958080426 | [NPY](tensors/0001635.npy) |
| 1636 | `model.layers.23.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.375 / 1.328125 / 0.12439727783203125 / 0.6081153578353877 | [NPY](tensors/0001636.npy) |
| 1637 | `model.layers.23` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9728.0 / 9.030479600694445 / 535.2443024633533 | [NPY](tensors/0001637.npy) |
| 1716 | `model.layers.23` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12992.0 / 12544.0 / -3.241501193576389 / 552.2794673097906 | [NPY](tensors/0001716.npy) |
| 1717 | `model.layers.23` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 335] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001717.npy) |
| 1718 | `model.layers.23` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0001718.npy) |
| 1719 | `model.layers.23` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0001719.npy) |
| 1720 | `model.layers.23` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0001720.npy) |
| 1721 | `model.layers.23` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1722 | `model.layers.23` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1723 | `model.layers.23` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1724 | `model.layers.23.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12992.0 / 12544.0 / -3.241501193576389 / 552.2794673097906 | [NPY](tensors/0001724.npy) |
| 1725 | `model.layers.23.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 61.0 / 0.004792851871914334 / 1.7918350045538272 | [NPY](tensors/0001725.npy) |
| 1726 | `model.layers.23.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 61.0 / 0.004792851871914334 / 1.7918350045538272 | [NPY](tensors/0001726.npy) |
| 1727 | `model.layers.23.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 335] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001727.npy) |
| 1728 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0001728.npy) |
| 1729 | `model.layers.23.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1730 | `model.layers.23.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1731 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0001731.npy) |
| 1732 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0001732.npy) |
| 1733 | `model.layers.23.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1734 | `model.layers.23.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 61.0 / 0.004792851871914334 / 1.7918350045538272 | [NPY](tensors/0001734.npy) |
| 1735 | `model.layers.23.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.3125 / 14.8125 / 0.03117693989770487 / 1.3079108908931625 | [NPY](tensors/0001735.npy) |
| 1736 | `model.layers.23.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 61.0 / 0.004792851871914334 / 1.7918350045538272 | [NPY](tensors/0001736.npy) |
| 1737 | `model.layers.23.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.25 / 44.5 / -0.05797840282320976 / 4.47501790774379 | [NPY](tensors/0001737.npy) |
| 1738 | `model.layers.23.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 61.0 / 0.004792851871914334 / 1.7918350045538272 | [NPY](tensors/0001738.npy) |
| 1739 | `model.layers.23.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.875 / 8.625 / 0.07545578479766846 / 2.525807627244047 | [NPY](tensors/0001739.npy) |
| 1740 | `model.layers.23.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.0625 / 7.0 / 0.028045080369338393 / 1.0547854200522055 | [NPY](tensors/0001740.npy) |
| 1741 | `model.layers.23.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4480.0 / 4640.0 / 4.5956051932440865 / 194.04425443709542 | [NPY](tensors/0001741.npy) |
| 1742 | `model.layers.23.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4480.0 / 4640.0 / 4.5956051932440865 / 194.04425443709542 | [NPY](tensors/0001742.npy) |
| 1743 | `model.layers.23.self_attn` | 14 | `output[1]` | [1, 64, 1, 335] | torch.bfloat16 → float32 | 4.6074255521944e-15 / 0.7734375 / 0.001552286619345298 / 0.011275128334001369 | [NPY](tensors/0001743.npy) |
| 1744 | `model.layers.23.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12416.0 / 11904.0 / 1.3585367838541667 / 584.4972385356825 | [NPY](tensors/0001744.npy) |
| 1745 | `model.layers.23.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 7.0 / -0.01111737224790785 / 1.1414756770122854 | [NPY](tensors/0001745.npy) |
| 1746 | `model.layers.23.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 7.0 / -0.01111737224790785 / 1.1414756770122854 | [NPY](tensors/0001746.npy) |
| 1747 | `model.layers.23.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.0 / 7.0 / -0.01111737224790785 / 1.1414756770122854 | [NPY](tensors/0001747.npy) |
| 1748 | `model.layers.23.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1749 | `model.layers.23.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1750 | `model.layers.23.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1751 | `model.layers.23.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2976.0 / 2928.0 / -2.6479181501600477 / 175.65763306543107 | [NPY](tensors/0001751.npy) |
| 1752 | `model.layers.23.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2976.0 / 2928.0 / -2.6479181501600477 / 175.65763306543107 | [NPY](tensors/0001752.npy) |
| 1753 | `model.layers.23.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.109375 / 1.5625 / -0.046970367431640625 / 0.7832790696659409 | [NPY](tensors/0001753.npy) |
| 1754 | `model.layers.23` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9472.0 / 9280.0 / -1.2914171006944444 / 475.28050896389436 | [NPY](tensors/0001754.npy) |
| 1833 | `model.layers.23` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11072.0 / 10176.0 / -7.163723415798611 / 509.28270370837754 | [NPY](tensors/0001833.npy) |
| 1834 | `model.layers.23` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 336] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001834.npy) |
| 1835 | `model.layers.23` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0001835.npy) |
| 1836 | `model.layers.23` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0001836.npy) |
| 1837 | `model.layers.23` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0001837.npy) |
| 1838 | `model.layers.23` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1839 | `model.layers.23` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1840 | `model.layers.23` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1841 | `model.layers.23.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11072.0 / 10176.0 / -7.163723415798611 / 509.28270370837754 | [NPY](tensors/0001841.npy) |
| 1842 | `model.layers.23.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 53.75 / -0.008367484145694309 / 1.7120500683164204 | [NPY](tensors/0001842.npy) |
| 1843 | `model.layers.23.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 53.75 / -0.008367484145694309 / 1.7120500683164204 | [NPY](tensors/0001843.npy) |
| 1844 | `model.layers.23.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 336] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001844.npy) |
| 1845 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0001845.npy) |
| 1846 | `model.layers.23.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1847 | `model.layers.23.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1848 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0001848.npy) |
| 1849 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0001849.npy) |
| 1850 | `model.layers.23.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1851 | `model.layers.23.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 53.75 / -0.008367484145694309 / 1.7120500683164204 | [NPY](tensors/0001851.npy) |
| 1852 | `model.layers.23.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.8125 / 19.125 / 0.018446881789714098 / 1.397743351955164 | [NPY](tensors/0001852.npy) |
| 1853 | `model.layers.23.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 53.75 / -0.008367484145694309 / 1.7120500683164204 | [NPY](tensors/0001853.npy) |
| 1854 | `model.layers.23.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -63.75 / 48.75 / -0.10957769677042961 / 5.560428721908967 | [NPY](tensors/0001854.npy) |
| 1855 | `model.layers.23.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 53.75 / -0.008367484145694309 / 1.7120500683164204 | [NPY](tensors/0001855.npy) |
| 1856 | `model.layers.23.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.375 / 15.1875 / 0.2929871082305908 / 4.021711799808733 | [NPY](tensors/0001856.npy) |
| 1857 | `model.layers.23.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.625 / 7.78125 / 0.016603041265625507 / 1.0762523771643455 | [NPY](tensors/0001857.npy) |
| 1858 | `model.layers.23.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5536.0 / 5760.0 / 5.839795706007216 / 242.81206388262103 | [NPY](tensors/0001858.npy) |
| 1859 | `model.layers.23.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5536.0 / 5760.0 / 5.839795706007216 / 242.81206388262103 | [NPY](tensors/0001859.npy) |
| 1860 | `model.layers.23.self_attn` | 15 | `output[1]` | [1, 64, 1, 336] | torch.bfloat16 → float32 | 1.021405182655144e-14 / 0.8046875 / 0.001347627361109372 / 0.01069924987375286 | [NPY](tensors/0001860.npy) |
| 1861 | `model.layers.23.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11072.0 / 10240.0 / -1.3353108723958333 / 589.3755161221827 | [NPY](tensors/0001861.npy) |
| 1862 | `model.layers.23.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 7.0 / -0.02669042613771227 / 1.1475697211635254 | [NPY](tensors/0001862.npy) |
| 1863 | `model.layers.23.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 7.0 / -0.02669042613771227 / 1.1475697211635254 | [NPY](tensors/0001863.npy) |
| 1864 | `model.layers.23.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -40.0 / 7.0 / -0.02669042613771227 / 1.1475697211635254 | [NPY](tensors/0001864.npy) |
| 1865 | `model.layers.23.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1866 | `model.layers.23.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1867 | `model.layers.23.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1868 | `model.layers.23.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3168.0 / 2976.0 / -1.5725257873535157 / 175.5772697777114 | [NPY](tensors/0001868.npy) |
| 1869 | `model.layers.23.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3168.0 / 2976.0 / -1.5725257873535157 / 175.5772697777114 | [NPY](tensors/0001869.npy) |
| 1870 | `model.layers.23.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.15625 / 1.328125 / 0.014535903930664062 / 0.8031892384168172 | [NPY](tensors/0001870.npy) |
| 1871 | `model.layers.23` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8096.0 / 7232.0 / -2.9143364800347222 / 457.59503583854035 | [NPY](tensors/0001871.npy) |
| 1950 | `model.layers.23` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 10240.0 / -10.738761393229167 / 525.1614830354702 | [NPY](tensors/0001950.npy) |
| 1951 | `model.layers.23` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 337] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001951.npy) |
| 1952 | `model.layers.23` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0001952.npy) |
| 1953 | `model.layers.23` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0001953.npy) |
| 1954 | `model.layers.23` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0001954.npy) |
| 1955 | `model.layers.23` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1956 | `model.layers.23` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1957 | `model.layers.23` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1958 | `model.layers.23.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 10240.0 / -10.738761393229167 / 525.1614830354702 | [NPY](tensors/0001958.npy) |
| 1959 | `model.layers.23.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 46.5 / -0.016082767645517984 / 1.6514874395440828 | [NPY](tensors/0001959.npy) |
| 1960 | `model.layers.23.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 46.5 / -0.016082767645517984 / 1.6514874395440828 | [NPY](tensors/0001960.npy) |
| 1961 | `model.layers.23.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 337] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001961.npy) |
| 1962 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0001962.npy) |
| 1963 | `model.layers.23.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1964 | `model.layers.23.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1965 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0001965.npy) |
| 1966 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0001966.npy) |
| 1967 | `model.layers.23.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1968 | `model.layers.23.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 46.5 / -0.016082767645517984 / 1.6514874395440828 | [NPY](tensors/0001968.npy) |
| 1969 | `model.layers.23.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.8125 / 16.125 / 0.030484001617878675 / 1.4681423797876871 | [NPY](tensors/0001969.npy) |
| 1970 | `model.layers.23.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 46.5 / -0.016082767645517984 / 1.6514874395440828 | [NPY](tensors/0001970.npy) |
| 1971 | `model.layers.23.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -69.0 / 57.25 / -0.06350638717412949 / 5.623769901251561 | [NPY](tensors/0001971.npy) |
| 1972 | `model.layers.23.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 46.5 / -0.016082767645517984 / 1.6514874395440828 | [NPY](tensors/0001972.npy) |
| 1973 | `model.layers.23.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -12.0 / 10.8125 / -0.046118587255477905 / 3.549205669010706 | [NPY](tensors/0001973.npy) |
| 1974 | `model.layers.23.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.1875 / 8.6875 / 0.028860407415777445 / 1.0007397051112283 | [NPY](tensors/0001974.npy) |
| 1975 | `model.layers.23.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3904.0 / 4128.0 / 3.032571072048611 / 173.64858598110757 | [NPY](tensors/0001975.npy) |
| 1976 | `model.layers.23.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3904.0 / 4128.0 / 3.032571072048611 / 173.64858598110757 | [NPY](tensors/0001976.npy) |
| 1977 | `model.layers.23.self_attn` | 16 | `output[1]` | [1, 64, 1, 337] | torch.bfloat16 → float32 | 7.860379014346108e-14 / 0.578125 / 0.0010849304098842177 / 0.010193250057799988 | [NPY](tensors/0001977.npy) |
| 1978 | `model.layers.23.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 10048.0 / -7.715467664930555 / 560.4092989932727 | [NPY](tensors/0001978.npy) |
| 1979 | `model.layers.23.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 9.375 / -0.0392453047964308 / 1.4184085733662937 | [NPY](tensors/0001979.npy) |
| 1980 | `model.layers.23.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 9.375 / -0.0392453047964308 / 1.4184085733662937 | [NPY](tensors/0001980.npy) |
| 1981 | `model.layers.23.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -45.5 / 9.375 / -0.0392453047964308 / 1.4184085733662937 | [NPY](tensors/0001981.npy) |
| 1982 | `model.layers.23.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1983 | `model.layers.23.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1984 | `model.layers.23.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1985 | `model.layers.23.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4288.0 / 4736.0 / -1.656560516357422 / 284.645999150036 | [NPY](tensors/0001985.npy) |
| 1986 | `model.layers.23.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4288.0 / 4736.0 / -1.656560516357422 / 284.645999150036 | [NPY](tensors/0001986.npy) |
| 1987 | `model.layers.23.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.34375 / 2.21875 / -0.0319366455078125 / 1.0253413252105275 | [NPY](tensors/0001987.npy) |
| 1988 | `model.layers.23` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10816.0 / 10176.0 / -9.389800347222222 / 696.2897471985088 | [NPY](tensors/0001988.npy) |
| 2067 | `model.layers.23` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 10496.0 / -5.242195638020833 / 498.19909221340237 | [NPY](tensors/0002067.npy) |
| 2068 | `model.layers.23` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 338] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002068.npy) |
| 2069 | `model.layers.23` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0002069.npy) |
| 2070 | `model.layers.23` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0002070.npy) |
| 2071 | `model.layers.23` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0002071.npy) |
| 2072 | `model.layers.23` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2073 | `model.layers.23` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2074 | `model.layers.23` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2075 | `model.layers.23.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 10496.0 / -5.242195638020833 / 498.19909221340237 | [NPY](tensors/0002075.npy) |
| 2076 | `model.layers.23.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.5 / -0.00395709408654107 / 1.727501842697064 | [NPY](tensors/0002076.npy) |
| 2077 | `model.layers.23.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.5 / -0.00395709408654107 / 1.727501842697064 | [NPY](tensors/0002077.npy) |
| 2078 | `model.layers.23.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 338] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002078.npy) |
| 2079 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0002079.npy) |
| 2080 | `model.layers.23.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2081 | `model.layers.23.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2082 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0002082.npy) |
| 2083 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0002083.npy) |
| 2084 | `model.layers.23.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2085 | `model.layers.23.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.5 / -0.00395709408654107 / 1.727501842697064 | [NPY](tensors/0002085.npy) |
| 2086 | `model.layers.23.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.3125 / 19.75 / 0.02726741664810106 / 1.575149908364751 | [NPY](tensors/0002086.npy) |
| 2087 | `model.layers.23.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.5 / -0.00395709408654107 / 1.727501842697064 | [NPY](tensors/0002087.npy) |
| 2088 | `model.layers.23.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -55.5 / 46.25 / -0.011638596653938293 / 4.947742282221608 | [NPY](tensors/0002088.npy) |
| 2089 | `model.layers.23.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.5 / -0.00395709408654107 / 1.727501842697064 | [NPY](tensors/0002089.npy) |
| 2090 | `model.layers.23.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.5 / 11.8125 / -0.24583005905151367 / 3.8803154770717003 | [NPY](tensors/0002090.npy) |
| 2091 | `model.layers.23.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.5 / 8.6875 / 0.0019591745804063976 / 1.3525538401854178 | [NPY](tensors/0002091.npy) |
| 2092 | `model.layers.23.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5376.0 / 5568.0 / 4.116904025607639 / 246.44866388223647 | [NPY](tensors/0002092.npy) |
| 2093 | `model.layers.23.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5376.0 / 5568.0 / 4.116904025607639 / 246.44866388223647 | [NPY](tensors/0002093.npy) |
| 2094 | `model.layers.23.self_attn` | 17 | `output[1]` | [1, 64, 1, 338] | torch.bfloat16 → float32 | 2.5396351688300456e-15 / 0.8984375 / 0.0014477155607732573 / 0.014130716546132072 | [NPY](tensors/0002094.npy) |
| 2095 | `model.layers.23.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 10496.0 / -1.1234320746527777 / 572.038711958488 | [NPY](tensors/0002095.npy) |
| 2096 | `model.layers.23.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.25 / 8.3125 / -0.024602735704845852 / 1.1783870001778114 | [NPY](tensors/0002096.npy) |
| 2097 | `model.layers.23.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.25 / 8.3125 / -0.024602735704845852 / 1.1783870001778114 | [NPY](tensors/0002097.npy) |
| 2098 | `model.layers.23.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.25 / 8.3125 / -0.024602735704845852 / 1.1783870001778114 | [NPY](tensors/0002098.npy) |
| 2099 | `model.layers.23.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2100 | `model.layers.23.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2101 | `model.layers.23.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2102 | `model.layers.23.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2352.0 / 2288.0 / -2.338893763224284 / 146.04429593751502 | [NPY](tensors/0002102.npy) |
| 2103 | `model.layers.23.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2352.0 / 2288.0 / -2.338893763224284 / 146.04429593751502 | [NPY](tensors/0002103.npy) |
| 2104 | `model.layers.23.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9453125 / 1.453125 / 0.0385284423828125 / 0.7178640488437298 | [NPY](tensors/0002104.npy) |
| 2105 | `model.layers.23` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8000.0 / 8128.0 / -3.4813774956597223 / 500.38489780139383 | [NPY](tensors/0002105.npy) |
| 2184 | `model.layers.23` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10752.0 / 9664.0 / -7.573480902777778 / 445.5461332639071 | [NPY](tensors/0002184.npy) |
| 2185 | `model.layers.23` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 339] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002185.npy) |
| 2186 | `model.layers.23` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0002186.npy) |
| 2187 | `model.layers.23` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0002187.npy) |
| 2188 | `model.layers.23` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0002188.npy) |
| 2189 | `model.layers.23` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2190 | `model.layers.23` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2191 | `model.layers.23` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2192 | `model.layers.23.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10752.0 / 9664.0 / -7.573480902777778 / 445.5461332639071 | [NPY](tensors/0002192.npy) |
| 2193 | `model.layers.23.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.0 / 58.25 / -0.010412389039993286 / 1.7887738901307795 | [NPY](tensors/0002193.npy) |
| 2194 | `model.layers.23.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.0 / 58.25 / -0.010412389039993286 / 1.7887738901307795 | [NPY](tensors/0002194.npy) |
| 2195 | `model.layers.23.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 339] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002195.npy) |
| 2196 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0002196.npy) |
| 2197 | `model.layers.23.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2198 | `model.layers.23.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2199 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0002199.npy) |
| 2200 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0002200.npy) |
| 2201 | `model.layers.23.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2202 | `model.layers.23.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.0 / 58.25 / -0.010412389039993286 / 1.7887738901307795 | [NPY](tensors/0002202.npy) |
| 2203 | `model.layers.23.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 14.125 / 0.034480118192732334 / 1.4340092160653815 | [NPY](tensors/0002203.npy) |
| 2204 | `model.layers.23.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.0 / 58.25 / -0.010412389039993286 / 1.7887738901307795 | [NPY](tensors/0002204.npy) |
| 2205 | `model.layers.23.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.0 / 52.75 / -0.0730484165251255 / 5.528936462900288 | [NPY](tensors/0002205.npy) |
| 2206 | `model.layers.23.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.0 / 58.25 / -0.010412389039993286 / 1.7887738901307795 | [NPY](tensors/0002206.npy) |
| 2207 | `model.layers.23.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.875 / 6.6875 / 0.03772926330566406 / 2.376028816597677 | [NPY](tensors/0002207.npy) |
| 2208 | `model.layers.23.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -18.125 / 7.375 / -0.014061756432056427 / 1.3545787540801195 | [NPY](tensors/0002208.npy) |
| 2209 | `model.layers.23.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5728.0 / 5888.0 / 5.150529310438368 / 254.9758802859678 | [NPY](tensors/0002209.npy) |
| 2210 | `model.layers.23.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5728.0 / 5888.0 / 5.150529310438368 / 254.9758802859678 | [NPY](tensors/0002210.npy) |
| 2211 | `model.layers.23.self_attn` | 18 | `output[1]` | [1, 64, 1, 339] | torch.bfloat16 → float32 | 6.972200594645983e-14 / 0.9609375 / 0.00219206073061669 / 0.011690238811701772 | [NPY](tensors/0002211.npy) |
| 2212 | `model.layers.23.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10944.0 / 9600.0 / -2.440166558159722 / 538.0919378841377 | [NPY](tensors/0002212.npy) |
| 2213 | `model.layers.23.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.25 / 8.1875 / -0.02881525225109524 / 0.9555565198223516 | [NPY](tensors/0002213.npy) |
| 2214 | `model.layers.23.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.25 / 8.1875 / -0.02881525225109524 / 0.9555565198223516 | [NPY](tensors/0002214.npy) |
| 2215 | `model.layers.23.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -26.25 / 8.1875 / -0.02881525225109524 / 0.9555565198223516 | [NPY](tensors/0002215.npy) |
| 2216 | `model.layers.23.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2217 | `model.layers.23.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2218 | `model.layers.23.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2219 | `model.layers.23.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -920.0 / 856.0 / -2.0201935874091252 / 67.61616095136452 | [NPY](tensors/0002219.npy) |
| 2220 | `model.layers.23.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -920.0 / 856.0 / -2.0201935874091252 / 67.61616095136452 | [NPY](tensors/0002220.npy) |
| 2221 | `model.layers.23.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.625 / 1.1796875 / 0.020442962646484375 / 0.43100012858765735 | [NPY](tensors/0002221.npy) |
| 2222 | `model.layers.23` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10176.0 / 8960.0 / -4.436187065972222 / 507.3208121566851 | [NPY](tensors/0002222.npy) |
| 2301 | `model.layers.23` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9984.0 / -5.107931857638889 / 419.9227293100293 | [NPY](tensors/0002301.npy) |
| 2302 | `model.layers.23` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 340] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002302.npy) |
| 2303 | `model.layers.23` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0002303.npy) |
| 2304 | `model.layers.23` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0002304.npy) |
| 2305 | `model.layers.23` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0002305.npy) |
| 2306 | `model.layers.23` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2307 | `model.layers.23` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2308 | `model.layers.23` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2309 | `model.layers.23.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9984.0 / -5.107931857638889 / 419.9227293100293 | [NPY](tensors/0002309.npy) |
| 2310 | `model.layers.23.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 64.0 / 0.0012472563319736057 / 1.8204592624563773 | [NPY](tensors/0002310.npy) |
| 2311 | `model.layers.23.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 64.0 / 0.0012472563319736057 / 1.8204592624563773 | [NPY](tensors/0002311.npy) |
| 2312 | `model.layers.23.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 340] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002312.npy) |
| 2313 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0002313.npy) |
| 2314 | `model.layers.23.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2315 | `model.layers.23.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2316 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0002316.npy) |
| 2317 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0002317.npy) |
| 2318 | `model.layers.23.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2319 | `model.layers.23.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 64.0 / 0.0012472563319736057 / 1.8204592624563773 | [NPY](tensors/0002319.npy) |
| 2320 | `model.layers.23.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.375 / 16.0 / 0.03715425234986469 / 1.5251755592477136 | [NPY](tensors/0002320.npy) |
| 2321 | `model.layers.23.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 64.0 / 0.0012472563319736057 / 1.8204592624563773 | [NPY](tensors/0002321.npy) |
| 2322 | `model.layers.23.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.75 / 40.25 / -0.11466890573501587 / 4.806331236094726 | [NPY](tensors/0002322.npy) |
| 2323 | `model.layers.23.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 64.0 / 0.0012472563319736057 / 1.8204592624563773 | [NPY](tensors/0002323.npy) |
| 2324 | `model.layers.23.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.5 / 14.375 / 0.2454283908009529 / 3.717228395820907 | [NPY](tensors/0002324.npy) |
| 2325 | `model.layers.23.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.1875 / 7.90625 / 0.0670133656822145 / 1.323285071627313 | [NPY](tensors/0002325.npy) |
| 2326 | `model.layers.23.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3600.0 / 3600.0 / 1.9959845066070556 / 169.31242104121003 | [NPY](tensors/0002326.npy) |
| 2327 | `model.layers.23.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3600.0 / 3600.0 / 1.9959845066070556 / 169.31242104121003 | [NPY](tensors/0002327.npy) |
| 2328 | `model.layers.23.self_attn` | 19 | `output[1]` | [1, 64, 1, 340] | torch.bfloat16 → float32 | 4.524158825347513e-15 / 0.97265625 / 0.0021727588721001064 / 0.016012607337516235 | [NPY](tensors/0002328.npy) |
| 2329 | `model.layers.23.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7840.0 / 8064.0 / -3.0929090711805554 / 402.7277110861896 | [NPY](tensors/0002329.npy) |
| 2330 | `model.layers.23.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.25 / 6.5625 / -0.032597451739841035 / 1.0688338635101322 | [NPY](tensors/0002330.npy) |
| 2331 | `model.layers.23.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.25 / 6.5625 / -0.032597451739841035 / 1.0688338635101322 | [NPY](tensors/0002331.npy) |
| 2332 | `model.layers.23.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -28.25 / 6.5625 / -0.032597451739841035 / 1.0688338635101322 | [NPY](tensors/0002332.npy) |
| 2333 | `model.layers.23.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2334 | `model.layers.23.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2335 | `model.layers.23.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2336 | `model.layers.23.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3296.0 / 3104.0 / -1.4343155754937067 / 157.40505610652548 | [NPY](tensors/0002336.npy) |
| 2337 | `model.layers.23.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3296.0 / 3104.0 / -1.4343155754937067 / 157.40505610652548 | [NPY](tensors/0002337.npy) |
| 2338 | `model.layers.23.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8359375 / 0.92578125 / -0.05535316467285156 / 0.6920512467729649 | [NPY](tensors/0002338.npy) |
| 2339 | `model.layers.23` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4736.0 / 4768.0 / -4.519802517361111 / 303.6970935185094 | [NPY](tensors/0002339.npy) |
| 2418 | `model.layers.23` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 9152.0 / -3.274941677517361 / 402.1702295882608 | [NPY](tensors/0002418.npy) |
| 2419 | `model.layers.23` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 341] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002419.npy) |
| 2420 | `model.layers.23` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.34375 / 0.7532014846801758 / 0.8246045706539666 | [NPY](tensors/0002420.npy) |
| 2421 | `model.layers.23` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.03213447332382202 / 0.7489573739100013 | [NPY](tensors/0002421.npy) |
| 2422 | `model.layers.23` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 340.0 / 340.0 / 340.0 / 0.0 | [NPY](tensors/0002422.npy) |
| 2423 | `model.layers.23` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2424 | `model.layers.23` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2425 | `model.layers.23` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2426 | `model.layers.23.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 9152.0 / -3.274941677517361 / 402.1702295882608 | [NPY](tensors/0002426.npy) |
| 2427 | `model.layers.23.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 61.25 / 0.009607504473792182 / 1.8140435074201644 | [NPY](tensors/0002427.npy) |
| 2428 | `model.layers.23.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 61.25 / 0.009607504473792182 / 1.8140435074201644 | [NPY](tensors/0002428.npy) |
| 2429 | `model.layers.23.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 341] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002429.npy) |
| 2430 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 340.0 / 340.0 / 340.0 / 0.0 | [NPY](tensors/0002430.npy) |
| 2431 | `model.layers.23.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2432 | `model.layers.23.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2433 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.34375 / 0.7532014846801758 / 0.8246045706539666 | [NPY](tensors/0002433.npy) |
| 2434 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.03213447332382202 / 0.7489573739100013 | [NPY](tensors/0002434.npy) |
| 2435 | `model.layers.23.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2436 | `model.layers.23.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 61.25 / 0.009607504473792182 / 1.8140435074201644 | [NPY](tensors/0002436.npy) |
| 2437 | `model.layers.23.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.0625 / 15.3125 / 0.03998084936756641 / 1.6403072446768148 | [NPY](tensors/0002437.npy) |
| 2438 | `model.layers.23.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 61.25 / 0.009607504473792182 / 1.8140435074201644 | [NPY](tensors/0002438.npy) |
| 2439 | `model.layers.23.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -46.5 / 29.75 / -0.13596419990062714 / 4.7232317995371815 | [NPY](tensors/0002439.npy) |
| 2440 | `model.layers.23.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 61.25 / 0.009607504473792182 / 1.8140435074201644 | [NPY](tensors/0002440.npy) |
| 2441 | `model.layers.23.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.5625 / 17.625 / 0.15252947807312012 / 4.513127374785653 | [NPY](tensors/0002441.npy) |
| 2442 | `model.layers.23.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.4375 / 8.9375 / 0.06840934813953936 / 1.3044881809354538 | [NPY](tensors/0002442.npy) |
| 2443 | `model.layers.23.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2896.0 / 2816.0 / 1.1850333319769966 / 140.64742962043837 | [NPY](tensors/0002443.npy) |
| 2444 | `model.layers.23.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2896.0 / 2816.0 / 1.1850333319769966 / 140.64742962043837 | [NPY](tensors/0002444.npy) |
| 2445 | `model.layers.23.self_attn` | 20 | `output[1]` | [1, 64, 1, 341] | torch.bfloat16 → float32 | 7.904787935331115e-14 / 0.95703125 / 0.0018758248202283936 / 0.013667392720333044 | [NPY](tensors/0002445.npy) |
| 2446 | `model.layers.23.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7552.0 / 7552.0 / -2.096728515625 / 374.8958178008097 | [NPY](tensors/0002446.npy) |
| 2447 | `model.layers.23.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.625 / 10.1875 / -0.030117777983347575 / 1.153038497457966 | [NPY](tensors/0002447.npy) |
| 2448 | `model.layers.23.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.625 / 10.1875 / -0.030117777983347575 / 1.153038497457966 | [NPY](tensors/0002448.npy) |
| 2449 | `model.layers.23.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -30.625 / 10.1875 / -0.030117777983347575 / 1.153038497457966 | [NPY](tensors/0002449.npy) |
| 2450 | `model.layers.23.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2451 | `model.layers.23.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2452 | `model.layers.23.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2453 | `model.layers.23.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5024.0 / 4640.0 / -1.2834614435831706 / 228.79966728380347 | [NPY](tensors/0002453.npy) |
| 2454 | `model.layers.23.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5024.0 / 4640.0 / -1.2834614435831706 / 228.79966728380347 | [NPY](tensors/0002454.npy) |
| 2455 | `model.layers.23.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.828125 / 1.140625 / -0.14319610595703125 / 0.8891190126765117 | [NPY](tensors/0002455.npy) |
| 2456 | `model.layers.23` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2912.0 / 2560.0 / -3.3826605902777778 / 247.3396830724326 | [NPY](tensors/0002456.npy) |
| 2535 | `model.layers.23` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10048.0 / -5.155948893229167 / 448.67021133730464 | [NPY](tensors/0002535.npy) |
| 2536 | `model.layers.23` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 342] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002536.npy) |
| 2537 | `model.layers.23` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.7198410034179688 / 0.8503804730267482 | [NPY](tensors/0002537.npy) |
| 2538 | `model.layers.23` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.027828902006149292 / 0.7525043584225227 | [NPY](tensors/0002538.npy) |
| 2539 | `model.layers.23` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 341.0 / 341.0 / 341.0 / 0.0 | [NPY](tensors/0002539.npy) |
| 2540 | `model.layers.23` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2541 | `model.layers.23` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2542 | `model.layers.23` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2543 | `model.layers.23.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10048.0 / -5.155948893229167 / 448.67021133730464 | [NPY](tensors/0002543.npy) |
| 2544 | `model.layers.23.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 57.0 / 0.0026978280809190538 / 1.7825832000912958 | [NPY](tensors/0002544.npy) |
| 2545 | `model.layers.23.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 57.0 / 0.0026978280809190538 / 1.7825832000912958 | [NPY](tensors/0002545.npy) |
| 2546 | `model.layers.23.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 342] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002546.npy) |
| 2547 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 341.0 / 341.0 / 341.0 / 0.0 | [NPY](tensors/0002547.npy) |
| 2548 | `model.layers.23.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2549 | `model.layers.23.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2550 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.7198410034179688 / 0.8503804730267482 | [NPY](tensors/0002550.npy) |
| 2551 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.027828902006149292 / 0.7525043584225227 | [NPY](tensors/0002551.npy) |
| 2552 | `model.layers.23.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2553 | `model.layers.23.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 57.0 / 0.0026978280809190538 / 1.7825832000912958 | [NPY](tensors/0002553.npy) |
| 2554 | `model.layers.23.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.5 / 14.875 / 0.030364185833605006 / 1.5932611575338484 | [NPY](tensors/0002554.npy) |
| 2555 | `model.layers.23.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 57.0 / 0.0026978280809190538 / 1.7825832000912958 | [NPY](tensors/0002555.npy) |
| 2556 | `model.layers.23.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.875 / 33.0 / -0.06474744342267513 / 4.652570229805721 | [NPY](tensors/0002556.npy) |
| 2557 | `model.layers.23.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 57.0 / 0.0026978280809190538 / 1.7825832000912958 | [NPY](tensors/0002557.npy) |
| 2558 | `model.layers.23.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.125 / 11.625 / -0.03420817852020264 / 3.8278157645139093 | [NPY](tensors/0002558.npy) |
| 2559 | `model.layers.23.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.75 / 8.125 / 0.09822180913761258 / 1.4811266950942694 | [NPY](tensors/0002559.npy) |
| 2560 | `model.layers.23.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3280.0 / 3136.0 / 1.2656075795491537 / 153.89567686681323 | [NPY](tensors/0002560.npy) |
| 2561 | `model.layers.23.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3280.0 / 3136.0 / 1.2656075795491537 / 153.89567686681323 | [NPY](tensors/0002561.npy) |
| 2562 | `model.layers.23.self_attn` | 21 | `output[1]` | [1, 64, 1, 342] | torch.bfloat16 → float32 | 3.9612757518625585e-13 / 0.9453125 / 0.002361112866410795 / 0.01509169642859475 | [NPY](tensors/0002562.npy) |
| 2563 | `model.layers.23.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 8832.0 / -3.905373806423611 / 436.18658120184534 | [NPY](tensors/0002563.npy) |
| 2564 | `model.layers.23.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.75 / 7.9375 / -0.03513630363676283 / 1.120620643334244 | [NPY](tensors/0002564.npy) |
| 2565 | `model.layers.23.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.75 / 7.9375 / -0.03513630363676283 / 1.120620643334244 | [NPY](tensors/0002565.npy) |
| 2566 | `model.layers.23.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -28.75 / 7.9375 / -0.03513630363676283 / 1.120620643334244 | [NPY](tensors/0002566.npy) |
| 2567 | `model.layers.23.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2568 | `model.layers.23.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2569 | `model.layers.23.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2570 | `model.layers.23.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5984.0 / 5312.0 / -3.525172593858507 / 267.1594039129908 | [NPY](tensors/0002570.npy) |
| 2571 | `model.layers.23.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5984.0 / 5312.0 / -3.525172593858507 / 267.1594039129908 | [NPY](tensors/0002571.npy) |
| 2572 | `model.layers.23.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.0 / 1.140625 / -0.08195114135742188 / 0.7039868805098082 | [NPY](tensors/0002572.npy) |
| 2573 | `model.layers.23` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4128.0 / 3616.0 / -7.430826822916667 / 291.6538116642988 | [NPY](tensors/0002573.npy) |
| 2652 | `model.layers.23` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9024.0 / 9408.0 / -2.6223822699652777 / 420.5169263467736 | [NPY](tensors/0002652.npy) |
| 2653 | `model.layers.23` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 343] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002653.npy) |
| 2654 | `model.layers.23` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.70660400390625 / 0.91681783844784 | [NPY](tensors/0002654.npy) |
| 2655 | `model.layers.23` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / -0.014852643013000488 / 0.6845543139796254 | [NPY](tensors/0002655.npy) |
| 2656 | `model.layers.23` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 342.0 / 342.0 / 342.0 / 0.0 | [NPY](tensors/0002656.npy) |
| 2657 | `model.layers.23` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2658 | `model.layers.23` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2659 | `model.layers.23` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2660 | `model.layers.23.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9024.0 / 9408.0 / -2.6223822699652777 / 420.5169263467736 | [NPY](tensors/0002660.npy) |
| 2661 | `model.layers.23.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 60.0 / 0.009763827588823106 / 1.7860576049732246 | [NPY](tensors/0002661.npy) |
| 2662 | `model.layers.23.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 60.0 / 0.009763827588823106 / 1.7860576049732246 | [NPY](tensors/0002662.npy) |
| 2663 | `model.layers.23.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 343] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002663.npy) |
| 2664 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 342.0 / 342.0 / 342.0 / 0.0 | [NPY](tensors/0002664.npy) |
| 2665 | `model.layers.23.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2666 | `model.layers.23.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2667 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.70660400390625 / 0.91681783844784 | [NPY](tensors/0002667.npy) |
| 2668 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / -0.014852643013000488 / 0.6845543139796254 | [NPY](tensors/0002668.npy) |
| 2669 | `model.layers.23.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2670 | `model.layers.23.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 60.0 / 0.009763827588823106 / 1.7860576049732246 | [NPY](tensors/0002670.npy) |
| 2671 | `model.layers.23.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.3125 / 16.75 / 0.04761710774619132 / 1.614824176972836 | [NPY](tensors/0002671.npy) |
| 2672 | `model.layers.23.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 60.0 / 0.009763827588823106 / 1.7860576049732246 | [NPY](tensors/0002672.npy) |
| 2673 | `model.layers.23.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.75 / 41.0 / -0.11505192518234253 / 5.391513573629354 | [NPY](tensors/0002673.npy) |
| 2674 | `model.layers.23.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 60.0 / 0.009763827588823106 / 1.7860576049732246 | [NPY](tensors/0002674.npy) |
| 2675 | `model.layers.23.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.125 / 13.75 / -0.05488121509552002 / 4.204509546204672 | [NPY](tensors/0002675.npy) |
| 2676 | `model.layers.23.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.1875 / 7.875 / 0.05446749785915017 / 1.2429851562559693 | [NPY](tensors/0002676.npy) |
| 2677 | `model.layers.23.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2816.0 / 2768.0 / 1.375999959309896 / 137.19837642129204 | [NPY](tensors/0002677.npy) |
| 2678 | `model.layers.23.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2816.0 / 2768.0 / 1.375999959309896 / 137.19837642129204 | [NPY](tensors/0002678.npy) |
| 2679 | `model.layers.23.self_attn` | 22 | `output[1]` | [1, 64, 1, 343] | torch.bfloat16 → float32 | 2.5934809855243657e-13 / 0.90234375 / 0.0018565550214375282 / 0.012703915543255007 | [NPY](tensors/0002679.npy) |
| 2680 | `model.layers.23.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7520.0 / 7904.0 / -1.24801025390625 / 400.19107938116775 | [NPY](tensors/0002680.npy) |
| 2681 | `model.layers.23.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 9.875 / -0.021692336930169 / 1.2466273610785075 | [NPY](tensors/0002681.npy) |
| 2682 | `model.layers.23.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 9.875 / -0.021692336930169 / 1.2466273610785075 | [NPY](tensors/0002682.npy) |
| 2683 | `model.layers.23.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.0 / 9.875 / -0.021692336930169 / 1.2466273610785075 | [NPY](tensors/0002683.npy) |
| 2684 | `model.layers.23.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2685 | `model.layers.23.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2686 | `model.layers.23.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2687 | `model.layers.23.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4608.0 / 4480.0 / -0.0818388197157118 / 236.80049524837563 | [NPY](tensors/0002687.npy) |
| 2688 | `model.layers.23.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4608.0 / 4480.0 / -0.0818388197157118 / 236.80049524837563 | [NPY](tensors/0002688.npy) |
| 2689 | `model.layers.23.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.40625 / 2.1875 / -0.04056549072265625 / 1.1903612934104735 | [NPY](tensors/0002689.npy) |
| 2690 | `model.layers.23` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3296.0 / 3296.0 / -1.3164605034722223 / 294.7614979747542 | [NPY](tensors/0002690.npy) |
| 2769 | `model.layers.23` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9600.0 / -0.7391370985243055 / 448.12540270390605 | [NPY](tensors/0002769.npy) |
| 2770 | `model.layers.23` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 344] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002770.npy) |
| 2771 | `model.layers.23` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.740966796875 / 0.9022817549113021 | [NPY](tensors/0002771.npy) |
| 2772 | `model.layers.23` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3046875 / -0.06294980645179749 / 0.6646640154085409 | [NPY](tensors/0002772.npy) |
| 2773 | `model.layers.23` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 343.0 / 343.0 / 343.0 / 0.0 | [NPY](tensors/0002773.npy) |
| 2774 | `model.layers.23` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2775 | `model.layers.23` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2776 | `model.layers.23` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2777 | `model.layers.23.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9600.0 / -0.7391370985243055 / 448.12540270390605 | [NPY](tensors/0002777.npy) |
| 2778 | `model.layers.23.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 57.5 / 0.011738256613413493 / 1.7590352461570986 | [NPY](tensors/0002778.npy) |
| 2779 | `model.layers.23.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 57.5 / 0.011738256613413493 / 1.7590352461570986 | [NPY](tensors/0002779.npy) |
| 2780 | `model.layers.23.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 344] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002780.npy) |
| 2781 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 343.0 / 343.0 / 343.0 / 0.0 | [NPY](tensors/0002781.npy) |
| 2782 | `model.layers.23.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2783 | `model.layers.23.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2784 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.740966796875 / 0.9022817549113021 | [NPY](tensors/0002784.npy) |
| 2785 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3046875 / -0.06294980645179749 / 0.6646640154085409 | [NPY](tensors/0002785.npy) |
| 2786 | `model.layers.23.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2787 | `model.layers.23.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 57.5 / 0.011738256613413493 / 1.7590352461570986 | [NPY](tensors/0002787.npy) |
| 2788 | `model.layers.23.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.9375 / 17.125 / 0.0204666112549603 / 1.588043924433617 | [NPY](tensors/0002788.npy) |
| 2789 | `model.layers.23.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 57.5 / 0.011738256613413493 / 1.7590352461570986 | [NPY](tensors/0002789.npy) |
| 2790 | `model.layers.23.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.0 / 27.875 / 0.055185675621032715 / 4.387803018401589 | [NPY](tensors/0002790.npy) |
| 2791 | `model.layers.23.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 57.5 / 0.011738256613413493 / 1.7590352461570986 | [NPY](tensors/0002791.npy) |
| 2792 | `model.layers.23.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -11.4375 / 12.875 / 0.012843295931816101 / 3.443160569511099 | [NPY](tensors/0002792.npy) |
| 2793 | `model.layers.23.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.875 / 7.09375 / 0.05347430822439492 / 1.2427375323025471 | [NPY](tensors/0002793.npy) |
| 2794 | `model.layers.23.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3088.0 / 3120.0 / 2.701643541124132 / 156.9944620036202 | [NPY](tensors/0002794.npy) |
| 2795 | `model.layers.23.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3088.0 / 3120.0 / 2.701643541124132 / 156.9944620036202 | [NPY](tensors/0002795.npy) |
| 2796 | `model.layers.23.self_attn` | 23 | `output[1]` | [1, 64, 1, 344] | torch.bfloat16 → float32 | 8.562039965909207e-13 / 0.8515625 / 0.0020877159930798046 / 0.012209455955695048 | [NPY](tensors/0002796.npy) |
| 2797 | `model.layers.23.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8256.0 / 7744.0 / 1.969970703125 / 422.34123334387374 | [NPY](tensors/0002797.npy) |
| 2798 | `model.layers.23.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 7.0625 / -0.011832231945461697 / 1.1788256575065814 | [NPY](tensors/0002798.npy) |
| 2799 | `model.layers.23.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 7.0625 / -0.011832231945461697 / 1.1788256575065814 | [NPY](tensors/0002799.npy) |
| 2800 | `model.layers.23.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -30.125 / 7.0625 / -0.011832231945461697 / 1.1788256575065814 | [NPY](tensors/0002800.npy) |
| 2801 | `model.layers.23.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2802 | `model.layers.23.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2803 | `model.layers.23.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2804 | `model.layers.23.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5216.0 / 5024.0 / -1.050243123372396 / 257.99710627710874 | [NPY](tensors/0002804.npy) |
| 2805 | `model.layers.23.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5216.0 / 5024.0 / -1.050243123372396 / 257.99710627710874 | [NPY](tensors/0002805.npy) |
| 2806 | `model.layers.23.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.390625 / 1.140625 / 0.04768943786621094 / 0.8144502782099207 | [NPY](tensors/0002806.npy) |
| 2807 | `model.layers.23` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3360.0 / 2688.0 / 0.9272732204861112 / 290.37226758493995 | [NPY](tensors/0002807.npy) |
| 2886 | `model.layers.23` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10304.0 / -1.0471462673611112 / 468.09755571304225 | [NPY](tensors/0002886.npy) |
| 2887 | `model.layers.23` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 345] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002887.npy) |
| 2888 | `model.layers.23` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8131542205810547 / 0.8233916239555151 | [NPY](tensors/0002888.npy) |
| 2889 | `model.layers.23` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.07140964269638062 / 0.6820182328303498 | [NPY](tensors/0002889.npy) |
| 2890 | `model.layers.23` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 344.0 / 344.0 / 344.0 / 0.0 | [NPY](tensors/0002890.npy) |
| 2891 | `model.layers.23` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2892 | `model.layers.23` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2893 | `model.layers.23` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2894 | `model.layers.23.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10304.0 / -1.0471462673611112 / 468.09755571304225 | [NPY](tensors/0002894.npy) |
| 2895 | `model.layers.23.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 58.75 / 0.01232237418492635 / 1.7690921867440403 | [NPY](tensors/0002895.npy) |
| 2896 | `model.layers.23.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 58.75 / 0.01232237418492635 / 1.7690921867440403 | [NPY](tensors/0002896.npy) |
| 2897 | `model.layers.23.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 345] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002897.npy) |
| 2898 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 344.0 / 344.0 / 344.0 / 0.0 | [NPY](tensors/0002898.npy) |
| 2899 | `model.layers.23.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2900 | `model.layers.23.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2901 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8131542205810547 / 0.8233916239555151 | [NPY](tensors/0002901.npy) |
| 2902 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.07140964269638062 / 0.6820182328303498 | [NPY](tensors/0002902.npy) |
| 2903 | `model.layers.23.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2904 | `model.layers.23.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 58.75 / 0.01232237418492635 / 1.7690921867440403 | [NPY](tensors/0002904.npy) |
| 2905 | `model.layers.23.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.875 / 15.0 / 0.03566283290274441 / 1.5672391630296492 | [NPY](tensors/0002905.npy) |
| 2906 | `model.layers.23.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 58.75 / 0.01232237418492635 / 1.7690921867440403 | [NPY](tensors/0002906.npy) |
| 2907 | `model.layers.23.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.5 / 33.25 / -0.058607637882232666 / 4.48871651967895 | [NPY](tensors/0002907.npy) |
| 2908 | `model.layers.23.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 58.75 / 0.01232237418492635 / 1.7690921867440403 | [NPY](tensors/0002908.npy) |
| 2909 | `model.layers.23.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.625 / 8.8125 / -0.15051984414458275 / 2.865596784099654 | [NPY](tensors/0002909.npy) |
| 2910 | `model.layers.23.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.1875 / 5.625 / 0.02342667046468705 / 1.1004225670543681 | [NPY](tensors/0002910.npy) |
| 2911 | `model.layers.23.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2848.0 / 2816.0 / 2.115425173441569 / 141.5571044192172 | [NPY](tensors/0002911.npy) |
| 2912 | `model.layers.23.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2848.0 / 2816.0 / 2.115425173441569 / 141.5571044192172 | [NPY](tensors/0002912.npy) |
| 2913 | `model.layers.23.self_attn` | 24 | `output[1]` | [1, 64, 1, 345] | torch.bfloat16 → float32 | 1.0160761121369433e-12 / 0.890625 / 0.0019026136136689174 / 0.01142708960242861 | [NPY](tensors/0002913.npy) |
| 2914 | `model.layers.23.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 8640.0 / 1.0594590928819445 / 428.6528995936472 | [NPY](tensors/0002914.npy) |
| 2915 | `model.layers.23.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 5.15625 / -0.020418413480122886 / 1.2254502847563424 | [NPY](tensors/0002915.npy) |
| 2916 | `model.layers.23.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 5.15625 / -0.020418413480122886 / 1.2254502847563424 | [NPY](tensors/0002916.npy) |
| 2917 | `model.layers.23.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.0 / 5.15625 / -0.020418413480122886 / 1.2254502847563424 | [NPY](tensors/0002917.npy) |
| 2918 | `model.layers.23.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2919 | `model.layers.23.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2920 | `model.layers.23.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2921 | `model.layers.23.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3968.0 / 3824.0 / 0.7034878836737739 / 198.65685445631416 | [NPY](tensors/0002921.npy) |
| 2922 | `model.layers.23.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3968.0 / 3824.0 / 0.7034878836737739 / 198.65685445631416 | [NPY](tensors/0002922.npy) |
| 2923 | `model.layers.23.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8671875 / 1.234375 / 0.005429506301879883 / 0.6782478057109553 | [NPY](tensors/0002923.npy) |
| 2924 | `model.layers.23` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4992.0 / 4672.0 / 1.7792670355902778 / 318.46150988604387 | [NPY](tensors/0002924.npy) |
| 3003 | `model.layers.23` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9472.0 / 9408.0 / 0.6295789930555555 / 427.03808197360695 | [NPY](tensors/0003003.npy) |
| 3004 | `model.layers.23` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 346] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003004.npy) |
| 3005 | `model.layers.23` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.8764495849609375 / 0.8009113437243138 | [NPY](tensors/0003005.npy) |
| 3006 | `model.layers.23` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.020697563886642456 / 0.632324519915983 | [NPY](tensors/0003006.npy) |
| 3007 | `model.layers.23` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 345.0 / 345.0 / 345.0 / 0.0 | [NPY](tensors/0003007.npy) |
| 3008 | `model.layers.23` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3009 | `model.layers.23` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3010 | `model.layers.23` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3011 | `model.layers.23.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9472.0 / 9408.0 / 0.6295789930555555 / 427.03808197360695 | [NPY](tensors/0003011.npy) |
| 3012 | `model.layers.23.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.75 / 0.01464177237616645 / 1.7784645384868625 | [NPY](tensors/0003012.npy) |
| 3013 | `model.layers.23.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.75 / 0.01464177237616645 / 1.7784645384868625 | [NPY](tensors/0003013.npy) |
| 3014 | `model.layers.23.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 346] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003014.npy) |
| 3015 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 345.0 / 345.0 / 345.0 / 0.0 | [NPY](tensors/0003015.npy) |
| 3016 | `model.layers.23.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3017 | `model.layers.23.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3018 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.8764495849609375 / 0.8009113437243138 | [NPY](tensors/0003018.npy) |
| 3019 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.020697563886642456 / 0.632324519915983 | [NPY](tensors/0003019.npy) |
| 3020 | `model.layers.23.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3021 | `model.layers.23.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.75 / 0.01464177237616645 / 1.7784645384868625 | [NPY](tensors/0003021.npy) |
| 3022 | `model.layers.23.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.5625 / 14.125 / 0.052454335149377584 / 1.6364605420818161 | [NPY](tensors/0003022.npy) |
| 3023 | `model.layers.23.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.75 / 0.01464177237616645 / 1.7784645384868625 | [NPY](tensors/0003023.npy) |
| 3024 | `model.layers.23.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.25 / 30.0 / -0.10378912091255188 / 4.335566854852342 | [NPY](tensors/0003024.npy) |
| 3025 | `model.layers.23.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.75 / 0.01464177237616645 / 1.7784645384868625 | [NPY](tensors/0003025.npy) |
| 3026 | `model.layers.23.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.0625 / 8.3125 / 0.11569952964782715 / 2.945259136435731 | [NPY](tensors/0003026.npy) |
| 3027 | `model.layers.23.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.0625 / 6.34375 / 0.04817339906003326 / 1.2313523536438247 | [NPY](tensors/0003027.npy) |
| 3028 | `model.layers.23.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3136.0 / 3056.0 / 1.9110440360175238 / 142.5574299166733 | [NPY](tensors/0003028.npy) |
| 3029 | `model.layers.23.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3136.0 / 3056.0 / 1.9110440360175238 / 142.5574299166733 | [NPY](tensors/0003029.npy) |
| 3030 | `model.layers.23.self_attn` | 25 | `output[1]` | [1, 64, 1, 346] | torch.bfloat16 → float32 | 3.232969447708456e-13 / 0.88671875 / 0.0019913945423160836 / 0.014058409711765751 | [NPY](tensors/0003030.npy) |
| 3031 | `model.layers.23.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8320.0 / 8320.0 / 2.5278428819444443 / 419.9831674447344 | [NPY](tensors/0003031.npy) |
| 3032 | `model.layers.23.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.0 / 8.25 / -0.012589716911315918 / 1.208449674771695 | [NPY](tensors/0003032.npy) |
| 3033 | `model.layers.23.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.0 / 8.25 / -0.012589716911315918 / 1.208449674771695 | [NPY](tensors/0003033.npy) |
| 3034 | `model.layers.23.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -35.0 / 8.25 / -0.012589716911315918 / 1.208449674771695 | [NPY](tensors/0003034.npy) |
| 3035 | `model.layers.23.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3036 | `model.layers.23.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3037 | `model.layers.23.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3038 | `model.layers.23.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5568.0 / 5248.0 / -0.5946445888943143 / 308.69045869714773 | [NPY](tensors/0003038.npy) |
| 3039 | `model.layers.23.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5568.0 / 5248.0 / -0.5946445888943143 / 308.69045869714773 | [NPY](tensors/0003039.npy) |
| 3040 | `model.layers.23.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.390625 / 1.96875 / -0.06662940979003906 / 0.8698469627833207 | [NPY](tensors/0003040.npy) |
| 3041 | `model.layers.23` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3136.0 / 2912.0 / 1.9211805555555554 / 329.15827168872 | [NPY](tensors/0003041.npy) |
| 3120 | `model.layers.23` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 9664.0 / -1.1202840169270833 / 439.3728481427494 | [NPY](tensors/0003120.npy) |
| 3121 | `model.layers.23` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 347] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003121.npy) |
| 3122 | `model.layers.23` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.887237548828125 / 0.808167570442007 | [NPY](tensors/0003122.npy) |
| 3123 | `model.layers.23` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.06384772062301636 / 0.6046658936992718 | [NPY](tensors/0003123.npy) |
| 3124 | `model.layers.23` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 346.0 / 346.0 / 346.0 / 0.0 | [NPY](tensors/0003124.npy) |
| 3125 | `model.layers.23` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3126 | `model.layers.23` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3127 | `model.layers.23` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3128 | `model.layers.23.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 9664.0 / -1.1202840169270833 / 439.3728481427494 | [NPY](tensors/0003128.npy) |
| 3129 | `model.layers.23.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 58.25 / 0.010033583641052246 / 1.7810858363134727 | [NPY](tensors/0003129.npy) |
| 3130 | `model.layers.23.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 58.25 / 0.010033583641052246 / 1.7810858363134727 | [NPY](tensors/0003130.npy) |
| 3131 | `model.layers.23.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 347] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003131.npy) |
| 3132 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 346.0 / 346.0 / 346.0 / 0.0 | [NPY](tensors/0003132.npy) |
| 3133 | `model.layers.23.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3134 | `model.layers.23.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3135 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.887237548828125 / 0.808167570442007 | [NPY](tensors/0003135.npy) |
| 3136 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.06384772062301636 / 0.6046658936992718 | [NPY](tensors/0003136.npy) |
| 3137 | `model.layers.23.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3138 | `model.layers.23.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 58.25 / 0.010033583641052246 / 1.7810858363134727 | [NPY](tensors/0003138.npy) |
| 3139 | `model.layers.23.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.5625 / 14.8125 / 0.05066803237423301 / 1.6291918537467052 | [NPY](tensors/0003139.npy) |
| 3140 | `model.layers.23.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 58.25 / 0.010033583641052246 / 1.7810858363134727 | [NPY](tensors/0003140.npy) |
| 3141 | `model.layers.23.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.5 / 25.875 / -0.18864142894744873 / 4.4134925749136205 | [NPY](tensors/0003141.npy) |
| 3142 | `model.layers.23.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 58.25 / 0.010033583641052246 / 1.7810858363134727 | [NPY](tensors/0003142.npy) |
| 3143 | `model.layers.23.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.5625 / 15.8125 / -0.1532684490084648 / 4.981529132808226 | [NPY](tensors/0003143.npy) |
| 3144 | `model.layers.23.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.8125 / 6.25 / 0.026832027127966285 / 1.021122995613869 | [NPY](tensors/0003144.npy) |
| 3145 | `model.layers.23.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2112.0 / 2352.0 / 1.4202329635620117 / 123.11704099604664 | [NPY](tensors/0003145.npy) |
| 3146 | `model.layers.23.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2112.0 / 2352.0 / 1.4202329635620117 / 123.11704099604664 | [NPY](tensors/0003146.npy) |
| 3147 | `model.layers.23.self_attn` | 26 | `output[1]` | [1, 64, 1, 347] | torch.bfloat16 → float32 | 1.3677947663381929e-13 / 0.88671875 / 0.0015802213103315937 / 0.010276508839057256 | [NPY](tensors/0003147.npy) |
| 3148 | `model.layers.23.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8032.0 / 7808.0 / 0.32217339409722223 / 377.99767979254045 | [NPY](tensors/0003148.npy) |
| 3149 | `model.layers.23.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.5 / 12.1875 / -0.021272971895005967 / 1.2472346345989482 | [NPY](tensors/0003149.npy) |
| 3150 | `model.layers.23.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.5 / 12.1875 / -0.021272971895005967 / 1.2472346345989482 | [NPY](tensors/0003150.npy) |
| 3151 | `model.layers.23.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.5 / 12.1875 / -0.021272971895005967 / 1.2472346345989482 | [NPY](tensors/0003151.npy) |
| 3152 | `model.layers.23.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3153 | `model.layers.23.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3154 | `model.layers.23.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3155 | `model.layers.23.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6272.0 / 5696.0 / -3.1880511813693575 / 276.1005626884704 | [NPY](tensors/0003155.npy) |
| 3156 | `model.layers.23.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6272.0 / 5696.0 / -3.1880511813693575 / 276.1005626884704 | [NPY](tensors/0003156.npy) |
| 3157 | `model.layers.23.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.75 / 1.609375 / -0.12761259078979492 / 0.994783350718231 | [NPY](tensors/0003157.npy) |
| 3158 | `model.layers.23` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2336.0 / 1984.0 / -2.8505967881944443 / 256.9390710735072 | [NPY](tensors/0003158.npy) |
| 3237 | `model.layers.23` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 8512.0 / -3.2815863715277778 / 424.6704821477252 | [NPY](tensors/0003237.npy) |
| 3238 | `model.layers.23` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 348] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003238.npy) |
| 3239 | `model.layers.23` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.8368129730224609 / 0.8204651963806046 | [NPY](tensors/0003239.npy) |
| 3240 | `model.layers.23` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.1309933364391327 / 0.6478045244450656 | [NPY](tensors/0003240.npy) |
| 3241 | `model.layers.23` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 347.0 / 347.0 / 347.0 / 0.0 | [NPY](tensors/0003241.npy) |
| 3242 | `model.layers.23` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3243 | `model.layers.23` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3244 | `model.layers.23` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3245 | `model.layers.23.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 8512.0 / -3.2815863715277778 / 424.6704821477252 | [NPY](tensors/0003245.npy) |
| 3246 | `model.layers.23.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 52.25 / 0.004859310388565063 / 1.7467224768118073 | [NPY](tensors/0003246.npy) |
| 3247 | `model.layers.23.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 52.25 / 0.004859310388565063 / 1.7467224768118073 | [NPY](tensors/0003247.npy) |
| 3248 | `model.layers.23.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 348] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003248.npy) |
| 3249 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 347.0 / 347.0 / 347.0 / 0.0 | [NPY](tensors/0003249.npy) |
| 3250 | `model.layers.23.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3251 | `model.layers.23.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3252 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.8368129730224609 / 0.8204651963806046 | [NPY](tensors/0003252.npy) |
| 3253 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.1309933364391327 / 0.6478045244450656 | [NPY](tensors/0003253.npy) |
| 3254 | `model.layers.23.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3255 | `model.layers.23.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 52.25 / 0.004859310388565063 / 1.7467224768118073 | [NPY](tensors/0003255.npy) |
| 3256 | `model.layers.23.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.5625 / 16.75 / 0.061456297524273396 / 1.8812628150555188 | [NPY](tensors/0003256.npy) |
| 3257 | `model.layers.23.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 52.25 / 0.004859310388565063 / 1.7467224768118073 | [NPY](tensors/0003257.npy) |
| 3258 | `model.layers.23.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.0 / 31.125 / -0.07850871980190277 / 4.815900097558992 | [NPY](tensors/0003258.npy) |
| 3259 | `model.layers.23.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 52.25 / 0.004859310388565063 / 1.7467224768118073 | [NPY](tensors/0003259.npy) |
| 3260 | `model.layers.23.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.5625 / 14.75 / 0.21997737884521484 / 4.092323925209055 | [NPY](tensors/0003260.npy) |
| 3261 | `model.layers.23.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.5 / 8.3125 / 0.027756009716540575 / 1.3065613647042793 | [NPY](tensors/0003261.npy) |
| 3262 | `model.layers.23.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3008.0 / 2960.0 / 0.46406012111239964 / 143.94500405801813 | [NPY](tensors/0003262.npy) |
| 3263 | `model.layers.23.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3008.0 / 2960.0 / 0.46406012111239964 / 143.94500405801813 | [NPY](tensors/0003263.npy) |
| 3264 | `model.layers.23.self_attn` | 27 | `output[1]` | [1, 64, 1, 348] | torch.bfloat16 → float32 | 3.175237850427948e-14 / 0.93359375 / 0.0018254095461953486 / 0.014000727246034475 | [NPY](tensors/0003264.npy) |
| 3265 | `model.layers.23.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8000.0 / 7456.0 / -2.804557291666667 / 421.41899774251783 | [NPY](tensors/0003265.npy) |
| 3266 | `model.layers.23.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.25 / 9.0 / -0.03841362396876017 / 1.3533766682286603 | [NPY](tensors/0003266.npy) |
| 3267 | `model.layers.23.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.25 / 9.0 / -0.03841362396876017 / 1.3533766682286603 | [NPY](tensors/0003267.npy) |
| 3268 | `model.layers.23.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.25 / 9.0 / -0.03841362396876017 / 1.3533766682286603 | [NPY](tensors/0003268.npy) |
| 3269 | `model.layers.23.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3270 | `model.layers.23.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3271 | `model.layers.23.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3272 | `model.layers.23.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7104.0 / 6400.0 / -0.7206207063462999 / 328.6081553081958 | [NPY](tensors/0003272.npy) |
| 3273 | `model.layers.23.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7104.0 / 6400.0 / -0.7206207063462999 / 328.6081553081958 | [NPY](tensors/0003273.npy) |
| 3274 | `model.layers.23.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.796875 / 1.5703125 / -0.05899810791015625 / 0.9586433857325314 | [NPY](tensors/0003274.npy) |
| 3275 | `model.layers.23` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1600.0 / 1432.0 / -3.5351671006944443 / 295.93466992469894 | [NPY](tensors/0003275.npy) |
| 3354 | `model.layers.23` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8576.0 / 7936.0 / -4.258940972222222 / 434.3964364067598 | [NPY](tensors/0003354.npy) |
| 3355 | `model.layers.23` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 349] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003355.npy) |
| 3356 | `model.layers.23` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7588653564453125 / 0.8828955932720353 | [NPY](tensors/0003356.npy) |
| 3357 | `model.layers.23` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14290890097618103 / 0.6590419455082627 | [NPY](tensors/0003357.npy) |
| 3358 | `model.layers.23` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 348.0 / 348.0 / 348.0 / 0.0 | [NPY](tensors/0003358.npy) |
| 3359 | `model.layers.23` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3360 | `model.layers.23` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3361 | `model.layers.23` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3362 | `model.layers.23.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8576.0 / 7936.0 / -4.258940972222222 / 434.3964364067598 | [NPY](tensors/0003362.npy) |
| 3363 | `model.layers.23.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 48.5 / 0.0030280815230475534 / 1.7019886919591798 | [NPY](tensors/0003363.npy) |
| 3364 | `model.layers.23.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 48.5 / 0.0030280815230475534 / 1.7019886919591798 | [NPY](tensors/0003364.npy) |
| 3365 | `model.layers.23.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 349] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003365.npy) |
| 3366 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 348.0 / 348.0 / 348.0 / 0.0 | [NPY](tensors/0003366.npy) |
| 3367 | `model.layers.23.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3368 | `model.layers.23.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3369 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7588653564453125 / 0.8828955932720353 | [NPY](tensors/0003369.npy) |
| 3370 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14290890097618103 / 0.6590419455082627 | [NPY](tensors/0003370.npy) |
| 3371 | `model.layers.23.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3372 | `model.layers.23.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 48.5 / 0.0030280815230475534 / 1.7019886919591798 | [NPY](tensors/0003372.npy) |
| 3373 | `model.layers.23.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.25 / 14.875 / 0.020381751004606485 / 1.799518690090542 | [NPY](tensors/0003373.npy) |
| 3374 | `model.layers.23.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 48.5 / 0.0030280815230475534 / 1.7019886919591798 | [NPY](tensors/0003374.npy) |
| 3375 | `model.layers.23.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.0 / 27.375 / -0.05838266760110855 / 4.587024325871526 | [NPY](tensors/0003375.npy) |
| 3376 | `model.layers.23.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 48.5 / 0.0030280815230475534 / 1.7019886919591798 | [NPY](tensors/0003376.npy) |
| 3377 | `model.layers.23.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.5 / 14.4375 / 0.018878936767578125 / 4.449621364676539 | [NPY](tensors/0003377.npy) |
| 3378 | `model.layers.23.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.25 / 10.0 / 0.030864352826029062 / 1.2757049083937815 | [NPY](tensors/0003378.npy) |
| 3379 | `model.layers.23.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2640.0 / 2544.0 / 0.8425999959309896 / 130.51357623595771 | [NPY](tensors/0003379.npy) |
| 3380 | `model.layers.23.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2640.0 / 2544.0 / 0.8425999959309896 / 130.51357623595771 | [NPY](tensors/0003380.npy) |
| 3381 | `model.layers.23.self_attn` | 28 | `output[1]` | [1, 64, 1, 349] | torch.bfloat16 → float32 | 3.552713678800501e-13 / 0.95703125 / 0.0018719808736292318 / 0.014041845825928568 | [NPY](tensors/0003381.npy) |
| 3382 | `model.layers.23.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7168.0 / 6656.0 / -3.4257107204861112 / 418.5022086437733 | [NPY](tensors/0003382.npy) |
| 3383 | `model.layers.23.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 11.0 / -0.034503009584214955 / 1.463968137136154 | [NPY](tensors/0003383.npy) |
| 3384 | `model.layers.23.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 11.0 / -0.034503009584214955 / 1.463968137136154 | [NPY](tensors/0003384.npy) |
| 3385 | `model.layers.23.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.5 / 11.0 / -0.034503009584214955 / 1.463968137136154 | [NPY](tensors/0003385.npy) |
| 3386 | `model.layers.23.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3387 | `model.layers.23.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3388 | `model.layers.23.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3389 | `model.layers.23.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4928.0 / 4736.0 / -0.14571143256293403 / 284.0489659557435 | [NPY](tensors/0003389.npy) |
| 3390 | `model.layers.23.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4928.0 / 4736.0 / -0.14571143256293403 / 284.0489659557435 | [NPY](tensors/0003390.npy) |
| 3391 | `model.layers.23.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.796875 / 1.546875 / -0.0445404052734375 / 1.0082483364579615 | [NPY](tensors/0003391.npy) |
| 3392 | `model.layers.23` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2560.0 / 1832.0 / -3.5671793619791665 / 361.8758707925922 | [NPY](tensors/0003392.npy) |
| 3471 | `model.layers.23` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9472.0 / 1.0419053819444444 / 420.388842548618 | [NPY](tensors/0003471.npy) |
| 3472 | `model.layers.23` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 350] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003472.npy) |
| 3473 | `model.layers.23` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.701873779296875 / 0.9298159802037973 | [NPY](tensors/0003473.npy) |
| 3474 | `model.layers.23` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.10132250189781189 / 0.6650396518932735 | [NPY](tensors/0003474.npy) |
| 3475 | `model.layers.23` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 349.0 / 349.0 / 349.0 / 0.0 | [NPY](tensors/0003475.npy) |
| 3476 | `model.layers.23` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3477 | `model.layers.23` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3478 | `model.layers.23` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3479 | `model.layers.23.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9472.0 / 1.0419053819444444 / 420.388842548618 | [NPY](tensors/0003479.npy) |
| 3480 | `model.layers.23.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 60.5 / 0.015618465344111125 / 1.812457466408632 | [NPY](tensors/0003480.npy) |
| 3481 | `model.layers.23.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 60.5 / 0.015618465344111125 / 1.812457466408632 | [NPY](tensors/0003481.npy) |
| 3482 | `model.layers.23.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 350] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003482.npy) |
| 3483 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 349.0 / 349.0 / 349.0 / 0.0 | [NPY](tensors/0003483.npy) |
| 3484 | `model.layers.23.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3485 | `model.layers.23.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3486 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.701873779296875 / 0.9298159802037973 | [NPY](tensors/0003486.npy) |
| 3487 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.10132250189781189 / 0.6650396518932735 | [NPY](tensors/0003487.npy) |
| 3488 | `model.layers.23.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3489 | `model.layers.23.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 60.5 / 0.015618465344111125 / 1.812457466408632 | [NPY](tensors/0003489.npy) |
| 3490 | `model.layers.23.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.875 / 15.25 / 0.04866082267835736 / 1.5023392474690007 | [NPY](tensors/0003490.npy) |
| 3491 | `model.layers.23.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 60.5 / 0.015618465344111125 / 1.812457466408632 | [NPY](tensors/0003491.npy) |
| 3492 | `model.layers.23.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -41.5 / 34.25 / -0.0746992938220501 / 4.500354764420069 | [NPY](tensors/0003492.npy) |
| 3493 | `model.layers.23.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 60.5 / 0.015618465344111125 / 1.812457466408632 | [NPY](tensors/0003493.npy) |
| 3494 | `model.layers.23.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.625 / 12.375 / 0.29575812816619873 / 3.7312752945819576 | [NPY](tensors/0003494.npy) |
| 3495 | `model.layers.23.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.9375 / 8.3125 / 0.056514188181608915 / 1.2203977625350604 | [NPY](tensors/0003495.npy) |
| 3496 | `model.layers.23.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4192.0 / 4256.0 / 2.700710063510471 / 182.9984612752661 | [NPY](tensors/0003496.npy) |
| 3497 | `model.layers.23.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4192.0 / 4256.0 / 2.700710063510471 / 182.9984612752661 | [NPY](tensors/0003497.npy) |
| 3498 | `model.layers.23.self_attn` | 29 | `output[1]` | [1, 64, 1, 350] | torch.bfloat16 → float32 | 2.6978419498391304e-14 / 0.88671875 / 0.0018157168988833566 / 0.011078901059421681 | [NPY](tensors/0003498.npy) |
| 3499 | `model.layers.23.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 8576.0 / 3.757861328125 / 449.5022336642882 | [NPY](tensors/0003499.npy) |
| 3500 | `model.layers.23.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 7.46875 / -0.007226030031840007 / 1.0361718870923136 | [NPY](tensors/0003500.npy) |
| 3501 | `model.layers.23.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 7.46875 / -0.007226030031840007 / 1.0361718870923136 | [NPY](tensors/0003501.npy) |
| 3502 | `model.layers.23.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.25 / 7.46875 / -0.007226030031840007 / 1.0361718870923136 | [NPY](tensors/0003502.npy) |
| 3503 | `model.layers.23.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3504 | `model.layers.23.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3505 | `model.layers.23.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3506 | `model.layers.23.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5024.0 / 4512.0 / -4.3960315704345705 / 237.76884631897116 | [NPY](tensors/0003506.npy) |
| 3507 | `model.layers.23.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5024.0 / 4512.0 / -4.3960315704345705 / 237.76884631897116 | [NPY](tensors/0003507.npy) |
| 3508 | `model.layers.23.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.453125 / 1.828125 / 0.00997161865234375 / 0.9313478891824477 | [NPY](tensors/0003508.npy) |
| 3509 | `model.layers.23` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4832.0 / 3552.0 / -0.6258626302083333 / 290.73477128366153 | [NPY](tensors/0003509.npy) |
| 3588 | `model.layers.23` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7808.0 / 8192.0 / 2.3270941840277777 / 409.7041127297599 | [NPY](tensors/0003588.npy) |
| 3589 | `model.layers.23` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 351] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003589.npy) |
| 3590 | `model.layers.23` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.690826416015625 / 0.927895842605205 | [NPY](tensors/0003590.npy) |
| 3591 | `model.layers.23` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.04170632362365723 / 0.685352030153117 | [NPY](tensors/0003591.npy) |
| 3592 | `model.layers.23` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 350.0 / 350.0 / 350.0 / 0.0 | [NPY](tensors/0003592.npy) |
| 3593 | `model.layers.23` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3594 | `model.layers.23` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3595 | `model.layers.23` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3596 | `model.layers.23.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7808.0 / 8192.0 / 2.3270941840277777 / 409.7041127297599 | [NPY](tensors/0003596.npy) |
| 3597 | `model.layers.23.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 53.75 / 0.01989433897866143 / 1.7208154344433595 | [NPY](tensors/0003597.npy) |
| 3598 | `model.layers.23.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 53.75 / 0.01989433897866143 / 1.7208154344433595 | [NPY](tensors/0003598.npy) |
| 3599 | `model.layers.23.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 351] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003599.npy) |
| 3600 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 350.0 / 350.0 / 350.0 / 0.0 | [NPY](tensors/0003600.npy) |
| 3601 | `model.layers.23.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3602 | `model.layers.23.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3603 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.690826416015625 / 0.927895842605205 | [NPY](tensors/0003603.npy) |
| 3604 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.04170632362365723 / 0.685352030153117 | [NPY](tensors/0003604.npy) |
| 3605 | `model.layers.23.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3606 | `model.layers.23.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 53.75 / 0.01989433897866143 / 1.7208154344433595 | [NPY](tensors/0003606.npy) |
| 3607 | `model.layers.23.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.125 / 11.5 / 0.043854197254404426 / 1.478334291366413 | [NPY](tensors/0003607.npy) |
| 3608 | `model.layers.23.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 53.75 / 0.01989433897866143 / 1.7208154344433595 | [NPY](tensors/0003608.npy) |
| 3609 | `model.layers.23.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.5 / 29.0 / -0.04123600944876671 / 4.57281498660217 | [NPY](tensors/0003609.npy) |
| 3610 | `model.layers.23.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 53.75 / 0.01989433897866143 / 1.7208154344433595 | [NPY](tensors/0003610.npy) |
| 3611 | `model.layers.23.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -12.875 / 10.75 / 0.01605081558227539 / 3.659021039736716 | [NPY](tensors/0003611.npy) |
| 3612 | `model.layers.23.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.3125 / 7.78125 / 0.03754287981428206 / 1.1293649885470611 | [NPY](tensors/0003612.npy) |
| 3613 | `model.layers.23.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2560.0 / 2688.0 / 0.7685856660207112 / 126.56006296952914 | [NPY](tensors/0003613.npy) |
| 3614 | `model.layers.23.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2560.0 / 2688.0 / 0.7685856660207112 / 126.56006296952914 | [NPY](tensors/0003614.npy) |
| 3615 | `model.layers.23.self_attn` | 30 | `output[1]` | [1, 64, 1, 351] | torch.bfloat16 → float32 | 7.887024366937112e-13 / 0.78515625 / 0.0013515325889514047 / 0.010665563298971403 | [NPY](tensors/0003615.npy) |
| 3616 | `model.layers.23.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6432.0 / 6784.0 / 3.0881049262152778 / 391.45340628901886 | [NPY](tensors/0003616.npy) |
| 3617 | `model.layers.23.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 9.1875 / -0.008113516039318508 / 1.4938230727550537 | [NPY](tensors/0003617.npy) |
| 3618 | `model.layers.23.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 9.1875 / -0.008113516039318508 / 1.4938230727550537 | [NPY](tensors/0003618.npy) |
| 3619 | `model.layers.23.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -46.5 / 9.1875 / -0.008113516039318508 / 1.4938230727550537 | [NPY](tensors/0003619.npy) |
| 3620 | `model.layers.23.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3621 | `model.layers.23.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3622 | `model.layers.23.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3623 | `model.layers.23.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3888.0 / 3344.0 / -1.0492206361558702 / 205.15215150168746 | [NPY](tensors/0003623.npy) |
| 3624 | `model.layers.23.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3888.0 / 3344.0 / -1.0492206361558702 / 205.15215150168746 | [NPY](tensors/0003624.npy) |
| 3625 | `model.layers.23.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.328125 / 2.5 / 0.05908203125 / 1.3831953607064962 | [NPY](tensors/0003625.npy) |
| 3626 | `model.layers.23` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3728.0 / 3280.0 / 2.0333251953125 / 335.7386044234476 | [NPY](tensors/0003626.npy) |
| 3705 | `model.layers.23` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6560.0 / 7104.0 / 1.2844685872395833 / 378.0092122005903 | [NPY](tensors/0003705.npy) |
| 3706 | `model.layers.23` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 352] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003706.npy) |
| 3707 | `model.layers.23` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.715423583984375 / 0.9264461804361078 | [NPY](tensors/0003707.npy) |
| 3708 | `model.layers.23` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.0011060535907745361 / 0.6627134184873914 | [NPY](tensors/0003708.npy) |
| 3709 | `model.layers.23` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 351.0 / 351.0 / 351.0 / 0.0 | [NPY](tensors/0003709.npy) |
| 3710 | `model.layers.23` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3711 | `model.layers.23` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3712 | `model.layers.23` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3713 | `model.layers.23.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6560.0 / 7104.0 / 1.2844685872395833 / 378.0092122005903 | [NPY](tensors/0003713.npy) |
| 3714 | `model.layers.23.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 50.5 / 0.017182260089450414 / 1.6939862725010573 | [NPY](tensors/0003714.npy) |
| 3715 | `model.layers.23.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 50.5 / 0.017182260089450414 / 1.6939862725010573 | [NPY](tensors/0003715.npy) |
| 3716 | `model.layers.23.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 352] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003716.npy) |
| 3717 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 351.0 / 351.0 / 351.0 / 0.0 | [NPY](tensors/0003717.npy) |
| 3718 | `model.layers.23.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3719 | `model.layers.23.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3720 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.715423583984375 / 0.9264461804361078 | [NPY](tensors/0003720.npy) |
| 3721 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.0011060535907745361 / 0.6627134184873914 | [NPY](tensors/0003721.npy) |
| 3722 | `model.layers.23.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3723 | `model.layers.23.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 50.5 / 0.017182260089450414 / 1.6939862725010573 | [NPY](tensors/0003723.npy) |
| 3724 | `model.layers.23.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.5 / 13.25 / 0.02363833854906261 / 1.6584570156655123 | [NPY](tensors/0003724.npy) |
| 3725 | `model.layers.23.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 50.5 / 0.017182260089450414 / 1.6939862725010573 | [NPY](tensors/0003725.npy) |
| 3726 | `model.layers.23.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.75 / 24.125 / -0.16479326784610748 / 4.473866936808374 | [NPY](tensors/0003726.npy) |
| 3727 | `model.layers.23.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 50.5 / 0.017182260089450414 / 1.6939862725010573 | [NPY](tensors/0003727.npy) |
| 3728 | `model.layers.23.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -11.5625 / 11.875 / 0.20435816049575806 / 3.7974729967826057 | [NPY](tensors/0003728.npy) |
| 3729 | `model.layers.23.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.125 / 7.09375 / 0.003819866629783064 / 1.1918788151560367 | [NPY](tensors/0003729.npy) |
| 3730 | `model.layers.23.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2720.0 / 2912.0 / 2.2220127317640515 / 128.02529017946134 | [NPY](tensors/0003730.npy) |
| 3731 | `model.layers.23.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2720.0 / 2912.0 / 2.2220127317640515 / 128.02529017946134 | [NPY](tensors/0003731.npy) |
| 3732 | `model.layers.23.self_attn` | 31 | `output[1]` | [1, 64, 1, 352] | torch.bfloat16 → float32 | 3.219646771412954e-15 / 0.88671875 / 0.0010661180472817324 / 0.01164575988809917 | [NPY](tensors/0003732.npy) |
| 3733 | `model.layers.23.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6112.0 / 6688.0 / 3.499774848090278 / 384.24231453754055 | [NPY](tensors/0003733.npy) |
| 3734 | `model.layers.23.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 10.75 / -0.01020205683178372 / 1.5807554167496123 | [NPY](tensors/0003734.npy) |
| 3735 | `model.layers.23.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 10.75 / -0.01020205683178372 / 1.5807554167496123 | [NPY](tensors/0003735.npy) |
| 3736 | `model.layers.23.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -49.0 / 10.75 / -0.01020205683178372 / 1.5807554167496123 | [NPY](tensors/0003736.npy) |
| 3737 | `model.layers.23.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3738 | `model.layers.23.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3739 | `model.layers.23.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3740 | `model.layers.23.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2496.0 / 2464.0 / -1.262666998969184 / 209.26319119034792 | [NPY](tensors/0003740.npy) |
| 3741 | `model.layers.23.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2496.0 / 2464.0 / -1.262666998969184 / 209.26319119034792 | [NPY](tensors/0003741.npy) |
| 3742 | `model.layers.23.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.71875 / 2.390625 / 0.09381103515625 / 1.4109638878582103 | [NPY](tensors/0003742.npy) |
| 3743 | `model.layers.23` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6592.0 / 6848.0 / 2.258322482638889 / 457.3703875674379 | [NPY](tensors/0003743.npy) |
| 3822 | `model.layers.23` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7808.0 / 9088.0 / -0.23247884114583334 / 395.06155522894335 | [NPY](tensors/0003822.npy) |
| 3823 | `model.layers.23` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 353] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003823.npy) |
| 3824 | `model.layers.23` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.09375 / 1.34375 / 0.7454833984375 / 0.8931286656122284 | [NPY](tensors/0003824.npy) |
| 3825 | `model.layers.23` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3203125 / -0.0122755765914917 / 0.6751613260908969 | [NPY](tensors/0003825.npy) |
| 3826 | `model.layers.23` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 352.0 / 352.0 / 352.0 / 0.0 | [NPY](tensors/0003826.npy) |
| 3827 | `model.layers.23` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3828 | `model.layers.23` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3829 | `model.layers.23` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3830 | `model.layers.23.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7808.0 / 9088.0 / -0.23247884114583334 / 395.06155522894335 | [NPY](tensors/0003830.npy) |
| 3831 | `model.layers.23.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 61.75 / 0.015731694963243274 / 1.7924473442469326 | [NPY](tensors/0003831.npy) |
| 3832 | `model.layers.23.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 61.75 / 0.015731694963243274 / 1.7924473442469326 | [NPY](tensors/0003832.npy) |
| 3833 | `model.layers.23.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 353] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003833.npy) |
| 3834 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 352.0 / 352.0 / 352.0 / 0.0 | [NPY](tensors/0003834.npy) |
| 3835 | `model.layers.23.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3836 | `model.layers.23.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3837 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.09375 / 1.34375 / 0.7454833984375 / 0.8931286656122284 | [NPY](tensors/0003837.npy) |
| 3838 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3203125 / -0.0122755765914917 / 0.6751613260908969 | [NPY](tensors/0003838.npy) |
| 3839 | `model.layers.23.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3840 | `model.layers.23.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 61.75 / 0.015731694963243274 / 1.7924473442469326 | [NPY](tensors/0003840.npy) |
| 3841 | `model.layers.23.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.375 / 16.25 / 0.04309112555347383 / 1.6416120872601896 | [NPY](tensors/0003841.npy) |
| 3842 | `model.layers.23.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 61.75 / 0.015731694963243274 / 1.7924473442469326 | [NPY](tensors/0003842.npy) |
| 3843 | `model.layers.23.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -37.0 / 33.75 / -0.1548643410205841 / 4.911252729293367 | [NPY](tensors/0003843.npy) |
| 3844 | `model.layers.23.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 61.75 / 0.015731694963243274 / 1.7924473442469326 | [NPY](tensors/0003844.npy) |
| 3845 | `model.layers.23.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.75 / 8.6875 / 0.11848807334899902 / 3.104972992936037 | [NPY](tensors/0003845.npy) |
| 3846 | `model.layers.23.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.0625 / 5.375 / 0.028838318889029324 / 1.1781388786503673 | [NPY](tensors/0003846.npy) |
| 3847 | `model.layers.23.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3344.0 / 3328.0 / 2.1445089128282335 / 145.72263884118576 | [NPY](tensors/0003847.npy) |
| 3848 | `model.layers.23.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3344.0 / 3328.0 / 2.1445089128282335 / 145.72263884118576 | [NPY](tensors/0003848.npy) |
| 3849 | `model.layers.23.self_attn` | 32 | `output[1]` | [1, 64, 1, 353] | torch.bfloat16 → float32 | 5.440092820663267e-14 / 0.875 / 0.0015186246161076535 / 0.012559273265739006 | [NPY](tensors/0003849.npy) |
| 3850 | `model.layers.23.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6976.0 / 8256.0 / 1.9341851128472223 / 402.9401751950978 | [NPY](tensors/0003850.npy) |
| 3851 | `model.layers.23.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.25 / 10.625 / -0.010403476821051704 / 1.280034436574155 | [NPY](tensors/0003851.npy) |
| 3852 | `model.layers.23.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.25 / 10.625 / -0.010403476821051704 / 1.280034436574155 | [NPY](tensors/0003852.npy) |
| 3853 | `model.layers.23.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.25 / 10.625 / -0.010403476821051704 / 1.280034436574155 | [NPY](tensors/0003853.npy) |
| 3854 | `model.layers.23.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3855 | `model.layers.23.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3856 | `model.layers.23.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3857 | `model.layers.23.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4096.0 / 4128.0 / -0.6824003431532119 / 236.81887869036828 | [NPY](tensors/0003857.npy) |
| 3858 | `model.layers.23.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4096.0 / 4128.0 / -0.6824003431532119 / 236.81887869036828 | [NPY](tensors/0003858.npy) |
| 3859 | `model.layers.23.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.875 / 2.5625 / 0.1076507568359375 / 1.575397187553786 | [NPY](tensors/0003859.npy) |
| 3860 | `model.layers.23` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3136.0 / 4320.0 / 1.2621771918402778 / 311.4282117770196 | [NPY](tensors/0003860.npy) |
| 3939 | `model.layers.23` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7040.0 / 7104.0 / -1.5523952907986112 / 383.5822402079694 | [NPY](tensors/0003939.npy) |
| 3940 | `model.layers.23` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 354] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003940.npy) |
| 3941 | `model.layers.23` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.9921875 / 1.34375 / 0.763092041015625 / 0.8164851998069582 | [NPY](tensors/0003941.npy) |
| 3942 | `model.layers.23` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3203125 / -0.015299439430236816 / 0.7488356747498943 | [NPY](tensors/0003942.npy) |
| 3943 | `model.layers.23` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 353.0 / 353.0 / 353.0 / 0.0 | [NPY](tensors/0003943.npy) |
| 3944 | `model.layers.23` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3945 | `model.layers.23` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3946 | `model.layers.23` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3947 | `model.layers.23.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7040.0 / 7104.0 / -1.5523952907986112 / 383.5822402079694 | [NPY](tensors/0003947.npy) |
| 3948 | `model.layers.23.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 49.5 / 0.008039359251658123 / 1.6952896156123771 | [NPY](tensors/0003948.npy) |
| 3949 | `model.layers.23.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 49.5 / 0.008039359251658123 / 1.6952896156123771 | [NPY](tensors/0003949.npy) |
| 3950 | `model.layers.23.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 354] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003950.npy) |
| 3951 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 353.0 / 353.0 / 353.0 / 0.0 | [NPY](tensors/0003951.npy) |
| 3952 | `model.layers.23.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3953 | `model.layers.23.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3954 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.9921875 / 1.34375 / 0.763092041015625 / 0.8164851998069582 | [NPY](tensors/0003954.npy) |
| 3955 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3203125 / -0.015299439430236816 / 0.7488356747498943 | [NPY](tensors/0003955.npy) |
| 3956 | `model.layers.23.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3957 | `model.layers.23.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 49.5 / 0.008039359251658123 / 1.6952896156123771 | [NPY](tensors/0003957.npy) |
| 3958 | `model.layers.23.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.0625 / 17.25 / 0.03633074904792011 / 1.7015381695981122 | [NPY](tensors/0003958.npy) |
| 3959 | `model.layers.23.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 49.5 / 0.008039359251658123 / 1.6952896156123771 | [NPY](tensors/0003959.npy) |
| 3960 | `model.layers.23.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 33.75 / -0.1749947927892208 / 4.916790390350571 | [NPY](tensors/0003960.npy) |
| 3961 | `model.layers.23.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 49.5 / 0.008039359251658123 / 1.6952896156123771 | [NPY](tensors/0003961.npy) |
| 3962 | `model.layers.23.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.875 / 20.75 / 0.3437565565109253 / 4.701028319312281 | [NPY](tensors/0003962.npy) |
| 3963 | `model.layers.23.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.375 / 6.1875 / -0.002799941605189815 / 1.300492056980821 | [NPY](tensors/0003963.npy) |
| 3964 | `model.layers.23.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3680.0 / 3648.0 / 3.6866800096299914 / 155.6945399410266 | [NPY](tensors/0003964.npy) |
| 3965 | `model.layers.23.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3680.0 / 3648.0 / 3.6866800096299914 / 155.6945399410266 | [NPY](tensors/0003965.npy) |
| 3966 | `model.layers.23.self_attn` | 33 | `output[1]` | [1, 64, 1, 354] | torch.bfloat16 → float32 | 6.300515664747763e-15 / 0.91015625 / 0.0015166604744745057 / 0.012242591767208719 | [NPY](tensors/0003966.npy) |
| 3967 | `model.layers.23.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7008.0 / 7136.0 / 2.143896484375 / 411.2293375785448 | [NPY](tensors/0003967.npy) |
| 3968 | `model.layers.23.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 11.5 / -0.014872899320390489 / 1.3719034770116922 | [NPY](tensors/0003968.npy) |
| 3969 | `model.layers.23.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 11.5 / -0.014872899320390489 / 1.3719034770116922 | [NPY](tensors/0003969.npy) |
| 3970 | `model.layers.23.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -39.5 / 11.5 / -0.014872899320390489 / 1.3719034770116922 | [NPY](tensors/0003970.npy) |
| 3971 | `model.layers.23.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3972 | `model.layers.23.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3973 | `model.layers.23.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3974 | `model.layers.23.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4576.0 / 4480.0 / -1.2319583468967015 / 230.73315452574906 | [NPY](tensors/0003974.npy) |
| 3975 | `model.layers.23.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4576.0 / 4480.0 / -1.2319583468967015 / 230.73315452574906 | [NPY](tensors/0003975.npy) |
| 3976 | `model.layers.23.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.65625 / 2.3125 / 0.06182861328125 / 1.401182292743173 | [NPY](tensors/0003976.npy) |
| 3977 | `model.layers.23` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2720.0 / 2656.0 / 0.9157769097222223 / 308.7194475708684 | [NPY](tensors/0003977.npy) |
| 4056 | `model.layers.23` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6624.0 / 6656.0 / -1.6979546440972222 / 386.0417051546777 | [NPY](tensors/0004056.npy) |
| 4057 | `model.layers.23` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 355] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004057.npy) |
| 4058 | `model.layers.23` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2265625 / 1.34375 / 0.7769069671630859 / 0.8058280923944267 | [NPY](tensors/0004058.npy) |
| 4059 | `model.layers.23` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / -0.027683675289154053 / 0.7450244855303801 | [NPY](tensors/0004059.npy) |
| 4060 | `model.layers.23` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 354.0 / 354.0 / 354.0 / 0.0 | [NPY](tensors/0004060.npy) |
| 4061 | `model.layers.23` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4062 | `model.layers.23` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4063 | `model.layers.23` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4064 | `model.layers.23.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6624.0 / 6656.0 / -1.6979546440972222 / 386.0417051546777 | [NPY](tensors/0004064.npy) |
| 4065 | `model.layers.23.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 46.25 / 0.0056112421883477105 / 1.6719359829467928 | [NPY](tensors/0004065.npy) |
| 4066 | `model.layers.23.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 46.25 / 0.0056112421883477105 / 1.6719359829467928 | [NPY](tensors/0004066.npy) |
| 4067 | `model.layers.23.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 355] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004067.npy) |
| 4068 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 354.0 / 354.0 / 354.0 / 0.0 | [NPY](tensors/0004068.npy) |
| 4069 | `model.layers.23.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4070 | `model.layers.23.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4071 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2265625 / 1.34375 / 0.7769069671630859 / 0.8058280923944267 | [NPY](tensors/0004071.npy) |
| 4072 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / -0.027683675289154053 / 0.7450244855303801 | [NPY](tensors/0004072.npy) |
| 4073 | `model.layers.23.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4074 | `model.layers.23.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 46.25 / 0.0056112421883477105 / 1.6719359829467928 | [NPY](tensors/0004074.npy) |
| 4075 | `model.layers.23.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.8125 / 15.25 / 0.055574431200511754 / 1.705430462537799 | [NPY](tensors/0004075.npy) |
| 4076 | `model.layers.23.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 46.25 / 0.0056112421883477105 / 1.6719359829467928 | [NPY](tensors/0004076.npy) |
| 4077 | `model.layers.23.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.25 / 37.25 / -0.11290192976593971 / 5.039377797499578 | [NPY](tensors/0004077.npy) |
| 4078 | `model.layers.23.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 46.25 / 0.0056112421883477105 / 1.6719359829467928 | [NPY](tensors/0004078.npy) |
| 4079 | `model.layers.23.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -20.375 / 10.3125 / 0.17541104555130005 / 4.1037443338935775 | [NPY](tensors/0004079.npy) |
| 4080 | `model.layers.23.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.6875 / 8.875 / -0.0007875128649175167 / 1.3180602561680388 | [NPY](tensors/0004080.npy) |
| 4081 | `model.layers.23.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3552.0 / 3552.0 / 1.453915744357639 / 158.57220533395588 | [NPY](tensors/0004081.npy) |
| 4082 | `model.layers.23.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3552.0 / 3552.0 / 1.453915744357639 / 158.57220533395588 | [NPY](tensors/0004082.npy) |
| 4083 | `model.layers.23.self_attn` | 34 | `output[1]` | [1, 64, 1, 355] | torch.bfloat16 → float32 | 5.773159728050814e-14 / 0.7890625 / 0.0012232313851487935 / 0.012430677303325617 | [NPY](tensors/0004083.npy) |
| 4084 | `model.layers.23.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6336.0 / 6336.0 / -0.2586208767361111 / 420.7400770629749 | [NPY](tensors/0004084.npy) |
| 4085 | `model.layers.23.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 11.5 / -0.019899553722805448 / 1.4746392600619052 | [NPY](tensors/0004085.npy) |
| 4086 | `model.layers.23.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 11.5 / -0.019899553722805448 / 1.4746392600619052 | [NPY](tensors/0004086.npy) |
| 4087 | `model.layers.23.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -40.0 / 11.5 / -0.019899553722805448 / 1.4746392600619052 | [NPY](tensors/0004087.npy) |
| 4088 | `model.layers.23.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4089 | `model.layers.23.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4090 | `model.layers.23.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4091 | `model.layers.23.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5504.0 / 4800.0 / -2.081032901340061 / 289.91358536640246 | [NPY](tensors/0004091.npy) |
| 4092 | `model.layers.23.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 4800.0 / -2.081032901340061 / 289.91358536640246 | [NPY](tensors/0004092.npy) |
| 4093 | `model.layers.23.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.09375 / 2.515625 / 0.1036376953125 / 1.6331089562870018 | [NPY](tensors/0004093.npy) |
| 4094 | `model.layers.23` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3536.0 / 1992.0 / -2.335129123263889 / 349.6781704029212 | [NPY](tensors/0004094.npy) |
| 4173 | `model.layers.23` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6816.0 / 7232.0 / 1.9481377495659722 / 395.36965526280204 | [NPY](tensors/0004173.npy) |
| 4174 | `model.layers.23` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 356] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004174.npy) |
| 4175 | `model.layers.23` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.80755615234375 / 0.8303206482187034 | [NPY](tensors/0004175.npy) |
| 4176 | `model.layers.23` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / -0.04510064423084259 / 0.6824180444259353 | [NPY](tensors/0004176.npy) |
| 4177 | `model.layers.23` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 355.0 / 355.0 / 355.0 / 0.0 | [NPY](tensors/0004177.npy) |
| 4178 | `model.layers.23` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4179 | `model.layers.23` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4180 | `model.layers.23` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4181 | `model.layers.23.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6816.0 / 7232.0 / 1.9481377495659722 / 395.36965526280204 | [NPY](tensors/0004181.npy) |
| 4182 | `model.layers.23.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 46.0 / 0.018312226401435004 / 1.6672253619380242 | [NPY](tensors/0004182.npy) |
| 4183 | `model.layers.23.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 46.0 / 0.018312226401435004 / 1.6672253619380242 | [NPY](tensors/0004183.npy) |
| 4184 | `model.layers.23.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 356] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004184.npy) |
| 4185 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 355.0 / 355.0 / 355.0 / 0.0 | [NPY](tensors/0004185.npy) |
| 4186 | `model.layers.23.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4187 | `model.layers.23.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4188 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.80755615234375 / 0.8303206482187034 | [NPY](tensors/0004188.npy) |
| 4189 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / -0.04510064423084259 / 0.6824180444259353 | [NPY](tensors/0004189.npy) |
| 4190 | `model.layers.23.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4191 | `model.layers.23.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 46.0 / 0.018312226401435004 / 1.6672253619380242 | [NPY](tensors/0004191.npy) |
| 4192 | `model.layers.23.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.125 / 16.0 / 0.05305846454575658 / 1.8009651460691716 | [NPY](tensors/0004192.npy) |
| 4193 | `model.layers.23.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 46.0 / 0.018312226401435004 / 1.6672253619380242 | [NPY](tensors/0004193.npy) |
| 4194 | `model.layers.23.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.75 / 47.5 / -0.0074400752782821655 / 5.422503791449609 | [NPY](tensors/0004194.npy) |
| 4195 | `model.layers.23.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 46.0 / 0.018312226401435004 / 1.6672253619380242 | [NPY](tensors/0004195.npy) |
| 4196 | `model.layers.23.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.3125 / 12.5 / 0.010122060775756836 / 4.061139311854998 | [NPY](tensors/0004196.npy) |
| 4197 | `model.layers.23.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.875 / 9.8125 / -0.03377399710007012 / 1.3524237376382289 | [NPY](tensors/0004197.npy) |
| 4198 | `model.layers.23.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3216.0 / 3184.0 / 0.13733206854926217 / 149.65730789169368 | [NPY](tensors/0004198.npy) |
| 4199 | `model.layers.23.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3216.0 / 3184.0 / 0.13733206854926217 / 149.65730789169368 | [NPY](tensors/0004199.npy) |
| 4200 | `model.layers.23.self_attn` | 35 | `output[1]` | [1, 64, 1, 356] | torch.bfloat16 → float32 | 1.5890067039947553e-15 / 0.92578125 / 0.0011544148127017463 / 0.014497691046133594 | [NPY](tensors/0004200.npy) |
| 4201 | `model.layers.23.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6048.0 / 6592.0 / 2.0674913194444446 / 411.0080989649275 | [NPY](tensors/0004201.npy) |
| 4202 | `model.layers.23.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 11.75 / -0.009366393089294434 / 1.4797738863307865 | [NPY](tensors/0004202.npy) |
| 4203 | `model.layers.23.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 11.75 / -0.009366393089294434 / 1.4797738863307865 | [NPY](tensors/0004203.npy) |
| 4204 | `model.layers.23.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -41.25 / 11.75 / -0.009366393089294434 / 1.4797738863307865 | [NPY](tensors/0004204.npy) |
| 4205 | `model.layers.23.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4206 | `model.layers.23.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4207 | `model.layers.23.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4208 | `model.layers.23.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3520.0 / 3104.0 / -5.612818908691406 / 283.2178539265231 | [NPY](tensors/0004208.npy) |
| 4209 | `model.layers.23.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3520.0 / 3104.0 / -5.612818908691406 / 283.2178539265231 | [NPY](tensors/0004209.npy) |
| 4210 | `model.layers.23.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.796875 / 2.625 / 0.047393798828125 / 1.5616601591273516 | [NPY](tensors/0004210.npy) |
| 4211 | `model.layers.23` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3200.0 / 3072.0 / -3.5609917534722224 / 420.3984032552268 | [NPY](tensors/0004211.npy) |
| 4290 | `model.layers.23` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9216.0 / 10240.0 / 1.9864176432291667 / 458.16798764868145 | [NPY](tensors/0004290.npy) |
| 4291 | `model.layers.23` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 357] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004291.npy) |
| 4292 | `model.layers.23` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.85931396484375 / 0.7701579969072487 | [NPY](tensors/0004292.npy) |
| 4293 | `model.layers.23` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3203125 / -0.04313334822654724 / 0.6902819775762118 | [NPY](tensors/0004293.npy) |
| 4294 | `model.layers.23` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 356.0 / 356.0 / 356.0 / 0.0 | [NPY](tensors/0004294.npy) |
| 4295 | `model.layers.23` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4296 | `model.layers.23` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4297 | `model.layers.23` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4298 | `model.layers.23.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9216.0 / 10240.0 / 1.9864176432291667 / 458.16798764868145 | [NPY](tensors/0004298.npy) |
| 4299 | `model.layers.23.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 60.0 / 0.020546760823991563 / 1.7730963023213515 | [NPY](tensors/0004299.npy) |
| 4300 | `model.layers.23.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 60.0 / 0.020546760823991563 / 1.7730963023213515 | [NPY](tensors/0004300.npy) |
| 4301 | `model.layers.23.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 357] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004301.npy) |
| 4302 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 356.0 / 356.0 / 356.0 / 0.0 | [NPY](tensors/0004302.npy) |
| 4303 | `model.layers.23.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4304 | `model.layers.23.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4305 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.85931396484375 / 0.7701579969072487 | [NPY](tensors/0004305.npy) |
| 4306 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3203125 / -0.04313334822654724 / 0.6902819775762118 | [NPY](tensors/0004306.npy) |
| 4307 | `model.layers.23.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4308 | `model.layers.23.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 60.0 / 0.020546760823991563 / 1.7730963023213515 | [NPY](tensors/0004308.npy) |
| 4309 | `model.layers.23.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.5 / 16.75 / 0.035785912070423365 / 1.6085927792581858 | [NPY](tensors/0004309.npy) |
| 4310 | `model.layers.23.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 60.0 / 0.020546760823991563 / 1.7730963023213515 | [NPY](tensors/0004310.npy) |
| 4311 | `model.layers.23.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 30.5 / -0.13277273625135422 / 4.3543442118784546 | [NPY](tensors/0004311.npy) |
| 4312 | `model.layers.23.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 60.0 / 0.020546760823991563 / 1.7730963023213515 | [NPY](tensors/0004312.npy) |
| 4313 | `model.layers.23.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.0 / 13.75 / 0.14165544509887695 / 3.985531036852181 | [NPY](tensors/0004313.npy) |
| 4314 | `model.layers.23.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.6875 / 5.90625 / 0.017138668161351234 / 1.1755040888992245 | [NPY](tensors/0004314.npy) |
| 4315 | `model.layers.23.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3632.0 / 3824.0 / 3.298987367418077 / 163.8731071469571 | [NPY](tensors/0004315.npy) |
| 4316 | `model.layers.23.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3632.0 / 3824.0 / 3.298987367418077 / 163.8731071469571 | [NPY](tensors/0004316.npy) |
| 4317 | `model.layers.23.self_attn` | 36 | `output[1]` | [1, 64, 1, 357] | torch.bfloat16 → float32 | 2.7422508708241367e-14 / 0.796875 / 0.0013591031967137546 / 0.009619780317432117 | [NPY](tensors/0004317.npy) |
| 4318 | `model.layers.23.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8192.0 / 9216.0 / 5.309366183810764 / 462.54775213622327 | [NPY](tensors/0004318.npy) |
| 4319 | `model.layers.23.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 10.3125 / -0.006177114778094821 / 1.313937202716092 | [NPY](tensors/0004319.npy) |
| 4320 | `model.layers.23.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 10.3125 / -0.006177114778094821 / 1.313937202716092 | [NPY](tensors/0004320.npy) |
| 4321 | `model.layers.23.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -41.25 / 10.3125 / -0.006177114778094821 / 1.313937202716092 | [NPY](tensors/0004321.npy) |
| 4322 | `model.layers.23.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4323 | `model.layers.23.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4324 | `model.layers.23.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4325 | `model.layers.23.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3392.0 / 3408.0 / -2.3863875495062934 / 196.45523132474165 | [NPY](tensors/0004325.npy) |
| 4326 | `model.layers.23.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3392.0 / 3408.0 / -2.3863875495062934 / 196.45523132474165 | [NPY](tensors/0004326.npy) |
| 4327 | `model.layers.23.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.640625 / 1.8125 / 0.036376953125 / 1.333958258310356 | [NPY](tensors/0004327.npy) |
| 4328 | `model.layers.23` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4864.0 / 5824.0 / 2.937738715277778 / 350.0685549895743 | [NPY](tensors/0004328.npy) |
| 4407 | `model.layers.23` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11840.0 / 12352.0 / -0.9144171820746527 / 518.6216327799149 | [NPY](tensors/0004407.npy) |
| 4408 | `model.layers.23` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 358] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004408.npy) |
| 4409 | `model.layers.23` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.9085693359375 / 0.6912552727986224 | [NPY](tensors/0004409.npy) |
| 4410 | `model.layers.23` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.3203125 / -0.004209965467453003 / 0.711058024090348 | [NPY](tensors/0004410.npy) |
| 4411 | `model.layers.23` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 357.0 / 357.0 / 357.0 / 0.0 | [NPY](tensors/0004411.npy) |
| 4412 | `model.layers.23` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4413 | `model.layers.23` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4414 | `model.layers.23` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4415 | `model.layers.23.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11840.0 / 12352.0 / -0.9144171820746527 / 518.6216327799149 | [NPY](tensors/0004415.npy) |
| 4416 | `model.layers.23.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 64.0 / 0.010900087157885234 / 1.8105504335868643 | [NPY](tensors/0004416.npy) |
| 4417 | `model.layers.23.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 64.0 / 0.010900087157885234 / 1.8105504335868643 | [NPY](tensors/0004417.npy) |
| 4418 | `model.layers.23.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 358] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004418.npy) |
| 4419 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 357.0 / 357.0 / 357.0 / 0.0 | [NPY](tensors/0004419.npy) |
| 4420 | `model.layers.23.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4421 | `model.layers.23.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4422 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.9085693359375 / 0.6912552727986224 | [NPY](tensors/0004422.npy) |
| 4423 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.3203125 / -0.004209965467453003 / 0.711058024090348 | [NPY](tensors/0004423.npy) |
| 4424 | `model.layers.23.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4425 | `model.layers.23.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 64.0 / 0.010900087157885234 / 1.8105504335868643 | [NPY](tensors/0004425.npy) |
| 4426 | `model.layers.23.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.625 / 13.4375 / 0.04644528171047568 / 1.3769850669663253 | [NPY](tensors/0004426.npy) |
| 4427 | `model.layers.23.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 64.0 / 0.010900087157885234 / 1.8105504335868643 | [NPY](tensors/0004427.npy) |
| 4428 | `model.layers.23.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.0 / 39.25 / -0.08271652460098267 / 4.685101303534048 | [NPY](tensors/0004428.npy) |
| 4429 | `model.layers.23.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 64.0 / 0.010900087157885234 / 1.8105504335868643 | [NPY](tensors/0004429.npy) |
| 4430 | `model.layers.23.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.25 / 7.4375 / 0.04366469010710716 / 2.395297227206259 | [NPY](tensors/0004430.npy) |
| 4431 | `model.layers.23.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.0625 / 6.21875 / 0.041654587956145406 / 1.2477014684078012 | [NPY](tensors/0004431.npy) |
| 4432 | `model.layers.23.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4768.0 / 4896.0 / 4.598109012179904 / 208.04931703761483 | [NPY](tensors/0004432.npy) |
| 4433 | `model.layers.23.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4768.0 / 4896.0 / 4.598109012179904 / 208.04931703761483 | [NPY](tensors/0004433.npy) |
| 4434 | `model.layers.23.self_attn` | 37 | `output[1]` | [1, 64, 1, 358] | torch.bfloat16 → float32 | 2.717825964282383e-13 / 0.83203125 / 0.0016972960495479543 / 0.011562836202293059 | [NPY](tensors/0004434.npy) |
| 4435 | `model.layers.23.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11136.0 / 11648.0 / 3.6616173638237846 / 554.4038522192183 | [NPY](tensors/0004435.npy) |
| 4436 | `model.layers.23.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 6.9375 / -0.007369006342358059 / 1.0715070068812658 | [NPY](tensors/0004436.npy) |
| 4437 | `model.layers.23.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 6.9375 / -0.007369006342358059 / 1.0715070068812658 | [NPY](tensors/0004437.npy) |
| 4438 | `model.layers.23.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.0 / 6.9375 / -0.007369006342358059 / 1.0715070068812658 | [NPY](tensors/0004438.npy) |
| 4439 | `model.layers.23.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4440 | `model.layers.23.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4441 | `model.layers.23.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4442 | `model.layers.23.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1496.0 / 1368.0 / -3.298598225911458 / 118.9519537902015 | [NPY](tensors/0004442.npy) |
| 4443 | `model.layers.23.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1496.0 / 1368.0 / -3.298598225911458 / 118.9519537902015 | [NPY](tensors/0004443.npy) |
| 4444 | `model.layers.23.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.1875 / 1.4453125 / 0.0015869140625 / 0.8096093121235679 | [NPY](tensors/0004444.npy) |
| 4445 | `model.layers.23` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9792.0 / 10368.0 / 0.3820529513888889 / 507.82062370615404 | [NPY](tensors/0004445.npy) |
| 4524 | `model.layers.23` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 10432.0 / -5.026534016927084 / 490.36559085663566 | [NPY](tensors/0004524.npy) |
| 4525 | `model.layers.23` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 359] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004525.npy) |
| 4526 | `model.layers.23` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0234375 / 1.34375 / 0.9233245849609375 / 0.6835210214822701 | [NPY](tensors/0004526.npy) |
| 4527 | `model.layers.23` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.060156017541885376 / 0.6978118882257907 | [NPY](tensors/0004527.npy) |
| 4528 | `model.layers.23` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 358.0 / 358.0 / 358.0 / 0.0 | [NPY](tensors/0004528.npy) |
| 4529 | `model.layers.23` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4530 | `model.layers.23` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4531 | `model.layers.23` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4532 | `model.layers.23.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 10432.0 / -5.026534016927084 / 490.36559085663566 | [NPY](tensors/0004532.npy) |
| 4533 | `model.layers.23.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 57.25 / -0.0003795093960232205 / 1.7488190972896838 | [NPY](tensors/0004533.npy) |
| 4534 | `model.layers.23.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 57.25 / -0.0003795093960232205 / 1.7488190972896838 | [NPY](tensors/0004534.npy) |
| 4535 | `model.layers.23.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 359] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004535.npy) |
| 4536 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 358.0 / 358.0 / 358.0 / 0.0 | [NPY](tensors/0004536.npy) |
| 4537 | `model.layers.23.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4538 | `model.layers.23.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4539 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0234375 / 1.34375 / 0.9233245849609375 / 0.6835210214822701 | [NPY](tensors/0004539.npy) |
| 4540 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.060156017541885376 / 0.6978118882257907 | [NPY](tensors/0004540.npy) |
| 4541 | `model.layers.23.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4542 | `model.layers.23.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 57.25 / -0.0003795093960232205 / 1.7488190972896838 | [NPY](tensors/0004542.npy) |
| 4543 | `model.layers.23.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.4375 / 19.25 / 0.022770053357817233 / 1.4444177496387545 | [NPY](tensors/0004543.npy) |
| 4544 | `model.layers.23.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 57.25 / -0.0003795093960232205 / 1.7488190972896838 | [NPY](tensors/0004544.npy) |
| 4545 | `model.layers.23.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -64.5 / 45.25 / -0.1450563222169876 / 5.722951170138402 | [NPY](tensors/0004545.npy) |
| 4546 | `model.layers.23.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 57.25 / -0.0003795093960232205 / 1.7488190972896838 | [NPY](tensors/0004546.npy) |
| 4547 | `model.layers.23.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -20.125 / 12.375 / 0.272935152053833 / 3.830434038823617 | [NPY](tensors/0004547.npy) |
| 4548 | `model.layers.23.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.625 / 7.28125 / -0.00022714887745678425 / 1.2131909805508572 | [NPY](tensors/0004548.npy) |
| 4549 | `model.layers.23.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5856.0 / 6080.0 / 5.672796228196886 / 258.05567520029706 | [NPY](tensors/0004549.npy) |
| 4550 | `model.layers.23.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5856.0 / 6080.0 / 5.672796228196886 / 258.05567520029706 | [NPY](tensors/0004550.npy) |
| 4551 | `model.layers.23.self_attn` | 38 | `output[1]` | [1, 64, 1, 359] | torch.bfloat16 → float32 | 1.687538997430238e-14 / 0.80859375 / 0.0014691708964882633 / 0.01109475900097796 | [NPY](tensors/0004551.npy) |
| 4552 | `model.layers.23.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 10816.0 / 0.65257568359375 / 588.5544464879691 | [NPY](tensors/0004552.npy) |
| 4553 | `model.layers.23.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 8.4375 / -0.021062446965111628 / 1.082224640219978 | [NPY](tensors/0004553.npy) |
| 4554 | `model.layers.23.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 8.4375 / -0.021062446965111628 / 1.082224640219978 | [NPY](tensors/0004554.npy) |
| 4555 | `model.layers.23.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.25 / 8.4375 / -0.021062446965111628 / 1.082224640219978 | [NPY](tensors/0004555.npy) |
| 4556 | `model.layers.23.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4557 | `model.layers.23.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4558 | `model.layers.23.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4559 | `model.layers.23.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1624.0 / 1632.0 / -1.514623631371392 / 117.04328775656471 | [NPY](tensors/0004559.npy) |
| 4560 | `model.layers.23.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1624.0 / 1632.0 / -1.514623631371392 / 117.04328775656471 | [NPY](tensors/0004560.npy) |
| 4561 | `model.layers.23.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.5 / 1.2578125 / 0.006591796875 / 0.9299587527223905 | [NPY](tensors/0004561.npy) |
| 4562 | `model.layers.23` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 9280.0 / -0.8535061306423611 / 521.5368078877864 | [NPY](tensors/0004562.npy) |
| 4641 | `model.layers.23` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11520.0 / 11776.0 / -8.5095947265625 / 561.0870233365255 | [NPY](tensors/0004641.npy) |
| 4642 | `model.layers.23` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 360] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004642.npy) |
| 4643 | `model.layers.23` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.8929443359375 / 0.7026515532326651 | [NPY](tensors/0004643.npy) |
| 4644 | `model.layers.23` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3203125 / 0.11357763409614563 / 0.7110437810662014 | [NPY](tensors/0004644.npy) |
| 4645 | `model.layers.23` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 359.0 / 359.0 / 359.0 / 0.0 | [NPY](tensors/0004645.npy) |
| 4646 | `model.layers.23` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4647 | `model.layers.23` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4648 | `model.layers.23` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4649 | `model.layers.23.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11520.0 / 11776.0 / -8.5095947265625 / 561.0870233365255 | [NPY](tensors/0004649.npy) |
| 4650 | `model.layers.23.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 54.0 / -0.00847235255771213 / 1.7061350793345045 | [NPY](tensors/0004650.npy) |
| 4651 | `model.layers.23.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 54.0 / -0.00847235255771213 / 1.7061350793345045 | [NPY](tensors/0004651.npy) |
| 4652 | `model.layers.23.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 360] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004652.npy) |
| 4653 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 359.0 / 359.0 / 359.0 / 0.0 | [NPY](tensors/0004653.npy) |
| 4654 | `model.layers.23.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4655 | `model.layers.23.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4656 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.8929443359375 / 0.7026515532326651 | [NPY](tensors/0004656.npy) |
| 4657 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3203125 / 0.11357763409614563 / 0.7110437810662014 | [NPY](tensors/0004657.npy) |
| 4658 | `model.layers.23.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4659 | `model.layers.23.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 54.0 / -0.00847235255771213 / 1.7061350793345045 | [NPY](tensors/0004659.npy) |
| 4660 | `model.layers.23.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.5 / 15.6875 / 0.029758866294287145 / 1.4423622841729709 | [NPY](tensors/0004660.npy) |
| 4661 | `model.layers.23.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 54.0 / -0.00847235255771213 / 1.7061350793345045 | [NPY](tensors/0004661.npy) |
| 4662 | `model.layers.23.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -63.75 / 53.5 / -0.04209268093109131 / 5.545383710532515 | [NPY](tensors/0004662.npy) |
| 4663 | `model.layers.23.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 54.0 / -0.00847235255771213 / 1.7061350793345045 | [NPY](tensors/0004663.npy) |
| 4664 | `model.layers.23.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.75 / 10.1875 / -0.01514193695038557 / 3.1498265315117893 | [NPY](tensors/0004664.npy) |
| 4665 | `model.layers.23.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.625 / 7.625 / -0.020463376422412694 / 1.2985137597102283 | [NPY](tensors/0004665.npy) |
| 4666 | `model.layers.23.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4576.0 / 4800.0 / 3.705573802524143 / 204.3857765047377 | [NPY](tensors/0004666.npy) |
| 4667 | `model.layers.23.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4576.0 / 4800.0 / 3.705573802524143 / 204.3857765047377 | [NPY](tensors/0004667.npy) |
| 4668 | `model.layers.23.self_attn` | 39 | `output[1]` | [1, 64, 1, 360] | torch.bfloat16 → float32 | 4.107825191113079e-14 / 0.7265625 / 0.0013911234390519395 / 0.012888373197382012 | [NPY](tensors/0004668.npy) |
| 4669 | `model.layers.23.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 11136.0 / -4.797943793402778 / 593.0816883613761 | [NPY](tensors/0004669.npy) |
| 4670 | `model.layers.23.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 9.5 / -0.02999598185221354 / 1.2507433202959501 | [NPY](tensors/0004670.npy) |
| 4671 | `model.layers.23.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 9.5 / -0.02999598185221354 / 1.2507433202959501 | [NPY](tensors/0004671.npy) |
| 4672 | `model.layers.23.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -42.5 / 9.5 / -0.02999598185221354 / 1.2507433202959501 | [NPY](tensors/0004672.npy) |
| 4673 | `model.layers.23.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4674 | `model.layers.23.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4675 | `model.layers.23.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4676 | `model.layers.23.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5504.0 / -1.2335099962022569 / 317.755042015416 | [NPY](tensors/0004676.npy) |
| 4677 | `model.layers.23.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5504.0 / -1.2335099962022569 / 317.755042015416 | [NPY](tensors/0004677.npy) |
| 4678 | `model.layers.23.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.4375 / 2.046875 / -0.047206878662109375 / 0.9718111870478581 | [NPY](tensors/0004678.npy) |
| 4679 | `model.layers.23` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12800.0 / 12672.0 / -5.989865451388889 / 782.1807334371647 | [NPY](tensors/0004679.npy) |
| 4758 | `model.layers.23` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9856.0 / -1.9731974283854166 / 463.55469829765997 | [NPY](tensors/0004758.npy) |
| 4759 | `model.layers.23` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 361] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004759.npy) |
| 4760 | `model.layers.23` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.8425521850585938 / 0.7592463038913561 | [NPY](tensors/0004760.npy) |
| 4761 | `model.layers.23` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.328125 / 0.12352868914604187 / 0.7124125188030568 | [NPY](tensors/0004761.npy) |
| 4762 | `model.layers.23` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 360.0 / 360.0 / 360.0 / 0.0 | [NPY](tensors/0004762.npy) |
| 4763 | `model.layers.23` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4764 | `model.layers.23` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4765 | `model.layers.23` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4766 | `model.layers.23.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9856.0 / -1.9731974283854166 / 463.55469829765997 | [NPY](tensors/0004766.npy) |
| 4767 | `model.layers.23.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 57.25 / 0.004286689228481717 / 1.7575330658604804 | [NPY](tensors/0004767.npy) |
| 4768 | `model.layers.23.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 57.25 / 0.004286689228481717 / 1.7575330658604804 | [NPY](tensors/0004768.npy) |
| 4769 | `model.layers.23.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 361] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004769.npy) |
| 4770 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 360.0 / 360.0 / 360.0 / 0.0 | [NPY](tensors/0004770.npy) |
| 4771 | `model.layers.23.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4772 | `model.layers.23.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4773 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.8425521850585938 / 0.7592463038913561 | [NPY](tensors/0004773.npy) |
| 4774 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.328125 / 0.12352868914604187 / 0.7124125188030568 | [NPY](tensors/0004774.npy) |
| 4775 | `model.layers.23.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4776 | `model.layers.23.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 57.25 / 0.004286689228481717 / 1.7575330658604804 | [NPY](tensors/0004776.npy) |
| 4777 | `model.layers.23.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.9375 / 19.125 / 0.025303247675765306 / 1.5493967518288894 | [NPY](tensors/0004777.npy) |
| 4778 | `model.layers.23.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 57.25 / 0.004286689228481717 / 1.7575330658604804 | [NPY](tensors/0004778.npy) |
| 4779 | `model.layers.23.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.0 / 44.75 / -0.02709221839904785 / 5.304432025005552 | [NPY](tensors/0004779.npy) |
| 4780 | `model.layers.23.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 57.25 / 0.004286689228481717 / 1.7575330658604804 | [NPY](tensors/0004780.npy) |
| 4781 | `model.layers.23.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -24.25 / 10.0625 / -0.10047847032546997 / 3.2587657319670753 | [NPY](tensors/0004781.npy) |
| 4782 | `model.layers.23.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -20.75 / 6.96875 / 0.00877737463451922 / 1.1408970088227208 | [NPY](tensors/0004782.npy) |
| 4783 | `model.layers.23.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5632.0 / 5952.0 / 5.455763265821669 / 253.92768324182816 | [NPY](tensors/0004783.npy) |
| 4784 | `model.layers.23.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5632.0 / 5952.0 / 5.455763265821669 / 253.92768324182816 | [NPY](tensors/0004784.npy) |
| 4785 | `model.layers.23.self_attn` | 40 | `output[1]` | [1, 64, 1, 361] | torch.bfloat16 → float32 | 2.5979218776228663e-14 / 0.85546875 / 0.0012851551477133798 / 0.010345563073843675 | [NPY](tensors/0004785.npy) |
| 4786 | `model.layers.23.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 10304.0 / 3.4672593858506944 / 563.5796760509683 | [NPY](tensors/0004786.npy) |
| 4787 | `model.layers.23.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 7.25 / -0.012733244895935058 / 1.099012619725654 | [NPY](tensors/0004787.npy) |
| 4788 | `model.layers.23.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 7.25 / -0.012733244895935058 / 1.099012619725654 | [NPY](tensors/0004788.npy) |
| 4789 | `model.layers.23.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.75 / 7.25 / -0.012733244895935058 / 1.099012619725654 | [NPY](tensors/0004789.npy) |
| 4790 | `model.layers.23.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4791 | `model.layers.23.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4792 | `model.layers.23.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4793 | `model.layers.23.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1184.0 / 1400.0 / -1.9601317511664496 / 119.17191771519661 | [NPY](tensors/0004793.npy) |
| 4794 | `model.layers.23.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1184.0 / 1400.0 / -1.9601317511664496 / 119.17191771519661 | [NPY](tensors/0004794.npy) |
| 4795 | `model.layers.23.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.203125 / 1.34375 / 0.036357879638671875 / 0.7647349472542577 | [NPY](tensors/0004795.npy) |
| 4796 | `model.layers.23` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9024.0 / 9344.0 / 1.504324001736111 / 516.1835942955968 | [NPY](tensors/0004796.npy) |
| 4875 | `model.layers.23` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9984.0 / 10880.0 / 2.2820149739583333 / 489.79264203636114 | [NPY](tensors/0004875.npy) |
| 4876 | `model.layers.23` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 362] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004876.npy) |
| 4877 | `model.layers.23` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.8165130615234375 / 0.8162570957147703 | [NPY](tensors/0004877.npy) |
| 4878 | `model.layers.23` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.09044128656387329 / 0.6843655856400834 | [NPY](tensors/0004878.npy) |
| 4879 | `model.layers.23` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 361.0 / 361.0 / 361.0 / 0.0 | [NPY](tensors/0004879.npy) |
| 4880 | `model.layers.23` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4881 | `model.layers.23` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4882 | `model.layers.23` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4883 | `model.layers.23.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9984.0 / 10880.0 / 2.2820149739583333 / 489.79264203636114 | [NPY](tensors/0004883.npy) |
| 4884 | `model.layers.23.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 59.75 / 0.019677122433980305 / 1.7790181443166926 | [NPY](tensors/0004884.npy) |
| 4885 | `model.layers.23.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 59.75 / 0.019677122433980305 / 1.7790181443166926 | [NPY](tensors/0004885.npy) |
| 4886 | `model.layers.23.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 362] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004886.npy) |
| 4887 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 361.0 / 361.0 / 361.0 / 0.0 | [NPY](tensors/0004887.npy) |
| 4888 | `model.layers.23.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4889 | `model.layers.23.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4890 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.8165130615234375 / 0.8162570957147703 | [NPY](tensors/0004890.npy) |
| 4891 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.09044128656387329 / 0.6843655856400834 | [NPY](tensors/0004891.npy) |
| 4892 | `model.layers.23.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4893 | `model.layers.23.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 59.75 / 0.019677122433980305 / 1.7790181443166926 | [NPY](tensors/0004893.npy) |
| 4894 | `model.layers.23.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.4375 / 16.125 / 0.05494559183716774 / 1.640043595095434 | [NPY](tensors/0004894.npy) |
| 4895 | `model.layers.23.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 59.75 / 0.019677122433980305 / 1.7790181443166926 | [NPY](tensors/0004895.npy) |
| 4896 | `model.layers.23.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.75 / 30.375 / -0.07949773967266083 / 4.496263307461467 | [NPY](tensors/0004896.npy) |
| 4897 | `model.layers.23.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 59.75 / 0.019677122433980305 / 1.7790181443166926 | [NPY](tensors/0004897.npy) |
| 4898 | `model.layers.23.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -20.25 / 19.25 / 0.05133175849914551 / 5.131095792079977 | [NPY](tensors/0004898.npy) |
| 4899 | `model.layers.23.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.3125 / 7.5625 / 0.06833234871737659 / 1.3560756951445772 | [NPY](tensors/0004899.npy) |
| 4900 | `model.layers.23.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3008.0 / 2928.0 / 2.339784367879232 / 156.1990553437414 | [NPY](tensors/0004900.npy) |
| 4901 | `model.layers.23.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3008.0 / 2928.0 / 2.339784367879232 / 156.1990553437414 | [NPY](tensors/0004901.npy) |
| 4902 | `model.layers.23.self_attn` | 41 | `output[1]` | [1, 64, 1, 362] | torch.bfloat16 → float32 | 3.6415315207705135e-14 / 0.93359375 / 0.0015972181620706757 / 0.013665922058972903 | [NPY](tensors/0004902.npy) |
| 4903 | `model.layers.23.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8320.0 / 9088.0 / 4.6004014756944445 / 468.5132611285552 | [NPY](tensors/0004903.npy) |
| 4904 | `model.layers.23.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 10.125 / -0.003153065840403239 / 1.341237351324873 | [NPY](tensors/0004904.npy) |
| 4905 | `model.layers.23.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 10.125 / -0.003153065840403239 / 1.341237351324873 | [NPY](tensors/0004905.npy) |
| 4906 | `model.layers.23.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.375 / 10.125 / -0.003153065840403239 / 1.341237351324873 | [NPY](tensors/0004906.npy) |
| 4907 | `model.layers.23.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4908 | `model.layers.23.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4909 | `model.layers.23.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4910 | `model.layers.23.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4896.0 / 4736.0 / -13.20823262532552 / 335.9366889467973 | [NPY](tensors/0004910.npy) |
| 4911 | `model.layers.23.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4896.0 / 4736.0 / -13.20823262532552 / 335.9366889467973 | [NPY](tensors/0004911.npy) |
| 4912 | `model.layers.23.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.296875 / 2.09375 / 0.02822113037109375 / 1.2126410527920795 | [NPY](tensors/0004912.npy) |
| 4913 | `model.layers.23` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3584.0 / 4192.0 / -8.612369791666667 / 438.5008093486041 | [NPY](tensors/0004913.npy) |
| 4992 | `model.layers.23` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8704.0 / 9088.0 / 1.3651502821180554 / 435.36665357089163 | [NPY](tensors/0004992.npy) |
| 4993 | `model.layers.23` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 363] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004993.npy) |
| 4994 | `model.layers.23` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.046875 / 1.34375 / 0.8409137725830078 / 0.7828598309066966 | [NPY](tensors/0004994.npy) |
| 4995 | `model.layers.23` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.05170133709907532 / 0.6983318090469743 | [NPY](tensors/0004995.npy) |
| 4996 | `model.layers.23` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 362.0 / 362.0 / 362.0 / 0.0 | [NPY](tensors/0004996.npy) |
| 4997 | `model.layers.23` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4998 | `model.layers.23` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4999 | `model.layers.23` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5000 | `model.layers.23.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8704.0 / 9088.0 / 1.3651502821180554 / 435.36665357089163 | [NPY](tensors/0005000.npy) |
| 5001 | `model.layers.23.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 56.0 / 0.02229591343137953 / 1.7550350437496822 | [NPY](tensors/0005001.npy) |
| 5002 | `model.layers.23.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 56.0 / 0.02229591343137953 / 1.7550350437496822 | [NPY](tensors/0005002.npy) |
| 5003 | `model.layers.23.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 363] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005003.npy) |
| 5004 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 362.0 / 362.0 / 362.0 / 0.0 | [NPY](tensors/0005004.npy) |
| 5005 | `model.layers.23.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5006 | `model.layers.23.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5007 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.046875 / 1.34375 / 0.8409137725830078 / 0.7828598309066966 | [NPY](tensors/0005007.npy) |
| 5008 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.05170133709907532 / 0.6983318090469743 | [NPY](tensors/0005008.npy) |
| 5009 | `model.layers.23.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5010 | `model.layers.23.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 56.0 / 0.02229591343137953 / 1.7550350437496822 | [NPY](tensors/0005010.npy) |
| 5011 | `model.layers.23.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.375 / 16.75 / 0.048329315963201225 / 1.734583892751565 | [NPY](tensors/0005011.npy) |
| 5012 | `model.layers.23.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 56.0 / 0.02229591343137953 / 1.7550350437496822 | [NPY](tensors/0005012.npy) |
| 5013 | `model.layers.23.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.25 / 35.25 / -0.08592450618743896 / 4.5560068255185175 | [NPY](tensors/0005013.npy) |
| 5014 | `model.layers.23.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 56.0 / 0.02229591343137953 / 1.7550350437496822 | [NPY](tensors/0005014.npy) |
| 5015 | `model.layers.23.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.0625 / 13.5625 / 0.032528430223464966 / 4.00246741619694 | [NPY](tensors/0005015.npy) |
| 5016 | `model.layers.23.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.625 / 10.4375 / 0.07022257812786847 / 1.6388535180154122 | [NPY](tensors/0005016.npy) |
| 5017 | `model.layers.23.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3584.0 / 3568.0 / 3.0629064771864147 / 180.99596083139406 | [NPY](tensors/0005017.npy) |
| 5018 | `model.layers.23.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3584.0 / 3568.0 / 3.0629064771864147 / 180.99596083139406 | [NPY](tensors/0005018.npy) |
| 5019 | `model.layers.23.self_attn` | 42 | `output[1]` | [1, 64, 1, 363] | torch.bfloat16 → float32 | 9.547918011776346e-15 / 0.96875 / 0.0018671485396218686 / 0.017050766644676158 | [NPY](tensors/0005019.npy) |
| 5020 | `model.layers.23.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7936.0 / 8320.0 / 4.459906684027778 / 464.7560593409565 | [NPY](tensors/0005020.npy) |
| 5021 | `model.layers.23.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.75 / 8.625 / -0.004847150378757053 / 1.338857760515692 | [NPY](tensors/0005021.npy) |
| 5022 | `model.layers.23.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.75 / 8.625 / -0.004847150378757053 / 1.338857760515692 | [NPY](tensors/0005022.npy) |
| 5023 | `model.layers.23.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -30.75 / 8.625 / -0.004847150378757053 / 1.338857760515692 | [NPY](tensors/0005023.npy) |
| 5024 | `model.layers.23.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5025 | `model.layers.23.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5026 | `model.layers.23.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5027 | `model.layers.23.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5952.0 / 5504.0 / -0.6124168395996094 / 346.19598688551434 | [NPY](tensors/0005027.npy) |
| 5028 | `model.layers.23.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5952.0 / 5504.0 / -0.6124168395996094 / 346.19598688551434 | [NPY](tensors/0005028.npy) |
| 5029 | `model.layers.23.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.125 / 1.6484375 / 0.025625228881835938 / 1.0761805875043204 | [NPY](tensors/0005029.npy) |
| 5030 | `model.layers.23` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2432.0 / 2368.0 / 3.836686197916667 / 416.26221352208586 | [NPY](tensors/0005030.npy) |

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
