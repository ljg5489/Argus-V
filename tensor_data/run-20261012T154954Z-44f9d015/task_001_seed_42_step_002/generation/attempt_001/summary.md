# Hook inspection: generation

Status: **complete**. 3960 full tensors; 5148 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.004958227176832093 / 2.7792336758217617 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 297, 297] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.2410509149014136e+38 / 1.604307706703658e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 297, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8016785844809279 / 0.8745460170790657 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 297, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12195024475191096 / 0.6221439169688554 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 297] | torch.int64 → int64 | 0.0 / 296.0 / 148.0 / 85.73602898820698 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.004958227176832093 / 2.7792336758217617 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 297, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0038798362785637417 / 0.7626499117273927 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 297, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0038798362785637417 / 0.7626499117273927 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 297, 297] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.2410509149014136e+38 / 1.604307706703658e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 297] | torch.int64 → int64 | 0.0 / 296.0 / 148.0 / 85.73602898820698 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 297, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8016785844809279 / 0.8745460170790657 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 297, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12195024475191096 / 0.6221439169688554 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0038798362785637417 / 0.7626499117273927 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 297, 4096] | torch.bfloat16 → float32 | -9.5 / 12.8125 / 0.021969671458038638 / 1.0405423610254365 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0038798362785637417 / 0.7626499117273927 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 297, 512] | torch.bfloat16 → float32 | -65.5 / 68.0 / 0.026520517187487797 / 5.7649610447345 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0038798362785637417 / 0.7626499117273927 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 297, 512] | torch.bfloat16 → float32 | -8.1875 / 9.0 / -0.014625858728733128 / 1.2197733533133268 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 297, 4096] | torch.bfloat16 → float32 | -8.1875 / 8.8125 / -0.005360590898194973 / 0.5519694612050223 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 297, 2880] | torch.bfloat16 → float32 | -48.25 / 56.5 / 0.029572993794598455 / 1.2048759678734133 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -48.25 / 56.5 / 0.029572993794598455 / 1.2048759678734133 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 297, 297] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0013059344564442994 / 0.023837925807536266 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -87.5 / 71.5 / 0.024625162076200836 / 2.965941823335721 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 297, 2880] | torch.bfloat16 → float32 | -7.25 / 3.796875 / 0.001616245521991341 / 0.3441577501468751 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -7.25 / 3.796875 / 0.001616245521991341 / 0.3441577501468751 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [297, 2880] | torch.bfloat16 → float32 | -7.25 / 3.796875 / 0.001616245521991341 / 0.3441577501468751 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [297, 2880] | torch.bfloat16 → float32 | -50.0 / 93.5 / 0.019390878698858617 / 0.9057407605657701 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -50.0 / 93.5 / 0.019390878698858617 / 0.9057407605657701 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [297, 32] | torch.bfloat16 → float32 | -5.59375 / 3.4375 / -0.11051958899706703 / 1.017822607232043 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 297, 2880] | torch.bfloat16 → float32 | -89.0 / 107.0 / 0.04401078860143397 / 3.247793165831515 | [NPY](tensors/0000038.npy) |
| 117 | `model.layers.0` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 43.75 / 0.02880006796783871 / 2.9013049797239288 | [NPY](tensors/0000117.npy) |
| 118 | `model.layers.0` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000118.npy) |
| 119 | `model.layers.0` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.4918212890625 / 1.117229907691466 | [NPY](tensors/0000119.npy) |
| 120 | `model.layers.0` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.3359375 / 0.18026646971702576 / 0.5362459422402894 | [NPY](tensors/0000120.npy) |
| 121 | `model.layers.0` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 297.0 / 297.0 / 297.0 / 0.0 | [NPY](tensors/0000121.npy) |
| 122 | `model.layers.0` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 123 | `model.layers.0` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 124 | `model.layers.0` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 125 | `model.layers.0.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 43.75 / 0.02880006796783871 / 2.9013049797239288 | [NPY](tensors/0000125.npy) |
| 126 | `model.layers.0.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000126.npy) |
| 127 | `model.layers.0.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000127.npy) |
| 128 | `model.layers.0.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000128.npy) |
| 129 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 297.0 / 297.0 / 297.0 / 0.0 | [NPY](tensors/0000129.npy) |
| 130 | `model.layers.0.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 131 | `model.layers.0.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 132 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.4918212890625 / 1.117229907691466 | [NPY](tensors/0000132.npy) |
| 133 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.3359375 / 0.18026646971702576 / 0.5362459422402894 | [NPY](tensors/0000133.npy) |
| 134 | `model.layers.0.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 135 | `model.layers.0.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000135.npy) |
| 136 | `model.layers.0.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 7.4375 / 0.039632019703276455 / 0.9975220123045838 | [NPY](tensors/0000136.npy) |
| 137 | `model.layers.0.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000137.npy) |
| 138 | `model.layers.0.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.5 / 41.25 / 0.060565054416656494 / 4.792407804689708 | [NPY](tensors/0000138.npy) |
| 139 | `model.layers.0.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000139.npy) |
| 140 | `model.layers.0.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.9375 / 3.90625 / 0.001153320074081421 / 1.2325447380756387 | [NPY](tensors/0000140.npy) |
| 141 | `model.layers.0.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.96875 / 2.5625 / 0.003701793632899353 / 0.4452152232083449 | [NPY](tensors/0000141.npy) |
| 142 | `model.layers.0.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.125 / 37.75 / 0.027310078259971407 / 1.123208225996704 | [NPY](tensors/0000142.npy) |
| 143 | `model.layers.0.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.125 / 37.75 / 0.027310078259971407 / 1.123208225996704 | [NPY](tensors/0000143.npy) |
| 144 | `model.layers.0.self_attn` | 1 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0034509012786479104 / 0.03811222921978941 | [NPY](tensors/0000144.npy) |
| 145 | `model.layers.0.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 42.5 / 0.05610760715272692 / 3.0231390369530713 | [NPY](tensors/0000145.npy) |
| 146 | `model.layers.0.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7890625 / 2.09375 / 0.004131104548772176 / 0.3161042350623349 | [NPY](tensors/0000146.npy) |
| 147 | `model.layers.0.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7890625 / 2.09375 / 0.004131104548772176 / 0.3161042350623349 | [NPY](tensors/0000147.npy) |
| 148 | `model.layers.0.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.7890625 / 2.09375 / 0.004131104548772176 / 0.3161042350623349 | [NPY](tensors/0000148.npy) |
| 149 | `model.layers.0.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 150 | `model.layers.0.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 151 | `model.layers.0.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 152 | `model.layers.0.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.71875 / 25.5 / 0.0027894659174813163 / 0.7531856013198293 | [NPY](tensors/0000152.npy) |
| 153 | `model.layers.0.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.71875 / 25.5 / 0.0027894659174813163 / 0.7531856013198293 | [NPY](tensors/0000153.npy) |
| 154 | `model.layers.0.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.5859375 / 2.34375 / -0.05203056335449219 / 0.9277611762472543 | [NPY](tensors/0000154.npy) |
| 155 | `model.layers.0` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 49.5 / 0.05891591178046333 / 3.136548784617744 | [NPY](tensors/0000155.npy) |
| 234 | `model.layers.0` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 45.75 / 0.04227736194928487 / 3.1518798398795616 | [NPY](tensors/0000234.npy) |
| 235 | `model.layers.0` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000235.npy) |
| 236 | `model.layers.0` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.47601318359375 / 1.1300177711987256 | [NPY](tensors/0000236.npy) |
| 237 | `model.layers.0` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2265625 / 0.09335732460021973 / 0.5447921260742894 | [NPY](tensors/0000237.npy) |
| 238 | `model.layers.0` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 298.0 / 298.0 / 298.0 / 0.0 | [NPY](tensors/0000238.npy) |
| 239 | `model.layers.0` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 240 | `model.layers.0` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 241 | `model.layers.0` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 242 | `model.layers.0.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 45.75 / 0.04227736194928487 / 3.1518798398795616 | [NPY](tensors/0000242.npy) |
| 243 | `model.layers.0.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000243.npy) |
| 244 | `model.layers.0.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000244.npy) |
| 245 | `model.layers.0.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000245.npy) |
| 246 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 298.0 / 298.0 / 298.0 / 0.0 | [NPY](tensors/0000246.npy) |
| 247 | `model.layers.0.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 248 | `model.layers.0.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 249 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.47601318359375 / 1.1300177711987256 | [NPY](tensors/0000249.npy) |
| 250 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2265625 / 0.09335732460021973 / 0.5447921260742894 | [NPY](tensors/0000250.npy) |
| 251 | `model.layers.0.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 252 | `model.layers.0.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000252.npy) |
| 253 | `model.layers.0.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5 / 8.1875 / 0.022865560371428728 / 0.9733268065645532 | [NPY](tensors/0000253.npy) |
| 254 | `model.layers.0.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000254.npy) |
| 255 | `model.layers.0.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.75 / 47.0 / 0.09419560432434082 / 4.904277940788795 | [NPY](tensors/0000255.npy) |
| 256 | `model.layers.0.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000256.npy) |
| 257 | `model.layers.0.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 4.34375 / -0.08974748849868774 / 1.1126171556291353 | [NPY](tensors/0000257.npy) |
| 258 | `model.layers.0.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.0 / 3.796875 / -0.008358064238564111 / 0.5546056336830721 | [NPY](tensors/0000258.npy) |
| 259 | `model.layers.0.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.625 / 32.75 / 0.025571237670050727 / 1.0887404044641258 | [NPY](tensors/0000259.npy) |
| 260 | `model.layers.0.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.625 / 32.75 / 0.025571237670050727 / 1.0887404044641258 | [NPY](tensors/0000260.npy) |
| 261 | `model.layers.0.self_attn` | 2 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0040344360159328616 / 0.04396814045657924 | [NPY](tensors/0000261.npy) |
| 262 | `model.layers.0.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 42.5 / 0.06770509084065755 / 3.28118445478735 | [NPY](tensors/0000262.npy) |
| 263 | `model.layers.0.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.203125 / 2.03125 / 0.0055565618806415135 / 0.3177571286178103 | [NPY](tensors/0000263.npy) |
| 264 | `model.layers.0.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.203125 / 2.03125 / 0.0055565618806415135 / 0.3177571286178103 | [NPY](tensors/0000264.npy) |
| 265 | `model.layers.0.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.203125 / 2.03125 / 0.0055565618806415135 / 0.3177571286178103 | [NPY](tensors/0000265.npy) |
| 266 | `model.layers.0.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 267 | `model.layers.0.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 268 | `model.layers.0.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 269 | `model.layers.0.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.96875 / 26.5 / 0.037725269008013936 / 0.8806477870738355 | [NPY](tensors/0000269.npy) |
| 270 | `model.layers.0.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.96875 / 26.5 / 0.037725269008013936 / 0.8806477870738355 | [NPY](tensors/0000270.npy) |
| 271 | `model.layers.0.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.421875 / 1.90625 / -0.13364410400390625 / 1.010632869059671 | [NPY](tensors/0000271.npy) |
| 272 | `model.layers.0` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 63.75 / 0.1055386914147271 / 3.546275731782674 | [NPY](tensors/0000272.npy) |
| 351 | `model.layers.0` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0000351.npy) |
| 352 | `model.layers.0` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000352.npy) |
| 353 | `model.layers.0` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.518310546875 / 1.0946292885024063 | [NPY](tensors/0000353.npy) |
| 354 | `model.layers.0` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.234375 / 0.009437993168830872 / 0.5857162614275052 | [NPY](tensors/0000354.npy) |
| 355 | `model.layers.0` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 299.0 / 299.0 / 299.0 / 0.0 | [NPY](tensors/0000355.npy) |
| 356 | `model.layers.0` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 357 | `model.layers.0` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 358 | `model.layers.0` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 359 | `model.layers.0.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0000359.npy) |
| 360 | `model.layers.0.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000360.npy) |
| 361 | `model.layers.0.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000361.npy) |
| 362 | `model.layers.0.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000362.npy) |
| 363 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 299.0 / 299.0 / 299.0 / 0.0 | [NPY](tensors/0000363.npy) |
| 364 | `model.layers.0.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 365 | `model.layers.0.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 366 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.518310546875 / 1.0946292885024063 | [NPY](tensors/0000366.npy) |
| 367 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.234375 / 0.009437993168830872 / 0.5857162614275052 | [NPY](tensors/0000367.npy) |
| 368 | `model.layers.0.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 369 | `model.layers.0.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000369.npy) |
| 370 | `model.layers.0.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 9.25 / 0.06582052947487682 / 1.0317253511582722 | [NPY](tensors/0000370.npy) |
| 371 | `model.layers.0.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000371.npy) |
| 372 | `model.layers.0.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.5 / 59.75 / -0.027341485023498535 / 6.496414800406944 | [NPY](tensors/0000372.npy) |
| 373 | `model.layers.0.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000373.npy) |
| 374 | `model.layers.0.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.453125 / 4.6875 / 0.06333106756210327 / 0.9556167387162166 | [NPY](tensors/0000374.npy) |
| 375 | `model.layers.0.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.09375 / 4.34375 / -0.009188390467897989 / 0.5476894077349002 | [NPY](tensors/0000375.npy) |
| 376 | `model.layers.0.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0625 / 36.25 / 0.03136710913644897 / 1.1337788973634024 | [NPY](tensors/0000376.npy) |
| 377 | `model.layers.0.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0625 / 36.25 / 0.03136710913644897 / 1.1337788973634024 | [NPY](tensors/0000377.npy) |
| 378 | `model.layers.0.self_attn` | 3 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003617964864074224 / 0.040336014592257476 | [NPY](tensors/0000378.npy) |
| 379 | `model.layers.0.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 36.25 / 0.08036180072360569 / 2.601343603070317 | [NPY](tensors/0000379.npy) |
| 380 | `model.layers.0.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.484375 / 1.90625 / 0.007076525688171386 / 0.3296948871420133 | [NPY](tensors/0000380.npy) |
| 381 | `model.layers.0.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.484375 / 1.90625 / 0.007076525688171386 / 0.3296948871420133 | [NPY](tensors/0000381.npy) |
| 382 | `model.layers.0.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.484375 / 1.90625 / 0.007076525688171386 / 0.3296948871420133 | [NPY](tensors/0000382.npy) |
| 383 | `model.layers.0.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 384 | `model.layers.0.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 385 | `model.layers.0.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 386 | `model.layers.0.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -12.8125 / 33.75 / 0.03494518432352278 / 1.2380304478660173 | [NPY](tensors/0000386.npy) |
| 387 | `model.layers.0.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.8125 / 33.75 / 0.03494518432352278 / 1.2380304478660173 | [NPY](tensors/0000387.npy) |
| 388 | `model.layers.0.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.234375 / 2.546875 / -0.1164093017578125 / 1.2740452717872548 | [NPY](tensors/0000388.npy) |
| 389 | `model.layers.0` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 68.0 / 0.1150899887084961 / 3.0181410143349368 | [NPY](tensors/0000389.npy) |
| 468 | `model.layers.0` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 27.0 / 0.003733634617593553 / 2.804623802992795 | [NPY](tensors/0000468.npy) |
| 469 | `model.layers.0` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000469.npy) |
| 470 | `model.layers.0` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6011199951171875 / 1.029134772776266 | [NPY](tensors/0000470.npy) |
| 471 | `model.layers.0` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.02744269371032715 / 0.6241199078176489 | [NPY](tensors/0000471.npy) |
| 472 | `model.layers.0` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 300.0 / 300.0 / 300.0 / 0.0 | [NPY](tensors/0000472.npy) |
| 473 | `model.layers.0` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 474 | `model.layers.0` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 475 | `model.layers.0` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 476 | `model.layers.0.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 27.0 / 0.003733634617593553 / 2.804623802992795 | [NPY](tensors/0000476.npy) |
| 477 | `model.layers.0.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0000477.npy) |
| 478 | `model.layers.0.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0000478.npy) |
| 479 | `model.layers.0.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000479.npy) |
| 480 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 300.0 / 300.0 / 300.0 / 0.0 | [NPY](tensors/0000480.npy) |
| 481 | `model.layers.0.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 482 | `model.layers.0.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 483 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6011199951171875 / 1.029134772776266 | [NPY](tensors/0000483.npy) |
| 484 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.02744269371032715 / 0.6241199078176489 | [NPY](tensors/0000484.npy) |
| 485 | `model.layers.0.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 486 | `model.layers.0.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0000486.npy) |
| 487 | `model.layers.0.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.875 / 10.625 / 0.036541547160595655 / 1.020216334584807 | [NPY](tensors/0000487.npy) |
| 488 | `model.layers.0.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0000488.npy) |
| 489 | `model.layers.0.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.0 / 61.0 / 0.009755432605743408 / 5.9442685357666845 | [NPY](tensors/0000489.npy) |
| 490 | `model.layers.0.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0000490.npy) |
| 491 | `model.layers.0.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.65625 / 5.65625 / -0.0710136890411377 / 1.3093894403473694 | [NPY](tensors/0000491.npy) |
| 492 | `model.layers.0.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.21875 / 3.53125 / -0.0071979061776801245 / 0.5533878380566672 | [NPY](tensors/0000492.npy) |
| 493 | `model.layers.0.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.3125 / 42.75 / 0.036383535692261326 / 1.2641313242256949 | [NPY](tensors/0000493.npy) |
| 494 | `model.layers.0.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.3125 / 42.75 / 0.036383535692261326 / 1.2641313242256949 | [NPY](tensors/0000494.npy) |
| 495 | `model.layers.0.self_attn` | 4 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0032446533768134707 / 0.03716120121926869 | [NPY](tensors/0000495.npy) |
| 496 | `model.layers.0.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 46.25 / 0.04008993572658963 / 3.1202728576502157 | [NPY](tensors/0000496.npy) |
| 497 | `model.layers.0.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9453125 / 1.7109375 / -0.0022635810905032687 / 0.3177049858921452 | [NPY](tensors/0000497.npy) |
| 498 | `model.layers.0.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9453125 / 1.7109375 / -0.0022635810905032687 / 0.3177049858921452 | [NPY](tensors/0000498.npy) |
| 499 | `model.layers.0.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.9453125 / 1.7109375 / -0.0022635810905032687 / 0.3177049858921452 | [NPY](tensors/0000499.npy) |
| 500 | `model.layers.0.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 501 | `model.layers.0.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 502 | `model.layers.0.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 503 | `model.layers.0.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.875 / 27.375 / 0.03041575238522556 / 0.8376458036276905 | [NPY](tensors/0000503.npy) |
| 504 | `model.layers.0.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.875 / 27.375 / 0.03041575238522556 / 0.8376458036276905 | [NPY](tensors/0000504.npy) |
| 505 | `model.layers.0.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.546875 / 1.4296875 / -0.19371795654296875 / 0.6507675092294495 | [NPY](tensors/0000505.npy) |
| 506 | `model.layers.0` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.375 / 72.0 / 0.07065749698215061 / 3.537397195004989 | [NPY](tensors/0000506.npy) |
| 585 | `model.layers.0` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 44.75 / 0.013139636483457354 / 2.9607003759627655 | [NPY](tensors/0000585.npy) |
| 586 | `model.layers.0` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000586.npy) |
| 587 | `model.layers.0` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6781768798828125 / 0.9972778713983161 | [NPY](tensors/0000587.npy) |
| 588 | `model.layers.0` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.0019666850566864014 / 0.5958225425092146 | [NPY](tensors/0000588.npy) |
| 589 | `model.layers.0` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 301.0 / 301.0 / 301.0 / 0.0 | [NPY](tensors/0000589.npy) |
| 590 | `model.layers.0` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 591 | `model.layers.0` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 592 | `model.layers.0` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 593 | `model.layers.0.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 44.75 / 0.013139636483457354 / 2.9607003759627655 | [NPY](tensors/0000593.npy) |
| 594 | `model.layers.0.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0000594.npy) |
| 595 | `model.layers.0.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0000595.npy) |
| 596 | `model.layers.0.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000596.npy) |
| 597 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 301.0 / 301.0 / 301.0 / 0.0 | [NPY](tensors/0000597.npy) |
| 598 | `model.layers.0.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 599 | `model.layers.0.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 600 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6781768798828125 / 0.9972778713983161 | [NPY](tensors/0000600.npy) |
| 601 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.0019666850566864014 / 0.5958225425092146 | [NPY](tensors/0000601.npy) |
| 602 | `model.layers.0.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 603 | `model.layers.0.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0000603.npy) |
| 604 | `model.layers.0.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5625 / 8.625 / 0.03118488343898207 / 1.013318010948837 | [NPY](tensors/0000604.npy) |
| 605 | `model.layers.0.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0000605.npy) |
| 606 | `model.layers.0.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.25 / 44.0 / -0.021389365196228027 / 5.266550301692611 | [NPY](tensors/0000606.npy) |
| 607 | `model.layers.0.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0000607.npy) |
| 608 | `model.layers.0.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.28125 / 4.4375 / -0.023247554898262024 / 1.2424791578118235 | [NPY](tensors/0000608.npy) |
| 609 | `model.layers.0.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.1875 / 4.71875 / -0.016223544440435944 / 0.5717459753824522 | [NPY](tensors/0000609.npy) |
| 610 | `model.layers.0.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.1875 / 39.5 / 0.0318547162744734 / 1.1532089172896571 | [NPY](tensors/0000610.npy) |
| 611 | `model.layers.0.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.1875 / 39.5 / 0.0318547162744734 / 1.1532089172896571 | [NPY](tensors/0000611.npy) |
| 612 | `model.layers.0.self_attn` | 5 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98046875 / 0.003420520313723164 / 0.036984617948265616 | [NPY](tensors/0000612.npy) |
| 613 | `model.layers.0.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.25 / 43.5 / 0.04494673411051432 / 3.1284924526598408 | [NPY](tensors/0000613.npy) |
| 614 | `model.layers.0.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.3125 / 1.6875 / 0.006996589236789279 / 0.3438034886621044 | [NPY](tensors/0000614.npy) |
| 615 | `model.layers.0.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.3125 / 1.6875 / 0.006996589236789279 / 0.3438034886621044 | [NPY](tensors/0000615.npy) |
| 616 | `model.layers.0.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -5.3125 / 1.6875 / 0.006996589236789279 / 0.3438034886621044 | [NPY](tensors/0000616.npy) |
| 617 | `model.layers.0.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 618 | `model.layers.0.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 619 | `model.layers.0.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 620 | `model.layers.0.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -30.0 / 20.75 / -0.0020571284823947484 / 0.8477412765202214 | [NPY](tensors/0000620.npy) |
| 621 | `model.layers.0.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.0 / 20.75 / -0.0020571284823947484 / 0.8477412765202214 | [NPY](tensors/0000621.npy) |
| 622 | `model.layers.0.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.15625 / 1.4921875 / -0.20076847076416016 / 0.8821516925406752 | [NPY](tensors/0000622.npy) |
| 623 | `model.layers.0` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.5 / 56.0 / 0.042816593911912705 / 3.4260714579987837 | [NPY](tensors/0000623.npy) |
| 702 | `model.layers.0` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 31.375 / -0.03532346973402633 / 2.513775339817436 | [NPY](tensors/0000702.npy) |
| 703 | `model.layers.0` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000703.npy) |
| 704 | `model.layers.0` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.707061767578125 / 0.9717983302810768 | [NPY](tensors/0000704.npy) |
| 705 | `model.layers.0` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.234375 / 0.05849510431289673 / 0.601804974311013 | [NPY](tensors/0000705.npy) |
| 706 | `model.layers.0` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 302.0 / 302.0 / 302.0 / 0.0 | [NPY](tensors/0000706.npy) |
| 707 | `model.layers.0` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 708 | `model.layers.0` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 709 | `model.layers.0` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 710 | `model.layers.0.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 31.375 / -0.03532346973402633 / 2.513775339817436 | [NPY](tensors/0000710.npy) |
| 711 | `model.layers.0.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0000711.npy) |
| 712 | `model.layers.0.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0000712.npy) |
| 713 | `model.layers.0.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000713.npy) |
| 714 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 302.0 / 302.0 / 302.0 / 0.0 | [NPY](tensors/0000714.npy) |
| 715 | `model.layers.0.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 716 | `model.layers.0.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 717 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.707061767578125 / 0.9717983302810768 | [NPY](tensors/0000717.npy) |
| 718 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.234375 / 0.05849510431289673 / 0.601804974311013 | [NPY](tensors/0000718.npy) |
| 719 | `model.layers.0.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 720 | `model.layers.0.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0000720.npy) |
| 721 | `model.layers.0.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 8.875 / -0.00043488043593242764 / 1.093332692665652 | [NPY](tensors/0000721.npy) |
| 722 | `model.layers.0.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0000722.npy) |
| 723 | `model.layers.0.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.0 / 57.0 / -0.11751466989517212 / 6.178501515201047 | [NPY](tensors/0000723.npy) |
| 724 | `model.layers.0.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0000724.npy) |
| 725 | `model.layers.0.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.15625 / 4.375 / -0.08698096498847008 / 1.3301958676902246 | [NPY](tensors/0000725.npy) |
| 726 | `model.layers.0.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.34375 / 4.375 / -0.013758798255366855 / 0.6070329324115776 | [NPY](tensors/0000726.npy) |
| 727 | `model.layers.0.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.5 / 45.5 / 0.02984736296865675 / 1.4182508791742738 | [NPY](tensors/0000727.npy) |
| 728 | `model.layers.0.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.5 / 45.5 / 0.02984736296865675 / 1.4182508791742738 | [NPY](tensors/0000728.npy) |
| 729 | `model.layers.0.self_attn` | 6 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003441978836019996 / 0.03715667950258119 | [NPY](tensors/0000729.npy) |
| 730 | `model.layers.0.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 45.5 / -0.00556120342678494 / 2.9841758086263437 | [NPY](tensors/0000730.npy) |
| 731 | `model.layers.0.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7421875 / 1.6484375 / 0.0028676635689205594 / 0.3519422178382794 | [NPY](tensors/0000731.npy) |
| 732 | `model.layers.0.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7421875 / 1.6484375 / 0.0028676635689205594 / 0.3519422178382794 | [NPY](tensors/0000732.npy) |
| 733 | `model.layers.0.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.7421875 / 1.6484375 / 0.0028676635689205594 / 0.3519422178382794 | [NPY](tensors/0000733.npy) |
| 734 | `model.layers.0.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 735 | `model.layers.0.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 736 | `model.layers.0.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 737 | `model.layers.0.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -13.0 / 37.5 / 0.02569622861014472 / 1.0690010768553115 | [NPY](tensors/0000737.npy) |
| 738 | `model.layers.0.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 37.5 / 0.02569622861014472 / 1.0690010768553115 | [NPY](tensors/0000738.npy) |
| 739 | `model.layers.0.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9296875 / 1.734375 / -0.19734954833984375 / 0.7125903231517411 | [NPY](tensors/0000739.npy) |
| 740 | `model.layers.0` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.75 / 81.0 / 0.019986502329508462 / 3.6466623308523927 | [NPY](tensors/0000740.npy) |
| 819 | `model.layers.0` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0000819.npy) |
| 820 | `model.layers.0` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000820.npy) |
| 821 | `model.layers.0` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.68243408203125 / 0.9684034292887866 | [NPY](tensors/0000821.npy) |
| 822 | `model.layers.0` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3359375 / 0.10489383339881897 / 0.6297841334602801 | [NPY](tensors/0000822.npy) |
| 823 | `model.layers.0` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 303.0 / 303.0 / 303.0 / 0.0 | [NPY](tensors/0000823.npy) |
| 824 | `model.layers.0` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 825 | `model.layers.0` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 826 | `model.layers.0` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 827 | `model.layers.0.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0000827.npy) |
| 828 | `model.layers.0.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000828.npy) |
| 829 | `model.layers.0.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000829.npy) |
| 830 | `model.layers.0.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000830.npy) |
| 831 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 303.0 / 303.0 / 303.0 / 0.0 | [NPY](tensors/0000831.npy) |
| 832 | `model.layers.0.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 833 | `model.layers.0.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 834 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.68243408203125 / 0.9684034292887866 | [NPY](tensors/0000834.npy) |
| 835 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3359375 / 0.10489383339881897 / 0.6297841334602801 | [NPY](tensors/0000835.npy) |
| 836 | `model.layers.0.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 837 | `model.layers.0.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000837.npy) |
| 838 | `model.layers.0.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 9.25 / 0.06582052947487682 / 1.0317253511582722 | [NPY](tensors/0000838.npy) |
| 839 | `model.layers.0.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000839.npy) |
| 840 | `model.layers.0.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.5 / 59.75 / -0.027341485023498535 / 6.496414800406944 | [NPY](tensors/0000840.npy) |
| 841 | `model.layers.0.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000841.npy) |
| 842 | `model.layers.0.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.453125 / 4.6875 / 0.06333106756210327 / 0.9556167387162166 | [NPY](tensors/0000842.npy) |
| 843 | `model.layers.0.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.15625 / 4.53125 / 0.00016799983495729975 / 0.503391120234608 | [NPY](tensors/0000843.npy) |
| 844 | `model.layers.0.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.625 / 35.75 / 0.02987857460975647 / 1.0645317750172616 | [NPY](tensors/0000844.npy) |
| 845 | `model.layers.0.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.625 / 35.75 / 0.02987857460975647 / 1.0645317750172616 | [NPY](tensors/0000845.npy) |
| 846 | `model.layers.0.self_attn` | 7 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003172895543820621 / 0.03366995850079785 | [NPY](tensors/0000846.npy) |
| 847 | `model.layers.0.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.0 / 34.75 / 0.07892060544755723 / 2.630702415504541 | [NPY](tensors/0000847.npy) |
| 848 | `model.layers.0.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.484375 / 1.8515625 / 0.005247908168368869 / 0.3222084706179726 | [NPY](tensors/0000848.npy) |
| 849 | `model.layers.0.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.484375 / 1.8515625 / 0.005247908168368869 / 0.3222084706179726 | [NPY](tensors/0000849.npy) |
| 850 | `model.layers.0.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.484375 / 1.8515625 / 0.005247908168368869 / 0.3222084706179726 | [NPY](tensors/0000850.npy) |
| 851 | `model.layers.0.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 852 | `model.layers.0.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 853 | `model.layers.0.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 854 | `model.layers.0.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.1875 / 13.75 / 0.007031635733114348 / 0.5897887678687994 | [NPY](tensors/0000854.npy) |
| 855 | `model.layers.0.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.1875 / 13.75 / 0.007031635733114348 / 0.5897887678687994 | [NPY](tensors/0000855.npy) |
| 856 | `model.layers.0.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.140625 / 2.78125 / -0.12891387939453125 / 1.2777423156396712 | [NPY](tensors/0000856.npy) |
| 857 | `model.layers.0` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.75 / 46.75 / 0.08619126743740506 / 2.7350850129828617 | [NPY](tensors/0000857.npy) |
| 936 | `model.layers.0` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 29.25 / -0.00022348099284701876 / 2.7220311703073143 | [NPY](tensors/0000936.npy) |
| 937 | `model.layers.0` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000937.npy) |
| 938 | `model.layers.0` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6405029296875 / 1.0356892994687845 | [NPY](tensors/0000938.npy) |
| 939 | `model.layers.0` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1875 / 1.2421875 / 0.10542488098144531 / 0.5631099040524371 | [NPY](tensors/0000939.npy) |
| 940 | `model.layers.0` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 304.0 / 304.0 / 304.0 / 0.0 | [NPY](tensors/0000940.npy) |
| 941 | `model.layers.0` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 942 | `model.layers.0` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 943 | `model.layers.0` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 944 | `model.layers.0.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 29.25 / -0.00022348099284701876 / 2.7220311703073143 | [NPY](tensors/0000944.npy) |
| 945 | `model.layers.0.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.4375 / 6.6875 / -0.004346310595671336 / 0.7345667952509644 | [NPY](tensors/0000945.npy) |
| 946 | `model.layers.0.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.4375 / 6.6875 / -0.004346310595671336 / 0.7345667952509644 | [NPY](tensors/0000946.npy) |
| 947 | `model.layers.0.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000947.npy) |
| 948 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 304.0 / 304.0 / 304.0 / 0.0 | [NPY](tensors/0000948.npy) |
| 949 | `model.layers.0.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 950 | `model.layers.0.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 951 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6405029296875 / 1.0356892994687845 | [NPY](tensors/0000951.npy) |
| 952 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1875 / 1.2421875 / 0.10542488098144531 / 0.5631099040524371 | [NPY](tensors/0000952.npy) |
| 953 | `model.layers.0.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 954 | `model.layers.0.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.4375 / 6.6875 / -0.004346310595671336 / 0.7345667952509644 | [NPY](tensors/0000954.npy) |
| 955 | `model.layers.0.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.90625 / 9.3125 / 0.04514955263584852 / 1.0336311772074183 | [NPY](tensors/0000955.npy) |
| 956 | `model.layers.0.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.4375 / 6.6875 / -0.004346310595671336 / 0.7345667952509644 | [NPY](tensors/0000956.npy) |
| 957 | `model.layers.0.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.5 / 54.0 / 0.10255575180053711 / 5.739039829137789 | [NPY](tensors/0000957.npy) |
| 958 | `model.layers.0.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.4375 / 6.6875 / -0.004346310595671336 / 0.7345667952509644 | [NPY](tensors/0000958.npy) |
| 959 | `model.layers.0.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.4375 / 5.375 / 0.0019010305404663086 / 1.2656572842475073 | [NPY](tensors/0000959.npy) |
| 960 | `model.layers.0.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.1875 / 4.65625 / 0.000826768462502514 / 0.5080653306798233 | [NPY](tensors/0000960.npy) |
| 961 | `model.layers.0.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.8125 / 41.25 / 0.03485293429758814 / 1.1902759456496048 | [NPY](tensors/0000961.npy) |
| 962 | `model.layers.0.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.8125 / 41.25 / 0.03485293429758814 / 1.1902759456496048 | [NPY](tensors/0000962.npy) |
| 963 | `model.layers.0.self_attn` | 8 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0030047563566113753 / 0.03370387864322316 | [NPY](tensors/0000963.npy) |
| 964 | `model.layers.0.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 38.5 / 0.03451818890041775 / 2.964958503563736 | [NPY](tensors/0000964.npy) |
| 965 | `model.layers.0.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.390625 / 1.515625 / -0.0011167301072014702 / 0.34514451553135084 | [NPY](tensors/0000965.npy) |
| 966 | `model.layers.0.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.390625 / 1.515625 / -0.0011167301072014702 / 0.34514451553135084 | [NPY](tensors/0000966.npy) |
| 967 | `model.layers.0.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.390625 / 1.515625 / -0.0011167301072014702 / 0.34514451553135084 | [NPY](tensors/0000967.npy) |
| 968 | `model.layers.0.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 969 | `model.layers.0.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 970 | `model.layers.0.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 971 | `model.layers.0.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.125 / 24.0 / 0.038036182191636826 / 0.9329753097520539 | [NPY](tensors/0000971.npy) |
| 972 | `model.layers.0.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.125 / 24.0 / 0.038036182191636826 / 0.9329753097520539 | [NPY](tensors/0000972.npy) |
| 973 | `model.layers.0.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.71875 / 1.8671875 / -0.15300750732421875 / 0.8816212136780919 | [NPY](tensors/0000973.npy) |
| 974 | `model.layers.0` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 60.75 / 0.07259638044569228 / 3.350320902434104 | [NPY](tensors/0000974.npy) |
| 1053 | `model.layers.0` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 31.875 / -0.02020004838705063 / 2.9122038503504397 | [NPY](tensors/0001053.npy) |
| 1054 | `model.layers.0` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001054.npy) |
| 1055 | `model.layers.0` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0001055.npy) |
| 1056 | `model.layers.0` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0001056.npy) |
| 1057 | `model.layers.0` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0001057.npy) |
| 1058 | `model.layers.0` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1059 | `model.layers.0` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1060 | `model.layers.0` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1061 | `model.layers.0.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 31.875 / -0.02020004838705063 / 2.9122038503504397 | [NPY](tensors/0001061.npy) |
| 1062 | `model.layers.0.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0 / 8.6875 / -0.00791252214047644 / 0.7453222329310414 | [NPY](tensors/0001062.npy) |
| 1063 | `model.layers.0.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0 / 8.6875 / -0.00791252214047644 / 0.7453222329310414 | [NPY](tensors/0001063.npy) |
| 1064 | `model.layers.0.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001064.npy) |
| 1065 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0001065.npy) |
| 1066 | `model.layers.0.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1067 | `model.layers.0.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1068 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0001068.npy) |
| 1069 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0001069.npy) |
| 1070 | `model.layers.0.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1071 | `model.layers.0.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0 / 8.6875 / -0.00791252214047644 / 0.7453222329310414 | [NPY](tensors/0001071.npy) |
| 1072 | `model.layers.0.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 8.1875 / 0.02979311952367425 / 1.0196444892687007 | [NPY](tensors/0001072.npy) |
| 1073 | `model.layers.0.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0 / 8.6875 / -0.00791252214047644 / 0.7453222329310414 | [NPY](tensors/0001073.npy) |
| 1074 | `model.layers.0.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -55.0 / 41.25 / -0.027835845947265625 / 5.524087109562007 | [NPY](tensors/0001074.npy) |
| 1075 | `model.layers.0.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0 / 8.6875 / -0.00791252214047644 / 0.7453222329310414 | [NPY](tensors/0001075.npy) |
| 1076 | `model.layers.0.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.9375 / 5.3125 / -0.06936751306056976 / 1.264370457214429 | [NPY](tensors/0001076.npy) |
| 1077 | `model.layers.0.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.90625 / 5.25 / -0.006326191170956008 / 0.5510755343716165 | [NPY](tensors/0001077.npy) |
| 1078 | `model.layers.0.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.125 / 40.5 / 0.021737991273403166 / 1.181113010661163 | [NPY](tensors/0001078.npy) |
| 1079 | `model.layers.0.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.125 / 40.5 / 0.021737991273403166 / 1.181113010661163 | [NPY](tensors/0001079.npy) |
| 1080 | `model.layers.0.self_attn` | 9 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.97265625 / 0.003179774088454399 / 0.035189657077274554 | [NPY](tensors/0001080.npy) |
| 1081 | `model.layers.0.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 38.75 / 0.0015058649910820855 / 3.1506350793295947 | [NPY](tensors/0001081.npy) |
| 1082 | `model.layers.0.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.3125 / 1.875 / -0.0013714200920528835 / 0.3104485613619601 | [NPY](tensors/0001082.npy) |
| 1083 | `model.layers.0.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.3125 / 1.875 / -0.0013714200920528835 / 0.3104485613619601 | [NPY](tensors/0001083.npy) |
| 1084 | `model.layers.0.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.3125 / 1.875 / -0.0013714200920528835 / 0.3104485613619601 | [NPY](tensors/0001084.npy) |
| 1085 | `model.layers.0.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1086 | `model.layers.0.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1087 | `model.layers.0.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1088 | `model.layers.0.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -22.0 / 18.375 / 0.006471146560377545 / 0.6995055372916973 | [NPY](tensors/0001088.npy) |
| 1089 | `model.layers.0.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.0 / 18.375 / 0.006471146560377545 / 0.6995055372916973 | [NPY](tensors/0001089.npy) |
| 1090 | `model.layers.0.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.34375 / 1.5 / -0.15644073486328125 / 0.7343272912334431 | [NPY](tensors/0001090.npy) |
| 1091 | `model.layers.0` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.0 / 57.0 / 0.007965792549981011 / 3.4110954973661145 | [NPY](tensors/0001091.npy) |
| 1170 | `model.layers.0` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001170.npy) |
| 1171 | `model.layers.0` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001171.npy) |
| 1172 | `model.layers.0` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0001172.npy) |
| 1173 | `model.layers.0` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0001173.npy) |
| 1174 | `model.layers.0` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0001174.npy) |
| 1175 | `model.layers.0` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1176 | `model.layers.0` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1177 | `model.layers.0` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1178 | `model.layers.0.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001178.npy) |
| 1179 | `model.layers.0.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001179.npy) |
| 1180 | `model.layers.0.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001180.npy) |
| 1181 | `model.layers.0.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001181.npy) |
| 1182 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0001182.npy) |
| 1183 | `model.layers.0.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1184 | `model.layers.0.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1185 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0001185.npy) |
| 1186 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0001186.npy) |
| 1187 | `model.layers.0.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1188 | `model.layers.0.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001188.npy) |
| 1189 | `model.layers.0.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.84375 / 8.5625 / 0.0153301190584898 / 1.0113524420299036 | [NPY](tensors/0001189.npy) |
| 1190 | `model.layers.0.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001190.npy) |
| 1191 | `model.layers.0.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.0 / 65.5 / 0.032654017210006714 / 6.89507515667232 | [NPY](tensors/0001191.npy) |
| 1192 | `model.layers.0.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001192.npy) |
| 1193 | `model.layers.0.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.28125 / 3.390625 / -0.002120666205883026 / 0.8566653376613583 | [NPY](tensors/0001193.npy) |
| 1194 | `model.layers.0.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.375 / 4.375 / 0.0003255805304434034 / 0.44663693628746387 | [NPY](tensors/0001194.npy) |
| 1195 | `model.layers.0.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.75 / 27.5 / 0.027176531735393736 / 0.9495673922208616 | [NPY](tensors/0001195.npy) |
| 1196 | `model.layers.0.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.75 / 27.5 / 0.027176531735393736 / 0.9495673922208616 | [NPY](tensors/0001196.npy) |
| 1197 | `model.layers.0.self_attn` | 10 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003050139502814589 / 0.029722089120593903 | [NPY](tensors/0001197.npy) |
| 1198 | `model.layers.0.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.75 / 31.75 / 0.025330707761976455 / 2.958359007638968 | [NPY](tensors/0001198.npy) |
| 1199 | `model.layers.0.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.59375 / 1.4296875 / -0.001498578406042523 / 0.2883230739509239 | [NPY](tensors/0001199.npy) |
| 1200 | `model.layers.0.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.59375 / 1.4296875 / -0.001498578406042523 / 0.2883230739509239 | [NPY](tensors/0001200.npy) |
| 1201 | `model.layers.0.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.59375 / 1.4296875 / -0.001498578406042523 / 0.2883230739509239 | [NPY](tensors/0001201.npy) |
| 1202 | `model.layers.0.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1203 | `model.layers.0.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1204 | `model.layers.0.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1205 | `model.layers.0.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.1875 / 14.0625 / 0.018262435826990338 / 0.6836088762382159 | [NPY](tensors/0001205.npy) |
| 1206 | `model.layers.0.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.1875 / 14.0625 / 0.018262435826990338 / 0.6836088762382159 | [NPY](tensors/0001206.npy) |
| 1207 | `model.layers.0.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.0 / 3.0 / -0.022548675537109375 / 1.4723379490064565 | [NPY](tensors/0001207.npy) |
| 1208 | `model.layers.0` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.25 / 44.75 / 0.04351464377509223 / 2.9136189861009503 | [NPY](tensors/0001208.npy) |
| 1287 | `model.layers.0` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 49.25 / -0.03481262918147776 / 3.3040972398817177 | [NPY](tensors/0001287.npy) |
| 1288 | `model.layers.0` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001288.npy) |
| 1289 | `model.layers.0` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0001289.npy) |
| 1290 | `model.layers.0` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0001290.npy) |
| 1291 | `model.layers.0` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0001291.npy) |
| 1292 | `model.layers.0` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1293 | `model.layers.0` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1294 | `model.layers.0` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1295 | `model.layers.0.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 49.25 / -0.03481262918147776 / 3.3040972398817177 | [NPY](tensors/0001295.npy) |
| 1296 | `model.layers.0.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001296.npy) |
| 1297 | `model.layers.0.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001297.npy) |
| 1298 | `model.layers.0.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001298.npy) |
| 1299 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0001299.npy) |
| 1300 | `model.layers.0.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1301 | `model.layers.0.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1302 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0001302.npy) |
| 1303 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0001303.npy) |
| 1304 | `model.layers.0.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1305 | `model.layers.0.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001305.npy) |
| 1306 | `model.layers.0.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 6.25 / 0.025897369312588125 / 0.9110042125091211 | [NPY](tensors/0001306.npy) |
| 1307 | `model.layers.0.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001307.npy) |
| 1308 | `model.layers.0.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.75 / 46.25 / 0.08283017575740814 / 5.101942263816244 | [NPY](tensors/0001308.npy) |
| 1309 | `model.layers.0.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0001309.npy) |
| 1310 | `model.layers.0.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.765625 / 3.28125 / 0.0731726735830307 / 0.9884409409989561 | [NPY](tensors/0001310.npy) |
| 1311 | `model.layers.0.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.546875 / 2.84375 / 0.009760619842381857 / 0.4263721371279713 | [NPY](tensors/0001311.npy) |
| 1312 | `model.layers.0.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.8125 / 31.875 / 0.02783125765207741 / 0.9528025683189785 | [NPY](tensors/0001312.npy) |
| 1313 | `model.layers.0.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.8125 / 31.875 / 0.02783125765207741 / 0.9528025683189785 | [NPY](tensors/0001313.npy) |
| 1314 | `model.layers.0.self_attn` | 11 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0033371140062900383 / 0.03331233455777737 | [NPY](tensors/0001314.npy) |
| 1315 | `model.layers.0.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.5 / 48.25 / -0.007071092393663194 / 3.336153299112855 | [NPY](tensors/0001315.npy) |
| 1316 | `model.layers.0.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.140625 / 2.046875 / -0.0038203572233517966 / 0.293058062435056 | [NPY](tensors/0001316.npy) |
| 1317 | `model.layers.0.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.140625 / 2.046875 / -0.0038203572233517966 / 0.293058062435056 | [NPY](tensors/0001317.npy) |
| 1318 | `model.layers.0.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.140625 / 2.046875 / -0.0038203572233517966 / 0.293058062435056 | [NPY](tensors/0001318.npy) |
| 1319 | `model.layers.0.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1320 | `model.layers.0.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1321 | `model.layers.0.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1322 | `model.layers.0.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.96875 / 20.125 / 0.031160848670535618 / 0.666918704706077 | [NPY](tensors/0001322.npy) |
| 1323 | `model.layers.0.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.96875 / 20.125 / 0.031160848670535618 / 0.666918704706077 | [NPY](tensors/0001323.npy) |
| 1324 | `model.layers.0.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.46875 / 1.6171875 / -0.06457138061523438 / 0.9013389593750469 | [NPY](tensors/0001324.npy) |
| 1325 | `model.layers.0` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 45.75 / 0.02385288874308268 / 3.3585355342786074 | [NPY](tensors/0001325.npy) |
| 1404 | `model.layers.0` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.25 / 40.75 / -0.02422896482878261 / 2.4202562004709502 | [NPY](tensors/0001404.npy) |
| 1405 | `model.layers.0` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001405.npy) |
| 1406 | `model.layers.0` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0001406.npy) |
| 1407 | `model.layers.0` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0001407.npy) |
| 1408 | `model.layers.0` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0001408.npy) |
| 1409 | `model.layers.0` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1410 | `model.layers.0` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1411 | `model.layers.0` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1412 | `model.layers.0.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.25 / 40.75 / -0.02422896482878261 / 2.4202562004709502 | [NPY](tensors/0001412.npy) |
| 1413 | `model.layers.0.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.625 / 11.125 / -0.0014607492834329606 / 0.72951763094264 | [NPY](tensors/0001413.npy) |
| 1414 | `model.layers.0.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.625 / 11.125 / -0.0014607492834329606 / 0.72951763094264 | [NPY](tensors/0001414.npy) |
| 1415 | `model.layers.0.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001415.npy) |
| 1416 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0001416.npy) |
| 1417 | `model.layers.0.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1418 | `model.layers.0.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1419 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0001419.npy) |
| 1420 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0001420.npy) |
| 1421 | `model.layers.0.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1422 | `model.layers.0.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.625 / 11.125 / -0.0014607492834329606 / 0.72951763094264 | [NPY](tensors/0001422.npy) |
| 1423 | `model.layers.0.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 8.8125 / 0.025038445135578513 / 1.0585335076795481 | [NPY](tensors/0001423.npy) |
| 1424 | `model.layers.0.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.625 / 11.125 / -0.0014607492834329606 / 0.72951763094264 | [NPY](tensors/0001424.npy) |
| 1425 | `model.layers.0.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.25 / 48.75 / -0.020088493824005127 / 5.833538471347034 | [NPY](tensors/0001425.npy) |
| 1426 | `model.layers.0.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.625 / 11.125 / -0.0014607492834329606 / 0.72951763094264 | [NPY](tensors/0001426.npy) |
| 1427 | `model.layers.0.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.78125 / 5.53125 / -0.010265827178955078 / 1.5574125899118745 | [NPY](tensors/0001427.npy) |
| 1428 | `model.layers.0.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.28125 / 3.703125 / 0.016399491891206708 / 0.47607981606035177 | [NPY](tensors/0001428.npy) |
| 1429 | `model.layers.0.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.625 / 43.25 / 0.03455890069405238 / 1.2764881616255002 | [NPY](tensors/0001429.npy) |
| 1430 | `model.layers.0.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.625 / 43.25 / 0.03455890069405238 / 1.2764881616255002 | [NPY](tensors/0001430.npy) |
| 1431 | `model.layers.0.self_attn` | 12 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.00273418219955583 / 0.034352329368341164 | [NPY](tensors/0001431.npy) |
| 1432 | `model.layers.0.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 44.0 / 0.010424349043104384 / 2.8487239663933277 | [NPY](tensors/0001432.npy) |
| 1433 | `model.layers.0.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.359375 / 1.75 / 0.0038580920961168077 / 0.35477180662813673 | [NPY](tensors/0001433.npy) |
| 1434 | `model.layers.0.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.359375 / 1.75 / 0.0038580920961168077 / 0.35477180662813673 | [NPY](tensors/0001434.npy) |
| 1435 | `model.layers.0.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.359375 / 1.75 / 0.0038580920961168077 / 0.35477180662813673 | [NPY](tensors/0001435.npy) |
| 1436 | `model.layers.0.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1437 | `model.layers.0.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1438 | `model.layers.0.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1439 | `model.layers.0.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.625 / 20.875 / 0.020452730937136544 / 0.6247699075603583 | [NPY](tensors/0001439.npy) |
| 1440 | `model.layers.0.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.625 / 20.875 / 0.020452730937136544 / 0.6247699075603583 | [NPY](tensors/0001440.npy) |
| 1441 | `model.layers.0.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.09375 / 1.140625 / -0.15600204467773438 / 0.5809593657310065 | [NPY](tensors/0001441.npy) |
| 1442 | `model.layers.0` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 63.5 / 0.030923316213819715 / 3.1805317384712324 | [NPY](tensors/0001442.npy) |
| 1521 | `model.layers.0` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 34.75 / -0.016191900273164115 / 2.5953228695685033 | [NPY](tensors/0001521.npy) |
| 1522 | `model.layers.0` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001522.npy) |
| 1523 | `model.layers.0` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0001523.npy) |
| 1524 | `model.layers.0` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0001524.npy) |
| 1525 | `model.layers.0` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0001525.npy) |
| 1526 | `model.layers.0` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1527 | `model.layers.0` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1528 | `model.layers.0` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1529 | `model.layers.0.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 34.75 / -0.016191900273164115 / 2.5953228695685033 | [NPY](tensors/0001529.npy) |
| 1530 | `model.layers.0.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.6875 / 13.0625 / -0.014683377411630418 / 0.7898696349203141 | [NPY](tensors/0001530.npy) |
| 1531 | `model.layers.0.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.6875 / 13.0625 / -0.014683377411630418 / 0.7898696349203141 | [NPY](tensors/0001531.npy) |
| 1532 | `model.layers.0.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001532.npy) |
| 1533 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0001533.npy) |
| 1534 | `model.layers.0.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1535 | `model.layers.0.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1536 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0001536.npy) |
| 1537 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0001537.npy) |
| 1538 | `model.layers.0.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1539 | `model.layers.0.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.6875 / 13.0625 / -0.014683377411630418 / 0.7898696349203141 | [NPY](tensors/0001539.npy) |
| 1540 | `model.layers.0.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 9.0625 / 0.03967268601991236 / 1.0228087923497517 | [NPY](tensors/0001540.npy) |
| 1541 | `model.layers.0.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.6875 / 13.0625 / -0.014683377411630418 / 0.7898696349203141 | [NPY](tensors/0001541.npy) |
| 1542 | `model.layers.0.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.5 / 45.0 / 0.15265456587076187 / 5.212176434679534 | [NPY](tensors/0001542.npy) |
| 1543 | `model.layers.0.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.6875 / 13.0625 / -0.014683377411630418 / 0.7898696349203141 | [NPY](tensors/0001543.npy) |
| 1544 | `model.layers.0.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.125 / 5.03125 / 0.11328548192977905 / 1.200509079937128 | [NPY](tensors/0001544.npy) |
| 1545 | `model.layers.0.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.09375 / 3.078125 / 0.02940140393366164 / 0.500803250499923 | [NPY](tensors/0001545.npy) |
| 1546 | `model.layers.0.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.25 / 39.0 / 0.032157751421133675 / 1.1346195487156185 | [NPY](tensors/0001546.npy) |
| 1547 | `model.layers.0.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.25 / 39.0 / 0.032157751421133675 / 1.1346195487156185 | [NPY](tensors/0001547.npy) |
| 1548 | `model.layers.0.self_attn` | 13 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0028864621921437005 / 0.0332745767098256 | [NPY](tensors/0001548.npy) |
| 1549 | `model.layers.0.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 36.25 / 0.015997706519232855 / 2.812325883816368 | [NPY](tensors/0001549.npy) |
| 1550 | `model.layers.0.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.25 / 1.875 / -0.011744971407784357 / 0.37597590874603565 | [NPY](tensors/0001550.npy) |
| 1551 | `model.layers.0.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.25 / 1.875 / -0.011744971407784357 / 0.37597590874603565 | [NPY](tensors/0001551.npy) |
| 1552 | `model.layers.0.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.25 / 1.875 / -0.011744971407784357 / 0.37597590874603565 | [NPY](tensors/0001552.npy) |
| 1553 | `model.layers.0.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1554 | `model.layers.0.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1555 | `model.layers.0.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1556 | `model.layers.0.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.9375 / 27.25 / 0.018315114825963975 / 0.7870424890181039 | [NPY](tensors/0001556.npy) |
| 1557 | `model.layers.0.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.9375 / 27.25 / 0.018315114825963975 / 0.7870424890181039 | [NPY](tensors/0001557.npy) |
| 1558 | `model.layers.0.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.890625 / 1.9375 / -0.03949546813964844 / 1.0293222698122055 | [NPY](tensors/0001558.npy) |
| 1559 | `model.layers.0` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 61.0 / 0.03435822592841254 / 3.174101850193418 | [NPY](tensors/0001559.npy) |
| 1638 | `model.layers.0` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001638.npy) |
| 1639 | `model.layers.0` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001639.npy) |
| 1640 | `model.layers.0` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0001640.npy) |
| 1641 | `model.layers.0` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0001641.npy) |
| 1642 | `model.layers.0` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0001642.npy) |
| 1643 | `model.layers.0` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1644 | `model.layers.0` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1645 | `model.layers.0` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1646 | `model.layers.0.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001646.npy) |
| 1647 | `model.layers.0.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001647.npy) |
| 1648 | `model.layers.0.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001648.npy) |
| 1649 | `model.layers.0.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001649.npy) |
| 1650 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0001650.npy) |
| 1651 | `model.layers.0.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1652 | `model.layers.0.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1653 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0001653.npy) |
| 1654 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0001654.npy) |
| 1655 | `model.layers.0.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1656 | `model.layers.0.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001656.npy) |
| 1657 | `model.layers.0.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.84375 / 8.5625 / 0.0153301190584898 / 1.0113524420299036 | [NPY](tensors/0001657.npy) |
| 1658 | `model.layers.0.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001658.npy) |
| 1659 | `model.layers.0.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.0 / 65.5 / 0.032654017210006714 / 6.89507515667232 | [NPY](tensors/0001659.npy) |
| 1660 | `model.layers.0.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001660.npy) |
| 1661 | `model.layers.0.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.28125 / 3.390625 / -0.002120666205883026 / 0.8566653376613583 | [NPY](tensors/0001661.npy) |
| 1662 | `model.layers.0.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.40625 / 3.578125 / 0.017114069778472185 / 0.4601071362923662 | [NPY](tensors/0001662.npy) |
| 1663 | `model.layers.0.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.9375 / 28.375 / 0.02737923264503479 / 0.9929831109688557 | [NPY](tensors/0001663.npy) |
| 1664 | `model.layers.0.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.9375 / 28.375 / 0.02737923264503479 / 0.9929831109688557 | [NPY](tensors/0001664.npy) |
| 1665 | `model.layers.0.self_attn` | 14 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0033727230104186054 / 0.0331496900611369 | [NPY](tensors/0001665.npy) |
| 1666 | `model.layers.0.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.75 / 32.5 / 0.025291612413194445 / 2.9521926364674798 | [NPY](tensors/0001666.npy) |
| 1667 | `model.layers.0.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.4453125 / -0.0020524813069237604 / 0.2919349309540397 | [NPY](tensors/0001667.npy) |
| 1668 | `model.layers.0.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.4453125 / -0.0020524813069237604 / 0.2919349309540397 | [NPY](tensors/0001668.npy) |
| 1669 | `model.layers.0.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.4453125 / -0.0020524813069237604 / 0.2919349309540397 | [NPY](tensors/0001669.npy) |
| 1670 | `model.layers.0.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1671 | `model.layers.0.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1672 | `model.layers.0.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1673 | `model.layers.0.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.3125 / 12.6875 / 0.020128098668323623 / 0.673020822114282 | [NPY](tensors/0001673.npy) |
| 1674 | `model.layers.0.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.3125 / 12.6875 / 0.020128098668323623 / 0.673020822114282 | [NPY](tensors/0001674.npy) |
| 1675 | `model.layers.0.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.03125 / 2.96875 / -0.023748397827148438 / 1.5072959602346114 | [NPY](tensors/0001675.npy) |
| 1676 | `model.layers.0` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.625 / 44.25 / 0.04538866678873698 / 2.874474815047036 | [NPY](tensors/0001676.npy) |
| 1755 | `model.layers.0` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 32.75 / 0.03959848284721375 / 2.636727096419094 | [NPY](tensors/0001755.npy) |
| 1756 | `model.layers.0` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001756.npy) |
| 1757 | `model.layers.0` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0001757.npy) |
| 1758 | `model.layers.0` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0001758.npy) |
| 1759 | `model.layers.0` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0001759.npy) |
| 1760 | `model.layers.0` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1761 | `model.layers.0` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1762 | `model.layers.0` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1763 | `model.layers.0.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 32.75 / 0.03959848284721375 / 2.636727096419094 | [NPY](tensors/0001763.npy) |
| 1764 | `model.layers.0.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0001764.npy) |
| 1765 | `model.layers.0.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0001765.npy) |
| 1766 | `model.layers.0.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001766.npy) |
| 1767 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0001767.npy) |
| 1768 | `model.layers.0.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1769 | `model.layers.0.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1770 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0001770.npy) |
| 1771 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0001771.npy) |
| 1772 | `model.layers.0.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1773 | `model.layers.0.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0001773.npy) |
| 1774 | `model.layers.0.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.0625 / 6.78125 / -0.006842018279712647 / 0.8517376388261615 | [NPY](tensors/0001774.npy) |
| 1775 | `model.layers.0.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0001775.npy) |
| 1776 | `model.layers.0.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.25 / 35.75 / 0.051442623138427734 / 3.999531927842787 | [NPY](tensors/0001776.npy) |
| 1777 | `model.layers.0.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0001777.npy) |
| 1778 | `model.layers.0.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 4.625 / 0.04163137078285217 / 1.1435466539669636 | [NPY](tensors/0001778.npy) |
| 1779 | `model.layers.0.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.03125 / 2.546875 / 0.006667460309472517 / 0.3519127769157313 | [NPY](tensors/0001779.npy) |
| 1780 | `model.layers.0.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.625 / 40.75 / 0.030368029057151743 / 1.1964032841064776 | [NPY](tensors/0001780.npy) |
| 1781 | `model.layers.0.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.625 / 40.75 / 0.030368029057151743 / 1.1964032841064776 | [NPY](tensors/0001781.npy) |
| 1782 | `model.layers.0.self_attn` | 15 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9453125 / 0.0027096287992641275 / 0.02510720991466303 | [NPY](tensors/0001782.npy) |
| 1783 | `model.layers.0.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.0 / 40.5 / 0.07000039948357475 / 2.9111448801439157 | [NPY](tensors/0001783.npy) |
| 1784 | `model.layers.0.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.28125 / 1.71875 / -0.0012085927857293022 / 0.3718545801967993 | [NPY](tensors/0001784.npy) |
| 1785 | `model.layers.0.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.28125 / 1.71875 / -0.0012085927857293022 / 0.3718545801967993 | [NPY](tensors/0001785.npy) |
| 1786 | `model.layers.0.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.28125 / 1.71875 / -0.0012085927857293022 / 0.3718545801967993 | [NPY](tensors/0001786.npy) |
| 1787 | `model.layers.0.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1788 | `model.layers.0.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1789 | `model.layers.0.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1790 | `model.layers.0.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.5 / 21.5 / 0.03766595953040653 / 0.8356784521575863 | [NPY](tensors/0001790.npy) |
| 1791 | `model.layers.0.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.5 / 21.5 / 0.03766595953040653 / 0.8356784521575863 | [NPY](tensors/0001791.npy) |
| 1792 | `model.layers.0.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6171875 / 1.640625 / -0.2007598876953125 / 0.7728744187191577 | [NPY](tensors/0001792.npy) |
| 1793 | `model.layers.0` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 62.0 / 0.1076762146419949 / 3.3557700528747 | [NPY](tensors/0001793.npy) |
| 1872 | `model.layers.0` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 32.5 / 0.02340112761594355 / 2.5180141341639093 | [NPY](tensors/0001872.npy) |
| 1873 | `model.layers.0` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001873.npy) |
| 1874 | `model.layers.0` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0001874.npy) |
| 1875 | `model.layers.0` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0001875.npy) |
| 1876 | `model.layers.0` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0001876.npy) |
| 1877 | `model.layers.0` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1878 | `model.layers.0` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1879 | `model.layers.0` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1880 | `model.layers.0.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 32.5 / 0.02340112761594355 / 2.5180141341639093 | [NPY](tensors/0001880.npy) |
| 1881 | `model.layers.0.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0001881.npy) |
| 1882 | `model.layers.0.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0001882.npy) |
| 1883 | `model.layers.0.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001883.npy) |
| 1884 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0001884.npy) |
| 1885 | `model.layers.0.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1886 | `model.layers.0.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1887 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0001887.npy) |
| 1888 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0001888.npy) |
| 1889 | `model.layers.0.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1890 | `model.layers.0.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0001890.npy) |
| 1891 | `model.layers.0.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.4375 / 5.40625 / -0.007190447126049548 / 0.8410779943508924 | [NPY](tensors/0001891.npy) |
| 1892 | `model.layers.0.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0001892.npy) |
| 1893 | `model.layers.0.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.375 / 29.25 / -0.0019535720348358154 / 3.219451134212101 | [NPY](tensors/0001893.npy) |
| 1894 | `model.layers.0.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0001894.npy) |
| 1895 | `model.layers.0.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.71875 / 3.5625 / -0.03649583458900452 / 1.2017397564519863 | [NPY](tensors/0001895.npy) |
| 1896 | `model.layers.0.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.03125 / 3.796875 / 0.017060451878933236 / 0.498082563717334 | [NPY](tensors/0001896.npy) |
| 1897 | `model.layers.0.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.5 / 44.75 / 0.02595855695092016 / 1.3930114225808146 | [NPY](tensors/0001897.npy) |
| 1898 | `model.layers.0.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.5 / 44.75 / 0.02595855695092016 / 1.3930114225808146 | [NPY](tensors/0001898.npy) |
| 1899 | `model.layers.0.self_attn` | 16 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9453125 / 0.0035097606085510097 / 0.032088155128689136 | [NPY](tensors/0001899.npy) |
| 1900 | `model.layers.0.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.5 / 46.75 / 0.04923784997728136 / 2.9465190527731084 | [NPY](tensors/0001900.npy) |
| 1901 | `model.layers.0.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.140625 / 1.640625 / -0.006186474280224906 / 0.37582994151814736 | [NPY](tensors/0001901.npy) |
| 1902 | `model.layers.0.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.140625 / 1.640625 / -0.006186474280224906 / 0.37582994151814736 | [NPY](tensors/0001902.npy) |
| 1903 | `model.layers.0.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.140625 / 1.640625 / -0.006186474280224906 / 0.37582994151814736 | [NPY](tensors/0001903.npy) |
| 1904 | `model.layers.0.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1905 | `model.layers.0.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1906 | `model.layers.0.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1907 | `model.layers.0.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.4375 / 5.65625 / 0.01758215741978751 / 0.45244068033718965 | [NPY](tensors/0001907.npy) |
| 1908 | `model.layers.0.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.4375 / 5.65625 / 0.01758215741978751 / 0.45244068033718965 | [NPY](tensors/0001908.npy) |
| 1909 | `model.layers.0.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6875 / 1.2734375 / -0.18764495849609375 / 0.7085555880662323 | [NPY](tensors/0001909.npy) |
| 1910 | `model.layers.0` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 50.25 / 0.06696223815282186 / 3.1153656572762545 | [NPY](tensors/0001910.npy) |
| 1989 | `model.layers.0` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.25 / 32.0 / 0.061791101429197526 / 2.238756913453412 | [NPY](tensors/0001989.npy) |
| 1990 | `model.layers.0` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001990.npy) |
| 1991 | `model.layers.0` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0001991.npy) |
| 1992 | `model.layers.0` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0001992.npy) |
| 1993 | `model.layers.0` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0001993.npy) |
| 1994 | `model.layers.0` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1995 | `model.layers.0` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1996 | `model.layers.0` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1997 | `model.layers.0.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.25 / 32.0 / 0.061791101429197526 / 2.238756913453412 | [NPY](tensors/0001997.npy) |
| 1998 | `model.layers.0.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0001998.npy) |
| 1999 | `model.layers.0.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0001999.npy) |
| 2000 | `model.layers.0.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002000.npy) |
| 2001 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0002001.npy) |
| 2002 | `model.layers.0.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2003 | `model.layers.0.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2004 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0002004.npy) |
| 2005 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0002005.npy) |
| 2006 | `model.layers.0.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2007 | `model.layers.0.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002007.npy) |
| 2008 | `model.layers.0.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.375 / 8.125 / 0.007972375839017332 / 1.0483744761991842 | [NPY](tensors/0002008.npy) |
| 2009 | `model.layers.0.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002009.npy) |
| 2010 | `model.layers.0.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.0 / 52.0 / -0.06352853029966354 / 5.834851084637073 | [NPY](tensors/0002010.npy) |
| 2011 | `model.layers.0.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002011.npy) |
| 2012 | `model.layers.0.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.75 / 4.5 / 0.031710169510915875 / 1.4942407070139319 | [NPY](tensors/0002012.npy) |
| 2013 | `model.layers.0.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.6875 / 3.546875 / -0.011923462094273418 / 0.6977389448879794 | [NPY](tensors/0002013.npy) |
| 2014 | `model.layers.0.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.5 / 39.5 / 0.011506854742765426 / 1.2449806123232918 | [NPY](tensors/0002014.npy) |
| 2015 | `model.layers.0.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.5 / 39.5 / 0.011506854742765426 / 1.2449806123232918 | [NPY](tensors/0002015.npy) |
| 2016 | `model.layers.0.self_attn` | 17 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.004253253170460033 / 0.04434373223951033 | [NPY](tensors/0002016.npy) |
| 2017 | `model.layers.0.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.5 / 39.25 / 0.07328346835242378 / 2.596603925641119 | [NPY](tensors/0002017.npy) |
| 2018 | `model.layers.0.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.46875 / 1.875 / 0.005263302061292861 / 0.45437918613341394 | [NPY](tensors/0002018.npy) |
| 2019 | `model.layers.0.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.46875 / 1.875 / 0.005263302061292861 / 0.45437918613341394 | [NPY](tensors/0002019.npy) |
| 2020 | `model.layers.0.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.46875 / 1.875 / 0.005263302061292861 / 0.45437918613341394 | [NPY](tensors/0002020.npy) |
| 2021 | `model.layers.0.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2022 | `model.layers.0.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2023 | `model.layers.0.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2024 | `model.layers.0.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.8125 / 38.5 / 0.01867800313565466 / 1.2072000648340884 | [NPY](tensors/0002024.npy) |
| 2025 | `model.layers.0.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.8125 / 38.5 / 0.01867800313565466 / 1.2072000648340884 | [NPY](tensors/0002025.npy) |
| 2026 | `model.layers.0.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.25 / 1.8515625 / -0.16916275024414062 / 0.8053703788549557 | [NPY](tensors/0002026.npy) |
| 2027 | `model.layers.0` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.0 / 77.0 / 0.09194140169355604 / 3.272436926780782 | [NPY](tensors/0002027.npy) |
| 2106 | `model.layers.0` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0002106.npy) |
| 2107 | `model.layers.0` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002107.npy) |
| 2108 | `model.layers.0` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0002108.npy) |
| 2109 | `model.layers.0` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0002109.npy) |
| 2110 | `model.layers.0` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0002110.npy) |
| 2111 | `model.layers.0` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2112 | `model.layers.0` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2113 | `model.layers.0` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2114 | `model.layers.0.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0002114.npy) |
| 2115 | `model.layers.0.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002115.npy) |
| 2116 | `model.layers.0.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002116.npy) |
| 2117 | `model.layers.0.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002117.npy) |
| 2118 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0002118.npy) |
| 2119 | `model.layers.0.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2120 | `model.layers.0.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2121 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0002121.npy) |
| 2122 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0002122.npy) |
| 2123 | `model.layers.0.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2124 | `model.layers.0.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002124.npy) |
| 2125 | `model.layers.0.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.34375 / 8.125 / 0.009809806477278471 / 1.0602451281469458 | [NPY](tensors/0002125.npy) |
| 2126 | `model.layers.0.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002126.npy) |
| 2127 | `model.layers.0.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.5 / 52.75 / 0.05987404379993677 / 5.486411371880323 | [NPY](tensors/0002127.npy) |
| 2128 | `model.layers.0.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0002128.npy) |
| 2129 | `model.layers.0.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.125 / 3.75 / 0.02330493927001953 / 1.1486258589347933 | [NPY](tensors/0002129.npy) |
| 2130 | `model.layers.0.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0625 / 3.96875 / 0.00595811108360067 / 0.7149018666285083 | [NPY](tensors/0002130.npy) |
| 2131 | `model.layers.0.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.5 / 42.0 / 0.032514481743176775 / 1.2757230710907392 | [NPY](tensors/0002131.npy) |
| 2132 | `model.layers.0.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.5 / 42.0 / 0.032514481743176775 / 1.2757230710907392 | [NPY](tensors/0002132.npy) |
| 2133 | `model.layers.0.self_attn` | 18 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.00451912601425056 / 0.04522838416613795 | [NPY](tensors/0002133.npy) |
| 2134 | `model.layers.0.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.5 / 46.5 / -0.031477795706854925 / 2.825169726333271 | [NPY](tensors/0002134.npy) |
| 2135 | `model.layers.0.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.015625 / 1.578125 / 0.0005250205596288045 / 0.40101286734093167 | [NPY](tensors/0002135.npy) |
| 2136 | `model.layers.0.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.015625 / 1.578125 / 0.0005250205596288045 / 0.40101286734093167 | [NPY](tensors/0002136.npy) |
| 2137 | `model.layers.0.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.015625 / 1.578125 / 0.0005250205596288045 / 0.40101286734093167 | [NPY](tensors/0002137.npy) |
| 2138 | `model.layers.0.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2139 | `model.layers.0.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2140 | `model.layers.0.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2141 | `model.layers.0.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.953125 / 23.0 / 0.017806630416048897 / 0.7191933911450429 | [NPY](tensors/0002141.npy) |
| 2142 | `model.layers.0.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.953125 / 23.0 / 0.017806630416048897 / 0.7191933911450429 | [NPY](tensors/0002142.npy) |
| 2143 | `model.layers.0.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9453125 / 1.9375 / -0.05558013916015625 / 0.8229564216232802 | [NPY](tensors/0002143.npy) |
| 2144 | `model.layers.0` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 69.5 / -0.013725916544596354 / 3.151998900635875 | [NPY](tensors/0002144.npy) |
| 2223 | `model.layers.0` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 34.75 / 0.06460592945416768 / 2.603620301499426 | [NPY](tensors/0002223.npy) |
| 2224 | `model.layers.0` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002224.npy) |
| 2225 | `model.layers.0` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0002225.npy) |
| 2226 | `model.layers.0` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0002226.npy) |
| 2227 | `model.layers.0` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0002227.npy) |
| 2228 | `model.layers.0` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2229 | `model.layers.0` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2230 | `model.layers.0` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2231 | `model.layers.0.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 34.75 / 0.06460592945416768 / 2.603620301499426 | [NPY](tensors/0002231.npy) |
| 2232 | `model.layers.0.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0002232.npy) |
| 2233 | `model.layers.0.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0002233.npy) |
| 2234 | `model.layers.0.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002234.npy) |
| 2235 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0002235.npy) |
| 2236 | `model.layers.0.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2237 | `model.layers.0.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2238 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0002238.npy) |
| 2239 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0002239.npy) |
| 2240 | `model.layers.0.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2241 | `model.layers.0.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0002241.npy) |
| 2242 | `model.layers.0.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.71875 / 8.4375 / 0.008836216118652374 / 1.127863321857116 | [NPY](tensors/0002242.npy) |
| 2243 | `model.layers.0.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0002243.npy) |
| 2244 | `model.layers.0.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -47.25 / 52.5 / -0.01974540948867798 / 5.528074362257702 | [NPY](tensors/0002244.npy) |
| 2245 | `model.layers.0.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0002245.npy) |
| 2246 | `model.layers.0.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.34375 / 5.1875 / 0.04988500475883484 / 1.3788012115777875 | [NPY](tensors/0002246.npy) |
| 2247 | `model.layers.0.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.09375 / 4.0 / -0.0017872754688141868 / 0.6005541698476173 | [NPY](tensors/0002247.npy) |
| 2248 | `model.layers.0.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.6875 / 42.75 / 0.029049541552861533 / 1.250576476077245 | [NPY](tensors/0002248.npy) |
| 2249 | `model.layers.0.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.6875 / 42.75 / 0.029049541552861533 / 1.250576476077245 | [NPY](tensors/0002249.npy) |
| 2250 | `model.layers.0.self_attn` | 19 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003166198382718346 / 0.03756498440562089 | [NPY](tensors/0002250.npy) |
| 2251 | `model.layers.0.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 41.75 / 0.09356221954027812 / 2.886620664974374 | [NPY](tensors/0002251.npy) |
| 2252 | `model.layers.0.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.78125 / 1.5625 / 0.002529639005661011 / 0.38727905045406325 | [NPY](tensors/0002252.npy) |
| 2253 | `model.layers.0.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.78125 / 1.5625 / 0.002529639005661011 / 0.38727905045406325 | [NPY](tensors/0002253.npy) |
| 2254 | `model.layers.0.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.78125 / 1.5625 / 0.002529639005661011 / 0.38727905045406325 | [NPY](tensors/0002254.npy) |
| 2255 | `model.layers.0.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2256 | `model.layers.0.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2257 | `model.layers.0.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2258 | `model.layers.0.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.9375 / 24.5 / 0.025961827900674608 / 0.7369993244860082 | [NPY](tensors/0002258.npy) |
| 2259 | `model.layers.0.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.9375 / 24.5 / 0.025961827900674608 / 0.7369993244860082 | [NPY](tensors/0002259.npy) |
| 2260 | `model.layers.0.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.4375 / 1.984375 / -0.2114391326904297 / 0.8510687784302264 | [NPY](tensors/0002260.npy) |
| 2261 | `model.layers.0` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 63.75 / 0.11964490678575304 / 3.1967435379360882 | [NPY](tensors/0002261.npy) |
| 2340 | `model.layers.0` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0002340.npy) |
| 2341 | `model.layers.0` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002341.npy) |
| 2342 | `model.layers.0` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0002342.npy) |
| 2343 | `model.layers.0` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0002343.npy) |
| 2344 | `model.layers.0` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0002344.npy) |
| 2345 | `model.layers.0` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2346 | `model.layers.0` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2347 | `model.layers.0` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2348 | `model.layers.0.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0002348.npy) |
| 2349 | `model.layers.0.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002349.npy) |
| 2350 | `model.layers.0.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002350.npy) |
| 2351 | `model.layers.0.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002351.npy) |
| 2352 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0002352.npy) |
| 2353 | `model.layers.0.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2354 | `model.layers.0.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2355 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0002355.npy) |
| 2356 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0002356.npy) |
| 2357 | `model.layers.0.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2358 | `model.layers.0.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002358.npy) |
| 2359 | `model.layers.0.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 9.25 / 0.06582052947487682 / 1.0317253511582722 | [NPY](tensors/0002359.npy) |
| 2360 | `model.layers.0.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002360.npy) |
| 2361 | `model.layers.0.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.5 / 59.75 / -0.027341485023498535 / 6.496414800406944 | [NPY](tensors/0002361.npy) |
| 2362 | `model.layers.0.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0002362.npy) |
| 2363 | `model.layers.0.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.453125 / 4.6875 / 0.06333106756210327 / 0.9556167387162166 | [NPY](tensors/0002363.npy) |
| 2364 | `model.layers.0.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.8125 / 4.5 / 0.010425757198390784 / 0.4772789765476881 | [NPY](tensors/0002364.npy) |
| 2365 | `model.layers.0.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.6875 / 35.75 / 0.023100559185776446 / 1.0570417097090252 | [NPY](tensors/0002365.npy) |
| 2366 | `model.layers.0.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.6875 / 35.75 / 0.023100559185776446 / 1.0570417097090252 | [NPY](tensors/0002366.npy) |
| 2367 | `model.layers.0.self_attn` | 20 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.00296960478385941 / 0.029938120684676956 | [NPY](tensors/0002367.npy) |
| 2368 | `model.layers.0.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.0 / 37.25 / 0.07219034565819635 / 2.6534155018837757 | [NPY](tensors/0002368.npy) |
| 2369 | `model.layers.0.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.484375 / 1.796875 / 0.004537834723790487 / 0.3196530655592586 | [NPY](tensors/0002369.npy) |
| 2370 | `model.layers.0.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.484375 / 1.796875 / 0.004537834723790487 / 0.3196530655592586 | [NPY](tensors/0002370.npy) |
| 2371 | `model.layers.0.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.484375 / 1.796875 / 0.004537834723790487 / 0.3196530655592586 | [NPY](tensors/0002371.npy) |
| 2372 | `model.layers.0.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2373 | `model.layers.0.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2374 | `model.layers.0.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2375 | `model.layers.0.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.96875 / 5.65625 / -0.003081254329946306 / 0.4496514977044279 | [NPY](tensors/0002375.npy) |
| 2376 | `model.layers.0.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.96875 / 5.65625 / -0.003081254329946306 / 0.4496514977044279 | [NPY](tensors/0002376.npy) |
| 2377 | `model.layers.0.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.8125 / 2.84375 / -0.13950443267822266 / 1.2202973944695312 | [NPY](tensors/0002377.npy) |
| 2378 | `model.layers.0` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 39.5 / 0.06905472278594971 / 2.629709667061886 | [NPY](tensors/0002378.npy) |
| 2457 | `model.layers.0` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.75 / 36.5 / -0.03277786038815975 / 2.7829041357151567 | [NPY](tensors/0002457.npy) |
| 2458 | `model.layers.0` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002458.npy) |
| 2459 | `model.layers.0` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0002459.npy) |
| 2460 | `model.layers.0` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0002460.npy) |
| 2461 | `model.layers.0` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0002461.npy) |
| 2462 | `model.layers.0` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2463 | `model.layers.0` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2464 | `model.layers.0` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2465 | `model.layers.0.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.75 / 36.5 / -0.03277786038815975 / 2.7829041357151567 | [NPY](tensors/0002465.npy) |
| 2466 | `model.layers.0.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002466.npy) |
| 2467 | `model.layers.0.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002467.npy) |
| 2468 | `model.layers.0.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002468.npy) |
| 2469 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0002469.npy) |
| 2470 | `model.layers.0.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2471 | `model.layers.0.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2472 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0002472.npy) |
| 2473 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0002473.npy) |
| 2474 | `model.layers.0.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2475 | `model.layers.0.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002475.npy) |
| 2476 | `model.layers.0.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0625 / 8.75 / 0.007699438836425543 / 0.9554901933770389 | [NPY](tensors/0002476.npy) |
| 2477 | `model.layers.0.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002477.npy) |
| 2478 | `model.layers.0.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.5 / 55.25 / -0.05697989463806152 / 6.049655579159513 | [NPY](tensors/0002478.npy) |
| 2479 | `model.layers.0.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0002479.npy) |
| 2480 | `model.layers.0.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -2.703125 / 3.4375 / 0.04050885885953903 / 0.8799544405823716 | [NPY](tensors/0002480.npy) |
| 2481 | `model.layers.0.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.609375 / 4.5625 / 0.009142040224105585 / 0.489754880588246 | [NPY](tensors/0002481.npy) |
| 2482 | `model.layers.0.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.5 / 28.5 / 0.02643406353890896 / 0.870105241247668 | [NPY](tensors/0002482.npy) |
| 2483 | `model.layers.0.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.5 / 28.5 / 0.02643406353890896 / 0.870105241247668 | [NPY](tensors/0002483.npy) |
| 2484 | `model.layers.0.self_attn` | 21 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.003256858453860829 / 0.03318923729447891 | [NPY](tensors/0002484.npy) |
| 2485 | `model.layers.0.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.0 / 37.0 / -0.006365357504950629 / 2.820364977324226 | [NPY](tensors/0002485.npy) |
| 2486 | `model.layers.0.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.15625 / 2.8125 / 0.003933474752638075 / 0.286852845974923 | [NPY](tensors/0002486.npy) |
| 2487 | `model.layers.0.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.15625 / 2.8125 / 0.003933474752638075 / 0.286852845974923 | [NPY](tensors/0002487.npy) |
| 2488 | `model.layers.0.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.15625 / 2.8125 / 0.003933474752638075 / 0.286852845974923 | [NPY](tensors/0002488.npy) |
| 2489 | `model.layers.0.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2490 | `model.layers.0.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2491 | `model.layers.0.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2492 | `model.layers.0.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.59375 / 9.75 / 0.011997236973709531 / 0.5166422952317411 | [NPY](tensors/0002492.npy) |
| 2493 | `model.layers.0.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.59375 / 9.75 / 0.011997236973709531 / 0.5166422952317411 | [NPY](tensors/0002493.npy) |
| 2494 | `model.layers.0.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.296875 / 1.625 / -0.0590667724609375 / 1.018561896150523 | [NPY](tensors/0002494.npy) |
| 2495 | `model.layers.0` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 36.75 / 0.005666187074449327 / 2.723496742650775 | [NPY](tensors/0002495.npy) |
| 2574 | `model.layers.0` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 25.375 / 0.03148116301745176 / 2.4913610061559237 | [NPY](tensors/0002574.npy) |
| 2575 | `model.layers.0` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002575.npy) |
| 2576 | `model.layers.0` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0002576.npy) |
| 2577 | `model.layers.0` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0002577.npy) |
| 2578 | `model.layers.0` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0002578.npy) |
| 2579 | `model.layers.0` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2580 | `model.layers.0` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2581 | `model.layers.0` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2582 | `model.layers.0.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 25.375 / 0.03148116301745176 / 2.4913610061559237 | [NPY](tensors/0002582.npy) |
| 2583 | `model.layers.0.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0002583.npy) |
| 2584 | `model.layers.0.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0002584.npy) |
| 2585 | `model.layers.0.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002585.npy) |
| 2586 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0002586.npy) |
| 2587 | `model.layers.0.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2588 | `model.layers.0.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2589 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0002589.npy) |
| 2590 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0002590.npy) |
| 2591 | `model.layers.0.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2592 | `model.layers.0.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0002592.npy) |
| 2593 | `model.layers.0.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.8125 / 9.875 / 0.001175960642285645 / 1.0708778134614567 | [NPY](tensors/0002593.npy) |
| 2594 | `model.layers.0.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0002594.npy) |
| 2595 | `model.layers.0.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.0 / 46.0 / -0.07610408216714859 / 5.694328378141193 | [NPY](tensors/0002595.npy) |
| 2596 | `model.layers.0.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0002596.npy) |
| 2597 | `model.layers.0.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.46875 / 6.09375 / -0.02648264169692993 / 1.4472391438112524 | [NPY](tensors/0002597.npy) |
| 2598 | `model.layers.0.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.03125 / 3.25 / 0.007885790149884997 / 0.4298525607810501 | [NPY](tensors/0002598.npy) |
| 2599 | `model.layers.0.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 42.0 / 0.020726909902360705 / 1.275864419027372 | [NPY](tensors/0002599.npy) |
| 2600 | `model.layers.0.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 42.0 / 0.020726909902360705 / 1.275864419027372 | [NPY](tensors/0002600.npy) |
| 2601 | `model.layers.0.self_attn` | 22 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0029567623287962406 / 0.03380769040818645 | [NPY](tensors/0002601.npy) |
| 2602 | `model.layers.0.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 43.0 / 0.05221103032430013 / 2.899438869372947 | [NPY](tensors/0002602.npy) |
| 2603 | `model.layers.0.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.28125 / 1.4765625 / 0.006196146210034688 / 0.363481331340924 | [NPY](tensors/0002603.npy) |
| 2604 | `model.layers.0.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.28125 / 1.4765625 / 0.006196146210034688 / 0.363481331340924 | [NPY](tensors/0002604.npy) |
| 2605 | `model.layers.0.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -5.28125 / 1.4765625 / 0.006196146210034688 / 0.363481331340924 | [NPY](tensors/0002605.npy) |
| 2606 | `model.layers.0.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2607 | `model.layers.0.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2608 | `model.layers.0.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2609 | `model.layers.0.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.984375 / 13.3125 / 0.020435340971582467 / 0.4829496514873178 | [NPY](tensors/0002609.npy) |
| 2610 | `model.layers.0.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.984375 / 13.3125 / 0.020435340971582467 / 0.4829496514873178 | [NPY](tensors/0002610.npy) |
| 2611 | `model.layers.0.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.21875 / 2.140625 / -0.2017974853515625 / 0.816916610108161 | [NPY](tensors/0002611.npy) |
| 2612 | `model.layers.0` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 55.25 / 0.07258157200283474 / 3.155635268337133 | [NPY](tensors/0002612.npy) |
| 2691 | `model.layers.0` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.25 / 22.875 / 0.02578953950562411 / 2.1256093624936447 | [NPY](tensors/0002691.npy) |
| 2692 | `model.layers.0` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002692.npy) |
| 2693 | `model.layers.0` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0002693.npy) |
| 2694 | `model.layers.0` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0002694.npy) |
| 2695 | `model.layers.0` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0002695.npy) |
| 2696 | `model.layers.0` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2697 | `model.layers.0` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2698 | `model.layers.0` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2699 | `model.layers.0.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.25 / 22.875 / 0.02578953950562411 / 2.1256093624936447 | [NPY](tensors/0002699.npy) |
| 2700 | `model.layers.0.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0002700.npy) |
| 2701 | `model.layers.0.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0002701.npy) |
| 2702 | `model.layers.0.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002702.npy) |
| 2703 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0002703.npy) |
| 2704 | `model.layers.0.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2705 | `model.layers.0.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2706 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0002706.npy) |
| 2707 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0002707.npy) |
| 2708 | `model.layers.0.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2709 | `model.layers.0.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0002709.npy) |
| 2710 | `model.layers.0.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.8125 / 7.9375 / -0.014699231367558241 / 1.1007098219776468 | [NPY](tensors/0002710.npy) |
| 2711 | `model.layers.0.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0002711.npy) |
| 2712 | `model.layers.0.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.25 / 55.25 / 0.1305762529373169 / 5.5847358405435745 | [NPY](tensors/0002712.npy) |
| 2713 | `model.layers.0.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0002713.npy) |
| 2714 | `model.layers.0.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.21875 / 5.84375 / -0.07473260164260864 / 1.5255124313159032 | [NPY](tensors/0002714.npy) |
| 2715 | `model.layers.0.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.4375 / 6.09375 / -0.001973583610379137 / 0.8141080087048616 | [NPY](tensors/0002715.npy) |
| 2716 | `model.layers.0.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 46.25 / 0.038691397507985434 / 1.485181314633634 | [NPY](tensors/0002716.npy) |
| 2717 | `model.layers.0.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 46.25 / 0.038691397507985434 / 1.485181314633634 | [NPY](tensors/0002717.npy) |
| 2718 | `model.layers.0.self_attn` | 23 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0038994581940746077 / 0.04632432942471369 | [NPY](tensors/0002718.npy) |
| 2719 | `model.layers.0.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 49.0 / 0.06446217430962456 / 2.7123778417970428 | [NPY](tensors/0002719.npy) |
| 2720 | `model.layers.0.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.625 / 1.7265625 / 0.01019052267074585 / 0.4627561142097228 | [NPY](tensors/0002720.npy) |
| 2721 | `model.layers.0.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.625 / 1.7265625 / 0.01019052267074585 / 0.4627561142097228 | [NPY](tensors/0002721.npy) |
| 2722 | `model.layers.0.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.625 / 1.7265625 / 0.01019052267074585 / 0.4627561142097228 | [NPY](tensors/0002722.npy) |
| 2723 | `model.layers.0.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2724 | `model.layers.0.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2725 | `model.layers.0.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2726 | `model.layers.0.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -18.25 / 40.25 / 0.009369334247377183 / 1.3848605169565562 | [NPY](tensors/0002726.npy) |
| 2727 | `model.layers.0.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.25 / 40.25 / 0.009369334247377183 / 1.3848605169565562 | [NPY](tensors/0002727.npy) |
| 2728 | `model.layers.0.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9765625 / 2.453125 / -0.052734375 / 0.8182748828324817 | [NPY](tensors/0002728.npy) |
| 2729 | `model.layers.0` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.5 / 89.0 / 0.073930295308431 / 3.521519430458359 | [NPY](tensors/0002729.npy) |
| 2808 | `model.layers.0` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 89.0 / 0.026544343266222212 / 4.541275344485995 | [NPY](tensors/0002808.npy) |
| 2809 | `model.layers.0` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002809.npy) |
| 2810 | `model.layers.0` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0002810.npy) |
| 2811 | `model.layers.0` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0002811.npy) |
| 2812 | `model.layers.0` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0002812.npy) |
| 2813 | `model.layers.0` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2814 | `model.layers.0` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2815 | `model.layers.0` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2816 | `model.layers.0.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 89.0 / 0.026544343266222212 / 4.541275344485995 | [NPY](tensors/0002816.npy) |
| 2817 | `model.layers.0.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0002817.npy) |
| 2818 | `model.layers.0.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0002818.npy) |
| 2819 | `model.layers.0.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002819.npy) |
| 2820 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0002820.npy) |
| 2821 | `model.layers.0.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2822 | `model.layers.0.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2823 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0002823.npy) |
| 2824 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0002824.npy) |
| 2825 | `model.layers.0.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2826 | `model.layers.0.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0002826.npy) |
| 2827 | `model.layers.0.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.875 / 7.84375 / 0.015290047216694802 / 0.914624676971129 | [NPY](tensors/0002827.npy) |
| 2828 | `model.layers.0.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0002828.npy) |
| 2829 | `model.layers.0.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.25 / 34.5 / -0.11417865753173828 / 4.434976879466014 | [NPY](tensors/0002829.npy) |
| 2830 | `model.layers.0.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0002830.npy) |
| 2831 | `model.layers.0.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.03125 / 4.8125 / -0.07233588397502899 / 1.0561324517062678 | [NPY](tensors/0002831.npy) |
| 2832 | `model.layers.0.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.09375 / 5.71875 / -0.039548337925225496 / 0.7995614568875714 | [NPY](tensors/0002832.npy) |
| 2833 | `model.layers.0.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.875 / 26.875 / 0.02775735424624549 / 1.1559588802831386 | [NPY](tensors/0002833.npy) |
| 2834 | `model.layers.0.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.875 / 26.875 / 0.02775735424624549 / 1.1559588802831386 | [NPY](tensors/0002834.npy) |
| 2835 | `model.layers.0.self_attn` | 24 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0041322696940237855 / 0.04403385448448412 | [NPY](tensors/0002835.npy) |
| 2836 | `model.layers.0.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -56.5 / 66.0 / 0.05421184433831109 / 4.0272481956059565 | [NPY](tensors/0002836.npy) |
| 2837 | `model.layers.0.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.03125 / 2.171875 / 0.009058142370647854 / 0.2858963374801823 | [NPY](tensors/0002837.npy) |
| 2838 | `model.layers.0.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.03125 / 2.171875 / 0.009058142370647854 / 0.2858963374801823 | [NPY](tensors/0002838.npy) |
| 2839 | `model.layers.0.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.03125 / 2.171875 / 0.009058142370647854 / 0.2858963374801823 | [NPY](tensors/0002839.npy) |
| 2840 | `model.layers.0.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2841 | `model.layers.0.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2842 | `model.layers.0.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2843 | `model.layers.0.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -29.375 / 25.375 / 0.023782263778977925 / 1.312062842324771 | [NPY](tensors/0002843.npy) |
| 2844 | `model.layers.0.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 25.375 / 0.023782263778977925 / 1.312062842324771 | [NPY](tensors/0002844.npy) |
| 2845 | `model.layers.0.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.703125 / 2.90625 / -0.17659759521484375 / 0.8633670626348343 | [NPY](tensors/0002845.npy) |
| 2846 | `model.layers.0` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 56.5 / 0.0781082895067003 / 3.5354693437085034 | [NPY](tensors/0002846.npy) |
| 2925 | `model.layers.0` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0002925.npy) |
| 2926 | `model.layers.0` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002926.npy) |
| 2927 | `model.layers.0` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0002927.npy) |
| 2928 | `model.layers.0` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0002928.npy) |
| 2929 | `model.layers.0` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0002929.npy) |
| 2930 | `model.layers.0` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2931 | `model.layers.0` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2932 | `model.layers.0` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2933 | `model.layers.0.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0002933.npy) |
| 2934 | `model.layers.0.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0002934.npy) |
| 2935 | `model.layers.0.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0002935.npy) |
| 2936 | `model.layers.0.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002936.npy) |
| 2937 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0002937.npy) |
| 2938 | `model.layers.0.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2939 | `model.layers.0.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2940 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0002940.npy) |
| 2941 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0002941.npy) |
| 2942 | `model.layers.0.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2943 | `model.layers.0.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0002943.npy) |
| 2944 | `model.layers.0.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 7.625 / 0.011268170550465584 / 0.9167789321734896 | [NPY](tensors/0002944.npy) |
| 2945 | `model.layers.0.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0002945.npy) |
| 2946 | `model.layers.0.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 43.75 / 0.046514674089848995 / 4.791095594233786 | [NPY](tensors/0002946.npy) |
| 2947 | `model.layers.0.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0002947.npy) |
| 2948 | `model.layers.0.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.84375 / 4.125 / -0.01808762550354004 / 1.3178383551916408 | [NPY](tensors/0002948.npy) |
| 2949 | `model.layers.0.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.875 / 4.28125 / -0.009001446538604796 / 0.47706278784134537 | [NPY](tensors/0002949.npy) |
| 2950 | `model.layers.0.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.9375 / 35.75 / 0.028838919599850972 / 1.019347858606827 | [NPY](tensors/0002950.npy) |
| 2951 | `model.layers.0.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.9375 / 35.75 / 0.028838919599850972 / 1.019347858606827 | [NPY](tensors/0002951.npy) |
| 2952 | `model.layers.0.self_attn` | 25 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.0031477634727525928 / 0.028038560646412088 | [NPY](tensors/0002952.npy) |
| 2953 | `model.layers.0.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 37.5 / 0.01841988033718533 / 2.8179484966317454 | [NPY](tensors/0002953.npy) |
| 2954 | `model.layers.0.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.1875 / 1.9765625 / 0.007893586821026272 / 0.37896638921960346 | [NPY](tensors/0002954.npy) |
| 2955 | `model.layers.0.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.1875 / 1.9765625 / 0.007893586821026272 / 0.37896638921960346 | [NPY](tensors/0002955.npy) |
| 2956 | `model.layers.0.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.1875 / 1.9765625 / 0.007893586821026272 / 0.37896638921960346 | [NPY](tensors/0002956.npy) |
| 2957 | `model.layers.0.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2958 | `model.layers.0.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2959 | `model.layers.0.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2960 | `model.layers.0.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.125 / 18.625 / 0.02087321306268374 / 0.6073956821706648 | [NPY](tensors/0002960.npy) |
| 2961 | `model.layers.0.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.125 / 18.625 / 0.02087321306268374 / 0.6073956821706648 | [NPY](tensors/0002961.npy) |
| 2962 | `model.layers.0.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.09375 / 1.8984375 / -0.07153701782226562 / 0.643441190598709 | [NPY](tensors/0002962.npy) |
| 2963 | `model.layers.0` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.5 / 55.5 / 0.03941718737284342 / 3.089341918984771 | [NPY](tensors/0002963.npy) |
| 3042 | `model.layers.0` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 30.875 / -0.03053326966861884 / 2.629557572976096 | [NPY](tensors/0003042.npy) |
| 3043 | `model.layers.0` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003043.npy) |
| 3044 | `model.layers.0` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0003044.npy) |
| 3045 | `model.layers.0` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0003045.npy) |
| 3046 | `model.layers.0` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0003046.npy) |
| 3047 | `model.layers.0` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3048 | `model.layers.0` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3049 | `model.layers.0` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3050 | `model.layers.0.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 30.875 / -0.03053326966861884 / 2.629557572976096 | [NPY](tensors/0003050.npy) |
| 3051 | `model.layers.0.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003051.npy) |
| 3052 | `model.layers.0.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003052.npy) |
| 3053 | `model.layers.0.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003053.npy) |
| 3054 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0003054.npy) |
| 3055 | `model.layers.0.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3056 | `model.layers.0.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3057 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0003057.npy) |
| 3058 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0003058.npy) |
| 3059 | `model.layers.0.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3060 | `model.layers.0.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003060.npy) |
| 3061 | `model.layers.0.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 9.375 / -0.0057218477595597506 / 1.0817809599468158 | [NPY](tensors/0003061.npy) |
| 3062 | `model.layers.0.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003062.npy) |
| 3063 | `model.layers.0.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.75 / 60.25 / 0.21187177300453186 / 5.623456193541793 | [NPY](tensors/0003063.npy) |
| 3064 | `model.layers.0.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003064.npy) |
| 3065 | `model.layers.0.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.15625 / 3.484375 / -0.04266364127397537 / 1.132992277020041 | [NPY](tensors/0003065.npy) |
| 3066 | `model.layers.0.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.78125 / 4.09375 / -0.0010928944102488458 / 0.8161590420372273 | [NPY](tensors/0003066.npy) |
| 3067 | `model.layers.0.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.25 / 45.5 / 0.03465916117032369 / 1.3615725025327194 | [NPY](tensors/0003067.npy) |
| 3068 | `model.layers.0.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.25 / 45.5 / 0.03465916117032369 / 1.3615725025327194 | [NPY](tensors/0003068.npy) |
| 3069 | `model.layers.0.self_attn` | 26 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004746578604597801 / 0.0508159629608295 | [NPY](tensors/0003069.npy) |
| 3070 | `model.layers.0.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 49.5 / 0.004017215304904514 / 3.0002685960254367 | [NPY](tensors/0003070.npy) |
| 3071 | `model.layers.0.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.84375 / 1.6484375 / 0.005147383610407511 / 0.3987413361492744 | [NPY](tensors/0003071.npy) |
| 3072 | `model.layers.0.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.84375 / 1.6484375 / 0.005147383610407511 / 0.3987413361492744 | [NPY](tensors/0003072.npy) |
| 3073 | `model.layers.0.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.84375 / 1.6484375 / 0.005147383610407511 / 0.3987413361492744 | [NPY](tensors/0003073.npy) |
| 3074 | `model.layers.0.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3075 | `model.layers.0.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3076 | `model.layers.0.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3077 | `model.layers.0.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.5625 / 39.25 / 0.05333998435073429 / 1.2373153575033067 | [NPY](tensors/0003077.npy) |
| 3078 | `model.layers.0.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 39.25 / 0.05333998435073429 / 1.2373153575033067 | [NPY](tensors/0003078.npy) |
| 3079 | `model.layers.0.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.40625 / 1.609375 / -0.1375732421875 / 0.6304635232049338 | [NPY](tensors/0003079.npy) |
| 3080 | `model.layers.0` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 89.0 / 0.057541055149502224 / 3.6600611305978976 | [NPY](tensors/0003080.npy) |
| 3159 | `model.layers.0` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 29.875 / -0.024451741410626306 / 2.4041472308375256 | [NPY](tensors/0003159.npy) |
| 3160 | `model.layers.0` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003160.npy) |
| 3161 | `model.layers.0` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0003161.npy) |
| 3162 | `model.layers.0` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0003162.npy) |
| 3163 | `model.layers.0` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0003163.npy) |
| 3164 | `model.layers.0` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3165 | `model.layers.0` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3166 | `model.layers.0` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3167 | `model.layers.0.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 29.875 / -0.024451741410626306 / 2.4041472308375256 | [NPY](tensors/0003167.npy) |
| 3168 | `model.layers.0.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003168.npy) |
| 3169 | `model.layers.0.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003169.npy) |
| 3170 | `model.layers.0.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003170.npy) |
| 3171 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0003171.npy) |
| 3172 | `model.layers.0.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3173 | `model.layers.0.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3174 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0003174.npy) |
| 3175 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0003175.npy) |
| 3176 | `model.layers.0.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3177 | `model.layers.0.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003177.npy) |
| 3178 | `model.layers.0.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.96875 / 9.3125 / 0.013412588275969028 / 1.162217466520388 | [NPY](tensors/0003178.npy) |
| 3179 | `model.layers.0.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003179.npy) |
| 3180 | `model.layers.0.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.5 / 52.75 / 0.024785220623016357 / 5.9833002218429145 | [NPY](tensors/0003180.npy) |
| 3181 | `model.layers.0.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0003181.npy) |
| 3182 | `model.layers.0.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.8125 / 6.03125 / -0.03467495460063219 / 1.460652286605354 | [NPY](tensors/0003182.npy) |
| 3183 | `model.layers.0.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.0 / 2.796875 / -0.033361222378516686 / 0.5652204234860947 | [NPY](tensors/0003183.npy) |
| 3184 | `model.layers.0.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.375 / 45.5 / 0.020936136775546604 / 1.3426647892938477 | [NPY](tensors/0003184.npy) |
| 3185 | `model.layers.0.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.375 / 45.5 / 0.020936136775546604 / 1.3426647892938477 | [NPY](tensors/0003185.npy) |
| 3186 | `model.layers.0.self_attn` | 27 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003089980048807647 / 0.037418720323706085 | [NPY](tensors/0003186.npy) |
| 3187 | `model.layers.0.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 44.5 / -0.0035129388173421225 / 2.814399675893517 | [NPY](tensors/0003187.npy) |
| 3188 | `model.layers.0.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9609375 / 1.8984375 / 0.006871145963668823 / 0.3748404161790276 | [NPY](tensors/0003188.npy) |
| 3189 | `model.layers.0.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9609375 / 1.8984375 / 0.006871145963668823 / 0.3748404161790276 | [NPY](tensors/0003189.npy) |
| 3190 | `model.layers.0.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.9609375 / 1.8984375 / 0.006871145963668823 / 0.3748404161790276 | [NPY](tensors/0003190.npy) |
| 3191 | `model.layers.0.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3192 | `model.layers.0.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3193 | `model.layers.0.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3194 | `model.layers.0.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.6875 / 29.5 / 0.03180673056178623 / 0.9611829965990047 | [NPY](tensors/0003194.npy) |
| 3195 | `model.layers.0.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.6875 / 29.5 / 0.03180673056178623 / 0.9611829965990047 | [NPY](tensors/0003195.npy) |
| 3196 | `model.layers.0.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9375 / 1.984375 / -0.15375041961669922 / 0.7902692832595652 | [NPY](tensors/0003196.npy) |
| 3197 | `model.layers.0` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 73.5 / 0.02834606170654297 / 3.309156599620994 | [NPY](tensors/0003197.npy) |
| 3276 | `model.layers.0` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 35.0 / -0.0015044911040200128 / 2.4601390841825688 | [NPY](tensors/0003276.npy) |
| 3277 | `model.layers.0` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003277.npy) |
| 3278 | `model.layers.0` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0003278.npy) |
| 3279 | `model.layers.0` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0003279.npy) |
| 3280 | `model.layers.0` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0003280.npy) |
| 3281 | `model.layers.0` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3282 | `model.layers.0` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3283 | `model.layers.0` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3284 | `model.layers.0.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 35.0 / -0.0015044911040200128 / 2.4601390841825688 | [NPY](tensors/0003284.npy) |
| 3285 | `model.layers.0.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003285.npy) |
| 3286 | `model.layers.0.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003286.npy) |
| 3287 | `model.layers.0.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003287.npy) |
| 3288 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0003288.npy) |
| 3289 | `model.layers.0.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3290 | `model.layers.0.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3291 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0003291.npy) |
| 3292 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0003292.npy) |
| 3293 | `model.layers.0.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3294 | `model.layers.0.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003294.npy) |
| 3295 | `model.layers.0.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 6.875 / 0.0073078901041299105 / 1.018639785574501 | [NPY](tensors/0003295.npy) |
| 3296 | `model.layers.0.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003296.npy) |
| 3297 | `model.layers.0.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.0 / 49.0 / 0.1723565487191081 / 4.808040616212344 | [NPY](tensors/0003297.npy) |
| 3298 | `model.layers.0.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0003298.npy) |
| 3299 | `model.layers.0.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.8125 / 3.265625 / 0.014979145489633083 / 1.106498243297265 | [NPY](tensors/0003299.npy) |
| 3300 | `model.layers.0.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.59375 / 5.75 / -0.009083947983526741 / 0.7516459007599207 | [NPY](tensors/0003300.npy) |
| 3301 | `model.layers.0.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 44.75 / 0.025730385051833258 / 1.348436106518225 | [NPY](tensors/0003301.npy) |
| 3302 | `model.layers.0.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 44.75 / 0.025730385051833258 / 1.348436106518225 | [NPY](tensors/0003302.npy) |
| 3303 | `model.layers.0.self_attn` | 28 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.004107125369895092 / 0.04286032355842304 | [NPY](tensors/0003303.npy) |
| 3304 | `model.layers.0.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.375 / 42.75 / 0.024469688203599717 / 2.8352089855988805 | [NPY](tensors/0003304.npy) |
| 3305 | `model.layers.0.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.109375 / 2.234375 / -0.0016298353672027587 / 0.4241203296143931 | [NPY](tensors/0003305.npy) |
| 3306 | `model.layers.0.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.109375 / 2.234375 / -0.0016298353672027587 / 0.4241203296143931 | [NPY](tensors/0003306.npy) |
| 3307 | `model.layers.0.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.109375 / 2.234375 / -0.0016298353672027587 / 0.4241203296143931 | [NPY](tensors/0003307.npy) |
| 3308 | `model.layers.0.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3309 | `model.layers.0.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3310 | `model.layers.0.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3311 | `model.layers.0.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.5625 / 23.375 / 0.019606961806615194 / 1.0259913546173685 | [NPY](tensors/0003311.npy) |
| 3312 | `model.layers.0.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 23.375 / 0.019606961806615194 / 1.0259913546173685 | [NPY](tensors/0003312.npy) |
| 3313 | `model.layers.0.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.1875 / 1.96875 / -0.01372528076171875 / 1.2768252596873824 | [NPY](tensors/0003313.npy) |
| 3314 | `model.layers.0` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.5 / 65.0 / 0.04416491190592448 / 3.2269699487308157 | [NPY](tensors/0003314.npy) |
| 3393 | `model.layers.0` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 22.625 / -0.02912892893784576 / 2.1983857303463927 | [NPY](tensors/0003393.npy) |
| 3394 | `model.layers.0` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003394.npy) |
| 3395 | `model.layers.0` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0003395.npy) |
| 3396 | `model.layers.0` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0003396.npy) |
| 3397 | `model.layers.0` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0003397.npy) |
| 3398 | `model.layers.0` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3399 | `model.layers.0` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3400 | `model.layers.0` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3401 | `model.layers.0.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 22.625 / -0.02912892893784576 / 2.1983857303463927 | [NPY](tensors/0003401.npy) |
| 3402 | `model.layers.0.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003402.npy) |
| 3403 | `model.layers.0.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003403.npy) |
| 3404 | `model.layers.0.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003404.npy) |
| 3405 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0003405.npy) |
| 3406 | `model.layers.0.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3407 | `model.layers.0.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3408 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0003408.npy) |
| 3409 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0003409.npy) |
| 3410 | `model.layers.0.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3411 | `model.layers.0.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003411.npy) |
| 3412 | `model.layers.0.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.78125 / 0.008440272184088826 / 1.120452857679885 | [NPY](tensors/0003412.npy) |
| 3413 | `model.layers.0.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003413.npy) |
| 3414 | `model.layers.0.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.5 / 51.5 / 0.1618337631225586 / 5.774741101565946 | [NPY](tensors/0003414.npy) |
| 3415 | `model.layers.0.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0003415.npy) |
| 3416 | `model.layers.0.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.9375 / 4.875 / -0.08827418088912964 / 1.3724833169271258 | [NPY](tensors/0003416.npy) |
| 3417 | `model.layers.0.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.3125 / 5.25 / -0.014001668827859248 / 0.6584232230163326 | [NPY](tensors/0003417.npy) |
| 3418 | `model.layers.0.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.0 / 48.0 / 0.022484661390384037 / 1.513555964001909 | [NPY](tensors/0003418.npy) |
| 3419 | `model.layers.0.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.0 / 48.0 / 0.022484661390384037 / 1.513555964001909 | [NPY](tensors/0003419.npy) |
| 3420 | `model.layers.0.self_attn` | 29 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0037842970641978916 / 0.04163755734133608 | [NPY](tensors/0003420.npy) |
| 3421 | `model.layers.0.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.5 / 54.5 / -0.006618437502119276 / 2.859105970168712 | [NPY](tensors/0003421.npy) |
| 3422 | `model.layers.0.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.625 / 1.828125 / 0.0036557131343417696 / 0.3630763869968306 | [NPY](tensors/0003422.npy) |
| 3423 | `model.layers.0.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.625 / 1.828125 / 0.0036557131343417696 / 0.3630763869968306 | [NPY](tensors/0003423.npy) |
| 3424 | `model.layers.0.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.625 / 1.828125 / 0.0036557131343417696 / 0.3630763869968306 | [NPY](tensors/0003424.npy) |
| 3425 | `model.layers.0.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3426 | `model.layers.0.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3427 | `model.layers.0.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3428 | `model.layers.0.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.625 / 26.0 / 0.0294959026388824 / 0.9126837626907829 | [NPY](tensors/0003428.npy) |
| 3429 | `model.layers.0.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.625 / 26.0 / 0.0294959026388824 / 0.9126837626907829 | [NPY](tensors/0003429.npy) |
| 3430 | `model.layers.0.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.234375 / 1.75 / -0.07578659057617188 / 0.7308643965669518 | [NPY](tensors/0003430.npy) |
| 3431 | `model.layers.0` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 76.0 / 0.022759829627143013 / 3.1344519684284777 | [NPY](tensors/0003431.npy) |
| 3510 | `model.layers.0` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0003510.npy) |
| 3511 | `model.layers.0` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003511.npy) |
| 3512 | `model.layers.0` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0003512.npy) |
| 3513 | `model.layers.0` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0003513.npy) |
| 3514 | `model.layers.0` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0003514.npy) |
| 3515 | `model.layers.0` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3516 | `model.layers.0` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3517 | `model.layers.0` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3518 | `model.layers.0.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0003518.npy) |
| 3519 | `model.layers.0.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003519.npy) |
| 3520 | `model.layers.0.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003520.npy) |
| 3521 | `model.layers.0.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003521.npy) |
| 3522 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0003522.npy) |
| 3523 | `model.layers.0.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3524 | `model.layers.0.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3525 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0003525.npy) |
| 3526 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0003526.npy) |
| 3527 | `model.layers.0.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3528 | `model.layers.0.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003528.npy) |
| 3529 | `model.layers.0.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 8.0 / 0.0014486645814031363 / 1.027321203413773 | [NPY](tensors/0003529.npy) |
| 3530 | `model.layers.0.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003530.npy) |
| 3531 | `model.layers.0.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.75 / 53.75 / 0.06940409168601036 / 5.734687316339554 | [NPY](tensors/0003531.npy) |
| 3532 | `model.layers.0.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003532.npy) |
| 3533 | `model.layers.0.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.8125 / 3.75 / -0.006423294544219971 / 0.9290448609736645 | [NPY](tensors/0003533.npy) |
| 3534 | `model.layers.0.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.09375 / 4.5625 / -0.0033674720780254574 / 0.6763463907390865 | [NPY](tensors/0003534.npy) |
| 3535 | `model.layers.0.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.875 / 35.0 / 0.02521000686619017 / 1.1162410012977066 | [NPY](tensors/0003535.npy) |
| 3536 | `model.layers.0.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.875 / 35.0 / 0.02521000686619017 / 1.1162410012977066 | [NPY](tensors/0003536.npy) |
| 3537 | `model.layers.0.self_attn` | 30 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004255426897494127 / 0.045270963903706087 | [NPY](tensors/0003537.npy) |
| 3538 | `model.layers.0.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.0 / 35.5 / -0.06595347192552355 / 2.934023999536777 | [NPY](tensors/0003538.npy) |
| 3539 | `model.layers.0.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 1.515625 / 0.0005772143602371215 / 0.3479559918854443 | [NPY](tensors/0003539.npy) |
| 3540 | `model.layers.0.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 1.515625 / 0.0005772143602371215 / 0.3479559918854443 | [NPY](tensors/0003540.npy) |
| 3541 | `model.layers.0.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 1.515625 / 0.0005772143602371215 / 0.3479559918854443 | [NPY](tensors/0003541.npy) |
| 3542 | `model.layers.0.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3543 | `model.layers.0.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3544 | `model.layers.0.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3545 | `model.layers.0.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.1875 / 13.5 / 0.021401390681664148 / 0.5399670385392845 | [NPY](tensors/0003545.npy) |
| 3546 | `model.layers.0.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.1875 / 13.5 / 0.021401390681664148 / 0.5399670385392845 | [NPY](tensors/0003546.npy) |
| 3547 | `model.layers.0.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.5625 / 1.5390625 / 0.0216064453125 / 1.3881460608078806 | [NPY](tensors/0003547.npy) |
| 3548 | `model.layers.0` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 38.75 / -0.04454614321390788 / 2.898914111854661 | [NPY](tensors/0003548.npy) |
| 3627 | `model.layers.0` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 30.0 / -0.032196171374784574 / 2.820171892718441 | [NPY](tensors/0003627.npy) |
| 3628 | `model.layers.0` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003628.npy) |
| 3629 | `model.layers.0` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0003629.npy) |
| 3630 | `model.layers.0` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0003630.npy) |
| 3631 | `model.layers.0` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0003631.npy) |
| 3632 | `model.layers.0` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3633 | `model.layers.0` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3634 | `model.layers.0` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3635 | `model.layers.0.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 30.0 / -0.032196171374784574 / 2.820171892718441 | [NPY](tensors/0003635.npy) |
| 3636 | `model.layers.0.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0003636.npy) |
| 3637 | `model.layers.0.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0003637.npy) |
| 3638 | `model.layers.0.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003638.npy) |
| 3639 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0003639.npy) |
| 3640 | `model.layers.0.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3641 | `model.layers.0.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3642 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0003642.npy) |
| 3643 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0003643.npy) |
| 3644 | `model.layers.0.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3645 | `model.layers.0.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0003645.npy) |
| 3646 | `model.layers.0.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.6875 / 10.0625 / 0.016296769957989454 / 1.0275877120532655 | [NPY](tensors/0003646.npy) |
| 3647 | `model.layers.0.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0003647.npy) |
| 3648 | `model.layers.0.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -57.0 / 59.0 / -0.06925755739212036 / 5.9291873125568 | [NPY](tensors/0003648.npy) |
| 3649 | `model.layers.0.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0003649.npy) |
| 3650 | `model.layers.0.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.0625 / 3.890625 / -0.020120687782764435 / 1.0179532107822138 | [NPY](tensors/0003650.npy) |
| 3651 | `model.layers.0.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.65625 / 3.4375 / -0.021551540788095735 / 0.5705458446249208 | [NPY](tensors/0003651.npy) |
| 3652 | `model.layers.0.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.875 / 35.0 / 0.01815983826915423 / 1.0973602132079487 | [NPY](tensors/0003652.npy) |
| 3653 | `model.layers.0.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.875 / 35.0 / 0.01815983826915423 / 1.0973602132079487 | [NPY](tensors/0003653.npy) |
| 3654 | `model.layers.0.self_attn` | 31 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.003766668469545916 / 0.04179620059625926 | [NPY](tensors/0003654.npy) |
| 3655 | `model.layers.0.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 36.5 / -0.014022148980034722 / 2.8699589395397105 | [NPY](tensors/0003655.npy) |
| 3656 | `model.layers.0.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.953125 / 1.5625 / 0.0022262851397196453 / 0.27366361425881325 | [NPY](tensors/0003656.npy) |
| 3657 | `model.layers.0.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.953125 / 1.5625 / 0.0022262851397196453 / 0.27366361425881325 | [NPY](tensors/0003657.npy) |
| 3658 | `model.layers.0.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.953125 / 1.5625 / 0.0022262851397196453 / 0.27366361425881325 | [NPY](tensors/0003658.npy) |
| 3659 | `model.layers.0.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3660 | `model.layers.0.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3661 | `model.layers.0.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3662 | `model.layers.0.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.625 / 10.5625 / 0.010624038676420847 / 0.5736370678997619 | [NPY](tensors/0003662.npy) |
| 3663 | `model.layers.0.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.625 / 10.5625 / 0.010624038676420847 / 0.5736370678997619 | [NPY](tensors/0003663.npy) |
| 3664 | `model.layers.0.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.625 / 1.7578125 / -0.0222625732421875 / 1.0469168459611986 | [NPY](tensors/0003664.npy) |
| 3665 | `model.layers.0` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 46.75 / -0.003381236394246419 / 2.8448183738931805 | [NPY](tensors/0003665.npy) |
| 3744 | `model.layers.0` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.5 / 30.625 / 0.03435131601161427 / 2.148670063069294 | [NPY](tensors/0003744.npy) |
| 3745 | `model.layers.0` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003745.npy) |
| 3746 | `model.layers.0` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0003746.npy) |
| 3747 | `model.layers.0` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0003747.npy) |
| 3748 | `model.layers.0` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0003748.npy) |
| 3749 | `model.layers.0` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3750 | `model.layers.0` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3751 | `model.layers.0` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3752 | `model.layers.0.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.5 / 30.625 / 0.03435131601161427 / 2.148670063069294 | [NPY](tensors/0003752.npy) |
| 3753 | `model.layers.0.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0003753.npy) |
| 3754 | `model.layers.0.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0003754.npy) |
| 3755 | `model.layers.0.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003755.npy) |
| 3756 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0003756.npy) |
| 3757 | `model.layers.0.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3758 | `model.layers.0.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3759 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0003759.npy) |
| 3760 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0003760.npy) |
| 3761 | `model.layers.0.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3762 | `model.layers.0.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0003762.npy) |
| 3763 | `model.layers.0.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.59375 / 8.875 / -0.01820482179755345 / 1.2112680722654519 | [NPY](tensors/0003763.npy) |
| 3764 | `model.layers.0.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0003764.npy) |
| 3765 | `model.layers.0.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -47.25 / 51.0 / 0.04916292428970337 / 5.661126585935481 | [NPY](tensors/0003765.npy) |
| 3766 | `model.layers.0.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0003766.npy) |
| 3767 | `model.layers.0.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.59375 / 4.9375 / -0.02149730920791626 / 1.5738961772339104 | [NPY](tensors/0003767.npy) |
| 3768 | `model.layers.0.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.03125 / 3.03125 / -0.017882345044085923 / 0.4575131578860492 | [NPY](tensors/0003768.npy) |
| 3769 | `model.layers.0.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.625 / 31.5 / 0.009339628140959474 / 1.0154530487455995 | [NPY](tensors/0003769.npy) |
| 3770 | `model.layers.0.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.625 / 31.5 / 0.009339628140959474 / 1.0154530487455995 | [NPY](tensors/0003770.npy) |
| 3771 | `model.layers.0.self_attn` | 32 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.002163326538904971 / 0.034264290814986297 | [NPY](tensors/0003771.npy) |
| 3772 | `model.layers.0.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 32.25 / 0.04363737106323242 / 2.4608646069263598 | [NPY](tensors/0003772.npy) |
| 3773 | `model.layers.0.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 2.4375 / 0.004804692003462049 / 0.4195563824612836 | [NPY](tensors/0003773.npy) |
| 3774 | `model.layers.0.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 2.4375 / 0.004804692003462049 / 0.4195563824612836 | [NPY](tensors/0003774.npy) |
| 3775 | `model.layers.0.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 2.4375 / 0.004804692003462049 / 0.4195563824612836 | [NPY](tensors/0003775.npy) |
| 3776 | `model.layers.0.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3777 | `model.layers.0.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3778 | `model.layers.0.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3779 | `model.layers.0.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.8125 / 45.0 / 0.032243776321411136 / 1.4071199967142778 | [NPY](tensors/0003779.npy) |
| 3780 | `model.layers.0.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 45.0 / 0.032243776321411136 / 1.4071199967142778 | [NPY](tensors/0003780.npy) |
| 3781 | `model.layers.0.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3515625 / 1.9453125 / -0.13764572143554688 / 0.859634044932618 | [NPY](tensors/0003781.npy) |
| 3782 | `model.layers.0` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 74.0 / 0.07594488991631401 / 3.2413136777696456 | [NPY](tensors/0003782.npy) |
| 3861 | `model.layers.0` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0003861.npy) |
| 3862 | `model.layers.0` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003862.npy) |
| 3863 | `model.layers.0` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0003863.npy) |
| 3864 | `model.layers.0` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0003864.npy) |
| 3865 | `model.layers.0` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0003865.npy) |
| 3866 | `model.layers.0` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3867 | `model.layers.0` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3868 | `model.layers.0` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3869 | `model.layers.0.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0003869.npy) |
| 3870 | `model.layers.0.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003870.npy) |
| 3871 | `model.layers.0.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003871.npy) |
| 3872 | `model.layers.0.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003872.npy) |
| 3873 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0003873.npy) |
| 3874 | `model.layers.0.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3875 | `model.layers.0.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3876 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0003876.npy) |
| 3877 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0003877.npy) |
| 3878 | `model.layers.0.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3879 | `model.layers.0.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003879.npy) |
| 3880 | `model.layers.0.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 8.0 / 0.0014486645814031363 / 1.027321203413773 | [NPY](tensors/0003880.npy) |
| 3881 | `model.layers.0.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003881.npy) |
| 3882 | `model.layers.0.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.75 / 53.75 / 0.06940409168601036 / 5.734687316339554 | [NPY](tensors/0003882.npy) |
| 3883 | `model.layers.0.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0003883.npy) |
| 3884 | `model.layers.0.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.8125 / 3.75 / -0.006423294544219971 / 0.9290448609736645 | [NPY](tensors/0003884.npy) |
| 3885 | `model.layers.0.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.28125 / 3.734375 / -0.0043900687705900054 / 0.6317722353944243 | [NPY](tensors/0003885.npy) |
| 3886 | `model.layers.0.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.875 / 32.0 / 0.02706612745920817 / 1.016927264714178 | [NPY](tensors/0003886.npy) |
| 3887 | `model.layers.0.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.875 / 32.0 / 0.02706612745920817 / 1.016927264714178 | [NPY](tensors/0003887.npy) |
| 3888 | `model.layers.0.self_attn` | 33 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003725465287675404 / 0.040899944887534165 | [NPY](tensors/0003888.npy) |
| 3889 | `model.layers.0.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.0 / 32.5 / -0.0639071888393826 / 2.9305079393630176 | [NPY](tensors/0003889.npy) |
| 3890 | `model.layers.0.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8359375 / 1.5546875 / 0.002487121687995063 / 0.3362046218268714 | [NPY](tensors/0003890.npy) |
| 3891 | `model.layers.0.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8359375 / 1.5546875 / 0.002487121687995063 / 0.3362046218268714 | [NPY](tensors/0003891.npy) |
| 3892 | `model.layers.0.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.8359375 / 1.5546875 / 0.002487121687995063 / 0.3362046218268714 | [NPY](tensors/0003892.npy) |
| 3893 | `model.layers.0.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3894 | `model.layers.0.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3895 | `model.layers.0.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3896 | `model.layers.0.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.375 / 10.75 / 0.014462471960319414 / 0.5353069417145597 | [NPY](tensors/0003896.npy) |
| 3897 | `model.layers.0.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.375 / 10.75 / 0.014462471960319414 / 0.5353069417145597 | [NPY](tensors/0003897.npy) |
| 3898 | `model.layers.0.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.625 / 1.453125 / -0.01860809326171875 / 1.327582264877274 | [NPY](tensors/0003898.npy) |
| 3899 | `model.layers.0` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.25 / 43.25 / -0.049409782886505126 / 2.971899016126656 | [NPY](tensors/0003899.npy) |
| 3978 | `model.layers.0` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 34.5 / 0.024106338868538538 / 2.181946652271328 | [NPY](tensors/0003978.npy) |
| 3979 | `model.layers.0` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003979.npy) |
| 3980 | `model.layers.0` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0003980.npy) |
| 3981 | `model.layers.0` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0003981.npy) |
| 3982 | `model.layers.0` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0003982.npy) |
| 3983 | `model.layers.0` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3984 | `model.layers.0` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3985 | `model.layers.0` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3986 | `model.layers.0.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 34.5 / 0.024106338868538538 / 2.181946652271328 | [NPY](tensors/0003986.npy) |
| 3987 | `model.layers.0.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5 / 9.75 / 0.014064499901400672 / 0.7386068996125579 | [NPY](tensors/0003987.npy) |
| 3988 | `model.layers.0.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5 / 9.75 / 0.014064499901400672 / 0.7386068996125579 | [NPY](tensors/0003988.npy) |
| 3989 | `model.layers.0.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003989.npy) |
| 3990 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0003990.npy) |
| 3991 | `model.layers.0.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3992 | `model.layers.0.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3993 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0003993.npy) |
| 3994 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0003994.npy) |
| 3995 | `model.layers.0.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3996 | `model.layers.0.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5 / 9.75 / 0.014064499901400672 / 0.7386068996125579 | [NPY](tensors/0003996.npy) |
| 3997 | `model.layers.0.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.6875 / 10.875 / -0.0016983961686491966 / 1.2644950903036258 | [NPY](tensors/0003997.npy) |
| 3998 | `model.layers.0.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5 / 9.75 / 0.014064499901400672 / 0.7386068996125579 | [NPY](tensors/0003998.npy) |
| 3999 | `model.layers.0.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.0 / 51.25 / -0.06648898124694824 / 5.791810722585411 | [NPY](tensors/0003999.npy) |
| 4000 | `model.layers.0.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5 / 9.75 / 0.014064499901400672 / 0.7386068996125579 | [NPY](tensors/0004000.npy) |
| 4001 | `model.layers.0.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.3125 / 4.84375 / -0.014546394348144531 / 1.5622975050793066 | [NPY](tensors/0004001.npy) |
| 4002 | `model.layers.0.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.03125 / 3.84375 / -0.02098724954521458 / 0.6201379149445598 | [NPY](tensors/0004002.npy) |
| 4003 | `model.layers.0.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.375 / 40.75 / 0.024036289213432205 / 1.2747134420678274 | [NPY](tensors/0004003.npy) |
| 4004 | `model.layers.0.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.375 / 40.75 / 0.024036289213432205 / 1.2747134420678274 | [NPY](tensors/0004004.npy) |
| 4005 | `model.layers.0.self_attn` | 34 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003800606809717129 / 0.04574481280975758 | [NPY](tensors/0004005.npy) |
| 4006 | `model.layers.0.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 43.5 / 0.04827229579289754 / 2.6817669041267136 | [NPY](tensors/0004006.npy) |
| 4007 | `model.layers.0.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7421875 / 1.6796875 / 0.016009737385643853 / 0.3950081695680721 | [NPY](tensors/0004007.npy) |
| 4008 | `model.layers.0.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7421875 / 1.6796875 / 0.016009737385643853 / 0.3950081695680721 | [NPY](tensors/0004008.npy) |
| 4009 | `model.layers.0.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.7421875 / 1.6796875 / 0.016009737385643853 / 0.3950081695680721 | [NPY](tensors/0004009.npy) |
| 4010 | `model.layers.0.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4011 | `model.layers.0.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4012 | `model.layers.0.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4013 | `model.layers.0.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.3125 / 32.0 / 0.01935254004266527 / 1.0657633943968534 | [NPY](tensors/0004013.npy) |
| 4014 | `model.layers.0.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.3125 / 32.0 / 0.01935254004266527 / 1.0657633943968534 | [NPY](tensors/0004014.npy) |
| 4015 | `model.layers.0.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6875 / 3.3125 / -0.2431640625 / 1.0869648416864173 | [NPY](tensors/0004015.npy) |
| 4016 | `model.layers.0` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 73.0 / 0.0677025212181939 / 3.3370179045415433 | [NPY](tensors/0004016.npy) |
| 4095 | `model.layers.0` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 35.75 / -0.0047709693511327105 / 2.981557331108137 | [NPY](tensors/0004095.npy) |
| 4096 | `model.layers.0` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004096.npy) |
| 4097 | `model.layers.0` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0004097.npy) |
| 4098 | `model.layers.0` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0004098.npy) |
| 4099 | `model.layers.0` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0004099.npy) |
| 4100 | `model.layers.0` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4101 | `model.layers.0` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4102 | `model.layers.0` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4103 | `model.layers.0.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 35.75 / -0.0047709693511327105 / 2.981557331108137 | [NPY](tensors/0004103.npy) |
| 4104 | `model.layers.0.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 7.90625 / -0.0012042447096771664 / 0.7138006798516943 | [NPY](tensors/0004104.npy) |
| 4105 | `model.layers.0.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 7.90625 / -0.0012042447096771664 / 0.7138006798516943 | [NPY](tensors/0004105.npy) |
| 4106 | `model.layers.0.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004106.npy) |
| 4107 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0004107.npy) |
| 4108 | `model.layers.0.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4109 | `model.layers.0.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4110 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0004110.npy) |
| 4111 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0004111.npy) |
| 4112 | `model.layers.0.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4113 | `model.layers.0.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 7.90625 / -0.0012042447096771664 / 0.7138006798516943 | [NPY](tensors/0004113.npy) |
| 4114 | `model.layers.0.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.46875 / 7.96875 / 0.01911622262559831 / 0.9444078323736833 | [NPY](tensors/0004114.npy) |
| 4115 | `model.layers.0.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 7.90625 / -0.0012042447096771664 / 0.7138006798516943 | [NPY](tensors/0004115.npy) |
| 4116 | `model.layers.0.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -58.75 / 51.0 / -0.010727882385253906 / 5.792212682257103 | [NPY](tensors/0004116.npy) |
| 4117 | `model.layers.0.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 7.90625 / -0.0012042447096771664 / 0.7138006798516943 | [NPY](tensors/0004117.npy) |
| 4118 | `model.layers.0.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.3125 / 4.46875 / -0.03268304467201233 / 1.040410062394765 | [NPY](tensors/0004118.npy) |
| 4119 | `model.layers.0.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.09375 / 3.625 / -0.013736929098740802 / 0.559777207865976 | [NPY](tensors/0004119.npy) |
| 4120 | `model.layers.0.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0 / 37.5 / 0.03566852410634359 / 1.0982844572851174 | [NPY](tensors/0004120.npy) |
| 4121 | `model.layers.0.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0 / 37.5 / 0.03566852410634359 / 1.0982844572851174 | [NPY](tensors/0004121.npy) |
| 4122 | `model.layers.0.self_attn` | 35 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.002997428393771909 / 0.03296775660086179 | [NPY](tensors/0004122.npy) |
| 4123 | `model.layers.0.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 45.0 / 0.0309289190504286 / 3.2228173624113174 | [NPY](tensors/0004123.npy) |
| 4124 | `model.layers.0.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 2.390625 / 0.006827433241738214 / 0.28740981091157924 | [NPY](tensors/0004124.npy) |
| 4125 | `model.layers.0.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 2.390625 / 0.006827433241738214 / 0.28740981091157924 | [NPY](tensors/0004125.npy) |
| 4126 | `model.layers.0.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 2.390625 / 0.006827433241738214 / 0.28740981091157924 | [NPY](tensors/0004126.npy) |
| 4127 | `model.layers.0.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4128 | `model.layers.0.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4129 | `model.layers.0.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4130 | `model.layers.0.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.15625 / 12.75 / 0.013396329370637734 / 0.6049425615091628 | [NPY](tensors/0004130.npy) |
| 4131 | `model.layers.0.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.15625 / 12.75 / 0.013396329370637734 / 0.6049425615091628 | [NPY](tensors/0004131.npy) |
| 4132 | `model.layers.0.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.28125 / 1.3828125 / -0.045772552490234375 / 0.9806863153404222 | [NPY](tensors/0004132.npy) |
| 4133 | `model.layers.0` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.5 / 56.0 / 0.044145859612358944 / 3.279792656731027 | [NPY](tensors/0004133.npy) |
| 4212 | `model.layers.0` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.75 / 34.25 / 0.03183326390054491 / 2.424402358822739 | [NPY](tensors/0004212.npy) |
| 4213 | `model.layers.0` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004213.npy) |
| 4214 | `model.layers.0` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0004214.npy) |
| 4215 | `model.layers.0` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0004215.npy) |
| 4216 | `model.layers.0` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0004216.npy) |
| 4217 | `model.layers.0` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4218 | `model.layers.0` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4219 | `model.layers.0` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4220 | `model.layers.0.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.75 / 34.25 / 0.03183326390054491 / 2.424402358822739 | [NPY](tensors/0004220.npy) |
| 4221 | `model.layers.0.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.25 / 8.875 / 3.695984681447347e-05 / 0.8401690750801883 | [NPY](tensors/0004221.npy) |
| 4222 | `model.layers.0.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.25 / 8.875 / 3.695984681447347e-05 / 0.8401690750801883 | [NPY](tensors/0004222.npy) |
| 4223 | `model.layers.0.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004223.npy) |
| 4224 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0004224.npy) |
| 4225 | `model.layers.0.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4226 | `model.layers.0.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4227 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0004227.npy) |
| 4228 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0004228.npy) |
| 4229 | `model.layers.0.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4230 | `model.layers.0.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.25 / 8.875 / 3.695984681447347e-05 / 0.8401690750801883 | [NPY](tensors/0004230.npy) |
| 4231 | `model.layers.0.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 9.1875 / 0.026697279885411263 / 1.08883890491105 | [NPY](tensors/0004231.npy) |
| 4232 | `model.layers.0.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.25 / 8.875 / 3.695984681447347e-05 / 0.8401690750801883 | [NPY](tensors/0004232.npy) |
| 4233 | `model.layers.0.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.25 / 52.5 / -0.06963016837835312 / 5.683357533348337 | [NPY](tensors/0004233.npy) |
| 4234 | `model.layers.0.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.25 / 8.875 / 3.695984681447347e-05 / 0.8401690750801883 | [NPY](tensors/0004234.npy) |
| 4235 | `model.layers.0.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.21875 / 6.90625 / -0.08950495719909668 / 1.4434920469697818 | [NPY](tensors/0004235.npy) |
| 4236 | `model.layers.0.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.34375 / 3.765625 / -0.019781100563704967 / 0.5522706002366014 | [NPY](tensors/0004236.npy) |
| 4237 | `model.layers.0.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.5 / 40.25 / 0.021355579959021674 / 1.2418467199477363 | [NPY](tensors/0004237.npy) |
| 4238 | `model.layers.0.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.5 / 40.25 / 0.021355579959021674 / 1.2418467199477363 | [NPY](tensors/0004238.npy) |
| 4239 | `model.layers.0.self_attn` | 36 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0029747159566313086 / 0.03722738044336677 | [NPY](tensors/0004239.npy) |
| 4240 | `model.layers.0.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.0 / 41.75 / 0.05317421621746487 / 2.8049135502688727 | [NPY](tensors/0004240.npy) |
| 4241 | `model.layers.0.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.5625 / 1.921875 / 0.0014461676279703777 / 0.39422979893748616 | [NPY](tensors/0004241.npy) |
| 4242 | `model.layers.0.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.5625 / 1.921875 / 0.0014461676279703777 / 0.39422979893748616 | [NPY](tensors/0004242.npy) |
| 4243 | `model.layers.0.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.5625 / 1.921875 / 0.0014461676279703777 / 0.39422979893748616 | [NPY](tensors/0004243.npy) |
| 4244 | `model.layers.0.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4245 | `model.layers.0.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4246 | `model.layers.0.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4247 | `model.layers.0.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -36.0 / 53.0 / 0.027929859856764477 / 1.7199073405891268 | [NPY](tensors/0004247.npy) |
| 4248 | `model.layers.0.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 53.0 / 0.027929859856764477 / 1.7199073405891268 | [NPY](tensors/0004248.npy) |
| 4249 | `model.layers.0.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.609375 / 2.78125 / -0.198944091796875 / 0.8267992666446554 | [NPY](tensors/0004249.npy) |
| 4250 | `model.layers.0` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.0 / 88.5 / 0.08098701900906033 / 3.935949835914979 | [NPY](tensors/0004250.npy) |
| 4329 | `model.layers.0` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.75 / 27.25 / -0.016518868009249368 / 2.0560686168012485 | [NPY](tensors/0004329.npy) |
| 4330 | `model.layers.0` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004330.npy) |
| 4331 | `model.layers.0` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0004331.npy) |
| 4332 | `model.layers.0` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0004332.npy) |
| 4333 | `model.layers.0` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0004333.npy) |
| 4334 | `model.layers.0` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4335 | `model.layers.0` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4336 | `model.layers.0` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4337 | `model.layers.0.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.75 / 27.25 / -0.016518868009249368 / 2.0560686168012485 | [NPY](tensors/0004337.npy) |
| 4338 | `model.layers.0.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 7.5625 / -0.013478766878445942 / 0.8394325172827353 | [NPY](tensors/0004338.npy) |
| 4339 | `model.layers.0.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 7.5625 / -0.013478766878445942 / 0.8394325172827353 | [NPY](tensors/0004339.npy) |
| 4340 | `model.layers.0.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004340.npy) |
| 4341 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0004341.npy) |
| 4342 | `model.layers.0.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4343 | `model.layers.0.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4344 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0004344.npy) |
| 4345 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0004345.npy) |
| 4346 | `model.layers.0.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4347 | `model.layers.0.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 7.5625 / -0.013478766878445942 / 0.8394325172827353 | [NPY](tensors/0004347.npy) |
| 4348 | `model.layers.0.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.46875 / 8.6875 / 0.028240101790288463 / 1.1043014445000683 | [NPY](tensors/0004348.npy) |
| 4349 | `model.layers.0.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 7.5625 / -0.013478766878445942 / 0.8394325172827353 | [NPY](tensors/0004349.npy) |
| 4350 | `model.layers.0.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.25 / 48.0 / -0.07602882385253906 / 4.956441244697324 | [NPY](tensors/0004350.npy) |
| 4351 | `model.layers.0.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 7.5625 / -0.013478766878445942 / 0.8394325172827353 | [NPY](tensors/0004351.npy) |
| 4352 | `model.layers.0.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 4.40625 / 0.025531575083732605 / 1.403797967132358 | [NPY](tensors/0004352.npy) |
| 4353 | `model.layers.0.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.3125 / 6.53125 / -0.015859910286962986 / 0.9620363467424061 | [NPY](tensors/0004353.npy) |
| 4354 | `model.layers.0.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 41.25 / 0.03380730284584893 / 1.5249181698935503 | [NPY](tensors/0004354.npy) |
| 4355 | `model.layers.0.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 41.25 / 0.03380730284584893 / 1.5249181698935503 | [NPY](tensors/0004355.npy) |
| 4356 | `model.layers.0.self_attn` | 37 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0053054528580425515 / 0.05309451836877907 | [NPY](tensors/0004356.npy) |
| 4357 | `model.layers.0.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.25 / 42.0 / 0.017333910200330947 / 2.6232710429286836 | [NPY](tensors/0004357.npy) |
| 4358 | `model.layers.0.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.78125 / 2.0 / 0.004831692245271471 / 0.4993053612097908 | [NPY](tensors/0004358.npy) |
| 4359 | `model.layers.0.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.78125 / 2.0 / 0.004831692245271471 / 0.4993053612097908 | [NPY](tensors/0004359.npy) |
| 4360 | `model.layers.0.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.78125 / 2.0 / 0.004831692245271471 / 0.4993053612097908 | [NPY](tensors/0004360.npy) |
| 4361 | `model.layers.0.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4362 | `model.layers.0.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4363 | `model.layers.0.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4364 | `model.layers.0.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -43.0 / 39.25 / 0.023941575156317816 / 1.4324689171247798 | [NPY](tensors/0004364.npy) |
| 4365 | `model.layers.0.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 39.25 / 0.023941575156317816 / 1.4324689171247798 | [NPY](tensors/0004365.npy) |
| 4366 | `model.layers.0.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.84375 / 2.140625 / -0.14072036743164062 / 0.8784865165109733 | [NPY](tensors/0004366.npy) |
| 4367 | `model.layers.0` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -81.0 / 81.0 / 0.041303719414605033 / 3.634588624235473 | [NPY](tensors/0004367.npy) |
| 4446 | `model.layers.0` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 28.375 / -0.06469851401117113 / 2.3802508094808466 | [NPY](tensors/0004446.npy) |
| 4447 | `model.layers.0` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004447.npy) |
| 4448 | `model.layers.0` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0004448.npy) |
| 4449 | `model.layers.0` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0004449.npy) |
| 4450 | `model.layers.0` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0004450.npy) |
| 4451 | `model.layers.0` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4452 | `model.layers.0` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4453 | `model.layers.0` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4454 | `model.layers.0.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 28.375 / -0.06469851401117113 / 2.3802508094808466 | [NPY](tensors/0004454.npy) |
| 4455 | `model.layers.0.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 7.59375 / -0.026988965107334985 / 0.7830140451399451 | [NPY](tensors/0004455.npy) |
| 4456 | `model.layers.0.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 7.59375 / -0.026988965107334985 / 0.7830140451399451 | [NPY](tensors/0004456.npy) |
| 4457 | `model.layers.0.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004457.npy) |
| 4458 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0004458.npy) |
| 4459 | `model.layers.0.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4460 | `model.layers.0.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4461 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0004461.npy) |
| 4462 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0004462.npy) |
| 4463 | `model.layers.0.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4464 | `model.layers.0.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 7.59375 / -0.026988965107334985 / 0.7830140451399451 | [NPY](tensors/0004464.npy) |
| 4465 | `model.layers.0.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.0625 / 10.0625 / 0.020746754482388496 / 1.0562843984008587 | [NPY](tensors/0004465.npy) |
| 4466 | `model.layers.0.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 7.59375 / -0.026988965107334985 / 0.7830140451399451 | [NPY](tensors/0004466.npy) |
| 4467 | `model.layers.0.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -46.25 / 52.75 / 0.00579071044921875 / 5.8102041575144 | [NPY](tensors/0004467.npy) |
| 4468 | `model.layers.0.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 7.59375 / -0.026988965107334985 / 0.7830140451399451 | [NPY](tensors/0004468.npy) |
| 4469 | `model.layers.0.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.84375 / 4.59375 / 0.06223616003990173 / 1.3586842316189938 | [NPY](tensors/0004469.npy) |
| 4470 | `model.layers.0.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.34375 / 4.3125 / -0.005663180197188922 / 0.6473051861295266 | [NPY](tensors/0004470.npy) |
| 4471 | `model.layers.0.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 51.5 / 0.028117510593599744 / 1.638276878427043 | [NPY](tensors/0004471.npy) |
| 4472 | `model.layers.0.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 51.5 / 0.028117510593599744 / 1.638276878427043 | [NPY](tensors/0004472.npy) |
| 4473 | `model.layers.0.self_attn` | 38 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0034103649716855406 / 0.03889039776843377 | [NPY](tensors/0004473.npy) |
| 4474 | `model.layers.0.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.75 / 51.25 / -0.036739540100097653 / 2.8697030791760803 | [NPY](tensors/0004474.npy) |
| 4475 | `model.layers.0.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.390625 / 1.7890625 / -0.00356658399105072 / 0.40353365333950736 | [NPY](tensors/0004475.npy) |
| 4476 | `model.layers.0.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.390625 / 1.7890625 / -0.00356658399105072 / 0.40353365333950736 | [NPY](tensors/0004476.npy) |
| 4477 | `model.layers.0.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.390625 / 1.7890625 / -0.00356658399105072 / 0.40353365333950736 | [NPY](tensors/0004477.npy) |
| 4478 | `model.layers.0.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4479 | `model.layers.0.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4480 | `model.layers.0.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4481 | `model.layers.0.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -35.25 / 28.25 / -0.0019831584559546578 / 1.0978180914944846 | [NPY](tensors/0004481.npy) |
| 4482 | `model.layers.0.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 28.25 / -0.0019831584559546578 / 1.0978180914944846 | [NPY](tensors/0004482.npy) |
| 4483 | `model.layers.0.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.875 / 1.7734375 / -0.1764068603515625 / 0.7328026358796106 | [NPY](tensors/0004483.npy) |
| 4484 | `model.layers.0` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.0 / 77.0 / -0.0386704338921441 / 3.568952995592652 | [NPY](tensors/0004484.npy) |
| 4563 | `model.layers.0` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 32.0 / -0.03988325885600514 / 2.321626226430588 | [NPY](tensors/0004563.npy) |
| 4564 | `model.layers.0` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004564.npy) |
| 4565 | `model.layers.0` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0004565.npy) |
| 4566 | `model.layers.0` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0004566.npy) |
| 4567 | `model.layers.0` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0004567.npy) |
| 4568 | `model.layers.0` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4569 | `model.layers.0` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4570 | `model.layers.0` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4571 | `model.layers.0.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 32.0 / -0.03988325885600514 / 2.321626226430588 | [NPY](tensors/0004571.npy) |
| 4572 | `model.layers.0.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.5625 / 9.625 / -0.010380937821335263 / 0.7750667532790622 | [NPY](tensors/0004572.npy) |
| 4573 | `model.layers.0.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.5625 / 9.625 / -0.010380937821335263 / 0.7750667532790622 | [NPY](tensors/0004573.npy) |
| 4574 | `model.layers.0.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004574.npy) |
| 4575 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0004575.npy) |
| 4576 | `model.layers.0.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4577 | `model.layers.0.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4578 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0004578.npy) |
| 4579 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0004579.npy) |
| 4580 | `model.layers.0.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4581 | `model.layers.0.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.5625 / 9.625 / -0.010380937821335263 / 0.7750667532790622 | [NPY](tensors/0004581.npy) |
| 4582 | `model.layers.0.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.4375 / 8.125 / 0.021404181607067585 / 1.0592509972333464 | [NPY](tensors/0004582.npy) |
| 4583 | `model.layers.0.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.5625 / 9.625 / -0.010380937821335263 / 0.7750667532790622 | [NPY](tensors/0004583.npy) |
| 4584 | `model.layers.0.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.75 / 59.25 / 0.008149027824401855 / 5.8966663185414685 | [NPY](tensors/0004584.npy) |
| 4585 | `model.layers.0.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.5625 / 9.625 / -0.010380937821335263 / 0.7750667532790622 | [NPY](tensors/0004585.npy) |
| 4586 | `model.layers.0.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.96875 / 5.65625 / 0.023187309503555298 / 1.5731311925190303 | [NPY](tensors/0004586.npy) |
| 4587 | `model.layers.0.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.09375 / 4.21875 / -0.0029975037032272667 / 0.6365747456573582 | [NPY](tensors/0004587.npy) |
| 4588 | `model.layers.0.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 49.0 / 0.028689629667335088 / 1.6172451764743927 | [NPY](tensors/0004588.npy) |
| 4589 | `model.layers.0.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 49.0 / 0.028689629667335088 / 1.6172451764743927 | [NPY](tensors/0004589.npy) |
| 4590 | `model.layers.0.self_attn` | 39 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0033669679919836964 / 0.038092569747198615 | [NPY](tensors/0004590.npy) |
| 4591 | `model.layers.0.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 50.25 / -0.011283228132459853 / 2.9881161515341264 | [NPY](tensors/0004591.npy) |
| 4592 | `model.layers.0.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.875 / 1.671875 / 0.0023649414380391438 / 0.3689771806109188 | [NPY](tensors/0004592.npy) |
| 4593 | `model.layers.0.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.875 / 1.671875 / 0.0023649414380391438 / 0.3689771806109188 | [NPY](tensors/0004593.npy) |
| 4594 | `model.layers.0.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.875 / 1.671875 / 0.0023649414380391438 / 0.3689771806109188 | [NPY](tensors/0004594.npy) |
| 4595 | `model.layers.0.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4596 | `model.layers.0.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4597 | `model.layers.0.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4598 | `model.layers.0.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.625 / 9.3125 / -0.003153918937055601 / 0.5711949425675522 | [NPY](tensors/0004598.npy) |
| 4599 | `model.layers.0.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.625 / 9.3125 / -0.003153918937055601 / 0.5711949425675522 | [NPY](tensors/0004599.npy) |
| 4600 | `model.layers.0.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.88671875 / 1.9765625 / -0.08816337585449219 / 0.6180749939349591 | [NPY](tensors/0004600.npy) |
| 4601 | `model.layers.0` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -56.5 / 56.5 / -0.014511977301703559 / 3.3035273490976707 | [NPY](tensors/0004601.npy) |
| 4680 | `model.layers.0` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 34.75 / -0.008174573961231444 / 2.1920079534405623 | [NPY](tensors/0004680.npy) |
| 4681 | `model.layers.0` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004681.npy) |
| 4682 | `model.layers.0` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0004682.npy) |
| 4683 | `model.layers.0` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0004683.npy) |
| 4684 | `model.layers.0` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0004684.npy) |
| 4685 | `model.layers.0` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4686 | `model.layers.0` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4687 | `model.layers.0` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4688 | `model.layers.0.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 34.75 / -0.008174573961231444 / 2.1920079534405623 | [NPY](tensors/0004688.npy) |
| 4689 | `model.layers.0.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.75 / 10.375 / -0.005402215818564097 / 0.8558610023483436 | [NPY](tensors/0004689.npy) |
| 4690 | `model.layers.0.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.75 / 10.375 / -0.005402215818564097 / 0.8558610023483436 | [NPY](tensors/0004690.npy) |
| 4691 | `model.layers.0.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004691.npy) |
| 4692 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0004692.npy) |
| 4693 | `model.layers.0.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4694 | `model.layers.0.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4695 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0004695.npy) |
| 4696 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0004696.npy) |
| 4697 | `model.layers.0.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4698 | `model.layers.0.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.75 / 10.375 / -0.005402215818564097 / 0.8558610023483436 | [NPY](tensors/0004698.npy) |
| 4699 | `model.layers.0.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.65625 / 9.9375 / 0.02846267237327993 / 1.174231893369701 | [NPY](tensors/0004699.npy) |
| 4700 | `model.layers.0.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.75 / 10.375 / -0.005402215818564097 / 0.8558610023483436 | [NPY](tensors/0004700.npy) |
| 4701 | `model.layers.0.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.5 / 54.75 / 0.04301157593727112 / 5.733899381295304 | [NPY](tensors/0004701.npy) |
| 4702 | `model.layers.0.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.75 / 10.375 / -0.005402215818564097 / 0.8558610023483436 | [NPY](tensors/0004702.npy) |
| 4703 | `model.layers.0.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.1875 / 5.1875 / 0.03233560919761658 / 1.4238076691102852 | [NPY](tensors/0004703.npy) |
| 4704 | `model.layers.0.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.96875 / 5.65625 / 0.0020709489363071043 / 0.6629377138156409 | [NPY](tensors/0004704.npy) |
| 4705 | `model.layers.0.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.75 / 45.0 / 0.036342051956388684 / 1.4319285912987096 | [NPY](tensors/0004705.npy) |
| 4706 | `model.layers.0.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.75 / 45.0 / 0.036342051956388684 / 1.4319285912987096 | [NPY](tensors/0004706.npy) |
| 4707 | `model.layers.0.self_attn` | 40 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0023520443163512444 / 0.03111770615897672 | [NPY](tensors/0004707.npy) |
| 4708 | `model.layers.0.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 43.5 / 0.028212775124443902 / 2.6781228783733986 | [NPY](tensors/0004708.npy) |
| 4709 | `model.layers.0.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.1875 / 1.609375 / 0.007536966933144464 / 0.42177812081546256 | [NPY](tensors/0004709.npy) |
| 4710 | `model.layers.0.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.1875 / 1.609375 / 0.007536966933144464 / 0.42177812081546256 | [NPY](tensors/0004710.npy) |
| 4711 | `model.layers.0.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.1875 / 1.609375 / 0.007536966933144464 / 0.42177812081546256 | [NPY](tensors/0004711.npy) |
| 4712 | `model.layers.0.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4713 | `model.layers.0.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4714 | `model.layers.0.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4715 | `model.layers.0.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -19.125 / 24.0 / 0.02146445595555835 / 0.8806051858080695 | [NPY](tensors/0004715.npy) |
| 4716 | `model.layers.0.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.125 / 24.0 / 0.02146445595555835 / 0.8806051858080695 | [NPY](tensors/0004716.npy) |
| 4717 | `model.layers.0.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.109375 / 1.75 / -0.19620895385742188 / 0.9083974013189233 | [NPY](tensors/0004717.npy) |
| 4718 | `model.layers.0` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.5 / 65.0 / 0.049576388465033636 / 3.308691409409574 | [NPY](tensors/0004718.npy) |
| 4797 | `model.layers.0` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 31.375 / -0.03532346973402633 / 2.513775339817436 | [NPY](tensors/0004797.npy) |
| 4798 | `model.layers.0` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004798.npy) |
| 4799 | `model.layers.0` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0004799.npy) |
| 4800 | `model.layers.0` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0004800.npy) |
| 4801 | `model.layers.0` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0004801.npy) |
| 4802 | `model.layers.0` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4803 | `model.layers.0` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4804 | `model.layers.0` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4805 | `model.layers.0.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 31.375 / -0.03532346973402633 / 2.513775339817436 | [NPY](tensors/0004805.npy) |
| 4806 | `model.layers.0.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0004806.npy) |
| 4807 | `model.layers.0.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0004807.npy) |
| 4808 | `model.layers.0.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004808.npy) |
| 4809 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0004809.npy) |
| 4810 | `model.layers.0.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4811 | `model.layers.0.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4812 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0004812.npy) |
| 4813 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0004813.npy) |
| 4814 | `model.layers.0.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4815 | `model.layers.0.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0004815.npy) |
| 4816 | `model.layers.0.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 8.875 / -0.00043488043593242764 / 1.093332692665652 | [NPY](tensors/0004816.npy) |
| 4817 | `model.layers.0.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0004817.npy) |
| 4818 | `model.layers.0.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.0 / 57.0 / -0.11751466989517212 / 6.178501515201047 | [NPY](tensors/0004818.npy) |
| 4819 | `model.layers.0.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0004819.npy) |
| 4820 | `model.layers.0.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.15625 / 4.375 / -0.08698096498847008 / 1.3301958676902246 | [NPY](tensors/0004820.npy) |
| 4821 | `model.layers.0.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.1875 / 5.09375 / -0.005623690667562187 / 0.71329172879147 | [NPY](tensors/0004821.npy) |
| 4822 | `model.layers.0.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 48.75 / 0.03488449139727486 / 1.541198407788812 | [NPY](tensors/0004822.npy) |
| 4823 | `model.layers.0.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 48.75 / 0.03488449139727486 / 1.541198407788812 | [NPY](tensors/0004823.npy) |
| 4824 | `model.layers.0.self_attn` | 41 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003746405275923927 / 0.03711198467522751 | [NPY](tensors/0004824.npy) |
| 4825 | `model.layers.0.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.75 / 47.0 / -0.0004655652576022678 / 3.0741383525938306 | [NPY](tensors/0004825.npy) |
| 4826 | `model.layers.0.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7265625 / 1.6015625 / 0.0003632353411780463 / 0.3729087170990913 | [NPY](tensors/0004826.npy) |
| 4827 | `model.layers.0.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7265625 / 1.6015625 / 0.0003632353411780463 / 0.3729087170990913 | [NPY](tensors/0004827.npy) |
| 4828 | `model.layers.0.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.7265625 / 1.6015625 / 0.0003632353411780463 / 0.3729087170990913 | [NPY](tensors/0004828.npy) |
| 4829 | `model.layers.0.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4830 | `model.layers.0.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4831 | `model.layers.0.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4832 | `model.layers.0.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.96875 / 27.875 / 0.017544530249304243 / 0.8129805934555364 | [NPY](tensors/0004832.npy) |
| 4833 | `model.layers.0.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.96875 / 27.875 / 0.017544530249304243 / 0.8129805934555364 | [NPY](tensors/0004833.npy) |
| 4834 | `model.layers.0.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.046875 / 1.640625 / -0.17608642578125 / 0.7336266673008274 | [NPY](tensors/0004834.npy) |
| 4835 | `model.layers.0` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.75 / 75.0 / 0.01710964838663737 / 3.534985135199582 | [NPY](tensors/0004835.npy) |
| 4914 | `model.layers.0` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 40.25 / -0.06394515766037835 / 2.6467228965831135 | [NPY](tensors/0004914.npy) |
| 4915 | `model.layers.0` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004915.npy) |
| 4916 | `model.layers.0` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0004916.npy) |
| 4917 | `model.layers.0` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0004917.npy) |
| 4918 | `model.layers.0` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0004918.npy) |
| 4919 | `model.layers.0` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4920 | `model.layers.0` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4921 | `model.layers.0` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4922 | `model.layers.0.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 40.25 / -0.06394515766037835 / 2.6467228965831135 | [NPY](tensors/0004922.npy) |
| 4923 | `model.layers.0.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004923.npy) |
| 4924 | `model.layers.0.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004924.npy) |
| 4925 | `model.layers.0.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004925.npy) |
| 4926 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0004926.npy) |
| 4927 | `model.layers.0.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4928 | `model.layers.0.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4929 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0004929.npy) |
| 4930 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0004930.npy) |
| 4931 | `model.layers.0.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4932 | `model.layers.0.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004932.npy) |
| 4933 | `model.layers.0.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.6875 / 7.625 / -0.005639673676341772 / 1.046891081389267 | [NPY](tensors/0004933.npy) |
| 4934 | `model.layers.0.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004934.npy) |
| 4935 | `model.layers.0.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.75 / 51.5 / 0.029395833611488342 / 5.690317737756353 | [NPY](tensors/0004935.npy) |
| 4936 | `model.layers.0.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0004936.npy) |
| 4937 | `model.layers.0.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.5625 / 4.03125 / 0.016885966062545776 / 1.1800325387513315 | [NPY](tensors/0004937.npy) |
| 4938 | `model.layers.0.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.1875 / 3.6875 / 0.006714132956858521 / 0.49494046336851194 | [NPY](tensors/0004938.npy) |
| 4939 | `model.layers.0.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.4375 / 43.25 / 0.03649657666683197 / 1.2796969429037848 | [NPY](tensors/0004939.npy) |
| 4940 | `model.layers.0.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.4375 / 43.25 / 0.03649657666683197 / 1.2796969429037848 | [NPY](tensors/0004940.npy) |
| 4941 | `model.layers.0.self_attn` | 42 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0028250430540292175 / 0.030352180846504474 | [NPY](tensors/0004941.npy) |
| 4942 | `model.layers.0.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 45.75 / -0.02754295137193468 / 3.0424678906914 | [NPY](tensors/0004942.npy) |
| 4943 | `model.layers.0.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8125 / 2.84375 / 0.0038325667381286623 / 0.3096731887358246 | [NPY](tensors/0004943.npy) |
| 4944 | `model.layers.0.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8125 / 2.84375 / 0.0038325667381286623 / 0.3096731887358246 | [NPY](tensors/0004944.npy) |
| 4945 | `model.layers.0.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.8125 / 2.84375 / 0.0038325667381286623 / 0.3096731887358246 | [NPY](tensors/0004945.npy) |
| 4946 | `model.layers.0.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4947 | `model.layers.0.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4948 | `model.layers.0.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4949 | `model.layers.0.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.53125 / 20.125 / 0.020698753371834754 / 0.7793067289093119 | [NPY](tensors/0004949.npy) |
| 4950 | `model.layers.0.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.53125 / 20.125 / 0.020698753371834754 / 0.7793067289093119 | [NPY](tensors/0004950.npy) |
| 4951 | `model.layers.0.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.515625 / 2.15625 / -0.047344207763671875 / 1.143069554515389 | [NPY](tensors/0004951.npy) |
| 4952 | `model.layers.0` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 65.0 / -0.006876309712727864 / 3.240368244516456 | [NPY](tensors/0004952.npy) |
| 5031 | `model.layers.0` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 50.75 / -0.03880806507335769 / 2.8720089898153187 | [NPY](tensors/0005031.npy) |
| 5032 | `model.layers.0` | 43 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005032.npy) |
| 5033 | `model.layers.0` | 43 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0005033.npy) |
| 5034 | `model.layers.0` | 43 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0005034.npy) |
| 5035 | `model.layers.0` | 43 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0005035.npy) |
| 5036 | `model.layers.0` | 43 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5037 | `model.layers.0` | 43 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5038 | `model.layers.0` | 43 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5039 | `model.layers.0.input_layernorm` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 50.75 / -0.03880806507335769 / 2.8720089898153187 | [NPY](tensors/0005039.npy) |
| 5040 | `model.layers.0.input_layernorm` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0005040.npy) |
| 5041 | `model.layers.0.self_attn` | 43 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0005041.npy) |
| 5042 | `model.layers.0.self_attn` | 43 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005042.npy) |
| 5043 | `model.layers.0.self_attn` | 43 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0005043.npy) |
| 5044 | `model.layers.0.self_attn` | 43 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5045 | `model.layers.0.self_attn` | 43 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5046 | `model.layers.0.self_attn` | 43 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0005046.npy) |
| 5047 | `model.layers.0.self_attn` | 43 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0005047.npy) |
| 5048 | `model.layers.0.self_attn` | 43 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5049 | `model.layers.0.self_attn.q_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0005049.npy) |
| 5050 | `model.layers.0.self_attn.q_proj` | 43 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.15625 / 6.84375 / 0.0022307498147711158 / 0.9416562142053898 | [NPY](tensors/0005050.npy) |
| 5051 | `model.layers.0.self_attn.k_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0005051.npy) |
| 5052 | `model.layers.0.self_attn.k_proj` | 43 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.0 / 42.75 / -0.03451061248779297 / 5.165071669827751 | [NPY](tensors/0005052.npy) |
| 5053 | `model.layers.0.self_attn.v_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0005053.npy) |
| 5054 | `model.layers.0.self_attn.v_proj` | 43 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.5625 / 3.5 / 0.010839223861694336 / 0.9793238812790538 | [NPY](tensors/0005054.npy) |
| 5055 | `model.layers.0.self_attn.o_proj` | 43 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.375 / 3.78125 / -0.0043052666951552965 / 0.5836589343021155 | [NPY](tensors/0005055.npy) |
| 5056 | `model.layers.0.self_attn.o_proj` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.5625 / 34.0 / 0.03739220466878679 / 1.0580238076215918 | [NPY](tensors/0005056.npy) |
| 5057 | `model.layers.0.self_attn` | 43 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.5625 / 34.0 / 0.03739220466878679 / 1.0580238076215918 | [NPY](tensors/0005057.npy) |
| 5058 | `model.layers.0.self_attn` | 43 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0033711509220180355 / 0.03661626369811236 | [NPY](tensors/0005058.npy) |
| 5059 | `model.layers.0.post_attention_layernorm` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 52.25 / -0.001423592037624783 / 2.9622269785550146 | [NPY](tensors/0005059.npy) |
| 5060 | `model.layers.0.post_attention_layernorm` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6796875 / 3.796875 / -0.006191072861353556 / 0.307006962731739 | [NPY](tensors/0005060.npy) |
| 5061 | `model.layers.0.mlp` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6796875 / 3.796875 / -0.006191072861353556 / 0.307006962731739 | [NPY](tensors/0005061.npy) |
| 5062 | `model.layers.0.mlp.experts` | 43 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.6796875 / 3.796875 / -0.006191072861353556 / 0.307006962731739 | [NPY](tensors/0005062.npy) |
| 5063 | `model.layers.0.mlp.experts` | 43 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5064 | `model.layers.0.mlp.experts` | 43 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5065 | `model.layers.0.mlp.experts` | 43 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5066 | `model.layers.0.mlp.experts` | 43 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.5 / 33.75 / 0.026793602315915956 / 1.0799154449630046 | [NPY](tensors/0005066.npy) |
| 5067 | `model.layers.0.mlp` | 43 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5 / 33.75 / 0.026793602315915956 / 1.0799154449630046 | [NPY](tensors/0005067.npy) |
| 5068 | `model.layers.0.mlp` | 43 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.0 / 2.3125 / -0.08465957641601562 / 1.0158910654935847 | [NPY](tensors/0005068.npy) |
| 5069 | `model.layers.0` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.375 / 69.0 / 0.025115701887342665 / 3.198953670409562 | [NPY](tensors/0005069.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.5056644772216706 / 49.741340386418365 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 297, 297] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.689059412825681e+38 / 1.694756088063524e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 297, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8016785844809279 / 0.8745460170790657 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 297, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12195024475191096 / 0.6221439169688554 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 297] | torch.int64 → int64 | 0.0 / 296.0 / 148.0 / 85.73602898820698 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.5056644772216706 / 49.741340386418365 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 297, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.06403203246201462 / 3.1864365948304862 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 297, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.06403203246201462 / 3.1864365948304862 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 297, 297] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.689059412825681e+38 / 1.694756088063524e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 297] | torch.int64 → int64 | 0.0 / 296.0 / 148.0 / 85.73602898820698 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 297, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8016785844809279 / 0.8745460170790657 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 297, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12195024475191096 / 0.6221439169688554 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.06403203246201462 / 3.1864365948304862 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 297, 4096] | torch.bfloat16 → float32 | -11.25 / 13.3125 / 0.04155091690900804 / 1.3266497721087425 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.06403203246201462 / 3.1864365948304862 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 297, 512] | torch.bfloat16 → float32 | -40.0 / 46.75 / 0.07911168344503877 / 3.6858974263098516 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.06403203246201462 / 3.1864365948304862 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 297, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.025495234161916406 / 2.4544376520068583 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 297, 4096] | torch.bfloat16 → float32 | -11.75 / 11.1875 / -0.02211424842661708 / 1.375314117695013 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 297, 2880] | torch.bfloat16 → float32 | -464.0 / 498.0 / -0.04034144207863072 / 6.536889929861397 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -464.0 / 498.0 / -0.04034144207863072 / 6.536889929861397 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 297, 297] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0028418510425538214 / 0.017712259814265417 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -41216.0 / 724.0 / 0.4654085845747468 / 48.881301954960755 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 297, 2880] | torch.bfloat16 → float32 | -78.5 / 6.3125 / 0.010387180388259316 / 0.7781310742810952 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -78.5 / 6.3125 / 0.010387180388259316 / 0.7781310742810952 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [297, 2880] | torch.bfloat16 → float32 | -78.5 / 6.3125 / 0.010387180388259316 / 0.7781310742810952 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [297, 2880] | torch.bfloat16 → float32 | -540.0 / 450.0 / 0.11764793355858286 / 9.051767020449857 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -540.0 / 450.0 / 0.11764793355858286 / 9.051767020449857 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [297, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.15567232703520392 / 0.7445883059455481 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 297, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.583042210137581 / 51.301359051608856 | [NPY](tensors/0000077.npy) |
| 156 | `model.layers.11` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -204.0 / 268.0 / 0.6120174407958985 / 16.996423168604256 | [NPY](tensors/0000156.npy) |
| 157 | `model.layers.11` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 298] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000157.npy) |
| 158 | `model.layers.11` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.4918212890625 / 1.117229907691466 | [NPY](tensors/0000158.npy) |
| 159 | `model.layers.11` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.3359375 / 0.18026646971702576 / 0.5362459422402894 | [NPY](tensors/0000159.npy) |
| 160 | `model.layers.11` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 297.0 / 297.0 / 297.0 / 0.0 | [NPY](tensors/0000160.npy) |
| 161 | `model.layers.11` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 162 | `model.layers.11` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 163 | `model.layers.11` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 164 | `model.layers.11.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -204.0 / 268.0 / 0.6120174407958985 / 16.996423168604256 | [NPY](tensors/0000164.npy) |
| 165 | `model.layers.11.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.0 / 74.0 / 0.08823374377356635 / 2.6115441659868615 | [NPY](tensors/0000165.npy) |
| 166 | `model.layers.11.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.0 / 74.0 / 0.08823374377356635 / 2.6115441659868615 | [NPY](tensors/0000166.npy) |
| 167 | `model.layers.11.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 298] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000167.npy) |
| 168 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 297.0 / 297.0 / 297.0 / 0.0 | [NPY](tensors/0000168.npy) |
| 169 | `model.layers.11.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 170 | `model.layers.11.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 171 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.4918212890625 / 1.117229907691466 | [NPY](tensors/0000171.npy) |
| 172 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.3359375 / 0.18026646971702576 / 0.5362459422402894 | [NPY](tensors/0000172.npy) |
| 173 | `model.layers.11.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 174 | `model.layers.11.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.0 / 74.0 / 0.08823374377356635 / 2.6115441659868615 | [NPY](tensors/0000174.npy) |
| 175 | `model.layers.11.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.4375 / 11.25 / 0.056488935835659504 / 1.3475291920121033 | [NPY](tensors/0000175.npy) |
| 176 | `model.layers.11.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.0 / 74.0 / 0.08823374377356635 / 2.6115441659868615 | [NPY](tensors/0000176.npy) |
| 177 | `model.layers.11.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.625 / 35.25 / 0.1038181334733963 / 3.828247958142739 | [NPY](tensors/0000177.npy) |
| 178 | `model.layers.11.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.0 / 74.0 / 0.08823374377356635 / 2.6115441659868615 | [NPY](tensors/0000178.npy) |
| 179 | `model.layers.11.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.28125 / 10.625 / -0.01979696750640869 / 2.6597833844263477 | [NPY](tensors/0000179.npy) |
| 180 | `model.layers.11.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 7.96875 / -0.021301613189280033 / 1.4812143706449725 | [NPY](tensors/0000180.npy) |
| 181 | `model.layers.11.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.75 / 70.5 / 0.06857673128445943 / 4.147651365603431 | [NPY](tensors/0000181.npy) |
| 182 | `model.layers.11.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.75 / 70.5 / 0.06857673128445943 / 4.147651365603431 | [NPY](tensors/0000182.npy) |
| 183 | `model.layers.11.self_attn` | 1 | `output[1]` | [1, 64, 1, 298] | torch.bfloat16 → float32 | 1.9826984498649836e-10 / 0.8046875 / 0.003117442102190821 / 0.010661974507695302 | [NPY](tensors/0000183.npy) |
| 184 | `model.layers.11.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -266.0 / 338.0 / 0.6802175733778212 / 18.961865623661303 | [NPY](tensors/0000184.npy) |
| 185 | `model.layers.11.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.609375 / 0.01346506824096044 / 0.7822406617065689 | [NPY](tensors/0000185.npy) |
| 186 | `model.layers.11.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.609375 / 0.01346506824096044 / 0.7822406617065689 | [NPY](tensors/0000186.npy) |
| 187 | `model.layers.11.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.09375 / 3.609375 / 0.01346506824096044 / 0.7822406617065689 | [NPY](tensors/0000187.npy) |
| 188 | `model.layers.11.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 189 | `model.layers.11.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 190 | `model.layers.11.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 191 | `model.layers.11.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -37.75 / 31.5 / 0.1502986643049452 / 5.308363044862237 | [NPY](tensors/0000191.npy) |
| 192 | `model.layers.11.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 31.5 / 0.1502986643049452 / 5.308363044862237 | [NPY](tensors/0000192.npy) |
| 193 | `model.layers.11.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.6171875 / -0.09896087646484375 / 0.634225220948479 | [NPY](tensors/0000193.npy) |
| 194 | `model.layers.11` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -304.0 / 370.0 / 0.829278564453125 / 20.63538633374647 | [NPY](tensors/0000194.npy) |
| 273 | `model.layers.11` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -302.0 / 356.0 / 0.5643966674804688 / 18.2837832450408 | [NPY](tensors/0000273.npy) |
| 274 | `model.layers.11` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 299] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000274.npy) |
| 275 | `model.layers.11` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.47601318359375 / 1.1300177711987256 | [NPY](tensors/0000275.npy) |
| 276 | `model.layers.11` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2265625 / 0.09335732460021973 / 0.5447921260742894 | [NPY](tensors/0000276.npy) |
| 277 | `model.layers.11` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 298.0 / 298.0 / 298.0 / 0.0 | [NPY](tensors/0000277.npy) |
| 278 | `model.layers.11` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 279 | `model.layers.11` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 280 | `model.layers.11` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 281 | `model.layers.11.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -302.0 / 356.0 / 0.5643966674804688 / 18.2837832450408 | [NPY](tensors/0000281.npy) |
| 282 | `model.layers.11.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 89.5 / 0.07571600808037651 / 3.021709879080471 | [NPY](tensors/0000282.npy) |
| 283 | `model.layers.11.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 89.5 / 0.07571600808037651 / 3.021709879080471 | [NPY](tensors/0000283.npy) |
| 284 | `model.layers.11.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 299] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000284.npy) |
| 285 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 298.0 / 298.0 / 298.0 / 0.0 | [NPY](tensors/0000285.npy) |
| 286 | `model.layers.11.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 287 | `model.layers.11.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 288 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.47601318359375 / 1.1300177711987256 | [NPY](tensors/0000288.npy) |
| 289 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2265625 / 0.09335732460021973 / 0.5447921260742894 | [NPY](tensors/0000289.npy) |
| 290 | `model.layers.11.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 291 | `model.layers.11.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 89.5 / 0.07571600808037651 / 3.021709879080471 | [NPY](tensors/0000291.npy) |
| 292 | `model.layers.11.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.59375 / 11.25 / 0.050249878666363657 / 1.2151264974171616 | [NPY](tensors/0000292.npy) |
| 293 | `model.layers.11.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 89.5 / 0.07571600808037651 / 3.021709879080471 | [NPY](tensors/0000293.npy) |
| 294 | `model.layers.11.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.875 / 35.25 / 0.1168442964553833 / 3.4570303062304575 | [NPY](tensors/0000294.npy) |
| 295 | `model.layers.11.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 89.5 / 0.07571600808037651 / 3.021709879080471 | [NPY](tensors/0000295.npy) |
| 296 | `model.layers.11.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.28125 / 5.90625 / -0.0007684230804443359 / 1.9191963620837529 | [NPY](tensors/0000296.npy) |
| 297 | `model.layers.11.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.25 / 6.53125 / -0.008318373467773199 / 1.2801408229833422 | [NPY](tensors/0000297.npy) |
| 298 | `model.layers.11.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 40.5 / -0.023582589626312257 / 3.461488336577244 | [NPY](tensors/0000298.npy) |
| 299 | `model.layers.11.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 40.5 / -0.023582589626312257 / 3.461488336577244 | [NPY](tensors/0000299.npy) |
| 300 | `model.layers.11.self_attn` | 2 | `output[1]` | [1, 64, 1, 299] | torch.bfloat16 → float32 | 1.255102688446641e-10 / 0.94921875 / 0.0031554921230657674 / 0.012259292227282143 | [NPY](tensors/0000300.npy) |
| 301 | `model.layers.11.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -302.0 / 344.0 / 0.5414298163519965 / 19.115809515812604 | [NPY](tensors/0000301.npy) |
| 302 | `model.layers.11.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.734375 / 2.796875 / 0.000965885321299235 / 0.7345277408076066 | [NPY](tensors/0000302.npy) |
| 303 | `model.layers.11.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.734375 / 2.796875 / 0.000965885321299235 / 0.7345277408076066 | [NPY](tensors/0000303.npy) |
| 304 | `model.layers.11.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.734375 / 2.796875 / 0.000965885321299235 / 0.7345277408076066 | [NPY](tensors/0000304.npy) |
| 305 | `model.layers.11.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 306 | `model.layers.11.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 307 | `model.layers.11.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 308 | `model.layers.11.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -56.75 / 111.0 / 0.21162216398451064 / 5.704038451172061 | [NPY](tensors/0000308.npy) |
| 309 | `model.layers.11.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -56.75 / 111.0 / 0.21162216398451064 / 5.704038451172061 | [NPY](tensors/0000309.npy) |
| 310 | `model.layers.11.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.4921875 / 1.0859375 / -0.06881332397460938 / 0.6174531129957802 | [NPY](tensors/0000310.npy) |
| 311 | `model.layers.11` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -358.0 / 416.0 / 0.7534871419270833 / 22.04394586606025 | [NPY](tensors/0000311.npy) |
| 390 | `model.layers.11` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -197.0 / 320.0 / 0.5442208184136285 / 14.749014240161236 | [NPY](tensors/0000390.npy) |
| 391 | `model.layers.11` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 300] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000391.npy) |
| 392 | `model.layers.11` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.518310546875 / 1.0946292885024063 | [NPY](tensors/0000392.npy) |
| 393 | `model.layers.11` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.234375 / 0.009437993168830872 / 0.5857162614275052 | [NPY](tensors/0000393.npy) |
| 394 | `model.layers.11` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 299.0 / 299.0 / 299.0 / 0.0 | [NPY](tensors/0000394.npy) |
| 395 | `model.layers.11` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 396 | `model.layers.11` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 397 | `model.layers.11` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 398 | `model.layers.11.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -197.0 / 320.0 / 0.5442208184136285 / 14.749014240161236 | [NPY](tensors/0000398.npy) |
| 399 | `model.layers.11.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 94.5 / 0.0872157335281372 / 3.007304677997496 | [NPY](tensors/0000399.npy) |
| 400 | `model.layers.11.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 94.5 / 0.0872157335281372 / 3.007304677997496 | [NPY](tensors/0000400.npy) |
| 401 | `model.layers.11.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 300] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000401.npy) |
| 402 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 299.0 / 299.0 / 299.0 / 0.0 | [NPY](tensors/0000402.npy) |
| 403 | `model.layers.11.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 404 | `model.layers.11.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 405 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.518310546875 / 1.0946292885024063 | [NPY](tensors/0000405.npy) |
| 406 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.234375 / 0.009437993168830872 / 0.5857162614275052 | [NPY](tensors/0000406.npy) |
| 407 | `model.layers.11.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 408 | `model.layers.11.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 94.5 / 0.0872157335281372 / 3.007304677997496 | [NPY](tensors/0000408.npy) |
| 409 | `model.layers.11.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.75 / 8.1875 / 0.04929582026670687 / 1.264322530727703 | [NPY](tensors/0000409.npy) |
| 410 | `model.layers.11.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 94.5 / 0.0872157335281372 / 3.007304677997496 | [NPY](tensors/0000410.npy) |
| 411 | `model.layers.11.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.75 / 40.25 / 0.11284226179122925 / 4.166593211110833 | [NPY](tensors/0000411.npy) |
| 412 | `model.layers.11.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 94.5 / 0.0872157335281372 / 3.007304677997496 | [NPY](tensors/0000412.npy) |
| 413 | `model.layers.11.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.6875 / 6.375 / -0.011392354965209961 / 2.1783338751602077 | [NPY](tensors/0000413.npy) |
| 414 | `model.layers.11.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.90625 / 7.0625 / -0.006351752672344446 / 1.3122563637640212 | [NPY](tensors/0000414.npy) |
| 415 | `model.layers.11.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 45.25 / 0.029833575752046374 / 3.2163319607221084 | [NPY](tensors/0000415.npy) |
| 416 | `model.layers.11.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 45.25 / 0.029833575752046374 / 3.2163319607221084 | [NPY](tensors/0000416.npy) |
| 417 | `model.layers.11.self_attn` | 3 | `output[1]` | [1, 64, 1, 300] | torch.bfloat16 → float32 | 4.1109160520136356e-10 / 0.89453125 / 0.0031299392303102045 / 0.012438277021483514 | [NPY](tensors/0000417.npy) |
| 418 | `model.layers.11.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -211.0 / 342.0 / 0.5735787285698785 / 16.041375163237284 | [NPY](tensors/0000418.npy) |
| 419 | `model.layers.11.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.578125 / 2.640625 / 0.012966105673048232 / 0.6897906287535818 | [NPY](tensors/0000419.npy) |
| 420 | `model.layers.11.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.578125 / 2.640625 / 0.012966105673048232 / 0.6897906287535818 | [NPY](tensors/0000420.npy) |
| 421 | `model.layers.11.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.578125 / 2.640625 / 0.012966105673048232 / 0.6897906287535818 | [NPY](tensors/0000421.npy) |
| 422 | `model.layers.11.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 423 | `model.layers.11.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 424 | `model.layers.11.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 425 | `model.layers.11.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -49.75 / 40.75 / 0.05725773572921753 / 3.8103337594007307 | [NPY](tensors/0000425.npy) |
| 426 | `model.layers.11.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.75 / 40.75 / 0.05725773572921753 / 3.8103337594007307 | [NPY](tensors/0000426.npy) |
| 427 | `model.layers.11.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.078125 / 1.0390625 / -0.07164382934570312 / 0.4590236782527649 | [NPY](tensors/0000427.npy) |
| 428 | `model.layers.11` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -260.0 / 354.0 / 0.6306771172417535 / 17.23173949876864 | [NPY](tensors/0000428.npy) |
| 507 | `model.layers.11` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -340.0 / 476.0 / 0.7894444783528646 / 19.47664700821977 | [NPY](tensors/0000507.npy) |
| 508 | `model.layers.11` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 301] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000508.npy) |
| 509 | `model.layers.11` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6011199951171875 / 1.029134772776266 | [NPY](tensors/0000509.npy) |
| 510 | `model.layers.11` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.02744269371032715 / 0.6241199078176489 | [NPY](tensors/0000510.npy) |
| 511 | `model.layers.11` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 300.0 / 300.0 / 300.0 / 0.0 | [NPY](tensors/0000511.npy) |
| 512 | `model.layers.11` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 513 | `model.layers.11` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 514 | `model.layers.11` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 515 | `model.layers.11.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -340.0 / 476.0 / 0.7894444783528646 / 19.47664700821977 | [NPY](tensors/0000515.npy) |
| 516 | `model.layers.11.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.5 / 114.5 / 0.08764225112067328 / 3.389970217835287 | [NPY](tensors/0000516.npy) |
| 517 | `model.layers.11.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.5 / 114.5 / 0.08764225112067328 / 3.389970217835287 | [NPY](tensors/0000517.npy) |
| 518 | `model.layers.11.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 301] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000518.npy) |
| 519 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 300.0 / 300.0 / 300.0 / 0.0 | [NPY](tensors/0000519.npy) |
| 520 | `model.layers.11.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 521 | `model.layers.11.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 522 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6011199951171875 / 1.029134772776266 | [NPY](tensors/0000522.npy) |
| 523 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.02744269371032715 / 0.6241199078176489 | [NPY](tensors/0000523.npy) |
| 524 | `model.layers.11.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 525 | `model.layers.11.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.5 / 114.5 / 0.08764225112067328 / 3.389970217835287 | [NPY](tensors/0000525.npy) |
| 526 | `model.layers.11.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 8.0625 / 0.051300788298249245 / 1.1916800655587692 | [NPY](tensors/0000526.npy) |
| 527 | `model.layers.11.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.5 / 114.5 / 0.08764225112067328 / 3.389970217835287 | [NPY](tensors/0000527.npy) |
| 528 | `model.layers.11.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.25 / 46.0 / 0.13708239421248436 / 4.1743255215249695 | [NPY](tensors/0000528.npy) |
| 529 | `model.layers.11.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.5 / 114.5 / 0.08764225112067328 / 3.389970217835287 | [NPY](tensors/0000529.npy) |
| 530 | `model.layers.11.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.40625 / 7.5 / 0.07434272766113281 / 1.9077477009393857 | [NPY](tensors/0000530.npy) |
| 531 | `model.layers.11.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.34375 / 7.0 / -0.0013478659093379974 / 1.3224406664756259 | [NPY](tensors/0000531.npy) |
| 532 | `model.layers.11.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.125 / 52.75 / 0.01916878488328722 / 3.746938041849371 | [NPY](tensors/0000532.npy) |
| 533 | `model.layers.11.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.125 / 52.75 / 0.01916878488328722 / 3.746938041849371 | [NPY](tensors/0000533.npy) |
| 534 | `model.layers.11.self_attn` | 4 | `output[1]` | [1, 64, 1, 301] | torch.bfloat16 → float32 | 2.0190782379359007e-10 / 0.9296875 / 0.0030852570423953005 / 0.01426680373169233 | [NPY](tensors/0000534.npy) |
| 535 | `model.layers.11.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -296.0 / 448.0 / 0.8096463521321614 / 20.052828662133336 | [NPY](tensors/0000535.npy) |
| 536 | `model.layers.11.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.71875 / 3.0625 / 0.018782921632130942 / 0.6399390151907496 | [NPY](tensors/0000536.npy) |
| 537 | `model.layers.11.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.71875 / 3.0625 / 0.018782921632130942 / 0.6399390151907496 | [NPY](tensors/0000537.npy) |
| 538 | `model.layers.11.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.71875 / 3.0625 / 0.018782921632130942 / 0.6399390151907496 | [NPY](tensors/0000538.npy) |
| 539 | `model.layers.11.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 540 | `model.layers.11.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 541 | `model.layers.11.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 542 | `model.layers.11.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -107.5 / 107.0 / 0.08833406236436632 / 4.721874980740597 | [NPY](tensors/0000542.npy) |
| 543 | `model.layers.11.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -107.5 / 107.0 / 0.08833406236436632 / 4.721874980740597 | [NPY](tensors/0000543.npy) |
| 544 | `model.layers.11.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.2265625 / 0.9609375 / -0.07172298431396484 / 0.45757875838617557 | [NPY](tensors/0000544.npy) |
| 545 | `model.layers.11` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -404.0 / 556.0 / 0.8976735432942708 / 22.996872649333998 | [NPY](tensors/0000545.npy) |
| 624 | `model.layers.11` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -334.0 / 426.0 / 0.21383226182725695 / 18.585752479739206 | [NPY](tensors/0000624.npy) |
| 625 | `model.layers.11` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 302] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000625.npy) |
| 626 | `model.layers.11` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6781768798828125 / 0.9972778713983161 | [NPY](tensors/0000626.npy) |
| 627 | `model.layers.11` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.0019666850566864014 / 0.5958225425092146 | [NPY](tensors/0000627.npy) |
| 628 | `model.layers.11` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 301.0 / 301.0 / 301.0 / 0.0 | [NPY](tensors/0000628.npy) |
| 629 | `model.layers.11` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 630 | `model.layers.11` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 631 | `model.layers.11` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 632 | `model.layers.11.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -334.0 / 426.0 / 0.21383226182725695 / 18.585752479739206 | [NPY](tensors/0000632.npy) |
| 633 | `model.layers.11.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 92.0 / 0.02792636553446452 / 3.201222557639413 | [NPY](tensors/0000633.npy) |
| 634 | `model.layers.11.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 92.0 / 0.02792636553446452 / 3.201222557639413 | [NPY](tensors/0000634.npy) |
| 635 | `model.layers.11.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 302] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000635.npy) |
| 636 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 301.0 / 301.0 / 301.0 / 0.0 | [NPY](tensors/0000636.npy) |
| 637 | `model.layers.11.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 638 | `model.layers.11.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 639 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6781768798828125 / 0.9972778713983161 | [NPY](tensors/0000639.npy) |
| 640 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.0019666850566864014 / 0.5958225425092146 | [NPY](tensors/0000640.npy) |
| 641 | `model.layers.11.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 642 | `model.layers.11.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 92.0 / 0.02792636553446452 / 3.201222557639413 | [NPY](tensors/0000642.npy) |
| 643 | `model.layers.11.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 10.0625 / 0.05914515070617199 / 1.2596641678189728 | [NPY](tensors/0000643.npy) |
| 644 | `model.layers.11.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 92.0 / 0.02792636553446452 / 3.201222557639413 | [NPY](tensors/0000644.npy) |
| 645 | `model.layers.11.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.0 / 48.25 / 0.20459964871406555 / 4.448501171925651 | [NPY](tensors/0000645.npy) |
| 646 | `model.layers.11.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 92.0 / 0.02792636553446452 / 3.201222557639413 | [NPY](tensors/0000646.npy) |
| 647 | `model.layers.11.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.5625 / 7.75 / -0.050304293632507324 / 2.178285971822371 | [NPY](tensors/0000647.npy) |
| 648 | `model.layers.11.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.96875 / 7.4375 / -0.023066909983754158 / 1.4316888194014261 | [NPY](tensors/0000648.npy) |
| 649 | `model.layers.11.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.125 / 57.5 / -0.010915872785780165 / 3.8477302031048475 | [NPY](tensors/0000649.npy) |
| 650 | `model.layers.11.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.125 / 57.5 / -0.010915872785780165 / 3.8477302031048475 | [NPY](tensors/0000650.npy) |
| 651 | `model.layers.11.self_attn` | 5 | `output[1]` | [1, 64, 1, 302] | torch.bfloat16 → float32 | 1.3358203432289883e-11 / 0.96484375 / 0.0031443917984981264 / 0.016028923957183968 | [NPY](tensors/0000651.npy) |
| 652 | `model.layers.11.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -276.0 / 424.0 / 0.20276319715711805 / 19.427288167909044 | [NPY](tensors/0000652.npy) |
| 653 | `model.layers.11.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.125 / 2.859375 / -0.005379579464594523 / 0.6699705816269605 | [NPY](tensors/0000653.npy) |
| 654 | `model.layers.11.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.125 / 2.859375 / -0.005379579464594523 / 0.6699705816269605 | [NPY](tensors/0000654.npy) |
| 655 | `model.layers.11.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.125 / 2.859375 / -0.005379579464594523 / 0.6699705816269605 | [NPY](tensors/0000655.npy) |
| 656 | `model.layers.11.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 657 | `model.layers.11.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 658 | `model.layers.11.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 659 | `model.layers.11.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -145.0 / 150.0 / 0.013011034329732258 / 6.1321205758855575 | [NPY](tensors/0000659.npy) |
| 660 | `model.layers.11.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -145.0 / 150.0 / 0.013011034329732258 / 6.1321205758855575 | [NPY](tensors/0000660.npy) |
| 661 | `model.layers.11.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.90625 / 0.76953125 / -0.1632232666015625 / 0.5506227301946327 | [NPY](tensors/0000661.npy) |
| 662 | `model.layers.11` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -420.0 / 502.0 / 0.21563712226019965 / 23.3122400354915 | [NPY](tensors/0000662.npy) |
| 741 | `model.layers.11` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -356.0 / 440.0 / 0.3933208889431424 / 19.377570946663937 | [NPY](tensors/0000741.npy) |
| 742 | `model.layers.11` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 303] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000742.npy) |
| 743 | `model.layers.11` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.707061767578125 / 0.9717983302810768 | [NPY](tensors/0000743.npy) |
| 744 | `model.layers.11` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.234375 / 0.05849510431289673 / 0.601804974311013 | [NPY](tensors/0000744.npy) |
| 745 | `model.layers.11` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 302.0 / 302.0 / 302.0 / 0.0 | [NPY](tensors/0000745.npy) |
| 746 | `model.layers.11` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 747 | `model.layers.11` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 748 | `model.layers.11` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 749 | `model.layers.11.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -356.0 / 440.0 / 0.3933208889431424 / 19.377570946663937 | [NPY](tensors/0000749.npy) |
| 750 | `model.layers.11.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -96.5 / 106.5 / 0.044551899698045516 / 3.32424860075225 | [NPY](tensors/0000750.npy) |
| 751 | `model.layers.11.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -96.5 / 106.5 / 0.044551899698045516 / 3.32424860075225 | [NPY](tensors/0000751.npy) |
| 752 | `model.layers.11.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 303] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000752.npy) |
| 753 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 302.0 / 302.0 / 302.0 / 0.0 | [NPY](tensors/0000753.npy) |
| 754 | `model.layers.11.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 755 | `model.layers.11.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 756 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.707061767578125 / 0.9717983302810768 | [NPY](tensors/0000756.npy) |
| 757 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.234375 / 0.05849510431289673 / 0.601804974311013 | [NPY](tensors/0000757.npy) |
| 758 | `model.layers.11.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 759 | `model.layers.11.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -96.5 / 106.5 / 0.044551899698045516 / 3.32424860075225 | [NPY](tensors/0000759.npy) |
| 760 | `model.layers.11.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.78125 / 9.125 / 0.06427011359483004 / 1.219295787271102 | [NPY](tensors/0000760.npy) |
| 761 | `model.layers.11.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -96.5 / 106.5 / 0.044551899698045516 / 3.32424860075225 | [NPY](tensors/0000761.npy) |
| 762 | `model.layers.11.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 49.0 / 0.14118171110749245 / 4.3050033109340085 | [NPY](tensors/0000762.npy) |
| 763 | `model.layers.11.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -96.5 / 106.5 / 0.044551899698045516 / 3.32424860075225 | [NPY](tensors/0000763.npy) |
| 764 | `model.layers.11.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.65625 / 11.0 / -0.02739008516073227 / 2.230490404363678 | [NPY](tensors/0000764.npy) |
| 765 | `model.layers.11.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.03125 / 8.0 / -0.0027020839042961597 / 1.5114224634899471 | [NPY](tensors/0000765.npy) |
| 766 | `model.layers.11.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.75 / 79.0 / 0.03050983879301283 / 3.9397713434212798 | [NPY](tensors/0000766.npy) |
| 767 | `model.layers.11.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.75 / 79.0 / 0.03050983879301283 / 3.9397713434212798 | [NPY](tensors/0000767.npy) |
| 768 | `model.layers.11.self_attn` | 6 | `output[1]` | [1, 64, 1, 303] | torch.bfloat16 → float32 | 5.5138116294983774e-12 / 0.96875 / 0.0030695270426450588 / 0.016918024659115266 | [NPY](tensors/0000768.npy) |
| 769 | `model.layers.11.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -276.0 / 386.0 / 0.4243267483181424 / 19.5327068299538 | [NPY](tensors/0000769.npy) |
| 770 | `model.layers.11.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.65625 / 5.09375 / 0.01226971877945794 / 0.6692276801004083 | [NPY](tensors/0000770.npy) |
| 771 | `model.layers.11.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.65625 / 5.09375 / 0.01226971877945794 / 0.6692276801004083 | [NPY](tensors/0000771.npy) |
| 772 | `model.layers.11.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.65625 / 5.09375 / 0.01226971877945794 / 0.6692276801004083 | [NPY](tensors/0000772.npy) |
| 773 | `model.layers.11.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 774 | `model.layers.11.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 775 | `model.layers.11.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 776 | `model.layers.11.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -164.0 / 172.0 / 0.08156438403659397 / 6.9912234432886535 | [NPY](tensors/0000776.npy) |
| 777 | `model.layers.11.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -164.0 / 172.0 / 0.08156438403659397 / 6.9912234432886535 | [NPY](tensors/0000777.npy) |
| 778 | `model.layers.11.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3984375 / 1.1796875 / -0.11783599853515625 / 0.5680806137026951 | [NPY](tensors/0000778.npy) |
| 779 | `model.layers.11` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -440.0 / 560.0 / 0.5067053053114149 / 24.12461117129565 | [NPY](tensors/0000779.npy) |
| 858 | `model.layers.11` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -262.0 / 378.0 / 0.5270063612196181 / 17.167558271064607 | [NPY](tensors/0000858.npy) |
| 859 | `model.layers.11` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 304] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000859.npy) |
| 860 | `model.layers.11` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.68243408203125 / 0.9684034292887866 | [NPY](tensors/0000860.npy) |
| 861 | `model.layers.11` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3359375 / 0.10489383339881897 / 0.6297841334602801 | [NPY](tensors/0000861.npy) |
| 862 | `model.layers.11` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 303.0 / 303.0 / 303.0 / 0.0 | [NPY](tensors/0000862.npy) |
| 863 | `model.layers.11` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 864 | `model.layers.11` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 865 | `model.layers.11` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 866 | `model.layers.11.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -262.0 / 378.0 / 0.5270063612196181 / 17.167558271064607 | [NPY](tensors/0000866.npy) |
| 867 | `model.layers.11.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 103.0 / 0.07984282506836785 / 3.128029488002834 | [NPY](tensors/0000867.npy) |
| 868 | `model.layers.11.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 103.0 / 0.07984282506836785 / 3.128029488002834 | [NPY](tensors/0000868.npy) |
| 869 | `model.layers.11.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 304] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000869.npy) |
| 870 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 303.0 / 303.0 / 303.0 / 0.0 | [NPY](tensors/0000870.npy) |
| 871 | `model.layers.11.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 872 | `model.layers.11.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 873 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.68243408203125 / 0.9684034292887866 | [NPY](tensors/0000873.npy) |
| 874 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3359375 / 0.10489383339881897 / 0.6297841334602801 | [NPY](tensors/0000874.npy) |
| 875 | `model.layers.11.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 876 | `model.layers.11.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 103.0 / 0.07984282506836785 / 3.128029488002834 | [NPY](tensors/0000876.npy) |
| 877 | `model.layers.11.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.9375 / 8.3125 / 0.05880276300013065 / 1.2766093527187539 | [NPY](tensors/0000877.npy) |
| 878 | `model.layers.11.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 103.0 / 0.07984282506836785 / 3.128029488002834 | [NPY](tensors/0000878.npy) |
| 879 | `model.layers.11.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.5 / 44.25 / 0.19921874441206455 / 4.134270374943797 | [NPY](tensors/0000879.npy) |
| 880 | `model.layers.11.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 103.0 / 0.07984282506836785 / 3.128029488002834 | [NPY](tensors/0000880.npy) |
| 881 | `model.layers.11.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.78125 / 9.0 / -0.027241945266723633 / 2.221244386043376 | [NPY](tensors/0000881.npy) |
| 882 | `model.layers.11.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.71875 / 7.625 / -0.012205835664644837 / 1.355620334265707 | [NPY](tensors/0000882.npy) |
| 883 | `model.layers.11.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.5 / 70.0 / 0.06641879743999905 / 3.694567000238091 | [NPY](tensors/0000883.npy) |
| 884 | `model.layers.11.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.5 / 70.0 / 0.06641879743999905 / 3.694567000238091 | [NPY](tensors/0000884.npy) |
| 885 | `model.layers.11.self_attn` | 7 | `output[1]` | [1, 64, 1, 304] | torch.bfloat16 → float32 | 1.9372237147763371e-10 / 0.92578125 / 0.0030634104191267454 / 0.014335678588528532 | [NPY](tensors/0000885.npy) |
| 886 | `model.layers.11.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -260.0 / 408.0 / 0.5934566921657987 / 18.76152750727597 | [NPY](tensors/0000886.npy) |
| 887 | `model.layers.11.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.171875 / 2.71875 / 0.021156876617007787 / 0.6999386227119665 | [NPY](tensors/0000887.npy) |
| 888 | `model.layers.11.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.171875 / 2.71875 / 0.021156876617007787 / 0.6999386227119665 | [NPY](tensors/0000888.npy) |
| 889 | `model.layers.11.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.171875 / 2.71875 / 0.021156876617007787 / 0.6999386227119665 | [NPY](tensors/0000889.npy) |
| 890 | `model.layers.11.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 891 | `model.layers.11.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 892 | `model.layers.11.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 893 | `model.layers.11.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -137.0 / 80.5 / -0.05807056294547187 / 4.600761009951325 | [NPY](tensors/0000893.npy) |
| 894 | `model.layers.11.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -137.0 / 80.5 / -0.05807056294547187 / 4.600761009951325 | [NPY](tensors/0000894.npy) |
| 895 | `model.layers.11.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.09375 / 0.7109375 / -0.04345327615737915 / 0.44303727708091445 | [NPY](tensors/0000895.npy) |
| 896 | `model.layers.11` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -396.0 / 488.0 / 0.5345309787326389 / 21.13320244706762 | [NPY](tensors/0000896.npy) |
| 975 | `model.layers.11` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -362.0 / 512.0 / 0.47131449381510415 / 21.549191708250365 | [NPY](tensors/0000975.npy) |
| 976 | `model.layers.11` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 305] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000976.npy) |
| 977 | `model.layers.11` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6405029296875 / 1.0356892994687845 | [NPY](tensors/0000977.npy) |
| 978 | `model.layers.11` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1875 / 1.2421875 / 0.10542488098144531 / 0.5631099040524371 | [NPY](tensors/0000978.npy) |
| 979 | `model.layers.11` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 304.0 / 304.0 / 304.0 / 0.0 | [NPY](tensors/0000979.npy) |
| 980 | `model.layers.11` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 981 | `model.layers.11` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 982 | `model.layers.11` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 983 | `model.layers.11.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -362.0 / 512.0 / 0.47131449381510415 / 21.549191708250365 | [NPY](tensors/0000983.npy) |
| 984 | `model.layers.11.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 111.5 / 0.06314765744739109 / 3.3015012364548815 | [NPY](tensors/0000984.npy) |
| 985 | `model.layers.11.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 111.5 / 0.06314765744739109 / 3.3015012364548815 | [NPY](tensors/0000985.npy) |
| 986 | `model.layers.11.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 305] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000986.npy) |
| 987 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 304.0 / 304.0 / 304.0 / 0.0 | [NPY](tensors/0000987.npy) |
| 988 | `model.layers.11.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 989 | `model.layers.11.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 990 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6405029296875 / 1.0356892994687845 | [NPY](tensors/0000990.npy) |
| 991 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1875 / 1.2421875 / 0.10542488098144531 / 0.5631099040524371 | [NPY](tensors/0000991.npy) |
| 992 | `model.layers.11.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 993 | `model.layers.11.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 111.5 / 0.06314765744739109 / 3.3015012364548815 | [NPY](tensors/0000993.npy) |
| 994 | `model.layers.11.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.59375 / 8.125 / 0.08029371983138844 / 1.2323588844319366 | [NPY](tensors/0000994.npy) |
| 995 | `model.layers.11.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 111.5 / 0.06314765744739109 / 3.3015012364548815 | [NPY](tensors/0000995.npy) |
| 996 | `model.layers.11.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.25 / 37.75 / 0.22621294856071472 / 3.599256074382832 | [NPY](tensors/0000996.npy) |
| 997 | `model.layers.11.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 111.5 / 0.06314765744739109 / 3.3015012364548815 | [NPY](tensors/0000997.npy) |
| 998 | `model.layers.11.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.625 / 6.65625 / 0.04256176948547363 / 2.1684448430927232 | [NPY](tensors/0000998.npy) |
| 999 | `model.layers.11.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.46875 / 6.75 / -0.005300831398926675 / 1.3094079824044826 | [NPY](tensors/0000999.npy) |
| 1000 | `model.layers.11.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 67.0 / 0.027354560958014595 / 3.974775882574112 | [NPY](tensors/0001000.npy) |
| 1001 | `model.layers.11.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 67.0 / 0.027354560958014595 / 3.974775882574112 | [NPY](tensors/0001001.npy) |
| 1002 | `model.layers.11.self_attn` | 8 | `output[1]` | [1, 64, 1, 305] | torch.bfloat16 → float32 | 2.8762769943568856e-11 / 0.98046875 / 0.0029478903103208843 / 0.014774247281903092 | [NPY](tensors/0001002.npy) |
| 1003 | `model.layers.11.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -304.0 / 466.0 / 0.49856465657552085 / 21.84504643403109 | [NPY](tensors/0001003.npy) |
| 1004 | `model.layers.11.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.90625 / 2.796875 / 0.0058284507857428655 / 0.7094504122447549 | [NPY](tensors/0001004.npy) |
| 1005 | `model.layers.11.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.90625 / 2.796875 / 0.0058284507857428655 / 0.7094504122447549 | [NPY](tensors/0001005.npy) |
| 1006 | `model.layers.11.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.90625 / 2.796875 / 0.0058284507857428655 / 0.7094504122447549 | [NPY](tensors/0001006.npy) |
| 1007 | `model.layers.11.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1008 | `model.layers.11.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1009 | `model.layers.11.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1010 | `model.layers.11.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -154.0 / 112.0 / -0.09056916236877441 / 5.606104958184937 | [NPY](tensors/0001010.npy) |
| 1011 | `model.layers.11.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -154.0 / 112.0 / -0.09056916236877441 / 5.606104958184937 | [NPY](tensors/0001011.npy) |
| 1012 | `model.layers.11.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.375 / 0.7890625 / -0.0580143928527832 / 0.48257332542903275 | [NPY](tensors/0001012.npy) |
| 1013 | `model.layers.11` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -458.0 / 576.0 / 0.40907355414496527 / 24.91860191366821 | [NPY](tensors/0001013.npy) |
| 1092 | `model.layers.11` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -368.0 / 476.0 / 0.2818070305718316 / 20.44622586027249 | [NPY](tensors/0001092.npy) |
| 1093 | `model.layers.11` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 306] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001093.npy) |
| 1094 | `model.layers.11` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0001094.npy) |
| 1095 | `model.layers.11` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0001095.npy) |
| 1096 | `model.layers.11` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0001096.npy) |
| 1097 | `model.layers.11` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1098 | `model.layers.11` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1099 | `model.layers.11` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1100 | `model.layers.11.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -368.0 / 476.0 / 0.2818070305718316 / 20.44622586027249 | [NPY](tensors/0001100.npy) |
| 1101 | `model.layers.11.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 99.5 / 0.03452457520696852 / 3.225123693264157 | [NPY](tensors/0001101.npy) |
| 1102 | `model.layers.11.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 99.5 / 0.03452457520696852 / 3.225123693264157 | [NPY](tensors/0001102.npy) |
| 1103 | `model.layers.11.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 306] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001103.npy) |
| 1104 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0001104.npy) |
| 1105 | `model.layers.11.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1106 | `model.layers.11.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1107 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0001107.npy) |
| 1108 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0001108.npy) |
| 1109 | `model.layers.11.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1110 | `model.layers.11.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 99.5 / 0.03452457520696852 / 3.225123693264157 | [NPY](tensors/0001110.npy) |
| 1111 | `model.layers.11.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5625 / 8.8125 / 0.041204644832760096 / 1.2399017997246016 | [NPY](tensors/0001111.npy) |
| 1112 | `model.layers.11.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 99.5 / 0.03452457520696852 / 3.225123693264157 | [NPY](tensors/0001112.npy) |
| 1113 | `model.layers.11.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.25 / 42.0 / 0.16281624510884285 / 4.089563379756607 | [NPY](tensors/0001113.npy) |
| 1114 | `model.layers.11.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.5 / 99.5 / 0.03452457520696852 / 3.225123693264157 | [NPY](tensors/0001114.npy) |
| 1115 | `model.layers.11.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.0625 / 7.75 / -0.0727115273475647 / 2.3572004521690726 | [NPY](tensors/0001115.npy) |
| 1116 | `model.layers.11.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.53125 / 7.21875 / -0.01612893957644701 / 1.4234505845280099 | [NPY](tensors/0001116.npy) |
| 1117 | `model.layers.11.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 58.75 / 0.019241147571139865 / 4.18991989669863 | [NPY](tensors/0001117.npy) |
| 1118 | `model.layers.11.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 58.75 / 0.019241147571139865 / 4.18991989669863 | [NPY](tensors/0001118.npy) |
| 1119 | `model.layers.11.self_attn` | 9 | `output[1]` | [1, 64, 1, 306] | torch.bfloat16 → float32 | 2.1827872842550278e-11 / 0.953125 / 0.0030796809644283215 / 0.01705132937921351 | [NPY](tensors/0001119.npy) |
| 1120 | `model.layers.11.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -310.0 / 480.0 / 0.301556396484375 / 21.08854318856883 | [NPY](tensors/0001120.npy) |
| 1121 | `model.layers.11.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.828125 / 2.640625 / -0.005272034141752455 / 0.678827759258283 | [NPY](tensors/0001121.npy) |
| 1122 | `model.layers.11.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.828125 / 2.640625 / -0.005272034141752455 / 0.678827759258283 | [NPY](tensors/0001122.npy) |
| 1123 | `model.layers.11.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.828125 / 2.640625 / -0.005272034141752455 / 0.678827759258283 | [NPY](tensors/0001123.npy) |
| 1124 | `model.layers.11.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1125 | `model.layers.11.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1126 | `model.layers.11.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1127 | `model.layers.11.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -163.0 / 191.0 / 0.19094341066148546 / 7.735707216591955 | [NPY](tensors/0001127.npy) |
| 1128 | `model.layers.11.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -163.0 / 191.0 / 0.19094341066148546 / 7.735707216591955 | [NPY](tensors/0001128.npy) |
| 1129 | `model.layers.11.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.03125 / 0.8359375 / -0.11899948120117188 / 0.40461892407365607 | [NPY](tensors/0001129.npy) |
| 1130 | `model.layers.11` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -472.0 / 588.0 / 0.4941036648220486 / 26.34611098783084 | [NPY](tensors/0001130.npy) |
| 1209 | `model.layers.11` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -232.0 / 358.0 / 0.7790286593967014 / 17.46671079208254 | [NPY](tensors/0001209.npy) |
| 1210 | `model.layers.11` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 307] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001210.npy) |
| 1211 | `model.layers.11` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0001211.npy) |
| 1212 | `model.layers.11` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0001212.npy) |
| 1213 | `model.layers.11` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0001213.npy) |
| 1214 | `model.layers.11` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1215 | `model.layers.11` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1216 | `model.layers.11` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1217 | `model.layers.11.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -232.0 / 358.0 / 0.7790286593967014 / 17.46671079208254 | [NPY](tensors/0001217.npy) |
| 1218 | `model.layers.11.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 91.0 / 0.1032887856165568 / 2.9522145169196565 | [NPY](tensors/0001218.npy) |
| 1219 | `model.layers.11.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 91.0 / 0.1032887856165568 / 2.9522145169196565 | [NPY](tensors/0001219.npy) |
| 1220 | `model.layers.11.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 307] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001220.npy) |
| 1221 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0001221.npy) |
| 1222 | `model.layers.11.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1223 | `model.layers.11.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1224 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0001224.npy) |
| 1225 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0001225.npy) |
| 1226 | `model.layers.11.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1227 | `model.layers.11.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 91.0 / 0.1032887856165568 / 2.9522145169196565 | [NPY](tensors/0001227.npy) |
| 1228 | `model.layers.11.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.5625 / 8.25 / 0.055311378557235 / 1.3254139165730858 | [NPY](tensors/0001228.npy) |
| 1229 | `model.layers.11.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 91.0 / 0.1032887856165568 / 2.9522145169196565 | [NPY](tensors/0001229.npy) |
| 1230 | `model.layers.11.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.0 / 37.75 / 0.13574747741222382 / 4.02712488247127 | [NPY](tensors/0001230.npy) |
| 1231 | `model.layers.11.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 91.0 / 0.1032887856165568 / 2.9522145169196565 | [NPY](tensors/0001231.npy) |
| 1232 | `model.layers.11.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.71875 / 9.5 / 0.01811826229095459 / 2.4425662356229845 | [NPY](tensors/0001232.npy) |
| 1233 | `model.layers.11.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.0625 / 7.5625 / -0.005499663995578885 / 1.4066620592783745 | [NPY](tensors/0001233.npy) |
| 1234 | `model.layers.11.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.375 / 61.25 / 0.09051183064778646 / 3.7868634615094554 | [NPY](tensors/0001234.npy) |
| 1235 | `model.layers.11.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.375 / 61.25 / 0.09051183064778646 / 3.7868634615094554 | [NPY](tensors/0001235.npy) |
| 1236 | `model.layers.11.self_attn` | 10 | `output[1]` | [1, 64, 1, 307] | torch.bfloat16 → float32 | 2.582964953035116e-10 / 0.9296875 / 0.0030476549144269997 / 0.014519967175640998 | [NPY](tensors/0001236.npy) |
| 1237 | `model.layers.11.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -228.0 / 390.0 / 0.8687984890407986 / 19.012440815550526 | [NPY](tensors/0001237.npy) |
| 1238 | `model.layers.11.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.203125 / 2.75 / 0.030664985709720188 / 0.7093088198255325 | [NPY](tensors/0001238.npy) |
| 1239 | `model.layers.11.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.203125 / 2.75 / 0.030664985709720188 / 0.7093088198255325 | [NPY](tensors/0001239.npy) |
| 1240 | `model.layers.11.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.203125 / 2.75 / 0.030664985709720188 / 0.7093088198255325 | [NPY](tensors/0001240.npy) |
| 1241 | `model.layers.11.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1242 | `model.layers.11.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1243 | `model.layers.11.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1244 | `model.layers.11.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -88.5 / 69.0 / -0.08625975184970432 / 4.315022154762759 | [NPY](tensors/0001244.npy) |
| 1245 | `model.layers.11.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 69.0 / -0.08625975184970432 / 4.315022154762759 | [NPY](tensors/0001245.npy) |
| 1246 | `model.layers.11.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.25 / 1.0625 / -0.033295631408691406 / 0.4601323756790714 | [NPY](tensors/0001246.npy) |
| 1247 | `model.layers.11` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -316.0 / 400.0 / 0.7829861111111112 / 20.714307664382865 | [NPY](tensors/0001247.npy) |
| 1326 | `model.layers.11` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -203.0 / 304.0 / 0.6473253038194444 / 15.411340292650596 | [NPY](tensors/0001326.npy) |
| 1327 | `model.layers.11` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 308] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001327.npy) |
| 1328 | `model.layers.11` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0001328.npy) |
| 1329 | `model.layers.11` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0001329.npy) |
| 1330 | `model.layers.11` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0001330.npy) |
| 1331 | `model.layers.11` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1332 | `model.layers.11` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1333 | `model.layers.11` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1334 | `model.layers.11.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -203.0 / 304.0 / 0.6473253038194444 / 15.411340292650596 | [NPY](tensors/0001334.npy) |
| 1335 | `model.layers.11.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 72.0 / 0.09829206466674804 / 2.791741173952692 | [NPY](tensors/0001335.npy) |
| 1336 | `model.layers.11.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 72.0 / 0.09829206466674804 / 2.791741173952692 | [NPY](tensors/0001336.npy) |
| 1337 | `model.layers.11.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 308] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001337.npy) |
| 1338 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0001338.npy) |
| 1339 | `model.layers.11.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1340 | `model.layers.11.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1341 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0001341.npy) |
| 1342 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0001342.npy) |
| 1343 | `model.layers.11.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1344 | `model.layers.11.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 72.0 / 0.09829206466674804 / 2.791741173952692 | [NPY](tensors/0001344.npy) |
| 1345 | `model.layers.11.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.78125 / 9.125 / 0.04110408558335621 / 1.2819179294967458 | [NPY](tensors/0001345.npy) |
| 1346 | `model.layers.11.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 72.0 / 0.09829206466674804 / 2.791741173952692 | [NPY](tensors/0001346.npy) |
| 1347 | `model.layers.11.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.0 / 38.5 / 0.10851471871137619 / 3.8950475401694855 | [NPY](tensors/0001347.npy) |
| 1348 | `model.layers.11.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 72.0 / 0.09829206466674804 / 2.791741173952692 | [NPY](tensors/0001348.npy) |
| 1349 | `model.layers.11.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.75 / 6.5 / 0.11793941259384155 / 2.0515773170740155 | [NPY](tensors/0001349.npy) |
| 1350 | `model.layers.11.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.21875 / 5.40625 / -0.007768050534650683 / 1.296266808646049 | [NPY](tensors/0001350.npy) |
| 1351 | `model.layers.11.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 103.0 / 0.06900982128249275 / 4.808917567063419 | [NPY](tensors/0001351.npy) |
| 1352 | `model.layers.11.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 103.0 / 0.06900982128249275 / 4.808917567063419 | [NPY](tensors/0001352.npy) |
| 1353 | `model.layers.11.self_attn` | 11 | `output[1]` | [1, 64, 1, 308] | torch.bfloat16 → float32 | 2.546585164964199e-09 / 0.84765625 / 0.002955999772317292 / 0.012621880637108524 | [NPY](tensors/0001353.npy) |
| 1354 | `model.layers.11.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -248.0 / 360.0 / 0.7168813069661458 / 18.02397037341264 | [NPY](tensors/0001354.npy) |
| 1355 | `model.layers.11.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.609375 / 2.9375 / 0.019516269365946453 / 0.7237047956644916 | [NPY](tensors/0001355.npy) |
| 1356 | `model.layers.11.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.609375 / 2.9375 / 0.019516269365946453 / 0.7237047956644916 | [NPY](tensors/0001356.npy) |
| 1357 | `model.layers.11.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.609375 / 2.9375 / 0.019516269365946453 / 0.7237047956644916 | [NPY](tensors/0001357.npy) |
| 1358 | `model.layers.11.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1359 | `model.layers.11.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1360 | `model.layers.11.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1361 | `model.layers.11.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -79.0 / 62.0 / 0.04800677299499512 / 4.792398920885393 | [NPY](tensors/0001361.npy) |
| 1362 | `model.layers.11.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -79.0 / 62.0 / 0.04800677299499512 / 4.792398920885393 | [NPY](tensors/0001362.npy) |
| 1363 | `model.layers.11.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.4609375 / 1.46875 / -0.030073165893554688 / 0.6150511374599537 | [NPY](tensors/0001363.npy) |
| 1364 | `model.layers.11` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -328.0 / 406.0 / 0.7652855767144098 / 20.453209240694196 | [NPY](tensors/0001364.npy) |
| 1443 | `model.layers.11` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -362.0 / 636.0 / 0.7559231228298611 / 23.01655745404146 | [NPY](tensors/0001443.npy) |
| 1444 | `model.layers.11` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 309] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001444.npy) |
| 1445 | `model.layers.11` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0001445.npy) |
| 1446 | `model.layers.11` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0001446.npy) |
| 1447 | `model.layers.11` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0001447.npy) |
| 1448 | `model.layers.11` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1449 | `model.layers.11` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1450 | `model.layers.11` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1451 | `model.layers.11.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -362.0 / 636.0 / 0.7559231228298611 / 23.01655745404146 | [NPY](tensors/0001451.npy) |
| 1452 | `model.layers.11.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 129.0 / 0.08873951435089111 / 3.4246978574681024 | [NPY](tensors/0001452.npy) |
| 1453 | `model.layers.11.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 129.0 / 0.08873951435089111 / 3.4246978574681024 | [NPY](tensors/0001453.npy) |
| 1454 | `model.layers.11.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 309] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001454.npy) |
| 1455 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0001455.npy) |
| 1456 | `model.layers.11.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1457 | `model.layers.11.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1458 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0001458.npy) |
| 1459 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0001459.npy) |
| 1460 | `model.layers.11.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1461 | `model.layers.11.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 129.0 / 0.08873951435089111 / 3.4246978574681024 | [NPY](tensors/0001461.npy) |
| 1462 | `model.layers.11.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.65625 / 7.90625 / 0.05596806528046727 / 1.237617298898219 | [NPY](tensors/0001462.npy) |
| 1463 | `model.layers.11.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 129.0 / 0.08873951435089111 / 3.4246978574681024 | [NPY](tensors/0001463.npy) |
| 1464 | `model.layers.11.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 43.75 / 0.06530734896659851 / 3.97440416430121 | [NPY](tensors/0001464.npy) |
| 1465 | `model.layers.11.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 129.0 / 0.08873951435089111 / 3.4246978574681024 | [NPY](tensors/0001465.npy) |
| 1466 | `model.layers.11.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.40625 / 7.03125 / 0.1535235522314906 / 2.2705319225177054 | [NPY](tensors/0001466.npy) |
| 1467 | `model.layers.11.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.4375 / 7.09375 / -0.010477186180651188 / 1.44965035612215 | [NPY](tensors/0001467.npy) |
| 1468 | `model.layers.11.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -96.0 / 107.5 / -0.01482441160413954 / 4.81455500287162 | [NPY](tensors/0001468.npy) |
| 1469 | `model.layers.11.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -96.0 / 107.5 / -0.01482441160413954 / 4.81455500287162 | [NPY](tensors/0001469.npy) |
| 1470 | `model.layers.11.self_attn` | 12 | `output[1]` | [1, 64, 1, 309] | torch.bfloat16 → float32 | 1.8047785488306545e-12 / 0.9609375 / 0.0029972171210100925 / 0.017268568321735355 | [NPY](tensors/0001470.npy) |
| 1471 | `model.layers.11.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -254.0 / 540.0 / 0.7408585442437066 / 22.23598124280516 | [NPY](tensors/0001471.npy) |
| 1472 | `model.layers.11.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.453125 / 3.015625 / 0.024133858415815564 / 0.7098011959437764 | [NPY](tensors/0001472.npy) |
| 1473 | `model.layers.11.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.453125 / 3.015625 / 0.024133858415815564 / 0.7098011959437764 | [NPY](tensors/0001473.npy) |
| 1474 | `model.layers.11.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.453125 / 3.015625 / 0.024133858415815564 / 0.7098011959437764 | [NPY](tensors/0001474.npy) |
| 1475 | `model.layers.11.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1476 | `model.layers.11.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1477 | `model.layers.11.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1478 | `model.layers.11.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -161.0 / 165.0 / -0.016223759121365016 / 6.892131756173358 | [NPY](tensors/0001478.npy) |
| 1479 | `model.layers.11.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -161.0 / 165.0 / -0.016223759121365016 / 6.892131756173358 | [NPY](tensors/0001479.npy) |
| 1480 | `model.layers.11.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.125 / 1.2265625 / -0.05147552490234375 / 0.5406448219687398 | [NPY](tensors/0001480.npy) |
| 1481 | `model.layers.11` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -416.0 / 672.0 / 0.7232891506618924 / 26.578339353070945 | [NPY](tensors/0001481.npy) |
| 1560 | `model.layers.11` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -266.0 / 506.0 / 0.8179879082573784 / 21.040911958701187 | [NPY](tensors/0001560.npy) |
| 1561 | `model.layers.11` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 310] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001561.npy) |
| 1562 | `model.layers.11` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0001562.npy) |
| 1563 | `model.layers.11` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0001563.npy) |
| 1564 | `model.layers.11` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0001564.npy) |
| 1565 | `model.layers.11` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1566 | `model.layers.11` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1567 | `model.layers.11` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1568 | `model.layers.11.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -266.0 / 506.0 / 0.8179879082573784 / 21.040911958701187 | [NPY](tensors/0001568.npy) |
| 1569 | `model.layers.11.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -66.5 / 112.5 / 0.10600971049732633 / 3.1766785301168063 | [NPY](tensors/0001569.npy) |
| 1570 | `model.layers.11.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -66.5 / 112.5 / 0.10600971049732633 / 3.1766785301168063 | [NPY](tensors/0001570.npy) |
| 1571 | `model.layers.11.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 310] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001571.npy) |
| 1572 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0001572.npy) |
| 1573 | `model.layers.11.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1574 | `model.layers.11.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1575 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0001575.npy) |
| 1576 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0001576.npy) |
| 1577 | `model.layers.11.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1578 | `model.layers.11.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -66.5 / 112.5 / 0.10600971049732633 / 3.1766785301168063 | [NPY](tensors/0001578.npy) |
| 1579 | `model.layers.11.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.4375 / 9.25 / 0.05880816886201501 / 1.3922742427814379 | [NPY](tensors/0001579.npy) |
| 1580 | `model.layers.11.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -66.5 / 112.5 / 0.10600971049732633 / 3.1766785301168063 | [NPY](tensors/0001580.npy) |
| 1581 | `model.layers.11.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.25 / 37.0 / 0.1996157169342041 / 3.9136519693773826 | [NPY](tensors/0001581.npy) |
| 1582 | `model.layers.11.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -66.5 / 112.5 / 0.10600971049732633 / 3.1766785301168063 | [NPY](tensors/0001582.npy) |
| 1583 | `model.layers.11.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.125 / 6.6875 / 0.12041562795639038 / 2.440763585561977 | [NPY](tensors/0001583.npy) |
| 1584 | `model.layers.11.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.34375 / 7.1875 / -0.014444339089095592 / 1.4621891710522499 | [NPY](tensors/0001584.npy) |
| 1585 | `model.layers.11.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 42.25 / 0.05902816984388563 / 3.9330014075541957 | [NPY](tensors/0001585.npy) |
| 1586 | `model.layers.11.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 42.25 / 0.05902816984388563 / 3.9330014075541957 | [NPY](tensors/0001586.npy) |
| 1587 | `model.layers.11.self_attn` | 13 | `output[1]` | [1, 64, 1, 310] | torch.bfloat16 → float32 | 3.808509063674137e-12 / 0.95703125 / 0.002930930269790896 / 0.016267154938493608 | [NPY](tensors/0001587.npy) |
| 1588 | `model.layers.11.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -224.0 / 474.0 / 0.8767317030164931 / 21.55999708341906 | [NPY](tensors/0001588.npy) |
| 1589 | `model.layers.11.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.9375 / 3.421875 / 0.024999426470862493 / 0.7183452805495227 | [NPY](tensors/0001589.npy) |
| 1590 | `model.layers.11.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.9375 / 3.421875 / 0.024999426470862493 / 0.7183452805495227 | [NPY](tensors/0001590.npy) |
| 1591 | `model.layers.11.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.9375 / 3.421875 / 0.024999426470862493 / 0.7183452805495227 | [NPY](tensors/0001591.npy) |
| 1592 | `model.layers.11.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1593 | `model.layers.11.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1594 | `model.layers.11.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1595 | `model.layers.11.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -210.0 / 151.0 / -0.036774401201142205 / 6.391498721514552 | [NPY](tensors/0001595.npy) |
| 1596 | `model.layers.11.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -210.0 / 151.0 / -0.036774401201142205 / 6.391498721514552 | [NPY](tensors/0001596.npy) |
| 1597 | `model.layers.11.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.6796875 / 0.9453125 / -0.02776336669921875 / 0.40983746939920856 | [NPY](tensors/0001597.npy) |
| 1598 | `model.layers.11` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -434.0 / 540.0 / 0.8406368679470486 / 24.71799033842312 | [NPY](tensors/0001598.npy) |
| 1677 | `model.layers.11` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -248.0 / 376.0 / 1.0627795749240452 / 18.358952765244418 | [NPY](tensors/0001677.npy) |
| 1678 | `model.layers.11` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 311] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001678.npy) |
| 1679 | `model.layers.11` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0001679.npy) |
| 1680 | `model.layers.11` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0001680.npy) |
| 1681 | `model.layers.11` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0001681.npy) |
| 1682 | `model.layers.11` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1683 | `model.layers.11` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1684 | `model.layers.11` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1685 | `model.layers.11.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -248.0 / 376.0 / 1.0627795749240452 / 18.358952765244418 | [NPY](tensors/0001685.npy) |
| 1686 | `model.layers.11.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -71.0 / 90.5 / 0.1285353382428487 / 3.018945674687429 | [NPY](tensors/0001686.npy) |
| 1687 | `model.layers.11.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -71.0 / 90.5 / 0.1285353382428487 / 3.018945674687429 | [NPY](tensors/0001687.npy) |
| 1688 | `model.layers.11.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 311] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001688.npy) |
| 1689 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0001689.npy) |
| 1690 | `model.layers.11.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1691 | `model.layers.11.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1692 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0001692.npy) |
| 1693 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0001693.npy) |
| 1694 | `model.layers.11.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1695 | `model.layers.11.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -71.0 / 90.5 / 0.1285353382428487 / 3.018945674687429 | [NPY](tensors/0001695.npy) |
| 1696 | `model.layers.11.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.3125 / 8.6875 / 0.03498257463797927 / 1.383806103014137 | [NPY](tensors/0001696.npy) |
| 1697 | `model.layers.11.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -71.0 / 90.5 / 0.1285353382428487 / 3.018945674687429 | [NPY](tensors/0001697.npy) |
| 1698 | `model.layers.11.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.25 / 39.0 / 0.16011661291122437 / 4.164402417260769 | [NPY](tensors/0001698.npy) |
| 1699 | `model.layers.11.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -71.0 / 90.5 / 0.1285353382428487 / 3.018945674687429 | [NPY](tensors/0001699.npy) |
| 1700 | `model.layers.11.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.59375 / 7.8125 / 0.05973103642463684 / 2.4923618479994616 | [NPY](tensors/0001700.npy) |
| 1701 | `model.layers.11.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.3125 / 7.28125 / -0.01671885442920029 / 1.4300741738828662 | [NPY](tensors/0001701.npy) |
| 1702 | `model.layers.11.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.625 / 48.0 / 0.019776671793725754 / 4.008119551049013 | [NPY](tensors/0001702.npy) |
| 1703 | `model.layers.11.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.625 / 48.0 / 0.019776671793725754 / 4.008119551049013 | [NPY](tensors/0001703.npy) |
| 1704 | `model.layers.11.self_attn` | 14 | `output[1]` | [1, 64, 1, 311] | torch.bfloat16 → float32 | 3.2514435588382185e-11 / 0.8125 / 0.002974757378362399 / 0.014111145366282869 | [NPY](tensors/0001704.npy) |
| 1705 | `model.layers.11.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -258.0 / 404.0 / 1.082389153374566 / 20.09102228077993 | [NPY](tensors/0001705.npy) |
| 1706 | `model.layers.11.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.703125 / 2.84375 / 0.03690878947575887 / 0.7197070319272787 | [NPY](tensors/0001706.npy) |
| 1707 | `model.layers.11.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.703125 / 2.84375 / 0.03690878947575887 / 0.7197070319272787 | [NPY](tensors/0001707.npy) |
| 1708 | `model.layers.11.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.703125 / 2.84375 / 0.03690878947575887 / 0.7197070319272787 | [NPY](tensors/0001708.npy) |
| 1709 | `model.layers.11.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1710 | `model.layers.11.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1711 | `model.layers.11.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1712 | `model.layers.11.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -71.0 / 60.75 / 0.0746924983130561 / 5.430383179300353 | [NPY](tensors/0001712.npy) |
| 1713 | `model.layers.11.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -71.0 / 60.75 / 0.0746924983130561 / 5.430383179300353 | [NPY](tensors/0001713.npy) |
| 1714 | `model.layers.11.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.28125 / -0.021183013916015625 / 0.5005871121444262 | [NPY](tensors/0001714.npy) |
| 1715 | `model.layers.11` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -328.0 / 454.0 / 1.1557942708333333 / 22.51080326891631 | [NPY](tensors/0001715.npy) |
| 1794 | `model.layers.11` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -324.0 / 386.0 / 1.0396330091688368 / 21.072812287526812 | [NPY](tensors/0001794.npy) |
| 1795 | `model.layers.11` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 312] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001795.npy) |
| 1796 | `model.layers.11` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0001796.npy) |
| 1797 | `model.layers.11` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0001797.npy) |
| 1798 | `model.layers.11` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0001798.npy) |
| 1799 | `model.layers.11` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1800 | `model.layers.11` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1801 | `model.layers.11` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1802 | `model.layers.11.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -324.0 / 386.0 / 1.0396330091688368 / 21.072812287526812 | [NPY](tensors/0001802.npy) |
| 1803 | `model.layers.11.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.5 / 86.0 / 0.10538353555732304 / 2.862351941157181 | [NPY](tensors/0001803.npy) |
| 1804 | `model.layers.11.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.5 / 86.0 / 0.10538353555732304 / 2.862351941157181 | [NPY](tensors/0001804.npy) |
| 1805 | `model.layers.11.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 312] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001805.npy) |
| 1806 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0001806.npy) |
| 1807 | `model.layers.11.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1808 | `model.layers.11.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1809 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0001809.npy) |
| 1810 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0001810.npy) |
| 1811 | `model.layers.11.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1812 | `model.layers.11.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.5 / 86.0 / 0.10538353555732304 / 2.862351941157181 | [NPY](tensors/0001812.npy) |
| 1813 | `model.layers.11.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.625 / 10.4375 / 0.04051035828888416 / 1.3480668653409986 | [NPY](tensors/0001813.npy) |
| 1814 | `model.layers.11.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.5 / 86.0 / 0.10538353555732304 / 2.862351941157181 | [NPY](tensors/0001814.npy) |
| 1815 | `model.layers.11.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -37.75 / 39.75 / 0.06129056215286255 / 4.06532913620675 | [NPY](tensors/0001815.npy) |
| 1816 | `model.layers.11.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.5 / 86.0 / 0.10538353555732304 / 2.862351941157181 | [NPY](tensors/0001816.npy) |
| 1817 | `model.layers.11.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.0625 / 7.59375 / 0.006667494773864746 / 2.327780658043428 | [NPY](tensors/0001817.npy) |
| 1818 | `model.layers.11.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.90625 / 7.1875 / -0.011858864221721888 / 1.3420639598368176 | [NPY](tensors/0001818.npy) |
| 1819 | `model.layers.11.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.625 / 53.75 / 0.015571930673387316 / 3.219794910660137 | [NPY](tensors/0001819.npy) |
| 1820 | `model.layers.11.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.625 / 53.75 / 0.015571930673387316 / 3.219794910660137 | [NPY](tensors/0001820.npy) |
| 1821 | `model.layers.11.self_attn` | 15 | `output[1]` | [1, 64, 1, 312] | torch.bfloat16 → float32 | 2.2282620193436742e-10 / 0.796875 / 0.002633634929274501 / 0.012068510112633882 | [NPY](tensors/0001821.npy) |
| 1822 | `model.layers.11.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -282.0 / 420.0 / 1.0554151746961806 / 22.03216422357466 | [NPY](tensors/0001822.npy) |
| 1823 | `model.layers.11.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.265625 / 4.75 / 0.02379788557688395 / 0.7339731332638462 | [NPY](tensors/0001823.npy) |
| 1824 | `model.layers.11.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.265625 / 4.75 / 0.02379788557688395 / 0.7339731332638462 | [NPY](tensors/0001824.npy) |
| 1825 | `model.layers.11.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.265625 / 4.75 / 0.02379788557688395 / 0.7339731332638462 | [NPY](tensors/0001825.npy) |
| 1826 | `model.layers.11.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1827 | `model.layers.11.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1828 | `model.layers.11.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1829 | `model.layers.11.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -95.5 / 82.5 / 0.056016466352674696 / 5.281840958897639 | [NPY](tensors/0001829.npy) |
| 1830 | `model.layers.11.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.5 / 82.5 / 0.056016466352674696 / 5.281840958897639 | [NPY](tensors/0001830.npy) |
| 1831 | `model.layers.11.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.625 / 1.421875 / -0.11946868896484375 / 0.648363182707838 | [NPY](tensors/0001831.npy) |
| 1832 | `model.layers.11` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -378.0 / 502.0 / 1.11194093492296 / 24.918087407219335 | [NPY](tensors/0001832.npy) |
| 1911 | `model.layers.11` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -372.0 / 496.0 / 0.8415941026475694 / 24.377724337999567 | [NPY](tensors/0001911.npy) |
| 1912 | `model.layers.11` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 313] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001912.npy) |
| 1913 | `model.layers.11` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0001913.npy) |
| 1914 | `model.layers.11` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0001914.npy) |
| 1915 | `model.layers.11` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0001915.npy) |
| 1916 | `model.layers.11` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1917 | `model.layers.11` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1918 | `model.layers.11` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1919 | `model.layers.11.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -372.0 / 496.0 / 0.8415941026475694 / 24.377724337999567 | [NPY](tensors/0001919.npy) |
| 1920 | `model.layers.11.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 95.5 / 0.07976792918311225 / 2.950768182255753 | [NPY](tensors/0001920.npy) |
| 1921 | `model.layers.11.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 95.5 / 0.07976792918311225 / 2.950768182255753 | [NPY](tensors/0001921.npy) |
| 1922 | `model.layers.11.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 313] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001922.npy) |
| 1923 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0001923.npy) |
| 1924 | `model.layers.11.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1925 | `model.layers.11.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1926 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0001926.npy) |
| 1927 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0001927.npy) |
| 1928 | `model.layers.11.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1929 | `model.layers.11.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 95.5 / 0.07976792918311225 / 2.950768182255753 | [NPY](tensors/0001929.npy) |
| 1930 | `model.layers.11.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 10.1875 / 0.019161705626174808 / 1.3512854641635554 | [NPY](tensors/0001930.npy) |
| 1931 | `model.layers.11.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 95.5 / 0.07976792918311225 / 2.950768182255753 | [NPY](tensors/0001931.npy) |
| 1932 | `model.layers.11.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.75 / 37.5 / 0.009696350432932377 / 3.8248005490223473 | [NPY](tensors/0001932.npy) |
| 1933 | `model.layers.11.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 95.5 / 0.07976792918311225 / 2.950768182255753 | [NPY](tensors/0001933.npy) |
| 1934 | `model.layers.11.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.84375 / 8.1875 / 0.028214097023010254 / 2.376563747820883 | [NPY](tensors/0001934.npy) |
| 1935 | `model.layers.11.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5625 / 6.6875 / -0.019241358269937336 / 1.4353889267153226 | [NPY](tensors/0001935.npy) |
| 1936 | `model.layers.11.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.5 / 84.0 / 0.01704919636249542 / 3.6922607303974715 | [NPY](tensors/0001936.npy) |
| 1937 | `model.layers.11.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.5 / 84.0 / 0.01704919636249542 / 3.6922607303974715 | [NPY](tensors/0001937.npy) |
| 1938 | `model.layers.11.self_attn` | 16 | `output[1]` | [1, 64, 1, 313] | torch.bfloat16 → float32 | 8.594724931754172e-11 / 0.8828125 / 0.0026118423725215653 / 0.017424141425790907 | [NPY](tensors/0001938.npy) |
| 1939 | `model.layers.11.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -288.0 / 460.0 / 0.8587310367160373 / 24.573280463539543 | [NPY](tensors/0001939.npy) |
| 1940 | `model.layers.11.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.890625 / 3.984375 / 0.011045341855949825 / 0.740424331028921 | [NPY](tensors/0001940.npy) |
| 1941 | `model.layers.11.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.890625 / 3.984375 / 0.011045341855949825 / 0.740424331028921 | [NPY](tensors/0001941.npy) |
| 1942 | `model.layers.11.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.890625 / 3.984375 / 0.011045341855949825 / 0.740424331028921 | [NPY](tensors/0001942.npy) |
| 1943 | `model.layers.11.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1944 | `model.layers.11.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1945 | `model.layers.11.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1946 | `model.layers.11.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -169.0 / 165.0 / 0.044494295285807714 / 7.347889575942175 | [NPY](tensors/0001946.npy) |
| 1947 | `model.layers.11.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -169.0 / 165.0 / 0.044494295285807714 / 7.347889575942175 | [NPY](tensors/0001947.npy) |
| 1948 | `model.layers.11.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.09375 / 1.609375 / -0.16260337829589844 / 0.6688077235835478 | [NPY](tensors/0001948.npy) |
| 1949 | `model.layers.11` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -456.0 / 624.0 / 0.9034310234917535 / 29.050277901690983 | [NPY](tensors/0001949.npy) |
| 2028 | `model.layers.11` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -376.0 / 608.0 / 0.9678392198350695 / 26.935373833740815 | [NPY](tensors/0002028.npy) |
| 2029 | `model.layers.11` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 314] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002029.npy) |
| 2030 | `model.layers.11` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0002030.npy) |
| 2031 | `model.layers.11` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0002031.npy) |
| 2032 | `model.layers.11` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0002032.npy) |
| 2033 | `model.layers.11` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2034 | `model.layers.11` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2035 | `model.layers.11` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2036 | `model.layers.11.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -376.0 / 608.0 / 0.9678392198350695 / 26.935373833740815 | [NPY](tensors/0002036.npy) |
| 2037 | `model.layers.11.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 105.5 / 0.08621105088127984 / 2.9941482268624013 | [NPY](tensors/0002037.npy) |
| 2038 | `model.layers.11.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 105.5 / 0.08621105088127984 / 2.9941482268624013 | [NPY](tensors/0002038.npy) |
| 2039 | `model.layers.11.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 314] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002039.npy) |
| 2040 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0002040.npy) |
| 2041 | `model.layers.11.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2042 | `model.layers.11.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2043 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0002043.npy) |
| 2044 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0002044.npy) |
| 2045 | `model.layers.11.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2046 | `model.layers.11.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 105.5 / 0.08621105088127984 / 2.9941482268624013 | [NPY](tensors/0002046.npy) |
| 2047 | `model.layers.11.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.8125 / 10.0625 / 0.0189578456338495 / 1.3535190276611768 | [NPY](tensors/0002047.npy) |
| 2048 | `model.layers.11.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 105.5 / 0.08621105088127984 / 2.9941482268624013 | [NPY](tensors/0002048.npy) |
| 2049 | `model.layers.11.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.125 / 35.5 / 0.029683977365493774 / 3.565391391331186 | [NPY](tensors/0002049.npy) |
| 2050 | `model.layers.11.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.0 / 105.5 / 0.08621105088127984 / 2.9941482268624013 | [NPY](tensors/0002050.npy) |
| 2051 | `model.layers.11.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.46875 / 9.5 / -0.09617282636463642 / 2.7229514384363918 | [NPY](tensors/0002051.npy) |
| 2052 | `model.layers.11.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 8.375 / -0.028420927934348583 / 1.580428339917747 | [NPY](tensors/0002052.npy) |
| 2053 | `model.layers.11.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.25 / 84.0 / 0.05416700575086805 / 4.618557081157812 | [NPY](tensors/0002053.npy) |
| 2054 | `model.layers.11.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.25 / 84.0 / 0.05416700575086805 / 4.618557081157812 | [NPY](tensors/0002054.npy) |
| 2055 | `model.layers.11.self_attn` | 17 | `output[1]` | [1, 64, 1, 314] | torch.bfloat16 → float32 | 3.4378899727016687e-10 / 0.7734375 / 0.0028923959248014714 / 0.014937688213420673 | [NPY](tensors/0002055.npy) |
| 2056 | `model.layers.11.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -388.0 / 616.0 / 1.020895046657986 / 28.391402651551175 | [NPY](tensors/0002056.npy) |
| 2057 | `model.layers.11.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.796875 / 3.734375 / 0.02037820683585273 / 0.7392891895590902 | [NPY](tensors/0002057.npy) |
| 2058 | `model.layers.11.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.796875 / 3.734375 / 0.02037820683585273 / 0.7392891895590902 | [NPY](tensors/0002058.npy) |
| 2059 | `model.layers.11.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.796875 / 3.734375 / 0.02037820683585273 / 0.7392891895590902 | [NPY](tensors/0002059.npy) |
| 2060 | `model.layers.11.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2061 | `model.layers.11.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2062 | `model.layers.11.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2063 | `model.layers.11.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -48.0 / 144.0 / 0.21422353055742052 / 6.43061478594584 | [NPY](tensors/0002063.npy) |
| 2064 | `model.layers.11.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 144.0 / 0.21422353055742052 / 6.43061478594584 | [NPY](tensors/0002064.npy) |
| 2065 | `model.layers.11.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.96875 / 0.9453125 / -0.1259307861328125 / 0.5457857743751314 | [NPY](tensors/0002065.npy) |
| 2066 | `model.layers.11` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -436.0 / 760.0 / 1.2344160291883681 / 32.2557681295191 | [NPY](tensors/0002066.npy) |
| 2145 | `model.layers.11` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -160.0 / 298.0 / 0.9486329820421007 / 16.249879772310564 | [NPY](tensors/0002145.npy) |
| 2146 | `model.layers.11` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 315] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002146.npy) |
| 2147 | `model.layers.11` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0002147.npy) |
| 2148 | `model.layers.11` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0002148.npy) |
| 2149 | `model.layers.11` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0002149.npy) |
| 2150 | `model.layers.11` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2151 | `model.layers.11` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2152 | `model.layers.11` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2153 | `model.layers.11.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -160.0 / 298.0 / 0.9486329820421007 / 16.249879772310564 | [NPY](tensors/0002153.npy) |
| 2154 | `model.layers.11.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 86.0 / 0.1256078799565633 / 2.7351591472524164 | [NPY](tensors/0002154.npy) |
| 2155 | `model.layers.11.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 86.0 / 0.1256078799565633 / 2.7351591472524164 | [NPY](tensors/0002155.npy) |
| 2156 | `model.layers.11.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 315] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002156.npy) |
| 2157 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0002157.npy) |
| 2158 | `model.layers.11.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2159 | `model.layers.11.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2160 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0002160.npy) |
| 2161 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0002161.npy) |
| 2162 | `model.layers.11.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2163 | `model.layers.11.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 86.0 / 0.1256078799565633 / 2.7351591472524164 | [NPY](tensors/0002163.npy) |
| 2164 | `model.layers.11.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.71875 / 11.9375 / 0.03150764509337023 / 1.4450537814975153 | [NPY](tensors/0002164.npy) |
| 2165 | `model.layers.11.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 86.0 / 0.1256078799565633 / 2.7351591472524164 | [NPY](tensors/0002165.npy) |
| 2166 | `model.layers.11.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 38.75 / 0.09439823031425476 / 4.2654446450977135 | [NPY](tensors/0002166.npy) |
| 2167 | `model.layers.11.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 86.0 / 0.1256078799565633 / 2.7351591472524164 | [NPY](tensors/0002167.npy) |
| 2168 | `model.layers.11.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.4375 / 10.5 / 0.055192410945892334 / 2.5859723940554935 | [NPY](tensors/0002168.npy) |
| 2169 | `model.layers.11.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.21875 / 7.71875 / -0.01839250884950161 / 1.4212203709863769 | [NPY](tensors/0002169.npy) |
| 2170 | `model.layers.11.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 116.5 / 0.1280085245768229 / 4.586676650774601 | [NPY](tensors/0002170.npy) |
| 2171 | `model.layers.11.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 116.5 / 0.1280085245768229 / 4.586676650774601 | [NPY](tensors/0002171.npy) |
| 2172 | `model.layers.11.self_attn` | 18 | `output[1]` | [1, 64, 1, 315] | torch.bfloat16 → float32 | 2.2737367544323206e-10 / 0.82421875 / 0.0027145798419703337 / 0.013927766258454285 | [NPY](tensors/0002172.npy) |
| 2173 | `model.layers.11.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -208.0 / 414.0 / 1.0773765563964843 / 18.805224623041276 | [NPY](tensors/0002173.npy) |
| 2174 | `model.layers.11.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.46875 / 3.796875 / 0.0343035724427965 / 0.7076580232142038 | [NPY](tensors/0002174.npy) |
| 2175 | `model.layers.11.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.46875 / 3.796875 / 0.0343035724427965 / 0.7076580232142038 | [NPY](tensors/0002175.npy) |
| 2176 | `model.layers.11.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.46875 / 3.796875 / 0.0343035724427965 / 0.7076580232142038 | [NPY](tensors/0002176.npy) |
| 2177 | `model.layers.11.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2178 | `model.layers.11.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2179 | `model.layers.11.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2180 | `model.layers.11.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -41.0 / 17.25 / 0.049842548370361325 / 3.9172416641747687 | [NPY](tensors/0002180.npy) |
| 2181 | `model.layers.11.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 17.25 / 0.049842548370361325 / 3.9172416641747687 | [NPY](tensors/0002181.npy) |
| 2182 | `model.layers.11.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3671875 / 1.6171875 / -0.0735931396484375 / 0.6284579964170446 | [NPY](tensors/0002182.npy) |
| 2183 | `model.layers.11` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -249.0 / 376.0 / 1.127852037217882 / 19.645334772325025 | [NPY](tensors/0002183.npy) |
| 2262 | `model.layers.11` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -426.0 / 600.0 / 0.8196004231770834 / 25.755964344133428 | [NPY](tensors/0002262.npy) |
| 2263 | `model.layers.11` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 316] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002263.npy) |
| 2264 | `model.layers.11` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0002264.npy) |
| 2265 | `model.layers.11` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0002265.npy) |
| 2266 | `model.layers.11` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0002266.npy) |
| 2267 | `model.layers.11` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2268 | `model.layers.11` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2269 | `model.layers.11` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2270 | `model.layers.11.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -426.0 / 600.0 / 0.8196004231770834 / 25.755964344133428 | [NPY](tensors/0002270.npy) |
| 2271 | `model.layers.11.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 109.0 / 0.06976396441459656 / 3.1044700603004083 | [NPY](tensors/0002271.npy) |
| 2272 | `model.layers.11.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 109.0 / 0.06976396441459656 / 3.1044700603004083 | [NPY](tensors/0002272.npy) |
| 2273 | `model.layers.11.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 316] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002273.npy) |
| 2274 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0002274.npy) |
| 2275 | `model.layers.11.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2276 | `model.layers.11.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2277 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0002277.npy) |
| 2278 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0002278.npy) |
| 2279 | `model.layers.11.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2280 | `model.layers.11.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 109.0 / 0.06976396441459656 / 3.1044700603004083 | [NPY](tensors/0002280.npy) |
| 2281 | `model.layers.11.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 9.25 / -1.3196375221014023e-05 / 1.320116735839495 | [NPY](tensors/0002281.npy) |
| 2282 | `model.layers.11.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 109.0 / 0.06976396441459656 / 3.1044700603004083 | [NPY](tensors/0002282.npy) |
| 2283 | `model.layers.11.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.5 / 28.75 / -0.04119408130645752 / 3.4363755199747206 | [NPY](tensors/0002283.npy) |
| 2284 | `model.layers.11.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.0 / 109.0 / 0.06976396441459656 / 3.1044700603004083 | [NPY](tensors/0002284.npy) |
| 2285 | `model.layers.11.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.8125 / 9.0625 / 0.01399010419845581 / 2.7875514529999568 | [NPY](tensors/0002285.npy) |
| 2286 | `model.layers.11.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.6875 / 8.0625 / -0.008884008741006255 / 1.4991697772696315 | [NPY](tensors/0002286.npy) |
| 2287 | `model.layers.11.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 53.5 / -0.0893870857026842 / 4.240713377906501 | [NPY](tensors/0002287.npy) |
| 2288 | `model.layers.11.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 53.5 / -0.0893870857026842 / 4.240713377906501 | [NPY](tensors/0002288.npy) |
| 2289 | `model.layers.11.self_attn` | 19 | `output[1]` | [1, 64, 1, 316] | torch.bfloat16 → float32 | 9.595169103704393e-11 / 0.9296875 / 0.0026001662378012575 / 0.016776816978676983 | [NPY](tensors/0002289.npy) |
| 2290 | `model.layers.11.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -372.0 / 502.0 / 0.7295239766438802 / 25.42862120026854 | [NPY](tensors/0002290.npy) |
| 2291 | `model.layers.11.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.265625 / 3.609375 / 0.010965232054392498 / 0.7743573697013725 | [NPY](tensors/0002291.npy) |
| 2292 | `model.layers.11.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.265625 / 3.609375 / 0.010965232054392498 / 0.7743573697013725 | [NPY](tensors/0002292.npy) |
| 2293 | `model.layers.11.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.265625 / 3.609375 / 0.010965232054392498 / 0.7743573697013725 | [NPY](tensors/0002293.npy) |
| 2294 | `model.layers.11.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2295 | `model.layers.11.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2296 | `model.layers.11.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2297 | `model.layers.11.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -278.0 / 264.0 / 0.17201798492007786 / 9.913433590546653 | [NPY](tensors/0002297.npy) |
| 2298 | `model.layers.11.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -278.0 / 264.0 / 0.17201798492007786 / 9.913433590546653 | [NPY](tensors/0002298.npy) |
| 2299 | `model.layers.11.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.078125 / 1.28125 / -0.1129913330078125 / 0.6762020130743646 | [NPY](tensors/0002299.npy) |
| 2300 | `model.layers.11` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -648.0 / 768.0 / 0.9027018229166667 / 32.36651341562922 | [NPY](tensors/0002300.npy) |
| 2379 | `model.layers.11` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -412.0 / 516.0 / 0.502780999077691 / 23.872031352210072 | [NPY](tensors/0002379.npy) |
| 2380 | `model.layers.11` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 317] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002380.npy) |
| 2381 | `model.layers.11` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0002381.npy) |
| 2382 | `model.layers.11` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0002382.npy) |
| 2383 | `model.layers.11` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0002383.npy) |
| 2384 | `model.layers.11` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2385 | `model.layers.11` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2386 | `model.layers.11` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2387 | `model.layers.11.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -412.0 / 516.0 / 0.502780999077691 / 23.872031352210072 | [NPY](tensors/0002387.npy) |
| 2388 | `model.layers.11.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 101.5 / 0.05703057050704956 / 3.0604190506455144 | [NPY](tensors/0002388.npy) |
| 2389 | `model.layers.11.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 101.5 / 0.05703057050704956 / 3.0604190506455144 | [NPY](tensors/0002389.npy) |
| 2390 | `model.layers.11.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 317] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002390.npy) |
| 2391 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0002391.npy) |
| 2392 | `model.layers.11.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2393 | `model.layers.11.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2394 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0002394.npy) |
| 2395 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0002395.npy) |
| 2396 | `model.layers.11.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2397 | `model.layers.11.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 101.5 / 0.05703057050704956 / 3.0604190506455144 | [NPY](tensors/0002397.npy) |
| 2398 | `model.layers.11.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.90625 / 10.25 / 0.01238045294303447 / 1.269721660987443 | [NPY](tensors/0002398.npy) |
| 2399 | `model.layers.11.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 101.5 / 0.05703057050704956 / 3.0604190506455144 | [NPY](tensors/0002399.npy) |
| 2400 | `model.layers.11.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.25 / 30.75 / 0.06147444248199463 / 3.378290390901053 | [NPY](tensors/0002400.npy) |
| 2401 | `model.layers.11.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 101.5 / 0.05703057050704956 / 3.0604190506455144 | [NPY](tensors/0002401.npy) |
| 2402 | `model.layers.11.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.375 / 8.25 / -0.011333882808685303 / 2.2035027477137117 | [NPY](tensors/0002402.npy) |
| 2403 | `model.layers.11.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.71875 / 8.25 / -0.019563493318855762 / 1.362306984940113 | [NPY](tensors/0002403.npy) |
| 2404 | `model.layers.11.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 61.0 / 0.005047028594546848 / 3.715290366139589 | [NPY](tensors/0002404.npy) |
| 2405 | `model.layers.11.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 61.0 / 0.005047028594546848 / 3.715290366139589 | [NPY](tensors/0002405.npy) |
| 2406 | `model.layers.11.self_attn` | 20 | `output[1]` | [1, 64, 1, 317] | torch.bfloat16 → float32 | 3.292370820418e-10 / 0.91796875 / 0.0025155514938419595 / 0.015209463408836573 | [NPY](tensors/0002406.npy) |
| 2407 | `model.layers.11.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -352.0 / 440.0 / 0.5064180162217882 / 23.65806580725576 | [NPY](tensors/0002407.npy) |
| 2408 | `model.layers.11.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.9375 / 4.40625 / 0.004972828759087456 / 0.753907563217212 | [NPY](tensors/0002408.npy) |
| 2409 | `model.layers.11.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.9375 / 4.40625 / 0.004972828759087456 / 0.753907563217212 | [NPY](tensors/0002409.npy) |
| 2410 | `model.layers.11.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.9375 / 4.40625 / 0.004972828759087456 / 0.753907563217212 | [NPY](tensors/0002410.npy) |
| 2411 | `model.layers.11.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2412 | `model.layers.11.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2413 | `model.layers.11.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2414 | `model.layers.11.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -101.0 / 127.5 / 0.054383108350965714 / 5.887526833690559 | [NPY](tensors/0002414.npy) |
| 2415 | `model.layers.11.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.0 / 127.5 / 0.054383108350965714 / 5.887526833690559 | [NPY](tensors/0002415.npy) |
| 2416 | `model.layers.11.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3828125 / 1.2421875 / -0.06954193115234375 / 0.5715515352439402 | [NPY](tensors/0002416.npy) |
| 2417 | `model.layers.11` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -452.0 / 556.0 / 0.5613101535373264 / 27.081444706463895 | [NPY](tensors/0002417.npy) |
| 2496 | `model.layers.11` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -482.0 / 680.0 / 0.2596554226345486 / 27.181478197336666 | [NPY](tensors/0002496.npy) |
| 2497 | `model.layers.11` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 318] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002497.npy) |
| 2498 | `model.layers.11` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0002498.npy) |
| 2499 | `model.layers.11` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0002499.npy) |
| 2500 | `model.layers.11` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0002500.npy) |
| 2501 | `model.layers.11` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2502 | `model.layers.11` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2503 | `model.layers.11` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2504 | `model.layers.11.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -482.0 / 680.0 / 0.2596554226345486 / 27.181478197336666 | [NPY](tensors/0002504.npy) |
| 2505 | `model.layers.11.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 117.5 / 0.040613896316952176 / 3.2219516226688345 | [NPY](tensors/0002505.npy) |
| 2506 | `model.layers.11.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 117.5 / 0.040613896316952176 / 3.2219516226688345 | [NPY](tensors/0002506.npy) |
| 2507 | `model.layers.11.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 318] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002507.npy) |
| 2508 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0002508.npy) |
| 2509 | `model.layers.11.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2510 | `model.layers.11.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2511 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0002511.npy) |
| 2512 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0002512.npy) |
| 2513 | `model.layers.11.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2514 | `model.layers.11.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 117.5 / 0.040613896316952176 / 3.2219516226688345 | [NPY](tensors/0002514.npy) |
| 2515 | `model.layers.11.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.46875 / 9.0 / 0.0006300704553723335 / 1.3006976853291843 | [NPY](tensors/0002515.npy) |
| 2516 | `model.layers.11.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 117.5 / 0.040613896316952176 / 3.2219516226688345 | [NPY](tensors/0002516.npy) |
| 2517 | `model.layers.11.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.875 / 30.75 / 0.010941088199615479 / 3.327223732768207 | [NPY](tensors/0002517.npy) |
| 2518 | `model.layers.11.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 117.5 / 0.040613896316952176 / 3.2219516226688345 | [NPY](tensors/0002518.npy) |
| 2519 | `model.layers.11.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.59375 / 8.375 / 0.03339183330535889 / 2.3896600209518235 | [NPY](tensors/0002519.npy) |
| 2520 | `model.layers.11.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.375 / 8.3125 / -0.018734400160610676 / 1.4762759976925708 | [NPY](tensors/0002520.npy) |
| 2521 | `model.layers.11.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -220.0 / 176.0 / -0.05137871901194255 / 6.40166215569696 | [NPY](tensors/0002521.npy) |
| 2522 | `model.layers.11.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -220.0 / 176.0 / -0.05137871901194255 / 6.40166215569696 | [NPY](tensors/0002522.npy) |
| 2523 | `model.layers.11.self_attn` | 21 | `output[1]` | [1, 64, 1, 318] | torch.bfloat16 → float32 | 1.659827830735594e-11 / 0.95703125 / 0.0022766344521491593 / 0.020405978752452196 | [NPY](tensors/0002523.npy) |
| 2524 | `model.layers.11.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -306.0 / 460.0 / 0.2067840576171875 / 24.434926409385113 | [NPY](tensors/0002524.npy) |
| 2525 | `model.layers.11.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.4375 / 4.1875 / -0.007478868961334229 / 0.8154171561739892 | [NPY](tensors/0002525.npy) |
| 2526 | `model.layers.11.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.4375 / 4.1875 / -0.007478868961334229 / 0.8154171561739892 | [NPY](tensors/0002526.npy) |
| 2527 | `model.layers.11.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.4375 / 4.1875 / -0.007478868961334229 / 0.8154171561739892 | [NPY](tensors/0002527.npy) |
| 2528 | `model.layers.11.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2529 | `model.layers.11.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2530 | `model.layers.11.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2531 | `model.layers.11.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -290.0 / 198.0 / 0.12026710444026523 / 9.074952216359621 | [NPY](tensors/0002531.npy) |
| 2532 | `model.layers.11.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -290.0 / 198.0 / 0.12026710444026523 / 9.074952216359621 | [NPY](tensors/0002532.npy) |
| 2533 | `model.layers.11.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.140625 / 1.59375 / -0.1992340087890625 / 0.7987085661862483 | [NPY](tensors/0002533.npy) |
| 2534 | `model.layers.11` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -596.0 / 656.0 / 0.3263497246636285 / 29.980483030934913 | [NPY](tensors/0002534.npy) |
| 2613 | `model.layers.11` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -412.0 / 556.0 / 0.3621307373046875 / 23.448591075416562 | [NPY](tensors/0002613.npy) |
| 2614 | `model.layers.11` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 319] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002614.npy) |
| 2615 | `model.layers.11` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0002615.npy) |
| 2616 | `model.layers.11` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0002616.npy) |
| 2617 | `model.layers.11` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0002617.npy) |
| 2618 | `model.layers.11` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2619 | `model.layers.11` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2620 | `model.layers.11` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2621 | `model.layers.11.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -412.0 / 556.0 / 0.3621307373046875 / 23.448591075416562 | [NPY](tensors/0002621.npy) |
| 2622 | `model.layers.11.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.0 / 111.0 / 0.05288289719157749 / 3.2466243271163466 | [NPY](tensors/0002622.npy) |
| 2623 | `model.layers.11.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.0 / 111.0 / 0.05288289719157749 / 3.2466243271163466 | [NPY](tensors/0002623.npy) |
| 2624 | `model.layers.11.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 319] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002624.npy) |
| 2625 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0002625.npy) |
| 2626 | `model.layers.11.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2627 | `model.layers.11.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2628 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0002628.npy) |
| 2629 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0002629.npy) |
| 2630 | `model.layers.11.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2631 | `model.layers.11.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.0 / 111.0 / 0.05288289719157749 / 3.2466243271163466 | [NPY](tensors/0002631.npy) |
| 2632 | `model.layers.11.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 10.3125 / 0.018643055111169815 / 1.320264118165321 | [NPY](tensors/0002632.npy) |
| 2633 | `model.layers.11.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.0 / 111.0 / 0.05288289719157749 / 3.2466243271163466 | [NPY](tensors/0002633.npy) |
| 2634 | `model.layers.11.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.75 / 32.75 / -0.009192734956741333 / 3.5779220909688925 | [NPY](tensors/0002634.npy) |
| 2635 | `model.layers.11.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.0 / 111.0 / 0.05288289719157749 / 3.2466243271163466 | [NPY](tensors/0002635.npy) |
| 2636 | `model.layers.11.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.65625 / 8.4375 / 0.05604441463947296 / 2.467312663943 | [NPY](tensors/0002636.npy) |
| 2637 | `model.layers.11.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.09375 / 7.28125 / 0.008087650872766972 / 1.3985282362923475 | [NPY](tensors/0002637.npy) |
| 2638 | `model.layers.11.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -164.0 / 149.0 / -0.05318240457110935 / 5.2190944964418415 | [NPY](tensors/0002638.npy) |
| 2639 | `model.layers.11.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -164.0 / 149.0 / -0.05318240457110935 / 5.2190944964418415 | [NPY](tensors/0002639.npy) |
| 2640 | `model.layers.11.self_attn` | 22 | `output[1]` | [1, 64, 1, 319] | torch.bfloat16 → float32 | 9.276845958083868e-11 / 0.90234375 / 0.0024662649277108453 / 0.018832986234308097 | [NPY](tensors/0002640.npy) |
| 2641 | `model.layers.11.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -264.0 / 392.0 / 0.30894894070095485 / 21.776013392020165 | [NPY](tensors/0002641.npy) |
| 2642 | `model.layers.11.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.03125 / 3.796875 / 0.006615134742524889 / 0.7363018391495987 | [NPY](tensors/0002642.npy) |
| 2643 | `model.layers.11.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.03125 / 3.796875 / 0.006615134742524889 / 0.7363018391495987 | [NPY](tensors/0002643.npy) |
| 2644 | `model.layers.11.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.03125 / 3.796875 / 0.006615134742524889 / 0.7363018391495987 | [NPY](tensors/0002644.npy) |
| 2645 | `model.layers.11.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2646 | `model.layers.11.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2647 | `model.layers.11.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2648 | `model.layers.11.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -258.0 / 172.0 / 0.08462225794792175 / 8.498241073754405 | [NPY](tensors/0002648.npy) |
| 2649 | `model.layers.11.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -258.0 / 172.0 / 0.08462225794792175 / 8.498241073754405 | [NPY](tensors/0002649.npy) |
| 2650 | `model.layers.11.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.125 / 1.4921875 / -0.20665550231933594 / 0.9097266014639891 | [NPY](tensors/0002650.npy) |
| 2651 | `model.layers.11` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -520.0 / 564.0 / 0.39488288031684027 / 27.045318749389825 | [NPY](tensors/0002651.npy) |
| 2730 | `model.layers.11` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -456.0 / 564.0 / 0.6162411159939236 / 24.295481384260363 | [NPY](tensors/0002730.npy) |
| 2731 | `model.layers.11` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 320] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002731.npy) |
| 2732 | `model.layers.11` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0002732.npy) |
| 2733 | `model.layers.11` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0002733.npy) |
| 2734 | `model.layers.11` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0002734.npy) |
| 2735 | `model.layers.11` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2736 | `model.layers.11` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2737 | `model.layers.11` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2738 | `model.layers.11.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -456.0 / 564.0 / 0.6162411159939236 / 24.295481384260363 | [NPY](tensors/0002738.npy) |
| 2739 | `model.layers.11.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 109.0 / 0.06875504520204333 / 3.2989274860307694 | [NPY](tensors/0002739.npy) |
| 2740 | `model.layers.11.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 109.0 / 0.06875504520204333 / 3.2989274860307694 | [NPY](tensors/0002740.npy) |
| 2741 | `model.layers.11.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 320] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002741.npy) |
| 2742 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0002742.npy) |
| 2743 | `model.layers.11.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2744 | `model.layers.11.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2745 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0002745.npy) |
| 2746 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0002746.npy) |
| 2747 | `model.layers.11.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2748 | `model.layers.11.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 109.0 / 0.06875504520204333 / 3.2989274860307694 | [NPY](tensors/0002748.npy) |
| 2749 | `model.layers.11.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.71875 / 9.375 / 0.013058967422693968 / 1.3645326293342228 | [NPY](tensors/0002749.npy) |
| 2750 | `model.layers.11.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 109.0 / 0.06875504520204333 / 3.2989274860307694 | [NPY](tensors/0002750.npy) |
| 2751 | `model.layers.11.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.5 / 37.25 / 0.014310158789157867 / 3.7410501288492823 | [NPY](tensors/0002751.npy) |
| 2752 | `model.layers.11.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 109.0 / 0.06875504520204333 / 3.2989274860307694 | [NPY](tensors/0002752.npy) |
| 2753 | `model.layers.11.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.71875 / 7.15625 / 0.025274701416492462 / 2.439314843609764 | [NPY](tensors/0002753.npy) |
| 2754 | `model.layers.11.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5 / 7.59375 / 0.0036898984108120203 / 1.4790332202646257 | [NPY](tensors/0002754.npy) |
| 2755 | `model.layers.11.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -144.0 / 145.0 / 0.020770021279652915 / 5.1130875274351295 | [NPY](tensors/0002755.npy) |
| 2756 | `model.layers.11.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -144.0 / 145.0 / 0.020770021279652915 / 5.1130875274351295 | [NPY](tensors/0002756.npy) |
| 2757 | `model.layers.11.self_attn` | 23 | `output[1]` | [1, 64, 1, 320] | torch.bfloat16 → float32 | 4.206412995699793e-11 / 0.91796875 / 0.002562596713779419 / 0.018163581316223892 | [NPY](tensors/0002757.npy) |
| 2758 | `model.layers.11.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 420.0 / 0.636179945203993 / 23.437320656844665 | [NPY](tensors/0002758.npy) |
| 2759 | `model.layers.11.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.0625 / 0.01684457858403524 / 0.7332669291866049 | [NPY](tensors/0002759.npy) |
| 2760 | `model.layers.11.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.0625 / 0.01684457858403524 / 0.7332669291866049 | [NPY](tensors/0002760.npy) |
| 2761 | `model.layers.11.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.75 / 3.0625 / 0.01684457858403524 / 0.7332669291866049 | [NPY](tensors/0002761.npy) |
| 2762 | `model.layers.11.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2763 | `model.layers.11.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2764 | `model.layers.11.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2765 | `model.layers.11.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -234.0 / 198.0 / 0.13006038665771485 / 8.231344219307548 | [NPY](tensors/0002765.npy) |
| 2766 | `model.layers.11.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -234.0 / 198.0 / 0.13006038665771485 / 8.231344219307548 | [NPY](tensors/0002766.npy) |
| 2767 | `model.layers.11.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.859375 / 1.4921875 / -0.17022705078125 / 0.8662451578195177 | [NPY](tensors/0002767.npy) |
| 2768 | `model.layers.11` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -544.0 / 616.0 / 0.7671566433376736 / 28.597323906046427 | [NPY](tensors/0002768.npy) |
| 2847 | `model.layers.11` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -370.0 / 520.0 / 0.6303124321831597 / 23.55690170961388 | [NPY](tensors/0002847.npy) |
| 2848 | `model.layers.11` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 321] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002848.npy) |
| 2849 | `model.layers.11` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0002849.npy) |
| 2850 | `model.layers.11` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0002850.npy) |
| 2851 | `model.layers.11` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0002851.npy) |
| 2852 | `model.layers.11` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2853 | `model.layers.11` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2854 | `model.layers.11` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2855 | `model.layers.11.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -370.0 / 520.0 / 0.6303124321831597 / 23.55690170961388 | [NPY](tensors/0002855.npy) |
| 2856 | `model.layers.11.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 103.5 / 0.06774003240797255 / 3.0755924216921917 | [NPY](tensors/0002856.npy) |
| 2857 | `model.layers.11.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 103.5 / 0.06774003240797255 / 3.0755924216921917 | [NPY](tensors/0002857.npy) |
| 2858 | `model.layers.11.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 321] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002858.npy) |
| 2859 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0002859.npy) |
| 2860 | `model.layers.11.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2861 | `model.layers.11.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2862 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0002862.npy) |
| 2863 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0002863.npy) |
| 2864 | `model.layers.11.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2865 | `model.layers.11.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 103.5 / 0.06774003240797255 / 3.0755924216921917 | [NPY](tensors/0002865.npy) |
| 2866 | `model.layers.11.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.875 / 8.25 / -0.007403162308037281 / 1.4007172740201363 | [NPY](tensors/0002866.npy) |
| 2867 | `model.layers.11.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 103.5 / 0.06774003240797255 / 3.0755924216921917 | [NPY](tensors/0002867.npy) |
| 2868 | `model.layers.11.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.0 / 35.0 / 0.008454550057649612 / 3.620304393777219 | [NPY](tensors/0002868.npy) |
| 2869 | `model.layers.11.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -82.5 / 103.5 / 0.06774003240797255 / 3.0755924216921917 | [NPY](tensors/0002869.npy) |
| 2870 | `model.layers.11.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.1875 / 6.5625 / -0.17097985744476318 / 2.3903142720386343 | [NPY](tensors/0002870.npy) |
| 2871 | `model.layers.11.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.3125 / 8.0625 / -0.027732240967452526 / 1.611153871027064 | [NPY](tensors/0002871.npy) |
| 2872 | `model.layers.11.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -157.0 / 138.0 / 0.0037230279710557725 / 5.578911597133598 | [NPY](tensors/0002872.npy) |
| 2873 | `model.layers.11.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -157.0 / 138.0 / 0.0037230279710557725 / 5.578911597133598 | [NPY](tensors/0002873.npy) |
| 2874 | `model.layers.11.self_attn` | 24 | `output[1]` | [1, 64, 1, 321] | torch.bfloat16 → float32 | 1.3358203432289883e-11 / 0.96484375 / 0.0025473920039432375 / 0.020812328189128676 | [NPY](tensors/0002874.npy) |
| 2875 | `model.layers.11.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -232.0 / 364.0 / 0.6344957139756945 / 22.606423145033368 | [NPY](tensors/0002875.npy) |
| 2876 | `model.layers.11.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.71875 / 3.5625 / 0.011147711012098525 / 0.7904871201517206 | [NPY](tensors/0002876.npy) |
| 2877 | `model.layers.11.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.71875 / 3.5625 / 0.011147711012098525 / 0.7904871201517206 | [NPY](tensors/0002877.npy) |
| 2878 | `model.layers.11.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.71875 / 3.5625 / 0.011147711012098525 / 0.7904871201517206 | [NPY](tensors/0002878.npy) |
| 2879 | `model.layers.11.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2880 | `model.layers.11.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2881 | `model.layers.11.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2882 | `model.layers.11.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -298.0 / 316.0 / 0.14012329313490127 / 10.744797724358635 | [NPY](tensors/0002882.npy) |
| 2883 | `model.layers.11.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -298.0 / 316.0 / 0.14012329313490127 / 10.744797724358635 | [NPY](tensors/0002883.npy) |
| 2884 | `model.layers.11.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.234375 / 1.796875 / -0.1636066436767578 / 0.8332411846088136 | [NPY](tensors/0002884.npy) |
| 2885 | `model.layers.11` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -528.0 / 680.0 / 0.7753689236111111 / 29.390708815006423 | [NPY](tensors/0002885.npy) |
| 2964 | `model.layers.11` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -249.0 / 408.0 / 0.7050889756944444 / 19.419840975572004 | [NPY](tensors/0002964.npy) |
| 2965 | `model.layers.11` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002965.npy) |
| 2966 | `model.layers.11` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0002966.npy) |
| 2967 | `model.layers.11` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0002967.npy) |
| 2968 | `model.layers.11` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0002968.npy) |
| 2969 | `model.layers.11` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2970 | `model.layers.11` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2971 | `model.layers.11` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2972 | `model.layers.11.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -249.0 / 408.0 / 0.7050889756944444 / 19.419840975572004 | [NPY](tensors/0002972.npy) |
| 2973 | `model.layers.11.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -67.5 / 98.5 / 0.09350817302862803 / 2.922642132359397 | [NPY](tensors/0002973.npy) |
| 2974 | `model.layers.11.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -67.5 / 98.5 / 0.09350817302862803 / 2.922642132359397 | [NPY](tensors/0002974.npy) |
| 2975 | `model.layers.11.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002975.npy) |
| 2976 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0002976.npy) |
| 2977 | `model.layers.11.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2978 | `model.layers.11.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2979 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0002979.npy) |
| 2980 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0002980.npy) |
| 2981 | `model.layers.11.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2982 | `model.layers.11.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -67.5 / 98.5 / 0.09350817302862803 / 2.922642132359397 | [NPY](tensors/0002982.npy) |
| 2983 | `model.layers.11.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.125 / 10.625 / 0.02901160402689129 / 1.4634051948992801 | [NPY](tensors/0002983.npy) |
| 2984 | `model.layers.11.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -67.5 / 98.5 / 0.09350817302862803 / 2.922642132359397 | [NPY](tensors/0002984.npy) |
| 2985 | `model.layers.11.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.875 / 40.0 / 0.07724420726299286 / 4.2341983305088755 | [NPY](tensors/0002985.npy) |
| 2986 | `model.layers.11.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -67.5 / 98.5 / 0.09350817302862803 / 2.922642132359397 | [NPY](tensors/0002986.npy) |
| 2987 | `model.layers.11.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.84375 / 7.53125 / -0.010166704654693604 / 2.3484179868214996 | [NPY](tensors/0002987.npy) |
| 2988 | `model.layers.11.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 8.0625 / -0.005338733200915158 / 1.5269956226856463 | [NPY](tensors/0002988.npy) |
| 2989 | `model.layers.11.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.0 / 36.0 / 0.0377254671520657 / 3.8999654858090844 | [NPY](tensors/0002989.npy) |
| 2990 | `model.layers.11.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.0 / 36.0 / 0.0377254671520657 / 3.8999654858090844 | [NPY](tensors/0002990.npy) |
| 2991 | `model.layers.11.self_attn` | 25 | `output[1]` | [1, 64, 1, 322] | torch.bfloat16 → float32 | 6.195932655828074e-12 / 0.9609375 / 0.002825153423513226 / 0.01645992332507731 | [NPY](tensors/0002991.npy) |
| 2992 | `model.layers.11.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -213.0 / 356.0 / 0.7431638929578993 / 20.125519208830355 | [NPY](tensors/0002992.npy) |
| 2993 | `model.layers.11.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.78125 / 3.65625 / 0.01700689991315206 / 0.7423776235487194 | [NPY](tensors/0002993.npy) |
| 2994 | `model.layers.11.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.78125 / 3.65625 / 0.01700689991315206 / 0.7423776235487194 | [NPY](tensors/0002994.npy) |
| 2995 | `model.layers.11.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.78125 / 3.65625 / 0.01700689991315206 / 0.7423776235487194 | [NPY](tensors/0002995.npy) |
| 2996 | `model.layers.11.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2997 | `model.layers.11.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2998 | `model.layers.11.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2999 | `model.layers.11.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -212.0 / 130.0 / 0.18728177282545302 / 7.407217608923624 | [NPY](tensors/0002999.npy) |
| 3000 | `model.layers.11.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -212.0 / 130.0 / 0.18728177282545302 / 7.407217608923624 | [NPY](tensors/0003000.npy) |
| 3001 | `model.layers.11.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.953125 / 2.015625 / -0.12001991271972656 / 0.7714928813446322 | [NPY](tensors/0003001.npy) |
| 3002 | `model.layers.11` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -424.0 / 486.0 / 0.9322645399305556 / 24.386343260703764 | [NPY](tensors/0003002.npy) |
| 3081 | `model.layers.11` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -320.0 / 396.0 / 0.3705373128255208 / 19.2511337434254 | [NPY](tensors/0003081.npy) |
| 3082 | `model.layers.11` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003082.npy) |
| 3083 | `model.layers.11` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0003083.npy) |
| 3084 | `model.layers.11` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0003084.npy) |
| 3085 | `model.layers.11` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0003085.npy) |
| 3086 | `model.layers.11` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3087 | `model.layers.11` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3088 | `model.layers.11` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3089 | `model.layers.11.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -320.0 / 396.0 / 0.3705373128255208 / 19.2511337434254 | [NPY](tensors/0003089.npy) |
| 3090 | `model.layers.11.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 96.5 / 0.05363401836819119 / 3.1094017958481155 | [NPY](tensors/0003090.npy) |
| 3091 | `model.layers.11.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 96.5 / 0.05363401836819119 / 3.1094017958481155 | [NPY](tensors/0003091.npy) |
| 3092 | `model.layers.11.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003092.npy) |
| 3093 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0003093.npy) |
| 3094 | `model.layers.11.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3095 | `model.layers.11.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3096 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0003096.npy) |
| 3097 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0003097.npy) |
| 3098 | `model.layers.11.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3099 | `model.layers.11.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 96.5 / 0.05363401836819119 / 3.1094017958481155 | [NPY](tensors/0003099.npy) |
| 3100 | `model.layers.11.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.5625 / 8.9375 / 0.028274822514504194 / 1.35654954335013 | [NPY](tensors/0003100.npy) |
| 3101 | `model.layers.11.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 96.5 / 0.05363401836819119 / 3.1094017958481155 | [NPY](tensors/0003101.npy) |
| 3102 | `model.layers.11.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.75 / 34.5 / 0.12141421437263489 / 3.8069582014250125 | [NPY](tensors/0003102.npy) |
| 3103 | `model.layers.11.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 96.5 / 0.05363401836819119 / 3.1094017958481155 | [NPY](tensors/0003103.npy) |
| 3104 | `model.layers.11.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.40625 / 8.0 / -0.14673420041799545 / 2.1873396970213275 | [NPY](tensors/0003104.npy) |
| 3105 | `model.layers.11.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.375 / 7.375 / 0.006516441470012069 / 1.4169043252372509 | [NPY](tensors/0003105.npy) |
| 3106 | `model.layers.11.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -135.0 / 172.0 / -0.022368432415856256 / 5.713117848195793 | [NPY](tensors/0003106.npy) |
| 3107 | `model.layers.11.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -135.0 / 172.0 / -0.022368432415856256 / 5.713117848195793 | [NPY](tensors/0003107.npy) |
| 3108 | `model.layers.11.self_attn` | 26 | `output[1]` | [1, 64, 1, 323] | torch.bfloat16 → float32 | 3.456079866737127e-11 / 0.91796875 / 0.0026864746137681144 / 0.01626503619413564 | [NPY](tensors/0003108.npy) |
| 3109 | `model.layers.11.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -215.0 / 260.0 / 0.3479817708333333 / 18.51518801050522 | [NPY](tensors/0003109.npy) |
| 3110 | `model.layers.11.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.703125 / 3.984375 / 0.01174072027206421 / 0.7942275969918898 | [NPY](tensors/0003110.npy) |
| 3111 | `model.layers.11.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.703125 / 3.984375 / 0.01174072027206421 / 0.7942275969918898 | [NPY](tensors/0003111.npy) |
| 3112 | `model.layers.11.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.703125 / 3.984375 / 0.01174072027206421 / 0.7942275969918898 | [NPY](tensors/0003112.npy) |
| 3113 | `model.layers.11.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3114 | `model.layers.11.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3115 | `model.layers.11.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3116 | `model.layers.11.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -248.0 / 282.0 / 0.24929174582163494 / 9.778047938206507 | [NPY](tensors/0003116.npy) |
| 3117 | `model.layers.11.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -248.0 / 282.0 / 0.24929174582163494 / 9.778047938206507 | [NPY](tensors/0003117.npy) |
| 3118 | `model.layers.11.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.5625 / 1.8125 / -0.153717041015625 / 0.8572264033858681 | [NPY](tensors/0003118.npy) |
| 3119 | `model.layers.11` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -396.0 / 544.0 / 0.5973171657986112 / 24.234876710797767 | [NPY](tensors/0003119.npy) |
| 3198 | `model.layers.11` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -372.0 / 592.0 / 0.4052769978841146 / 21.633169023245504 | [NPY](tensors/0003198.npy) |
| 3199 | `model.layers.11` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003199.npy) |
| 3200 | `model.layers.11` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0003200.npy) |
| 3201 | `model.layers.11` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0003201.npy) |
| 3202 | `model.layers.11` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0003202.npy) |
| 3203 | `model.layers.11` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3204 | `model.layers.11` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3205 | `model.layers.11` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3206 | `model.layers.11.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -372.0 / 592.0 / 0.4052769978841146 / 21.633169023245504 | [NPY](tensors/0003206.npy) |
| 3207 | `model.layers.11.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 128.0 / 0.06208810806274414 / 3.426978473057382 | [NPY](tensors/0003207.npy) |
| 3208 | `model.layers.11.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 128.0 / 0.06208810806274414 / 3.426978473057382 | [NPY](tensors/0003208.npy) |
| 3209 | `model.layers.11.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003209.npy) |
| 3210 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0003210.npy) |
| 3211 | `model.layers.11.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3212 | `model.layers.11.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3213 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0003213.npy) |
| 3214 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0003214.npy) |
| 3215 | `model.layers.11.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3216 | `model.layers.11.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 128.0 / 0.06208810806274414 / 3.426978473057382 | [NPY](tensors/0003216.npy) |
| 3217 | `model.layers.11.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.125 / 8.9375 / -0.0007906286045908928 / 1.307262437499847 | [NPY](tensors/0003217.npy) |
| 3218 | `model.layers.11.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 128.0 / 0.06208810806274414 / 3.426978473057382 | [NPY](tensors/0003218.npy) |
| 3219 | `model.layers.11.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.125 / 33.0 / -0.02896621823310852 / 3.5694199794853327 | [NPY](tensors/0003219.npy) |
| 3220 | `model.layers.11.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 128.0 / 0.06208810806274414 / 3.426978473057382 | [NPY](tensors/0003220.npy) |
| 3221 | `model.layers.11.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.46875 / 8.1875 / -0.12250838987529278 / 2.37813087568862 | [NPY](tensors/0003221.npy) |
| 3222 | `model.layers.11.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.59375 / 7.25 / -0.004085618536919355 / 1.3910414879595054 | [NPY](tensors/0003222.npy) |
| 3223 | `model.layers.11.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -247.0 / 207.0 / -0.11526503413915634 / 7.01614735475185 | [NPY](tensors/0003223.npy) |
| 3224 | `model.layers.11.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -247.0 / 207.0 / -0.11526503413915634 / 7.01614735475185 | [NPY](tensors/0003224.npy) |
| 3225 | `model.layers.11.self_attn` | 27 | `output[1]` | [1, 64, 1, 324] | torch.bfloat16 → float32 | 1.3073986337985843e-11 / 0.94140625 / 0.002518275953583261 / 0.017578184475156806 | [NPY](tensors/0003225.npy) |
| 3226 | `model.layers.11.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -178.0 / 344.0 / 0.28968336317274307 / 18.914782917992117 | [NPY](tensors/0003226.npy) |
| 3227 | `model.layers.11.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.0 / 5.0 / 0.006901576121648153 / 0.7625916287445557 | [NPY](tensors/0003227.npy) |
| 3228 | `model.layers.11.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.0 / 5.0 / 0.006901576121648153 / 0.7625916287445557 | [NPY](tensors/0003228.npy) |
| 3229 | `model.layers.11.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.0 / 5.0 / 0.006901576121648153 / 0.7625916287445557 | [NPY](tensors/0003229.npy) |
| 3230 | `model.layers.11.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3231 | `model.layers.11.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3232 | `model.layers.11.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3233 | `model.layers.11.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -408.0 / 388.0 / 0.2859234174092611 / 14.571615527247273 | [NPY](tensors/0003233.npy) |
| 3234 | `model.layers.11.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -408.0 / 388.0 / 0.2859234174092611 / 14.571615527247273 | [NPY](tensors/0003234.npy) |
| 3235 | `model.layers.11.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.515625 / 1.8828125 / -0.21466928720474243 / 1.1184007415160395 | [NPY](tensors/0003235.npy) |
| 3236 | `model.layers.11` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -572.0 / 732.0 / 0.5759489271375868 / 28.531677251060476 | [NPY](tensors/0003236.npy) |
| 3315 | `model.layers.11` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -186.0 / 404.0 / 0.7679780748155381 / 15.934281776821061 | [NPY](tensors/0003315.npy) |
| 3316 | `model.layers.11` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003316.npy) |
| 3317 | `model.layers.11` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0003317.npy) |
| 3318 | `model.layers.11` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0003318.npy) |
| 3319 | `model.layers.11` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0003319.npy) |
| 3320 | `model.layers.11` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3321 | `model.layers.11` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3322 | `model.layers.11` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3323 | `model.layers.11.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -186.0 / 404.0 / 0.7679780748155381 / 15.934281776821061 | [NPY](tensors/0003323.npy) |
| 3324 | `model.layers.11.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.25 / 118.5 / 0.11523251268598768 / 3.1637740321723644 | [NPY](tensors/0003324.npy) |
| 3325 | `model.layers.11.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.25 / 118.5 / 0.11523251268598768 / 3.1637740321723644 | [NPY](tensors/0003325.npy) |
| 3326 | `model.layers.11.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003326.npy) |
| 3327 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0003327.npy) |
| 3328 | `model.layers.11.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3329 | `model.layers.11.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3330 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0003330.npy) |
| 3331 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0003331.npy) |
| 3332 | `model.layers.11.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3333 | `model.layers.11.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.25 / 118.5 / 0.11523251268598768 / 3.1637740321723644 | [NPY](tensors/0003333.npy) |
| 3334 | `model.layers.11.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.625 / 9.0625 / 0.039687504991889 / 1.3146567426567242 | [NPY](tensors/0003334.npy) |
| 3335 | `model.layers.11.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.25 / 118.5 / 0.11523251268598768 / 3.1637740321723644 | [NPY](tensors/0003335.npy) |
| 3336 | `model.layers.11.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 44.5 / 0.19012868404388428 / 4.292511599631668 | [NPY](tensors/0003336.npy) |
| 3337 | `model.layers.11.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.25 / 118.5 / 0.11523251268598768 / 3.1637740321723644 | [NPY](tensors/0003337.npy) |
| 3338 | `model.layers.11.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.71875 / 7.0 / 0.06133115291595459 / 2.365236703535114 | [NPY](tensors/0003338.npy) |
| 3339 | `model.layers.11.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.5 / 6.78125 / 0.005106939468532801 / 1.5043958984699353 | [NPY](tensors/0003339.npy) |
| 3340 | `model.layers.11.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 26.875 / 0.018458943896823458 / 3.9816784527915807 | [NPY](tensors/0003340.npy) |
| 3341 | `model.layers.11.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 26.875 / 0.018458943896823458 / 3.9816784527915807 | [NPY](tensors/0003341.npy) |
| 3342 | `model.layers.11.self_attn` | 28 | `output[1]` | [1, 64, 1, 325] | torch.bfloat16 → float32 | 1.2505552149377763e-12 / 0.96484375 / 0.0028898248703642135 / 0.015261060215211017 | [NPY](tensors/0003342.npy) |
| 3343 | `model.layers.11.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -159.0 / 366.0 / 0.7861501057942708 / 16.607370668427215 | [NPY](tensors/0003343.npy) |
| 3344 | `model.layers.11.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.375 / 2.8125 / 0.03569569322797987 / 0.7471953139829826 | [NPY](tensors/0003344.npy) |
| 3345 | `model.layers.11.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.375 / 2.8125 / 0.03569569322797987 / 0.7471953139829826 | [NPY](tensors/0003345.npy) |
| 3346 | `model.layers.11.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.375 / 2.8125 / 0.03569569322797987 / 0.7471953139829826 | [NPY](tensors/0003346.npy) |
| 3347 | `model.layers.11.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3348 | `model.layers.11.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3349 | `model.layers.11.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3350 | `model.layers.11.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -153.0 / 105.5 / -0.006814119550916884 / 6.050342457690215 | [NPY](tensors/0003350.npy) |
| 3351 | `model.layers.11.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -153.0 / 105.5 / -0.006814119550916884 / 6.050342457690215 | [NPY](tensors/0003351.npy) |
| 3352 | `model.layers.11.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.1328125 / -0.084075927734375 / 0.5815073523576907 | [NPY](tensors/0003352.npy) |
| 3353 | `model.layers.11` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 472.0 / 0.7796454535590278 / 19.96036714413795 | [NPY](tensors/0003353.npy) |
| 3432 | `model.layers.11` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -340.0 / 536.0 / 0.31498328314887153 / 20.201480460628797 | [NPY](tensors/0003432.npy) |
| 3433 | `model.layers.11` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003433.npy) |
| 3434 | `model.layers.11` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0003434.npy) |
| 3435 | `model.layers.11` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0003435.npy) |
| 3436 | `model.layers.11` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0003436.npy) |
| 3437 | `model.layers.11` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3438 | `model.layers.11` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3439 | `model.layers.11` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3440 | `model.layers.11.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -340.0 / 536.0 / 0.31498328314887153 / 20.201480460628797 | [NPY](tensors/0003440.npy) |
| 3441 | `model.layers.11.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 124.5 / 0.052930871645609535 / 3.345117886626555 | [NPY](tensors/0003441.npy) |
| 3442 | `model.layers.11.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 124.5 / 0.052930871645609535 / 3.345117886626555 | [NPY](tensors/0003442.npy) |
| 3443 | `model.layers.11.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003443.npy) |
| 3444 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0003444.npy) |
| 3445 | `model.layers.11.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3446 | `model.layers.11.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3447 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0003447.npy) |
| 3448 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0003448.npy) |
| 3449 | `model.layers.11.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3450 | `model.layers.11.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 124.5 / 0.052930871645609535 / 3.345117886626555 | [NPY](tensors/0003450.npy) |
| 3451 | `model.layers.11.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.03125 / 10.375 / 0.010654324709321372 / 1.2867815051814557 | [NPY](tensors/0003451.npy) |
| 3452 | `model.layers.11.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 124.5 / 0.052930871645609535 / 3.345117886626555 | [NPY](tensors/0003452.npy) |
| 3453 | `model.layers.11.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.625 / 31.25 / -0.030289411544799805 / 3.564053155976414 | [NPY](tensors/0003453.npy) |
| 3454 | `model.layers.11.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 124.5 / 0.052930871645609535 / 3.345117886626555 | [NPY](tensors/0003454.npy) |
| 3455 | `model.layers.11.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.8125 / 7.96875 / 0.014444053173065186 / 2.378558133591894 | [NPY](tensors/0003455.npy) |
| 3456 | `model.layers.11.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.125 / 6.1875 / 0.011009473586454988 / 1.395293229156063 | [NPY](tensors/0003456.npy) |
| 3457 | `model.layers.11.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -136.0 / 112.0 / -0.023655094040764702 / 4.751011651377421 | [NPY](tensors/0003457.npy) |
| 3458 | `model.layers.11.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -136.0 / 112.0 / -0.023655094040764702 / 4.751011651377421 | [NPY](tensors/0003458.npy) |
| 3459 | `model.layers.11.self_attn` | 29 | `output[1]` | [1, 64, 1, 326] | torch.bfloat16 → float32 | 6.338041202980094e-12 / 0.96875 / 0.002810695306833294 / 0.015586513007588261 | [NPY](tensors/0003459.npy) |
| 3460 | `model.layers.11.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -228.0 / 400.0 / 0.29095848931206597 / 19.1713775076877 | [NPY](tensors/0003460.npy) |
| 3461 | `model.layers.11.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.953125 / 3.8125 / 0.008411770396762424 / 0.7170081633581432 | [NPY](tensors/0003461.npy) |
| 3462 | `model.layers.11.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.953125 / 3.8125 / 0.008411770396762424 / 0.7170081633581432 | [NPY](tensors/0003462.npy) |
| 3463 | `model.layers.11.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.953125 / 3.8125 / 0.008411770396762424 / 0.7170081633581432 | [NPY](tensors/0003463.npy) |
| 3464 | `model.layers.11.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3465 | `model.layers.11.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3466 | `model.layers.11.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3467 | `model.layers.11.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -214.0 / 225.0 / 0.16125933395491707 / 8.370729657438776 | [NPY](tensors/0003467.npy) |
| 3468 | `model.layers.11.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -214.0 / 225.0 / 0.16125933395491707 / 8.370729657438776 | [NPY](tensors/0003468.npy) |
| 3469 | `model.layers.11.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.578125 / 1.484375 / -0.19818735122680664 / 0.9127909283680764 | [NPY](tensors/0003469.npy) |
| 3470 | `model.layers.11` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -442.0 / 624.0 / 0.45168490939670136 / 24.83453609828336 | [NPY](tensors/0003470.npy) |
| 3549 | `model.layers.11` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -171.0 / 364.0 / 0.3393394046359592 / 14.318331700227297 | [NPY](tensors/0003549.npy) |
| 3550 | `model.layers.11` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003550.npy) |
| 3551 | `model.layers.11` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0003551.npy) |
| 3552 | `model.layers.11` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0003552.npy) |
| 3553 | `model.layers.11` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0003553.npy) |
| 3554 | `model.layers.11` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3555 | `model.layers.11` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3556 | `model.layers.11` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3557 | `model.layers.11.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -171.0 / 364.0 / 0.3393394046359592 / 14.318331700227297 | [NPY](tensors/0003557.npy) |
| 3558 | `model.layers.11.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.75 / 102.0 / 0.0789727322757244 / 3.1058144277652335 | [NPY](tensors/0003558.npy) |
| 3559 | `model.layers.11.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.75 / 102.0 / 0.0789727322757244 / 3.1058144277652335 | [NPY](tensors/0003559.npy) |
| 3560 | `model.layers.11.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003560.npy) |
| 3561 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0003561.npy) |
| 3562 | `model.layers.11.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3563 | `model.layers.11.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3564 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0003564.npy) |
| 3565 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0003565.npy) |
| 3566 | `model.layers.11.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3567 | `model.layers.11.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.75 / 102.0 / 0.0789727322757244 / 3.1058144277652335 | [NPY](tensors/0003567.npy) |
| 3568 | `model.layers.11.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.5625 / 7.75 / 0.017711902037262917 / 1.2599441157352167 | [NPY](tensors/0003568.npy) |
| 3569 | `model.layers.11.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.75 / 102.0 / 0.0789727322757244 / 3.1058144277652335 | [NPY](tensors/0003569.npy) |
| 3570 | `model.layers.11.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.75 / 36.0 / 0.1381659060716629 / 3.714134609195613 | [NPY](tensors/0003570.npy) |
| 3571 | `model.layers.11.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.75 / 102.0 / 0.0789727322757244 / 3.1058144277652335 | [NPY](tensors/0003571.npy) |
| 3572 | `model.layers.11.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.375 / 7.125 / 0.00022157281637191772 / 1.9222399518666018 | [NPY](tensors/0003572.npy) |
| 3573 | `model.layers.11.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.53125 / 5.6875 / -0.01620375458151102 / 1.2754045915590444 | [NPY](tensors/0003573.npy) |
| 3574 | `model.layers.11.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.75 / 38.25 / 0.07542264726426866 / 4.1658737288526115 | [NPY](tensors/0003574.npy) |
| 3575 | `model.layers.11.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.75 / 38.25 / 0.07542264726426866 / 4.1658737288526115 | [NPY](tensors/0003575.npy) |
| 3576 | `model.layers.11.self_attn` | 30 | `output[1]` | [1, 64, 1, 327] | torch.bfloat16 → float32 | 5.566107574850321e-10 / 0.828125 / 0.002805961613692882 / 0.011563136029167514 | [NPY](tensors/0003576.npy) |
| 3577 | `model.layers.11.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -163.0 / 368.0 / 0.4143400404188368 / 15.643922583421764 | [NPY](tensors/0003577.npy) |
| 3578 | `model.layers.11.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.453125 / 3.859375 / 0.005057175954182942 / 0.6757162418542415 | [NPY](tensors/0003578.npy) |
| 3579 | `model.layers.11.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.453125 / 3.859375 / 0.005057175954182942 / 0.6757162418542415 | [NPY](tensors/0003579.npy) |
| 3580 | `model.layers.11.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.453125 / 3.859375 / 0.005057175954182942 / 0.6757162418542415 | [NPY](tensors/0003580.npy) |
| 3581 | `model.layers.11.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3582 | `model.layers.11.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3583 | `model.layers.11.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3584 | `model.layers.11.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -160.0 / 218.0 / 0.15980040497250028 / 7.510540085861946 | [NPY](tensors/0003584.npy) |
| 3585 | `model.layers.11.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -160.0 / 218.0 / 0.15980040497250028 / 7.510540085861946 | [NPY](tensors/0003585.npy) |
| 3586 | `model.layers.11.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.375 / 1.140625 / -0.12110495567321777 / 0.6534366680404372 | [NPY](tensors/0003586.npy) |
| 3587 | `model.layers.11` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -324.0 / 536.0 / 0.5745469835069444 / 20.811150581880632 | [NPY](tensors/0003587.npy) |
| 3666 | `model.layers.11` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -224.0 / 342.0 / 0.25311126708984377 / 13.461949171181763 | [NPY](tensors/0003666.npy) |
| 3667 | `model.layers.11` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003667.npy) |
| 3668 | `model.layers.11` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0003668.npy) |
| 3669 | `model.layers.11` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0003669.npy) |
| 3670 | `model.layers.11` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0003670.npy) |
| 3671 | `model.layers.11` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3672 | `model.layers.11` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3673 | `model.layers.11` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3674 | `model.layers.11.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -224.0 / 342.0 / 0.25311126708984377 / 13.461949171181763 | [NPY](tensors/0003674.npy) |
| 3675 | `model.layers.11.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 93.5 / 0.05520790417989095 / 3.152646447714153 | [NPY](tensors/0003675.npy) |
| 3676 | `model.layers.11.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 93.5 / 0.05520790417989095 / 3.152646447714153 | [NPY](tensors/0003676.npy) |
| 3677 | `model.layers.11.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003677.npy) |
| 3678 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0003678.npy) |
| 3679 | `model.layers.11.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3680 | `model.layers.11.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3681 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0003681.npy) |
| 3682 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0003682.npy) |
| 3683 | `model.layers.11.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3684 | `model.layers.11.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 93.5 / 0.05520790417989095 / 3.152646447714153 | [NPY](tensors/0003684.npy) |
| 3685 | `model.layers.11.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.0 / 8.1875 / 0.03722104933694936 / 1.231101781381261 | [NPY](tensors/0003685.npy) |
| 3686 | `model.layers.11.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 93.5 / 0.05520790417989095 / 3.152646447714153 | [NPY](tensors/0003686.npy) |
| 3687 | `model.layers.11.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.5 / 36.25 / 0.1741015687584877 / 3.701986009569941 | [NPY](tensors/0003687.npy) |
| 3688 | `model.layers.11.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 93.5 / 0.05520790417989095 / 3.152646447714153 | [NPY](tensors/0003688.npy) |
| 3689 | `model.layers.11.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.90625 / 6.90625 / 0.041986823081970215 / 1.8126472125918374 | [NPY](tensors/0003689.npy) |
| 3690 | `model.layers.11.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.21875 / 5.21875 / -0.0005790097056888044 / 1.2626578241513908 | [NPY](tensors/0003690.npy) |
| 3691 | `model.layers.11.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 71.0 / 0.02547526094648573 / 3.966131861280471 | [NPY](tensors/0003691.npy) |
| 3692 | `model.layers.11.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 71.0 / 0.02547526094648573 / 3.966131861280471 | [NPY](tensors/0003692.npy) |
| 3693 | `model.layers.11.self_attn` | 31 | `output[1]` | [1, 64, 1, 328] | torch.bfloat16 → float32 | 2.7625901566352695e-11 / 0.875 / 0.0028925812413753745 / 0.011416881129901064 | [NPY](tensors/0003693.npy) |
| 3694 | `model.layers.11.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -268.0 / 360.0 / 0.2778548346625434 / 15.479694936731475 | [NPY](tensors/0003694.npy) |
| 3695 | `model.layers.11.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.828125 / 4.625 / -0.0013958228958977593 / 0.6025011622129942 | [NPY](tensors/0003695.npy) |
| 3696 | `model.layers.11.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.828125 / 4.625 / -0.0013958228958977593 / 0.6025011622129942 | [NPY](tensors/0003696.npy) |
| 3697 | `model.layers.11.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.828125 / 4.625 / -0.0013958228958977593 / 0.6025011622129942 | [NPY](tensors/0003697.npy) |
| 3698 | `model.layers.11.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3699 | `model.layers.11.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3700 | `model.layers.11.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3701 | `model.layers.11.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -93.5 / 50.0 / 0.04733340607749091 / 3.6477711580366274 | [NPY](tensors/0003701.npy) |
| 3702 | `model.layers.11.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 50.0 / 0.04733340607749091 / 3.6477711580366274 | [NPY](tensors/0003702.npy) |
| 3703 | `model.layers.11.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.703125 / 0.66796875 / -0.12122154235839844 / 0.47088832529888225 | [NPY](tensors/0003703.npy) |
| 3704 | `model.layers.11` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -362.0 / 410.0 / 0.3241290622287326 / 17.2305252796192 | [NPY](tensors/0003704.npy) |
| 3783 | `model.layers.11` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -368.0 / 544.0 / 0.7586678398980035 / 22.10542855866534 | [NPY](tensors/0003783.npy) |
| 3784 | `model.layers.11` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003784.npy) |
| 3785 | `model.layers.11` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0003785.npy) |
| 3786 | `model.layers.11` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0003786.npy) |
| 3787 | `model.layers.11` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0003787.npy) |
| 3788 | `model.layers.11` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3789 | `model.layers.11` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3790 | `model.layers.11` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3791 | `model.layers.11.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -368.0 / 544.0 / 0.7586678398980035 / 22.10542855866534 | [NPY](tensors/0003791.npy) |
| 3792 | `model.layers.11.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 115.5 / 0.08789717356363932 / 3.256816918758209 | [NPY](tensors/0003792.npy) |
| 3793 | `model.layers.11.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 115.5 / 0.08789717356363932 / 3.256816918758209 | [NPY](tensors/0003793.npy) |
| 3794 | `model.layers.11.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003794.npy) |
| 3795 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0003795.npy) |
| 3796 | `model.layers.11.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3797 | `model.layers.11.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3798 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0003798.npy) |
| 3799 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0003799.npy) |
| 3800 | `model.layers.11.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3801 | `model.layers.11.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 115.5 / 0.08789717356363932 / 3.256816918758209 | [NPY](tensors/0003801.npy) |
| 3802 | `model.layers.11.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 9.4375 / 0.042499365750700235 / 1.311209111534629 | [NPY](tensors/0003802.npy) |
| 3803 | `model.layers.11.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 115.5 / 0.08789717356363932 / 3.256816918758209 | [NPY](tensors/0003803.npy) |
| 3804 | `model.layers.11.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.25 / 33.5 / 0.04518023133277893 / 3.6506820944896825 | [NPY](tensors/0003804.npy) |
| 3805 | `model.layers.11.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 115.5 / 0.08789717356363932 / 3.256816918758209 | [NPY](tensors/0003805.npy) |
| 3806 | `model.layers.11.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.125 / 10.125 / -0.033216810785233974 / 2.421102873801967 | [NPY](tensors/0003806.npy) |
| 3807 | `model.layers.11.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.65625 / 5.9375 / 0.0041148304007947445 / 1.3093470273366195 | [NPY](tensors/0003807.npy) |
| 3808 | `model.layers.11.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -185.0 / 183.0 / -0.051719486713409424 / 5.951579729454852 | [NPY](tensors/0003808.npy) |
| 3809 | `model.layers.11.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -185.0 / 183.0 / -0.051719486713409424 / 5.951579729454852 | [NPY](tensors/0003809.npy) |
| 3810 | `model.layers.11.self_attn` | 32 | `output[1]` | [1, 64, 1, 329] | torch.bfloat16 → float32 | 7.673861546209082e-12 / 0.91015625 / 0.0026385696894879376 / 0.011935267959504474 | [NPY](tensors/0003810.npy) |
| 3811 | `model.layers.11.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -185.0 / 360.0 / 0.7088416205512152 / 19.874917769190798 | [NPY](tensors/0003811.npy) |
| 3812 | `model.layers.11.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.1875 / 5.3125 / 0.018592230478922524 / 0.7258594334954318 | [NPY](tensors/0003812.npy) |
| 3813 | `model.layers.11.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.1875 / 5.3125 / 0.018592230478922524 / 0.7258594334954318 | [NPY](tensors/0003813.npy) |
| 3814 | `model.layers.11.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.1875 / 5.3125 / 0.018592230478922524 / 0.7258594334954318 | [NPY](tensors/0003814.npy) |
| 3815 | `model.layers.11.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3816 | `model.layers.11.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3817 | `model.layers.11.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3818 | `model.layers.11.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -241.0 / 274.0 / 0.34599541558159724 / 9.345250178645193 | [NPY](tensors/0003818.npy) |
| 3819 | `model.layers.11.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -241.0 / 274.0 / 0.34599541558159724 / 9.345250178645193 | [NPY](tensors/0003819.npy) |
| 3820 | `model.layers.11.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.3125 / 1.8984375 / -0.1873922348022461 / 0.9509044546730203 | [NPY](tensors/0003820.npy) |
| 3821 | `model.layers.11` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -426.0 / 632.0 / 1.0543460422092015 / 26.063941929838045 | [NPY](tensors/0003821.npy) |
| 3900 | `model.layers.11` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -344.0 / 462.0 / 0.6467515733506944 / 19.289386812157176 | [NPY](tensors/0003900.npy) |
| 3901 | `model.layers.11` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 330] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003901.npy) |
| 3902 | `model.layers.11` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0003902.npy) |
| 3903 | `model.layers.11` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0003903.npy) |
| 3904 | `model.layers.11` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0003904.npy) |
| 3905 | `model.layers.11` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3906 | `model.layers.11` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3907 | `model.layers.11` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3908 | `model.layers.11.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -344.0 / 462.0 / 0.6467515733506944 / 19.289386812157176 | [NPY](tensors/0003908.npy) |
| 3909 | `model.layers.11.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 112.0 / 0.0863814910252889 / 3.3755480478367526 | [NPY](tensors/0003909.npy) |
| 3910 | `model.layers.11.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 112.0 / 0.0863814910252889 / 3.3755480478367526 | [NPY](tensors/0003910.npy) |
| 3911 | `model.layers.11.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 330] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003911.npy) |
| 3912 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0003912.npy) |
| 3913 | `model.layers.11.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3914 | `model.layers.11.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3915 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0003915.npy) |
| 3916 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0003916.npy) |
| 3917 | `model.layers.11.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3918 | `model.layers.11.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 112.0 / 0.0863814910252889 / 3.3755480478367526 | [NPY](tensors/0003918.npy) |
| 3919 | `model.layers.11.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.75 / 8.25 / 0.02480583218857646 / 1.2240790963014028 | [NPY](tensors/0003919.npy) |
| 3920 | `model.layers.11.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 112.0 / 0.0863814910252889 / 3.3755480478367526 | [NPY](tensors/0003920.npy) |
| 3921 | `model.layers.11.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.875 / 37.5 / 0.09938013553619385 / 3.646722597070892 | [NPY](tensors/0003921.npy) |
| 3922 | `model.layers.11.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.5 / 112.0 / 0.0863814910252889 / 3.3755480478367526 | [NPY](tensors/0003922.npy) |
| 3923 | `model.layers.11.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.6875 / 5.84375 / 0.008935272693634033 / 1.7933286247897904 | [NPY](tensors/0003923.npy) |
| 3924 | `model.layers.11.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.28125 / 6.125 / 0.0061080073937773705 / 1.3284418595896494 | [NPY](tensors/0003924.npy) |
| 3925 | `model.layers.11.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -137.0 / 149.0 / -0.04168053997887505 / 5.017641137620022 | [NPY](tensors/0003925.npy) |
| 3926 | `model.layers.11.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -137.0 / 149.0 / -0.04168053997887505 / 5.017641137620022 | [NPY](tensors/0003926.npy) |
| 3927 | `model.layers.11.self_attn` | 33 | `output[1]` | [1, 64, 1, 330] | torch.bfloat16 → float32 | 7.685230229981244e-11 / 0.9609375 / 0.002778659006780924 / 0.011616513560520573 | [NPY](tensors/0003927.npy) |
| 3928 | `model.layers.11.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -195.0 / 334.0 / 0.6043109469943576 / 17.83843722799735 | [NPY](tensors/0003928.npy) |
| 3929 | `model.layers.11.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.28125 / 4.15625 / 0.020720880561404757 / 0.70946297615614 | [NPY](tensors/0003929.npy) |
| 3930 | `model.layers.11.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.28125 / 4.15625 / 0.020720880561404757 / 0.70946297615614 | [NPY](tensors/0003930.npy) |
| 3931 | `model.layers.11.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.28125 / 4.15625 / 0.020720880561404757 / 0.70946297615614 | [NPY](tensors/0003931.npy) |
| 3932 | `model.layers.11.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3933 | `model.layers.11.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3934 | `model.layers.11.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3935 | `model.layers.11.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -208.0 / 165.0 / 0.08314163637244039 / 7.441992201572574 | [NPY](tensors/0003935.npy) |
| 3936 | `model.layers.11.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -208.0 / 165.0 / 0.08314163637244039 / 7.441992201572574 | [NPY](tensors/0003936.npy) |
| 3937 | `model.layers.11.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.046875 / 1.4453125 / -0.14296913146972656 / 0.783490437383169 | [NPY](tensors/0003937.npy) |
| 3938 | `model.layers.11` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -404.0 / 488.0 / 0.6861636691623264 / 22.460861426272537 | [NPY](tensors/0003938.npy) |
| 4017 | `model.layers.11` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -386.0 / 524.0 / 0.721610344780816 / 21.601482352910228 | [NPY](tensors/0004017.npy) |
| 4018 | `model.layers.11` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 331] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004018.npy) |
| 4019 | `model.layers.11` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0004019.npy) |
| 4020 | `model.layers.11` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0004020.npy) |
| 4021 | `model.layers.11` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0004021.npy) |
| 4022 | `model.layers.11` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4023 | `model.layers.11` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4024 | `model.layers.11` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4025 | `model.layers.11.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -386.0 / 524.0 / 0.721610344780816 / 21.601482352910228 | [NPY](tensors/0004025.npy) |
| 4026 | `model.layers.11.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 113.5 / 0.08248649173312717 / 3.327427951516922 | [NPY](tensors/0004026.npy) |
| 4027 | `model.layers.11.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 113.5 / 0.08248649173312717 / 3.327427951516922 | [NPY](tensors/0004027.npy) |
| 4028 | `model.layers.11.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 331] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004028.npy) |
| 4029 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0004029.npy) |
| 4030 | `model.layers.11.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4031 | `model.layers.11.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4032 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0004032.npy) |
| 4033 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0004033.npy) |
| 4034 | `model.layers.11.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4035 | `model.layers.11.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 113.5 / 0.08248649173312717 / 3.327427951516922 | [NPY](tensors/0004035.npy) |
| 4036 | `model.layers.11.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5 / 7.4375 / 0.04445988265797496 / 1.2371553624281706 | [NPY](tensors/0004036.npy) |
| 4037 | `model.layers.11.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 113.5 / 0.08248649173312717 / 3.327427951516922 | [NPY](tensors/0004037.npy) |
| 4038 | `model.layers.11.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.75 / 39.75 / 0.05303725600242615 / 3.8652228261019195 | [NPY](tensors/0004038.npy) |
| 4039 | `model.layers.11.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -94.0 / 113.5 / 0.08248649173312717 / 3.327427951516922 | [NPY](tensors/0004039.npy) |
| 4040 | `model.layers.11.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.0 / 10.0625 / 0.05862017720937729 / 2.32222621083129 | [NPY](tensors/0004040.npy) |
| 4041 | `model.layers.11.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 6.71875 / -0.0068390919477678835 / 1.376333398097215 | [NPY](tensors/0004041.npy) |
| 4042 | `model.layers.11.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -144.0 / 153.0 / -0.08326655758751764 / 5.427449825127218 | [NPY](tensors/0004042.npy) |
| 4043 | `model.layers.11.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -144.0 / 153.0 / -0.08326655758751764 / 5.427449825127218 | [NPY](tensors/0004043.npy) |
| 4044 | `model.layers.11.self_attn` | 34 | `output[1]` | [1, 64, 1, 331] | torch.bfloat16 → float32 | 2.7398527890909463e-11 / 0.93359375 / 0.002716409932192179 / 0.014913798779601587 | [NPY](tensors/0004044.npy) |
| 4045 | `model.layers.11.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -233.0 / 380.0 / 0.6387366400824652 / 20.211678754260074 | [NPY](tensors/0004045.npy) |
| 4046 | `model.layers.11.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.03125 / 3.328125 / 0.026629212167527942 / 0.7633925653993656 | [NPY](tensors/0004046.npy) |
| 4047 | `model.layers.11.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.03125 / 3.328125 / 0.026629212167527942 / 0.7633925653993656 | [NPY](tensors/0004047.npy) |
| 4048 | `model.layers.11.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.03125 / 3.328125 / 0.026629212167527942 / 0.7633925653993656 | [NPY](tensors/0004048.npy) |
| 4049 | `model.layers.11.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4050 | `model.layers.11.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4051 | `model.layers.11.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4052 | `model.layers.11.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -236.0 / 234.0 / 0.03798081345028347 / 8.856288326911594 | [NPY](tensors/0004052.npy) |
| 4053 | `model.layers.11.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -236.0 / 234.0 / 0.03798081345028347 / 8.856288326911594 | [NPY](tensors/0004053.npy) |
| 4054 | `model.layers.11.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.71875 / 1.53125 / -0.15268898010253906 / 0.9501545732436756 | [NPY](tensors/0004054.npy) |
| 4055 | `model.layers.11` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -468.0 / 616.0 / 0.6775390625 / 25.650297520661855 | [NPY](tensors/0004055.npy) |
| 4134 | `model.layers.11` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -336.0 / 548.0 / 0.37629597981770835 / 19.98749972664689 | [NPY](tensors/0004134.npy) |
| 4135 | `model.layers.11` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 332] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004135.npy) |
| 4136 | `model.layers.11` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0004136.npy) |
| 4137 | `model.layers.11` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0004137.npy) |
| 4138 | `model.layers.11` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0004138.npy) |
| 4139 | `model.layers.11` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4140 | `model.layers.11` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4141 | `model.layers.11` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4142 | `model.layers.11.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -336.0 / 548.0 / 0.37629597981770835 / 19.98749972664689 | [NPY](tensors/0004142.npy) |
| 4143 | `model.layers.11.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 128.0 / 0.054997295803493926 / 3.4133104163133337 | [NPY](tensors/0004143.npy) |
| 4144 | `model.layers.11.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 128.0 / 0.054997295803493926 / 3.4133104163133337 | [NPY](tensors/0004144.npy) |
| 4145 | `model.layers.11.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 332] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004145.npy) |
| 4146 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0004146.npy) |
| 4147 | `model.layers.11.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4148 | `model.layers.11.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4149 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0004149.npy) |
| 4150 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0004150.npy) |
| 4151 | `model.layers.11.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4152 | `model.layers.11.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 128.0 / 0.054997295803493926 / 3.4133104163133337 | [NPY](tensors/0004152.npy) |
| 4153 | `model.layers.11.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.375 / 9.5 / 0.04453606065362692 / 1.2941230765311458 | [NPY](tensors/0004153.npy) |
| 4154 | `model.layers.11.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 128.0 / 0.054997295803493926 / 3.4133104163133337 | [NPY](tensors/0004154.npy) |
| 4155 | `model.layers.11.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -26.0 / 32.5 / 0.042353685945272446 / 3.5771987165997157 | [NPY](tensors/0004155.npy) |
| 4156 | `model.layers.11.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.0 / 128.0 / 0.054997295803493926 / 3.4133104163133337 | [NPY](tensors/0004156.npy) |
| 4157 | `model.layers.11.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.5625 / 7.59375 / 0.1016708854585886 / 2.3116122634649416 | [NPY](tensors/0004157.npy) |
| 4158 | `model.layers.11.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.5625 / 7.375 / 0.01103944331407547 / 1.4918003436614877 | [NPY](tensors/0004158.npy) |
| 4159 | `model.layers.11.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -136.0 / 134.0 / -0.0991863383187188 / 5.240035880796844 | [NPY](tensors/0004159.npy) |
| 4160 | `model.layers.11.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -136.0 / 134.0 / -0.0991863383187188 / 5.240035880796844 | [NPY](tensors/0004160.npy) |
| 4161 | `model.layers.11.self_attn` | 35 | `output[1]` | [1, 64, 1, 332] | torch.bfloat16 → float32 | 1.3415046851150692e-11 / 0.96875 / 0.0028965998063464346 / 0.01456727306568081 | [NPY](tensors/0004161.npy) |
| 4162 | `model.layers.11.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -202.0 / 412.0 / 0.2780758327907986 / 18.852035335896378 | [NPY](tensors/0004162.npy) |
| 4163 | `model.layers.11.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.5 / 2.921875 / 0.0012369182374742296 / 0.7299594923180303 | [NPY](tensors/0004163.npy) |
| 4164 | `model.layers.11.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.5 / 2.921875 / 0.0012369182374742296 / 0.7299594923180303 | [NPY](tensors/0004164.npy) |
| 4165 | `model.layers.11.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.5 / 2.921875 / 0.0012369182374742296 / 0.7299594923180303 | [NPY](tensors/0004165.npy) |
| 4166 | `model.layers.11.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4167 | `model.layers.11.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4168 | `model.layers.11.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4169 | `model.layers.11.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -154.0 / 168.0 / 0.032805808385213214 / 7.207142534825538 | [NPY](tensors/0004169.npy) |
| 4170 | `model.layers.11.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -154.0 / 168.0 / 0.032805808385213214 / 7.207142534825538 | [NPY](tensors/0004170.npy) |
| 4171 | `model.layers.11.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.171875 / 1.203125 / -0.15026569366455078 / 0.6431761637634841 | [NPY](tensors/0004171.npy) |
| 4172 | `model.layers.11` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -356.0 / 580.0 / 0.3118167453342014 / 23.320188664027846 | [NPY](tensors/0004172.npy) |
| 4251 | `model.layers.11` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -324.0 / 468.0 / 0.33527713351779515 / 19.8721147252265 | [NPY](tensors/0004251.npy) |
| 4252 | `model.layers.11` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 333] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004252.npy) |
| 4253 | `model.layers.11` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0004253.npy) |
| 4254 | `model.layers.11` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0004254.npy) |
| 4255 | `model.layers.11` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0004255.npy) |
| 4256 | `model.layers.11` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4257 | `model.layers.11` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4258 | `model.layers.11` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4259 | `model.layers.11.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -324.0 / 468.0 / 0.33527713351779515 / 19.8721147252265 | [NPY](tensors/0004259.npy) |
| 4260 | `model.layers.11.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 110.5 / 0.05127765072716607 / 3.2146959483678508 | [NPY](tensors/0004260.npy) |
| 4261 | `model.layers.11.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 110.5 / 0.05127765072716607 / 3.2146959483678508 | [NPY](tensors/0004261.npy) |
| 4262 | `model.layers.11.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 333] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004262.npy) |
| 4263 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0004263.npy) |
| 4264 | `model.layers.11.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4265 | `model.layers.11.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4266 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0004266.npy) |
| 4267 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0004267.npy) |
| 4268 | `model.layers.11.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4269 | `model.layers.11.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 110.5 / 0.05127765072716607 / 3.2146959483678508 | [NPY](tensors/0004269.npy) |
| 4270 | `model.layers.11.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.625 / 9.0 / 0.04575854039285332 / 1.2843806083454554 | [NPY](tensors/0004270.npy) |
| 4271 | `model.layers.11.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 110.5 / 0.05127765072716607 / 3.2146959483678508 | [NPY](tensors/0004271.npy) |
| 4272 | `model.layers.11.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -24.0 / 31.25 / 0.06335054337978363 / 3.418570857816087 | [NPY](tensors/0004272.npy) |
| 4273 | `model.layers.11.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 110.5 / 0.05127765072716607 / 3.2146959483678508 | [NPY](tensors/0004273.npy) |
| 4274 | `model.layers.11.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.3125 / 7.84375 / 0.0018655061721801758 / 2.3536175024079604 | [NPY](tensors/0004274.npy) |
| 4275 | `model.layers.11.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.9375 / 6.96875 / 0.006445954495575279 / 1.3913383888323236 | [NPY](tensors/0004275.npy) |
| 4276 | `model.layers.11.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -158.0 / 128.0 / -0.13550544844733345 / 5.329581002248649 | [NPY](tensors/0004276.npy) |
| 4277 | `model.layers.11.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -158.0 / 128.0 / -0.13550544844733345 / 5.329581002248649 | [NPY](tensors/0004277.npy) |
| 4278 | `model.layers.11.self_attn` | 36 | `output[1]` | [1, 64, 1, 333] | torch.bfloat16 → float32 | 7.901235221652314e-12 / 0.94140625 / 0.002896462410986286 / 0.013543469661880152 | [NPY](tensors/0004278.npy) |
| 4279 | `model.layers.11.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -196.0 / 310.0 / 0.20020497639973958 / 18.415088589248327 | [NPY](tensors/0004279.npy) |
| 4280 | `model.layers.11.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.75 / 2.984375 / -0.006327372127109104 / 0.7582683371177255 | [NPY](tensors/0004280.npy) |
| 4281 | `model.layers.11.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.75 / 2.984375 / -0.006327372127109104 / 0.7582683371177255 | [NPY](tensors/0004281.npy) |
| 4282 | `model.layers.11.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.75 / 2.984375 / -0.006327372127109104 / 0.7582683371177255 | [NPY](tensors/0004282.npy) |
| 4283 | `model.layers.11.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4284 | `model.layers.11.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4285 | `model.layers.11.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4286 | `model.layers.11.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -149.0 / 210.0 / 0.15305042266845703 / 7.817630141519954 | [NPY](tensors/0004286.npy) |
| 4287 | `model.layers.11.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -149.0 / 210.0 / 0.15305042266845703 / 7.817630141519954 | [NPY](tensors/0004287.npy) |
| 4288 | `model.layers.11.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.25 / 1.3203125 / -0.18550872802734375 / 0.7753704801324985 | [NPY](tensors/0004288.npy) |
| 4289 | `model.layers.11` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -344.0 / 490.0 / 0.3537689208984375 / 23.335771832906648 | [NPY](tensors/0004289.npy) |
| 4368 | `model.layers.11` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -364.0 / 436.0 / 0.3174997965494792 / 17.54489946741679 | [NPY](tensors/0004368.npy) |
| 4369 | `model.layers.11` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 334] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004369.npy) |
| 4370 | `model.layers.11` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0004370.npy) |
| 4371 | `model.layers.11` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0004371.npy) |
| 4372 | `model.layers.11` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0004372.npy) |
| 4373 | `model.layers.11` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4374 | `model.layers.11` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4375 | `model.layers.11` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4376 | `model.layers.11.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -364.0 / 436.0 / 0.3174997965494792 / 17.54489946741679 | [NPY](tensors/0004376.npy) |
| 4377 | `model.layers.11.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 100.5 / 0.04871267941262987 / 3.39176201673947 | [NPY](tensors/0004377.npy) |
| 4378 | `model.layers.11.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 100.5 / 0.04871267941262987 / 3.39176201673947 | [NPY](tensors/0004378.npy) |
| 4379 | `model.layers.11.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 334] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004379.npy) |
| 4380 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0004380.npy) |
| 4381 | `model.layers.11.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4382 | `model.layers.11.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4383 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0004383.npy) |
| 4384 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0004384.npy) |
| 4385 | `model.layers.11.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4386 | `model.layers.11.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 100.5 / 0.04871267941262987 / 3.39176201673947 | [NPY](tensors/0004386.npy) |
| 4387 | `model.layers.11.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.6875 / 7.8125 / 0.02858235128223896 / 1.225760014097248 | [NPY](tensors/0004387.npy) |
| 4388 | `model.layers.11.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 100.5 / 0.04871267941262987 / 3.39176201673947 | [NPY](tensors/0004388.npy) |
| 4389 | `model.layers.11.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.5 / 34.75 / 0.13531605899333954 / 3.5061906232237106 | [NPY](tensors/0004389.npy) |
| 4390 | `model.layers.11.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 100.5 / 0.04871267941262987 / 3.39176201673947 | [NPY](tensors/0004390.npy) |
| 4391 | `model.layers.11.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.3125 / 7.09375 / 0.04240018129348755 / 1.7978720338215044 | [NPY](tensors/0004391.npy) |
| 4392 | `model.layers.11.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.46875 / 5.625 / 0.002909756265580654 / 1.1758319795595256 | [NPY](tensors/0004392.npy) |
| 4393 | `model.layers.11.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -116.0 / 118.0 / -0.025757371054755316 / 4.5252792983638255 | [NPY](tensors/0004393.npy) |
| 4394 | `model.layers.11.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -116.0 / 118.0 / -0.025757371054755316 / 4.5252792983638255 | [NPY](tensors/0004394.npy) |
| 4395 | `model.layers.11.self_attn` | 37 | `output[1]` | [1, 64, 1, 334] | torch.bfloat16 → float32 | 3.979039320256561e-11 / 0.93359375 / 0.0028582087151062564 / 0.011347983372836228 | [NPY](tensors/0004395.npy) |
| 4396 | `model.layers.11.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -246.0 / 390.0 / 0.29115871853298614 / 16.238890550244836 | [NPY](tensors/0004396.npy) |
| 4397 | `model.layers.11.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.515625 / 5.0 / -0.005599382850858901 / 0.7027414632402776 | [NPY](tensors/0004397.npy) |
| 4398 | `model.layers.11.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.515625 / 5.0 / -0.005599382850858901 / 0.7027414632402776 | [NPY](tensors/0004398.npy) |
| 4399 | `model.layers.11.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.515625 / 5.0 / -0.005599382850858901 / 0.7027414632402776 | [NPY](tensors/0004399.npy) |
| 4400 | `model.layers.11.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4401 | `model.layers.11.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4402 | `model.layers.11.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4403 | `model.layers.11.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -184.0 / 174.0 / 0.14849047131008572 / 7.213535056206608 | [NPY](tensors/0004403.npy) |
| 4404 | `model.layers.11.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -184.0 / 174.0 / 0.14849047131008572 / 7.213535056206608 | [NPY](tensors/0004404.npy) |
| 4405 | `model.layers.11.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.3125 / 0.92578125 / -0.16523170471191406 / 0.6385402203089032 | [NPY](tensors/0004405.npy) |
| 4406 | `model.layers.11` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -430.0 / 506.0 / 0.43956739637586806 / 21.384908356624663 | [NPY](tensors/0004406.npy) |
| 4485 | `model.layers.11` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -268.0 / 422.0 / 0.05990464952256944 / 18.599322607542877 | [NPY](tensors/0004485.npy) |
| 4486 | `model.layers.11` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 335] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004486.npy) |
| 4487 | `model.layers.11` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0004487.npy) |
| 4488 | `model.layers.11` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0004488.npy) |
| 4489 | `model.layers.11` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0004489.npy) |
| 4490 | `model.layers.11` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4491 | `model.layers.11` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4492 | `model.layers.11` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4493 | `model.layers.11.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -268.0 / 422.0 / 0.05990464952256944 / 18.599322607542877 | [NPY](tensors/0004493.npy) |
| 4494 | `model.layers.11.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 106.5 / 0.026466830571492513 / 3.130095744396421 | [NPY](tensors/0004494.npy) |
| 4495 | `model.layers.11.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 106.5 / 0.026466830571492513 / 3.130095744396421 | [NPY](tensors/0004495.npy) |
| 4496 | `model.layers.11.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 335] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004496.npy) |
| 4497 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0004497.npy) |
| 4498 | `model.layers.11.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4499 | `model.layers.11.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4500 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0004500.npy) |
| 4501 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0004501.npy) |
| 4502 | `model.layers.11.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4503 | `model.layers.11.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 106.5 / 0.026466830571492513 / 3.130095744396421 | [NPY](tensors/0004503.npy) |
| 4504 | `model.layers.11.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 9.4375 / 0.03762976513826288 / 1.3379142793181227 | [NPY](tensors/0004504.npy) |
| 4505 | `model.layers.11.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 106.5 / 0.026466830571492513 / 3.130095744396421 | [NPY](tensors/0004505.npy) |
| 4506 | `model.layers.11.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.875 / 31.875 / 0.13694562460295856 / 3.627783616814077 | [NPY](tensors/0004506.npy) |
| 4507 | `model.layers.11.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 106.5 / 0.026466830571492513 / 3.130095744396421 | [NPY](tensors/0004507.npy) |
| 4508 | `model.layers.11.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.5 / 7.59375 / 0.013832569122314453 / 2.31696851819682 | [NPY](tensors/0004508.npy) |
| 4509 | `model.layers.11.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.625 / 6.09375 / -0.013640289893373847 / 1.4042564672379945 | [NPY](tensors/0004509.npy) |
| 4510 | `model.layers.11.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.5 / 61.25 / -0.08328424162334866 / 4.257493707173653 | [NPY](tensors/0004510.npy) |
| 4511 | `model.layers.11.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -105.5 / 61.25 / -0.08328424162334866 / 4.257493707173653 | [NPY](tensors/0004511.npy) |
| 4512 | `model.layers.11.self_attn` | 38 | `output[1]` | [1, 64, 1, 335] | torch.bfloat16 → float32 | 5.661604518536478e-11 / 0.91015625 / 0.0028959801836013896 / 0.013810610655869292 | [NPY](tensors/0004512.npy) |
| 4513 | `model.layers.11.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -207.0 / 316.0 / -0.024250708685980903 / 17.82530843760279 | [NPY](tensors/0004513.npy) |
| 4514 | `model.layers.11.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.296875 / 3.53125 / -0.0187307337919871 / 0.7550160739514321 | [NPY](tensors/0004514.npy) |
| 4515 | `model.layers.11.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.296875 / 3.53125 / -0.0187307337919871 / 0.7550160739514321 | [NPY](tensors/0004515.npy) |
| 4516 | `model.layers.11.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.296875 / 3.53125 / -0.0187307337919871 / 0.7550160739514321 | [NPY](tensors/0004516.npy) |
| 4517 | `model.layers.11.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4518 | `model.layers.11.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4519 | `model.layers.11.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4520 | `model.layers.11.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -107.5 / 173.0 / 0.11030802070680591 / 6.240144578391975 | [NPY](tensors/0004520.npy) |
| 4521 | `model.layers.11.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -107.5 / 173.0 / 0.11030802070680591 / 6.240144578391975 | [NPY](tensors/0004521.npy) |
| 4522 | `model.layers.11.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.5 / 1.296875 / -0.19394683837890625 / 0.7892539922047235 | [NPY](tensors/0004522.npy) |
| 4523 | `model.layers.11` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -314.0 / 432.0 / 0.0870285881890191 / 21.320396858325083 | [NPY](tensors/0004523.npy) |
| 4602 | `model.layers.11` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -119.0 / 264.0 / 0.7070790608723958 / 14.566859290138435 | [NPY](tensors/0004602.npy) |
| 4603 | `model.layers.11` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 336] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004603.npy) |
| 4604 | `model.layers.11` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0004604.npy) |
| 4605 | `model.layers.11` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0004605.npy) |
| 4606 | `model.layers.11` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0004606.npy) |
| 4607 | `model.layers.11` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4608 | `model.layers.11` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4609 | `model.layers.11` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4610 | `model.layers.11.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -119.0 / 264.0 / 0.7070790608723958 / 14.566859290138435 | [NPY](tensors/0004610.npy) |
| 4611 | `model.layers.11.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.75 / 85.0 / 0.11891156832377116 / 2.652171275417953 | [NPY](tensors/0004611.npy) |
| 4612 | `model.layers.11.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.75 / 85.0 / 0.11891156832377116 / 2.652171275417953 | [NPY](tensors/0004612.npy) |
| 4613 | `model.layers.11.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 336] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004613.npy) |
| 4614 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0004614.npy) |
| 4615 | `model.layers.11.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4616 | `model.layers.11.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4617 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0004617.npy) |
| 4618 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0004618.npy) |
| 4619 | `model.layers.11.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4620 | `model.layers.11.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.75 / 85.0 / 0.11891156832377116 / 2.652171275417953 | [NPY](tensors/0004620.npy) |
| 4621 | `model.layers.11.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.625 / 10.125 / 0.04233212466351688 / 1.3705158971153693 | [NPY](tensors/0004621.npy) |
| 4622 | `model.layers.11.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.75 / 85.0 / 0.11891156832377116 / 2.652171275417953 | [NPY](tensors/0004622.npy) |
| 4623 | `model.layers.11.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 40.0 / 0.17001153528690338 / 4.233468749024988 | [NPY](tensors/0004623.npy) |
| 4624 | `model.layers.11.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.75 / 85.0 / 0.11891156832377116 / 2.652171275417953 | [NPY](tensors/0004624.npy) |
| 4625 | `model.layers.11.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.96875 / 10.1875 / 0.08589625358581543 / 2.5183207493878506 | [NPY](tensors/0004625.npy) |
| 4626 | `model.layers.11.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.6875 / 5.625 / 0.009320304729044437 / 1.373320025897212 | [NPY](tensors/0004626.npy) |
| 4627 | `model.layers.11.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.25 / 53.25 / 0.07012764712174734 / 3.453874563599232 | [NPY](tensors/0004627.npy) |
| 4628 | `model.layers.11.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.25 / 53.25 / 0.07012764712174734 / 3.453874563599232 | [NPY](tensors/0004628.npy) |
| 4629 | `model.layers.11.self_attn` | 39 | `output[1]` | [1, 64, 1, 336] | torch.bfloat16 → float32 | 3.7471181713044643e-10 / 0.73828125 / 0.0028027878055724947 / 0.01056864944117721 | [NPY](tensors/0004629.npy) |
| 4630 | `model.layers.11.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -135.0 / 302.0 / 0.7770902845594618 / 16.252383829021422 | [NPY](tensors/0004630.npy) |
| 4631 | `model.layers.11.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.484375 / 3.578125 / 0.024712860584259033 / 0.722307961706156 | [NPY](tensors/0004631.npy) |
| 4632 | `model.layers.11.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.484375 / 3.578125 / 0.024712860584259033 / 0.722307961706156 | [NPY](tensors/0004632.npy) |
| 4633 | `model.layers.11.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.484375 / 3.578125 / 0.024712860584259033 / 0.722307961706156 | [NPY](tensors/0004633.npy) |
| 4634 | `model.layers.11.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4635 | `model.layers.11.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4636 | `model.layers.11.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4637 | `model.layers.11.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -169.0 / 168.0 / 0.15833395851982965 / 7.040139279957873 | [NPY](tensors/0004637.npy) |
| 4638 | `model.layers.11.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -169.0 / 168.0 / 0.15833395851982965 / 7.040139279957873 | [NPY](tensors/0004638.npy) |
| 4639 | `model.layers.11.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8671875 / 1.65625 / -0.1091766357421875 / 0.6885535107554024 | [NPY](tensors/0004639.npy) |
| 4640 | `model.layers.11` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -304.0 / 470.0 / 0.9354604085286459 / 20.360753850557135 | [NPY](tensors/0004640.npy) |
| 4719 | `model.layers.11` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -280.0 / 418.0 / 0.37443949381510416 / 18.330383585425654 | [NPY](tensors/0004719.npy) |
| 4720 | `model.layers.11` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 337] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004720.npy) |
| 4721 | `model.layers.11` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0004721.npy) |
| 4722 | `model.layers.11` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0004722.npy) |
| 4723 | `model.layers.11` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0004723.npy) |
| 4724 | `model.layers.11` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4725 | `model.layers.11` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4726 | `model.layers.11` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4727 | `model.layers.11.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -280.0 / 418.0 / 0.37443949381510416 / 18.330383585425654 | [NPY](tensors/0004727.npy) |
| 4728 | `model.layers.11.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 99.0 / 0.04941788779364692 / 3.093623018375775 | [NPY](tensors/0004728.npy) |
| 4729 | `model.layers.11.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 99.0 / 0.04941788779364692 / 3.093623018375775 | [NPY](tensors/0004729.npy) |
| 4730 | `model.layers.11.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 337] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004730.npy) |
| 4731 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0004731.npy) |
| 4732 | `model.layers.11.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4733 | `model.layers.11.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4734 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0004734.npy) |
| 4735 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0004735.npy) |
| 4736 | `model.layers.11.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4737 | `model.layers.11.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 99.0 / 0.04941788779364692 / 3.093623018375775 | [NPY](tensors/0004737.npy) |
| 4738 | `model.layers.11.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.53125 / 9.375 / 0.06401289533823729 / 1.2959210040436575 | [NPY](tensors/0004738.npy) |
| 4739 | `model.layers.11.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 99.0 / 0.04941788779364692 / 3.093623018375775 | [NPY](tensors/0004739.npy) |
| 4740 | `model.layers.11.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.0 / 42.0 / 0.2568548880517483 / 4.0846074096194736 | [NPY](tensors/0004740.npy) |
| 4741 | `model.layers.11.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 99.0 / 0.04941788779364692 / 3.093623018375775 | [NPY](tensors/0004741.npy) |
| 4742 | `model.layers.11.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.125 / 8.9375 / -0.012228965759277344 / 2.3798428858639586 | [NPY](tensors/0004742.npy) |
| 4743 | `model.layers.11.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.625 / 8.5 / -0.02676795981824398 / 1.4166189805306288 | [NPY](tensors/0004743.npy) |
| 4744 | `model.layers.11.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.0 / 67.5 / 0.01812828845447964 / 4.045170894292825 | [NPY](tensors/0004744.npy) |
| 4745 | `model.layers.11.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.0 / 67.5 / 0.01812828845447964 / 4.045170894292825 | [NPY](tensors/0004745.npy) |
| 4746 | `model.layers.11.self_attn` | 40 | `output[1]` | [1, 64, 1, 337] | torch.bfloat16 → float32 | 2.808064891723916e-11 / 0.95703125 / 0.0028416955657179976 / 0.014758445968621942 | [NPY](tensors/0004746.npy) |
| 4747 | `model.layers.11.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -212.0 / 396.0 / 0.3922857496473524 / 18.41162050384772 | [NPY](tensors/0004747.npy) |
| 4748 | `model.layers.11.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.890625 / 2.71875 / 0.001269951131608751 / 0.7202871195015795 | [NPY](tensors/0004748.npy) |
| 4749 | `model.layers.11.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.890625 / 2.71875 / 0.001269951131608751 / 0.7202871195015795 | [NPY](tensors/0004749.npy) |
| 4750 | `model.layers.11.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.890625 / 2.71875 / 0.001269951131608751 / 0.7202871195015795 | [NPY](tensors/0004750.npy) |
| 4751 | `model.layers.11.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4752 | `model.layers.11.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4753 | `model.layers.11.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4754 | `model.layers.11.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -137.0 / 134.0 / 0.13020088407728408 / 5.48573855939068 | [NPY](tensors/0004754.npy) |
| 4755 | `model.layers.11.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -137.0 / 134.0 / 0.13020088407728408 / 5.48573855939068 | [NPY](tensors/0004755.npy) |
| 4756 | `model.layers.11.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.171875 / 0.98828125 / -0.1583404541015625 / 0.5522535171397734 | [NPY](tensors/0004756.npy) |
| 4757 | `model.layers.11` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -348.0 / 466.0 / 0.5231638590494792 / 21.309583337012736 | [NPY](tensors/0004757.npy) |
| 4836 | `model.layers.11` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -274.0 / 470.0 / 0.3938346015082465 / 19.024026219913598 | [NPY](tensors/0004836.npy) |
| 4837 | `model.layers.11` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 338] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004837.npy) |
| 4838 | `model.layers.11` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0004838.npy) |
| 4839 | `model.layers.11` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0004839.npy) |
| 4840 | `model.layers.11` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0004840.npy) |
| 4841 | `model.layers.11` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4842 | `model.layers.11` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4843 | `model.layers.11` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4844 | `model.layers.11.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -274.0 / 470.0 / 0.3938346015082465 / 19.024026219913598 | [NPY](tensors/0004844.npy) |
| 4845 | `model.layers.11.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 116.0 / 0.05570643742879232 / 3.230950285692869 | [NPY](tensors/0004845.npy) |
| 4846 | `model.layers.11.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 116.0 / 0.05570643742879232 / 3.230950285692869 | [NPY](tensors/0004846.npy) |
| 4847 | `model.layers.11.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 338] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004847.npy) |
| 4848 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0004848.npy) |
| 4849 | `model.layers.11.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4850 | `model.layers.11.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4851 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0004851.npy) |
| 4852 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0004852.npy) |
| 4853 | `model.layers.11.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4854 | `model.layers.11.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 116.0 / 0.05570643742879232 / 3.230950285692869 | [NPY](tensors/0004854.npy) |
| 4855 | `model.layers.11.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5 / 8.8125 / 0.06526215904159471 / 1.2307705145149455 | [NPY](tensors/0004855.npy) |
| 4856 | `model.layers.11.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 116.0 / 0.05570643742879232 / 3.230950285692869 | [NPY](tensors/0004856.npy) |
| 4857 | `model.layers.11.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.5 / 43.0 / 0.20087351649999619 / 4.022518867114111 | [NPY](tensors/0004857.npy) |
| 4858 | `model.layers.11.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.5 / 116.0 / 0.05570643742879232 / 3.230950285692869 | [NPY](tensors/0004858.npy) |
| 4859 | `model.layers.11.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.375 / 6.65625 / -0.10375922918319702 / 2.3179708503921277 | [NPY](tensors/0004859.npy) |
| 4860 | `model.layers.11.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.46875 / 7.3125 / -0.022294335067272186 / 1.4859550032194098 | [NPY](tensors/0004860.npy) |
| 4861 | `model.layers.11.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -123.5 / 83.0 / 0.029010680649015637 / 4.595534275002751 | [NPY](tensors/0004861.npy) |
| 4862 | `model.layers.11.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -123.5 / 83.0 / 0.029010680649015637 / 4.595534275002751 | [NPY](tensors/0004862.npy) |
| 4863 | `model.layers.11.self_attn` | 41 | `output[1]` | [1, 64, 1, 338] | torch.bfloat16 → float32 | 2.0463630789890885e-11 / 0.97265625 / 0.0027126678102264413 / 0.0163244690518727 | [NPY](tensors/0004863.npy) |
| 4864 | `model.layers.11.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -195.0 / 346.0 / 0.4223475138346354 / 18.389295119325094 | [NPY](tensors/0004864.npy) |
| 4865 | `model.layers.11.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.5625 / 5.125 / 0.01443996164533827 / 0.7267087345412843 | [NPY](tensors/0004865.npy) |
| 4866 | `model.layers.11.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.5625 / 5.125 / 0.01443996164533827 / 0.7267087345412843 | [NPY](tensors/0004866.npy) |
| 4867 | `model.layers.11.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.5625 / 5.125 / 0.01443996164533827 / 0.7267087345412843 | [NPY](tensors/0004867.npy) |
| 4868 | `model.layers.11.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4869 | `model.layers.11.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4870 | `model.layers.11.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4871 | `model.layers.11.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -258.0 / 230.0 / 0.060698318481445315 / 8.875342800549605 | [NPY](tensors/0004871.npy) |
| 4872 | `model.layers.11.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -258.0 / 230.0 / 0.060698318481445315 / 8.875342800549605 | [NPY](tensors/0004872.npy) |
| 4873 | `model.layers.11.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.828125 / 1.1640625 / -0.14348602294921875 / 0.7627702015252563 | [NPY](tensors/0004873.npy) |
| 4874 | `model.layers.11` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -448.0 / 576.0 / 0.48394368489583334 / 24.12751762015172 | [NPY](tensors/0004874.npy) |
| 4953 | `model.layers.11` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -221.0 / 424.0 / 0.9934882269965277 / 18.724782799661085 | [NPY](tensors/0004953.npy) |
| 4954 | `model.layers.11` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 339] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004954.npy) |
| 4955 | `model.layers.11` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0004955.npy) |
| 4956 | `model.layers.11` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0004956.npy) |
| 4957 | `model.layers.11` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0004957.npy) |
| 4958 | `model.layers.11` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4959 | `model.layers.11` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4960 | `model.layers.11` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4961 | `model.layers.11.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -221.0 / 424.0 / 0.9934882269965277 / 18.724782799661085 | [NPY](tensors/0004961.npy) |
| 4962 | `model.layers.11.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.0 / 106.0 / 0.12589539421929252 / 3.0638059917041707 | [NPY](tensors/0004962.npy) |
| 4963 | `model.layers.11.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.0 / 106.0 / 0.12589539421929252 / 3.0638059917041707 | [NPY](tensors/0004963.npy) |
| 4964 | `model.layers.11.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 339] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004964.npy) |
| 4965 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0004965.npy) |
| 4966 | `model.layers.11.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4967 | `model.layers.11.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4968 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0004968.npy) |
| 4969 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0004969.npy) |
| 4970 | `model.layers.11.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4971 | `model.layers.11.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.0 / 106.0 / 0.12589539421929252 / 3.0638059917041707 | [NPY](tensors/0004971.npy) |
| 4972 | `model.layers.11.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.5 / 9.0625 / 0.05425625969655812 / 1.3166436228006069 | [NPY](tensors/0004972.npy) |
| 4973 | `model.layers.11.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.0 / 106.0 / 0.12589539421929252 / 3.0638059917041707 | [NPY](tensors/0004973.npy) |
| 4974 | `model.layers.11.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.0 / 41.0 / 0.1336708664894104 / 4.253837654155411 | [NPY](tensors/0004974.npy) |
| 4975 | `model.layers.11.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.0 / 106.0 / 0.12589539421929252 / 3.0638059917041707 | [NPY](tensors/0004975.npy) |
| 4976 | `model.layers.11.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.875 / 8.5 / 0.03428840637207031 / 2.6309951548698316 | [NPY](tensors/0004976.npy) |
| 4977 | `model.layers.11.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.03125 / 6.9375 / -0.0028566252440214157 / 1.5302044371008525 | [NPY](tensors/0004977.npy) |
| 4978 | `model.layers.11.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.5 / 36.5 / 0.0067233085632324215 / 3.8945701778194604 | [NPY](tensors/0004978.npy) |
| 4979 | `model.layers.11.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -62.5 / 36.5 / 0.0067233085632324215 / 3.8945701778194604 | [NPY](tensors/0004979.npy) |
| 4980 | `model.layers.11.self_attn` | 42 | `output[1]` | [1, 64, 1, 339] | torch.bfloat16 → float32 | 3.54702933691442e-11 / 0.9765625 / 0.0027208343001097223 / 0.014534676894855422 | [NPY](tensors/0004980.npy) |
| 4981 | `model.layers.11.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -188.0 / 362.0 / 1.0006351047092015 / 18.977441803546593 | [NPY](tensors/0004981.npy) |
| 4982 | `model.layers.11.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.671875 / 2.828125 / 0.04669860468970405 / 0.7528624429653511 | [NPY](tensors/0004982.npy) |
| 4983 | `model.layers.11.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.671875 / 2.828125 / 0.04669860468970405 / 0.7528624429653511 | [NPY](tensors/0004983.npy) |
| 4984 | `model.layers.11.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.671875 / 2.828125 / 0.04669860468970405 / 0.7528624429653511 | [NPY](tensors/0004984.npy) |
| 4985 | `model.layers.11.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4986 | `model.layers.11.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4987 | `model.layers.11.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4988 | `model.layers.11.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -162.0 / 194.0 / 0.08076713879903158 / 7.374636435248582 | [NPY](tensors/0004988.npy) |
| 4989 | `model.layers.11.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -162.0 / 194.0 / 0.08076713879903158 / 7.374636435248582 | [NPY](tensors/0004989.npy) |
| 4990 | `model.layers.11.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.703125 / 1.0078125 / -0.09632207453250885 / 0.5844278977662968 | [NPY](tensors/0004990.npy) |
| 4991 | `model.layers.11` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -350.0 / 556.0 / 1.0816474066840278 / 23.46271538186672 | [NPY](tensors/0004991.npy) |
| 5070 | `model.layers.11` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -238.0 / 386.0 / 0.9481399536132813 / 18.924816198867845 | [NPY](tensors/0005070.npy) |
| 5071 | `model.layers.11` | 43 | `input.kwargs['attention_mask']` | [1, 1, 1, 340] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005071.npy) |
| 5072 | `model.layers.11` | 43 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0005072.npy) |
| 5073 | `model.layers.11` | 43 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0005073.npy) |
| 5074 | `model.layers.11` | 43 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0005074.npy) |
| 5075 | `model.layers.11` | 43 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5076 | `model.layers.11` | 43 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5077 | `model.layers.11` | 43 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5078 | `model.layers.11.input_layernorm` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -238.0 / 386.0 / 0.9481399536132813 / 18.924816198867845 | [NPY](tensors/0005078.npy) |
| 5079 | `model.layers.11.input_layernorm` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -66.0 / 95.5 / 0.12157769997914632 / 2.925756360368001 | [NPY](tensors/0005079.npy) |
| 5080 | `model.layers.11.self_attn` | 43 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -66.0 / 95.5 / 0.12157769997914632 / 2.925756360368001 | [NPY](tensors/0005080.npy) |
| 5081 | `model.layers.11.self_attn` | 43 | `input.kwargs['attention_mask']` | [1, 1, 1, 340] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005081.npy) |
| 5082 | `model.layers.11.self_attn` | 43 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0005082.npy) |
| 5083 | `model.layers.11.self_attn` | 43 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5084 | `model.layers.11.self_attn` | 43 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5085 | `model.layers.11.self_attn` | 43 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0005085.npy) |
| 5086 | `model.layers.11.self_attn` | 43 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0005086.npy) |
| 5087 | `model.layers.11.self_attn` | 43 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5088 | `model.layers.11.self_attn.q_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -66.0 / 95.5 / 0.12157769997914632 / 2.925756360368001 | [NPY](tensors/0005088.npy) |
| 5089 | `model.layers.11.self_attn.q_proj` | 43 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0 / 8.8125 / 0.04523355420678854 / 1.4125672031269179 | [NPY](tensors/0005089.npy) |
| 5090 | `model.layers.11.self_attn.k_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -66.0 / 95.5 / 0.12157769997914632 / 2.925756360368001 | [NPY](tensors/0005090.npy) |
| 5091 | `model.layers.11.self_attn.k_proj` | 43 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.0 / 38.25 / 0.13150262832641602 / 4.130405275040939 | [NPY](tensors/0005091.npy) |
| 5092 | `model.layers.11.self_attn.v_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -66.0 / 95.5 / 0.12157769997914632 / 2.925756360368001 | [NPY](tensors/0005092.npy) |
| 5093 | `model.layers.11.self_attn.v_proj` | 43 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.6875 / 11.8125 / 0.03890490531921387 / 2.6718874338226026 | [NPY](tensors/0005093.npy) |
| 5094 | `model.layers.11.self_attn.o_proj` | 43 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.3125 / 7.375 / 0.012011007180262823 / 1.4916092736195734 | [NPY](tensors/0005094.npy) |
| 5095 | `model.layers.11.self_attn.o_proj` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -59.0 / 66.5 / 0.014378237724304199 / 3.952172291684556 | [NPY](tensors/0005095.npy) |
| 5096 | `model.layers.11.self_attn` | 43 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -59.0 / 66.5 / 0.014378237724304199 / 3.952172291684556 | [NPY](tensors/0005096.npy) |
| 5097 | `model.layers.11.self_attn` | 43 | `output[1]` | [1, 64, 1, 340] | torch.bfloat16 → float32 | 2.1600499167107046e-11 / 0.9453125 / 0.002758858049086378 / 0.013015231585530676 | [NPY](tensors/0005097.npy) |
| 5098 | `model.layers.11.post_attention_layernorm` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -172.0 / 328.0 / 0.9625751071506077 / 19.084719998588646 | [NPY](tensors/0005098.npy) |
| 5099 | `model.layers.11.post_attention_layernorm` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.734375 / 3.0625 / 0.04425853490829468 / 0.7727711592477622 | [NPY](tensors/0005099.npy) |
| 5100 | `model.layers.11.mlp` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.734375 / 3.0625 / 0.04425853490829468 / 0.7727711592477622 | [NPY](tensors/0005100.npy) |
| 5101 | `model.layers.11.mlp.experts` | 43 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.734375 / 3.0625 / 0.04425853490829468 / 0.7727711592477622 | [NPY](tensors/0005101.npy) |
| 5102 | `model.layers.11.mlp.experts` | 43 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5103 | `model.layers.11.mlp.experts` | 43 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5104 | `model.layers.11.mlp.experts` | 43 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5105 | `model.layers.11.mlp.experts` | 43 | `output` | [1, 2880] | torch.bfloat16 → float32 | -148.0 / 190.0 / 0.14393629497951932 / 7.25825945606989 | [NPY](tensors/0005105.npy) |
| 5106 | `model.layers.11.mlp` | 43 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -148.0 / 190.0 / 0.14393629497951932 / 7.25825945606989 | [NPY](tensors/0005106.npy) |
| 5107 | `model.layers.11.mlp` | 43 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.0 / 1.3203125 / -0.12509918212890625 / 0.7021324194601759 | [NPY](tensors/0005107.npy) |
| 5108 | `model.layers.11` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -320.0 / 520.0 / 1.1073294745551214 / 23.58937116908144 | [NPY](tensors/0005108.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.8760830686193166 / 416.48071795241606 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 297, 297] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.689059412825681e+38 / 1.694756088063524e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 297, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8016785844809279 / 0.8745460170790657 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 297, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12195024475191096 / 0.6221439169688554 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 297] | torch.int64 → int64 | 0.0 / 296.0 / 148.0 / 85.73602898820698 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.8760830686193166 / 416.48071795241606 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 297, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.008040844788722584 / 1.7591935591579988 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 297, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.008040844788722584 / 1.7591935591579988 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 297, 297] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.689059412825681e+38 / 1.694756088063524e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 297] | torch.int64 → int64 | 0.0 / 296.0 / 148.0 / 85.73602898820698 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 297, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8016785844809279 / 0.8745460170790657 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 297, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12195024475191096 / 0.6221439169688554 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.008040844788722584 / 1.7591935591579988 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 297, 4096] | torch.bfloat16 → float32 | -18.125 / 23.75 / 0.03246129194887317 / 1.6405020623124649 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.008040844788722584 / 1.7591935591579988 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 297, 512] | torch.bfloat16 → float32 | -91.0 / 69.0 / -0.08537227270014659 / 4.9928250260142875 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.008040844788722584 / 1.7591935591579988 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 297, 512] | torch.bfloat16 → float32 | -28.125 / 24.625 / 0.004611398435200907 / 3.255427175924012 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 297, 4096] | torch.bfloat16 → float32 | -24.75 / 12.9375 / -0.0022099885353497363 / 1.1342901996479713 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 297, 2880] | torch.bfloat16 → float32 | -6336.0 / 6560.0 / 2.655270264209365 / 164.20741981370398 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -6336.0 / 6560.0 / 2.655270264209365 / 164.20741981370398 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 297, 297] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0015741200287502837 / 0.012343549196610584 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -10752.0 / 11264.0 / 0.7791301391921238 / 363.7985317287594 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 297, 2880] | torch.bfloat16 → float32 | -50.75 / 30.875 / -0.015702770878949324 / 1.2207292563004488 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -50.75 / 30.875 / -0.015702770878949324 / 1.2207292563004488 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [297, 2880] | torch.bfloat16 → float32 | -50.75 / 30.875 / -0.015702770878949324 / 1.2207292563004488 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [297, 2880] | torch.bfloat16 → float32 | -4832.0 / 4736.0 / -1.5305360902885443 / 153.40007883481837 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 297, 2880] | torch.bfloat16 → float32 | -4832.0 / 4736.0 / -1.5305360902885443 / 153.40007883481837 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [297, 32] | torch.bfloat16 → float32 | -8.1875 / 4.6875 / 0.23428875268107713 / 2.494530816893551 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 297, 2880] | torch.bfloat16 → float32 | -10816.0 / 10944.0 / -0.7524882341207212 / 414.20319446758134 | [NPY](tensors/0000116.npy) |
| 195 | `model.layers.23` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7872.0 / 7680.0 / -2.2713026258680555 / 374.66834629842884 | [NPY](tensors/0000195.npy) |
| 196 | `model.layers.23` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 298] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000196.npy) |
| 197 | `model.layers.23` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.4918212890625 / 1.117229907691466 | [NPY](tensors/0000197.npy) |
| 198 | `model.layers.23` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.3359375 / 0.18026646971702576 / 0.5362459422402894 | [NPY](tensors/0000198.npy) |
| 199 | `model.layers.23` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 297.0 / 297.0 / 297.0 / 0.0 | [NPY](tensors/0000199.npy) |
| 200 | `model.layers.23` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 201 | `model.layers.23` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 202 | `model.layers.23` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 203 | `model.layers.23.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7872.0 / 7680.0 / -2.2713026258680555 / 374.66834629842884 | [NPY](tensors/0000203.npy) |
| 204 | `model.layers.23.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 55.0 / 0.0023215916421678333 / 1.7395070468892406 | [NPY](tensors/0000204.npy) |
| 205 | `model.layers.23.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 55.0 / 0.0023215916421678333 / 1.7395070468892406 | [NPY](tensors/0000205.npy) |
| 206 | `model.layers.23.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 298] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000206.npy) |
| 207 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 297.0 / 297.0 / 297.0 / 0.0 | [NPY](tensors/0000207.npy) |
| 208 | `model.layers.23.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 209 | `model.layers.23.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 210 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.4918212890625 / 1.117229907691466 | [NPY](tensors/0000210.npy) |
| 211 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.3359375 / 0.18026646971702576 / 0.5362459422402894 | [NPY](tensors/0000211.npy) |
| 212 | `model.layers.23.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 213 | `model.layers.23.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 55.0 / 0.0023215916421678333 / 1.7395070468892406 | [NPY](tensors/0000213.npy) |
| 214 | `model.layers.23.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.625 / 19.25 / 0.05443573708180338 / 1.5516064291036002 | [NPY](tensors/0000214.npy) |
| 215 | `model.layers.23.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 55.0 / 0.0023215916421678333 / 1.7395070468892406 | [NPY](tensors/0000215.npy) |
| 216 | `model.layers.23.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -66.5 / 50.75 / -0.1461990922689438 / 5.945555747492359 | [NPY](tensors/0000216.npy) |
| 217 | `model.layers.23.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 55.0 / 0.0023215916421678333 / 1.7395070468892406 | [NPY](tensors/0000217.npy) |
| 218 | `model.layers.23.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -20.875 / 15.4375 / -0.0745115876197815 / 3.5303804843941924 | [NPY](tensors/0000218.npy) |
| 219 | `model.layers.23.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -19.625 / 5.6875 / -0.029000131296925247 / 1.0409045456767312 | [NPY](tensors/0000219.npy) |
| 220 | `model.layers.23.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5536.0 / 5888.0 / 6.213146691852145 / 256.9719845522175 | [NPY](tensors/0000220.npy) |
| 221 | `model.layers.23.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5536.0 / 5888.0 / 6.213146691852145 / 256.9719845522175 | [NPY](tensors/0000221.npy) |
| 222 | `model.layers.23.self_attn` | 1 | `output[1]` | [1, 64, 1, 298] | torch.bfloat16 → float32 | 6.110667527536862e-13 / 0.77734375 / 0.001726199469733907 / 0.011185095954338762 | [NPY](tensors/0000222.npy) |
| 223 | `model.layers.23.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 8832.0 / 3.943332248263889 / 496.756952969456 | [NPY](tensors/0000223.npy) |
| 224 | `model.layers.23.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 8.5 / -0.012875758277045356 / 1.0256512788310088 | [NPY](tensors/0000224.npy) |
| 225 | `model.layers.23.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 8.5 / -0.012875758277045356 / 1.0256512788310088 | [NPY](tensors/0000225.npy) |
| 226 | `model.layers.23.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.5 / 8.5 / -0.012875758277045356 / 1.0256512788310088 | [NPY](tensors/0000226.npy) |
| 227 | `model.layers.23.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 228 | `model.layers.23.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 229 | `model.layers.23.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 230 | `model.layers.23.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2112.0 / 1888.0 / -1.52482164700826 / 94.51615070963103 | [NPY](tensors/0000230.npy) |
| 231 | `model.layers.23.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2112.0 / 1888.0 / -1.52482164700826 / 94.51615070963103 | [NPY](tensors/0000231.npy) |
| 232 | `model.layers.23.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.1015625 / 0.8046875 / 0.11997222900390625 / 0.42224371153363155 | [NPY](tensors/0000232.npy) |
| 233 | `model.layers.23` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 8832.0 / 2.4249437120225696 / 517.8459128076533 | [NPY](tensors/0000233.npy) |
| 312 | `model.layers.23` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9216.0 / -1.0064344618055556 / 431.89720915398834 | [NPY](tensors/0000312.npy) |
| 313 | `model.layers.23` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 299] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000313.npy) |
| 314 | `model.layers.23` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.47601318359375 / 1.1300177711987256 | [NPY](tensors/0000314.npy) |
| 315 | `model.layers.23` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2265625 / 0.09335732460021973 / 0.5447921260742894 | [NPY](tensors/0000315.npy) |
| 316 | `model.layers.23` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 298.0 / 298.0 / 298.0 / 0.0 | [NPY](tensors/0000316.npy) |
| 317 | `model.layers.23` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 318 | `model.layers.23` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 319 | `model.layers.23` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 320 | `model.layers.23.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9216.0 / -1.0064344618055556 / 431.89720915398834 | [NPY](tensors/0000320.npy) |
| 321 | `model.layers.23.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 57.25 / 0.006473863787121243 / 1.74341735483946 | [NPY](tensors/0000321.npy) |
| 322 | `model.layers.23.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 57.25 / 0.006473863787121243 / 1.74341735483946 | [NPY](tensors/0000322.npy) |
| 323 | `model.layers.23.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 299] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000323.npy) |
| 324 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 298.0 / 298.0 / 298.0 / 0.0 | [NPY](tensors/0000324.npy) |
| 325 | `model.layers.23.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 326 | `model.layers.23.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 327 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.47601318359375 / 1.1300177711987256 | [NPY](tensors/0000327.npy) |
| 328 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.2265625 / 0.09335732460021973 / 0.5447921260742894 | [NPY](tensors/0000328.npy) |
| 329 | `model.layers.23.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 330 | `model.layers.23.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 57.25 / 0.006473863787121243 / 1.74341735483946 | [NPY](tensors/0000330.npy) |
| 331 | `model.layers.23.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.625 / 16.75 / 0.045079673640429974 / 1.364899348890434 | [NPY](tensors/0000331.npy) |
| 332 | `model.layers.23.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 57.25 / 0.006473863787121243 / 1.74341735483946 | [NPY](tensors/0000332.npy) |
| 333 | `model.layers.23.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.5 / 41.0 / -0.05783480138052255 / 4.910644170434362 | [NPY](tensors/0000333.npy) |
| 334 | `model.layers.23.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 57.25 / 0.006473863787121243 / 1.74341735483946 | [NPY](tensors/0000334.npy) |
| 335 | `model.layers.23.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.125 / 7.6875 / -0.16404247283935547 / 2.886843892626565 | [NPY](tensors/0000335.npy) |
| 336 | `model.layers.23.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.5 / 6.125 / -0.04461459076264873 / 1.2837458800965773 | [NPY](tensors/0000336.npy) |
| 337 | `model.layers.23.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5632.0 / 6016.0 / 5.760398885938856 / 256.4515188797877 | [NPY](tensors/0000337.npy) |
| 338 | `model.layers.23.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5632.0 / 6016.0 / 5.760398885938856 / 256.4515188797877 | [NPY](tensors/0000338.npy) |
| 339 | `model.layers.23.self_attn` | 2 | `output[1]` | [1, 64, 1, 299] | torch.bfloat16 → float32 | 2.0161650127192843e-13 / 0.79296875 / 0.0023723460747082066 / 0.011902144637665405 | [NPY](tensors/0000339.npy) |
| 340 | `model.layers.23.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9216.0 / 4.746999782986111 / 521.835395845692 | [NPY](tensors/0000340.npy) |
| 341 | `model.layers.23.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.125 / 8.1875 / -0.009618730015224881 / 0.8890432463945855 | [NPY](tensors/0000341.npy) |
| 342 | `model.layers.23.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.125 / 8.1875 / -0.009618730015224881 / 0.8890432463945855 | [NPY](tensors/0000342.npy) |
| 343 | `model.layers.23.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -27.125 / 8.1875 / -0.009618730015224881 / 0.8890432463945855 | [NPY](tensors/0000343.npy) |
| 344 | `model.layers.23.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 345 | `model.layers.23.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 346 | `model.layers.23.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 347 | `model.layers.23.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1012.0 / 656.0 / -1.3000047471788194 / 58.38445013445398 | [NPY](tensors/0000347.npy) |
| 348 | `model.layers.23.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1012.0 / 656.0 / -1.3000047471788194 / 58.38445013445398 | [NPY](tensors/0000348.npy) |
| 349 | `model.layers.23.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0546875 / 1.1015625 / 0.13455963134765625 / 0.4638978129240535 | [NPY](tensors/0000349.npy) |
| 350 | `model.layers.23` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8960.0 / 8768.0 / 3.423198784722222 / 501.82278669188474 | [NPY](tensors/0000350.npy) |
| 429 | `model.layers.23` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9344.0 / -3.6986219618055554 / 445.7824048417835 | [NPY](tensors/0000429.npy) |
| 430 | `model.layers.23` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 300] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000430.npy) |
| 431 | `model.layers.23` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.518310546875 / 1.0946292885024063 | [NPY](tensors/0000431.npy) |
| 432 | `model.layers.23` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.234375 / 0.009437993168830872 / 0.5857162614275052 | [NPY](tensors/0000432.npy) |
| 433 | `model.layers.23` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 299.0 / 299.0 / 299.0 / 0.0 | [NPY](tensors/0000433.npy) |
| 434 | `model.layers.23` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 435 | `model.layers.23` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 436 | `model.layers.23` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 437 | `model.layers.23.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9344.0 / -3.6986219618055554 / 445.7824048417835 | [NPY](tensors/0000437.npy) |
| 438 | `model.layers.23.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 56.25 / -0.0009319265683492025 / 1.7291450909738242 | [NPY](tensors/0000438.npy) |
| 439 | `model.layers.23.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 56.25 / -0.0009319265683492025 / 1.7291450909738242 | [NPY](tensors/0000439.npy) |
| 440 | `model.layers.23.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 300] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000440.npy) |
| 441 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 299.0 / 299.0 / 299.0 / 0.0 | [NPY](tensors/0000441.npy) |
| 442 | `model.layers.23.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 443 | `model.layers.23.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 444 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.518310546875 / 1.0946292885024063 | [NPY](tensors/0000444.npy) |
| 445 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.234375 / 0.009437993168830872 / 0.5857162614275052 | [NPY](tensors/0000445.npy) |
| 446 | `model.layers.23.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 447 | `model.layers.23.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 56.25 / -0.0009319265683492025 / 1.7291450909738242 | [NPY](tensors/0000447.npy) |
| 448 | `model.layers.23.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.375 / 16.375 / 0.04658326040953398 / 1.4158448779094872 | [NPY](tensors/0000448.npy) |
| 449 | `model.layers.23.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 56.25 / -0.0009319265683492025 / 1.7291450909738242 | [NPY](tensors/0000449.npy) |
| 450 | `model.layers.23.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.0 / 45.0 / -0.017103448510169983 / 4.9211805898028675 | [NPY](tensors/0000450.npy) |
| 451 | `model.layers.23.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 56.25 / -0.0009319265683492025 / 1.7291450909738242 | [NPY](tensors/0000451.npy) |
| 452 | `model.layers.23.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.75 / 7.96875 / -0.13114970736205578 / 2.259539944033717 | [NPY](tensors/0000452.npy) |
| 453 | `model.layers.23.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.875 / 6.8125 / -0.03155051008798182 / 1.0037514777995833 | [NPY](tensors/0000453.npy) |
| 454 | `model.layers.23.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5632.0 / 6016.0 / 6.091759830050998 / 256.02698135946764 | [NPY](tensors/0000454.npy) |
| 455 | `model.layers.23.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5632.0 / 6016.0 / 6.091759830050998 / 256.02698135946764 | [NPY](tensors/0000455.npy) |
| 456 | `model.layers.23.self_attn` | 3 | `output[1]` | [1, 64, 1, 300] | torch.bfloat16 → float32 | 5.1736392947532295e-14 / 0.8046875 / 0.0018778879525368933 / 0.010809090933701818 | [NPY](tensors/0000456.npy) |
| 457 | `model.layers.23.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 10048.0 / 2.4059583875868054 / 552.4056683243546 | [NPY](tensors/0000457.npy) |
| 458 | `model.layers.23.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.75 / 8.3125 / -0.017727320392926533 / 0.9442407895542739 | [NPY](tensors/0000458.npy) |
| 459 | `model.layers.23.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.75 / 8.3125 / -0.017727320392926533 / 0.9442407895542739 | [NPY](tensors/0000459.npy) |
| 460 | `model.layers.23.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.75 / 8.3125 / -0.017727320392926533 / 0.9442407895542739 | [NPY](tensors/0000460.npy) |
| 461 | `model.layers.23.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 462 | `model.layers.23.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 463 | `model.layers.23.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 464 | `model.layers.23.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1272.0 / 988.0 / -1.0693887498643664 / 56.96935663902916 | [NPY](tensors/0000464.npy) |
| 465 | `model.layers.23.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1272.0 / 988.0 / -1.0693887498643664 / 56.96935663902916 | [NPY](tensors/0000465.npy) |
| 466 | `model.layers.23.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.90234375 / 1.3984375 / 0.031920433044433594 / 0.47063776597784884 | [NPY](tensors/0000466.npy) |
| 467 | `model.layers.23` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9664.0 / 9856.0 / 1.3451095581054688 / 551.3136574901614 | [NPY](tensors/0000467.npy) |
| 546 | `model.layers.23` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9664.0 / 9856.0 / 7.437556966145833 / 456.6504253462196 | [NPY](tensors/0000546.npy) |
| 547 | `model.layers.23` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 301] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000547.npy) |
| 548 | `model.layers.23` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6011199951171875 / 1.029134772776266 | [NPY](tensors/0000548.npy) |
| 549 | `model.layers.23` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.02744269371032715 / 0.6241199078176489 | [NPY](tensors/0000549.npy) |
| 550 | `model.layers.23` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 300.0 / 300.0 / 300.0 / 0.0 | [NPY](tensors/0000550.npy) |
| 551 | `model.layers.23` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 552 | `model.layers.23` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 553 | `model.layers.23` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 554 | `model.layers.23.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9664.0 / 9856.0 / 7.437556966145833 / 456.6504253462196 | [NPY](tensors/0000554.npy) |
| 555 | `model.layers.23.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.0 / 0.032765644126468235 / 1.7407540844683855 | [NPY](tensors/0000555.npy) |
| 556 | `model.layers.23.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.0 / 0.032765644126468235 / 1.7407540844683855 | [NPY](tensors/0000556.npy) |
| 557 | `model.layers.23.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 301] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000557.npy) |
| 558 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 300.0 / 300.0 / 300.0 / 0.0 | [NPY](tensors/0000558.npy) |
| 559 | `model.layers.23.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 560 | `model.layers.23.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 561 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6011199951171875 / 1.029134772776266 | [NPY](tensors/0000561.npy) |
| 562 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.02744269371032715 / 0.6241199078176489 | [NPY](tensors/0000562.npy) |
| 563 | `model.layers.23.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 564 | `model.layers.23.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.0 / 0.032765644126468235 / 1.7407540844683855 | [NPY](tensors/0000564.npy) |
| 565 | `model.layers.23.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.8125 / 14.875 / 0.041689636651426554 / 1.3848118673632133 | [NPY](tensors/0000565.npy) |
| 566 | `model.layers.23.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.0 / 0.032765644126468235 / 1.7407540844683855 | [NPY](tensors/0000566.npy) |
| 567 | `model.layers.23.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.75 / 45.75 / -0.06757187843322754 / 5.240192230528173 | [NPY](tensors/0000567.npy) |
| 568 | `model.layers.23.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.0 / 0.032765644126468235 / 1.7407540844683855 | [NPY](tensors/0000568.npy) |
| 569 | `model.layers.23.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.125 / 8.375 / -0.039832502603530884 / 2.967675166605031 | [NPY](tensors/0000569.npy) |
| 570 | `model.layers.23.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.875 / 7.40625 / -0.04959069471806288 / 1.561063470554689 | [NPY](tensors/0000570.npy) |
| 571 | `model.layers.23.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5984.0 / 6304.0 / 6.152065404256185 / 274.68200410366205 | [NPY](tensors/0000571.npy) |
| 572 | `model.layers.23.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5984.0 / 6304.0 / 6.152065404256185 / 274.68200410366205 | [NPY](tensors/0000572.npy) |
| 573 | `model.layers.23.self_attn` | 4 | `output[1]` | [1, 64, 1, 301] | torch.bfloat16 → float32 | 2.6147972675971687e-12 / 0.84375 / 0.002388126469074743 / 0.015448167250880777 | [NPY](tensors/0000573.npy) |
| 574 | `model.layers.23.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 10176.0 / 13.56812472873264 / 566.0200891491643 | [NPY](tensors/0000574.npy) |
| 575 | `model.layers.23.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 8.4375 / 0.00814500053723653 / 0.9634977419078953 | [NPY](tensors/0000575.npy) |
| 576 | `model.layers.23.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 8.4375 / 0.00814500053723653 / 0.9634977419078953 | [NPY](tensors/0000576.npy) |
| 577 | `model.layers.23.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.25 / 8.4375 / 0.00814500053723653 / 0.9634977419078953 | [NPY](tensors/0000577.npy) |
| 578 | `model.layers.23.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 579 | `model.layers.23.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 580 | `model.layers.23.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 581 | `model.layers.23.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1984.0 / 1664.0 / -0.49424481126997205 / 90.36465663634515 | [NPY](tensors/0000581.npy) |
| 582 | `model.layers.23.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1984.0 / 1664.0 / -0.49424481126997205 / 90.36465663634515 | [NPY](tensors/0000582.npy) |
| 583 | `model.layers.23.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.875 / 1.34375 / 0.09909820556640625 / 0.46276501411717724 | [NPY](tensors/0000583.npy) |
| 584 | `model.layers.23` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 10496.0 / 13.08206515842014 / 595.4197764949627 | [NPY](tensors/0000584.npy) |
| 663 | `model.layers.23` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 9536.0 / -1.8525177001953126 / 452.1621821199856 | [NPY](tensors/0000663.npy) |
| 664 | `model.layers.23` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 302] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000664.npy) |
| 665 | `model.layers.23` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6781768798828125 / 0.9972778713983161 | [NPY](tensors/0000665.npy) |
| 666 | `model.layers.23` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.0019666850566864014 / 0.5958225425092146 | [NPY](tensors/0000666.npy) |
| 667 | `model.layers.23` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 301.0 / 301.0 / 301.0 / 0.0 | [NPY](tensors/0000667.npy) |
| 668 | `model.layers.23` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 669 | `model.layers.23` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 670 | `model.layers.23` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 671 | `model.layers.23.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 9536.0 / -1.8525177001953126 / 452.1621821199856 | [NPY](tensors/0000671.npy) |
| 672 | `model.layers.23.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 54.0 / -0.0011237170961168076 / 1.7333753075128322 | [NPY](tensors/0000672.npy) |
| 673 | `model.layers.23.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 54.0 / -0.0011237170961168076 / 1.7333753075128322 | [NPY](tensors/0000673.npy) |
| 674 | `model.layers.23.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 302] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000674.npy) |
| 675 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 301.0 / 301.0 / 301.0 / 0.0 | [NPY](tensors/0000675.npy) |
| 676 | `model.layers.23.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 677 | `model.layers.23.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 678 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.6781768798828125 / 0.9972778713983161 | [NPY](tensors/0000678.npy) |
| 679 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.234375 / -0.0019666850566864014 / 0.5958225425092146 | [NPY](tensors/0000679.npy) |
| 680 | `model.layers.23.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 681 | `model.layers.23.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 54.0 / -0.0011237170961168076 / 1.7333753075128322 | [NPY](tensors/0000681.npy) |
| 682 | `model.layers.23.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.875 / 16.625 / 0.05224997573532164 / 1.5703113453085011 | [NPY](tensors/0000682.npy) |
| 683 | `model.layers.23.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 54.0 / -0.0011237170961168076 / 1.7333753075128322 | [NPY](tensors/0000683.npy) |
| 684 | `model.layers.23.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.75 / 35.5 / 0.0526256263256073 / 5.438889443713534 | [NPY](tensors/0000684.npy) |
| 685 | `model.layers.23.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 54.0 / -0.0011237170961168076 / 1.7333753075128322 | [NPY](tensors/0000685.npy) |
| 686 | `model.layers.23.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.125 / 15.625 / -0.018583059310913086 / 4.233652682953632 | [NPY](tensors/0000686.npy) |
| 687 | `model.layers.23.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.125 / 6.375 / -0.006377180281560868 / 1.3824829850784255 | [NPY](tensors/0000687.npy) |
| 688 | `model.layers.23.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6304.0 / 6592.0 / 8.7463507215182 / 280.6689590672982 | [NPY](tensors/0000688.npy) |
| 689 | `model.layers.23.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6304.0 / 6592.0 / 8.7463507215182 / 280.6689590672982 | [NPY](tensors/0000689.npy) |
| 690 | `model.layers.23.self_attn` | 5 | `output[1]` | [1, 64, 1, 302] | torch.bfloat16 → float32 | 5.684341886080802e-14 / 0.8828125 / 0.0019350278273294803 / 0.014047369038982599 | [NPY](tensors/0000690.npy) |
| 691 | `model.layers.23.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9856.0 / 6.897694227430556 / 564.0312208431903 | [NPY](tensors/0000691.npy) |
| 692 | `model.layers.23.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 7.34375 / -0.004987587200270759 / 0.9611861024438241 | [NPY](tensors/0000692.npy) |
| 693 | `model.layers.23.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 7.34375 / -0.004987587200270759 / 0.9611861024438241 | [NPY](tensors/0000693.npy) |
| 694 | `model.layers.23.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.25 / 7.34375 / -0.004987587200270759 / 0.9611861024438241 | [NPY](tensors/0000694.npy) |
| 695 | `model.layers.23.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 696 | `model.layers.23.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 697 | `model.layers.23.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 698 | `model.layers.23.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1512.0 / 1096.0 / -1.6059756808810763 / 88.43059116979573 | [NPY](tensors/0000698.npy) |
| 699 | `model.layers.23.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1512.0 / 1096.0 / -1.6059756808810763 / 88.43059116979573 | [NPY](tensors/0000699.npy) |
| 700 | `model.layers.23.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.59375 / 0.9375 / 0.136444091796875 / 0.5904346807510371 | [NPY](tensors/0000700.npy) |
| 701 | `model.layers.23` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 8896.0 / 5.301277669270833 / 519.0775398457021 | [NPY](tensors/0000701.npy) |
| 780 | `model.layers.23` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 8832.0 / 1.222055392795139 / 429.5866595025512 | [NPY](tensors/0000780.npy) |
| 781 | `model.layers.23` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 303] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000781.npy) |
| 782 | `model.layers.23` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.707061767578125 / 0.9717983302810768 | [NPY](tensors/0000782.npy) |
| 783 | `model.layers.23` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.234375 / 0.05849510431289673 / 0.601804974311013 | [NPY](tensors/0000783.npy) |
| 784 | `model.layers.23` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 302.0 / 302.0 / 302.0 / 0.0 | [NPY](tensors/0000784.npy) |
| 785 | `model.layers.23` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 786 | `model.layers.23` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 787 | `model.layers.23` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 788 | `model.layers.23.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 8832.0 / 1.222055392795139 / 429.5866595025512 | [NPY](tensors/0000788.npy) |
| 789 | `model.layers.23.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 54.75 / 0.008539831638336182 / 1.7444282296915548 | [NPY](tensors/0000789.npy) |
| 790 | `model.layers.23.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 54.75 / 0.008539831638336182 / 1.7444282296915548 | [NPY](tensors/0000790.npy) |
| 791 | `model.layers.23.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 303] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000791.npy) |
| 792 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 302.0 / 302.0 / 302.0 / 0.0 | [NPY](tensors/0000792.npy) |
| 793 | `model.layers.23.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 794 | `model.layers.23.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 795 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.707061767578125 / 0.9717983302810768 | [NPY](tensors/0000795.npy) |
| 796 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.234375 / 0.05849510431289673 / 0.601804974311013 | [NPY](tensors/0000796.npy) |
| 797 | `model.layers.23.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 798 | `model.layers.23.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 54.75 / 0.008539831638336182 / 1.7444282296915548 | [NPY](tensors/0000798.npy) |
| 799 | `model.layers.23.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.3125 / 15.625 / 0.05911495929467492 / 1.5002315791869443 | [NPY](tensors/0000799.npy) |
| 800 | `model.layers.23.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 54.75 / 0.008539831638336182 / 1.7444282296915548 | [NPY](tensors/0000800.npy) |
| 801 | `model.layers.23.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.5 / 46.5 / 0.006983071565628052 / 5.700934038349826 | [NPY](tensors/0000801.npy) |
| 802 | `model.layers.23.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 54.75 / 0.008539831638336182 / 1.7444282296915548 | [NPY](tensors/0000802.npy) |
| 803 | `model.layers.23.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.6875 / 13.6875 / 0.04769623279571533 / 3.0913755286377294 | [NPY](tensors/0000803.npy) |
| 804 | `model.layers.23.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.75 / 7.34375 / -0.033261641627177596 / 1.1697283935649494 | [NPY](tensors/0000804.npy) |
| 805 | `model.layers.23.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5824.0 / 6080.0 / 5.865321752760146 / 258.82137495812697 | [NPY](tensors/0000805.npy) |
| 806 | `model.layers.23.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5824.0 / 6080.0 / 5.865321752760146 / 258.82137495812697 | [NPY](tensors/0000806.npy) |
| 807 | `model.layers.23.self_attn` | 6 | `output[1]` | [1, 64, 1, 303] | torch.bfloat16 → float32 | 1.2363443602225743e-12 / 0.84375 / 0.0017308437958101146 / 0.012773678865326021 | [NPY](tensors/0000807.npy) |
| 808 | `model.layers.23.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9024.0 / 7.110224066840278 / 524.6647623838458 | [NPY](tensors/0000808.npy) |
| 809 | `model.layers.23.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.875 / 7.625 / -0.0024701459540261163 / 0.9511255118372327 | [NPY](tensors/0000809.npy) |
| 810 | `model.layers.23.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.875 / 7.625 / -0.0024701459540261163 / 0.9511255118372327 | [NPY](tensors/0000810.npy) |
| 811 | `model.layers.23.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -28.875 / 7.625 / -0.0024701459540261163 / 0.9511255118372327 | [NPY](tensors/0000811.npy) |
| 812 | `model.layers.23.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 813 | `model.layers.23.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 814 | `model.layers.23.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 815 | `model.layers.23.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1160.0 / 944.0 / -0.5976601070827908 / 56.17175153921108 | [NPY](tensors/0000815.npy) |
| 816 | `model.layers.23.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1160.0 / 944.0 / -0.5976601070827908 / 56.17175153921108 | [NPY](tensors/0000816.npy) |
| 817 | `model.layers.23.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.6953125 / 1.421875 / 0.14377307891845703 / 0.45138180139829376 | [NPY](tensors/0000817.npy) |
| 818 | `model.layers.23` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9088.0 / 6.505927191840278 / 530.5176198021169 | [NPY](tensors/0000818.npy) |
| 897 | `model.layers.23` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 10112.0 / -0.7726508246527778 / 485.5126521442488 | [NPY](tensors/0000897.npy) |
| 898 | `model.layers.23` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 304] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000898.npy) |
| 899 | `model.layers.23` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.68243408203125 / 0.9684034292887866 | [NPY](tensors/0000899.npy) |
| 900 | `model.layers.23` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3359375 / 0.10489383339881897 / 0.6297841334602801 | [NPY](tensors/0000900.npy) |
| 901 | `model.layers.23` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 303.0 / 303.0 / 303.0 / 0.0 | [NPY](tensors/0000901.npy) |
| 902 | `model.layers.23` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 903 | `model.layers.23` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 904 | `model.layers.23` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 905 | `model.layers.23.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 10112.0 / -0.7726508246527778 / 485.5126521442488 | [NPY](tensors/0000905.npy) |
| 906 | `model.layers.23.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.0 / 0.00647797319624159 / 1.7379764383195144 | [NPY](tensors/0000906.npy) |
| 907 | `model.layers.23.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.0 / 0.00647797319624159 / 1.7379764383195144 | [NPY](tensors/0000907.npy) |
| 908 | `model.layers.23.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 304] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000908.npy) |
| 909 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 303.0 / 303.0 / 303.0 / 0.0 | [NPY](tensors/0000909.npy) |
| 910 | `model.layers.23.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 911 | `model.layers.23.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 912 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.68243408203125 / 0.9684034292887866 | [NPY](tensors/0000912.npy) |
| 913 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.3359375 / 0.10489383339881897 / 0.6297841334602801 | [NPY](tensors/0000913.npy) |
| 914 | `model.layers.23.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 915 | `model.layers.23.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.0 / 0.00647797319624159 / 1.7379764383195144 | [NPY](tensors/0000915.npy) |
| 916 | `model.layers.23.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0 / 15.8125 / 0.056038155424175784 / 1.465567431992186 | [NPY](tensors/0000916.npy) |
| 917 | `model.layers.23.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.0 / 0.00647797319624159 / 1.7379764383195144 | [NPY](tensors/0000917.npy) |
| 918 | `model.layers.23.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.75 / 46.0 / -0.06460518017411232 / 5.099588380390739 | [NPY](tensors/0000918.npy) |
| 919 | `model.layers.23.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.0 / 0.00647797319624159 / 1.7379764383195144 | [NPY](tensors/0000919.npy) |
| 920 | `model.layers.23.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.25 / 6.3125 / -0.07671580463647842 / 2.4191427607154026 | [NPY](tensors/0000920.npy) |
| 921 | `model.layers.23.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.5 / 6.03125 / -0.034785854688379914 / 0.9238224948616879 | [NPY](tensors/0000921.npy) |
| 922 | `model.layers.23.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6016.0 / 6368.0 / 6.601104863484701 / 276.943060262964 | [NPY](tensors/0000922.npy) |
| 923 | `model.layers.23.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6016.0 / 6368.0 / 6.601104863484701 / 276.943060262964 | [NPY](tensors/0000923.npy) |
| 924 | `model.layers.23.self_attn` | 7 | `output[1]` | [1, 64, 1, 304] | torch.bfloat16 → float32 | 7.904787935331115e-14 / 0.84375 / 0.0011177298207906154 / 0.009949425648506541 | [NPY](tensors/0000924.npy) |
| 925 | `model.layers.23.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10880.0 / 10880.0 / 5.809893120659722 / 604.8067880495887 | [NPY](tensors/0000925.npy) |
| 926 | `model.layers.23.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 10.125 / -0.012966938813527425 / 1.031559109154833 | [NPY](tensors/0000926.npy) |
| 927 | `model.layers.23.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 10.125 / -0.012966938813527425 / 1.031559109154833 | [NPY](tensors/0000927.npy) |
| 928 | `model.layers.23.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.25 / 10.125 / -0.012966938813527425 / 1.031559109154833 | [NPY](tensors/0000928.npy) |
| 929 | `model.layers.23.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 930 | `model.layers.23.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 931 | `model.layers.23.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 932 | `model.layers.23.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -984.0 / 796.0 / -0.4175546434190538 / 51.11116987735686 | [NPY](tensors/0000932.npy) |
| 933 | `model.layers.23.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -984.0 / 796.0 / -0.4175546434190538 / 51.11116987735686 | [NPY](tensors/0000933.npy) |
| 934 | `model.layers.23.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.4375 / 1.25 / 0.017871856689453125 / 0.33616205940949767 | [NPY](tensors/0000934.npy) |
| 935 | `model.layers.23` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10752.0 / 10752.0 / 5.361078559027778 / 599.2937132176761 | [NPY](tensors/0000935.npy) |
| 1014 | `model.layers.23` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 10304.0 / 10.535394965277778 / 493.25494310203965 | [NPY](tensors/0001014.npy) |
| 1015 | `model.layers.23` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 305] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001015.npy) |
| 1016 | `model.layers.23` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6405029296875 / 1.0356892994687845 | [NPY](tensors/0001016.npy) |
| 1017 | `model.layers.23` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1875 / 1.2421875 / 0.10542488098144531 / 0.5631099040524371 | [NPY](tensors/0001017.npy) |
| 1018 | `model.layers.23` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 304.0 / 304.0 / 304.0 / 0.0 | [NPY](tensors/0001018.npy) |
| 1019 | `model.layers.23` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1020 | `model.layers.23` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1021 | `model.layers.23` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1022 | `model.layers.23.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 10304.0 / 10.535394965277778 / 493.25494310203965 | [NPY](tensors/0001022.npy) |
| 1023 | `model.layers.23.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 56.25 / 0.03813833097616832 / 1.726955861865305 | [NPY](tensors/0001023.npy) |
| 1024 | `model.layers.23.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 56.25 / 0.03813833097616832 / 1.726955861865305 | [NPY](tensors/0001024.npy) |
| 1025 | `model.layers.23.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 305] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001025.npy) |
| 1026 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 304.0 / 304.0 / 304.0 / 0.0 | [NPY](tensors/0001026.npy) |
| 1027 | `model.layers.23.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1028 | `model.layers.23.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1029 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6405029296875 / 1.0356892994687845 | [NPY](tensors/0001029.npy) |
| 1030 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1875 / 1.2421875 / 0.10542488098144531 / 0.5631099040524371 | [NPY](tensors/0001030.npy) |
| 1031 | `model.layers.23.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1032 | `model.layers.23.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 56.25 / 0.03813833097616832 / 1.726955861865305 | [NPY](tensors/0001032.npy) |
| 1033 | `model.layers.23.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.59375 / 15.5 / 0.046476724091917276 / 1.3622165576460488 | [NPY](tensors/0001033.npy) |
| 1034 | `model.layers.23.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 56.25 / 0.03813833097616832 / 1.726955861865305 | [NPY](tensors/0001034.npy) |
| 1035 | `model.layers.23.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.5 / 35.75 / -0.038837701082229614 / 4.592848609563629 | [NPY](tensors/0001035.npy) |
| 1036 | `model.layers.23.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 56.25 / 0.03813833097616832 / 1.726955861865305 | [NPY](tensors/0001036.npy) |
| 1037 | `model.layers.23.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.75 / 7.71875 / 0.010808318853378296 / 2.764861510093486 | [NPY](tensors/0001037.npy) |
| 1038 | `model.layers.23.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.375 / 5.9375 / -0.031118252780288458 / 1.2757461819307017 | [NPY](tensors/0001038.npy) |
| 1039 | `model.layers.23.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6144.0 / 6432.0 / 6.843901125590007 / 273.42078172023133 | [NPY](tensors/0001039.npy) |
| 1040 | `model.layers.23.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6144.0 / 6432.0 / 6.843901125590007 / 273.42078172023133 | [NPY](tensors/0001040.npy) |
| 1041 | `model.layers.23.self_attn` | 8 | `output[1]` | [1, 64, 1, 305] | torch.bfloat16 → float32 | 1.0613732115416497e-13 / 0.8828125 / 0.0019361361434677296 / 0.013248725428228575 | [NPY](tensors/0001041.npy) |
| 1042 | `model.layers.23.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 10240.0 / 17.39377983940972 / 585.856431459353 | [NPY](tensors/0001042.npy) |
| 1043 | `model.layers.23.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.5 / 9.5625 / 0.018272414472368027 / 0.9361925621739381 | [NPY](tensors/0001043.npy) |
| 1044 | `model.layers.23.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.5 / 9.5625 / 0.018272414472368027 / 0.9361925621739381 | [NPY](tensors/0001044.npy) |
| 1045 | `model.layers.23.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.5 / 9.5625 / 0.018272414472368027 / 0.9361925621739381 | [NPY](tensors/0001045.npy) |
| 1046 | `model.layers.23.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1047 | `model.layers.23.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1048 | `model.layers.23.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1049 | `model.layers.23.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1224.0 / 816.0 / -0.7262171162499322 / 65.1874029819946 | [NPY](tensors/0001049.npy) |
| 1050 | `model.layers.23.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1224.0 / 816.0 / -0.7262171162499322 / 65.1874029819946 | [NPY](tensors/0001050.npy) |
| 1051 | `model.layers.23.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.80078125 / 1.3671875 / 0.08672642707824707 / 0.4212947313132187 | [NPY](tensors/0001051.npy) |
| 1052 | `model.layers.23` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 9920.0 / 16.66042751736111 / 561.4308706516124 | [NPY](tensors/0001052.npy) |
| 1131 | `model.layers.23` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9856.0 / 9600.0 / -4.846408420138889 / 446.96217827262063 | [NPY](tensors/0001131.npy) |
| 1132 | `model.layers.23` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 306] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001132.npy) |
| 1133 | `model.layers.23` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0001133.npy) |
| 1134 | `model.layers.23` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0001134.npy) |
| 1135 | `model.layers.23` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0001135.npy) |
| 1136 | `model.layers.23` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1137 | `model.layers.23` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1138 | `model.layers.23` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1139 | `model.layers.23.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9856.0 / 9600.0 / -4.846408420138889 / 446.96217827262063 | [NPY](tensors/0001139.npy) |
| 1140 | `model.layers.23.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 57.0 / -0.011690294742584229 / 1.751753168543248 | [NPY](tensors/0001140.npy) |
| 1141 | `model.layers.23.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 57.0 / -0.011690294742584229 / 1.751753168543248 | [NPY](tensors/0001141.npy) |
| 1142 | `model.layers.23.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 306] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001142.npy) |
| 1143 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0001143.npy) |
| 1144 | `model.layers.23.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1145 | `model.layers.23.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1146 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0001146.npy) |
| 1147 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0001147.npy) |
| 1148 | `model.layers.23.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1149 | `model.layers.23.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 57.0 / -0.011690294742584229 / 1.751753168543248 | [NPY](tensors/0001149.npy) |
| 1150 | `model.layers.23.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.25 / 16.125 / 0.04965448938310146 / 1.5015099590575416 | [NPY](tensors/0001150.npy) |
| 1151 | `model.layers.23.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 57.0 / -0.011690294742584229 / 1.751753168543248 | [NPY](tensors/0001151.npy) |
| 1152 | `model.layers.23.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.0 / 35.75 / 0.04798528179526329 / 4.800795708551433 | [NPY](tensors/0001152.npy) |
| 1153 | `model.layers.23.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 57.0 / -0.011690294742584229 / 1.751753168543248 | [NPY](tensors/0001153.npy) |
| 1154 | `model.layers.23.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.25 / 15.5 / -0.04844491183757782 / 3.6485336681613587 | [NPY](tensors/0001154.npy) |
| 1155 | `model.layers.23.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.5 / 7.34375 / -0.040703142527490854 / 1.116923115739997 | [NPY](tensors/0001155.npy) |
| 1156 | `model.layers.23.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5408.0 / 5696.0 / 5.732149799664815 / 238.6941005272321 | [NPY](tensors/0001156.npy) |
| 1157 | `model.layers.23.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5408.0 / 5696.0 / 5.732149799664815 / 238.6941005272321 | [NPY](tensors/0001157.npy) |
| 1158 | `model.layers.23.self_attn` | 9 | `output[1]` | [1, 64, 1, 306] | torch.bfloat16 → float32 | 8.715250743307479e-15 / 0.88671875 / 0.0015361890714330085 / 0.01275882645268544 | [NPY](tensors/0001158.npy) |
| 1159 | `model.layers.23.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9280.0 / 0.8956597222222222 / 513.615648149102 | [NPY](tensors/0001159.npy) |
| 1160 | `model.layers.23.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.0 / 7.3125 / -0.024743599361843532 / 0.9546963287890562 | [NPY](tensors/0001160.npy) |
| 1161 | `model.layers.23.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.0 / 7.3125 / -0.024743599361843532 / 0.9546963287890562 | [NPY](tensors/0001161.npy) |
| 1162 | `model.layers.23.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.0 / 7.3125 / -0.024743599361843532 / 0.9546963287890562 | [NPY](tensors/0001162.npy) |
| 1163 | `model.layers.23.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1164 | `model.layers.23.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1165 | `model.layers.23.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1166 | `model.layers.23.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -756.0 / 788.0 / -0.7188223097059462 / 55.129917747224034 | [NPY](tensors/0001166.npy) |
| 1167 | `model.layers.23.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -756.0 / 788.0 / -0.7188223097059462 / 55.129917747224034 | [NPY](tensors/0001167.npy) |
| 1168 | `model.layers.23.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.48828125 / 1.3125 / 0.14818382263183594 / 0.38853052761682555 | [NPY](tensors/0001168.npy) |
| 1169 | `model.layers.23` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8960.0 / 8576.0 / 0.17687445746527777 / 481.40759706951616 | [NPY](tensors/0001169.npy) |
| 1248 | `model.layers.23` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 9728.0 / -5.5033203125 / 442.0423251677544 | [NPY](tensors/0001248.npy) |
| 1249 | `model.layers.23` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 307] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001249.npy) |
| 1250 | `model.layers.23` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0001250.npy) |
| 1251 | `model.layers.23` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0001251.npy) |
| 1252 | `model.layers.23` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0001252.npy) |
| 1253 | `model.layers.23` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1254 | `model.layers.23` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1255 | `model.layers.23` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1256 | `model.layers.23.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 9728.0 / -5.5033203125 / 442.0423251677544 | [NPY](tensors/0001256.npy) |
| 1257 | `model.layers.23.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 54.0 / -0.0044097191757626 / 1.749106790517274 | [NPY](tensors/0001257.npy) |
| 1258 | `model.layers.23.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 54.0 / -0.0044097191757626 / 1.749106790517274 | [NPY](tensors/0001258.npy) |
| 1259 | `model.layers.23.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 307] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001259.npy) |
| 1260 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0001260.npy) |
| 1261 | `model.layers.23.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1262 | `model.layers.23.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1263 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0001263.npy) |
| 1264 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0001264.npy) |
| 1265 | `model.layers.23.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1266 | `model.layers.23.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 54.0 / -0.0044097191757626 / 1.749106790517274 | [NPY](tensors/0001266.npy) |
| 1267 | `model.layers.23.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.53125 / 15.0 / 0.04122609575279057 / 1.4038664640393141 | [NPY](tensors/0001267.npy) |
| 1268 | `model.layers.23.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 54.0 / -0.0044097191757626 / 1.749106790517274 | [NPY](tensors/0001268.npy) |
| 1269 | `model.layers.23.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.25 / 43.0 / -0.06939340429380536 / 5.2063923041125 | [NPY](tensors/0001269.npy) |
| 1270 | `model.layers.23.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 54.0 / -0.0044097191757626 / 1.749106790517274 | [NPY](tensors/0001270.npy) |
| 1271 | `model.layers.23.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.375 / 8.125 / 0.019007056951522827 / 2.385365136705757 | [NPY](tensors/0001271.npy) |
| 1272 | `model.layers.23.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.75 / 7.75 / -0.050980525789782405 / 1.4305157935176087 | [NPY](tensors/0001272.npy) |
| 1273 | `model.layers.23.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6016.0 / 6272.0 / 5.66198255750868 / 271.04559141965535 | [NPY](tensors/0001273.npy) |
| 1274 | `model.layers.23.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6016.0 / 6272.0 / 5.66198255750868 / 271.04559141965535 | [NPY](tensors/0001274.npy) |
| 1275 | `model.layers.23.self_attn` | 10 | `output[1]` | [1, 64, 1, 307] | torch.bfloat16 → float32 | 1.4033219031261979e-13 / 0.91015625 / 0.0024129875398205417 / 0.014084833260163725 | [NPY](tensors/0001275.npy) |
| 1276 | `model.layers.23.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9920.0 / 0.14042426215277778 / 542.4901169381328 | [NPY](tensors/0001276.npy) |
| 1277 | `model.layers.23.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.875 / 7.96875 / -0.025122621324327257 / 1.0171980823455369 | [NPY](tensors/0001277.npy) |
| 1278 | `model.layers.23.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.875 / 7.96875 / -0.025122621324327257 / 1.0171980823455369 | [NPY](tensors/0001278.npy) |
| 1279 | `model.layers.23.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.875 / 7.96875 / -0.025122621324327257 / 1.0171980823455369 | [NPY](tensors/0001279.npy) |
| 1280 | `model.layers.23.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1281 | `model.layers.23.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1282 | `model.layers.23.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1283 | `model.layers.23.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -800.0 / 504.0 / -1.324212180243598 / 55.75959909920222 | [NPY](tensors/0001283.npy) |
| 1284 | `model.layers.23.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -800.0 / 504.0 / -1.324212180243598 / 55.75959909920222 | [NPY](tensors/0001284.npy) |
| 1285 | `model.layers.23.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.71875 / 1.3125 / 0.0554962158203125 / 0.4528280322478497 | [NPY](tensors/0001285.npy) |
| 1286 | `model.layers.23` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9536.0 / -1.2074273003472222 / 529.7367577454874 | [NPY](tensors/0001286.npy) |
| 1365 | `model.layers.23` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 9664.0 / -3.2527452256944445 / 471.54328734989446 | [NPY](tensors/0001365.npy) |
| 1366 | `model.layers.23` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 308] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001366.npy) |
| 1367 | `model.layers.23` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0001367.npy) |
| 1368 | `model.layers.23` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0001368.npy) |
| 1369 | `model.layers.23` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0001369.npy) |
| 1370 | `model.layers.23` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1371 | `model.layers.23` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1372 | `model.layers.23` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1373 | `model.layers.23.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 9664.0 / -3.2527452256944445 / 471.54328734989446 | [NPY](tensors/0001373.npy) |
| 1374 | `model.layers.23.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 51.75 / -0.00010221401850382486 / 1.6905837929486887 | [NPY](tensors/0001374.npy) |
| 1375 | `model.layers.23.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 51.75 / -0.00010221401850382486 / 1.6905837929486887 | [NPY](tensors/0001375.npy) |
| 1376 | `model.layers.23.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 308] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001376.npy) |
| 1377 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0001377.npy) |
| 1378 | `model.layers.23.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1379 | `model.layers.23.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1380 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0001380.npy) |
| 1381 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0001381.npy) |
| 1382 | `model.layers.23.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1383 | `model.layers.23.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 51.75 / -0.00010221401850382486 / 1.6905837929486887 | [NPY](tensors/0001383.npy) |
| 1384 | `model.layers.23.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.4375 / 16.625 / 0.03908267104998231 / 1.422135333437255 | [NPY](tensors/0001384.npy) |
| 1385 | `model.layers.23.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 51.75 / -0.00010221401850382486 / 1.6905837929486887 | [NPY](tensors/0001385.npy) |
| 1386 | `model.layers.23.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.75 / 44.25 / -0.09145160764455795 / 4.681170066511743 | [NPY](tensors/0001386.npy) |
| 1387 | `model.layers.23.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 51.75 / -0.00010221401850382486 / 1.6905837929486887 | [NPY](tensors/0001387.npy) |
| 1388 | `model.layers.23.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.125 / 10.0625 / -0.03576721251010895 / 2.892795899831176 | [NPY](tensors/0001388.npy) |
| 1389 | `model.layers.23.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.125 / 8.4375 / -0.029180991929024458 / 1.0550587739305946 | [NPY](tensors/0001389.npy) |
| 1390 | `model.layers.23.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 5856.0 / 5.464472632937961 / 246.5778116208318 | [NPY](tensors/0001390.npy) |
| 1391 | `model.layers.23.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 5856.0 / 5.464472632937961 / 246.5778116208318 | [NPY](tensors/0001391.npy) |
| 1392 | `model.layers.23.self_attn` | 11 | `output[1]` | [1, 64, 1, 308] | torch.bfloat16 → float32 | 1.199040866595169e-14 / 0.8359375 / 0.0018828156099647312 / 0.010605337530284004 | [NPY](tensors/0001392.npy) |
| 1393 | `model.layers.23.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 9920.0 / 2.2341932508680555 / 560.3135795966755 | [NPY](tensors/0001393.npy) |
| 1394 | `model.layers.23.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 8.3125 / -0.0214520083533393 / 1.080394183542977 | [NPY](tensors/0001394.npy) |
| 1395 | `model.layers.23.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 8.3125 / -0.0214520083533393 / 1.080394183542977 | [NPY](tensors/0001395.npy) |
| 1396 | `model.layers.23.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.0 / 8.3125 / -0.0214520083533393 / 1.080394183542977 | [NPY](tensors/0001396.npy) |
| 1397 | `model.layers.23.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1398 | `model.layers.23.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1399 | `model.layers.23.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1400 | `model.layers.23.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1064.0 / 732.0 / -1.6117802090115017 / 59.37265928341971 | [NPY](tensors/0001400.npy) |
| 1401 | `model.layers.23.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1064.0 / 732.0 / -1.6117802090115017 / 59.37265928341971 | [NPY](tensors/0001401.npy) |
| 1402 | `model.layers.23.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.15625 / 1.453125 / 0.051665306091308594 / 0.5322031788919246 | [NPY](tensors/0001402.npy) |
| 1403 | `model.layers.23` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9664.0 / 9472.0 / 0.60662841796875 / 546.1212859013176 | [NPY](tensors/0001403.npy) |
| 1482 | `model.layers.23` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 10240.0 / 1.3352810329861111 / 462.95651677964435 | [NPY](tensors/0001482.npy) |
| 1483 | `model.layers.23` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 309] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001483.npy) |
| 1484 | `model.layers.23` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0001484.npy) |
| 1485 | `model.layers.23` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0001485.npy) |
| 1486 | `model.layers.23` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0001486.npy) |
| 1487 | `model.layers.23` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1488 | `model.layers.23` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1489 | `model.layers.23` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1490 | `model.layers.23.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 10240.0 / 1.3352810329861111 / 462.95651677964435 | [NPY](tensors/0001490.npy) |
| 1491 | `model.layers.23.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 59.5 / 0.013374451630645328 / 1.76724964971545 | [NPY](tensors/0001491.npy) |
| 1492 | `model.layers.23.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 59.5 / 0.013374451630645328 / 1.76724964971545 | [NPY](tensors/0001492.npy) |
| 1493 | `model.layers.23.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 309] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001493.npy) |
| 1494 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0001494.npy) |
| 1495 | `model.layers.23.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1496 | `model.layers.23.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1497 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0001497.npy) |
| 1498 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0001498.npy) |
| 1499 | `model.layers.23.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1500 | `model.layers.23.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 59.5 / 0.013374451630645328 / 1.76724964971545 | [NPY](tensors/0001500.npy) |
| 1501 | `model.layers.23.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.0 / 17.125 / 0.05406074342317879 / 1.4154210287070934 | [NPY](tensors/0001501.npy) |
| 1502 | `model.layers.23.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 59.5 / 0.013374451630645328 / 1.76724964971545 | [NPY](tensors/0001502.npy) |
| 1503 | `model.layers.23.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.75 / 43.5 / -0.03847533464431763 / 4.875541966316899 | [NPY](tensors/0001503.npy) |
| 1504 | `model.layers.23.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 59.5 / 0.013374451630645328 / 1.76724964971545 | [NPY](tensors/0001504.npy) |
| 1505 | `model.layers.23.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -12.625 / 10.0 / -0.1180519312620163 / 3.430758912902683 | [NPY](tensors/0001505.npy) |
| 1506 | `model.layers.23.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.625 / 6.8125 / -0.045347750186920166 / 1.345011929700742 | [NPY](tensors/0001506.npy) |
| 1507 | `model.layers.23.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5056.0 / 5376.0 / 4.546515062120226 / 231.9997234889314 | [NPY](tensors/0001507.npy) |
| 1508 | `model.layers.23.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5056.0 / 5376.0 / 4.546515062120226 / 231.9997234889314 | [NPY](tensors/0001508.npy) |
| 1509 | `model.layers.23.self_attn` | 12 | `output[1]` | [1, 64, 1, 309] | torch.bfloat16 → float32 | 1.474376176702208e-13 / 0.84375 / 0.002113871532206842 / 0.012532950425417006 | [NPY](tensors/0001509.npy) |
| 1510 | `model.layers.23.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 9472.0 / 5.882492404513889 / 510.322804544557 | [NPY](tensors/0001510.npy) |
| 1511 | `model.layers.23.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.375 / 8.875 / -0.009131171968248156 / 0.9830260794523438 | [NPY](tensors/0001511.npy) |
| 1512 | `model.layers.23.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.375 / 8.875 / -0.009131171968248156 / 0.9830260794523438 | [NPY](tensors/0001512.npy) |
| 1513 | `model.layers.23.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -28.375 / 8.875 / -0.009131171968248156 / 0.9830260794523438 | [NPY](tensors/0001513.npy) |
| 1514 | `model.layers.23.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1515 | `model.layers.23.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1516 | `model.layers.23.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1517 | `model.layers.23.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1568.0 / 1280.0 / -1.6266730626424153 / 71.51929156190486 | [NPY](tensors/0001517.npy) |
| 1518 | `model.layers.23.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1568.0 / 1280.0 / -1.6266730626424153 / 71.51929156190486 | [NPY](tensors/0001518.npy) |
| 1519 | `model.layers.23.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.98046875 / 1.3359375 / 0.17454147338867188 / 0.4836655409688235 | [NPY](tensors/0001519.npy) |
| 1520 | `model.layers.23` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 9600.0 / 4.295556640625 / 527.8893776268125 | [NPY](tensors/0001520.npy) |
| 1599 | `model.layers.23` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 8640.0 / -6.567332628038194 / 433.7334440799843 | [NPY](tensors/0001599.npy) |
| 1600 | `model.layers.23` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 310] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001600.npy) |
| 1601 | `model.layers.23` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0001601.npy) |
| 1602 | `model.layers.23` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0001602.npy) |
| 1603 | `model.layers.23` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0001603.npy) |
| 1604 | `model.layers.23` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1605 | `model.layers.23` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1606 | `model.layers.23` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1607 | `model.layers.23.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 8640.0 / -6.567332628038194 / 433.7334440799843 | [NPY](tensors/0001607.npy) |
| 1608 | `model.layers.23.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 51.5 / -0.014573277367485895 / 1.7118184777568854 | [NPY](tensors/0001608.npy) |
| 1609 | `model.layers.23.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 51.5 / -0.014573277367485895 / 1.7118184777568854 | [NPY](tensors/0001609.npy) |
| 1610 | `model.layers.23.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 310] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001610.npy) |
| 1611 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0001611.npy) |
| 1612 | `model.layers.23.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1613 | `model.layers.23.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1614 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0001614.npy) |
| 1615 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0001615.npy) |
| 1616 | `model.layers.23.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1617 | `model.layers.23.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 51.5 / -0.014573277367485895 / 1.7118184777568854 | [NPY](tensors/0001617.npy) |
| 1618 | `model.layers.23.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.75 / 16.625 / 0.05616414803080261 / 1.5022102207100176 | [NPY](tensors/0001618.npy) |
| 1619 | `model.layers.23.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 51.5 / -0.014573277367485895 / 1.7118184777568854 | [NPY](tensors/0001619.npy) |
| 1620 | `model.layers.23.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.25 / 46.75 / -0.11928033083677292 / 4.89553233274213 | [NPY](tensors/0001620.npy) |
| 1621 | `model.layers.23.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 51.5 / -0.014573277367485895 / 1.7118184777568854 | [NPY](tensors/0001621.npy) |
| 1622 | `model.layers.23.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.375 / 9.125 / -0.17883090302348137 / 2.957982744375149 | [NPY](tensors/0001622.npy) |
| 1623 | `model.layers.23.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.125 / 7.09375 / -0.039256966731045395 / 1.1475324378476406 | [NPY](tensors/0001623.npy) |
| 1624 | `model.layers.23.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 5920.0 / 5.405785899692112 / 253.76998172928018 | [NPY](tensors/0001624.npy) |
| 1625 | `model.layers.23.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 5920.0 / 5.405785899692112 / 253.76998172928018 | [NPY](tensors/0001625.npy) |
| 1626 | `model.layers.23.self_attn` | 13 | `output[1]` | [1, 64, 1, 310] | torch.bfloat16 → float32 | 2.2537527399890678e-14 / 0.73828125 / 0.0016554502801574746 / 0.011256933305172667 | [NPY](tensors/0001626.npy) |
| 1627 | `model.layers.23.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 8960.0 / -1.1566480848524305 / 527.8318267614584 | [NPY](tensors/0001627.npy) |
| 1628 | `model.layers.23.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.5 / 9.4375 / -0.03205962512228224 / 1.011467756912648 | [NPY](tensors/0001628.npy) |
| 1629 | `model.layers.23.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.5 / 9.4375 / -0.03205962512228224 / 1.011467756912648 | [NPY](tensors/0001629.npy) |
| 1630 | `model.layers.23.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -27.5 / 9.4375 / -0.03205962512228224 / 1.011467756912648 | [NPY](tensors/0001630.npy) |
| 1631 | `model.layers.23.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1632 | `model.layers.23.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1633 | `model.layers.23.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1634 | `model.layers.23.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1664.0 / 1488.0 / -1.4148580021328396 / 86.3184576848896 | [NPY](tensors/0001634.npy) |
| 1635 | `model.layers.23.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1664.0 / 1488.0 / -1.4148580021328396 / 86.3184576848896 | [NPY](tensors/0001635.npy) |
| 1636 | `model.layers.23.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.734375 / 1.5 / 0.13712596893310547 / 0.47446782852664854 | [NPY](tensors/0001636.npy) |
| 1637 | `model.layers.23` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10176.0 / 9344.0 / -2.58568115234375 / 567.1257108946676 | [NPY](tensors/0001637.npy) |
| 1716 | `model.layers.23` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10176.0 / 9280.0 / -8.502433268229167 / 430.46675932437574 | [NPY](tensors/0001716.npy) |
| 1717 | `model.layers.23` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 311] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001717.npy) |
| 1718 | `model.layers.23` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0001718.npy) |
| 1719 | `model.layers.23` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0001719.npy) |
| 1720 | `model.layers.23` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0001720.npy) |
| 1721 | `model.layers.23` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1722 | `model.layers.23` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1723 | `model.layers.23` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1724 | `model.layers.23.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10176.0 / 9280.0 / -8.502433268229167 / 430.46675932437574 | [NPY](tensors/0001724.npy) |
| 1725 | `model.layers.23.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.75 / 53.5 / -0.012871197859446208 / 1.7507823405481913 | [NPY](tensors/0001725.npy) |
| 1726 | `model.layers.23.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.75 / 53.5 / -0.012871197859446208 / 1.7507823405481913 | [NPY](tensors/0001726.npy) |
| 1727 | `model.layers.23.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 311] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001727.npy) |
| 1728 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0001728.npy) |
| 1729 | `model.layers.23.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1730 | `model.layers.23.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1731 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0001731.npy) |
| 1732 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0001732.npy) |
| 1733 | `model.layers.23.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1734 | `model.layers.23.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.75 / 53.5 / -0.012871197859446208 / 1.7507823405481913 | [NPY](tensors/0001734.npy) |
| 1735 | `model.layers.23.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.375 / 15.9375 / 0.033720154664479196 / 1.4540147876218403 | [NPY](tensors/0001735.npy) |
| 1736 | `model.layers.23.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.75 / 53.5 / -0.012871197859446208 / 1.7507823405481913 | [NPY](tensors/0001736.npy) |
| 1737 | `model.layers.23.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.25 / 48.0 / -0.08548139035701752 / 5.515779679311301 | [NPY](tensors/0001737.npy) |
| 1738 | `model.layers.23.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.75 / 53.5 / -0.012871197859446208 / 1.7507823405481913 | [NPY](tensors/0001738.npy) |
| 1739 | `model.layers.23.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -22.0 / 7.59375 / -0.07772624492645264 / 2.658922742582473 | [NPY](tensors/0001739.npy) |
| 1740 | `model.layers.23.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -21.125 / 7.0 / -0.0552436513826251 / 1.4511889307261978 | [NPY](tensors/0001740.npy) |
| 1741 | `model.layers.23.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6336.0 / 6560.0 / 6.339485592312283 / 288.42390173141524 | [NPY](tensors/0001741.npy) |
| 1742 | `model.layers.23.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6336.0 / 6560.0 / 6.339485592312283 / 288.42390173141524 | [NPY](tensors/0001742.npy) |
| 1743 | `model.layers.23.self_attn` | 14 | `output[1]` | [1, 64, 1, 311] | torch.bfloat16 → float32 | 5.186961971048731e-13 / 0.9609375 / 0.002403079086222105 / 0.013512575595874049 | [NPY](tensors/0001743.npy) |
| 1744 | `model.layers.23.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10880.0 / 9920.0 / -2.167648654513889 / 556.3647682460829 | [NPY](tensors/0001744.npy) |
| 1745 | `model.layers.23.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.5 / 7.5625 / -0.02998805046081543 / 0.962461126564606 | [NPY](tensors/0001745.npy) |
| 1746 | `model.layers.23.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.5 / 7.5625 / -0.02998805046081543 / 0.962461126564606 | [NPY](tensors/0001746.npy) |
| 1747 | `model.layers.23.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -26.5 / 7.5625 / -0.02998805046081543 / 0.962461126564606 | [NPY](tensors/0001747.npy) |
| 1748 | `model.layers.23.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1749 | `model.layers.23.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1750 | `model.layers.23.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1751 | `model.layers.23.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1272.0 / 880.0 / -2.27513943778144 / 61.06625094128257 | [NPY](tensors/0001751.npy) |
| 1752 | `model.layers.23.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1272.0 / 880.0 / -2.27513943778144 / 61.06625094128257 | [NPY](tensors/0001752.npy) |
| 1753 | `model.layers.23.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.80859375 / 1.1328125 / 0.0639047622680664 / 0.4201825989296939 | [NPY](tensors/0001753.npy) |
| 1754 | `model.layers.23` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 9728.0 / -4.438620334201389 / 554.2429126315568 | [NPY](tensors/0001754.npy) |
| 1833 | `model.layers.23` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9728.0 / -4.891048177083333 / 415.3134165664853 | [NPY](tensors/0001833.npy) |
| 1834 | `model.layers.23` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 312] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001834.npy) |
| 1835 | `model.layers.23` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0001835.npy) |
| 1836 | `model.layers.23` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0001836.npy) |
| 1837 | `model.layers.23` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0001837.npy) |
| 1838 | `model.layers.23` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1839 | `model.layers.23` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1840 | `model.layers.23` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1841 | `model.layers.23.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9728.0 / -4.891048177083333 / 415.3134165664853 | [NPY](tensors/0001841.npy) |
| 1842 | `model.layers.23.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 63.0 / 0.003852438926696777 / 1.8122940159795256 | [NPY](tensors/0001842.npy) |
| 1843 | `model.layers.23.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 63.0 / 0.003852438926696777 / 1.8122940159795256 | [NPY](tensors/0001843.npy) |
| 1844 | `model.layers.23.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 312] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001844.npy) |
| 1845 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0001845.npy) |
| 1846 | `model.layers.23.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1847 | `model.layers.23.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1848 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0001848.npy) |
| 1849 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0001849.npy) |
| 1850 | `model.layers.23.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1851 | `model.layers.23.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 63.0 / 0.003852438926696777 / 1.8122940159795256 | [NPY](tensors/0001851.npy) |
| 1852 | `model.layers.23.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.625 / 16.5 / 0.03714023868087679 / 1.538945646029812 | [NPY](tensors/0001852.npy) |
| 1853 | `model.layers.23.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 63.0 / 0.003852438926696777 / 1.8122940159795256 | [NPY](tensors/0001853.npy) |
| 1854 | `model.layers.23.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -47.75 / 37.5 / -0.1337486356496811 / 4.671342352965032 | [NPY](tensors/0001854.npy) |
| 1855 | `model.layers.23.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 63.0 / 0.003852438926696777 / 1.8122940159795256 | [NPY](tensors/0001855.npy) |
| 1856 | `model.layers.23.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.375 / 14.375 / 0.17169371247291565 / 3.806377065575246 | [NPY](tensors/0001856.npy) |
| 1857 | `model.layers.23.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.4375 / 8.3125 / 0.06141071091406047 / 1.3111234494392445 | [NPY](tensors/0001857.npy) |
| 1858 | `model.layers.23.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3312.0 / 3328.0 / 2.422886742485894 / 165.28259407563039 | [NPY](tensors/0001858.npy) |
| 1859 | `model.layers.23.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3312.0 / 3328.0 / 2.422886742485894 / 165.28259407563039 | [NPY](tensors/0001859.npy) |
| 1860 | `model.layers.23.self_attn` | 15 | `output[1]` | [1, 64, 1, 312] | torch.bfloat16 → float32 | 3.712308238590367e-16 / 0.96875 / 0.002441426738000656 / 0.016152184159953096 | [NPY](tensors/0001860.npy) |
| 1861 | `model.layers.23.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7552.0 / 7488.0 / -2.4791775173611112 / 380.8322699043604 | [NPY](tensors/0001861.npy) |
| 1862 | `model.layers.23.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.0 / 8.25 / -0.029614473713768852 / 1.0922692883451863 | [NPY](tensors/0001862.npy) |
| 1863 | `model.layers.23.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.0 / 8.25 / -0.029614473713768852 / 1.0922692883451863 | [NPY](tensors/0001863.npy) |
| 1864 | `model.layers.23.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.0 / 8.25 / -0.029614473713768852 / 1.0922692883451863 | [NPY](tensors/0001864.npy) |
| 1865 | `model.layers.23.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1866 | `model.layers.23.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1867 | `model.layers.23.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1868 | `model.layers.23.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3632.0 / 3440.0 / -0.8763321770562066 / 171.18320776409828 | [NPY](tensors/0001868.npy) |
| 1869 | `model.layers.23.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3632.0 / 3440.0 / -0.8763321770562066 / 171.18320776409828 | [NPY](tensors/0001869.npy) |
| 1870 | `model.layers.23.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.375 / 1.1328125 / -0.03719770908355713 / 0.897578622078318 | [NPY](tensors/0001870.npy) |
| 1871 | `model.layers.23` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4096.0 / 3856.0 / -3.3412543402777777 / 273.4616454466067 | [NPY](tensors/0001871.npy) |
| 1950 | `model.layers.23` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9088.0 / -2.3250244140625 / 404.0700774146825 | [NPY](tensors/0001950.npy) |
| 1951 | `model.layers.23` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 313] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001951.npy) |
| 1952 | `model.layers.23` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0001952.npy) |
| 1953 | `model.layers.23` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0001953.npy) |
| 1954 | `model.layers.23` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0001954.npy) |
| 1955 | `model.layers.23` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1956 | `model.layers.23` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1957 | `model.layers.23` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1958 | `model.layers.23.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9088.0 / -2.3250244140625 / 404.0700774146825 | [NPY](tensors/0001958.npy) |
| 1959 | `model.layers.23.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 60.5 / 0.013769998815324572 / 1.8070343955926402 | [NPY](tensors/0001959.npy) |
| 1960 | `model.layers.23.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 60.5 / 0.013769998815324572 / 1.8070343955926402 | [NPY](tensors/0001960.npy) |
| 1961 | `model.layers.23.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 313] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001961.npy) |
| 1962 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0001962.npy) |
| 1963 | `model.layers.23.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1964 | `model.layers.23.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1965 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0001965.npy) |
| 1966 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0001966.npy) |
| 1967 | `model.layers.23.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1968 | `model.layers.23.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 60.5 / 0.013769998815324572 / 1.8070343955926402 | [NPY](tensors/0001968.npy) |
| 1969 | `model.layers.23.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.625 / 15.625 / 0.052123251371085644 / 1.650836988784421 | [NPY](tensors/0001969.npy) |
| 1970 | `model.layers.23.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 60.5 / 0.013769998815324572 / 1.8070343955926402 | [NPY](tensors/0001970.npy) |
| 1971 | `model.layers.23.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.75 / 31.0 / -0.11110968142747879 / 4.739901737931939 | [NPY](tensors/0001971.npy) |
| 1972 | `model.layers.23.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 60.5 / 0.013769998815324572 / 1.8070343955926402 | [NPY](tensors/0001972.npy) |
| 1973 | `model.layers.23.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.25 / 18.0 / 0.08820325136184692 / 4.534631685652105 | [NPY](tensors/0001973.npy) |
| 1974 | `model.layers.23.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.6875 / 8.75 / 0.05876390476623783 / 1.3176477240501094 | [NPY](tensors/0001974.npy) |
| 1975 | `model.layers.23.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2784.0 / 2704.0 / 1.4680115487840442 / 143.8550883807583 | [NPY](tensors/0001975.npy) |
| 1976 | `model.layers.23.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2784.0 / 2704.0 / 1.4680115487840442 / 143.8550883807583 | [NPY](tensors/0001976.npy) |
| 1977 | `model.layers.23.self_attn` | 16 | `output[1]` | [1, 64, 1, 313] | torch.bfloat16 → float32 | 1.6306400674181987e-15 / 0.953125 / 0.0021488387560850567 / 0.014825379776619924 | [NPY](tensors/0001977.npy) |
| 1978 | `model.layers.23.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7488.0 / 7232.0 / -0.8733832465277778 / 364.9525434833759 | [NPY](tensors/0001978.npy) |
| 1979 | `model.layers.23.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.875 / 10.4375 / -0.023046984937455918 / 1.1386669415362785 | [NPY](tensors/0001979.npy) |
| 1980 | `model.layers.23.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.875 / 10.4375 / -0.023046984937455918 / 1.1386669415362785 | [NPY](tensors/0001980.npy) |
| 1981 | `model.layers.23.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -30.875 / 10.4375 / -0.023046984937455918 / 1.1386669415362785 | [NPY](tensors/0001981.npy) |
| 1982 | `model.layers.23.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1983 | `model.layers.23.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1984 | `model.layers.23.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1985 | `model.layers.23.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5024.0 / 4608.0 / -1.8376521428426107 / 226.5906729603589 | [NPY](tensors/0001985.npy) |
| 1986 | `model.layers.23.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5024.0 / 4608.0 / -1.8376521428426107 / 226.5906729603589 | [NPY](tensors/0001986.npy) |
| 1987 | `model.layers.23.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.9375 / 1.1171875 / -0.14159393310546875 / 0.916001138256129 | [NPY](tensors/0001987.npy) |
| 1988 | `model.layers.23` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2880.0 / 2624.0 / -2.705935329861111 / 239.68831570254338 | [NPY](tensors/0001988.npy) |
| 2067 | `model.layers.23` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 9728.0 / -1.3438313802083333 / 434.38417307933946 | [NPY](tensors/0002067.npy) |
| 2068 | `model.layers.23` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 314] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002068.npy) |
| 2069 | `model.layers.23` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0002069.npy) |
| 2070 | `model.layers.23` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0002070.npy) |
| 2071 | `model.layers.23` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0002071.npy) |
| 2072 | `model.layers.23` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2073 | `model.layers.23` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2074 | `model.layers.23` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2075 | `model.layers.23.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 9728.0 / -1.3438313802083333 / 434.38417307933946 | [NPY](tensors/0002075.npy) |
| 2076 | `model.layers.23.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.75 / 56.25 / 0.014038034280141195 / 1.7747759478381966 | [NPY](tensors/0002076.npy) |
| 2077 | `model.layers.23.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.75 / 56.25 / 0.014038034280141195 / 1.7747759478381966 | [NPY](tensors/0002077.npy) |
| 2078 | `model.layers.23.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 314] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002078.npy) |
| 2079 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0002079.npy) |
| 2080 | `model.layers.23.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2081 | `model.layers.23.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2082 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0002082.npy) |
| 2083 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0002083.npy) |
| 2084 | `model.layers.23.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2085 | `model.layers.23.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.75 / 56.25 / 0.014038034280141195 / 1.7747759478381966 | [NPY](tensors/0002085.npy) |
| 2086 | `model.layers.23.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.9375 / 15.3125 / 0.04048404563218355 / 1.6034078459635837 | [NPY](tensors/0002086.npy) |
| 2087 | `model.layers.23.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.75 / 56.25 / 0.014038034280141195 / 1.7747759478381966 | [NPY](tensors/0002087.npy) |
| 2088 | `model.layers.23.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.875 / 33.5 / -0.042805951088666916 / 4.626541740436234 | [NPY](tensors/0002088.npy) |
| 2089 | `model.layers.23.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.75 / 56.25 / 0.014038034280141195 / 1.7747759478381966 | [NPY](tensors/0002089.npy) |
| 2090 | `model.layers.23.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.9375 / 13.125 / -0.0006775856018066406 / 3.986728465954799 | [NPY](tensors/0002090.npy) |
| 2091 | `model.layers.23.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.9375 / 8.0625 / 0.08892206382006407 / 1.4545663373708413 | [NPY](tensors/0002091.npy) |
| 2092 | `model.layers.23.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3040.0 / 2944.0 / 1.4775544908311633 / 149.29854973888177 | [NPY](tensors/0002092.npy) |
| 2093 | `model.layers.23.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3040.0 / 2944.0 / 1.4775544908311633 / 149.29854973888177 | [NPY](tensors/0002093.npy) |
| 2094 | `model.layers.23.self_attn` | 17 | `output[1]` | [1, 64, 1, 314] | torch.bfloat16 → float32 | 9.325873406851315e-15 / 0.9453125 / 0.0025749981498869377 / 0.01555636312551796 | [NPY](tensors/0002094.npy) |
| 2095 | `model.layers.23.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 8320.0 / 0.13753797743055557 / 405.2921582896476 | [NPY](tensors/0002095.npy) |
| 2096 | `model.layers.23.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 8.5 / -0.01820125381151835 / 1.1082081561829522 | [NPY](tensors/0002096.npy) |
| 2097 | `model.layers.23.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 8.5 / -0.01820125381151835 / 1.1082081561829522 | [NPY](tensors/0002097.npy) |
| 2098 | `model.layers.23.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -28.625 / 8.5 / -0.01820125381151835 / 1.1082081561829522 | [NPY](tensors/0002098.npy) |
| 2099 | `model.layers.23.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2100 | `model.layers.23.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2101 | `model.layers.23.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2102 | `model.layers.23.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5440.0 / 4672.0 / -4.0600312338935005 / 230.33751901612547 | [NPY](tensors/0002102.npy) |
| 2103 | `model.layers.23.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5440.0 / 4672.0 / -4.0600312338935005 / 230.33751901612547 | [NPY](tensors/0002103.npy) |
| 2104 | `model.layers.23.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.203125 / 1.140625 / -0.1023712158203125 / 0.763900540128977 | [NPY](tensors/0002104.npy) |
| 2105 | `model.layers.23` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4160.0 / 3712.0 / -3.927007378472222 / 274.0262347643198 | [NPY](tensors/0002105.npy) |
| 2184 | `model.layers.23` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8576.0 / 8832.0 / -2.5204766167534722 / 395.4482647019442 | [NPY](tensors/0002184.npy) |
| 2185 | `model.layers.23` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 315] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002185.npy) |
| 2186 | `model.layers.23` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0002186.npy) |
| 2187 | `model.layers.23` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0002187.npy) |
| 2188 | `model.layers.23` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0002188.npy) |
| 2189 | `model.layers.23` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2190 | `model.layers.23` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2191 | `model.layers.23` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2192 | `model.layers.23.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8576.0 / 8832.0 / -2.5204766167534722 / 395.4482647019442 | [NPY](tensors/0002192.npy) |
| 2193 | `model.layers.23.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 60.0 / 0.010211986965603298 / 1.7919260407131032 | [NPY](tensors/0002193.npy) |
| 2194 | `model.layers.23.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 60.0 / 0.010211986965603298 / 1.7919260407131032 | [NPY](tensors/0002194.npy) |
| 2195 | `model.layers.23.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 315] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002195.npy) |
| 2196 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0002196.npy) |
| 2197 | `model.layers.23.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2198 | `model.layers.23.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2199 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0002199.npy) |
| 2200 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0002200.npy) |
| 2201 | `model.layers.23.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2202 | `model.layers.23.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 60.0 / 0.010211986965603298 / 1.7919260407131032 | [NPY](tensors/0002202.npy) |
| 2203 | `model.layers.23.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.0625 / 16.75 / 0.05085431758197956 / 1.6573280106574058 | [NPY](tensors/0002203.npy) |
| 2204 | `model.layers.23.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 60.0 / 0.010211986965603298 / 1.7919260407131032 | [NPY](tensors/0002204.npy) |
| 2205 | `model.layers.23.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.75 / 36.5 / -0.06286175549030304 / 5.402054722985593 | [NPY](tensors/0002205.npy) |
| 2206 | `model.layers.23.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 60.0 / 0.010211986965603298 / 1.7919260407131032 | [NPY](tensors/0002206.npy) |
| 2207 | `model.layers.23.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -12.5625 / 12.0 / -0.017101891338825226 / 3.701065446766092 | [NPY](tensors/0002207.npy) |
| 2208 | `model.layers.23.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.3125 / 8.0625 / 0.054781638318672776 / 1.2701565117638238 | [NPY](tensors/0002208.npy) |
| 2209 | `model.layers.23.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2800.0 / 2704.0 / 1.9045516596900092 / 136.57662560920613 | [NPY](tensors/0002209.npy) |
| 2210 | `model.layers.23.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2800.0 / 2704.0 / 1.9045516596900092 / 136.57662560920613 | [NPY](tensors/0002210.npy) |
| 2211 | `model.layers.23.self_attn` | 18 | `output[1]` | [1, 64, 1, 315] | torch.bfloat16 → float32 | 4.529709940470639e-14 / 0.90234375 / 0.002174114864108732 / 0.014030133827490153 | [NPY](tensors/0002211.npy) |
| 2212 | `model.layers.23.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6976.0 / 7296.0 / -0.626287841796875 / 371.0550287974565 | [NPY](tensors/0002212.npy) |
| 2213 | `model.layers.23.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 10.375 / -0.018725265396965875 / 1.221344566482711 | [NPY](tensors/0002213.npy) |
| 2214 | `model.layers.23.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 10.375 / -0.018725265396965875 / 1.221344566482711 | [NPY](tensors/0002214.npy) |
| 2215 | `model.layers.23.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.0 / 10.375 / -0.018725265396965875 / 1.221344566482711 | [NPY](tensors/0002215.npy) |
| 2216 | `model.layers.23.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2217 | `model.layers.23.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2218 | `model.layers.23.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2219 | `model.layers.23.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3920.0 / 3920.0 / -1.2044264051649305 / 204.02251644544535 | [NPY](tensors/0002219.npy) |
| 2220 | `model.layers.23.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3920.0 / 3920.0 / -1.2044264051649305 / 204.02251644544535 | [NPY](tensors/0002220.npy) |
| 2221 | `model.layers.23.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.484375 / 2.125 / -0.04724311828613281 / 1.2458312782933045 | [NPY](tensors/0002221.npy) |
| 2222 | `model.layers.23` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3056.0 / 3376.0 / -1.8286349826388888 / 280.7729321916708 | [NPY](tensors/0002222.npy) |
| 2301 | `model.layers.23` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 9728.0 / 1.256787109375 / 451.0865518826958 | [NPY](tensors/0002301.npy) |
| 2302 | `model.layers.23` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 316] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002302.npy) |
| 2303 | `model.layers.23` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0002303.npy) |
| 2304 | `model.layers.23` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0002304.npy) |
| 2305 | `model.layers.23` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0002305.npy) |
| 2306 | `model.layers.23` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2307 | `model.layers.23` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2308 | `model.layers.23` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2309 | `model.layers.23.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 9728.0 / 1.256787109375 / 451.0865518826958 | [NPY](tensors/0002309.npy) |
| 2310 | `model.layers.23.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 58.0 / 0.018436788188086615 / 1.7634246067895931 | [NPY](tensors/0002310.npy) |
| 2311 | `model.layers.23.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 58.0 / 0.018436788188086615 / 1.7634246067895931 | [NPY](tensors/0002311.npy) |
| 2312 | `model.layers.23.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 316] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002312.npy) |
| 2313 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0002313.npy) |
| 2314 | `model.layers.23.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2315 | `model.layers.23.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2316 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0002316.npy) |
| 2317 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0002317.npy) |
| 2318 | `model.layers.23.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2319 | `model.layers.23.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 58.0 / 0.018436788188086615 / 1.7634246067895931 | [NPY](tensors/0002319.npy) |
| 2320 | `model.layers.23.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.1875 / 17.625 / 0.021410244837170467 / 1.5670167367478316 | [NPY](tensors/0002320.npy) |
| 2321 | `model.layers.23.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 58.0 / 0.018436788188086615 / 1.7634246067895931 | [NPY](tensors/0002321.npy) |
| 2322 | `model.layers.23.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.75 / 27.125 / 0.06442916393280029 / 4.400265234320001 | [NPY](tensors/0002322.npy) |
| 2323 | `model.layers.23.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 58.0 / 0.018436788188086615 / 1.7634246067895931 | [NPY](tensors/0002323.npy) |
| 2324 | `model.layers.23.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -10.875 / 13.125 / -0.00992196798324585 / 3.464871649227661 | [NPY](tensors/0002324.npy) |
| 2325 | `model.layers.23.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.5625 / 7.40625 / 0.0370812323744758 / 1.2204222234671562 | [NPY](tensors/0002325.npy) |
| 2326 | `model.layers.23.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3264.0 / 3280.0 / 2.9872372097439235 / 161.87874910185874 | [NPY](tensors/0002326.npy) |
| 2327 | `model.layers.23.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3264.0 / 3280.0 / 2.9872372097439235 / 161.87874910185874 | [NPY](tensors/0002327.npy) |
| 2328 | `model.layers.23.self_attn` | 19 | `output[1]` | [1, 64, 1, 316] | torch.bfloat16 → float32 | 9.192646643896296e-14 / 0.8671875 / 0.002198378186591868 / 0.012511382003045479 | [NPY](tensors/0002328.npy) |
| 2329 | `model.layers.23.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8384.0 / 7968.0 / 4.2379340277777775 / 421.27812085694717 | [NPY](tensors/0002329.npy) |
| 2330 | `model.layers.23.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.0 / 7.8125 / -0.0023325814141167533 / 1.1157209336259561 | [NPY](tensors/0002330.npy) |
| 2331 | `model.layers.23.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.0 / 7.8125 / -0.0023325814141167533 / 1.1157209336259561 | [NPY](tensors/0002331.npy) |
| 2332 | `model.layers.23.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -28.0 / 7.8125 / -0.0023325814141167533 / 1.1157209336259561 | [NPY](tensors/0002332.npy) |
| 2333 | `model.layers.23.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2334 | `model.layers.23.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2335 | `model.layers.23.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2336 | `model.layers.23.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4256.0 / 4096.0 / -1.2975068834092882 / 212.21758260979314 | [NPY](tensors/0002336.npy) |
| 2337 | `model.layers.23.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4256.0 / 4096.0 / -1.2975068834092882 / 212.21758260979314 | [NPY](tensors/0002337.npy) |
| 2338 | `model.layers.23.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.296875 / 1.1875 / 0.0431976318359375 / 0.7847137602492822 | [NPY](tensors/0002338.npy) |
| 2339 | `model.layers.23` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4416.0 / 3808.0 / 2.9524034288194443 / 299.6376508545438 | [NPY](tensors/0002339.npy) |
| 2418 | `model.layers.23` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 10432.0 / -1.67501220703125 / 463.23525427481667 | [NPY](tensors/0002418.npy) |
| 2419 | `model.layers.23` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 317] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002419.npy) |
| 2420 | `model.layers.23` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0002420.npy) |
| 2421 | `model.layers.23` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0002421.npy) |
| 2422 | `model.layers.23` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0002422.npy) |
| 2423 | `model.layers.23` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2424 | `model.layers.23` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2425 | `model.layers.23` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2426 | `model.layers.23.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 10432.0 / -1.67501220703125 / 463.23525427481667 | [NPY](tensors/0002426.npy) |
| 2427 | `model.layers.23.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 60.5 / 0.010076323482725356 / 1.78652336672327 | [NPY](tensors/0002427.npy) |
| 2428 | `model.layers.23.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 60.5 / 0.010076323482725356 / 1.78652336672327 | [NPY](tensors/0002428.npy) |
| 2429 | `model.layers.23.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 317] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002429.npy) |
| 2430 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0002430.npy) |
| 2431 | `model.layers.23.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2432 | `model.layers.23.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2433 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0002433.npy) |
| 2434 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0002434.npy) |
| 2435 | `model.layers.23.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2436 | `model.layers.23.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 60.5 / 0.010076323482725356 / 1.78652336672327 | [NPY](tensors/0002436.npy) |
| 2437 | `model.layers.23.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.125 / 15.3125 / 0.04112097586039454 / 1.5800578318289014 | [NPY](tensors/0002437.npy) |
| 2438 | `model.layers.23.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 60.5 / 0.010076323482725356 / 1.78652336672327 | [NPY](tensors/0002438.npy) |
| 2439 | `model.layers.23.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -37.25 / 31.375 / -0.03427133709192276 / 4.427247733883246 | [NPY](tensors/0002439.npy) |
| 2440 | `model.layers.23.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 60.5 / 0.010076323482725356 / 1.78652336672327 | [NPY](tensors/0002440.npy) |
| 2441 | `model.layers.23.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.875 / 7.90625 / -0.13015571236610413 / 2.887315148409653 | [NPY](tensors/0002441.npy) |
| 2442 | `model.layers.23.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.3125 / 6.0 / 0.029409735463559628 / 1.1732107967983734 | [NPY](tensors/0002442.npy) |
| 2443 | `model.layers.23.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3024.0 / 2944.0 / 2.2145834181043837 / 147.30017698949322 | [NPY](tensors/0002443.npy) |
| 2444 | `model.layers.23.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3024.0 / 2944.0 / 2.2145834181043837 / 147.30017698949322 | [NPY](tensors/0002444.npy) |
| 2445 | `model.layers.23.self_attn` | 20 | `output[1]` | [1, 64, 1, 317] | torch.bfloat16 → float32 | 1.0524914273446484e-13 / 0.875 / 0.002178820109967123 / 0.01208485379142862 | [NPY](tensors/0002445.npy) |
| 2446 | `model.layers.23.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8768.0 / 8448.0 / 0.5232042100694444 / 425.43679054632696 | [NPY](tensors/0002446.npy) |
| 2447 | `model.layers.23.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 5.28125 / -0.02487678130467733 / 1.2243358199489998 | [NPY](tensors/0002447.npy) |
| 2448 | `model.layers.23.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 5.28125 / -0.02487678130467733 / 1.2243358199489998 | [NPY](tensors/0002448.npy) |
| 2449 | `model.layers.23.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.0 / 5.28125 / -0.02487678130467733 / 1.2243358199489998 | [NPY](tensors/0002449.npy) |
| 2450 | `model.layers.23.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2451 | `model.layers.23.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2452 | `model.layers.23.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2453 | `model.layers.23.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3808.0 / 3712.0 / 0.5897774590386284 / 194.4077685485807 | [NPY](tensors/0002453.npy) |
| 2454 | `model.layers.23.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3808.0 / 3712.0 / 0.5897774590386284 / 194.4077685485807 | [NPY](tensors/0002454.npy) |
| 2455 | `model.layers.23.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.90625 / 1.4140625 / 0.0078125 / 0.6920416244205937 | [NPY](tensors/0002455.npy) |
| 2456 | `model.layers.23` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5088.0 / 4768.0 / 1.087353515625 / 320.95452448011474 | [NPY](tensors/0002456.npy) |
| 2535 | `model.layers.23` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9408.0 / -1.1991997612847223 / 424.18907065110005 | [NPY](tensors/0002535.npy) |
| 2536 | `model.layers.23` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 318] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002536.npy) |
| 2537 | `model.layers.23` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0002537.npy) |
| 2538 | `model.layers.23` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0002538.npy) |
| 2539 | `model.layers.23` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0002539.npy) |
| 2540 | `model.layers.23` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2541 | `model.layers.23` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2542 | `model.layers.23` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2543 | `model.layers.23.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9408.0 / -1.1991997612847223 / 424.18907065110005 | [NPY](tensors/0002543.npy) |
| 2544 | `model.layers.23.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 59.5 / 0.008912059995863173 / 1.7869954123529195 | [NPY](tensors/0002544.npy) |
| 2545 | `model.layers.23.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 59.5 / 0.008912059995863173 / 1.7869954123529195 | [NPY](tensors/0002545.npy) |
| 2546 | `model.layers.23.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 318] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002546.npy) |
| 2547 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0002547.npy) |
| 2548 | `model.layers.23.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2549 | `model.layers.23.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2550 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0002550.npy) |
| 2551 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0002551.npy) |
| 2552 | `model.layers.23.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2553 | `model.layers.23.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 59.5 / 0.008912059995863173 / 1.7869954123529195 | [NPY](tensors/0002553.npy) |
| 2554 | `model.layers.23.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.0625 / 14.8125 / 0.05111384700285271 / 1.6325909708982154 | [NPY](tensors/0002554.npy) |
| 2555 | `model.layers.23.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 59.5 / 0.008912059995863173 / 1.7869954123529195 | [NPY](tensors/0002555.npy) |
| 2556 | `model.layers.23.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.25 / 27.125 / -0.08556218631565571 / 4.294783327498602 | [NPY](tensors/0002556.npy) |
| 2557 | `model.layers.23.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 59.5 / 0.008912059995863173 / 1.7869954123529195 | [NPY](tensors/0002557.npy) |
| 2558 | `model.layers.23.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.1875 / 9.625 / 0.08756014704704285 / 3.059687659457118 | [NPY](tensors/0002558.npy) |
| 2559 | `model.layers.23.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.4375 / 6.0 / 0.07353135058656335 / 1.31213602677546 | [NPY](tensors/0002559.npy) |
| 2560 | `model.layers.23.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3216.0 / 3168.0 / 1.8278534001774258 / 144.78046868528247 | [NPY](tensors/0002560.npy) |
| 2561 | `model.layers.23.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3216.0 / 3168.0 / 1.8278534001774258 / 144.78046868528247 | [NPY](tensors/0002561.npy) |
| 2562 | `model.layers.23.self_attn` | 21 | `output[1]` | [1, 64, 1, 318] | torch.bfloat16 → float32 | 2.5868196473766147e-14 / 0.8828125 / 0.0022484644327850504 / 0.014953071990806678 | [NPY](tensors/0002562.npy) |
| 2563 | `model.layers.23.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8192.0 / 8320.0 / 0.6324055989583334 / 420.9225832777939 | [NPY](tensors/0002563.npy) |
| 2564 | `model.layers.23.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.5 / 9.0625 / -0.02216927210489909 / 1.2100992502590153 | [NPY](tensors/0002564.npy) |
| 2565 | `model.layers.23.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.5 / 9.0625 / -0.02216927210489909 / 1.2100992502590153 | [NPY](tensors/0002565.npy) |
| 2566 | `model.layers.23.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -35.5 / 9.0625 / -0.02216927210489909 / 1.2100992502590153 | [NPY](tensors/0002566.npy) |
| 2567 | `model.layers.23.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2568 | `model.layers.23.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2569 | `model.layers.23.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2570 | `model.layers.23.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6272.0 / 5920.0 / -1.7027514139811197 / 350.5950353536328 | [NPY](tensors/0002570.npy) |
| 2571 | `model.layers.23.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6272.0 / 5920.0 / -1.7027514139811197 / 350.5950353536328 | [NPY](tensors/0002571.npy) |
| 2572 | `model.layers.23.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.59375 / 2.09375 / -0.051591239869594574 / 0.964715744831435 | [NPY](tensors/0002572.npy) |
| 2573 | `model.layers.23` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2560.0 / 2048.0 / -1.0811957465277777 / 332.4215660731604 | [NPY](tensors/0002573.npy) |
| 2652 | `model.layers.23` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9856.0 / -0.3813680013020833 / 444.5743598470171 | [NPY](tensors/0002652.npy) |
| 2653 | `model.layers.23` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 319] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002653.npy) |
| 2654 | `model.layers.23` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0002654.npy) |
| 2655 | `model.layers.23` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0002655.npy) |
| 2656 | `model.layers.23` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0002656.npy) |
| 2657 | `model.layers.23` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2658 | `model.layers.23` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2659 | `model.layers.23` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2660 | `model.layers.23.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9856.0 / -0.3813680013020833 / 444.5743598470171 | [NPY](tensors/0002660.npy) |
| 2661 | `model.layers.23.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 58.5 / 0.012284319930606418 / 1.777820942965057 | [NPY](tensors/0002661.npy) |
| 2662 | `model.layers.23.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 58.5 / 0.012284319930606418 / 1.777820942965057 | [NPY](tensors/0002662.npy) |
| 2663 | `model.layers.23.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 319] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002663.npy) |
| 2664 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0002664.npy) |
| 2665 | `model.layers.23.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2666 | `model.layers.23.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2667 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0002667.npy) |
| 2668 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0002668.npy) |
| 2669 | `model.layers.23.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2670 | `model.layers.23.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 58.5 / 0.012284319930606418 / 1.777820942965057 | [NPY](tensors/0002670.npy) |
| 2671 | `model.layers.23.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.6875 / 15.25 / 0.053232618258334696 / 1.6043399040048083 | [NPY](tensors/0002671.npy) |
| 2672 | `model.layers.23.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 58.5 / 0.012284319930606418 / 1.777820942965057 | [NPY](tensors/0002672.npy) |
| 2673 | `model.layers.23.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -41.0 / 25.5 / -0.17019294202327728 / 4.470648519132962 | [NPY](tensors/0002673.npy) |
| 2674 | `model.layers.23.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 58.5 / 0.012284319930606418 / 1.777820942965057 | [NPY](tensors/0002674.npy) |
| 2675 | `model.layers.23.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.1875 / 15.0625 / -0.18266752362251282 / 5.022083888607742 | [NPY](tensors/0002675.npy) |
| 2676 | `model.layers.23.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.4375 / 6.84375 / 0.03000486952078063 / 1.0450800464491963 | [NPY](tensors/0002676.npy) |
| 2677 | `model.layers.23.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2384.0 / 2672.0 / 1.0281619416342842 / 128.67378758196963 | [NPY](tensors/0002677.npy) |
| 2678 | `model.layers.23.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2384.0 / 2672.0 / 1.0281619416342842 / 128.67378758196963 | [NPY](tensors/0002678.npy) |
| 2679 | `model.layers.23.self_attn` | 22 | `output[1]` | [1, 64, 1, 319] | torch.bfloat16 → float32 | 1.4432899320127035e-14 / 0.88671875 / 0.0016819498507352703 / 0.010720542274393532 | [NPY](tensors/0002679.npy) |
| 2680 | `model.layers.23.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7808.0 / 7744.0 / 0.6764078776041667 / 370.5249042937598 | [NPY](tensors/0002680.npy) |
| 2681 | `model.layers.23.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 12.4375 / -0.019916415214538574 / 1.2777433750714986 | [NPY](tensors/0002681.npy) |
| 2682 | `model.layers.23.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 12.4375 / -0.019916415214538574 / 1.2777433750714986 | [NPY](tensors/0002682.npy) |
| 2683 | `model.layers.23.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -35.25 / 12.4375 / -0.019916415214538574 / 1.2777433750714986 | [NPY](tensors/0002683.npy) |
| 2684 | `model.layers.23.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2685 | `model.layers.23.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2686 | `model.layers.23.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2687 | `model.layers.23.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6240.0 / 5600.0 / -2.8550014919704862 / 272.66440067659016 | [NPY](tensors/0002687.npy) |
| 2688 | `model.layers.23.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6240.0 / 5600.0 / -2.8550014919704862 / 272.66440067659016 | [NPY](tensors/0002688.npy) |
| 2689 | `model.layers.23.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.96875 / 1.7265625 / -0.11587285995483398 / 1.0822828534699425 | [NPY](tensors/0002689.npy) |
| 2690 | `model.layers.23` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2208.0 / 2016.0 / -2.1841796875 / 254.3384410203536 | [NPY](tensors/0002690.npy) |
| 2769 | `model.layers.23` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 8576.0 / -2.582272677951389 / 425.2076223146175 | [NPY](tensors/0002769.npy) |
| 2770 | `model.layers.23` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 320] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002770.npy) |
| 2771 | `model.layers.23` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0002771.npy) |
| 2772 | `model.layers.23` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0002772.npy) |
| 2773 | `model.layers.23` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0002773.npy) |
| 2774 | `model.layers.23` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2775 | `model.layers.23` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2776 | `model.layers.23` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2777 | `model.layers.23.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 8576.0 / -2.582272677951389 / 425.2076223146175 | [NPY](tensors/0002777.npy) |
| 2778 | `model.layers.23.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 52.5 / 0.006453221374087863 / 1.7456475472320734 | [NPY](tensors/0002778.npy) |
| 2779 | `model.layers.23.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 52.5 / 0.006453221374087863 / 1.7456475472320734 | [NPY](tensors/0002779.npy) |
| 2780 | `model.layers.23.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 320] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002780.npy) |
| 2781 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0002781.npy) |
| 2782 | `model.layers.23.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2783 | `model.layers.23.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2784 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0002784.npy) |
| 2785 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0002785.npy) |
| 2786 | `model.layers.23.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2787 | `model.layers.23.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 52.5 / 0.006453221374087863 / 1.7456475472320734 | [NPY](tensors/0002787.npy) |
| 2788 | `model.layers.23.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.125 / 16.875 / 0.06089957646327093 / 1.8850465506082608 | [NPY](tensors/0002788.npy) |
| 2789 | `model.layers.23.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 52.5 / 0.006453221374087863 / 1.7456475472320734 | [NPY](tensors/0002789.npy) |
| 2790 | `model.layers.23.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.0 / 29.375 / -0.06172230839729309 / 4.793681345320053 | [NPY](tensors/0002790.npy) |
| 2791 | `model.layers.23.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 52.5 / 0.006453221374087863 / 1.7456475472320734 | [NPY](tensors/0002791.npy) |
| 2792 | `model.layers.23.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.5 / 14.625 / 0.24185341596603394 / 4.114276156233656 | [NPY](tensors/0002792.npy) |
| 2793 | `model.layers.23.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.8125 / 8.75 / 0.041544068488292396 / 1.3182931799738182 | [NPY](tensors/0002793.npy) |
| 2794 | `model.layers.23.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2928.0 / 2896.0 / 0.2406457159254286 / 144.82463431843192 | [NPY](tensors/0002794.npy) |
| 2795 | `model.layers.23.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2928.0 / 2896.0 / 0.2406457159254286 / 144.82463431843192 | [NPY](tensors/0002795.npy) |
| 2796 | `model.layers.23.self_attn` | 23 | `output[1]` | [1, 64, 1, 320] | torch.bfloat16 → float32 | 9.103828801926284e-15 / 0.92578125 / 0.0019245675548428935 / 0.014419881495632784 | [NPY](tensors/0002796.npy) |
| 2797 | `model.layers.23.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7648.0 / 7264.0 / -2.3376600477430554 / 413.0254255427515 | [NPY](tensors/0002797.npy) |
| 2798 | `model.layers.23.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 9.125 / -0.03783758216434055 / 1.3852907520062445 | [NPY](tensors/0002798.npy) |
| 2799 | `model.layers.23.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 9.125 / -0.03783758216434055 / 1.3852907520062445 | [NPY](tensors/0002799.npy) |
| 2800 | `model.layers.23.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -40.25 / 9.125 / -0.03783758216434055 / 1.3852907520062445 | [NPY](tensors/0002800.npy) |
| 2801 | `model.layers.23.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2802 | `model.layers.23.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2803 | `model.layers.23.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2804 | `model.layers.23.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6848.0 / 6144.0 / -0.35226898193359374 / 314.7233784442207 | [NPY](tensors/0002804.npy) |
| 2805 | `model.layers.23.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6848.0 / 6144.0 / -0.35226898193359374 / 314.7233784442207 | [NPY](tensors/0002805.npy) |
| 2806 | `model.layers.23.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.921875 / 1.6171875 / -0.0506591796875 / 1.0188459947181827 | [NPY](tensors/0002806.npy) |
| 2807 | `model.layers.23` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1504.0 / 1416.0 / -2.681890190972222 / 293.88883270844656 | [NPY](tensors/0002807.npy) |
| 2886 | `model.layers.23` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8448.0 / 7872.0 / -4.911544460720486 / 425.2237971715582 | [NPY](tensors/0002886.npy) |
| 2887 | `model.layers.23` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 321] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002887.npy) |
| 2888 | `model.layers.23` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0002888.npy) |
| 2889 | `model.layers.23` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0002889.npy) |
| 2890 | `model.layers.23` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0002890.npy) |
| 2891 | `model.layers.23` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2892 | `model.layers.23` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2893 | `model.layers.23` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2894 | `model.layers.23.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8448.0 / 7872.0 / -4.911544460720486 / 425.2237971715582 | [NPY](tensors/0002894.npy) |
| 2895 | `model.layers.23.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 48.5 / 1.1123551262749567e-05 / 1.6991660084921008 | [NPY](tensors/0002895.npy) |
| 2896 | `model.layers.23.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 48.5 / 1.1123551262749567e-05 / 1.6991660084921008 | [NPY](tensors/0002896.npy) |
| 2897 | `model.layers.23.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 321] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002897.npy) |
| 2898 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0002898.npy) |
| 2899 | `model.layers.23.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2900 | `model.layers.23.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2901 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0002901.npy) |
| 2902 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0002902.npy) |
| 2903 | `model.layers.23.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2904 | `model.layers.23.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 48.5 / 1.1123551262749567e-05 / 1.6991660084921008 | [NPY](tensors/0002904.npy) |
| 2905 | `model.layers.23.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.25 / 15.375 / 0.025791372230742127 / 1.7799163565203417 | [NPY](tensors/0002905.npy) |
| 2906 | `model.layers.23.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 48.5 / 1.1123551262749567e-05 / 1.6991660084921008 | [NPY](tensors/0002906.npy) |
| 2907 | `model.layers.23.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.75 / 26.625 / -0.048778235912323 / 4.633354188380411 | [NPY](tensors/0002907.npy) |
| 2908 | `model.layers.23.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 48.5 / 1.1123551262749567e-05 / 1.6991660084921008 | [NPY](tensors/0002908.npy) |
| 2909 | `model.layers.23.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.875 / 13.875 / 0.031163930892944336 / 4.481403878035296 | [NPY](tensors/0002909.npy) |
| 2910 | `model.layers.23.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.625 / 9.625 / 0.04071728634880856 / 1.2631117457248984 | [NPY](tensors/0002910.npy) |
| 2911 | `model.layers.23.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2560.0 / 2448.0 / 0.9473044713338216 / 133.05388651030427 | [NPY](tensors/0002911.npy) |
| 2912 | `model.layers.23.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2560.0 / 2448.0 / 0.9473044713338216 / 133.05388651030427 | [NPY](tensors/0002912.npy) |
| 2913 | `model.layers.23.self_attn` | 24 | `output[1]` | [1, 64, 1, 321] | torch.bfloat16 → float32 | 4.468647674116255e-15 / 0.95703125 / 0.001993636708160752 / 0.014569249863274573 | [NPY](tensors/0002913.npy) |
| 2914 | `model.layers.23.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6688.0 / 6272.0 / -3.9620713975694444 / 396.4100851085927 | [NPY](tensors/0002914.npy) |
| 2915 | `model.layers.23.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 11.4375 / -0.03859499163097806 / 1.4819559631475567 | [NPY](tensors/0002915.npy) |
| 2916 | `model.layers.23.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 11.4375 / -0.03859499163097806 / 1.4819559631475567 | [NPY](tensors/0002916.npy) |
| 2917 | `model.layers.23.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.5 / 11.4375 / -0.03859499163097806 / 1.4819559631475567 | [NPY](tensors/0002917.npy) |
| 2918 | `model.layers.23.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2919 | `model.layers.23.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2920 | `model.layers.23.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2921 | `model.layers.23.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5056.0 / 4768.0 / 1.3702418009440105 / 284.12441089692277 | [NPY](tensors/0002921.npy) |
| 2922 | `model.layers.23.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5056.0 / 4768.0 / 1.3702418009440105 / 284.12441089692277 | [NPY](tensors/0002922.npy) |
| 2923 | `model.layers.23.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.078125 / 1.5703125 / -0.026336669921875 / 1.1317912328249915 | [NPY](tensors/0002923.npy) |
| 2924 | `model.layers.23` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1984.0 / 1776.0 / -2.5921983506944444 / 349.9852788884202 | [NPY](tensors/0002924.npy) |
| 3003 | `model.layers.23` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 9600.0 / 0.94287109375 / 425.1154206720278 | [NPY](tensors/0003003.npy) |
| 3004 | `model.layers.23` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003004.npy) |
| 3005 | `model.layers.23` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0003005.npy) |
| 3006 | `model.layers.23` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0003006.npy) |
| 3007 | `model.layers.23` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0003007.npy) |
| 3008 | `model.layers.23` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3009 | `model.layers.23` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3010 | `model.layers.23` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3011 | `model.layers.23.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 9600.0 / 0.94287109375 / 425.1154206720278 | [NPY](tensors/0003011.npy) |
| 3012 | `model.layers.23.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 60.75 / 0.016300921969943576 / 1.814243356462678 | [NPY](tensors/0003012.npy) |
| 3013 | `model.layers.23.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 60.75 / 0.016300921969943576 / 1.814243356462678 | [NPY](tensors/0003013.npy) |
| 3014 | `model.layers.23.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003014.npy) |
| 3015 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0003015.npy) |
| 3016 | `model.layers.23.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3017 | `model.layers.23.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3018 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0003018.npy) |
| 3019 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0003019.npy) |
| 3020 | `model.layers.23.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3021 | `model.layers.23.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 60.75 / 0.016300921969943576 / 1.814243356462678 | [NPY](tensors/0003021.npy) |
| 3022 | `model.layers.23.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.8125 / 15.0625 / 0.05650333105586469 / 1.487260529075683 | [NPY](tensors/0003022.npy) |
| 3023 | `model.layers.23.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 60.75 / 0.016300921969943576 / 1.814243356462678 | [NPY](tensors/0003023.npy) |
| 3024 | `model.layers.23.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.5 / 32.5 / -0.07225248217582703 / 4.507380603637282 | [NPY](tensors/0003024.npy) |
| 3025 | `model.layers.23.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 60.75 / 0.016300921969943576 / 1.814243356462678 | [NPY](tensors/0003025.npy) |
| 3026 | `model.layers.23.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.875 / 13.375 / 0.32895612716674805 / 3.7913073177014462 | [NPY](tensors/0003026.npy) |
| 3027 | `model.layers.23.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.0 / 8.0625 / 0.04757910118496511 / 1.2092555251001866 | [NPY](tensors/0003027.npy) |
| 3028 | `model.layers.23.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4048.0 / 4128.0 / 2.868794947862625 / 178.7861601061491 | [NPY](tensors/0003028.npy) |
| 3029 | `model.layers.23.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4048.0 / 4128.0 / 2.868794947862625 / 178.7861601061491 | [NPY](tensors/0003029.npy) |
| 3030 | `model.layers.23.self_attn` | 25 | `output[1]` | [1, 64, 1, 322] | torch.bfloat16 → float32 | 7.283063041541027e-14 / 0.87890625 / 0.0019462826769583044 / 0.011179250741297275 | [NPY](tensors/0003030.npy) |
| 3031 | `model.layers.23.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 8512.0 / 3.8232069227430556 / 443.8539760009645 | [NPY](tensors/0003031.npy) |
| 3032 | `model.layers.23.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 7.71875 / -0.00655097332265642 / 1.0566866442088887 | [NPY](tensors/0003032.npy) |
| 3033 | `model.layers.23.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 7.71875 / -0.00655097332265642 / 1.0566866442088887 | [NPY](tensors/0003033.npy) |
| 3034 | `model.layers.23.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.5 / 7.71875 / -0.00655097332265642 / 1.0566866442088887 | [NPY](tensors/0003034.npy) |
| 3035 | `model.layers.23.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3036 | `model.layers.23.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3037 | `model.layers.23.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3038 | `model.layers.23.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4192.0 / 3728.0 / -4.749682362874349 / 202.98770772234457 | [NPY](tensors/0003038.npy) |
| 3039 | `model.layers.23.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4192.0 / 3728.0 / -4.749682362874349 / 202.98770772234457 | [NPY](tensors/0003039.npy) |
| 3040 | `model.layers.23.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.71875 / 1.9609375 / 0.02960205078125 / 1.0457467344023548 | [NPY](tensors/0003040.npy) |
| 3041 | `model.layers.23` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5440.0 / 4320.0 / -0.9407769097222223 / 314.9110733927643 | [NPY](tensors/0003041.npy) |
| 3120 | `model.layers.23` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7456.0 / 7968.0 / 3.8565199110243054 / 409.22969453020477 | [NPY](tensors/0003120.npy) |
| 3121 | `model.layers.23` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003121.npy) |
| 3122 | `model.layers.23` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0003122.npy) |
| 3123 | `model.layers.23` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0003123.npy) |
| 3124 | `model.layers.23` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0003124.npy) |
| 3125 | `model.layers.23` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3126 | `model.layers.23` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3127 | `model.layers.23` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3128 | `model.layers.23.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7456.0 / 7968.0 / 3.8565199110243054 / 409.22969453020477 | [NPY](tensors/0003128.npy) |
| 3129 | `model.layers.23.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 52.25 / 0.025475806328985426 / 1.7052460286707907 | [NPY](tensors/0003129.npy) |
| 3130 | `model.layers.23.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 52.25 / 0.025475806328985426 / 1.7052460286707907 | [NPY](tensors/0003130.npy) |
| 3131 | `model.layers.23.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003131.npy) |
| 3132 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0003132.npy) |
| 3133 | `model.layers.23.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3134 | `model.layers.23.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3135 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0003135.npy) |
| 3136 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0003136.npy) |
| 3137 | `model.layers.23.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3138 | `model.layers.23.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 52.25 / 0.025475806328985426 / 1.7052460286707907 | [NPY](tensors/0003138.npy) |
| 3139 | `model.layers.23.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.5 / 12.0 / 0.04767695808550343 / 1.4724263181061228 | [NPY](tensors/0003139.npy) |
| 3140 | `model.layers.23.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 52.25 / 0.025475806328985426 / 1.7052460286707907 | [NPY](tensors/0003140.npy) |
| 3141 | `model.layers.23.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -37.5 / 28.125 / -0.012825213372707367 / 4.472275575277133 | [NPY](tensors/0003141.npy) |
| 3142 | `model.layers.23.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 52.25 / 0.025475806328985426 / 1.7052460286707907 | [NPY](tensors/0003142.npy) |
| 3143 | `model.layers.23.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -12.875 / 11.0625 / 0.04618406295776367 / 3.778066100702078 | [NPY](tensors/0003143.npy) |
| 3144 | `model.layers.23.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.125 / 8.6875 / 0.0298125036933925 / 1.1241341918365269 | [NPY](tensors/0003144.npy) |
| 3145 | `model.layers.23.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2336.0 / 2496.0 / 0.5388524903191461 / 123.73613785055882 | [NPY](tensors/0003145.npy) |
| 3146 | `model.layers.23.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2336.0 / 2496.0 / 0.5388524903191461 / 123.73613785055882 | [NPY](tensors/0003146.npy) |
| 3147 | `model.layers.23.self_attn` | 26 | `output[1]` | [1, 64, 1, 323] | torch.bfloat16 → float32 | 4.405364961712621e-13 / 0.8203125 / 0.0013496207942758124 / 0.011207665356861815 | [NPY](tensors/0003147.npy) |
| 3148 | `model.layers.23.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5824.0 / 6336.0 / 4.407351345486111 / 381.17559562838795 | [NPY](tensors/0003148.npy) |
| 3149 | `model.layers.23.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 9.8125 / -0.0013138413429260253 / 1.5549127039101767 | [NPY](tensors/0003149.npy) |
| 3150 | `model.layers.23.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 9.8125 / -0.0013138413429260253 / 1.5549127039101767 | [NPY](tensors/0003150.npy) |
| 3151 | `model.layers.23.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -48.25 / 9.8125 / -0.0013138413429260253 / 1.5549127039101767 | [NPY](tensors/0003151.npy) |
| 3152 | `model.layers.23.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3153 | `model.layers.23.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3154 | `model.layers.23.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3155 | `model.layers.23.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3744.0 / 3216.0 / -0.481546868218316 / 208.07816745726868 | [NPY](tensors/0003155.npy) |
| 3156 | `model.layers.23.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3744.0 / 3216.0 / -0.481546868218316 / 208.07816745726868 | [NPY](tensors/0003156.npy) |
| 3157 | `model.layers.23.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.65625 / 2.65625 / 0.07958984375 / 1.5355922865963794 | [NPY](tensors/0003157.npy) |
| 3158 | `model.layers.23` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3808.0 / 3008.0 / 3.9226996527777778 / 339.1843578266702 | [NPY](tensors/0003158.npy) |
| 3237 | `model.layers.23` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6400.0 / 6976.0 / 0.9970113118489583 / 382.0507188211861 | [NPY](tensors/0003237.npy) |
| 3238 | `model.layers.23` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003238.npy) |
| 3239 | `model.layers.23` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0003239.npy) |
| 3240 | `model.layers.23` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0003240.npy) |
| 3241 | `model.layers.23` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0003241.npy) |
| 3242 | `model.layers.23` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3243 | `model.layers.23` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3244 | `model.layers.23` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3245 | `model.layers.23.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6400.0 / 6976.0 / 0.9970113118489583 / 382.0507188211861 | [NPY](tensors/0003245.npy) |
| 3246 | `model.layers.23.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 49.0 / 0.015927942593892415 / 1.6777003218760214 | [NPY](tensors/0003246.npy) |
| 3247 | `model.layers.23.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 49.0 / 0.015927942593892415 / 1.6777003218760214 | [NPY](tensors/0003247.npy) |
| 3248 | `model.layers.23.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003248.npy) |
| 3249 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0003249.npy) |
| 3250 | `model.layers.23.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3251 | `model.layers.23.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3252 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0003252.npy) |
| 3253 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0003253.npy) |
| 3254 | `model.layers.23.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3255 | `model.layers.23.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 49.0 / 0.015927942593892415 / 1.6777003218760214 | [NPY](tensors/0003255.npy) |
| 3256 | `model.layers.23.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.5625 / 13.125 / 0.0251000146381557 / 1.6415216558712737 | [NPY](tensors/0003256.npy) |
| 3257 | `model.layers.23.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 49.0 / 0.015927942593892415 / 1.6777003218760214 | [NPY](tensors/0003257.npy) |
| 3258 | `model.layers.23.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.25 / 24.75 / -0.12850379943847656 / 4.317828346826004 | [NPY](tensors/0003258.npy) |
| 3259 | `model.layers.23.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 49.0 / 0.015927942593892415 / 1.6777003218760214 | [NPY](tensors/0003259.npy) |
| 3260 | `model.layers.23.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -11.4375 / 11.1875 / 0.2762632369995117 / 3.9054901609008623 | [NPY](tensors/0003260.npy) |
| 3261 | `model.layers.23.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.875 / 6.875 / 0.012557591311633587 / 1.1916125365022012 | [NPY](tensors/0003261.npy) |
| 3262 | `model.layers.23.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2848.0 / 3024.0 / 2.2771727561950685 / 131.97804657619383 | [NPY](tensors/0003262.npy) |
| 3263 | `model.layers.23.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2848.0 / 3024.0 / 2.2771727561950685 / 131.97804657619383 | [NPY](tensors/0003263.npy) |
| 3264 | `model.layers.23.self_attn` | 27 | `output[1]` | [1, 64, 1, 324] | torch.bfloat16 → float32 | 7.494005416219807e-15 / 0.89453125 / 0.001171042407156858 / 0.012011855047973061 | [NPY](tensors/0003264.npy) |
| 3265 | `model.layers.23.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5984.0 / 6592.0 / 3.2733669704861112 / 392.55690814802927 | [NPY](tensors/0003265.npy) |
| 3266 | `model.layers.23.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 10.5625 / -0.013102791044447157 / 1.595413243583453 | [NPY](tensors/0003266.npy) |
| 3267 | `model.layers.23.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 10.5625 / -0.013102791044447157 / 1.595413243583453 | [NPY](tensors/0003267.npy) |
| 3268 | `model.layers.23.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -49.5 / 10.5625 / -0.013102791044447157 / 1.595413243583453 | [NPY](tensors/0003268.npy) |
| 3269 | `model.layers.23.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3270 | `model.layers.23.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3271 | `model.layers.23.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3272 | `model.layers.23.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2656.0 / 2608.0 / -0.6713551839192708 / 213.038854836989 | [NPY](tensors/0003272.npy) |
| 3273 | `model.layers.23.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2656.0 / 2608.0 / -0.6713551839192708 / 213.038854836989 | [NPY](tensors/0003273.npy) |
| 3274 | `model.layers.23.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.6875 / 2.34375 / 0.0997314453125 / 1.3987408474153142 | [NPY](tensors/0003274.npy) |
| 3275 | `model.layers.23` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6464.0 / 6688.0 / 2.591330295138889 / 468.5238918338613 | [NPY](tensors/0003275.npy) |
| 3354 | `model.layers.23` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6848.0 / 7744.0 / -0.5095974392361111 / 364.7835911574435 | [NPY](tensors/0003354.npy) |
| 3355 | `model.layers.23` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003355.npy) |
| 3356 | `model.layers.23` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0003356.npy) |
| 3357 | `model.layers.23` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0003357.npy) |
| 3358 | `model.layers.23` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0003358.npy) |
| 3359 | `model.layers.23` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3360 | `model.layers.23` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3361 | `model.layers.23` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3362 | `model.layers.23.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6848.0 / 7744.0 / -0.5095974392361111 / 364.7835911574435 | [NPY](tensors/0003362.npy) |
| 3363 | `model.layers.23.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 57.0 / 0.015228667524125841 / 1.7533409785370373 | [NPY](tensors/0003363.npy) |
| 3364 | `model.layers.23.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 57.0 / 0.015228667524125841 / 1.7533409785370373 | [NPY](tensors/0003364.npy) |
| 3365 | `model.layers.23.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003365.npy) |
| 3366 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0003366.npy) |
| 3367 | `model.layers.23.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3368 | `model.layers.23.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3369 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0003369.npy) |
| 3370 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0003370.npy) |
| 3371 | `model.layers.23.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3372 | `model.layers.23.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 57.0 / 0.015228667524125841 / 1.7533409785370373 | [NPY](tensors/0003372.npy) |
| 3373 | `model.layers.23.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.8125 / 18.125 / 0.05481089698150754 / 1.7301777110798393 | [NPY](tensors/0003373.npy) |
| 3374 | `model.layers.23.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 57.0 / 0.015228667524125841 / 1.7533409785370373 | [NPY](tensors/0003374.npy) |
| 3375 | `model.layers.23.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.75 / 30.625 / -0.11908456683158875 / 4.616535518918772 | [NPY](tensors/0003375.npy) |
| 3376 | `model.layers.23.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.5 / 57.0 / 0.015228667524125841 / 1.7533409785370373 | [NPY](tensors/0003376.npy) |
| 3377 | `model.layers.23.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.875 / 12.125 / 0.059522151947021484 / 3.5806555975535694 | [NPY](tensors/0003377.npy) |
| 3378 | `model.layers.23.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.75 / 10.4375 / 0.018975481623783708 / 1.2417097621226425 | [NPY](tensors/0003378.npy) |
| 3379 | `model.layers.23.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2400.0 / 2368.0 / 1.1367843204074435 / 120.32005109106116 | [NPY](tensors/0003379.npy) |
| 3380 | `model.layers.23.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2400.0 / 2368.0 / 1.1367843204074435 / 120.32005109106116 | [NPY](tensors/0003380.npy) |
| 3381 | `model.layers.23.self_attn` | 28 | `output[1]` | [1, 64, 1, 325] | torch.bfloat16 → float32 | 1.1102230246251565e-14 / 0.8828125 / 0.0014372027094071845 / 0.014610615001240956 | [NPY](tensors/0003381.npy) |
| 3382 | `model.layers.23.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5760.0 / 6656.0 / 0.6372694227430555 / 349.79873492007147 | [NPY](tensors/0003382.npy) |
| 3383 | `model.layers.23.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.75 / 13.0625 / -0.011659467220306396 / 1.4547660143638639 | [NPY](tensors/0003383.npy) |
| 3384 | `model.layers.23.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.75 / 13.0625 / -0.011659467220306396 / 1.4547660143638639 | [NPY](tensors/0003384.npy) |
| 3385 | `model.layers.23.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -42.75 / 13.0625 / -0.011659467220306396 / 1.4547660143638639 | [NPY](tensors/0003385.npy) |
| 3386 | `model.layers.23.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3387 | `model.layers.23.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3388 | `model.layers.23.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3389 | `model.layers.23.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3968.0 / 3936.0 / -0.9835018581814237 / 274.315067978547 | [NPY](tensors/0003389.npy) |
| 3390 | `model.layers.23.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3968.0 / 3936.0 / -0.9835018581814237 / 274.315067978547 | [NPY](tensors/0003390.npy) |
| 3391 | `model.layers.23.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -5.03125 / 3.15625 / 0.2034912109375 / 2.149333791174137 | [NPY](tensors/0003391.npy) |
| 3392 | `model.layers.23` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3008.0 / 3056.0 / -0.35604383680555557 / 324.51281501442514 | [NPY](tensors/0003392.npy) |
| 3471 | `model.layers.23` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6784.0 / 6656.0 / -2.6960015190972224 / 379.17087276223486 | [NPY](tensors/0003471.npy) |
| 3472 | `model.layers.23` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003472.npy) |
| 3473 | `model.layers.23` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0003473.npy) |
| 3474 | `model.layers.23` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0003474.npy) |
| 3475 | `model.layers.23` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0003475.npy) |
| 3476 | `model.layers.23` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3477 | `model.layers.23` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3478 | `model.layers.23` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3479 | `model.layers.23.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6784.0 / 6656.0 / -2.6960015190972224 / 379.17087276223486 | [NPY](tensors/0003479.npy) |
| 3480 | `model.layers.23.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 45.25 / 0.003246638509962294 / 1.666014029864387 | [NPY](tensors/0003480.npy) |
| 3481 | `model.layers.23.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 45.25 / 0.003246638509962294 / 1.666014029864387 | [NPY](tensors/0003481.npy) |
| 3482 | `model.layers.23.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003482.npy) |
| 3483 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0003483.npy) |
| 3484 | `model.layers.23.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3485 | `model.layers.23.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3486 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0003486.npy) |
| 3487 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0003487.npy) |
| 3488 | `model.layers.23.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3489 | `model.layers.23.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 45.25 / 0.003246638509962294 / 1.666014029864387 | [NPY](tensors/0003489.npy) |
| 3490 | `model.layers.23.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.0 / 17.875 / 0.03658123733475804 / 1.6807613472469982 | [NPY](tensors/0003490.npy) |
| 3491 | `model.layers.23.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 45.25 / 0.003246638509962294 / 1.666014029864387 | [NPY](tensors/0003491.npy) |
| 3492 | `model.layers.23.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.375 / 34.5 / -0.1874881200492382 / 4.667850591929902 | [NPY](tensors/0003492.npy) |
| 3493 | `model.layers.23.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 45.25 / 0.003246638509962294 / 1.666014029864387 | [NPY](tensors/0003493.npy) |
| 3494 | `model.layers.23.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.875 / 19.75 / 0.3447144627571106 / 4.668031044864549 | [NPY](tensors/0003494.npy) |
| 3495 | `model.layers.23.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.0 / 6.375 / -0.002670859801582992 / 1.2674448264975926 | [NPY](tensors/0003495.npy) |
| 3496 | `model.layers.23.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3088.0 / 3088.0 / 2.8308513853285047 / 132.76966353228931 | [NPY](tensors/0003496.npy) |
| 3497 | `model.layers.23.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3088.0 / 3088.0 / 2.8308513853285047 / 132.76966353228931 | [NPY](tensors/0003497.npy) |
| 3498 | `model.layers.23.self_attn` | 29 | `output[1]` | [1, 64, 1, 326] | torch.bfloat16 → float32 | 8.659739592076221e-15 / 0.87890625 / 0.0014217223709075447 / 0.011920257757897582 | [NPY](tensors/0003498.npy) |
| 3499 | `model.layers.23.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6560.0 / 6272.0 / 0.13791775173611112 / 390.19260844771986 | [NPY](tensors/0003499.npy) |
| 3500 | `model.layers.23.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 12.25 / -0.021682769722408717 / 1.4987916062633004 | [NPY](tensors/0003500.npy) |
| 3501 | `model.layers.23.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 12.25 / -0.021682769722408717 / 1.4987916062633004 | [NPY](tensors/0003501.npy) |
| 3502 | `model.layers.23.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -44.0 / 12.25 / -0.021682769722408717 / 1.4987916062633004 | [NPY](tensors/0003502.npy) |
| 3503 | `model.layers.23.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3504 | `model.layers.23.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3505 | `model.layers.23.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3506 | `model.layers.23.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4256.0 / 4288.0 / -1.833936987982856 / 234.3807296963021 | [NPY](tensors/0003506.npy) |
| 3507 | `model.layers.23.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4256.0 / 4288.0 / -1.833936987982856 / 234.3807296963021 | [NPY](tensors/0003507.npy) |
| 3508 | `model.layers.23.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.1875 / 2.546875 / 0.109100341796875 / 1.6185797118379952 | [NPY](tensors/0003508.npy) |
| 3509 | `model.layers.23` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2464.0 / 2176.0 / -1.6782443576388888 / 314.72004352184535 | [NPY](tensors/0003509.npy) |
| 3588 | `model.layers.23` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6112.0 / 6624.0 / 2.8729844835069445 / 358.38197094305167 | [NPY](tensors/0003588.npy) |
| 3589 | `model.layers.23` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003589.npy) |
| 3590 | `model.layers.23` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0003590.npy) |
| 3591 | `model.layers.23` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0003591.npy) |
| 3592 | `model.layers.23` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0003592.npy) |
| 3593 | `model.layers.23` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3594 | `model.layers.23` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3595 | `model.layers.23` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3596 | `model.layers.23.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6112.0 / 6624.0 / 2.8729844835069445 / 358.38197094305167 | [NPY](tensors/0003596.npy) |
| 3597 | `model.layers.23.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 49.75 / 0.02159803443484836 / 1.699676664136608 | [NPY](tensors/0003597.npy) |
| 3598 | `model.layers.23.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 49.75 / 0.02159803443484836 / 1.699676664136608 | [NPY](tensors/0003598.npy) |
| 3599 | `model.layers.23.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003599.npy) |
| 3600 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0003600.npy) |
| 3601 | `model.layers.23.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3602 | `model.layers.23.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3603 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0003603.npy) |
| 3604 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0003604.npy) |
| 3605 | `model.layers.23.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3606 | `model.layers.23.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 49.75 / 0.02159803443484836 / 1.699676664136608 | [NPY](tensors/0003606.npy) |
| 3607 | `model.layers.23.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.375 / 15.5625 / 0.06132592284120619 / 1.7693614674690286 | [NPY](tensors/0003607.npy) |
| 3608 | `model.layers.23.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 49.75 / 0.02159803443484836 / 1.699676664136608 | [NPY](tensors/0003608.npy) |
| 3609 | `model.layers.23.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.5 / 41.0 / -0.07853388786315918 / 4.904020759721014 | [NPY](tensors/0003609.npy) |
| 3610 | `model.layers.23.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 49.75 / 0.02159803443484836 / 1.699676664136608 | [NPY](tensors/0003610.npy) |
| 3611 | `model.layers.23.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -22.5 / 10.6875 / 0.17505967617034912 / 3.9942320635562285 | [NPY](tensors/0003611.npy) |
| 3612 | `model.layers.23.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -18.625 / 9.375 / -0.00047361187171190977 / 1.247840730950896 | [NPY](tensors/0003612.npy) |
| 3613 | `model.layers.23.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3232.0 / 3280.0 / 0.5344736735026042 / 145.45214714454838 | [NPY](tensors/0003613.npy) |
| 3614 | `model.layers.23.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3232.0 / 3280.0 / 0.5344736735026042 / 145.45214714454838 | [NPY](tensors/0003614.npy) |
| 3615 | `model.layers.23.self_attn` | 30 | `output[1]` | [1, 64, 1, 327] | torch.bfloat16 → float32 | 7.93809462606987e-15 / 0.83203125 / 0.001185132855026401 / 0.013326508203824255 | [NPY](tensors/0003615.npy) |
| 3616 | `model.layers.23.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5856.0 / 6304.0 / 3.4013271755642362 / 386.3517109486953 | [NPY](tensors/0003616.npy) |
| 3617 | `model.layers.23.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 11.875 / -0.005560547113418579 / 1.4877827468990035 | [NPY](tensors/0003617.npy) |
| 3618 | `model.layers.23.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 11.875 / -0.005560547113418579 / 1.4877827468990035 | [NPY](tensors/0003618.npy) |
| 3619 | `model.layers.23.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -43.25 / 11.875 / -0.005560547113418579 / 1.4877827468990035 | [NPY](tensors/0003619.npy) |
| 3620 | `model.layers.23.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3621 | `model.layers.23.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3622 | `model.layers.23.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3623 | `model.layers.23.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5280.0 / 4608.0 / -5.696517266167534 / 295.84039367830496 | [NPY](tensors/0003623.npy) |
| 3624 | `model.layers.23.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5280.0 / 4608.0 / -5.696517266167534 / 295.84039367830496 | [NPY](tensors/0003624.npy) |
| 3625 | `model.layers.23.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.34375 / 2.734375 / 0.14363861083984375 / 1.7864967115333177 | [NPY](tensors/0003625.npy) |
| 3626 | `model.layers.23` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3264.0 / 1872.0 / -2.2706814236111112 / 329.22180336950566 | [NPY](tensors/0003626.npy) |
| 3705 | `model.layers.23` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 6208.0 / 4.872507052951389 / 340.10476162824244 | [NPY](tensors/0003705.npy) |
| 3706 | `model.layers.23` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003706.npy) |
| 3707 | `model.layers.23` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0003707.npy) |
| 3708 | `model.layers.23` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0003708.npy) |
| 3709 | `model.layers.23` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0003709.npy) |
| 3710 | `model.layers.23` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3711 | `model.layers.23` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3712 | `model.layers.23` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3713 | `model.layers.23.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 6208.0 / 4.872507052951389 / 340.10476162824244 | [NPY](tensors/0003713.npy) |
| 3714 | `model.layers.23.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 44.5 / 0.031826326582166886 / 1.6396671423353275 | [NPY](tensors/0003714.npy) |
| 3715 | `model.layers.23.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 44.5 / 0.031826326582166886 / 1.6396671423353275 | [NPY](tensors/0003715.npy) |
| 3716 | `model.layers.23.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003716.npy) |
| 3717 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0003717.npy) |
| 3718 | `model.layers.23.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3719 | `model.layers.23.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3720 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0003720.npy) |
| 3721 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0003721.npy) |
| 3722 | `model.layers.23.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3723 | `model.layers.23.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 44.5 / 0.031826326582166886 / 1.6396671423353275 | [NPY](tensors/0003723.npy) |
| 3724 | `model.layers.23.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.125 / 18.125 / 0.05505217262543738 / 1.8559987979661579 | [NPY](tensors/0003724.npy) |
| 3725 | `model.layers.23.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 44.5 / 0.031826326582166886 / 1.6396671423353275 | [NPY](tensors/0003725.npy) |
| 3726 | `model.layers.23.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.25 / 46.25 / 0.03698056936264038 / 4.930245300964486 | [NPY](tensors/0003726.npy) |
| 3727 | `model.layers.23.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.75 / 44.5 / 0.031826326582166886 / 1.6396671423353275 | [NPY](tensors/0003727.npy) |
| 3728 | `model.layers.23.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.25 / 12.375 / -0.27604007720947266 / 4.04143221941497 | [NPY](tensors/0003728.npy) |
| 3729 | `model.layers.23.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -19.5 / 11.25 / -0.027842551862704568 / 1.3750903724453971 | [NPY](tensors/0003729.npy) |
| 3730 | `model.layers.23.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3312.0 / 3344.0 / -0.9579396565755208 / 157.14715822324075 | [NPY](tensors/0003730.npy) |
| 3731 | `model.layers.23.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3312.0 / 3344.0 / -0.9579396565755208 / 157.14715822324075 | [NPY](tensors/0003731.npy) |
| 3732 | `model.layers.23.self_attn` | 31 | `output[1]` | [1, 64, 1, 328] | torch.bfloat16 → float32 | 4.926614671774132e-16 / 0.9453125 / 0.0012917996003576975 / 0.01576458096477455 | [NPY](tensors/0003732.npy) |
| 3733 | `model.layers.23.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5408.0 / 6112.0 / 3.9246039496527776 / 374.313893213614 | [NPY](tensors/0003733.npy) |
| 3734 | `model.layers.23.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 10.75 / 0.0009568068716261121 / 1.4247015381601433 | [NPY](tensors/0003734.npy) |
| 3735 | `model.layers.23.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 10.75 / 0.0009568068716261121 / 1.4247015381601433 | [NPY](tensors/0003735.npy) |
| 3736 | `model.layers.23.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -39.25 / 10.75 / 0.0009568068716261121 / 1.4247015381601433 | [NPY](tensors/0003736.npy) |
| 3737 | `model.layers.23.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3738 | `model.layers.23.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3739 | `model.layers.23.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3740 | `model.layers.23.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5376.0 / 4832.0 / -5.2511481391059025 / 305.7523535274164 | [NPY](tensors/0003740.npy) |
| 3741 | `model.layers.23.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5376.0 / 4832.0 / -5.2511481391059025 / 305.7523535274164 | [NPY](tensors/0003741.npy) |
| 3742 | `model.layers.23.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.8125 / 2.6875 / 0.13616943359375 / 1.621756929305965 | [NPY](tensors/0003742.npy) |
| 3743 | `model.layers.23` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2592.0 / 1704.0 / -1.3212944878472221 / 340.02719870797273 | [NPY](tensors/0003743.npy) |
| 3822 | `model.layers.23` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 10240.0 / 0.8884358723958333 / 465.3982101998098 | [NPY](tensors/0003822.npy) |
| 3823 | `model.layers.23` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003823.npy) |
| 3824 | `model.layers.23` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0003824.npy) |
| 3825 | `model.layers.23` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0003825.npy) |
| 3826 | `model.layers.23` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0003826.npy) |
| 3827 | `model.layers.23` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3828 | `model.layers.23` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3829 | `model.layers.23` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3830 | `model.layers.23.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 10240.0 / 0.8884358723958333 / 465.3982101998098 | [NPY](tensors/0003830.npy) |
| 3831 | `model.layers.23.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 59.25 / 0.015693603621588812 / 1.7674310176590116 | [NPY](tensors/0003831.npy) |
| 3832 | `model.layers.23.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 59.25 / 0.015693603621588812 / 1.7674310176590116 | [NPY](tensors/0003832.npy) |
| 3833 | `model.layers.23.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003833.npy) |
| 3834 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0003834.npy) |
| 3835 | `model.layers.23.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3836 | `model.layers.23.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3837 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0003837.npy) |
| 3838 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0003838.npy) |
| 3839 | `model.layers.23.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3840 | `model.layers.23.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 59.25 / 0.015693603621588812 / 1.7674310176590116 | [NPY](tensors/0003840.npy) |
| 3841 | `model.layers.23.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.125 / 16.125 / 0.048421936109662056 / 1.5327624186875213 | [NPY](tensors/0003841.npy) |
| 3842 | `model.layers.23.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 59.25 / 0.015693603621588812 / 1.7674310176590116 | [NPY](tensors/0003842.npy) |
| 3843 | `model.layers.23.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.375 / 28.0 / -0.12126746028661728 / 4.104019961064713 | [NPY](tensors/0003843.npy) |
| 3844 | `model.layers.23.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 59.25 / 0.015693603621588812 / 1.7674310176590116 | [NPY](tensors/0003844.npy) |
| 3845 | `model.layers.23.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.1875 / 13.875 / 0.16324687004089355 / 4.00619603372651 | [NPY](tensors/0003845.npy) |
| 3846 | `model.layers.23.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.4375 / 7.34375 / 0.02141554350964725 / 1.19429105991797 | [NPY](tensors/0003846.npy) |
| 3847 | `model.layers.23.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2896.0 / 3056.0 / 2.757200304667155 / 151.80346565590943 | [NPY](tensors/0003847.npy) |
| 3848 | `model.layers.23.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2896.0 / 3056.0 / 2.757200304667155 / 151.80346565590943 | [NPY](tensors/0003848.npy) |
| 3849 | `model.layers.23.self_attn` | 32 | `output[1]` | [1, 64, 1, 329] | torch.bfloat16 → float32 | 2.7533531010703882e-14 / 0.80078125 / 0.0014350300258739953 / 0.010164686121248693 | [NPY](tensors/0003849.npy) |
| 3850 | `model.layers.23.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7392.0 / 8128.0 / 3.641552734375 / 427.7061145095611 | [NPY](tensors/0003850.npy) |
| 3851 | `model.layers.23.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 11.75 / -0.01351565784878201 / 1.4358588541937019 | [NPY](tensors/0003851.npy) |
| 3852 | `model.layers.23.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.25 / 11.75 / -0.01351565784878201 / 1.4358588541937019 | [NPY](tensors/0003852.npy) |
| 3853 | `model.layers.23.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -44.25 / 11.75 / -0.01351565784878201 / 1.4358588541937019 | [NPY](tensors/0003853.npy) |
| 3854 | `model.layers.23.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3855 | `model.layers.23.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3856 | `model.layers.23.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3857 | `model.layers.23.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4832.0 / 4928.0 / -3.65863528781467 / 254.4807412738391 | [NPY](tensors/0003857.npy) |
| 3858 | `model.layers.23.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4832.0 / 4928.0 / -3.65863528781467 / 254.4807412738391 | [NPY](tensors/0003858.npy) |
| 3859 | `model.layers.23.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.1875 / 2.03125 / 0.0535888671875 / 1.565663677773348 | [NPY](tensors/0003859.npy) |
| 3860 | `model.layers.23` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2560.0 / 3296.0 / -0.0263671875 / 316.7429137030631 | [NPY](tensors/0003860.npy) |
| 3939 | `model.layers.23` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11392.0 / 11456.0 / 0.0207763671875 / 511.10033506094237 | [NPY](tensors/0003939.npy) |
| 3940 | `model.layers.23` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 330] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003940.npy) |
| 3941 | `model.layers.23` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0003941.npy) |
| 3942 | `model.layers.23` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0003942.npy) |
| 3943 | `model.layers.23` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0003943.npy) |
| 3944 | `model.layers.23` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3945 | `model.layers.23` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3946 | `model.layers.23` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3947 | `model.layers.23.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11392.0 / 11456.0 / 0.0207763671875 / 511.10033506094237 | [NPY](tensors/0003947.npy) |
| 3948 | `model.layers.23.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 60.25 / 0.011846649646759033 / 1.7711662536451318 | [NPY](tensors/0003948.npy) |
| 3949 | `model.layers.23.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 60.25 / 0.011846649646759033 / 1.7711662536451318 | [NPY](tensors/0003949.npy) |
| 3950 | `model.layers.23.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 330] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003950.npy) |
| 3951 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0003951.npy) |
| 3952 | `model.layers.23.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3953 | `model.layers.23.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3954 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0003954.npy) |
| 3955 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0003955.npy) |
| 3956 | `model.layers.23.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3957 | `model.layers.23.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 60.25 / 0.011846649646759033 / 1.7711662536451318 | [NPY](tensors/0003957.npy) |
| 3958 | `model.layers.23.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.25 / 12.4375 / 0.05289991619065404 / 1.310979412070991 | [NPY](tensors/0003958.npy) |
| 3959 | `model.layers.23.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 60.25 / 0.011846649646759033 / 1.7711662536451318 | [NPY](tensors/0003959.npy) |
| 3960 | `model.layers.23.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.0 / 36.0 / -0.07092150300741196 / 4.3469109128677985 | [NPY](tensors/0003960.npy) |
| 3961 | `model.layers.23.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 60.25 / 0.011846649646759033 / 1.7711662536451318 | [NPY](tensors/0003961.npy) |
| 3962 | `model.layers.23.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -20.875 / 7.59375 / -0.05499356985092163 / 2.6389641666569092 | [NPY](tensors/0003962.npy) |
| 3963 | `model.layers.23.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.875 / 6.21875 / 0.006579346605576575 / 1.1853691800051567 | [NPY](tensors/0003963.npy) |
| 3964 | `model.layers.23.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5248.0 / 5504.0 / 4.9357247670491535 / 230.57522421520673 | [NPY](tensors/0003964.npy) |
| 3965 | `model.layers.23.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5248.0 / 5504.0 / 4.9357247670491535 / 230.57522421520673 | [NPY](tensors/0003965.npy) |
| 3966 | `model.layers.23.self_attn` | 33 | `output[1]` | [1, 64, 1, 330] | torch.bfloat16 → float32 | 2.4868995751603507e-13 / 0.76171875 / 0.0017059121482143535 / 0.011923614181231551 | [NPY](tensors/0003966.npy) |
| 3967 | `model.layers.23.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11136.0 / 11264.0 / 4.962310112847222 / 575.0821037501385 | [NPY](tensors/0003967.npy) |
| 3968 | `model.layers.23.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 6.03125 / -0.0054334176911248104 / 1.0859615185307443 | [NPY](tensors/0003968.npy) |
| 3969 | `model.layers.23.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 6.03125 / -0.0054334176911248104 / 1.0859615185307443 | [NPY](tensors/0003969.npy) |
| 3970 | `model.layers.23.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.0 / 6.03125 / -0.0054334176911248104 / 1.0859615185307443 | [NPY](tensors/0003970.npy) |
| 3971 | `model.layers.23.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3972 | `model.layers.23.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3973 | `model.layers.23.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3974 | `model.layers.23.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1688.0 / 1472.0 / -3.472469520568848 / 105.40141461243306 | [NPY](tensors/0003974.npy) |
| 3975 | `model.layers.23.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1688.0 / 1472.0 / -3.472469520568848 / 105.40141461243306 | [NPY](tensors/0003975.npy) |
| 3976 | `model.layers.23.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.140625 / 1.5859375 / -0.038982391357421875 / 0.8148186259230903 | [NPY](tensors/0003976.npy) |
| 3977 | `model.layers.23` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 10304.0 / 1.4787217881944446 / 546.3967601676192 | [NPY](tensors/0003977.npy) |
| 4056 | `model.layers.23` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 9600.0 / 0.4848442925347222 / 456.9447919985986 | [NPY](tensors/0004056.npy) |
| 4057 | `model.layers.23` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 331] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004057.npy) |
| 4058 | `model.layers.23` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0004058.npy) |
| 4059 | `model.layers.23` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0004059.npy) |
| 4060 | `model.layers.23` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0004060.npy) |
| 4061 | `model.layers.23` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4062 | `model.layers.23` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4063 | `model.layers.23` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4064 | `model.layers.23.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 9600.0 / 0.4848442925347222 / 456.9447919985986 | [NPY](tensors/0004064.npy) |
| 4065 | `model.layers.23.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 56.0 / 0.014423149824142455 / 1.7483199942146022 | [NPY](tensors/0004065.npy) |
| 4066 | `model.layers.23.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 56.0 / 0.014423149824142455 / 1.7483199942146022 | [NPY](tensors/0004066.npy) |
| 4067 | `model.layers.23.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 331] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004067.npy) |
| 4068 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0004068.npy) |
| 4069 | `model.layers.23.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4070 | `model.layers.23.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4071 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0004071.npy) |
| 4072 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0004072.npy) |
| 4073 | `model.layers.23.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4074 | `model.layers.23.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 56.0 / 0.014423149824142455 / 1.7483199942146022 | [NPY](tensors/0004074.npy) |
| 4075 | `model.layers.23.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.3125 / 17.875 / 0.039300597156398 / 1.3763066794666468 | [NPY](tensors/0004075.npy) |
| 4076 | `model.layers.23.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 56.0 / 0.014423149824142455 / 1.7483199942146022 | [NPY](tensors/0004076.npy) |
| 4077 | `model.layers.23.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.0 / 36.0 / -0.11007484793663025 / 4.976788427269218 | [NPY](tensors/0004077.npy) |
| 4078 | `model.layers.23.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 56.0 / 0.014423149824142455 / 1.7483199942146022 | [NPY](tensors/0004078.npy) |
| 4079 | `model.layers.23.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -20.875 / 11.8125 / -0.15062427520751953 / 3.5767513646460274 | [NPY](tensors/0004079.npy) |
| 4080 | `model.layers.23.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.5 / 5.03125 / 0.0016551257140235975 / 1.247717982801709 | [NPY](tensors/0004080.npy) |
| 4081 | `model.layers.23.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5792.0 / 6048.0 / 5.564828681945801 / 262.1034563018628 | [NPY](tensors/0004081.npy) |
| 4082 | `model.layers.23.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5792.0 / 6048.0 / 5.564828681945801 / 262.1034563018628 | [NPY](tensors/0004082.npy) |
| 4083 | `model.layers.23.self_attn` | 34 | `output[1]` | [1, 64, 1, 331] | torch.bfloat16 → float32 | 7.904787935331115e-14 / 0.74609375 / 0.0018294668444063184 / 0.011447548081764646 | [NPY](tensors/0004083.npy) |
| 4084 | `model.layers.23.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 9792.0 / 6.033371310763889 / 555.5055545524918 | [NPY](tensors/0004084.npy) |
| 4085 | `model.layers.23.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 5.84375 / -0.007213606105910407 / 1.0293768978220739 | [NPY](tensors/0004085.npy) |
| 4086 | `model.layers.23.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 5.84375 / -0.007213606105910407 / 1.0293768978220739 | [NPY](tensors/0004086.npy) |
| 4087 | `model.layers.23.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.25 / 5.84375 / -0.007213606105910407 / 1.0293768978220739 | [NPY](tensors/0004087.npy) |
| 4088 | `model.layers.23.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4089 | `model.layers.23.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4090 | `model.layers.23.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4091 | `model.layers.23.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1784.0 / 1800.0 / -2.4623475816514757 / 122.6281521232112 | [NPY](tensors/0004091.npy) |
| 4092 | `model.layers.23.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1784.0 / 1800.0 / -2.4623475816514757 / 122.6281521232112 | [NPY](tensors/0004092.npy) |
| 4093 | `model.layers.23.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.484375 / 1.1796875 / 0.030059814453125 / 0.8676355848516858 | [NPY](tensors/0004093.npy) |
| 4094 | `model.layers.23` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 8000.0 / 3.5398274739583333 / 481.17380064761625 | [NPY](tensors/0004094.npy) |
| 4173 | `model.layers.23` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9792.0 / -1.4726671006944445 / 452.1840844778476 | [NPY](tensors/0004173.npy) |
| 4174 | `model.layers.23` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 332] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004174.npy) |
| 4175 | `model.layers.23` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0004175.npy) |
| 4176 | `model.layers.23` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0004176.npy) |
| 4177 | `model.layers.23` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0004177.npy) |
| 4178 | `model.layers.23` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4179 | `model.layers.23` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4180 | `model.layers.23` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4181 | `model.layers.23.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9792.0 / -1.4726671006944445 / 452.1840844778476 | [NPY](tensors/0004181.npy) |
| 4182 | `model.layers.23.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.25 / 0.009202455149756537 / 1.7633032660936792 | [NPY](tensors/0004182.npy) |
| 4183 | `model.layers.23.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.25 / 0.009202455149756537 / 1.7633032660936792 | [NPY](tensors/0004183.npy) |
| 4184 | `model.layers.23.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 332] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004184.npy) |
| 4185 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0004185.npy) |
| 4186 | `model.layers.23.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4187 | `model.layers.23.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4188 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0004188.npy) |
| 4189 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0004189.npy) |
| 4190 | `model.layers.23.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4191 | `model.layers.23.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.25 / 0.009202455149756537 / 1.7633032660936792 | [NPY](tensors/0004191.npy) |
| 4192 | `model.layers.23.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.75 / 14.6875 / 0.051107642939314246 / 1.482416279147686 | [NPY](tensors/0004192.npy) |
| 4193 | `model.layers.23.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.25 / 0.009202455149756537 / 1.7633032660936792 | [NPY](tensors/0004193.npy) |
| 4194 | `model.layers.23.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -41.75 / 40.5 / -0.13954422622919083 / 4.982071758662175 | [NPY](tensors/0004194.npy) |
| 4195 | `model.layers.23.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 58.25 / 0.009202455149756537 / 1.7633032660936792 | [NPY](tensors/0004195.npy) |
| 4196 | `model.layers.23.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -21.0 / 10.4375 / 0.06098639965057373 / 3.204504774080666 | [NPY](tensors/0004196.npy) |
| 4197 | `model.layers.23.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -18.875 / 8.875 / 0.03661021590232849 / 1.543627448724939 | [NPY](tensors/0004197.npy) |
| 4198 | `model.layers.23.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3728.0 / 3776.0 / 7.313944837782118 / 175.6320937053386 | [NPY](tensors/0004198.npy) |
| 4199 | `model.layers.23.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3728.0 / 3776.0 / 7.313944837782118 / 175.6320937053386 | [NPY](tensors/0004199.npy) |
| 4200 | `model.layers.23.self_attn` | 35 | `output[1]` | [1, 64, 1, 332] | torch.bfloat16 → float32 | 1.7053025658242404e-13 / 0.859375 / 0.001626405996963598 / 0.015882593080577847 | [NPY](tensors/0004200.npy) |
| 4201 | `model.layers.23.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8832.0 / 8896.0 / 5.824153645833333 / 467.210363986654 | [NPY](tensors/0004201.npy) |
| 4202 | `model.layers.23.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 12.625 / 0.005851920445760091 / 1.2119523798017706 | [NPY](tensors/0004202.npy) |
| 4203 | `model.layers.23.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.0 / 12.625 / 0.005851920445760091 / 1.2119523798017706 | [NPY](tensors/0004203.npy) |
| 4204 | `model.layers.23.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.0 / 12.625 / 0.005851920445760091 / 1.2119523798017706 | [NPY](tensors/0004204.npy) |
| 4205 | `model.layers.23.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4206 | `model.layers.23.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4207 | `model.layers.23.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4208 | `model.layers.23.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1552.0 / 1544.0 / -0.4947767893473307 / 126.68254243601922 | [NPY](tensors/0004208.npy) |
| 4209 | `model.layers.23.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1552.0 / 1544.0 / -0.4947767893473307 / 126.68254243601922 | [NPY](tensors/0004209.npy) |
| 4210 | `model.layers.23.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.375 / 2.1875 / 0.103271484375 / 1.8189500777318242 | [NPY](tensors/0004210.npy) |
| 4211 | `model.layers.23` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7296.0 / 7360.0 / 5.313151041666667 / 434.95313840394215 | [NPY](tensors/0004211.npy) |
| 4290 | `model.layers.23` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7936.0 / 8320.0 / 0.9970235188802083 / 408.5121866250388 | [NPY](tensors/0004290.npy) |
| 4291 | `model.layers.23` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 333] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004291.npy) |
| 4292 | `model.layers.23` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0004292.npy) |
| 4293 | `model.layers.23` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0004293.npy) |
| 4294 | `model.layers.23` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0004294.npy) |
| 4295 | `model.layers.23` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4296 | `model.layers.23` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4297 | `model.layers.23` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4298 | `model.layers.23.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7936.0 / 8320.0 / 0.9970235188802083 / 408.5121866250388 | [NPY](tensors/0004298.npy) |
| 4299 | `model.layers.23.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 54.75 / 0.020053729746076797 / 1.7273629692912786 | [NPY](tensors/0004299.npy) |
| 4300 | `model.layers.23.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 54.75 / 0.020053729746076797 / 1.7273629692912786 | [NPY](tensors/0004300.npy) |
| 4301 | `model.layers.23.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 333] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004301.npy) |
| 4302 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0004302.npy) |
| 4303 | `model.layers.23.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4304 | `model.layers.23.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4305 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0004305.npy) |
| 4306 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0004306.npy) |
| 4307 | `model.layers.23.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4308 | `model.layers.23.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 54.75 / 0.020053729746076797 / 1.7273629692912786 | [NPY](tensors/0004308.npy) |
| 4309 | `model.layers.23.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.1875 / 15.75 / 0.046584582538343966 / 1.6453394377481738 | [NPY](tensors/0004309.npy) |
| 4310 | `model.layers.23.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 54.75 / 0.020053729746076797 / 1.7273629692912786 | [NPY](tensors/0004310.npy) |
| 4311 | `model.layers.23.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.75 / 27.0 / -0.13539612293243408 / 4.972386113888094 | [NPY](tensors/0004311.npy) |
| 4312 | `model.layers.23.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 54.75 / 0.020053729746076797 / 1.7273629692912786 | [NPY](tensors/0004312.npy) |
| 4313 | `model.layers.23.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.125 / 14.125 / 0.03294563293457031 / 3.5514135737414985 | [NPY](tensors/0004313.npy) |
| 4314 | `model.layers.23.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -18.75 / 13.375 / 0.0010256091482006013 / 1.825343741836779 | [NPY](tensors/0004314.npy) |
| 4315 | `model.layers.23.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3920.0 / 3936.0 / 6.470174577501085 / 182.49198375662166 | [NPY](tensors/0004315.npy) |
| 4316 | `model.layers.23.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3920.0 / 3936.0 / 6.470174577501085 / 182.49198375662166 | [NPY](tensors/0004316.npy) |
| 4317 | `model.layers.23.self_attn` | 36 | `output[1]` | [1, 64, 1, 333] | torch.bfloat16 → float32 | 2.5757174171303632e-14 / 0.9609375 / 0.0018513044175341264 / 0.01822402515636753 | [NPY](tensors/0004317.npy) |
| 4318 | `model.layers.23.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7584.0 / 8192.0 / 7.480902777777778 / 447.2963965753323 | [NPY](tensors/0004318.npy) |
| 4319 | `model.layers.23.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 11.4375 / 0.004157115353478326 / 1.3248968463034565 | [NPY](tensors/0004319.npy) |
| 4320 | `model.layers.23.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.5 / 11.4375 / 0.004157115353478326 / 1.3248968463034565 | [NPY](tensors/0004320.npy) |
| 4321 | `model.layers.23.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -43.5 / 11.4375 / 0.004157115353478326 / 1.3248968463034565 | [NPY](tensors/0004321.npy) |
| 4322 | `model.layers.23.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4323 | `model.layers.23.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4324 | `model.layers.23.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4325 | `model.layers.23.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2240.0 / 1928.0 / -2.548875766330295 / 130.81667320322958 | [NPY](tensors/0004325.npy) |
| 4326 | `model.layers.23.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2240.0 / 1928.0 / -2.548875766330295 / 130.81667320322958 | [NPY](tensors/0004326.npy) |
| 4327 | `model.layers.23.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.859375 / 2.078125 / 0.2066650390625 / 1.6425282973126525 | [NPY](tensors/0004327.npy) |
| 4328 | `model.layers.23` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5696.0 / 5952.0 / 4.935091145833334 / 387.0522403567332 | [NPY](tensors/0004328.npy) |
| 4407 | `model.layers.23` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7296.0 / 7488.0 / -4.741908094618055 / 367.1887420730633 | [NPY](tensors/0004407.npy) |
| 4408 | `model.layers.23` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 334] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004408.npy) |
| 4409 | `model.layers.23` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0004409.npy) |
| 4410 | `model.layers.23` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0004410.npy) |
| 4411 | `model.layers.23` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0004411.npy) |
| 4412 | `model.layers.23` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4413 | `model.layers.23` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4414 | `model.layers.23` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4415 | `model.layers.23.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7296.0 / 7488.0 / -4.741908094618055 / 367.1887420730633 | [NPY](tensors/0004415.npy) |
| 4416 | `model.layers.23.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 54.75 / -0.00362007286813524 / 1.7210517119835427 | [NPY](tensors/0004416.npy) |
| 4417 | `model.layers.23.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 54.75 / -0.00362007286813524 / 1.7210517119835427 | [NPY](tensors/0004417.npy) |
| 4418 | `model.layers.23.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 334] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004418.npy) |
| 4419 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0004419.npy) |
| 4420 | `model.layers.23.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4421 | `model.layers.23.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4422 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0004422.npy) |
| 4423 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0004423.npy) |
| 4424 | `model.layers.23.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4425 | `model.layers.23.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 54.75 / -0.00362007286813524 / 1.7210517119835427 | [NPY](tensors/0004425.npy) |
| 4426 | `model.layers.23.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.3125 / 18.375 / 0.0332052675075829 / 1.7831590665798835 | [NPY](tensors/0004426.npy) |
| 4427 | `model.layers.23.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 54.75 / -0.00362007286813524 / 1.7210517119835427 | [NPY](tensors/0004427.npy) |
| 4428 | `model.layers.23.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.75 / 42.5 / -0.015459656715393066 / 4.026615752066422 | [NPY](tensors/0004428.npy) |
| 4429 | `model.layers.23.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.0 / 54.75 / -0.00362007286813524 / 1.7210517119835427 | [NPY](tensors/0004429.npy) |
| 4430 | `model.layers.23.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.5 / 14.25 / -0.060101866722106934 / 2.805159823391102 | [NPY](tensors/0004430.npy) |
| 4431 | `model.layers.23.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -18.75 / 10.875 / 0.013126541714882478 / 1.699638890239081 | [NPY](tensors/0004431.npy) |
| 4432 | `model.layers.23.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3440.0 / 3536.0 / 5.955268266465929 / 180.53710537546047 | [NPY](tensors/0004432.npy) |
| 4433 | `model.layers.23.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3440.0 / 3536.0 / 5.955268266465929 / 180.53710537546047 | [NPY](tensors/0004433.npy) |
| 4434 | `model.layers.23.self_attn` | 37 | `output[1]` | [1, 64, 1, 334] | torch.bfloat16 → float32 | 1.7889335846010823e-17 / 0.9375 / 0.0018371042120635054 / 0.017095059084898275 | [NPY](tensors/0004434.npy) |
| 4435 | `model.layers.23.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6464.0 / 6656.0 / 1.2135091145833334 / 399.52746691314326 | [NPY](tensors/0004435.npy) |
| 4436 | `model.layers.23.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 11.4375 / -0.009711946381462945 / 1.339140131555001 | [NPY](tensors/0004436.npy) |
| 4437 | `model.layers.23.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.75 / 11.4375 / -0.009711946381462945 / 1.339140131555001 | [NPY](tensors/0004437.npy) |
| 4438 | `model.layers.23.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.75 / 11.4375 / -0.009711946381462945 / 1.339140131555001 | [NPY](tensors/0004438.npy) |
| 4439 | `model.layers.23.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4440 | `model.layers.23.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4441 | `model.layers.23.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4442 | `model.layers.23.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3984.0 / 4160.0 / 0.3269481235080295 / 210.97347845919373 | [NPY](tensors/0004442.npy) |
| 4443 | `model.layers.23.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3984.0 / 4160.0 / 0.3269481235080295 / 210.97347845919373 | [NPY](tensors/0004443.npy) |
| 4444 | `model.layers.23.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.890625 / 1.96875 / 0.27239990234375 / 1.7722958816306529 | [NPY](tensors/0004444.npy) |
| 4445 | `model.layers.23` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2304.0 / 2672.0 / 1.5507988823784722 / 307.8664582968442 | [NPY](tensors/0004445.npy) |
| 4524 | `model.layers.23` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7904.0 / 8384.0 / -1.8654513888888888 / 419.29701372171274 | [NPY](tensors/0004524.npy) |
| 4525 | `model.layers.23` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 335] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004525.npy) |
| 4526 | `model.layers.23` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0004526.npy) |
| 4527 | `model.layers.23` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0004527.npy) |
| 4528 | `model.layers.23` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0004528.npy) |
| 4529 | `model.layers.23` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4530 | `model.layers.23` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4531 | `model.layers.23` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4532 | `model.layers.23.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7904.0 / 8384.0 / -1.8654513888888888 / 419.29701372171274 | [NPY](tensors/0004532.npy) |
| 4533 | `model.layers.23.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.75 / 53.75 / 0.008467033174302844 / 1.711881253261 | [NPY](tensors/0004533.npy) |
| 4534 | `model.layers.23.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.75 / 53.75 / 0.008467033174302844 / 1.711881253261 | [NPY](tensors/0004534.npy) |
| 4535 | `model.layers.23.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 335] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004535.npy) |
| 4536 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0004536.npy) |
| 4537 | `model.layers.23.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4538 | `model.layers.23.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4539 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0004539.npy) |
| 4540 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0004540.npy) |
| 4541 | `model.layers.23.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4542 | `model.layers.23.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.75 / 53.75 / 0.008467033174302844 / 1.711881253261 | [NPY](tensors/0004542.npy) |
| 4543 | `model.layers.23.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.125 / 14.25 / 0.05562404356896877 / 1.583621898978626 | [NPY](tensors/0004543.npy) |
| 4544 | `model.layers.23.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.75 / 53.75 / 0.008467033174302844 / 1.711881253261 | [NPY](tensors/0004544.npy) |
| 4545 | `model.layers.23.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -57.0 / 38.25 / -0.1317345555871725 / 5.494112352543256 | [NPY](tensors/0004545.npy) |
| 4546 | `model.layers.23.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.75 / 53.75 / 0.008467033174302844 / 1.711881253261 | [NPY](tensors/0004546.npy) |
| 4547 | `model.layers.23.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.375 / 12.875 / -0.13671303540468216 / 3.3907488824508447 | [NPY](tensors/0004547.npy) |
| 4548 | `model.layers.23.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -23.75 / 8.0625 / -0.0343382079154253 / 1.5749555458009648 | [NPY](tensors/0004548.npy) |
| 4549 | `model.layers.23.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6304.0 / 6496.0 / 6.764633708530003 / 294.2547139678558 | [NPY](tensors/0004549.npy) |
| 4550 | `model.layers.23.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6304.0 / 6496.0 / 6.764633708530003 / 294.2547139678558 | [NPY](tensors/0004550.npy) |
| 4551 | `model.layers.23.self_attn` | 38 | `output[1]` | [1, 64, 1, 335] | torch.bfloat16 → float32 | 8.482103908136196e-14 / 0.85546875 / 0.0017262917752757343 / 0.01472930974634321 | [NPY](tensors/0004551.npy) |
| 4552 | `model.layers.23.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9856.0 / 4.881277126736111 / 568.8052521591007 | [NPY](tensors/0004552.npy) |
| 4553 | `model.layers.23.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 9.25 / -0.007956049177381727 / 1.1380341562344038 | [NPY](tensors/0004553.npy) |
| 4554 | `model.layers.23.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 9.25 / -0.007956049177381727 / 1.1380341562344038 | [NPY](tensors/0004554.npy) |
| 4555 | `model.layers.23.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -40.5 / 9.25 / -0.007956049177381727 / 1.1380341562344038 | [NPY](tensors/0004555.npy) |
| 4556 | `model.layers.23.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4557 | `model.layers.23.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4558 | `model.layers.23.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4559 | `model.layers.23.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2320.0 / 2352.0 / 0.27482087877061634 / 138.36055843389843 | [NPY](tensors/0004559.npy) |
| 4560 | `model.layers.23.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2320.0 / 2352.0 / 0.27482087877061634 / 138.36055843389843 | [NPY](tensors/0004560.npy) |
| 4561 | `model.layers.23.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.546875 / 1.203125 / 0.101654052734375 / 1.0601426046915743 | [NPY](tensors/0004561.npy) |
| 4562 | `model.layers.23` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8576.0 / 9088.0 / 5.150713433159722 / 552.1730724484471 | [NPY](tensors/0004562.npy) |
| 4641 | `model.layers.23` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6560.0 / 6976.0 / -2.8972547743055554 / 348.12736732906166 | [NPY](tensors/0004641.npy) |
| 4642 | `model.layers.23` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 336] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004642.npy) |
| 4643 | `model.layers.23` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0004643.npy) |
| 4644 | `model.layers.23` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0004644.npy) |
| 4645 | `model.layers.23` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0004645.npy) |
| 4646 | `model.layers.23` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4647 | `model.layers.23` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4648 | `model.layers.23` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4649 | `model.layers.23.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6560.0 / 6976.0 / -2.8972547743055554 / 348.12736732906166 | [NPY](tensors/0004649.npy) |
| 4650 | `model.layers.23.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.75 / 53.75 / 0.011754498216840955 / 1.7191949608745432 | [NPY](tensors/0004650.npy) |
| 4651 | `model.layers.23.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.75 / 53.75 / 0.011754498216840955 / 1.7191949608745432 | [NPY](tensors/0004651.npy) |
| 4652 | `model.layers.23.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 336] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004652.npy) |
| 4653 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0004653.npy) |
| 4654 | `model.layers.23.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4655 | `model.layers.23.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4656 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0004656.npy) |
| 4657 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0004657.npy) |
| 4658 | `model.layers.23.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4659 | `model.layers.23.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.75 / 53.75 / 0.011754498216840955 / 1.7191949608745432 | [NPY](tensors/0004659.npy) |
| 4660 | `model.layers.23.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.3125 / 17.75 / 0.07407132210209966 / 1.7590039337065313 | [NPY](tensors/0004660.npy) |
| 4661 | `model.layers.23.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.75 / 53.75 / 0.011754498216840955 / 1.7191949608745432 | [NPY](tensors/0004661.npy) |
| 4662 | `model.layers.23.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.75 / 40.25 / -0.013453930616378784 / 5.0148717990497085 | [NPY](tensors/0004662.npy) |
| 4663 | `model.layers.23.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.75 / 53.75 / 0.011754498216840955 / 1.7191949608745432 | [NPY](tensors/0004663.npy) |
| 4664 | `model.layers.23.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.25 / 10.625 / -0.19590309262275696 / 3.8620867283924922 | [NPY](tensors/0004664.npy) |
| 4665 | `model.layers.23.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -19.5 / 11.25 / -0.05519544368144125 / 1.7459734812011811 | [NPY](tensors/0004665.npy) |
| 4666 | `model.layers.23.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3120.0 / 3184.0 / 3.239126902156406 / 164.8289610567553 | [NPY](tensors/0004666.npy) |
| 4667 | `model.layers.23.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3120.0 / 3184.0 / 3.239126902156406 / 164.8289610567553 | [NPY](tensors/0004667.npy) |
| 4668 | `model.layers.23.self_attn` | 39 | `output[1]` | [1, 64, 1, 336] | torch.bfloat16 → float32 | 4.3298697960381105e-15 / 0.94140625 / 0.001958824671751662 / 0.015132789330023799 | [NPY](tensors/0004668.npy) |
| 4669 | `model.layers.23.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 5856.0 / 0.34453396267361114 / 358.14765152487354 | [NPY](tensors/0004669.npy) |
| 4670 | `model.layers.23.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.5 / 14.125 / -0.004223026169670953 / 1.3780165939498217 | [NPY](tensors/0004670.npy) |
| 4671 | `model.layers.23.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.5 / 14.125 / -0.004223026169670953 / 1.3780165939498217 | [NPY](tensors/0004671.npy) |
| 4672 | `model.layers.23.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -28.5 / 14.125 / -0.004223026169670953 / 1.3780165939498217 | [NPY](tensors/0004672.npy) |
| 4673 | `model.layers.23.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4674 | `model.layers.23.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4675 | `model.layers.23.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4676 | `model.layers.23.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2624.0 / 2160.0 / -5.856626976860894 / 294.8211668048794 | [NPY](tensors/0004676.npy) |
| 4677 | `model.layers.23.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2624.0 / 2160.0 / -5.856626976860894 / 294.8211668048794 | [NPY](tensors/0004677.npy) |
| 4678 | `model.layers.23.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.96875 / 2.78125 / 0.16802978515625 / 2.233814221649294 | [NPY](tensors/0004678.npy) |
| 4679 | `model.layers.23` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3344.0 / 3744.0 / -5.5028700086805555 / 430.92819969387983 | [NPY](tensors/0004679.npy) |
| 4758 | `model.layers.23` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7936.0 / 7520.0 / -2.551345486111111 / 368.8881420332231 | [NPY](tensors/0004758.npy) |
| 4759 | `model.layers.23` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 337] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004759.npy) |
| 4760 | `model.layers.23` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0004760.npy) |
| 4761 | `model.layers.23` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0004761.npy) |
| 4762 | `model.layers.23` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0004762.npy) |
| 4763 | `model.layers.23` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4764 | `model.layers.23` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4765 | `model.layers.23` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4766 | `model.layers.23.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7936.0 / 7520.0 / -2.551345486111111 / 368.8881420332231 | [NPY](tensors/0004766.npy) |
| 4767 | `model.layers.23.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 53.5 / 0.0003798981507619222 / 1.7648646696633825 | [NPY](tensors/0004767.npy) |
| 4768 | `model.layers.23.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 53.5 / 0.0003798981507619222 / 1.7648646696633825 | [NPY](tensors/0004768.npy) |
| 4769 | `model.layers.23.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 337] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004769.npy) |
| 4770 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0004770.npy) |
| 4771 | `model.layers.23.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4772 | `model.layers.23.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4773 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0004773.npy) |
| 4774 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0004774.npy) |
| 4775 | `model.layers.23.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4776 | `model.layers.23.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 53.5 / 0.0003798981507619222 / 1.7648646696633825 | [NPY](tensors/0004776.npy) |
| 4777 | `model.layers.23.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.25 / 17.125 / 0.04766785656102002 / 1.6739881419541451 | [NPY](tensors/0004777.npy) |
| 4778 | `model.layers.23.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 53.5 / 0.0003798981507619222 / 1.7648646696633825 | [NPY](tensors/0004778.npy) |
| 4779 | `model.layers.23.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -59.25 / 44.25 / 0.0318269282579422 / 6.0220928521281225 | [NPY](tensors/0004779.npy) |
| 4780 | `model.layers.23.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 53.5 / 0.0003798981507619222 / 1.7648646696633825 | [NPY](tensors/0004780.npy) |
| 4781 | `model.layers.23.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -24.75 / 15.9375 / -0.025727182626724243 / 3.9545811886016042 | [NPY](tensors/0004781.npy) |
| 4782 | `model.layers.23.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -22.75 / 9.25 / 0.012178839519037865 / 1.4342086112413652 | [NPY](tensors/0004782.npy) |
| 4783 | `model.layers.23.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4048.0 / 4192.0 / 5.656884765625 / 179.5932949450254 | [NPY](tensors/0004783.npy) |
| 4784 | `model.layers.23.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4048.0 / 4192.0 / 5.656884765625 / 179.5932949450254 | [NPY](tensors/0004784.npy) |
| 4785 | `model.layers.23.self_attn` | 40 | `output[1]` | [1, 64, 1, 337] | torch.bfloat16 → float32 | 1.6393136847980827e-16 / 0.91015625 / 0.001637046236989719 / 0.015318905074177231 | [NPY](tensors/0004785.npy) |
| 4786 | `model.layers.23.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8256.0 / 7936.0 / 3.083132595486111 / 428.0774143348856 | [NPY](tensors/0004786.npy) |
| 4787 | `model.layers.23.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 13.3125 / -0.009077719847361247 / 1.162144721315391 | [NPY](tensors/0004787.npy) |
| 4788 | `model.layers.23.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 13.3125 / -0.009077719847361247 / 1.162144721315391 | [NPY](tensors/0004788.npy) |
| 4789 | `model.layers.23.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.5 / 13.3125 / -0.009077719847361247 / 1.162144721315391 | [NPY](tensors/0004789.npy) |
| 4790 | `model.layers.23.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4791 | `model.layers.23.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4792 | `model.layers.23.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4793 | `model.layers.23.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1520.0 / 1296.0 / -0.9007272296481662 / 96.86445428720681 | [NPY](tensors/0004793.npy) |
| 4794 | `model.layers.23.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1520.0 / 1296.0 / -0.9007272296481662 / 96.86445428720681 | [NPY](tensors/0004794.npy) |
| 4795 | `model.layers.23.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.6875 / 2.09375 / 0.21405029296875 / 2.020904361055872 | [NPY](tensors/0004795.npy) |
| 4796 | `model.layers.23` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7040.0 / 6592.0 / 2.201144748263889 / 395.4543647070185 | [NPY](tensors/0004796.npy) |
| 4875 | `model.layers.23` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8448.0 / 8320.0 / -1.9097086588541667 / 414.7992784689769 | [NPY](tensors/0004875.npy) |
| 4876 | `model.layers.23` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 338] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004876.npy) |
| 4877 | `model.layers.23` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0004877.npy) |
| 4878 | `model.layers.23` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0004878.npy) |
| 4879 | `model.layers.23` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0004879.npy) |
| 4880 | `model.layers.23` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4881 | `model.layers.23` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4882 | `model.layers.23` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4883 | `model.layers.23.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8448.0 / 8320.0 / -1.9097086588541667 / 414.7992784689769 | [NPY](tensors/0004883.npy) |
| 4884 | `model.layers.23.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 54.0 / 0.002662348747253418 / 1.7244056277126432 | [NPY](tensors/0004884.npy) |
| 4885 | `model.layers.23.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 54.0 / 0.002662348747253418 / 1.7244056277126432 | [NPY](tensors/0004885.npy) |
| 4886 | `model.layers.23.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 338] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004886.npy) |
| 4887 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0004887.npy) |
| 4888 | `model.layers.23.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4889 | `model.layers.23.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4890 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0004890.npy) |
| 4891 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0004891.npy) |
| 4892 | `model.layers.23.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4893 | `model.layers.23.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 54.0 / 0.002662348747253418 / 1.7244056277126432 | [NPY](tensors/0004893.npy) |
| 4894 | `model.layers.23.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.4375 / 16.125 / 0.04079852456925437 / 1.5003750564626679 | [NPY](tensors/0004894.npy) |
| 4895 | `model.layers.23.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 54.0 / 0.002662348747253418 / 1.7244056277126432 | [NPY](tensors/0004895.npy) |
| 4896 | `model.layers.23.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.0 / 40.5 / 0.016181355342268944 / 5.215103912774215 | [NPY](tensors/0004896.npy) |
| 4897 | `model.layers.23.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 54.0 / 0.002662348747253418 / 1.7244056277126432 | [NPY](tensors/0004897.npy) |
| 4898 | `model.layers.23.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -24.375 / 11.3125 / 0.18678869307041168 / 2.850573157546308 | [NPY](tensors/0004898.npy) |
| 4899 | `model.layers.23.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -20.5 / 5.34375 / 0.005226050700002816 / 1.1009889990487454 | [NPY](tensors/0004899.npy) |
| 4900 | `model.layers.23.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4992.0 / 5248.0 / 5.098554907904731 / 223.24505920166345 | [NPY](tensors/0004900.npy) |
| 4901 | `model.layers.23.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4992.0 / 5248.0 / 5.098554907904731 / 223.24505920166345 | [NPY](tensors/0004901.npy) |
| 4902 | `model.layers.23.self_attn` | 41 | `output[1]` | [1, 64, 1, 338] | torch.bfloat16 → float32 | 7.860379014346108e-14 / 0.83984375 / 0.001092941983537361 / 0.009820962786274104 | [NPY](tensors/0004902.npy) |
| 4903 | `model.layers.23.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8512.0 / 8640.0 / 3.191145833333333 / 494.31715779772236 | [NPY](tensors/0004903.npy) |
| 4904 | `model.layers.23.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 7.25 / -0.01385513146718343 / 1.1461201451079979 | [NPY](tensors/0004904.npy) |
| 4905 | `model.layers.23.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 7.25 / -0.01385513146718343 / 1.1461201451079979 | [NPY](tensors/0004905.npy) |
| 4906 | `model.layers.23.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.25 / 7.25 / -0.01385513146718343 / 1.1461201451079979 | [NPY](tensors/0004906.npy) |
| 4907 | `model.layers.23.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4908 | `model.layers.23.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4909 | `model.layers.23.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4910 | `model.layers.23.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1400.0 / 1504.0 / -2.393368191189236 / 127.14021055865605 | [NPY](tensors/0004910.npy) |
| 4911 | `model.layers.23.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1400.0 / 1504.0 / -2.393368191189236 / 127.14021055865605 | [NPY](tensors/0004911.npy) |
| 4912 | `model.layers.23.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.8125 / 1.7421875 / 0.07881546020507812 / 1.0002925771733602 | [NPY](tensors/0004912.npy) |
| 4913 | `model.layers.23` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7008.0 / 7456.0 / 0.787060546875 / 446.7622610283051 | [NPY](tensors/0004913.npy) |
| 4992 | `model.layers.23` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 9856.0 / 0.6800320095486111 / 474.6887382165908 | [NPY](tensors/0004992.npy) |
| 4993 | `model.layers.23` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 339] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004993.npy) |
| 4994 | `model.layers.23` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0004994.npy) |
| 4995 | `model.layers.23` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0004995.npy) |
| 4996 | `model.layers.23` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0004996.npy) |
| 4997 | `model.layers.23` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4998 | `model.layers.23` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4999 | `model.layers.23` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5000 | `model.layers.23.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 9856.0 / 0.6800320095486111 / 474.6887382165908 | [NPY](tensors/0005000.npy) |
| 5001 | `model.layers.23.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 55.75 / 0.01632982095082601 / 1.7466569368160818 | [NPY](tensors/0005001.npy) |
| 5002 | `model.layers.23.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 55.75 / 0.01632982095082601 / 1.7466569368160818 | [NPY](tensors/0005002.npy) |
| 5003 | `model.layers.23.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 339] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005003.npy) |
| 5004 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0005004.npy) |
| 5005 | `model.layers.23.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5006 | `model.layers.23.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5007 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0005007.npy) |
| 5008 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0005008.npy) |
| 5009 | `model.layers.23.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5010 | `model.layers.23.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 55.75 / 0.01632982095082601 / 1.7466569368160818 | [NPY](tensors/0005010.npy) |
| 5011 | `model.layers.23.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.8125 / 16.375 / 0.06397253461182117 / 1.7167641098446176 | [NPY](tensors/0005011.npy) |
| 5012 | `model.layers.23.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 55.75 / 0.01632982095082601 / 1.7466569368160818 | [NPY](tensors/0005012.npy) |
| 5013 | `model.layers.23.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.0 / 28.75 / -0.02463410049676895 / 4.62446677704638 | [NPY](tensors/0005013.npy) |
| 5014 | `model.layers.23.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.75 / 55.75 / 0.01632982095082601 / 1.7466569368160818 | [NPY](tensors/0005014.npy) |
| 5015 | `model.layers.23.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -24.25 / 21.375 / 0.14937996864318848 / 5.550787877827691 | [NPY](tensors/0005015.npy) |
| 5016 | `model.layers.23.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.625 / 7.125 / 0.06735432986170053 / 1.4329936870917064 | [NPY](tensors/0005016.npy) |
| 5017 | `model.layers.23.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3184.0 / 3024.0 / 1.9592388153076172 / 158.3830387297727 | [NPY](tensors/0005017.npy) |
| 5018 | `model.layers.23.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3184.0 / 3024.0 / 1.9592388153076172 / 158.3830387297727 | [NPY](tensors/0005018.npy) |
| 5019 | `model.layers.23.self_attn` | 42 | `output[1]` | [1, 64, 1, 339] | torch.bfloat16 → float32 | 4.3576253716537394e-15 / 0.93359375 / 0.0016542204829528124 / 0.015000920031847215 | [NPY](tensors/0005019.npy) |
| 5020 | `model.layers.23.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7904.0 / 8640.0 / 2.665874565972222 / 472.507053098185 | [NPY](tensors/0005020.npy) |
| 5021 | `model.layers.23.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 10.875 / -0.010449768437279596 / 1.39935125479623 | [NPY](tensors/0005021.npy) |
| 5022 | `model.layers.23.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 10.875 / -0.010449768437279596 / 1.39935125479623 | [NPY](tensors/0005022.npy) |
| 5023 | `model.layers.23.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.25 / 10.875 / -0.010449768437279596 / 1.39935125479623 | [NPY](tensors/0005023.npy) |
| 5024 | `model.layers.23.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5025 | `model.layers.23.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5026 | `model.layers.23.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5027 | `model.layers.23.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5120.0 / 5024.0 / -15.151061587863499 / 359.35006159092785 | [NPY](tensors/0005027.npy) |
| 5028 | `model.layers.23.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5120.0 / 5024.0 / -15.151061587863499 / 359.35006159092785 | [NPY](tensors/0005028.npy) |
| 5029 | `model.layers.23.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.515625 / 2.265625 / 0.0347137451171875 / 1.3127134998662462 | [NPY](tensors/0005029.npy) |
| 5030 | `model.layers.23` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2880.0 / 3520.0 / -12.453537326388888 / 455.07262309483264 | [NPY](tensors/0005030.npy) |
| 5109 | `model.layers.23` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8320.0 / 8832.0 / 0.42293836805555557 / 433.8609872937337 | [NPY](tensors/0005109.npy) |
| 5110 | `model.layers.23` | 43 | `input.kwargs['attention_mask']` | [1, 1, 1, 340] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005110.npy) |
| 5111 | `model.layers.23` | 43 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0005111.npy) |
| 5112 | `model.layers.23` | 43 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0005112.npy) |
| 5113 | `model.layers.23` | 43 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0005113.npy) |
| 5114 | `model.layers.23` | 43 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5115 | `model.layers.23` | 43 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5116 | `model.layers.23` | 43 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5117 | `model.layers.23.input_layernorm` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8320.0 / 8832.0 / 0.42293836805555557 / 433.8609872937337 | [NPY](tensors/0005117.npy) |
| 5118 | `model.layers.23.input_layernorm` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 54.75 / 0.019513013627794056 / 1.7466375908427392 | [NPY](tensors/0005118.npy) |
| 5119 | `model.layers.23.self_attn` | 43 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 54.75 / 0.019513013627794056 / 1.7466375908427392 | [NPY](tensors/0005119.npy) |
| 5120 | `model.layers.23.self_attn` | 43 | `input.kwargs['attention_mask']` | [1, 1, 1, 340] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005120.npy) |
| 5121 | `model.layers.23.self_attn` | 43 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0005121.npy) |
| 5122 | `model.layers.23.self_attn` | 43 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5123 | `model.layers.23.self_attn` | 43 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5124 | `model.layers.23.self_attn` | 43 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0005124.npy) |
| 5125 | `model.layers.23.self_attn` | 43 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0005125.npy) |
| 5126 | `model.layers.23.self_attn` | 43 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5127 | `model.layers.23.self_attn.q_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 54.75 / 0.019513013627794056 / 1.7466375908427392 | [NPY](tensors/0005127.npy) |
| 5128 | `model.layers.23.self_attn.q_proj` | 43 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.0 / 16.875 / 0.05609641381306574 / 1.82015451840687 | [NPY](tensors/0005128.npy) |
| 5129 | `model.layers.23.self_attn.k_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 54.75 / 0.019513013627794056 / 1.7466375908427392 | [NPY](tensors/0005129.npy) |
| 5130 | `model.layers.23.self_attn.k_proj` | 43 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.5 / 35.5 / -0.041474826633930206 / 4.638268146817649 | [NPY](tensors/0005130.npy) |
| 5131 | `model.layers.23.self_attn.v_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 54.75 / 0.019513013627794056 / 1.7466375908427392 | [NPY](tensors/0005131.npy) |
| 5132 | `model.layers.23.self_attn.v_proj` | 43 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.25 / 13.125 / 0.01009012758731842 / 3.982673720299507 | [NPY](tensors/0005132.npy) |
| 5133 | `model.layers.23.self_attn.o_proj` | 43 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.8125 / 8.8125 / 0.0789627640042454 / 1.7263119842975727 | [NPY](tensors/0005133.npy) |
| 5134 | `model.layers.23.self_attn.o_proj` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3712.0 / 3728.0 / 3.125531768798828 / 190.7447657099852 | [NPY](tensors/0005134.npy) |
| 5135 | `model.layers.23.self_attn` | 43 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3712.0 / 3728.0 / 3.125531768798828 / 190.7447657099852 | [NPY](tensors/0005135.npy) |
| 5136 | `model.layers.23.self_attn` | 43 | `output[1]` | [1, 64, 1, 340] | torch.bfloat16 → float32 | 7.494005416219807e-15 / 0.97265625 / 0.0019982049271177714 / 0.019410094469417542 | [NPY](tensors/0005136.npy) |
| 5137 | `model.layers.23.post_attention_layernorm` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7904.0 / 8448.0 / 3.5679253472222223 / 478.22964178617156 | [NPY](tensors/0005137.npy) |
| 5138 | `model.layers.23.post_attention_layernorm` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.0 / 9.0 / -0.008249017927381728 / 1.3425526386105844 | [NPY](tensors/0005138.npy) |
| 5139 | `model.layers.23.mlp` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.0 / 9.0 / -0.008249017927381728 / 1.3425526386105844 | [NPY](tensors/0005139.npy) |
| 5140 | `model.layers.23.mlp.experts` | 43 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.0 / 9.0 / -0.008249017927381728 / 1.3425526386105844 | [NPY](tensors/0005140.npy) |
| 5141 | `model.layers.23.mlp.experts` | 43 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5142 | `model.layers.23.mlp.experts` | 43 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5143 | `model.layers.23.mlp.experts` | 43 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5144 | `model.layers.23.mlp.experts` | 43 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6912.0 / 6400.0 / -0.09772978888617621 / 379.21809531630197 | [NPY](tensors/0005144.npy) |
| 5145 | `model.layers.23.mlp` | 43 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6912.0 / 6400.0 / -0.09772978888617621 / 379.21809531630197 | [NPY](tensors/0005145.npy) |
| 5146 | `model.layers.23.mlp` | 43 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.1875 / 1.71875 / 0.013164430856704712 / 1.1271521223440746 | [NPY](tensors/0005146.npy) |
| 5147 | `model.layers.23` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1640.0 / 2448.0 / 3.492692057291667 / 419.86577128392264 | [NPY](tensors/0005147.npy) |

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
