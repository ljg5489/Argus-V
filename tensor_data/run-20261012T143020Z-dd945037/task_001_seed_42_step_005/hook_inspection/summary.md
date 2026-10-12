# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.01221544439083482 / 2.9000172551034193 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 306, 306] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.2659138241871622e+38 / 1.5956254490885013e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 306, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7958170518376468 / 0.8809086742441157 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 306, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12029854664894801 / 0.6210293197906489 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 306] | torch.int64 → int64 | 0.0 / 305.0 / 152.5 / 88.33411949335697 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.01221544439083482 / 2.9000172551034193 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 306, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006086902524893812 / 0.7521687774423463 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 306, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006086902524893812 / 0.7521687774423463 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 306, 306] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.2659138241871622e+38 / 1.5956254490885013e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 306] | torch.int64 → int64 | 0.0 / 305.0 / 152.5 / 88.33411949335697 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 306, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7958170518376468 / 0.8809086742441157 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 306, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12029854664894801 / 0.6210293197906489 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006086902524893812 / 0.7521687774423463 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 306, 4096] | torch.bfloat16 → float32 | -9.5 / 12.8125 / 0.019182684433319223 / 1.022044711594749 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006086902524893812 / 0.7521687774423463 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 306, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.02128933477245904 / 5.812849692971427 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006086902524893812 / 0.7521687774423463 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 306, 512] | torch.bfloat16 → float32 | -7.375 / 7.71875 / -0.015992639890683242 / 1.17116022555435 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 306, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / -0.005939034079444296 / 0.5432505552483167 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 306, 2880] | torch.bfloat16 → float32 | -38.25 / 56.25 / 0.027972944006932947 / 1.1859362507683389 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -38.25 / 56.25 / 0.027972944006932947 / 1.1859362507683389 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 306, 306] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0013620179826733774 / 0.024016754301750407 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -87.5 / 71.0 / 0.015767049565965394 / 3.032743926296034 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 306, 2880] | torch.bfloat16 → float32 | -7.25 / 3.8125 / 0.0002846093912600129 / 0.3236859999727625 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -7.25 / 3.8125 / 0.0002846093912600129 / 0.3236859999727625 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [306, 2880] | torch.bfloat16 → float32 | -7.25 / 3.8125 / 0.0002846093912600129 / 0.3236859999727625 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [306, 2880] | torch.bfloat16 → float32 | -50.0 / 93.5 / 0.017541310256489095 / 0.8754364267181465 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -50.0 / 93.5 / 0.017541310256489095 / 0.8754364267181465 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [306, 32] | torch.bfloat16 → float32 | -5.0625 / 3.4375 / -0.10008861816007328 / 1.0604697764488173 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 306, 2880] | torch.bfloat16 → float32 | -89.0 / 107.0 / 0.03330355111723284 / 3.217850835322725 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.5020684141825313 / 48.937038914208976 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 306, 306] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6892272446433307e+38 / 1.6947566448467322e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 306, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7958170518376468 / 0.8809086742441157 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 306, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12029854664894801 / 0.6210293197906489 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 306] | torch.int64 → int64 | 0.0 / 305.0 / 152.5 / 88.33411949335697 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.5020684141825313 / 48.937038914208976 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 306, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06701203366916034 / 3.167288899149805 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 306, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06701203366916034 / 3.167288899149805 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 306, 306] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6892272446433307e+38 / 1.6947566448467322e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 306] | torch.int64 → int64 | 0.0 / 305.0 / 152.5 / 88.33411949335697 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 306, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7958170518376468 / 0.8809086742441157 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 306, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12029854664894801 / 0.6210293197906489 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06701203366916034 / 3.167288899149805 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 306, 4096] | torch.bfloat16 → float32 | -11.25 / 13.3125 / 0.03656867085370393 / 1.3348977616872595 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06701203366916034 / 3.167288899149805 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 306, 512] | torch.bfloat16 → float32 | -40.5 / 49.25 / 0.08207472266471075 / 3.7854636494309304 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06701203366916034 / 3.167288899149805 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 306, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.027921823115130653 / 2.5216305154438454 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 306, 4096] | torch.bfloat16 → float32 | -11.75 / 12.1875 / -0.024428788581374292 / 1.4615085040894469 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 306, 2880] | torch.bfloat16 → float32 | -464.0 / 498.0 / -0.02171094373569228 / 6.414932192344873 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -464.0 / 498.0 / -0.02171094373569228 / 6.414932192344873 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 306, 306] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0027875559056371123 / 0.01706299189983625 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -41216.0 / 724.0 / 0.48040749910696745 / 48.22233436162931 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 306, 2880] | torch.bfloat16 → float32 | -78.5 / 6.03125 / 0.010459218163934511 / 0.783874438444039 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -78.5 / 6.03125 / 0.010459218163934511 / 0.783874438444039 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [306, 2880] | torch.bfloat16 → float32 | -78.5 / 6.03125 / 0.010459218163934511 / 0.783874438444039 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [306, 2880] | torch.bfloat16 → float32 | -532.0 / 444.0 / 0.1317206378942308 / 9.183099455641306 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -532.0 / 444.0 / 0.1317206378942308 / 9.183099455641306 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [306, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.1514214425305136 / 0.7455849012947644 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 306, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.6121100805943308 / 50.68835403762196 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.5144271182944657 / 407.28124028289335 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 306, 306] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6892272446433307e+38 / 1.6947566448467322e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 306, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7958170518376468 / 0.8809086742441157 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 306, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12029854664894801 / 0.6210293197906489 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 306] | torch.int64 → int64 | 0.0 / 305.0 / 152.5 / 88.33411949335697 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.5144271182944657 / 407.28124028289335 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 306, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.00953176333166567 / 1.7553902740835126 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 306, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.00953176333166567 / 1.7553902740835126 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 306, 306] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6892272446433307e+38 / 1.6947566448467322e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 306] | torch.int64 → int64 | 0.0 / 305.0 / 152.5 / 88.33411949335697 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 306, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7958170518376468 / 0.8809086742441157 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 306, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12029854664894801 / 0.6210293197906489 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.00953176333166567 / 1.7553902740835126 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 306, 4096] | torch.bfloat16 → float32 | -20.375 / 24.25 / 0.03099700907053678 / 1.632411817931577 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.00953176333166567 / 1.7553902740835126 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 306, 512] | torch.bfloat16 → float32 | -88.5 / 65.5 / -0.07589046932221238 / 5.149529980759489 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.00953176333166567 / 1.7553902740835126 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 306, 512] | torch.bfloat16 → float32 | -26.25 / 24.375 / 0.006226091408262066 / 3.1403501955750253 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 306, 4096] | torch.bfloat16 → float32 | -23.0 / 12.9375 / -0.003922281230295673 / 1.1567643564826664 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 306, 2880] | torch.bfloat16 → float32 | -6272.0 / 6624.0 / 2.836712565855782 / 169.02540517357554 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -6272.0 / 6624.0 / 2.836712565855782 / 169.02540517357554 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 306, 306] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0016750382247432845 / 0.012132399626099017 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -11328.0 / 11392.0 / 1.3211393950551682 / 379.06676772304047 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 306, 2880] | torch.bfloat16 → float32 | -48.5 / 20.75 / -0.015143431334491864 / 1.1949182573343922 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -48.5 / 20.75 / -0.015143431334491864 / 1.1949182573343922 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [306, 2880] | torch.bfloat16 → float32 | -48.5 / 20.75 / -0.015143431334491864 / 1.1949182573343922 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [306, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.5898406633364608 / 143.47672473391063 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 306, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.5898406633364608 / 143.47672473391063 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [306, 32] | torch.bfloat16 → float32 | -7.1875 / 4.1875 / 0.23034181859758165 / 2.332137456459701 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 306, 2880] | torch.bfloat16 → float32 | -10816.0 / 10944.0 / -0.2690055498110703 / 417.92427975476005 | [NPY](tensors/0000116.npy) |

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
