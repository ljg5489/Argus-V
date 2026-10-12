# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012572546625485112 / 2.7638890250948616 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 632, 632] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.7720186205319398e+38 / 1.3083412755496757e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 632, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7496074138185645 / 0.9041196964182873 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 632, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09953980505695977 / 0.6483694930655288 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 632] | torch.int64 → int64 | 0.0 / 631.0 / 315.5 / 182.44245668155207 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012572546625485112 / 2.7638890250948616 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 632, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.0066818185115430605 / 0.7621130197947918 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 632, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.0066818185115430605 / 0.7621130197947918 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 632, 632] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.7720186205319398e+38 / 1.3083412755496757e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 632] | torch.int64 → int64 | 0.0 / 631.0 / 315.5 / 182.44245668155207 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 632, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7496074138185645 / 0.9041196964182873 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 632, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09953980505695977 / 0.6483694930655288 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.0066818185115430605 / 0.7621130197947918 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 632, 4096] | torch.bfloat16 → float32 | -9.375 / 11.6875 / 0.021400477903001307 / 1.0219150090516211 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.0066818185115430605 / 0.7621130197947918 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 632, 512] | torch.bfloat16 → float32 | -63.75 / 68.0 / 0.019630854609319234 / 5.761249111998444 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.0066818185115430605 / 0.7621130197947918 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 632, 512] | torch.bfloat16 → float32 | -8.5 / 7.71875 / -0.01155141305014096 / 1.1997322669867971 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 632, 4096] | torch.bfloat16 → float32 | -8.5 / 7.46875 / -0.0050974457375831716 / 0.5460660018899424 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 632, 2880] | torch.bfloat16 → float32 | -39.25 / 53.75 / 0.02805606206683275 / 1.1980251641702493 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -39.25 / 53.75 / 0.02805606206683275 / 1.1980251641702493 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 632, 632] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0006301096509035214 / 0.01599531060798581 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -89.0 / 71.0 / 0.015486685122702529 / 2.9786550995327095 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 632, 2880] | torch.bfloat16 → float32 | -6.625 / 3.078125 / 0.0011970480390511317 / 0.3323022857656023 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -6.625 / 3.078125 / 0.0011970480390511317 / 0.3323022857656023 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [632, 2880] | torch.bfloat16 → float32 | -6.625 / 3.078125 / 0.0011970480390511317 / 0.3323022857656023 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [632, 2880] | torch.bfloat16 → float32 | -49.5 / 135.0 / 0.017007005749055504 / 0.8353505527777383 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -49.5 / 135.0 / 0.017007005749055504 / 0.8353505527777383 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [632, 32] | torch.bfloat16 → float32 | -5.09375 / 4.4375 / -0.11197959924045997 / 1.0001741975214442 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 632, 2880] | torch.bfloat16 → float32 | -85.0 / 156.0 / 0.03249542565201573 / 3.2352900174020616 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -41728.0 / 1088.0 / 0.41448117321888944 / 37.58628857984495 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 632, 632] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6920841033368029e+38 / 1.6947635731123443e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 632, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7496074138185645 / 0.9041196964182873 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 632, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09953980505695977 / 0.6483694930655288 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 632] | torch.int64 → int64 | 0.0 / 631.0 / 315.5 / 182.44245668155207 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -41728.0 / 1088.0 / 0.41448117321888944 / 37.58628857984495 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 632, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05569644219074371 / 3.1083269861522513 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 632, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05569644219074371 / 3.1083269861522513 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 632, 632] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6920841033368029e+38 / 1.6947635731123443e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 632] | torch.int64 → int64 | 0.0 / 631.0 / 315.5 / 182.44245668155207 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 632, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7496074138185645 / 0.9041196964182873 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 632, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09953980505695977 / 0.6483694930655288 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05569644219074371 / 3.1083269861522513 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 632, 4096] | torch.bfloat16 → float32 | -13.0 / 14.625 / 0.04215321704550602 / 1.3572711263334507 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05569644219074371 / 3.1083269861522513 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 632, 512] | torch.bfloat16 → float32 | -44.25 / 52.25 / 0.08031356162094118 / 3.4872563674400574 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05569644219074371 / 3.1083269861522513 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 632, 512] | torch.bfloat16 → float32 | -16.0 / 22.0 / -0.013222234421800174 / 2.535254455694622 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 632, 4096] | torch.bfloat16 → float32 | -11.6875 / 12.9375 / -0.013227230415100382 / 1.4028467706607899 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 632, 2880] | torch.bfloat16 → float32 | -474.0 / 432.0 / -0.026876205857777665 / 5.418666095803501 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -474.0 / 432.0 / -0.026876205857777665 / 5.418666095803501 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 632, 632] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0013496518186999016 / 0.011521083434345443 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -41728.0 / 640.0 / 0.3876229287786659 / 37.15032938426738 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 632, 2880] | torch.bfloat16 → float32 | -78.5 / 8.375 / 0.007514319581938475 / 0.7624408110923155 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -78.5 / 8.375 / 0.007514319581938475 / 0.7624408110923155 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [632, 2880] | torch.bfloat16 → float32 | -78.5 / 8.375 / 0.007514319581938475 / 0.7624408110923155 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [632, 2880] | torch.bfloat16 → float32 | -436.0 / 438.0 / 0.08237082608641452 / 7.861504611740801 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -436.0 / 438.0 / 0.08237082608641452 / 7.861504611740801 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [632, 32] | torch.bfloat16 → float32 | -10.75 / 2.96875 / -0.15602087823650504 / 0.7369699460721498 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 632, 2880] | torch.bfloat16 → float32 | -41728.0 / 880.0 / 0.47005298761375847 / 39.813162251497324 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -12736.0 / 14144.0 / -0.9225112432165992 / 413.0538088814939 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 632, 632] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6920841033368029e+38 / 1.6947635731123443e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 632, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7496074138185645 / 0.9041196964182873 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 632, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09953980505695977 / 0.6483694930655288 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 632] | torch.int64 → int64 | 0.0 / 631.0 / 315.5 / 182.44245668155207 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -12736.0 / 14144.0 / -0.9225112432165992 / 413.0538088814939 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 632, 2880] | torch.bfloat16 → float32 | -57.25 / 70.5 / 0.010262744650886552 / 1.7690962763046647 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 632, 2880] | torch.bfloat16 → float32 | -57.25 / 70.5 / 0.010262744650886552 / 1.7690962763046647 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 632, 632] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6920841033368029e+38 / 1.6947635731123443e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 632] | torch.int64 → int64 | 0.0 / 631.0 / 315.5 / 182.44245668155207 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 632, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7496074138185645 / 0.9041196964182873 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 632, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09953980505695977 / 0.6483694930655288 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -57.25 / 70.5 / 0.010262744650886552 / 1.7690962763046647 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 632, 4096] | torch.bfloat16 → float32 | -20.25 / 24.5 / 0.03570473113376381 / 1.6674657326072166 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -57.25 / 70.5 / 0.010262744650886552 / 1.7690962763046647 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 632, 512] | torch.bfloat16 → float32 | -83.5 / 61.0 / -0.09016363955448423 / 4.747437338623892 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -57.25 / 70.5 / 0.010262744650886552 / 1.7690962763046647 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 632, 512] | torch.bfloat16 → float32 | -22.625 / 19.875 / -0.010568295898729393 / 3.3047791863148728 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 632, 4096] | torch.bfloat16 → float32 | -21.0 / 14.3125 / -0.004486164342843414 / 1.110737021784403 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 632, 2880] | torch.bfloat16 → float32 | -5984.0 / 6048.0 / 2.35329822598185 / 138.67420058415397 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -5984.0 / 6048.0 / 2.35329822598185 / 138.67420058415397 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 632, 632] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0008170126283949386 / 0.008525280246595386 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -11200.0 / 11392.0 / 1.430486959814187 / 361.22274339010147 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 632, 2880] | torch.bfloat16 → float32 | -49.5 / 24.125 / -0.013552640556225503 / 1.211601334113506 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -49.5 / 24.125 / -0.013552640556225503 / 1.211601334113506 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [632, 2880] | torch.bfloat16 → float32 | -49.5 / 24.125 / -0.013552640556225503 / 1.211601334113506 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [632, 2880] | torch.bfloat16 → float32 | -6464.0 / 6432.0 / -1.3051321381087373 / 169.55349420242678 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 632, 2880] | torch.bfloat16 → float32 | -6464.0 / 6432.0 / -1.3051321381087373 / 169.55349420242678 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [632, 32] | torch.bfloat16 → float32 | -8.3125 / 4.40625 / 0.24467827775810339 / 2.590001437232517 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 632, 2880] | torch.bfloat16 → float32 | -11840.0 / 12096.0 / 0.12526284659126813 / 418.8494083927656 | [NPY](tensors/0000116.npy) |

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
