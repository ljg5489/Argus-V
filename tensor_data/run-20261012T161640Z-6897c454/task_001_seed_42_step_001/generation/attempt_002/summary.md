# Hook inspection: generation

Status: **complete**. 4230 full tensors; 5499 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.0016833860045706059 / 2.7432837670218246 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 305, 305] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.2631976692349434e+38 / 1.5965950801384408e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 305, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7963737057857826 / 0.8801360272441033 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 305, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12046455383190091 / 0.6213787871646592 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 305] | torch.int64 → int64 | 0.0 / 304.0 / 152.0 / 88.04544281222056 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.0016833860045706059 / 2.7432837670218246 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 305, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0030088462206265317 / 0.7639884368836956 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 305, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0030088462206265317 / 0.7639884368836956 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 305, 305] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.2631976692349434e+38 / 1.5965950801384408e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 305] | torch.int64 → int64 | 0.0 / 304.0 / 152.0 / 88.04544281222056 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 305, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7963737057857826 / 0.8801360272441033 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 305, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12046455383190091 / 0.6213787871646592 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0030088462206265317 / 0.7639884368836956 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 305, 4096] | torch.bfloat16 → float32 | -10.25 / 12.8125 / 0.02298440170048767 / 1.0489816505864078 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0030088462206265317 / 0.7639884368836956 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 305, 512] | torch.bfloat16 → float32 | -65.5 / 68.0 / 0.030857334811179363 / 5.754960316961059 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0030088462206265317 / 0.7639884368836956 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 305, 512] | torch.bfloat16 → float32 | -8.1875 / 9.0 / -0.015273289944304795 / 1.2366695268381345 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 305, 4096] | torch.bfloat16 → float32 | -8.1875 / 8.8125 / -0.006719317154437113 / 0.5541600400462819 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 305, 2880] | torch.bfloat16 → float32 | -47.25 / 56.5 / 0.030141371659122795 / 1.2040876085660277 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -47.25 / 56.5 / 0.030141371659122795 / 1.2040876085660277 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 305, 305] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0012331298711134703 / 0.023133149220726464 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -87.5 / 70.5 / 0.028465838278686196 / 2.94330682270803 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 305, 2880] | torch.bfloat16 → float32 | -7.25 / 3.75 / 0.0016059985911585594 / 0.3506944991921169 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -7.25 / 3.75 / 0.0016059985911585594 / 0.3506944991921169 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [305, 2880] | torch.bfloat16 → float32 | -7.25 / 3.75 / 0.0016059985911585594 / 0.3506944991921169 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [305, 2880] | torch.bfloat16 → float32 | -50.0 / 93.5 / 0.019516618528516997 / 0.9205900363695072 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -50.0 / 93.5 / 0.019516618528516997 / 0.9205900363695072 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [305, 32] | torch.bfloat16 → float32 | -5.5625 / 3.4375 / -0.11194887630275038 / 1.0001410580209535 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 305, 2880] | torch.bfloat16 → float32 | -89.0 / 107.0 / 0.04798104051249492 / 3.245814647216757 | [NPY](tensors/0000038.npy) |
| 117 | `model.layers.0` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 43.75 / 0.02880006796783871 / 2.9013049797239288 | [NPY](tensors/0000117.npy) |
| 118 | `model.layers.0` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000118.npy) |
| 119 | `model.layers.0` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0000119.npy) |
| 120 | `model.layers.0` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0000120.npy) |
| 121 | `model.layers.0` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0000121.npy) |
| 122 | `model.layers.0` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 123 | `model.layers.0` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 124 | `model.layers.0` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 125 | `model.layers.0.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 43.75 / 0.02880006796783871 / 2.9013049797239288 | [NPY](tensors/0000125.npy) |
| 126 | `model.layers.0.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000126.npy) |
| 127 | `model.layers.0.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000127.npy) |
| 128 | `model.layers.0.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000128.npy) |
| 129 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0000129.npy) |
| 130 | `model.layers.0.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 131 | `model.layers.0.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 132 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0000132.npy) |
| 133 | `model.layers.0.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0000133.npy) |
| 134 | `model.layers.0.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 135 | `model.layers.0.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000135.npy) |
| 136 | `model.layers.0.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 7.4375 / 0.039632019703276455 / 0.9975220123045838 | [NPY](tensors/0000136.npy) |
| 137 | `model.layers.0.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000137.npy) |
| 138 | `model.layers.0.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.5 / 41.25 / 0.060565054416656494 / 4.792407804689708 | [NPY](tensors/0000138.npy) |
| 139 | `model.layers.0.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.8125 / 10.6875 / 0.003105699767669042 / 0.7022435753589298 | [NPY](tensors/0000139.npy) |
| 140 | `model.layers.0.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.9375 / 3.90625 / 0.001153320074081421 / 1.2325447380756387 | [NPY](tensors/0000140.npy) |
| 141 | `model.layers.0.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.21875 / 2.640625 / -0.00024047596343734767 / 0.4587331859370379 | [NPY](tensors/0000141.npy) |
| 142 | `model.layers.0.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.9375 / 40.5 / 0.027184226198328866 / 1.2048727386124982 | [NPY](tensors/0000142.npy) |
| 143 | `model.layers.0.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.9375 / 40.5 / 0.027184226198328866 / 1.2048727386124982 | [NPY](tensors/0000143.npy) |
| 144 | `model.layers.0.self_attn` | 1 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0033930266017234414 / 0.037871046509267654 | [NPY](tensors/0000144.npy) |
| 145 | `model.layers.0.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 43.25 / 0.056050713857014975 / 3.0805567673870073 | [NPY](tensors/0000145.npy) |
| 146 | `model.layers.0.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8203125 / 2.078125 / 0.0026728060510423446 / 0.31272078321934393 | [NPY](tensors/0000146.npy) |
| 147 | `model.layers.0.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8203125 / 2.078125 / 0.0026728060510423446 / 0.31272078321934393 | [NPY](tensors/0000147.npy) |
| 148 | `model.layers.0.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.8203125 / 2.078125 / 0.0026728060510423446 / 0.31272078321934393 | [NPY](tensors/0000148.npy) |
| 149 | `model.layers.0.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 150 | `model.layers.0.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 151 | `model.layers.0.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 152 | `model.layers.0.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.25 / 27.75 / 0.0033971454948186876 / 0.8169899951113848 | [NPY](tensors/0000152.npy) |
| 153 | `model.layers.0.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.25 / 27.75 / 0.0033971454948186876 / 0.8169899951113848 | [NPY](tensors/0000153.npy) |
| 154 | `model.layers.0.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.4921875 / 2.21875 / -0.0714406967163086 / 0.8974150452086472 | [NPY](tensors/0000154.npy) |
| 155 | `model.layers.0` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 54.0 / 0.05965434180365668 / 3.238621026963438 | [NPY](tensors/0000155.npy) |
| 234 | `model.layers.0` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 45.75 / 0.04227736194928487 / 3.1518798398795616 | [NPY](tensors/0000234.npy) |
| 235 | `model.layers.0` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000235.npy) |
| 236 | `model.layers.0` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0000236.npy) |
| 237 | `model.layers.0` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0000237.npy) |
| 238 | `model.layers.0` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0000238.npy) |
| 239 | `model.layers.0` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 240 | `model.layers.0` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 241 | `model.layers.0` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 242 | `model.layers.0.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.0 / 45.75 / 0.04227736194928487 / 3.1518798398795616 | [NPY](tensors/0000242.npy) |
| 243 | `model.layers.0.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000243.npy) |
| 244 | `model.layers.0.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000244.npy) |
| 245 | `model.layers.0.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000245.npy) |
| 246 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0000246.npy) |
| 247 | `model.layers.0.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 248 | `model.layers.0.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 249 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0000249.npy) |
| 250 | `model.layers.0.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0000250.npy) |
| 251 | `model.layers.0.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 252 | `model.layers.0.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000252.npy) |
| 253 | `model.layers.0.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5 / 8.1875 / 0.022865560371428728 / 0.9733268065645532 | [NPY](tensors/0000253.npy) |
| 254 | `model.layers.0.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000254.npy) |
| 255 | `model.layers.0.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.75 / 47.0 / 0.09419560432434082 / 4.904277940788795 | [NPY](tensors/0000255.npy) |
| 256 | `model.layers.0.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0625 / 7.71875 / 0.0019994721644454533 / 0.7450198873572877 | [NPY](tensors/0000256.npy) |
| 257 | `model.layers.0.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 4.34375 / -0.08974748849868774 / 1.1126171556291353 | [NPY](tensors/0000257.npy) |
| 258 | `model.layers.0.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.25 / 3.78125 / -0.008958423510193825 / 0.5488930052128136 | [NPY](tensors/0000258.npy) |
| 259 | `model.layers.0.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.9375 / 38.0 / 0.023666565948062473 / 1.1898436230557554 | [NPY](tensors/0000259.npy) |
| 260 | `model.layers.0.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.9375 / 38.0 / 0.023666565948062473 / 1.1898436230557554 | [NPY](tensors/0000260.npy) |
| 261 | `model.layers.0.self_attn` | 2 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0038577254993085387 / 0.04201180118474399 | [NPY](tensors/0000261.npy) |
| 262 | `model.layers.0.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 45.5 / 0.06597404215070936 / 3.357741490530941 | [NPY](tensors/0000262.npy) |
| 263 | `model.layers.0.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.109375 / 2.015625 / 0.005368478430642022 / 0.3119484701100422 | [NPY](tensors/0000263.npy) |
| 264 | `model.layers.0.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.109375 / 2.015625 / 0.005368478430642022 / 0.3119484701100422 | [NPY](tensors/0000264.npy) |
| 265 | `model.layers.0.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.109375 / 2.015625 / 0.005368478430642022 / 0.3119484701100422 | [NPY](tensors/0000265.npy) |
| 266 | `model.layers.0.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 267 | `model.layers.0.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 268 | `model.layers.0.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 269 | `model.layers.0.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.53125 / 22.625 / 0.027308263091577425 / 0.7531954863173017 | [NPY](tensors/0000269.npy) |
| 270 | `model.layers.0.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.53125 / 22.625 / 0.027308263091577425 / 0.7531954863173017 | [NPY](tensors/0000270.npy) |
| 271 | `model.layers.0.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.546875 / 1.8359375 / -0.14989089965820312 / 0.9986264718043815 | [NPY](tensors/0000271.npy) |
| 272 | `model.layers.0` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 65.5 / 0.09329053031073677 / 3.563321624084059 | [NPY](tensors/0000272.npy) |
| 351 | `model.layers.0` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0000351.npy) |
| 352 | `model.layers.0` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000352.npy) |
| 353 | `model.layers.0` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0000353.npy) |
| 354 | `model.layers.0` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0000354.npy) |
| 355 | `model.layers.0` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0000355.npy) |
| 356 | `model.layers.0` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 357 | `model.layers.0` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 358 | `model.layers.0` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 359 | `model.layers.0.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0000359.npy) |
| 360 | `model.layers.0.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000360.npy) |
| 361 | `model.layers.0.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000361.npy) |
| 362 | `model.layers.0.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000362.npy) |
| 363 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0000363.npy) |
| 364 | `model.layers.0.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 365 | `model.layers.0.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 366 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0000366.npy) |
| 367 | `model.layers.0.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0000367.npy) |
| 368 | `model.layers.0.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 369 | `model.layers.0.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000369.npy) |
| 370 | `model.layers.0.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 9.25 / 0.06582052947487682 / 1.0317253511582722 | [NPY](tensors/0000370.npy) |
| 371 | `model.layers.0.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000371.npy) |
| 372 | `model.layers.0.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.5 / 59.75 / -0.027341485023498535 / 6.496414800406944 | [NPY](tensors/0000372.npy) |
| 373 | `model.layers.0.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0000373.npy) |
| 374 | `model.layers.0.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.453125 / 4.6875 / 0.06333106756210327 / 0.9556167387162166 | [NPY](tensors/0000374.npy) |
| 375 | `model.layers.0.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.28125 / 4.34375 / -0.01035036221401242 / 0.5506801449994422 | [NPY](tensors/0000375.npy) |
| 376 | `model.layers.0.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.1875 / 39.5 / 0.03133485513842768 / 1.2034737810917815 | [NPY](tensors/0000376.npy) |
| 377 | `model.layers.0.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.1875 / 39.5 / 0.03133485513842768 / 1.2034737810917815 | [NPY](tensors/0000377.npy) |
| 378 | `model.layers.0.self_attn` | 3 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.00354342599565536 / 0.03939570384302806 | [NPY](tensors/0000378.npy) |
| 379 | `model.layers.0.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 39.25 / 0.08041817877027724 / 2.6626921133872807 | [NPY](tensors/0000379.npy) |
| 380 | `model.layers.0.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.375 / 1.875 / 0.006455167134602865 / 0.3261656159891806 | [NPY](tensors/0000380.npy) |
| 381 | `model.layers.0.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.375 / 1.875 / 0.006455167134602865 / 0.3261656159891806 | [NPY](tensors/0000381.npy) |
| 382 | `model.layers.0.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.375 / 1.875 / 0.006455167134602865 / 0.3261656159891806 | [NPY](tensors/0000382.npy) |
| 383 | `model.layers.0.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 384 | `model.layers.0.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 385 | `model.layers.0.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 386 | `model.layers.0.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -15.5625 / 50.0 / 0.04245785805914137 / 1.6234092746704218 | [NPY](tensors/0000386.npy) |
| 387 | `model.layers.0.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.5625 / 50.0 / 0.04245785805914137 / 1.6234092746704218 | [NPY](tensors/0000387.npy) |
| 388 | `model.layers.0.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.296875 / 2.421875 / -0.1252288818359375 / 1.2615920259143496 | [NPY](tensors/0000388.npy) |
| 389 | `model.layers.0` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 87.0 / 0.12301173210144042 / 3.393817987750657 | [NPY](tensors/0000389.npy) |
| 468 | `model.layers.0` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 27.0 / 0.003733634617593553 / 2.804623802992795 | [NPY](tensors/0000468.npy) |
| 469 | `model.layers.0` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000469.npy) |
| 470 | `model.layers.0` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0000470.npy) |
| 471 | `model.layers.0` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0000471.npy) |
| 472 | `model.layers.0` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0000472.npy) |
| 473 | `model.layers.0` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 474 | `model.layers.0` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 475 | `model.layers.0` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 476 | `model.layers.0.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 27.0 / 0.003733634617593553 / 2.804623802992795 | [NPY](tensors/0000476.npy) |
| 477 | `model.layers.0.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0000477.npy) |
| 478 | `model.layers.0.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0000478.npy) |
| 479 | `model.layers.0.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000479.npy) |
| 480 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0000480.npy) |
| 481 | `model.layers.0.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 482 | `model.layers.0.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 483 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0000483.npy) |
| 484 | `model.layers.0.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0000484.npy) |
| 485 | `model.layers.0.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 486 | `model.layers.0.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0000486.npy) |
| 487 | `model.layers.0.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.875 / 10.625 / 0.036541547160595655 / 1.020216334584807 | [NPY](tensors/0000487.npy) |
| 488 | `model.layers.0.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0000488.npy) |
| 489 | `model.layers.0.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.0 / 61.0 / 0.009755432605743408 / 5.9442685357666845 | [NPY](tensors/0000489.npy) |
| 490 | `model.layers.0.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.6875 / 6.53125 / -0.003438378456566069 / 0.7308596720936491 | [NPY](tensors/0000490.npy) |
| 491 | `model.layers.0.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.65625 / 5.65625 / -0.0710136890411377 / 1.3093894403473694 | [NPY](tensors/0000491.npy) |
| 492 | `model.layers.0.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.28125 / 3.546875 / -0.0066963747181034705 / 0.5430449784577636 | [NPY](tensors/0000492.npy) |
| 493 | `model.layers.0.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.375 / 44.75 / 0.035726118915610845 / 1.320571695915031 | [NPY](tensors/0000493.npy) |
| 494 | `model.layers.0.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.375 / 44.75 / 0.035726118915610845 / 1.320571695915031 | [NPY](tensors/0000494.npy) |
| 495 | `model.layers.0.self_attn` | 4 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.003051201441415916 / 0.035435785784369324 | [NPY](tensors/0000495.npy) |
| 496 | `model.layers.0.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.0 / 48.25 / 0.03932642406887478 / 3.1401558496119857 | [NPY](tensors/0000496.npy) |
| 497 | `model.layers.0.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.921875 / 1.703125 / -0.0035643633868959216 / 0.3162889745228954 | [NPY](tensors/0000497.npy) |
| 498 | `model.layers.0.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.921875 / 1.703125 / -0.0035643633868959216 / 0.3162889745228954 | [NPY](tensors/0000498.npy) |
| 499 | `model.layers.0.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.921875 / 1.703125 / -0.0035643633868959216 / 0.3162889745228954 | [NPY](tensors/0000499.npy) |
| 500 | `model.layers.0.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 501 | `model.layers.0.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 502 | `model.layers.0.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 503 | `model.layers.0.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.40625 / 28.5 / 0.032391547453072336 / 0.8687563893238707 | [NPY](tensors/0000503.npy) |
| 504 | `model.layers.0.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.40625 / 28.5 / 0.032391547453072336 / 0.8687563893238707 | [NPY](tensors/0000504.npy) |
| 505 | `model.layers.0.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.546875 / 1.609375 / -0.19828414916992188 / 0.6564921620647872 | [NPY](tensors/0000505.npy) |
| 506 | `model.layers.0` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.5 / 76.0 / 0.07188633812798394 / 3.579681573648129 | [NPY](tensors/0000506.npy) |
| 585 | `model.layers.0` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 44.75 / 0.013139636483457354 / 2.9607003759627655 | [NPY](tensors/0000585.npy) |
| 586 | `model.layers.0` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000586.npy) |
| 587 | `model.layers.0` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0000587.npy) |
| 588 | `model.layers.0` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0000588.npy) |
| 589 | `model.layers.0` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0000589.npy) |
| 590 | `model.layers.0` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 591 | `model.layers.0` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 592 | `model.layers.0` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 593 | `model.layers.0.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 44.75 / 0.013139636483457354 / 2.9607003759627655 | [NPY](tensors/0000593.npy) |
| 594 | `model.layers.0.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0000594.npy) |
| 595 | `model.layers.0.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0000595.npy) |
| 596 | `model.layers.0.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000596.npy) |
| 597 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0000597.npy) |
| 598 | `model.layers.0.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 599 | `model.layers.0.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 600 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0000600.npy) |
| 601 | `model.layers.0.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0000601.npy) |
| 602 | `model.layers.0.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 603 | `model.layers.0.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0000603.npy) |
| 604 | `model.layers.0.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5625 / 8.625 / 0.03118488343898207 / 1.013318010948837 | [NPY](tensors/0000604.npy) |
| 605 | `model.layers.0.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0000605.npy) |
| 606 | `model.layers.0.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.25 / 44.0 / -0.021389365196228027 / 5.266550301692611 | [NPY](tensors/0000606.npy) |
| 607 | `model.layers.0.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0000607.npy) |
| 608 | `model.layers.0.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.28125 / 4.4375 / -0.023247554898262024 / 1.2424791578118235 | [NPY](tensors/0000608.npy) |
| 609 | `model.layers.0.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.15625 / 4.71875 / -0.017934701550302634 / 0.5809089105813979 | [NPY](tensors/0000609.npy) |
| 610 | `model.layers.0.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.375 / 43.75 / 0.037402047051323786 / 1.275135504139389 | [NPY](tensors/0000610.npy) |
| 611 | `model.layers.0.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -18.375 / 43.75 / 0.037402047051323786 / 1.275135504139389 | [NPY](tensors/0000611.npy) |
| 612 | `model.layers.0.self_attn` | 5 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98046875 / 0.003348693653250602 / 0.03721280879785641 | [NPY](tensors/0000612.npy) |
| 613 | `model.layers.0.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -52.0 / 43.75 / 0.050531711843278676 / 3.1809761578837166 | [NPY](tensors/0000613.npy) |
| 614 | `model.layers.0.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.21875 / 1.671875 / 0.00601499941613939 / 0.3398636214930915 | [NPY](tensors/0000614.npy) |
| 615 | `model.layers.0.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.21875 / 1.671875 / 0.00601499941613939 / 0.3398636214930915 | [NPY](tensors/0000615.npy) |
| 616 | `model.layers.0.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -5.21875 / 1.671875 / 0.00601499941613939 / 0.3398636214930915 | [NPY](tensors/0000616.npy) |
| 617 | `model.layers.0.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 618 | `model.layers.0.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 619 | `model.layers.0.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 620 | `model.layers.0.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -31.25 / 22.75 / -0.001746575203206804 / 0.8711289719924435 | [NPY](tensors/0000620.npy) |
| 621 | `model.layers.0.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.25 / 22.75 / -0.001746575203206804 / 0.8711289719924435 | [NPY](tensors/0000621.npy) |
| 622 | `model.layers.0.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.265625 / 1.375 / -0.20605623722076416 / 0.8841535302621578 | [NPY](tensors/0000622.npy) |
| 623 | `model.layers.0` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.0 / 62.25 / 0.048849127027723524 / 3.5167886880318457 | [NPY](tensors/0000623.npy) |
| 702 | `model.layers.0` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 31.375 / -0.03532346973402633 / 2.513775339817436 | [NPY](tensors/0000702.npy) |
| 703 | `model.layers.0` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000703.npy) |
| 704 | `model.layers.0` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0000704.npy) |
| 705 | `model.layers.0` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0000705.npy) |
| 706 | `model.layers.0` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0000706.npy) |
| 707 | `model.layers.0` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 708 | `model.layers.0` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 709 | `model.layers.0` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 710 | `model.layers.0.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 31.375 / -0.03532346973402633 / 2.513775339817436 | [NPY](tensors/0000710.npy) |
| 711 | `model.layers.0.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0000711.npy) |
| 712 | `model.layers.0.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0000712.npy) |
| 713 | `model.layers.0.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000713.npy) |
| 714 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0000714.npy) |
| 715 | `model.layers.0.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 716 | `model.layers.0.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 717 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0000717.npy) |
| 718 | `model.layers.0.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0000718.npy) |
| 719 | `model.layers.0.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 720 | `model.layers.0.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0000720.npy) |
| 721 | `model.layers.0.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 8.875 / -0.00043488043593242764 / 1.093332692665652 | [NPY](tensors/0000721.npy) |
| 722 | `model.layers.0.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0000722.npy) |
| 723 | `model.layers.0.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.0 / 57.0 / -0.11751466989517212 / 6.178501515201047 | [NPY](tensors/0000723.npy) |
| 724 | `model.layers.0.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0000724.npy) |
| 725 | `model.layers.0.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.15625 / 4.375 / -0.08698096498847008 / 1.3301958676902246 | [NPY](tensors/0000725.npy) |
| 726 | `model.layers.0.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.34375 / 4.375 / -0.012451506721845362 / 0.616925770534127 | [NPY](tensors/0000726.npy) |
| 727 | `model.layers.0.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.625 / 49.0 / 0.03273069808880488 / 1.542333107202846 | [NPY](tensors/0000727.npy) |
| 728 | `model.layers.0.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.625 / 49.0 / 0.03273069808880488 / 1.542333107202846 | [NPY](tensors/0000728.npy) |
| 729 | `model.layers.0.self_attn` | 6 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.00343137366635265 / 0.03725551483032633 | [NPY](tensors/0000729.npy) |
| 730 | `model.layers.0.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.0 / 48.75 / -0.0025980313618977863 / 3.0689650084240103 | [NPY](tensors/0000730.npy) |
| 731 | `model.layers.0.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6875 / 1.609375 / 0.0018063690927293565 / 0.3448720239952845 | [NPY](tensors/0000731.npy) |
| 732 | `model.layers.0.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6875 / 1.609375 / 0.0018063690927293565 / 0.3448720239952845 | [NPY](tensors/0000732.npy) |
| 733 | `model.layers.0.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.6875 / 1.609375 / 0.0018063690927293565 / 0.3448720239952845 | [NPY](tensors/0000733.npy) |
| 734 | `model.layers.0.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 735 | `model.layers.0.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 736 | `model.layers.0.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 737 | `model.layers.0.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -11.5 / 37.0 / 0.023440364541278944 / 1.026930653552298 | [NPY](tensors/0000737.npy) |
| 738 | `model.layers.0.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.5 / 37.0 / 0.023440364541278944 / 1.026930653552298 | [NPY](tensors/0000738.npy) |
| 739 | `model.layers.0.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.890625 / 1.7265625 / -0.19521236419677734 / 0.6884699220977282 | [NPY](tensors/0000739.npy) |
| 740 | `model.layers.0` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 84.0 / 0.02053905063205295 / 3.7064833993747768 | [NPY](tensors/0000740.npy) |
| 819 | `model.layers.0` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.75 / 55.25 / 0.04413516670465469 / 2.743070253110853 | [NPY](tensors/0000819.npy) |
| 820 | `model.layers.0` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000820.npy) |
| 821 | `model.layers.0` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0000821.npy) |
| 822 | `model.layers.0` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0000822.npy) |
| 823 | `model.layers.0` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0000823.npy) |
| 824 | `model.layers.0` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 825 | `model.layers.0` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 826 | `model.layers.0` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 827 | `model.layers.0.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.75 / 55.25 / 0.04413516670465469 / 2.743070253110853 | [NPY](tensors/0000827.npy) |
| 828 | `model.layers.0.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.125 / 15.0 / 0.009613696402973599 / 0.7933645735195622 | [NPY](tensors/0000828.npy) |
| 829 | `model.layers.0.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.125 / 15.0 / 0.009613696402973599 / 0.7933645735195622 | [NPY](tensors/0000829.npy) |
| 830 | `model.layers.0.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000830.npy) |
| 831 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0000831.npy) |
| 832 | `model.layers.0.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 833 | `model.layers.0.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 834 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0000834.npy) |
| 835 | `model.layers.0.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0000835.npy) |
| 836 | `model.layers.0.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 837 | `model.layers.0.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.125 / 15.0 / 0.009613696402973599 / 0.7933645735195622 | [NPY](tensors/0000837.npy) |
| 838 | `model.layers.0.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.40625 / 7.375 / 0.0315710362046957 / 0.9632114202302644 | [NPY](tensors/0000838.npy) |
| 839 | `model.layers.0.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.125 / 15.0 / 0.009613696402973599 / 0.7933645735195622 | [NPY](tensors/0000839.npy) |
| 840 | `model.layers.0.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.75 / 53.75 / 0.18583789467811584 / 5.652296549443049 | [NPY](tensors/0000840.npy) |
| 841 | `model.layers.0.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.125 / 15.0 / 0.009613696402973599 / 0.7933645735195622 | [NPY](tensors/0000841.npy) |
| 842 | `model.layers.0.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -2.90625 / 4.125 / 0.05435967445373535 / 0.9301505088501508 | [NPY](tensors/0000842.npy) |
| 843 | `model.layers.0.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.1875 / 3.9375 / 0.0008902206612901864 / 0.4161987168617829 | [NPY](tensors/0000843.npy) |
| 844 | `model.layers.0.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.8125 / 36.0 / 0.030999321242173514 / 1.083689784550349 | [NPY](tensors/0000844.npy) |
| 845 | `model.layers.0.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.8125 / 36.0 / 0.030999321242173514 / 1.083689784550349 | [NPY](tensors/0000845.npy) |
| 846 | `model.layers.0.self_attn` | 7 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002573431377994583 / 0.027384575545308383 | [NPY](tensors/0000846.npy) |
| 847 | `model.layers.0.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 55.75 / 0.07520859506395128 / 2.9315249696217878 | [NPY](tensors/0000847.npy) |
| 848 | `model.layers.0.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.40625 / 2.078125 / 0.009649964504771763 / 0.31184581420249846 | [NPY](tensors/0000848.npy) |
| 849 | `model.layers.0.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.40625 / 2.078125 / 0.009649964504771763 / 0.31184581420249846 | [NPY](tensors/0000849.npy) |
| 850 | `model.layers.0.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.40625 / 2.078125 / 0.009649964504771763 / 0.31184581420249846 | [NPY](tensors/0000850.npy) |
| 851 | `model.layers.0.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 852 | `model.layers.0.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 853 | `model.layers.0.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 854 | `model.layers.0.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.5 / 15.5625 / 0.013956714421510696 / 0.6206020369388642 | [NPY](tensors/0000854.npy) |
| 855 | `model.layers.0.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.5 / 15.5625 / 0.013956714421510696 / 0.6206020369388642 | [NPY](tensors/0000855.npy) |
| 856 | `model.layers.0.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.28125 / 2.40625 / -0.0892333984375 / 1.1684018547271111 | [NPY](tensors/0000856.npy) |
| 857 | `model.layers.0` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 54.5 / 0.08928587701585558 / 3.0592712903338577 | [NPY](tensors/0000857.npy) |
| 936 | `model.layers.0` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 36.25 / -0.016887722081608242 / 2.850530266483584 | [NPY](tensors/0000936.npy) |
| 937 | `model.layers.0` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000937.npy) |
| 938 | `model.layers.0` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0000938.npy) |
| 939 | `model.layers.0` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0000939.npy) |
| 940 | `model.layers.0` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0000940.npy) |
| 941 | `model.layers.0` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 942 | `model.layers.0` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 943 | `model.layers.0` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 944 | `model.layers.0.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 36.25 / -0.016887722081608242 / 2.850530266483584 | [NPY](tensors/0000944.npy) |
| 945 | `model.layers.0.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.0625 / 9.0 / -0.014405341943105061 / 0.7625060332963726 | [NPY](tensors/0000945.npy) |
| 946 | `model.layers.0.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.0625 / 9.0 / -0.014405341943105061 / 0.7625060332963726 | [NPY](tensors/0000946.npy) |
| 947 | `model.layers.0.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000947.npy) |
| 948 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0000948.npy) |
| 949 | `model.layers.0.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 950 | `model.layers.0.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 951 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0000951.npy) |
| 952 | `model.layers.0.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0000952.npy) |
| 953 | `model.layers.0.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 954 | `model.layers.0.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.0625 / 9.0 / -0.014405341943105061 / 0.7625060332963726 | [NPY](tensors/0000954.npy) |
| 955 | `model.layers.0.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.53125 / 8.1875 / 0.017331954149995 / 0.9978045276660307 | [NPY](tensors/0000955.npy) |
| 956 | `model.layers.0.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.0625 / 9.0 / -0.014405341943105061 / 0.7625060332963726 | [NPY](tensors/0000956.npy) |
| 957 | `model.layers.0.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -59.25 / 46.0 / -0.06331458687782288 / 5.667576581582531 | [NPY](tensors/0000957.npy) |
| 958 | `model.layers.0.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.0625 / 9.0 / -0.014405341943105061 / 0.7625060332963726 | [NPY](tensors/0000958.npy) |
| 959 | `model.layers.0.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.46875 / 5.375 / -0.1045680046081543 / 1.2260077299701782 | [NPY](tensors/0000959.npy) |
| 960 | `model.layers.0.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.1875 / 4.40625 / -0.01595062205888098 / 0.5530880742498357 | [NPY](tensors/0000960.npy) |
| 961 | `model.layers.0.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.0 / 50.5 / 0.03178233870615562 / 1.470279230865996 | [NPY](tensors/0000961.npy) |
| 962 | `model.layers.0.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.0 / 50.5 / 0.03178233870615562 / 1.470279230865996 | [NPY](tensors/0000962.npy) |
| 963 | `model.layers.0.self_attn` | 8 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0031666510592991753 / 0.03697311761635486 | [NPY](tensors/0000963.npy) |
| 964 | `model.layers.0.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 48.5 / 0.014769311745961506 / 3.216191995052419 | [NPY](tensors/0000964.npy) |
| 965 | `model.layers.0.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.140625 / 1.6953125 / -0.004053321811887953 / 0.31389756751495257 | [NPY](tensors/0000965.npy) |
| 966 | `model.layers.0.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.140625 / 1.6953125 / -0.004053321811887953 / 0.31389756751495257 | [NPY](tensors/0000966.npy) |
| 967 | `model.layers.0.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.140625 / 1.6953125 / -0.004053321811887953 / 0.31389756751495257 | [NPY](tensors/0000967.npy) |
| 968 | `model.layers.0.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 969 | `model.layers.0.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 970 | `model.layers.0.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 971 | `model.layers.0.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.25 / 19.125 / 0.00962624458803071 / 0.5887698933245887 | [NPY](tensors/0000971.npy) |
| 972 | `model.layers.0.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.25 / 19.125 / 0.00962624458803071 / 0.5887698933245887 | [NPY](tensors/0000972.npy) |
| 973 | `model.layers.0.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.546875 / 1.2734375 / -0.18392324447631836 / 0.640212294795235 | [NPY](tensors/0000973.npy) |
| 974 | `model.layers.0` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 65.0 / 0.024317010243733724 / 3.4282945242119123 | [NPY](tensors/0000974.npy) |
| 1053 | `model.layers.0` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.375 / 29.625 / 0.05945163071155548 / 2.589817192687879 | [NPY](tensors/0001053.npy) |
| 1054 | `model.layers.0` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001054.npy) |
| 1055 | `model.layers.0` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0001055.npy) |
| 1056 | `model.layers.0` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0001056.npy) |
| 1057 | `model.layers.0` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0001057.npy) |
| 1058 | `model.layers.0` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1059 | `model.layers.0` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1060 | `model.layers.0` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1061 | `model.layers.0.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.375 / 29.625 / 0.05945163071155548 / 2.589817192687879 | [NPY](tensors/0001061.npy) |
| 1062 | `model.layers.0.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.875 / 8.0 / 0.015711419449912178 / 0.7391480555883723 | [NPY](tensors/0001062.npy) |
| 1063 | `model.layers.0.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.875 / 8.0 / 0.015711419449912178 / 0.7391480555883723 | [NPY](tensors/0001063.npy) |
| 1064 | `model.layers.0.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001064.npy) |
| 1065 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0001065.npy) |
| 1066 | `model.layers.0.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1067 | `model.layers.0.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1068 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0001068.npy) |
| 1069 | `model.layers.0.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0001069.npy) |
| 1070 | `model.layers.0.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1071 | `model.layers.0.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.875 / 8.0 / 0.015711419449912178 / 0.7391480555883723 | [NPY](tensors/0001071.npy) |
| 1072 | `model.layers.0.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.4375 / 8.6875 / 0.019142933073453605 / 1.0001132339927892 | [NPY](tensors/0001072.npy) |
| 1073 | `model.layers.0.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.875 / 8.0 / 0.015711419449912178 / 0.7391480555883723 | [NPY](tensors/0001073.npy) |
| 1074 | `model.layers.0.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -55.25 / 50.25 / -0.08650314807891846 / 5.914248074644324 | [NPY](tensors/0001074.npy) |
| 1075 | `model.layers.0.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.875 / 8.0 / 0.015711419449912178 / 0.7391480555883723 | [NPY](tensors/0001075.npy) |
| 1076 | `model.layers.0.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.53125 / 3.78125 / -0.12119460105895996 / 1.1960588620113954 | [NPY](tensors/0001076.npy) |
| 1077 | `model.layers.0.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.46875 / 4.84375 / -0.034735149041807745 / 0.6117560049328309 | [NPY](tensors/0001077.npy) |
| 1078 | `model.layers.0.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.625 / 47.25 / 0.03141141910519865 / 1.4428735987923489 | [NPY](tensors/0001078.npy) |
| 1079 | `model.layers.0.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.625 / 47.25 / 0.03141141910519865 / 1.4428735987923489 | [NPY](tensors/0001079.npy) |
| 1080 | `model.layers.0.self_attn` | 9 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0031668050057050163 / 0.03746767807498638 | [NPY](tensors/0001080.npy) |
| 1081 | `model.layers.0.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 46.75 / 0.09087483882904053 / 3.047666528612914 | [NPY](tensors/0001081.npy) |
| 1082 | `model.layers.0.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.3203125 / 1.515625 / 0.008010154631402757 / 0.34733566431148283 | [NPY](tensors/0001082.npy) |
| 1083 | `model.layers.0.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.3203125 / 1.515625 / 0.008010154631402757 / 0.34733566431148283 | [NPY](tensors/0001083.npy) |
| 1084 | `model.layers.0.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.3203125 / 1.515625 / 0.008010154631402757 / 0.34733566431148283 | [NPY](tensors/0001084.npy) |
| 1085 | `model.layers.0.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1086 | `model.layers.0.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1087 | `model.layers.0.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1088 | `model.layers.0.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.9375 / 30.0 / 0.01917482829756207 / 0.8602789903127944 | [NPY](tensors/0001088.npy) |
| 1089 | `model.layers.0.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.9375 / 30.0 / 0.01917482829756207 / 0.8602789903127944 | [NPY](tensors/0001089.npy) |
| 1090 | `model.layers.0.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.765625 / 1.6875 / -0.14972496032714844 / 0.6993543096816108 | [NPY](tensors/0001090.npy) |
| 1091 | `model.layers.0` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 75.5 / 0.10999682214525011 / 3.498992783335408 | [NPY](tensors/0001091.npy) |
| 1170 | `model.layers.0` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 36.5 / 0.003960044019752079 / 2.604051180596326 | [NPY](tensors/0001170.npy) |
| 1171 | `model.layers.0` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001171.npy) |
| 1172 | `model.layers.0` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0001172.npy) |
| 1173 | `model.layers.0` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0001173.npy) |
| 1174 | `model.layers.0` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0001174.npy) |
| 1175 | `model.layers.0` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1176 | `model.layers.0` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1177 | `model.layers.0` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1178 | `model.layers.0.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 36.5 / 0.003960044019752079 / 2.604051180596326 | [NPY](tensors/0001178.npy) |
| 1179 | `model.layers.0.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0001179.npy) |
| 1180 | `model.layers.0.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0001180.npy) |
| 1181 | `model.layers.0.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001181.npy) |
| 1182 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0001182.npy) |
| 1183 | `model.layers.0.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1184 | `model.layers.0.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1185 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0001185.npy) |
| 1186 | `model.layers.0.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0001186.npy) |
| 1187 | `model.layers.0.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1188 | `model.layers.0.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0001188.npy) |
| 1189 | `model.layers.0.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.875 / 0.01883023022674024 / 0.9918892179158483 | [NPY](tensors/0001189.npy) |
| 1190 | `model.layers.0.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0001190.npy) |
| 1191 | `model.layers.0.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -59.0 / 65.0 / 0.14313117787241936 / 6.505845010629575 | [NPY](tensors/0001191.npy) |
| 1192 | `model.layers.0.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0001192.npy) |
| 1193 | `model.layers.0.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.234375 / 2.921875 / 0.04315391927957535 / 0.7946671204576984 | [NPY](tensors/0001193.npy) |
| 1194 | `model.layers.0.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.15625 / 4.03125 / 0.0057423864273005165 / 0.4220409697651807 | [NPY](tensors/0001194.npy) |
| 1195 | `model.layers.0.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5 / 38.5 / 0.032015605519215264 / 1.1038383765070627 | [NPY](tensors/0001195.npy) |
| 1196 | `model.layers.0.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.5 / 38.5 / 0.032015605519215264 / 1.1038383765070627 | [NPY](tensors/0001196.npy) |
| 1197 | `model.layers.0.self_attn` | 10 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002592297033915744 / 0.02694691993787531 | [NPY](tensors/0001197.npy) |
| 1198 | `model.layers.0.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.5 / 37.0 / 0.03597632514105903 / 2.689014050046197 | [NPY](tensors/0001198.npy) |
| 1199 | `model.layers.0.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.953125 / 1.953125 / 0.0017636491192711723 / 0.3206049707668855 | [NPY](tensors/0001199.npy) |
| 1200 | `model.layers.0.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.953125 / 1.953125 / 0.0017636491192711723 / 0.3206049707668855 | [NPY](tensors/0001200.npy) |
| 1201 | `model.layers.0.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.953125 / 1.953125 / 0.0017636491192711723 / 0.3206049707668855 | [NPY](tensors/0001201.npy) |
| 1202 | `model.layers.0.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1203 | `model.layers.0.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1204 | `model.layers.0.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1205 | `model.layers.0.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.3125 / 12.0 / 0.008526665241354042 / 0.4815289367385008 | [NPY](tensors/0001205.npy) |
| 1206 | `model.layers.0.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.3125 / 12.0 / 0.008526665241354042 / 0.4815289367385008 | [NPY](tensors/0001206.npy) |
| 1207 | `model.layers.0.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.84375 / 2.234375 / -0.01921844482421875 / 1.5432858711423072 | [NPY](tensors/0001207.npy) |
| 1208 | `model.layers.0` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.5 / 44.25 / 0.04455810123019748 / 2.69135540822458 | [NPY](tensors/0001208.npy) |
| 1287 | `model.layers.0` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 38.0 / -0.06326880652664436 / 2.951675969690126 | [NPY](tensors/0001287.npy) |
| 1288 | `model.layers.0` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001288.npy) |
| 1289 | `model.layers.0` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0001289.npy) |
| 1290 | `model.layers.0` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0001290.npy) |
| 1291 | `model.layers.0` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0001291.npy) |
| 1292 | `model.layers.0` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1293 | `model.layers.0` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1294 | `model.layers.0` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1295 | `model.layers.0.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 38.0 / -0.06326880652664436 / 2.951675969690126 | [NPY](tensors/0001295.npy) |
| 1296 | `model.layers.0.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.625 / 7.84375 / -0.016052363978491888 / 0.7668244063012224 | [NPY](tensors/0001296.npy) |
| 1297 | `model.layers.0.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.625 / 7.84375 / -0.016052363978491888 / 0.7668244063012224 | [NPY](tensors/0001297.npy) |
| 1298 | `model.layers.0.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001298.npy) |
| 1299 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0001299.npy) |
| 1300 | `model.layers.0.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1301 | `model.layers.0.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1302 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0001302.npy) |
| 1303 | `model.layers.0.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0001303.npy) |
| 1304 | `model.layers.0.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1305 | `model.layers.0.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.625 / 7.84375 / -0.016052363978491888 / 0.7668244063012224 | [NPY](tensors/0001305.npy) |
| 1306 | `model.layers.0.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.25 / 7.21875 / 0.03142339817713946 / 0.940898415448983 | [NPY](tensors/0001306.npy) |
| 1307 | `model.layers.0.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.625 / 7.84375 / -0.016052363978491888 / 0.7668244063012224 | [NPY](tensors/0001307.npy) |
| 1308 | `model.layers.0.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.25 / 48.5 / -0.038690418004989624 / 5.169497433852926 | [NPY](tensors/0001308.npy) |
| 1309 | `model.layers.0.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.625 / 7.84375 / -0.016052363978491888 / 0.7668244063012224 | [NPY](tensors/0001309.npy) |
| 1310 | `model.layers.0.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.90625 / 5.46875 / -0.07878408581018448 / 1.2143039235485282 | [NPY](tensors/0001310.npy) |
| 1311 | `model.layers.0.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.4375 / 4.21875 / 0.0026221377140700497 / 0.4740744478814309 | [NPY](tensors/0001311.npy) |
| 1312 | `model.layers.0.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.3125 / 46.5 / 0.03872991734080845 / 1.3410972867088677 | [NPY](tensors/0001312.npy) |
| 1313 | `model.layers.0.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.3125 / 46.5 / 0.03872991734080845 / 1.3410972867088677 | [NPY](tensors/0001313.npy) |
| 1314 | `model.layers.0.self_attn` | 11 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0031249381261008874 / 0.033704234432634074 | [NPY](tensors/0001314.npy) |
| 1315 | `model.layers.0.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 45.0 / -0.024677817026774088 / 3.238897297775875 | [NPY](tensors/0001315.npy) |
| 1316 | `model.layers.0.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.78125 / 1.953125 / 0.0008011516597535875 / 0.3228960775800032 | [NPY](tensors/0001316.npy) |
| 1317 | `model.layers.0.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.78125 / 1.953125 / 0.0008011516597535875 / 0.3228960775800032 | [NPY](tensors/0001317.npy) |
| 1318 | `model.layers.0.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.78125 / 1.953125 / 0.0008011516597535875 / 0.3228960775800032 | [NPY](tensors/0001318.npy) |
| 1319 | `model.layers.0.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1320 | `model.layers.0.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1321 | `model.layers.0.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1322 | `model.layers.0.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.15625 / 24.875 / 0.02569689154624939 / 0.7133869974794443 | [NPY](tensors/0001322.npy) |
| 1323 | `model.layers.0.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.15625 / 24.875 / 0.02569689154624939 / 0.7133869974794443 | [NPY](tensors/0001323.npy) |
| 1324 | `model.layers.0.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.03125 / 0.890625 / -0.1773700714111328 / 0.7446297430572146 | [NPY](tensors/0001324.npy) |
| 1325 | `model.layers.0` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 70.0 / 0.0008719629711574978 / 3.519571188088565 | [NPY](tensors/0001325.npy) |
| 1404 | `model.layers.0` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 31.875 / -0.02020004838705063 / 2.9122038503504397 | [NPY](tensors/0001404.npy) |
| 1405 | `model.layers.0` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001405.npy) |
| 1406 | `model.layers.0` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0001406.npy) |
| 1407 | `model.layers.0` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0001407.npy) |
| 1408 | `model.layers.0` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0001408.npy) |
| 1409 | `model.layers.0` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1410 | `model.layers.0` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1411 | `model.layers.0` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1412 | `model.layers.0.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 31.875 / -0.02020004838705063 / 2.9122038503504397 | [NPY](tensors/0001412.npy) |
| 1413 | `model.layers.0.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0 / 8.6875 / -0.00791252214047644 / 0.7453222329310414 | [NPY](tensors/0001413.npy) |
| 1414 | `model.layers.0.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0 / 8.6875 / -0.00791252214047644 / 0.7453222329310414 | [NPY](tensors/0001414.npy) |
| 1415 | `model.layers.0.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001415.npy) |
| 1416 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0001416.npy) |
| 1417 | `model.layers.0.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1418 | `model.layers.0.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1419 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0001419.npy) |
| 1420 | `model.layers.0.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0001420.npy) |
| 1421 | `model.layers.0.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1422 | `model.layers.0.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0 / 8.6875 / -0.00791252214047644 / 0.7453222329310414 | [NPY](tensors/0001422.npy) |
| 1423 | `model.layers.0.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 8.1875 / 0.02979311952367425 / 1.0196444892687007 | [NPY](tensors/0001423.npy) |
| 1424 | `model.layers.0.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0 / 8.6875 / -0.00791252214047644 / 0.7453222329310414 | [NPY](tensors/0001424.npy) |
| 1425 | `model.layers.0.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -55.0 / 41.25 / -0.027835845947265625 / 5.524087109562007 | [NPY](tensors/0001425.npy) |
| 1426 | `model.layers.0.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0 / 8.6875 / -0.00791252214047644 / 0.7453222329310414 | [NPY](tensors/0001426.npy) |
| 1427 | `model.layers.0.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.9375 / 5.3125 / -0.06936751306056976 / 1.264370457214429 | [NPY](tensors/0001427.npy) |
| 1428 | `model.layers.0.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.875 / 4.65625 / -0.03018899138260167 / 0.6091089190486203 | [NPY](tensors/0001428.npy) |
| 1429 | `model.layers.0.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.375 / 47.25 / 0.03235033783647749 / 1.4122145007499083 | [NPY](tensors/0001429.npy) |
| 1430 | `model.layers.0.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.375 / 47.25 / 0.03235033783647749 / 1.4122145007499083 | [NPY](tensors/0001430.npy) |
| 1431 | `model.layers.0.self_attn` | 12 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0033284565490635815 / 0.036536145302269 | [NPY](tensors/0001431.npy) |
| 1432 | `model.layers.0.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.5 / 45.5 / 0.012062750922309028 / 3.2869917483612534 | [NPY](tensors/0001432.npy) |
| 1433 | `model.layers.0.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.234375 / 1.8359375 / -0.0009661224153306749 / 0.31282359310370117 | [NPY](tensors/0001433.npy) |
| 1434 | `model.layers.0.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.234375 / 1.8359375 / -0.0009661224153306749 / 0.31282359310370117 | [NPY](tensors/0001434.npy) |
| 1435 | `model.layers.0.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.234375 / 1.8359375 / -0.0009661224153306749 / 0.31282359310370117 | [NPY](tensors/0001435.npy) |
| 1436 | `model.layers.0.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1437 | `model.layers.0.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1438 | `model.layers.0.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1439 | `model.layers.0.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -11.6875 / 14.125 / 0.002018608897924423 / 0.5369711606178572 | [NPY](tensors/0001439.npy) |
| 1440 | `model.layers.0.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.6875 / 14.125 / 0.002018608897924423 / 0.5369711606178572 | [NPY](tensors/0001440.npy) |
| 1441 | `model.layers.0.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.53125 / 1.203125 / -0.13079833984375 / 0.7151954077747091 | [NPY](tensors/0001441.npy) |
| 1442 | `model.layers.0` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.25 / 59.5 / 0.014249817530314127 / 3.444271950617546 | [NPY](tensors/0001442.npy) |
| 1521 | `model.layers.0` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 36.5 / 0.003960044019752079 / 2.604051180596326 | [NPY](tensors/0001521.npy) |
| 1522 | `model.layers.0` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001522.npy) |
| 1523 | `model.layers.0` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0001523.npy) |
| 1524 | `model.layers.0` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0001524.npy) |
| 1525 | `model.layers.0` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0001525.npy) |
| 1526 | `model.layers.0` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1527 | `model.layers.0` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1528 | `model.layers.0` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1529 | `model.layers.0.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 36.5 / 0.003960044019752079 / 2.604051180596326 | [NPY](tensors/0001529.npy) |
| 1530 | `model.layers.0.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0001530.npy) |
| 1531 | `model.layers.0.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0001531.npy) |
| 1532 | `model.layers.0.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001532.npy) |
| 1533 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0001533.npy) |
| 1534 | `model.layers.0.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1535 | `model.layers.0.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1536 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0001536.npy) |
| 1537 | `model.layers.0.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0001537.npy) |
| 1538 | `model.layers.0.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1539 | `model.layers.0.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0001539.npy) |
| 1540 | `model.layers.0.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.875 / 0.01883023022674024 / 0.9918892179158483 | [NPY](tensors/0001540.npy) |
| 1541 | `model.layers.0.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0001541.npy) |
| 1542 | `model.layers.0.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -59.0 / 65.0 / 0.14313117787241936 / 6.505845010629575 | [NPY](tensors/0001542.npy) |
| 1543 | `model.layers.0.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.125 / 10.4375 / -0.0035582956340577867 / 0.7892471012533537 | [NPY](tensors/0001543.npy) |
| 1544 | `model.layers.0.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.234375 / 2.921875 / 0.04315391927957535 / 0.7946671204576984 | [NPY](tensors/0001544.npy) |
| 1545 | `model.layers.0.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.15625 / 4.03125 / 0.008465779630569159 / 0.42998898987664486 | [NPY](tensors/0001545.npy) |
| 1546 | `model.layers.0.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0 / 35.25 / 0.020171455236979656 / 1.037607610232405 | [NPY](tensors/0001546.npy) |
| 1547 | `model.layers.0.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.0 / 35.25 / 0.020171455236979656 / 1.037607610232405 | [NPY](tensors/0001547.npy) |
| 1548 | `model.layers.0.self_attn` | 13 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002759754520230741 / 0.03074770819426648 | [NPY](tensors/0001548.npy) |
| 1549 | `model.layers.0.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 36.5 / 0.02410313818189833 / 2.6425770425663146 | [NPY](tensors/0001549.npy) |
| 1550 | `model.layers.0.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.953125 / 1.9609375 / -0.0024398373232947454 / 0.31496793377857657 | [NPY](tensors/0001550.npy) |
| 1551 | `model.layers.0.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.953125 / 1.9609375 / -0.0024398373232947454 / 0.31496793377857657 | [NPY](tensors/0001551.npy) |
| 1552 | `model.layers.0.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.953125 / 1.9609375 / -0.0024398373232947454 / 0.31496793377857657 | [NPY](tensors/0001552.npy) |
| 1553 | `model.layers.0.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1554 | `model.layers.0.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1555 | `model.layers.0.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1556 | `model.layers.0.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.5625 / 13.4375 / 0.006369631282157368 / 0.5355859375906772 | [NPY](tensors/0001556.npy) |
| 1557 | `model.layers.0.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.5625 / 13.4375 / 0.006369631282157368 / 0.5355859375906772 | [NPY](tensors/0001557.npy) |
| 1558 | `model.layers.0.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.6875 / 2.28125 / -0.0304412841796875 / 1.514829734755979 | [NPY](tensors/0001558.npy) |
| 1559 | `model.layers.0` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 42.5 / 0.030535724427964952 / 2.6502184210615574 | [NPY](tensors/0001559.npy) |
| 1638 | `model.layers.0` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -71.5 / 37.5 / 0.009075783358679878 / 2.9823669690542474 | [NPY](tensors/0001638.npy) |
| 1639 | `model.layers.0` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001639.npy) |
| 1640 | `model.layers.0` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0001640.npy) |
| 1641 | `model.layers.0` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0001641.npy) |
| 1642 | `model.layers.0` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0001642.npy) |
| 1643 | `model.layers.0` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1644 | `model.layers.0` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1645 | `model.layers.0` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1646 | `model.layers.0.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -71.5 / 37.5 / 0.009075783358679878 / 2.9823669690542474 | [NPY](tensors/0001646.npy) |
| 1647 | `model.layers.0.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.0625 / 8.875 / -0.0029986129866706 / 0.745512106171101 | [NPY](tensors/0001647.npy) |
| 1648 | `model.layers.0.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.0625 / 8.875 / -0.0029986129866706 / 0.745512106171101 | [NPY](tensors/0001648.npy) |
| 1649 | `model.layers.0.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001649.npy) |
| 1650 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0001650.npy) |
| 1651 | `model.layers.0.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1652 | `model.layers.0.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1653 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0001653.npy) |
| 1654 | `model.layers.0.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0001654.npy) |
| 1655 | `model.layers.0.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1656 | `model.layers.0.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.0625 / 8.875 / -0.0029986129866706 / 0.745512106171101 | [NPY](tensors/0001656.npy) |
| 1657 | `model.layers.0.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.15625 / 8.9375 / 0.028376701433444396 / 1.0086632614938627 | [NPY](tensors/0001657.npy) |
| 1658 | `model.layers.0.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.0625 / 8.875 / -0.0029986129866706 / 0.745512106171101 | [NPY](tensors/0001658.npy) |
| 1659 | `model.layers.0.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -47.75 / 51.75 / 0.07890784740447998 / 5.378659246455776 | [NPY](tensors/0001659.npy) |
| 1660 | `model.layers.0.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.0625 / 8.875 / -0.0029986129866706 / 0.745512106171101 | [NPY](tensors/0001660.npy) |
| 1661 | `model.layers.0.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.6875 / 5.15625 / -0.0656258761882782 / 1.2458672546530496 | [NPY](tensors/0001661.npy) |
| 1662 | `model.layers.0.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.375 / 5.375 / -0.0018927457858808339 / 0.5340894478617741 | [NPY](tensors/0001662.npy) |
| 1663 | `model.layers.0.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.75 / 43.5 / 0.03327575913733906 / 1.2817262151268747 | [NPY](tensors/0001663.npy) |
| 1664 | `model.layers.0.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.75 / 43.5 / 0.03327575913733906 / 1.2817262151268747 | [NPY](tensors/0001664.npy) |
| 1665 | `model.layers.0.self_attn` | 14 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0036652190775259305 / 0.037977267656742156 | [NPY](tensors/0001665.npy) |
| 1666 | `model.layers.0.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 47.5 / 0.04248112572564019 / 3.237845893284782 | [NPY](tensors/0001666.npy) |
| 1667 | `model.layers.0.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.90625 / 1.765625 / 0.0013462993833753799 / 0.31077504154073765 | [NPY](tensors/0001667.npy) |
| 1668 | `model.layers.0.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.90625 / 1.765625 / 0.0013462993833753799 / 0.31077504154073765 | [NPY](tensors/0001668.npy) |
| 1669 | `model.layers.0.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.90625 / 1.765625 / 0.0013462993833753799 / 0.31077504154073765 | [NPY](tensors/0001669.npy) |
| 1670 | `model.layers.0.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1671 | `model.layers.0.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1672 | `model.layers.0.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1673 | `model.layers.0.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -19.875 / 26.75 / 0.02124463833040661 / 0.8689174827493475 | [NPY](tensors/0001673.npy) |
| 1674 | `model.layers.0.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.875 / 26.75 / 0.02124463833040661 / 0.8689174827493475 | [NPY](tensors/0001674.npy) |
| 1675 | `model.layers.0.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.578125 / 1.25 / -0.15576553344726562 / 0.7938957412866728 | [NPY](tensors/0001675.npy) |
| 1676 | `model.layers.0` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.0 / 74.0 / 0.06348152160644531 / 3.5859981591160808 | [NPY](tensors/0001676.npy) |
| 1755 | `model.layers.0` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 32.5 / -0.08864142522215843 / 2.810578421971992 | [NPY](tensors/0001755.npy) |
| 1756 | `model.layers.0` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001756.npy) |
| 1757 | `model.layers.0` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0001757.npy) |
| 1758 | `model.layers.0` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0001758.npy) |
| 1759 | `model.layers.0` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0001759.npy) |
| 1760 | `model.layers.0` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1761 | `model.layers.0` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1762 | `model.layers.0` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1763 | `model.layers.0.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 32.5 / -0.08864142522215843 / 2.810578421971992 | [NPY](tensors/0001763.npy) |
| 1764 | `model.layers.0.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 10.0 / -0.029531719618373448 / 0.8066069227499595 | [NPY](tensors/0001764.npy) |
| 1765 | `model.layers.0.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 10.0 / -0.029531719618373448 / 0.8066069227499595 | [NPY](tensors/0001765.npy) |
| 1766 | `model.layers.0.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001766.npy) |
| 1767 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0001767.npy) |
| 1768 | `model.layers.0.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1769 | `model.layers.0.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1770 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0001770.npy) |
| 1771 | `model.layers.0.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0001771.npy) |
| 1772 | `model.layers.0.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1773 | `model.layers.0.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 10.0 / -0.029531719618373448 / 0.8066069227499595 | [NPY](tensors/0001773.npy) |
| 1774 | `model.layers.0.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.28125 / 8.8125 / 0.03415511851198971 / 0.9911786094445456 | [NPY](tensors/0001774.npy) |
| 1775 | `model.layers.0.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 10.0 / -0.029531719618373448 / 0.8066069227499595 | [NPY](tensors/0001775.npy) |
| 1776 | `model.layers.0.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -55.75 / 43.25 / -0.06454649940133095 / 5.556119905230212 | [NPY](tensors/0001776.npy) |
| 1777 | `model.layers.0.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 10.0 / -0.029531719618373448 / 0.8066069227499595 | [NPY](tensors/0001777.npy) |
| 1778 | `model.layers.0.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.125 / 5.8125 / -0.11264276504516602 / 1.2232508657301422 | [NPY](tensors/0001778.npy) |
| 1779 | `model.layers.0.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.34375 / 5.0 / -0.022161657725519035 / 0.5176085736942049 | [NPY](tensors/0001779.npy) |
| 1780 | `model.layers.0.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.0 / 44.5 / 0.03228669944736692 / 1.3000709017192693 | [NPY](tensors/0001780.npy) |
| 1781 | `model.layers.0.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.0 / 44.5 / 0.03228669944736692 / 1.3000709017192693 | [NPY](tensors/0001781.npy) |
| 1782 | `model.layers.0.self_attn` | 15 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98046875 / 0.0031267409488809367 / 0.030839397600700386 | [NPY](tensors/0001782.npy) |
| 1783 | `model.layers.0.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 42.0 / -0.056280024846394855 / 3.095930436335049 | [NPY](tensors/0001783.npy) |
| 1784 | `model.layers.0.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.0625 / 2.15625 / -0.0047982003953721784 / 0.33808056635032124 | [NPY](tensors/0001784.npy) |
| 1785 | `model.layers.0.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.0625 / 2.15625 / -0.0047982003953721784 / 0.33808056635032124 | [NPY](tensors/0001785.npy) |
| 1786 | `model.layers.0.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.0625 / 2.15625 / -0.0047982003953721784 / 0.33808056635032124 | [NPY](tensors/0001786.npy) |
| 1787 | `model.layers.0.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1788 | `model.layers.0.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1789 | `model.layers.0.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1790 | `model.layers.0.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -16.625 / 22.125 / -0.008275091606709693 / 0.7223706444751093 | [NPY](tensors/0001790.npy) |
| 1791 | `model.layers.0.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.625 / 22.125 / -0.008275091606709693 / 0.7223706444751093 | [NPY](tensors/0001791.npy) |
| 1792 | `model.layers.0.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.046875 / 1.4921875 / -0.18393325805664062 / 0.7765901837874033 | [NPY](tensors/0001792.npy) |
| 1793 | `model.layers.0` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -56.5 / 62.5 / -0.064541052447425 / 3.435009377967022 | [NPY](tensors/0001793.npy) |
| 1872 | `model.layers.0` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.375 / 29.625 / 0.05945163071155548 / 2.589817192687879 | [NPY](tensors/0001872.npy) |
| 1873 | `model.layers.0` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001873.npy) |
| 1874 | `model.layers.0` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0001874.npy) |
| 1875 | `model.layers.0` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0001875.npy) |
| 1876 | `model.layers.0` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0001876.npy) |
| 1877 | `model.layers.0` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1878 | `model.layers.0` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1879 | `model.layers.0` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1880 | `model.layers.0.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.375 / 29.625 / 0.05945163071155548 / 2.589817192687879 | [NPY](tensors/0001880.npy) |
| 1881 | `model.layers.0.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.875 / 8.0 / 0.015711419449912178 / 0.7391480555883723 | [NPY](tensors/0001881.npy) |
| 1882 | `model.layers.0.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.875 / 8.0 / 0.015711419449912178 / 0.7391480555883723 | [NPY](tensors/0001882.npy) |
| 1883 | `model.layers.0.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001883.npy) |
| 1884 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0001884.npy) |
| 1885 | `model.layers.0.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1886 | `model.layers.0.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1887 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0001887.npy) |
| 1888 | `model.layers.0.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0001888.npy) |
| 1889 | `model.layers.0.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1890 | `model.layers.0.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.875 / 8.0 / 0.015711419449912178 / 0.7391480555883723 | [NPY](tensors/0001890.npy) |
| 1891 | `model.layers.0.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.4375 / 8.6875 / 0.019142933073453605 / 1.0001132339927892 | [NPY](tensors/0001891.npy) |
| 1892 | `model.layers.0.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.875 / 8.0 / 0.015711419449912178 / 0.7391480555883723 | [NPY](tensors/0001892.npy) |
| 1893 | `model.layers.0.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -55.25 / 50.25 / -0.08650314807891846 / 5.914248074644324 | [NPY](tensors/0001893.npy) |
| 1894 | `model.layers.0.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.875 / 8.0 / 0.015711419449912178 / 0.7391480555883723 | [NPY](tensors/0001894.npy) |
| 1895 | `model.layers.0.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.53125 / 3.78125 / -0.12119460105895996 / 1.1960588620113954 | [NPY](tensors/0001895.npy) |
| 1896 | `model.layers.0.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.375 / 4.4375 / -0.020306347199948505 / 0.6157170510811459 | [NPY](tensors/0001896.npy) |
| 1897 | `model.layers.0.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.875 / 48.25 / 0.02851252125369178 / 1.494185516994768 | [NPY](tensors/0001897.npy) |
| 1898 | `model.layers.0.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.875 / 48.25 / 0.02851252125369178 / 1.494185516994768 | [NPY](tensors/0001898.npy) |
| 1899 | `model.layers.0.self_attn` | 16 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0034201569781659733 / 0.03618479229608628 | [NPY](tensors/0001899.npy) |
| 1900 | `model.layers.0.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 46.75 / 0.08809480667114258 / 3.078317166203887 | [NPY](tensors/0001900.npy) |
| 1901 | `model.layers.0.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.390625 / 1.5703125 / 0.008344769229491551 / 0.34297829284844095 | [NPY](tensors/0001901.npy) |
| 1902 | `model.layers.0.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.390625 / 1.5703125 / 0.008344769229491551 / 0.34297829284844095 | [NPY](tensors/0001902.npy) |
| 1903 | `model.layers.0.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.390625 / 1.5703125 / 0.008344769229491551 / 0.34297829284844095 | [NPY](tensors/0001903.npy) |
| 1904 | `model.layers.0.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1905 | `model.layers.0.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1906 | `model.layers.0.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1907 | `model.layers.0.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.4375 / 28.25 / 0.016603716711203257 / 0.7662003067489941 | [NPY](tensors/0001907.npy) |
| 1908 | `model.layers.0.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.4375 / 28.25 / 0.016603716711203257 / 0.7662003067489941 | [NPY](tensors/0001908.npy) |
| 1909 | `model.layers.0.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.828125 / 1.46875 / -0.14823603630065918 / 0.7231812759960349 | [NPY](tensors/0001909.npy) |
| 1910 | `model.layers.0` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 75.0 / 0.10473717053731282 / 3.4877094322746096 | [NPY](tensors/0001910.npy) |
| 1989 | `model.layers.0` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001989.npy) |
| 1990 | `model.layers.0` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001990.npy) |
| 1991 | `model.layers.0` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0001991.npy) |
| 1992 | `model.layers.0` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0001992.npy) |
| 1993 | `model.layers.0` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0001993.npy) |
| 1994 | `model.layers.0` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1995 | `model.layers.0` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1996 | `model.layers.0` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1997 | `model.layers.0.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0001997.npy) |
| 1998 | `model.layers.0.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001998.npy) |
| 1999 | `model.layers.0.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0001999.npy) |
| 2000 | `model.layers.0.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002000.npy) |
| 2001 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0002001.npy) |
| 2002 | `model.layers.0.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2003 | `model.layers.0.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2004 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0002004.npy) |
| 2005 | `model.layers.0.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0002005.npy) |
| 2006 | `model.layers.0.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2007 | `model.layers.0.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0002007.npy) |
| 2008 | `model.layers.0.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.84375 / 8.5625 / 0.0153301190584898 / 1.0113524420299036 | [NPY](tensors/0002008.npy) |
| 2009 | `model.layers.0.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0002009.npy) |
| 2010 | `model.layers.0.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.0 / 65.5 / 0.032654017210006714 / 6.89507515667232 | [NPY](tensors/0002010.npy) |
| 2011 | `model.layers.0.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0002011.npy) |
| 2012 | `model.layers.0.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.28125 / 3.390625 / -0.002120666205883026 / 0.8566653376613583 | [NPY](tensors/0002012.npy) |
| 2013 | `model.layers.0.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.1875 / 3.6875 / -0.002445327716486645 / 0.45431221867222815 | [NPY](tensors/0002013.npy) |
| 2014 | `model.layers.0.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.875 / 33.75 / 0.034584098392062716 / 1.0644307851176895 | [NPY](tensors/0002014.npy) |
| 2015 | `model.layers.0.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.875 / 33.75 / 0.034584098392062716 / 1.0644307851176895 | [NPY](tensors/0002015.npy) |
| 2016 | `model.layers.0.self_attn` | 17 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0029736309388561626 / 0.028434558809664702 | [NPY](tensors/0002016.npy) |
| 2017 | `model.layers.0.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.75 / 37.0 / 0.03258286582099067 / 3.046097856449091 | [NPY](tensors/0002017.npy) |
| 2018 | `model.layers.0.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.578125 / 1.3828125 / 0.0009039461612701416 / 0.28850703519420345 | [NPY](tensors/0002018.npy) |
| 2019 | `model.layers.0.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.578125 / 1.3828125 / 0.0009039461612701416 / 0.28850703519420345 | [NPY](tensors/0002019.npy) |
| 2020 | `model.layers.0.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.578125 / 1.3828125 / 0.0009039461612701416 / 0.28850703519420345 | [NPY](tensors/0002020.npy) |
| 2021 | `model.layers.0.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2022 | `model.layers.0.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2023 | `model.layers.0.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2024 | `model.layers.0.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.53125 / 14.1875 / 0.016956719590557945 / 0.6237318387535244 | [NPY](tensors/0002024.npy) |
| 2025 | `model.layers.0.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.53125 / 14.1875 / 0.016956719590557945 / 0.6237318387535244 | [NPY](tensors/0002025.npy) |
| 2026 | `model.layers.0.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.15625 / 2.671875 / -0.0182037353515625 / 1.4358765255243753 | [NPY](tensors/0002026.npy) |
| 2027 | `model.layers.0` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.25 / 51.25 / 0.049710252549913195 / 2.9991697585269987 | [NPY](tensors/0002027.npy) |
| 2106 | `model.layers.0` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 49.25 / -0.03481262918147776 / 3.3040972398817177 | [NPY](tensors/0002106.npy) |
| 2107 | `model.layers.0` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002107.npy) |
| 2108 | `model.layers.0` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0002108.npy) |
| 2109 | `model.layers.0` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0002109.npy) |
| 2110 | `model.layers.0` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0002110.npy) |
| 2111 | `model.layers.0` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2112 | `model.layers.0` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2113 | `model.layers.0` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2114 | `model.layers.0.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 49.25 / -0.03481262918147776 / 3.3040972398817177 | [NPY](tensors/0002114.npy) |
| 2115 | `model.layers.0.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0002115.npy) |
| 2116 | `model.layers.0.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0002116.npy) |
| 2117 | `model.layers.0.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002117.npy) |
| 2118 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0002118.npy) |
| 2119 | `model.layers.0.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2120 | `model.layers.0.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2121 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0002121.npy) |
| 2122 | `model.layers.0.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0002122.npy) |
| 2123 | `model.layers.0.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2124 | `model.layers.0.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0002124.npy) |
| 2125 | `model.layers.0.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 6.25 / 0.025897369312588125 / 0.9110042125091211 | [NPY](tensors/0002125.npy) |
| 2126 | `model.layers.0.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0002126.npy) |
| 2127 | `model.layers.0.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.75 / 46.25 / 0.08283017575740814 / 5.101942263816244 | [NPY](tensors/0002127.npy) |
| 2128 | `model.layers.0.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.375 / 11.125 / -0.011280816379520628 / 0.742495217287664 | [NPY](tensors/0002128.npy) |
| 2129 | `model.layers.0.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.765625 / 3.28125 / 0.0731726735830307 / 0.9884409409989561 | [NPY](tensors/0002129.npy) |
| 2130 | `model.layers.0.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.25 / 2.78125 / 0.005772891987362527 / 0.42513175137260356 | [NPY](tensors/0002130.npy) |
| 2131 | `model.layers.0.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.5 / 37.75 / 0.03166451988120874 / 1.0987011875704693 | [NPY](tensors/0002131.npy) |
| 2132 | `model.layers.0.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.5 / 37.75 / 0.03166451988120874 / 1.0987011875704693 | [NPY](tensors/0002132.npy) |
| 2133 | `model.layers.0.self_attn` | 18 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0032509756626826814 / 0.03234831745514616 | [NPY](tensors/0002133.npy) |
| 2134 | `model.layers.0.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 48.75 / -0.0032036940256754557 / 3.4092432597161895 | [NPY](tensors/0002134.npy) |
| 2135 | `model.layers.0.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.078125 / 2.015625 / -0.003172057867050171 / 0.29005942103074295 | [NPY](tensors/0002135.npy) |
| 2136 | `model.layers.0.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.078125 / 2.015625 / -0.003172057867050171 / 0.29005942103074295 | [NPY](tensors/0002136.npy) |
| 2137 | `model.layers.0.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.078125 / 2.015625 / -0.003172057867050171 / 0.29005942103074295 | [NPY](tensors/0002137.npy) |
| 2138 | `model.layers.0.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2139 | `model.layers.0.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2140 | `model.layers.0.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2141 | `model.layers.0.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.25 / 19.0 / 0.030066123066676987 / 0.6356850840574217 | [NPY](tensors/0002141.npy) |
| 2142 | `model.layers.0.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.25 / 19.0 / 0.030066123066676987 / 0.6356850840574217 | [NPY](tensors/0002142.npy) |
| 2143 | `model.layers.0.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.390625 / 1.59375 / -0.06692695617675781 / 0.8733802285380988 | [NPY](tensors/0002143.npy) |
| 2144 | `model.layers.0` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.25 / 49.0 / 0.027000284194946288 / 3.442761444253515 | [NPY](tensors/0002144.npy) |
| 2223 | `model.layers.0` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.625 / 30.5 / 0.04508908689022064 / 2.5992970622569604 | [NPY](tensors/0002223.npy) |
| 2224 | `model.layers.0` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002224.npy) |
| 2225 | `model.layers.0` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0002225.npy) |
| 2226 | `model.layers.0` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0002226.npy) |
| 2227 | `model.layers.0` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0002227.npy) |
| 2228 | `model.layers.0` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2229 | `model.layers.0` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2230 | `model.layers.0` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2231 | `model.layers.0.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -26.625 / 30.5 / 0.04508908689022064 / 2.5992970622569604 | [NPY](tensors/0002231.npy) |
| 2232 | `model.layers.0.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.875 / 6.6875 / 0.018102761440806917 / 0.776861650263515 | [NPY](tensors/0002232.npy) |
| 2233 | `model.layers.0.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.875 / 6.6875 / 0.018102761440806917 / 0.776861650263515 | [NPY](tensors/0002233.npy) |
| 2234 | `model.layers.0.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002234.npy) |
| 2235 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0002235.npy) |
| 2236 | `model.layers.0.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2237 | `model.layers.0.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2238 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0002238.npy) |
| 2239 | `model.layers.0.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0002239.npy) |
| 2240 | `model.layers.0.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2241 | `model.layers.0.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.875 / 6.6875 / 0.018102761440806917 / 0.776861650263515 | [NPY](tensors/0002241.npy) |
| 2242 | `model.layers.0.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.90625 / 9.875 / 0.018646324053406715 / 1.0334345205917428 | [NPY](tensors/0002242.npy) |
| 2243 | `model.layers.0.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.875 / 6.6875 / 0.018102761440806917 / 0.776861650263515 | [NPY](tensors/0002243.npy) |
| 2244 | `model.layers.0.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.75 / 53.25 / 0.04424262046813965 / 5.351344482462548 | [NPY](tensors/0002244.npy) |
| 2245 | `model.layers.0.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.875 / 6.6875 / 0.018102761440806917 / 0.776861650263515 | [NPY](tensors/0002245.npy) |
| 2246 | `model.layers.0.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.65625 / 4.90625 / -0.09139278531074524 / 1.3186347201251025 | [NPY](tensors/0002246.npy) |
| 2247 | `model.layers.0.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.40625 / 3.25 / 0.025725724117364734 / 0.48467416932728374 | [NPY](tensors/0002247.npy) |
| 2248 | `model.layers.0.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0625 / 51.25 / 0.04385285476843516 / 1.479884774163004 | [NPY](tensors/0002248.npy) |
| 2249 | `model.layers.0.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0625 / 51.25 / 0.04385285476843516 / 1.479884774163004 | [NPY](tensors/0002249.npy) |
| 2250 | `model.layers.0.self_attn` | 19 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.002883006632323425 / 0.03543228805233314 | [NPY](tensors/0002250.npy) |
| 2251 | `model.layers.0.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.125 / 53.25 / 0.08908531135982937 / 3.0482420350729296 | [NPY](tensors/0002251.npy) |
| 2252 | `model.layers.0.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.703125 / 1.671875 / 0.01578000651465522 / 0.3542716653100784 | [NPY](tensors/0002252.npy) |
| 2253 | `model.layers.0.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.703125 / 1.671875 / 0.01578000651465522 / 0.3542716653100784 | [NPY](tensors/0002253.npy) |
| 2254 | `model.layers.0.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.703125 / 1.671875 / 0.01578000651465522 / 0.3542716653100784 | [NPY](tensors/0002254.npy) |
| 2255 | `model.layers.0.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2256 | `model.layers.0.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2257 | `model.layers.0.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2258 | `model.layers.0.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.25 / 34.5 / 0.03967399855868684 / 1.0844560853286882 | [NPY](tensors/0002258.npy) |
| 2259 | `model.layers.0.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.25 / 34.5 / 0.03967399855868684 / 1.0844560853286882 | [NPY](tensors/0002259.npy) |
| 2260 | `model.layers.0.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.109375 / 1.3203125 / -0.11461162567138672 / 0.7820184248516712 | [NPY](tensors/0002260.npy) |
| 2261 | `model.layers.0` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.5 / 88.0 / 0.12899753782484266 / 3.7072567166751247 | [NPY](tensors/0002261.npy) |
| 2340 | `model.layers.0` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 44.75 / 0.013139636483457354 / 2.9607003759627655 | [NPY](tensors/0002340.npy) |
| 2341 | `model.layers.0` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002341.npy) |
| 2342 | `model.layers.0` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0002342.npy) |
| 2343 | `model.layers.0` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0002343.npy) |
| 2344 | `model.layers.0` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0002344.npy) |
| 2345 | `model.layers.0` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2346 | `model.layers.0` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2347 | `model.layers.0` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2348 | `model.layers.0.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 44.75 / 0.013139636483457354 / 2.9607003759627655 | [NPY](tensors/0002348.npy) |
| 2349 | `model.layers.0.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0002349.npy) |
| 2350 | `model.layers.0.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0002350.npy) |
| 2351 | `model.layers.0.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002351.npy) |
| 2352 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0002352.npy) |
| 2353 | `model.layers.0.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2354 | `model.layers.0.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2355 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0002355.npy) |
| 2356 | `model.layers.0.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0002356.npy) |
| 2357 | `model.layers.0.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2358 | `model.layers.0.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0002358.npy) |
| 2359 | `model.layers.0.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5625 / 8.625 / 0.03118488343898207 / 1.013318010948837 | [NPY](tensors/0002359.npy) |
| 2360 | `model.layers.0.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0002360.npy) |
| 2361 | `model.layers.0.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.25 / 44.0 / -0.021389365196228027 / 5.266550301692611 | [NPY](tensors/0002361.npy) |
| 2362 | `model.layers.0.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.75 / 9.9375 / -0.0032807601822747124 / 0.8349184849634347 | [NPY](tensors/0002362.npy) |
| 2363 | `model.layers.0.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.28125 / 4.4375 / -0.023247554898262024 / 1.2424791578118235 | [NPY](tensors/0002363.npy) |
| 2364 | `model.layers.0.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.25 / 4.34375 / -0.00031532481443719007 / 0.5602702810961412 | [NPY](tensors/0002364.npy) |
| 2365 | `model.layers.0.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.75 / 50.5 / 0.034137294358677336 / 1.4642205665174541 | [NPY](tensors/0002365.npy) |
| 2366 | `model.layers.0.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -20.75 / 50.5 / 0.034137294358677336 / 1.4642205665174541 | [NPY](tensors/0002366.npy) |
| 2367 | `model.layers.0.self_attn` | 20 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98046875 / 0.0033971580932037142 / 0.03760308454887054 | [NPY](tensors/0002367.npy) |
| 2368 | `model.layers.0.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.5 / 46.25 / 0.04728905359903971 / 3.276676994593124 | [NPY](tensors/0002368.npy) |
| 2369 | `model.layers.0.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.15625 / 1.6796875 / 0.0037877281506856282 / 0.3316808714704868 | [NPY](tensors/0002369.npy) |
| 2370 | `model.layers.0.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.15625 / 1.6796875 / 0.0037877281506856282 / 0.3316808714704868 | [NPY](tensors/0002370.npy) |
| 2371 | `model.layers.0.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -5.15625 / 1.6796875 / 0.0037877281506856282 / 0.3316808714704868 | [NPY](tensors/0002371.npy) |
| 2372 | `model.layers.0.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2373 | `model.layers.0.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2374 | `model.layers.0.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2375 | `model.layers.0.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.3125 / 18.875 / 0.012194161117076874 / 0.5978255375082625 | [NPY](tensors/0002375.npy) |
| 2376 | `model.layers.0.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.3125 / 18.875 / 0.012194161117076874 / 0.5978255375082625 | [NPY](tensors/0002376.npy) |
| 2377 | `model.layers.0.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.96875 / 1.5 / -0.18613862991333008 / 0.8569503341260833 | [NPY](tensors/0002377.npy) |
| 2378 | `model.layers.0` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 65.0 / 0.059286610285441084 / 3.519447873402264 | [NPY](tensors/0002378.npy) |
| 2457 | `model.layers.0` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 31.375 / -0.03532346973402633 / 2.513775339817436 | [NPY](tensors/0002457.npy) |
| 2458 | `model.layers.0` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002458.npy) |
| 2459 | `model.layers.0` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0002459.npy) |
| 2460 | `model.layers.0` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0002460.npy) |
| 2461 | `model.layers.0` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0002461.npy) |
| 2462 | `model.layers.0` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2463 | `model.layers.0` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2464 | `model.layers.0` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2465 | `model.layers.0.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.125 / 31.375 / -0.03532346973402633 / 2.513775339817436 | [NPY](tensors/0002465.npy) |
| 2466 | `model.layers.0.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0002466.npy) |
| 2467 | `model.layers.0.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0002467.npy) |
| 2468 | `model.layers.0.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002468.npy) |
| 2469 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0002469.npy) |
| 2470 | `model.layers.0.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2471 | `model.layers.0.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2472 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0002472.npy) |
| 2473 | `model.layers.0.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0002473.npy) |
| 2474 | `model.layers.0.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2475 | `model.layers.0.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0002475.npy) |
| 2476 | `model.layers.0.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 8.875 / -0.00043488043593242764 / 1.093332692665652 | [NPY](tensors/0002476.npy) |
| 2477 | `model.layers.0.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0002477.npy) |
| 2478 | `model.layers.0.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.0 / 57.0 / -0.11751466989517212 / 6.178501515201047 | [NPY](tensors/0002478.npy) |
| 2479 | `model.layers.0.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 8.8125 / -0.010665703585578336 / 0.7544454935222373 | [NPY](tensors/0002479.npy) |
| 2480 | `model.layers.0.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.15625 / 4.375 / -0.08698096498847008 / 1.3301958676902246 | [NPY](tensors/0002480.npy) |
| 2481 | `model.layers.0.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.34375 / 4.375 / -0.010732570110121742 / 0.6743339101947442 | [NPY](tensors/0002481.npy) |
| 2482 | `model.layers.0.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.125 / 48.75 / 0.03034556723303265 / 1.5476539600954038 | [NPY](tensors/0002482.npy) |
| 2483 | `model.layers.0.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.125 / 48.75 / 0.03034556723303265 / 1.5476539600954038 | [NPY](tensors/0002483.npy) |
| 2484 | `model.layers.0.self_attn` | 21 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003877563115317625 / 0.041195961063090585 | [NPY](tensors/0002484.npy) |
| 2485 | `model.layers.0.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.5 / 48.25 / -0.005075783199734158 / 3.052437131193535 | [NPY](tensors/0002485.npy) |
| 2486 | `model.layers.0.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.734375 / 1.640625 / -0.0017739641997549268 / 0.35380487229901453 | [NPY](tensors/0002486.npy) |
| 2487 | `model.layers.0.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.734375 / 1.640625 / -0.0017739641997549268 / 0.35380487229901453 | [NPY](tensors/0002487.npy) |
| 2488 | `model.layers.0.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.734375 / 1.640625 / -0.0017739641997549268 / 0.35380487229901453 | [NPY](tensors/0002488.npy) |
| 2489 | `model.layers.0.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2490 | `model.layers.0.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2491 | `model.layers.0.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2492 | `model.layers.0.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.9375 / 29.875 / 0.018820407738288244 / 0.8860759362523768 | [NPY](tensors/0002492.npy) |
| 2493 | `model.layers.0.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.9375 / 29.875 / 0.018820407738288244 / 0.8860759362523768 | [NPY](tensors/0002493.npy) |
| 2494 | `model.layers.0.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6640625 / 1.5859375 / -0.19756317138671875 / 0.6447902469284845 | [NPY](tensors/0002494.npy) |
| 2495 | `model.layers.0` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -58.0 / 77.0 / 0.013826458983951144 / 3.565753345694757 | [NPY](tensors/0002495.npy) |
| 2574 | `model.layers.0` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0002574.npy) |
| 2575 | `model.layers.0` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002575.npy) |
| 2576 | `model.layers.0` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0002576.npy) |
| 2577 | `model.layers.0` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0002577.npy) |
| 2578 | `model.layers.0` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0002578.npy) |
| 2579 | `model.layers.0` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2580 | `model.layers.0` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2581 | `model.layers.0` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2582 | `model.layers.0.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 36.75 / -0.002020619318096174 / 3.1439085894690497 | [NPY](tensors/0002582.npy) |
| 2583 | `model.layers.0.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0002583.npy) |
| 2584 | `model.layers.0.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0002584.npy) |
| 2585 | `model.layers.0.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002585.npy) |
| 2586 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0002586.npy) |
| 2587 | `model.layers.0.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2588 | `model.layers.0.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2589 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0002589.npy) |
| 2590 | `model.layers.0.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0002590.npy) |
| 2591 | `model.layers.0.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2592 | `model.layers.0.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0002592.npy) |
| 2593 | `model.layers.0.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.84375 / 8.5625 / 0.0153301190584898 / 1.0113524420299036 | [NPY](tensors/0002593.npy) |
| 2594 | `model.layers.0.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0002594.npy) |
| 2595 | `model.layers.0.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.0 / 65.5 / 0.032654017210006714 / 6.89507515667232 | [NPY](tensors/0002595.npy) |
| 2596 | `model.layers.0.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.125 / 7.65625 / -0.004369420516822074 / 0.755514005710006 | [NPY](tensors/0002596.npy) |
| 2597 | `model.layers.0.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.28125 / 3.390625 / -0.002120666205883026 / 0.8566653376613583 | [NPY](tensors/0002597.npy) |
| 2598 | `model.layers.0.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.15625 / 3.5625 / 0.011225185067814891 / 0.48592503756810035 | [NPY](tensors/0002598.npy) |
| 2599 | `model.layers.0.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.9375 / 33.25 / 0.03524649606810676 / 1.098663417984539 | [NPY](tensors/0002599.npy) |
| 2600 | `model.layers.0.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.9375 / 33.25 / 0.03524649606810676 / 1.098663417984539 | [NPY](tensors/0002600.npy) |
| 2601 | `model.layers.0.self_attn` | 22 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003211775392450572 / 0.033612175194755456 | [NPY](tensors/0002601.npy) |
| 2602 | `model.layers.0.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.0 / 36.5 / 0.033238728841145836 / 3.0206644318850997 | [NPY](tensors/0002602.npy) |
| 2603 | `model.layers.0.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.4140625 / 0.0007053590483135648 / 0.2909355042433378 | [NPY](tensors/0002603.npy) |
| 2604 | `model.layers.0.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.4140625 / 0.0007053590483135648 / 0.2909355042433378 | [NPY](tensors/0002604.npy) |
| 2605 | `model.layers.0.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.4140625 / 0.0007053590483135648 / 0.2909355042433378 | [NPY](tensors/0002605.npy) |
| 2606 | `model.layers.0.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2607 | `model.layers.0.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2608 | `model.layers.0.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2609 | `model.layers.0.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.03125 / 13.8125 / 0.019463080198814472 / 0.6137762056772053 | [NPY](tensors/0002609.npy) |
| 2610 | `model.layers.0.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.03125 / 13.8125 / 0.019463080198814472 / 0.6137762056772053 | [NPY](tensors/0002610.npy) |
| 2611 | `model.layers.0.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.4375 / 2.875 / -0.0088043212890625 / 1.5493138405994724 | [NPY](tensors/0002611.npy) |
| 2612 | `model.layers.0` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.375 / 50.25 / 0.05285305447048611 / 2.9627691690287214 | [NPY](tensors/0002612.npy) |
| 2691 | `model.layers.0` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 32.75 / 0.03959848284721375 / 2.636727096419094 | [NPY](tensors/0002691.npy) |
| 2692 | `model.layers.0` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002692.npy) |
| 2693 | `model.layers.0` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0002693.npy) |
| 2694 | `model.layers.0` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0002694.npy) |
| 2695 | `model.layers.0` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0002695.npy) |
| 2696 | `model.layers.0` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2697 | `model.layers.0` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2698 | `model.layers.0` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2699 | `model.layers.0.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 32.75 / 0.03959848284721375 / 2.636727096419094 | [NPY](tensors/0002699.npy) |
| 2700 | `model.layers.0.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002700.npy) |
| 2701 | `model.layers.0.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002701.npy) |
| 2702 | `model.layers.0.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002702.npy) |
| 2703 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0002703.npy) |
| 2704 | `model.layers.0.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2705 | `model.layers.0.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2706 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0002706.npy) |
| 2707 | `model.layers.0.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0002707.npy) |
| 2708 | `model.layers.0.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2709 | `model.layers.0.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002709.npy) |
| 2710 | `model.layers.0.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.0625 / 6.78125 / -0.006842018279712647 / 0.8517376388261615 | [NPY](tensors/0002710.npy) |
| 2711 | `model.layers.0.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002711.npy) |
| 2712 | `model.layers.0.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.25 / 35.75 / 0.051442623138427734 / 3.999531927842787 | [NPY](tensors/0002712.npy) |
| 2713 | `model.layers.0.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.5 / 8.75 / 3.0359625816345216e-05 / 0.8461694669061269 | [NPY](tensors/0002713.npy) |
| 2714 | `model.layers.0.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.25 / 4.625 / 0.04163137078285217 / 1.1435466539669636 | [NPY](tensors/0002714.npy) |
| 2715 | `model.layers.0.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.15625 / 2.640625 / 0.0015345531282946467 / 0.3684608363498701 | [NPY](tensors/0002715.npy) |
| 2716 | `model.layers.0.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.5 / 44.5 / 0.032654010494136146 / 1.3408593390459635 | [NPY](tensors/0002716.npy) |
| 2717 | `model.layers.0.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.5 / 44.5 / 0.032654010494136146 / 1.3408593390459635 | [NPY](tensors/0002717.npy) |
| 2718 | `model.layers.0.self_attn` | 23 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.94921875 / 0.002664449415644308 / 0.02487757853627874 | [NPY](tensors/0002718.npy) |
| 2719 | `model.layers.0.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.25 / 44.25 / 0.0722493569056193 / 2.9718317011037034 | [NPY](tensors/0002719.npy) |
| 2720 | `model.layers.0.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.21875 / 1.6875 / -0.001274604598681132 / 0.3667426744563323 | [NPY](tensors/0002720.npy) |
| 2721 | `model.layers.0.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.21875 / 1.6875 / -0.001274604598681132 / 0.3667426744563323 | [NPY](tensors/0002721.npy) |
| 2722 | `model.layers.0.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.21875 / 1.6875 / -0.001274604598681132 / 0.3667426744563323 | [NPY](tensors/0002722.npy) |
| 2723 | `model.layers.0.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2724 | `model.layers.0.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2725 | `model.layers.0.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2726 | `model.layers.0.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.625 / 24.625 / 0.04051270464228259 / 0.9079187888007254 | [NPY](tensors/0002726.npy) |
| 2727 | `model.layers.0.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.625 / 24.625 / 0.04051270464228259 / 0.9079187888007254 | [NPY](tensors/0002727.npy) |
| 2728 | `model.layers.0.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.625 / 1.78125 / -0.20586204528808594 / 0.8013374567602747 | [NPY](tensors/0002728.npy) |
| 2729 | `model.layers.0` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.625 / 69.0 / 0.11307530403137207 / 3.4795478843412986 | [NPY](tensors/0002729.npy) |
| 2808 | `model.layers.0` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 32.5 / 0.02340112761594355 / 2.5180141341639093 | [NPY](tensors/0002808.npy) |
| 2809 | `model.layers.0` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002809.npy) |
| 2810 | `model.layers.0` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0002810.npy) |
| 2811 | `model.layers.0` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0002811.npy) |
| 2812 | `model.layers.0` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0002812.npy) |
| 2813 | `model.layers.0` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2814 | `model.layers.0` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2815 | `model.layers.0` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2816 | `model.layers.0.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.875 / 32.5 / 0.02340112761594355 / 2.5180141341639093 | [NPY](tensors/0002816.npy) |
| 2817 | `model.layers.0.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002817.npy) |
| 2818 | `model.layers.0.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002818.npy) |
| 2819 | `model.layers.0.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002819.npy) |
| 2820 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0002820.npy) |
| 2821 | `model.layers.0.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2822 | `model.layers.0.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2823 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0002823.npy) |
| 2824 | `model.layers.0.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0002824.npy) |
| 2825 | `model.layers.0.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2826 | `model.layers.0.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002826.npy) |
| 2827 | `model.layers.0.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.4375 / 5.40625 / -0.007190447126049548 / 0.8410779943508924 | [NPY](tensors/0002827.npy) |
| 2828 | `model.layers.0.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002828.npy) |
| 2829 | `model.layers.0.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.375 / 29.25 / -0.0019535720348358154 / 3.219451134212101 | [NPY](tensors/0002829.npy) |
| 2830 | `model.layers.0.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -14.75 / 7.1875 / 0.0010128589553965463 / 0.7755971192498221 | [NPY](tensors/0002830.npy) |
| 2831 | `model.layers.0.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.71875 / 3.5625 / -0.03649583458900452 / 1.2017397564519863 | [NPY](tensors/0002831.npy) |
| 2832 | `model.layers.0.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.0625 / 3.859375 / 0.014137519916403107 / 0.5083776331318537 | [NPY](tensors/0002832.npy) |
| 2833 | `model.layers.0.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 47.25 / 0.028633600307835474 / 1.4959199528902605 | [NPY](tensors/0002833.npy) |
| 2834 | `model.layers.0.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 47.25 / 0.028633600307835474 / 1.4959199528902605 | [NPY](tensors/0002834.npy) |
| 2835 | `model.layers.0.self_attn` | 24 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.94921875 / 0.003525637682650612 / 0.0322273082774035 | [NPY](tensors/0002835.npy) |
| 2836 | `model.layers.0.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 49.25 / 0.05204127099778917 / 3.0037118686309032 | [NPY](tensors/0002836.npy) |
| 2837 | `model.layers.0.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 1.6015625 / -0.005612981981701321 / 0.37110079356209524 | [NPY](tensors/0002837.npy) |
| 2838 | `model.layers.0.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.09375 / 1.6015625 / -0.005612981981701321 / 0.37110079356209524 | [NPY](tensors/0002838.npy) |
| 2839 | `model.layers.0.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.09375 / 1.6015625 / -0.005612981981701321 / 0.37110079356209524 | [NPY](tensors/0002839.npy) |
| 2840 | `model.layers.0.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2841 | `model.layers.0.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2842 | `model.layers.0.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2843 | `model.layers.0.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.4375 / 7.28125 / 0.019055221809281243 / 0.46241682159743674 | [NPY](tensors/0002843.npy) |
| 2844 | `model.layers.0.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.4375 / 7.28125 / 0.019055221809281243 / 0.46241682159743674 | [NPY](tensors/0002844.npy) |
| 2845 | `model.layers.0.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.65625 / 1.28125 / -0.18654632568359375 / 0.7028411778756176 | [NPY](tensors/0002845.npy) |
| 2846 | `model.layers.0` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.75 / 54.0 / 0.07124935785929362 / 3.197590515292423 | [NPY](tensors/0002846.npy) |
| 2925 | `model.layers.0` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.25 / 32.0 / 0.061791101429197526 / 2.238756913453412 | [NPY](tensors/0002925.npy) |
| 2926 | `model.layers.0` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002926.npy) |
| 2927 | `model.layers.0` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0002927.npy) |
| 2928 | `model.layers.0` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0002928.npy) |
| 2929 | `model.layers.0` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0002929.npy) |
| 2930 | `model.layers.0` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2931 | `model.layers.0` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2932 | `model.layers.0` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2933 | `model.layers.0.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.25 / 32.0 / 0.061791101429197526 / 2.238756913453412 | [NPY](tensors/0002933.npy) |
| 2934 | `model.layers.0.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002934.npy) |
| 2935 | `model.layers.0.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002935.npy) |
| 2936 | `model.layers.0.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002936.npy) |
| 2937 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0002937.npy) |
| 2938 | `model.layers.0.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2939 | `model.layers.0.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2940 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0002940.npy) |
| 2941 | `model.layers.0.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0002941.npy) |
| 2942 | `model.layers.0.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2943 | `model.layers.0.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002943.npy) |
| 2944 | `model.layers.0.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.375 / 8.125 / 0.007972375839017332 / 1.0483744761991842 | [NPY](tensors/0002944.npy) |
| 2945 | `model.layers.0.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002945.npy) |
| 2946 | `model.layers.0.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.0 / 52.0 / -0.06352853029966354 / 5.834851084637073 | [NPY](tensors/0002946.npy) |
| 2947 | `model.layers.0.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 8.25 / 0.015403711878591114 / 0.8476386218369807 | [NPY](tensors/0002947.npy) |
| 2948 | `model.layers.0.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.75 / 4.5 / 0.031710169510915875 / 1.4942407070139319 | [NPY](tensors/0002948.npy) |
| 2949 | `model.layers.0.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.6875 / 3.546875 / -0.012659257088671438 / 0.698586636105905 | [NPY](tensors/0002949.npy) |
| 2950 | `model.layers.0.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.5 / 40.75 / 0.014021721730629603 / 1.290587963332439 | [NPY](tensors/0002950.npy) |
| 2951 | `model.layers.0.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.5 / 40.75 / 0.014021721730629603 / 1.290587963332439 | [NPY](tensors/0002951.npy) |
| 2952 | `model.layers.0.self_attn` | 25 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.004216129009660849 / 0.04409095206640364 | [NPY](tensors/0002952.npy) |
| 2953 | `model.layers.0.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.5 / 40.5 / 0.07586779329511854 / 2.6216960654925607 | [NPY](tensors/0002953.npy) |
| 2954 | `model.layers.0.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.4375 / 1.859375 / 0.006122559309005737 / 0.45120012255260433 | [NPY](tensors/0002954.npy) |
| 2955 | `model.layers.0.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.4375 / 1.859375 / 0.006122559309005737 / 0.45120012255260433 | [NPY](tensors/0002955.npy) |
| 2956 | `model.layers.0.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.4375 / 1.859375 / 0.006122559309005737 / 0.45120012255260433 | [NPY](tensors/0002956.npy) |
| 2957 | `model.layers.0.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2958 | `model.layers.0.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2959 | `model.layers.0.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2960 | `model.layers.0.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7.75 / 37.75 / 0.020271587702963088 / 1.1829340123989005 | [NPY](tensors/0002960.npy) |
| 2961 | `model.layers.0.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.75 / 37.75 / 0.020271587702963088 / 1.1829340123989005 | [NPY](tensors/0002961.npy) |
| 2962 | `model.layers.0.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.265625 / 1.8125 / -0.1685619354248047 / 0.7955043017559016 | [NPY](tensors/0002962.npy) |
| 2963 | `model.layers.0` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.125 / 78.0 / 0.09621330897013346 / 3.2991049376075146 | [NPY](tensors/0002963.npy) |
| 3042 | `model.layers.0` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0003042.npy) |
| 3043 | `model.layers.0` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003043.npy) |
| 3044 | `model.layers.0` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0003044.npy) |
| 3045 | `model.layers.0` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0003045.npy) |
| 3046 | `model.layers.0` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0003046.npy) |
| 3047 | `model.layers.0` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3048 | `model.layers.0` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3049 | `model.layers.0` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3050 | `model.layers.0.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.375 / 27.625 / -0.06391873326566484 / 2.541301245112155 | [NPY](tensors/0003050.npy) |
| 3051 | `model.layers.0.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0003051.npy) |
| 3052 | `model.layers.0.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0003052.npy) |
| 3053 | `model.layers.0.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003053.npy) |
| 3054 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0003054.npy) |
| 3055 | `model.layers.0.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3056 | `model.layers.0.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3057 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0003057.npy) |
| 3058 | `model.layers.0.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0003058.npy) |
| 3059 | `model.layers.0.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3060 | `model.layers.0.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0003060.npy) |
| 3061 | `model.layers.0.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.34375 / 8.125 / 0.009809806477278471 / 1.0602451281469458 | [NPY](tensors/0003061.npy) |
| 3062 | `model.layers.0.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0003062.npy) |
| 3063 | `model.layers.0.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.5 / 52.75 / 0.05987404379993677 / 5.486411371880323 | [NPY](tensors/0003063.npy) |
| 3064 | `model.layers.0.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 6.71875 / -0.015269790755377875 / 0.7106748405201326 | [NPY](tensors/0003064.npy) |
| 3065 | `model.layers.0.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.125 / 3.75 / 0.02330493927001953 / 1.1486258589347933 | [NPY](tensors/0003065.npy) |
| 3066 | `model.layers.0.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0625 / 3.96875 / 0.004545304022030905 / 0.7208584105669894 | [NPY](tensors/0003066.npy) |
| 3067 | `model.layers.0.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.5 / 43.0 / 0.03397364616394043 / 1.3146543790164011 | [NPY](tensors/0003067.npy) |
| 3068 | `model.layers.0.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.5 / 43.0 / 0.03397364616394043 / 1.3146543790164011 | [NPY](tensors/0003068.npy) |
| 3069 | `model.layers.0.self_attn` | 26 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.004530528412073591 / 0.0449415732198927 | [NPY](tensors/0003069.npy) |
| 3070 | `model.layers.0.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.75 / 47.5 / -0.030169586340586346 / 2.8367821888316107 | [NPY](tensors/0003070.npy) |
| 3071 | `model.layers.0.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0 / 1.6015625 / 0.0008240448104010687 / 0.4012836166031918 | [NPY](tensors/0003071.npy) |
| 3072 | `model.layers.0.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.0 / 1.6015625 / 0.0008240448104010687 / 0.4012836166031918 | [NPY](tensors/0003072.npy) |
| 3073 | `model.layers.0.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.0 / 1.6015625 / 0.0008240448104010687 / 0.4012836166031918 | [NPY](tensors/0003073.npy) |
| 3074 | `model.layers.0.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3075 | `model.layers.0.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3076 | `model.layers.0.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3077 | `model.layers.0.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.84375 / 23.875 / 0.017904450247685114 / 0.7230398542422127 | [NPY](tensors/0003077.npy) |
| 3078 | `model.layers.0.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.84375 / 23.875 / 0.017904450247685114 / 0.7230398542422127 | [NPY](tensors/0003078.npy) |
| 3079 | `model.layers.0.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.875 / 1.8828125 / -0.05365753173828125 / 0.811076209103255 | [NPY](tensors/0003079.npy) |
| 3080 | `model.layers.0` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 71.5 / -0.012251991695827908 / 3.17934876144956 | [NPY](tensors/0003080.npy) |
| 3159 | `model.layers.0` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 34.75 / 0.06460592945416768 / 2.603620301499426 | [NPY](tensors/0003159.npy) |
| 3160 | `model.layers.0` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003160.npy) |
| 3161 | `model.layers.0` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0003161.npy) |
| 3162 | `model.layers.0` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0003162.npy) |
| 3163 | `model.layers.0` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0003163.npy) |
| 3164 | `model.layers.0` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3165 | `model.layers.0` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3166 | `model.layers.0` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3167 | `model.layers.0.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 34.75 / 0.06460592945416768 / 2.603620301499426 | [NPY](tensors/0003167.npy) |
| 3168 | `model.layers.0.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0003168.npy) |
| 3169 | `model.layers.0.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0003169.npy) |
| 3170 | `model.layers.0.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003170.npy) |
| 3171 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0003171.npy) |
| 3172 | `model.layers.0.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3173 | `model.layers.0.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3174 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0003174.npy) |
| 3175 | `model.layers.0.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0003175.npy) |
| 3176 | `model.layers.0.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3177 | `model.layers.0.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0003177.npy) |
| 3178 | `model.layers.0.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.71875 / 8.4375 / 0.008836216118652374 / 1.127863321857116 | [NPY](tensors/0003178.npy) |
| 3179 | `model.layers.0.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0003179.npy) |
| 3180 | `model.layers.0.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -47.25 / 52.5 / -0.01974540948867798 / 5.528074362257702 | [NPY](tensors/0003180.npy) |
| 3181 | `model.layers.0.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.125 / 7.78125 / 0.009009621209568448 / 0.8580928010695072 | [NPY](tensors/0003181.npy) |
| 3182 | `model.layers.0.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.34375 / 5.1875 / 0.04988500475883484 / 1.3788012115777875 | [NPY](tensors/0003182.npy) |
| 3183 | `model.layers.0.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 4.0625 / -0.0016696029633749276 / 0.5972161371802336 | [NPY](tensors/0003183.npy) |
| 3184 | `model.layers.0.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.6875 / 43.5 / 0.030975176393985747 / 1.2793540131412042 | [NPY](tensors/0003184.npy) |
| 3185 | `model.layers.0.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.6875 / 43.5 / 0.030975176393985747 / 1.2793540131412042 | [NPY](tensors/0003185.npy) |
| 3186 | `model.layers.0.self_attn` | 27 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0030981032707457197 / 0.036909143300169055 | [NPY](tensors/0003186.npy) |
| 3187 | `model.layers.0.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 42.5 / 0.09553637504577636 / 2.9044583305275764 | [NPY](tensors/0003187.npy) |
| 3188 | `model.layers.0.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.75 / 1.5546875 / 0.0029973626136779786 / 0.38439181140822015 | [NPY](tensors/0003188.npy) |
| 3189 | `model.layers.0.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.75 / 1.5546875 / 0.0029973626136779786 / 0.38439181140822015 | [NPY](tensors/0003189.npy) |
| 3190 | `model.layers.0.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.75 / 1.5546875 / 0.0029973626136779786 / 0.38439181140822015 | [NPY](tensors/0003190.npy) |
| 3191 | `model.layers.0.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3192 | `model.layers.0.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3193 | `model.layers.0.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3194 | `model.layers.0.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.5625 / 24.375 / 0.02523269671946764 / 0.725258961676999 | [NPY](tensors/0003194.npy) |
| 3195 | `model.layers.0.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.5625 / 24.375 / 0.02523269671946764 / 0.725258961676999 | [NPY](tensors/0003195.npy) |
| 3196 | `model.layers.0.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.390625 / 1.921875 / -0.2139720916748047 / 0.8427856950037548 | [NPY](tensors/0003196.npy) |
| 3197 | `model.layers.0` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 64.0 / 0.12089640299479167 / 3.2161802588045267 | [NPY](tensors/0003197.npy) |
| 3276 | `model.layers.0` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0003276.npy) |
| 3277 | `model.layers.0` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003277.npy) |
| 3278 | `model.layers.0` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0003278.npy) |
| 3279 | `model.layers.0` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0003279.npy) |
| 3280 | `model.layers.0` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0003280.npy) |
| 3281 | `model.layers.0` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3282 | `model.layers.0` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3283 | `model.layers.0` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3284 | `model.layers.0.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 32.25 / 0.04899513756649362 / 2.5441517263773514 | [NPY](tensors/0003284.npy) |
| 3285 | `model.layers.0.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0003285.npy) |
| 3286 | `model.layers.0.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0003286.npy) |
| 3287 | `model.layers.0.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003287.npy) |
| 3288 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0003288.npy) |
| 3289 | `model.layers.0.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3290 | `model.layers.0.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3291 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0003291.npy) |
| 3292 | `model.layers.0.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0003292.npy) |
| 3293 | `model.layers.0.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3294 | `model.layers.0.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0003294.npy) |
| 3295 | `model.layers.0.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 9.25 / 0.06582052947487682 / 1.0317253511582722 | [NPY](tensors/0003295.npy) |
| 3296 | `model.layers.0.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0003296.npy) |
| 3297 | `model.layers.0.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.5 / 59.75 / -0.027341485023498535 / 6.496414800406944 | [NPY](tensors/0003297.npy) |
| 3298 | `model.layers.0.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.875 / 9.4375 / 0.006209394956628481 / 0.7829393322295389 | [NPY](tensors/0003298.npy) |
| 3299 | `model.layers.0.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.453125 / 4.6875 / 0.06333106756210327 / 0.9556167387162166 | [NPY](tensors/0003299.npy) |
| 3300 | `model.layers.0.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.09375 / 4.5625 / 0.008487508619509754 / 0.4773078968914873 | [NPY](tensors/0003300.npy) |
| 3301 | `model.layers.0.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.125 / 38.5 / 0.026908974846204123 / 1.1252762581463918 | [NPY](tensors/0003301.npy) |
| 3302 | `model.layers.0.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.125 / 38.5 / 0.026908974846204123 / 1.1252762581463918 | [NPY](tensors/0003302.npy) |
| 3303 | `model.layers.0.self_attn` | 28 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0029056118749875588 / 0.03073080177297956 | [NPY](tensors/0003303.npy) |
| 3304 | `model.layers.0.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.0 / 39.5 / 0.07609803411695693 / 2.695722778725796 | [NPY](tensors/0003304.npy) |
| 3305 | `model.layers.0.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.4375 / 1.78125 / 0.005193908347023858 / 0.3171232724244797 | [NPY](tensors/0003305.npy) |
| 3306 | `model.layers.0.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.4375 / 1.78125 / 0.005193908347023858 / 0.3171232724244797 | [NPY](tensors/0003306.npy) |
| 3307 | `model.layers.0.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.4375 / 1.78125 / 0.005193908347023858 / 0.3171232724244797 | [NPY](tensors/0003307.npy) |
| 3308 | `model.layers.0.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3309 | `model.layers.0.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3310 | `model.layers.0.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3311 | `model.layers.0.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.53125 / 7.0 / -0.0008253595067395104 / 0.45963683000193284 | [NPY](tensors/0003311.npy) |
| 3312 | `model.layers.0.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.53125 / 7.0 / -0.0008253595067395104 / 0.45963683000193284 | [NPY](tensors/0003312.npy) |
| 3313 | `model.layers.0.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.875 / 2.796875 / -0.13339471817016602 / 1.2202184772076567 | [NPY](tensors/0003313.npy) |
| 3314 | `model.layers.0` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.75 / 44.25 / 0.07539363437228733 / 2.7113610771441574 | [NPY](tensors/0003314.npy) |
| 3393 | `model.layers.0` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.75 / 36.5 / -0.03277786038815975 / 2.7829041357151567 | [NPY](tensors/0003393.npy) |
| 3394 | `model.layers.0` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003394.npy) |
| 3395 | `model.layers.0` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0003395.npy) |
| 3396 | `model.layers.0` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0003396.npy) |
| 3397 | `model.layers.0` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0003397.npy) |
| 3398 | `model.layers.0` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3399 | `model.layers.0` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3400 | `model.layers.0` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3401 | `model.layers.0.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.75 / 36.5 / -0.03277786038815975 / 2.7829041357151567 | [NPY](tensors/0003401.npy) |
| 3402 | `model.layers.0.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0003402.npy) |
| 3403 | `model.layers.0.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0003403.npy) |
| 3404 | `model.layers.0.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003404.npy) |
| 3405 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0003405.npy) |
| 3406 | `model.layers.0.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3407 | `model.layers.0.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3408 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0003408.npy) |
| 3409 | `model.layers.0.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0003409.npy) |
| 3410 | `model.layers.0.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3411 | `model.layers.0.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0003411.npy) |
| 3412 | `model.layers.0.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0625 / 8.75 / 0.007699438836425543 / 0.9554901933770389 | [NPY](tensors/0003412.npy) |
| 3413 | `model.layers.0.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0003413.npy) |
| 3414 | `model.layers.0.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.5 / 55.25 / -0.05697989463806152 / 6.049655579159513 | [NPY](tensors/0003414.npy) |
| 3415 | `model.layers.0.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.3125 / 8.5625 / -0.006851756996992562 / 0.6765854318423068 | [NPY](tensors/0003415.npy) |
| 3416 | `model.layers.0.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -2.703125 / 3.4375 / 0.04050885885953903 / 0.8799544405823716 | [NPY](tensors/0003416.npy) |
| 3417 | `model.layers.0.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -3.78125 / 4.5625 / 0.007780896555232175 / 0.4922269515911046 | [NPY](tensors/0003417.npy) |
| 3418 | `model.layers.0.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.96875 / 29.875 / 0.028395860062705145 / 0.9101142434600208 | [NPY](tensors/0003418.npy) |
| 3419 | `model.layers.0.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.96875 / 29.875 / 0.028395860062705145 / 0.9101142434600208 | [NPY](tensors/0003419.npy) |
| 3420 | `model.layers.0.self_attn` | 29 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.003246843467059655 / 0.032777052614989 | [NPY](tensors/0003420.npy) |
| 3421 | `model.layers.0.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -56.75 / 36.75 / -0.004294382201300727 / 2.8456738544040863 | [NPY](tensors/0003421.npy) |
| 3422 | `model.layers.0.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.125 / 2.78125 / 0.004452264971203274 / 0.28523520054419027 | [NPY](tensors/0003422.npy) |
| 3423 | `model.layers.0.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.125 / 2.78125 / 0.004452264971203274 / 0.28523520054419027 | [NPY](tensors/0003423.npy) |
| 3424 | `model.layers.0.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.125 / 2.78125 / 0.004452264971203274 / 0.28523520054419027 | [NPY](tensors/0003424.npy) |
| 3425 | `model.layers.0.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3426 | `model.layers.0.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3427 | `model.layers.0.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3428 | `model.layers.0.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.40625 / 8.875 / 0.01079204339120123 / 0.5105875004962269 | [NPY](tensors/0003428.npy) |
| 3429 | `model.layers.0.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.40625 / 8.875 / 0.01079204339120123 / 0.5105875004962269 | [NPY](tensors/0003429.npy) |
| 3430 | `model.layers.0.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.265625 / 1.65625 / -0.055370330810546875 / 1.012158947928023 | [NPY](tensors/0003430.npy) |
| 3431 | `model.layers.0` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 36.25 / 0.006468402014838325 / 2.7572471726535377 | [NPY](tensors/0003431.npy) |
| 3510 | `model.layers.0` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 25.375 / 0.03148116301745176 / 2.4913610061559237 | [NPY](tensors/0003510.npy) |
| 3511 | `model.layers.0` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003511.npy) |
| 3512 | `model.layers.0` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0003512.npy) |
| 3513 | `model.layers.0` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0003513.npy) |
| 3514 | `model.layers.0` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0003514.npy) |
| 3515 | `model.layers.0` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3516 | `model.layers.0` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3517 | `model.layers.0` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3518 | `model.layers.0.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 25.375 / 0.03148116301745176 / 2.4913610061559237 | [NPY](tensors/0003518.npy) |
| 3519 | `model.layers.0.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003519.npy) |
| 3520 | `model.layers.0.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003520.npy) |
| 3521 | `model.layers.0.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003521.npy) |
| 3522 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0003522.npy) |
| 3523 | `model.layers.0.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3524 | `model.layers.0.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3525 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0003525.npy) |
| 3526 | `model.layers.0.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0003526.npy) |
| 3527 | `model.layers.0.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3528 | `model.layers.0.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003528.npy) |
| 3529 | `model.layers.0.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.8125 / 9.875 / 0.001175960642285645 / 1.0708778134614567 | [NPY](tensors/0003529.npy) |
| 3530 | `model.layers.0.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003530.npy) |
| 3531 | `model.layers.0.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.0 / 46.0 / -0.07610408216714859 / 5.694328378141193 | [NPY](tensors/0003531.npy) |
| 3532 | `model.layers.0.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 7.96875 / 0.004362174123525619 / 0.8710862357914362 | [NPY](tensors/0003532.npy) |
| 3533 | `model.layers.0.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.46875 / 6.09375 / -0.02648264169692993 / 1.4472391438112524 | [NPY](tensors/0003533.npy) |
| 3534 | `model.layers.0.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.21875 / 3.21875 / 0.006778704399948765 / 0.44610960013598505 | [NPY](tensors/0003534.npy) |
| 3535 | `model.layers.0.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.375 / 43.75 / 0.02341255330377155 / 1.3467578521889032 | [NPY](tensors/0003535.npy) |
| 3536 | `model.layers.0.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.375 / 43.75 / 0.02341255330377155 / 1.3467578521889032 | [NPY](tensors/0003536.npy) |
| 3537 | `model.layers.0.self_attn` | 30 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0029691178976005957 / 0.03427989970612561 | [NPY](tensors/0003537.npy) |
| 3538 | `model.layers.0.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 44.75 / 0.05500134891933865 / 2.941301695162254 | [NPY](tensors/0003538.npy) |
| 3539 | `model.layers.0.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.1875 / 1.453125 / 0.006493790613280402 / 0.3600784123590619 | [NPY](tensors/0003539.npy) |
| 3540 | `model.layers.0.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.1875 / 1.453125 / 0.006493790613280402 / 0.3600784123590619 | [NPY](tensors/0003540.npy) |
| 3541 | `model.layers.0.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -5.1875 / 1.453125 / 0.006493790613280402 / 0.3600784123590619 | [NPY](tensors/0003541.npy) |
| 3542 | `model.layers.0.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3543 | `model.layers.0.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3544 | `model.layers.0.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3545 | `model.layers.0.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.71875 / 14.0625 / 0.019501182871560257 / 0.5063812387933192 | [NPY](tensors/0003545.npy) |
| 3546 | `model.layers.0.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.71875 / 14.0625 / 0.019501182871560257 / 0.5063812387933192 | [NPY](tensors/0003546.npy) |
| 3547 | `model.layers.0.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.203125 / 2.0625 / -0.2020416259765625 / 0.809238489933469 | [NPY](tensors/0003547.npy) |
| 3548 | `model.layers.0` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -55.25 / 58.0 / 0.07437009281582302 / 3.232529520614825 | [NPY](tensors/0003548.npy) |
| 3627 | `model.layers.0` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.25 / 22.875 / 0.02578953950562411 / 2.1256093624936447 | [NPY](tensors/0003627.npy) |
| 3628 | `model.layers.0` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003628.npy) |
| 3629 | `model.layers.0` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0003629.npy) |
| 3630 | `model.layers.0` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0003630.npy) |
| 3631 | `model.layers.0` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0003631.npy) |
| 3632 | `model.layers.0` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3633 | `model.layers.0` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3634 | `model.layers.0` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3635 | `model.layers.0.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.25 / 22.875 / 0.02578953950562411 / 2.1256093624936447 | [NPY](tensors/0003635.npy) |
| 3636 | `model.layers.0.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003636.npy) |
| 3637 | `model.layers.0.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003637.npy) |
| 3638 | `model.layers.0.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003638.npy) |
| 3639 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0003639.npy) |
| 3640 | `model.layers.0.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3641 | `model.layers.0.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3642 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0003642.npy) |
| 3643 | `model.layers.0.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0003643.npy) |
| 3644 | `model.layers.0.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3645 | `model.layers.0.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003645.npy) |
| 3646 | `model.layers.0.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.8125 / 7.9375 / -0.014699231367558241 / 1.1007098219776468 | [NPY](tensors/0003646.npy) |
| 3647 | `model.layers.0.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003647.npy) |
| 3648 | `model.layers.0.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.25 / 55.25 / 0.1305762529373169 / 5.5847358405435745 | [NPY](tensors/0003648.npy) |
| 3649 | `model.layers.0.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 6.6875 / 0.011547544929716323 / 0.7677878619823203 | [NPY](tensors/0003649.npy) |
| 3650 | `model.layers.0.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.21875 / 5.84375 / -0.07473260164260864 / 1.5255124313159032 | [NPY](tensors/0003650.npy) |
| 3651 | `model.layers.0.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.4375 / 6.09375 / -0.0021136613158887485 / 0.8181902253031039 | [NPY](tensors/0003651.npy) |
| 3652 | `model.layers.0.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.5 / 47.25 / 0.04086248183933397 / 1.5242224417821175 | [NPY](tensors/0003652.npy) |
| 3653 | `model.layers.0.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.5 / 47.25 / 0.04086248183933397 / 1.5242224417821175 | [NPY](tensors/0003653.npy) |
| 3654 | `model.layers.0.self_attn` | 31 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003886833246421736 / 0.04613891252838148 | [NPY](tensors/0003654.npy) |
| 3655 | `model.layers.0.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 50.0 / 0.06660965813530816 / 2.7385082687675326 | [NPY](tensors/0003655.npy) |
| 3656 | `model.layers.0.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.609375 / 1.75 / 0.010421439674165514 / 0.45981339158333673 | [NPY](tensors/0003656.npy) |
| 3657 | `model.layers.0.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.609375 / 1.75 / 0.010421439674165514 / 0.45981339158333673 | [NPY](tensors/0003657.npy) |
| 3658 | `model.layers.0.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.609375 / 1.75 / 0.010421439674165514 / 0.45981339158333673 | [NPY](tensors/0003658.npy) |
| 3659 | `model.layers.0.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3660 | `model.layers.0.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3661 | `model.layers.0.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3662 | `model.layers.0.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -19.125 / 39.5 / 0.012318907181421916 / 1.3883504382825846 | [NPY](tensors/0003662.npy) |
| 3663 | `model.layers.0.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.125 / 39.5 / 0.012318907181421916 / 1.3883504382825846 | [NPY](tensors/0003663.npy) |
| 3664 | `model.layers.0.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9609375 / 2.46875 / -0.0523681640625 / 0.8135579447434491 | [NPY](tensors/0003664.npy) |
| 3665 | `model.layers.0` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -59.5 / 89.5 / 0.07885448667738172 / 3.5615718272754187 | [NPY](tensors/0003665.npy) |
| 3744 | `model.layers.0` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 89.0 / 0.026544343266222212 / 4.541275344485995 | [NPY](tensors/0003744.npy) |
| 3745 | `model.layers.0` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003745.npy) |
| 3746 | `model.layers.0` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0003746.npy) |
| 3747 | `model.layers.0` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0003747.npy) |
| 3748 | `model.layers.0` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0003748.npy) |
| 3749 | `model.layers.0` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3750 | `model.layers.0` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3751 | `model.layers.0` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3752 | `model.layers.0.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.5 / 89.0 / 0.026544343266222212 / 4.541275344485995 | [NPY](tensors/0003752.npy) |
| 3753 | `model.layers.0.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003753.npy) |
| 3754 | `model.layers.0.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003754.npy) |
| 3755 | `model.layers.0.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003755.npy) |
| 3756 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0003756.npy) |
| 3757 | `model.layers.0.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3758 | `model.layers.0.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3759 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0003759.npy) |
| 3760 | `model.layers.0.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0003760.npy) |
| 3761 | `model.layers.0.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3762 | `model.layers.0.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003762.npy) |
| 3763 | `model.layers.0.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.875 / 7.84375 / 0.015290047216694802 / 0.914624676971129 | [NPY](tensors/0003763.npy) |
| 3764 | `model.layers.0.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003764.npy) |
| 3765 | `model.layers.0.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.25 / 34.5 / -0.11417865753173828 / 4.434976879466014 | [NPY](tensors/0003765.npy) |
| 3766 | `model.layers.0.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.4375 / 12.125 / 0.002336695873075061 / 0.6770639346011466 | [NPY](tensors/0003766.npy) |
| 3767 | `model.layers.0.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.03125 / 4.8125 / -0.07233588397502899 / 1.0561324517062678 | [NPY](tensors/0003767.npy) |
| 3768 | `model.layers.0.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.09375 / 5.6875 / -0.042490541469305754 / 0.793359060858361 | [NPY](tensors/0003768.npy) |
| 3769 | `model.layers.0.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.375 / 29.125 / 0.030531143811013964 / 1.1843102260847052 | [NPY](tensors/0003769.npy) |
| 3770 | `model.layers.0.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -22.375 / 29.125 / 0.030531143811013964 / 1.1843102260847052 | [NPY](tensors/0003770.npy) |
| 3771 | `model.layers.0.self_attn` | 32 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004084815344491631 / 0.04284967669275136 | [NPY](tensors/0003771.npy) |
| 3772 | `model.layers.0.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -59.25 / 66.5 / 0.05719488461812337 / 4.066998069433461 | [NPY](tensors/0003772.npy) |
| 3773 | `model.layers.0.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.015625 / 2.15625 / 0.009551481074757047 / 0.28309902490455585 | [NPY](tensors/0003773.npy) |
| 3774 | `model.layers.0.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.015625 / 2.15625 / 0.009551481074757047 / 0.28309902490455585 | [NPY](tensors/0003774.npy) |
| 3775 | `model.layers.0.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.015625 / 2.15625 / 0.009551481074757047 / 0.28309902490455585 | [NPY](tensors/0003775.npy) |
| 3776 | `model.layers.0.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3777 | `model.layers.0.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3778 | `model.layers.0.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3779 | `model.layers.0.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -28.75 / 25.625 / 0.022637995580832165 / 1.279646182383944 | [NPY](tensors/0003779.npy) |
| 3780 | `model.layers.0.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.75 / 25.625 / 0.022637995580832165 / 1.279646182383944 | [NPY](tensors/0003780.npy) |
| 3781 | `model.layers.0.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.6875 / 2.890625 / -0.17775726318359375 / 0.8545259269797207 | [NPY](tensors/0003781.npy) |
| 3782 | `model.layers.0` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 59.0 / 0.07978358798556857 / 3.6052095882708106 | [NPY](tensors/0003782.npy) |
| 3861 | `model.layers.0` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0003861.npy) |
| 3862 | `model.layers.0` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003862.npy) |
| 3863 | `model.layers.0` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0003863.npy) |
| 3864 | `model.layers.0` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0003864.npy) |
| 3865 | `model.layers.0` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0003865.npy) |
| 3866 | `model.layers.0` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3867 | `model.layers.0` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3868 | `model.layers.0` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3869 | `model.layers.0.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 36.25 / -0.01066279336810112 / 2.593975032265128 | [NPY](tensors/0003869.npy) |
| 3870 | `model.layers.0.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003870.npy) |
| 3871 | `model.layers.0.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003871.npy) |
| 3872 | `model.layers.0.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003872.npy) |
| 3873 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0003873.npy) |
| 3874 | `model.layers.0.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3875 | `model.layers.0.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3876 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0003876.npy) |
| 3877 | `model.layers.0.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0003877.npy) |
| 3878 | `model.layers.0.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3879 | `model.layers.0.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003879.npy) |
| 3880 | `model.layers.0.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 7.625 / 0.011268170550465584 / 0.9167789321734896 | [NPY](tensors/0003880.npy) |
| 3881 | `model.layers.0.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003881.npy) |
| 3882 | `model.layers.0.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 43.75 / 0.046514674089848995 / 4.791095594233786 | [NPY](tensors/0003882.npy) |
| 3883 | `model.layers.0.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.0 / 9.875 / -0.0037169910139507717 / 0.8322557931125475 | [NPY](tensors/0003883.npy) |
| 3884 | `model.layers.0.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.84375 / 4.125 / -0.01808762550354004 / 1.3178383551916408 | [NPY](tensors/0003884.npy) |
| 3885 | `model.layers.0.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.15625 / 4.28125 / -0.009937559843820054 / 0.4934533589807458 | [NPY](tensors/0003885.npy) |
| 3886 | `model.layers.0.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.6875 / 38.75 / 0.029485286275545756 / 1.1216514150627257 | [NPY](tensors/0003886.npy) |
| 3887 | `model.layers.0.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -15.6875 / 38.75 / 0.029485286275545756 / 1.1216514150627257 | [NPY](tensors/0003887.npy) |
| 3888 | `model.layers.0.self_attn` | 33 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.0031459876067036017 / 0.028322580409475388 | [NPY](tensors/0003888.npy) |
| 3889 | `model.layers.0.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.0 / 39.75 / 0.01875818040635851 / 2.859640971366937 | [NPY](tensors/0003889.npy) |
| 3890 | `model.layers.0.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.15625 / 1.9609375 / 0.00783636834886339 / 0.37551692500224715 | [NPY](tensors/0003890.npy) |
| 3891 | `model.layers.0.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.15625 / 1.9609375 / 0.00783636834886339 / 0.37551692500224715 | [NPY](tensors/0003891.npy) |
| 3892 | `model.layers.0.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.15625 / 1.9609375 / 0.00783636834886339 / 0.37551692500224715 | [NPY](tensors/0003892.npy) |
| 3893 | `model.layers.0.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3894 | `model.layers.0.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3895 | `model.layers.0.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3896 | `model.layers.0.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4.03125 / 16.875 / 0.020520527039964993 / 0.5754398625559397 | [NPY](tensors/0003896.npy) |
| 3897 | `model.layers.0.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.03125 / 16.875 / 0.020520527039964993 / 0.5754398625559397 | [NPY](tensors/0003897.npy) |
| 3898 | `model.layers.0.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.8984375 / -0.07773208618164062 / 0.6393932697954587 | [NPY](tensors/0003898.npy) |
| 3899 | `model.layers.0` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.5 / 56.5 / 0.039052115546332464 / 3.109633423488847 | [NPY](tensors/0003899.npy) |
| 3978 | `model.layers.0` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 30.875 / -0.03053326966861884 / 2.629557572976096 | [NPY](tensors/0003978.npy) |
| 3979 | `model.layers.0` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003979.npy) |
| 3980 | `model.layers.0` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0003980.npy) |
| 3981 | `model.layers.0` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0003981.npy) |
| 3982 | `model.layers.0` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0003982.npy) |
| 3983 | `model.layers.0` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3984 | `model.layers.0` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3985 | `model.layers.0` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3986 | `model.layers.0.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 30.875 / -0.03053326966861884 / 2.629557572976096 | [NPY](tensors/0003986.npy) |
| 3987 | `model.layers.0.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003987.npy) |
| 3988 | `model.layers.0.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003988.npy) |
| 3989 | `model.layers.0.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003989.npy) |
| 3990 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0003990.npy) |
| 3991 | `model.layers.0.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3992 | `model.layers.0.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3993 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0003993.npy) |
| 3994 | `model.layers.0.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0003994.npy) |
| 3995 | `model.layers.0.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3996 | `model.layers.0.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003996.npy) |
| 3997 | `model.layers.0.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 9.375 / -0.0057218477595597506 / 1.0817809599468158 | [NPY](tensors/0003997.npy) |
| 3998 | `model.layers.0.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0003998.npy) |
| 3999 | `model.layers.0.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.75 / 60.25 / 0.21187177300453186 / 5.623456193541793 | [NPY](tensors/0003999.npy) |
| 4000 | `model.layers.0.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 8.9375 / -0.00973054708706008 / 0.7352439266565889 | [NPY](tensors/0004000.npy) |
| 4001 | `model.layers.0.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.15625 / 3.484375 / -0.04266364127397537 / 1.132992277020041 | [NPY](tensors/0004001.npy) |
| 4002 | `model.layers.0.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.78125 / 4.09375 / -0.0014670134405605495 / 0.8143841146258343 | [NPY](tensors/0004002.npy) |
| 4003 | `model.layers.0.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.3125 / 47.5 / 0.03656625466214286 / 1.4224770355608256 | [NPY](tensors/0004003.npy) |
| 4004 | `model.layers.0.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.3125 / 47.5 / 0.03656625466214286 / 1.4224770355608256 | [NPY](tensors/0004004.npy) |
| 4005 | `model.layers.0.self_attn` | 34 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004727192222772011 / 0.05076458369978892 | [NPY](tensors/0004005.npy) |
| 4006 | `model.layers.0.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.25 / 51.5 / 0.0061333550347222225 / 3.039519316650355 | [NPY](tensors/0004006.npy) |
| 4007 | `model.layers.0.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 1.625 / 0.0057234379980299205 / 0.3947134713707105 | [NPY](tensors/0004007.npy) |
| 4008 | `model.layers.0.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.8125 / 1.625 / 0.0057234379980299205 / 0.3947134713707105 | [NPY](tensors/0004008.npy) |
| 4009 | `model.layers.0.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.8125 / 1.625 / 0.0057234379980299205 / 0.3947134713707105 | [NPY](tensors/0004009.npy) |
| 4010 | `model.layers.0.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4011 | `model.layers.0.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4012 | `model.layers.0.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4013 | `model.layers.0.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.3125 / 40.0 / 0.053927974982394114 / 1.2483275809130585 | [NPY](tensors/0004013.npy) |
| 4014 | `model.layers.0.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.3125 / 40.0 / 0.053927974982394114 / 1.2483275809130585 | [NPY](tensors/0004014.npy) |
| 4015 | `model.layers.0.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.640625 / -0.13843536376953125 / 0.6191160019162283 | [NPY](tensors/0004015.npy) |
| 4016 | `model.layers.0` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 91.5 / 0.06008378134833442 / 3.7104880753477225 | [NPY](tensors/0004016.npy) |
| 4095 | `model.layers.0` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 29.875 / -0.024451741410626306 / 2.4041472308375256 | [NPY](tensors/0004095.npy) |
| 4096 | `model.layers.0` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004096.npy) |
| 4097 | `model.layers.0` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0004097.npy) |
| 4098 | `model.layers.0` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0004098.npy) |
| 4099 | `model.layers.0` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0004099.npy) |
| 4100 | `model.layers.0` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4101 | `model.layers.0` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4102 | `model.layers.0` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4103 | `model.layers.0.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 29.875 / -0.024451741410626306 / 2.4041472308375256 | [NPY](tensors/0004103.npy) |
| 4104 | `model.layers.0.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0004104.npy) |
| 4105 | `model.layers.0.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0004105.npy) |
| 4106 | `model.layers.0.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004106.npy) |
| 4107 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0004107.npy) |
| 4108 | `model.layers.0.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4109 | `model.layers.0.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4110 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0004110.npy) |
| 4111 | `model.layers.0.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0004111.npy) |
| 4112 | `model.layers.0.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4113 | `model.layers.0.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0004113.npy) |
| 4114 | `model.layers.0.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.96875 / 9.3125 / 0.013412588275969028 / 1.162217466520388 | [NPY](tensors/0004114.npy) |
| 4115 | `model.layers.0.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0004115.npy) |
| 4116 | `model.layers.0.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.5 / 52.75 / 0.024785220623016357 / 5.9833002218429145 | [NPY](tensors/0004116.npy) |
| 4117 | `model.layers.0.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.0 / 9.0 / -0.005062205758359697 / 0.7617937907293079 | [NPY](tensors/0004117.npy) |
| 4118 | `model.layers.0.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.8125 / 6.03125 / -0.03467495460063219 / 1.460652286605354 | [NPY](tensors/0004118.npy) |
| 4119 | `model.layers.0.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.09375 / 2.796875 / -0.033375994287780486 / 0.5718922220987421 | [NPY](tensors/0004119.npy) |
| 4120 | `model.layers.0.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.625 / 46.25 / 0.022721532426981463 / 1.3703748787250292 | [NPY](tensors/0004120.npy) |
| 4121 | `model.layers.0.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.625 / 46.25 / 0.022721532426981463 / 1.3703748787250292 | [NPY](tensors/0004121.npy) |
| 4122 | `model.layers.0.self_attn` | 35 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0030968445415655308 / 0.03764216359870313 | [NPY](tensors/0004122.npy) |
| 4123 | `model.layers.0.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 45.25 / -0.0016532527075873481 / 2.834255709880888 | [NPY](tensors/0004123.npy) |
| 4124 | `model.layers.0.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9453125 / 1.890625 / 0.0074110613928900825 / 0.373405123761075 | [NPY](tensors/0004124.npy) |
| 4125 | `model.layers.0.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9453125 / 1.890625 / 0.0074110613928900825 / 0.373405123761075 | [NPY](tensors/0004125.npy) |
| 4126 | `model.layers.0.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.9453125 / 1.890625 / 0.0074110613928900825 / 0.373405123761075 | [NPY](tensors/0004126.npy) |
| 4127 | `model.layers.0.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4128 | `model.layers.0.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4129 | `model.layers.0.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4130 | `model.layers.0.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.8125 / 29.75 / 0.030880874395370482 / 0.9607599160036085 | [NPY](tensors/0004130.npy) |
| 4131 | `model.layers.0.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.8125 / 29.75 / 0.030880874395370482 / 0.9607599160036085 | [NPY](tensors/0004131.npy) |
| 4132 | `model.layers.0.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9375 / 1.9140625 / -0.15441465377807617 / 0.7840528582227246 | [NPY](tensors/0004132.npy) |
| 4133 | `model.layers.0` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 74.5 / 0.029284922281901042 / 3.3352489479316674 | [NPY](tensors/0004133.npy) |
| 4212 | `model.layers.0` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 35.0 / -0.0015044911040200128 / 2.4601390841825688 | [NPY](tensors/0004212.npy) |
| 4213 | `model.layers.0` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004213.npy) |
| 4214 | `model.layers.0` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.34375 / 0.7532014846801758 / 0.8246045706539666 | [NPY](tensors/0004214.npy) |
| 4215 | `model.layers.0` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.03213447332382202 / 0.7489573739100013 | [NPY](tensors/0004215.npy) |
| 4216 | `model.layers.0` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 340.0 / 340.0 / 340.0 / 0.0 | [NPY](tensors/0004216.npy) |
| 4217 | `model.layers.0` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4218 | `model.layers.0` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4219 | `model.layers.0` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4220 | `model.layers.0.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 35.0 / -0.0015044911040200128 / 2.4601390841825688 | [NPY](tensors/0004220.npy) |
| 4221 | `model.layers.0.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0004221.npy) |
| 4222 | `model.layers.0.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0004222.npy) |
| 4223 | `model.layers.0.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004223.npy) |
| 4224 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 340.0 / 340.0 / 340.0 / 0.0 | [NPY](tensors/0004224.npy) |
| 4225 | `model.layers.0.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4226 | `model.layers.0.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4227 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.34375 / 0.7532014846801758 / 0.8246045706539666 | [NPY](tensors/0004227.npy) |
| 4228 | `model.layers.0.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.03213447332382202 / 0.7489573739100013 | [NPY](tensors/0004228.npy) |
| 4229 | `model.layers.0.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4230 | `model.layers.0.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0004230.npy) |
| 4231 | `model.layers.0.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 6.875 / 0.0073078901041299105 / 1.018639785574501 | [NPY](tensors/0004231.npy) |
| 4232 | `model.layers.0.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0004232.npy) |
| 4233 | `model.layers.0.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.0 / 49.0 / 0.1723565487191081 / 4.808040616212344 | [NPY](tensors/0004233.npy) |
| 4234 | `model.layers.0.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.0 / 8.8125 / -0.0015076852507061428 / 0.7537271454987554 | [NPY](tensors/0004234.npy) |
| 4235 | `model.layers.0.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.8125 / 3.265625 / 0.014979145489633083 / 1.106498243297265 | [NPY](tensors/0004235.npy) |
| 4236 | `model.layers.0.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.625 / 5.78125 / -0.008955116572906263 / 0.7527461582925071 | [NPY](tensors/0004236.npy) |
| 4237 | `model.layers.0.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.9375 / 44.25 / 0.02840309352096584 / 1.3447210230662663 | [NPY](tensors/0004237.npy) |
| 4238 | `model.layers.0.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.9375 / 44.25 / 0.02840309352096584 / 1.3447210230662663 | [NPY](tensors/0004238.npy) |
| 4239 | `model.layers.0.self_attn` | 36 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.004130738535601054 / 0.04301188028853654 | [NPY](tensors/0004239.npy) |
| 4240 | `model.layers.0.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.25 / 42.5 / 0.026887673801845976 / 2.829092094389079 | [NPY](tensors/0004240.npy) |
| 4241 | `model.layers.0.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.09375 / 2.25 / -0.0007884025573730469 / 0.42676086575901534 | [NPY](tensors/0004241.npy) |
| 4242 | `model.layers.0.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.09375 / 2.25 / -0.0007884025573730469 / 0.42676086575901534 | [NPY](tensors/0004242.npy) |
| 4243 | `model.layers.0.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.09375 / 2.25 / -0.0007884025573730469 / 0.42676086575901534 | [NPY](tensors/0004243.npy) |
| 4244 | `model.layers.0.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4245 | `model.layers.0.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4246 | `model.layers.0.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4247 | `model.layers.0.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.5625 / 24.25 / 0.021492100755373635 / 1.061509576367505 | [NPY](tensors/0004247.npy) |
| 4248 | `model.layers.0.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.5625 / 24.25 / 0.021492100755373635 / 1.061509576367505 | [NPY](tensors/0004248.npy) |
| 4249 | `model.layers.0.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.21875 / 1.96875 / -0.011962890625 / 1.2773813364640942 | [NPY](tensors/0004249.npy) |
| 4250 | `model.layers.0` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 65.0 / 0.04824836519029405 / 3.2382996744544412 | [NPY](tensors/0004250.npy) |
| 4329 | `model.layers.0` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 22.625 / -0.02912892893784576 / 2.1983857303463927 | [NPY](tensors/0004329.npy) |
| 4330 | `model.layers.0` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004330.npy) |
| 4331 | `model.layers.0` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.7198410034179688 / 0.8503804730267482 | [NPY](tensors/0004331.npy) |
| 4332 | `model.layers.0` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.027828902006149292 / 0.7525043584225227 | [NPY](tensors/0004332.npy) |
| 4333 | `model.layers.0` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 341.0 / 341.0 / 341.0 / 0.0 | [NPY](tensors/0004333.npy) |
| 4334 | `model.layers.0` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4335 | `model.layers.0` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4336 | `model.layers.0` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4337 | `model.layers.0.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.625 / 22.625 / -0.02912892893784576 / 2.1983857303463927 | [NPY](tensors/0004337.npy) |
| 4338 | `model.layers.0.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0004338.npy) |
| 4339 | `model.layers.0.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0004339.npy) |
| 4340 | `model.layers.0.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004340.npy) |
| 4341 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 341.0 / 341.0 / 341.0 / 0.0 | [NPY](tensors/0004341.npy) |
| 4342 | `model.layers.0.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4343 | `model.layers.0.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4344 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.7198410034179688 / 0.8503804730267482 | [NPY](tensors/0004344.npy) |
| 4345 | `model.layers.0.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.027828902006149292 / 0.7525043584225227 | [NPY](tensors/0004345.npy) |
| 4346 | `model.layers.0.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4347 | `model.layers.0.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0004347.npy) |
| 4348 | `model.layers.0.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.78125 / 0.008440272184088826 / 1.120452857679885 | [NPY](tensors/0004348.npy) |
| 4349 | `model.layers.0.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0004349.npy) |
| 4350 | `model.layers.0.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.5 / 51.5 / 0.1618337631225586 / 5.774741101565946 | [NPY](tensors/0004350.npy) |
| 4351 | `model.layers.0.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.125 / 7.03125 / -0.008195026136106915 / 0.7386760512843252 | [NPY](tensors/0004351.npy) |
| 4352 | `model.layers.0.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.9375 / 4.875 / -0.08827418088912964 / 1.3724833169271258 | [NPY](tensors/0004352.npy) |
| 4353 | `model.layers.0.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.28125 / 5.21875 / -0.016578779220878914 / 0.6689780374889343 | [NPY](tensors/0004353.npy) |
| 4354 | `model.layers.0.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 50.0 / 0.026897617222534285 / 1.5907075028818911 | [NPY](tensors/0004354.npy) |
| 4355 | `model.layers.0.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 50.0 / 0.026897617222534285 / 1.5907075028818911 | [NPY](tensors/0004355.npy) |
| 4356 | `model.layers.0.self_attn` | 37 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0038113755488727694 / 0.04232780330354161 | [NPY](tensors/0004356.npy) |
| 4357 | `model.layers.0.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.0 / 56.75 / -0.002193646960788303 / 2.9120718422185843 | [NPY](tensors/0004357.npy) |
| 4358 | `model.layers.0.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.671875 / 1.8671875 / 0.0047889305485619435 / 0.35910171307986316 | [NPY](tensors/0004358.npy) |
| 4359 | `model.layers.0.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.671875 / 1.8671875 / 0.0047889305485619435 / 0.35910171307986316 | [NPY](tensors/0004359.npy) |
| 4360 | `model.layers.0.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.671875 / 1.8671875 / 0.0047889305485619435 / 0.35910171307986316 | [NPY](tensors/0004360.npy) |
| 4361 | `model.layers.0.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4362 | `model.layers.0.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4363 | `model.layers.0.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4364 | `model.layers.0.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6.3125 / 24.5 / 0.0277971883614858 / 0.8630078965571383 | [NPY](tensors/0004364.npy) |
| 4365 | `model.layers.0.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6.3125 / 24.5 / 0.0277971883614858 / 0.8630078965571383 | [NPY](tensors/0004365.npy) |
| 4366 | `model.layers.0.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.1875 / 1.6328125 / -0.07491683959960938 / 0.7181430061377094 | [NPY](tensors/0004366.npy) |
| 4367 | `model.layers.0` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 76.5 / 0.02571840551164415 / 3.1608577226170853 | [NPY](tensors/0004367.npy) |
| 4446 | `model.layers.0` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0004446.npy) |
| 4447 | `model.layers.0` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004447.npy) |
| 4448 | `model.layers.0` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.70660400390625 / 0.91681783844784 | [NPY](tensors/0004448.npy) |
| 4449 | `model.layers.0` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / -0.014852643013000488 / 0.6845543139796254 | [NPY](tensors/0004449.npy) |
| 4450 | `model.layers.0` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 342.0 / 342.0 / 342.0 / 0.0 | [NPY](tensors/0004450.npy) |
| 4451 | `model.layers.0` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4452 | `model.layers.0` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4453 | `model.layers.0` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4454 | `model.layers.0.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0004454.npy) |
| 4455 | `model.layers.0.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004455.npy) |
| 4456 | `model.layers.0.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004456.npy) |
| 4457 | `model.layers.0.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004457.npy) |
| 4458 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 342.0 / 342.0 / 342.0 / 0.0 | [NPY](tensors/0004458.npy) |
| 4459 | `model.layers.0.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4460 | `model.layers.0.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4461 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.70660400390625 / 0.91681783844784 | [NPY](tensors/0004461.npy) |
| 4462 | `model.layers.0.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / -0.014852643013000488 / 0.6845543139796254 | [NPY](tensors/0004462.npy) |
| 4463 | `model.layers.0.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4464 | `model.layers.0.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004464.npy) |
| 4465 | `model.layers.0.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 8.0 / 0.0014486645814031363 / 1.027321203413773 | [NPY](tensors/0004465.npy) |
| 4466 | `model.layers.0.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004466.npy) |
| 4467 | `model.layers.0.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.75 / 53.75 / 0.06940409168601036 / 5.734687316339554 | [NPY](tensors/0004467.npy) |
| 4468 | `model.layers.0.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004468.npy) |
| 4469 | `model.layers.0.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.8125 / 3.75 / -0.006423294544219971 / 0.9290448609736645 | [NPY](tensors/0004469.npy) |
| 4470 | `model.layers.0.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.15625 / 4.46875 / -0.0025470784639765043 / 0.6682491293275585 | [NPY](tensors/0004470.npy) |
| 4471 | `model.layers.0.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.125 / 36.75 / 0.02715280999739965 / 1.157362067144178 | [NPY](tensors/0004471.npy) |
| 4472 | `model.layers.0.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.125 / 36.75 / 0.02715280999739965 / 1.157362067144178 | [NPY](tensors/0004472.npy) |
| 4473 | `model.layers.0.self_attn` | 38 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004222176268450473 / 0.044815143674820965 | [NPY](tensors/0004473.npy) |
| 4474 | `model.layers.0.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.5 / 37.25 / -0.06393822564019097 / 2.9693015508314677 | [NPY](tensors/0004474.npy) |
| 4475 | `model.layers.0.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.828125 / 1.5390625 / 0.0014553712473975287 / 0.34307414400139713 | [NPY](tensors/0004475.npy) |
| 4476 | `model.layers.0.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.828125 / 1.5390625 / 0.0014553712473975287 / 0.34307414400139713 | [NPY](tensors/0004476.npy) |
| 4477 | `model.layers.0.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.828125 / 1.5390625 / 0.0014553712473975287 / 0.34307414400139713 | [NPY](tensors/0004477.npy) |
| 4478 | `model.layers.0.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4479 | `model.layers.0.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4480 | `model.layers.0.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4481 | `model.layers.0.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.984375 / 13.6875 / 0.02105182082288795 / 0.5252881494481996 | [NPY](tensors/0004481.npy) |
| 4482 | `model.layers.0.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.984375 / 13.6875 / 0.02105182082288795 / 0.5252881494481996 | [NPY](tensors/0004482.npy) |
| 4483 | `model.layers.0.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.5 / 1.5078125 / 0.021749496459960938 / 1.3790983883628276 | [NPY](tensors/0004483.npy) |
| 4484 | `model.layers.0` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.75 / 39.75 / -0.04282171991136339 / 2.9206880977758534 | [NPY](tensors/0004484.npy) |
| 4563 | `model.layers.0` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 30.0 / -0.032196171374784574 / 2.820171892718441 | [NPY](tensors/0004563.npy) |
| 4564 | `model.layers.0` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004564.npy) |
| 4565 | `model.layers.0` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.740966796875 / 0.9022817549113021 | [NPY](tensors/0004565.npy) |
| 4566 | `model.layers.0` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3046875 / -0.06294980645179749 / 0.6646640154085409 | [NPY](tensors/0004566.npy) |
| 4567 | `model.layers.0` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 343.0 / 343.0 / 343.0 / 0.0 | [NPY](tensors/0004567.npy) |
| 4568 | `model.layers.0` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4569 | `model.layers.0` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4570 | `model.layers.0` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4571 | `model.layers.0.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.75 / 30.0 / -0.032196171374784574 / 2.820171892718441 | [NPY](tensors/0004571.npy) |
| 4572 | `model.layers.0.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004572.npy) |
| 4573 | `model.layers.0.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004573.npy) |
| 4574 | `model.layers.0.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004574.npy) |
| 4575 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 343.0 / 343.0 / 343.0 / 0.0 | [NPY](tensors/0004575.npy) |
| 4576 | `model.layers.0.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4577 | `model.layers.0.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4578 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.740966796875 / 0.9022817549113021 | [NPY](tensors/0004578.npy) |
| 4579 | `model.layers.0.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3046875 / -0.06294980645179749 / 0.6646640154085409 | [NPY](tensors/0004579.npy) |
| 4580 | `model.layers.0.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4581 | `model.layers.0.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004581.npy) |
| 4582 | `model.layers.0.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.6875 / 10.0625 / 0.016296769957989454 / 1.0275877120532655 | [NPY](tensors/0004582.npy) |
| 4583 | `model.layers.0.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004583.npy) |
| 4584 | `model.layers.0.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -57.0 / 59.0 / -0.06925755739212036 / 5.9291873125568 | [NPY](tensors/0004584.npy) |
| 4585 | `model.layers.0.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.75 / 6.65625 / -0.013581904106669956 / 0.7022594084362029 | [NPY](tensors/0004585.npy) |
| 4586 | `model.layers.0.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.0625 / 3.890625 / -0.020120687782764435 / 1.0179532107822138 | [NPY](tensors/0004586.npy) |
| 4587 | `model.layers.0.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.8125 / 3.453125 / -0.023405524501868058 / 0.5810861051220846 | [NPY](tensors/0004587.npy) |
| 4588 | `model.layers.0.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.75 / 36.25 / 0.020187566181023915 / 1.1322145587963854 | [NPY](tensors/0004588.npy) |
| 4589 | `model.layers.0.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.75 / 36.25 / 0.020187566181023915 / 1.1322145587963854 | [NPY](tensors/0004589.npy) |
| 4590 | `model.layers.0.self_attn` | 39 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.003785030521222544 / 0.04253385106242022 | [NPY](tensors/0004590.npy) |
| 4591 | `model.layers.0.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 37.5 / -0.011864720450507269 / 2.888494231977817 | [NPY](tensors/0004591.npy) |
| 4592 | `model.layers.0.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9609375 / 1.6484375 / 0.0025280204084184433 / 0.2755135147235741 | [NPY](tensors/0004592.npy) |
| 4593 | `model.layers.0.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.9609375 / 1.6484375 / 0.0025280204084184433 / 0.2755135147235741 | [NPY](tensors/0004593.npy) |
| 4594 | `model.layers.0.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.9609375 / 1.6484375 / 0.0025280204084184433 / 0.2755135147235741 | [NPY](tensors/0004594.npy) |
| 4595 | `model.layers.0.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4596 | `model.layers.0.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4597 | `model.layers.0.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4598 | `model.layers.0.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.75 / 11.125 / 0.011076855411132177 / 0.5862117180976141 | [NPY](tensors/0004598.npy) |
| 4599 | `model.layers.0.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.75 / 11.125 / 0.011076855411132177 / 0.5862117180976141 | [NPY](tensors/0004599.npy) |
| 4600 | `model.layers.0.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.59375 / 1.765625 / -0.0222625732421875 / 1.0340851738538226 | [NPY](tensors/0004600.npy) |
| 4601 | `model.layers.0` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 48.5 / -0.0009659290313720703 / 2.8804744807650082 | [NPY](tensors/0004601.npy) |
| 4680 | `model.layers.0` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.5 / 30.625 / 0.03435131601161427 / 2.148670063069294 | [NPY](tensors/0004680.npy) |
| 4681 | `model.layers.0` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004681.npy) |
| 4682 | `model.layers.0` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8131542205810547 / 0.8233916239555151 | [NPY](tensors/0004682.npy) |
| 4683 | `model.layers.0` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.07140964269638062 / 0.6820182328303498 | [NPY](tensors/0004683.npy) |
| 4684 | `model.layers.0` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 344.0 / 344.0 / 344.0 / 0.0 | [NPY](tensors/0004684.npy) |
| 4685 | `model.layers.0` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4686 | `model.layers.0` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4687 | `model.layers.0` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4688 | `model.layers.0.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.5 / 30.625 / 0.03435131601161427 / 2.148670063069294 | [NPY](tensors/0004688.npy) |
| 4689 | `model.layers.0.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004689.npy) |
| 4690 | `model.layers.0.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004690.npy) |
| 4691 | `model.layers.0.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004691.npy) |
| 4692 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 344.0 / 344.0 / 344.0 / 0.0 | [NPY](tensors/0004692.npy) |
| 4693 | `model.layers.0.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4694 | `model.layers.0.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4695 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8131542205810547 / 0.8233916239555151 | [NPY](tensors/0004695.npy) |
| 4696 | `model.layers.0.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.07140964269638062 / 0.6820182328303498 | [NPY](tensors/0004696.npy) |
| 4697 | `model.layers.0.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4698 | `model.layers.0.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004698.npy) |
| 4699 | `model.layers.0.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.59375 / 8.875 / -0.01820482179755345 / 1.2112680722654519 | [NPY](tensors/0004699.npy) |
| 4700 | `model.layers.0.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004700.npy) |
| 4701 | `model.layers.0.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -47.25 / 51.0 / 0.04916292428970337 / 5.661126585935481 | [NPY](tensors/0004701.npy) |
| 4702 | `model.layers.0.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7.84375 / 9.3125 / 0.010035791165298886 / 0.7617563854706693 | [NPY](tensors/0004702.npy) |
| 4703 | `model.layers.0.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.59375 / 4.9375 / -0.02149730920791626 / 1.5738961772339104 | [NPY](tensors/0004703.npy) |
| 4704 | `model.layers.0.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.03125 / 3.015625 / -0.017591250526947988 / 0.45642561558791706 | [NPY](tensors/0004704.npy) |
| 4705 | `model.layers.0.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.875 / 31.5 / 0.0104297763771481 / 1.0197891094525726 | [NPY](tensors/0004705.npy) |
| 4706 | `model.layers.0.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.875 / 31.5 / 0.0104297763771481 / 1.0197891094525726 | [NPY](tensors/0004706.npy) |
| 4707 | `model.layers.0.self_attn` | 40 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0021620716028708463 / 0.034145427377324906 | [NPY](tensors/0004707.npy) |
| 4708 | `model.layers.0.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 32.25 / 0.0448478725221422 / 2.4640775763391045 | [NPY](tensors/0004708.npy) |
| 4709 | `model.layers.0.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 2.4375 / 0.005500896771748861 / 0.41969444801532835 | [NPY](tensors/0004709.npy) |
| 4710 | `model.layers.0.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 2.4375 / 0.005500896771748861 / 0.41969444801532835 | [NPY](tensors/0004710.npy) |
| 4711 | `model.layers.0.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.7734375 / 2.4375 / 0.005500896771748861 / 0.41969444801532835 | [NPY](tensors/0004711.npy) |
| 4712 | `model.layers.0.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4713 | `model.layers.0.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4714 | `model.layers.0.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4715 | `model.layers.0.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.0 / 46.25 / 0.03134716318713294 / 1.4360386214657397 | [NPY](tensors/0004715.npy) |
| 4716 | `model.layers.0.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0 / 46.25 / 0.03134716318713294 / 1.4360386214657397 | [NPY](tensors/0004716.npy) |
| 4717 | `model.layers.0.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.9765625 / -0.13604736328125 / 0.8464991279094528 | [NPY](tensors/0004717.npy) |
| 4718 | `model.layers.0` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 75.0 / 0.07634320788913303 / 3.2764269072015293 | [NPY](tensors/0004718.npy) |
| 4797 | `model.layers.0` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0004797.npy) |
| 4798 | `model.layers.0` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004798.npy) |
| 4799 | `model.layers.0` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.8764495849609375 / 0.8009113437243138 | [NPY](tensors/0004799.npy) |
| 4800 | `model.layers.0` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.020697563886642456 / 0.632324519915983 | [NPY](tensors/0004800.npy) |
| 4801 | `model.layers.0` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 345.0 / 345.0 / 345.0 / 0.0 | [NPY](tensors/0004801.npy) |
| 4802 | `model.layers.0` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4803 | `model.layers.0` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4804 | `model.layers.0` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4805 | `model.layers.0.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 23.375 / -0.09108336199488905 / 2.701134768574775 | [NPY](tensors/0004805.npy) |
| 4806 | `model.layers.0.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004806.npy) |
| 4807 | `model.layers.0.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004807.npy) |
| 4808 | `model.layers.0.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004808.npy) |
| 4809 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 345.0 / 345.0 / 345.0 / 0.0 | [NPY](tensors/0004809.npy) |
| 4810 | `model.layers.0.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4811 | `model.layers.0.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4812 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.8764495849609375 / 0.8009113437243138 | [NPY](tensors/0004812.npy) |
| 4813 | `model.layers.0.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.020697563886642456 / 0.632324519915983 | [NPY](tensors/0004813.npy) |
| 4814 | `model.layers.0.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4815 | `model.layers.0.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004815.npy) |
| 4816 | `model.layers.0.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 8.0 / 0.0014486645814031363 / 1.027321203413773 | [NPY](tensors/0004816.npy) |
| 4817 | `model.layers.0.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004817.npy) |
| 4818 | `model.layers.0.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.75 / 53.75 / 0.06940409168601036 / 5.734687316339554 | [NPY](tensors/0004818.npy) |
| 4819 | `model.layers.0.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.75 / 5.0625 / -0.02284202788852983 / 0.7234370963774958 | [NPY](tensors/0004819.npy) |
| 4820 | `model.layers.0.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.8125 / 3.75 / -0.006423294544219971 / 0.9290448609736645 | [NPY](tensors/0004820.npy) |
| 4821 | `model.layers.0.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.28125 / 3.734375 / -0.0038824975717943744 / 0.6331420761873983 | [NPY](tensors/0004821.npy) |
| 4822 | `model.layers.0.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0625 / 33.5 / 0.02855037757092052 / 1.061713733779361 | [NPY](tensors/0004822.npy) |
| 4823 | `model.layers.0.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11.0625 / 33.5 / 0.02855037757092052 / 1.061713733779361 | [NPY](tensors/0004823.npy) |
| 4824 | `model.layers.0.self_attn` | 41 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003758483205422312 / 0.040953433505635094 | [NPY](tensors/0004824.npy) |
| 4825 | `model.layers.0.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 34.0 / -0.06258060932159423 / 2.9677332522152855 | [NPY](tensors/0004825.npy) |
| 4826 | `model.layers.0.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8828125 / 1.5703125 / 0.003181644280751546 / 0.3327213418736389 | [NPY](tensors/0004826.npy) |
| 4827 | `model.layers.0.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.8828125 / 1.5703125 / 0.003181644280751546 / 0.3327213418736389 | [NPY](tensors/0004827.npy) |
| 4828 | `model.layers.0.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.8828125 / 1.5703125 / 0.003181644280751546 / 0.3327213418736389 | [NPY](tensors/0004828.npy) |
| 4829 | `model.layers.0.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4830 | `model.layers.0.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4831 | `model.layers.0.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4832 | `model.layers.0.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3.21875 / 11.3125 / 0.014593226835131645 / 0.5139209966853948 | [NPY](tensors/0004832.npy) |
| 4833 | `model.layers.0.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.21875 / 11.3125 / 0.014593226835131645 / 0.5139209966853948 | [NPY](tensors/0004833.npy) |
| 4834 | `model.layers.0.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.5625 / 1.4296875 / -0.015621185302734375 / 1.3207948795561788 | [NPY](tensors/0004834.npy) |
| 4835 | `model.layers.0` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 43.5 / -0.0480810801188151 / 2.9892122016908598 | [NPY](tensors/0004835.npy) |
| 4914 | `model.layers.0` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.75 / 32.0 / 0.02612974349823263 / 2.3052590463349314 | [NPY](tensors/0004914.npy) |
| 4915 | `model.layers.0` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004915.npy) |
| 4916 | `model.layers.0` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.887237548828125 / 0.808167570442007 | [NPY](tensors/0004916.npy) |
| 4917 | `model.layers.0` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.06384772062301636 / 0.6046658936992718 | [NPY](tensors/0004917.npy) |
| 4918 | `model.layers.0` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 346.0 / 346.0 / 346.0 / 0.0 | [NPY](tensors/0004918.npy) |
| 4919 | `model.layers.0` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4920 | `model.layers.0` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4921 | `model.layers.0` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4922 | `model.layers.0.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.75 / 32.0 / 0.02612974349823263 / 2.3052590463349314 | [NPY](tensors/0004922.npy) |
| 4923 | `model.layers.0.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004923.npy) |
| 4924 | `model.layers.0.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004924.npy) |
| 4925 | `model.layers.0.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004925.npy) |
| 4926 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 346.0 / 346.0 / 346.0 / 0.0 | [NPY](tensors/0004926.npy) |
| 4927 | `model.layers.0.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4928 | `model.layers.0.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4929 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.887237548828125 / 0.808167570442007 | [NPY](tensors/0004929.npy) |
| 4930 | `model.layers.0.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.06384772062301636 / 0.6046658936992718 | [NPY](tensors/0004930.npy) |
| 4931 | `model.layers.0.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4932 | `model.layers.0.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004932.npy) |
| 4933 | `model.layers.0.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.375 / 10.0625 / -0.0011312136193737388 / 1.2762524673806912 | [NPY](tensors/0004933.npy) |
| 4934 | `model.layers.0.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004934.npy) |
| 4935 | `model.layers.0.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.5 / 51.25 / 0.02611599490046501 / 5.9708322691785325 | [NPY](tensors/0004935.npy) |
| 4936 | `model.layers.0.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -12.375 / 8.5625 / 0.009641877685983976 / 0.733799081899011 | [NPY](tensors/0004936.npy) |
| 4937 | `model.layers.0.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / 0.016116023063659668 / 1.5717161949904705 | [NPY](tensors/0004937.npy) |
| 4938 | `model.layers.0.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.875 / 3.734375 / -0.016199328315451567 / 0.6137620946020743 | [NPY](tensors/0004938.npy) |
| 4939 | `model.layers.0.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 35.0 / 0.021492521299256218 / 1.0998753581366 | [NPY](tensors/0004939.npy) |
| 4940 | `model.layers.0.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 35.0 / 0.021492521299256218 / 1.0998753581366 | [NPY](tensors/0004940.npy) |
| 4941 | `model.layers.0.self_attn` | 42 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0037083790992370274 / 0.04746295092010576 | [NPY](tensors/0004941.npy) |
| 4942 | `model.layers.0.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 37.75 / 0.04749086168077257 / 2.635136297593191 | [NPY](tensors/0004942.npy) |
| 4943 | `model.layers.0.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.6796875 / 0.014766797092225817 / 0.4040087821051304 | [NPY](tensors/0004943.npy) |
| 4944 | `model.layers.0.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.6796875 / 0.014766797092225817 / 0.4040087821051304 | [NPY](tensors/0004944.npy) |
| 4945 | `model.layers.0.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.5703125 / 1.6796875 / 0.014766797092225817 / 0.4040087821051304 | [NPY](tensors/0004945.npy) |
| 4946 | `model.layers.0.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4947 | `model.layers.0.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4948 | `model.layers.0.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4949 | `model.layers.0.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -10.9375 / 24.625 / 0.02113725675476922 / 1.0727099362868557 | [NPY](tensors/0004949.npy) |
| 4950 | `model.layers.0.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.9375 / 24.625 / 0.02113725675476922 / 1.0727099362868557 | [NPY](tensors/0004950.npy) |
| 4951 | `model.layers.0.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6796875 / 3.34375 / -0.277923583984375 / 1.1837981109795712 | [NPY](tensors/0004951.npy) |
| 4952 | `model.layers.0` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 62.5 / 0.06890830198923746 / 3.1137127609817408 | [NPY](tensors/0004952.npy) |
| 5031 | `model.layers.0` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 38.75 / -0.019637677404615615 / 2.869533421530457 | [NPY](tensors/0005031.npy) |
| 5032 | `model.layers.0` | 43 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005032.npy) |
| 5033 | `model.layers.0` | 43 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.8368129730224609 / 0.8204651963806046 | [NPY](tensors/0005033.npy) |
| 5034 | `model.layers.0` | 43 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.1309933364391327 / 0.6478045244450656 | [NPY](tensors/0005034.npy) |
| 5035 | `model.layers.0` | 43 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 347.0 / 347.0 / 347.0 / 0.0 | [NPY](tensors/0005035.npy) |
| 5036 | `model.layers.0` | 43 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5037 | `model.layers.0` | 43 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5038 | `model.layers.0` | 43 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5039 | `model.layers.0.input_layernorm` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 38.75 / -0.019637677404615615 / 2.869533421530457 | [NPY](tensors/0005039.npy) |
| 5040 | `model.layers.0.input_layernorm` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0005040.npy) |
| 5041 | `model.layers.0.self_attn` | 43 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0005041.npy) |
| 5042 | `model.layers.0.self_attn` | 43 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005042.npy) |
| 5043 | `model.layers.0.self_attn` | 43 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 347.0 / 347.0 / 347.0 / 0.0 | [NPY](tensors/0005043.npy) |
| 5044 | `model.layers.0.self_attn` | 43 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5045 | `model.layers.0.self_attn` | 43 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5046 | `model.layers.0.self_attn` | 43 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.8368129730224609 / 0.8204651963806046 | [NPY](tensors/0005046.npy) |
| 5047 | `model.layers.0.self_attn` | 43 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.1309933364391327 / 0.6478045244450656 | [NPY](tensors/0005047.npy) |
| 5048 | `model.layers.0.self_attn` | 43 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5049 | `model.layers.0.self_attn.q_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0005049.npy) |
| 5050 | `model.layers.0.self_attn.q_proj` | 43 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0 / 9.4375 / 0.009774616220965981 / 1.008080585961609 | [NPY](tensors/0005050.npy) |
| 5051 | `model.layers.0.self_attn.k_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0005051.npy) |
| 5052 | `model.layers.0.self_attn.k_proj` | 43 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -61.5 / 52.0 / -0.04840673506259918 / 6.119228313490181 | [NPY](tensors/0005052.npy) |
| 5053 | `model.layers.0.self_attn.v_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.9375 / 10.0625 / -0.00924550924036238 / 0.7240862587758806 | [NPY](tensors/0005053.npy) |
| 5054 | `model.layers.0.self_attn.v_proj` | 43 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.34375 / 3.625 / -0.03821904957294464 / 0.9543836895451787 | [NPY](tensors/0005054.npy) |
| 5055 | `model.layers.0.self_attn.o_proj` | 43 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.1875 / 4.65625 / -0.00684710304994951 / 0.5509643783007258 | [NPY](tensors/0005055.npy) |
| 5056 | `model.layers.0.self_attn.o_proj` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.0 / 33.0 / 0.03213132342530622 / 1.0463234268780046 | [NPY](tensors/0005056.npy) |
| 5057 | `model.layers.0.self_attn` | 43 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.0 / 33.0 / 0.03213132342530622 / 1.0463234268780046 | [NPY](tensors/0005057.npy) |
| 5058 | `model.layers.0.self_attn` | 43 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0033205031487517937 / 0.035366953244580585 | [NPY](tensors/0005058.npy) |
| 5059 | `model.layers.0.post_attention_layernorm` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.0 / 38.5 / 0.012546104855007595 / 2.84469365129548 | [NPY](tensors/0005059.npy) |
| 5060 | `model.layers.0.post_attention_layernorm` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.4453125 / 2.109375 / 0.002359534634484185 / 0.28740217918203914 | [NPY](tensors/0005060.npy) |
| 5061 | `model.layers.0.mlp` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.4453125 / 2.109375 / 0.002359534634484185 / 0.28740217918203914 | [NPY](tensors/0005061.npy) |
| 5062 | `model.layers.0.mlp.experts` | 43 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.4453125 / 2.109375 / 0.002359534634484185 / 0.28740217918203914 | [NPY](tensors/0005062.npy) |
| 5063 | `model.layers.0.mlp.experts` | 43 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5064 | `model.layers.0.mlp.experts` | 43 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5065 | `model.layers.0.mlp.experts` | 43 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5066 | `model.layers.0.mlp.experts` | 43 | `output` | [1, 2880] | torch.bfloat16 → float32 | -13.1875 / 20.875 / 0.020382344557179344 / 0.9039035700957314 | [NPY](tensors/0005066.npy) |
| 5067 | `model.layers.0.mlp` | 43 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -13.1875 / 20.875 / 0.020382344557179344 / 0.9039035700957314 | [NPY](tensors/0005067.npy) |
| 5068 | `model.layers.0.mlp` | 43 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.125 / 1.8203125 / -0.013019561767578125 / 1.222278105211446 | [NPY](tensors/0005068.npy) |
| 5069 | `model.layers.0` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 51.0 / 0.03296167585584853 / 3.045987235712438 | [NPY](tensors/0005069.npy) |
| 5148 | `model.layers.0` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 25.0 / 0.01804563016113308 / 2.3323165527333782 | [NPY](tensors/0005148.npy) |
| 5149 | `model.layers.0` | 44 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005149.npy) |
| 5150 | `model.layers.0` | 44 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7588653564453125 / 0.8828955932720353 | [NPY](tensors/0005150.npy) |
| 5151 | `model.layers.0` | 44 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14290890097618103 / 0.6590419455082627 | [NPY](tensors/0005151.npy) |
| 5152 | `model.layers.0` | 44 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 348.0 / 348.0 / 348.0 / 0.0 | [NPY](tensors/0005152.npy) |
| 5153 | `model.layers.0` | 44 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5154 | `model.layers.0` | 44 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5155 | `model.layers.0` | 44 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5156 | `model.layers.0.input_layernorm` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.5 / 25.0 / 0.01804563016113308 / 2.3323165527333782 | [NPY](tensors/0005156.npy) |
| 5157 | `model.layers.0.input_layernorm` | 44 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0005157.npy) |
| 5158 | `model.layers.0.self_attn` | 44 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0005158.npy) |
| 5159 | `model.layers.0.self_attn` | 44 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005159.npy) |
| 5160 | `model.layers.0.self_attn` | 44 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 348.0 / 348.0 / 348.0 / 0.0 | [NPY](tensors/0005160.npy) |
| 5161 | `model.layers.0.self_attn` | 44 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5162 | `model.layers.0.self_attn` | 44 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5163 | `model.layers.0.self_attn` | 44 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7588653564453125 / 0.8828955932720353 | [NPY](tensors/0005163.npy) |
| 5164 | `model.layers.0.self_attn` | 44 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14290890097618103 / 0.6590419455082627 | [NPY](tensors/0005164.npy) |
| 5165 | `model.layers.0.self_attn` | 44 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5166 | `model.layers.0.self_attn.q_proj` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0005166.npy) |
| 5167 | `model.layers.0.self_attn.q_proj` | 44 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.875 / 8.75 / 0.005578655982390046 / 1.1564340991725837 | [NPY](tensors/0005167.npy) |
| 5168 | `model.layers.0.self_attn.k_proj` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0005168.npy) |
| 5169 | `model.layers.0.self_attn.k_proj` | 44 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -56.25 / 41.75 / -0.16974663734436035 / 5.496621344446725 | [NPY](tensors/0005169.npy) |
| 5170 | `model.layers.0.self_attn.v_proj` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -17.0 / 7.1875 / 0.005011025609241592 / 0.7429613513531744 | [NPY](tensors/0005170.npy) |
| 5171 | `model.layers.0.self_attn.v_proj` | 44 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.6875 / 4.5 / 0.06943026185035706 / 1.339855997999367 | [NPY](tensors/0005171.npy) |
| 5172 | `model.layers.0.self_attn.o_proj` | 44 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.34375 / 4.3125 / -0.005727620460675098 / 0.5104028908476557 | [NPY](tensors/0005172.npy) |
| 5173 | `model.layers.0.self_attn.o_proj` | 44 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.5 / 38.25 / 0.01789053347375658 / 1.2013926478787431 | [NPY](tensors/0005173.npy) |
| 5174 | `model.layers.0.self_attn` | 44 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -23.5 / 38.25 / 0.01789053347375658 / 1.2013926478787431 | [NPY](tensors/0005174.npy) |
| 5175 | `model.layers.0.self_attn` | 44 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002929031396784562 / 0.036713068297741715 | [NPY](tensors/0005175.npy) |
| 5176 | `model.layers.0.post_attention_layernorm` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -54.25 / 43.5 / 0.0358121739493476 / 2.778150797052786 | [NPY](tensors/0005176.npy) |
| 5177 | `model.layers.0.post_attention_layernorm` | 44 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.09375 / 1.4765625 / 0.006227383017539978 / 0.29646706809087015 | [NPY](tensors/0005177.npy) |
| 5178 | `model.layers.0.mlp` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.09375 / 1.4765625 / 0.006227383017539978 / 0.29646706809087015 | [NPY](tensors/0005178.npy) |
| 5179 | `model.layers.0.mlp.experts` | 44 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.09375 / 1.4765625 / 0.006227383017539978 / 0.29646706809087015 | [NPY](tensors/0005179.npy) |
| 5180 | `model.layers.0.mlp.experts` | 44 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5181 | `model.layers.0.mlp.experts` | 44 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5182 | `model.layers.0.mlp.experts` | 44 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5183 | `model.layers.0.mlp.experts` | 44 | `output` | [1, 2880] | torch.bfloat16 → float32 | -9.0625 / 29.125 / 0.02009754478931427 / 1.0221981389932357 | [NPY](tensors/0005183.npy) |
| 5184 | `model.layers.0.mlp` | 44 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9.0625 / 29.125 / 0.02009754478931427 / 1.0221981389932357 | [NPY](tensors/0005184.npy) |
| 5185 | `model.layers.0.mlp` | 44 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.390625 / 2.015625 / -0.1522989273071289 / 0.72949946984203 | [NPY](tensors/0005185.npy) |
| 5186 | `model.layers.0` | 44 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.0 / 70.5 / 0.055859041213989255 / 3.3458290338333923 | [NPY](tensors/0005186.npy) |
| 5265 | `model.layers.0` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 40.25 / -0.06394515766037835 / 2.6467228965831135 | [NPY](tensors/0005265.npy) |
| 5266 | `model.layers.0` | 45 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005266.npy) |
| 5267 | `model.layers.0` | 45 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.701873779296875 / 0.9298159802037973 | [NPY](tensors/0005267.npy) |
| 5268 | `model.layers.0` | 45 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.10132250189781189 / 0.6650396518932735 | [NPY](tensors/0005268.npy) |
| 5269 | `model.layers.0` | 45 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 349.0 / 349.0 / 349.0 / 0.0 | [NPY](tensors/0005269.npy) |
| 5270 | `model.layers.0` | 45 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5271 | `model.layers.0` | 45 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5272 | `model.layers.0` | 45 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5273 | `model.layers.0.input_layernorm` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 40.25 / -0.06394515766037835 / 2.6467228965831135 | [NPY](tensors/0005273.npy) |
| 5274 | `model.layers.0.input_layernorm` | 45 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0005274.npy) |
| 5275 | `model.layers.0.self_attn` | 45 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0005275.npy) |
| 5276 | `model.layers.0.self_attn` | 45 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005276.npy) |
| 5277 | `model.layers.0.self_attn` | 45 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 349.0 / 349.0 / 349.0 / 0.0 | [NPY](tensors/0005277.npy) |
| 5278 | `model.layers.0.self_attn` | 45 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5279 | `model.layers.0.self_attn` | 45 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5280 | `model.layers.0.self_attn` | 45 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.701873779296875 / 0.9298159802037973 | [NPY](tensors/0005280.npy) |
| 5281 | `model.layers.0.self_attn` | 45 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.10132250189781189 / 0.6650396518932735 | [NPY](tensors/0005281.npy) |
| 5282 | `model.layers.0.self_attn` | 45 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5283 | `model.layers.0.self_attn.q_proj` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0005283.npy) |
| 5284 | `model.layers.0.self_attn.q_proj` | 45 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.6875 / 7.625 / -0.005639673676341772 / 1.046891081389267 | [NPY](tensors/0005284.npy) |
| 5285 | `model.layers.0.self_attn.k_proj` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0005285.npy) |
| 5286 | `model.layers.0.self_attn.k_proj` | 45 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.75 / 51.5 / 0.029395833611488342 / 5.690317737756353 | [NPY](tensors/0005286.npy) |
| 5287 | `model.layers.0.self_attn.v_proj` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 9.9375 / -0.014668897125456068 / 0.721906723387859 | [NPY](tensors/0005287.npy) |
| 5288 | `model.layers.0.self_attn.v_proj` | 45 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.5625 / 4.03125 / 0.016885966062545776 / 1.1800325387513315 | [NPY](tensors/0005288.npy) |
| 5289 | `model.layers.0.self_attn.o_proj` | 45 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.4375 / 3.65625 / 0.006977523677051067 / 0.5404168829091903 | [NPY](tensors/0005289.npy) |
| 5290 | `model.layers.0.self_attn.o_proj` | 45 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.5 / 40.25 / 0.030569617905550534 / 1.1815139165230168 | [NPY](tensors/0005290.npy) |
| 5291 | `model.layers.0.self_attn` | 45 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -16.5 / 40.25 / 0.030569617905550534 / 1.1815139165230168 | [NPY](tensors/0005291.npy) |
| 5292 | `model.layers.0.self_attn` | 45 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0032796165389670793 / 0.03391422380116854 | [NPY](tensors/0005292.npy) |
| 5293 | `model.layers.0.post_attention_layernorm` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.5 / 41.75 / -0.03345110416412354 / 2.9825498878540744 | [NPY](tensors/0005293.npy) |
| 5294 | `model.layers.0.post_attention_layernorm` | 45 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.875 / 2.96875 / 0.00446298254860772 / 0.31387322681695606 | [NPY](tensors/0005294.npy) |
| 5295 | `model.layers.0.mlp` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.875 / 2.96875 / 0.00446298254860772 / 0.31387322681695606 | [NPY](tensors/0005295.npy) |
| 5296 | `model.layers.0.mlp.experts` | 45 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.875 / 2.96875 / 0.00446298254860772 / 0.31387322681695606 | [NPY](tensors/0005296.npy) |
| 5297 | `model.layers.0.mlp.experts` | 45 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5298 | `model.layers.0.mlp.experts` | 45 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5299 | `model.layers.0.mlp.experts` | 45 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5300 | `model.layers.0.mlp.experts` | 45 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5.0625 / 17.375 / 0.014021821071704228 / 0.7070016654807889 | [NPY](tensors/0005300.npy) |
| 5301 | `model.layers.0.mlp` | 45 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5.0625 / 17.375 / 0.014021821071704228 / 0.7070016654807889 | [NPY](tensors/0005301.npy) |
| 5302 | `model.layers.0.mlp` | 45 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.671875 / 1.96875 / -0.0564117431640625 / 1.1562630741847773 | [NPY](tensors/0005302.npy) |
| 5303 | `model.layers.0` | 45 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.0 / 58.75 / -0.01933187378777398 / 3.0890872263615505 | [NPY](tensors/0005303.npy) |
| 5382 | `model.layers.0` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 50.75 / -0.03880806507335769 / 2.8720089898153187 | [NPY](tensors/0005382.npy) |
| 5383 | `model.layers.0` | 46 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005383.npy) |
| 5384 | `model.layers.0` | 46 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.690826416015625 / 0.927895842605205 | [NPY](tensors/0005384.npy) |
| 5385 | `model.layers.0` | 46 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.04170632362365723 / 0.685352030153117 | [NPY](tensors/0005385.npy) |
| 5386 | `model.layers.0` | 46 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 350.0 / 350.0 / 350.0 / 0.0 | [NPY](tensors/0005386.npy) |
| 5387 | `model.layers.0` | 46 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5388 | `model.layers.0` | 46 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5389 | `model.layers.0` | 46 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5390 | `model.layers.0.input_layernorm` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.5 / 50.75 / -0.03880806507335769 / 2.8720089898153187 | [NPY](tensors/0005390.npy) |
| 5391 | `model.layers.0.input_layernorm` | 46 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0005391.npy) |
| 5392 | `model.layers.0.self_attn` | 46 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0005392.npy) |
| 5393 | `model.layers.0.self_attn` | 46 | `input.kwargs['attention_mask']` | [1, 1, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005393.npy) |
| 5394 | `model.layers.0.self_attn` | 46 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 350.0 / 350.0 / 350.0 / 0.0 | [NPY](tensors/0005394.npy) |
| 5395 | `model.layers.0.self_attn` | 46 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5396 | `model.layers.0.self_attn` | 46 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5397 | `model.layers.0.self_attn` | 46 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.690826416015625 / 0.927895842605205 | [NPY](tensors/0005397.npy) |
| 5398 | `model.layers.0.self_attn` | 46 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.04170632362365723 / 0.685352030153117 | [NPY](tensors/0005398.npy) |
| 5399 | `model.layers.0.self_attn` | 46 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5400 | `model.layers.0.self_attn.q_proj` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0005400.npy) |
| 5401 | `model.layers.0.self_attn.q_proj` | 46 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.15625 / 6.84375 / 0.0022307498147711158 / 0.9416562142053898 | [NPY](tensors/0005401.npy) |
| 5402 | `model.layers.0.self_attn.k_proj` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0005402.npy) |
| 5403 | `model.layers.0.self_attn.k_proj` | 46 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -53.0 / 42.75 / -0.03451061248779297 / 5.165071669827751 | [NPY](tensors/0005403.npy) |
| 5404 | `model.layers.0.self_attn.v_proj` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10.375 / 11.5 / -0.013169772591855792 / 0.7035512633919093 | [NPY](tensors/0005404.npy) |
| 5405 | `model.layers.0.self_attn.v_proj` | 46 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -3.5625 / 3.5 / 0.010839223861694336 / 0.9793238812790538 | [NPY](tensors/0005405.npy) |
| 5406 | `model.layers.0.self_attn.o_proj` | 46 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -4.375 / 3.78125 / 0.006095752420151257 / 0.5855693787147419 | [NPY](tensors/0005406.npy) |
| 5407 | `model.layers.0.self_attn.o_proj` | 46 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.375 / 34.0 / 0.03994197812345293 / 1.0448729114322806 | [NPY](tensors/0005407.npy) |
| 5408 | `model.layers.0.self_attn` | 46 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.375 / 34.0 / 0.03994197812345293 / 1.0448729114322806 | [NPY](tensors/0005408.npy) |
| 5409 | `model.layers.0.self_attn` | 46 | `output[1]` | [1, 64, 1, 128] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0035895634367435415 / 0.03812704739380731 | [NPY](tensors/0005409.npy) |
| 5410 | `model.layers.0.post_attention_layernorm` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 52.5 / 0.0011417018042670355 / 2.957363834354904 | [NPY](tensors/0005410.npy) |
| 5411 | `model.layers.0.post_attention_layernorm` | 46 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6640625 / 3.8125 / -0.001568391587999132 / 0.3017780186877547 | [NPY](tensors/0005411.npy) |
| 5412 | `model.layers.0.mlp` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1.6640625 / 3.8125 / -0.001568391587999132 / 0.3017780186877547 | [NPY](tensors/0005412.npy) |
| 5413 | `model.layers.0.mlp.experts` | 46 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -1.6640625 / 3.8125 / -0.001568391587999132 / 0.3017780186877547 | [NPY](tensors/0005413.npy) |
| 5414 | `model.layers.0.mlp.experts` | 46 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5415 | `model.layers.0.mlp.experts` | 46 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5416 | `model.layers.0.mlp.experts` | 46 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5417 | `model.layers.0.mlp.experts` | 46 | `output` | [1, 2880] | torch.bfloat16 → float32 | -8.25 / 30.125 / 0.021228201687335968 / 0.9465058264974929 | [NPY](tensors/0005417.npy) |
| 5418 | `model.layers.0.mlp` | 46 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8.25 / 30.125 / 0.021228201687335968 / 0.9465058264974929 | [NPY](tensors/0005418.npy) |
| 5419 | `model.layers.0.mlp` | 46 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.21875 / 2.328125 / -0.0782003402709961 / 1.0735204182138292 | [NPY](tensors/0005419.npy) |
| 5420 | `model.layers.0` | 46 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.0 / 65.5 / 0.022229152255588108 / 3.131754700436771 | [NPY](tensors/0005420.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.5021708492980846 / 49.263621414294526 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 305, 305] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6892090857909291e+38 / 1.694756585406476e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 305, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7963737057857826 / 0.8801360272441033 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 305, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12046455383190091 / 0.6213787871646592 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 305] | torch.int64 → int64 | 0.0 / 304.0 / 152.0 / 88.04544281222056 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.5021708492980846 / 49.263621414294526 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 305, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.06437157036611074 / 3.163273898829052 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 305, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.06437157036611074 / 3.163273898829052 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 305, 305] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6892090857909291e+38 / 1.694756585406476e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 305] | torch.int64 → int64 | 0.0 / 304.0 / 152.0 / 88.04544281222056 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 305, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7963737057857826 / 0.8801360272441033 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 305, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12046455383190091 / 0.6213787871646592 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.06437157036611074 / 3.163273898829052 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 305, 4096] | torch.bfloat16 → float32 | -11.25 / 13.3125 / 0.039656549904647675 / 1.3449855500144743 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.06437157036611074 / 3.163273898829052 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 305, 512] | torch.bfloat16 → float32 | -40.25 / 46.0 / 0.07321160659804696 / 3.668427399785015 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.06437157036611074 / 3.163273898829052 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 305, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.03565423200364973 / 2.491843021386286 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 305, 4096] | torch.bfloat16 → float32 | -11.8125 / 11.1875 / -0.02916721757446496 / 1.4368727632358913 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 305, 2880] | torch.bfloat16 → float32 | -464.0 / 498.0 / -0.03939656304490696 / 6.494148965491316 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -464.0 / 498.0 / -0.03939656304490696 / 6.494148965491316 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 305, 305] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0027772512752763717 / 0.017326023108170566 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -41216.0 / 724.0 / 0.4627783613778203 / 48.49148222698095 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 305, 2880] | torch.bfloat16 → float32 | -78.5 / 6.3125 / 0.009773982766271826 / 0.7794896137344188 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -78.5 / 6.3125 / 0.009773982766271826 / 0.7794896137344188 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [305, 2880] | torch.bfloat16 → float32 | -78.5 / 6.3125 / 0.009773982766271826 / 0.7794896137344188 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [305, 2880] | torch.bfloat16 → float32 | -548.0 / 456.0 / 0.10264933592200497 / 8.977113792884795 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -548.0 / 456.0 / 0.10264933592200497 / 8.977113792884795 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [305, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.15350090871091748 / 0.7373804893922785 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 305, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5655275373337265 / 50.928405501402096 | [NPY](tensors/0000077.npy) |
| 156 | `model.layers.11` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -190.0 / 243.0 / 0.3021241929796007 / 16.293842253002946 | [NPY](tensors/0000156.npy) |
| 157 | `model.layers.11` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 306] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000157.npy) |
| 158 | `model.layers.11` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0000158.npy) |
| 159 | `model.layers.11` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0000159.npy) |
| 160 | `model.layers.11` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0000160.npy) |
| 161 | `model.layers.11` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 162 | `model.layers.11` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 163 | `model.layers.11` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 164 | `model.layers.11.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -190.0 / 243.0 / 0.3021241929796007 / 16.293842253002946 | [NPY](tensors/0000164.npy) |
| 165 | `model.layers.11.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.25 / 68.0 / 0.06337158150143093 / 2.5632071863105184 | [NPY](tensors/0000165.npy) |
| 166 | `model.layers.11.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.25 / 68.0 / 0.06337158150143093 / 2.5632071863105184 | [NPY](tensors/0000166.npy) |
| 167 | `model.layers.11.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 306] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000167.npy) |
| 168 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0000168.npy) |
| 169 | `model.layers.11.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 170 | `model.layers.11.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 171 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0000171.npy) |
| 172 | `model.layers.11.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0000172.npy) |
| 173 | `model.layers.11.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 174 | `model.layers.11.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.25 / 68.0 / 0.06337158150143093 / 2.5632071863105184 | [NPY](tensors/0000174.npy) |
| 175 | `model.layers.11.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.53125 / 11.5625 / 0.06128166802227497 / 1.2875979820711532 | [NPY](tensors/0000175.npy) |
| 176 | `model.layers.11.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.25 / 68.0 / 0.06337158150143093 / 2.5632071863105184 | [NPY](tensors/0000176.npy) |
| 177 | `model.layers.11.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.75 / 33.0 / 0.07095721364021301 / 3.557036322734646 | [NPY](tensors/0000177.npy) |
| 178 | `model.layers.11.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -61.25 / 68.0 / 0.06337158150143093 / 2.5632071863105184 | [NPY](tensors/0000178.npy) |
| 179 | `model.layers.11.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.78125 / 9.1875 / -0.060971589758992195 / 2.417867971631514 | [NPY](tensors/0000179.npy) |
| 180 | `model.layers.11.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.65625 / 7.0 / -0.034567913389764726 / 1.4813935050018834 | [NPY](tensors/0000180.npy) |
| 181 | `model.layers.11.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 81.0 / 0.01899651288986206 / 4.418650014694393 | [NPY](tensors/0000181.npy) |
| 182 | `model.layers.11.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 81.0 / 0.01899651288986206 / 4.418650014694393 | [NPY](tensors/0000182.npy) |
| 183 | `model.layers.11.self_attn` | 1 | `output[1]` | [1, 64, 1, 306] | torch.bfloat16 → float32 | 2.419255906715989e-10 / 0.8671875 / 0.0029872005656913785 / 0.011932825447981894 | [NPY](tensors/0000183.npy) |
| 184 | `model.layers.11.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -270.0 / 316.0 / 0.3206759982638889 / 18.579019569130075 | [NPY](tensors/0000184.npy) |
| 185 | `model.layers.11.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.140625 / 3.578125 / -0.00543609791331821 / 0.7673854827011773 | [NPY](tensors/0000185.npy) |
| 186 | `model.layers.11.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.140625 / 3.578125 / -0.00543609791331821 / 0.7673854827011773 | [NPY](tensors/0000186.npy) |
| 187 | `model.layers.11.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.140625 / 3.578125 / -0.00543609791331821 / 0.7673854827011773 | [NPY](tensors/0000187.npy) |
| 188 | `model.layers.11.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 189 | `model.layers.11.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 190 | `model.layers.11.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 191 | `model.layers.11.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -57.5 / 92.0 / 0.28278281589349114 / 5.83334267498169 | [NPY](tensors/0000191.npy) |
| 192 | `model.layers.11.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.5 / 92.0 / 0.28278281589349114 / 5.83334267498169 | [NPY](tensors/0000192.npy) |
| 193 | `model.layers.11.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3984375 / 1.5703125 / -0.061278343200683594 / 0.7082484787670505 | [NPY](tensors/0000193.npy) |
| 194 | `model.layers.11` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -328.0 / 408.0 / 0.6045688205295139 / 21.739892491528348 | [NPY](tensors/0000194.npy) |
| 273 | `model.layers.11` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -296.0 / 416.0 / 0.41511789957682294 / 19.186379560450433 | [NPY](tensors/0000273.npy) |
| 274 | `model.layers.11` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 307] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000274.npy) |
| 275 | `model.layers.11` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0000275.npy) |
| 276 | `model.layers.11` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0000276.npy) |
| 277 | `model.layers.11` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0000277.npy) |
| 278 | `model.layers.11` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 279 | `model.layers.11` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 280 | `model.layers.11` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 281 | `model.layers.11.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -296.0 / 416.0 / 0.41511789957682294 / 19.186379560450433 | [NPY](tensors/0000281.npy) |
| 282 | `model.layers.11.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -81.0 / 101.5 / 0.06569293472501966 / 3.092844563157117 | [NPY](tensors/0000282.npy) |
| 283 | `model.layers.11.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -81.0 / 101.5 / 0.06569293472501966 / 3.092844563157117 | [NPY](tensors/0000283.npy) |
| 284 | `model.layers.11.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 307] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000284.npy) |
| 285 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0000285.npy) |
| 286 | `model.layers.11.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 287 | `model.layers.11.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 288 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0000288.npy) |
| 289 | `model.layers.11.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0000289.npy) |
| 290 | `model.layers.11.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 291 | `model.layers.11.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -81.0 / 101.5 / 0.06569293472501966 / 3.092844563157117 | [NPY](tensors/0000291.npy) |
| 292 | `model.layers.11.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.75 / 10.625 / 0.052706106449477375 / 1.2016420219847639 | [NPY](tensors/0000292.npy) |
| 293 | `model.layers.11.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -81.0 / 101.5 / 0.06569293472501966 / 3.092844563157117 | [NPY](tensors/0000293.npy) |
| 294 | `model.layers.11.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.625 / 35.0 / 0.1060841977596283 / 3.3748696860814658 | [NPY](tensors/0000294.npy) |
| 295 | `model.layers.11.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -81.0 / 101.5 / 0.06569293472501966 / 3.092844563157117 | [NPY](tensors/0000295.npy) |
| 296 | `model.layers.11.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.03125 / 5.5625 / -0.025850772857666016 / 1.8949719991004177 | [NPY](tensors/0000296.npy) |
| 297 | `model.layers.11.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 5.625 / -0.03196520730853081 / 1.3469625358823525 | [NPY](tensors/0000297.npy) |
| 298 | `model.layers.11.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 30.875 / -0.10062485271030003 / 3.856508378630781 | [NPY](tensors/0000298.npy) |
| 299 | `model.layers.11.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.25 / 30.875 / -0.10062485271030003 / 3.856508378630781 | [NPY](tensors/0000299.npy) |
| 300 | `model.layers.11.self_attn` | 2 | `output[1]` | [1, 64, 1, 307] | torch.bfloat16 → float32 | 1.7280399333685637e-11 / 0.96875 / 0.0030793585980227146 / 0.013477708088869346 | [NPY](tensors/0000300.npy) |
| 301 | `model.layers.11.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -294.0 / 374.0 / 0.314096917046441 / 19.57270240918563 | [NPY](tensors/0000301.npy) |
| 302 | `model.layers.11.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.703125 / 3.59375 / -0.016100052992502847 / 0.7128935358456312 | [NPY](tensors/0000302.npy) |
| 303 | `model.layers.11.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.703125 / 3.59375 / -0.016100052992502847 / 0.7128935358456312 | [NPY](tensors/0000303.npy) |
| 304 | `model.layers.11.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.703125 / 3.59375 / -0.016100052992502847 / 0.7128935358456312 | [NPY](tensors/0000304.npy) |
| 305 | `model.layers.11.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 306 | `model.layers.11.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 307 | `model.layers.11.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 308 | `model.layers.11.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -103.0 / 141.0 / 0.22103550699022081 / 5.996554397197976 | [NPY](tensors/0000308.npy) |
| 309 | `model.layers.11.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.0 / 141.0 / 0.22103550699022081 / 5.996554397197976 | [NPY](tensors/0000309.npy) |
| 310 | `model.layers.11.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6484375 / 1.1953125 / -0.06434154510498047 / 0.6378958023545676 | [NPY](tensors/0000310.npy) |
| 311 | `model.layers.11` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -396.0 / 476.0 / 0.53387451171875 / 23.157338134080092 | [NPY](tensors/0000311.npy) |
| 390 | `model.layers.11` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -204.0 / 348.0 / 0.5032079908582899 / 14.309180377151963 | [NPY](tensors/0000390.npy) |
| 391 | `model.layers.11` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 308] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000391.npy) |
| 392 | `model.layers.11` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0000392.npy) |
| 393 | `model.layers.11` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0000393.npy) |
| 394 | `model.layers.11` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0000394.npy) |
| 395 | `model.layers.11` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 396 | `model.layers.11` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 397 | `model.layers.11` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 398 | `model.layers.11.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -204.0 / 348.0 / 0.5032079908582899 / 14.309180377151963 | [NPY](tensors/0000398.npy) |
| 399 | `model.layers.11.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.0 / 99.5 / 0.0896952662203047 / 3.133972526582658 | [NPY](tensors/0000399.npy) |
| 400 | `model.layers.11.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.0 / 99.5 / 0.0896952662203047 / 3.133972526582658 | [NPY](tensors/0000400.npy) |
| 401 | `model.layers.11.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 308] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000401.npy) |
| 402 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0000402.npy) |
| 403 | `model.layers.11.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 404 | `model.layers.11.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 405 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0000405.npy) |
| 406 | `model.layers.11.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0000406.npy) |
| 407 | `model.layers.11.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 408 | `model.layers.11.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.0 / 99.5 / 0.0896952662203047 / 3.133972526582658 | [NPY](tensors/0000408.npy) |
| 409 | `model.layers.11.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.15625 / 8.0625 / 0.058177508413791656 / 1.187256895749316 | [NPY](tensors/0000409.npy) |
| 410 | `model.layers.11.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.0 / 99.5 / 0.0896952662203047 / 3.133972526582658 | [NPY](tensors/0000410.npy) |
| 411 | `model.layers.11.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.25 / 35.25 / 0.11111897230148315 / 3.598482509995758 | [NPY](tensors/0000411.npy) |
| 412 | `model.layers.11.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -75.0 / 99.5 / 0.0896952662203047 / 3.133972526582658 | [NPY](tensors/0000412.npy) |
| 413 | `model.layers.11.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.28125 / 6.125 / -0.020404517650604248 / 1.8349377297994587 | [NPY](tensors/0000413.npy) |
| 414 | `model.layers.11.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.90625 / 5.34375 / -0.001891086925752461 / 1.1961217775219293 | [NPY](tensors/0000414.npy) |
| 415 | `model.layers.11.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 18.375 / 0.018518601523505318 / 3.1523231570276153 | [NPY](tensors/0000415.npy) |
| 416 | `model.layers.11.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.125 / 18.375 / 0.018518601523505318 / 3.1523231570276153 | [NPY](tensors/0000416.npy) |
| 417 | `model.layers.11.self_attn` | 3 | `output[1]` | [1, 64, 1, 308] | torch.bfloat16 → float32 | 4.001776687800884e-10 / 0.8671875 / 0.003032292589346986 / 0.011982234153355892 | [NPY](tensors/0000417.npy) |
| 418 | `model.layers.11.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -219.0 / 342.0 / 0.5224990844726562 / 15.102752022621333 | [NPY](tensors/0000418.npy) |
| 419 | `model.layers.11.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.53125 / 3.484375 / 0.01514062484105428 / 0.6749236921371946 | [NPY](tensors/0000419.npy) |
| 420 | `model.layers.11.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.53125 / 3.484375 / 0.01514062484105428 / 0.6749236921371946 | [NPY](tensors/0000420.npy) |
| 421 | `model.layers.11.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.53125 / 3.484375 / 0.01514062484105428 / 0.6749236921371946 | [NPY](tensors/0000421.npy) |
| 422 | `model.layers.11.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 423 | `model.layers.11.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 424 | `model.layers.11.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 425 | `model.layers.11.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -95.5 / 84.0 / 0.016534190707736544 / 4.278326851815222 | [NPY](tensors/0000425.npy) |
| 426 | `model.layers.11.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.5 / 84.0 / 0.016534190707736544 / 4.278326851815222 | [NPY](tensors/0000426.npy) |
| 427 | `model.layers.11.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.421875 / 0.92578125 / -0.07372665405273438 / 0.5262880287773735 | [NPY](tensors/0000427.npy) |
| 428 | `model.layers.11` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -314.0 / 382.0 / 0.5390477498372396 / 17.495828262795637 | [NPY](tensors/0000428.npy) |
| 507 | `model.layers.11` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -396.0 / 500.0 / 0.7943829854329427 / 20.27529243271835 | [NPY](tensors/0000507.npy) |
| 508 | `model.layers.11` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 309] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000508.npy) |
| 509 | `model.layers.11` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0000509.npy) |
| 510 | `model.layers.11` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0000510.npy) |
| 511 | `model.layers.11` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0000511.npy) |
| 512 | `model.layers.11` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 513 | `model.layers.11` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 514 | `model.layers.11` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 515 | `model.layers.11.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -396.0 / 500.0 / 0.7943829854329427 / 20.27529243271835 | [NPY](tensors/0000515.npy) |
| 516 | `model.layers.11.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.5 / 109.5 / 0.08561265468597412 / 3.4750110971320183 | [NPY](tensors/0000516.npy) |
| 517 | `model.layers.11.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.5 / 109.5 / 0.08561265468597412 / 3.4750110971320183 | [NPY](tensors/0000517.npy) |
| 518 | `model.layers.11.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 309] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000518.npy) |
| 519 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0000519.npy) |
| 520 | `model.layers.11.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 521 | `model.layers.11.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 522 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0000522.npy) |
| 523 | `model.layers.11.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0000523.npy) |
| 524 | `model.layers.11.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 525 | `model.layers.11.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.5 / 109.5 / 0.08561265468597412 / 3.4750110971320183 | [NPY](tensors/0000525.npy) |
| 526 | `model.layers.11.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.90625 / 7.40625 / 0.03360309486743063 / 1.139532572935187 | [NPY](tensors/0000526.npy) |
| 527 | `model.layers.11.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.5 / 109.5 / 0.08561265468597412 / 3.4750110971320183 | [NPY](tensors/0000527.npy) |
| 528 | `model.layers.11.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.75 / 42.75 / 0.10850007832050323 / 3.942902206046032 | [NPY](tensors/0000528.npy) |
| 529 | `model.layers.11.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.5 / 109.5 / 0.08561265468597412 / 3.4750110971320183 | [NPY](tensors/0000529.npy) |
| 530 | `model.layers.11.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -4.53125 / 7.0625 / 0.08068835735321045 / 1.785922689435329 | [NPY](tensors/0000530.npy) |
| 531 | `model.layers.11.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5 / 6.84375 / 0.008917322615161538 / 1.3054958320540129 | [NPY](tensors/0000531.npy) |
| 532 | `model.layers.11.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 72.5 / -0.019604806105295816 / 4.230622013248112 | [NPY](tensors/0000532.npy) |
| 533 | `model.layers.11.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 72.5 / -0.019604806105295816 / 4.230622013248112 | [NPY](tensors/0000533.npy) |
| 534 | `model.layers.11.self_attn` | 4 | `output[1]` | [1, 64, 1, 309] | torch.bfloat16 → float32 | 2.9842794901924208e-12 / 0.9609375 / 0.0030093212944222094 / 0.014905427172292755 | [NPY](tensors/0000534.npy) |
| 535 | `model.layers.11.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -324.0 / 468.0 / 0.7748397827148438 / 20.433378185966724 | [NPY](tensors/0000535.npy) |
| 536 | `model.layers.11.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.703125 / 3.0625 / 0.01629947688844469 / 0.636190839483984 | [NPY](tensors/0000536.npy) |
| 537 | `model.layers.11.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.703125 / 3.0625 / 0.01629947688844469 / 0.636190839483984 | [NPY](tensors/0000537.npy) |
| 538 | `model.layers.11.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.703125 / 3.0625 / 0.01629947688844469 / 0.636190839483984 | [NPY](tensors/0000538.npy) |
| 539 | `model.layers.11.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 540 | `model.layers.11.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 541 | `model.layers.11.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 542 | `model.layers.11.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -165.0 / 127.0 / 0.025807041592068144 / 5.5849122598094 | [NPY](tensors/0000542.npy) |
| 543 | `model.layers.11.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -165.0 / 127.0 / 0.025807041592068144 / 5.5849122598094 | [NPY](tensors/0000543.npy) |
| 544 | `model.layers.11.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.2265625 / -0.0666050910949707 / 0.49025823888832193 | [NPY](tensors/0000544.npy) |
| 545 | `model.layers.11` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -488.0 / 556.0 / 0.8012349446614583 / 24.06549374993523 | [NPY](tensors/0000545.npy) |
| 624 | `model.layers.11` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -354.0 / 432.0 / 0.24093153211805557 / 18.82069131441934 | [NPY](tensors/0000624.npy) |
| 625 | `model.layers.11` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 310] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000625.npy) |
| 626 | `model.layers.11` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0000626.npy) |
| 627 | `model.layers.11` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0000627.npy) |
| 628 | `model.layers.11` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0000628.npy) |
| 629 | `model.layers.11` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 630 | `model.layers.11` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 631 | `model.layers.11` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 632 | `model.layers.11.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -354.0 / 432.0 / 0.24093153211805557 / 18.82069131441934 | [NPY](tensors/0000632.npy) |
| 633 | `model.layers.11.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 88.5 / 0.031187322404649522 / 3.199205460000611 | [NPY](tensors/0000633.npy) |
| 634 | `model.layers.11.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 88.5 / 0.031187322404649522 / 3.199205460000611 | [NPY](tensors/0000634.npy) |
| 635 | `model.layers.11.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 310] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000635.npy) |
| 636 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0000636.npy) |
| 637 | `model.layers.11.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 638 | `model.layers.11.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 639 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0000639.npy) |
| 640 | `model.layers.11.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0000640.npy) |
| 641 | `model.layers.11.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 642 | `model.layers.11.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 88.5 / 0.031187322404649522 / 3.199205460000611 | [NPY](tensors/0000642.npy) |
| 643 | `model.layers.11.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.65625 / 9.625 / 0.05622560949996114 / 1.2373778017034576 | [NPY](tensors/0000643.npy) |
| 644 | `model.layers.11.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 88.5 / 0.031187322404649522 / 3.199205460000611 | [NPY](tensors/0000644.npy) |
| 645 | `model.layers.11.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -37.0 / 44.0 / 0.20838046073913574 / 4.1974424098601775 | [NPY](tensors/0000645.npy) |
| 646 | `model.layers.11.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 88.5 / 0.031187322404649522 / 3.199205460000611 | [NPY](tensors/0000646.npy) |
| 647 | `model.layers.11.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.625 / 7.40625 / -0.01674462854862213 / 2.134456681861216 | [NPY](tensors/0000647.npy) |
| 648 | `model.layers.11.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.625 / 6.75 / -0.023474688176065683 / 1.4468362871935376 | [NPY](tensors/0000648.npy) |
| 649 | `model.layers.11.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.25 / 48.0 / -0.02468912336561415 / 4.167925835710018 | [NPY](tensors/0000649.npy) |
| 650 | `model.layers.11.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.25 / 48.0 / -0.02468912336561415 / 4.167925835710018 | [NPY](tensors/0000650.npy) |
| 651 | `model.layers.11.self_attn` | 5 | `output[1]` | [1, 64, 1, 310] | torch.bfloat16 → float32 | 7.425171588693047e-13 / 0.9453125 / 0.003075766299359956 / 0.016962557518465076 | [NPY](tensors/0000651.npy) |
| 652 | `model.layers.11.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -310.0 / 450.0 / 0.21565280490451388 / 20.015824162381875 | [NPY](tensors/0000652.npy) |
| 653 | `model.layers.11.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.078125 / 2.890625 / -0.0029452853732638887 / 0.6664077635217067 | [NPY](tensors/0000653.npy) |
| 654 | `model.layers.11.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.078125 / 2.890625 / -0.0029452853732638887 / 0.6664077635217067 | [NPY](tensors/0000654.npy) |
| 655 | `model.layers.11.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.078125 / 2.890625 / -0.0029452853732638887 / 0.6664077635217067 | [NPY](tensors/0000655.npy) |
| 656 | `model.layers.11.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 657 | `model.layers.11.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 658 | `model.layers.11.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 659 | `model.layers.11.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -187.0 / 142.0 / 0.00458302464750078 / 6.57256179289231 | [NPY](tensors/0000659.npy) |
| 660 | `model.layers.11.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -187.0 / 142.0 / 0.00458302464750078 / 6.57256179289231 | [NPY](tensors/0000660.npy) |
| 661 | `model.layers.11.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.703125 / 0.83203125 / -0.15704727172851562 / 0.5450024111067021 | [NPY](tensors/0000661.npy) |
| 662 | `model.layers.11` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -496.0 / 556.0 / 0.22171427408854166 / 24.312964367608995 | [NPY](tensors/0000662.npy) |
| 741 | `model.layers.11` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -420.0 / 460.0 / 0.4498708936903212 / 20.30317600476532 | [NPY](tensors/0000741.npy) |
| 742 | `model.layers.11` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 311] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000742.npy) |
| 743 | `model.layers.11` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0000743.npy) |
| 744 | `model.layers.11` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0000744.npy) |
| 745 | `model.layers.11` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0000745.npy) |
| 746 | `model.layers.11` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 747 | `model.layers.11` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 748 | `model.layers.11` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 749 | `model.layers.11.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -420.0 / 460.0 / 0.4498708936903212 / 20.30317600476532 | [NPY](tensors/0000749.npy) |
| 750 | `model.layers.11.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.5 / 97.0 / 0.04446728097067939 / 3.376210158019438 | [NPY](tensors/0000750.npy) |
| 751 | `model.layers.11.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.5 / 97.0 / 0.04446728097067939 / 3.376210158019438 | [NPY](tensors/0000751.npy) |
| 752 | `model.layers.11.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 311] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000752.npy) |
| 753 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0000753.npy) |
| 754 | `model.layers.11.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 755 | `model.layers.11.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 756 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0000756.npy) |
| 757 | `model.layers.11.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0000757.npy) |
| 758 | `model.layers.11.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 759 | `model.layers.11.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.5 / 97.0 / 0.04446728097067939 / 3.376210158019438 | [NPY](tensors/0000759.npy) |
| 760 | `model.layers.11.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.40625 / 9.0 / 0.058482807129621506 / 1.165324653937853 | [NPY](tensors/0000760.npy) |
| 761 | `model.layers.11.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.5 / 97.0 / 0.04446728097067939 / 3.376210158019438 | [NPY](tensors/0000761.npy) |
| 762 | `model.layers.11.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.5 / 47.0 / 0.1591682732105255 / 4.192469868842422 | [NPY](tensors/0000762.npy) |
| 763 | `model.layers.11.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -108.5 / 97.0 / 0.04446728097067939 / 3.376210158019438 | [NPY](tensors/0000763.npy) |
| 764 | `model.layers.11.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.21875 / 9.0 / -0.01195932924747467 / 2.2022874724330195 | [NPY](tensors/0000764.npy) |
| 765 | `model.layers.11.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.1875 / 7.125 / 0.0015354554343502969 / 1.5174857849551886 | [NPY](tensors/0000765.npy) |
| 766 | `model.layers.11.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 132.0 / 0.03440231747097439 / 4.92047462693797 | [NPY](tensors/0000766.npy) |
| 767 | `model.layers.11.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 132.0 / 0.03440231747097439 / 4.92047462693797 | [NPY](tensors/0000767.npy) |
| 768 | `model.layers.11.self_attn` | 6 | `output[1]` | [1, 64, 1, 311] | torch.bfloat16 → float32 | 4.050093593832571e-13 / 0.96484375 / 0.002997694710458302 / 0.019121828299625162 | [NPY](tensors/0000768.npy) |
| 769 | `model.layers.11.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -288.0 / 418.0 / 0.4833243899875217 / 19.723667139528033 | [NPY](tensors/0000769.npy) |
| 770 | `model.layers.11.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.453125 / 5.375 / 0.01713855266571045 / 0.6867134007730428 | [NPY](tensors/0000770.npy) |
| 771 | `model.layers.11.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.453125 / 5.375 / 0.01713855266571045 / 0.6867134007730428 | [NPY](tensors/0000771.npy) |
| 772 | `model.layers.11.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.453125 / 5.375 / 0.01713855266571045 / 0.6867134007730428 | [NPY](tensors/0000772.npy) |
| 773 | `model.layers.11.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 774 | `model.layers.11.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 775 | `model.layers.11.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 776 | `model.layers.11.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -294.0 / 276.0 / 0.14816586971282958 / 9.914394247919766 | [NPY](tensors/0000776.npy) |
| 777 | `model.layers.11.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -294.0 / 276.0 / 0.14816586971282958 / 9.914394247919766 | [NPY](tensors/0000777.npy) |
| 778 | `model.layers.11.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8671875 / 1.328125 / -0.14021682739257812 / 0.6957632794960987 | [NPY](tensors/0000778.npy) |
| 779 | `model.layers.11` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -584.0 / 604.0 / 0.6310682508680555 / 26.736816302192288 | [NPY](tensors/0000779.npy) |
| 858 | `model.layers.11` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -276.0 / 368.0 / 0.901910909016927 / 16.544980716166307 | [NPY](tensors/0000858.npy) |
| 859 | `model.layers.11` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 312] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000859.npy) |
| 860 | `model.layers.11` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0000860.npy) |
| 861 | `model.layers.11` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0000861.npy) |
| 862 | `model.layers.11` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0000862.npy) |
| 863 | `model.layers.11` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 864 | `model.layers.11` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 865 | `model.layers.11` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 866 | `model.layers.11.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -276.0 / 368.0 / 0.901910909016927 / 16.544980716166307 | [NPY](tensors/0000866.npy) |
| 867 | `model.layers.11.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 100.5 / 0.11157588164011638 / 3.2164541929674106 | [NPY](tensors/0000867.npy) |
| 868 | `model.layers.11.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 100.5 / 0.11157588164011638 / 3.2164541929674106 | [NPY](tensors/0000868.npy) |
| 869 | `model.layers.11.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 312] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000869.npy) |
| 870 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0000870.npy) |
| 871 | `model.layers.11.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 872 | `model.layers.11.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 873 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0000873.npy) |
| 874 | `model.layers.11.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0000874.npy) |
| 875 | `model.layers.11.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 876 | `model.layers.11.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 100.5 / 0.11157588164011638 / 3.2164541929674106 | [NPY](tensors/0000876.npy) |
| 877 | `model.layers.11.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.8125 / 8.875 / 0.037178698694333434 / 1.2215487789552093 | [NPY](tensors/0000877.npy) |
| 878 | `model.layers.11.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 100.5 / 0.11157588164011638 / 3.2164541929674106 | [NPY](tensors/0000878.npy) |
| 879 | `model.layers.11.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 42.0 / 0.17864662362262607 / 4.145085981806948 | [NPY](tensors/0000879.npy) |
| 880 | `model.layers.11.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -87.5 / 100.5 / 0.11157588164011638 / 3.2164541929674106 | [NPY](tensors/0000880.npy) |
| 881 | `model.layers.11.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.59375 / 9.0 / 0.04381585121154785 / 2.167037476585435 | [NPY](tensors/0000881.npy) |
| 882 | `model.layers.11.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.25 / 7.65625 / 0.013628306798636913 / 1.3469203489600683 | [NPY](tensors/0000882.npy) |
| 883 | `model.layers.11.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.875 / 70.0 / 0.0068309982617696125 / 3.726318921458315 | [NPY](tensors/0000883.npy) |
| 884 | `model.layers.11.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -19.875 / 70.0 / 0.0068309982617696125 / 3.726318921458315 | [NPY](tensors/0000884.npy) |
| 885 | `model.layers.11.self_attn` | 7 | `output[1]` | [1, 64, 1, 312] | torch.bfloat16 → float32 | 2.7057467377744615e-11 / 0.921875 / 0.0029782935170507663 / 0.01415668174075316 | [NPY](tensors/0000885.npy) |
| 886 | `model.layers.11.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -242.0 / 372.0 / 0.9091313680013021 / 17.618815848200704 | [NPY](tensors/0000886.npy) |
| 887 | `model.layers.11.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.125 / 3.609375 / 0.02906611230638292 / 0.6756898230737786 | [NPY](tensors/0000887.npy) |
| 888 | `model.layers.11.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.125 / 3.609375 / 0.02906611230638292 / 0.6756898230737786 | [NPY](tensors/0000888.npy) |
| 889 | `model.layers.11.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.125 / 3.609375 / 0.02906611230638292 / 0.6756898230737786 | [NPY](tensors/0000889.npy) |
| 890 | `model.layers.11.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 891 | `model.layers.11.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 892 | `model.layers.11.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 893 | `model.layers.11.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -127.0 / 85.5 / 0.015159483750661213 / 4.675122960731247 | [NPY](tensors/0000893.npy) |
| 894 | `model.layers.11.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -127.0 / 85.5 / 0.015159483750661213 / 4.675122960731247 | [NPY](tensors/0000894.npy) |
| 895 | `model.layers.11.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.0625 / -0.0645294189453125 / 0.45098745795289086 | [NPY](tensors/0000895.npy) |
| 896 | `model.layers.11` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -368.0 / 446.0 / 0.9249666002061632 / 20.037910507070038 | [NPY](tensors/0000896.npy) |
| 975 | `model.layers.11` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -468.0 / 474.0 / 0.35662095811631944 / 20.214849088420006 | [NPY](tensors/0000975.npy) |
| 976 | `model.layers.11` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 313] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000976.npy) |
| 977 | `model.layers.11` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0000977.npy) |
| 978 | `model.layers.11` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0000978.npy) |
| 979 | `model.layers.11` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0000979.npy) |
| 980 | `model.layers.11` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 981 | `model.layers.11` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 982 | `model.layers.11` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 983 | `model.layers.11.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -468.0 / 474.0 / 0.35662095811631944 / 20.214849088420006 | [NPY](tensors/0000983.npy) |
| 984 | `model.layers.11.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -121.5 / 85.5 / 0.037392422556877136 / 3.4023781345275292 | [NPY](tensors/0000984.npy) |
| 985 | `model.layers.11.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -121.5 / 85.5 / 0.037392422556877136 / 3.4023781345275292 | [NPY](tensors/0000985.npy) |
| 986 | `model.layers.11.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 313] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000986.npy) |
| 987 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0000987.npy) |
| 988 | `model.layers.11.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 989 | `model.layers.11.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 990 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0000990.npy) |
| 991 | `model.layers.11.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0000991.npy) |
| 992 | `model.layers.11.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 993 | `model.layers.11.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -121.5 / 85.5 / 0.037392422556877136 / 3.4023781345275292 | [NPY](tensors/0000993.npy) |
| 994 | `model.layers.11.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.28125 / 8.875 / 0.03848988376557827 / 1.2479732167780595 | [NPY](tensors/0000994.npy) |
| 995 | `model.layers.11.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -121.5 / 85.5 / 0.037392422556877136 / 3.4023781345275292 | [NPY](tensors/0000995.npy) |
| 996 | `model.layers.11.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.0 / 36.5 / 0.18784647062420845 / 4.026161047358257 | [NPY](tensors/0000996.npy) |
| 997 | `model.layers.11.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -121.5 / 85.5 / 0.037392422556877136 / 3.4023781345275292 | [NPY](tensors/0000997.npy) |
| 998 | `model.layers.11.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.4375 / 6.84375 / 0.07668942213058472 / 2.164728506576596 | [NPY](tensors/0000998.npy) |
| 999 | `model.layers.11.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.1875 / 7.5625 / 0.009775609942153096 / 1.5674634363115152 | [NPY](tensors/0000999.npy) |
| 1000 | `model.layers.11.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.0 / 147.0 / -0.033502835697597926 / 5.391354339152843 | [NPY](tensors/0001000.npy) |
| 1001 | `model.layers.11.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.0 / 147.0 / -0.033502835697597926 / 5.391354339152843 | [NPY](tensors/0001001.npy) |
| 1002 | `model.layers.11.self_attn` | 8 | `output[1]` | [1, 64, 1, 313] | torch.bfloat16 → float32 | 9.414691248821327e-14 / 0.96484375 / 0.0030355660624353893 / 0.0200496109121098 | [NPY](tensors/0001002.npy) |
| 1003 | `model.layers.11.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -320.0 / 422.0 / 0.3231136745876736 / 19.559124251137504 | [NPY](tensors/0001003.npy) |
| 1004 | `model.layers.11.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.796875 / 4.53125 / 0.0053038133515252005 / 0.7001006938357034 | [NPY](tensors/0001004.npy) |
| 1005 | `model.layers.11.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.796875 / 4.53125 / 0.0053038133515252005 / 0.7001006938357034 | [NPY](tensors/0001005.npy) |
| 1006 | `model.layers.11.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.796875 / 4.53125 / 0.0053038133515252005 / 0.7001006938357034 | [NPY](tensors/0001006.npy) |
| 1007 | `model.layers.11.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1008 | `model.layers.11.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1009 | `model.layers.11.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1010 | `model.layers.11.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -316.0 / 258.0 / 0.03870012760162354 / 9.941897034134582 | [NPY](tensors/0001010.npy) |
| 1011 | `model.layers.11.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -316.0 / 258.0 / 0.03870012760162354 / 9.941897034134582 | [NPY](tensors/0001011.npy) |
| 1012 | `model.layers.11.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.0 / 0.84765625 / -0.18966293334960938 / 0.6512448978401358 | [NPY](tensors/0001012.npy) |
| 1013 | `model.layers.11` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -636.0 / 568.0 / 0.36221516927083336 / 26.53412943042027 | [NPY](tensors/0001013.npy) |
| 1092 | `model.layers.11` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -398.0 / 464.0 / 0.41997884114583334 / 20.603267761059687 | [NPY](tensors/0001092.npy) |
| 1093 | `model.layers.11` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 314] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001093.npy) |
| 1094 | `model.layers.11` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0001094.npy) |
| 1095 | `model.layers.11` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0001095.npy) |
| 1096 | `model.layers.11` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0001096.npy) |
| 1097 | `model.layers.11` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1098 | `model.layers.11` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1099 | `model.layers.11` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1100 | `model.layers.11.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -398.0 / 464.0 / 0.41997884114583334 / 20.603267761059687 | [NPY](tensors/0001100.npy) |
| 1101 | `model.layers.11.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 101.0 / 0.05433693064583672 / 3.3012005415211068 | [NPY](tensors/0001101.npy) |
| 1102 | `model.layers.11.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 101.0 / 0.05433693064583672 / 3.3012005415211068 | [NPY](tensors/0001102.npy) |
| 1103 | `model.layers.11.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 314] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001103.npy) |
| 1104 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0001104.npy) |
| 1105 | `model.layers.11.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1106 | `model.layers.11.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1107 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0001107.npy) |
| 1108 | `model.layers.11.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0001108.npy) |
| 1109 | `model.layers.11.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1110 | `model.layers.11.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 101.0 / 0.05433693064583672 / 3.3012005415211068 | [NPY](tensors/0001110.npy) |
| 1111 | `model.layers.11.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.78125 / 7.75 / 0.063714875432197 / 1.2264260949268386 | [NPY](tensors/0001111.npy) |
| 1112 | `model.layers.11.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 101.0 / 0.05433693064583672 / 3.3012005415211068 | [NPY](tensors/0001112.npy) |
| 1113 | `model.layers.11.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.25 / 35.75 / 0.16732892394065857 / 4.037041861592945 | [NPY](tensors/0001113.npy) |
| 1114 | `model.layers.11.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 101.0 / 0.05433693064583672 / 3.3012005415211068 | [NPY](tensors/0001114.npy) |
| 1115 | `model.layers.11.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.53125 / 8.5 / 0.06961899995803833 / 2.325708255709022 | [NPY](tensors/0001115.npy) |
| 1116 | `model.layers.11.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.125 / 7.78125 / 0.02095202449709177 / 1.615899182318629 | [NPY](tensors/0001116.npy) |
| 1117 | `model.layers.11.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 83.0 / -0.032539855109320746 / 4.459042288703416 | [NPY](tensors/0001117.npy) |
| 1118 | `model.layers.11.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 83.0 / -0.032539855109320746 / 4.459042288703416 | [NPY](tensors/0001118.npy) |
| 1119 | `model.layers.11.self_attn` | 9 | `output[1]` | [1, 64, 1, 314] | torch.bfloat16 → float32 | 6.679101716144942e-13 / 0.96484375 / 0.00298924136552132 / 0.019765362676302103 | [NPY](tensors/0001119.npy) |
| 1120 | `model.layers.11.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -324.0 / 440.0 / 0.3880740695529514 / 21.058094345994096 | [NPY](tensors/0001120.npy) |
| 1121 | `model.layers.11.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.21875 / 3.984375 / 0.00617770618862576 / 0.6514746243436722 | [NPY](tensors/0001121.npy) |
| 1122 | `model.layers.11.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.21875 / 3.984375 / 0.00617770618862576 / 0.6514746243436722 | [NPY](tensors/0001122.npy) |
| 1123 | `model.layers.11.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.21875 / 3.984375 / 0.00617770618862576 / 0.6514746243436722 | [NPY](tensors/0001123.npy) |
| 1124 | `model.layers.11.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1125 | `model.layers.11.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1126 | `model.layers.11.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1127 | `model.layers.11.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -173.0 / 135.0 / -0.03511111471388075 / 6.242118345863078 | [NPY](tensors/0001127.npy) |
| 1128 | `model.layers.11.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -173.0 / 135.0 / -0.03511111471388075 / 6.242118345863078 | [NPY](tensors/0001128.npy) |
| 1129 | `model.layers.11.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3125 / 0.9921875 / -0.08221435546875 / 0.5279735901162815 | [NPY](tensors/0001129.npy) |
| 1130 | `model.layers.11` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -496.0 / 540.0 / 0.35214674207899305 / 25.058767839137026 | [NPY](tensors/0001130.npy) |
| 1209 | `model.layers.11` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -262.0 / 348.0 / 0.5554623074001737 / 15.524789462055134 | [NPY](tensors/0001209.npy) |
| 1210 | `model.layers.11` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 315] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001210.npy) |
| 1211 | `model.layers.11` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0001211.npy) |
| 1212 | `model.layers.11` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0001212.npy) |
| 1213 | `model.layers.11` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0001213.npy) |
| 1214 | `model.layers.11` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1215 | `model.layers.11` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1216 | `model.layers.11` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1217 | `model.layers.11.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -262.0 / 348.0 / 0.5554623074001737 / 15.524789462055134 | [NPY](tensors/0001217.npy) |
| 1218 | `model.layers.11.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 88.0 / 0.0862988207075331 / 3.09846087408116 | [NPY](tensors/0001218.npy) |
| 1219 | `model.layers.11.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 88.0 / 0.0862988207075331 / 3.09846087408116 | [NPY](tensors/0001219.npy) |
| 1220 | `model.layers.11.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 315] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001220.npy) |
| 1221 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0001221.npy) |
| 1222 | `model.layers.11.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1223 | `model.layers.11.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1224 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0001224.npy) |
| 1225 | `model.layers.11.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0001225.npy) |
| 1226 | `model.layers.11.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1227 | `model.layers.11.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 88.0 / 0.0862988207075331 / 3.09846087408116 | [NPY](tensors/0001227.npy) |
| 1228 | `model.layers.11.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.90625 / 8.0625 / 0.04085614625364542 / 1.218940813939524 | [NPY](tensors/0001228.npy) |
| 1229 | `model.layers.11.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 88.0 / 0.0862988207075331 / 3.09846087408116 | [NPY](tensors/0001229.npy) |
| 1230 | `model.layers.11.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.0 / 37.75 / 0.16876019537448883 / 4.067316834797566 | [NPY](tensors/0001230.npy) |
| 1231 | `model.layers.11.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 88.0 / 0.0862988207075331 / 3.09846087408116 | [NPY](tensors/0001231.npy) |
| 1232 | `model.layers.11.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.25 / 6.375 / 0.05846930854022503 / 2.0702021489084617 | [NPY](tensors/0001232.npy) |
| 1233 | `model.layers.11.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.0625 / 6.34375 / 0.011278967838734388 / 1.3391693910779061 | [NPY](tensors/0001233.npy) |
| 1234 | `model.layers.11.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 101.0 / -0.05137338108486599 / 4.499663550633116 | [NPY](tensors/0001234.npy) |
| 1235 | `model.layers.11.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.25 / 101.0 / -0.05137338108486599 / 4.499663550633116 | [NPY](tensors/0001235.npy) |
| 1236 | `model.layers.11.self_attn` | 10 | `output[1]` | [1, 64, 1, 315] | torch.bfloat16 → float32 | 8.458300726488233e-11 / 0.828125 / 0.0029313296312511827 / 0.01409919643358982 | [NPY](tensors/0001236.npy) |
| 1237 | `model.layers.11.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -298.0 / 384.0 / 0.5041017320421007 / 17.91988559767365 | [NPY](tensors/0001237.npy) |
| 1238 | `model.layers.11.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5625 / 3.578125 / 0.007820106877221001 / 0.6538986137294052 | [NPY](tensors/0001238.npy) |
| 1239 | `model.layers.11.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5625 / 3.578125 / 0.007820106877221001 / 0.6538986137294052 | [NPY](tensors/0001239.npy) |
| 1240 | `model.layers.11.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.5625 / 3.578125 / 0.007820106877221001 / 0.6538986137294052 | [NPY](tensors/0001240.npy) |
| 1241 | `model.layers.11.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1242 | `model.layers.11.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1243 | `model.layers.11.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1244 | `model.layers.11.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -80.0 / 51.75 / 0.06078033314810859 / 3.647718144907612 | [NPY](tensors/0001244.npy) |
| 1245 | `model.layers.11.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 51.75 / 0.06078033314810859 / 3.647718144907612 | [NPY](tensors/0001245.npy) |
| 1246 | `model.layers.11.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.875 / 0.9375 / -0.055637359619140625 / 0.40431057604362847 | [NPY](tensors/0001246.npy) |
| 1247 | `model.layers.11` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -378.0 / 422.0 / 0.5650894165039062 / 19.7354391939569 | [NPY](tensors/0001247.npy) |
| 1326 | `model.layers.11` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -452.0 / 500.0 / 0.37520523071289064 / 20.236262120929105 | [NPY](tensors/0001326.npy) |
| 1327 | `model.layers.11` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 316] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001327.npy) |
| 1328 | `model.layers.11` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0001328.npy) |
| 1329 | `model.layers.11` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0001329.npy) |
| 1330 | `model.layers.11` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0001330.npy) |
| 1331 | `model.layers.11` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1332 | `model.layers.11` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1333 | `model.layers.11` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1334 | `model.layers.11.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -452.0 / 500.0 / 0.37520523071289064 / 20.236262120929105 | [NPY](tensors/0001334.npy) |
| 1335 | `model.layers.11.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 95.0 / 0.04997372163666619 / 3.460784278862752 | [NPY](tensors/0001335.npy) |
| 1336 | `model.layers.11.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 95.0 / 0.04997372163666619 / 3.460784278862752 | [NPY](tensors/0001336.npy) |
| 1337 | `model.layers.11.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 316] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001337.npy) |
| 1338 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0001338.npy) |
| 1339 | `model.layers.11.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1340 | `model.layers.11.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1341 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0001341.npy) |
| 1342 | `model.layers.11.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0001342.npy) |
| 1343 | `model.layers.11.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1344 | `model.layers.11.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 95.0 / 0.04997372163666619 / 3.460784278862752 | [NPY](tensors/0001344.npy) |
| 1345 | `model.layers.11.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.15625 / 7.4375 / 0.03974773269146681 / 1.1883816244849141 | [NPY](tensors/0001345.npy) |
| 1346 | `model.layers.11.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 95.0 / 0.04997372163666619 / 3.460784278862752 | [NPY](tensors/0001346.npy) |
| 1347 | `model.layers.11.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 36.25 / 0.12305888533592224 / 3.745516004641759 | [NPY](tensors/0001347.npy) |
| 1348 | `model.layers.11.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 95.0 / 0.04997372163666619 / 3.460784278862752 | [NPY](tensors/0001348.npy) |
| 1349 | `model.layers.11.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.9375 / 6.84375 / -0.01586073637008667 / 1.8459087783230221 | [NPY](tensors/0001349.npy) |
| 1350 | `model.layers.11.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5 / 5.96875 / 0.005001803394407034 / 1.29764849393936 | [NPY](tensors/0001350.npy) |
| 1351 | `model.layers.11.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.0 / 96.0 / 0.02272989484998915 / 4.706460706019872 | [NPY](tensors/0001351.npy) |
| 1352 | `model.layers.11.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -65.0 / 96.0 / 0.02272989484998915 / 4.706460706019872 | [NPY](tensors/0001352.npy) |
| 1353 | `model.layers.11.self_attn` | 11 | `output[1]` | [1, 64, 1, 316] | torch.bfloat16 → float32 | 1.3216094885137863e-12 / 0.90625 / 0.002967133020038069 / 0.015255415283085305 | [NPY](tensors/0001353.npy) |
| 1354 | `model.layers.11.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -406.0 / 516.0 / 0.3987345377604167 / 21.62857723703915 | [NPY](tensors/0001354.npy) |
| 1355 | `model.layers.11.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.875 / 2.90625 / -0.0030507279766930472 / 0.6197403070443541 | [NPY](tensors/0001355.npy) |
| 1356 | `model.layers.11.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.875 / 2.90625 / -0.0030507279766930472 / 0.6197403070443541 | [NPY](tensors/0001356.npy) |
| 1357 | `model.layers.11.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.875 / 2.90625 / -0.0030507279766930472 / 0.6197403070443541 | [NPY](tensors/0001357.npy) |
| 1358 | `model.layers.11.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1359 | `model.layers.11.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1360 | `model.layers.11.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1361 | `model.layers.11.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -214.0 / 160.0 / 0.07596891588634914 / 6.5249895444237875 | [NPY](tensors/0001361.npy) |
| 1362 | `model.layers.11.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -214.0 / 160.0 / 0.07596891588634914 / 6.5249895444237875 | [NPY](tensors/0001362.npy) |
| 1363 | `model.layers.11.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.34375 / 0.6484375 / -0.06646442413330078 / 0.40652981523958637 | [NPY](tensors/0001363.npy) |
| 1364 | `model.layers.11` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -620.0 / 592.0 / 0.4764242384168837 / 26.249453289030765 | [NPY](tensors/0001364.npy) |
| 1443 | `model.layers.11` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -362.0 / 466.0 / 0.2773464626736111 / 18.924413403068108 | [NPY](tensors/0001443.npy) |
| 1444 | `model.layers.11` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 317] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001444.npy) |
| 1445 | `model.layers.11` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0001445.npy) |
| 1446 | `model.layers.11` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0001446.npy) |
| 1447 | `model.layers.11` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0001447.npy) |
| 1448 | `model.layers.11` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1449 | `model.layers.11` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1450 | `model.layers.11` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1451 | `model.layers.11.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -362.0 / 466.0 / 0.2773464626736111 / 18.924413403068108 | [NPY](tensors/0001451.npy) |
| 1452 | `model.layers.11.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 88.0 / 0.037098262707392374 / 3.2089303464405914 | [NPY](tensors/0001452.npy) |
| 1453 | `model.layers.11.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 88.0 / 0.037098262707392374 / 3.2089303464405914 | [NPY](tensors/0001453.npy) |
| 1454 | `model.layers.11.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 317] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001454.npy) |
| 1455 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0001455.npy) |
| 1456 | `model.layers.11.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1457 | `model.layers.11.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1458 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0001458.npy) |
| 1459 | `model.layers.11.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0001459.npy) |
| 1460 | `model.layers.11.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1461 | `model.layers.11.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 88.0 / 0.037098262707392374 / 3.2089303464405914 | [NPY](tensors/0001461.npy) |
| 1462 | `model.layers.11.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.46875 / 8.625 / 0.05162325920537114 / 1.2251626808499743 | [NPY](tensors/0001462.npy) |
| 1463 | `model.layers.11.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 88.0 / 0.037098262707392374 / 3.2089303464405914 | [NPY](tensors/0001463.npy) |
| 1464 | `model.layers.11.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.5 / 40.0 / 0.1478595733642578 / 4.126262665136567 | [NPY](tensors/0001464.npy) |
| 1465 | `model.layers.11.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 88.0 / 0.037098262707392374 / 3.2089303464405914 | [NPY](tensors/0001465.npy) |
| 1466 | `model.layers.11.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.25 / 7.1875 / -0.04476689547300339 / 2.1747322433348018 | [NPY](tensors/0001466.npy) |
| 1467 | `model.layers.11.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 6.40625 / -0.015176313929259777 / 1.3704956667577848 | [NPY](tensors/0001467.npy) |
| 1468 | `model.layers.11.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 52.25 / 0.018387826283772786 / 4.243151748925795 | [NPY](tensors/0001468.npy) |
| 1469 | `model.layers.11.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.0 / 52.25 / 0.018387826283772786 / 4.243151748925795 | [NPY](tensors/0001469.npy) |
| 1470 | `model.layers.11.self_attn` | 12 | `output[1]` | [1, 64, 1, 317] | torch.bfloat16 → float32 | 2.2026824808563106e-12 / 0.9140625 / 0.0029924622643587627 / 0.0159213520351498 | [NPY](tensors/0001470.npy) |
| 1471 | `model.layers.11.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -310.0 / 482.0 / 0.29517652723524307 / 19.891156157031936 | [NPY](tensors/0001471.npy) |
| 1472 | `model.layers.11.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.21875 / 2.90625 / 9.138451682196723e-05 / 0.665590095042993 | [NPY](tensors/0001472.npy) |
| 1473 | `model.layers.11.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.21875 / 2.90625 / 9.138451682196723e-05 / 0.665590095042993 | [NPY](tensors/0001473.npy) |
| 1474 | `model.layers.11.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.21875 / 2.90625 / 9.138451682196723e-05 / 0.665590095042993 | [NPY](tensors/0001474.npy) |
| 1475 | `model.layers.11.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1476 | `model.layers.11.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1477 | `model.layers.11.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1478 | `model.layers.11.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -181.0 / 178.0 / 0.11821769873301188 / 7.364787179608972 | [NPY](tensors/0001478.npy) |
| 1479 | `model.layers.11.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -181.0 / 178.0 / 0.11821769873301188 / 7.364787179608972 | [NPY](tensors/0001479.npy) |
| 1480 | `model.layers.11.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0390625 / 0.91796875 / -0.1052093505859375 / 0.4162564764144576 | [NPY](tensors/0001480.npy) |
| 1481 | `model.layers.11` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -492.0 / 608.0 / 0.4125962151421441 / 25.07324626744072 | [NPY](tensors/0001481.npy) |
| 1560 | `model.layers.11` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -242.0 / 410.0 / 0.3110692342122396 / 17.246188213398746 | [NPY](tensors/0001560.npy) |
| 1561 | `model.layers.11` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 318] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001561.npy) |
| 1562 | `model.layers.11` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0001562.npy) |
| 1563 | `model.layers.11` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0001563.npy) |
| 1564 | `model.layers.11` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0001564.npy) |
| 1565 | `model.layers.11` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1566 | `model.layers.11` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1567 | `model.layers.11` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1568 | `model.layers.11.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -242.0 / 410.0 / 0.3110692342122396 / 17.246188213398746 | [NPY](tensors/0001568.npy) |
| 1569 | `model.layers.11.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.5 / 102.0 / 0.06434412797292073 / 3.126171765231101 | [NPY](tensors/0001569.npy) |
| 1570 | `model.layers.11.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.5 / 102.0 / 0.06434412797292073 / 3.126171765231101 | [NPY](tensors/0001570.npy) |
| 1571 | `model.layers.11.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 318] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001571.npy) |
| 1572 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0001572.npy) |
| 1573 | `model.layers.11.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1574 | `model.layers.11.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1575 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0001575.npy) |
| 1576 | `model.layers.11.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0001576.npy) |
| 1577 | `model.layers.11.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1578 | `model.layers.11.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.5 / 102.0 / 0.06434412797292073 / 3.126171765231101 | [NPY](tensors/0001578.npy) |
| 1579 | `model.layers.11.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.90625 / 9.9375 / 0.04839925089618191 / 1.2565312623458498 | [NPY](tensors/0001579.npy) |
| 1580 | `model.layers.11.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.5 / 102.0 / 0.06434412797292073 / 3.126171765231101 | [NPY](tensors/0001580.npy) |
| 1581 | `model.layers.11.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 37.25 / 0.1675010547041893 / 3.9895557586663184 | [NPY](tensors/0001581.npy) |
| 1582 | `model.layers.11.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.5 / 102.0 / 0.06434412797292073 / 3.126171765231101 | [NPY](tensors/0001582.npy) |
| 1583 | `model.layers.11.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.3125 / 7.6875 / -0.018900364637374878 / 2.2313227221693803 | [NPY](tensors/0001583.npy) |
| 1584 | `model.layers.11.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.53125 / 6.78125 / 0.01888756497646682 / 1.3378147994085088 | [NPY](tensors/0001584.npy) |
| 1585 | `model.layers.11.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.5 / 58.0 / -0.07700997789700827 / 3.917716482696802 | [NPY](tensors/0001585.npy) |
| 1586 | `model.layers.11.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.5 / 58.0 / -0.07700997789700827 / 3.917716482696802 | [NPY](tensors/0001586.npy) |
| 1587 | `model.layers.11.self_attn` | 13 | `output[1]` | [1, 64, 1, 318] | torch.bfloat16 → float32 | 6.991740519879386e-12 / 0.94140625 / 0.0029883057291498574 / 0.014181247094079624 | [NPY](tensors/0001587.npy) |
| 1588 | `model.layers.11.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -256.0 / 422.0 / 0.23435177273220487 / 18.629250240695008 | [NPY](tensors/0001588.npy) |
| 1589 | `model.layers.11.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.640625 / 2.9375 / -0.008242930306328668 / 0.6709815671737154 | [NPY](tensors/0001589.npy) |
| 1590 | `model.layers.11.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.640625 / 2.9375 / -0.008242930306328668 / 0.6709815671737154 | [NPY](tensors/0001590.npy) |
| 1591 | `model.layers.11.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.640625 / 2.9375 / -0.008242930306328668 / 0.6709815671737154 | [NPY](tensors/0001591.npy) |
| 1592 | `model.layers.11.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1593 | `model.layers.11.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1594 | `model.layers.11.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1595 | `model.layers.11.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -205.0 / 79.5 / 0.0732632663514879 / 5.683100911953742 | [NPY](tensors/0001595.npy) |
| 1596 | `model.layers.11.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -205.0 / 79.5 / 0.0732632663514879 / 5.683100911953742 | [NPY](tensors/0001596.npy) |
| 1597 | `model.layers.11.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0234375 / 0.875 / -0.037334442138671875 / 0.4015785692175465 | [NPY](tensors/0001597.npy) |
| 1598 | `model.layers.11` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -460.0 / 480.0 / 0.30789930555555556 / 21.818410701800758 | [NPY](tensors/0001598.npy) |
| 1677 | `model.layers.11` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -374.0 / 498.0 / 0.41025390625 / 20.160279361245717 | [NPY](tensors/0001677.npy) |
| 1678 | `model.layers.11` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 319] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001678.npy) |
| 1679 | `model.layers.11` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0001679.npy) |
| 1680 | `model.layers.11` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0001680.npy) |
| 1681 | `model.layers.11` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0001681.npy) |
| 1682 | `model.layers.11` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1683 | `model.layers.11` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1684 | `model.layers.11` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1685 | `model.layers.11.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -374.0 / 498.0 / 0.41025390625 / 20.160279361245717 | [NPY](tensors/0001685.npy) |
| 1686 | `model.layers.11.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 97.5 / 0.047594429386986624 / 3.3127600891216837 | [NPY](tensors/0001686.npy) |
| 1687 | `model.layers.11.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 97.5 / 0.047594429386986624 / 3.3127600891216837 | [NPY](tensors/0001687.npy) |
| 1688 | `model.layers.11.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 319] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001688.npy) |
| 1689 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0001689.npy) |
| 1690 | `model.layers.11.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1691 | `model.layers.11.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1692 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0001692.npy) |
| 1693 | `model.layers.11.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0001693.npy) |
| 1694 | `model.layers.11.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1695 | `model.layers.11.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 97.5 / 0.047594429386986624 / 3.3127600891216837 | [NPY](tensors/0001695.npy) |
| 1696 | `model.layers.11.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.9375 / 10.75 / 0.024265257641673088 / 1.2032492738883422 | [NPY](tensors/0001696.npy) |
| 1697 | `model.layers.11.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 97.5 / 0.047594429386986624 / 3.3127600891216837 | [NPY](tensors/0001697.npy) |
| 1698 | `model.layers.11.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.5 / 39.5 / 0.07752543687820435 / 3.825515264209109 | [NPY](tensors/0001698.npy) |
| 1699 | `model.layers.11.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 97.5 / 0.047594429386986624 / 3.3127600891216837 | [NPY](tensors/0001699.npy) |
| 1700 | `model.layers.11.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.0625 / 7.6875 / 0.0026707723736763 / 2.2978276035172662 | [NPY](tensors/0001700.npy) |
| 1701 | `model.layers.11.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.5 / 5.875 / 0.021245517767965794 / 1.449852622981929 | [NPY](tensors/0001701.npy) |
| 1702 | `model.layers.11.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 75.0 / 0.005204615328047011 / 4.103899309047325 | [NPY](tensors/0001702.npy) |
| 1703 | `model.layers.11.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.0 / 75.0 / 0.005204615328047011 / 4.103899309047325 | [NPY](tensors/0001703.npy) |
| 1704 | `model.layers.11.self_attn` | 14 | `output[1]` | [1, 64, 1, 319] | torch.bfloat16 → float32 | 7.247535904753022e-12 / 0.97265625 / 0.002892586901211123 / 0.016428775517443796 | [NPY](tensors/0001704.npy) |
| 1705 | `model.layers.11.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -360.0 / 492.0 / 0.41649966769748265 / 20.75615023886581 | [NPY](tensors/0001705.npy) |
| 1706 | `model.layers.11.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.65625 / 2.640625 / 0.004132992029190064 / 0.6455011393892846 | [NPY](tensors/0001706.npy) |
| 1707 | `model.layers.11.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.65625 / 2.640625 / 0.004132992029190064 / 0.6455011393892846 | [NPY](tensors/0001707.npy) |
| 1708 | `model.layers.11.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.65625 / 2.640625 / 0.004132992029190064 / 0.6455011393892846 | [NPY](tensors/0001708.npy) |
| 1709 | `model.layers.11.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1710 | `model.layers.11.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1711 | `model.layers.11.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1712 | `model.layers.11.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -201.0 / 141.0 / 0.03210199938880073 / 6.367860081966107 | [NPY](tensors/0001712.npy) |
| 1713 | `model.layers.11.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -201.0 / 141.0 / 0.03210199938880073 / 6.367860081966107 | [NPY](tensors/0001713.npy) |
| 1714 | `model.layers.11.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0625 / 1.0390625 / -0.08294677734375 / 0.47576508878247764 | [NPY](tensors/0001714.npy) |
| 1715 | `model.layers.11` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -560.0 / 540.0 / 0.44955902099609374 / 24.70027241288898 | [NPY](tensors/0001715.npy) |
| 1794 | `model.layers.11` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -400.0 / 540.0 / 0.15968560112847222 / 20.618901987222927 | [NPY](tensors/0001794.npy) |
| 1795 | `model.layers.11` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 320] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001795.npy) |
| 1796 | `model.layers.11` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0001796.npy) |
| 1797 | `model.layers.11` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0001797.npy) |
| 1798 | `model.layers.11` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0001798.npy) |
| 1799 | `model.layers.11` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1800 | `model.layers.11` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1801 | `model.layers.11` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1802 | `model.layers.11.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -400.0 / 540.0 / 0.15968560112847222 / 20.618901987222927 | [NPY](tensors/0001802.npy) |
| 1803 | `model.layers.11.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.0 / 101.0 / 0.026667541927761503 / 3.4144805938864247 | [NPY](tensors/0001803.npy) |
| 1804 | `model.layers.11.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.0 / 101.0 / 0.026667541927761503 / 3.4144805938864247 | [NPY](tensors/0001804.npy) |
| 1805 | `model.layers.11.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 320] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001805.npy) |
| 1806 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0001806.npy) |
| 1807 | `model.layers.11.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1808 | `model.layers.11.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1809 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0001809.npy) |
| 1810 | `model.layers.11.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0001810.npy) |
| 1811 | `model.layers.11.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1812 | `model.layers.11.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.0 / 101.0 / 0.026667541927761503 / 3.4144805938864247 | [NPY](tensors/0001812.npy) |
| 1813 | `model.layers.11.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.90625 / 10.8125 / 0.032792513840831816 / 1.2681503625729138 | [NPY](tensors/0001813.npy) |
| 1814 | `model.layers.11.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.0 / 101.0 / 0.026667541927761503 / 3.4144805938864247 | [NPY](tensors/0001814.npy) |
| 1815 | `model.layers.11.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.75 / 36.25 / 0.1382962092757225 / 3.85986968365828 | [NPY](tensors/0001815.npy) |
| 1816 | `model.layers.11.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -102.0 / 101.0 / 0.026667541927761503 / 3.4144805938864247 | [NPY](tensors/0001816.npy) |
| 1817 | `model.layers.11.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.8125 / 7.375 / 0.06979605555534363 / 2.269890747232916 | [NPY](tensors/0001817.npy) |
| 1818 | `model.layers.11.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.25 / 6.875 / 0.017181789269670844 / 1.4699089336230315 | [NPY](tensors/0001818.npy) |
| 1819 | `model.layers.11.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.015084386699729495 / 4.730848863642684 | [NPY](tensors/0001819.npy) |
| 1820 | `model.layers.11.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.015084386699729495 / 4.730848863642684 | [NPY](tensors/0001820.npy) |
| 1821 | `model.layers.11.self_attn` | 15 | `output[1]` | [1, 64, 1, 320] | torch.bfloat16 → float32 | 6.217248937900877e-14 / 0.96875 / 0.0029170991744065827 / 0.018124851694030403 | [NPY](tensors/0001821.npy) |
| 1822 | `model.layers.11.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 508.0 / 0.14392242431640626 / 20.304830643346907 | [NPY](tensors/0001822.npy) |
| 1823 | `model.layers.11.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.96875 / 3.296875 / 0.0007991843753390842 / 0.6578316906114494 | [NPY](tensors/0001823.npy) |
| 1824 | `model.layers.11.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.96875 / 3.296875 / 0.0007991843753390842 / 0.6578316906114494 | [NPY](tensors/0001824.npy) |
| 1825 | `model.layers.11.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.96875 / 3.296875 / 0.0007991843753390842 / 0.6578316906114494 | [NPY](tensors/0001825.npy) |
| 1826 | `model.layers.11.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1827 | `model.layers.11.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1828 | `model.layers.11.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1829 | `model.layers.11.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -184.0 / 144.0 / 0.02534488042195638 / 6.477368653187756 | [NPY](tensors/0001829.npy) |
| 1830 | `model.layers.11.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -184.0 / 144.0 / 0.02534488042195638 / 6.477368653187756 | [NPY](tensors/0001830.npy) |
| 1831 | `model.layers.11.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.328125 / 0.92578125 / -0.13070082664489746 / 0.5307016308122827 | [NPY](tensors/0001831.npy) |
| 1832 | `model.layers.11` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -496.0 / 632.0 / 0.16964772542317708 / 24.540250125978307 | [NPY](tensors/0001832.npy) |
| 1911 | `model.layers.11` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -330.0 / 484.0 / 0.5261410183376736 / 19.97713254310386 | [NPY](tensors/0001911.npy) |
| 1912 | `model.layers.11` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 321] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001912.npy) |
| 1913 | `model.layers.11` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0001913.npy) |
| 1914 | `model.layers.11` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0001914.npy) |
| 1915 | `model.layers.11` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0001915.npy) |
| 1916 | `model.layers.11` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1917 | `model.layers.11` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1918 | `model.layers.11` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1919 | `model.layers.11.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -330.0 / 484.0 / 0.5261410183376736 / 19.97713254310386 | [NPY](tensors/0001919.npy) |
| 1920 | `model.layers.11.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 105.5 / 0.05735682249069214 / 3.281123615214016 | [NPY](tensors/0001920.npy) |
| 1921 | `model.layers.11.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 105.5 / 0.05735682249069214 / 3.281123615214016 | [NPY](tensors/0001921.npy) |
| 1922 | `model.layers.11.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 321] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001922.npy) |
| 1923 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0001923.npy) |
| 1924 | `model.layers.11.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1925 | `model.layers.11.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1926 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0001926.npy) |
| 1927 | `model.layers.11.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0001927.npy) |
| 1928 | `model.layers.11.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1929 | `model.layers.11.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 105.5 / 0.05735682249069214 / 3.281123615214016 | [NPY](tensors/0001929.npy) |
| 1930 | `model.layers.11.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.3125 / 10.125 / 0.0485871066339314 / 1.2485822703052856 | [NPY](tensors/0001930.npy) |
| 1931 | `model.layers.11.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 105.5 / 0.05735682249069214 / 3.281123615214016 | [NPY](tensors/0001931.npy) |
| 1932 | `model.layers.11.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.25 / 38.0 / 0.1006823480129242 / 3.948991479777574 | [NPY](tensors/0001932.npy) |
| 1933 | `model.layers.11.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -86.5 / 105.5 / 0.05735682249069214 / 3.281123615214016 | [NPY](tensors/0001933.npy) |
| 1934 | `model.layers.11.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -10.0 / 7.09375 / 0.04494833946228027 / 2.5615613462560813 | [NPY](tensors/0001934.npy) |
| 1935 | `model.layers.11.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.40625 / 7.0 / 0.02493591606616974 / 1.5695484393466432 | [NPY](tensors/0001935.npy) |
| 1936 | `model.layers.11.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 77.0 / 0.05253921614752875 / 4.617245387613985 | [NPY](tensors/0001936.npy) |
| 1937 | `model.layers.11.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -84.5 / 77.0 / 0.05253921614752875 / 4.617245387613985 | [NPY](tensors/0001937.npy) |
| 1938 | `model.layers.11.self_attn` | 16 | `output[1]` | [1, 64, 1, 321] | torch.bfloat16 → float32 | 1.9095836023552692e-13 / 0.96484375 / 0.002896767790342499 / 0.017340095240305452 | [NPY](tensors/0001938.npy) |
| 1939 | `model.layers.11.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -276.0 / 444.0 / 0.578435770670573 / 19.88440391288556 | [NPY](tensors/0001939.npy) |
| 1940 | `model.layers.11.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5 / 4.25 / 0.023740880025757683 / 0.6710645805185295 | [NPY](tensors/0001940.npy) |
| 1941 | `model.layers.11.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5 / 4.25 / 0.023740880025757683 / 0.6710645805185295 | [NPY](tensors/0001941.npy) |
| 1942 | `model.layers.11.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.5 / 4.25 / 0.023740880025757683 / 0.6710645805185295 | [NPY](tensors/0001942.npy) |
| 1943 | `model.layers.11.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1944 | `model.layers.11.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1945 | `model.layers.11.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1946 | `model.layers.11.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -185.0 / 203.0 / 0.10412904421488443 / 7.262874129936873 | [NPY](tensors/0001946.npy) |
| 1947 | `model.layers.11.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -185.0 / 203.0 / 0.10412904421488443 / 7.262874129936873 | [NPY](tensors/0001947.npy) |
| 1948 | `model.layers.11.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.5390625 / 1.140625 / -0.10518836975097656 / 0.5930519971245386 | [NPY](tensors/0001948.npy) |
| 1949 | `model.layers.11` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -460.0 / 568.0 / 0.6807393391927083 / 24.66416748009555 | [NPY](tensors/0001949.npy) |
| 2028 | `model.layers.11` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -212.0 / 354.0 / 0.46265936957465276 / 15.504105224917339 | [NPY](tensors/0002028.npy) |
| 2029 | `model.layers.11` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002029.npy) |
| 2030 | `model.layers.11` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0002030.npy) |
| 2031 | `model.layers.11` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0002031.npy) |
| 2032 | `model.layers.11` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0002032.npy) |
| 2033 | `model.layers.11` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2034 | `model.layers.11` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2035 | `model.layers.11` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2036 | `model.layers.11.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -212.0 / 354.0 / 0.46265936957465276 / 15.504105224917339 | [NPY](tensors/0002036.npy) |
| 2037 | `model.layers.11.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 80.0 / 0.07273883157306248 / 2.9225965537253646 | [NPY](tensors/0002037.npy) |
| 2038 | `model.layers.11.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 80.0 / 0.07273883157306248 / 2.9225965537253646 | [NPY](tensors/0002038.npy) |
| 2039 | `model.layers.11.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002039.npy) |
| 2040 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0002040.npy) |
| 2041 | `model.layers.11.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2042 | `model.layers.11.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2043 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0002043.npy) |
| 2044 | `model.layers.11.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0002044.npy) |
| 2045 | `model.layers.11.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2046 | `model.layers.11.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 80.0 / 0.07273883157306248 / 2.9225965537253646 | [NPY](tensors/0002046.npy) |
| 2047 | `model.layers.11.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.625 / 9.4375 / 0.039362275041639805 / 1.232698954290934 | [NPY](tensors/0002047.npy) |
| 2048 | `model.layers.11.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 80.0 / 0.07273883157306248 / 2.9225965537253646 | [NPY](tensors/0002048.npy) |
| 2049 | `model.layers.11.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.5 / 41.25 / 0.07278325408697128 / 4.1269397937154935 | [NPY](tensors/0002049.npy) |
| 2050 | `model.layers.11.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 80.0 / 0.07273883157306248 / 2.9225965537253646 | [NPY](tensors/0002050.npy) |
| 2051 | `model.layers.11.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.59375 / 8.4375 / -0.04444935917854309 / 2.272888795584309 | [NPY](tensors/0002051.npy) |
| 2052 | `model.layers.11.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.15625 / 5.34375 / -0.008184192251064815 / 1.3493450392822617 | [NPY](tensors/0002052.npy) |
| 2053 | `model.layers.11.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 119.5 / 0.1066959778467814 / 5.3475913648734865 | [NPY](tensors/0002053.npy) |
| 2054 | `model.layers.11.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 119.5 / 0.1066959778467814 / 5.3475913648734865 | [NPY](tensors/0002054.npy) |
| 2055 | `model.layers.11.self_attn` | 17 | `output[1]` | [1, 64, 1, 322] | torch.bfloat16 → float32 | 1.8553691916167736e-10 / 0.85546875 / 0.0029272488692431045 / 0.012778873845040633 | [NPY](tensors/0002055.npy) |
| 2056 | `model.layers.11.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -314.0 / 412.0 / 0.5696248372395833 / 18.735500469254614 | [NPY](tensors/0002056.npy) |
| 2057 | `model.layers.11.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.34375 / 3.265625 / 0.008899536397722032 / 0.6381807142572584 | [NPY](tensors/0002057.npy) |
| 2058 | `model.layers.11.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.34375 / 3.265625 / 0.008899536397722032 / 0.6381807142572584 | [NPY](tensors/0002058.npy) |
| 2059 | `model.layers.11.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.34375 / 3.265625 / 0.008899536397722032 / 0.6381807142572584 | [NPY](tensors/0002059.npy) |
| 2060 | `model.layers.11.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2061 | `model.layers.11.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2062 | `model.layers.11.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2063 | `model.layers.11.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -97.5 / 112.0 / 0.06390785839822558 / 4.584104602696718 | [NPY](tensors/0002063.npy) |
| 2064 | `model.layers.11.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.5 / 112.0 / 0.06390785839822558 / 4.584104602696718 | [NPY](tensors/0002064.npy) |
| 2065 | `model.layers.11.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.89453125 / 0.9921875 / -0.03205108642578125 / 0.4030905962297602 | [NPY](tensors/0002065.npy) |
| 2066 | `model.layers.11` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -412.0 / 480.0 / 0.6337839762369791 / 21.459106235804295 | [NPY](tensors/0002066.npy) |
| 2145 | `model.layers.11` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -194.0 / 338.0 / 0.46842702229817706 / 15.782262910772076 | [NPY](tensors/0002145.npy) |
| 2146 | `model.layers.11` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002146.npy) |
| 2147 | `model.layers.11` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0002147.npy) |
| 2148 | `model.layers.11` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0002148.npy) |
| 2149 | `model.layers.11` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0002149.npy) |
| 2150 | `model.layers.11` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2151 | `model.layers.11` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2152 | `model.layers.11` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2153 | `model.layers.11.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -194.0 / 338.0 / 0.46842702229817706 / 15.782262910772076 | [NPY](tensors/0002153.npy) |
| 2154 | `model.layers.11.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 83.0 / 0.07827253209220039 / 2.8952950456482776 | [NPY](tensors/0002154.npy) |
| 2155 | `model.layers.11.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 83.0 / 0.07827253209220039 / 2.8952950456482776 | [NPY](tensors/0002155.npy) |
| 2156 | `model.layers.11.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002156.npy) |
| 2157 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0002157.npy) |
| 2158 | `model.layers.11.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2159 | `model.layers.11.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2160 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0002160.npy) |
| 2161 | `model.layers.11.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0002161.npy) |
| 2162 | `model.layers.11.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2163 | `model.layers.11.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 83.0 / 0.07827253209220039 / 2.8952950456482776 | [NPY](tensors/0002163.npy) |
| 2164 | `model.layers.11.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.5625 / 8.5625 / 0.05163200837523618 / 1.2173000025166143 | [NPY](tensors/0002164.npy) |
| 2165 | `model.layers.11.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 83.0 / 0.07827253209220039 / 2.8952950456482776 | [NPY](tensors/0002165.npy) |
| 2166 | `model.layers.11.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.75 / 37.5 / 0.12858232855796814 / 3.7719661244775606 | [NPY](tensors/0002166.npy) |
| 2167 | `model.layers.11.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -64.5 / 83.0 / 0.07827253209220039 / 2.8952950456482776 | [NPY](tensors/0002167.npy) |
| 2168 | `model.layers.11.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.21875 / 5.90625 / 0.08153606951236725 / 1.8279898982798746 | [NPY](tensors/0002168.npy) |
| 2169 | `model.layers.11.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.75 / 5.4375 / -0.022320830263197422 / 1.2415251995079268 | [NPY](tensors/0002169.npy) |
| 2170 | `model.layers.11.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 79.5 / 0.04735402133729723 / 4.044247239730224 | [NPY](tensors/0002170.npy) |
| 2171 | `model.layers.11.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 79.5 / 0.04735402133729723 / 4.044247239730224 | [NPY](tensors/0002171.npy) |
| 2172 | `model.layers.11.self_attn` | 18 | `output[1]` | [1, 64, 1, 323] | torch.bfloat16 → float32 | 5.32054400537163e-11 / 0.85546875 / 0.002864408847078947 / 0.011693948170705562 | [NPY](tensors/0002172.npy) |
| 2173 | `model.layers.11.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -227.0 / 356.0 / 0.5164243062337239 / 17.7350280566922 | [NPY](tensors/0002173.npy) |
| 2174 | `model.layers.11.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.640625 / 3.546875 / 0.004515324698554145 / 0.6912730026364319 | [NPY](tensors/0002174.npy) |
| 2175 | `model.layers.11.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.640625 / 3.546875 / 0.004515324698554145 / 0.6912730026364319 | [NPY](tensors/0002175.npy) |
| 2176 | `model.layers.11.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.640625 / 3.546875 / 0.004515324698554145 / 0.6912730026364319 | [NPY](tensors/0002176.npy) |
| 2177 | `model.layers.11.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2178 | `model.layers.11.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2179 | `model.layers.11.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2180 | `model.layers.11.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -131.0 / 108.5 / 0.07736385398440891 / 5.252022990648327 | [NPY](tensors/0002180.npy) |
| 2181 | `model.layers.11.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -131.0 / 108.5 / 0.07736385398440891 / 5.252022990648327 | [NPY](tensors/0002181.npy) |
| 2182 | `model.layers.11.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.5703125 / 1.4296875 / -0.037567138671875 / 0.6443153099083803 | [NPY](tensors/0002182.npy) |
| 2183 | `model.layers.11` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -358.0 / 440.0 / 0.5930575900607639 / 21.056914575937867 | [NPY](tensors/0002183.npy) |
| 2262 | `model.layers.11` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -402.0 / 492.0 / 0.7352019415961372 / 21.25982112249542 | [NPY](tensors/0002262.npy) |
| 2263 | `model.layers.11` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002263.npy) |
| 2264 | `model.layers.11` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0002264.npy) |
| 2265 | `model.layers.11` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0002265.npy) |
| 2266 | `model.layers.11` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0002266.npy) |
| 2267 | `model.layers.11` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2268 | `model.layers.11` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2269 | `model.layers.11` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2270 | `model.layers.11.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -402.0 / 492.0 / 0.7352019415961372 / 21.25982112249542 | [NPY](tensors/0002270.npy) |
| 2271 | `model.layers.11.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.0 / 108.5 / 0.07703411247995165 / 3.3652799834584366 | [NPY](tensors/0002271.npy) |
| 2272 | `model.layers.11.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.0 / 108.5 / 0.07703411247995165 / 3.3652799834584366 | [NPY](tensors/0002272.npy) |
| 2273 | `model.layers.11.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002273.npy) |
| 2274 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0002274.npy) |
| 2275 | `model.layers.11.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2276 | `model.layers.11.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2277 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0002277.npy) |
| 2278 | `model.layers.11.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0002278.npy) |
| 2279 | `model.layers.11.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2280 | `model.layers.11.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.0 / 108.5 / 0.07703411247995165 / 3.3652799834584366 | [NPY](tensors/0002280.npy) |
| 2281 | `model.layers.11.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.0 / 7.84375 / 0.048891212325543165 / 1.1733454162515813 | [NPY](tensors/0002281.npy) |
| 2282 | `model.layers.11.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.0 / 108.5 / 0.07703411247995165 / 3.3652799834584366 | [NPY](tensors/0002282.npy) |
| 2283 | `model.layers.11.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.125 / 36.0 / 0.16175086796283722 / 3.430454132786156 | [NPY](tensors/0002283.npy) |
| 2284 | `model.layers.11.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.0 / 108.5 / 0.07703411247995165 / 3.3652799834584366 | [NPY](tensors/0002284.npy) |
| 2285 | `model.layers.11.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.25 / 6.125 / 0.06600439548492432 / 1.9722202708682697 | [NPY](tensors/0002285.npy) |
| 2286 | `model.layers.11.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.0625 / 5.96875 / -0.00037241773679852486 / 1.2072702338670436 | [NPY](tensors/0002286.npy) |
| 2287 | `model.layers.11.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -76.0 / 120.0 / -0.0818919943438636 / 4.470814841345558 | [NPY](tensors/0002287.npy) |
| 2288 | `model.layers.11.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -76.0 / 120.0 / -0.0818919943438636 / 4.470814841345558 | [NPY](tensors/0002288.npy) |
| 2289 | `model.layers.11.self_attn` | 19 | `output[1]` | [1, 64, 1, 324] | torch.bfloat16 → float32 | 1.1880274541908875e-11 / 0.96875 / 0.0028526532003577154 / 0.013099884371063235 | [NPY](tensors/0002289.npy) |
| 2290 | `model.layers.11.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -282.0 / 416.0 / 0.6533135308159722 / 20.378891966437486 | [NPY](tensors/0002290.npy) |
| 2291 | `model.layers.11.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.53125 / 3.21875 / 0.010218099090788099 / 0.6904559904679088 | [NPY](tensors/0002291.npy) |
| 2292 | `model.layers.11.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.53125 / 3.21875 / 0.010218099090788099 / 0.6904559904679088 | [NPY](tensors/0002292.npy) |
| 2293 | `model.layers.11.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.53125 / 3.21875 / 0.010218099090788099 / 0.6904559904679088 | [NPY](tensors/0002293.npy) |
| 2294 | `model.layers.11.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2295 | `model.layers.11.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2296 | `model.layers.11.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2297 | `model.layers.11.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -153.0 / 191.0 / 0.08291596836513943 / 7.505228447497385 | [NPY](tensors/0002297.npy) |
| 2298 | `model.layers.11.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -153.0 / 191.0 / 0.08291596836513943 / 7.505228447497385 | [NPY](tensors/0002298.npy) |
| 2299 | `model.layers.11.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.546875 / 1.3203125 / -0.05725860595703125 / 0.5739367199033523 | [NPY](tensors/0002299.npy) |
| 2300 | `model.layers.11` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -436.0 / 608.0 / 0.7366800944010417 / 25.34199253535385 | [NPY](tensors/0002300.npy) |
| 2379 | `model.layers.11` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -336.0 / 422.0 / 0.34052954779730904 / 17.92229978424138 | [NPY](tensors/0002379.npy) |
| 2380 | `model.layers.11` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002380.npy) |
| 2381 | `model.layers.11` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0002381.npy) |
| 2382 | `model.layers.11` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0002382.npy) |
| 2383 | `model.layers.11` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0002383.npy) |
| 2384 | `model.layers.11` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2385 | `model.layers.11` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2386 | `model.layers.11` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2387 | `model.layers.11.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -336.0 / 422.0 / 0.34052954779730904 / 17.92229978424138 | [NPY](tensors/0002387.npy) |
| 2388 | `model.layers.11.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 90.5 / 0.040425537692175974 / 3.230523287357349 | [NPY](tensors/0002388.npy) |
| 2389 | `model.layers.11.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 90.5 / 0.040425537692175974 / 3.230523287357349 | [NPY](tensors/0002389.npy) |
| 2390 | `model.layers.11.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002390.npy) |
| 2391 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0002391.npy) |
| 2392 | `model.layers.11.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2393 | `model.layers.11.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2394 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0002394.npy) |
| 2395 | `model.layers.11.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0002395.npy) |
| 2396 | `model.layers.11.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2397 | `model.layers.11.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 90.5 / 0.040425537692175974 / 3.230523287357349 | [NPY](tensors/0002397.npy) |
| 2398 | `model.layers.11.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.6875 / 8.625 / 0.0344364398624748 / 1.2273723875588929 | [NPY](tensors/0002398.npy) |
| 2399 | `model.layers.11.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 90.5 / 0.040425537692175974 / 3.230523287357349 | [NPY](tensors/0002399.npy) |
| 2400 | `model.layers.11.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -37.0 / 46.25 / 0.21700383722782135 / 4.345904711375601 | [NPY](tensors/0002400.npy) |
| 2401 | `model.layers.11.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 90.5 / 0.040425537692175974 / 3.230523287357349 | [NPY](tensors/0002401.npy) |
| 2402 | `model.layers.11.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.9375 / 8.3125 / 0.027716293931007385 / 2.0732004015282066 | [NPY](tensors/0002402.npy) |
| 2403 | `model.layers.11.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.3125 / 7.5625 / -0.01856843417044729 / 1.3567609744337574 | [NPY](tensors/0002403.npy) |
| 2404 | `model.layers.11.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 78.5 / -0.010394854015774196 / 4.1649425449846245 | [NPY](tensors/0002404.npy) |
| 2405 | `model.layers.11.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 78.5 / -0.010394854015774196 / 4.1649425449846245 | [NPY](tensors/0002405.npy) |
| 2406 | `model.layers.11.self_attn` | 20 | `output[1]` | [1, 64, 1, 325] | torch.bfloat16 → float32 | 3.54702933691442e-11 / 0.9375 / 0.0029341311364574863 / 0.015364606342388773 | [NPY](tensors/0002406.npy) |
| 2407 | `model.layers.11.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -258.0 / 444.0 / 0.3299828423394097 / 18.7727783589722 | [NPY](tensors/0002407.npy) |
| 2408 | `model.layers.11.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.0 / 2.90625 / 0.0011490874820285373 / 0.6810634247073604 | [NPY](tensors/0002408.npy) |
| 2409 | `model.layers.11.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.0 / 2.90625 / 0.0011490874820285373 / 0.6810634247073604 | [NPY](tensors/0002409.npy) |
| 2410 | `model.layers.11.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.0 / 2.90625 / 0.0011490874820285373 / 0.6810634247073604 | [NPY](tensors/0002410.npy) |
| 2411 | `model.layers.11.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2412 | `model.layers.11.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2413 | `model.layers.11.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2414 | `model.layers.11.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -205.0 / 177.0 / -0.017960562970903184 / 7.007131152717249 | [NPY](tensors/0002414.npy) |
| 2415 | `model.layers.11.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -205.0 / 177.0 / -0.017960562970903184 / 7.007131152717249 | [NPY](tensors/0002415.npy) |
| 2416 | `model.layers.11.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.46875 / 0.68359375 / -0.14936065673828125 / 0.4695833060466113 | [NPY](tensors/0002416.npy) |
| 2417 | `model.layers.11` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -464.0 / 532.0 / 0.31338060167100695 / 23.434804183411043 | [NPY](tensors/0002417.npy) |
| 2496 | `model.layers.11` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -346.0 / 422.0 / 0.4100750393337674 / 19.71853982494535 | [NPY](tensors/0002496.npy) |
| 2497 | `model.layers.11` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002497.npy) |
| 2498 | `model.layers.11` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0002498.npy) |
| 2499 | `model.layers.11` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0002499.npy) |
| 2500 | `model.layers.11` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0002500.npy) |
| 2501 | `model.layers.11` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2502 | `model.layers.11` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2503 | `model.layers.11` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2504 | `model.layers.11.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -346.0 / 422.0 / 0.4100750393337674 / 19.71853982494535 | [NPY](tensors/0002504.npy) |
| 2505 | `model.layers.11.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.0 / 100.5 / 0.046614672078026664 / 3.2404263450976347 | [NPY](tensors/0002505.npy) |
| 2506 | `model.layers.11.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.0 / 100.5 / 0.046614672078026664 / 3.2404263450976347 | [NPY](tensors/0002506.npy) |
| 2507 | `model.layers.11.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002507.npy) |
| 2508 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0002508.npy) |
| 2509 | `model.layers.11.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2510 | `model.layers.11.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2511 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0002511.npy) |
| 2512 | `model.layers.11.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0002512.npy) |
| 2513 | `model.layers.11.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2514 | `model.layers.11.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.0 / 100.5 / 0.046614672078026664 / 3.2404263450976347 | [NPY](tensors/0002514.npy) |
| 2515 | `model.layers.11.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.1875 / 8.125 / 0.052352112834341824 / 1.2159401370944545 | [NPY](tensors/0002515.npy) |
| 2516 | `model.layers.11.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.0 / 100.5 / 0.046614672078026664 / 3.2404263450976347 | [NPY](tensors/0002516.npy) |
| 2517 | `model.layers.11.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.0 / 48.75 / 0.18469130992889404 / 4.266771223602132 | [NPY](tensors/0002517.npy) |
| 2518 | `model.layers.11.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.0 / 100.5 / 0.046614672078026664 / 3.2404263450976347 | [NPY](tensors/0002518.npy) |
| 2519 | `model.layers.11.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.78125 / 8.75 / 0.040056198835372925 / 2.2684398797450056 | [NPY](tensors/0002519.npy) |
| 2520 | `model.layers.11.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.34375 / 7.34375 / 0.0031138979829847813 / 1.4760211549147222 | [NPY](tensors/0002520.npy) |
| 2521 | `model.layers.11.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 88.0 / 0.007177963852882385 / 4.46331887208295 | [NPY](tensors/0002521.npy) |
| 2522 | `model.layers.11.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 88.0 / 0.007177963852882385 / 4.46331887208295 | [NPY](tensors/0002522.npy) |
| 2523 | `model.layers.11.self_attn` | 21 | `output[1]` | [1, 64, 1, 326] | torch.bfloat16 → float32 | 1.7053025658242404e-11 / 0.95703125 / 0.0028888373153812554 / 0.016579805269298347 | [NPY](tensors/0002523.npy) |
| 2524 | `model.layers.11.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -258.0 / 402.0 / 0.4179048326280382 / 20.345672374845144 | [NPY](tensors/0002524.npy) |
| 2525 | `model.layers.11.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.1875 / 4.96875 / 0.009826689296298556 / 0.686770969121017 | [NPY](tensors/0002525.npy) |
| 2526 | `model.layers.11.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.1875 / 4.96875 / 0.009826689296298556 / 0.686770969121017 | [NPY](tensors/0002526.npy) |
| 2527 | `model.layers.11.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.1875 / 4.96875 / 0.009826689296298556 / 0.686770969121017 | [NPY](tensors/0002527.npy) |
| 2528 | `model.layers.11.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2529 | `model.layers.11.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2530 | `model.layers.11.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2531 | `model.layers.11.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -225.0 / 260.0 / 0.06418981552124023 / 8.506658204922942 | [NPY](tensors/0002531.npy) |
| 2532 | `model.layers.11.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -225.0 / 260.0 / 0.06418981552124023 / 8.506658204922942 | [NPY](tensors/0002532.npy) |
| 2533 | `model.layers.11.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.15625 / -0.09645462036132812 / 0.5287107147317217 | [NPY](tensors/0002533.npy) |
| 2534 | `model.layers.11` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -484.0 / 636.0 / 0.4812016805013021 / 26.21609330788281 | [NPY](tensors/0002534.npy) |
| 2613 | `model.layers.11` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -276.0 / 430.0 / 0.7777877807617187 / 18.822138144371234 | [NPY](tensors/0002613.npy) |
| 2614 | `model.layers.11` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002614.npy) |
| 2615 | `model.layers.11` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0002615.npy) |
| 2616 | `model.layers.11` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0002616.npy) |
| 2617 | `model.layers.11` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0002617.npy) |
| 2618 | `model.layers.11` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2619 | `model.layers.11` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2620 | `model.layers.11` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2621 | `model.layers.11.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -276.0 / 430.0 / 0.7777877807617187 / 18.822138144371234 | [NPY](tensors/0002621.npy) |
| 2622 | `model.layers.11.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 107.0 / 0.09495075941085815 / 3.15076192017909 | [NPY](tensors/0002622.npy) |
| 2623 | `model.layers.11.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 107.0 / 0.09495075941085815 / 3.15076192017909 | [NPY](tensors/0002623.npy) |
| 2624 | `model.layers.11.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002624.npy) |
| 2625 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0002625.npy) |
| 2626 | `model.layers.11.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2627 | `model.layers.11.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2628 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0002628.npy) |
| 2629 | `model.layers.11.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0002629.npy) |
| 2630 | `model.layers.11.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2631 | `model.layers.11.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 107.0 / 0.09495075941085815 / 3.15076192017909 | [NPY](tensors/0002631.npy) |
| 2632 | `model.layers.11.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.1875 / 8.1875 / 0.05593694299750496 / 1.2021414320836343 | [NPY](tensors/0002632.npy) |
| 2633 | `model.layers.11.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 107.0 / 0.09495075941085815 / 3.15076192017909 | [NPY](tensors/0002633.npy) |
| 2634 | `model.layers.11.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.25 / 38.75 / 0.17817559838294983 / 3.775828360581785 | [NPY](tensors/0002634.npy) |
| 2635 | `model.layers.11.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -77.0 / 107.0 / 0.09495075941085815 / 3.15076192017909 | [NPY](tensors/0002635.npy) |
| 2636 | `model.layers.11.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.875 / 8.1875 / 0.057937443256378174 / 2.267344239725003 | [NPY](tensors/0002636.npy) |
| 2637 | `model.layers.11.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.8125 / 6.46875 / -0.0018854618538171053 / 1.3120068210727875 | [NPY](tensors/0002637.npy) |
| 2638 | `model.layers.11.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 108.0 / -0.003141793277528551 / 4.395595339118916 | [NPY](tensors/0002638.npy) |
| 2639 | `model.layers.11.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 108.0 / -0.003141793277528551 / 4.395595339118916 | [NPY](tensors/0002639.npy) |
| 2640 | `model.layers.11.self_attn` | 22 | `output[1]` | [1, 64, 1, 327] | torch.bfloat16 → float32 | 2.1373125491663814e-11 / 0.93359375 / 0.0028699265956943117 / 0.013137032906612129 | [NPY](tensors/0002640.npy) |
| 2641 | `model.layers.11.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -168.0 / 382.0 / 0.7742796156141493 / 18.934477255122204 | [NPY](tensors/0002641.npy) |
| 2642 | `model.layers.11.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.703125 / 2.765625 / 0.023655033111572264 / 0.7413688171005688 | [NPY](tensors/0002642.npy) |
| 2643 | `model.layers.11.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.703125 / 2.765625 / 0.023655033111572264 / 0.7413688171005688 | [NPY](tensors/0002643.npy) |
| 2644 | `model.layers.11.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.703125 / 2.765625 / 0.023655033111572264 / 0.7413688171005688 | [NPY](tensors/0002644.npy) |
| 2645 | `model.layers.11.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2646 | `model.layers.11.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2647 | `model.layers.11.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2648 | `model.layers.11.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -186.0 / 171.0 / 0.06165440811051263 / 7.554654499189114 | [NPY](tensors/0002648.npy) |
| 2649 | `model.layers.11.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -186.0 / 171.0 / 0.06165440811051263 / 7.554654499189114 | [NPY](tensors/0002649.npy) |
| 2650 | `model.layers.11.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3984375 / 1.2421875 / -0.032611846923828125 / 0.5438473184390457 | [NPY](tensors/0002650.npy) |
| 2651 | `model.layers.11` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -354.0 / 552.0 / 0.8352305094401041 / 23.62909943409249 | [NPY](tensors/0002651.npy) |
| 2730 | `model.layers.11` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -380.0 / 400.0 / 0.9303448147243923 / 21.452256033550267 | [NPY](tensors/0002730.npy) |
| 2731 | `model.layers.11` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002731.npy) |
| 2732 | `model.layers.11` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0002732.npy) |
| 2733 | `model.layers.11` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0002733.npy) |
| 2734 | `model.layers.11` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0002734.npy) |
| 2735 | `model.layers.11` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2736 | `model.layers.11` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2737 | `model.layers.11` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2738 | `model.layers.11.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -380.0 / 400.0 / 0.9303448147243923 / 21.452256033550267 | [NPY](tensors/0002738.npy) |
| 2739 | `model.layers.11.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 87.5 / 0.09168030420939127 / 2.9977537076474974 | [NPY](tensors/0002739.npy) |
| 2740 | `model.layers.11.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 87.5 / 0.09168030420939127 / 2.9977537076474974 | [NPY](tensors/0002740.npy) |
| 2741 | `model.layers.11.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002741.npy) |
| 2742 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0002742.npy) |
| 2743 | `model.layers.11.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2744 | `model.layers.11.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2745 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0002745.npy) |
| 2746 | `model.layers.11.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0002746.npy) |
| 2747 | `model.layers.11.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2748 | `model.layers.11.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 87.5 / 0.09168030420939127 / 2.9977537076474974 | [NPY](tensors/0002748.npy) |
| 2749 | `model.layers.11.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.40625 / 10.6875 / 0.05286849639378488 / 1.2889759057754995 | [NPY](tensors/0002749.npy) |
| 2750 | `model.layers.11.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 87.5 / 0.09168030420939127 / 2.9977537076474974 | [NPY](tensors/0002750.npy) |
| 2751 | `model.layers.11.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.25 / 36.75 / 0.04382467269897461 / 3.831097628581113 | [NPY](tensors/0002751.npy) |
| 2752 | `model.layers.11.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 87.5 / 0.09168030420939127 / 2.9977537076474974 | [NPY](tensors/0002752.npy) |
| 2753 | `model.layers.11.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.71875 / 8.75 / -0.002889089286327362 / 2.1708620176016713 | [NPY](tensors/0002753.npy) |
| 2754 | `model.layers.11.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.71875 / 6.21875 / -0.022275271359831095 / 1.2323606003555212 | [NPY](tensors/0002754.npy) |
| 2755 | `model.layers.11.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.25 / 136.0 / 0.01573642094930013 / 4.01400026340263 | [NPY](tensors/0002755.npy) |
| 2756 | `model.layers.11.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -57.25 / 136.0 / 0.01573642094930013 / 4.01400026340263 | [NPY](tensors/0002756.npy) |
| 2757 | `model.layers.11.self_attn` | 23 | `output[1]` | [1, 64, 1, 328] | torch.bfloat16 → float32 | 1.4915713109076023e-10 / 0.87890625 / 0.002483266862535719 / 0.014651243001428376 | [NPY](tensors/0002757.npy) |
| 2758 | `model.layers.11.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -244.0 / 342.0 / 0.944932386610243 / 20.914549622100733 | [NPY](tensors/0002758.npy) |
| 2759 | `model.layers.11.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.46875 / 5.375 / 0.023948762151930068 / 0.760849969977936 | [NPY](tensors/0002759.npy) |
| 2760 | `model.layers.11.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.46875 / 5.375 / 0.023948762151930068 / 0.760849969977936 | [NPY](tensors/0002760.npy) |
| 2761 | `model.layers.11.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.46875 / 5.375 / 0.023948762151930068 / 0.760849969977936 | [NPY](tensors/0002761.npy) |
| 2762 | `model.layers.11.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2763 | `model.layers.11.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2764 | `model.layers.11.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2765 | `model.layers.11.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -166.0 / 177.0 / 0.16534294287363688 / 7.357747165091684 | [NPY](tensors/0002765.npy) |
| 2766 | `model.layers.11.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -166.0 / 177.0 / 0.16534294287363688 / 7.357747165091684 | [NPY](tensors/0002766.npy) |
| 2767 | `model.layers.11.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.7734375 / 1.6484375 / -0.12734222412109375 / 0.6617011542198208 | [NPY](tensors/0002767.npy) |
| 2768 | `model.layers.11` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -410.0 / 520.0 / 1.1108873155381944 / 25.43191174902445 | [NPY](tensors/0002768.npy) |
| 2847 | `model.layers.11` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -380.0 / 496.0 / 0.8104632907443576 / 23.932922622076813 | [NPY](tensors/0002847.npy) |
| 2848 | `model.layers.11` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002848.npy) |
| 2849 | `model.layers.11` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0002849.npy) |
| 2850 | `model.layers.11` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0002850.npy) |
| 2851 | `model.layers.11` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0002851.npy) |
| 2852 | `model.layers.11` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2853 | `model.layers.11` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2854 | `model.layers.11` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2855 | `model.layers.11.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -380.0 / 496.0 / 0.8104632907443576 / 23.932922622076813 | [NPY](tensors/0002855.npy) |
| 2856 | `model.layers.11.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.5 / 97.0 / 0.07890267372131347 / 3.004527782786843 | [NPY](tensors/0002856.npy) |
| 2857 | `model.layers.11.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.5 / 97.0 / 0.07890267372131347 / 3.004527782786843 | [NPY](tensors/0002857.npy) |
| 2858 | `model.layers.11.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002858.npy) |
| 2859 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0002859.npy) |
| 2860 | `model.layers.11.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2861 | `model.layers.11.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2862 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0002862.npy) |
| 2863 | `model.layers.11.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0002863.npy) |
| 2864 | `model.layers.11.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2865 | `model.layers.11.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.5 / 97.0 / 0.07890267372131347 / 3.004527782786843 | [NPY](tensors/0002865.npy) |
| 2866 | `model.layers.11.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.90625 / 10.5625 / 0.02734872791916132 / 1.3183321626619198 | [NPY](tensors/0002866.npy) |
| 2867 | `model.layers.11.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.5 / 97.0 / 0.07890267372131347 / 3.004527782786843 | [NPY](tensors/0002867.npy) |
| 2868 | `model.layers.11.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.125 / 37.75 / 0.008016906678676605 / 3.7416861853734638 | [NPY](tensors/0002868.npy) |
| 2869 | `model.layers.11.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -83.5 / 97.0 / 0.07890267372131347 / 3.004527782786843 | [NPY](tensors/0002869.npy) |
| 2870 | `model.layers.11.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.15625 / 8.625 / 0.035398781299591064 / 2.2065837690511567 | [NPY](tensors/0002870.npy) |
| 2871 | `model.layers.11.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.46875 / 6.5625 / -0.02527819713577628 / 1.2814717300049083 | [NPY](tensors/0002871.npy) |
| 2872 | `model.layers.11.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 103.5 / 0.027998241616619957 / 3.588779425674537 | [NPY](tensors/0002872.npy) |
| 2873 | `model.layers.11.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.25 / 103.5 / 0.027998241616619957 / 3.588779425674537 | [NPY](tensors/0002873.npy) |
| 2874 | `model.layers.11.self_attn` | 24 | `output[1]` | [1, 64, 1, 329] | torch.bfloat16 → float32 | 4.092726157978177e-11 / 0.87890625 / 0.0024576578425533923 / 0.016868130241424344 | [NPY](tensors/0002874.npy) |
| 2875 | `model.layers.11.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -276.0 / 450.0 / 0.8390423244900174 / 23.647142675405217 | [NPY](tensors/0002875.npy) |
| 2876 | `model.layers.11.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.125 / 4.34375 / 0.013738062646653917 / 0.7303642675303097 | [NPY](tensors/0002876.npy) |
| 2877 | `model.layers.11.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.125 / 4.34375 / 0.013738062646653917 / 0.7303642675303097 | [NPY](tensors/0002877.npy) |
| 2878 | `model.layers.11.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.125 / 4.34375 / 0.013738062646653917 / 0.7303642675303097 | [NPY](tensors/0002878.npy) |
| 2879 | `model.layers.11.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2880 | `model.layers.11.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2881 | `model.layers.11.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2882 | `model.layers.11.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -183.0 / 185.0 / 0.05764473809136285 / 7.552235132081618 | [NPY](tensors/0002882.npy) |
| 2883 | `model.layers.11.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -183.0 / 185.0 / 0.05764473809136285 / 7.552235132081618 | [NPY](tensors/0002883.npy) |
| 2884 | `model.layers.11.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.171875 / 1.71875 / -0.16228199005126953 / 0.7199891333409365 | [NPY](tensors/0002884.npy) |
| 2885 | `model.layers.11` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -460.0 / 636.0 / 0.8964603000217014 / 28.407319823168848 | [NPY](tensors/0002885.npy) |
| 2964 | `model.layers.11` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -362.0 / 588.0 / 0.8389339870876736 / 26.432582786983403 | [NPY](tensors/0002964.npy) |
| 2965 | `model.layers.11` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 330] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002965.npy) |
| 2966 | `model.layers.11` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0002966.npy) |
| 2967 | `model.layers.11` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0002967.npy) |
| 2968 | `model.layers.11` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0002968.npy) |
| 2969 | `model.layers.11` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2970 | `model.layers.11` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2971 | `model.layers.11` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2972 | `model.layers.11.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -362.0 / 588.0 / 0.8389339870876736 / 26.432582786983403 | [NPY](tensors/0002972.npy) |
| 2973 | `model.layers.11.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 104.0 / 0.08021009299490187 / 2.9749330004928334 | [NPY](tensors/0002973.npy) |
| 2974 | `model.layers.11.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 104.0 / 0.08021009299490187 / 2.9749330004928334 | [NPY](tensors/0002974.npy) |
| 2975 | `model.layers.11.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 330] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002975.npy) |
| 2976 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0002976.npy) |
| 2977 | `model.layers.11.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2978 | `model.layers.11.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2979 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0002979.npy) |
| 2980 | `model.layers.11.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0002980.npy) |
| 2981 | `model.layers.11.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2982 | `model.layers.11.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 104.0 / 0.08021009299490187 / 2.9749330004928334 | [NPY](tensors/0002982.npy) |
| 2983 | `model.layers.11.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5625 / 10.8125 / 0.02607506886124611 / 1.3600103370011867 | [NPY](tensors/0002983.npy) |
| 2984 | `model.layers.11.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 104.0 / 0.08021009299490187 / 2.9749330004928334 | [NPY](tensors/0002984.npy) |
| 2985 | `model.layers.11.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.75 / 37.0 / 0.022864580154418945 / 3.6078324515702445 | [NPY](tensors/0002985.npy) |
| 2986 | `model.layers.11.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -72.0 / 104.0 / 0.08021009299490187 / 2.9749330004928334 | [NPY](tensors/0002986.npy) |
| 2987 | `model.layers.11.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.46875 / 10.6875 / -0.11931651830673218 / 2.7403282330934404 | [NPY](tensors/0002987.npy) |
| 2988 | `model.layers.11.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.75 / 8.75 / -0.04269274917896837 / 1.5552518079925723 | [NPY](tensors/0002988.npy) |
| 2989 | `model.layers.11.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.625 / 60.75 / 0.06494170294867621 / 4.330233805154307 | [NPY](tensors/0002989.npy) |
| 2990 | `model.layers.11.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -21.625 / 60.75 / 0.06494170294867621 / 4.330233805154307 | [NPY](tensors/0002990.npy) |
| 2991 | `model.layers.11.self_attn` | 25 | `output[1]` | [1, 64, 1, 330] | torch.bfloat16 → float32 | 2.1645973902195692e-10 / 0.77734375 / 0.00277279228910717 / 0.015547126499352453 | [NPY](tensors/0002991.npy) |
| 2992 | `model.layers.11.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -348.0 / 576.0 / 0.9029437594943577 / 27.51885912805224 | [NPY](tensors/0002992.npy) |
| 2993 | `model.layers.11.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.03125 / 4.0 / 0.016084673669603138 / 0.7434767066402211 | [NPY](tensors/0002993.npy) |
| 2994 | `model.layers.11.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.03125 / 4.0 / 0.016084673669603138 / 0.7434767066402211 | [NPY](tensors/0002994.npy) |
| 2995 | `model.layers.11.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.03125 / 4.0 / 0.016084673669603138 / 0.7434767066402211 | [NPY](tensors/0002995.npy) |
| 2996 | `model.layers.11.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2997 | `model.layers.11.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2998 | `model.layers.11.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2999 | `model.layers.11.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -133.0 / 203.0 / 0.22854971885681152 / 7.629548691607309 | [NPY](tensors/0002999.npy) |
| 3000 | `model.layers.11.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -133.0 / 203.0 / 0.22854971885681152 / 7.629548691607309 | [NPY](tensors/0003000.npy) |
| 3001 | `model.layers.11.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.109375 / 0.98828125 / -0.13135528564453125 / 0.56967531654554 | [NPY](tensors/0003001.npy) |
| 3002 | `model.layers.11` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -480.0 / 740.0 / 1.132456292046441 / 32.472948215853535 | [NPY](tensors/0003002.npy) |
| 3081 | `model.layers.11` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -145.0 / 292.0 / 0.73623046875 / 15.599016455171085 | [NPY](tensors/0003081.npy) |
| 3082 | `model.layers.11` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 331] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003082.npy) |
| 3083 | `model.layers.11` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0003083.npy) |
| 3084 | `model.layers.11` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0003084.npy) |
| 3085 | `model.layers.11` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0003085.npy) |
| 3086 | `model.layers.11` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3087 | `model.layers.11` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3088 | `model.layers.11` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3089 | `model.layers.11.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -145.0 / 292.0 / 0.73623046875 / 15.599016455171085 | [NPY](tensors/0003089.npy) |
| 3090 | `model.layers.11.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 87.5 / 0.11033915943569607 / 2.797116399627227 | [NPY](tensors/0003090.npy) |
| 3091 | `model.layers.11.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 87.5 / 0.11033915943569607 / 2.797116399627227 | [NPY](tensors/0003091.npy) |
| 3092 | `model.layers.11.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 331] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003092.npy) |
| 3093 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0003093.npy) |
| 3094 | `model.layers.11.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3095 | `model.layers.11.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3096 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0003096.npy) |
| 3097 | `model.layers.11.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0003097.npy) |
| 3098 | `model.layers.11.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3099 | `model.layers.11.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 87.5 / 0.11033915943569607 / 2.797116399627227 | [NPY](tensors/0003099.npy) |
| 3100 | `model.layers.11.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.8125 / 10.4375 / 0.02750333317089826 / 1.3876099208174386 | [NPY](tensors/0003100.npy) |
| 3101 | `model.layers.11.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 87.5 / 0.11033915943569607 / 2.797116399627227 | [NPY](tensors/0003101.npy) |
| 3102 | `model.layers.11.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.5 / 38.25 / 0.07739093899726868 / 4.119837578787669 | [NPY](tensors/0003102.npy) |
| 3103 | `model.layers.11.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 87.5 / 0.11033915943569607 / 2.797116399627227 | [NPY](tensors/0003103.npy) |
| 3104 | `model.layers.11.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.125 / 6.875 / 0.07555270195007324 / 2.4453884083143467 | [NPY](tensors/0003104.npy) |
| 3105 | `model.layers.11.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.59375 / 6.1875 / -0.027180724136997014 / 1.4012231501781522 | [NPY](tensors/0003105.npy) |
| 3106 | `model.layers.11.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 85.0 / 0.13719945351282756 / 3.9412795375879766 | [NPY](tensors/0003106.npy) |
| 3107 | `model.layers.11.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.0 / 85.0 / 0.13719945351282756 / 3.9412795375879766 | [NPY](tensors/0003107.npy) |
| 3108 | `model.layers.11.self_attn` | 26 | `output[1]` | [1, 64, 1, 331] | torch.bfloat16 → float32 | 9.74978320300579e-10 / 0.80859375 / 0.0027168272894423874 / 0.013823194842900012 | [NPY](tensors/0003108.npy) |
| 3109 | `model.layers.11.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -174.0 / 376.0 / 0.8736654493543837 / 17.724941268775115 | [NPY](tensors/0003109.npy) |
| 3110 | `model.layers.11.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.390625 / 2.984375 / 0.025698110792371963 / 0.7202963502722212 | [NPY](tensors/0003110.npy) |
| 3111 | `model.layers.11.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.390625 / 2.984375 / 0.025698110792371963 / 0.7202963502722212 | [NPY](tensors/0003111.npy) |
| 3112 | `model.layers.11.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.390625 / 2.984375 / 0.025698110792371963 / 0.7202963502722212 | [NPY](tensors/0003112.npy) |
| 3113 | `model.layers.11.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3114 | `model.layers.11.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3115 | `model.layers.11.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3116 | `model.layers.11.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -117.0 / 61.75 / 0.01359620624118381 / 4.717388899804566 | [NPY](tensors/0003116.npy) |
| 3117 | `model.layers.11.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -117.0 / 61.75 / 0.01359620624118381 / 4.717388899804566 | [NPY](tensors/0003117.npy) |
| 3118 | `model.layers.11.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.4765625 / 1.2890625 / -0.08851969242095947 / 0.6172569215689852 | [NPY](tensors/0003118.npy) |
| 3119 | `model.layers.11` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -292.0 / 394.0 / 0.8869316948784722 / 19.87671903150262 | [NPY](tensors/0003119.npy) |
| 3198 | `model.layers.11` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -438.0 / 600.0 / 0.7470252143012153 / 25.339487725401735 | [NPY](tensors/0003198.npy) |
| 3199 | `model.layers.11` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 332] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003199.npy) |
| 3200 | `model.layers.11` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0003200.npy) |
| 3201 | `model.layers.11` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0003201.npy) |
| 3202 | `model.layers.11` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0003202.npy) |
| 3203 | `model.layers.11` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3204 | `model.layers.11` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3205 | `model.layers.11` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3206 | `model.layers.11.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -438.0 / 600.0 / 0.7470252143012153 / 25.339487725401735 | [NPY](tensors/0003206.npy) |
| 3207 | `model.layers.11.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 111.0 / 0.06682477162943946 / 3.163746424451344 | [NPY](tensors/0003207.npy) |
| 3208 | `model.layers.11.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 111.0 / 0.06682477162943946 / 3.163746424451344 | [NPY](tensors/0003208.npy) |
| 3209 | `model.layers.11.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 332] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003209.npy) |
| 3210 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0003210.npy) |
| 3211 | `model.layers.11.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3212 | `model.layers.11.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3213 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0003213.npy) |
| 3214 | `model.layers.11.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0003214.npy) |
| 3215 | `model.layers.11.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3216 | `model.layers.11.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 111.0 / 0.06682477162943946 / 3.163746424451344 | [NPY](tensors/0003216.npy) |
| 3217 | `model.layers.11.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.84375 / 9.375 / 0.007634767331182957 / 1.3045617103262237 | [NPY](tensors/0003217.npy) |
| 3218 | `model.layers.11.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 111.0 / 0.06682477162943946 / 3.163746424451344 | [NPY](tensors/0003218.npy) |
| 3219 | `model.layers.11.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.0 / 30.0 / -0.04519838094711304 / 3.422818320012213 | [NPY](tensors/0003219.npy) |
| 3220 | `model.layers.11.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -90.5 / 111.0 / 0.06682477162943946 / 3.163746424451344 | [NPY](tensors/0003220.npy) |
| 3221 | `model.layers.11.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -9.4375 / 9.1875 / 0.011774510145187378 / 2.6867076119019773 | [NPY](tensors/0003221.npy) |
| 3222 | `model.layers.11.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.3125 / 7.90625 / -0.01487588370218873 / 1.4488735776319683 | [NPY](tensors/0003222.npy) |
| 3223 | `model.layers.11.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.5 / 68.5 / -0.09074568880928888 / 4.053611120917404 | [NPY](tensors/0003223.npy) |
| 3224 | `model.layers.11.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.5 / 68.5 / -0.09074568880928888 / 4.053611120917404 | [NPY](tensors/0003224.npy) |
| 3225 | `model.layers.11.self_attn` | 27 | `output[1]` | [1, 64, 1, 332] | torch.bfloat16 → float32 | 5.6843418860808015e-11 / 0.9140625 / 0.00250609107847394 / 0.015322645569848409 | [NPY](tensors/0003225.npy) |
| 3226 | `model.layers.11.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -370.0 / 510.0 / 0.6542728000217014 / 24.767154028371014 | [NPY](tensors/0003226.npy) |
| 3227 | `model.layers.11.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.25 / 3.5 / 0.007278038395775689 / 0.7594408261584701 | [NPY](tensors/0003227.npy) |
| 3228 | `model.layers.11.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.25 / 3.5 / 0.007278038395775689 / 0.7594408261584701 | [NPY](tensors/0003228.npy) |
| 3229 | `model.layers.11.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.25 / 3.5 / 0.007278038395775689 / 0.7594408261584701 | [NPY](tensors/0003229.npy) |
| 3230 | `model.layers.11.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3231 | `model.layers.11.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3232 | `model.layers.11.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3233 | `model.layers.11.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -260.0 / 232.0 / 0.1636023097568088 / 9.111555503966846 | [NPY](tensors/0003233.npy) |
| 3234 | `model.layers.11.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -260.0 / 232.0 / 0.1636023097568088 / 9.111555503966846 | [NPY](tensors/0003234.npy) |
| 3235 | `model.layers.11.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.09375 / 1.25 / -0.11194992065429688 / 0.6735555637342188 | [NPY](tensors/0003235.npy) |
| 3236 | `model.layers.11` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -632.0 / 744.0 / 0.8173536512586805 / 31.20836704048943 | [NPY](tensors/0003236.npy) |
| 3315 | `model.layers.11` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -392.0 / 572.0 / 0.43354220920138886 / 24.05310515359864 | [NPY](tensors/0003315.npy) |
| 3316 | `model.layers.11` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 333] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003316.npy) |
| 3317 | `model.layers.11` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0003317.npy) |
| 3318 | `model.layers.11` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0003318.npy) |
| 3319 | `model.layers.11` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0003319.npy) |
| 3320 | `model.layers.11` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3321 | `model.layers.11` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3322 | `model.layers.11` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3323 | `model.layers.11.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -392.0 / 572.0 / 0.43354220920138886 / 24.05310515359864 | [NPY](tensors/0003323.npy) |
| 3324 | `model.layers.11.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 111.5 / 0.055610791842142744 / 3.1159449570093987 | [NPY](tensors/0003324.npy) |
| 3325 | `model.layers.11.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 111.5 / 0.055610791842142744 / 3.1159449570093987 | [NPY](tensors/0003325.npy) |
| 3326 | `model.layers.11.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 333] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003326.npy) |
| 3327 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0003327.npy) |
| 3328 | `model.layers.11.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3329 | `model.layers.11.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3330 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0003330.npy) |
| 3331 | `model.layers.11.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0003331.npy) |
| 3332 | `model.layers.11.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3333 | `model.layers.11.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 111.5 / 0.055610791842142744 / 3.1159449570093987 | [NPY](tensors/0003333.npy) |
| 3334 | `model.layers.11.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.90625 / 10.3125 / 0.019038744270801544 / 1.260002436193543 | [NPY](tensors/0003334.npy) |
| 3335 | `model.layers.11.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 111.5 / 0.055610791842142744 / 3.1159449570093987 | [NPY](tensors/0003335.npy) |
| 3336 | `model.layers.11.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.75 / 31.0 / 0.06546103954315186 / 3.389705914699592 | [NPY](tensors/0003336.npy) |
| 3337 | `model.layers.11.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.5 / 111.5 / 0.055610791842142744 / 3.1159449570093987 | [NPY](tensors/0003337.npy) |
| 3338 | `model.layers.11.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -8.1875 / 7.9375 / -0.0085221529006958 / 2.1851641711505643 | [NPY](tensors/0003338.npy) |
| 3339 | `model.layers.11.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.03125 / 8.0 / -0.02502937358804047 / 1.36176846890926 | [NPY](tensors/0003339.npy) |
| 3340 | `model.layers.11.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.0 / 75.5 / 0.005567385546035237 / 3.893866153188151 | [NPY](tensors/0003340.npy) |
| 3341 | `model.layers.11.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -89.0 / 75.5 / 0.005567385546035237 / 3.893866153188151 | [NPY](tensors/0003341.npy) |
| 3342 | `model.layers.11.self_attn` | 28 | `output[1]` | [1, 64, 1, 333] | torch.bfloat16 → float32 | 2.9467628337442875e-10 / 0.9296875 / 0.0025263442108779655 / 0.014729317035357703 | [NPY](tensors/0003342.npy) |
| 3343 | `model.layers.11.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -316.0 / 484.0 / 0.43865898980034723 / 23.580077912861714 | [NPY](tensors/0003343.npy) |
| 3344 | `model.layers.11.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.90625 / 4.28125 / -0.0011143710878160264 / 0.7564688475664096 | [NPY](tensors/0003344.npy) |
| 3345 | `model.layers.11.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.90625 / 4.28125 / -0.0011143710878160264 / 0.7564688475664096 | [NPY](tensors/0003345.npy) |
| 3346 | `model.layers.11.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.90625 / 4.28125 / -0.0011143710878160264 / 0.7564688475664096 | [NPY](tensors/0003346.npy) |
| 3347 | `model.layers.11.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3348 | `model.layers.11.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3349 | `model.layers.11.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3350 | `model.layers.11.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -125.0 / 125.5 / 0.039606295691596134 / 5.807809089335999 | [NPY](tensors/0003350.npy) |
| 3351 | `model.layers.11.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -125.0 / 125.5 / 0.039606295691596134 / 5.807809089335999 | [NPY](tensors/0003351.npy) |
| 3352 | `model.layers.11.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3671875 / 1.265625 / -0.06158447265625 / 0.5679403969615366 | [NPY](tensors/0003352.npy) |
| 3353 | `model.layers.11` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -440.0 / 572.0 / 0.4791619194878472 / 26.811901816924163 | [NPY](tensors/0003353.npy) |
| 3432 | `model.layers.11` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -528.0 / 648.0 / 0.21806233723958332 / 26.79427020910533 | [NPY](tensors/0003432.npy) |
| 3433 | `model.layers.11` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 334] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003433.npy) |
| 3434 | `model.layers.11` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0003434.npy) |
| 3435 | `model.layers.11` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0003435.npy) |
| 3436 | `model.layers.11` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0003436.npy) |
| 3437 | `model.layers.11` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3438 | `model.layers.11` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3439 | `model.layers.11` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3440 | `model.layers.11.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -528.0 / 648.0 / 0.21806233723958332 / 26.79427020910533 | [NPY](tensors/0003440.npy) |
| 3441 | `model.layers.11.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.5 / 113.5 / 0.03476798037687937 / 3.2763186826706328 | [NPY](tensors/0003441.npy) |
| 3442 | `model.layers.11.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.5 / 113.5 / 0.03476798037687937 / 3.2763186826706328 | [NPY](tensors/0003442.npy) |
| 3443 | `model.layers.11.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 334] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003443.npy) |
| 3444 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0003444.npy) |
| 3445 | `model.layers.11.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3446 | `model.layers.11.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3447 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0003447.npy) |
| 3448 | `model.layers.11.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0003448.npy) |
| 3449 | `model.layers.11.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3450 | `model.layers.11.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.5 / 113.5 / 0.03476798037687937 / 3.2763186826706328 | [NPY](tensors/0003450.npy) |
| 3451 | `model.layers.11.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.03125 / 9.1875 / 0.009306089727033395 / 1.2782322795874574 | [NPY](tensors/0003451.npy) |
| 3452 | `model.layers.11.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.5 / 113.5 / 0.03476798037687937 / 3.2763186826706328 | [NPY](tensors/0003452.npy) |
| 3453 | `model.layers.11.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.625 / 30.375 / 0.010152280330657959 / 3.3059874090049988 | [NPY](tensors/0003453.npy) |
| 3454 | `model.layers.11.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -103.5 / 113.5 / 0.03476798037687937 / 3.2763186826706328 | [NPY](tensors/0003454.npy) |
| 3455 | `model.layers.11.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.625 / 8.1875 / 0.03486132621765137 / 2.3298229240544535 | [NPY](tensors/0003455.npy) |
| 3456 | `model.layers.11.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.3125 / 8.0625 / -0.01938534341752529 / 1.343109826697775 | [NPY](tensors/0003456.npy) |
| 3457 | `model.layers.11.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -232.0 / 217.0 / -0.05299826363722483 / 6.970331632103938 | [NPY](tensors/0003457.npy) |
| 3458 | `model.layers.11.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -232.0 / 217.0 / -0.05299826363722483 / 6.970331632103938 | [NPY](tensors/0003458.npy) |
| 3459 | `model.layers.11.self_attn` | 29 | `output[1]` | [1, 64, 1, 334] | torch.bfloat16 → float32 | 4.7975845518521965e-11 / 0.921875 / 0.002155621983584255 / 0.017377635821696213 | [NPY](tensors/0003459.npy) |
| 3460 | `model.layers.11.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 416.0 / 0.16490919325086806 / 23.558156143760538 | [NPY](tensors/0003460.npy) |
| 3461 | `model.layers.11.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.578125 / 4.15625 / -0.007234022352430556 / 0.8239822990212337 | [NPY](tensors/0003461.npy) |
| 3462 | `model.layers.11.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.578125 / 4.15625 / -0.007234022352430556 / 0.8239822990212337 | [NPY](tensors/0003462.npy) |
| 3463 | `model.layers.11.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.578125 / 4.15625 / -0.007234022352430556 / 0.8239822990212337 | [NPY](tensors/0003463.npy) |
| 3464 | `model.layers.11.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3465 | `model.layers.11.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3466 | `model.layers.11.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3467 | `model.layers.11.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -300.0 / 218.0 / 0.13008956909179686 / 9.431672836125964 | [NPY](tensors/0003467.npy) |
| 3468 | `model.layers.11.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -300.0 / 218.0 / 0.13008956909179686 / 9.431672836125964 | [NPY](tensors/0003468.npy) |
| 3469 | `model.layers.11.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.25 / 1.5234375 / -0.20911788940429688 / 0.8184456605417109 | [NPY](tensors/0003469.npy) |
| 3470 | `model.layers.11` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -612.0 / 632.0 / 0.2935268825954861 / 29.482981274641926 | [NPY](tensors/0003470.npy) |
| 3549 | `model.layers.11` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -420.0 / 584.0 / 0.38472374810112847 / 23.873272069748175 | [NPY](tensors/0003549.npy) |
| 3550 | `model.layers.11` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 335] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003550.npy) |
| 3551 | `model.layers.11` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0003551.npy) |
| 3552 | `model.layers.11` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0003552.npy) |
| 3553 | `model.layers.11` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0003553.npy) |
| 3554 | `model.layers.11` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3555 | `model.layers.11` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3556 | `model.layers.11` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3557 | `model.layers.11.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -420.0 / 584.0 / 0.38472374810112847 / 23.873272069748175 | [NPY](tensors/0003557.npy) |
| 3558 | `model.layers.11.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 114.5 / 0.053465092182159425 / 3.2736404960524847 | [NPY](tensors/0003558.npy) |
| 3559 | `model.layers.11.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 114.5 / 0.053465092182159425 / 3.2736404960524847 | [NPY](tensors/0003559.npy) |
| 3560 | `model.layers.11.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 335] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003560.npy) |
| 3561 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0003561.npy) |
| 3562 | `model.layers.11.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3563 | `model.layers.11.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3564 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0003564.npy) |
| 3565 | `model.layers.11.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0003565.npy) |
| 3566 | `model.layers.11.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3567 | `model.layers.11.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 114.5 / 0.053465092182159425 / 3.2736404960524847 | [NPY](tensors/0003567.npy) |
| 3568 | `model.layers.11.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.78125 / 10.0 / 0.01972659584134817 / 1.3023972409433924 | [NPY](tensors/0003568.npy) |
| 3569 | `model.layers.11.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 114.5 / 0.053465092182159425 / 3.2736404960524847 | [NPY](tensors/0003569.npy) |
| 3570 | `model.layers.11.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.25 / 32.0 / -0.009326577186584473 / 3.5213692272726593 | [NPY](tensors/0003570.npy) |
| 3571 | `model.layers.11.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -92.5 / 114.5 / 0.053465092182159425 / 3.2736404960524847 | [NPY](tensors/0003571.npy) |
| 3572 | `model.layers.11.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.875 / 7.90625 / 0.060528673231601715 / 2.4608651219372635 | [NPY](tensors/0003572.npy) |
| 3573 | `model.layers.11.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.3125 / 6.75 / 0.007609224878251553 / 1.3481446594197328 | [NPY](tensors/0003573.npy) |
| 3574 | `model.layers.11.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -170.0 / 167.0 / -0.07295077906714545 / 5.461851963513963 | [NPY](tensors/0003574.npy) |
| 3575 | `model.layers.11.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -170.0 / 167.0 / -0.07295077906714545 / 5.461851963513963 | [NPY](tensors/0003575.npy) |
| 3576 | `model.layers.11.self_attn` | 30 | `output[1]` | [1, 64, 1, 335] | torch.bfloat16 → float32 | 1.5370460459962487e-10 / 0.91015625 / 0.0023260284195823597 / 0.0176385903659365 | [NPY](tensors/0003576.npy) |
| 3577 | `model.layers.11.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -253.0 / 414.0 / 0.3122236463758681 / 21.783687147850966 | [NPY](tensors/0003577.npy) |
| 3578 | `model.layers.11.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.9375 / 3.828125 / 0.006375314791997274 / 0.7339584403108076 | [NPY](tensors/0003578.npy) |
| 3579 | `model.layers.11.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.9375 / 3.828125 / 0.006375314791997274 / 0.7339584403108076 | [NPY](tensors/0003579.npy) |
| 3580 | `model.layers.11.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.9375 / 3.828125 / 0.006375314791997274 / 0.7339584403108076 | [NPY](tensors/0003580.npy) |
| 3581 | `model.layers.11.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3582 | `model.layers.11.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3583 | `model.layers.11.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3584 | `model.layers.11.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -264.0 / 177.0 / 0.10191621217462751 / 8.452787211664814 | [NPY](tensors/0003584.npy) |
| 3585 | `model.layers.11.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -264.0 / 177.0 / 0.10191621217462751 / 8.452787211664814 | [NPY](tensors/0003585.npy) |
| 3586 | `model.layers.11.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.109375 / 1.484375 / -0.20481491088867188 / 0.8990192909181224 | [NPY](tensors/0003586.npy) |
| 3587 | `model.layers.11` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -516.0 / 584.0 / 0.4156521267361111 / 27.037212817302322 | [NPY](tensors/0003587.npy) |
| 3666 | `model.layers.11` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -470.0 / 560.0 / 0.6445465087890625 / 24.326878075621764 | [NPY](tensors/0003666.npy) |
| 3667 | `model.layers.11` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 336] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003667.npy) |
| 3668 | `model.layers.11` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0003668.npy) |
| 3669 | `model.layers.11` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0003669.npy) |
| 3670 | `model.layers.11` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0003670.npy) |
| 3671 | `model.layers.11` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3672 | `model.layers.11` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3673 | `model.layers.11` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3674 | `model.layers.11.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -470.0 / 560.0 / 0.6445465087890625 / 24.326878075621764 | [NPY](tensors/0003674.npy) |
| 3675 | `model.layers.11.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 108.0 / 0.06806503675050206 / 3.3064604029442832 | [NPY](tensors/0003675.npy) |
| 3676 | `model.layers.11.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 108.0 / 0.06806503675050206 / 3.3064604029442832 | [NPY](tensors/0003676.npy) |
| 3677 | `model.layers.11.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 336] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003677.npy) |
| 3678 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0003678.npy) |
| 3679 | `model.layers.11.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3680 | `model.layers.11.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3681 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0003681.npy) |
| 3682 | `model.layers.11.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0003682.npy) |
| 3683 | `model.layers.11.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3684 | `model.layers.11.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 108.0 / 0.06806503675050206 / 3.3064604029442832 | [NPY](tensors/0003684.npy) |
| 3685 | `model.layers.11.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.625 / 9.125 / 0.016238038428127766 / 1.3528828986265022 | [NPY](tensors/0003685.npy) |
| 3686 | `model.layers.11.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 108.0 / 0.06806503675050206 / 3.3064604029442832 | [NPY](tensors/0003686.npy) |
| 3687 | `model.layers.11.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.125 / 36.25 / 0.019651293754577637 / 3.6758790817299785 | [NPY](tensors/0003687.npy) |
| 3688 | `model.layers.11.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 108.0 / 0.06806503675050206 / 3.3064604029442832 | [NPY](tensors/0003688.npy) |
| 3689 | `model.layers.11.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.6875 / 7.25 / 0.027772903442382812 / 2.4201282964169257 | [NPY](tensors/0003689.npy) |
| 3690 | `model.layers.11.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.03125 / 6.625 / 0.006238194589968771 / 1.4080316699499371 | [NPY](tensors/0003690.npy) |
| 3691 | `model.layers.11.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -144.0 / 156.0 / 0.01691658231947157 / 5.093978617482638 | [NPY](tensors/0003691.npy) |
| 3692 | `model.layers.11.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -144.0 / 156.0 / 0.01691658231947157 / 5.093978617482638 | [NPY](tensors/0003692.npy) |
| 3693 | `model.layers.11.self_attn` | 31 | `output[1]` | [1, 64, 1, 336] | torch.bfloat16 → float32 | 1.2676082405960187e-11 / 0.9140625 / 0.00236291616752164 / 0.017177735230692794 | [NPY](tensors/0003693.npy) |
| 3694 | `model.layers.11.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -314.0 / 416.0 / 0.6617436726888021 / 23.149771278980694 | [NPY](tensors/0003694.npy) |
| 3695 | `model.layers.11.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5625 / 3.171875 / 0.01692314710881975 / 0.7309542743219033 | [NPY](tensors/0003695.npy) |
| 3696 | `model.layers.11.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.5625 / 3.171875 / 0.01692314710881975 / 0.7309542743219033 | [NPY](tensors/0003696.npy) |
| 3697 | `model.layers.11.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.5625 / 3.171875 / 0.01692314710881975 / 0.7309542743219033 | [NPY](tensors/0003697.npy) |
| 3698 | `model.layers.11.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3699 | `model.layers.11.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3700 | `model.layers.11.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3701 | `model.layers.11.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -243.0 / 197.0 / 0.1465363687939114 / 8.391658715673374 | [NPY](tensors/0003701.npy) |
| 3702 | `model.layers.11.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -243.0 / 197.0 / 0.1465363687939114 / 8.391658715673374 | [NPY](tensors/0003702.npy) |
| 3703 | `model.layers.11.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.828125 / 1.5234375 / -0.17066574096679688 / 0.8601452975087833 | [NPY](tensors/0003703.npy) |
| 3704 | `model.layers.11` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -556.0 / 612.0 / 0.8088027954101562 / 28.504069727186707 | [NPY](tensors/0003704.npy) |
| 3783 | `model.layers.11` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -376.0 / 520.0 / 0.6112575954861111 / 23.20914034145904 | [NPY](tensors/0003783.npy) |
| 3784 | `model.layers.11` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 337] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003784.npy) |
| 3785 | `model.layers.11` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0003785.npy) |
| 3786 | `model.layers.11` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0003786.npy) |
| 3787 | `model.layers.11` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0003787.npy) |
| 3788 | `model.layers.11` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3789 | `model.layers.11` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3790 | `model.layers.11` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3791 | `model.layers.11.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -376.0 / 520.0 / 0.6112575954861111 / 23.20914034145904 | [NPY](tensors/0003791.npy) |
| 3792 | `model.layers.11.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 105.0 / 0.06523239612579346 / 3.092726574815985 | [NPY](tensors/0003792.npy) |
| 3793 | `model.layers.11.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 105.0 / 0.06523239612579346 / 3.092726574815985 | [NPY](tensors/0003793.npy) |
| 3794 | `model.layers.11.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 337] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003794.npy) |
| 3795 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0003795.npy) |
| 3796 | `model.layers.11.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3797 | `model.layers.11.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3798 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0003798.npy) |
| 3799 | `model.layers.11.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0003799.npy) |
| 3800 | `model.layers.11.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3801 | `model.layers.11.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 105.0 / 0.06523239612579346 / 3.092726574815985 | [NPY](tensors/0003801.npy) |
| 3802 | `model.layers.11.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.0 / 8.1875 / 0.0017298096790909767 / 1.3883304081875918 | [NPY](tensors/0003802.npy) |
| 3803 | `model.layers.11.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 105.0 / 0.06523239612579346 / 3.092726574815985 | [NPY](tensors/0003803.npy) |
| 3804 | `model.layers.11.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.25 / 35.75 / 0.014116883277893066 / 3.603540369007615 | [NPY](tensors/0003804.npy) |
| 3805 | `model.layers.11.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -85.0 / 105.0 / 0.06523239612579346 / 3.092726574815985 | [NPY](tensors/0003805.npy) |
| 3806 | `model.layers.11.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.46875 / 7.0 / -0.16878756880760193 / 2.389609069491364 | [NPY](tensors/0003806.npy) |
| 3807 | `model.layers.11.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.03125 / 7.1875 / -0.028642105869948864 / 1.511195697939579 | [NPY](tensors/0003807.npy) |
| 3808 | `model.layers.11.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -171.0 / 156.0 / 0.027057986789279512 / 5.828013160447737 | [NPY](tensors/0003808.npy) |
| 3809 | `model.layers.11.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -171.0 / 156.0 / 0.027057986789279512 / 5.828013160447737 | [NPY](tensors/0003809.npy) |
| 3810 | `model.layers.11.self_attn` | 32 | `output[1]` | [1, 64, 1, 337] | torch.bfloat16 → float32 | 1.693933882052079e-11 / 0.94921875 / 0.002370971078092226 / 0.019052618660039582 | [NPY](tensors/0003810.npy) |
| 3811 | `model.layers.11.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -220.0 / 348.0 / 0.6379550509982639 / 21.862330135478576 | [NPY](tensors/0003811.npy) |
| 3812 | `model.layers.11.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.734375 / 3.28125 / 0.012695135010613336 / 0.7987183020528995 | [NPY](tensors/0003812.npy) |
| 3813 | `model.layers.11.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.734375 / 3.28125 / 0.012695135010613336 / 0.7987183020528995 | [NPY](tensors/0003813.npy) |
| 3814 | `model.layers.11.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.734375 / 3.28125 / 0.012695135010613336 / 0.7987183020528995 | [NPY](tensors/0003814.npy) |
| 3815 | `model.layers.11.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3816 | `model.layers.11.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3817 | `model.layers.11.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3818 | `model.layers.11.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -320.0 / 356.0 / 0.1347791247897678 / 11.739811061823842 | [NPY](tensors/0003818.npy) |
| 3819 | `model.layers.11.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -320.0 / 356.0 / 0.1347791247897678 / 11.739811061823842 | [NPY](tensors/0003819.npy) |
| 3820 | `model.layers.11.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.203125 / 1.875 / -0.16583633422851562 / 0.8523555582071526 | [NPY](tensors/0003820.npy) |
| 3821 | `model.layers.11` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -540.0 / 704.0 / 0.7737186008029514 / 29.480803381402943 | [NPY](tensors/0003821.npy) |
| 3900 | `model.layers.11` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -252.0 / 404.0 / 0.5846569485134548 / 19.103715276500342 | [NPY](tensors/0003900.npy) |
| 3901 | `model.layers.11` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 338] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003901.npy) |
| 3902 | `model.layers.11` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0003902.npy) |
| 3903 | `model.layers.11` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0003903.npy) |
| 3904 | `model.layers.11` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0003904.npy) |
| 3905 | `model.layers.11` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3906 | `model.layers.11` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3907 | `model.layers.11` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3908 | `model.layers.11.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -252.0 / 404.0 / 0.5846569485134548 / 19.103715276500342 | [NPY](tensors/0003908.npy) |
| 3909 | `model.layers.11.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 99.0 / 0.08263667027155558 / 2.941197139475496 | [NPY](tensors/0003909.npy) |
| 3910 | `model.layers.11.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 99.0 / 0.08263667027155558 / 2.941197139475496 | [NPY](tensors/0003910.npy) |
| 3911 | `model.layers.11.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 338] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003911.npy) |
| 3912 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0003912.npy) |
| 3913 | `model.layers.11.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3914 | `model.layers.11.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3915 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0003915.npy) |
| 3916 | `model.layers.11.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0003916.npy) |
| 3917 | `model.layers.11.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3918 | `model.layers.11.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 99.0 / 0.08263667027155558 / 2.941197139475496 | [NPY](tensors/0003918.npy) |
| 3919 | `model.layers.11.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.96875 / 9.625 / 0.033615799620747566 / 1.3881462389213621 | [NPY](tensors/0003919.npy) |
| 3920 | `model.layers.11.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 99.0 / 0.08263667027155558 / 2.941197139475496 | [NPY](tensors/0003920.npy) |
| 3921 | `model.layers.11.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.25 / 40.5 / 0.06721332669258118 / 4.143116255914169 | [NPY](tensors/0003921.npy) |
| 3922 | `model.layers.11.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -69.0 / 99.0 / 0.08263667027155558 / 2.941197139475496 | [NPY](tensors/0003922.npy) |
| 3923 | `model.layers.11.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.0 / 7.25 / -0.009697876870632172 / 2.276193474034054 | [NPY](tensors/0003923.npy) |
| 3924 | `model.layers.11.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.6875 / 6.625 / -0.02115936577320099 / 1.4252314584389678 | [NPY](tensors/0003924.npy) |
| 3925 | `model.layers.11.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 69.0 / 0.06442068244020144 / 3.7457198021279345 | [NPY](tensors/0003925.npy) |
| 3926 | `model.layers.11.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 69.0 / 0.06442068244020144 / 3.7457198021279345 | [NPY](tensors/0003926.npy) |
| 3927 | `model.layers.11.self_attn` | 33 | `output[1]` | [1, 64, 1, 338] | torch.bfloat16 → float32 | 6.252776074688882e-12 / 0.953125 / 0.0026439267612000696 / 0.015449909719648734 | [NPY](tensors/0003927.npy) |
| 3928 | `model.layers.11.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -183.0 / 360.0 / 0.6486173841688369 / 19.512682886526566 | [NPY](tensors/0003928.npy) |
| 3929 | `model.layers.11.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.71875 / 3.65625 / 0.013213986820644803 / 0.7355056629447986 | [NPY](tensors/0003929.npy) |
| 3930 | `model.layers.11.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.71875 / 3.65625 / 0.013213986820644803 / 0.7355056629447986 | [NPY](tensors/0003930.npy) |
| 3931 | `model.layers.11.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.71875 / 3.65625 / 0.013213986820644803 / 0.7355056629447986 | [NPY](tensors/0003931.npy) |
| 3932 | `model.layers.11.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3933 | `model.layers.11.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3934 | `model.layers.11.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3935 | `model.layers.11.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -240.0 / 150.0 / 0.1916532701916165 / 7.882725517160059 | [NPY](tensors/0003935.npy) |
| 3936 | `model.layers.11.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -240.0 / 150.0 / 0.1916532701916165 / 7.882725517160059 | [NPY](tensors/0003936.npy) |
| 3937 | `model.layers.11.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9921875 / 1.9921875 / -0.12084197998046875 / 0.7818442742424154 | [NPY](tensors/0003937.npy) |
| 3938 | `model.layers.11` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -424.0 / 510.0 / 0.8385908338758681 / 24.16700635472869 | [NPY](tensors/0003938.npy) |
| 4017 | `model.layers.11` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -348.0 / 420.0 / 0.31367933485243055 / 19.62631135642103 | [NPY](tensors/0004017.npy) |
| 4018 | `model.layers.11` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 339] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004018.npy) |
| 4019 | `model.layers.11` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0004019.npy) |
| 4020 | `model.layers.11` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0004020.npy) |
| 4021 | `model.layers.11` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0004021.npy) |
| 4022 | `model.layers.11` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4023 | `model.layers.11` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4024 | `model.layers.11` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4025 | `model.layers.11.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -348.0 / 420.0 / 0.31367933485243055 / 19.62631135642103 | [NPY](tensors/0004025.npy) |
| 4026 | `model.layers.11.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 100.5 / 0.04540554947323269 / 3.18901746139836 | [NPY](tensors/0004026.npy) |
| 4027 | `model.layers.11.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 100.5 / 0.04540554947323269 / 3.18901746139836 | [NPY](tensors/0004027.npy) |
| 4028 | `model.layers.11.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 339] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004028.npy) |
| 4029 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0004029.npy) |
| 4030 | `model.layers.11.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4031 | `model.layers.11.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4032 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0004032.npy) |
| 4033 | `model.layers.11.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0004033.npy) |
| 4034 | `model.layers.11.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4035 | `model.layers.11.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 100.5 / 0.04540554947323269 / 3.18901746139836 | [NPY](tensors/0004035.npy) |
| 4036 | `model.layers.11.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.96875 / 8.6875 / 0.030083201825618744 / 1.3113072664072272 | [NPY](tensors/0004036.npy) |
| 4037 | `model.layers.11.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 100.5 / 0.04540554947323269 / 3.18901746139836 | [NPY](tensors/0004037.npy) |
| 4038 | `model.layers.11.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.0 / 33.5 / 0.11603659391403198 / 3.6372621641500547 | [NPY](tensors/0004038.npy) |
| 4039 | `model.layers.11.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -93.0 / 100.5 / 0.04540554947323269 / 3.18901746139836 | [NPY](tensors/0004039.npy) |
| 4040 | `model.layers.11.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.125 / 7.3125 / -0.09604835510253906 / 2.1056330907384306 | [NPY](tensors/0004040.npy) |
| 4041 | `model.layers.11.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.25 / 6.125 / 0.0035294522531330585 / 1.257798305930209 | [NPY](tensors/0004041.npy) |
| 4042 | `model.layers.11.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -161.0 / 154.0 / -0.01125285890367296 / 5.633354957842623 | [NPY](tensors/0004042.npy) |
| 4043 | `model.layers.11.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -161.0 / 154.0 / -0.01125285890367296 / 5.633354957842623 | [NPY](tensors/0004043.npy) |
| 4044 | `model.layers.11.self_attn` | 34 | `output[1]` | [1, 64, 1, 339] | torch.bfloat16 → float32 | 2.955857780762017e-11 / 0.890625 / 0.002518327816424265 / 0.01432473335385881 | [NPY](tensors/0004044.npy) |
| 4045 | `model.layers.11.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -235.0 / 272.0 / 0.30251600477430557 / 18.269479872467883 | [NPY](tensors/0004045.npy) |
| 4046 | `model.layers.11.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.09375 / 3.859375 / 0.00863316986295912 / 0.7891124638790205 | [NPY](tensors/0004046.npy) |
| 4047 | `model.layers.11.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.09375 / 3.859375 / 0.00863316986295912 / 0.7891124638790205 | [NPY](tensors/0004047.npy) |
| 4048 | `model.layers.11.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.09375 / 3.859375 / 0.00863316986295912 / 0.7891124638790205 | [NPY](tensors/0004048.npy) |
| 4049 | `model.layers.11.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4050 | `model.layers.11.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4051 | `model.layers.11.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4052 | `model.layers.11.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -252.0 / 255.0 / 0.2081467436419593 / 9.171244958183653 | [NPY](tensors/0004052.npy) |
| 4053 | `model.layers.11.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -252.0 / 255.0 / 0.2081467436419593 / 9.171244958183653 | [NPY](tensors/0004053.npy) |
| 4054 | `model.layers.11.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.625 / 1.8125 / -0.1536712646484375 / 0.8826189560850319 | [NPY](tensors/0004054.npy) |
| 4055 | `model.layers.11` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -446.0 / 516.0 / 0.511944580078125 / 23.70171677168289 | [NPY](tensors/0004055.npy) |
| 4134 | `model.layers.11` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -370.0 / 580.0 / 0.33283267550998263 / 21.28510244741268 | [NPY](tensors/0004134.npy) |
| 4135 | `model.layers.11` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 340] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004135.npy) |
| 4136 | `model.layers.11` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0004136.npy) |
| 4137 | `model.layers.11` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0004137.npy) |
| 4138 | `model.layers.11` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0004138.npy) |
| 4139 | `model.layers.11` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4140 | `model.layers.11` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4141 | `model.layers.11` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4142 | `model.layers.11.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -370.0 / 580.0 / 0.33283267550998263 / 21.28510244741268 | [NPY](tensors/0004142.npy) |
| 4143 | `model.layers.11.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.0 / 127.5 / 0.05691198574172126 / 3.432446299054052 | [NPY](tensors/0004143.npy) |
| 4144 | `model.layers.11.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.0 / 127.5 / 0.05691198574172126 / 3.432446299054052 | [NPY](tensors/0004144.npy) |
| 4145 | `model.layers.11.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 340] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004145.npy) |
| 4146 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0004146.npy) |
| 4147 | `model.layers.11.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4148 | `model.layers.11.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4149 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0004149.npy) |
| 4150 | `model.layers.11.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0004150.npy) |
| 4151 | `model.layers.11.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4152 | `model.layers.11.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.0 / 127.5 / 0.05691198574172126 / 3.432446299054052 | [NPY](tensors/0004152.npy) |
| 4153 | `model.layers.11.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 8.9375 / 0.0007447204552590847 / 1.2763211696235335 | [NPY](tensors/0004153.npy) |
| 4154 | `model.layers.11.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.0 / 127.5 / 0.05691198574172126 / 3.432446299054052 | [NPY](tensors/0004154.npy) |
| 4155 | `model.layers.11.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.75 / 33.5 / -0.021932512521743774 / 3.5810568852520412 | [NPY](tensors/0004155.npy) |
| 4156 | `model.layers.11.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -91.0 / 127.5 / 0.05691198574172126 / 3.432446299054052 | [NPY](tensors/0004156.npy) |
| 4157 | `model.layers.11.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.8125 / 7.875 / -0.1163446307182312 / 2.2805541381231555 | [NPY](tensors/0004157.npy) |
| 4158 | `model.layers.11.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.34375 / 6.5 / -0.00178585946559906 / 1.3080898678103139 | [NPY](tensors/0004158.npy) |
| 4159 | `model.layers.11.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -242.0 / 198.0 / -0.10983768436643812 / 7.010231822365815 | [NPY](tensors/0004159.npy) |
| 4160 | `model.layers.11.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -242.0 / 198.0 / -0.10983768436643812 / 7.010231822365815 | [NPY](tensors/0004160.npy) |
| 4161 | `model.layers.11.self_attn` | 35 | `output[1]` | [1, 64, 1, 340] | torch.bfloat16 → float32 | 1.659827830735594e-11 / 0.93359375 / 0.002385307348220882 / 0.01655374410540808 | [NPY](tensors/0004161.npy) |
| 4162 | `model.layers.11.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -182.0 / 338.0 / 0.22286936442057292 / 18.50220417378785 | [NPY](tensors/0004162.npy) |
| 4163 | `model.layers.11.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.125 / 4.71875 / 0.0033427132500542535 / 0.7550509196575981 | [NPY](tensors/0004163.npy) |
| 4164 | `model.layers.11.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.125 / 4.71875 / 0.0033427132500542535 / 0.7550509196575981 | [NPY](tensors/0004164.npy) |
| 4165 | `model.layers.11.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.125 / 4.71875 / 0.0033427132500542535 / 0.7550509196575981 | [NPY](tensors/0004165.npy) |
| 4166 | `model.layers.11.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4167 | `model.layers.11.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4168 | `model.layers.11.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4169 | `model.layers.11.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -448.0 / 406.0 / 0.31660752296447753 / 15.027647922166897 | [NPY](tensors/0004169.npy) |
| 4170 | `model.layers.11.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -448.0 / 406.0 / 0.31660752296447753 / 15.027647922166897 | [NPY](tensors/0004170.npy) |
| 4171 | `model.layers.11.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.53125 / 1.9453125 / -0.21159744262695312 / 1.1152206371864923 | [NPY](tensors/0004171.npy) |
| 4172 | `model.layers.11` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -620.0 / 744.0 / 0.5406226264105902 / 28.639136808776424 | [NPY](tensors/0004172.npy) |
| 4251 | `model.layers.11` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -243.0 / 392.0 / 0.6485792371961806 / 15.955087094035404 | [NPY](tensors/0004251.npy) |
| 4252 | `model.layers.11` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 341] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004252.npy) |
| 4253 | `model.layers.11` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.34375 / 0.7532014846801758 / 0.8246045706539666 | [NPY](tensors/0004253.npy) |
| 4254 | `model.layers.11` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.03213447332382202 / 0.7489573739100013 | [NPY](tensors/0004254.npy) |
| 4255 | `model.layers.11` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 340.0 / 340.0 / 340.0 / 0.0 | [NPY](tensors/0004255.npy) |
| 4256 | `model.layers.11` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4257 | `model.layers.11` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4258 | `model.layers.11` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4259 | `model.layers.11.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -243.0 / 392.0 / 0.6485792371961806 / 15.955087094035404 | [NPY](tensors/0004259.npy) |
| 4260 | `model.layers.11.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 115.0 / 0.09404397010803223 / 3.2719103220437473 | [NPY](tensors/0004260.npy) |
| 4261 | `model.layers.11.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 115.0 / 0.09404397010803223 / 3.2719103220437473 | [NPY](tensors/0004261.npy) |
| 4262 | `model.layers.11.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 341] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004262.npy) |
| 4263 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 340.0 / 340.0 / 340.0 / 0.0 | [NPY](tensors/0004263.npy) |
| 4264 | `model.layers.11.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4265 | `model.layers.11.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4266 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.34375 / 0.7532014846801758 / 0.8246045706539666 | [NPY](tensors/0004266.npy) |
| 4267 | `model.layers.11.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.03213447332382202 / 0.7489573739100013 | [NPY](tensors/0004267.npy) |
| 4268 | `model.layers.11.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4269 | `model.layers.11.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 115.0 / 0.09404397010803223 / 3.2719103220437473 | [NPY](tensors/0004269.npy) |
| 4270 | `model.layers.11.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.65625 / 7.25 / 0.04803156666457653 / 1.1977173806357795 | [NPY](tensors/0004270.npy) |
| 4271 | `model.layers.11.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 115.0 / 0.09404397010803223 / 3.2719103220437473 | [NPY](tensors/0004271.npy) |
| 4272 | `model.layers.11.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.25 / 42.5 / 0.20511611551046371 / 3.9001775775538667 | [NPY](tensors/0004272.npy) |
| 4273 | `model.layers.11.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -80.0 / 115.0 / 0.09404397010803223 / 3.2719103220437473 | [NPY](tensors/0004273.npy) |
| 4274 | `model.layers.11.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.34375 / 6.0625 / 0.040249768644571304 / 2.115686527119715 | [NPY](tensors/0004274.npy) |
| 4275 | `model.layers.11.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.5 / 6.84375 / -0.0030478378757834435 / 1.2301287345983254 | [NPY](tensors/0004275.npy) |
| 4276 | `model.layers.11.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -76.5 / 113.5 / -0.010756746927897135 / 4.118165516070644 | [NPY](tensors/0004276.npy) |
| 4277 | `model.layers.11.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -76.5 / 113.5 / -0.010756746927897135 / 4.118165516070644 | [NPY](tensors/0004277.npy) |
| 4278 | `model.layers.11.self_attn` | 36 | `output[1]` | [1, 64, 1, 341] | torch.bfloat16 → float32 | 2.1827872842550278e-11 / 0.94921875 / 0.0026930425581660014 / 0.012757413984964916 | [NPY](tensors/0004278.npy) |
| 4279 | `model.layers.11.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -130.0 / 332.0 / 0.6371548970540365 / 15.597398820827944 | [NPY](tensors/0004279.npy) |
| 4280 | `model.layers.11.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.234375 / 2.9375 / 0.026736264758639865 / 0.7374782992963443 | [NPY](tensors/0004280.npy) |
| 4281 | `model.layers.11.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.234375 / 2.9375 / 0.026736264758639865 / 0.7374782992963443 | [NPY](tensors/0004281.npy) |
| 4282 | `model.layers.11.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.234375 / 2.9375 / 0.026736264758639865 / 0.7374782992963443 | [NPY](tensors/0004282.npy) |
| 4283 | `model.layers.11.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4284 | `model.layers.11.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4285 | `model.layers.11.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4286 | `model.layers.11.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -203.0 / 179.0 / -0.00358125368754069 / 7.584688140405973 | [NPY](tensors/0004286.npy) |
| 4287 | `model.layers.11.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -203.0 / 179.0 / -0.00358125368754069 / 7.584688140405973 | [NPY](tensors/0004287.npy) |
| 4288 | `model.layers.11.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.171875 / -0.0835418701171875 / 0.6089610792011435 | [NPY](tensors/0004288.npy) |
| 4289 | `model.layers.11` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -332.0 / 496.0 / 0.6346118503146702 / 20.484297687256586 | [NPY](tensors/0004289.npy) |
| 4368 | `model.layers.11` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -384.0 / 524.0 / 0.3312157524956597 / 20.309565527711555 | [NPY](tensors/0004368.npy) |
| 4369 | `model.layers.11` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 342] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004369.npy) |
| 4370 | `model.layers.11` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.7198410034179688 / 0.8503804730267482 | [NPY](tensors/0004370.npy) |
| 4371 | `model.layers.11` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.027828902006149292 / 0.7525043584225227 | [NPY](tensors/0004371.npy) |
| 4372 | `model.layers.11` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 341.0 / 341.0 / 341.0 / 0.0 | [NPY](tensors/0004372.npy) |
| 4373 | `model.layers.11` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4374 | `model.layers.11` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4375 | `model.layers.11` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4376 | `model.layers.11.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -384.0 / 524.0 / 0.3312157524956597 / 20.309565527711555 | [NPY](tensors/0004376.npy) |
| 4377 | `model.layers.11.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.5 / 121.0 / 0.04938818878597683 / 3.401031678148696 | [NPY](tensors/0004377.npy) |
| 4378 | `model.layers.11.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.5 / 121.0 / 0.04938818878597683 / 3.401031678148696 | [NPY](tensors/0004378.npy) |
| 4379 | `model.layers.11.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 342] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004379.npy) |
| 4380 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 341.0 / 341.0 / 341.0 / 0.0 | [NPY](tensors/0004380.npy) |
| 4381 | `model.layers.11.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4382 | `model.layers.11.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4383 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.7198410034179688 / 0.8503804730267482 | [NPY](tensors/0004383.npy) |
| 4384 | `model.layers.11.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.027828902006149292 / 0.7525043584225227 | [NPY](tensors/0004384.npy) |
| 4385 | `model.layers.11.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4386 | `model.layers.11.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.5 / 121.0 / 0.04938818878597683 / 3.401031678148696 | [NPY](tensors/0004386.npy) |
| 4387 | `model.layers.11.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.375 / 9.6875 / 0.022386625641956925 / 1.2579972322637782 | [NPY](tensors/0004387.npy) |
| 4388 | `model.layers.11.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.5 / 121.0 / 0.04938818878597683 / 3.401031678148696 | [NPY](tensors/0004388.npy) |
| 4389 | `model.layers.11.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.625 / 33.5 / -0.021655552089214325 / 3.6148090263367583 | [NPY](tensors/0004389.npy) |
| 4390 | `model.layers.11.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -99.5 / 121.0 / 0.04938818878597683 / 3.401031678148696 | [NPY](tensors/0004390.npy) |
| 4391 | `model.layers.11.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.59375 / 7.34375 / 0.05975574254989624 / 2.2088393369937247 | [NPY](tensors/0004391.npy) |
| 4392 | `model.layers.11.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.46875 / 6.15625 / 0.010562685318291187 / 1.2528311584529712 | [NPY](tensors/0004392.npy) |
| 4393 | `model.layers.11.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -142.0 / 146.0 / -0.013911505043506623 / 4.980041185050961 | [NPY](tensors/0004393.npy) |
| 4394 | `model.layers.11.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -142.0 / 146.0 / -0.013911505043506623 / 4.980041185050961 | [NPY](tensors/0004394.npy) |
| 4395 | `model.layers.11.self_attn` | 37 | `output[1]` | [1, 64, 1, 342] | torch.bfloat16 → float32 | 4.916955731459893e-12 / 0.9609375 / 0.0025986924075123517 / 0.014433027326321131 | [NPY](tensors/0004395.npy) |
| 4396 | `model.layers.11.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -238.0 / 382.0 / 0.3165615505642361 / 18.69969331141816 | [NPY](tensors/0004396.npy) |
| 4397 | `model.layers.11.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.140625 / 3.5 / 0.009439271026187473 / 0.7029495320365575 | [NPY](tensors/0004397.npy) |
| 4398 | `model.layers.11.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.140625 / 3.5 / 0.009439271026187473 / 0.7029495320365575 | [NPY](tensors/0004398.npy) |
| 4399 | `model.layers.11.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.140625 / 3.5 / 0.009439271026187473 / 0.7029495320365575 | [NPY](tensors/0004399.npy) |
| 4400 | `model.layers.11.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4401 | `model.layers.11.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4402 | `model.layers.11.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4403 | `model.layers.11.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -280.0 / 272.0 / 0.14500515460968016 / 9.568414788625459 | [NPY](tensors/0004403.npy) |
| 4404 | `model.layers.11.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -280.0 / 272.0 / 0.14500515460968016 / 9.568414788625459 | [NPY](tensors/0004404.npy) |
| 4405 | `model.layers.11.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.34375 / 1.6328125 / -0.1906599998474121 / 0.9066811070650442 | [NPY](tensors/0004405.npy) |
| 4406 | `model.layers.11` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -520.0 / 656.0 / 0.46206995646158855 / 25.589831968737535 | [NPY](tensors/0004406.npy) |
| 4485 | `model.layers.11` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -183.0 / 344.0 / 0.34590988159179686 / 13.096210521151399 | [NPY](tensors/0004485.npy) |
| 4486 | `model.layers.11` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 343] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004486.npy) |
| 4487 | `model.layers.11` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.70660400390625 / 0.91681783844784 | [NPY](tensors/0004487.npy) |
| 4488 | `model.layers.11` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / -0.014852643013000488 / 0.6845543139796254 | [NPY](tensors/0004488.npy) |
| 4489 | `model.layers.11` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 342.0 / 342.0 / 342.0 / 0.0 | [NPY](tensors/0004489.npy) |
| 4490 | `model.layers.11` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4491 | `model.layers.11` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4492 | `model.layers.11` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4493 | `model.layers.11.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -183.0 / 344.0 / 0.34590988159179686 / 13.096210521151399 | [NPY](tensors/0004493.npy) |
| 4494 | `model.layers.11.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.5 / 94.5 / 0.07613912290996976 / 3.149213835542686 | [NPY](tensors/0004494.npy) |
| 4495 | `model.layers.11.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.5 / 94.5 / 0.07613912290996976 / 3.149213835542686 | [NPY](tensors/0004495.npy) |
| 4496 | `model.layers.11.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 343] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004496.npy) |
| 4497 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 342.0 / 342.0 / 342.0 / 0.0 | [NPY](tensors/0004497.npy) |
| 4498 | `model.layers.11.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4499 | `model.layers.11.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4500 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.70660400390625 / 0.91681783844784 | [NPY](tensors/0004500.npy) |
| 4501 | `model.layers.11.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / -0.014852643013000488 / 0.6845543139796254 | [NPY](tensors/0004501.npy) |
| 4502 | `model.layers.11.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4503 | `model.layers.11.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.5 / 94.5 / 0.07613912290996976 / 3.149213835542686 | [NPY](tensors/0004503.npy) |
| 4504 | `model.layers.11.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0 / 7.875 / 0.032271192234475166 / 1.2504833710108254 | [NPY](tensors/0004504.npy) |
| 4505 | `model.layers.11.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.5 / 94.5 / 0.07613912290996976 / 3.149213835542686 | [NPY](tensors/0004505.npy) |
| 4506 | `model.layers.11.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.5 / 37.75 / 0.1641387641429901 / 3.7740480058863555 | [NPY](tensors/0004506.npy) |
| 4507 | `model.layers.11.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -73.5 / 94.5 / 0.07613912290996976 / 3.149213835542686 | [NPY](tensors/0004507.npy) |
| 4508 | `model.layers.11.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.78125 / 5.46875 / -0.04489457607269287 / 1.7479392016008273 | [NPY](tensors/0004508.npy) |
| 4509 | `model.layers.11.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.3125 / 5.0 / -0.0076020092237740755 / 1.171732166219462 | [NPY](tensors/0004509.npy) |
| 4510 | `model.layers.11.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.75 / 44.0 / 0.03794009288152059 / 3.375856216325131 | [NPY](tensors/0004510.npy) |
| 4511 | `model.layers.11.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -24.75 / 44.0 / 0.03794009288152059 / 3.375856216325131 | [NPY](tensors/0004511.npy) |
| 4512 | `model.layers.11.self_attn` | 38 | `output[1]` | [1, 64, 1, 343] | torch.bfloat16 → float32 | 6.868503987789154e-09 / 0.84375 / 0.0026605359950706707 / 0.01164336722370998 | [NPY](tensors/0004512.npy) |
| 4513 | `model.layers.11.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -155.0 / 348.0 / 0.3844453599717882 / 14.007299596921083 | [NPY](tensors/0004513.npy) |
| 4514 | `model.layers.11.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.546875 / 3.546875 / 0.0048298478126525875 / 0.6641597282745768 | [NPY](tensors/0004514.npy) |
| 4515 | `model.layers.11.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.546875 / 3.546875 / 0.0048298478126525875 / 0.6641597282745768 | [NPY](tensors/0004515.npy) |
| 4516 | `model.layers.11.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.546875 / 3.546875 / 0.0048298478126525875 / 0.6641597282745768 | [NPY](tensors/0004516.npy) |
| 4517 | `model.layers.11.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4518 | `model.layers.11.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4519 | `model.layers.11.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4520 | `model.layers.11.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -140.0 / 148.0 / 0.07225643528832329 / 5.617489128540022 | [NPY](tensors/0004520.npy) |
| 4521 | `model.layers.11.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -140.0 / 148.0 / 0.07225643528832329 / 5.617489128540022 | [NPY](tensors/0004521.npy) |
| 4522 | `model.layers.11.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.328125 / 1.015625 / -0.13145160675048828 / 0.6617914631006628 | [NPY](tensors/0004522.npy) |
| 4523 | `model.layers.11` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -296.0 / 404.0 / 0.4569129096137153 / 17.49826749688367 | [NPY](tensors/0004523.npy) |
| 4602 | `model.layers.11` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -268.0 / 388.0 / 0.2772015041775174 / 14.510444608260558 | [NPY](tensors/0004602.npy) |
| 4603 | `model.layers.11` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 344] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004603.npy) |
| 4604 | `model.layers.11` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.740966796875 / 0.9022817549113021 | [NPY](tensors/0004604.npy) |
| 4605 | `model.layers.11` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3046875 / -0.06294980645179749 / 0.6646640154085409 | [NPY](tensors/0004605.npy) |
| 4606 | `model.layers.11` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 343.0 / 343.0 / 343.0 / 0.0 | [NPY](tensors/0004606.npy) |
| 4607 | `model.layers.11` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4608 | `model.layers.11` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4609 | `model.layers.11` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4610 | `model.layers.11.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -268.0 / 388.0 / 0.2772015041775174 / 14.510444608260558 | [NPY](tensors/0004610.npy) |
| 4611 | `model.layers.11.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.0 / 99.0 / 0.05494998428556654 / 3.308171322698614 | [NPY](tensors/0004611.npy) |
| 4612 | `model.layers.11.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.0 / 99.0 / 0.05494998428556654 / 3.308171322698614 | [NPY](tensors/0004612.npy) |
| 4613 | `model.layers.11.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 344] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004613.npy) |
| 4614 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 343.0 / 343.0 / 343.0 / 0.0 | [NPY](tensors/0004614.npy) |
| 4615 | `model.layers.11.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4616 | `model.layers.11.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4617 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.740966796875 / 0.9022817549113021 | [NPY](tensors/0004617.npy) |
| 4618 | `model.layers.11.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3046875 / -0.06294980645179749 / 0.6646640154085409 | [NPY](tensors/0004618.npy) |
| 4619 | `model.layers.11.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4620 | `model.layers.11.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.0 / 99.0 / 0.05494998428556654 / 3.308171322698614 | [NPY](tensors/0004620.npy) |
| 4621 | `model.layers.11.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.84375 / 7.6875 / 0.06557046109810472 / 1.1905432548590338 | [NPY](tensors/0004621.npy) |
| 4622 | `model.layers.11.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.0 / 99.0 / 0.05494998428556654 / 3.308171322698614 | [NPY](tensors/0004622.npy) |
| 4623 | `model.layers.11.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -26.375 / 32.0 / 0.21344859898090363 / 3.296484787689683 | [NPY](tensors/0004623.npy) |
| 4624 | `model.layers.11.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -97.0 / 99.0 / 0.05494998428556654 / 3.308171322698614 | [NPY](tensors/0004624.npy) |
| 4625 | `model.layers.11.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.6875 / 6.75 / 0.05904871225357056 / 1.82154950608211 | [NPY](tensors/0004625.npy) |
| 4626 | `model.layers.11.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.125 / 5.0625 / -0.013676505768671632 / 1.2064900498998081 | [NPY](tensors/0004626.npy) |
| 4627 | `model.layers.11.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.25 / 63.0 / -0.028196191125445896 / 3.6287863919632604 | [NPY](tensors/0004627.npy) |
| 4628 | `model.layers.11.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -53.25 / 63.0 / -0.028196191125445896 / 3.6287863919632604 | [NPY](tensors/0004628.npy) |
| 4629 | `model.layers.11.self_attn` | 39 | `output[1]` | [1, 64, 1, 344] | torch.bfloat16 → float32 | 2.582964953035116e-10 / 0.9296875 / 0.002794711136470919 / 0.011834524243428781 | [NPY](tensors/0004629.npy) |
| 4630 | `model.layers.11.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -216.0 / 374.0 / 0.24860602484809027 / 14.946883820383016 | [NPY](tensors/0004630.npy) |
| 4631 | `model.layers.11.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.9375 / 4.34375 / -0.0026892383893330893 / 0.6433259258193207 | [NPY](tensors/0004631.npy) |
| 4632 | `model.layers.11.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.9375 / 4.34375 / -0.0026892383893330893 / 0.6433259258193207 | [NPY](tensors/0004632.npy) |
| 4633 | `model.layers.11.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.9375 / 4.34375 / -0.0026892383893330893 / 0.6433259258193207 | [NPY](tensors/0004633.npy) |
| 4634 | `model.layers.11.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4635 | `model.layers.11.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4636 | `model.layers.11.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4637 | `model.layers.11.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -104.0 / 65.0 / -0.05312412447399563 / 3.997902958844063 | [NPY](tensors/0004637.npy) |
| 4638 | `model.layers.11.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -104.0 / 65.0 / -0.05312412447399563 / 3.997902958844063 | [NPY](tensors/0004638.npy) |
| 4639 | `model.layers.11.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8359375 / 0.7109375 / -0.12349236011505127 / 0.5358169925049239 | [NPY](tensors/0004639.npy) |
| 4640 | `model.layers.11` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -320.0 / 422.0 / 0.19563768174913193 / 17.017357039941363 | [NPY](tensors/0004640.npy) |
| 4719 | `model.layers.11` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -374.0 / 552.0 / 0.6999243842230902 / 22.170683725047198 | [NPY](tensors/0004719.npy) |
| 4720 | `model.layers.11` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 345] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004720.npy) |
| 4721 | `model.layers.11` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8131542205810547 / 0.8233916239555151 | [NPY](tensors/0004721.npy) |
| 4722 | `model.layers.11` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.07140964269638062 / 0.6820182328303498 | [NPY](tensors/0004722.npy) |
| 4723 | `model.layers.11` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 344.0 / 344.0 / 344.0 / 0.0 | [NPY](tensors/0004723.npy) |
| 4724 | `model.layers.11` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4725 | `model.layers.11` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4726 | `model.layers.11` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4727 | `model.layers.11.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -374.0 / 552.0 / 0.6999243842230902 / 22.170683725047198 | [NPY](tensors/0004727.npy) |
| 4728 | `model.layers.11.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 116.5 / 0.08340355157852172 / 3.28425026486836 | [NPY](tensors/0004728.npy) |
| 4729 | `model.layers.11.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 116.5 / 0.08340355157852172 / 3.28425026486836 | [NPY](tensors/0004729.npy) |
| 4730 | `model.layers.11.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 345] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004730.npy) |
| 4731 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 344.0 / 344.0 / 344.0 / 0.0 | [NPY](tensors/0004731.npy) |
| 4732 | `model.layers.11.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4733 | `model.layers.11.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4734 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8131542205810547 / 0.8233916239555151 | [NPY](tensors/0004734.npy) |
| 4735 | `model.layers.11.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.07140964269638062 / 0.6820182328303498 | [NPY](tensors/0004735.npy) |
| 4736 | `model.layers.11.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4737 | `model.layers.11.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 116.5 / 0.08340355157852172 / 3.28425026486836 | [NPY](tensors/0004737.npy) |
| 4738 | `model.layers.11.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.09375 / 9.25 / 0.04451028257608414 / 1.2914391086859451 | [NPY](tensors/0004738.npy) |
| 4739 | `model.layers.11.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 116.5 / 0.08340355157852172 / 3.28425026486836 | [NPY](tensors/0004739.npy) |
| 4740 | `model.layers.11.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.375 / 34.75 / 0.04196806997060776 / 3.6957485457560093 | [NPY](tensors/0004740.npy) |
| 4741 | `model.layers.11.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -88.5 / 116.5 / 0.08340355157852172 / 3.28425026486836 | [NPY](tensors/0004741.npy) |
| 4742 | `model.layers.11.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.5 / 9.8125 / -0.024666547775268555 / 2.373735384848612 | [NPY](tensors/0004742.npy) |
| 4743 | `model.layers.11.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.625 / 5.75 / 0.00156651739962399 / 1.246772731092994 | [NPY](tensors/0004743.npy) |
| 4744 | `model.layers.11.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -203.0 / 200.0 / -0.05947893725501167 / 6.459370201735934 | [NPY](tensors/0004744.npy) |
| 4745 | `model.layers.11.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -203.0 / 200.0 / -0.05947893725501167 / 6.459370201735934 | [NPY](tensors/0004745.npy) |
| 4746 | `model.layers.11.self_attn` | 40 | `output[1]` | [1, 64, 1, 345] | torch.bfloat16 → float32 | 2.091837814077735e-11 / 0.9140625 / 0.002478701383182604 / 0.01172409028754773 | [NPY](tensors/0004746.npy) |
| 4747 | `model.layers.11.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -182.0 / 348.0 / 0.6399190266927083 / 19.43355028217583 | [NPY](tensors/0004747.npy) |
| 4748 | `model.layers.11.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.125 / 5.3125 / 0.015603039662043254 / 0.7341764738861201 | [NPY](tensors/0004748.npy) |
| 4749 | `model.layers.11.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.125 / 5.3125 / 0.015603039662043254 / 0.7341764738861201 | [NPY](tensors/0004749.npy) |
| 4750 | `model.layers.11.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.125 / 5.3125 / 0.015603039662043254 / 0.7341764738861201 | [NPY](tensors/0004750.npy) |
| 4751 | `model.layers.11.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4752 | `model.layers.11.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4753 | `model.layers.11.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4754 | `model.layers.11.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -298.0 / 304.0 / 0.3573382642534044 / 10.529545246781037 | [NPY](tensors/0004754.npy) |
| 4755 | `model.layers.11.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -298.0 / 304.0 / 0.3573382642534044 / 10.529545246781037 | [NPY](tensors/0004755.npy) |
| 4756 | `model.layers.11.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.4375 / 1.984375 / -0.18452835083007812 / 0.9794805258902826 | [NPY](tensors/0004756.npy) |
| 4757 | `model.layers.11` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -472.0 / 652.0 / 0.9969883388943143 / 26.549520708569023 | [NPY](tensors/0004757.npy) |
| 4836 | `model.layers.11` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -404.0 / 540.0 / 0.5592815823025173 / 21.068704129278665 | [NPY](tensors/0004836.npy) |
| 4837 | `model.layers.11` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 346] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004837.npy) |
| 4838 | `model.layers.11` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.8764495849609375 / 0.8009113437243138 | [NPY](tensors/0004838.npy) |
| 4839 | `model.layers.11` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.020697563886642456 / 0.632324519915983 | [NPY](tensors/0004839.npy) |
| 4840 | `model.layers.11` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 345.0 / 345.0 / 345.0 / 0.0 | [NPY](tensors/0004840.npy) |
| 4841 | `model.layers.11` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4842 | `model.layers.11` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4843 | `model.layers.11` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4844 | `model.layers.11.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -404.0 / 540.0 / 0.5592815823025173 / 21.068704129278665 | [NPY](tensors/0004844.npy) |
| 4845 | `model.layers.11.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 120.0 / 0.07153825826115079 / 3.4884131879145683 | [NPY](tensors/0004845.npy) |
| 4846 | `model.layers.11.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 120.0 / 0.07153825826115079 / 3.4884131879145683 | [NPY](tensors/0004846.npy) |
| 4847 | `model.layers.11.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 346] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004847.npy) |
| 4848 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 345.0 / 345.0 / 345.0 / 0.0 | [NPY](tensors/0004848.npy) |
| 4849 | `model.layers.11.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4850 | `model.layers.11.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4851 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.8764495849609375 / 0.8009113437243138 | [NPY](tensors/0004851.npy) |
| 4852 | `model.layers.11.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.020697563886642456 / 0.632324519915983 | [NPY](tensors/0004852.npy) |
| 4853 | `model.layers.11.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4854 | `model.layers.11.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 120.0 / 0.07153825826115079 / 3.4884131879145683 | [NPY](tensors/0004854.npy) |
| 4855 | `model.layers.11.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.46875 / 6.625 / 0.030091654509305954 / 1.185934786545575 | [NPY](tensors/0004855.npy) |
| 4856 | `model.layers.11.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 120.0 / 0.07153825826115079 / 3.4884131879145683 | [NPY](tensors/0004856.npy) |
| 4857 | `model.layers.11.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -29.875 / 36.5 / 0.07767842710018158 / 3.5277577779287665 | [NPY](tensors/0004857.npy) |
| 4858 | `model.layers.11.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -100.5 / 120.0 / 0.07153825826115079 / 3.4884131879145683 | [NPY](tensors/0004858.npy) |
| 4859 | `model.layers.11.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.9375 / 6.21875 / 0.06404000520706177 / 1.8622204265770068 | [NPY](tensors/0004859.npy) |
| 4860 | `model.layers.11.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.71875 / 6.0625 / 0.0074002682231366634 / 1.2019703100663703 | [NPY](tensors/0004860.npy) |
| 4861 | `model.layers.11.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -167.0 / 182.0 / -0.039922300974527994 / 5.928617100379548 | [NPY](tensors/0004861.npy) |
| 4862 | `model.layers.11.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -167.0 / 182.0 / -0.039922300974527994 / 5.928617100379548 | [NPY](tensors/0004862.npy) |
| 4863 | `model.layers.11.self_attn` | 41 | `output[1]` | [1, 64, 1, 346] | torch.bfloat16 → float32 | 2.8535396268125623e-11 / 0.96875 / 0.002622853651552507 / 0.012198419794218398 | [NPY](tensors/0004863.npy) |
| 4864 | `model.layers.11.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -222.0 / 372.0 / 0.5190667046440972 / 18.740383059036105 | [NPY](tensors/0004864.npy) |
| 4865 | `model.layers.11.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.28125 / 3.8125 / 0.013914555973476834 / 0.7193736181219388 | [NPY](tensors/0004865.npy) |
| 4866 | `model.layers.11.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.28125 / 3.8125 / 0.013914555973476834 / 0.7193736181219388 | [NPY](tensors/0004866.npy) |
| 4867 | `model.layers.11.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.28125 / 3.8125 / 0.013914555973476834 / 0.7193736181219388 | [NPY](tensors/0004867.npy) |
| 4868 | `model.layers.11.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4869 | `model.layers.11.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4870 | `model.layers.11.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4871 | `model.layers.11.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -200.0 / 215.0 / 0.1091146575080024 / 8.914708455753246 | [NPY](tensors/0004871.npy) |
| 4872 | `model.layers.11.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -200.0 / 215.0 / 0.1091146575080024 / 8.914708455753246 | [NPY](tensors/0004872.npy) |
| 4873 | `model.layers.11.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.828125 / 1.625 / -0.12299728393554688 / 0.7773432766727074 | [NPY](tensors/0004873.npy) |
| 4874 | `model.layers.11` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -422.0 / 588.0 / 0.6273247612847223 / 24.759407719980928 | [NPY](tensors/0004874.npy) |
| 4953 | `model.layers.11` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -470.0 / 616.0 / 0.37106560601128474 / 24.283925539214273 | [NPY](tensors/0004953.npy) |
| 4954 | `model.layers.11` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 347] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004954.npy) |
| 4955 | `model.layers.11` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.887237548828125 / 0.808167570442007 | [NPY](tensors/0004955.npy) |
| 4956 | `model.layers.11` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.06384772062301636 / 0.6046658936992718 | [NPY](tensors/0004956.npy) |
| 4957 | `model.layers.11` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 346.0 / 346.0 / 346.0 / 0.0 | [NPY](tensors/0004957.npy) |
| 4958 | `model.layers.11` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4959 | `model.layers.11` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4960 | `model.layers.11` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4961 | `model.layers.11.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -470.0 / 616.0 / 0.37106560601128474 / 24.283925539214273 | [NPY](tensors/0004961.npy) |
| 4962 | `model.layers.11.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 119.0 / 0.049741829766167533 / 3.4293895691488556 | [NPY](tensors/0004962.npy) |
| 4963 | `model.layers.11.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 119.0 / 0.049741829766167533 / 3.4293895691488556 | [NPY](tensors/0004963.npy) |
| 4964 | `model.layers.11.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 347] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004964.npy) |
| 4965 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 346.0 / 346.0 / 346.0 / 0.0 | [NPY](tensors/0004965.npy) |
| 4966 | `model.layers.11.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4967 | `model.layers.11.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4968 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.887237548828125 / 0.808167570442007 | [NPY](tensors/0004968.npy) |
| 4969 | `model.layers.11.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.06384772062301636 / 0.6046658936992718 | [NPY](tensors/0004969.npy) |
| 4970 | `model.layers.11.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4971 | `model.layers.11.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 119.0 / 0.049741829766167533 / 3.4293895691488556 | [NPY](tensors/0004971.npy) |
| 4972 | `model.layers.11.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.3125 / 7.28125 / 0.03941674611996859 / 1.1566783390859858 | [NPY](tensors/0004972.npy) |
| 4973 | `model.layers.11.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 119.0 / 0.049741829766167533 / 3.4293895691488556 | [NPY](tensors/0004973.npy) |
| 4974 | `model.layers.11.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.25 / 38.0 / 0.020210742950439453 / 3.5042993108687783 | [NPY](tensors/0004974.npy) |
| 4975 | `model.layers.11.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -101.5 / 119.0 / 0.049741829766167533 / 3.4293895691488556 | [NPY](tensors/0004975.npy) |
| 4976 | `model.layers.11.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.46875 / 7.71875 / -0.09098035097122192 / 2.3312978549429277 | [NPY](tensors/0004976.npy) |
| 4977 | `model.layers.11.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.625 / 6.15625 / 0.009169083074084483 / 1.1924306567012233 | [NPY](tensors/0004977.npy) |
| 4978 | `model.layers.11.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -216.0 / 182.0 / -0.12477611369556851 / 6.514157677829998 | [NPY](tensors/0004978.npy) |
| 4979 | `model.layers.11.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -216.0 / 182.0 / -0.12477611369556851 / 6.514157677829998 | [NPY](tensors/0004979.npy) |
| 4980 | `model.layers.11.self_attn` | 42 | `output[1]` | [1, 64, 1, 347] | torch.bfloat16 → float32 | 6.572520305780927e-13 / 0.953125 / 0.0025137953432537315 / 0.014350493448064565 | [NPY](tensors/0004980.npy) |
| 4981 | `model.layers.11.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -288.0 / 400.0 / 0.24660907321506076 / 21.45917950128935 | [NPY](tensors/0004981.npy) |
| 4982 | `model.layers.11.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.0 / 4.03125 / 0.0023481170336405437 / 0.7639492834224587 | [NPY](tensors/0004982.npy) |
| 4983 | `model.layers.11.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.0 / 4.03125 / 0.0023481170336405437 / 0.7639492834224587 | [NPY](tensors/0004983.npy) |
| 4984 | `model.layers.11.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.0 / 4.03125 / 0.0023481170336405437 / 0.7639492834224587 | [NPY](tensors/0004984.npy) |
| 4985 | `model.layers.11.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4986 | `model.layers.11.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4987 | `model.layers.11.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4988 | `model.layers.11.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -300.0 / 312.0 / -0.02751913070678711 / 11.309509145097921 | [NPY](tensors/0004988.npy) |
| 4989 | `model.layers.11.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -300.0 / 312.0 / -0.02751913070678711 / 11.309509145097921 | [NPY](tensors/0004989.npy) |
| 4990 | `model.layers.11.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.015625 / 1.7265625 / -0.134700745344162 / 0.8117607164270964 | [NPY](tensors/0004990.npy) |
| 4991 | `model.layers.11` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -588.0 / 712.0 / 0.21903788248697917 / 29.36049407443782 | [NPY](tensors/0004991.npy) |
| 5070 | `model.layers.11` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -436.0 / 552.0 / 0.22920650906032985 / 20.964573598320296 | [NPY](tensors/0005070.npy) |
| 5071 | `model.layers.11` | 43 | `input.kwargs['attention_mask']` | [1, 1, 1, 348] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005071.npy) |
| 5072 | `model.layers.11` | 43 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.8368129730224609 / 0.8204651963806046 | [NPY](tensors/0005072.npy) |
| 5073 | `model.layers.11` | 43 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.1309933364391327 / 0.6478045244450656 | [NPY](tensors/0005073.npy) |
| 5074 | `model.layers.11` | 43 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 347.0 / 347.0 / 347.0 / 0.0 | [NPY](tensors/0005074.npy) |
| 5075 | `model.layers.11` | 43 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5076 | `model.layers.11` | 43 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5077 | `model.layers.11` | 43 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5078 | `model.layers.11.input_layernorm` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -436.0 / 552.0 / 0.22920650906032985 / 20.964573598320296 | [NPY](tensors/0005078.npy) |
| 5079 | `model.layers.11.input_layernorm` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 123.5 / 0.046279326412412856 / 3.537674996915276 | [NPY](tensors/0005079.npy) |
| 5080 | `model.layers.11.self_attn` | 43 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 123.5 / 0.046279326412412856 / 3.537674996915276 | [NPY](tensors/0005080.npy) |
| 5081 | `model.layers.11.self_attn` | 43 | `input.kwargs['attention_mask']` | [1, 1, 1, 348] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005081.npy) |
| 5082 | `model.layers.11.self_attn` | 43 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 347.0 / 347.0 / 347.0 / 0.0 | [NPY](tensors/0005082.npy) |
| 5083 | `model.layers.11.self_attn` | 43 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5084 | `model.layers.11.self_attn` | 43 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5085 | `model.layers.11.self_attn` | 43 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.8368129730224609 / 0.8204651963806046 | [NPY](tensors/0005085.npy) |
| 5086 | `model.layers.11.self_attn` | 43 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.1309933364391327 / 0.6478045244450656 | [NPY](tensors/0005086.npy) |
| 5087 | `model.layers.11.self_attn` | 43 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5088 | `model.layers.11.self_attn.q_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 123.5 / 0.046279326412412856 / 3.537674996915276 | [NPY](tensors/0005088.npy) |
| 5089 | `model.layers.11.self_attn.q_proj` | 43 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.375 / 8.125 / 0.037478608544915915 / 1.1147869307280946 | [NPY](tensors/0005089.npy) |
| 5090 | `model.layers.11.self_attn.k_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 123.5 / 0.046279326412412856 / 3.537674996915276 | [NPY](tensors/0005090.npy) |
| 5091 | `model.layers.11.self_attn.k_proj` | 43 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.625 / 38.0 / 0.06249678134918213 / 3.384273092685948 | [NPY](tensors/0005091.npy) |
| 5092 | `model.layers.11.self_attn.v_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -109.0 / 123.5 / 0.046279326412412856 / 3.537674996915276 | [NPY](tensors/0005092.npy) |
| 5093 | `model.layers.11.self_attn.v_proj` | 43 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -5.65625 / 6.03125 / -0.02855515480041504 / 1.9434428736041285 | [NPY](tensors/0005093.npy) |
| 5094 | `model.layers.11.self_attn.o_proj` | 43 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.4375 / 5.84375 / 0.003424679860472679 / 1.1586775855097788 | [NPY](tensors/0005094.npy) |
| 5095 | `model.layers.11.self_attn.o_proj` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -188.0 / 164.0 / -0.09182402292887369 / 5.8657525734225 | [NPY](tensors/0005095.npy) |
| 5096 | `model.layers.11.self_attn` | 43 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -188.0 / 164.0 / -0.09182402292887369 / 5.8657525734225 | [NPY](tensors/0005096.npy) |
| 5097 | `model.layers.11.self_attn` | 43 | `output[1]` | [1, 64, 1, 348] | torch.bfloat16 → float32 | 1.7195134205394424e-12 / 0.9140625 / 0.002527099347315534 / 0.012669163948705068 | [NPY](tensors/0005097.npy) |
| 5098 | `model.layers.11.post_attention_layernorm` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -272.0 / 364.0 / 0.13752966986762152 / 18.379380035305868 | [NPY](tensors/0005098.npy) |
| 5099 | `model.layers.11.post_attention_layernorm` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.1875 / 4.40625 / 0.006329892741309272 / 0.7485463518648958 | [NPY](tensors/0005099.npy) |
| 5100 | `model.layers.11.mlp` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4.1875 / 4.40625 / 0.006329892741309272 / 0.7485463518648958 | [NPY](tensors/0005100.npy) |
| 5101 | `model.layers.11.mlp.experts` | 43 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -4.1875 / 4.40625 / 0.006329892741309272 / 0.7485463518648958 | [NPY](tensors/0005101.npy) |
| 5102 | `model.layers.11.mlp.experts` | 43 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5103 | `model.layers.11.mlp.experts` | 43 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5104 | `model.layers.11.mlp.experts` | 43 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5105 | `model.layers.11.mlp.experts` | 43 | `output` | [1, 2880] | torch.bfloat16 → float32 | -232.0 / 272.0 / -0.06925905810462105 / 9.884645594467294 | [NPY](tensors/0005105.npy) |
| 5106 | `model.layers.11.mlp` | 43 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -232.0 / 272.0 / -0.06925905810462105 / 9.884645594467294 | [NPY](tensors/0005106.npy) |
| 5107 | `model.layers.11.mlp` | 43 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.8671875 / 1.546875 / -0.14138031005859375 / 0.7237556197824907 | [NPY](tensors/0005107.npy) |
| 5108 | `model.layers.11` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -504.0 / 636.0 / 0.06943495008680556 / 25.310279974543565 | [NPY](tensors/0005108.npy) |
| 5187 | `model.layers.11` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -548.0 / 576.0 / 0.7103156195746527 / 24.976542157870284 | [NPY](tensors/0005187.npy) |
| 5188 | `model.layers.11` | 44 | `input.kwargs['attention_mask']` | [1, 1, 1, 349] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005188.npy) |
| 5189 | `model.layers.11` | 44 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7588653564453125 / 0.8828955932720353 | [NPY](tensors/0005189.npy) |
| 5190 | `model.layers.11` | 44 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14290890097618103 / 0.6590419455082627 | [NPY](tensors/0005190.npy) |
| 5191 | `model.layers.11` | 44 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 348.0 / 348.0 / 348.0 / 0.0 | [NPY](tensors/0005191.npy) |
| 5192 | `model.layers.11` | 44 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5193 | `model.layers.11` | 44 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5194 | `model.layers.11` | 44 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5195 | `model.layers.11.input_layernorm` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -548.0 / 576.0 / 0.7103156195746527 / 24.976542157870284 | [NPY](tensors/0005195.npy) |
| 5196 | `model.layers.11.input_layernorm` | 44 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -115.0 / 108.0 / 0.06803161965476143 / 3.4140123796018247 | [NPY](tensors/0005196.npy) |
| 5197 | `model.layers.11.self_attn` | 44 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -115.0 / 108.0 / 0.06803161965476143 / 3.4140123796018247 | [NPY](tensors/0005197.npy) |
| 5198 | `model.layers.11.self_attn` | 44 | `input.kwargs['attention_mask']` | [1, 1, 1, 349] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005198.npy) |
| 5199 | `model.layers.11.self_attn` | 44 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 348.0 / 348.0 / 348.0 / 0.0 | [NPY](tensors/0005199.npy) |
| 5200 | `model.layers.11.self_attn` | 44 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5201 | `model.layers.11.self_attn` | 44 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5202 | `model.layers.11.self_attn` | 44 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7588653564453125 / 0.8828955932720353 | [NPY](tensors/0005202.npy) |
| 5203 | `model.layers.11.self_attn` | 44 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14290890097618103 / 0.6590419455082627 | [NPY](tensors/0005203.npy) |
| 5204 | `model.layers.11.self_attn` | 44 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5205 | `model.layers.11.self_attn.q_proj` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -115.0 / 108.0 / 0.06803161965476143 / 3.4140123796018247 | [NPY](tensors/0005205.npy) |
| 5206 | `model.layers.11.self_attn.q_proj` | 44 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.625 / 8.875 / 0.057741365337278694 / 1.2482251133888003 | [NPY](tensors/0005206.npy) |
| 5207 | `model.layers.11.self_attn.k_proj` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -115.0 / 108.0 / 0.06803161965476143 / 3.4140123796018247 | [NPY](tensors/0005207.npy) |
| 5208 | `model.layers.11.self_attn.k_proj` | 44 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.0 / 33.75 / 0.11013352870941162 / 3.525176643786406 | [NPY](tensors/0005208.npy) |
| 5209 | `model.layers.11.self_attn.v_proj` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -115.0 / 108.0 / 0.06803161965476143 / 3.4140123796018247 | [NPY](tensors/0005209.npy) |
| 5210 | `model.layers.11.self_attn.v_proj` | 44 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -6.75 / 7.5 / 0.009892359375953674 / 2.5170464215775046 | [NPY](tensors/0005210.npy) |
| 5211 | `model.layers.11.self_attn.o_proj` | 44 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.46875 / 6.34375 / -0.016508388482179726 / 1.1141242585711821 | [NPY](tensors/0005211.npy) |
| 5212 | `model.layers.11.self_attn.o_proj` | 44 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -243.0 / 255.0 / -0.20036845207214354 / 7.4833097084289 | [NPY](tensors/0005212.npy) |
| 5213 | `model.layers.11.self_attn` | 44 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -243.0 / 255.0 / -0.20036845207214354 / 7.4833097084289 | [NPY](tensors/0005213.npy) |
| 5214 | `model.layers.11.self_attn` | 44 | `output[1]` | [1, 64, 1, 349] | torch.bfloat16 → float32 | 5.435651928564766e-13 / 0.89453125 / 0.002151200819446445 / 0.016445940130576955 | [NPY](tensors/0005214.npy) |
| 5215 | `model.layers.11.post_attention_layernorm` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -292.0 / 332.0 / 0.5098470052083334 / 21.45792035111288 | [NPY](tensors/0005215.npy) |
| 5216 | `model.layers.11.post_attention_layernorm` | 44 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.453125 / 5.53125 / 0.00741156604554918 / 0.8077794825955505 | [NPY](tensors/0005216.npy) |
| 5217 | `model.layers.11.mlp` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.453125 / 5.53125 / 0.00741156604554918 / 0.8077794825955505 | [NPY](tensors/0005217.npy) |
| 5218 | `model.layers.11.mlp.experts` | 44 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.453125 / 5.53125 / 0.00741156604554918 / 0.8077794825955505 | [NPY](tensors/0005218.npy) |
| 5219 | `model.layers.11.mlp.experts` | 44 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5220 | `model.layers.11.mlp.experts` | 44 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5221 | `model.layers.11.mlp.experts` | 44 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5222 | `model.layers.11.mlp.experts` | 44 | `output` | [1, 2880] | torch.bfloat16 → float32 | -344.0 / 256.0 / 0.08162732521692911 / 11.448789109139685 | [NPY](tensors/0005222.npy) |
| 5223 | `model.layers.11.mlp` | 44 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -344.0 / 256.0 / 0.08162732521692911 / 11.448789109139685 | [NPY](tensors/0005223.npy) |
| 5224 | `model.layers.11.mlp` | 44 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.328125 / 1.671875 / -0.1721935272216797 / 0.8734230836305913 | [NPY](tensors/0005224.npy) |
| 5225 | `model.layers.11` | 44 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -636.0 / 588.0 / 0.5921702914767795 / 28.76116589148917 | [NPY](tensors/0005225.npy) |
| 5304 | `model.layers.11` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 468.0 / 0.8350816514756945 / 20.860717010856636 | [NPY](tensors/0005304.npy) |
| 5305 | `model.layers.11` | 45 | `input.kwargs['attention_mask']` | [1, 1, 1, 350] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005305.npy) |
| 5306 | `model.layers.11` | 45 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.701873779296875 / 0.9298159802037973 | [NPY](tensors/0005306.npy) |
| 5307 | `model.layers.11` | 45 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.10132250189781189 / 0.6650396518932735 | [NPY](tensors/0005307.npy) |
| 5308 | `model.layers.11` | 45 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 349.0 / 349.0 / 349.0 / 0.0 | [NPY](tensors/0005308.npy) |
| 5309 | `model.layers.11` | 45 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5310 | `model.layers.11` | 45 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5311 | `model.layers.11` | 45 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5312 | `model.layers.11.input_layernorm` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -312.0 / 468.0 / 0.8350816514756945 / 20.860717010856636 | [NPY](tensors/0005312.npy) |
| 5313 | `model.layers.11.input_layernorm` | 45 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -78.5 / 105.0 / 0.09562639130486382 / 3.1350572652185202 | [NPY](tensors/0005313.npy) |
| 5314 | `model.layers.11.self_attn` | 45 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -78.5 / 105.0 / 0.09562639130486382 / 3.1350572652185202 | [NPY](tensors/0005314.npy) |
| 5315 | `model.layers.11.self_attn` | 45 | `input.kwargs['attention_mask']` | [1, 1, 1, 350] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005315.npy) |
| 5316 | `model.layers.11.self_attn` | 45 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 349.0 / 349.0 / 349.0 / 0.0 | [NPY](tensors/0005316.npy) |
| 5317 | `model.layers.11.self_attn` | 45 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5318 | `model.layers.11.self_attn` | 45 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5319 | `model.layers.11.self_attn` | 45 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.701873779296875 / 0.9298159802037973 | [NPY](tensors/0005319.npy) |
| 5320 | `model.layers.11.self_attn` | 45 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.10132250189781189 / 0.6650396518932735 | [NPY](tensors/0005320.npy) |
| 5321 | `model.layers.11.self_attn` | 45 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5322 | `model.layers.11.self_attn.q_proj` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -78.5 / 105.0 / 0.09562639130486382 / 3.1350572652185202 | [NPY](tensors/0005322.npy) |
| 5323 | `model.layers.11.self_attn.q_proj` | 45 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.0 / 9.25 / 0.05631444533355534 / 1.3054429046273461 | [NPY](tensors/0005323.npy) |
| 5324 | `model.layers.11.self_attn.k_proj` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -78.5 / 105.0 / 0.09562639130486382 / 3.1350572652185202 | [NPY](tensors/0005324.npy) |
| 5325 | `model.layers.11.self_attn.k_proj` | 45 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.875 / 30.5 / 0.08006582036614418 / 3.6245674580465255 | [NPY](tensors/0005325.npy) |
| 5326 | `model.layers.11.self_attn.v_proj` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -78.5 / 105.0 / 0.09562639130486382 / 3.1350572652185202 | [NPY](tensors/0005326.npy) |
| 5327 | `model.layers.11.self_attn.v_proj` | 45 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.625 / 8.0625 / 1.119077205657959e-05 / 2.6532033323977586 | [NPY](tensors/0005327.npy) |
| 5328 | `model.layers.11.self_attn.o_proj` | 45 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -5.90625 / 7.0625 / 0.000861145555973053 / 1.3699520455148542 | [NPY](tensors/0005328.npy) |
| 5329 | `model.layers.11.self_attn.o_proj` | 45 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 109.5 / -0.13448667062653435 / 4.721365876820147 | [NPY](tensors/0005329.npy) |
| 5330 | `model.layers.11.self_attn` | 45 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -98.5 / 109.5 / -0.13448667062653435 / 4.721365876820147 | [NPY](tensors/0005330.npy) |
| 5331 | `model.layers.11.self_attn` | 45 | `output[1]` | [1, 64, 1, 350] | torch.bfloat16 → float32 | 1.3784529073745944e-12 / 0.94140625 / 0.0026202607095899637 / 0.01424665049456096 | [NPY](tensors/0005331.npy) |
| 5332 | `model.layers.11.post_attention_layernorm` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -202.0 / 370.0 / 0.7013215806749132 / 20.142006634994576 | [NPY](tensors/0005332.npy) |
| 5333 | `model.layers.11.post_attention_layernorm` | 45 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.0 / 3.09375 / 0.023758288224538168 / 0.7722004747987146 | [NPY](tensors/0005333.npy) |
| 5334 | `model.layers.11.mlp` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3.0 / 3.09375 / 0.023758288224538168 / 0.7722004747987146 | [NPY](tensors/0005334.npy) |
| 5335 | `model.layers.11.mlp.experts` | 45 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -3.0 / 3.09375 / 0.023758288224538168 / 0.7722004747987146 | [NPY](tensors/0005335.npy) |
| 5336 | `model.layers.11.mlp.experts` | 45 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5337 | `model.layers.11.mlp.experts` | 45 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5338 | `model.layers.11.mlp.experts` | 45 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5339 | `model.layers.11.mlp.experts` | 45 | `output` | [1, 2880] | torch.bfloat16 → float32 | -240.0 / 302.0 / 0.08655701743231879 / 10.729945795132851 | [NPY](tensors/0005339.npy) |
| 5340 | `model.layers.11.mlp` | 45 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -240.0 / 302.0 / 0.08655701743231879 / 10.729945795132851 | [NPY](tensors/0005340.npy) |
| 5341 | `model.layers.11.mlp` | 45 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2578125 / -0.08652114868164062 / 0.5336267415859919 | [NPY](tensors/0005341.npy) |
| 5342 | `model.layers.11` | 45 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -442.0 / 672.0 / 0.7869594997829861 / 27.507338324012135 | [NPY](tensors/0005342.npy) |
| 5421 | `model.layers.11` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -252.0 / 392.0 / 0.6900846693250868 / 18.840768567233972 | [NPY](tensors/0005421.npy) |
| 5422 | `model.layers.11` | 46 | `input.kwargs['attention_mask']` | [1, 1, 1, 351] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005422.npy) |
| 5423 | `model.layers.11` | 46 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.690826416015625 / 0.927895842605205 | [NPY](tensors/0005423.npy) |
| 5424 | `model.layers.11` | 46 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.04170632362365723 / 0.685352030153117 | [NPY](tensors/0005424.npy) |
| 5425 | `model.layers.11` | 46 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 350.0 / 350.0 / 350.0 / 0.0 | [NPY](tensors/0005425.npy) |
| 5426 | `model.layers.11` | 46 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5427 | `model.layers.11` | 46 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5428 | `model.layers.11` | 46 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5429 | `model.layers.11.input_layernorm` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -252.0 / 392.0 / 0.6900846693250868 / 18.840768567233972 | [NPY](tensors/0005429.npy) |
| 5430 | `model.layers.11.input_layernorm` | 46 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 97.5 / 0.09894609053929647 / 2.986716051708106 | [NPY](tensors/0005430.npy) |
| 5431 | `model.layers.11.self_attn` | 46 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 97.5 / 0.09894609053929647 / 2.986716051708106 | [NPY](tensors/0005431.npy) |
| 5432 | `model.layers.11.self_attn` | 46 | `input.kwargs['attention_mask']` | [1, 1, 1, 351] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005432.npy) |
| 5433 | `model.layers.11.self_attn` | 46 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 350.0 / 350.0 / 350.0 / 0.0 | [NPY](tensors/0005433.npy) |
| 5434 | `model.layers.11.self_attn` | 46 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5435 | `model.layers.11.self_attn` | 46 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5436 | `model.layers.11.self_attn` | 46 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.690826416015625 / 0.927895842605205 | [NPY](tensors/0005436.npy) |
| 5437 | `model.layers.11.self_attn` | 46 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.04170632362365723 / 0.685352030153117 | [NPY](tensors/0005437.npy) |
| 5438 | `model.layers.11.self_attn` | 46 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5439 | `model.layers.11.self_attn.q_proj` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 97.5 / 0.09894609053929647 / 2.986716051708106 | [NPY](tensors/0005439.npy) |
| 5440 | `model.layers.11.self_attn.q_proj` | 46 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.75 / 8.4375 / 0.04448364954441786 / 1.3289107772517648 | [NPY](tensors/0005440.npy) |
| 5441 | `model.layers.11.self_attn.k_proj` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 97.5 / 0.09894609053929647 / 2.986716051708106 | [NPY](tensors/0005441.npy) |
| 5442 | `model.layers.11.self_attn.k_proj` | 46 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.875 / 33.75 / 0.09686035756021738 / 3.8544160504468454 | [NPY](tensors/0005442.npy) |
| 5443 | `model.layers.11.self_attn.v_proj` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -70.0 / 97.5 / 0.09894609053929647 / 2.986716051708106 | [NPY](tensors/0005443.npy) |
| 5444 | `model.layers.11.self_attn.v_proj` | 46 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -7.75 / 11.75 / 0.09395933151245117 / 2.62751064931047 | [NPY](tensors/0005444.npy) |
| 5445 | `model.layers.11.self_attn.o_proj` | 46 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -6.25 / 7.375 / 0.006731720641255379 / 1.3534995183525678 | [NPY](tensors/0005445.npy) |
| 5446 | `model.layers.11.self_attn.o_proj` | 46 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.75 / 79.5 / -0.024784993794229295 / 3.8092362884926145 | [NPY](tensors/0005446.npy) |
| 5447 | `model.layers.11.self_attn` | 46 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -63.75 / 79.5 / -0.024784993794229295 / 3.8092362884926145 | [NPY](tensors/0005447.npy) |
| 5448 | `model.layers.11.self_attn` | 46 | `output[1]` | [1, 64, 1, 351] | torch.bfloat16 → float32 | 2.05773176276125e-11 / 0.8984375 / 0.0026237169268010755 / 0.013087167742179932 | [NPY](tensors/0005448.npy) |
| 5449 | `model.layers.11.post_attention_layernorm` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -172.0 / 342.0 / 0.6646160549587674 / 18.645674917827527 | [NPY](tensors/0005449.npy) |
| 5450 | `model.layers.11.post_attention_layernorm` | 46 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.78125 / 2.9375 / 0.02691657344500224 / 0.766138724891338 | [NPY](tensors/0005450.npy) |
| 5451 | `model.layers.11.mlp` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2.78125 / 2.9375 / 0.02691657344500224 / 0.766138724891338 | [NPY](tensors/0005451.npy) |
| 5452 | `model.layers.11.mlp.experts` | 46 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -2.78125 / 2.9375 / 0.02691657344500224 / 0.766138724891338 | [NPY](tensors/0005452.npy) |
| 5453 | `model.layers.11.mlp.experts` | 46 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5454 | `model.layers.11.mlp.experts` | 46 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5455 | `model.layers.11.mlp.experts` | 46 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5456 | `model.layers.11.mlp.experts` | 46 | `output` | [1, 2880] | torch.bfloat16 → float32 | -186.0 / 187.0 / 0.11649236679077149 / 7.554671102985016 | [NPY](tensors/0005456.npy) |
| 5457 | `model.layers.11.mlp` | 46 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -186.0 / 187.0 / 0.11649236679077149 / 7.554671102985016 | [NPY](tensors/0005457.npy) |
| 5458 | `model.layers.11.mlp` | 46 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.90625 / 1.2265625 / -0.10329723358154297 / 0.69554149653332 | [NPY](tensors/0005458.npy) |
| 5459 | `model.layers.11` | 46 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -358.0 / 528.0 / 0.7812876383463542 / 23.50347612587499 | [NPY](tensors/0005459.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -2.1218596178065234 / 415.91059113379794 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 305, 305] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6892090857909291e+38 / 1.694756585406476e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 305, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7963737057857826 / 0.8801360272441033 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 305, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12046455383190091 / 0.6213787871646592 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 305] | torch.int64 → int64 | 0.0 / 304.0 / 152.0 / 88.04544281222056 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -2.1218596178065234 / 415.91059113379794 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 305, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.007222467059700434 / 1.7594104282140874 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 305, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.007222467059700434 / 1.7594104282140874 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 305, 305] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6892090857909291e+38 / 1.694756585406476e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 305] | torch.int64 → int64 | 0.0 / 304.0 / 152.0 / 88.04544281222056 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | True | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 305, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7963737057857826 / 0.8801360272441033 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 305, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12046455383190091 / 0.6213787871646592 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.007222467059700434 / 1.7594104282140874 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 305, 4096] | torch.bfloat16 → float32 | -18.5 / 24.25 / 0.0310429804404834 / 1.6535877699711667 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.007222467059700434 / 1.7594104282140874 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 305, 512] | torch.bfloat16 → float32 | -87.0 / 63.25 / -0.08898738027840364 / 5.014070728073474 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.007222467059700434 / 1.7594104282140874 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 305, 512] | torch.bfloat16 → float32 | -27.5 / 24.25 / 0.01808321554152692 / 3.247828710691316 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 305, 4096] | torch.bfloat16 → float32 | -25.75 / 12.9375 / 0.0009682356339371685 / 1.1302111216809296 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 305, 2880] | torch.bfloat16 → float32 | -6912.0 / 7232.0 / 2.560890149926879 / 164.36779880394067 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -6912.0 / 7232.0 / 2.560890149926879 / 164.36779880394067 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 305, 305] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0015655495632801823 / 0.011956269759309645 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -10496.0 / 11264.0 / 0.43861334128457996 / 359.7170987950198 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 305, 2880] | torch.bfloat16 → float32 | -49.0 / 25.5 / -0.016759140325917136 / 1.2282132363524298 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -49.0 / 25.5 / -0.016759140325917136 / 1.2282132363524298 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [305, 2880] | torch.bfloat16 → float32 | -49.0 / 25.5 / -0.016759140325917136 / 1.2282132363524298 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [305, 2880] | torch.bfloat16 → float32 | -4832.0 / 4736.0 / -1.562317157043568 / 149.7265566452393 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 305, 2880] | torch.bfloat16 → float32 | -4832.0 / 4736.0 / -1.562317157043568 / 149.7265566452393 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [305, 32] | torch.bfloat16 → float32 | -7.625 / 4.5625 / 0.24359242877022164 / 2.566862017053978 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 305, 2880] | torch.bfloat16 → float32 | -10816.0 / 10944.0 / -1.1249250079156705 / 407.33467768667595 | [NPY](tensors/0000116.npy) |
| 195 | `model.layers.23` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9792.0 / 10048.0 / -1.4266798231336806 / 438.057103582942 | [NPY](tensors/0000195.npy) |
| 196 | `model.layers.23` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 306] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000196.npy) |
| 197 | `model.layers.23` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0000197.npy) |
| 198 | `model.layers.23` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0000198.npy) |
| 199 | `model.layers.23` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0000199.npy) |
| 200 | `model.layers.23` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 201 | `model.layers.23` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 202 | `model.layers.23` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 203 | `model.layers.23.input_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9792.0 / 10048.0 / -1.4266798231336806 / 438.057103582942 | [NPY](tensors/0000203.npy) |
| 204 | `model.layers.23.input_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 61.75 / 0.007669621706008911 / 1.8003054975040986 | [NPY](tensors/0000204.npy) |
| 205 | `model.layers.23.self_attn` | 1 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 61.75 / 0.007669621706008911 / 1.8003054975040986 | [NPY](tensors/0000205.npy) |
| 206 | `model.layers.23.self_attn` | 1 | `input.kwargs['attention_mask']` | [1, 1, 1, 306] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000206.npy) |
| 207 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 305.0 / 305.0 / 305.0 / 0.0 | [NPY](tensors/0000207.npy) |
| 208 | `model.layers.23.self_attn` | 1 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 209 | `model.layers.23.self_attn` | 1 | `input.kwargs['use_cache']` | — | bool | True | — |
| 210 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.62603759765625 / 1.0779998247069276 | [NPY](tensors/0000210.npy) |
| 211 | `model.layers.23.self_attn` | 1 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -0.91796875 / 1.265625 / 0.06966635584831238 / 0.5006796949328058 | [NPY](tensors/0000211.npy) |
| 212 | `model.layers.23.self_attn` | 1 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 213 | `model.layers.23.self_attn.q_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 61.75 / 0.007669621706008911 / 1.8003054975040986 | [NPY](tensors/0000213.npy) |
| 214 | `model.layers.23.self_attn.q_proj` | 1 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.9375 / 18.75 / 0.04016726135159843 / 1.4339016008929146 | [NPY](tensors/0000214.npy) |
| 215 | `model.layers.23.self_attn.k_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 61.75 / 0.007669621706008911 / 1.8003054975040986 | [NPY](tensors/0000215.npy) |
| 216 | `model.layers.23.self_attn.k_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.25 / 38.75 / -0.20014747977256775 / 4.9580007704509725 | [NPY](tensors/0000216.npy) |
| 217 | `model.layers.23.self_attn.v_proj` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 61.75 / 0.007669621706008911 / 1.8003054975040986 | [NPY](tensors/0000217.npy) |
| 218 | `model.layers.23.self_attn.v_proj` | 1 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.75 / 7.90625 / -0.03775531053543091 / 2.408343741944624 | [NPY](tensors/0000218.npy) |
| 219 | `model.layers.23.self_attn.o_proj` | 1 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.75 / 5.71875 / -0.016618172638118267 / 0.9663656615279297 | [NPY](tensors/0000219.npy) |
| 220 | `model.layers.23.self_attn.o_proj` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 5888.0 / 5.742147699991862 / 250.22431320151435 | [NPY](tensors/0000220.npy) |
| 221 | `model.layers.23.self_attn` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 5888.0 / 5.742147699991862 / 250.22431320151435 | [NPY](tensors/0000221.npy) |
| 222 | `model.layers.23.self_attn` | 1 | `output[1]` | [1, 64, 1, 306] | torch.bfloat16 → float32 | 2.631228568361621e-14 / 0.8671875 / 0.001726680021338849 / 0.012247408877195207 | [NPY](tensors/0000222.npy) |
| 223 | `model.layers.23.post_attention_layernorm` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9984.0 / 10240.0 / 4.327713351779514 / 530.4797279215927 | [NPY](tensors/0000223.npy) |
| 224 | `model.layers.23.post_attention_layernorm` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.875 / 9.0 / -0.010434636804792617 / 0.9312966793419509 | [NPY](tensors/0000224.npy) |
| 225 | `model.layers.23.mlp` | 1 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -30.875 / 9.0 / -0.010434636804792617 / 0.9312966793419509 | [NPY](tensors/0000225.npy) |
| 226 | `model.layers.23.mlp.experts` | 1 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -30.875 / 9.0 / -0.010434636804792617 / 0.9312966793419509 | [NPY](tensors/0000226.npy) |
| 227 | `model.layers.23.mlp.experts` | 1 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 228 | `model.layers.23.mlp.experts` | 1 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 229 | `model.layers.23.mlp.experts` | 1 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 230 | `model.layers.23.mlp.experts` | 1 | `output` | [1, 2880] | torch.bfloat16 → float32 | -960.0 / 752.0 / -1.5546496550242106 / 61.715929129862424 | [NPY](tensors/0000230.npy) |
| 231 | `model.layers.23.mlp` | 1 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -960.0 / 752.0 / -1.5546496550242106 / 61.715929129862424 | [NPY](tensors/0000231.npy) |
| 232 | `model.layers.23.mlp` | 1 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.55078125 / 1.1328125 / 0.08843708038330078 / 0.32064641674092476 | [NPY](tensors/0000232.npy) |
| 233 | `model.layers.23` | 1 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9856.0 / 2.784435017903646 / 500.3889921207373 | [NPY](tensors/0000233.npy) |
| 312 | `model.layers.23` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 9984.0 / -0.18666178385416668 / 442.38929380599467 | [NPY](tensors/0000312.npy) |
| 313 | `model.layers.23` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 307] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000313.npy) |
| 314 | `model.layers.23` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0000314.npy) |
| 315 | `model.layers.23` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0000315.npy) |
| 316 | `model.layers.23` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0000316.npy) |
| 317 | `model.layers.23` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 318 | `model.layers.23` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 319 | `model.layers.23` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 320 | `model.layers.23.input_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 9984.0 / -0.18666178385416668 / 442.38929380599467 | [NPY](tensors/0000320.npy) |
| 321 | `model.layers.23.input_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 60.75 / 0.008146858546468946 / 1.77473329046844 | [NPY](tensors/0000321.npy) |
| 322 | `model.layers.23.self_attn` | 2 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 60.75 / 0.008146858546468946 / 1.77473329046844 | [NPY](tensors/0000322.npy) |
| 323 | `model.layers.23.self_attn` | 2 | `input.kwargs['attention_mask']` | [1, 1, 1, 307] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000323.npy) |
| 324 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 306.0 / 306.0 / 306.0 / 0.0 | [NPY](tensors/0000324.npy) |
| 325 | `model.layers.23.self_attn` | 2 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 326 | `model.layers.23.self_attn` | 2 | `input.kwargs['use_cache']` | — | bool | True | — |
| 327 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.65350341796875 / 1.032357154387917 | [NPY](tensors/0000327.npy) |
| 328 | `model.layers.23.self_attn` | 2 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.3125 / 0.03961661458015442 / 0.5610788035014659 | [NPY](tensors/0000328.npy) |
| 329 | `model.layers.23.self_attn` | 2 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 330 | `model.layers.23.self_attn.q_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 60.75 / 0.008146858546468946 / 1.77473329046844 | [NPY](tensors/0000330.npy) |
| 331 | `model.layers.23.self_attn.q_proj` | 2 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.6875 / 16.875 / 0.034725520526990294 / 1.3460609602584928 | [NPY](tensors/0000331.npy) |
| 332 | `model.layers.23.self_attn.k_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 60.75 / 0.008146858546468946 / 1.77473329046844 | [NPY](tensors/0000332.npy) |
| 333 | `model.layers.23.self_attn.k_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -33.0 / 38.25 / -0.09395775571465492 / 4.706330491039139 | [NPY](tensors/0000333.npy) |
| 334 | `model.layers.23.self_attn.v_proj` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 60.75 / 0.008146858546468946 / 1.77473329046844 | [NPY](tensors/0000334.npy) |
| 335 | `model.layers.23.self_attn.v_proj` | 2 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.5625 / 7.125 / -0.04424762725830078 / 2.6133677228544188 | [NPY](tensors/0000335.npy) |
| 336 | `model.layers.23.self_attn.o_proj` | 2 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.9375 / 6.25 / 0.002419814351014793 / 1.1485005221170232 | [NPY](tensors/0000336.npy) |
| 337 | `model.layers.23.self_attn.o_proj` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5216.0 / 5504.0 / 5.177081208758884 / 229.21102332622104 | [NPY](tensors/0000337.npy) |
| 338 | `model.layers.23.self_attn` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5216.0 / 5504.0 / 5.177081208758884 / 229.21102332622104 | [NPY](tensors/0000338.npy) |
| 339 | `model.layers.23.self_attn` | 2 | `output[1]` | [1, 64, 1, 307] | torch.bfloat16 → float32 | 9.237055564881302e-14 / 0.87109375 / 0.0022867767586011345 / 0.011844678785488743 | [NPY](tensors/0000339.npy) |
| 340 | `model.layers.23.post_attention_layernorm` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 9408.0 / 5.010762532552083 / 495.2008895904423 | [NPY](tensors/0000340.npy) |
| 341 | `model.layers.23.post_attention_layernorm` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 8.0625 / -0.008726827303568522 / 0.853991270205241 | [NPY](tensors/0000341.npy) |
| 342 | `model.layers.23.mlp` | 2 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -25.75 / 8.0625 / -0.008726827303568522 / 0.853991270205241 | [NPY](tensors/0000342.npy) |
| 343 | `model.layers.23.mlp.experts` | 2 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -25.75 / 8.0625 / -0.008726827303568522 / 0.853991270205241 | [NPY](tensors/0000343.npy) |
| 344 | `model.layers.23.mlp.experts` | 2 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 345 | `model.layers.23.mlp.experts` | 2 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 346 | `model.layers.23.mlp.experts` | 2 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 347 | `model.layers.23.mlp.experts` | 2 | `output` | [1, 2880] | torch.bfloat16 → float32 | -844.0 / 876.0 / -1.3770289950900607 / 63.86736368472666 | [NPY](tensors/0000347.npy) |
| 348 | `model.layers.23.mlp` | 2 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -844.0 / 876.0 / -1.3770289950900607 / 63.86736368472666 | [NPY](tensors/0000348.npy) |
| 349 | `model.layers.23.mlp` | 2 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.9453125 / 1.0859375 / 0.1177816390991211 / 0.4312022632254433 | [NPY](tensors/0000349.npy) |
| 350 | `model.layers.23` | 2 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8448.0 / 8640.0 / 3.6365424262152777 / 458.70641432470626 | [NPY](tensors/0000350.npy) |
| 429 | `model.layers.23` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 10048.0 / -5.450553385416667 / 476.2406790170122 | [NPY](tensors/0000429.npy) |
| 430 | `model.layers.23` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 308] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000430.npy) |
| 431 | `model.layers.23` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0000431.npy) |
| 432 | `model.layers.23` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0000432.npy) |
| 433 | `model.layers.23` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0000433.npy) |
| 434 | `model.layers.23` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 435 | `model.layers.23` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 436 | `model.layers.23` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 437 | `model.layers.23.input_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 10048.0 / -5.450553385416667 / 476.2406790170122 | [NPY](tensors/0000437.npy) |
| 438 | `model.layers.23.input_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.75 / -0.004862531026204427 / 1.7338191877412048 | [NPY](tensors/0000438.npy) |
| 439 | `model.layers.23.self_attn` | 3 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.75 / -0.004862531026204427 / 1.7338191877412048 | [NPY](tensors/0000439.npy) |
| 440 | `model.layers.23.self_attn` | 3 | `input.kwargs['attention_mask']` | [1, 1, 1, 308] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000440.npy) |
| 441 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 307.0 / 307.0 / 307.0 / 0.0 | [NPY](tensors/0000441.npy) |
| 442 | `model.layers.23.self_attn` | 3 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 443 | `model.layers.23.self_attn` | 3 | `input.kwargs['use_cache']` | — | bool | True | — |
| 444 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.699249267578125 / 0.9799463615887513 | [NPY](tensors/0000444.npy) |
| 445 | `model.layers.23.self_attn` | 3 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.3359375 / 0.04834452271461487 / 0.5989908659298642 | [NPY](tensors/0000445.npy) |
| 446 | `model.layers.23.self_attn` | 3 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 447 | `model.layers.23.self_attn.q_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.75 / -0.004862531026204427 / 1.7338191877412048 | [NPY](tensors/0000447.npy) |
| 448 | `model.layers.23.self_attn.q_proj` | 3 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.4375 / 16.875 / 0.03977743606083095 / 1.4126189495046642 | [NPY](tensors/0000448.npy) |
| 449 | `model.layers.23.self_attn.k_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.75 / -0.004862531026204427 / 1.7338191877412048 | [NPY](tensors/0000449.npy) |
| 450 | `model.layers.23.self_attn.k_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.75 / 41.25 / -0.06989345699548721 / 4.85146376166384 | [NPY](tensors/0000450.npy) |
| 451 | `model.layers.23.self_attn.v_proj` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.75 / -0.004862531026204427 / 1.7338191877412048 | [NPY](tensors/0000451.npy) |
| 452 | `model.layers.23.self_attn.v_proj` | 3 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.3125 / 7.65625 / -0.10590982437133789 / 2.085670104806328 | [NPY](tensors/0000452.npy) |
| 453 | `model.layers.23.self_attn.o_proj` | 3 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.9375 / 6.6875 / -0.00921026454307139 / 0.9856619379055155 | [NPY](tensors/0000453.npy) |
| 454 | `model.layers.23.self_attn.o_proj` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5696.0 / 5.746093002955119 / 237.7093618653312 | [NPY](tensors/0000454.npy) |
| 455 | `model.layers.23.self_attn` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5344.0 / 5696.0 / 5.746093002955119 / 237.7093618653312 | [NPY](tensors/0000455.npy) |
| 456 | `model.layers.23.self_attn` | 3 | `output[1]` | [1, 64, 1, 308] | torch.bfloat16 → float32 | 2.0650148258027912e-14 / 0.87109375 / 0.0018162168752908485 / 0.011579128436994124 | [NPY](tensors/0000456.npy) |
| 457 | `model.layers.23.post_attention_layernorm` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 10176.0 / 0.28713921440972223 / 553.3043597284054 | [NPY](tensors/0000457.npy) |
| 458 | `model.layers.23.post_attention_layernorm` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.625 / 8.3125 / -0.020921616421805487 / 0.9423956116033517 | [NPY](tensors/0000458.npy) |
| 459 | `model.layers.23.mlp` | 3 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.625 / 8.3125 / -0.020921616421805487 / 0.9423956116033517 | [NPY](tensors/0000459.npy) |
| 460 | `model.layers.23.mlp.experts` | 3 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.625 / 8.3125 / -0.020921616421805487 / 0.9423956116033517 | [NPY](tensors/0000460.npy) |
| 461 | `model.layers.23.mlp.experts` | 3 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 462 | `model.layers.23.mlp.experts` | 3 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 463 | `model.layers.23.mlp.experts` | 3 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 464 | `model.layers.23.mlp.experts` | 3 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1352.0 / 1040.0 / -1.3583945804172093 / 60.67516276366839 | [NPY](tensors/0000464.npy) |
| 465 | `model.layers.23.mlp` | 3 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1352.0 / 1040.0 / -1.3583945804172093 / 60.67516276366839 | [NPY](tensors/0000465.npy) |
| 466 | `model.layers.23.mlp` | 3 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.859375 / 1.3203125 / 0.017641007900238037 / 0.44701135077915327 | [NPY](tensors/0000466.npy) |
| 467 | `model.layers.23` | 3 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 9856.0 / -1.071652560763889 / 546.1417914554553 | [NPY](tensors/0000467.npy) |
| 546 | `model.layers.23` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10496.0 / 6.172387017144097 / 479.6642328296832 | [NPY](tensors/0000546.npy) |
| 547 | `model.layers.23` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 309] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000547.npy) |
| 548 | `model.layers.23` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0000548.npy) |
| 549 | `model.layers.23` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0000549.npy) |
| 550 | `model.layers.23` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0000550.npy) |
| 551 | `model.layers.23` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 552 | `model.layers.23` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 553 | `model.layers.23` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 554 | `model.layers.23.input_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10496.0 / 6.172387017144097 / 479.6642328296832 | [NPY](tensors/0000554.npy) |
| 555 | `model.layers.23.input_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.75 / 0.026960736513137816 / 1.7519398992275939 | [NPY](tensors/0000555.npy) |
| 556 | `model.layers.23.self_attn` | 4 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.75 / 0.026960736513137816 / 1.7519398992275939 | [NPY](tensors/0000556.npy) |
| 557 | `model.layers.23.self_attn` | 4 | `input.kwargs['attention_mask']` | [1, 1, 1, 309] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000557.npy) |
| 558 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 308.0 / 308.0 / 308.0 / 0.0 | [NPY](tensors/0000558.npy) |
| 559 | `model.layers.23.self_attn` | 4 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 560 | `model.layers.23.self_attn` | 4 | `input.kwargs['use_cache']` | — | bool | True | — |
| 561 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.721038818359375 / 0.9607888892832113 | [NPY](tensors/0000561.npy) |
| 562 | `model.layers.23.self_attn` | 4 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.0950009822845459 / 0.5972484786943767 | [NPY](tensors/0000562.npy) |
| 563 | `model.layers.23.self_attn` | 4 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 564 | `model.layers.23.self_attn.q_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.75 / 0.026960736513137816 / 1.7519398992275939 | [NPY](tensors/0000564.npy) |
| 565 | `model.layers.23.self_attn.q_proj` | 4 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.125 / 14.75 / 0.036589073279174045 / 1.3560452840896962 | [NPY](tensors/0000565.npy) |
| 566 | `model.layers.23.self_attn.k_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.75 / 0.026960736513137816 / 1.7519398992275939 | [NPY](tensors/0000566.npy) |
| 567 | `model.layers.23.self_attn.k_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -57.0 / 45.0 / -0.1046440601348877 / 5.188097083322773 | [NPY](tensors/0000567.npy) |
| 568 | `model.layers.23.self_attn.v_proj` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 58.75 / 0.026960736513137816 / 1.7519398992275939 | [NPY](tensors/0000568.npy) |
| 569 | `model.layers.23.self_attn.v_proj` | 4 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.625 / 7.875 / -0.04972732067108154 / 2.8767271293039873 | [NPY](tensors/0000569.npy) |
| 570 | `model.layers.23.self_attn.o_proj` | 4 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.375 / 8.5625 / -0.03450534588773735 / 1.5994275456122595 | [NPY](tensors/0000570.npy) |
| 571 | `model.layers.23.self_attn.o_proj` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5664.0 / 5888.0 / 7.455178207821316 / 258.9060229063882 | [NPY](tensors/0000571.npy) |
| 572 | `model.layers.23.self_attn` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5664.0 / 5888.0 / 7.455178207821316 / 258.9060229063882 | [NPY](tensors/0000572.npy) |
| 573 | `model.layers.23.self_attn` | 4 | `output[1]` | [1, 64, 1, 309] | torch.bfloat16 → float32 | 1.2718714970105793e-12 / 0.8671875 / 0.002375378957703514 / 0.016629561107542348 | [NPY](tensors/0000573.npy) |
| 574 | `model.layers.23.post_attention_layernorm` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10368.0 / 13.586583116319444 / 565.4565838241344 | [NPY](tensors/0000574.npy) |
| 575 | `model.layers.23.post_attention_layernorm` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 9.0 / 0.012398346927430895 / 0.9657768294475397 | [NPY](tensors/0000575.npy) |
| 576 | `model.layers.23.mlp` | 4 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 9.0 / 0.012398346927430895 / 0.9657768294475397 | [NPY](tensors/0000576.npy) |
| 577 | `model.layers.23.mlp.experts` | 4 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.25 / 9.0 / 0.012398346927430895 / 0.9657768294475397 | [NPY](tensors/0000577.npy) |
| 578 | `model.layers.23.mlp.experts` | 4 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 579 | `model.layers.23.mlp.experts` | 4 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 580 | `model.layers.23.mlp.experts` | 4 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 581 | `model.layers.23.mlp.experts` | 4 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1920.0 / 1632.0 / 0.7165409300062392 / 90.31500028663963 | [NPY](tensors/0000581.npy) |
| 582 | `model.layers.23.mlp` | 4 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1920.0 / 1632.0 / 0.7165409300062392 / 90.31500028663963 | [NPY](tensors/0000582.npy) |
| 583 | `model.layers.23.mlp` | 4 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.85546875 / 1.203125 / 0.09727859497070312 / 0.4255075735645668 | [NPY](tensors/0000583.npy) |
| 584 | `model.layers.23` | 4 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 10368.0 / 14.305696614583333 / 582.6841150167866 | [NPY](tensors/0000584.npy) |
| 663 | `model.layers.23` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10816.0 / 10240.0 / -0.23034735785590277 / 468.66302911780275 | [NPY](tensors/0000663.npy) |
| 664 | `model.layers.23` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 310] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000664.npy) |
| 665 | `model.layers.23` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0000665.npy) |
| 666 | `model.layers.23` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0000666.npy) |
| 667 | `model.layers.23` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0000667.npy) |
| 668 | `model.layers.23` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 669 | `model.layers.23` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 670 | `model.layers.23` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 671 | `model.layers.23.input_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10816.0 / 10240.0 / -0.23034735785590277 / 468.66302911780275 | [NPY](tensors/0000671.npy) |
| 672 | `model.layers.23.input_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 56.5 / 0.00404709710015191 / 1.7530261517982948 | [NPY](tensors/0000672.npy) |
| 673 | `model.layers.23.self_attn` | 5 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 56.5 / 0.00404709710015191 / 1.7530261517982948 | [NPY](tensors/0000673.npy) |
| 674 | `model.layers.23.self_attn` | 5 | `input.kwargs['attention_mask']` | [1, 1, 1, 310] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000674.npy) |
| 675 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 309.0 / 309.0 / 309.0 / 0.0 | [NPY](tensors/0000675.npy) |
| 676 | `model.layers.23.self_attn` | 5 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 677 | `model.layers.23.self_attn` | 5 | `input.kwargs['use_cache']` | — | bool | True | — |
| 678 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6971588134765625 / 0.961755448906076 | [NPY](tensors/0000678.npy) |
| 679 | `model.layers.23.self_attn` | 5 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.14570441842079163 / 0.6143349820973056 | [NPY](tensors/0000679.npy) |
| 680 | `model.layers.23.self_attn` | 5 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 681 | `model.layers.23.self_attn.q_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 56.5 / 0.00404709710015191 / 1.7530261517982948 | [NPY](tensors/0000681.npy) |
| 682 | `model.layers.23.self_attn.q_proj` | 5 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.0625 / 16.25 / 0.04058735829312354 / 1.5383151768726324 | [NPY](tensors/0000682.npy) |
| 683 | `model.layers.23.self_attn.k_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 56.5 / 0.00404709710015191 / 1.7530261517982948 | [NPY](tensors/0000683.npy) |
| 684 | `model.layers.23.self_attn.k_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.75 / 39.0 / 0.024605438113212585 / 5.253052128741816 | [NPY](tensors/0000684.npy) |
| 685 | `model.layers.23.self_attn.v_proj` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.75 / 56.5 / 0.00404709710015191 / 1.7530261517982948 | [NPY](tensors/0000685.npy) |
| 686 | `model.layers.23.self_attn.v_proj` | 5 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.75 / 15.4375 / -0.013289600610733032 / 4.127853024753456 | [NPY](tensors/0000686.npy) |
| 687 | `model.layers.23.self_attn.o_proj` | 5 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.9375 / 6.8125 / -0.006648915121331811 / 1.4310303031256641 | [NPY](tensors/0000687.npy) |
| 688 | `model.layers.23.self_attn.o_proj` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5920.0 / 6176.0 / 8.945171949598524 / 261.959271668439 | [NPY](tensors/0000688.npy) |
| 689 | `model.layers.23.self_attn` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5920.0 / 6176.0 / 8.945171949598524 / 261.959271668439 | [NPY](tensors/0000689.npy) |
| 690 | `model.layers.23.self_attn` | 5 | `output[1]` | [1, 64, 1, 310] | torch.bfloat16 → float32 | 8.770761894538737e-15 / 0.88671875 / 0.0019947489930158403 / 0.01562168952366429 | [NPY](tensors/0000690.npy) |
| 691 | `model.layers.23.post_attention_layernorm` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10880.0 / 10304.0 / 8.752037217881945 / 559.5492427710848 | [NPY](tensors/0000691.npy) |
| 692 | `model.layers.23.post_attention_layernorm` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.75 / 7.5625 / 0.0012632287210888333 / 0.9554760370974281 | [NPY](tensors/0000692.npy) |
| 693 | `model.layers.23.mlp` | 5 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.75 / 7.5625 / 0.0012632287210888333 / 0.9554760370974281 | [NPY](tensors/0000693.npy) |
| 694 | `model.layers.23.mlp.experts` | 5 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.75 / 7.5625 / 0.0012632287210888333 / 0.9554760370974281 | [NPY](tensors/0000694.npy) |
| 695 | `model.layers.23.mlp.experts` | 5 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 696 | `model.layers.23.mlp.experts` | 5 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 697 | `model.layers.23.mlp.experts` | 5 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 698 | `model.layers.23.mlp.experts` | 5 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1640.0 / 1120.0 / -0.958414798312717 / 92.50897561665533 | [NPY](tensors/0000698.npy) |
| 699 | `model.layers.23.mlp` | 5 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1640.0 / 1120.0 / -0.958414798312717 / 92.50897561665533 | [NPY](tensors/0000699.npy) |
| 700 | `model.layers.23.mlp` | 5 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.609375 / 0.875 / 0.1067047119140625 / 0.5898062079447484 | [NPY](tensors/0000700.npy) |
| 701 | `model.layers.23` | 5 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9728.0 / 9344.0 / 7.814564344618056 / 512.9578209043675 | [NPY](tensors/0000701.npy) |
| 780 | `model.layers.23` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 9216.0 / 4.253592936197917 / 428.1578918228209 | [NPY](tensors/0000780.npy) |
| 781 | `model.layers.23` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 311] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000781.npy) |
| 782 | `model.layers.23` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0000782.npy) |
| 783 | `model.layers.23` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0000783.npy) |
| 784 | `model.layers.23` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0000784.npy) |
| 785 | `model.layers.23` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 786 | `model.layers.23` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 787 | `model.layers.23` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 788 | `model.layers.23.input_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 9216.0 / 4.253592936197917 / 428.1578918228209 | [NPY](tensors/0000788.npy) |
| 789 | `model.layers.23.input_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 57.75 / 0.018838501969973245 / 1.7589142993499416 | [NPY](tensors/0000789.npy) |
| 790 | `model.layers.23.self_attn` | 6 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 57.75 / 0.018838501969973245 / 1.7589142993499416 | [NPY](tensors/0000790.npy) |
| 791 | `model.layers.23.self_attn` | 6 | `input.kwargs['attention_mask']` | [1, 1, 1, 311] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000791.npy) |
| 792 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 310.0 / 310.0 / 310.0 / 0.0 | [NPY](tensors/0000792.npy) |
| 793 | `model.layers.23.self_attn` | 6 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 794 | `model.layers.23.self_attn` | 6 | `input.kwargs['use_cache']` | — | bool | True | — |
| 795 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.64337158203125 / 1.0043987873081799 | [NPY](tensors/0000795.npy) |
| 796 | `model.layers.23.self_attn` | 6 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.3203125 / 0.1631743311882019 / 0.5991618463902445 | [NPY](tensors/0000796.npy) |
| 797 | `model.layers.23.self_attn` | 6 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 798 | `model.layers.23.self_attn.q_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 57.75 / 0.018838501969973245 / 1.7589142993499416 | [NPY](tensors/0000798.npy) |
| 799 | `model.layers.23.self_attn.q_proj` | 6 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.0625 / 15.0625 / 0.03659508901182562 / 1.470843725775486 | [NPY](tensors/0000799.npy) |
| 800 | `model.layers.23.self_attn.k_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 57.75 / 0.018838501969973245 / 1.7589142993499416 | [NPY](tensors/0000800.npy) |
| 801 | `model.layers.23.self_attn.k_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.5 / 50.75 / 0.012501329183578491 / 5.538311946151882 | [NPY](tensors/0000801.npy) |
| 802 | `model.layers.23.self_attn.v_proj` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 57.75 / 0.018838501969973245 / 1.7589142993499416 | [NPY](tensors/0000802.npy) |
| 803 | `model.layers.23.self_attn.v_proj` | 6 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.25 / 14.875 / 0.03973400592803955 / 3.1613511482257874 | [NPY](tensors/0000803.npy) |
| 804 | `model.layers.23.self_attn.o_proj` | 6 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.75 / 6.78125 / -0.04148318571969867 / 1.4580799906831476 | [NPY](tensors/0000804.npy) |
| 805 | `model.layers.23.self_attn.o_proj` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5856.0 / 6048.0 / 6.505926598442925 / 262.1342888520926 | [NPY](tensors/0000805.npy) |
| 806 | `model.layers.23.self_attn` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5856.0 / 6048.0 / 6.505926598442925 / 262.1342888520926 | [NPY](tensors/0000806.npy) |
| 807 | `model.layers.23.self_attn` | 6 | `output[1]` | [1, 64, 1, 311] | torch.bfloat16 → float32 | 8.455458555545192e-13 / 0.8203125 / 0.002206073866105563 / 0.01479201556012342 | [NPY](tensors/0000807.npy) |
| 808 | `model.layers.23.post_attention_layernorm` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9728.0 / 10.77239990234375 / 526.78411662091 | [NPY](tensors/0000808.npy) |
| 809 | `model.layers.23.post_attention_layernorm` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 8.25 / 0.007955016030205622 / 0.9731355655621001 | [NPY](tensors/0000809.npy) |
| 810 | `model.layers.23.mlp` | 6 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 8.25 / 0.007955016030205622 / 0.9731355655621001 | [NPY](tensors/0000810.npy) |
| 811 | `model.layers.23.mlp.experts` | 6 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -29.625 / 8.25 / 0.007955016030205622 / 0.9731355655621001 | [NPY](tensors/0000811.npy) |
| 812 | `model.layers.23.mlp.experts` | 6 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 813 | `model.layers.23.mlp.experts` | 6 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 814 | `model.layers.23.mlp.experts` | 6 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 815 | `model.layers.23.mlp.experts` | 6 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1488.0 / 1288.0 / -0.0038121117485894096 / 76.09362619635377 | [NPY](tensors/0000815.npy) |
| 816 | `model.layers.23.mlp` | 6 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1488.0 / 1288.0 / -0.0038121117485894096 / 76.09362619635377 | [NPY](tensors/0000816.npy) |
| 817 | `model.layers.23.mlp` | 6 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.9375 / 1.1640625 / 0.0977783203125 / 0.4294971922443644 | [NPY](tensors/0000817.npy) |
| 818 | `model.layers.23` | 6 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 10176.0 / 10.742713758680555 / 556.8241406060507 | [NPY](tensors/0000818.npy) |
| 897 | `model.layers.23` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 10816.0 / 6.739504665798611 / 489.52435871267045 | [NPY](tensors/0000897.npy) |
| 898 | `model.layers.23` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 312] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000898.npy) |
| 899 | `model.layers.23` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0000899.npy) |
| 900 | `model.layers.23` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0000900.npy) |
| 901 | `model.layers.23` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0000901.npy) |
| 902 | `model.layers.23` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 903 | `model.layers.23` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 904 | `model.layers.23` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 905 | `model.layers.23.input_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 10816.0 / 6.739504665798611 / 489.52435871267045 | [NPY](tensors/0000905.npy) |
| 906 | `model.layers.23.input_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 59.25 / 0.03037972648938497 / 1.750827701394487 | [NPY](tensors/0000906.npy) |
| 907 | `model.layers.23.self_attn` | 7 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 59.25 / 0.03037972648938497 / 1.750827701394487 | [NPY](tensors/0000907.npy) |
| 908 | `model.layers.23.self_attn` | 7 | `input.kwargs['attention_mask']` | [1, 1, 1, 312] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0000908.npy) |
| 909 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 311.0 / 311.0 / 311.0 / 0.0 | [NPY](tensors/0000909.npy) |
| 910 | `model.layers.23.self_attn` | 7 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 911 | `model.layers.23.self_attn` | 7 | `input.kwargs['use_cache']` | — | bool | True | — |
| 912 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.59527587890625 / 1.0305763974333966 | [NPY](tensors/0000912.npy) |
| 913 | `model.layers.23.self_attn` | 7 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2421875 / 1.2890625 / 0.14041495323181152 / 0.6111484014934663 | [NPY](tensors/0000913.npy) |
| 914 | `model.layers.23.self_attn` | 7 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 915 | `model.layers.23.self_attn.q_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 59.25 / 0.03037972648938497 / 1.750827701394487 | [NPY](tensors/0000915.npy) |
| 916 | `model.layers.23.self_attn.q_proj` | 7 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.375 / 16.5 / 0.03395426890347153 / 1.428859387987032 | [NPY](tensors/0000916.npy) |
| 917 | `model.layers.23.self_attn.k_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 59.25 / 0.03037972648938497 / 1.750827701394487 | [NPY](tensors/0000917.npy) |
| 918 | `model.layers.23.self_attn.k_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -54.0 / 56.25 / -0.017828240990638733 / 5.428306651999608 | [NPY](tensors/0000918.npy) |
| 919 | `model.layers.23.self_attn.v_proj` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 59.25 / 0.03037972648938497 / 1.750827701394487 | [NPY](tensors/0000919.npy) |
| 920 | `model.layers.23.self_attn.v_proj` | 7 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.75 / 10.625 / -0.006054341793060303 / 2.2504153556767634 | [NPY](tensors/0000920.npy) |
| 921 | `model.layers.23.self_attn.o_proj` | 7 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.625 / 6.75 / -0.030011811293661594 / 1.352571773803886 | [NPY](tensors/0000921.npy) |
| 922 | `model.layers.23.self_attn.o_proj` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 5888.0 / 6.409597502814399 / 249.84511571210234 | [NPY](tensors/0000922.npy) |
| 923 | `model.layers.23.self_attn` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5600.0 / 5888.0 / 6.409597502814399 / 249.84511571210234 | [NPY](tensors/0000923.npy) |
| 924 | `model.layers.23.self_attn` | 7 | `output[1]` | [1, 64, 1, 312] | torch.bfloat16 → float32 | 1.7141843500212417e-13 / 0.8671875 / 0.0020112533013327927 / 0.014844553287136603 | [NPY](tensors/0000924.npy) |
| 925 | `model.layers.23.post_attention_layernorm` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 11008.0 / 13.172505696614584 / 570.0490284379797 | [NPY](tensors/0000925.npy) |
| 926 | `model.layers.23.post_attention_layernorm` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 7.0 / 0.007127281030019124 / 0.9394387832348666 | [NPY](tensors/0000926.npy) |
| 927 | `model.layers.23.mlp` | 7 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 7.0 / 0.007127281030019124 / 0.9394387832348666 | [NPY](tensors/0000927.npy) |
| 928 | `model.layers.23.mlp.experts` | 7 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -29.875 / 7.0 / 0.007127281030019124 / 0.9394387832348666 | [NPY](tensors/0000928.npy) |
| 929 | `model.layers.23.mlp.experts` | 7 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 930 | `model.layers.23.mlp.experts` | 7 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 931 | `model.layers.23.mlp.experts` | 7 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 932 | `model.layers.23.mlp.experts` | 7 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1416.0 / 1152.0 / 0.16056375503540038 / 68.37765925678858 | [NPY](tensors/0000932.npy) |
| 933 | `model.layers.23.mlp` | 7 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1416.0 / 1152.0 / 0.16056375503540038 / 68.37765925678858 | [NPY](tensors/0000933.npy) |
| 934 | `model.layers.23.mlp` | 7 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.2578125 / 0.1316680908203125 / 0.5262804771636335 | [NPY](tensors/0000934.npy) |
| 935 | `model.layers.23` | 7 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 10816.0 / 13.334781901041667 / 564.0979301021572 | [NPY](tensors/0000935.npy) |
| 1014 | `model.layers.23` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 10048.0 / -1.0215603298611111 / 464.78735998784447 | [NPY](tensors/0001014.npy) |
| 1015 | `model.layers.23` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 313] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001015.npy) |
| 1016 | `model.layers.23` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0001016.npy) |
| 1017 | `model.layers.23` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0001017.npy) |
| 1018 | `model.layers.23` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0001018.npy) |
| 1019 | `model.layers.23` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1020 | `model.layers.23` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1021 | `model.layers.23` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1022 | `model.layers.23.input_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 10048.0 / -1.0215603298611111 / 464.78735998784447 | [NPY](tensors/0001022.npy) |
| 1023 | `model.layers.23.input_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 58.0 / 0.0026864091555277507 / 1.759442279999494 | [NPY](tensors/0001023.npy) |
| 1024 | `model.layers.23.self_attn` | 8 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 58.0 / 0.0026864091555277507 / 1.759442279999494 | [NPY](tensors/0001024.npy) |
| 1025 | `model.layers.23.self_attn` | 8 | `input.kwargs['attention_mask']` | [1, 1, 1, 313] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001025.npy) |
| 1026 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 312.0 / 312.0 / 312.0 / 0.0 | [NPY](tensors/0001026.npy) |
| 1027 | `model.layers.23.self_attn` | 8 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1028 | `model.layers.23.self_attn` | 8 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1029 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.5780181884765625 / 0.9875377507054134 | [NPY](tensors/0001029.npy) |
| 1030 | `model.layers.23.self_attn` | 8 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.09894603490829468 / 0.7006760635632429 | [NPY](tensors/0001030.npy) |
| 1031 | `model.layers.23.self_attn` | 8 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1032 | `model.layers.23.self_attn.q_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 58.0 / 0.0026864091555277507 / 1.759442279999494 | [NPY](tensors/0001032.npy) |
| 1033 | `model.layers.23.self_attn.q_proj` | 8 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.875 / 16.875 / 0.033946987707167864 / 1.543059548784917 | [NPY](tensors/0001033.npy) |
| 1034 | `model.layers.23.self_attn.k_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 58.0 / 0.0026864091555277507 / 1.759442279999494 | [NPY](tensors/0001034.npy) |
| 1035 | `model.layers.23.self_attn.k_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -57.0 / 60.75 / -0.04420249164104462 / 5.760428890490354 | [NPY](tensors/0001035.npy) |
| 1036 | `model.layers.23.self_attn.v_proj` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 58.0 / 0.0026864091555277507 / 1.759442279999494 | [NPY](tensors/0001036.npy) |
| 1037 | `model.layers.23.self_attn.v_proj` | 8 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.75 / 15.125 / 0.06364965438842773 / 4.12387190908132 | [NPY](tensors/0001037.npy) |
| 1038 | `model.layers.23.self_attn.o_proj` | 8 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.25 / 6.84375 / 0.01314339810051024 / 1.3669475386717898 | [NPY](tensors/0001038.npy) |
| 1039 | `model.layers.23.self_attn.o_proj` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5120.0 / 5280.0 / 6.201407877604167 / 223.92634542281647 | [NPY](tensors/0001039.npy) |
| 1040 | `model.layers.23.self_attn` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5120.0 / 5280.0 / 6.201407877604167 / 223.92634542281647 | [NPY](tensors/0001040.npy) |
| 1041 | `model.layers.23.self_attn` | 8 | `output[1]` | [1, 64, 1, 313] | torch.bfloat16 → float32 | 1.4363510381087963e-15 / 0.83984375 / 0.0018143117552919768 / 0.016820454307329005 | [NPY](tensors/0001041.npy) |
| 1042 | `model.layers.23.post_attention_layernorm` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10176.0 / 9792.0 / 5.165196397569445 / 528.9067441215484 | [NPY](tensors/0001042.npy) |
| 1043 | `model.layers.23.post_attention_layernorm` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.5 / 7.1875 / -0.013580576578776041 / 1.018752521318953 | [NPY](tensors/0001043.npy) |
| 1044 | `model.layers.23.mlp` | 8 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -35.5 / 7.1875 / -0.013580576578776041 / 1.018752521318953 | [NPY](tensors/0001044.npy) |
| 1045 | `model.layers.23.mlp.experts` | 8 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -35.5 / 7.1875 / -0.013580576578776041 / 1.018752521318953 | [NPY](tensors/0001045.npy) |
| 1046 | `model.layers.23.mlp.experts` | 8 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1047 | `model.layers.23.mlp.experts` | 8 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1048 | `model.layers.23.mlp.experts` | 8 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1049 | `model.layers.23.mlp.experts` | 8 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1712.0 / 1400.0 / -0.32670782936943904 / 103.63071729853384 | [NPY](tensors/0001049.npy) |
| 1050 | `model.layers.23.mlp` | 8 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1712.0 / 1400.0 / -0.32670782936943904 / 103.63071729853384 | [NPY](tensors/0001050.npy) |
| 1051 | `model.layers.23.mlp` | 8 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.328125 / 1.03125 / 0.219329833984375 / 0.9178718957127374 | [NPY](tensors/0001051.npy) |
| 1052 | `model.layers.23` | 8 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8896.0 / 8448.0 / 4.847824435763889 / 481.89210370180587 | [NPY](tensors/0001052.npy) |
| 1131 | `model.layers.23` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9024.0 / 9280.0 / -2.1007039388020834 / 434.14801184018205 | [NPY](tensors/0001131.npy) |
| 1132 | `model.layers.23` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 314] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001132.npy) |
| 1133 | `model.layers.23` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0001133.npy) |
| 1134 | `model.layers.23` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0001134.npy) |
| 1135 | `model.layers.23` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0001135.npy) |
| 1136 | `model.layers.23` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1137 | `model.layers.23` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1138 | `model.layers.23` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1139 | `model.layers.23.input_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9024.0 / 9280.0 / -2.1007039388020834 / 434.14801184018205 | [NPY](tensors/0001139.npy) |
| 1140 | `model.layers.23.input_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 57.5 / -0.0005441311332914564 / 1.7507508435566403 | [NPY](tensors/0001140.npy) |
| 1141 | `model.layers.23.self_attn` | 9 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 57.5 / -0.0005441311332914564 / 1.7507508435566403 | [NPY](tensors/0001141.npy) |
| 1142 | `model.layers.23.self_attn` | 9 | `input.kwargs['attention_mask']` | [1, 1, 1, 314] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001142.npy) |
| 1143 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 313.0 / 313.0 / 313.0 / 0.0 | [NPY](tensors/0001143.npy) |
| 1144 | `model.layers.23.self_attn` | 9 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1145 | `model.layers.23.self_attn` | 9 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1146 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3203125 / 1.34375 / 0.5865020751953125 / 0.9669963986005182 | [NPY](tensors/0001146.npy) |
| 1147 | `model.layers.23.self_attn` | 9 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.06996363401412964 / 0.7251401734789152 | [NPY](tensors/0001147.npy) |
| 1148 | `model.layers.23.self_attn` | 9 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1149 | `model.layers.23.self_attn.q_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 57.5 / -0.0005441311332914564 / 1.7507508435566403 | [NPY](tensors/0001149.npy) |
| 1150 | `model.layers.23.self_attn.q_proj` | 9 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.875 / 15.875 / 0.03940329421311617 / 1.4815111053130035 | [NPY](tensors/0001150.npy) |
| 1151 | `model.layers.23.self_attn.k_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 57.5 / -0.0005441311332914564 / 1.7507508435566403 | [NPY](tensors/0001151.npy) |
| 1152 | `model.layers.23.self_attn.k_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -60.25 / 56.0 / -0.09520329535007477 / 5.565854207062259 | [NPY](tensors/0001152.npy) |
| 1153 | `model.layers.23.self_attn.v_proj` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.75 / 57.5 / -0.0005441311332914564 / 1.7507508435566403 | [NPY](tensors/0001153.npy) |
| 1154 | `model.layers.23.self_attn.v_proj` | 9 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.625 / 10.0 / 0.13200075924396515 / 2.9805986505450113 | [NPY](tensors/0001154.npy) |
| 1155 | `model.layers.23.self_attn.o_proj` | 9 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.25 / 6.90625 / -0.022296473383903503 / 1.2808956882985176 | [NPY](tensors/0001155.npy) |
| 1156 | `model.layers.23.self_attn.o_proj` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5888.0 / 6080.0 / 7.207076093885633 / 261.1650674528736 | [NPY](tensors/0001156.npy) |
| 1157 | `model.layers.23.self_attn` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5888.0 / 6080.0 / 7.207076093885633 / 261.1650674528736 | [NPY](tensors/0001157.npy) |
| 1158 | `model.layers.23.self_attn` | 9 | `output[1]` | [1, 64, 1, 314] | torch.bfloat16 → float32 | 8.704148513061227e-14 / 0.8203125 / 0.0021632550583985475 / 0.012992752715900103 | [NPY](tensors/0001158.npy) |
| 1159 | `model.layers.23.post_attention_layernorm` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9408.0 / 9600.0 / 5.117578125 / 534.3620841766677 | [NPY](tensors/0001159.npy) |
| 1160 | `model.layers.23.post_attention_layernorm` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 7.6875 / -0.009310966067843967 / 0.9616637996917843 | [NPY](tensors/0001160.npy) |
| 1161 | `model.layers.23.mlp` | 9 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.875 / 7.6875 / -0.009310966067843967 / 0.9616637996917843 | [NPY](tensors/0001161.npy) |
| 1162 | `model.layers.23.mlp.experts` | 9 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -29.875 / 7.6875 / -0.009310966067843967 / 0.9616637996917843 | [NPY](tensors/0001162.npy) |
| 1163 | `model.layers.23.mlp.experts` | 9 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1164 | `model.layers.23.mlp.experts` | 9 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1165 | `model.layers.23.mlp.experts` | 9 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1166 | `model.layers.23.mlp.experts` | 9 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1120.0 / 840.0 / 0.3747200197643704 / 56.12819943088565 | [NPY](tensors/0001166.npy) |
| 1167 | `model.layers.23.mlp` | 9 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1120.0 / 840.0 / 0.3747200197643704 / 56.12819943088565 | [NPY](tensors/0001167.npy) |
| 1168 | `model.layers.23.mlp` | 9 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.69140625 / 1.2578125 / 0.13962078094482422 / 0.41322732633450937 | [NPY](tensors/0001168.npy) |
| 1169 | `model.layers.23` | 9 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9920.0 / 5.488023546006945 / 549.4736276546373 | [NPY](tensors/0001169.npy) |
| 1248 | `model.layers.23` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 10176.0 / -0.02043728298611111 / 473.5715702349801 | [NPY](tensors/0001248.npy) |
| 1249 | `model.layers.23` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 315] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001249.npy) |
| 1250 | `model.layers.23` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0001250.npy) |
| 1251 | `model.layers.23` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0001251.npy) |
| 1252 | `model.layers.23` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0001252.npy) |
| 1253 | `model.layers.23` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1254 | `model.layers.23` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1255 | `model.layers.23` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1256 | `model.layers.23.input_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 10176.0 / -0.02043728298611111 / 473.5715702349801 | [NPY](tensors/0001256.npy) |
| 1257 | `model.layers.23.input_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 57.75 / 0.010319964090983073 / 1.7464625220283985 | [NPY](tensors/0001257.npy) |
| 1258 | `model.layers.23.self_attn` | 10 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 57.75 / 0.010319964090983073 / 1.7464625220283985 | [NPY](tensors/0001258.npy) |
| 1259 | `model.layers.23.self_attn` | 10 | `input.kwargs['attention_mask']` | [1, 1, 1, 315] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001259.npy) |
| 1260 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 314.0 / 314.0 / 314.0 / 0.0 | [NPY](tensors/0001260.npy) |
| 1261 | `model.layers.23.self_attn` | 10 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1262 | `model.layers.23.self_attn` | 10 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1263 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.5947418212890625 / 1.0014743403435982 | [NPY](tensors/0001263.npy) |
| 1264 | `model.layers.23.self_attn` | 10 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.06113007664680481 / 0.6706132413066062 | [NPY](tensors/0001264.npy) |
| 1265 | `model.layers.23.self_attn` | 10 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1266 | `model.layers.23.self_attn.q_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 57.75 / 0.010319964090983073 / 1.7464625220283985 | [NPY](tensors/0001266.npy) |
| 1267 | `model.layers.23.self_attn.q_proj` | 10 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.3125 / 14.125 / 0.04361455608159304 / 1.425809567329504 | [NPY](tensors/0001267.npy) |
| 1268 | `model.layers.23.self_attn.k_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 57.75 / 0.010319964090983073 / 1.7464625220283985 | [NPY](tensors/0001268.npy) |
| 1269 | `model.layers.23.self_attn.k_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.5 / 48.75 / -0.05267695151269436 / 5.026016941866148 | [NPY](tensors/0001269.npy) |
| 1270 | `model.layers.23.self_attn.v_proj` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 57.75 / 0.010319964090983073 / 1.7464625220283985 | [NPY](tensors/0001270.npy) |
| 1271 | `model.layers.23.self_attn.v_proj` | 10 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.375 / 6.96875 / -0.015526622533798218 / 1.999853115811075 | [NPY](tensors/0001271.npy) |
| 1272 | `model.layers.23.self_attn.o_proj` | 10 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.0 / 6.8125 / -0.014892924402374774 / 1.1106116166110953 | [NPY](tensors/0001272.npy) |
| 1273 | `model.layers.23.self_attn.o_proj` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5632.0 / 5920.0 / 6.741245301564534 / 250.64417992761722 | [NPY](tensors/0001273.npy) |
| 1274 | `model.layers.23.self_attn` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5632.0 / 5920.0 / 6.741245301564534 / 250.64417992761722 | [NPY](tensors/0001274.npy) |
| 1275 | `model.layers.23.self_attn` | 10 | `output[1]` | [1, 64, 1, 315] | torch.bfloat16 → float32 | 6.217248937900877e-14 / 0.8515625 / 0.002001421642019148 / 0.012537985474173405 | [NPY](tensors/0001275.npy) |
| 1276 | `model.layers.23.post_attention_layernorm` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 10560.0 / 6.7088812934027775 / 562.988058226542 | [NPY](tensors/0001276.npy) |
| 1277 | `model.layers.23.post_attention_layernorm` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 7.9375 / -0.005867594480514526 / 0.9641781541853885 | [NPY](tensors/0001277.npy) |
| 1278 | `model.layers.23.mlp` | 10 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 7.9375 / -0.005867594480514526 / 0.9641781541853885 | [NPY](tensors/0001278.npy) |
| 1279 | `model.layers.23.mlp.experts` | 10 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.0 / 7.9375 / -0.005867594480514526 / 0.9641781541853885 | [NPY](tensors/0001279.npy) |
| 1280 | `model.layers.23.mlp.experts` | 10 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1281 | `model.layers.23.mlp.experts` | 10 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1282 | `model.layers.23.mlp.experts` | 10 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1283 | `model.layers.23.mlp.experts` | 10 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1336.0 / 1024.0 / -0.12399052513970268 / 60.46504098271802 | [NPY](tensors/0001283.npy) |
| 1284 | `model.layers.23.mlp` | 10 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1336.0 / 1024.0 / -0.12399052513970268 / 60.46504098271802 | [NPY](tensors/0001284.npy) |
| 1285 | `model.layers.23.mlp` | 10 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.6953125 / 1.3125 / 0.08897829055786133 / 0.43496583783458265 | [NPY](tensors/0001285.npy) |
| 1286 | `model.layers.23` | 10 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 10624.0 / 6.616913519965278 / 569.5966416656613 | [NPY](tensors/0001286.npy) |
| 1365 | `model.layers.23` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 10496.0 / 6.7116509331597225 / 482.7732526840998 | [NPY](tensors/0001365.npy) |
| 1366 | `model.layers.23` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 316] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001366.npy) |
| 1367 | `model.layers.23` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0001367.npy) |
| 1368 | `model.layers.23` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0001368.npy) |
| 1369 | `model.layers.23` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0001369.npy) |
| 1370 | `model.layers.23` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1371 | `model.layers.23` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1372 | `model.layers.23` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1373 | `model.layers.23.input_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 10496.0 / 6.7116509331597225 / 482.7732526840998 | [NPY](tensors/0001373.npy) |
| 1374 | `model.layers.23.input_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 58.5 / 0.029126146104600695 / 1.75001123760472 | [NPY](tensors/0001374.npy) |
| 1375 | `model.layers.23.self_attn` | 11 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 58.5 / 0.029126146104600695 / 1.75001123760472 | [NPY](tensors/0001375.npy) |
| 1376 | `model.layers.23.self_attn` | 11 | `input.kwargs['attention_mask']` | [1, 1, 1, 316] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001376.npy) |
| 1377 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 315.0 / 315.0 / 315.0 / 0.0 | [NPY](tensors/0001377.npy) |
| 1378 | `model.layers.23.self_attn` | 11 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1379 | `model.layers.23.self_attn` | 11 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1380 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.296875 / 1.34375 / 0.58709716796875 / 1.008764229733789 | [NPY](tensors/0001380.npy) |
| 1381 | `model.layers.23.self_attn` | 11 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.28125 / 0.05546322464942932 / 0.6672384041861009 | [NPY](tensors/0001381.npy) |
| 1382 | `model.layers.23.self_attn` | 11 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1383 | `model.layers.23.self_attn.q_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 58.5 / 0.029126146104600695 / 1.75001123760472 | [NPY](tensors/0001383.npy) |
| 1384 | `model.layers.23.self_attn.q_proj` | 11 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.5 / 14.875 / 0.0437104906886816 / 1.4205776406249728 | [NPY](tensors/0001384.npy) |
| 1385 | `model.layers.23.self_attn.k_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 58.5 / 0.029126146104600695 / 1.75001123760472 | [NPY](tensors/0001385.npy) |
| 1386 | `model.layers.23.self_attn.k_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -44.75 / 42.0 / -0.06919864472001791 / 4.975744105884885 | [NPY](tensors/0001386.npy) |
| 1387 | `model.layers.23.self_attn.v_proj` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.75 / 58.5 / 0.029126146104600695 / 1.75001123760472 | [NPY](tensors/0001387.npy) |
| 1388 | `model.layers.23.self_attn.v_proj` | 11 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.125 / 7.40625 / -0.1627623438835144 / 2.8781750716918273 | [NPY](tensors/0001388.npy) |
| 1389 | `model.layers.23.self_attn.o_proj` | 11 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.625 / 6.9375 / -0.03228518273681402 / 1.356649310247598 | [NPY](tensors/0001389.npy) |
| 1390 | `model.layers.23.self_attn.o_proj` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6272.0 / 6528.0 / 7.150557486216227 / 278.75268491361214 | [NPY](tensors/0001390.npy) |
| 1391 | `model.layers.23.self_attn` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6272.0 / 6528.0 / 7.150557486216227 / 278.75268491361214 | [NPY](tensors/0001391.npy) |
| 1392 | `model.layers.23.self_attn` | 11 | `output[1]` | [1, 64, 1, 316] | torch.bfloat16 → float32 | 6.039613253960852e-13 / 0.87109375 / 0.0020413222192137447 / 0.014136214424435552 | [NPY](tensors/0001392.npy) |
| 1393 | `model.layers.23.post_attention_layernorm` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11008.0 / 11072.0 / 13.837265353732638 / 592.287554264112 | [NPY](tensors/0001393.npy) |
| 1394 | `model.layers.23.post_attention_layernorm` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.75 / 8.125 / 0.007347397009531657 / 0.9368342020431072 | [NPY](tensors/0001394.npy) |
| 1395 | `model.layers.23.mlp` | 11 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.75 / 8.125 / 0.007347397009531657 / 0.9368342020431072 | [NPY](tensors/0001395.npy) |
| 1396 | `model.layers.23.mlp.experts` | 11 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.75 / 8.125 / 0.007347397009531657 / 0.9368342020431072 | [NPY](tensors/0001396.npy) |
| 1397 | `model.layers.23.mlp.experts` | 11 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1398 | `model.layers.23.mlp.experts` | 11 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1399 | `model.layers.23.mlp.experts` | 11 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1400 | `model.layers.23.mlp.experts` | 11 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1216.0 / 792.0 / -0.7399968889024523 / 61.765055980715154 | [NPY](tensors/0001400.npy) |
| 1401 | `model.layers.23.mlp` | 11 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1216.0 / 792.0 / -0.7399968889024523 / 61.765055980715154 | [NPY](tensors/0001401.npy) |
| 1402 | `model.layers.23.mlp` | 11 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.69921875 / 1.2890625 / 0.11431694030761719 / 0.3901682088686519 | [NPY](tensors/0001402.npy) |
| 1403 | `model.layers.23` | 11 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10816.0 / 13.116465928819444 / 574.9474710469224 | [NPY](tensors/0001403.npy) |
| 1482 | `model.layers.23` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 9472.0 / -1.8732231987847223 / 454.16522084239983 | [NPY](tensors/0001482.npy) |
| 1483 | `model.layers.23` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 317] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001483.npy) |
| 1484 | `model.layers.23` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0001484.npy) |
| 1485 | `model.layers.23` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0001485.npy) |
| 1486 | `model.layers.23` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0001486.npy) |
| 1487 | `model.layers.23` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1488 | `model.layers.23` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1489 | `model.layers.23` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1490 | `model.layers.23.input_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 9472.0 / -1.8732231987847223 / 454.16522084239983 | [NPY](tensors/0001490.npy) |
| 1491 | `model.layers.23.input_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 54.5 / -0.003214458293384976 / 1.7370423707008749 | [NPY](tensors/0001491.npy) |
| 1492 | `model.layers.23.self_attn` | 12 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 54.5 / -0.003214458293384976 / 1.7370423707008749 | [NPY](tensors/0001492.npy) |
| 1493 | `model.layers.23.self_attn` | 12 | `input.kwargs['attention_mask']` | [1, 1, 1, 317] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001493.npy) |
| 1494 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 316.0 / 316.0 / 316.0 / 0.0 | [NPY](tensors/0001494.npy) |
| 1495 | `model.layers.23.self_attn` | 12 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1496 | `model.layers.23.self_attn` | 12 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1497 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2890625 / 1.34375 / 0.57403564453125 / 1.0150800398305975 | [NPY](tensors/0001497.npy) |
| 1498 | `model.layers.23.self_attn` | 12 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.296875 / 0.030997484922409058 / 0.6708695672417114 | [NPY](tensors/0001498.npy) |
| 1499 | `model.layers.23.self_attn` | 12 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1500 | `model.layers.23.self_attn.q_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 54.5 / -0.003214458293384976 / 1.7370423707008749 | [NPY](tensors/0001500.npy) |
| 1501 | `model.layers.23.self_attn.q_proj` | 12 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.5625 / 15.625 / 0.04254568263422698 / 1.5330481748148066 | [NPY](tensors/0001501.npy) |
| 1502 | `model.layers.23.self_attn.k_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 54.5 / -0.003214458293384976 / 1.7370423707008749 | [NPY](tensors/0001502.npy) |
| 1503 | `model.layers.23.self_attn.k_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -34.75 / 38.5 / 0.015342369675636292 / 4.7704128428401384 | [NPY](tensors/0001503.npy) |
| 1504 | `model.layers.23.self_attn.v_proj` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 54.5 / -0.003214458293384976 / 1.7370423707008749 | [NPY](tensors/0001504.npy) |
| 1505 | `model.layers.23.self_attn.v_proj` | 12 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.625 / 12.75 / -0.024987071752548218 / 3.564198907511649 | [NPY](tensors/0001505.npy) |
| 1506 | `model.layers.23.self_attn.o_proj` | 12 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.5 / 7.53125 / -0.03783587459474802 / 1.1701192335133803 | [NPY](tensors/0001506.npy) |
| 1507 | `model.layers.23.self_attn.o_proj` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5728.0 / 5920.0 / 6.282442262437608 / 249.8037565817534 | [NPY](tensors/0001507.npy) |
| 1508 | `model.layers.23.self_attn` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5728.0 / 5920.0 / 6.282442262437608 / 249.8037565817534 | [NPY](tensors/0001508.npy) |
| 1509 | `model.layers.23.self_attn` | 12 | `output[1]` | [1, 64, 1, 317] | torch.bfloat16 → float32 | 3.042011087472929e-14 / 0.8828125 / 0.0017372043488907752 / 0.01265286896242948 | [NPY](tensors/0001509.npy) |
| 1510 | `model.layers.23.post_attention_layernorm` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9664.0 / 4.372358703613282 / 539.8130236368994 | [NPY](tensors/0001510.npy) |
| 1511 | `model.layers.23.post_attention_layernorm` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.5 / 8.375 / -0.012081497245364718 / 0.971149112896409 | [NPY](tensors/0001511.npy) |
| 1512 | `model.layers.23.mlp` | 12 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.5 / 8.375 / -0.012081497245364718 / 0.971149112896409 | [NPY](tensors/0001512.npy) |
| 1513 | `model.layers.23.mlp.experts` | 12 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.5 / 8.375 / -0.012081497245364718 / 0.971149112896409 | [NPY](tensors/0001513.npy) |
| 1514 | `model.layers.23.mlp.experts` | 12 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1515 | `model.layers.23.mlp.experts` | 12 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1516 | `model.layers.23.mlp.experts` | 12 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1517 | `model.layers.23.mlp.experts` | 12 | `output` | [1, 2880] | torch.bfloat16 → float32 | -908.0 / 580.0 / -0.8062233103646173 / 46.13407617660115 | [NPY](tensors/0001517.npy) |
| 1518 | `model.layers.23.mlp` | 12 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -908.0 / 580.0 / -0.8062233103646173 / 46.13407617660115 | [NPY](tensors/0001518.npy) |
| 1519 | `model.layers.23.mlp` | 12 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.361328125 / 1.265625 / 0.13696765899658203 / 0.382107610145455 | [NPY](tensors/0001519.npy) |
| 1520 | `model.layers.23` | 12 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10176.0 / 9664.0 / 3.598342556423611 / 537.824560980055 | [NPY](tensors/0001520.npy) |
| 1599 | `model.layers.23` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 10240.0 / -0.7518825954861111 / 491.7215918730247 | [NPY](tensors/0001599.npy) |
| 1600 | `model.layers.23` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 318] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001600.npy) |
| 1601 | `model.layers.23` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0001601.npy) |
| 1602 | `model.layers.23` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0001602.npy) |
| 1603 | `model.layers.23` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0001603.npy) |
| 1604 | `model.layers.23` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1605 | `model.layers.23` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1606 | `model.layers.23` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1607 | `model.layers.23.input_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 10240.0 / -0.7518825954861111 / 491.7215918730247 | [NPY](tensors/0001607.npy) |
| 1608 | `model.layers.23.input_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 56.0 / 0.004061296251085069 / 1.7303320529041701 | [NPY](tensors/0001608.npy) |
| 1609 | `model.layers.23.self_attn` | 13 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 56.0 / 0.004061296251085069 / 1.7303320529041701 | [NPY](tensors/0001609.npy) |
| 1610 | `model.layers.23.self_attn` | 13 | `input.kwargs['attention_mask']` | [1, 1, 1, 318] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001610.npy) |
| 1611 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 317.0 / 317.0 / 317.0 / 0.0 | [NPY](tensors/0001611.npy) |
| 1612 | `model.layers.23.self_attn` | 13 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1613 | `model.layers.23.self_attn` | 13 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1614 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.580535888671875 / 1.048553799870887 | [NPY](tensors/0001614.npy) |
| 1615 | `model.layers.23.self_attn` | 13 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.265625 / -0.010465651750564575 / 0.6110442923446456 | [NPY](tensors/0001615.npy) |
| 1616 | `model.layers.23.self_attn` | 13 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1617 | `model.layers.23.self_attn.q_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 56.0 / 0.004061296251085069 / 1.7303320529041701 | [NPY](tensors/0001617.npy) |
| 1618 | `model.layers.23.self_attn.q_proj` | 13 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.0 / 14.125 / 0.04181616008281708 / 1.4322127712958526 | [NPY](tensors/0001618.npy) |
| 1619 | `model.layers.23.self_attn.k_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 56.0 / 0.004061296251085069 / 1.7303320529041701 | [NPY](tensors/0001619.npy) |
| 1620 | `model.layers.23.self_attn.k_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.25 / 46.0 / -0.03466895408928394 / 4.894753129987662 | [NPY](tensors/0001620.npy) |
| 1621 | `model.layers.23.self_attn.v_proj` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.5 / 56.0 / 0.004061296251085069 / 1.7303320529041701 | [NPY](tensors/0001621.npy) |
| 1622 | `model.layers.23.self_attn.v_proj` | 13 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.25 / 6.5 / -0.06578963994979858 / 2.0799272922091663 | [NPY](tensors/0001622.npy) |
| 1623 | `model.layers.23.self_attn.o_proj` | 13 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.375 / 7.0 / -0.01960931858047843 / 1.041958322239446 | [NPY](tensors/0001623.npy) |
| 1624 | `model.layers.23.self_attn.o_proj` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5696.0 / 6048.0 / 6.927967087427775 / 253.62466138906558 | [NPY](tensors/0001624.npy) |
| 1625 | `model.layers.23.self_attn` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5696.0 / 6048.0 / 6.927967087427775 / 253.62466138906558 | [NPY](tensors/0001625.npy) |
| 1626 | `model.layers.23.self_attn` | 13 | `output[1]` | [1, 64, 1, 318] | torch.bfloat16 → float32 | 1.4210854715202004e-14 / 0.875 / 0.0015945308908226086 / 0.011708998352460242 | [NPY](tensors/0001626.npy) |
| 1627 | `model.layers.23.post_attention_layernorm` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10816.0 / 10880.0 / 6.1941718207465275 / 584.6496532816552 | [NPY](tensors/0001627.npy) |
| 1628 | `model.layers.23.post_attention_layernorm` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 7.75 / -0.009780796037779914 / 1.0317391607090474 | [NPY](tensors/0001628.npy) |
| 1629 | `model.layers.23.mlp` | 13 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 7.75 / -0.009780796037779914 / 1.0317391607090474 | [NPY](tensors/0001629.npy) |
| 1630 | `model.layers.23.mlp.experts` | 13 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.5 / 7.75 / -0.009780796037779914 / 1.0317391607090474 | [NPY](tensors/0001630.npy) |
| 1631 | `model.layers.23.mlp.experts` | 13 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1632 | `model.layers.23.mlp.experts` | 13 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1633 | `model.layers.23.mlp.experts` | 13 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1634 | `model.layers.23.mlp.experts` | 13 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1656.0 / 1344.0 / -0.7525520192252265 / 68.98378077685686 | [NPY](tensors/0001634.npy) |
| 1635 | `model.layers.23.mlp` | 13 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1656.0 / 1344.0 / -0.7525520192252265 / 68.98378077685686 | [NPY](tensors/0001635.npy) |
| 1636 | `model.layers.23.mlp` | 13 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.94140625 / 1.3125 / 0.10747528076171875 / 0.4886149438616153 | [NPY](tensors/0001636.npy) |
| 1637 | `model.layers.23` | 13 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10752.0 / 10944.0 / 5.441761610243056 / 593.8071894747562 | [NPY](tensors/0001637.npy) |
| 1716 | `model.layers.23` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 10368.0 / -0.3669921875 / 496.8861592459731 | [NPY](tensors/0001716.npy) |
| 1717 | `model.layers.23` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 319] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001717.npy) |
| 1718 | `model.layers.23` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0001718.npy) |
| 1719 | `model.layers.23` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0001719.npy) |
| 1720 | `model.layers.23` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0001720.npy) |
| 1721 | `model.layers.23` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1722 | `model.layers.23` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1723 | `model.layers.23` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1724 | `model.layers.23.input_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 10368.0 / -0.3669921875 / 496.8861592459731 | [NPY](tensors/0001724.npy) |
| 1725 | `model.layers.23.input_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / 0.0027117633157306247 / 1.7182641769547653 | [NPY](tensors/0001725.npy) |
| 1726 | `model.layers.23.self_attn` | 14 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / 0.0027117633157306247 / 1.7182641769547653 | [NPY](tensors/0001726.npy) |
| 1727 | `model.layers.23.self_attn` | 14 | `input.kwargs['attention_mask']` | [1, 1, 1, 319] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001727.npy) |
| 1728 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 318.0 / 318.0 / 318.0 / 0.0 | [NPY](tensors/0001728.npy) |
| 1729 | `model.layers.23.self_attn` | 14 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1730 | `model.layers.23.self_attn` | 14 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1731 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.619964599609375 / 1.0379556801141203 | [NPY](tensors/0001731.npy) |
| 1732 | `model.layers.23.self_attn` | 14 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.265625 / -0.04225417971611023 / 0.587908626341704 | [NPY](tensors/0001732.npy) |
| 1733 | `model.layers.23.self_attn` | 14 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1734 | `model.layers.23.self_attn.q_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / 0.0027117633157306247 / 1.7182641769547653 | [NPY](tensors/0001734.npy) |
| 1735 | `model.layers.23.self_attn.q_proj` | 14 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.0625 / 16.125 / 0.04424472409300506 / 1.4230880743286072 | [NPY](tensors/0001735.npy) |
| 1736 | `model.layers.23.self_attn.k_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / 0.0027117633157306247 / 1.7182641769547653 | [NPY](tensors/0001736.npy) |
| 1737 | `model.layers.23.self_attn.k_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.5 / 48.75 / -0.11332210898399353 / 5.140364587228664 | [NPY](tensors/0001737.npy) |
| 1738 | `model.layers.23.self_attn.v_proj` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / 0.0027117633157306247 / 1.7182641769547653 | [NPY](tensors/0001738.npy) |
| 1739 | `model.layers.23.self_attn.v_proj` | 14 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.375 / 9.9375 / 0.15995230292901397 / 3.222333294004435 | [NPY](tensors/0001739.npy) |
| 1740 | `model.layers.23.self_attn.o_proj` | 14 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.625 / 6.34375 / -0.018678374588489532 / 1.3145288447618104 | [NPY](tensors/0001740.npy) |
| 1741 | `model.layers.23.self_attn.o_proj` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6112.0 / 6368.0 / 7.4965907202826605 / 270.7975364409435 | [NPY](tensors/0001741.npy) |
| 1742 | `model.layers.23.self_attn` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6112.0 / 6368.0 / 7.4965907202826605 / 270.7975364409435 | [NPY](tensors/0001742.npy) |
| 1743 | `model.layers.23.self_attn` | 14 | `output[1]` | [1, 64, 1, 319] | torch.bfloat16 → float32 | 6.938893903907228e-15 / 0.90234375 / 0.001972618915971051 / 0.01397937604163164 | [NPY](tensors/0001743.npy) |
| 1744 | `model.layers.23.post_attention_layernorm` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10752.0 / 10496.0 / 7.155772569444444 / 586.833861309141 | [NPY](tensors/0001744.npy) |
| 1745 | `model.layers.23.post_attention_layernorm` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 8.5 / -0.009205156564712524 / 0.9975457560547332 | [NPY](tensors/0001745.npy) |
| 1746 | `model.layers.23.mlp` | 14 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 8.5 / -0.009205156564712524 / 0.9975457560547332 | [NPY](tensors/0001746.npy) |
| 1747 | `model.layers.23.mlp.experts` | 14 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.5 / 8.5 / -0.009205156564712524 / 0.9975457560547332 | [NPY](tensors/0001747.npy) |
| 1748 | `model.layers.23.mlp.experts` | 14 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1749 | `model.layers.23.mlp.experts` | 14 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1750 | `model.layers.23.mlp.experts` | 14 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1751 | `model.layers.23.mlp.experts` | 14 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1888.0 / 1512.0 / -0.29126046498616537 / 81.47487963798162 | [NPY](tensors/0001751.npy) |
| 1752 | `model.layers.23.mlp` | 14 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1888.0 / 1512.0 / -0.29126046498616537 / 81.47487963798162 | [NPY](tensors/0001752.npy) |
| 1753 | `model.layers.23.mlp` | 14 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0859375 / 1.2578125 / 0.1187286376953125 / 0.494873007118965 | [NPY](tensors/0001753.npy) |
| 1754 | `model.layers.23` | 14 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10688.0 / 10496.0 / 6.8753038194444445 / 595.7590910013985 | [NPY](tensors/0001754.npy) |
| 1833 | `model.layers.23` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9920.0 / -3.8388237847222224 / 472.46406358807013 | [NPY](tensors/0001833.npy) |
| 1834 | `model.layers.23` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 320] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001834.npy) |
| 1835 | `model.layers.23` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0001835.npy) |
| 1836 | `model.layers.23` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0001836.npy) |
| 1837 | `model.layers.23` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0001837.npy) |
| 1838 | `model.layers.23` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1839 | `model.layers.23` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1840 | `model.layers.23` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1841 | `model.layers.23.input_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9920.0 / -3.8388237847222224 / 472.46406358807013 | [NPY](tensors/0001841.npy) |
| 1842 | `model.layers.23.input_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / -0.008906150112549464 / 1.7358045703960834 | [NPY](tensors/0001842.npy) |
| 1843 | `model.layers.23.self_attn` | 15 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / -0.008906150112549464 / 1.7358045703960834 | [NPY](tensors/0001843.npy) |
| 1844 | `model.layers.23.self_attn` | 15 | `input.kwargs['attention_mask']` | [1, 1, 1, 320] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001844.npy) |
| 1845 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 319.0 / 319.0 / 319.0 / 0.0 | [NPY](tensors/0001845.npy) |
| 1846 | `model.layers.23.self_attn` | 15 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1847 | `model.layers.23.self_attn` | 15 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1848 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.265625 / 1.34375 / 0.6713409423828125 / 0.9952241382224756 | [NPY](tensors/0001848.npy) |
| 1849 | `model.layers.23.self_attn` | 15 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / -0.035349249839782715 / 0.6063876804299041 | [NPY](tensors/0001849.npy) |
| 1850 | `model.layers.23.self_attn` | 15 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1851 | `model.layers.23.self_attn.q_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / -0.008906150112549464 / 1.7358045703960834 | [NPY](tensors/0001851.npy) |
| 1852 | `model.layers.23.self_attn.q_proj` | 15 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.9375 / 15.75 / 0.03680485382210463 / 1.6201712230176377 | [NPY](tensors/0001852.npy) |
| 1853 | `model.layers.23.self_attn.k_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / -0.008906150112549464 / 1.7358045703960834 | [NPY](tensors/0001853.npy) |
| 1854 | `model.layers.23.self_attn.k_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -50.5 / 51.25 / 0.020796023309230804 / 5.59584994732802 | [NPY](tensors/0001854.npy) |
| 1855 | `model.layers.23.self_attn.v_proj` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.25 / 56.0 / -0.008906150112549464 / 1.7358045703960834 | [NPY](tensors/0001855.npy) |
| 1856 | `model.layers.23.self_attn.v_proj` | 15 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -20.625 / 12.5 / -0.1311969757080078 / 4.193230994115381 | [NPY](tensors/0001856.npy) |
| 1857 | `model.layers.23.self_attn.o_proj` | 15 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -18.125 / 6.125 / 0.0008762790821492672 / 1.4424686819461874 | [NPY](tensors/0001857.npy) |
| 1858 | `model.layers.23.self_attn.o_proj` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6528.0 / 6720.0 / 8.241671880086264 / 291.1212189324526 | [NPY](tensors/0001858.npy) |
| 1859 | `model.layers.23.self_attn` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6528.0 / 6720.0 / 8.241671880086264 / 291.1212189324526 | [NPY](tensors/0001859.npy) |
| 1860 | `model.layers.23.self_attn` | 15 | `output[1]` | [1, 64, 1, 320] | torch.bfloat16 → float32 | 2.6645352591003757e-14 / 0.875 / 0.0018696596857828087 / 0.016482622522289776 | [NPY](tensors/0001860.npy) |
| 1861 | `model.layers.23.post_attention_layernorm` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10752.0 / 10560.0 / 4.413711208767361 / 597.4184281839301 | [NPY](tensors/0001861.npy) |
| 1862 | `model.layers.23.post_attention_layernorm` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 9.0625 / -0.017340771357218423 / 1.0433093467652075 | [NPY](tensors/0001862.npy) |
| 1863 | `model.layers.23.mlp` | 15 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.0 / 9.0625 / -0.017340771357218423 / 1.0433093467652075 | [NPY](tensors/0001863.npy) |
| 1864 | `model.layers.23.mlp.experts` | 15 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.0 / 9.0625 / -0.017340771357218423 / 1.0433093467652075 | [NPY](tensors/0001864.npy) |
| 1865 | `model.layers.23.mlp.experts` | 15 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1866 | `model.layers.23.mlp.experts` | 15 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1867 | `model.layers.23.mlp.experts` | 15 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1868 | `model.layers.23.mlp.experts` | 15 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2352.0 / 1960.0 / -0.41327137417263454 / 106.00932075975322 | [NPY](tensors/0001868.npy) |
| 1869 | `model.layers.23.mlp` | 15 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2352.0 / 1960.0 / -0.41327137417263454 / 106.00932075975322 | [NPY](tensors/0001869.npy) |
| 1870 | `model.layers.23.mlp` | 15 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.6328125 / 1.0625 / 0.15093231201171875 / 0.6228606197813951 | [NPY](tensors/0001870.npy) |
| 1871 | `model.layers.23` | 15 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9792.0 / 9856.0 / 4.0021477593315975 / 587.3744857773098 | [NPY](tensors/0001871.npy) |
| 1950 | `model.layers.23` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8768.0 / 8832.0 / -4.626247829861111 / 420.45742861461116 | [NPY](tensors/0001950.npy) |
| 1951 | `model.layers.23` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 321] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001951.npy) |
| 1952 | `model.layers.23` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0001952.npy) |
| 1953 | `model.layers.23` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0001953.npy) |
| 1954 | `model.layers.23` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0001954.npy) |
| 1955 | `model.layers.23` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1956 | `model.layers.23` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1957 | `model.layers.23` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1958 | `model.layers.23.input_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8768.0 / 8832.0 / -4.626247829861111 / 420.45742861461116 | [NPY](tensors/0001958.npy) |
| 1959 | `model.layers.23.input_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.5 / -0.010547098186280992 / 1.7466091702030926 | [NPY](tensors/0001959.npy) |
| 1960 | `model.layers.23.self_attn` | 16 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.5 / -0.010547098186280992 / 1.7466091702030926 | [NPY](tensors/0001960.npy) |
| 1961 | `model.layers.23.self_attn` | 16 | `input.kwargs['attention_mask']` | [1, 1, 1, 321] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0001961.npy) |
| 1962 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 320.0 / 320.0 / 320.0 / 0.0 | [NPY](tensors/0001962.npy) |
| 1963 | `model.layers.23.self_attn` | 16 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 1964 | `model.layers.23.self_attn` | 16 | `input.kwargs['use_cache']` | — | bool | True | — |
| 1965 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.69775390625 / 0.9769506064729132 | [NPY](tensors/0001965.npy) |
| 1966 | `model.layers.23.self_attn` | 16 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.2734375 / 0.008575469255447388 / 0.6075148340976938 | [NPY](tensors/0001966.npy) |
| 1967 | `model.layers.23.self_attn` | 16 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 1968 | `model.layers.23.self_attn.q_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.5 / -0.010547098186280992 / 1.7466091702030926 | [NPY](tensors/0001968.npy) |
| 1969 | `model.layers.23.self_attn.q_proj` | 16 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.5625 / 17.625 / 0.03573844500351697 / 1.5524035542904595 | [NPY](tensors/0001969.npy) |
| 1970 | `model.layers.23.self_attn.k_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.5 / -0.010547098186280992 / 1.7466091702030926 | [NPY](tensors/0001970.npy) |
| 1971 | `model.layers.23.self_attn.k_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -65.5 / 54.5 / -0.058336153626441956 / 5.777672603273708 | [NPY](tensors/0001971.npy) |
| 1972 | `model.layers.23.self_attn.v_proj` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 56.5 / -0.010547098186280992 / 1.7466091702030926 | [NPY](tensors/0001972.npy) |
| 1973 | `model.layers.23.self_attn.v_proj` | 16 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.75 / 8.9375 / 0.15118587017059326 / 3.143102556431696 | [NPY](tensors/0001973.npy) |
| 1974 | `model.layers.23.self_attn.o_proj` | 16 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.0 / 6.8125 / -0.012935744947753847 / 1.1739305636767308 | [NPY](tensors/0001974.npy) |
| 1975 | `model.layers.23.self_attn.o_proj` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -6048.0 / 6336.0 / 7.381698269314236 / 271.086876252695 | [NPY](tensors/0001975.npy) |
| 1976 | `model.layers.23.self_attn` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6048.0 / 6336.0 / 7.381698269314236 / 271.086876252695 | [NPY](tensors/0001976.npy) |
| 1977 | `model.layers.23.self_attn` | 16 | `output[1]` | [1, 64, 1, 321] | torch.bfloat16 → float32 | 3.26405569239796e-14 / 0.83984375 / 0.0018031470741736266 / 0.01212905817328677 | [NPY](tensors/0001977.npy) |
| 1978 | `model.layers.23.post_attention_layernorm` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9600.0 / 2.7624891493055554 / 537.7251514294117 | [NPY](tensors/0001978.npy) |
| 1979 | `model.layers.23.post_attention_layernorm` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 7.53125 / -0.01847916046778361 / 0.968957902596089 | [NPY](tensors/0001979.npy) |
| 1980 | `model.layers.23.mlp` | 16 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 7.53125 / -0.01847916046778361 / 0.968957902596089 | [NPY](tensors/0001980.npy) |
| 1981 | `model.layers.23.mlp.experts` | 16 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.25 / 7.53125 / -0.01847916046778361 / 0.968957902596089 | [NPY](tensors/0001981.npy) |
| 1982 | `model.layers.23.mlp.experts` | 16 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 1983 | `model.layers.23.mlp.experts` | 16 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1984 | `model.layers.23.mlp.experts` | 16 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 1985 | `model.layers.23.mlp.experts` | 16 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1000.0 / 572.0 / -0.34022511376274955 / 45.208768709995184 | [NPY](tensors/0001985.npy) |
| 1986 | `model.layers.23.mlp` | 16 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1000.0 / 572.0 / -0.34022511376274955 / 45.208768709995184 | [NPY](tensors/0001986.npy) |
| 1987 | `model.layers.23.mlp` | 16 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.78125 / 1.1796875 / 0.19273829460144043 / 0.38709192849451285 | [NPY](tensors/0001987.npy) |
| 1988 | `model.layers.23` | 16 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9664.0 / 2.430908203125 / 541.605143475618 | [NPY](tensors/0001988.npy) |
| 2067 | `model.layers.23` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9792.0 / -6.447785101996528 / 458.2539081472683 | [NPY](tensors/0002067.npy) |
| 2068 | `model.layers.23` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002068.npy) |
| 2069 | `model.layers.23` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0002069.npy) |
| 2070 | `model.layers.23` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0002070.npy) |
| 2071 | `model.layers.23` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0002071.npy) |
| 2072 | `model.layers.23` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2073 | `model.layers.23` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2074 | `model.layers.23` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2075 | `model.layers.23.input_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9792.0 / -6.447785101996528 / 458.2539081472683 | [NPY](tensors/0002075.npy) |
| 2076 | `model.layers.23.input_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 56.75 / -0.006421156724294027 / 1.7675370007209936 | [NPY](tensors/0002076.npy) |
| 2077 | `model.layers.23.self_attn` | 17 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 56.75 / -0.006421156724294027 / 1.7675370007209936 | [NPY](tensors/0002077.npy) |
| 2078 | `model.layers.23.self_attn` | 17 | `input.kwargs['attention_mask']` | [1, 1, 1, 322] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002078.npy) |
| 2079 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 321.0 / 321.0 / 321.0 / 0.0 | [NPY](tensors/0002079.npy) |
| 2080 | `model.layers.23.self_attn` | 17 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2081 | `model.layers.23.self_attn` | 17 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2082 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.672332763671875 / 0.9654583841041487 | [NPY](tensors/0002082.npy) |
| 2083 | `model.layers.23.self_attn` | 17 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.05426234006881714 / 0.6503649986230469 | [NPY](tensors/0002083.npy) |
| 2084 | `model.layers.23.self_attn` | 17 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2085 | `model.layers.23.self_attn.q_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 56.75 / -0.006421156724294027 / 1.7675370007209936 | [NPY](tensors/0002085.npy) |
| 2086 | `model.layers.23.self_attn.q_proj` | 17 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.0625 / 15.375 / 0.045200750697404146 / 1.390859941483844 | [NPY](tensors/0002086.npy) |
| 2087 | `model.layers.23.self_attn.k_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 56.75 / -0.006421156724294027 / 1.7675370007209936 | [NPY](tensors/0002087.npy) |
| 2088 | `model.layers.23.self_attn.k_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -42.5 / 43.75 / -0.07298056781291962 / 5.126776979465604 | [NPY](tensors/0002088.npy) |
| 2089 | `model.layers.23.self_attn.v_proj` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -49.0 / 56.75 / -0.006421156724294027 / 1.7675370007209936 | [NPY](tensors/0002089.npy) |
| 2090 | `model.layers.23.self_attn.v_proj` | 17 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.25 / 7.4375 / -0.006035864353179932 / 2.081987750120961 | [NPY](tensors/0002090.npy) |
| 2091 | `model.layers.23.self_attn.o_proj` | 17 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.875 / 7.3125 / -0.04413216281682253 / 1.324309855485891 | [NPY](tensors/0002091.npy) |
| 2092 | `model.layers.23.self_attn.o_proj` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5632.0 / 5888.0 / 5.721439584096273 / 252.77143255105867 | [NPY](tensors/0002092.npy) |
| 2093 | `model.layers.23.self_attn` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5632.0 / 5888.0 / 5.721439584096273 / 252.77143255105867 | [NPY](tensors/0002093.npy) |
| 2094 | `model.layers.23.self_attn` | 17 | `output[1]` | [1, 64, 1, 322] | torch.bfloat16 → float32 | 6.465938895416912e-13 / 0.92578125 / 0.002226514616233103 / 0.014060116296187725 | [NPY](tensors/0002094.npy) |
| 2095 | `model.layers.23.post_attention_layernorm` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10944.0 / 9984.0 / -0.6982449001736111 / 548.5411078520364 | [NPY](tensors/0002095.npy) |
| 2096 | `model.layers.23.post_attention_layernorm` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 8.5625 / -0.027448965443505183 / 0.9669046544955594 | [NPY](tensors/0002096.npy) |
| 2097 | `model.layers.23.mlp` | 17 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.625 / 8.5625 / -0.027448965443505183 / 0.9669046544955594 | [NPY](tensors/0002097.npy) |
| 2098 | `model.layers.23.mlp.experts` | 17 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -29.625 / 8.5625 / -0.027448965443505183 / 0.9669046544955594 | [NPY](tensors/0002098.npy) |
| 2099 | `model.layers.23.mlp.experts` | 17 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2100 | `model.layers.23.mlp.experts` | 17 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2101 | `model.layers.23.mlp.experts` | 17 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2102 | `model.layers.23.mlp.experts` | 17 | `output` | [1, 2880] | torch.bfloat16 → float32 | -692.0 / 708.0 / -1.5148375935024685 / 57.98882646341171 | [NPY](tensors/0002102.npy) |
| 2103 | `model.layers.23.mlp` | 17 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -692.0 / 708.0 / -1.5148375935024685 / 57.98882646341171 | [NPY](tensors/0002103.npy) |
| 2104 | `model.layers.23.mlp` | 17 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.71484375 / 1.3125 / 0.03466033935546875 / 0.4260796683829846 | [NPY](tensors/0002104.npy) |
| 2105 | `model.layers.23` | 17 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10304.0 / 9408.0 / -2.2143446180555557 / 523.196810900763 | [NPY](tensors/0002105.npy) |
| 2184 | `model.layers.23` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 9984.0 / -3.3456380208333334 / 487.4353171914526 | [NPY](tensors/0002184.npy) |
| 2185 | `model.layers.23` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002185.npy) |
| 2186 | `model.layers.23` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0002186.npy) |
| 2187 | `model.layers.23` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0002187.npy) |
| 2188 | `model.layers.23` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0002188.npy) |
| 2189 | `model.layers.23` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2190 | `model.layers.23` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2191 | `model.layers.23` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2192 | `model.layers.23.input_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 9984.0 / -3.3456380208333334 / 487.4353171914526 | [NPY](tensors/0002192.npy) |
| 2193 | `model.layers.23.input_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 55.0 / -0.001436093118455675 / 1.7304208077498793 | [NPY](tensors/0002193.npy) |
| 2194 | `model.layers.23.self_attn` | 18 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 55.0 / -0.001436093118455675 / 1.7304208077498793 | [NPY](tensors/0002194.npy) |
| 2195 | `model.layers.23.self_attn` | 18 | `input.kwargs['attention_mask']` | [1, 1, 1, 323] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002195.npy) |
| 2196 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 322.0 / 322.0 / 322.0 / 0.0 | [NPY](tensors/0002196.npy) |
| 2197 | `model.layers.23.self_attn` | 18 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2198 | `model.layers.23.self_attn` | 18 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2199 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6120681762695312 / 0.9910055868303792 | [NPY](tensors/0002199.npy) |
| 2200 | `model.layers.23.self_attn` | 18 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.05691227316856384 / 0.6712295436692187 | [NPY](tensors/0002200.npy) |
| 2201 | `model.layers.23.self_attn` | 18 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2202 | `model.layers.23.self_attn.q_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 55.0 / -0.001436093118455675 / 1.7304208077498793 | [NPY](tensors/0002202.npy) |
| 2203 | `model.layers.23.self_attn.q_proj` | 18 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -9.75 / 16.5 / 0.0429055392742157 / 1.4197422895287213 | [NPY](tensors/0002203.npy) |
| 2204 | `model.layers.23.self_attn.k_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 55.0 / -0.001436093118455675 / 1.7304208077498793 | [NPY](tensors/0002204.npy) |
| 2205 | `model.layers.23.self_attn.k_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.0 / 43.5 / -0.09864985942840576 / 4.784206909942606 | [NPY](tensors/0002205.npy) |
| 2206 | `model.layers.23.self_attn.v_proj` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.75 / 55.0 / -0.001436093118455675 / 1.7304208077498793 | [NPY](tensors/0002206.npy) |
| 2207 | `model.layers.23.self_attn.v_proj` | 18 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.125 / 9.1875 / -0.071186363697052 / 2.8893792379534116 | [NPY](tensors/0002207.npy) |
| 2208 | `model.layers.23.self_attn.o_proj` | 18 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.8125 / 7.9375 / -0.02282929641660303 / 0.9593501183596213 | [NPY](tensors/0002208.npy) |
| 2209 | `model.layers.23.self_attn.o_proj` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 5824.0 / 6.148479991488987 / 247.2361977045327 | [NPY](tensors/0002209.npy) |
| 2210 | `model.layers.23.self_attn` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 5824.0 / 6.148479991488987 / 247.2361977045327 | [NPY](tensors/0002210.npy) |
| 2211 | `model.layers.23.self_attn` | 18 | `output[1]` | [1, 64, 1, 323] | torch.bfloat16 → float32 | 5.162537064506978e-15 / 0.86328125 / 0.001300581117751206 / 0.009978248371766604 | [NPY](tensors/0002211.npy) |
| 2212 | `model.layers.23.post_attention_layernorm` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10816.0 / 10496.0 / 2.8155110677083335 / 577.799602556475 | [NPY](tensors/0002212.npy) |
| 2213 | `model.layers.23.post_attention_layernorm` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 7.78125 / -0.019619981778992546 / 1.0632478179288398 | [NPY](tensors/0002213.npy) |
| 2214 | `model.layers.23.mlp` | 18 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 7.78125 / -0.019619981778992546 / 1.0632478179288398 | [NPY](tensors/0002214.npy) |
| 2215 | `model.layers.23.mlp.experts` | 18 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.0 / 7.78125 / -0.019619981778992546 / 1.0632478179288398 | [NPY](tensors/0002215.npy) |
| 2216 | `model.layers.23.mlp.experts` | 18 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2217 | `model.layers.23.mlp.experts` | 18 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2218 | `model.layers.23.mlp.experts` | 18 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2219 | `model.layers.23.mlp.experts` | 18 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1160.0 / 816.0 / -0.5227657106187609 / 57.87847831908742 | [NPY](tensors/0002219.npy) |
| 2220 | `model.layers.23.mlp` | 18 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1160.0 / 816.0 / -0.5227657106187609 / 57.87847831908742 | [NPY](tensors/0002220.npy) |
| 2221 | `model.layers.23.mlp` | 18 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.86328125 / 1.5 / 0.006977081298828125 / 0.47365981876358937 | [NPY](tensors/0002221.npy) |
| 2222 | `model.layers.23` | 18 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10368.0 / 10048.0 / 2.2612413194444443 / 565.2319364244661 | [NPY](tensors/0002222.npy) |
| 2301 | `model.layers.23` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10240.0 / 1.3515706380208334 / 480.1811232097893 | [NPY](tensors/0002301.npy) |
| 2302 | `model.layers.23` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002302.npy) |
| 2303 | `model.layers.23` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0002303.npy) |
| 2304 | `model.layers.23` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0002304.npy) |
| 2305 | `model.layers.23` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0002305.npy) |
| 2306 | `model.layers.23` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2307 | `model.layers.23` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2308 | `model.layers.23` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2309 | `model.layers.23.input_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 10240.0 / 1.3515706380208334 / 480.1811232097893 | [NPY](tensors/0002309.npy) |
| 2310 | `model.layers.23.input_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 57.25 / 0.014616542392306857 / 1.7427049222830853 | [NPY](tensors/0002310.npy) |
| 2311 | `model.layers.23.self_attn` | 19 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 57.25 / 0.014616542392306857 / 1.7427049222830853 | [NPY](tensors/0002311.npy) |
| 2312 | `model.layers.23.self_attn` | 19 | `input.kwargs['attention_mask']` | [1, 1, 1, 324] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002312.npy) |
| 2313 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 323.0 / 323.0 / 323.0 / 0.0 | [NPY](tensors/0002313.npy) |
| 2314 | `model.layers.23.self_attn` | 19 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2315 | `model.layers.23.self_attn` | 19 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2316 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.56378173828125 / 1.0666243902954833 | [NPY](tensors/0002316.npy) |
| 2317 | `model.layers.23.self_attn` | 19 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.2734375 / 0.0013155341148376465 / 0.594453943411649 | [NPY](tensors/0002317.npy) |
| 2318 | `model.layers.23.self_attn` | 19 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2319 | `model.layers.23.self_attn.q_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 57.25 / 0.014616542392306857 / 1.7427049222830853 | [NPY](tensors/0002319.npy) |
| 2320 | `model.layers.23.self_attn.q_proj` | 19 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -8.5 / 15.6875 / 0.05329700405127369 / 1.3646946365323112 | [NPY](tensors/0002320.npy) |
| 2321 | `model.layers.23.self_attn.k_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 57.25 / 0.014616542392306857 / 1.7427049222830853 | [NPY](tensors/0002321.npy) |
| 2322 | `model.layers.23.self_attn.k_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.0 / 37.0 / -0.09258433617651463 / 4.636315007367592 | [NPY](tensors/0002322.npy) |
| 2323 | `model.layers.23.self_attn.v_proj` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 57.25 / 0.014616542392306857 / 1.7427049222830853 | [NPY](tensors/0002323.npy) |
| 2324 | `model.layers.23.self_attn.v_proj` | 19 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.375 / 8.75 / -0.15375615656375885 / 2.985250983277707 | [NPY](tensors/0002324.npy) |
| 2325 | `model.layers.23.self_attn.o_proj` | 19 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.4375 / 8.0625 / -0.023457489907741547 / 1.5201202408917844 | [NPY](tensors/0002325.npy) |
| 2326 | `model.layers.23.self_attn.o_proj` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 5696.0 / 6.04831780327691 / 247.14833687217293 | [NPY](tensors/0002326.npy) |
| 2327 | `model.layers.23.self_attn` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5504.0 / 5696.0 / 6.04831780327691 / 247.14833687217293 | [NPY](tensors/0002327.npy) |
| 2328 | `model.layers.23.self_attn` | 19 | `output[1]` | [1, 64, 1, 324] | torch.bfloat16 → float32 | 2.731148640577885e-14 / 0.8984375 / 0.002194938224750152 / 0.013787887397893883 | [NPY](tensors/0002328.npy) |
| 2329 | `model.layers.23.post_attention_layernorm` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 10112.0 / 7.393478732638889 / 553.2585060534806 | [NPY](tensors/0002329.npy) |
| 2330 | `model.layers.23.post_attention_layernorm` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 9.3125 / -0.004868221282958984 / 0.9941159275792238 | [NPY](tensors/0002330.npy) |
| 2331 | `model.layers.23.mlp` | 19 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.25 / 9.3125 / -0.004868221282958984 / 0.9941159275792238 | [NPY](tensors/0002331.npy) |
| 2332 | `model.layers.23.mlp.experts` | 19 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.25 / 9.3125 / -0.004868221282958984 / 0.9941159275792238 | [NPY](tensors/0002332.npy) |
| 2333 | `model.layers.23.mlp.experts` | 19 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2334 | `model.layers.23.mlp.experts` | 19 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2335 | `model.layers.23.mlp.experts` | 19 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2336 | `model.layers.23.mlp.experts` | 19 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1456.0 / 1080.0 / 0.1761167738172743 / 72.75829203697538 | [NPY](tensors/0002336.npy) |
| 2337 | `model.layers.23.mlp` | 19 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1456.0 / 1080.0 / 0.1761167738172743 / 72.75829203697538 | [NPY](tensors/0002337.npy) |
| 2338 | `model.layers.23.mlp` | 19 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.82421875 / 1.203125 / 0.1278839111328125 / 0.395701421927471 | [NPY](tensors/0002338.npy) |
| 2339 | `model.layers.23` | 19 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10176.0 / 9920.0 / 7.557199435763889 / 549.0557362852273 | [NPY](tensors/0002339.npy) |
| 2418 | `model.layers.23` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9664.0 / -2.759506564670139 / 451.92459114712204 | [NPY](tensors/0002418.npy) |
| 2419 | `model.layers.23` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002419.npy) |
| 2420 | `model.layers.23` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0002420.npy) |
| 2421 | `model.layers.23` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0002421.npy) |
| 2422 | `model.layers.23` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0002422.npy) |
| 2423 | `model.layers.23` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2424 | `model.layers.23` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2425 | `model.layers.23` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2426 | `model.layers.23.input_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9664.0 / -2.759506564670139 / 451.92459114712204 | [NPY](tensors/0002426.npy) |
| 2427 | `model.layers.23.input_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 54.0 / -0.004436247878604465 / 1.7283305294796718 | [NPY](tensors/0002427.npy) |
| 2428 | `model.layers.23.self_attn` | 20 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 54.0 / -0.004436247878604465 / 1.7283305294796718 | [NPY](tensors/0002428.npy) |
| 2429 | `model.layers.23.self_attn` | 20 | `input.kwargs['attention_mask']` | [1, 1, 1, 325] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002429.npy) |
| 2430 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 324.0 / 324.0 / 324.0 / 0.0 | [NPY](tensors/0002430.npy) |
| 2431 | `model.layers.23.self_attn` | 20 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2432 | `model.layers.23.self_attn` | 20 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2433 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.57232666015625 / 1.0787558972909173 | [NPY](tensors/0002433.npy) |
| 2434 | `model.layers.23.self_attn` | 20 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.28125 / -0.08452567458152771 / 0.5568571011489967 | [NPY](tensors/0002434.npy) |
| 2435 | `model.layers.23.self_attn` | 20 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2436 | `model.layers.23.self_attn.q_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 54.0 / -0.004436247878604465 / 1.7283305294796718 | [NPY](tensors/0002436.npy) |
| 2437 | `model.layers.23.self_attn.q_proj` | 20 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.4375 / 15.8125 / 0.04878704471047968 / 1.5565803744539384 | [NPY](tensors/0002437.npy) |
| 2438 | `model.layers.23.self_attn.k_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 54.0 / -0.004436247878604465 / 1.7283305294796718 | [NPY](tensors/0002438.npy) |
| 2439 | `model.layers.23.self_attn.k_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -43.0 / 35.75 / 0.024780988693237305 / 5.478653236014003 | [NPY](tensors/0002439.npy) |
| 2440 | `model.layers.23.self_attn.v_proj` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 54.0 / -0.004436247878604465 / 1.7283305294796718 | [NPY](tensors/0002440.npy) |
| 2441 | `model.layers.23.self_attn.v_proj` | 20 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.0 / 14.3125 / -0.022156953811645508 / 4.032368007911188 | [NPY](tensors/0002441.npy) |
| 2442 | `model.layers.23.self_attn.o_proj` | 20 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.375 / 6.4375 / 0.0008142264559864998 / 1.3814172745113054 | [NPY](tensors/0002442.npy) |
| 2443 | `model.layers.23.self_attn.o_proj` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5920.0 / 6112.0 / 8.456724548339844 / 260.9159111196334 | [NPY](tensors/0002443.npy) |
| 2444 | `model.layers.23.self_attn` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5920.0 / 6112.0 / 8.456724548339844 / 260.9159111196334 | [NPY](tensors/0002444.npy) |
| 2445 | `model.layers.23.self_attn` | 20 | `output[1]` | [1, 64, 1, 325] | torch.bfloat16 → float32 | 5.440092820663267e-15 / 0.90625 / 0.0018467951596300295 / 0.013582215165738237 | [NPY](tensors/0002445.npy) |
| 2446 | `model.layers.23.post_attention_layernorm` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 9984.0 / 5.694514973958333 / 549.9115378853077 | [NPY](tensors/0002446.npy) |
| 2447 | `model.layers.23.post_attention_layernorm` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 9.125 / -0.0064081314537260264 / 1.0128306305181987 | [NPY](tensors/0002447.npy) |
| 2448 | `model.layers.23.mlp` | 20 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 9.125 / -0.0064081314537260264 / 1.0128306305181987 | [NPY](tensors/0002448.npy) |
| 2449 | `model.layers.23.mlp.experts` | 20 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.5 / 9.125 / -0.0064081314537260264 / 1.0128306305181987 | [NPY](tensors/0002449.npy) |
| 2450 | `model.layers.23.mlp.experts` | 20 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2451 | `model.layers.23.mlp.experts` | 20 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2452 | `model.layers.23.mlp.experts` | 20 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2453 | `model.layers.23.mlp.experts` | 20 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1816.0 / 1472.0 / -0.8227627489301893 / 84.0838158961308 | [NPY](tensors/0002453.npy) |
| 2454 | `model.layers.23.mlp` | 20 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1816.0 / 1472.0 / -0.8227627489301893 / 84.0838158961308 | [NPY](tensors/0002454.npy) |
| 2455 | `model.layers.23.mlp` | 20 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.0625 / 0.11692047119140625 / 0.520515846596152 | [NPY](tensors/0002455.npy) |
| 2456 | `model.layers.23` | 20 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9920.0 / 9536.0 / 4.886287434895833 / 539.024019723015 | [NPY](tensors/0002456.npy) |
| 2535 | `model.layers.23` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9088.0 / -4.2484551323784725 / 431.6948033896613 | [NPY](tensors/0002535.npy) |
| 2536 | `model.layers.23` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002536.npy) |
| 2537 | `model.layers.23` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0002537.npy) |
| 2538 | `model.layers.23` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0002538.npy) |
| 2539 | `model.layers.23` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0002539.npy) |
| 2540 | `model.layers.23` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2541 | `model.layers.23` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2542 | `model.layers.23` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2543 | `model.layers.23.input_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 9088.0 / -4.2484551323784725 / 431.6948033896613 | [NPY](tensors/0002543.npy) |
| 2544 | `model.layers.23.input_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 56.5 / -0.008287039068010118 / 1.755680059849112 | [NPY](tensors/0002544.npy) |
| 2545 | `model.layers.23.self_attn` | 21 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 56.5 / -0.008287039068010118 / 1.755680059849112 | [NPY](tensors/0002545.npy) |
| 2546 | `model.layers.23.self_attn` | 21 | `input.kwargs['attention_mask']` | [1, 1, 1, 326] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002546.npy) |
| 2547 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 325.0 / 325.0 / 325.0 / 0.0 | [NPY](tensors/0002547.npy) |
| 2548 | `model.layers.23.self_attn` | 21 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2549 | `model.layers.23.self_attn` | 21 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2550 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.642181396484375 / 0.9966882422938053 | [NPY](tensors/0002550.npy) |
| 2551 | `model.layers.23.self_attn` | 21 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.28125 / -0.14685702323913574 / 0.6180212443372857 | [NPY](tensors/0002551.npy) |
| 2552 | `model.layers.23.self_attn` | 21 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2553 | `model.layers.23.self_attn.q_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 56.5 / -0.008287039068010118 / 1.755680059849112 | [NPY](tensors/0002553.npy) |
| 2554 | `model.layers.23.self_attn.q_proj` | 21 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.625 / 15.125 / 0.03701616951730102 / 1.4604544656385865 | [NPY](tensors/0002554.npy) |
| 2555 | `model.layers.23.self_attn.k_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 56.5 / -0.008287039068010118 / 1.755680059849112 | [NPY](tensors/0002555.npy) |
| 2556 | `model.layers.23.self_attn.k_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.0 / 45.5 / 0.006867766380310059 / 5.592825200274788 | [NPY](tensors/0002556.npy) |
| 2557 | `model.layers.23.self_attn.v_proj` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 56.5 / -0.008287039068010118 / 1.755680059849112 | [NPY](tensors/0002557.npy) |
| 2558 | `model.layers.23.self_attn.v_proj` | 21 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.125 / 13.0625 / 0.07182395458221436 / 3.043155221973189 | [NPY](tensors/0002558.npy) |
| 2559 | `model.layers.23.self_attn.o_proj` | 21 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.875 / 7.5625 / -0.02264253841713071 / 1.2045548138613749 | [NPY](tensors/0002559.npy) |
| 2560 | `model.layers.23.self_attn.o_proj` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5792.0 / 6048.0 / 6.439470163981119 / 258.82921238907494 | [NPY](tensors/0002560.npy) |
| 2561 | `model.layers.23.self_attn` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5792.0 / 6048.0 / 6.439470163981119 / 258.82921238907494 | [NPY](tensors/0002561.npy) |
| 2562 | `model.layers.23.self_attn` | 21 | `output[1]` | [1, 64, 1, 326] | torch.bfloat16 → float32 | 4.907185768843192e-14 / 0.8671875 / 0.001692590980634313 / 0.011055818425261816 | [NPY](tensors/0002562.npy) |
| 2563 | `model.layers.23.post_attention_layernorm` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9984.0 / 9472.0 / 2.1958658854166666 / 530.0110252129627 | [NPY](tensors/0002563.npy) |
| 2564 | `model.layers.23.post_attention_layernorm` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.25 / 8.5 / -0.018424657980600993 / 0.9954181513131256 | [NPY](tensors/0002564.npy) |
| 2565 | `model.layers.23.mlp` | 21 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.25 / 8.5 / -0.018424657980600993 / 0.9954181513131256 | [NPY](tensors/0002565.npy) |
| 2566 | `model.layers.23.mlp.experts` | 21 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -29.25 / 8.5 / -0.018424657980600993 / 0.9954181513131256 | [NPY](tensors/0002566.npy) |
| 2567 | `model.layers.23.mlp.experts` | 21 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2568 | `model.layers.23.mlp.experts` | 21 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2569 | `model.layers.23.mlp.experts` | 21 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2570 | `model.layers.23.mlp.experts` | 21 | `output` | [1, 2880] | torch.bfloat16 → float32 | -924.0 / 564.0 / -0.28173917134602866 / 51.56880446450731 | [NPY](tensors/0002570.npy) |
| 2571 | `model.layers.23.mlp` | 21 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -924.0 / 564.0 / -0.28173917134602866 / 51.56880446450731 | [NPY](tensors/0002571.npy) |
| 2572 | `model.layers.23.mlp` | 21 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -0.8046875 / 1.2578125 / 0.13232994079589844 / 0.4310762116661536 | [NPY](tensors/0002572.npy) |
| 2573 | `model.layers.23` | 21 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9344.0 / 1.9370768229166666 / 521.5284061846129 | [NPY](tensors/0002573.npy) |
| 2652 | `model.layers.23` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 9472.0 / -6.6865858289930555 / 441.4343306844747 | [NPY](tensors/0002652.npy) |
| 2653 | `model.layers.23` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002653.npy) |
| 2654 | `model.layers.23` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0002654.npy) |
| 2655 | `model.layers.23` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0002655.npy) |
| 2656 | `model.layers.23` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0002656.npy) |
| 2657 | `model.layers.23` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2658 | `model.layers.23` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2659 | `model.layers.23` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2660 | `model.layers.23.input_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10560.0 / 9472.0 / -6.6865858289930555 / 441.4343306844747 | [NPY](tensors/0002660.npy) |
| 2661 | `model.layers.23.input_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 51.5 / -0.007722187042236328 / 1.7387604642068377 | [NPY](tensors/0002661.npy) |
| 2662 | `model.layers.23.self_attn` | 22 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 51.5 / -0.007722187042236328 / 1.7387604642068377 | [NPY](tensors/0002662.npy) |
| 2663 | `model.layers.23.self_attn` | 22 | `input.kwargs['attention_mask']` | [1, 1, 1, 327] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002663.npy) |
| 2664 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 326.0 / 326.0 / 326.0 / 0.0 | [NPY](tensors/0002664.npy) |
| 2665 | `model.layers.23.self_attn` | 22 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2666 | `model.layers.23.self_attn` | 22 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2667 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.7359704971313477 / 0.9162170422568309 | [NPY](tensors/0002667.npy) |
| 2668 | `model.layers.23.self_attn` | 22 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.28125 / -0.14859804511070251 / 0.6369306733537604 | [NPY](tensors/0002668.npy) |
| 2669 | `model.layers.23.self_attn` | 22 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2670 | `model.layers.23.self_attn.q_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 51.5 / -0.007722187042236328 / 1.7387604642068377 | [NPY](tensors/0002670.npy) |
| 2671 | `model.layers.23.self_attn.q_proj` | 22 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -7.5 / 15.0625 / 0.029229806154035032 / 1.4668876617591315 | [NPY](tensors/0002671.npy) |
| 2672 | `model.layers.23.self_attn.k_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 51.5 / -0.007722187042236328 / 1.7387604642068377 | [NPY](tensors/0002672.npy) |
| 2673 | `model.layers.23.self_attn.k_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -49.75 / 45.75 / -0.10057798400521278 / 5.429887339873362 | [NPY](tensors/0002673.npy) |
| 2674 | `model.layers.23.self_attn.v_proj` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.5 / 51.5 / -0.007722187042236328 / 1.7387604642068377 | [NPY](tensors/0002674.npy) |
| 2675 | `model.layers.23.self_attn.v_proj` | 22 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.125 / 7.28125 / 0.03990679979324341 / 2.4323116132807847 | [NPY](tensors/0002675.npy) |
| 2676 | `model.layers.23.self_attn.o_proj` | 22 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -18.875 / 6.90625 / -0.033134757075458765 / 1.3810099724292604 | [NPY](tensors/0002676.npy) |
| 2677 | `model.layers.23.self_attn.o_proj` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5728.0 / 5888.0 / 5.466727595859104 / 255.77999086577086 | [NPY](tensors/0002677.npy) |
| 2678 | `model.layers.23.self_attn` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5728.0 / 5888.0 / 5.466727595859104 / 255.77999086577086 | [NPY](tensors/0002678.npy) |
| 2679 | `model.layers.23.self_attn` | 22 | `output[1]` | [1, 64, 1, 327] | torch.bfloat16 → float32 | 7.438494264988549e-15 / 0.97265625 / 0.0022136844437282144 / 0.014248198817274094 | [NPY](tensors/0002679.npy) |
| 2680 | `model.layers.23.post_attention_layernorm` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11072.0 / 9920.0 / -1.2142930772569445 / 542.1886568029428 | [NPY](tensors/0002680.npy) |
| 2681 | `model.layers.23.post_attention_layernorm` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 7.09375 / -0.025933800141016643 / 1.0394531308866206 | [NPY](tensors/0002681.npy) |
| 2682 | `model.layers.23.mlp` | 22 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -31.5 / 7.09375 / -0.025933800141016643 / 1.0394531308866206 | [NPY](tensors/0002682.npy) |
| 2683 | `model.layers.23.mlp.experts` | 22 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -31.5 / 7.09375 / -0.025933800141016643 / 1.0394531308866206 | [NPY](tensors/0002683.npy) |
| 2684 | `model.layers.23.mlp.experts` | 22 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2685 | `model.layers.23.mlp.experts` | 22 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2686 | `model.layers.23.mlp.experts` | 22 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2687 | `model.layers.23.mlp.experts` | 22 | `output` | [1, 2880] | torch.bfloat16 → float32 | -840.0 / 684.0 / -2.168507046169705 / 61.93098979747597 | [NPY](tensors/0002687.npy) |
| 2688 | `model.layers.23.mlp` | 22 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -840.0 / 684.0 / -2.168507046169705 / 61.93098979747597 | [NPY](tensors/0002688.npy) |
| 2689 | `model.layers.23.mlp` | 22 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.0 / 1.21875 / 0.014515876770019531 / 0.4900490314149707 | [NPY](tensors/0002689.npy) |
| 2690 | `model.layers.23` | 22 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9472.0 / -3.380365668402778 / 523.396869645866 | [NPY](tensors/0002690.npy) |
| 2769 | `model.layers.23` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 10176.0 / -5.170998806423611 / 430.255652772262 | [NPY](tensors/0002769.npy) |
| 2770 | `model.layers.23` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002770.npy) |
| 2771 | `model.layers.23` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0002771.npy) |
| 2772 | `model.layers.23` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0002772.npy) |
| 2773 | `model.layers.23` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0002773.npy) |
| 2774 | `model.layers.23` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2775 | `model.layers.23` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2776 | `model.layers.23` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2777 | `model.layers.23.input_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10432.0 / 10176.0 / -5.170998806423611 / 430.255652772262 | [NPY](tensors/0002777.npy) |
| 2778 | `model.layers.23.input_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 63.5 / 0.0009075116780069139 / 1.8316848185815433 | [NPY](tensors/0002778.npy) |
| 2779 | `model.layers.23.self_attn` | 23 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 63.5 / 0.0009075116780069139 / 1.8316848185815433 | [NPY](tensors/0002779.npy) |
| 2780 | `model.layers.23.self_attn` | 23 | `input.kwargs['attention_mask']` | [1, 1, 1, 328] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002780.npy) |
| 2781 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 327.0 / 327.0 / 327.0 / 0.0 | [NPY](tensors/0002781.npy) |
| 2782 | `model.layers.23.self_attn` | 23 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2783 | `model.layers.23.self_attn` | 23 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2784 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.802703857421875 / 0.8603227585637486 | [NPY](tensors/0002784.npy) |
| 2785 | `model.layers.23.self_attn` | 23 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.28125 / -0.09632280468940735 / 0.6444531895940394 | [NPY](tensors/0002785.npy) |
| 2786 | `model.layers.23.self_attn` | 23 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2787 | `model.layers.23.self_attn.q_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 63.5 / 0.0009075116780069139 / 1.8316848185815433 | [NPY](tensors/0002787.npy) |
| 2788 | `model.layers.23.self_attn.q_proj` | 23 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.5625 / 16.5 / 0.032813038444146514 / 1.5253062603146619 | [NPY](tensors/0002788.npy) |
| 2789 | `model.layers.23.self_attn.k_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 63.5 / 0.0009075116780069139 / 1.8316848185815433 | [NPY](tensors/0002789.npy) |
| 2790 | `model.layers.23.self_attn.k_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -48.5 / 38.0 / -0.10566797852516174 / 4.570068129776858 | [NPY](tensors/0002790.npy) |
| 2791 | `model.layers.23.self_attn.v_proj` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.25 / 63.5 / 0.0009075116780069139 / 1.8316848185815433 | [NPY](tensors/0002791.npy) |
| 2792 | `model.layers.23.self_attn.v_proj` | 23 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.5 / 16.5 / 0.237341046333313 / 3.8002850463854707 | [NPY](tensors/0002792.npy) |
| 2793 | `model.layers.23.self_attn.o_proj` | 23 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.6875 / 6.6875 / 0.06318822503089905 / 1.3050765519697205 | [NPY](tensors/0002793.npy) |
| 2794 | `model.layers.23.self_attn.o_proj` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3456.0 / 3520.0 / 2.6391210556030273 / 169.90793009267404 | [NPY](tensors/0002794.npy) |
| 2795 | `model.layers.23.self_attn` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3456.0 / 3520.0 / 2.6391210556030273 / 169.90793009267404 | [NPY](tensors/0002795.npy) |
| 2796 | `model.layers.23.self_attn` | 23 | `output[1]` | [1, 64, 1, 328] | torch.bfloat16 → float32 | 3.694961003830599e-16 / 0.96875 / 0.002345929408707388 / 0.01604238571030634 | [NPY](tensors/0002796.npy) |
| 2797 | `model.layers.23.post_attention_layernorm` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8512.0 / 8096.0 / -2.5349290635850696 / 405.5567698430782 | [NPY](tensors/0002797.npy) |
| 2798 | `model.layers.23.post_attention_layernorm` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.75 / 7.0625 / -0.029657975832621256 / 1.055418373474076 | [NPY](tensors/0002798.npy) |
| 2799 | `model.layers.23.mlp` | 23 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.75 / 7.0625 / -0.029657975832621256 / 1.055418373474076 | [NPY](tensors/0002799.npy) |
| 2800 | `model.layers.23.mlp.experts` | 23 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -28.75 / 7.0625 / -0.029657975832621256 / 1.055418373474076 | [NPY](tensors/0002800.npy) |
| 2801 | `model.layers.23.mlp.experts` | 23 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2802 | `model.layers.23.mlp.experts` | 23 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2803 | `model.layers.23.mlp.experts` | 23 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2804 | `model.layers.23.mlp.experts` | 23 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3104.0 / 2944.0 / -1.8427688598632812 / 154.1093733674892 | [NPY](tensors/0002804.npy) |
| 2805 | `model.layers.23.mlp` | 23 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3104.0 / 2944.0 / -1.8427688598632812 / 154.1093733674892 | [NPY](tensors/0002805.npy) |
| 2806 | `model.layers.23.mlp` | 23 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.046875 / 1.1875 / -0.0249176025390625 / 0.7814843134871461 | [NPY](tensors/0002806.npy) |
| 2807 | `model.layers.23` | 23 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5568.0 / 4992.0 / -4.380240885416667 / 310.6940433194878 | [NPY](tensors/0002807.npy) |
| 2886 | `model.layers.23` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9600.0 / -1.8610297309027777 / 414.56497506258694 | [NPY](tensors/0002886.npy) |
| 2887 | `model.layers.23` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002887.npy) |
| 2888 | `model.layers.23` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0002888.npy) |
| 2889 | `model.layers.23` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0002889.npy) |
| 2890 | `model.layers.23` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0002890.npy) |
| 2891 | `model.layers.23` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2892 | `model.layers.23` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2893 | `model.layers.23` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2894 | `model.layers.23.input_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10112.0 / 9600.0 / -1.8610297309027777 / 414.56497506258694 | [NPY](tensors/0002894.npy) |
| 2895 | `model.layers.23.input_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 62.25 / 0.013211989402770996 / 1.8263920898741788 | [NPY](tensors/0002895.npy) |
| 2896 | `model.layers.23.self_attn` | 24 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 62.25 / 0.013211989402770996 / 1.8263920898741788 | [NPY](tensors/0002896.npy) |
| 2897 | `model.layers.23.self_attn` | 24 | `input.kwargs['attention_mask']` | [1, 1, 1, 329] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0002897.npy) |
| 2898 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 328.0 / 328.0 / 328.0 / 0.0 | [NPY](tensors/0002898.npy) |
| 2899 | `model.layers.23.self_attn` | 24 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 2900 | `model.layers.23.self_attn` | 24 | `input.kwargs['use_cache']` | — | bool | True | — |
| 2901 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1484375 / 1.34375 / 0.817108154296875 / 0.820964163268981 | [NPY](tensors/0002901.npy) |
| 2902 | `model.layers.23.self_attn` | 24 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.2890625 / -0.02890107035636902 / 0.6827631156187098 | [NPY](tensors/0002902.npy) |
| 2903 | `model.layers.23.self_attn` | 24 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 2904 | `model.layers.23.self_attn.q_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 62.25 / 0.013211989402770996 / 1.8263920898741788 | [NPY](tensors/0002904.npy) |
| 2905 | `model.layers.23.self_attn.q_proj` | 24 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.3125 / 15.1875 / 0.04348959098570049 / 1.5647034356664595 | [NPY](tensors/0002905.npy) |
| 2906 | `model.layers.23.self_attn.k_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 62.25 / 0.013211989402770996 / 1.8263920898741788 | [NPY](tensors/0002906.npy) |
| 2907 | `model.layers.23.self_attn.k_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.75 / 32.5 / -0.11042919754981995 / 4.488127821515643 | [NPY](tensors/0002907.npy) |
| 2908 | `model.layers.23.self_attn.v_proj` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 62.25 / 0.013211989402770996 / 1.8263920898741788 | [NPY](tensors/0002908.npy) |
| 2909 | `model.layers.23.self_attn.v_proj` | 24 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.75 / 18.875 / 0.14136523008346558 / 4.517428807650585 | [NPY](tensors/0002909.npy) |
| 2910 | `model.layers.23.self_attn.o_proj` | 24 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.4375 / 7.90625 / 0.057075496995821595 / 1.2282814183719806 | [NPY](tensors/0002910.npy) |
| 2911 | `model.layers.23.self_attn.o_proj` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2848.0 / 2816.0 / 1.992841805352105 / 145.38204258684002 | [NPY](tensors/0002911.npy) |
| 2912 | `model.layers.23.self_attn` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2848.0 / 2816.0 / 1.992841805352105 / 145.38204258684002 | [NPY](tensors/0002912.npy) |
| 2913 | `model.layers.23.self_attn` | 24 | `output[1]` | [1, 64, 1, 329] | torch.bfloat16 → float32 | 3.730349362740526e-14 / 0.953125 / 0.0018515023511337836 / 0.013327234703454139 | [NPY](tensors/0002913.npy) |
| 2914 | `model.layers.23.post_attention_layernorm` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8256.0 / 7776.0 / 0.13700900607638888 / 374.924668958621 | [NPY](tensors/0002914.npy) |
| 2915 | `model.layers.23.post_attention_layernorm` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.125 / 9.75 / -0.017688242594401042 / 1.0396218138900666 | [NPY](tensors/0002915.npy) |
| 2916 | `model.layers.23.mlp` | 24 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -27.125 / 9.75 / -0.017688242594401042 / 1.0396218138900666 | [NPY](tensors/0002916.npy) |
| 2917 | `model.layers.23.mlp.experts` | 24 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -27.125 / 9.75 / -0.017688242594401042 / 1.0396218138900666 | [NPY](tensors/0002917.npy) |
| 2918 | `model.layers.23.mlp.experts` | 24 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 2919 | `model.layers.23.mlp.experts` | 24 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2920 | `model.layers.23.mlp.experts` | 24 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 2921 | `model.layers.23.mlp.experts` | 24 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4064.0 / 3904.0 / -1.76745189693239 / 194.11715711731 | [NPY](tensors/0002921.npy) |
| 2922 | `model.layers.23.mlp` | 24 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4064.0 / 3904.0 / -1.76745189693239 / 194.11715711731 | [NPY](tensors/0002922.npy) |
| 2923 | `model.layers.23.mlp` | 24 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.765625 / 1.359375 / -0.12843704223632812 / 0.8716742823953592 | [NPY](tensors/0002923.npy) |
| 2924 | `model.layers.23` | 24 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4416.0 / 3888.0 / -1.6345567491319444 / 253.40337866753265 | [NPY](tensors/0002924.npy) |
| 3003 | `model.layers.23` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10752.0 / 10432.0 / 0.10021158854166666 / 444.5192392129245 | [NPY](tensors/0003003.npy) |
| 3004 | `model.layers.23` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 330] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003004.npy) |
| 3005 | `model.layers.23` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0003005.npy) |
| 3006 | `model.layers.23` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0003006.npy) |
| 3007 | `model.layers.23` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0003007.npy) |
| 3008 | `model.layers.23` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3009 | `model.layers.23` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3010 | `model.layers.23` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3011 | `model.layers.23.input_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10752.0 / 10432.0 / 0.10021158854166666 / 444.5192392129245 | [NPY](tensors/0003011.npy) |
| 3012 | `model.layers.23.input_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.0 / 55.25 / 0.016809183359146117 / 1.7631654520018236 | [NPY](tensors/0003012.npy) |
| 3013 | `model.layers.23.self_attn` | 25 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.0 / 55.25 / 0.016809183359146117 / 1.7631654520018236 | [NPY](tensors/0003013.npy) |
| 3014 | `model.layers.23.self_attn` | 25 | `input.kwargs['attention_mask']` | [1, 1, 1, 330] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003014.npy) |
| 3015 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 329.0 / 329.0 / 329.0 / 0.0 | [NPY](tensors/0003015.npy) |
| 3016 | `model.layers.23.self_attn` | 25 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3017 | `model.layers.23.self_attn` | 25 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3018 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0703125 / 1.34375 / 0.79522705078125 / 0.8430708673085846 | [NPY](tensors/0003018.npy) |
| 3019 | `model.layers.23.self_attn` | 25 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.2890625 / 0.014278113842010498 / 0.6832416349180735 | [NPY](tensors/0003019.npy) |
| 3020 | `model.layers.23.self_attn` | 25 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3021 | `model.layers.23.self_attn.q_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.0 / 55.25 / 0.016809183359146117 / 1.7631654520018236 | [NPY](tensors/0003021.npy) |
| 3022 | `model.layers.23.self_attn.q_proj` | 25 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.6875 / 14.8125 / 0.034882737789303064 / 1.5455965694336034 | [NPY](tensors/0003022.npy) |
| 3023 | `model.layers.23.self_attn.k_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.0 / 55.25 / 0.016809183359146117 / 1.7631654520018236 | [NPY](tensors/0003023.npy) |
| 3024 | `model.layers.23.self_attn.k_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -25.625 / 32.75 / -0.04745668172836304 / 4.516457398918728 | [NPY](tensors/0003024.npy) |
| 3025 | `model.layers.23.self_attn.v_proj` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.0 / 55.25 / 0.016809183359146117 / 1.7631654520018236 | [NPY](tensors/0003025.npy) |
| 3026 | `model.layers.23.self_attn.v_proj` | 25 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.0 / 12.25 / -0.002835474908351898 / 3.946175266568185 | [NPY](tensors/0003026.npy) |
| 3027 | `model.layers.23.self_attn.o_proj` | 25 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.1875 / 7.4375 / 0.08477007399778813 / 1.419936168009203 | [NPY](tensors/0003027.npy) |
| 3028 | `model.layers.23.self_attn.o_proj` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3040.0 / 2960.0 / 1.7266937255859376 / 150.30329451064577 | [NPY](tensors/0003028.npy) |
| 3029 | `model.layers.23.self_attn` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3040.0 / 2960.0 / 1.7266937255859376 / 150.30329451064577 | [NPY](tensors/0003029.npy) |
| 3030 | `model.layers.23.self_attn` | 25 | `output[1]` | [1, 64, 1, 330] | torch.bfloat16 → float32 | 1.2967404927621828e-13 / 0.953125 / 0.0023463682344176074 / 0.014951773915505484 | [NPY](tensors/0003030.npy) |
| 3031 | `model.layers.23.post_attention_layernorm` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9088.0 / 8960.0 / 1.8422322591145834 / 415.063273419798 | [NPY](tensors/0003031.npy) |
| 3032 | `model.layers.23.post_attention_layernorm` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.375 / 7.78125 / -0.01224567625257704 / 1.1048661656945504 | [NPY](tensors/0003032.npy) |
| 3033 | `model.layers.23.mlp` | 25 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -28.375 / 7.78125 / -0.01224567625257704 / 1.1048661656945504 | [NPY](tensors/0003033.npy) |
| 3034 | `model.layers.23.mlp.experts` | 25 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -28.375 / 7.78125 / -0.01224567625257704 / 1.1048661656945504 | [NPY](tensors/0003034.npy) |
| 3035 | `model.layers.23.mlp.experts` | 25 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3036 | `model.layers.23.mlp.experts` | 25 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3037 | `model.layers.23.mlp.experts` | 25 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3038 | `model.layers.23.mlp.experts` | 25 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3520.0 / 3248.0 / -3.628090074327257 / 171.98242954778897 | [NPY](tensors/0003038.npy) |
| 3039 | `model.layers.23.mlp` | 25 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3520.0 / 3248.0 / -3.628090074327257 / 171.98242954778897 | [NPY](tensors/0003039.npy) |
| 3040 | `model.layers.23.mlp` | 25 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.7890625 / 1.171875 / -0.12264823913574219 / 0.6554324357601433 | [NPY](tensors/0003040.npy) |
| 3041 | `model.layers.23` | 25 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5888.0 / 5888.0 / -1.7781358506944445 / 324.4151506470477 | [NPY](tensors/0003041.npy) |
| 3120 | `model.layers.23` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8640.0 / 8832.0 / -2.5742865668402777 / 401.3923526771275 | [NPY](tensors/0003120.npy) |
| 3121 | `model.layers.23` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 331] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003121.npy) |
| 3122 | `model.layers.23` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0003122.npy) |
| 3123 | `model.layers.23` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0003123.npy) |
| 3124 | `model.layers.23` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0003124.npy) |
| 3125 | `model.layers.23` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3126 | `model.layers.23` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3127 | `model.layers.23` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3128 | `model.layers.23.input_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8640.0 / 8832.0 / -2.5742865668402777 / 401.3923526771275 | [NPY](tensors/0003128.npy) |
| 3129 | `model.layers.23.input_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 59.25 / 0.006978164778815375 / 1.7825915357242084 | [NPY](tensors/0003129.npy) |
| 3130 | `model.layers.23.self_attn` | 26 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 59.25 / 0.006978164778815375 / 1.7825915357242084 | [NPY](tensors/0003130.npy) |
| 3131 | `model.layers.23.self_attn` | 26 | `input.kwargs['attention_mask']` | [1, 1, 1, 331] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003131.npy) |
| 3132 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 330.0 / 330.0 / 330.0 / 0.0 | [NPY](tensors/0003132.npy) |
| 3133 | `model.layers.23.self_attn` | 26 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3134 | `model.layers.23.self_attn` | 26 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3135 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.771484375 / 0.8646549670100193 | [NPY](tensors/0003135.npy) |
| 3136 | `model.layers.23.self_attn` | 26 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.171875 / 1.2890625 / 0.02460893988609314 / 0.6832809302317245 | [NPY](tensors/0003136.npy) |
| 3137 | `model.layers.23.self_attn` | 26 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3138 | `model.layers.23.self_attn.q_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 59.25 / 0.006978164778815375 / 1.7825915357242084 | [NPY](tensors/0003138.npy) |
| 3139 | `model.layers.23.self_attn.q_proj` | 26 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.5 / 17.25 / 0.052616925444453955 / 1.6528927927321782 | [NPY](tensors/0003139.npy) |
| 3140 | `model.layers.23.self_attn.k_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 59.25 / 0.006978164778815375 / 1.7825915357242084 | [NPY](tensors/0003140.npy) |
| 3141 | `model.layers.23.self_attn.k_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.25 / 40.5 / -0.05863659828901291 / 5.256063607840107 | [NPY](tensors/0003141.npy) |
| 3142 | `model.layers.23.self_attn.v_proj` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 59.25 / 0.006978164778815375 / 1.7825915357242084 | [NPY](tensors/0003142.npy) |
| 3143 | `model.layers.23.self_attn.v_proj` | 26 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.1875 / 13.4375 / 0.03637838363647461 / 3.8585574150263717 | [NPY](tensors/0003143.npy) |
| 3144 | `model.layers.23.self_attn.o_proj` | 26 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.9375 / 6.875 / 0.05732956691645086 / 1.2436746101009288 | [NPY](tensors/0003144.npy) |
| 3145 | `model.layers.23.self_attn.o_proj` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2992.0 / 2928.0 / 1.8399739795260959 / 137.70110361302142 | [NPY](tensors/0003145.npy) |
| 3146 | `model.layers.23.self_attn` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2992.0 / 2928.0 / 1.8399739795260959 / 137.70110361302142 | [NPY](tensors/0003146.npy) |
| 3147 | `model.layers.23.self_attn` | 26 | `output[1]` | [1, 64, 1, 331] | torch.bfloat16 → float32 | 5.861977570020827e-14 / 0.9140625 / 0.00199664020037055 / 0.013485130237457541 | [NPY](tensors/0003147.npy) |
| 3148 | `model.layers.23.post_attention_layernorm` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7424.0 / 7712.0 / -0.7345709906684028 / 391.2606121375177 | [NPY](tensors/0003148.npy) |
| 3149 | `model.layers.23.post_attention_layernorm` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 10.375 / -0.02345777087741428 / 1.213427904021665 | [NPY](tensors/0003149.npy) |
| 3150 | `model.layers.23.mlp` | 26 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.25 / 10.375 / -0.02345777087741428 / 1.213427904021665 | [NPY](tensors/0003150.npy) |
| 3151 | `model.layers.23.mlp.experts` | 26 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.25 / 10.375 / -0.02345777087741428 / 1.213427904021665 | [NPY](tensors/0003151.npy) |
| 3152 | `model.layers.23.mlp.experts` | 26 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3153 | `model.layers.23.mlp.experts` | 26 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3154 | `model.layers.23.mlp.experts` | 26 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3155 | `model.layers.23.mlp.experts` | 26 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4064.0 / 4016.0 / -0.5928173489040799 / 210.37560495635896 | [NPY](tensors/0003155.npy) |
| 3156 | `model.layers.23.mlp` | 26 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4064.0 / 4016.0 / -0.5928173489040799 / 210.37560495635896 | [NPY](tensors/0003156.npy) |
| 3157 | `model.layers.23.mlp` | 26 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.1875 / 2.21875 / -0.0754241943359375 / 1.1627862769077142 | [NPY](tensors/0003157.npy) |
| 3158 | `model.layers.23` | 26 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3408.0 / 3648.0 / -1.3261338975694446 / 298.96820461688884 | [NPY](tensors/0003158.npy) |
| 3237 | `model.layers.23` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9856.0 / 2.3135267469618057 / 448.754324741109 | [NPY](tensors/0003237.npy) |
| 3238 | `model.layers.23` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 332] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003238.npy) |
| 3239 | `model.layers.23` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0003239.npy) |
| 3240 | `model.layers.23` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0003240.npy) |
| 3241 | `model.layers.23` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0003241.npy) |
| 3242 | `model.layers.23` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3243 | `model.layers.23` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3244 | `model.layers.23` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3245 | `model.layers.23.input_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9856.0 / 2.3135267469618057 / 448.754324741109 | [NPY](tensors/0003245.npy) |
| 3246 | `model.layers.23.input_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 59.0 / 0.020857037438286676 / 1.7717937645323658 | [NPY](tensors/0003246.npy) |
| 3247 | `model.layers.23.self_attn` | 27 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 59.0 / 0.020857037438286676 / 1.7717937645323658 | [NPY](tensors/0003247.npy) |
| 3248 | `model.layers.23.self_attn` | 27 | `input.kwargs['attention_mask']` | [1, 1, 1, 332] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003248.npy) |
| 3249 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 331.0 / 331.0 / 331.0 / 0.0 | [NPY](tensors/0003249.npy) |
| 3250 | `model.layers.23.self_attn` | 27 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3251 | `model.layers.23.self_attn` | 27 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3252 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.03125 / 1.34375 / 0.766754150390625 / 0.8387503353839877 | [NPY](tensors/0003252.npy) |
| 3253 | `model.layers.23.self_attn` | 27 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.023283839225769043 / 0.7189323983289349 | [NPY](tensors/0003253.npy) |
| 3254 | `model.layers.23.self_attn` | 27 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3255 | `model.layers.23.self_attn.q_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 59.0 / 0.020857037438286676 / 1.7717937645323658 | [NPY](tensors/0003255.npy) |
| 3256 | `model.layers.23.self_attn.q_proj` | 27 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.4375 / 17.75 / 0.021233470120932907 / 1.5758970178891973 | [NPY](tensors/0003256.npy) |
| 3257 | `model.layers.23.self_attn.k_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 59.0 / 0.020857037438286676 / 1.7717937645323658 | [NPY](tensors/0003257.npy) |
| 3258 | `model.layers.23.self_attn.k_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -31.375 / 28.875 / 0.07083210349082947 / 4.4017719874474786 | [NPY](tensors/0003258.npy) |
| 3259 | `model.layers.23.self_attn.v_proj` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.25 / 59.0 / 0.020857037438286676 / 1.7717937645323658 | [NPY](tensors/0003259.npy) |
| 3260 | `model.layers.23.self_attn.v_proj` | 27 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -10.9375 / 12.5 / 0.006061013787984848 / 3.3829200689999666 | [NPY](tensors/0003260.npy) |
| 3261 | `model.layers.23.self_attn.o_proj` | 27 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.25 / 6.8125 / 0.04984970670193434 / 1.241196663911368 | [NPY](tensors/0003261.npy) |
| 3262 | `model.layers.23.self_attn.o_proj` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3344.0 / 3424.0 / 3.147354083591037 / 166.6958647937879 | [NPY](tensors/0003262.npy) |
| 3263 | `model.layers.23.self_attn` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3344.0 / 3424.0 / 3.147354083591037 / 166.6958647937879 | [NPY](tensors/0003263.npy) |
| 3264 | `model.layers.23.self_attn` | 27 | `output[1]` | [1, 64, 1, 332] | torch.bfloat16 → float32 | 2.3647750424515834e-14 / 0.8828125 / 0.002087954908011432 / 0.012542978969723926 | [NPY](tensors/0003264.npy) |
| 3265 | `model.layers.23.post_attention_layernorm` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8192.0 / 7808.0 / 5.460498046875 / 421.73865590926476 | [NPY](tensors/0003265.npy) |
| 3266 | `model.layers.23.post_attention_layernorm` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 7.125 / 0.0010243230395846896 / 1.1346669606467517 | [NPY](tensors/0003266.npy) |
| 3267 | `model.layers.23.mlp` | 27 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -29.375 / 7.125 / 0.0010243230395846896 / 1.1346669606467517 | [NPY](tensors/0003267.npy) |
| 3268 | `model.layers.23.mlp.experts` | 27 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -29.375 / 7.125 / 0.0010243230395846896 / 1.1346669606467517 | [NPY](tensors/0003268.npy) |
| 3269 | `model.layers.23.mlp.experts` | 27 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3270 | `model.layers.23.mlp.experts` | 27 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3271 | `model.layers.23.mlp.experts` | 27 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3272 | `model.layers.23.mlp.experts` | 27 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4192.0 / 4080.0 / -2.603729671902127 / 215.40117336890063 | [NPY](tensors/0003272.npy) |
| 3273 | `model.layers.23.mlp` | 27 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4192.0 / 4080.0 / -2.603729671902127 / 215.40117336890063 | [NPY](tensors/0003273.npy) |
| 3274 | `model.layers.23.mlp` | 27 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.15625 / 1.2890625 / 0.04278397560119629 / 0.7223230383082814 | [NPY](tensors/0003274.npy) |
| 3275 | `model.layers.23` | 27 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4160.0 / 3776.0 / 2.861447482638889 / 300.1417423081074 | [NPY](tensors/0003275.npy) |
| 3354 | `model.layers.23` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 10624.0 / -1.0301961263020833 / 464.8480077910817 | [NPY](tensors/0003354.npy) |
| 3355 | `model.layers.23` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 333] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003355.npy) |
| 3356 | `model.layers.23` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0003356.npy) |
| 3357 | `model.layers.23` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0003357.npy) |
| 3358 | `model.layers.23` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0003358.npy) |
| 3359 | `model.layers.23` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3360 | `model.layers.23` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3361 | `model.layers.23` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3362 | `model.layers.23.input_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10496.0 / 10624.0 / -1.0301961263020833 / 464.8480077910817 | [NPY](tensors/0003362.npy) |
| 3363 | `model.layers.23.input_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 61.5 / 0.01299076279004415 / 1.7978532589102783 | [NPY](tensors/0003363.npy) |
| 3364 | `model.layers.23.self_attn` | 28 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 61.5 / 0.01299076279004415 / 1.7978532589102783 | [NPY](tensors/0003364.npy) |
| 3365 | `model.layers.23.self_attn` | 28 | `input.kwargs['attention_mask']` | [1, 1, 1, 333] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003365.npy) |
| 3366 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 332.0 / 332.0 / 332.0 / 0.0 | [NPY](tensors/0003366.npy) |
| 3367 | `model.layers.23.self_attn` | 28 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3368 | `model.layers.23.self_attn` | 28 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3369 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1328125 / 1.34375 / 0.77264404296875 / 0.8502384159090605 | [NPY](tensors/0003369.npy) |
| 3370 | `model.layers.23.self_attn` | 28 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.234375 / 1.3125 / 0.034249186515808105 / 0.6988751213874137 | [NPY](tensors/0003370.npy) |
| 3371 | `model.layers.23.self_attn` | 28 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3372 | `model.layers.23.self_attn.q_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 61.5 / 0.01299076279004415 / 1.7978532589102783 | [NPY](tensors/0003372.npy) |
| 3373 | `model.layers.23.self_attn.q_proj` | 28 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.0 / 15.1875 / 0.03127716205926845 / 1.5586299279761497 | [NPY](tensors/0003373.npy) |
| 3374 | `model.layers.23.self_attn.k_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 61.5 / 0.01299076279004415 / 1.7978532589102783 | [NPY](tensors/0003374.npy) |
| 3375 | `model.layers.23.self_attn.k_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -41.5 / 35.0 / -0.05771560221910477 / 4.5601559350243175 | [NPY](tensors/0003375.npy) |
| 3376 | `model.layers.23.self_attn.v_proj` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.75 / 61.5 / 0.01299076279004415 / 1.7978532589102783 | [NPY](tensors/0003376.npy) |
| 3377 | `model.layers.23.self_attn.v_proj` | 28 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.1875 / 8.875 / -0.13660848140716553 / 2.9323418678995106 | [NPY](tensors/0003377.npy) |
| 3378 | `model.layers.23.self_attn.o_proj` | 28 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.875 / 5.71875 / 0.023047438939101994 / 1.1362663248210587 | [NPY](tensors/0003378.npy) |
| 3379 | `model.layers.23.self_attn.o_proj` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2656.0 / 2576.0 / 2.3729394065009224 / 137.50564553386533 | [NPY](tensors/0003379.npy) |
| 3380 | `model.layers.23.self_attn` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2656.0 / 2576.0 / 2.3729394065009224 / 137.50564553386533 | [NPY](tensors/0003380.npy) |
| 3381 | `model.layers.23.self_attn` | 28 | `output[1]` | [1, 64, 1, 333] | torch.bfloat16 → float32 | 4.529709940470639e-14 / 0.90625 / 0.0019663632098749664 / 0.01196710983381065 | [NPY](tensors/0003381.npy) |
| 3382 | `model.layers.23.post_attention_layernorm` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8576.0 / 8576.0 / 1.3597113715277778 / 420.9806745474302 | [NPY](tensors/0003382.npy) |
| 3383 | `model.layers.23.post_attention_layernorm` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 5.5625 / -0.02051280869377984 / 1.2574601736886422 | [NPY](tensors/0003383.npy) |
| 3384 | `model.layers.23.mlp` | 28 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 5.5625 / -0.02051280869377984 / 1.2574601736886422 | [NPY](tensors/0003384.npy) |
| 3385 | `model.layers.23.mlp.experts` | 28 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.75 / 5.5625 / -0.02051280869377984 / 1.2574601736886422 | [NPY](tensors/0003385.npy) |
| 3386 | `model.layers.23.mlp.experts` | 28 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3387 | `model.layers.23.mlp.experts` | 28 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3388 | `model.layers.23.mlp.experts` | 28 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3389 | `model.layers.23.mlp.experts` | 28 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4016.0 / 3872.0 / 0.375770992702908 / 203.7910733849145 | [NPY](tensors/0003389.npy) |
| 3390 | `model.layers.23.mlp` | 28 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4016.0 / 3872.0 / 0.375770992702908 / 203.7910733849145 | [NPY](tensors/0003390.npy) |
| 3391 | `model.layers.23.mlp` | 28 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9921875 / 1.359375 / -0.00051116943359375 / 0.7275021853717665 | [NPY](tensors/0003391.npy) |
| 3392 | `model.layers.23` | 28 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4768.0 / 4736.0 / 1.71669921875 / 317.1110591294852 | [NPY](tensors/0003392.npy) |
| 3471 | `model.layers.23` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9280.0 / 9600.0 / -0.8732530381944444 / 425.8468583174679 | [NPY](tensors/0003471.npy) |
| 3472 | `model.layers.23` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 334] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003472.npy) |
| 3473 | `model.layers.23` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0003473.npy) |
| 3474 | `model.layers.23` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0003474.npy) |
| 3475 | `model.layers.23` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0003475.npy) |
| 3476 | `model.layers.23` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3477 | `model.layers.23` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3478 | `model.layers.23` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3479 | `model.layers.23.input_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9280.0 / 9600.0 / -0.8732530381944444 / 425.8468583174679 | [NPY](tensors/0003479.npy) |
| 3480 | `model.layers.23.input_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 60.5 / 0.010129176245795356 / 1.7879455100599153 | [NPY](tensors/0003480.npy) |
| 3481 | `model.layers.23.self_attn` | 29 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 60.5 / 0.010129176245795356 / 1.7879455100599153 | [NPY](tensors/0003481.npy) |
| 3482 | `model.layers.23.self_attn` | 29 | `input.kwargs['attention_mask']` | [1, 1, 1, 334] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003482.npy) |
| 3483 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 333.0 / 333.0 / 333.0 / 0.0 | [NPY](tensors/0003483.npy) |
| 3484 | `model.layers.23.self_attn` | 29 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3485 | `model.layers.23.self_attn` | 29 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3486 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.7655029296875 / 0.8822427362627807 | [NPY](tensors/0003486.npy) |
| 3487 | `model.layers.23.self_attn` | 29 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.3359375 / 0.0599483847618103 / 0.6642548384372724 | [NPY](tensors/0003487.npy) |
| 3488 | `model.layers.23.self_attn` | 29 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3489 | `model.layers.23.self_attn.q_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 60.5 / 0.010129176245795356 / 1.7879455100599153 | [NPY](tensors/0003489.npy) |
| 3490 | `model.layers.23.self_attn.q_proj` | 29 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.875 / 14.5625 / 0.05104689626023173 / 1.6228849721814493 | [NPY](tensors/0003490.npy) |
| 3491 | `model.layers.23.self_attn.k_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 60.5 / 0.010129176245795356 / 1.7879455100599153 | [NPY](tensors/0003491.npy) |
| 3492 | `model.layers.23.self_attn.k_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.75 / 29.75 / -0.08464318513870239 / 4.294836545275545 | [NPY](tensors/0003492.npy) |
| 3493 | `model.layers.23.self_attn.v_proj` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.0 / 60.5 / 0.010129176245795356 / 1.7879455100599153 | [NPY](tensors/0003493.npy) |
| 3494 | `model.layers.23.self_attn.v_proj` | 29 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.0 / 8.3125 / 0.06820666790008545 / 2.9559480681823875 | [NPY](tensors/0003494.npy) |
| 3495 | `model.layers.23.self_attn.o_proj` | 29 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.125 / 5.59375 / 0.047861281549558043 / 1.2284366622242848 | [NPY](tensors/0003495.npy) |
| 3496 | `model.layers.23.self_attn.o_proj` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2912.0 / 2864.0 / 2.4850925657484266 / 133.26963301406775 | [NPY](tensors/0003496.npy) |
| 3497 | `model.layers.23.self_attn` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2912.0 / 2864.0 / 2.4850925657484266 / 133.26963301406775 | [NPY](tensors/0003497.npy) |
| 3498 | `model.layers.23.self_attn` | 29 | `output[1]` | [1, 64, 1, 334] | torch.bfloat16 → float32 | 1.84297022087776e-14 / 0.8828125 / 0.001982118729037049 / 0.014453286154479997 | [NPY](tensors/0003498.npy) |
| 3499 | `model.layers.23.post_attention_layernorm` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8032.0 / 8384.0 / 1.6163384331597221 / 412.3872628631049 | [NPY](tensors/0003499.npy) |
| 3500 | `model.layers.23.post_attention_layernorm` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 9.125 / -0.017720208565394083 / 1.2086569253657098 | [NPY](tensors/0003500.npy) |
| 3501 | `model.layers.23.mlp` | 29 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.25 / 9.125 / -0.017720208565394083 / 1.2086569253657098 | [NPY](tensors/0003501.npy) |
| 3502 | `model.layers.23.mlp.experts` | 29 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.25 / 9.125 / -0.017720208565394083 / 1.2086569253657098 | [NPY](tensors/0003502.npy) |
| 3503 | `model.layers.23.mlp.experts` | 29 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3504 | `model.layers.23.mlp.experts` | 29 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3505 | `model.layers.23.mlp.experts` | 29 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3506 | `model.layers.23.mlp.experts` | 29 | `output` | [1, 2880] | torch.bfloat16 → float32 | -7104.0 / 6432.0 / -3.6650537490844726 / 370.79984323666076 | [NPY](tensors/0003506.npy) |
| 3507 | `model.layers.23.mlp` | 29 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7104.0 / 6432.0 / -3.6650537490844726 / 370.79984323666076 | [NPY](tensors/0003507.npy) |
| 3508 | `model.layers.23.mlp` | 29 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.640625 / 2.109375 / -0.07272911071777344 / 0.9510958570523338 | [NPY](tensors/0003508.npy) |
| 3509 | `model.layers.23` | 29 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2576.0 / 1632.0 / -2.0572916666666665 / 327.51856897931555 | [NPY](tensors/0003509.npy) |
| 3588 | `model.layers.23` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9856.0 / -0.5557908799913195 / 446.1099860027951 | [NPY](tensors/0003588.npy) |
| 3589 | `model.layers.23` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 335] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003589.npy) |
| 3590 | `model.layers.23` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0003590.npy) |
| 3591 | `model.layers.23` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0003591.npy) |
| 3592 | `model.layers.23` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0003592.npy) |
| 3593 | `model.layers.23` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3594 | `model.layers.23` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3595 | `model.layers.23` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3596 | `model.layers.23.input_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9856.0 / -0.5557908799913195 / 446.1099860027951 | [NPY](tensors/0003596.npy) |
| 3597 | `model.layers.23.input_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 57.75 / 0.011275036136309306 / 1.7763476317104858 | [NPY](tensors/0003597.npy) |
| 3598 | `model.layers.23.self_attn` | 30 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 57.75 / 0.011275036136309306 / 1.7763476317104858 | [NPY](tensors/0003598.npy) |
| 3599 | `model.layers.23.self_attn` | 30 | `input.kwargs['attention_mask']` | [1, 1, 1, 335] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003599.npy) |
| 3600 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 334.0 / 334.0 / 334.0 / 0.0 | [NPY](tensors/0003600.npy) |
| 3601 | `model.layers.23.self_attn` | 30 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3602 | `model.layers.23.self_attn` | 30 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3603 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0390625 / 1.34375 / 0.7343063354492188 / 0.8714465193226816 | [NPY](tensors/0003603.npy) |
| 3604 | `model.layers.23.self_attn` | 30 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.07659786939620972 / 0.7103761289112627 | [NPY](tensors/0003604.npy) |
| 3605 | `model.layers.23.self_attn` | 30 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3606 | `model.layers.23.self_attn.q_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 57.75 / 0.011275036136309306 / 1.7763476317104858 | [NPY](tensors/0003606.npy) |
| 3607 | `model.layers.23.self_attn.q_proj` | 30 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.75 / 15.0625 / 0.049495318438857794 / 1.592708167795974 | [NPY](tensors/0003607.npy) |
| 3608 | `model.layers.23.self_attn.k_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 57.75 / 0.011275036136309306 / 1.7763476317104858 | [NPY](tensors/0003608.npy) |
| 3609 | `model.layers.23.self_attn.k_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.25 / 26.875 / -0.17802651226520538 / 4.46004857768503 | [NPY](tensors/0003609.npy) |
| 3610 | `model.layers.23.self_attn.v_proj` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -48.5 / 57.75 / 0.011275036136309306 / 1.7763476317104858 | [NPY](tensors/0003610.npy) |
| 3611 | `model.layers.23.self_attn.v_proj` | 30 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -15.125 / 15.5625 / -0.18274542689323425 / 4.97401174724424 | [NPY](tensors/0003611.npy) |
| 3612 | `model.layers.23.self_attn.o_proj` | 30 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.625 / 7.09375 / 0.02443096158094704 / 1.0027274352961737 | [NPY](tensors/0003612.npy) |
| 3613 | `model.layers.23.self_attn.o_proj` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2272.0 / 2576.0 / 1.4068084292941623 / 123.8206929289905 | [NPY](tensors/0003613.npy) |
| 3614 | `model.layers.23.self_attn` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2272.0 / 2576.0 / 1.4068084292941623 / 123.8206929289905 | [NPY](tensors/0003614.npy) |
| 3615 | `model.layers.23.self_attn` | 30 | `output[1]` | [1, 64, 1, 335] | torch.bfloat16 → float32 | 3.4861002973229915e-14 / 0.89453125 / 0.001457803508917228 / 0.01022674663914765 | [NPY](tensors/0003615.npy) |
| 3616 | `model.layers.23.post_attention_layernorm` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8064.0 / 7808.0 / 0.8490939670138888 / 374.3459268500575 | [NPY](tensors/0003616.npy) |
| 3617 | `model.layers.23.post_attention_layernorm` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 12.5625 / -0.018954453534550136 / 1.276560141476729 | [NPY](tensors/0003617.npy) |
| 3618 | `model.layers.23.mlp` | 30 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.5 / 12.5625 / -0.018954453534550136 / 1.276560141476729 | [NPY](tensors/0003618.npy) |
| 3619 | `model.layers.23.mlp.experts` | 30 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -34.5 / 12.5625 / -0.018954453534550136 / 1.276560141476729 | [NPY](tensors/0003619.npy) |
| 3620 | `model.layers.23.mlp.experts` | 30 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3621 | `model.layers.23.mlp.experts` | 30 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3622 | `model.layers.23.mlp.experts` | 30 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3623 | `model.layers.23.mlp.experts` | 30 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6272.0 / 5632.0 / -3.863108147515191 / 276.44387016287726 | [NPY](tensors/0003623.npy) |
| 3624 | `model.layers.23.mlp` | 30 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6272.0 / 5632.0 / -3.863108147515191 / 276.44387016287726 | [NPY](tensors/0003624.npy) |
| 3625 | `model.layers.23.mlp` | 30 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.96875 / 1.71875 / -0.11948585510253906 / 1.0883877404952464 | [NPY](tensors/0003625.npy) |
| 3626 | `model.layers.23` | 30 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2432.0 / 2016.0 / -3.0106825086805555 / 258.1203104282865 | [NPY](tensors/0003626.npy) |
| 3705 | `model.layers.23` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8960.0 / 8256.0 / -1.9814765082465278 / 420.97060403510244 | [NPY](tensors/0003705.npy) |
| 3706 | `model.layers.23` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 336] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003706.npy) |
| 3707 | `model.layers.23` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0003707.npy) |
| 3708 | `model.layers.23` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0003708.npy) |
| 3709 | `model.layers.23` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0003709.npy) |
| 3710 | `model.layers.23` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3711 | `model.layers.23` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3712 | `model.layers.23` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3713 | `model.layers.23.input_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8960.0 / 8256.0 / -1.9814765082465278 / 420.97060403510244 | [NPY](tensors/0003713.npy) |
| 3714 | `model.layers.23.input_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 52.0 / 0.00840551323360867 / 1.7418803364556745 | [NPY](tensors/0003714.npy) |
| 3715 | `model.layers.23.self_attn` | 31 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 52.0 / 0.00840551323360867 / 1.7418803364556745 | [NPY](tensors/0003715.npy) |
| 3716 | `model.layers.23.self_attn` | 31 | `input.kwargs['attention_mask']` | [1, 1, 1, 336] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003716.npy) |
| 3717 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 335.0 / 335.0 / 335.0 / 0.0 | [NPY](tensors/0003717.npy) |
| 3718 | `model.layers.23.self_attn` | 31 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3719 | `model.layers.23.self_attn` | 31 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3720 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2578125 / 1.34375 / 0.6957244873046875 / 0.8958272508521689 | [NPY](tensors/0003720.npy) |
| 3721 | `model.layers.23.self_attn` | 31 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3203125 / 0.062175244092941284 / 0.7207292391344657 | [NPY](tensors/0003721.npy) |
| 3722 | `model.layers.23.self_attn` | 31 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3723 | `model.layers.23.self_attn.q_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 52.0 / 0.00840551323360867 / 1.7418803364556745 | [NPY](tensors/0003723.npy) |
| 3724 | `model.layers.23.self_attn.q_proj` | 31 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.125 / 17.25 / 0.05664812368922867 / 1.9113770031771955 | [NPY](tensors/0003724.npy) |
| 3725 | `model.layers.23.self_attn.k_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 52.0 / 0.00840551323360867 / 1.7418803364556745 | [NPY](tensors/0003725.npy) |
| 3726 | `model.layers.23.self_attn.k_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.75 / 31.25 / -0.06026230752468109 / 4.862342978315286 | [NPY](tensors/0003726.npy) |
| 3727 | `model.layers.23.self_attn.v_proj` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 52.0 / 0.00840551323360867 / 1.7418803364556745 | [NPY](tensors/0003727.npy) |
| 3728 | `model.layers.23.self_attn.v_proj` | 31 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -14.125 / 15.0625 / 0.2100091576576233 / 4.180000534760662 | [NPY](tensors/0003728.npy) |
| 3729 | `model.layers.23.self_attn.o_proj` | 31 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.875 / 8.8125 / 0.03394798131193966 / 1.328125852956079 | [NPY](tensors/0003729.npy) |
| 3730 | `model.layers.23.self_attn.o_proj` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2976.0 / 2928.0 / 0.5467019822862413 / 144.8356274387192 | [NPY](tensors/0003730.npy) |
| 3731 | `model.layers.23.self_attn` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2976.0 / 2928.0 / 0.5467019822862413 / 144.8356274387192 | [NPY](tensors/0003731.npy) |
| 3732 | `model.layers.23.self_attn` | 31 | `output[1]` | [1, 64, 1, 336] | torch.bfloat16 → float32 | 9.159339953157541e-15 / 0.93359375 / 0.0016722362721780344 / 0.014415066317362368 | [NPY](tensors/0003732.npy) |
| 3733 | `model.layers.23.post_attention_layernorm` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7840.0 / 7232.0 / -1.4479926215277779 / 419.8912740294748 | [NPY](tensors/0003733.npy) |
| 3734 | `model.layers.23.post_attention_layernorm` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 8.5 / -0.033857952223883735 / 1.3874415963025262 | [NPY](tensors/0003734.npy) |
| 3735 | `model.layers.23.mlp` | 31 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 8.5 / -0.033857952223883735 / 1.3874415963025262 | [NPY](tensors/0003735.npy) |
| 3736 | `model.layers.23.mlp.experts` | 31 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -40.25 / 8.5 / -0.033857952223883735 / 1.3874415963025262 | [NPY](tensors/0003736.npy) |
| 3737 | `model.layers.23.mlp.experts` | 31 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3738 | `model.layers.23.mlp.experts` | 31 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3739 | `model.layers.23.mlp.experts` | 31 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3740 | `model.layers.23.mlp.experts` | 31 | `output` | [1, 2880] | torch.bfloat16 → float32 | -6816.0 / 6176.0 / -0.3840984344482422 / 320.06622985011313 | [NPY](tensors/0003740.npy) |
| 3741 | `model.layers.23.mlp` | 31 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6816.0 / 6176.0 / -0.3840984344482422 / 320.06622985011313 | [NPY](tensors/0003741.npy) |
| 3742 | `model.layers.23.mlp` | 31 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.734375 / 1.6640625 / -0.057646989822387695 / 0.9590416523978224 | [NPY](tensors/0003742.npy) |
| 3743 | `model.layers.23` | 31 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -1664.0 / 1392.0 / -1.8438368055555556 / 298.9398686906213 | [NPY](tensors/0003743.npy) |
| 3822 | `model.layers.23` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8320.0 / 7840.0 / -3.32275390625 / 425.82481516219025 | [NPY](tensors/0003822.npy) |
| 3823 | `model.layers.23` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 337] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003823.npy) |
| 3824 | `model.layers.23` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0003824.npy) |
| 3825 | `model.layers.23` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0003825.npy) |
| 3826 | `model.layers.23` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0003826.npy) |
| 3827 | `model.layers.23` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3828 | `model.layers.23` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3829 | `model.layers.23` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3830 | `model.layers.23.input_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8320.0 / 7840.0 / -3.32275390625 / 425.82481516219025 | [NPY](tensors/0003830.npy) |
| 3831 | `model.layers.23.input_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 47.75 / 0.005382308695051405 / 1.6902710589558054 | [NPY](tensors/0003831.npy) |
| 3832 | `model.layers.23.self_attn` | 32 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 47.75 / 0.005382308695051405 / 1.6902710589558054 | [NPY](tensors/0003832.npy) |
| 3833 | `model.layers.23.self_attn` | 32 | `input.kwargs['attention_mask']` | [1, 1, 1, 337] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003833.npy) |
| 3834 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 336.0 / 336.0 / 336.0 / 0.0 | [NPY](tensors/0003834.npy) |
| 3835 | `model.layers.23.self_attn` | 32 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3836 | `model.layers.23.self_attn` | 32 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3837 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.680389404296875 / 0.9561607367289703 | [NPY](tensors/0003837.npy) |
| 3838 | `model.layers.23.self_attn` | 32 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.296875 / 0.021264642477035522 / 0.6563918938951827 | [NPY](tensors/0003838.npy) |
| 3839 | `model.layers.23.self_attn` | 32 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3840 | `model.layers.23.self_attn.q_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 47.75 / 0.005382308695051405 / 1.6902710589558054 | [NPY](tensors/0003840.npy) |
| 3841 | `model.layers.23.self_attn.q_proj` | 32 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.0625 / 14.9375 / 0.02411646069958806 / 1.800694651837208 | [NPY](tensors/0003841.npy) |
| 3842 | `model.layers.23.self_attn.k_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 47.75 / 0.005382308695051405 / 1.6902710589558054 | [NPY](tensors/0003842.npy) |
| 3843 | `model.layers.23.self_attn.k_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.5 / 27.875 / -0.06712093949317932 / 4.652629959223177 | [NPY](tensors/0003843.npy) |
| 3844 | `model.layers.23.self_attn.v_proj` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 47.75 / 0.005382308695051405 / 1.6902710589558054 | [NPY](tensors/0003844.npy) |
| 3845 | `model.layers.23.self_attn.v_proj` | 32 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.25 / 13.875 / 0.048192381858825684 / 4.493375430370707 | [NPY](tensors/0003845.npy) |
| 3846 | `model.layers.23.self_attn.o_proj` | 32 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.3125 / 9.8125 / 0.033163588494062424 / 1.2706199645201803 | [NPY](tensors/0003846.npy) |
| 3847 | `model.layers.23.self_attn.o_proj` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2688.0 / 2608.0 / 0.8793054156833224 / 135.43121714914943 | [NPY](tensors/0003847.npy) |
| 3848 | `model.layers.23.self_attn` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2688.0 / 2608.0 / 0.8793054156833224 / 135.43121714914943 | [NPY](tensors/0003848.npy) |
| 3849 | `model.layers.23.self_attn` | 32 | `output[1]` | [1, 64, 1, 337] | torch.bfloat16 → float32 | 1.1457501614131615e-13 / 0.953125 / 0.0018242285884309054 / 0.014475567362143473 | [NPY](tensors/0003849.npy) |
| 3850 | `model.layers.23.post_attention_layernorm` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6848.0 / 6496.0 / -2.433490668402778 / 410.2398828721684 | [NPY](tensors/0003850.npy) |
| 3851 | `model.layers.23.post_attention_layernorm` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.25 / 10.875 / -0.032386864556206596 / 1.4766804315970108 | [NPY](tensors/0003851.npy) |
| 3852 | `model.layers.23.mlp` | 32 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.25 / 10.875 / -0.032386864556206596 / 1.4766804315970108 | [NPY](tensors/0003852.npy) |
| 3853 | `model.layers.23.mlp.experts` | 32 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.25 / 10.875 / -0.032386864556206596 / 1.4766804315970108 | [NPY](tensors/0003853.npy) |
| 3854 | `model.layers.23.mlp.experts` | 32 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3855 | `model.layers.23.mlp.experts` | 32 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3856 | `model.layers.23.mlp.experts` | 32 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3857 | `model.layers.23.mlp.experts` | 32 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4960.0 / 4672.0 / 0.3985823737250434 / 282.0277498804893 | [NPY](tensors/0003857.npy) |
| 3858 | `model.layers.23.mlp` | 32 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4960.0 / 4672.0 / 0.3985823737250434 / 282.0277498804893 | [NPY](tensors/0003858.npy) |
| 3859 | `model.layers.23.mlp` | 32 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.78125 / 1.5703125 / -0.03476715087890625 / 1.0071045878057663 | [NPY](tensors/0003859.npy) |
| 3860 | `model.layers.23` | 32 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2176.0 / 1776.0 / -2.04873046875 / 355.23496395804693 | [NPY](tensors/0003860.npy) |
| 3939 | `model.layers.23` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9344.0 / 1.213132052951389 / 419.5889248811901 | [NPY](tensors/0003939.npy) |
| 3940 | `model.layers.23` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 338] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003940.npy) |
| 3941 | `model.layers.23` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0003941.npy) |
| 3942 | `model.layers.23` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0003942.npy) |
| 3943 | `model.layers.23` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0003943.npy) |
| 3944 | `model.layers.23` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3945 | `model.layers.23` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3946 | `model.layers.23` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3947 | `model.layers.23.input_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9344.0 / 1.213132052951389 / 419.5889248811901 | [NPY](tensors/0003947.npy) |
| 3948 | `model.layers.23.input_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 59.75 / 0.017893987231784397 / 1.8091818050038588 | [NPY](tensors/0003948.npy) |
| 3949 | `model.layers.23.self_attn` | 33 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 59.75 / 0.017893987231784397 / 1.8091818050038588 | [NPY](tensors/0003949.npy) |
| 3950 | `model.layers.23.self_attn` | 33 | `input.kwargs['attention_mask']` | [1, 1, 1, 338] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0003950.npy) |
| 3951 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 337.0 / 337.0 / 337.0 / 0.0 | [NPY](tensors/0003951.npy) |
| 3952 | `model.layers.23.self_attn` | 33 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 3953 | `model.layers.23.self_attn` | 33 | `input.kwargs['use_cache']` | — | bool | True | — |
| 3954 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3125 / 1.34375 / 0.70196533203125 / 0.9484979675442874 | [NPY](tensors/0003954.npy) |
| 3955 | `model.layers.23.self_attn` | 33 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.016728609800338745 / 0.6458623738489303 | [NPY](tensors/0003955.npy) |
| 3956 | `model.layers.23.self_attn` | 33 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 3957 | `model.layers.23.self_attn.q_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 59.75 / 0.017893987231784397 / 1.8091818050038588 | [NPY](tensors/0003957.npy) |
| 3958 | `model.layers.23.self_attn.q_proj` | 33 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.375 / 15.625 / 0.06189208570867777 / 1.4952792034652802 | [NPY](tensors/0003958.npy) |
| 3959 | `model.layers.23.self_attn.k_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 59.75 / 0.017893987231784397 / 1.8091818050038588 | [NPY](tensors/0003959.npy) |
| 3960 | `model.layers.23.self_attn.k_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.5 / 34.25 / -0.08121149241924286 / 4.430979317983583 | [NPY](tensors/0003960.npy) |
| 3961 | `model.layers.23.self_attn.v_proj` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -51.5 / 59.75 / 0.017893987231784397 / 1.8091818050038588 | [NPY](tensors/0003961.npy) |
| 3962 | `model.layers.23.self_attn.v_proj` | 33 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.375 / 13.1875 / 0.26917576789855957 / 3.8009896276202944 | [NPY](tensors/0003962.npy) |
| 3963 | `model.layers.23.self_attn.o_proj` | 33 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.875 / 7.03125 / 0.029751505004242063 / 1.1308722691129025 | [NPY](tensors/0003963.npy) |
| 3964 | `model.layers.23.self_attn.o_proj` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4000.0 / 4160.0 / 2.9740628136528864 / 177.44063891027923 | [NPY](tensors/0003964.npy) |
| 3965 | `model.layers.23.self_attn` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4000.0 / 4160.0 / 2.9740628136528864 / 177.44063891027923 | [NPY](tensors/0003965.npy) |
| 3966 | `model.layers.23.self_attn` | 33 | `output[1]` | [1, 64, 1, 338] | torch.bfloat16 → float32 | 4.529709940470639e-14 / 0.90625 / 0.001625472363644546 / 0.01127056851197377 | [NPY](tensors/0003966.npy) |
| 3967 | `model.layers.23.post_attention_layernorm` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9280.0 / 8448.0 / 4.173668077256944 / 442.9075977137741 | [NPY](tensors/0003967.npy) |
| 3968 | `model.layers.23.post_attention_layernorm` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.75 / 7.9375 / -0.0045898099740346275 / 1.0580377794569475 | [NPY](tensors/0003968.npy) |
| 3969 | `model.layers.23.mlp` | 33 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -32.75 / 7.9375 / -0.0045898099740346275 / 1.0580377794569475 | [NPY](tensors/0003969.npy) |
| 3970 | `model.layers.23.mlp.experts` | 33 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -32.75 / 7.9375 / -0.0045898099740346275 / 1.0580377794569475 | [NPY](tensors/0003970.npy) |
| 3971 | `model.layers.23.mlp.experts` | 33 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 3972 | `model.layers.23.mlp.experts` | 33 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3973 | `model.layers.23.mlp.experts` | 33 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 3974 | `model.layers.23.mlp.experts` | 33 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4384.0 / 4064.0 / -3.9873895433213975 / 220.3106487400961 | [NPY](tensors/0003974.npy) |
| 3975 | `model.layers.23.mlp` | 33 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4384.0 / 4064.0 / -3.9873895433213975 / 220.3106487400961 | [NPY](tensors/0003975.npy) |
| 3976 | `model.layers.23.mlp` | 33 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.46875 / 1.9296875 / -0.01312255859375 / 0.9480971668422874 | [NPY](tensors/0003976.npy) |
| 3977 | `model.layers.23` | 33 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5216.0 / 4064.0 / 0.20316297743055556 / 298.8485598358324 | [NPY](tensors/0003977.npy) |
| 4056 | `model.layers.23` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7552.0 / 8096.0 / 2.8445638020833335 / 411.3131257011453 | [NPY](tensors/0004056.npy) |
| 4057 | `model.layers.23` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 339] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004057.npy) |
| 4058 | `model.layers.23` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0004058.npy) |
| 4059 | `model.layers.23` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0004059.npy) |
| 4060 | `model.layers.23` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0004060.npy) |
| 4061 | `model.layers.23` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4062 | `model.layers.23` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4063 | `model.layers.23` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4064 | `model.layers.23.input_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7552.0 / 8096.0 / 2.8445638020833335 / 411.3131257011453 | [NPY](tensors/0004064.npy) |
| 4065 | `model.layers.23.input_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 53.0 / 0.021502365006340875 / 1.7122489985080929 | [NPY](tensors/0004065.npy) |
| 4066 | `model.layers.23.self_attn` | 34 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 53.0 / 0.021502365006340875 / 1.7122489985080929 | [NPY](tensors/0004066.npy) |
| 4067 | `model.layers.23.self_attn` | 34 | `input.kwargs['attention_mask']` | [1, 1, 1, 339] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004067.npy) |
| 4068 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 338.0 / 338.0 / 338.0 / 0.0 | [NPY](tensors/0004068.npy) |
| 4069 | `model.layers.23.self_attn` | 34 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4070 | `model.layers.23.self_attn` | 34 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4071 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3046875 / 1.34375 / 0.7426223754882812 / 0.8913750955952611 | [NPY](tensors/0004071.npy) |
| 4072 | `model.layers.23.self_attn` | 34 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / -0.023150116205215454 / 0.6807039853682878 | [NPY](tensors/0004072.npy) |
| 4073 | `model.layers.23.self_attn` | 34 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4074 | `model.layers.23.self_attn.q_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 53.0 / 0.021502365006340875 / 1.7122489985080929 | [NPY](tensors/0004074.npy) |
| 4075 | `model.layers.23.self_attn.q_proj` | 34 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.0625 / 12.5 / 0.046158918004948646 / 1.4669357471009787 | [NPY](tensors/0004075.npy) |
| 4076 | `model.layers.23.self_attn.k_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 53.0 / 0.021502365006340875 / 1.7122489985080929 | [NPY](tensors/0004076.npy) |
| 4077 | `model.layers.23.self_attn.k_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -36.75 / 27.25 / -0.027877584099769592 / 4.339482114110918 | [NPY](tensors/0004077.npy) |
| 4078 | `model.layers.23.self_attn.v_proj` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.75 / 53.0 / 0.021502365006340875 / 1.7122489985080929 | [NPY](tensors/0004078.npy) |
| 4079 | `model.layers.23.self_attn.v_proj` | 34 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.8125 / 11.125 / 0.07515335083007812 / 3.878893096789866 | [NPY](tensors/0004079.npy) |
| 4080 | `model.layers.23.self_attn.o_proj` | 34 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.375 / 8.125 / 0.026685806224122643 / 1.127289380357603 | [NPY](tensors/0004080.npy) |
| 4081 | `model.layers.23.self_attn.o_proj` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2640.0 / 2736.0 / 0.9570561832851834 / 125.61644650172836 | [NPY](tensors/0004081.npy) |
| 4082 | `model.layers.23.self_attn` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2640.0 / 2736.0 / 0.9570561832851834 / 125.61644650172836 | [NPY](tensors/0004082.npy) |
| 4083 | `model.layers.23.self_attn` | 34 | `output[1]` | [1, 64, 1, 339] | torch.bfloat16 → float32 | 1.3073986337985843e-12 / 0.7890625 / 0.0012175079525015044 / 0.01088008766617093 | [NPY](tensors/0004083.npy) |
| 4084 | `model.layers.23.post_attention_layernorm` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6272.0 / 6752.0 / 3.810080295138889 / 395.339309200232 | [NPY](tensors/0004084.npy) |
| 4085 | `model.layers.23.post_attention_layernorm` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 9.4375 / -0.004902604553434584 / 1.5025271574139836 | [NPY](tensors/0004085.npy) |
| 4086 | `model.layers.23.mlp` | 34 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.5 / 9.4375 / -0.004902604553434584 / 1.5025271574139836 | [NPY](tensors/0004086.npy) |
| 4087 | `model.layers.23.mlp.experts` | 34 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -45.5 / 9.4375 / -0.004902604553434584 / 1.5025271574139836 | [NPY](tensors/0004087.npy) |
| 4088 | `model.layers.23.mlp.experts` | 34 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4089 | `model.layers.23.mlp.experts` | 34 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4090 | `model.layers.23.mlp.experts` | 34 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4091 | `model.layers.23.mlp.experts` | 34 | `output` | [1, 2880] | torch.bfloat16 → float32 | -3744.0 / 3280.0 / -1.0353474934895834 / 209.82595189824207 | [NPY](tensors/0004091.npy) |
| 4092 | `model.layers.23.mlp` | 34 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3744.0 / 3280.0 / -1.0353474934895834 / 209.82595189824207 | [NPY](tensors/0004092.npy) |
| 4093 | `model.layers.23.mlp` | 34 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.34375 / 2.59375 / 0.057708740234375 / 1.4066199210178503 | [NPY](tensors/0004093.npy) |
| 4094 | `model.layers.23` | 34 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3648.0 / 3216.0 / 2.768679470486111 / 345.4610685824866 | [NPY](tensors/0004094.npy) |
| 4173 | `model.layers.23` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6624.0 / 7136.0 / 0.514990234375 / 383.5871743873096 | [NPY](tensors/0004173.npy) |
| 4174 | `model.layers.23` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 340] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004174.npy) |
| 4175 | `model.layers.23` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0004175.npy) |
| 4176 | `model.layers.23` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0004176.npy) |
| 4177 | `model.layers.23` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0004177.npy) |
| 4178 | `model.layers.23` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4179 | `model.layers.23` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4180 | `model.layers.23` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4181 | `model.layers.23.input_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6624.0 / 7136.0 / 0.514990234375 / 383.5871743873096 | [NPY](tensors/0004181.npy) |
| 4182 | `model.layers.23.input_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 50.0 / 0.014159986707899306 / 1.6888589206049043 | [NPY](tensors/0004182.npy) |
| 4183 | `model.layers.23.self_attn` | 35 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 50.0 / 0.014159986707899306 / 1.6888589206049043 | [NPY](tensors/0004183.npy) |
| 4184 | `model.layers.23.self_attn` | 35 | `input.kwargs['attention_mask']` | [1, 1, 1, 340] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004184.npy) |
| 4185 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 339.0 / 339.0 / 339.0 / 0.0 | [NPY](tensors/0004185.npy) |
| 4186 | `model.layers.23.self_attn` | 35 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4187 | `model.layers.23.self_attn` | 35 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4188 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.0 / 1.34375 / 0.766754150390625 / 0.8524599546585812 | [NPY](tensors/0004188.npy) |
| 4189 | `model.layers.23.self_attn` | 35 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.296875 / 0.003652721643447876 / 0.7034483912008976 | [NPY](tensors/0004189.npy) |
| 4190 | `model.layers.23.self_attn` | 35 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4191 | `model.layers.23.self_attn.q_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 50.0 / 0.014159986707899306 / 1.6888589206049043 | [NPY](tensors/0004191.npy) |
| 4192 | `model.layers.23.self_attn.q_proj` | 35 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.4375 / 13.3125 / 0.02263543661683798 / 1.6420127735130654 | [NPY](tensors/0004192.npy) |
| 4193 | `model.layers.23.self_attn.k_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 50.0 / 0.014159986707899306 / 1.6888589206049043 | [NPY](tensors/0004193.npy) |
| 4194 | `model.layers.23.self_attn.k_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.5 / 24.0 / -0.12458701431751251 / 4.334865351340687 | [NPY](tensors/0004194.npy) |
| 4195 | `model.layers.23.self_attn.v_proj` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.5 / 50.0 / 0.014159986707899306 / 1.6888589206049043 | [NPY](tensors/0004195.npy) |
| 4196 | `model.layers.23.self_attn.v_proj` | 35 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -11.625 / 12.25 / 0.24589774012565613 / 3.9431777463039057 | [NPY](tensors/0004196.npy) |
| 4197 | `model.layers.23.self_attn.o_proj` | 35 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.625 / 7.625 / 0.00047102279495447874 / 1.1682208684829318 | [NPY](tensors/0004197.npy) |
| 4198 | `model.layers.23.self_attn.o_proj` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2800.0 / 2976.0 / 2.5134774102105033 / 130.204498633617 | [NPY](tensors/0004198.npy) |
| 4199 | `model.layers.23.self_attn` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2800.0 / 2976.0 / 2.5134774102105033 / 130.204498633617 | [NPY](tensors/0004199.npy) |
| 4200 | `model.layers.23.self_attn` | 35 | `output[1]` | [1, 64, 1, 340] | torch.bfloat16 → float32 | 4.8183679268731794e-14 / 0.8515625 / 0.0009470928448653444 / 0.011370273232592718 | [NPY](tensors/0004200.npy) |
| 4201 | `model.layers.23.post_attention_layernorm` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6208.0 / 6688.0 / 3.0270887586805557 / 391.2238115577901 | [NPY](tensors/0004201.npy) |
| 4202 | `model.layers.23.post_attention_layernorm` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 10.3125 / -0.014246283637152777 / 1.5922071764257946 | [NPY](tensors/0004202.npy) |
| 4203 | `model.layers.23.mlp` | 35 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -50.25 / 10.3125 / -0.014246283637152777 / 1.5922071764257946 | [NPY](tensors/0004203.npy) |
| 4204 | `model.layers.23.mlp.experts` | 35 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -50.25 / 10.3125 / -0.014246283637152777 / 1.5922071764257946 | [NPY](tensors/0004204.npy) |
| 4205 | `model.layers.23.mlp.experts` | 35 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4206 | `model.layers.23.mlp.experts` | 35 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4207 | `model.layers.23.mlp.experts` | 35 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4208 | `model.layers.23.mlp.experts` | 35 | `output` | [1, 2880] | torch.bfloat16 → float32 | -2848.0 / 2784.0 / -0.10466588338216146 / 219.17131168950507 | [NPY](tensors/0004208.npy) |
| 4209 | `model.layers.23.mlp` | 35 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2848.0 / 2784.0 / -0.10466588338216146 / 219.17131168950507 | [NPY](tensors/0004209.npy) |
| 4210 | `model.layers.23.mlp` | 35 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.546875 / 2.25 / 0.075927734375 / 1.322691427665452 | [NPY](tensors/0004210.npy) |
| 4211 | `model.layers.23` | 35 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -7392.0 / 7520.0 / 2.9194227430555557 / 488.1424534427046 | [NPY](tensors/0004211.npy) |
| 4290 | `model.layers.23` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6976.0 / 7936.0 / -1.9787882486979167 / 373.89404570770574 | [NPY](tensors/0004290.npy) |
| 4291 | `model.layers.23` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 341] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004291.npy) |
| 4292 | `model.layers.23` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.34375 / 0.7532014846801758 / 0.8246045706539666 | [NPY](tensors/0004292.npy) |
| 4293 | `model.layers.23` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.03213447332382202 / 0.7489573739100013 | [NPY](tensors/0004293.npy) |
| 4294 | `model.layers.23` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 340.0 / 340.0 / 340.0 / 0.0 | [NPY](tensors/0004294.npy) |
| 4295 | `model.layers.23` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4296 | `model.layers.23` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4297 | `model.layers.23` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4298 | `model.layers.23.input_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6976.0 / 7936.0 / -1.9787882486979167 / 373.89404570770574 | [NPY](tensors/0004298.npy) |
| 4299 | `model.layers.23.input_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 57.0 / 0.009517020649380155 / 1.755481861908399 | [NPY](tensors/0004299.npy) |
| 4300 | `model.layers.23.self_attn` | 36 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 57.0 / 0.009517020649380155 / 1.755481861908399 | [NPY](tensors/0004300.npy) |
| 4301 | `model.layers.23.self_attn` | 36 | `input.kwargs['attention_mask']` | [1, 1, 1, 341] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004301.npy) |
| 4302 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 340.0 / 340.0 / 340.0 / 0.0 | [NPY](tensors/0004302.npy) |
| 4303 | `model.layers.23.self_attn` | 36 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4304 | `model.layers.23.self_attn` | 36 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4305 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.1171875 / 1.34375 / 0.7532014846801758 / 0.8246045706539666 | [NPY](tensors/0004305.npy) |
| 4306 | `model.layers.23.self_attn` | 36 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.03213447332382202 / 0.7489573739100013 | [NPY](tensors/0004306.npy) |
| 4307 | `model.layers.23.self_attn` | 36 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4308 | `model.layers.23.self_attn.q_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 57.0 / 0.009517020649380155 / 1.755481861908399 | [NPY](tensors/0004308.npy) |
| 4309 | `model.layers.23.self_attn.q_proj` | 36 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.1875 / 17.625 / 0.047407036647200584 / 1.7334273609759927 | [NPY](tensors/0004309.npy) |
| 4310 | `model.layers.23.self_attn.k_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 57.0 / 0.009517020649380155 / 1.755481861908399 | [NPY](tensors/0004310.npy) |
| 4311 | `model.layers.23.self_attn.k_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -30.25 / 29.875 / -0.12505987286567688 / 4.739432827765539 | [NPY](tensors/0004311.npy) |
| 4312 | `model.layers.23.self_attn.v_proj` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -39.25 / 57.0 / 0.009517020649380155 / 1.755481861908399 | [NPY](tensors/0004312.npy) |
| 4313 | `model.layers.23.self_attn.v_proj` | 36 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -17.875 / 9.5625 / 0.10239005088806152 / 3.4221306195412393 | [NPY](tensors/0004313.npy) |
| 4314 | `model.layers.23.self_attn.o_proj` | 36 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.6875 / 6.6875 / 0.009845754830166698 / 1.1961886212284178 | [NPY](tensors/0004314.npy) |
| 4315 | `model.layers.23.self_attn.o_proj` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2800.0 / 2848.0 / 1.7234963523017035 / 129.8586058980303 | [NPY](tensors/0004315.npy) |
| 4316 | `model.layers.23.self_attn` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2800.0 / 2848.0 / 1.7234963523017035 / 129.8586058980303 | [NPY](tensors/0004316.npy) |
| 4317 | `model.layers.23.self_attn` | 36 | `output[1]` | [1, 64, 1, 341] | torch.bfloat16 → float32 | 4.163336342344337e-15 / 0.89453125 / 0.0011503237857870025 / 0.01401517570100951 | [NPY](tensors/0004317.npy) |
| 4318 | `model.layers.23.post_attention_layernorm` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6240.0 / 7264.0 / -0.2503689236111111 / 377.108137583426 | [NPY](tensors/0004318.npy) |
| 4319 | `model.layers.23.post_attention_layernorm` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 11.8125 / -0.017453694343566896 / 1.4085425112303585 | [NPY](tensors/0004319.npy) |
| 4320 | `model.layers.23.mlp` | 36 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 11.8125 / -0.017453694343566896 / 1.4085425112303585 | [NPY](tensors/0004320.npy) |
| 4321 | `model.layers.23.mlp.experts` | 36 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -41.75 / 11.8125 / -0.017453694343566896 / 1.4085425112303585 | [NPY](tensors/0004321.npy) |
| 4322 | `model.layers.23.mlp.experts` | 36 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4323 | `model.layers.23.mlp.experts` | 36 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4324 | `model.layers.23.mlp.experts` | 36 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4325 | `model.layers.23.mlp.experts` | 36 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4576.0 / 4608.0 / -0.11921454535590278 / 278.209974995728 | [NPY](tensors/0004325.npy) |
| 4326 | `model.layers.23.mlp` | 36 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4576.0 / 4608.0 / -0.11921454535590278 / 278.209974995728 | [NPY](tensors/0004326.npy) |
| 4327 | `model.layers.23.mlp` | 36 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.21875 / 2.8125 / 0.13541936874389648 / 1.737738188434206 | [NPY](tensors/0004327.npy) |
| 4328 | `model.layers.23` | 36 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2928.0 / 3136.0 / -0.36532118055555557 / 310.8164841167237 | [NPY](tensors/0004328.npy) |
| 4407 | `model.layers.23` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6752.0 / 6784.0 / -1.7124837239583333 / 379.94376509577523 | [NPY](tensors/0004407.npy) |
| 4408 | `model.layers.23` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 342] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004408.npy) |
| 4409 | `model.layers.23` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.7198410034179688 / 0.8503804730267482 | [NPY](tensors/0004409.npy) |
| 4410 | `model.layers.23` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.027828902006149292 / 0.7525043584225227 | [NPY](tensors/0004410.npy) |
| 4411 | `model.layers.23` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 341.0 / 341.0 / 341.0 / 0.0 | [NPY](tensors/0004411.npy) |
| 4412 | `model.layers.23` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4413 | `model.layers.23` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4414 | `model.layers.23` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4415 | `model.layers.23.input_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6752.0 / 6784.0 / -1.7124837239583333 / 379.94376509577523 | [NPY](tensors/0004415.npy) |
| 4416 | `model.layers.23.input_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 47.25 / 0.007643882433573405 / 1.679093716857868 | [NPY](tensors/0004416.npy) |
| 4417 | `model.layers.23.self_attn` | 37 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 47.25 / 0.007643882433573405 / 1.679093716857868 | [NPY](tensors/0004417.npy) |
| 4418 | `model.layers.23.self_attn` | 37 | `input.kwargs['attention_mask']` | [1, 1, 1, 342] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004418.npy) |
| 4419 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 341.0 / 341.0 / 341.0 / 0.0 | [NPY](tensors/0004419.npy) |
| 4420 | `model.layers.23.self_attn` | 37 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4421 | `model.layers.23.self_attn` | 37 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4422 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.21875 / 1.34375 / 0.7198410034179688 / 0.8503804730267482 | [NPY](tensors/0004422.npy) |
| 4423 | `model.layers.23.self_attn` | 37 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.027828902006149292 / 0.7525043584225227 | [NPY](tensors/0004423.npy) |
| 4424 | `model.layers.23.self_attn` | 37 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4425 | `model.layers.23.self_attn.q_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 47.25 / 0.007643882433573405 / 1.679093716857868 | [NPY](tensors/0004425.npy) |
| 4426 | `model.layers.23.self_attn.q_proj` | 37 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.25 / 17.875 / 0.03151706326752901 / 1.6814787184507443 | [NPY](tensors/0004426.npy) |
| 4427 | `model.layers.23.self_attn.k_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 47.25 / 0.007643882433573405 / 1.679093716857868 | [NPY](tensors/0004427.npy) |
| 4428 | `model.layers.23.self_attn.k_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -28.375 / 36.5 / -0.21140500903129578 / 4.72104123639921 | [NPY](tensors/0004428.npy) |
| 4429 | `model.layers.23.self_attn.v_proj` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.5 / 47.25 / 0.007643882433573405 / 1.679093716857868 | [NPY](tensors/0004429.npy) |
| 4430 | `model.layers.23.self_attn.v_proj` | 37 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -16.125 / 19.625 / 0.3148972988128662 / 4.637043240748526 | [NPY](tensors/0004430.npy) |
| 4431 | `model.layers.23.self_attn.o_proj` | 37 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.0625 / 5.6875 / -0.012061609217198566 / 1.2697308652509374 | [NPY](tensors/0004431.npy) |
| 4432 | `model.layers.23.self_attn.o_proj` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3280.0 / 3264.0 / 3.0905215793185765 / 139.6795094107875 | [NPY](tensors/0004432.npy) |
| 4433 | `model.layers.23.self_attn` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3280.0 / 3264.0 / 3.0905215793185765 / 139.6795094107875 | [NPY](tensors/0004433.npy) |
| 4434 | `model.layers.23.self_attn` | 37 | `output[1]` | [1, 64, 1, 342] | torch.bfloat16 → float32 | 1.0269562977782698e-15 / 0.8671875 / 0.0011381372197562247 / 0.01218589949144802 | [NPY](tensors/0004434.npy) |
| 4435 | `model.layers.23.post_attention_layernorm` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6592.0 / 6560.0 / 1.3730251736111112 / 397.04669263881675 | [NPY](tensors/0004435.npy) |
| 4436 | `model.layers.23.post_attention_layernorm` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 11.875 / -0.01749366521835327 / 1.4859297984088322 | [NPY](tensors/0004436.npy) |
| 4437 | `model.layers.23.mlp` | 37 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -45.0 / 11.875 / -0.01749366521835327 / 1.4859297984088322 | [NPY](tensors/0004437.npy) |
| 4438 | `model.layers.23.mlp.experts` | 37 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -45.0 / 11.875 / -0.01749366521835327 / 1.4859297984088322 | [NPY](tensors/0004438.npy) |
| 4439 | `model.layers.23.mlp.experts` | 37 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4440 | `model.layers.23.mlp.experts` | 37 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4441 | `model.layers.23.mlp.experts` | 37 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4442 | `model.layers.23.mlp.experts` | 37 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4480.0 / 4544.0 / -1.9874467637803819 / 240.46309929496175 | [NPY](tensors/0004442.npy) |
| 4443 | `model.layers.23.mlp` | 37 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4480.0 / 4544.0 / -1.9874467637803819 / 240.46309929496175 | [NPY](tensors/0004443.npy) |
| 4444 | `model.layers.23.mlp` | 37 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.96875 / 2.5 / 0.100433349609375 / 1.5289000386656257 | [NPY](tensors/0004444.npy) |
| 4445 | `model.layers.23` | 37 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2208.0 / 2112.0 / -0.6042426215277777 / 309.33445491056693 | [NPY](tensors/0004445.npy) |
| 4524 | `model.layers.23` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5760.0 / 6368.0 / 3.202387152777778 / 355.5270281081571 | [NPY](tensors/0004524.npy) |
| 4525 | `model.layers.23` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 343] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004525.npy) |
| 4526 | `model.layers.23` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.70660400390625 / 0.91681783844784 | [NPY](tensors/0004526.npy) |
| 4527 | `model.layers.23` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / -0.014852643013000488 / 0.6845543139796254 | [NPY](tensors/0004527.npy) |
| 4528 | `model.layers.23` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 342.0 / 342.0 / 342.0 / 0.0 | [NPY](tensors/0004528.npy) |
| 4529 | `model.layers.23` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4530 | `model.layers.23` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4531 | `model.layers.23` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4532 | `model.layers.23.input_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5760.0 / 6368.0 / 3.202387152777778 / 355.5270281081571 | [NPY](tensors/0004532.npy) |
| 4533 | `model.layers.23.input_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 48.25 / 0.024221640162997774 / 1.6882969418829707 | [NPY](tensors/0004533.npy) |
| 4534 | `model.layers.23.self_attn` | 38 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 48.25 / 0.024221640162997774 / 1.6882969418829707 | [NPY](tensors/0004534.npy) |
| 4535 | `model.layers.23.self_attn` | 38 | `input.kwargs['attention_mask']` | [1, 1, 1, 343] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004535.npy) |
| 4536 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 342.0 / 342.0 / 342.0 / 0.0 | [NPY](tensors/0004536.npy) |
| 4537 | `model.layers.23.self_attn` | 38 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4538 | `model.layers.23.self_attn` | 38 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4539 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.70660400390625 / 0.91681783844784 | [NPY](tensors/0004539.npy) |
| 4540 | `model.layers.23.self_attn` | 38 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / -0.014852643013000488 / 0.6845543139796254 | [NPY](tensors/0004540.npy) |
| 4541 | `model.layers.23.self_attn` | 38 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4542 | `model.layers.23.self_attn.q_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 48.25 / 0.024221640162997774 / 1.6882969418829707 | [NPY](tensors/0004542.npy) |
| 4543 | `model.layers.23.self_attn.q_proj` | 38 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -14.0625 / 15.5625 / 0.05271700274897739 / 1.7994148978233027 | [NPY](tensors/0004543.npy) |
| 4544 | `model.layers.23.self_attn.k_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 48.25 / 0.024221640162997774 / 1.6882969418829707 | [NPY](tensors/0004544.npy) |
| 4545 | `model.layers.23.self_attn.k_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -38.0 / 43.75 / -0.09142396599054337 / 5.095803159124377 | [NPY](tensors/0004545.npy) |
| 4546 | `model.layers.23.self_attn.v_proj` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -34.25 / 48.25 / 0.024221640162997774 / 1.6882969418829707 | [NPY](tensors/0004546.npy) |
| 4547 | `model.layers.23.self_attn.v_proj` | 38 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -24.125 / 11.5625 / 0.21382222697138786 / 4.337262852357165 | [NPY](tensors/0004547.npy) |
| 4548 | `model.layers.23.self_attn.o_proj` | 38 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -19.375 / 9.4375 / -0.004503595002461225 / 1.3039733779847658 | [NPY](tensors/0004548.npy) |
| 4549 | `model.layers.23.self_attn.o_proj` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3760.0 / 3760.0 / 0.5610033671061198 / 169.32320742046673 | [NPY](tensors/0004549.npy) |
| 4550 | `model.layers.23.self_attn` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3760.0 / 3760.0 / 0.5610033671061198 / 169.32320742046673 | [NPY](tensors/0004550.npy) |
| 4551 | `model.layers.23.self_attn` | 38 | `output[1]` | [1, 64, 1, 343] | torch.bfloat16 → float32 | 3.8191672047105385e-14 / 0.86328125 / 0.0009750596871788491 / 0.013598880797625614 | [NPY](tensors/0004551.npy) |
| 4552 | `model.layers.23.post_attention_layernorm` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5920.0 / 6528.0 / 3.732063802083333 / 405.74537839588794 | [NPY](tensors/0004552.npy) |
| 4553 | `model.layers.23.post_attention_layernorm` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 11.3125 / -0.006050017144944932 / 1.4548726235680005 | [NPY](tensors/0004553.npy) |
| 4554 | `model.layers.23.mlp` | 38 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.75 / 11.3125 / -0.006050017144944932 / 1.4548726235680005 | [NPY](tensors/0004554.npy) |
| 4555 | `model.layers.23.mlp.experts` | 38 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -41.75 / 11.3125 / -0.006050017144944932 / 1.4548726235680005 | [NPY](tensors/0004555.npy) |
| 4556 | `model.layers.23.mlp.experts` | 38 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4557 | `model.layers.23.mlp.experts` | 38 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4558 | `model.layers.23.mlp.experts` | 38 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4559 | `model.layers.23.mlp.experts` | 38 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5920.0 / 5344.0 / -4.706051974826389 / 323.08596299381674 | [NPY](tensors/0004559.npy) |
| 4560 | `model.layers.23.mlp` | 38 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5920.0 / 5344.0 / -4.706051974826389 / 323.08596299381674 | [NPY](tensors/0004560.npy) |
| 4561 | `model.layers.23.mlp` | 38 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.15625 / 2.640625 / 0.12883758544921875 / 1.6665258255087638 | [NPY](tensors/0004561.npy) |
| 4562 | `model.layers.23` | 38 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3056.0 / 1848.0 / -0.9780436197916667 / 331.86526531023765 | [NPY](tensors/0004562.npy) |
| 4641 | `model.layers.23` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6240.0 / 6464.0 / 2.6108723958333333 / 356.35524082451104 | [NPY](tensors/0004641.npy) |
| 4642 | `model.layers.23` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 344] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004642.npy) |
| 4643 | `model.layers.23` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.740966796875 / 0.9022817549113021 | [NPY](tensors/0004643.npy) |
| 4644 | `model.layers.23` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3046875 / -0.06294980645179749 / 0.6646640154085409 | [NPY](tensors/0004644.npy) |
| 4645 | `model.layers.23` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 343.0 / 343.0 / 343.0 / 0.0 | [NPY](tensors/0004645.npy) |
| 4646 | `model.layers.23` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4647 | `model.layers.23` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4648 | `model.layers.23` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4649 | `model.layers.23.input_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -6240.0 / 6464.0 / 2.6108723958333333 / 356.35524082451104 | [NPY](tensors/0004649.npy) |
| 4650 | `model.layers.23.input_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 47.5 / 0.0246264828575982 / 1.680128258430527 | [NPY](tensors/0004650.npy) |
| 4651 | `model.layers.23.self_attn` | 39 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 47.5 / 0.0246264828575982 / 1.680128258430527 | [NPY](tensors/0004651.npy) |
| 4652 | `model.layers.23.self_attn` | 39 | `input.kwargs['attention_mask']` | [1, 1, 1, 344] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004652.npy) |
| 4653 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 343.0 / 343.0 / 343.0 / 0.0 | [NPY](tensors/0004653.npy) |
| 4654 | `model.layers.23.self_attn` | 39 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4655 | `model.layers.23.self_attn` | 39 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4656 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.740966796875 / 0.9022817549113021 | [NPY](tensors/0004656.npy) |
| 4657 | `model.layers.23.self_attn` | 39 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.3046875 / -0.06294980645179749 / 0.6646640154085409 | [NPY](tensors/0004657.npy) |
| 4658 | `model.layers.23.self_attn` | 39 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4659 | `model.layers.23.self_attn.q_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 47.5 / 0.0246264828575982 / 1.680128258430527 | [NPY](tensors/0004659.npy) |
| 4660 | `model.layers.23.self_attn.q_proj` | 39 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.875 / 18.5 / 0.05666336207650602 / 1.874913532509156 | [NPY](tensors/0004660.npy) |
| 4661 | `model.layers.23.self_attn.k_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 47.5 / 0.0246264828575982 / 1.680128258430527 | [NPY](tensors/0004661.npy) |
| 4662 | `model.layers.23.self_attn.k_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -40.0 / 45.25 / 0.009071636945009232 / 4.941743669458801 | [NPY](tensors/0004662.npy) |
| 4663 | `model.layers.23.self_attn.v_proj` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.0 / 47.5 / 0.0246264828575982 / 1.680128258430527 | [NPY](tensors/0004663.npy) |
| 4664 | `model.layers.23.self_attn.v_proj` | 39 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.125 / 14.625 / -0.07131356559693813 / 4.483112406602933 | [NPY](tensors/0004664.npy) |
| 4665 | `model.layers.23.self_attn.o_proj` | 39 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -19.625 / 11.5625 / -0.033774276584153995 / 1.464333278761169 | [NPY](tensors/0004665.npy) |
| 4666 | `model.layers.23.self_attn.o_proj` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3264.0 / 3232.0 / -0.8052284452650282 / 154.71549458699278 | [NPY](tensors/0004666.npy) |
| 4667 | `model.layers.23.self_attn` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3264.0 / 3232.0 / -0.8052284452650282 / 154.71549458699278 | [NPY](tensors/0004667.npy) |
| 4668 | `model.layers.23.self_attn` | 39 | `output[1]` | [1, 64, 1, 344] | torch.bfloat16 → float32 | 3.694961003830599e-16 / 0.96875 / 0.0011449353672884138 / 0.016370100668183472 | [NPY](tensors/0004668.npy) |
| 4669 | `model.layers.23.post_attention_layernorm` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5568.0 / 5920.0 / 1.7964301215277778 / 378.28183675428295 | [NPY](tensors/0004669.npy) |
| 4670 | `model.layers.23.post_attention_layernorm` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 12.3125 / -0.009424303637610541 / 1.485800743303553 | [NPY](tensors/0004670.npy) |
| 4671 | `model.layers.23.mlp` | 39 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 12.3125 / -0.009424303637610541 / 1.485800743303553 | [NPY](tensors/0004671.npy) |
| 4672 | `model.layers.23.mlp.experts` | 39 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -42.5 / 12.3125 / -0.009424303637610541 / 1.485800743303553 | [NPY](tensors/0004672.npy) |
| 4673 | `model.layers.23.mlp.experts` | 39 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4674 | `model.layers.23.mlp.experts` | 39 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4675 | `model.layers.23.mlp.experts` | 39 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4676 | `model.layers.23.mlp.experts` | 39 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5664.0 / 5184.0 / -6.045426432291666 / 323.5181492065789 | [NPY](tensors/0004676.npy) |
| 4677 | `model.layers.23.mlp` | 39 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5664.0 / 5184.0 / -6.045426432291666 / 323.5181492065789 | [NPY](tensors/0004677.npy) |
| 4678 | `model.layers.23.mlp` | 39 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.28125 / 2.59375 / 0.1131591796875 / 1.7612066391574668 | [NPY](tensors/0004678.npy) |
| 4679 | `model.layers.23` | 39 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2752.0 / 1760.0 / -4.269574652777778 / 351.5918837672199 | [NPY](tensors/0004679.npy) |
| 4758 | `model.layers.23` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 10176.0 / 0.9804456922743056 / 459.3244311750787 | [NPY](tensors/0004758.npy) |
| 4759 | `model.layers.23` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 345] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004759.npy) |
| 4760 | `model.layers.23` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8131542205810547 / 0.8233916239555151 | [NPY](tensors/0004760.npy) |
| 4761 | `model.layers.23` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.07140964269638062 / 0.6820182328303498 | [NPY](tensors/0004761.npy) |
| 4762 | `model.layers.23` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 344.0 / 344.0 / 344.0 / 0.0 | [NPY](tensors/0004762.npy) |
| 4763 | `model.layers.23` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4764 | `model.layers.23` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4765 | `model.layers.23` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4766 | `model.layers.23.input_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9344.0 / 10176.0 / 0.9804456922743056 / 459.3244311750787 | [NPY](tensors/0004766.npy) |
| 4767 | `model.layers.23.input_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 59.5 / 0.01622528764936659 / 1.7732148814786868 | [NPY](tensors/0004767.npy) |
| 4768 | `model.layers.23.self_attn` | 40 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 59.5 / 0.01622528764936659 / 1.7732148814786868 | [NPY](tensors/0004768.npy) |
| 4769 | `model.layers.23.self_attn` | 40 | `input.kwargs['attention_mask']` | [1, 1, 1, 345] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004769.npy) |
| 4770 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 344.0 / 344.0 / 344.0 / 0.0 | [NPY](tensors/0004770.npy) |
| 4771 | `model.layers.23.self_attn` | 40 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4772 | `model.layers.23.self_attn` | 40 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4773 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8131542205810547 / 0.8233916239555151 | [NPY](tensors/0004773.npy) |
| 4774 | `model.layers.23.self_attn` | 40 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.07140964269638062 / 0.6820182328303498 | [NPY](tensors/0004774.npy) |
| 4775 | `model.layers.23.self_attn` | 40 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4776 | `model.layers.23.self_attn.q_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 59.5 / 0.01622528764936659 / 1.7732148814786868 | [NPY](tensors/0004776.npy) |
| 4777 | `model.layers.23.self_attn.q_proj` | 40 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -12.0625 / 16.625 / 0.04947617091238499 / 1.5435893014899926 | [NPY](tensors/0004777.npy) |
| 4778 | `model.layers.23.self_attn.k_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 59.5 / 0.01622528764936659 / 1.7732148814786868 | [NPY](tensors/0004778.npy) |
| 4779 | `model.layers.23.self_attn.k_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -32.0 / 28.625 / -0.12573682516813278 / 4.247339236163782 | [NPY](tensors/0004779.npy) |
| 4780 | `model.layers.23.self_attn.v_proj` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -43.0 / 59.5 / 0.01622528764936659 / 1.7732148814786868 | [NPY](tensors/0004780.npy) |
| 4781 | `model.layers.23.self_attn.v_proj` | 40 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.5 / 13.75 / 0.1576840877532959 / 4.017761839948759 | [NPY](tensors/0004781.npy) |
| 4782 | `model.layers.23.self_attn.o_proj` | 40 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.9375 / 7.34375 / 0.016842440945765702 / 1.1909686280721268 | [NPY](tensors/0004782.npy) |
| 4783 | `model.layers.23.self_attn.o_proj` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2944.0 / 3088.0 / 2.9030497550964354 / 153.75363578919948 | [NPY](tensors/0004783.npy) |
| 4784 | `model.layers.23.self_attn` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2944.0 / 3088.0 / 2.9030497550964354 / 153.75363578919948 | [NPY](tensors/0004784.npy) |
| 4785 | `model.layers.23.self_attn` | 40 | `output[1]` | [1, 64, 1, 345] | torch.bfloat16 → float32 | 6.661338147750939e-14 / 0.80859375 / 0.0011721054244967356 / 0.009964116730840687 | [NPY](tensors/0004785.npy) |
| 4786 | `model.layers.23.post_attention_layernorm` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7360.0 / 8000.0 / 3.8815266927083334 / 421.74476937431774 | [NPY](tensors/0004786.npy) |
| 4787 | `model.layers.23.post_attention_layernorm` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 11.8125 / -0.010087373521592882 / 1.4225673176618867 | [NPY](tensors/0004787.npy) |
| 4788 | `model.layers.23.mlp` | 40 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 11.8125 / -0.010087373521592882 / 1.4225673176618867 | [NPY](tensors/0004788.npy) |
| 4789 | `model.layers.23.mlp.experts` | 40 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -42.5 / 11.8125 / -0.010087373521592882 / 1.4225673176618867 | [NPY](tensors/0004789.npy) |
| 4790 | `model.layers.23.mlp.experts` | 40 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4791 | `model.layers.23.mlp.experts` | 40 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4792 | `model.layers.23.mlp.experts` | 40 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4793 | `model.layers.23.mlp.experts` | 40 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4896.0 / 5056.0 / -3.6747754361894396 / 262.76886205599885 | [NPY](tensors/0004793.npy) |
| 4794 | `model.layers.23.mlp` | 40 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4896.0 / 5056.0 / -3.6747754361894396 / 262.76886205599885 | [NPY](tensors/0004794.npy) |
| 4795 | `model.layers.23.mlp` | 40 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -4.03125 / 2.078125 / 0.02081298828125 / 1.4686882825322825 | [NPY](tensors/0004795.npy) |
| 4796 | `model.layers.23` | 40 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2432.0 / 3104.0 / 0.20249565972222222 / 311.88066419199896 | [NPY](tensors/0004796.npy) |
| 4875 | `model.layers.23` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11136.0 / 11072.0 / -1.5689914279513888 / 496.0071066158983 | [NPY](tensors/0004875.npy) |
| 4876 | `model.layers.23` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 346] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004876.npy) |
| 4877 | `model.layers.23` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.8764495849609375 / 0.8009113437243138 | [NPY](tensors/0004877.npy) |
| 4878 | `model.layers.23` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.020697563886642456 / 0.632324519915983 | [NPY](tensors/0004878.npy) |
| 4879 | `model.layers.23` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 345.0 / 345.0 / 345.0 / 0.0 | [NPY](tensors/0004879.npy) |
| 4880 | `model.layers.23` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4881 | `model.layers.23` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4882 | `model.layers.23` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4883 | `model.layers.23.input_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -11136.0 / 11072.0 / -1.5689914279513888 / 496.0071066158983 | [NPY](tensors/0004883.npy) |
| 4884 | `model.layers.23.input_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 60.0 / 0.007280835840437147 / 1.772624873556222 | [NPY](tensors/0004884.npy) |
| 4885 | `model.layers.23.self_attn` | 41 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 60.0 / 0.007280835840437147 / 1.772624873556222 | [NPY](tensors/0004885.npy) |
| 4886 | `model.layers.23.self_attn` | 41 | `input.kwargs['attention_mask']` | [1, 1, 1, 346] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004886.npy) |
| 4887 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 345.0 / 345.0 / 345.0 / 0.0 | [NPY](tensors/0004887.npy) |
| 4888 | `model.layers.23.self_attn` | 41 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4889 | `model.layers.23.self_attn` | 41 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4890 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.328125 / 1.34375 / 0.8764495849609375 / 0.8009113437243138 | [NPY](tensors/0004890.npy) |
| 4891 | `model.layers.23.self_attn` | 41 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3046875 / -0.020697563886642456 / 0.632324519915983 | [NPY](tensors/0004891.npy) |
| 4892 | `model.layers.23.self_attn` | 41 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 4893 | `model.layers.23.self_attn.q_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 60.0 / 0.007280835840437147 / 1.772624873556222 | [NPY](tensors/0004893.npy) |
| 4894 | `model.layers.23.self_attn.q_proj` | 41 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.8125 / 12.125 / 0.04976822389289737 / 1.3750328678166202 | [NPY](tensors/0004894.npy) |
| 4895 | `model.layers.23.self_attn.k_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 60.0 / 0.007280835840437147 / 1.772624873556222 | [NPY](tensors/0004895.npy) |
| 4896 | `model.layers.23.self_attn.k_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -39.25 / 39.25 / -0.1024648416787386 / 4.529369519095281 | [NPY](tensors/0004896.npy) |
| 4897 | `model.layers.23.self_attn.v_proj` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -47.25 / 60.0 / 0.007280835840437147 / 1.772624873556222 | [NPY](tensors/0004897.npy) |
| 4898 | `model.layers.23.self_attn.v_proj` | 41 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -19.75 / 6.875 / -0.03501710295677185 / 2.547343888182812 | [NPY](tensors/0004898.npy) |
| 4899 | `model.layers.23.self_attn.o_proj` | 41 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -16.625 / 6.0625 / 0.017979695927351713 / 1.0588865449387916 | [NPY](tensors/0004899.npy) |
| 4900 | `model.layers.23.self_attn.o_proj` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4736.0 / 4992.0 / 4.946696514553494 / 208.68976890201964 | [NPY](tensors/0004900.npy) |
| 4901 | `model.layers.23.self_attn` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4736.0 / 4992.0 / 4.946696514553494 / 208.68976890201964 | [NPY](tensors/0004901.npy) |
| 4902 | `model.layers.23.self_attn` | 41 | `output[1]` | [1, 64, 1, 346] | torch.bfloat16 → float32 | 1.1723955140041653e-13 / 0.76171875 / 0.0013977954178997897 / 0.01108696215688388 | [NPY](tensors/0004902.npy) |
| 4903 | `model.layers.23.post_attention_layernorm` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10880.0 / 10880.0 / 3.3971733940972224 / 551.7226028892312 | [NPY](tensors/0004903.npy) |
| 4904 | `model.layers.23.post_attention_layernorm` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 6.25 / -0.00995224548710717 / 1.0990333027647476 | [NPY](tensors/0004904.npy) |
| 4905 | `model.layers.23.mlp` | 41 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -36.75 / 6.25 / -0.00995224548710717 / 1.0990333027647476 | [NPY](tensors/0004905.npy) |
| 4906 | `model.layers.23.mlp.experts` | 41 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -36.75 / 6.25 / -0.00995224548710717 / 1.0990333027647476 | [NPY](tensors/0004906.npy) |
| 4907 | `model.layers.23.mlp.experts` | 41 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 4908 | `model.layers.23.mlp.experts` | 41 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4909 | `model.layers.23.mlp.experts` | 41 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 4910 | `model.layers.23.mlp.experts` | 41 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1432.0 / 1344.0 / -2.16568537818061 / 113.83820674185708 | [NPY](tensors/0004910.npy) |
| 4911 | `model.layers.23.mlp` | 41 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1432.0 / 1344.0 / -2.16568537818061 / 113.83820674185708 | [NPY](tensors/0004911.npy) |
| 4912 | `model.layers.23.mlp` | 41 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.109375 / 1.6328125 / -0.067047119140625 / 0.7795812779801432 | [NPY](tensors/0004912.npy) |
| 4913 | `model.layers.23` | 41 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9600.0 / 9600.0 / 1.266672092013889 / 499.39475514354706 | [NPY](tensors/0004913.npy) |
| 4992 | `model.layers.23` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9472.0 / -5.1521728515625 / 462.93476880715076 | [NPY](tensors/0004992.npy) |
| 4993 | `model.layers.23` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 347] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0004993.npy) |
| 4994 | `model.layers.23` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.887237548828125 / 0.808167570442007 | [NPY](tensors/0004994.npy) |
| 4995 | `model.layers.23` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.06384772062301636 / 0.6046658936992718 | [NPY](tensors/0004995.npy) |
| 4996 | `model.layers.23` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 346.0 / 346.0 / 346.0 / 0.0 | [NPY](tensors/0004996.npy) |
| 4997 | `model.layers.23` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 4998 | `model.layers.23` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 4999 | `model.layers.23` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5000 | `model.layers.23.input_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10240.0 / 9472.0 / -5.1521728515625 / 462.93476880715076 | [NPY](tensors/0005000.npy) |
| 5001 | `model.layers.23.input_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 55.0 / -0.0026896079381306965 / 1.7329897393066402 | [NPY](tensors/0005001.npy) |
| 5002 | `model.layers.23.self_attn` | 42 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 55.0 / -0.0026896079381306965 / 1.7329897393066402 | [NPY](tensors/0005002.npy) |
| 5003 | `model.layers.23.self_attn` | 42 | `input.kwargs['attention_mask']` | [1, 1, 1, 347] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005003.npy) |
| 5004 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 346.0 / 346.0 / 346.0 / 0.0 | [NPY](tensors/0005004.npy) |
| 5005 | `model.layers.23.self_attn` | 42 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5006 | `model.layers.23.self_attn` | 42 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5007 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.887237548828125 / 0.808167570442007 | [NPY](tensors/0005007.npy) |
| 5008 | `model.layers.23.self_attn` | 42 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.06384772062301636 / 0.6046658936992718 | [NPY](tensors/0005008.npy) |
| 5009 | `model.layers.23.self_attn` | 42 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5010 | `model.layers.23.self_attn.q_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 55.0 / -0.0026896079381306965 / 1.7329897393066402 | [NPY](tensors/0005010.npy) |
| 5011 | `model.layers.23.self_attn.q_proj` | 42 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -10.6875 / 17.625 / 0.029837314039468765 / 1.3955077519498176 | [NPY](tensors/0005011.npy) |
| 5012 | `model.layers.23.self_attn.k_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 55.0 / -0.0026896079381306965 / 1.7329897393066402 | [NPY](tensors/0005012.npy) |
| 5013 | `model.layers.23.self_attn.k_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -51.0 / 36.75 / -0.1951447408646345 / 5.095557412845144 | [NPY](tensors/0005013.npy) |
| 5014 | `model.layers.23.self_attn.v_proj` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.75 / 55.0 / -0.0026896079381306965 / 1.7329897393066402 | [NPY](tensors/0005014.npy) |
| 5015 | `model.layers.23.self_attn.v_proj` | 42 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.25 / 13.0625 / 0.22152471542358398 / 4.030587614302054 | [NPY](tensors/0005015.npy) |
| 5016 | `model.layers.23.self_attn.o_proj` | 42 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.9375 / 7.0625 / 0.028347486746497452 / 1.2355016213985253 | [NPY](tensors/0005016.npy) |
| 5017 | `model.layers.23.self_attn.o_proj` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5248.0 / 5344.0 / 7.4377527025010854 / 227.044961333298 | [NPY](tensors/0005017.npy) |
| 5018 | `model.layers.23.self_attn` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5248.0 / 5344.0 / 7.4377527025010854 / 227.044961333298 | [NPY](tensors/0005018.npy) |
| 5019 | `model.layers.23.self_attn` | 42 | `output[1]` | [1, 64, 1, 347] | torch.bfloat16 → float32 | 5.1958437552457326e-14 / 0.8046875 / 0.0016036890012105804 / 0.011632639777350313 | [NPY](tensors/0005019.npy) |
| 5020 | `model.layers.23.post_attention_layernorm` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10048.0 / 9408.0 / 2.2781846788194446 / 528.5689689627113 | [NPY](tensors/0005020.npy) |
| 5021 | `model.layers.23.post_attention_layernorm` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 7.375 / -0.016044481678141487 / 1.1168560382174666 | [NPY](tensors/0005021.npy) |
| 5022 | `model.layers.23.mlp` | 42 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -38.5 / 7.375 / -0.016044481678141487 / 1.1168560382174666 | [NPY](tensors/0005022.npy) |
| 5023 | `model.layers.23.mlp.experts` | 42 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -38.5 / 7.375 / -0.016044481678141487 / 1.1168560382174666 | [NPY](tensors/0005023.npy) |
| 5024 | `model.layers.23.mlp.experts` | 42 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5025 | `model.layers.23.mlp.experts` | 42 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5026 | `model.layers.23.mlp.experts` | 42 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5027 | `model.layers.23.mlp.experts` | 42 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1392.0 / 1352.0 / -1.0791892528533935 / 116.06826885168938 | [NPY](tensors/0005027.npy) |
| 5028 | `model.layers.23.mlp` | 42 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1392.0 / 1352.0 / -1.0791892528533935 / 116.06826885168938 | [NPY](tensors/0005028.npy) |
| 5029 | `model.layers.23.mlp` | 42 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.25 / 1.1796875 / 0.003570556640625 / 0.8247409037787335 | [NPY](tensors/0005029.npy) |
| 5030 | `model.layers.23` | 42 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -8768.0 / 8096.0 / 1.2193793402777777 / 480.41036348638147 | [NPY](tensors/0005030.npy) |
| 5109 | `model.layers.23` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 10176.0 / -3.5945258246527776 / 486.9278541894808 | [NPY](tensors/0005109.npy) |
| 5110 | `model.layers.23` | 43 | `input.kwargs['attention_mask']` | [1, 1, 1, 348] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005110.npy) |
| 5111 | `model.layers.23` | 43 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.8368129730224609 / 0.8204651963806046 | [NPY](tensors/0005111.npy) |
| 5112 | `model.layers.23` | 43 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.1309933364391327 / 0.6478045244450656 | [NPY](tensors/0005112.npy) |
| 5113 | `model.layers.23` | 43 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 347.0 / 347.0 / 347.0 / 0.0 | [NPY](tensors/0005113.npy) |
| 5114 | `model.layers.23` | 43 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5115 | `model.layers.23` | 43 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5116 | `model.layers.23` | 43 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5117 | `model.layers.23.input_layernorm` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 10176.0 / -3.5945258246527776 / 486.9278541894808 | [NPY](tensors/0005117.npy) |
| 5118 | `model.layers.23.input_layernorm` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 50.75 / 0.0005502671003341675 / 1.691639600334009 | [NPY](tensors/0005118.npy) |
| 5119 | `model.layers.23.self_attn` | 43 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 50.75 / 0.0005502671003341675 / 1.691639600334009 | [NPY](tensors/0005119.npy) |
| 5120 | `model.layers.23.self_attn` | 43 | `input.kwargs['attention_mask']` | [1, 1, 1, 348] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005120.npy) |
| 5121 | `model.layers.23.self_attn` | 43 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 347.0 / 347.0 / 347.0 / 0.0 | [NPY](tensors/0005121.npy) |
| 5122 | `model.layers.23.self_attn` | 43 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5123 | `model.layers.23.self_attn` | 43 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5124 | `model.layers.23.self_attn` | 43 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.28125 / 1.34375 / 0.8368129730224609 / 0.8204651963806046 | [NPY](tensors/0005124.npy) |
| 5125 | `model.layers.23.self_attn` | 43 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.1309933364391327 / 0.6478045244450656 | [NPY](tensors/0005125.npy) |
| 5126 | `model.layers.23.self_attn` | 43 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5127 | `model.layers.23.self_attn.q_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 50.75 / 0.0005502671003341675 / 1.691639600334009 | [NPY](tensors/0005127.npy) |
| 5128 | `model.layers.23.self_attn.q_proj` | 43 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.6875 / 14.5625 / 0.03348583338083699 / 1.4750565176368013 | [NPY](tensors/0005128.npy) |
| 5129 | `model.layers.23.self_attn.k_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 50.75 / 0.0005502671003341675 / 1.691639600334009 | [NPY](tensors/0005129.npy) |
| 5130 | `model.layers.23.self_attn.k_proj` | 43 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -52.75 / 42.0 / -0.07703039050102234 / 4.831607658226055 | [NPY](tensors/0005130.npy) |
| 5131 | `model.layers.23.self_attn.v_proj` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -41.25 / 50.75 / 0.0005502671003341675 / 1.691639600334009 | [NPY](tensors/0005131.npy) |
| 5132 | `model.layers.23.self_attn.v_proj` | 43 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.0 / 11.25 / -0.07972132414579391 / 3.366583019129327 | [NPY](tensors/0005132.npy) |
| 5133 | `model.layers.23.self_attn.o_proj` | 43 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -15.1875 / 7.34375 / 0.02766044539748691 / 0.927161002528058 | [NPY](tensors/0005133.npy) |
| 5134 | `model.layers.23.self_attn.o_proj` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3904.0 / 4096.0 / 3.3805433577961392 / 169.8197757694179 | [NPY](tensors/0005134.npy) |
| 5135 | `model.layers.23.self_attn` | 43 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3904.0 / 4096.0 / 3.3805433577961392 / 169.8197757694179 | [NPY](tensors/0005135.npy) |
| 5136 | `model.layers.23.self_attn` | 43 | `output[1]` | [1, 64, 1, 348] | torch.bfloat16 → float32 | 1.0380585280245214e-14 / 0.6328125 / 0.0009738562423959519 / 0.009632951417669485 | [NPY](tensors/0005136.npy) |
| 5137 | `model.layers.23.post_attention_layernorm` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9152.0 / 9856.0 / -0.20875922309027778 / 513.2949077965391 | [NPY](tensors/0005137.npy) |
| 5138 | `model.layers.23.post_attention_layernorm` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 9.75 / -0.021992100609673396 / 1.3465766356794855 | [NPY](tensors/0005138.npy) |
| 5139 | `model.layers.23.mlp` | 43 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -44.0 / 9.75 / -0.021992100609673396 / 1.3465766356794855 | [NPY](tensors/0005139.npy) |
| 5140 | `model.layers.23.mlp.experts` | 43 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -44.0 / 9.75 / -0.021992100609673396 / 1.3465766356794855 | [NPY](tensors/0005140.npy) |
| 5141 | `model.layers.23.mlp.experts` | 43 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5142 | `model.layers.23.mlp.experts` | 43 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5143 | `model.layers.23.mlp.experts` | 43 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5144 | `model.layers.23.mlp.experts` | 43 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4320.0 / 4576.0 / 0.5042795817057292 / 265.7584642385036 | [NPY](tensors/0005144.npy) |
| 5145 | `model.layers.23.mlp` | 43 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4320.0 / 4576.0 / 0.5042795817057292 / 265.7584642385036 | [NPY](tensors/0005145.npy) |
| 5146 | `model.layers.23.mlp` | 43 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -2.421875 / 2.203125 / -0.0331730842590332 / 1.0844794611044577 | [NPY](tensors/0005146.npy) |
| 5147 | `model.layers.23` | 43 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -10176.0 / 10304.0 / 0.33450520833333336 / 645.6012990889753 | [NPY](tensors/0005147.npy) |
| 5226 | `model.layers.23` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9408.0 / 1.0370985243055555 / 483.2122075034688 | [NPY](tensors/0005226.npy) |
| 5227 | `model.layers.23` | 44 | `input.kwargs['attention_mask']` | [1, 1, 1, 349] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005227.npy) |
| 5228 | `model.layers.23` | 44 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7588653564453125 / 0.8828955932720353 | [NPY](tensors/0005228.npy) |
| 5229 | `model.layers.23` | 44 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14290890097618103 / 0.6590419455082627 | [NPY](tensors/0005229.npy) |
| 5230 | `model.layers.23` | 44 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 348.0 / 348.0 / 348.0 / 0.0 | [NPY](tensors/0005230.npy) |
| 5231 | `model.layers.23` | 44 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5232 | `model.layers.23` | 44 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5233 | `model.layers.23` | 44 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5234 | `model.layers.23.input_layernorm` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9408.0 / 1.0370985243055555 / 483.2122075034688 | [NPY](tensors/0005234.npy) |
| 5235 | `model.layers.23.input_layernorm` | 44 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 52.25 / 0.015177257855733236 / 1.717896077121647 | [NPY](tensors/0005235.npy) |
| 5236 | `model.layers.23.self_attn` | 44 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 52.25 / 0.015177257855733236 / 1.717896077121647 | [NPY](tensors/0005236.npy) |
| 5237 | `model.layers.23.self_attn` | 44 | `input.kwargs['attention_mask']` | [1, 1, 1, 349] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005237.npy) |
| 5238 | `model.layers.23.self_attn` | 44 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 348.0 / 348.0 / 348.0 / 0.0 | [NPY](tensors/0005238.npy) |
| 5239 | `model.layers.23.self_attn` | 44 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5240 | `model.layers.23.self_attn` | 44 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5241 | `model.layers.23.self_attn` | 44 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7588653564453125 / 0.8828955932720353 | [NPY](tensors/0005241.npy) |
| 5242 | `model.layers.23.self_attn` | 44 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3125 / 0.14290890097618103 / 0.6590419455082627 | [NPY](tensors/0005242.npy) |
| 5243 | `model.layers.23.self_attn` | 44 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5244 | `model.layers.23.self_attn.q_proj` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 52.25 / 0.015177257855733236 / 1.717896077121647 | [NPY](tensors/0005244.npy) |
| 5245 | `model.layers.23.self_attn.q_proj` | 44 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.5625 / 17.5 / 0.03715611173538491 / 1.565663714177844 | [NPY](tensors/0005245.npy) |
| 5246 | `model.layers.23.self_attn.k_proj` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 52.25 / 0.015177257855733236 / 1.717896077121647 | [NPY](tensors/0005246.npy) |
| 5247 | `model.layers.23.self_attn.k_proj` | 44 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -45.25 / 31.125 / -0.044940559193491936 / 4.392107420489146 | [NPY](tensors/0005247.npy) |
| 5248 | `model.layers.23.self_attn.v_proj` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -46.5 / 52.25 / 0.015177257855733236 / 1.717896077121647 | [NPY](tensors/0005248.npy) |
| 5249 | `model.layers.23.self_attn.v_proj` | 44 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -20.5 / 13.3125 / -0.18051481246948242 / 3.7636243733327084 | [NPY](tensors/0005249.npy) |
| 5250 | `model.layers.23.self_attn.o_proj` | 44 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -17.5 / 7.375 / 0.025085669825784862 / 1.4254854820749734 | [NPY](tensors/0005250.npy) |
| 5251 | `model.layers.23.self_attn.o_proj` | 44 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -5632.0 / 5792.0 / 7.504941940307617 / 252.12636811676822 | [NPY](tensors/0005251.npy) |
| 5252 | `model.layers.23.self_attn` | 44 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5632.0 / 5792.0 / 7.504941940307617 / 252.12636811676822 | [NPY](tensors/0005252.npy) |
| 5253 | `model.layers.23.self_attn` | 44 | `output[1]` | [1, 64, 1, 349] | torch.bfloat16 → float32 | 3.774758283725532e-14 / 0.85546875 / 0.0017317094501197242 / 0.014581511279403528 | [NPY](tensors/0005253.npy) |
| 5254 | `model.layers.23.post_attention_layernorm` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -10624.0 / 9472.0 / 8.54656032986111 / 560.9462727322777 | [NPY](tensors/0005254.npy) |
| 5255 | `model.layers.23.post_attention_layernorm` | 44 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 8.5 / 0.005181321832868788 / 1.193934536197944 | [NPY](tensors/0005255.npy) |
| 5256 | `model.layers.23.mlp` | 44 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -37.25 / 8.5 / 0.005181321832868788 / 1.193934536197944 | [NPY](tensors/0005256.npy) |
| 5257 | `model.layers.23.mlp.experts` | 44 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -37.25 / 8.5 / 0.005181321832868788 / 1.193934536197944 | [NPY](tensors/0005257.npy) |
| 5258 | `model.layers.23.mlp.experts` | 44 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5259 | `model.layers.23.mlp.experts` | 44 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5260 | `model.layers.23.mlp.experts` | 44 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5261 | `model.layers.23.mlp.experts` | 44 | `output` | [1, 2880] | torch.bfloat16 → float32 | -1728.0 / 1528.0 / -1.9811260647243925 / 128.82711595975886 | [NPY](tensors/0005261.npy) |
| 5262 | `model.layers.23.mlp` | 44 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -1728.0 / 1528.0 / -1.9811260647243925 / 128.82711595975886 | [NPY](tensors/0005262.npy) |
| 5263 | `model.layers.23.mlp` | 44 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -1.9140625 / 1.171875 / -0.007095962762832642 / 0.6631551286214813 | [NPY](tensors/0005263.npy) |
| 5264 | `model.layers.23` | 44 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -9536.0 / 8576.0 / 6.5455946180555555 / 541.1121183363466 | [NPY](tensors/0005264.npy) |
| 5343 | `model.layers.23` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9856.0 / 10688.0 / -0.7337429470486111 / 488.88120468335114 | [NPY](tensors/0005343.npy) |
| 5344 | `model.layers.23` | 45 | `input.kwargs['attention_mask']` | [1, 1, 1, 350] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005344.npy) |
| 5345 | `model.layers.23` | 45 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.701873779296875 / 0.9298159802037973 | [NPY](tensors/0005345.npy) |
| 5346 | `model.layers.23` | 45 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.10132250189781189 / 0.6650396518932735 | [NPY](tensors/0005346.npy) |
| 5347 | `model.layers.23` | 45 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 349.0 / 349.0 / 349.0 / 0.0 | [NPY](tensors/0005347.npy) |
| 5348 | `model.layers.23` | 45 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5349 | `model.layers.23` | 45 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5350 | `model.layers.23` | 45 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5351 | `model.layers.23.input_layernorm` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -9856.0 / 10688.0 / -0.7337429470486111 / 488.88120468335114 | [NPY](tensors/0005351.npy) |
| 5352 | `model.layers.23.input_layernorm` | 45 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 58.75 / 0.011098076899846395 / 1.7763907018039413 | [NPY](tensors/0005352.npy) |
| 5353 | `model.layers.23.self_attn` | 45 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 58.75 / 0.011098076899846395 / 1.7763907018039413 | [NPY](tensors/0005353.npy) |
| 5354 | `model.layers.23.self_attn` | 45 | `input.kwargs['attention_mask']` | [1, 1, 1, 350] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005354.npy) |
| 5355 | `model.layers.23.self_attn` | 45 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 349.0 / 349.0 / 349.0 / 0.0 | [NPY](tensors/0005355.npy) |
| 5356 | `model.layers.23.self_attn` | 45 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5357 | `model.layers.23.self_attn` | 45 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5358 | `model.layers.23.self_attn` | 45 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.34375 / 0.701873779296875 / 0.9298159802037973 | [NPY](tensors/0005358.npy) |
| 5359 | `model.layers.23.self_attn` | 45 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.34375 / 1.3359375 / 0.10132250189781189 / 0.6650396518932735 | [NPY](tensors/0005359.npy) |
| 5360 | `model.layers.23.self_attn` | 45 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5361 | `model.layers.23.self_attn.q_proj` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 58.75 / 0.011098076899846395 / 1.7763907018039413 | [NPY](tensors/0005361.npy) |
| 5362 | `model.layers.23.self_attn.q_proj` | 45 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.6875 / 16.625 / 0.058741282555274665 / 1.6661077409773137 | [NPY](tensors/0005362.npy) |
| 5363 | `model.layers.23.self_attn.k_proj` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 58.75 / 0.011098076899846395 / 1.7763907018039413 | [NPY](tensors/0005363.npy) |
| 5364 | `model.layers.23.self_attn.k_proj` | 45 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -35.25 / 28.375 / -0.10308495163917542 / 4.464399066615399 | [NPY](tensors/0005364.npy) |
| 5365 | `model.layers.23.self_attn.v_proj` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -42.5 / 58.75 / 0.011098076899846395 / 1.7763907018039413 | [NPY](tensors/0005365.npy) |
| 5366 | `model.layers.23.self_attn.v_proj` | 45 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -18.75 / 17.75 / -0.07493293285369873 / 5.0682696901633655 | [NPY](tensors/0005366.npy) |
| 5367 | `model.layers.23.self_attn.o_proj` | 45 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.8125 / 7.03125 / 0.05428475479129702 / 1.37101662789311 | [NPY](tensors/0005367.npy) |
| 5368 | `model.layers.23.self_attn.o_proj` | 45 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2944.0 / 2976.0 / 2.240946536593967 / 155.21492569616007 | [NPY](tensors/0005368.npy) |
| 5369 | `model.layers.23.self_attn` | 45 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -2944.0 / 2976.0 / 2.240946536593967 / 155.21492569616007 | [NPY](tensors/0005369.npy) |
| 5370 | `model.layers.23.self_attn` | 45 | `output[1]` | [1, 64, 1, 350] | torch.bfloat16 → float32 | 7.022160630754115e-15 / 0.9140625 / 0.0014322046624155346 / 0.013857691681057343 | [NPY](tensors/0005370.npy) |
| 5371 | `model.layers.23.post_attention_layernorm` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8384.0 / 9152.0 / 1.5372938368055555 / 476.09298202688956 | [NPY](tensors/0005371.npy) |
| 5372 | `model.layers.23.post_attention_layernorm` | 45 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 10.3125 / -0.013625717163085938 / 1.3768129593000107 | [NPY](tensors/0005372.npy) |
| 5373 | `model.layers.23.mlp` | 45 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.5 / 10.3125 / -0.013625717163085938 / 1.3768129593000107 | [NPY](tensors/0005373.npy) |
| 5374 | `model.layers.23.mlp.experts` | 45 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.5 / 10.3125 / -0.013625717163085938 / 1.3768129593000107 | [NPY](tensors/0005374.npy) |
| 5375 | `model.layers.23.mlp.experts` | 45 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5376 | `model.layers.23.mlp.experts` | 45 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5377 | `model.layers.23.mlp.experts` | 45 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5378 | `model.layers.23.mlp.experts` | 45 | `output` | [1, 2880] | torch.bfloat16 → float32 | -4448.0 / 4256.0 / -11.688961781395806 / 324.13005972390977 | [NPY](tensors/0005378.npy) |
| 5379 | `model.layers.23.mlp` | 45 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -4448.0 / 4256.0 / -11.688961781395806 / 324.13005972390977 | [NPY](tensors/0005379.npy) |
| 5380 | `model.layers.23.mlp` | 45 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.328125 / 2.015625 / 0.0254974365234375 / 1.2084293338368945 | [NPY](tensors/0005380.npy) |
| 5381 | `model.layers.23` | 45 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -4128.0 / 4704.0 / -10.160763888888889 / 450.45113705305795 | [NPY](tensors/0005381.npy) |
| 5460 | `model.layers.23` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8640.0 / 9472.0 / -0.4444037543402778 / 452.6356691741967 | [NPY](tensors/0005460.npy) |
| 5461 | `model.layers.23` | 46 | `input.kwargs['attention_mask']` | [1, 1, 1, 351] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005461.npy) |
| 5462 | `model.layers.23` | 46 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.690826416015625 / 0.927895842605205 | [NPY](tensors/0005462.npy) |
| 5463 | `model.layers.23` | 46 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.04170632362365723 / 0.685352030153117 | [NPY](tensors/0005463.npy) |
| 5464 | `model.layers.23` | 46 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 350.0 / 350.0 / 350.0 / 0.0 | [NPY](tensors/0005464.npy) |
| 5465 | `model.layers.23` | 46 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5466 | `model.layers.23` | 46 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5467 | `model.layers.23` | 46 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5468 | `model.layers.23.input_layernorm` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -8640.0 / 9472.0 / -0.4444037543402778 / 452.6356691741967 | [NPY](tensors/0005468.npy) |
| 5469 | `model.layers.23.input_layernorm` | 46 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 56.25 / 0.017531349923875596 / 1.7542369103934714 | [NPY](tensors/0005469.npy) |
| 5470 | `model.layers.23.self_attn` | 46 | `input.kwargs['hidden_states']` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 56.25 / 0.017531349923875596 / 1.7542369103934714 | [NPY](tensors/0005470.npy) |
| 5471 | `model.layers.23.self_attn` | 46 | `input.kwargs['attention_mask']` | [1, 1, 1, 351] | torch.bfloat16 → float32 | 0.0 / 0.0 / 0.0 / 0.0 | [NPY](tensors/0005471.npy) |
| 5472 | `model.layers.23.self_attn` | 46 | `input.kwargs['position_ids']` | [1, 1] | torch.int64 → int64 | 350.0 / 350.0 / 350.0 / 0.0 | [NPY](tensors/0005472.npy) |
| 5473 | `model.layers.23.self_attn` | 46 | `input.kwargs['past_key_values']` | — | DynamicCache | opaque object or empty container; no tensor leaf exposed | — |
| 5474 | `model.layers.23.self_attn` | 46 | `input.kwargs['use_cache']` | — | bool | True | — |
| 5475 | `model.layers.23.self_attn` | 46 | `input.kwargs['position_embeddings'][0]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.2734375 / 1.34375 / 0.690826416015625 / 0.927895842605205 | [NPY](tensors/0005475.npy) |
| 5476 | `model.layers.23.self_attn` | 46 | `input.kwargs['position_embeddings'][1]` | [1, 1, 32] | torch.bfloat16 → float32 | -1.3359375 / 1.328125 / 0.04170632362365723 / 0.685352030153117 | [NPY](tensors/0005476.npy) |
| 5477 | `model.layers.23.self_attn` | 46 | `input.kwargs['output_router_logits']` | — | bool | False | — |
| 5478 | `model.layers.23.self_attn.q_proj` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 56.25 / 0.017531349923875596 / 1.7542369103934714 | [NPY](tensors/0005478.npy) |
| 5479 | `model.layers.23.self_attn.q_proj` | 46 | `output` | [1, 1, 4096] | torch.bfloat16 → float32 | -11.5 / 16.375 / 0.05070975667331368 / 1.7851377396690022 | [NPY](tensors/0005479.npy) |
| 5480 | `model.layers.23.self_attn.k_proj` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 56.25 / 0.017531349923875596 / 1.7542369103934714 | [NPY](tensors/0005480.npy) |
| 5481 | `model.layers.23.self_attn.k_proj` | 46 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -27.375 / 33.75 / -0.07872530072927475 / 4.439301844496079 | [NPY](tensors/0005481.npy) |
| 5482 | `model.layers.23.self_attn.v_proj` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -40.25 / 56.25 / 0.017531349923875596 / 1.7542369103934714 | [NPY](tensors/0005482.npy) |
| 5483 | `model.layers.23.self_attn.v_proj` | 46 | `output` | [1, 1, 512] | torch.bfloat16 → float32 | -13.5625 / 12.3125 / 0.007243037223815918 / 3.614131797197381 | [NPY](tensors/0005483.npy) |
| 5484 | `model.layers.23.self_attn.o_proj` | 46 | `input.args[0]` | [1, 1, 4096] | torch.bfloat16 → float32 | -13.125 / 12.8125 / 0.07096371077932417 / 1.7802515215387538 | [NPY](tensors/0005484.npy) |
| 5485 | `model.layers.23.self_attn.o_proj` | 46 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -3536.0 / 3504.0 / 3.634653833177355 / 189.2839849009779 | [NPY](tensors/0005485.npy) |
| 5486 | `model.layers.23.self_attn` | 46 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -3536.0 / 3504.0 / 3.634653833177355 / 189.2839849009779 | [NPY](tensors/0005486.npy) |
| 5487 | `model.layers.23.self_attn` | 46 | `output[1]` | [1, 64, 1, 351] | torch.bfloat16 → float32 | 1.6653345369377348e-15 / 0.96875 / 0.001792517656964271 / 0.018801364963866772 | [NPY](tensors/0005487.npy) |
| 5488 | `model.layers.23.post_attention_layernorm` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -7776.0 / 8576.0 / 3.199235026041667 / 482.2308976941501 | [NPY](tensors/0005488.npy) |
| 5489 | `model.layers.23.post_attention_layernorm` | 46 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 8.4375 / -0.009855047861735026 / 1.3925100337984564 | [NPY](tensors/0005489.npy) |
| 5490 | `model.layers.23.mlp` | 46 | `input.args[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -33.0 / 8.4375 / -0.009855047861735026 / 1.3925100337984564 | [NPY](tensors/0005490.npy) |
| 5491 | `model.layers.23.mlp.experts` | 46 | `input.args[0]` | [1, 2880] | torch.bfloat16 → float32 | -33.0 / 8.4375 / -0.009855047861735026 / 1.3925100337984564 | [NPY](tensors/0005491.npy) |
| 5492 | `model.layers.23.mlp.experts` | 46 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 5493 | `model.layers.23.mlp.experts` | 46 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5494 | `model.layers.23.mlp.experts` | 46 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 5495 | `model.layers.23.mlp.experts` | 46 | `output` | [1, 2880] | torch.bfloat16 → float32 | -5856.0 / 5376.0 / -0.8039282533857558 / 336.764375358299 | [NPY](tensors/0005495.npy) |
| 5496 | `model.layers.23.mlp` | 46 | `output[0]` | [1, 1, 2880] | torch.bfloat16 → float32 | -5856.0 / 5376.0 / -0.8039282533857558 / 336.764375358299 | [NPY](tensors/0005496.npy) |
| 5497 | `model.layers.23.mlp` | 46 | `output[1]` | [1, 32] | torch.bfloat16 → float32 | -3.046875 / 1.59375 / 0.02037811279296875 / 1.0442104091942894 | [NPY](tensors/0005497.npy) |
| 5498 | `model.layers.23` | 46 | `output` | [1, 1, 2880] | torch.bfloat16 → float32 | -2400.0 / 2720.0 / 2.396408420138889 / 430.844533377934 | [NPY](tensors/0005498.npy) |

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
