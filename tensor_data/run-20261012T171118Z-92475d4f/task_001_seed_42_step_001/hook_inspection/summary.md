# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012248383095620591 / 2.7925898800936846 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 468, 468] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.58826587857742e+38 / 1.4401000593565452e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 468, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7667423239630512 / 0.8927289354142104 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 468, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11385805286458618 / 0.6416538774207843 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 468] | torch.int64 → int64 | 0.0 / 467.0 / 233.5 / 135.09965457641508 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012248383095620591 / 2.7925898800936846 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 468, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.007153573925446875 / 0.76773653792045 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 468, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.007153573925446875 / 0.76773653792045 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 468, 468] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.58826587857742e+38 / 1.4401000593565452e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 468] | torch.int64 → int64 | 0.0 / 467.0 / 233.5 / 135.09965457641508 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 468, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7667423239630512 / 0.8927289354142104 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 468, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11385805286458618 / 0.6416538774207843 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.007153573925446875 / 0.76773653792045 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 468, 4096] | torch.bfloat16 → float32 | -9.0625 / 11.6875 / 0.023920843663148863 / 1.013455326626122 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.007153573925446875 / 0.76773653792045 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 468, 512] | torch.bfloat16 → float32 | -63.5 / 65.5 / 0.028924843358596325 / 5.762605763221187 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.007153573925446875 / 0.76773653792045 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 468, 512] | torch.bfloat16 → float32 | -7.375 / 9.0 / -0.011154511037012005 / 1.1835456789680396 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 468, 4096] | torch.bfloat16 → float32 | -6.84375 / 6.46875 / -0.005822698020877325 / 0.5291191586644962 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 468, 2880] | torch.bfloat16 → float32 | -39.25 / 53.75 / 0.028255972630165067 / 1.1926471327359371 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -39.25 / 53.75 / 0.028255972630165067 / 1.1926471327359371 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 468, 468] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0008478255232993375 / 0.018530588497897682 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -87.5 / 71.0 / 0.016008364594234586 / 2.9916450681243525 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 468, 2880] | torch.bfloat16 → float32 | -6.625 / 3.0625 / 0.0007669165319208576 / 0.3299014580879845 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -6.625 / 3.0625 / 0.0007669165319208576 / 0.3299014580879845 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [468, 2880] | torch.bfloat16 → float32 | -6.625 / 3.0625 / 0.0007669165319208576 / 0.3299014580879845 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [468, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.016722679116337753 / 0.8268770218207709 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.016722679116337753 / 0.8268770218207709 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [468, 32] | torch.bfloat16 → float32 | -5.125 / 3.8125 / -0.11064098227737296 / 1.0164447098853184 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 468, 2880] | torch.bfloat16 → float32 | -85.0 / 156.0 / 0.03273398574788375 / 3.2455904165373353 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -41728.0 / 1096.0 / 0.409177677629114 / 41.99222456975606 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 468, 468] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6911444004064819e+38 / 1.6947618257172713e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 468, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7667423239630512 / 0.8927289354142104 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 468, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11385805286458618 / 0.6416538774207843 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 468] | torch.int64 → int64 | 0.0 / 467.0 / 233.5 / 135.09965457641508 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -41728.0 / 1096.0 / 0.409177677629114 / 41.99222456975606 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 468, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.0554128730779289 / 3.100705278820042 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 468, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.0554128730779289 / 3.100705278820042 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 468, 468] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6911444004064819e+38 / 1.6947618257172713e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 468] | torch.int64 → int64 | 0.0 / 467.0 / 233.5 / 135.09965457641508 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 468, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7667423239630512 / 0.8927289354142104 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 468, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11385805286458618 / 0.6416538774207843 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.0554128730779289 / 3.100705278820042 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 468, 4096] | torch.bfloat16 → float32 | -12.9375 / 14.5625 / 0.0408263499395896 / 1.3735176892964887 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.0554128730779289 / 3.100705278820042 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 468, 512] | torch.bfloat16 → float32 | -39.75 / 41.5 / 0.06374521517061975 / 3.3686417983195214 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.0554128730779289 / 3.100705278820042 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 468, 512] | torch.bfloat16 → float32 | -16.0 / 22.0 / -0.013129692634370608 / 2.546187765008437 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 468, 4096] | torch.bfloat16 → float32 | -11.625 / 13.1875 / -0.014087999691201912 / 1.4078264051702682 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 468, 2880] | torch.bfloat16 → float32 | -470.0 / 394.0 / -0.03320623381896491 / 5.5501643670430205 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -470.0 / 394.0 / -0.03320623381896491 / 5.5501643670430205 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 468, 468] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0017787442033273203 / 0.01355527657044428 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -41728.0 / 648.0 / 0.37597947872375603 / 41.534825821371186 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 468, 2880] | torch.bfloat16 → float32 | -78.5 / 6.5625 / 0.0071548921715004704 / 0.7676117667734814 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -78.5 / 6.5625 / 0.0071548921715004704 / 0.7676117667734814 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [468, 2880] | torch.bfloat16 → float32 | -78.5 / 6.5625 / 0.0071548921715004704 / 0.7676117667734814 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [468, 2880] | torch.bfloat16 → float32 | -416.0 / 374.0 / 0.08603048874498657 / 7.923649649882352 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -416.0 / 374.0 / 0.08603048874498657 / 7.923649649882352 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [468, 32] | torch.bfloat16 → float32 | -10.75 / 3.015625 / -0.15743214197647878 / 0.7438231439395379 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 468, 2880] | torch.bfloat16 → float32 | -41728.0 / 872.0 / 0.46203527015838186 / 43.96024694441836 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -12800.0 / 14208.0 / -0.9613070497938485 / 414.7430846215963 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 468, 468] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6911444004064819e+38 / 1.6947618257172713e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 468, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7667423239630512 / 0.8927289354142104 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 468, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11385805286458618 / 0.6416538774207843 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 468] | torch.int64 → int64 | 0.0 / 467.0 / 233.5 / 135.09965457641508 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -12800.0 / 14208.0 / -0.9613070497938485 / 414.7430846215963 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 468, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009924069965383833 / 1.7639357181015356 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 468, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009924069965383833 / 1.7639357181015356 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 468, 468] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6911444004064819e+38 / 1.6947618257172713e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 468] | torch.int64 → int64 | 0.0 / 467.0 / 233.5 / 135.09965457641508 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 468, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7667423239630512 / 0.8927289354142104 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 468, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11385805286458618 / 0.6416538774207843 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009924069965383833 / 1.7639357181015356 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 468, 4096] | torch.bfloat16 → float32 | -19.875 / 24.75 / 0.03534140513759737 / 1.667793192728545 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009924069965383833 / 1.7639357181015356 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 468, 512] | torch.bfloat16 → float32 | -81.5 / 54.75 / -0.0879693217026433 / 4.6567465986166505 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009924069965383833 / 1.7639357181015356 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 468, 512] | torch.bfloat16 → float32 | -22.5 / 19.0 / -0.01378032515068244 / 3.251115768469466 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 468, 4096] | torch.bfloat16 → float32 | -20.625 / 14.25 / -0.007102535721367173 / 1.1027361755065708 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 468, 2880] | torch.bfloat16 → float32 | -4480.0 / 4800.0 / 2.2956714116854124 / 139.22840049513135 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -4480.0 / 4800.0 / 2.2956714116854124 / 139.22840049513135 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 468, 468] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0010841739545601548 / 0.009861038988349445 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -11200.0 / 11392.0 / 1.3334079836621697 / 357.8572689921899 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 468, 2880] | torch.bfloat16 → float32 | -50.5 / 18.5 / -0.014045935077813841 / 1.2163638845835119 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -50.5 / 18.5 / -0.014045935077813841 / 1.2163638845835119 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [468, 2880] | torch.bfloat16 → float32 | -50.5 / 18.5 / -0.014045935077813841 / 1.2163638845835119 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [468, 2880] | torch.bfloat16 → float32 | -6496.0 / 6464.0 / -1.2622661507232973 / 163.75956396423143 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 468, 2880] | torch.bfloat16 → float32 | -6496.0 / 6464.0 / -1.2622661507232973 / 163.75956396423143 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [468, 32] | torch.bfloat16 → float32 | -6.90625 / 4.03125 / 0.26460080065278924 / 2.5804495426962277 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 468, 2880] | torch.bfloat16 → float32 | -11840.0 / 12032.0 / 0.07173143406765638 / 416.02836531477874 | [NPY](tensors/0000116.npy) |

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
