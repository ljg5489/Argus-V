# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.01654049346119406 / 2.8033308559135977 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 495, 495] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.625484464688161e+38 / 1.4163309396937944e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 495, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.760406024769099 / 0.8987960380804979 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 495, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11105676834563245 / 0.6412171836282708 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 495] | torch.int64 → int64 | 0.0 / 494.0 / 247.0 / 142.89390003308984 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.01654049346119406 / 2.8033308559135977 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 495, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006787156777191953 / 0.742831337958353 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 495, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006787156777191953 / 0.742831337958353 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 495, 495] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.625484464688161e+38 / 1.4163309396937944e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 495] | torch.int64 → int64 | 0.0 / 494.0 / 247.0 / 142.89390003308984 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 495, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.760406024769099 / 0.8987960380804979 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 495, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11105676834563245 / 0.6412171836282708 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006787156777191953 / 0.742831337958353 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 495, 4096] | torch.bfloat16 → float32 | -9.5 / 12.8125 / 0.017974879808319414 / 1.0262887831073217 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006787156777191953 / 0.742831337958353 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 495, 512] | torch.bfloat16 → float32 | -65.5 / 69.0 / 0.004324322503361136 / 5.824301300603005 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006787156777191953 / 0.742831337958353 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 495, 512] | torch.bfloat16 → float32 | -7.375 / 8.5 / -0.008211697914491813 / 1.1817097648403012 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 495, 4096] | torch.bfloat16 → float32 | -7.28125 / 7.75 / -0.003922063600195657 / 0.5524895265225496 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 495, 2880] | torch.bfloat16 → float32 | -41.75 / 58.75 / 0.027839012345152528 / 1.1963004419829806 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -41.75 / 58.75 / 0.027839012345152528 / 1.1963004419829806 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 495, 495] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0008056077140414855 / 0.018567784309976756 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -87.5 / 71.5 / 0.011293321972008372 / 2.999637992051407 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 495, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 9.62867354921888e-05 / 0.3231159600791225 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 9.62867354921888e-05 / 0.3231159600791225 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [495, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 9.62867354921888e-05 / 0.3231159600791225 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [495, 2880] | torch.bfloat16 → float32 | -50.0 / 92.5 / 0.018190219451314802 / 0.8650221748335892 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -50.0 / 92.5 / 0.018190219451314802 / 0.8650221748335892 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [495, 32] | torch.bfloat16 → float32 | -5.71875 / 3.421875 / -0.0959201581550367 / 1.0539024264503383 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 495, 2880] | torch.bfloat16 → float32 | -93.0 / 106.0 / 0.029485324187043267 / 3.2069440090106753 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.46843004853904713 / 40.62248792773143 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 495, 495] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6913419255457158e+38 / 1.694762236269633e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 495, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.760406024769099 / 0.8987960380804979 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 495, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11105676834563245 / 0.6412171836282708 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 495] | torch.int64 → int64 | 0.0 / 494.0 / 247.0 / 142.89390003308984 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.46843004853904713 / 40.62248792773143 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 495, 2880] | torch.bfloat16 → float32 | -191.0 / 146.0 / 0.06166488435959775 / 3.2169044922905132 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 495, 2880] | torch.bfloat16 → float32 | -191.0 / 146.0 / 0.06166488435959775 / 3.2169044922905132 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 495, 495] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6913419255457158e+38 / 1.694762236269633e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 495] | torch.int64 → int64 | 0.0 / 494.0 / 247.0 / 142.89390003308984 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 495, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.760406024769099 / 0.8987960380804979 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 495, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11105676834563245 / 0.6412171836282708 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -191.0 / 146.0 / 0.06166488435959775 / 3.2169044922905132 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 495, 4096] | torch.bfloat16 → float32 | -12.25 / 13.3125 / 0.03817114594694615 / 1.3246192676844901 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -191.0 / 146.0 / 0.06166488435959775 / 3.2169044922905132 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 495, 512] | torch.bfloat16 → float32 | -38.75 / 49.5 / 0.08397183275706313 / 3.7966833834554072 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -191.0 / 146.0 / 0.06166488435959775 / 3.2169044922905132 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 495, 512] | torch.bfloat16 → float32 | -15.875 / 22.125 / -0.044402818347214525 / 2.5053500599158913 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 495, 4096] | torch.bfloat16 → float32 | -11.75 / 11.375 / -0.03204014624310675 / 1.4331991225445306 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 495, 2880] | torch.bfloat16 → float32 | -468.0 / 502.0 / -0.0074641809598506165 / 6.195408187677823 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -468.0 / 502.0 / -0.0074641809598506165 / 6.195408187677823 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 495, 495] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0017562539991042886 / 0.014554936027470593 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -41216.0 / 700.0 / 0.46091686106423874 / 39.800041384399655 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 495, 2880] | torch.bfloat16 → float32 | -78.5 / 9.9375 / 0.009935486937897106 / 0.783723336584785 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -78.5 / 9.9375 / 0.009935486937897106 / 0.783723336584785 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [495, 2880] | torch.bfloat16 → float32 | -78.5 / 9.9375 / 0.009935486937897106 / 0.783723336584785 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [495, 2880] | torch.bfloat16 → float32 | -488.0 / 386.0 / 0.11013566989288587 / 9.32510742956736 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -488.0 / 386.0 / 0.11013566989288587 / 9.32510742956736 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [495, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.16991548586373378 / 0.8147181288663868 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 495, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5711062157113945 / 42.793678839465606 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -12864.0 / 13952.0 / -1.514364474346876 / 393.8831503839612 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 495, 495] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6913419255457158e+38 / 1.694762236269633e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 495, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.760406024769099 / 0.8987960380804979 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 495, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11105676834563245 / 0.6412171836282708 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 495] | torch.int64 → int64 | 0.0 / 494.0 / 247.0 / 142.89390003308984 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -12864.0 / 13952.0 / -1.514364474346876 / 393.8831503839612 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 495, 2880] | torch.bfloat16 → float32 | -53.5 / 72.0 / 0.009781006331295278 / 1.7522214036472115 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 495, 2880] | torch.bfloat16 → float32 | -53.5 / 72.0 / 0.009781006331295278 / 1.7522214036472115 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 495, 495] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6913419255457158e+38 / 1.694762236269633e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 495] | torch.int64 → int64 | 0.0 / 494.0 / 247.0 / 142.89390003308984 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 495, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.760406024769099 / 0.8987960380804979 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 495, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11105676834563245 / 0.6412171836282708 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -53.5 / 72.0 / 0.009781006331295278 / 1.7522214036472115 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 495, 4096] | torch.bfloat16 → float32 | -21.75 / 24.875 / 0.02944334736395574 / 1.6803402600898187 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -53.5 / 72.0 / 0.009781006331295278 / 1.7522214036472115 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 495, 512] | torch.bfloat16 → float32 | -86.0 / 64.5 / -0.057472899156849534 / 5.06956575256346 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -53.5 / 72.0 / 0.009781006331295278 / 1.7522214036472115 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 495, 512] | torch.bfloat16 → float32 | -27.75 / 24.625 / 0.010022111890856366 / 3.1220840984613294 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 495, 4096] | torch.bfloat16 → float32 | -26.375 / 12.9375 / -0.0002337382187412151 / 1.1337031186459747 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 495, 2880] | torch.bfloat16 → float32 | -6400.0 / 6688.0 / 2.4083966700570483 / 160.54590998915833 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -6400.0 / 6688.0 / 2.4083966700570483 / 160.54590998915833 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 495, 495] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0010104423942682134 / 0.00972501831256991 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -10560.0 / 11264.0 / 0.8942577719126485 / 349.2705242912942 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 495, 2880] | torch.bfloat16 → float32 | -52.75 / 29.0 / -0.015937351603332726 / 1.3059594153785652 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -52.75 / 29.0 / -0.015937351603332726 / 1.3059594153785652 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [495, 2880] | torch.bfloat16 → float32 | -52.75 / 29.0 / -0.015937351603332726 / 1.3059594153785652 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [495, 2880] | torch.bfloat16 → float32 | -5824.0 / 5504.0 / -1.4540934612989158 / 143.72067943633184 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 495, 2880] | torch.bfloat16 → float32 | -5824.0 / 5504.0 / -1.4540934612989158 / 143.72067943633184 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [495, 32] | torch.bfloat16 → float32 | -9.25 / 4.78125 / 0.2768177205866033 / 2.9006361300840626 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 495, 2880] | torch.bfloat16 → float32 | -10688.0 / 10944.0 / -0.5589663617511926 / 376.1286102316024 | [NPY](tensors/0000116.npy) |

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
