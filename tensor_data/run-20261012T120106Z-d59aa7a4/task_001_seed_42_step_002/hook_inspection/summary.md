# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.009419712769729947 / 2.828938285190086 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 255, 255] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.1118044624797763e+38 / 1.6426531666140518e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 255, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8182444488300996 / 0.8629355353842294 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 255, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11400633055657404 / 0.6182551235517021 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 255] | torch.int64 → int64 | 0.0 / 254.0 / 127.0 / 73.6115932898254 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.009419712769729947 / 2.828938285190086 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 255, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.005242976132102619 / 0.7583613861644031 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 255, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.005242976132102619 / 0.7583613861644031 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 255, 255] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.1118044624797763e+38 / 1.6426531666140518e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 255] | torch.int64 → int64 | 0.0 / 254.0 / 127.0 / 73.6115932898254 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 255, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8182444488300996 / 0.8629355353842294 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 255, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11400633055657404 / 0.6182551235517021 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.005242976132102619 / 0.7583613861644031 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 255, 4096] | torch.bfloat16 → float32 | -9.5 / 12.8125 / 0.02146070173234786 / 1.0340701134458914 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.005242976132102619 / 0.7583613861644031 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 255, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.023181033718819716 / 5.789086258275197 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.005242976132102619 / 0.7583613861644031 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 255, 512] | torch.bfloat16 → float32 | -7.375 / 9.0 / -0.014693966829309277 / 1.2041354742658075 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 255, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / -0.006018066019529426 / 0.5498886851206733 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 255, 2880] | torch.bfloat16 → float32 | -38.0 / 56.25 / 0.028810906778789714 / 1.17750155986675 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -38.0 / 56.25 / 0.028810906778789714 / 1.17750155986675 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 255, 255] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0015597869448941964 / 0.026048313094279067 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -87.5 / 71.5 / 0.019395656959034 / 2.9847144379881816 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 255, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0009953170412571083 / 0.3369325241368563 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0009953170412571083 / 0.3369325241368563 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [255, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0009953170412571083 / 0.3369325241368563 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [255, 2880] | torch.bfloat16 → float32 | -49.75 / 92.5 / 0.019749055476879503 / 0.9212796027273762 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -49.75 / 92.5 / 0.019749055476879503 / 0.9212796027273762 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [255, 32] | torch.bfloat16 → float32 | -5.03125 / 3.4375 / -0.10329439499798942 / 1.027566091252422 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 255, 2880] | torch.bfloat16 → float32 | -89.0 / 106.0 / 0.03912650701526983 / 3.2353246297127054 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.5065551214280472 / 53.09383749138942 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 255, 255] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6881195546468432e+38 / 1.6947526629286475e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 255, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8182444488300996 / 0.8629355353842294 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 255, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11400633055657404 / 0.6182551235517021 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 255] | torch.int64 → int64 | 0.0 / 254.0 / 127.0 / 73.6115932898254 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.5065551214280472 / 53.09383749138942 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 255, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06463043871398585 / 3.1727106185319607 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 255, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06463043871398585 / 3.1727106185319607 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 255, 255] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6881195546468432e+38 / 1.6947526629286475e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 255] | torch.int64 → int64 | 0.0 / 254.0 / 127.0 / 73.6115932898254 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 255, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8182444488300996 / 0.8629355353842294 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 255, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11400633055657404 / 0.6182551235517021 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06463043871398585 / 3.1727106185319607 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 255, 4096] | torch.bfloat16 → float32 | -11.3125 / 13.3125 / 0.03863337487769148 / 1.3216796125876455 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06463043871398585 / 3.1727106185319607 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 255, 512] | torch.bfloat16 → float32 | -40.75 / 47.75 / 0.0754166081502084 / 3.677246184391991 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06463043871398585 / 3.1727106185319607 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 255, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.042490927728952146 / 2.455925474278855 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 255, 4096] | torch.bfloat16 → float32 | -11.6875 / 11.1875 / -0.03171052050887845 / 1.3887789401608452 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 255, 2880] | torch.bfloat16 → float32 | -472.0 / 502.0 / -0.04314590760277918 / 6.692699052813419 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -472.0 / 502.0 / -0.04314590760277918 / 6.692699052813419 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 255, 255] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0032483183532534634 / 0.019288540867110827 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -41216.0 / 696.0 / 0.46339622202522096 / 52.24860351671936 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 255, 2880] | torch.bfloat16 → float32 | -78.5 / 6.0625 / 0.010255791538299624 / 0.7805676259669901 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -78.5 / 6.0625 / 0.010255791538299624 / 0.7805676259669901 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [255, 2880] | torch.bfloat16 → float32 | -78.5 / 6.0625 / 0.010255791538299624 / 0.7805676259669901 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [255, 2880] | torch.bfloat16 → float32 | -492.0 / 386.0 / 0.1152677306422481 / 9.25057891235332 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -492.0 / 386.0 / 0.1152677306422481 / 9.25057891235332 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [255, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.1548952401853075 / 0.7672985430309204 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 255, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5787607227067803 / 54.5942461807216 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.6441952647622635 / 422.5973368338377 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 255, 255] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6881195546468432e+38 / 1.6947526629286475e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 255, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8182444488300996 / 0.8629355353842294 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 255, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11400633055657404 / 0.6182551235517021 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 255] | torch.int64 → int64 | 0.0 / 254.0 / 127.0 / 73.6115932898254 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.6441952647622635 / 422.5973368338377 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 255, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.008721534363714438 / 1.7574563212815932 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 255, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.008721534363714438 / 1.7574563212815932 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 255, 255] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6881195546468432e+38 / 1.6947526629286475e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 255] | torch.int64 → int64 | 0.0 / 254.0 / 127.0 / 73.6115932898254 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 255, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8182444488300996 / 0.8629355353842294 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 255, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11400633055657404 / 0.6182551235517021 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.008721534363714438 / 1.7574563212815932 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 255, 4096] | torch.bfloat16 → float32 | -18.625 / 24.25 / 0.032332393370405256 / 1.6182562241550493 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.008721534363714438 / 1.7574563212815932 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 255, 512] | torch.bfloat16 → float32 | -83.0 / 62.25 / -0.06928821883949579 / 4.982492970446611 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.008721534363714438 / 1.7574563212815932 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 255, 512] | torch.bfloat16 → float32 | -27.625 / 24.0 / -0.00614230749653835 / 3.219003961694343 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 255, 4096] | torch.bfloat16 → float32 | -22.625 / 13.0 / -0.006289987788113649 / 1.125122728622314 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 255, 2880] | torch.bfloat16 → float32 | -6016.0 / 6272.0 / 2.847839256604253 / 170.05876316139825 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -6016.0 / 6272.0 / 2.847839256604253 / 170.05876316139825 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 255, 255] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0018043554152402238 / 0.013429774700820723 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -11328.0 / 11200.0 / 1.2035998970646744 / 383.9371393193113 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 255, 2880] | torch.bfloat16 → float32 | -51.0 / 21.625 / -0.015047800126678284 / 1.193896962008526 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -51.0 / 21.625 / -0.015047800126678284 / 1.193896962008526 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [255, 2880] | torch.bfloat16 → float32 | -51.0 / 21.625 / -0.015047800126678284 / 1.193896962008526 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [255, 2880] | torch.bfloat16 → float32 | -4768.0 / 4672.0 / -1.5313486512294263 / 149.667722473334 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 255, 2880] | torch.bfloat16 → float32 | -4768.0 / 4672.0 / -1.5313486512294263 / 149.667722473334 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [255, 32] | torch.bfloat16 → float32 | -7.65625 / 4.59375 / 0.21171210700390386 / 2.28348533816998 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 255, 2880] | torch.bfloat16 → float32 | -10752.0 / 10880.0 / -0.32692529084116284 / 423.3062207165728 | [NPY](tensors/0000116.npy) |

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
