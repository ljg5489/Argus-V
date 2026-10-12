# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.017095922459983738 / 2.80698141969223 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 441, 441] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.54738147883029e+38 / 1.464676443521117e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 441, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7750061609847746 / 0.887814389668553 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 441, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11249321569990084 / 0.6387686808901938 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 441] | torch.int64 → int64 | 0.0 / 440.0 / 220.0 / 127.30540705982078 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.017095922459983738 / 2.80698141969223 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 441, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006950837755290677 / 0.743934067565311 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 441, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006950837755290677 / 0.743934067565311 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 441, 441] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.54738147883029e+38 / 1.464676443521117e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 441] | torch.int64 → int64 | 0.0 / 440.0 / 220.0 / 127.30540705982078 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 441, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7750061609847746 / 0.887814389668553 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 441, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11249321569990084 / 0.6387686808901938 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006950837755290677 / 0.743934067565311 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 441, 4096] | torch.bfloat16 → float32 | -9.5 / 12.8125 / 0.01854017691306057 / 1.0240568341328233 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006950837755290677 / 0.743934067565311 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 441, 512] | torch.bfloat16 → float32 | -65.5 / 69.0 / 0.006533505104676463 / 5.827945393448579 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006950837755290677 / 0.743934067565311 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 441, 512] | torch.bfloat16 → float32 | -7.375 / 8.5 / -0.008071707501292626 / 1.1786898043125558 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 441, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.75 / -0.003965620630227779 / 0.5497030856002291 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 441, 2880] | torch.bfloat16 → float32 | -41.5 / 58.75 / 0.028064111623085676 / 1.200040116538799 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -41.5 / 58.75 / 0.028064111623085676 / 1.200040116538799 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 441, 441] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0009053934935908596 / 0.01961441229763502 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -87.5 / 71.5 / 0.010964487695399625 / 3.0020479439668994 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 441, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 3.8403451994613346e-05 / 0.3229620533291572 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 3.8403451994613346e-05 / 0.3229620533291572 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [441, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 3.8403451994613346e-05 / 0.3229620533291572 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [441, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.01809677765712904 / 0.8636003210256229 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.01809677765712904 / 0.8636003210256229 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [441, 32] | torch.bfloat16 → float32 | -5.71875 / 3.4375 / -0.09504509837178686 / 1.0547430984824073 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 441, 2880] | torch.bfloat16 → float32 | -93.0 / 105.5 / 0.02906525885166765 / 3.2076304650056575 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.48656573133403763 / 42.451642701865325 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 441, 441] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909226885155053e+38 / 1.6947613374703818e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 441, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7750061609847746 / 0.887814389668553 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 441, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11249321569990084 / 0.6387686808901938 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 441] | torch.int64 → int64 | 0.0 / 440.0 / 220.0 / 127.30540705982078 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.48656573133403763 / 42.451642701865325 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 441, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06254672764226304 / 3.2238856055854628 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 441, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06254672764226304 / 3.2238856055854628 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 441, 441] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909226885155053e+38 / 1.6947613374703818e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 441] | torch.int64 → int64 | 0.0 / 440.0 / 220.0 / 127.30540705982078 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 441, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7750061609847746 / 0.887814389668553 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 441, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11249321569990084 / 0.6387686808901938 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06254672764226304 / 3.2238856055854628 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 441, 4096] | torch.bfloat16 → float32 | -11.875 / 13.3125 / 0.03857702841837419 / 1.3279546284002133 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06254672764226304 / 3.2238856055854628 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 441, 512] | torch.bfloat16 → float32 | -38.75 / 49.0 / 0.08441340721311584 / 3.783461609600926 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06254672764226304 / 3.2238856055854628 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 441, 512] | torch.bfloat16 → float32 | -15.875 / 22.125 / -0.04373096680277093 / 2.491196791898232 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 441, 4096] | torch.bfloat16 → float32 | -11.625 / 11.3125 / -0.031416887767149765 / 1.4336065588108244 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 441, 2880] | torch.bfloat16 → float32 | -464.0 / 502.0 / -0.009045006945303602 / 6.295337444135763 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -464.0 / 502.0 / -0.009045006945303602 / 6.295337444135763 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 441, 441] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.001958626284816923 / 0.015563931810075364 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -41216.0 / 700.0 / 0.4774798825274309 / 41.61798185115994 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 441, 2880] | torch.bfloat16 → float32 | -78.5 / 9.8125 / 0.010486154133934058 / 0.7832458545200917 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -78.5 / 9.8125 / 0.010486154133934058 / 0.7832458545200917 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [441, 2880] | torch.bfloat16 → float32 | -78.5 / 9.8125 / 0.010486154133934058 / 0.7832458545200917 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [441, 2880] | torch.bfloat16 → float32 | -490.0 / 390.0 / 0.1096828374447586 / 9.328166956392232 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -490.0 / 390.0 / 0.1096828374447586 / 9.328166956392232 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [441, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.17060777497670007 / 0.8226840432687528 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 441, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5871644603241959 / 44.49514843011525 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.5028298245115466 / 395.0158962940062 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 441, 441] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909226885155053e+38 / 1.6947613374703818e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 441, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7750061609847746 / 0.887814389668553 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 441, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11249321569990084 / 0.6387686808901938 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 441] | torch.int64 → int64 | 0.0 / 440.0 / 220.0 / 127.30540705982078 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.5028298245115466 / 395.0158962940062 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 441, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009919436528066088 / 1.7513466900748664 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 441, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009919436528066088 / 1.7513466900748664 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 441, 441] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909226885155053e+38 / 1.6947613374703818e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 441] | torch.int64 → int64 | 0.0 / 440.0 / 220.0 / 127.30540705982078 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 441, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7750061609847746 / 0.887814389668553 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 441, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11249321569990084 / 0.6387686808901938 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009919436528066088 / 1.7513466900748664 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 441, 4096] | torch.bfloat16 → float32 | -22.625 / 24.75 / 0.028741083029732353 / 1.6773144816729568 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009919436528066088 / 1.7513466900748664 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 441, 512] | torch.bfloat16 → float32 | -86.0 / 64.5 / -0.05852012143469291 / 5.0407279541631596 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009919436528066088 / 1.7513466900748664 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 441, 512] | torch.bfloat16 → float32 | -27.75 / 24.375 / 0.007629926376627618 / 3.124557740022755 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 441, 4096] | torch.bfloat16 → float32 | -26.25 / 12.875 / -0.0008378442399638903 / 1.1337152574473295 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 441, 2880] | torch.bfloat16 → float32 | -6432.0 / 6720.0 / 2.4486704488373823 / 160.42844330703994 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -6432.0 / 6720.0 / 2.4486704488373823 / 160.42844330703994 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 441, 441] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0011132824834276622 / 0.010347742382578469 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -10496.0 / 11264.0 / 0.9458176766393406 / 350.4790882528324 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 441, 2880] | torch.bfloat16 → float32 | -52.5 / 25.875 / -0.01566577419698704 / 1.2980303111565537 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -52.5 / 25.875 / -0.01566577419698704 / 1.2980303111565537 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [441, 2880] | torch.bfloat16 → float32 | -52.5 / 25.875 / -0.01566577419698704 / 1.2980303111565537 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [441, 2880] | torch.bfloat16 → float32 | -5824.0 / 5504.0 / -1.4889569486169678 / 145.11659759631627 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 441, 2880] | torch.bfloat16 → float32 | -5824.0 / 5504.0 / -1.4889569486169678 / 145.11659759631627 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [441, 32] | torch.bfloat16 → float32 | -8.375 / 4.75 / 0.2728391785740582 / 2.845252682659019 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 441, 2880] | torch.bfloat16 → float32 | -10688.0 / 10944.0 / -0.5428155785154772 / 380.7249875425531 | [NPY](tensors/0000116.npy) |

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
