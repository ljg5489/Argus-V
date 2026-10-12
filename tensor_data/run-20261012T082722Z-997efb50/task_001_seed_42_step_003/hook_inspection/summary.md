# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.007334225449292579 / 2.779540772643133 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.007334225449292579 / 2.779540772643133 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.004344932996620764 / 0.7558275989788132 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.004344932996620764 / 0.7558275989788132 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.004344932996620764 / 0.7558275989788132 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -10.25 / 12.8125 / 0.01792548890496366 / 1.0390347715332726 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.004344932996620764 / 0.7558275989788132 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -65.5 / 69.0 / 0.02375915249223125 / 5.770282412902776 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.004344932996620764 / 0.7558275989788132 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -8.125 / 8.5 / -0.015738108300138266 / 1.2188948290868398 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -8.125 / 7.75 / -0.006269019416445304 / 0.5599836241080393 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41.5 / 58.75 / 0.029410982298908383 / 1.2179603882707455 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41.5 / 58.75 / 0.029410982298908383 / 1.2179603882707455 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0010060948979672404 / 0.020877642031381424 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -87.5 / 71.5 / 0.02207443638525264 / 2.9810495404049493 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 0.0007146957281940261 / 0.34166587273232796 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 0.0007146957281940261 / 0.34166587273232796 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 0.0007146957281940261 / 0.34166587273232796 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.018839225969034996 / 0.9134131887698185 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.018839225969034996 / 0.9134131887698185 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -5.71875 / 3.4375 / -0.1032537774194645 / 1.0216639921912398 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -93.0 / 105.5 / 0.04091641430613361 / 3.2482748945147977 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.503709911019155 / 44.364807908694566 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.503709911019155 / 44.364807908694566 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.0650405526662091 / 3.179156979519789 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.0650405526662091 / 3.179156979519789 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.0650405526662091 / 3.179156979519789 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -11.8125 / 13.3125 / 0.03524046155651814 / 1.3338477664631876 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.0650405526662091 / 3.179156979519789 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -38.75 / 49.25 / 0.07757833692616536 / 3.782986996647276 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.0650405526662091 / 3.179156979519789 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -15.875 / 22.125 / -0.04071336590060139 / 2.4934286210836176 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -11.625 / 11.3125 / -0.031455580061585255 / 1.4357824518467397 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -464.0 / 502.0 / -0.016879438435457094 / 6.26315828239978 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -464.0 / 502.0 / -0.016879438435457094 / 6.26315828239978 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002185079256296959 / 0.01555520034491797 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 700.0 / 0.48681620947251675 / 43.615562114405805 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -78.5 / 7.40625 / 0.011239520141752713 / 0.7771169476699492 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -78.5 / 7.40625 / 0.011239520141752713 / 0.7771169476699492 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -78.5 / 7.40625 / 0.011239520141752713 / 0.7771169476699492 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -504.0 / 402.0 / 0.11640954083866545 / 9.120710893237378 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -504.0 / 402.0 / 0.11640954083866545 / 9.120710893237378 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.15218740777124332 / 0.764872474834454 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.6032201320578444 / 46.34521113784479 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.7412591449721455 / 405.16407451577606 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.7412591449721455 / 405.16407451577606 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.008652323391471902 / 1.7542450497363318 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.008652323391471902 / 1.7542450497363318 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.008652323391471902 / 1.7542450497363318 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -19.875 / 24.625 / 0.0318815278413286 / 1.6637545549260213 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.008652323391471902 / 1.7542450497363318 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -86.5 / 61.75 / -0.0631072611493483 / 5.087785186039847 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.008652323391471902 / 1.7542450497363318 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -27.875 / 24.125 / 0.02253915367801261 / 3.200494524679318 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -26.0 / 12.9375 / 0.002551975443870267 / 1.1421444771447677 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -6272.0 / 6400.0 / 2.300071610426098 / 164.55440215019473 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -6272.0 / 6400.0 / 2.300071610426098 / 164.55440215019473 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0012633987360976967 / 0.010800478411443614 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -10496.0 / 11264.0 / 0.5590979495631994 / 354.49985797239333 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.5 / 25.875 / -0.017072050410850723 / 1.280687551743766 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.5 / 25.875 / -0.017072050410850723 / 1.280687551743766 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -52.5 / 25.875 / -0.017072050410850723 / 1.280687551743766 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -5888.0 / 5536.0 / -1.647315231087171 / 146.3283428699995 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -5888.0 / 5536.0 / -1.647315231087171 / 146.3283428699995 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -8.5 / 4.96875 / 0.25666749205770373 / 2.732047378335963 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -10688.0 / 10944.0 / -1.0882537730199544 / 380.9975615452588 | [NPY](tensors/0000116.npy) |

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
