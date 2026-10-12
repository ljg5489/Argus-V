# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.004721636979126681 / 2.7858390100016175 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 250, 250] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.094893096064133e+38 / 1.6468542201113438e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 250, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8167760858535766 / 0.8650047391753637 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 250, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11152652447088622 / 0.617762377477986 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 250] | torch.int64 → int64 | 0.0 / 249.0 / 124.5 / 72.16820629612461 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.004721636979126681 / 2.7858390100016175 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 250, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.00392667945412298 / 0.7637886291864958 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 250, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.00392667945412298 / 0.7637886291864958 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 250, 250] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.094893096064133e+38 / 1.6468542201113438e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 250] | torch.int64 → int64 | 0.0 / 249.0 / 124.5 / 72.16820629612461 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 250, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8167760858535766 / 0.8650047391753637 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 250, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11152652447088622 / 0.617762377477986 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.00392667945412298 / 0.7637886291864958 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 250, 4096] | torch.bfloat16 → float32 | -9.3125 / 12.8125 / 0.022631005556817397 / 1.0381272232442258 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.00392667945412298 / 0.7637886291864958 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 250, 512] | torch.bfloat16 → float32 | -65.5 / 68.0 / 0.025185172080993648 / 5.773701789653396 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.00392667945412298 / 0.7637886291864958 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 250, 512] | torch.bfloat16 → float32 | -8.1875 / 9.0 / -0.013648958891630173 / 1.2182517045057388 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 250, 4096] | torch.bfloat16 → float32 | -8.1875 / 8.8125 / -0.005147212595646636 / 0.549077533881866 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 250, 2880] | torch.bfloat16 → float32 | -48.25 / 56.5 / 0.029702787813148463 / 1.1955531886963677 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -48.25 / 56.5 / 0.029702787813148463 / 1.1955531886963677 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 250, 250] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0015367869887971388 / 0.025835258446457354 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -87.5 / 70.5 / 0.024982099156247245 / 2.9665244638191393 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 250, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0017028557089467844 / 0.34314604335844134 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0017028557089467844 / 0.34314604335844134 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [250, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0017028557089467844 / 0.34314604335844134 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [250, 2880] | torch.bfloat16 → float32 | -49.75 / 92.5 / 0.019387940652834043 / 0.9011436448123108 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -49.75 / 92.5 / 0.019387940652834043 / 0.9011436448123108 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [250, 32] | torch.bfloat16 → float32 | -5.625 / 3.4375 / -0.11089896392822265 / 1.0113357334831334 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 250, 2880] | torch.bfloat16 → float32 | -89.0 / 106.0 / 0.044352935049268925 / 3.2439261774039805 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.4830101967705621 / 53.53966495168943 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 250, 250] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6879866318472646e+38 / 1.6947521364459778e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 250, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8167760858535766 / 0.8650047391753637 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 250, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11152652447088622 / 0.617762377477986 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 250] | torch.int64 → int64 | 0.0 / 249.0 / 124.5 / 72.16820629612461 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.4830101967705621 / 53.53966495168943 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 250, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.0613978539135721 / 3.2057478916536755 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 250, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.0613978539135721 / 3.2057478916536755 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 250, 250] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6879866318472646e+38 / 1.6947521364459778e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 250] | torch.int64 → int64 | 0.0 / 249.0 / 124.5 / 72.16820629612461 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 250, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8167760858535766 / 0.8650047391753637 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 250, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11152652447088622 / 0.617762377477986 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.0613978539135721 / 3.2057478916536755 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 250, 4096] | torch.bfloat16 → float32 | -11.3125 / 13.3125 / 0.041022265803985644 / 1.32629010811899 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.0613978539135721 / 3.2057478916536755 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 250, 512] | torch.bfloat16 → float32 | -39.75 / 46.75 / 0.0740017440021038 / 3.618507825389655 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.0613978539135721 / 3.2057478916536755 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 250, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.02685804748535156 / 2.4476169223853144 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 250, 4096] | torch.bfloat16 → float32 | -11.625 / 11.1875 / -0.02431331783943096 / 1.3682372125164104 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 250, 2880] | torch.bfloat16 → float32 | -470.0 / 502.0 / -0.05398191821426153 / 6.837304884798915 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -470.0 / 502.0 / -0.05398191821426153 / 6.837304884798915 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 250, 250] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003322573760448063 / 0.019776332211737576 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -41216.0 / 696.0 / 0.42904499418470593 / 52.61665598362857 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 250, 2880] | torch.bfloat16 → float32 | -78.5 / 6.28125 / 0.008874749777590236 / 0.7829307105970827 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -78.5 / 6.28125 / 0.008874749777590236 / 0.7829307105970827 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [250, 2880] | torch.bfloat16 → float32 | -78.5 / 6.28125 / 0.008874749777590236 / 0.7829307105970827 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [250, 2880] | torch.bfloat16 → float32 | -540.0 / 452.0 / 0.11588528639475502 / 9.283129683237881 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -540.0 / 452.0 / 0.11588528639475502 / 9.283129683237881 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [250, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.1602799949645996 / 0.7651757942094275 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 250, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5448677656385634 / 54.961937211161064 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -12864.0 / 14016.0 / -1.927607839287652 / 419.6227096010718 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 250, 250] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6879866318472646e+38 / 1.6947521364459778e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 250, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8167760858535766 / 0.8650047391753637 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 250, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11152652447088622 / 0.617762377477986 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 250] | torch.int64 → int64 | 0.0 / 249.0 / 124.5 / 72.16820629612461 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -12864.0 / 14016.0 / -1.927607839287652 / 419.6227096010718 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 250, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.007704044405288168 / 1.7599646030846026 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 250, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.007704044405288168 / 1.7599646030846026 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 250, 250] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6879866318472646e+38 / 1.6947521364459778e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 250] | torch.int64 → int64 | 0.0 / 249.0 / 124.5 / 72.16820629612461 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 250, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8167760858535766 / 0.8650047391753637 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 250, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11152652447088622 / 0.617762377477986 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.007704044405288168 / 1.7599646030846026 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 250, 4096] | torch.bfloat16 → float32 | -18.625 / 24.125 / 0.03225051771145082 / 1.6355082354024706 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.007704044405288168 / 1.7599646030846026 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 250, 512] | torch.bfloat16 → float32 | -87.0 / 69.0 / -0.0858036867119372 / 4.9332705997323645 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.007704044405288168 / 1.7599646030846026 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 250, 512] | torch.bfloat16 → float32 | -24.25 / 24.0 / 0.0008422006368637089 / 3.199564758544547 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 250, 4096] | torch.bfloat16 → float32 | -22.625 / 12.9375 / -0.0032041887928608045 / 1.11311245722024 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 250, 2880] | torch.bfloat16 → float32 | -5984.0 / 6208.0 / 2.600482069291671 / 162.2787695002333 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -5984.0 / 6208.0 / 2.600482069291671 / 162.2787695002333 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 250, 250] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0018013205745440921 / 0.013236195940366824 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -10496.0 / 11200.0 / 0.6716666422526041 / 359.32992110467615 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 250, 2880] | torch.bfloat16 → float32 | -47.25 / 30.625 / -0.01592384029792415 / 1.216133148225807 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -47.25 / 30.625 / -0.01592384029792415 / 1.216133148225807 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [250, 2880] | torch.bfloat16 → float32 | -47.25 / 30.625 / -0.01592384029792415 / 1.216133148225807 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [250, 2880] | torch.bfloat16 → float32 | -4768.0 / 4672.0 / -1.462948758771684 / 154.8239049667447 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 250, 2880] | torch.bfloat16 → float32 | -4768.0 / 4672.0 / -1.462948758771684 / 154.8239049667447 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [250, 32] | torch.bfloat16 → float32 | -8.125 / 4.5625 / 0.24233095932006837 / 2.5106201180394216 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 250, 2880] | torch.bfloat16 → float32 | -10688.0 / 10880.0 / -0.7899420952690972 / 416.39866492359477 | [NPY](tensors/0000116.npy) |

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
