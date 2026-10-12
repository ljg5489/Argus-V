# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.003469631152205177 / 2.769721386636214 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 264, 264] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.141411933705286e+38 / 1.6348510319893011e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 264, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8132713717041593 / 0.8668290175897085 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 264, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11761705536606093 / 0.618693978891033 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 264] | torch.int64 → int64 | 0.0 / 263.0 / 131.5 / 76.20968879786 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.003469631152205177 / 2.769721386636214 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 264, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0033324274029668966 / 0.7615760639491994 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 264, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0033324274029668966 / 0.7615760639491994 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 264, 264] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.141411933705286e+38 / 1.6348510319893011e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 264] | torch.int64 → int64 | 0.0 / 263.0 / 131.5 / 76.20968879786 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 264, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8132713717041593 / 0.8668290175897085 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 264, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11761705536606093 / 0.618693978891033 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0033324274029668966 / 0.7615760639491994 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 264, 4096] | torch.bfloat16 → float32 | -10.25 / 12.8125 / 0.02313160695643312 / 1.0497057858358283 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0033324274029668966 / 0.7615760639491994 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 264, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.02975154673737107 / 5.771912824901167 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0033324274029668966 / 0.7615760639491994 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 264, 512] | torch.bfloat16 → float32 | -8.125 / 9.0 / -0.01436376255570036 / 1.2321149663758708 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 264, 4096] | torch.bfloat16 → float32 | -8.125 / 7.71875 / -0.007101316013548012 / 0.5564446096203716 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 264, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.02956133820045965 / 1.1742211236267743 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.02956133820045965 / 1.1742211236267743 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 264, 264] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0014342558400537574 / 0.02514449207194485 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -87.5 / 70.5 / 0.02609840251869124 / 2.942095871809081 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 264, 2880] | torch.bfloat16 → float32 | -7.25 / 3.75 / 0.0013564610254859885 / 0.3496477866351446 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -7.25 / 3.75 / 0.0013564610254859885 / 0.3496477866351446 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [264, 2880] | torch.bfloat16 → float32 | -7.25 / 3.75 / 0.0013564610254859885 / 0.3496477866351446 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [264, 2880] | torch.bfloat16 → float32 | -50.0 / 93.0 / 0.020311866360105044 / 0.942291271412583 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -50.0 / 93.0 / 0.020311866360105044 / 0.942291271412583 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [264, 32] | torch.bfloat16 → float32 | -4.90625 / 3.4375 / -0.10749905037157463 / 1.0103721000954524 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 264, 2880] | torch.bfloat16 → float32 | -89.5 / 106.5 / 0.0464060679429308 / 3.2334765478654393 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.5070429539439654 / 52.31874587529033 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 264, 264] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6883461276006701e+38 / 1.6947535363112748e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 264, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8132713717041593 / 0.8668290175897085 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 264, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11761705536606093 / 0.618693978891033 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 264] | torch.int64 → int64 | 0.0 / 263.0 / 131.5 / 76.20968879786 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.5070429539439654 / 52.31874587529033 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 264, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06626268530465186 / 3.142961624487184 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 264, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06626268530465186 / 3.142961624487184 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 264, 264] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6883461276006701e+38 / 1.6947535363112748e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 264] | torch.int64 → int64 | 0.0 / 263.0 / 131.5 / 76.20968879786 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 264, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8132713717041593 / 0.8668290175897085 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 264, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11761705536606093 / 0.618693978891033 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06626268530465186 / 3.142961624487184 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 264, 4096] | torch.bfloat16 → float32 | -11.3125 / 13.3125 / 0.03662199298521569 / 1.3462913000861327 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06626268530465186 / 3.142961624487184 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 264, 512] | torch.bfloat16 → float32 | -40.0 / 44.25 / 0.06713120074886264 / 3.668864971890607 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06626268530465186 / 3.142961624487184 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 264, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.0494292550014727 / 2.4922031163720435 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 264, 4096] | torch.bfloat16 → float32 | -11.6875 / 11.375 / -0.037348807635883975 / 1.451268411817854 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 264, 2880] | torch.bfloat16 → float32 | -466.0 / 502.0 / -0.04406826573609052 / 6.641151679337854 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -466.0 / 502.0 / -0.04406826573609052 / 6.641151679337854 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 264, 264] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0031598112542843876 / 0.018643866688386287 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -41216.0 / 720.0 / 0.4629977438586328 / 51.561054079189105 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 264, 2880] | torch.bfloat16 → float32 | -78.5 / 6.0625 / 0.009598115932056056 / 0.7855695061449331 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -78.5 / 6.0625 / 0.009598115932056056 / 0.7855695061449331 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [264, 2880] | torch.bfloat16 → float32 | -78.5 / 6.0625 / 0.009598115932056056 / 0.7855695061449331 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [264, 2880] | torch.bfloat16 → float32 | -548.0 / 456.0 / 0.11284813119305505 / 9.208691161883838 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -548.0 / 456.0 / 0.11284813119305505 / 9.208691161883838 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [264, 32] | torch.bfloat16 → float32 | -10.6875 / 2.859375 / -0.15450452674518933 / 0.7601013646014904 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 264, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.575881395115194 / 53.93016117083187 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -2.0213804196829748 / 418.2814108579596 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 264, 264] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6883461276006701e+38 / 1.6947535363112748e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 264, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8132713717041593 / 0.8668290175897085 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 264, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11761705536606093 / 0.618693978891033 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 264] | torch.int64 → int64 | 0.0 / 263.0 / 131.5 / 76.20968879786 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -2.0213804196829748 / 418.2814108579596 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 264, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.007954353903128644 / 1.7587610121796569 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 264, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.007954353903128644 / 1.7587610121796569 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 264, 264] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6883461276006701e+38 / 1.6947535363112748e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 264] | torch.int64 → int64 | 0.0 / 263.0 / 131.5 / 76.20968879786 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 264, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8132713717041593 / 0.8668290175897085 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 264, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11761705536606093 / 0.618693978891033 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.007954353903128644 / 1.7587610121796569 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 264, 4096] | torch.bfloat16 → float32 | -18.625 / 24.125 / 0.030916789066657548 / 1.6488327518718497 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.007954353903128644 / 1.7587610121796569 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 264, 512] | torch.bfloat16 → float32 | -84.0 / 57.5 / -0.08132555329057416 / 5.002291261464704 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.007954353903128644 / 1.7587610121796569 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 264, 512] | torch.bfloat16 → float32 | -25.5 / 24.625 / 0.016415785095005325 / 3.2305554419211027 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 264, 4096] | torch.bfloat16 → float32 | -23.75 / 12.9375 / 0.0008066262747936912 / 1.1273754695317877 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 264, 2880] | torch.bfloat16 → float32 | -6240.0 / 6528.0 / 2.594585293875098 / 164.35742968965243 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -6240.0 / 6528.0 / 2.594585293875098 / 164.35742968965243 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 264, 264] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.001794218248419141 / 0.012874466473793962 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -10560.0 / 11200.0 / 0.5722638602208608 / 366.5437213096134 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 264, 2880] | torch.bfloat16 → float32 | -49.25 / 24.625 / -0.01644771405643084 / 1.218184947815402 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -49.25 / 24.625 / -0.01644771405643084 / 1.218184947815402 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [264, 2880] | torch.bfloat16 → float32 | -49.25 / 24.625 / -0.01644771405643084 / 1.218184947815402 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [264, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.5659792103650996 / 150.31207272221314 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 264, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.5659792103650996 / 150.31207272221314 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [264, 32] | torch.bfloat16 → float32 | -7.5625 / 4.21875 / 0.23617391694675793 / 2.507695111433198 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 264, 2880] | torch.bfloat16 → float32 | -10816.0 / 10880.0 / -0.9956834349969421 / 411.12445189825246 | [NPY](tensors/0000116.npy) |

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
