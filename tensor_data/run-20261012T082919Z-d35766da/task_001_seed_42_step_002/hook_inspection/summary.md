# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.014795195941483421 / 2.85469493560359 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 273, 273] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.169956811111896e+38 / 1.6267833790929349e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 273, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.80946212548476 / 0.8694203967724968 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 273, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11820535256843775 / 0.6199495524269698 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 273] | torch.int64 → int64 | 0.0 / 272.0 / 136.0 / 78.80778303357269 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.014795195941483421 / 2.85469493560359 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 273, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0068570349384567365 / 0.7538462043428837 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 273, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0068570349384567365 / 0.7538462043428837 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 273, 273] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.169956811111896e+38 / 1.6267833790929349e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 273] | torch.int64 → int64 | 0.0 / 272.0 / 136.0 / 78.80778303357269 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 273, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.80946212548476 / 0.8694203967724968 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 273, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11820535256843775 / 0.6199495524269698 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0068570349384567365 / 0.7538462043428837 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 273, 4096] | torch.bfloat16 → float32 | -9.5625 / 12.8125 / 0.01706400179137502 / 1.0213438149674157 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0068570349384567365 / 0.7538462043428837 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 273, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.008587819316011646 / 5.813203813608543 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0068570349384567365 / 0.7538462043428837 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 273, 512] | torch.bfloat16 → float32 | -7.375 / 8.5 / -0.012878619052551605 / 1.1905552670338744 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 273, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / -0.005050829074519235 / 0.5569946357673522 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 273, 2880] | torch.bfloat16 → float32 | -39.5 / 57.75 / 0.0289074808518773 / 1.2090651452039254 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -39.5 / 57.75 / 0.0289074808518773 / 1.2090651452039254 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 273, 273] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0015176059204671192 / 0.025734892910424776 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -87.5 / 71.5 / 0.014114941286638006 / 3.028283553835194 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 273, 2880] | torch.bfloat16 → float32 | -7.25 / 3.75 / 0.0002007672327426958 / 0.32754753489395905 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -7.25 / 3.75 / 0.0002007672327426958 / 0.32754753489395905 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [273, 2880] | torch.bfloat16 → float32 | -7.25 / 3.75 / 0.0002007672327426958 / 0.32754753489395905 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [273, 2880] | torch.bfloat16 → float32 | -50.0 / 93.0 / 0.017590392261779934 / 0.8922043962690537 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -50.0 / 93.0 / 0.017590392261779934 / 0.8922043962690537 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [273, 32] | torch.bfloat16 → float32 | -5.65625 / 3.4375 / -0.09941923399984619 / 1.0304883047155284 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 273, 2880] | torch.bfloat16 → float32 | -89.0 / 106.5 / 0.03170186745038496 / 3.2454443458355096 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.528277737559659 / 51.69048521362484 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 273, 273] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6885577616784206e+38 / 1.6947543247470655e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 273, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.80946212548476 / 0.8694203967724968 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 273, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11820535256843775 / 0.6199495524269698 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 273] | torch.int64 → int64 | 0.0 / 272.0 / 136.0 / 78.80778303357269 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.528277737559659 / 51.69048521362484 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 273, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06599060582299518 / 3.2339616724813585 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 273, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06599060582299518 / 3.2339616724813585 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 273, 273] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6885577616784206e+38 / 1.6947543247470655e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 273] | torch.int64 → int64 | 0.0 / 272.0 / 136.0 / 78.80778303357269 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 273, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.80946212548476 / 0.8694203967724968 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 273, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11820535256843775 / 0.6199495524269698 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06599060582299518 / 3.2339616724813585 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 273, 4096] | torch.bfloat16 → float32 | -11.25 / 13.3125 / 0.03570664259983033 / 1.32247660546186 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06599060582299518 / 3.2339616724813585 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 273, 512] | torch.bfloat16 → float32 | -41.25 / 47.25 / 0.06416859228041145 / 3.706899026698322 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06599060582299518 / 3.2339616724813585 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 273, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.025044037527217098 / 2.459489648847415 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 273, 4096] | torch.bfloat16 → float32 | -11.75 / 11.375 / -0.0235159240411678 / 1.399885620356336 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 273, 2880] | torch.bfloat16 → float32 | -466.0 / 502.0 / -0.03575971414110297 / 6.841093060641345 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -466.0 / 502.0 / -0.03575971414110297 / 6.841093060641345 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 273, 273] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003063429113323099 / 0.02011166838779322 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -41216.0 / 720.0 / 0.49242543083504536 / 50.73562825757075 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 273, 2880] | torch.bfloat16 → float32 | -78.5 / 7.1875 / 0.011567412380574101 / 0.7860362296584149 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -78.5 / 7.1875 / 0.011567412380574101 / 0.7860362296584149 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [273, 2880] | torch.bfloat16 → float32 | -78.5 / 7.1875 / 0.011567412380574101 / 0.7860362296584149 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [273, 2880] | torch.bfloat16 → float32 | -544.0 / 456.0 / 0.11846460162695702 / 9.501891604230662 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -544.0 / 456.0 / 0.11846460162695702 / 9.501891604230662 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [273, 32] | torch.bfloat16 → float32 | -10.6875 / 2.859375 / -0.1654074550111652 / 0.812437002074077 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 273, 2880] | torch.bfloat16 → float32 | -41216.0 / 828.0 / 0.6108487922193366 / 53.24182569403957 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -1.2682889082104782 / 418.8170443351537 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 273, 273] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6885577616784206e+38 / 1.6947543247470655e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 273, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.80946212548476 / 0.8694203967724968 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 273, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11820535256843775 / 0.6199495524269698 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 273] | torch.int64 → int64 | 0.0 / 272.0 / 136.0 / 78.80778303357269 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -1.2682889082104782 / 418.8170443351537 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 273, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.010321627657043288 / 1.7614929543413322 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 273, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.010321627657043288 / 1.7614929543413322 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 273, 273] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6885577616784206e+38 / 1.6947543247470655e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 273] | torch.int64 → int64 | 0.0 / 272.0 / 136.0 / 78.80778303357269 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 273, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.80946212548476 / 0.8694203967724968 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 273, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11820535256843775 / 0.6199495524269698 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.010321627657043288 / 1.7614929543413322 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 273, 4096] | torch.bfloat16 → float32 | -19.875 / 24.75 / 0.03222988475085296 / 1.6330241834001102 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.010321627657043288 / 1.7614929543413322 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 273, 512] | torch.bfloat16 → float32 | -81.5 / 64.0 / -0.05908987965202812 / 4.909388091203153 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.010321627657043288 / 1.7614929543413322 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 273, 512] | torch.bfloat16 → float32 | -31.0 / 24.25 / 0.010914992609303512 / 3.157268335937761 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 273, 4096] | torch.bfloat16 → float32 | -28.375 / 13.625 / 0.0003399506461128682 / 1.133603323353273 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 273, 2880] | torch.bfloat16 → float32 | -6816.0 / 7104.0 / 2.3837417435551447 / 166.87945770845403 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -6816.0 / 7104.0 / 2.3837417435551447 / 166.87945770845403 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 273, 273] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0016938055438434942 / 0.01337757555642192 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -10944.0 / 11200.0 / 1.1144852485703316 / 368.1920339098753 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 273, 2880] | torch.bfloat16 → float32 | -56.25 / 24.375 / -0.015111071192179942 / 1.2449205408937247 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -56.25 / 24.375 / -0.015111071192179942 / 1.2449205408937247 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [273, 2880] | torch.bfloat16 → float32 | -56.25 / 24.375 / -0.015111071192179942 / 1.2449205408937247 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [273, 2880] | torch.bfloat16 → float32 | -6944.0 / 6464.0 / -1.497171086725492 / 154.39197784213363 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 273, 2880] | torch.bfloat16 → float32 | -6944.0 / 6464.0 / -1.497171086725492 / 154.39197784213363 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [273, 32] | torch.bfloat16 → float32 | -8.4375 / 4.375 / 0.2421505459935674 / 2.545369206868534 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 273, 2880] | torch.bfloat16 → float32 | -10816.0 / 10880.0 / -0.3833231359659583 / 405.7203379243522 | [NPY](tensors/0000116.npy) |

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
