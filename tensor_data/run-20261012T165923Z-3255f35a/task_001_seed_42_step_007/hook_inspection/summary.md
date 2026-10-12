# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.016401424710467693 / 2.7044479911769903 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1285, 1285] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -3.0685817840964194e+38 / 9.92401185001271e+37 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1285, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7036832386620546 / 0.922331608002599 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1285, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09626051079412082 / 0.674277127954085 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 1285] | torch.int64 → int64 | 0.0 / 1284.0 / 642.0 / 370.9474356293625 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.016401424710467693 / 2.7044479911769903 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 1285, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006878337801779973 / 0.7598474056372804 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1285, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006878337801779973 / 0.7598474056372804 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1285, 1285] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -3.0685817840964194e+38 / 9.92401185001271e+37 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1285] | torch.int64 → int64 | 0.0 / 1284.0 / 642.0 / 370.9474356293625 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1285, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7036832386620546 / 0.922331608002599 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1285, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09626051079412082 / 0.674277127954085 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006878337801779973 / 0.7598474056372804 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 1285, 4096] | torch.bfloat16 → float32 | -9.5 / 14.0 / 0.01734007335442528 / 1.0281363532899663 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006878337801779973 / 0.7598474056372804 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 1285, 512] | torch.bfloat16 → float32 | -63.75 / 67.5 / 0.018246854484943738 / 5.719575438261625 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006878337801779973 / 0.7598474056372804 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 1285, 512] | torch.bfloat16 → float32 | -7.78125 / 9.0 / -0.014459822048045374 / 1.216480487845552 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1285, 4096] | torch.bfloat16 → float32 | -7.0625 / 6.625 / -0.006771459832424114 / 0.5599412733417723 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 1285, 2880] | torch.bfloat16 → float32 | -50.75 / 58.0 / 0.027966360159653453 / 1.2448929144201983 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -50.75 / 58.0 / 0.027966360159653453 / 1.2448929144201983 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 1285, 1285] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.00031263277851325167 / 0.011357113220638806 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -90.5 / 71.0 / 0.011567910339375672 / 2.969282925627486 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 1285, 2880] | torch.bfloat16 → float32 | -6.625 / 3.828125 / 0.0018868415535842759 / 0.34067084832830785 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -6.625 / 3.828125 / 0.0018868415535842759 / 0.34067084832830785 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [1285, 2880] | torch.bfloat16 → float32 | -6.625 / 3.828125 / 0.0018868415535842759 / 0.34067084832830785 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [1285, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.017761217472656847 / 0.8639713118625318 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.017761217472656847 / 0.8639713118625318 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [1285, 32] | torch.bfloat16 → float32 | -5.21875 / 3.8125 / -0.11365030043783819 / 0.9686349805932319 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 1285, 2880] | torch.bfloat16 → float32 | -87.5 / 156.0 / 0.029326258434447392 / 3.259082142214678 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -41728.0 / 1096.0 / 0.44482844198930327 / 29.23430234008689 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1285, 1285] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6934468108167204e+38 / 1.6947651814413286e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1285, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7036832386620546 / 0.922331608002599 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1285, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09626051079412082 / 0.674277127954085 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 1285] | torch.int64 → int64 | 0.0 / 1284.0 / 642.0 / 370.9474356293625 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -41728.0 / 1096.0 / 0.44482844198930327 / 29.23430234008689 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 1285, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.06160598298126468 / 3.1094620593478957 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1285, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.06160598298126468 / 3.1094620593478957 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1285, 1285] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6934468108167204e+38 / 1.6947651814413286e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1285] | torch.int64 → int64 | 0.0 / 1284.0 / 642.0 / 370.9474356293625 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1285, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7036832386620546 / 0.922331608002599 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1285, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09626051079412082 / 0.674277127954085 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.06160598298126468 / 3.1094620593478957 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 1285, 4096] | torch.bfloat16 → float32 | -13.0 / 14.625 / 0.039594634887766336 / 1.3373525768931565 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.06160598298126468 / 3.1094620593478957 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 1285, 512] | torch.bfloat16 → float32 | -49.0 / 52.0 / 0.1039611343732978 / 3.900926148934927 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.06160598298126468 / 3.1094620593478957 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 1285, 512] | torch.bfloat16 → float32 | -16.0 / 22.0 / -0.020066609816781537 / 2.4348717102165254 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1285, 4096] | torch.bfloat16 → float32 | -11.4375 / 12.8125 / -0.011272080393382036 / 1.4232098251234484 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 1285, 2880] | torch.bfloat16 → float32 | -482.0 / 438.0 / 0.016704828898485635 / 5.158216205458927 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -482.0 / 438.0 / 0.016704828898485635 / 5.158216205458927 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 1285, 1285] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0007015440098298005 / 0.007803489582074431 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -41728.0 / 656.0 / 0.4615190741276773 / 29.21775450932188 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 1285, 2880] | torch.bfloat16 → float32 | -78.5 / 7.6875 / 0.009625967948939499 / 0.7489659790748007 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -78.5 / 7.6875 / 0.009625967948939499 / 0.7489659790748007 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [1285, 2880] | torch.bfloat16 → float32 | -78.5 / 7.6875 / 0.009625967948939499 / 0.7489659790748007 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [1285, 2880] | torch.bfloat16 → float32 | -430.0 / 402.0 / 0.09181132446183721 / 7.460058539704069 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -430.0 / 402.0 / 0.09181132446183721 / 7.460058539704069 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [1285, 32] | torch.bfloat16 → float32 | -10.75 / 4.71875 / -0.15877490451827586 / 0.8213212201022184 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 1285, 2880] | torch.bfloat16 → float32 | -41728.0 / 848.0 / 0.5533195178208801 / 32.207305922965595 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -12736.0 / 14208.0 / -1.1880053313140275 / 399.5601946328205 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1285, 1285] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6934468108167204e+38 / 1.6947651814413286e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1285, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7036832386620546 / 0.922331608002599 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1285, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09626051079412082 / 0.674277127954085 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 1285] | torch.int64 → int64 | 0.0 / 1284.0 / 642.0 / 370.9474356293625 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -12736.0 / 14208.0 / -1.1880053313140275 / 399.5601946328205 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 1285, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.009887294981433774 / 1.7502938574783722 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1285, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.009887294981433774 / 1.7502938574783722 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1285, 1285] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6934468108167204e+38 / 1.6947651814413286e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1285] | torch.int64 → int64 | 0.0 / 1284.0 / 642.0 / 370.9474356293625 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1285, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7036832386620546 / 0.922331608002599 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1285, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09626051079412082 / 0.674277127954085 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.009887294981433774 / 1.7502938574783722 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 1285, 4096] | torch.bfloat16 → float32 | -20.25 / 24.75 / 0.031202931931953216 / 1.6533661485962743 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.009887294981433774 / 1.7502938574783722 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 1285, 512] | torch.bfloat16 → float32 | -93.0 / 67.5 / -0.05946244339883085 / 5.339212804459222 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.009887294981433774 / 1.7502938574783722 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 1285, 512] | torch.bfloat16 → float32 | -42.0 / 22.125 / -0.007338395287964043 / 3.391812937419508 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1285, 4096] | torch.bfloat16 → float32 | -36.25 / 17.375 / -0.001603804296391829 / 1.3152279859359226 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 1285, 2880] | torch.bfloat16 → float32 | -7968.0 / 8512.0 / 3.0605654153032926 / 165.59291746750577 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -7968.0 / 8512.0 / 3.0605654153032926 / 165.59291746750577 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 1285, 1285] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.00043741962491399624 / 0.00630870979090662 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -11584.0 / 11456.0 / 1.8735270111044402 / 395.34363904992045 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 1285, 2880] | torch.bfloat16 → float32 | -50.75 / 22.375 / -0.013019329202005062 / 1.2631735214362843 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -50.75 / 22.375 / -0.013019329202005062 / 1.2631735214362843 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [1285, 2880] | torch.bfloat16 → float32 | -50.75 / 22.375 / -0.013019329202005062 / 1.2631735214362843 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [1285, 2880] | torch.bfloat16 → float32 | -6656.0 / 6464.0 / -1.6303238671711395 / 164.52774998990185 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 1285, 2880] | torch.bfloat16 → float32 | -6656.0 / 6464.0 / -1.6303238671711395 / 164.52774998990185 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [1285, 32] | torch.bfloat16 → float32 | -8.375 / 5.0 / 0.24707116598285125 / 2.5633563299899964 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 1285, 2880] | torch.bfloat16 → float32 | -11904.0 / 12160.0 / 0.2433684360687216 / 399.8847860729332 | [NPY](tensors/0000116.npy) |

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
