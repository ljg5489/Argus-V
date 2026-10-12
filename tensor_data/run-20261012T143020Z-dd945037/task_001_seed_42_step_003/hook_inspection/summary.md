# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.013368750528044928 / 2.9145061477480283 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 235, 235] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.0421888259767557e+38 / 1.6587730186745368e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 235, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8151296747491715 / 0.8691277849688902 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 235, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11401846084045246 / 0.6136835714206922 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 235] | torch.int64 → int64 | 0.0 / 234.0 / 117.0 / 67.83804242458652 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.013368750528044928 / 2.9145061477480283 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 235, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.00662087279592088 / 0.7543731195517848 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 235, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.00662087279592088 / 0.7543731195517848 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 235, 235] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.0421888259767557e+38 / 1.6587730186745368e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 235] | torch.int64 → int64 | 0.0 / 234.0 / 117.0 / 67.83804242458652 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 235, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8151296747491715 / 0.8691277849688902 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 235, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11401846084045246 / 0.6136835714206922 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.00662087279592088 / 0.7543731195517848 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 235, 4096] | torch.bfloat16 → float32 | -8.25 / 12.8125 / 0.020112795481133827 / 1.018419101717025 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.00662087279592088 / 0.7543731195517848 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 235, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.0162253312608029 / 5.831671542528689 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.00662087279592088 / 0.7543731195517848 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 235, 512] | torch.bfloat16 → float32 | -7.375 / 7.71875 / -0.015023906972814112 / 1.1697196655457387 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 235, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / -0.00609667098306568 / 0.5402612904106066 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 235, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.028066186610131518 / 1.1774761841194408 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.028066186610131518 / 1.1774761841194408 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 235, 235] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0017626644969613889 / 0.02749788083657789 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -87.5 / 71.0 / 0.01469715915039076 / 3.0378479280527837 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 235, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.796875 / 0.00016034456907857396 / 0.32195174997774156 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.796875 / 0.00016034456907857396 / 0.32195174997774156 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [235, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.796875 / 0.00016034456907857396 / 0.32195174997774156 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [235, 2880] | torch.bfloat16 → float32 | -49.75 / 92.5 / 0.017513762001238817 / 0.8858331246557194 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -49.75 / 92.5 / 0.017513762001238817 / 0.8858331246557194 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [235, 32] | torch.bfloat16 → float32 | -5.0 / 3.4375 / -0.10068922651574967 / 1.0547760707408205 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 235, 2880] | torch.bfloat16 → float32 | -89.0 / 106.0 / 0.03220195562845144 / 3.227263311993595 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.4996202680799696 / 54.86693435324175 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 235, 235] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6875539257124666e+38 / 1.694750350367128e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 235, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8151296747491715 / 0.8691277849688902 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 235, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11401846084045246 / 0.6136835714206922 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 235] | torch.int64 → int64 | 0.0 / 234.0 / 117.0 / 67.83804242458652 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.4996202680799696 / 54.86693435324175 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 235, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.0664042493181378 / 3.190915247395912 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 235, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.0664042493181378 / 3.190915247395912 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 235, 235] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6875539257124666e+38 / 1.694750350367128e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 235] | torch.int64 → int64 | 0.0 / 234.0 / 117.0 / 67.83804242458652 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 235, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8151296747491715 / 0.8691277849688902 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 235, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11401846084045246 / 0.6136835714206922 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.0664042493181378 / 3.190915247395912 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 235, 4096] | torch.bfloat16 → float32 | -11.3125 / 13.3125 / 0.03554287801804442 / 1.3296459795849853 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.0664042493181378 / 3.190915247395912 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 235, 512] | torch.bfloat16 → float32 | -38.75 / 49.25 / 0.06987285720224076 / 3.710903525478611 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.0664042493181378 / 3.190915247395912 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 235, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.029424545993196202 / 2.4956392022590568 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 235, 4096] | torch.bfloat16 → float32 | -11.625 / 12.0 / -0.027442331159657808 / 1.436204586579329 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 235, 2880] | torch.bfloat16 → float32 | -472.0 / 502.0 / -0.03956773815630334 / 6.839346828185251 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -472.0 / 502.0 / -0.03956773815630334 / 6.839346828185251 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 235, 235] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0035447942918198556 / 0.020183662772111498 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -41216.0 / 696.0 / 0.4600957829676058 / 54.044983790009915 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 235, 2880] | torch.bfloat16 → float32 | -78.5 / 6.03125 / 0.010051893738294395 / 0.7895390358402987 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -78.5 / 6.03125 / 0.010051893738294395 / 0.7895390358402987 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [235, 2880] | torch.bfloat16 → float32 | -78.5 / 6.03125 / 0.010051893738294395 / 0.7895390358402987 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [235, 2880] | torch.bfloat16 → float32 | -492.0 / 384.0 / 0.12803840761207239 / 9.516164916304003 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -492.0 / 384.0 / 0.12803840761207239 / 9.516164916304003 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [235, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.15443673742578384 / 0.7698460575477306 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 235, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5881139876994681 / 56.390736942018265 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.527853186857616 / 417.4317540266124 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 235, 235] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6875539257124666e+38 / 1.694750350367128e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 235, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8151296747491715 / 0.8691277849688902 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 235, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11401846084045246 / 0.6136835714206922 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 235] | torch.int64 → int64 | 0.0 / 234.0 / 117.0 / 67.83804242458652 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.527853186857616 / 417.4317540266124 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 235, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.009420204619143871 / 1.7582964402060177 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 235, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.009420204619143871 / 1.7582964402060177 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 235, 235] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6875539257124666e+38 / 1.694750350367128e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 235] | torch.int64 → int64 | 0.0 / 234.0 / 117.0 / 67.83804242458652 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 235, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8151296747491715 / 0.8691277849688902 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 235, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11401846084045246 / 0.6136835714206922 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.009420204619143871 / 1.7582964402060177 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 235, 4096] | torch.bfloat16 → float32 | -20.375 / 24.25 / 0.031229022246461298 / 1.6113370773247435 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.009420204619143871 / 1.7582964402060177 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 235, 512] | torch.bfloat16 → float32 | -83.5 / 66.5 / -0.06923642189816592 / 5.0170627726514505 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.009420204619143871 / 1.7582964402060177 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 235, 512] | torch.bfloat16 → float32 | -26.125 / 24.5 / 0.004526533979050657 / 3.1077732859703135 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 235, 4096] | torch.bfloat16 → float32 | -23.0 / 13.0 / -0.0042444776222838945 / 1.1450220605042623 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 235, 2880] | torch.bfloat16 → float32 | -6304.0 / 6656.0 / 2.91013602353016 / 172.19613486849 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -6304.0 / 6656.0 / 2.91013602353016 / 172.19613486849 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 235, 235] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0020683232657056237 / 0.014131309986909682 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -11200.0 / 11456.0 / 1.3826467671856533 / 384.43486375058404 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 235, 2880] | torch.bfloat16 → float32 | -48.25 / 20.625 / -0.015041471639071232 / 1.1790444037929075 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -48.25 / 20.625 / -0.015041471639071232 / 1.1790444037929075 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [235, 2880] | torch.bfloat16 → float32 | -48.25 / 20.625 / -0.015041471639071232 / 1.1790444037929075 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [235, 2880] | torch.bfloat16 → float32 | -4768.0 / 4672.0 / -1.5383423533789091 / 147.8527074931127 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 235, 2880] | torch.bfloat16 → float32 | -4768.0 / 4672.0 / -1.5383423533789091 / 147.8527074931127 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [235, 32] | torch.bfloat16 → float32 | -7.15625 / 3.984375 / 0.22704757528102143 / 2.2575254425939963 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 235, 2880] | torch.bfloat16 → float32 | -10752.0 / 10880.0 / -0.15460418917608598 / 428.0896764647545 | [NPY](tensors/0000116.npy) |

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
