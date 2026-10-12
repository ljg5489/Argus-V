# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.008014511134254398 / 2.7930702656026978 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 385, 385] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4484890837667713e+38 / 1.5179366957624288e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 385, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.783022167775538 / 0.8866473259384456 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 385, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10869839949179562 / 0.6312119036011952 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 385] | torch.int64 → int64 | 0.0 / 384.0 / 192.0 / 111.13955191559843 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.008014511134254398 / 2.7930702656026978 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 385, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0044954683579851214 / 0.7542217226175194 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 385, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0044954683579851214 / 0.7542217226175194 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 385, 385] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4484890837667713e+38 / 1.5179366957624288e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 385] | torch.int64 → int64 | 0.0 / 384.0 / 192.0 / 111.13955191559843 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 385, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.783022167775538 / 0.8866473259384456 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 385, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10869839949179562 / 0.6312119036011952 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0044954683579851214 / 0.7542217226175194 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 385, 4096] | torch.bfloat16 → float32 | -10.25 / 12.8125 / 0.017810125862680642 / 1.0383914610792002 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0044954683579851214 / 0.7542217226175194 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 385, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.0182508174639933 / 5.788280380908394 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0044954683579851214 / 0.7542217226175194 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 385, 512] | torch.bfloat16 → float32 | -8.125 / 8.5 / -0.013837827605273962 / 1.2135574417811428 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 385, 4096] | torch.bfloat16 → float32 | -8.125 / 8.375 / -0.005784936326462637 / 0.5596374138331391 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 385, 2880] | torch.bfloat16 → float32 | -39.25 / 57.0 / 0.02907390570535471 / 1.2031040409967428 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -39.25 / 57.0 / 0.02907390570535471 / 1.2031040409967428 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 385, 385] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0010363701622502748 / 0.02121905859378473 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -87.5 / 71.5 / 0.021055506174096468 / 2.9842759374334364 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 385, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.765625 / 0.0007597313663273147 / 0.3384966052072857 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.765625 / 0.0007597313663273147 / 0.3384966052072857 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [385, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.765625 / 0.0007597313663273147 / 0.3384966052072857 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [385, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.018195114115744957 / 0.9027213377195761 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.018195114115744957 / 0.9027213377195761 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [385, 32] | torch.bfloat16 → float32 | -5.65625 / 3.4375 / -0.10190939717478566 / 1.0197887525196407 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 385, 2880] | torch.bfloat16 → float32 | -89.5 / 105.5 / 0.039249587117507506 / 3.2334432631890815 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.534496329171317 / 44.87641206346559 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 385, 385] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6903637058085579e+38 / 1.6947599777475318e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 385, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.783022167775538 / 0.8866473259384456 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 385, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10869839949179562 / 0.6312119036011952 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 385] | torch.int64 → int64 | 0.0 / 384.0 / 192.0 / 111.13955191559843 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.534496329171317 / 44.87641206346559 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 385, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06782792969334005 / 3.202166144933063 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 385, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06782792969334005 / 3.202166144933063 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 385, 385] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6903637058085579e+38 / 1.6947599777475318e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 385] | torch.int64 → int64 | 0.0 / 384.0 / 192.0 / 111.13955191559843 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 385, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.783022167775538 / 0.8866473259384456 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 385, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10869839949179562 / 0.6312119036011952 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06782792969334005 / 3.202166144933063 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 385, 4096] | torch.bfloat16 → float32 | -11.5 / 13.3125 / 0.03693961517058703 / 1.329957450595269 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06782792969334005 / 3.202166144933063 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 385, 512] | torch.bfloat16 → float32 | -38.25 / 47.25 / 0.07413846978512532 / 3.7518672373567314 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06782792969334005 / 3.202166144933063 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 385, 512] | torch.bfloat16 → float32 | -15.875 / 22.125 / -0.033122431804946104 / 2.4880359882217773 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 385, 4096] | torch.bfloat16 → float32 | -11.625 / 11.375 / -0.027275345563115973 / 1.4245311108416243 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 385, 2880] | torch.bfloat16 → float32 | -464.0 / 502.0 / -0.025235656368698053 / 6.379664359106236 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -464.0 / 502.0 / -0.025235656368698053 / 6.379664359106236 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 385, 385] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0022395970778061264 / 0.016245526590446764 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -41216.0 / 700.0 / 0.5092114489763158 / 44.08205265516772 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 385, 2880] | torch.bfloat16 → float32 | -78.5 / 9.4375 / 0.010707645970537806 / 0.7781917336973874 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -78.5 / 9.4375 / 0.010707645970537806 / 0.7781917336973874 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [385, 2880] | torch.bfloat16 → float32 | -78.5 / 9.4375 / 0.010707645970537806 / 0.7781917336973874 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [385, 2880] | torch.bfloat16 → float32 | -504.0 / 402.0 / 0.1196786076578743 / 9.250571126041628 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -504.0 / 402.0 / 0.1196786076578743 / 9.250571126041628 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [385, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.15266263020503057 / 0.7581005910484687 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 385, 2880] | torch.bfloat16 → float32 | -41216.0 / 848.0 / 0.6288635949138955 / 46.85198893262486 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.4158809191771229 / 409.6935649752671 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 385, 385] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6903637058085579e+38 / 1.6947599777475318e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 385, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.783022167775538 / 0.8866473259384456 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 385, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10869839949179562 / 0.6312119036011952 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 385] | torch.int64 → int64 | 0.0 / 384.0 / 192.0 / 111.13955191559843 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.4158809191771229 / 409.6935649752671 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 385, 2880] | torch.bfloat16 → float32 | -53.5 / 72.0 / 0.009829728737537995 / 1.7554859501855298 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 385, 2880] | torch.bfloat16 → float32 | -53.5 / 72.0 / 0.009829728737537995 / 1.7554859501855298 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 385, 385] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6903637058085579e+38 / 1.6947599777475318e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 385] | torch.int64 → int64 | 0.0 / 384.0 / 192.0 / 111.13955191559843 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 385, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.783022167775538 / 0.8866473259384456 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 385, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10869839949179562 / 0.6312119036011952 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -53.5 / 72.0 / 0.009829728737537995 / 1.7554859501855298 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 385, 4096] | torch.bfloat16 → float32 | -20.375 / 26.5 / 0.0326136805985993 / 1.6535127661527669 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -53.5 / 72.0 / 0.009829728737537995 / 1.7554859501855298 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 385, 512] | torch.bfloat16 → float32 | -80.5 / 65.0 / -0.0583057014001367 / 4.9884644622036465 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -53.5 / 72.0 / 0.009829728737537995 / 1.7554859501855298 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 385, 512] | torch.bfloat16 → float32 | -31.875 / 24.125 / 0.01804947353802718 / 3.2016467028889544 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 385, 4096] | torch.bfloat16 → float32 | -29.75 / 12.9375 / -0.0010322402490872899 / 1.1534989720254185 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 385, 2880] | torch.bfloat16 → float32 | -6784.0 / 7040.0 / 2.5210059605231363 / 168.39334303473115 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -6784.0 / 7040.0 / 2.5210059605231363 / 168.39334303473115 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 385, 385] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0012802601908190705 / 0.011059415226311448 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -10880.0 / 11264.0 / 1.105737263623082 / 365.03509575668244 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 385, 2880] | torch.bfloat16 → float32 | -54.0 / 25.125 / -0.015010402209486967 / 1.2555899620030484 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -54.0 / 25.125 / -0.015010402209486967 / 1.2555899620030484 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [385, 2880] | torch.bfloat16 → float32 | -54.0 / 25.125 / -0.015010402209486967 / 1.2555899620030484 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [385, 2880] | torch.bfloat16 → float32 | -6080.0 / 5568.0 / -1.5954531466221227 / 148.4897260211677 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 385, 2880] | torch.bfloat16 → float32 | -6080.0 / 5568.0 / -1.5954531466221227 / 148.4897260211677 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [385, 32] | torch.bfloat16 → float32 | -8.25 / 4.59375 / 0.24977839581378095 / 2.6107413080156086 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 385, 2880] | torch.bfloat16 → float32 | -10688.0 / 10944.0 / -0.4890585208248782 / 392.76760478294665 | [NPY](tensors/0000116.npy) |

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
