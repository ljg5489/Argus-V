# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.016069528265818166 / 2.6941438548937544 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1488, 1488] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -3.1104015786382382e+38 / 9.31775618685417e+37 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1488, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6869190193647619 / 0.9356863093136888 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1488, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09268716356484064 / 0.6736924890156535 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 1488] | torch.int64 → int64 | 0.0 / 1487.0 / 743.5 / 429.5485032760173 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.016069528265818166 / 2.6941438548937544 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 1488, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006590145085485549 / 0.7585159825578383 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1488, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006590145085485549 / 0.7585159825578383 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1488, 1488] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -3.1104015786382382e+38 / 9.31775618685417e+37 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1488] | torch.int64 → int64 | 0.0 / 1487.0 / 743.5 / 429.5485032760173 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1488, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6869190193647619 / 0.9356863093136888 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1488, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09268716356484064 / 0.6736924890156535 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006590145085485549 / 0.7585159825578383 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 1488, 4096] | torch.bfloat16 → float32 | -9.5 / 14.0 / 0.01639312827982668 / 1.0314944857684016 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006590145085485549 / 0.7585159825578383 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 1488, 512] | torch.bfloat16 → float32 | -63.5 / 67.5 / 0.0166939225029676 / 5.708162745087548 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006590145085485549 / 0.7585159825578383 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 1488, 512] | torch.bfloat16 → float32 | -7.78125 / 9.0 / -0.015063025832792083 / 1.2195308849232407 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1488, 4096] | torch.bfloat16 → float32 | -7.0625 / 6.625 / -0.0070955172032945695 / 0.5640374010614169 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 1488, 2880] | torch.bfloat16 → float32 | -50.75 / 58.0 / 0.028047076995662126 / 1.2515395140303678 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -50.75 / 58.0 / 0.028047076995662126 / 1.2515395140303678 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 1488, 1488] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.00027040342481082064 / 0.010604112166263387 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -90.5 / 71.0 / 0.011984089354727433 / 2.965513834283189 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 1488, 2880] | torch.bfloat16 → float32 | -6.625 / 3.828125 / 0.002197529210005537 / 0.3428310591019966 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -6.625 / 3.828125 / 0.002197529210005537 / 0.3428310591019966 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [1488, 2880] | torch.bfloat16 → float32 | -6.625 / 3.828125 / 0.002197529210005537 / 0.3428310591019966 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [1488, 2880] | torch.bfloat16 → float32 | -49.5 / 135.0 / 0.018319888964680384 / 0.8798647046873845 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -49.5 / 135.0 / 0.018319888964680384 / 0.8798647046873845 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [1488, 32] | torch.bfloat16 → float32 | -5.1875 / 3.8125 / -0.11423751743890906 / 0.9650288795885276 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 1488, 2880] | torch.bfloat16 → float32 | -88.0 / 156.0 / 0.030306789049324597 / 3.2661689908362974 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -41728.0 / 1112.0 / 0.44571854696478896 / 27.8407087399144 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1488, 1488] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6936267391858304e+38 / 1.6947653119122032e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1488, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6869190193647619 / 0.9356863093136888 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1488, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09268716356484064 / 0.6736924890156535 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 1488] | torch.int64 → int64 | 0.0 / 1487.0 / 743.5 / 429.5485032760173 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -41728.0 / 1112.0 / 0.44571854696478896 / 27.8407087399144 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 1488, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.061524040433867506 / 3.1060850401750018 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1488, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.061524040433867506 / 3.1060850401750018 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1488, 1488] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6936267391858304e+38 / 1.6947653119122032e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1488] | torch.int64 → int64 | 0.0 / 1487.0 / 743.5 / 429.5485032760173 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1488, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6869190193647619 / 0.9356863093136888 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1488, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09268716356484064 / 0.6736924890156535 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.061524040433867506 / 3.1060850401750018 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 1488, 4096] | torch.bfloat16 → float32 | -14.25 / 14.6875 / 0.03956110075755631 / 1.3289951759881824 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.061524040433867506 / 3.1060850401750018 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 1488, 512] | torch.bfloat16 → float32 | -48.0 / 53.0 / 0.10618725264401056 / 3.928713601071762 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.061524040433867506 / 3.1060850401750018 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 1488, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.023692291693042798 / 2.3995278979549997 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1488, 4096] | torch.bfloat16 → float32 | -11.375 / 12.8125 / -0.01227023605087297 / 1.409475195613199 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 1488, 2880] | torch.bfloat16 → float32 | -478.0 / 434.0 / 0.01928285180027643 / 5.1047017813111095 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -478.0 / 434.0 / 0.01928285180027643 / 5.1047017813111095 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 1488, 1488] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0006061703706010548 / 0.007196121351123535 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -41728.0 / 664.0 / 0.46501634994848867 / 27.905197689489746 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 1488, 2880] | torch.bfloat16 → float32 | -78.5 / 7.75 / 0.010313210736867261 / 0.750908933898072 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -78.5 / 7.75 / 0.010313210736867261 / 0.750908933898072 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [1488, 2880] | torch.bfloat16 → float32 | -78.5 / 7.75 / 0.010313210736867261 / 0.750908933898072 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [1488, 2880] | torch.bfloat16 → float32 | -444.0 / 390.0 / 0.09509073782672162 / 7.410602806108569 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -444.0 / 390.0 / 0.09509073782672162 / 7.410602806108569 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [1488, 32] | torch.bfloat16 → float32 | -10.75 / 5.34375 / -0.17022649559282488 / 0.9277816465086128 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 1488, 2880] | torch.bfloat16 → float32 | -41728.0 / 864.0 / 0.5601522177350992 / 30.96790777256584 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -12672.0 / 14080.0 / -1.1695509768159016 / 398.0050372955028 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1488, 1488] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6936267391858304e+38 / 1.6947653119122032e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1488, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6869190193647619 / 0.9356863093136888 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1488, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09268716356484064 / 0.6736924890156535 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 1488] | torch.int64 → int64 | 0.0 / 1487.0 / 743.5 / 429.5485032760173 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -12672.0 / 14080.0 / -1.1695509768159016 / 398.0050372955028 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 1488, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009961405003458938 / 1.7479857238249332 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1488, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009961405003458938 / 1.7479857238249332 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1488, 1488] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6936267391858304e+38 / 1.6947653119122032e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1488] | torch.int64 → int64 | 0.0 / 1487.0 / 743.5 / 429.5485032760173 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1488, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.6869190193647619 / 0.9356863093136888 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1488, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09268716356484064 / 0.6736924890156535 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009961405003458938 / 1.7479857238249332 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 1488, 4096] | torch.bfloat16 → float32 | -21.0 / 27.5 / 0.03007762857670066 / 1.642526484899424 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009961405003458938 / 1.7479857238249332 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 1488, 512] | torch.bfloat16 → float32 | -90.0 / 69.0 / -0.05552668204392185 / 5.40177173992109 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.009961405003458938 / 1.7479857238249332 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 1488, 512] | torch.bfloat16 → float32 | -42.0 / 23.375 / -0.00796342147429729 / 3.4168235519175307 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1488, 4096] | torch.bfloat16 → float32 | -36.5 / 17.5 / -0.001113038142562913 / 1.347636363313418 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 1488, 2880] | torch.bfloat16 → float32 | -8064.0 / 8576.0 / 3.2736088721102745 / 171.20305430167025 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -8064.0 / 8576.0 / 3.2736088721102745 / 171.20305430167025 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 1488, 1488] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0003769103314843832 / 0.005894569831386611 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -11648.0 / 11392.0 / 2.1041474157764073 / 403.5114439573735 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 1488, 2880] | torch.bfloat16 → float32 | -51.25 / 22.5 / -0.012047223770560358 / 1.2623773842238633 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -51.25 / 22.5 / -0.012047223770560358 / 1.2623773842238633 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [1488, 2880] | torch.bfloat16 → float32 | -51.25 / 22.5 / -0.012047223770560358 / 1.2623773842238633 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [1488, 2880] | torch.bfloat16 → float32 | -6656.0 / 6752.0 / -1.7028636390198661 / 168.81645548259036 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 1488, 2880] | torch.bfloat16 → float32 | -6656.0 / 6752.0 / -1.7028636390198661 / 168.81645548259036 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [1488, 32] | torch.bfloat16 → float32 | -8.375 / 5.0 / 0.23751560270145375 / 2.491516171311551 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 1488, 2880] | torch.bfloat16 → float32 | -11840.0 / 11968.0 / 0.4017506037704121 / 403.2744843896011 | [NPY](tensors/0000116.npy) |

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
