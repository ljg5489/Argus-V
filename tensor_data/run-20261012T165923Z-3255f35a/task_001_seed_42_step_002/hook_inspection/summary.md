# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.015381895724972087 / 2.74510660687576 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 574, 574] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.7172956600959904e+38 / 1.3515410572364518e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 574, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.746566295831461 / 0.9090294216729291 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 574, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10191277785213317 / 0.6446124038386847 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 574] | torch.int64 → int64 | 0.0 / 573.0 / 286.5 / 165.6992757980553 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.015381895724972087 / 2.74510660687576 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 574, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007420874296940295 / 0.7644994881665944 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 574, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007420874296940295 / 0.7644994881665944 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 574, 574] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.7172956600959904e+38 / 1.3515410572364518e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 574] | torch.int64 → int64 | 0.0 / 573.0 / 286.5 / 165.6992757980553 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 574, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.746566295831461 / 0.9090294216729291 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 574, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10191277785213317 / 0.6446124038386847 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007420874296940295 / 0.7644994881665944 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 574, 4096] | torch.bfloat16 → float32 | -9.3125 / 12.25 / 0.02063935804021211 / 1.0176965269760336 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007420874296940295 / 0.7644994881665944 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 574, 512] | torch.bfloat16 → float32 | -63.75 / 67.5 / 0.02092629142116937 / 5.7576532655110695 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007420874296940295 / 0.7644994881665944 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 574, 512] | torch.bfloat16 → float32 | -7.78125 / 9.0 / -0.012776503338192944 / 1.1983529575182257 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 574, 4096] | torch.bfloat16 → float32 | -6.96875 / 6.46875 / -0.005308678066595826 / 0.5421104835143434 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 574, 2880] | torch.bfloat16 → float32 | -50.75 / 55.25 / 0.027219473377639136 / 1.2054218032233301 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -50.75 / 55.25 / 0.027219473377639136 / 1.2054218032233301 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 574, 574] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0006966645886104323 / 0.016835731117724132 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -89.5 / 71.0 / 0.011838208513923549 / 2.972752707472549 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 574, 2880] | torch.bfloat16 → float32 | -6.625 / 3.828125 / 0.0009079763497053952 / 0.33386865715367875 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -6.625 / 3.828125 / 0.0009079763497053952 / 0.33386865715367875 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [574, 2880] | torch.bfloat16 → float32 | -6.625 / 3.828125 / 0.0009079763497053952 / 0.33386865715367875 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [574, 2880] | torch.bfloat16 → float32 | -49.5 / 135.0 / 0.016855629932090638 / 0.8380345307987341 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -49.5 / 135.0 / 0.016855629932090638 / 0.8380345307987341 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [574, 32] | torch.bfloat16 → float32 | -5.1875 / 3.84375 / -0.11105581941504927 / 0.9955475185960122 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 574, 2880] | torch.bfloat16 → float32 | -89.0 / 156.0 / 0.02869151808405125 / 3.2371078588913393 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -41728.0 / 1096.0 / 0.45198272973864384 / 38.771416132606404 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 574, 574] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.69181314115081e+38 / 1.6947631227131238e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 574, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.746566295831461 / 0.9090294216729291 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 574, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10191277785213317 / 0.6446124038386847 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 574] | torch.int64 → int64 | 0.0 / 573.0 / 286.5 / 165.6992757980553 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -41728.0 / 1096.0 / 0.45198272973864384 / 38.771416132606404 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 574, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06026433824629681 / 3.0903781890065556 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 574, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06026433824629681 / 3.0903781890065556 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 574, 574] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.69181314115081e+38 / 1.6947631227131238e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 574] | torch.int64 → int64 | 0.0 / 573.0 / 286.5 / 165.6992757980553 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 574, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.746566295831461 / 0.9090294216729291 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 574, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10191277785213317 / 0.6446124038386847 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06026433824629681 / 3.0903781890065556 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 574, 4096] | torch.bfloat16 → float32 | -12.875 / 14.625 / 0.03949650580165871 / 1.3645710185132323 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06026433824629681 / 3.0903781890065556 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 574, 512] | torch.bfloat16 → float32 | -42.75 / 47.25 / 0.07192324738013449 / 3.6756718941178343 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06026433824629681 / 3.0903781890065556 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 574, 512] | torch.bfloat16 → float32 | -16.0 / 22.0 / -0.007027202193038732 / 2.52209768853958 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 574, 4096] | torch.bfloat16 → float32 | -11.0625 / 13.125 / -0.007309585964966428 / 1.4393225817030537 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 574, 2880] | torch.bfloat16 → float32 | -476.0 / 432.0 / -0.009499440841705604 / 5.4499142157255 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -476.0 / 432.0 / -0.009499440841705604 / 5.4499142157255 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 574, 574] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0015085052901833815 / 0.012268876662065048 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -41728.0 / 648.0 / 0.4424963236016632 / 38.37837446394321 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 574, 2880] | torch.bfloat16 → float32 | -78.5 / 7.71875 / 0.009199923568665174 / 0.758892428203923 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -78.5 / 7.71875 / 0.009199923568665174 / 0.758892428203923 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [574, 2880] | torch.bfloat16 → float32 | -78.5 / 7.71875 / 0.009199923568665174 / 0.758892428203923 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [574, 2880] | torch.bfloat16 → float32 | -444.0 / 380.0 / 0.08629096041019232 / 7.675657207349707 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -444.0 / 380.0 / 0.08629096041019232 / 7.675657207349707 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [574, 32] | torch.bfloat16 → float32 | -10.75 / 3.28125 / -0.1548857182160487 / 0.7181789916136627 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 574, 2880] | torch.bfloat16 → float32 | -41728.0 / 864.0 / 0.5287820993630958 / 40.8652213549912 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -12672.0 / 14080.0 / -0.9349534504735743 / 412.76411984064845 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 574, 574] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.69181314115081e+38 / 1.6947631227131238e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 574, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.746566295831461 / 0.9090294216729291 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 574, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10191277785213317 / 0.6446124038386847 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 574] | torch.int64 → int64 | 0.0 / 573.0 / 286.5 / 165.6992757980553 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -12672.0 / 14080.0 / -0.9349534504735743 / 412.76411984064845 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 574, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010480832147433278 / 1.7670517525630502 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 574, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010480832147433278 / 1.7670517525630502 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 574, 574] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.69181314115081e+38 / 1.6947631227131238e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 574] | torch.int64 → int64 | 0.0 / 573.0 / 286.5 / 165.6992757980553 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 574, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.746566295831461 / 0.9090294216729291 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 574, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10191277785213317 / 0.6446124038386847 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010480832147433278 / 1.7670517525630502 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 574, 4096] | torch.bfloat16 → float32 | -20.125 / 24.25 / 0.03538950622832176 / 1.6658660482429022 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010480832147433278 / 1.7670517525630502 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 574, 512] | torch.bfloat16 → float32 | -84.0 / 61.75 / -0.0893937162596583 / 4.991342118894218 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010480832147433278 / 1.7670517525630502 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 574, 512] | torch.bfloat16 → float32 | -27.75 / 22.25 / -0.017091040803729605 / 3.296722703260683 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 574, 4096] | torch.bfloat16 → float32 | -25.875 / 18.125 / -0.004242951357115938 / 1.1379789676869132 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 574, 2880] | torch.bfloat16 → float32 | -6528.0 / 6912.0 / 2.4327964084967824 / 145.89106171905135 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -6528.0 / 6912.0 / 2.4327964084967824 / 145.89106171905135 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 574, 574] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0009132153739681175 / 0.00891158747902253 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -11264.0 / 11328.0 / 1.4977432576529148 / 360.6248221982633 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 574, 2880] | torch.bfloat16 → float32 | -51.25 / 22.625 / -0.013923026010122954 / 1.2389389451384378 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -51.25 / 22.625 / -0.013923026010122954 / 1.2389389451384378 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [574, 2880] | torch.bfloat16 → float32 | -51.25 / 22.625 / -0.013923026010122954 / 1.2389389451384378 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [574, 2880] | torch.bfloat16 → float32 | -6720.0 / 6656.0 / -1.2146991474241697 / 153.896381142972 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 574, 2880] | torch.bfloat16 → float32 | -6720.0 / 6656.0 / -1.2146991474241697 / 153.896381142972 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [574, 32] | torch.bfloat16 → float32 | -8.0 / 4.5 / 0.23782796622984084 / 2.522530575421991 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 574, 2880] | torch.bfloat16 → float32 | -11904.0 / 11968.0 / 0.28297068573364303 / 394.29211361504656 | [NPY](tensors/0000116.npy) |

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
