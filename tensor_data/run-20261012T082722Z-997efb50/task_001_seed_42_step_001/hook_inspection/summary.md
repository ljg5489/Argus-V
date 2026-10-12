# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.004622689370421747 / 2.803841486091545 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 244, 244] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.0741636585126973e+38 / 1.6517529914242059e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 244, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8149455971405154 / 0.8679542089257619 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 244, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11224381587650345 / 0.6159125941189683 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 244] | torch.int64 → int64 | 0.0 / 243.0 / 121.5 / 70.43614129124337 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.004622689370421747 / 2.803841486091545 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 244, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.003788502502169473 / 0.7609679541495404 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 244, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.003788502502169473 / 0.7609679541495404 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 244, 244] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.0741636585126973e+38 / 1.6517529914242059e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 244] | torch.int64 → int64 | 0.0 / 243.0 / 121.5 / 70.43614129124337 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 244, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8149455971405154 / 0.8679542089257619 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 244, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11224381587650345 / 0.6159125941189683 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.003788502502169473 / 0.7609679541495404 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 244, 4096] | torch.bfloat16 → float32 | -10.25 / 12.8125 / 0.02259907951465124 / 1.0424890232860655 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.003788502502169473 / 0.7609679541495404 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 244, 512] | torch.bfloat16 → float32 | -65.5 / 69.0 / 0.025575254784255735 / 5.79146507782466 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.003788502502169473 / 0.7609679541495404 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 244, 512] | torch.bfloat16 → float32 | -8.125 / 7.71875 / -0.01596595911828221 / 1.2207179205189806 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 244, 4096] | torch.bfloat16 → float32 | -8.125 / 7.71875 / -0.007282728917109239 / 0.5495608214732326 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 244, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.02929709752620188 / 1.1767907296483178 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.02929709752620188 / 1.1767907296483178 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 244, 244] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0015720032372444595 / 0.02617309202157712 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -87.5 / 70.5 / 0.02466890449162389 / 2.9656195098003595 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 244, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0010156934420987014 / 0.34306666239207223 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0010156934420987014 / 0.34306666239207223 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [244, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0010156934420987014 / 0.34306666239207223 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [244, 2880] | torch.bfloat16 → float32 | -49.75 / 92.5 / 0.019497168262596013 / 0.9275709749330556 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -49.75 / 92.5 / 0.019497168262596013 / 0.9275709749330556 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [244, 32] | torch.bfloat16 → float32 | -4.9375 / 3.4375 / -0.10661478511622695 / 1.0164650923552812 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 244, 2880] | torch.bfloat16 → float32 | -90.0 / 106.0 / 0.04414727422926161 / 3.2360911879160077 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.508386029224361 / 54.07577120000092 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 244, 244] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6878199335822195e+38 / 1.6947514614491082e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 244, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8149455971405154 / 0.8679542089257619 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 244, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11224381587650345 / 0.6159125941189683 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 244] | torch.int64 → int64 | 0.0 / 243.0 / 121.5 / 70.43614129124337 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -41216.0 / 824.0 / 0.508386029224361 / 54.07577120000092 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 244, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06723223448559669 / 3.150760458142107 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 244, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06723223448559669 / 3.150760458142107 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 244, 244] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6878199335822195e+38 / 1.6947514614491082e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 244] | torch.int64 → int64 | 0.0 / 243.0 / 121.5 / 70.43614129124337 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 244, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8149455971405154 / 0.8679542089257619 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 244, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11224381587650345 / 0.6159125941189683 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06723223448559669 / 3.150760458142107 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 244, 4096] | torch.bfloat16 → float32 | -11.625 / 13.3125 / 0.034466862935214074 / 1.350349299245532 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06723223448559669 / 3.150760458142107 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 244, 512] | torch.bfloat16 → float32 | -38.25 / 46.5 / 0.05994341166720527 / 3.6683475878652536 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -191.0 / 142.0 / 0.06723223448559669 / 3.150760458142107 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 244, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.04926822212387304 / 2.5060327032276866 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 244, 4096] | torch.bfloat16 → float32 | -11.625 / 11.1875 / -0.038526561627532666 / 1.4793565393047938 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 244, 2880] | torch.bfloat16 → float32 | -472.0 / 502.0 / -0.04341834155598381 / 6.791791543103403 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -472.0 / 502.0 / -0.04341834155598381 / 6.791791543103403 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 244, 244] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003422623914861184 / 0.019751971663563198 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -41216.0 / 696.0 / 0.4649323777735016 / 53.319959100184555 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 244, 2880] | torch.bfloat16 → float32 | -78.5 / 7.3125 / 0.010409772550078187 / 0.7924505682046752 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -78.5 / 7.3125 / 0.010409772550078187 / 0.7924505682046752 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [244, 2880] | torch.bfloat16 → float32 | -78.5 / 7.3125 / 0.010409772550078187 / 0.7924505682046752 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [244, 2880] | torch.bfloat16 → float32 | -512.0 / 410.0 / 0.11651709770244327 / 9.43280193451588 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -512.0 / 410.0 / 0.11651709770244327 / 9.43280193451588 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [244, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.15445073022217046 / 0.7619441747654759 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 244, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.58146012502507 / 55.6717143350408 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -2.005842494096044 / 417.97498060339694 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 244, 244] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6878199335822195e+38 / 1.6947514614491082e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 244, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8149455971405154 / 0.8679542089257619 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 244, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11224381587650345 / 0.6159125941189683 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 244] | torch.int64 → int64 | 0.0 / 243.0 / 121.5 / 70.43614129124337 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -2.005842494096044 / 417.97498060339694 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 244, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.00782468311763445 / 1.7566022910326407 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 244, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.00782468311763445 / 1.7566022910326407 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 244, 244] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6878199335822195e+38 / 1.6947514614491082e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 244] | torch.int64 → int64 | 0.0 / 243.0 / 121.5 / 70.43614129124337 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 244, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8149455971405154 / 0.8679542089257619 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 244, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11224381587650345 / 0.6159125941189683 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.00782468311763445 / 1.7566022910326407 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 244, 4096] | torch.bfloat16 → float32 | -18.25 / 24.125 / 0.030999863122986894 / 1.6406544361029092 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.00782468311763445 / 1.7566022910326407 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 244, 512] | torch.bfloat16 → float32 | -82.0 / 55.75 / -0.08673097014610395 / 4.981741203131586 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -52.75 / 71.5 / 0.00782468311763445 / 1.7566022910326407 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 244, 512] | torch.bfloat16 → float32 | -27.75 / 24.5 / 0.02057583312519261 / 3.208607770684717 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 244, 4096] | torch.bfloat16 → float32 | -25.625 / 13.0625 / -9.098703713177899e-05 / 1.1384812969750404 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 244, 2880] | torch.bfloat16 → float32 | -6560.0 / 6784.0 / 2.6184121849690523 / 166.89861257613455 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -6560.0 / 6784.0 / 2.6184121849690523 / 166.89861257613455 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 244, 244] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0019707463130819738 / 0.01360946501797371 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -10496.0 / 11200.0 / 0.6128985545674308 / 368.1164983907113 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 244, 2880] | torch.bfloat16 → float32 | -45.75 / 24.125 / -0.01675144559237258 / 1.219112673696663 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -45.75 / 24.125 / -0.01675144559237258 / 1.219112673696663 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [244, 2880] | torch.bfloat16 → float32 | -45.75 / 24.125 / -0.01675144559237258 / 1.219112673696663 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [244, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.5649899224765966 / 150.59455531083805 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 244, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.5649899224765966 / 150.59455531083805 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [244, 32] | torch.bfloat16 → float32 | -7.59375 / 4.25 / 0.24543007866280978 / 2.508327573775325 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 244, 2880] | torch.bfloat16 → float32 | -10752.0 / 10880.0 / -0.9517720957271388 / 415.1536280389326 | [NPY](tensors/0000116.npy) |

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
