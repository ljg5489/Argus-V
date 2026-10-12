# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.014570307614662374 / 2.7483574439101304 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 559, 559] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.7015611163969e+38 / 1.3633025116902884e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 559, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7490176150112118 / 0.9077314645461902 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 559, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10540706606418118 / 0.6430212556480804 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 559] | torch.int64 → int64 | 0.0 / 558.0 / 279.0 / 161.36914203155447 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.014570307614662374 / 2.7483574439101304 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 559, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007174273502804329 / 0.7648286088319676 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 559, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007174273502804329 / 0.7648286088319676 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 559, 559] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.7015611163969e+38 / 1.3633025116902884e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 559] | torch.int64 → int64 | 0.0 / 558.0 / 279.0 / 161.36914203155447 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 559, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7490176150112118 / 0.9077314645461902 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 559, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10540706606418118 / 0.6430212556480804 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007174273502804329 / 0.7648286088319676 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 559, 4096] | torch.bfloat16 → float32 | -9.0625 / 11.8125 / 0.021009970706744523 / 1.0171063439133512 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007174273502804329 / 0.7648286088319676 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 559, 512] | torch.bfloat16 → float32 | -63.75 / 67.5 / 0.021779084734348763 / 5.750660207014095 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007174273502804329 / 0.7648286088319676 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 559, 512] | torch.bfloat16 → float32 | -7.78125 / 9.0 / -0.011582594786808962 / 1.1986959288006493 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 559, 4096] | torch.bfloat16 → float32 | -6.96875 / 6.53125 / -0.004912190103058157 / 0.5449603315684791 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 559, 2880] | torch.bfloat16 → float32 | -50.5 / 55.0 / 0.027218210105208755 / 1.2012205685412465 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -50.5 / 55.0 / 0.027218210105208755 / 1.2012205685412465 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 559, 559] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0007164679632091585 / 0.017089985925036584 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -89.5 / 71.0 / 0.012641070257406585 / 2.973834294585067 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 559, 2880] | torch.bfloat16 → float32 | -6.59375 / 3.15625 / 0.0009101894155257243 / 0.33474151076767394 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -6.59375 / 3.15625 / 0.0009101894155257243 / 0.33474151076767394 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [559, 2880] | torch.bfloat16 → float32 | -6.59375 / 3.15625 / 0.0009101894155257243 / 0.33474151076767394 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [559, 2880] | torch.bfloat16 → float32 | -49.5 / 135.0 / 0.016973647393791227 / 0.841212669499586 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -49.5 / 135.0 / 0.016973647393791227 / 0.841212669499586 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [559, 32] | torch.bfloat16 → float32 | -5.1875 / 3.8125 / -0.11039313860570808 / 0.9963624651062699 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 559, 2880] | torch.bfloat16 → float32 | -89.0 / 156.0 / 0.02960711063032619 / 3.237312399844935 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -41728.0 / 1096.0 / 0.4571408888426909 / 39.14050043949176 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 559, 559] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6917339134189238e+38 / 1.6947629828336098e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 559, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7490176150112118 / 0.9077314645461902 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 559, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10540706606418118 / 0.6430212556480804 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 559] | torch.int64 → int64 | 0.0 / 558.0 / 279.0 / 161.36914203155447 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -41728.0 / 1096.0 / 0.4571408888426909 / 39.14050043949176 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 559, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06101863294646598 / 3.0821728452620634 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 559, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06101863294646598 / 3.0821728452620634 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 559, 559] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6917339134189238e+38 / 1.6947629828336098e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 559] | torch.int64 → int64 | 0.0 / 558.0 / 279.0 / 161.36914203155447 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 559, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7490176150112118 / 0.9077314645461902 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 559, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10540706606418118 / 0.6430212556480804 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06101863294646598 / 3.0821728452620634 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 559, 4096] | torch.bfloat16 → float32 | -12.9375 / 14.625 / 0.03905195556025887 / 1.3650823235699427 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06101863294646598 / 3.0821728452620634 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 559, 512] | torch.bfloat16 → float32 | -43.0 / 47.25 / 0.06996932482386045 / 3.6738168701075935 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06101863294646598 / 3.0821728452620634 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 559, 512] | torch.bfloat16 → float32 | -16.0 / 22.0 / -0.007757185621783538 / 2.5236348090421834 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 559, 4096] | torch.bfloat16 → float32 | -11.0625 / 13.125 / -0.008242601206820337 / 1.4474039914436043 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 559, 2880] | torch.bfloat16 → float32 | -476.0 / 432.0 / -0.012164119939586172 / 5.434066046996403 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -476.0 / 432.0 / -0.012164119939586172 / 5.434066046996403 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 559, 559] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0015463649873049795 / 0.01226349018749613 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -41728.0 / 648.0 / 0.4450413430289184 / 38.752124194270415 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 559, 2880] | torch.bfloat16 → float32 | -78.5 / 7.15625 / 0.009020219276017021 / 0.7591991426376633 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -78.5 / 7.15625 / 0.009020219276017021 / 0.7591991426376633 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [559, 2880] | torch.bfloat16 → float32 | -78.5 / 7.15625 / 0.009020219276017021 / 0.7591991426376633 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [559, 2880] | torch.bfloat16 → float32 | -410.0 / 376.0 / 0.08599878488205888 / 7.609228764343158 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -410.0 / 376.0 / 0.08599878488205888 / 7.609228764343158 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [559, 32] | torch.bfloat16 → float32 | -10.75 / 3.171875 / -0.1539018427110102 / 0.7157290018971654 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 559, 2880] | torch.bfloat16 → float32 | -41728.0 / 776.0 / 0.5310787298550923 / 41.179901929449 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -12672.0 / 14144.0 / -1.0353642375159753 / 412.42532782598005 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 559, 559] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6917339134189238e+38 / 1.6947629828336098e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 559, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7490176150112118 / 0.9077314645461902 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 559, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10540706606418118 / 0.6430212556480804 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 559] | torch.int64 → int64 | 0.0 / 558.0 / 279.0 / 161.36914203155447 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -12672.0 / 14144.0 / -1.0353642375159753 / 412.42532782598005 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 559, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.01032929804736626 / 1.766730497507978 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 559, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.01032929804736626 / 1.766730497507978 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 559, 559] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6917339134189238e+38 / 1.6947629828336098e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 559] | torch.int64 → int64 | 0.0 / 558.0 / 279.0 / 161.36914203155447 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 559, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7490176150112118 / 0.9077314645461902 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 559, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10540706606418118 / 0.6430212556480804 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.01032929804736626 / 1.766730497507978 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 559, 4096] | torch.bfloat16 → float32 | -19.0 / 24.75 / 0.035637055293269264 / 1.6666028845317165 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.01032929804736626 / 1.766730497507978 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 559, 512] | torch.bfloat16 → float32 | -86.0 / 65.5 / -0.09019120244546927 / 5.005375853076895 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.01032929804736626 / 1.766730497507978 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 559, 512] | torch.bfloat16 → float32 | -27.125 / 21.125 / -0.015193028479218083 / 3.2743460499156 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 559, 4096] | torch.bfloat16 → float32 | -25.5 / 17.75 / -0.00443613146699347 / 1.1364982731397357 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 559, 2880] | torch.bfloat16 → float32 | -6496.0 / 6752.0 / 2.413949250949528 / 146.3579060198191 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -6496.0 / 6752.0 / 2.413949250949528 / 146.3579060198191 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 559, 559] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0009493373960589341 / 0.009064639368947214 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -11264.0 / 11328.0 / 1.3770864768664233 / 360.67480542074173 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 559, 2880] | torch.bfloat16 → float32 | -49.75 / 26.0 / -0.014604267134930758 / 1.2313521358878439 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -49.75 / 26.0 / -0.014604267134930758 / 1.2313521358878439 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [559, 2880] | torch.bfloat16 → float32 | -49.75 / 26.0 / -0.014604267134930758 / 1.2313521358878439 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [559, 2880] | torch.bfloat16 → float32 | -6592.0 / 6592.0 / -1.2403593363616892 / 150.67619037281236 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 559, 2880] | torch.bfloat16 → float32 | -6592.0 / 6592.0 / -1.2403593363616892 / 150.67619037281236 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [559, 32] | torch.bfloat16 → float32 | -8.125 / 4.5625 / 0.24023609255208953 / 2.520187534548958 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 559, 2880] | torch.bfloat16 → float32 | -11904.0 / 11968.0 / 0.136897309678043 / 391.67622307370283 | [NPY](tensors/0000116.npy) |

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
