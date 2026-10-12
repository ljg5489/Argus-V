# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.01042159666387153 / 2.8788802652284713 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 222, 222] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.9942141904621687e+38 / 1.6681011234399662e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 222, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8173356528754707 / 0.8703252823838353 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 222, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11969384281064367 / 0.6079767873552681 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 222] | torch.int64 → int64 | 0.0 / 221.0 / 110.5 / 64.0852297075283 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.01042159666387153 / 2.8788802652284713 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 222, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.005611933692906367 / 0.7564241515115085 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 222, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.005611933692906367 / 0.7564241515115085 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 222, 222] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.9942141904621687e+38 / 1.6681011234399662e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 222] | torch.int64 → int64 | 0.0 / 221.0 / 110.5 / 64.0852297075283 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 222, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8173356528754707 / 0.8703252823838353 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 222, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11969384281064367 / 0.6079767873552681 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.005611933692906367 / 0.7564241515115085 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 222, 4096] | torch.bfloat16 → float32 | -8.3125 / 12.8125 / 0.02049363173558926 / 1.0254585438756183 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.005611933692906367 / 0.7564241515115085 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 222, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.014088575501699705 / 5.833766326155449 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.005611933692906367 / 0.7564241515115085 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 222, 512] | torch.bfloat16 → float32 | -7.375 / 8.4375 / -0.016649330823539612 / 1.1880271558638698 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 222, 4096] | torch.bfloat16 → float32 | -6.9375 / 8.4375 / -0.006711269751544887 / 0.5430128547115937 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 222, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.02833299241141762 / 1.1778083689187966 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.02833299241141762 / 1.1778083689187966 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 222, 222] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0018222782636651718 / 0.028178073489895393 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -87.5 / 71.5 / 0.01791283240890479 / 3.01741037900237 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 222, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.000492507870587799 / 0.32802807041972537 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.000492507870587799 / 0.32802807041972537 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [222, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.000492507870587799 / 0.32802807041972537 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [222, 2880] | torch.bfloat16 → float32 | -49.75 / 92.5 / 0.01789946663897257 / 0.902846790375046 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -49.75 / 92.5 / 0.01789946663897257 / 0.902846790375046 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [222, 32] | torch.bfloat16 → float32 | -4.96875 / 3.4375 / -0.1022940798922702 / 1.0374788286101662 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 222, 2880] | torch.bfloat16 → float32 | -89.0 / 106.0 / 0.03579415771159324 / 3.237749596940978 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -41216.0 / 828.0 / 0.5085336562988159 / 56.3831161569137 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 222, 222] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6871316149202463e+38 / 1.6947485006653378e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 222, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8173356528754707 / 0.8703252823838353 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 222, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11969384281064367 / 0.6079767873552681 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 222] | torch.int64 → int64 | 0.0 / 221.0 / 110.5 / 64.0852297075283 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -41216.0 / 828.0 / 0.5085336562988159 / 56.3831161569137 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 222, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06520354760898364 / 3.2130568976975007 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 222, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06520354760898364 / 3.2130568976975007 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 222, 222] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6871316149202463e+38 / 1.6947485006653378e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 222] | torch.int64 → int64 | 0.0 / 221.0 / 110.5 / 64.0852297075283 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 222, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8173356528754707 / 0.8703252823838353 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 222, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11969384281064367 / 0.6079767873552681 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06520354760898364 / 3.2130568976975007 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 222, 4096] | torch.bfloat16 → float32 | -11.3125 / 13.3125 / 0.03742846649336505 / 1.3201636825412248 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06520354760898364 / 3.2130568976975007 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 222, 512] | torch.bfloat16 → float32 | -38.5 / 46.0 / 0.0608545504174791 / 3.665525135166516 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.06520354760898364 / 3.2130568976975007 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 222, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.03548720465587066 / 2.460122958654245 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 222, 4096] | torch.bfloat16 → float32 | -11.6875 / 11.5 / -0.02920169387764028 / 1.4027718706722263 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 222, 2880] | torch.bfloat16 → float32 | -466.0 / 500.0 / -0.05222161248087644 / 7.119205153886288 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -466.0 / 500.0 / -0.05222161248087644 / 7.119205153886288 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 222, 222] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0037129144627894546 / 0.021763155902372898 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -41216.0 / 696.0 / 0.45629623964861465 / 55.44655159865794 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 222, 2880] | torch.bfloat16 → float32 | -78.5 / 9.3125 / 0.010115345826165544 / 0.7915290955419174 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -78.5 / 9.3125 / 0.010115345826165544 / 0.7915290955419174 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [222, 2880] | torch.bfloat16 → float32 | -78.5 / 9.3125 / 0.010115345826165544 / 0.7915290955419174 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [222, 2880] | torch.bfloat16 → float32 | -508.0 / 406.0 / 0.13034196781801866 / 9.777789237490632 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -508.0 / 406.0 / 0.13034196781801866 / 9.777789237490632 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [222, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.15875714534037821 / 0.7859185853041784 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 222, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5866547467114331 / 57.826318691001724 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -12992.0 / 14080.0 / -1.455557551875606 / 422.9912883564802 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 222, 222] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6871316149202463e+38 / 1.6947485006653378e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 222, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8173356528754707 / 0.8703252823838353 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 222, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11969384281064367 / 0.6079767873552681 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 222] | torch.int64 → int64 | 0.0 / 221.0 / 110.5 / 64.0852297075283 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -12992.0 / 14080.0 / -1.455557551875606 / 422.9912883564802 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 222, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.00954848165354422 / 1.7603611237296917 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 222, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.00954848165354422 / 1.7603611237296917 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 222, 222] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6871316149202463e+38 / 1.6947485006653378e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 222] | torch.int64 → int64 | 0.0 / 221.0 / 110.5 / 64.0852297075283 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 222, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8173356528754707 / 0.8703252823838353 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 222, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11969384281064367 / 0.6079767873552681 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.00954848165354422 / 1.7603611237296917 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 222, 4096] | torch.bfloat16 → float32 | -18.25 / 24.25 / 0.03261606873841194 / 1.6119486376615215 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.00954848165354422 / 1.7603611237296917 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 222, 512] | torch.bfloat16 → float32 | -76.0 / 62.0 / -0.06513953592149993 / 4.916680358156925 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.00954848165354422 / 1.7603611237296917 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 222, 512] | torch.bfloat16 → float32 | -26.75 / 24.25 / 0.007047732671101888 / 3.1375523370245513 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 222, 4096] | torch.bfloat16 → float32 | -22.625 / 12.9375 / -0.004780059956677481 / 1.1265010102263067 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 222, 2880] | torch.bfloat16 → float32 | -6176.0 / 6496.0 / 2.7964640482051957 / 168.74768362789507 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -6176.0 / 6496.0 / 2.7964640482051957 / 168.74768362789507 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 222, 222] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.002070190560036154 / 0.014564970405039759 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -10880.0 / 11136.0 / 1.340571181647651 / 377.66372249232063 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 222, 2880] | torch.bfloat16 → float32 | -54.25 / 22.375 / -0.01456599619288046 / 1.192134850105383 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -54.25 / 22.375 / -0.01456599619288046 / 1.192134850105383 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [222, 2880] | torch.bfloat16 → float32 | -54.25 / 22.375 / -0.01456599619288046 / 1.192134850105383 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [222, 2880] | torch.bfloat16 → float32 | -4896.0 / 4768.0 / -1.5553760434533501 / 153.33930847343922 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 222, 2880] | torch.bfloat16 → float32 | -4896.0 / 4768.0 / -1.5553760434533501 / 153.33930847343922 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [222, 32] | torch.bfloat16 → float32 | -7.1875 / 4.0 / 0.22903856071265968 / 2.2980187206260347 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 222, 2880] | torch.bfloat16 → float32 | -10624.0 / 10816.0 / -0.21286930240787663 / 423.5273631034203 | [NPY](tensors/0000116.npy) |

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
