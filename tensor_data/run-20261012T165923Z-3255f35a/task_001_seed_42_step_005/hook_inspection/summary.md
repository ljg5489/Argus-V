# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.017062409307860328 / 2.7189368529403635 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1083, 1083] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -3.0124110580251633e+38 / 1.0658524550764218e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1083, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7150825520982538 / 0.9206003184169874 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1083, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09421078571511195 / 0.6648455514504725 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 1083] | torch.int64 → int64 | 0.0 / 1082.0 / 541.0 / 312.63503749046856 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.017062409307860328 / 2.7189368529403635 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 1083, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007368780492166768 / 0.7618542648365257 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1083, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007368780492166768 / 0.7618542648365257 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1083, 1083] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -3.0124110580251633e+38 / 1.0658524550764218e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1083] | torch.int64 → int64 | 0.0 / 1082.0 / 541.0 / 312.63503749046856 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1083, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7150825520982538 / 0.9206003184169874 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1083, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09421078571511195 / 0.6648455514504725 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007368780492166768 / 0.7618542648365257 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 1083, 4096] | torch.bfloat16 → float32 | -9.5 / 14.0 / 0.018499138045963506 / 1.0236632893449427 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007368780492166768 / 0.7618542648365257 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 1083, 512] | torch.bfloat16 → float32 | -63.75 / 67.5 / 0.018869779064962407 / 5.738126141211335 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007368780492166768 / 0.7618542648365257 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 1083, 512] | torch.bfloat16 → float32 | -7.78125 / 9.0 / -0.01388051356545831 / 1.2113396899564686 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1083, 4096] | torch.bfloat16 → float32 | -7.03125 / 6.625 / -0.006426285375325808 / 0.5552126764269245 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 1083, 2880] | torch.bfloat16 → float32 | -50.75 / 58.0 / 0.027835331354454356 / 1.2381740316573018 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -50.75 / 58.0 / 0.027835331354454356 / 1.2381740316573018 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 1083, 1083] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0003711178100309576 / 0.012319312298409563 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -90.5 / 71.0 / 0.010776158325000335 / 2.975687277915266 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 1083, 2880] | torch.bfloat16 → float32 | -6.59375 / 3.828125 / 0.0014508090845264388 / 0.33772560908512556 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -6.59375 / 3.828125 / 0.0014508090845264388 / 0.33772560908512556 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [1083, 2880] | torch.bfloat16 → float32 | -6.59375 / 3.828125 / 0.0014508090845264388 / 0.33772560908512556 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [1083, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.017016034500424125 / 0.8423597892896747 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.017016034500424125 / 0.8423597892896747 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [1083, 32] | torch.bfloat16 → float32 | -5.21875 / 3.84375 / -0.11288226542380378 / 0.973507990798974 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 1083, 2880] | torch.bfloat16 → float32 | -88.5 / 156.0 / 0.027790942296769497 / 3.2512206013571876 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -41728.0 / 1088.0 / 0.44282034215186455 / 30.910024813857724 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1083, 1083] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6932008140213118e+38 / 1.694764972150727e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1083, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7150825520982538 / 0.9206003184169874 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1083, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09421078571511195 / 0.6648455514504725 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 1083] | torch.int64 → int64 | 0.0 / 1082.0 / 541.0 / 312.63503749046856 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -41728.0 / 1088.0 / 0.44282034215186455 / 30.910024813857724 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 1083, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.061339197316157015 / 3.1036039761484213 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1083, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.061339197316157015 / 3.1036039761484213 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1083, 1083] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6932008140213118e+38 / 1.694764972150727e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1083] | torch.int64 → int64 | 0.0 / 1082.0 / 541.0 / 312.63503749046856 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1083, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7150825520982538 / 0.9206003184169874 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1083, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09421078571511195 / 0.6648455514504725 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.061339197316157015 / 3.1036039761484213 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 1083, 4096] | torch.bfloat16 → float32 | -13.0625 / 14.8125 / 0.039898269714257834 / 1.3471212096687524 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.061339197316157015 / 3.1036039761484213 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 1083, 512] | torch.bfloat16 → float32 | -45.25 / 51.75 / 0.0991876375722692 / 3.8502287474822294 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.061339197316157015 / 3.1036039761484213 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 1083, 512] | torch.bfloat16 → float32 | -16.0 / 22.25 / -0.01535432613717043 / 2.46473775498954 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1083, 4096] | torch.bfloat16 → float32 | -11.375 / 13.3125 / -0.010060762907447297 / 1.4301403315425454 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 1083, 2880] | torch.bfloat16 → float32 | -486.0 / 440.0 / 0.011747881183086395 / 5.2016689601599895 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -486.0 / 440.0 / 0.011747881183086395 / 5.2016689601599895 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 1083, 1083] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0008305425716395373 / 0.008510300888167484 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -41728.0 / 640.0 / 0.45458821630516427 / 30.829328645827342 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 1083, 2880] | torch.bfloat16 → float32 | -78.5 / 7.71875 / 0.008853139167521966 / 0.7481436190778394 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -78.5 / 7.71875 / 0.008853139167521966 / 0.7481436190778394 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [1083, 2880] | torch.bfloat16 → float32 | -78.5 / 7.71875 / 0.008853139167521966 / 0.7481436190778394 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [1083, 2880] | torch.bfloat16 → float32 | -444.0 / 380.0 / 0.08691049032520978 / 7.4961570601346414 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -444.0 / 380.0 / 0.08691049032520978 / 7.4961570601346414 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [1083, 32] | torch.bfloat16 → float32 | -10.6875 / 4.1875 / -0.1500540642637075 / 0.7312928640750348 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 1083, 2880] | torch.bfloat16 → float32 | -41728.0 / 864.0 / 0.5415321046197744 / 33.728167441758 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -12672.0 / 14208.0 / -1.202902077655004 / 400.5808979436339 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1083, 1083] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6932008140213118e+38 / 1.694764972150727e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1083, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7150825520982538 / 0.9206003184169874 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1083, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09421078571511195 / 0.6648455514504725 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 1083] | torch.int64 → int64 | 0.0 / 1082.0 / 541.0 / 312.63503749046856 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -12672.0 / 14208.0 / -1.202902077655004 / 400.5808979436339 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 1083, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009735548406123897 / 1.7540684211283586 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1083, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009735548406123897 / 1.7540684211283586 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1083, 1083] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6932008140213118e+38 / 1.694764972150727e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1083] | torch.int64 → int64 | 0.0 / 1082.0 / 541.0 / 312.63503749046856 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1083, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7150825520982538 / 0.9206003184169874 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1083, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09421078571511195 / 0.6648455514504725 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009735548406123897 / 1.7540684211283586 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 1083, 4096] | torch.bfloat16 → float32 | -20.125 / 25.125 / 0.03216144619343988 / 1.6667890243702637 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009735548406123897 / 1.7540684211283586 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 1083, 512] | torch.bfloat16 → float32 | -92.0 / 67.0 / -0.06438138633852032 / 5.275513321089276 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009735548406123897 / 1.7540684211283586 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 1083, 512] | torch.bfloat16 → float32 | -41.75 / 23.25 / -0.007012449779688783 / 3.3625590915450165 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1083, 4096] | torch.bfloat16 → float32 | -31.75 / 17.375 / -0.0018909107068625505 / 1.275138192725051 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 1083, 2880] | torch.bfloat16 → float32 | -7968.0 / 8512.0 / 2.848656921686301 / 159.0286979071613 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -7968.0 / 8512.0 / 2.848656921686301 / 159.0286979071613 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 1083, 1083] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0005146999194595569 / 0.00687564079789059 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -11520.0 / 11328.0 / 1.6455633471657145 / 383.72723970094114 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 1083, 2880] | torch.bfloat16 → float32 | -50.25 / 22.625 / -0.01408567218219083 / 1.2693560351353947 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -50.25 / 22.625 / -0.01408567218219083 / 1.2693560351353947 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [1083, 2880] | torch.bfloat16 → float32 | -50.25 / 22.625 / -0.01408567218219083 / 1.2693560351353947 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [1083, 2880] | torch.bfloat16 → float32 | -6656.0 / 6464.0 / -1.5076872992248944 / 158.3114933906061 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 1083, 2880] | torch.bfloat16 → float32 | -6656.0 / 6464.0 / -1.5076872992248944 / 158.3114933906061 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [1083, 32] | torch.bfloat16 → float32 | -8.375 / 5.0 / 0.2621750745746898 / 2.6662562573923094 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 1083, 2880] | torch.bfloat16 → float32 | -11776.0 / 11968.0 / 0.13752304269703178 / 392.1545214730021 | [NPY](tensors/0000116.npy) |

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
