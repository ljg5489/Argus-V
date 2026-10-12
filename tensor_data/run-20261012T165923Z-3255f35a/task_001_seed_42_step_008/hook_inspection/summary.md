# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.015588328623021825 / 2.696132523638347 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1294, 1294] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -3.070698808052449e+38 / 9.894639089205432e+37 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1294, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7032479281973387 / 0.9228089616333243 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1294, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09674495558532054 / 0.6740107274887593 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 1294] | torch.int64 → int64 | 0.0 / 1293.0 / 646.5 / 373.54551262195616 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.015588328623021825 / 2.696132523638347 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 1294, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006479361624495006 / 0.7582148250853136 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1294, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006479361624495006 / 0.7582148250853136 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1294, 1294] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -3.070698808052449e+38 / 9.894639089205432e+37 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1294] | torch.int64 → int64 | 0.0 / 1293.0 / 646.5 / 373.54551262195616 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1294, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7032479281973387 / 0.9228089616333243 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1294, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09674495558532054 / 0.6740107274887593 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006479361624495006 / 0.7582148250853136 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 1294, 4096] | torch.bfloat16 → float32 | -9.5 / 14.0 / 0.016230271715692517 / 1.0312876776352022 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006479361624495006 / 0.7582148250853136 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 1294, 512] | torch.bfloat16 → float32 | -63.75 / 67.5 / 0.01572863927519113 / 5.711978789138559 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.006479361624495006 / 0.7582148250853136 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 1294, 512] | torch.bfloat16 → float32 | -7.78125 / 9.0 / -0.01543029320337759 / 1.2166889724452825 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1294, 4096] | torch.bfloat16 → float32 | -7.0625 / 6.625 / -0.007119493887198791 / 0.5627718257837435 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 1294, 2880] | torch.bfloat16 → float32 | -50.75 / 58.0 / 0.027928115273044708 / 1.2500061987987123 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -50.75 / 58.0 / 0.027928115273044708 / 1.2500061987987123 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 1294, 1294] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.00031104691457838795 / 0.011387463865428394 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -90.5 / 71.0 / 0.012345313640234912 / 2.964542202169624 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 1294, 2880] | torch.bfloat16 → float32 | -6.59375 / 3.828125 / 0.002229771868054034 / 0.34235809632340347 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -6.59375 / 3.828125 / 0.002229771868054034 / 0.34235809632340347 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [1294, 2880] | torch.bfloat16 → float32 | -6.59375 / 3.828125 / 0.002229771868054034 / 0.34235809632340347 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [1294, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.01842490979979717 / 0.8841849995587859 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.01842490979979717 / 0.8841849995587859 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [1294, 32] | torch.bfloat16 → float32 | -5.21875 / 3.8125 / -0.11396116524980832 / 0.9691019302319743 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 1294, 2880] | torch.bfloat16 → float32 | -88.0 / 156.0 / 0.030769342590438824 / 3.266194070133718 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -41728.0 / 1120.0 / 0.4487649295249388 / 29.09058070753692 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1294, 1294] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6934559838880356e+38 / 1.6947651885550825e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1294, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7032479281973387 / 0.9228089616333243 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1294, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09674495558532054 / 0.6740107274887593 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 1294] | torch.int64 → int64 | 0.0 / 1293.0 / 646.5 / 373.54551262195616 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -41728.0 / 1120.0 / 0.4487649295249388 / 29.09058070753692 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 1294, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.06130310163457185 / 3.1230176993818795 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1294, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.06130310163457185 / 3.1230176993818795 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1294, 1294] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6934559838880356e+38 / 1.6947651885550825e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1294] | torch.int64 → int64 | 0.0 / 1293.0 / 646.5 / 373.54551262195616 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1294, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7032479281973387 / 0.9228089616333243 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1294, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09674495558532054 / 0.6740107274887593 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.06130310163457185 / 3.1230176993818795 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 1294, 4096] | torch.bfloat16 → float32 | -13.0625 / 14.625 / 0.03961752718438765 / 1.324194794880968 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.06130310163457185 / 3.1230176993818795 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 1294, 512] | torch.bfloat16 → float32 | -47.25 / 52.5 / 0.10702529958362444 / 3.8984414972760972 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.06130310163457185 / 3.1230176993818795 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 1294, 512] | torch.bfloat16 → float32 | -16.0 / 22.0 / -0.020254518229919565 / 2.3999293683574883 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1294, 4096] | torch.bfloat16 → float32 | -11.375 / 12.875 / -0.009071235132566953 / 1.395025112753437 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 1294, 2880] | torch.bfloat16 → float32 | -482.0 / 438.0 / 0.014151626992404524 / 5.136479332025211 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -482.0 / 438.0 / 0.014151626992404524 / 5.136479332025211 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 1294, 1294] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0006949051003482761 / 0.00781362583972388 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -41728.0 / 652.0 / 0.46291226313406103 / 29.046528064935885 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 1294, 2880] | torch.bfloat16 → float32 | -78.5 / 7.6875 / 0.010061387584510972 / 0.750898350600148 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -78.5 / 7.6875 / 0.010061387584510972 / 0.750898350600148 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [1294, 2880] | torch.bfloat16 → float32 | -78.5 / 7.6875 / 0.010061387584510972 / 0.750898350600148 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [1294, 2880] | torch.bfloat16 → float32 | -444.0 / 398.0 / 0.0939642278799666 / 7.491921328555208 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -444.0 / 398.0 / 0.0939642278799666 / 7.491921328555208 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [1294, 32] | torch.bfloat16 → float32 | -10.75 / 5.3125 / -0.16741397391883814 / 0.895962652708406 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 1294, 2880] | torch.bfloat16 → float32 | -41728.0 / 864.0 / 0.5568798384878536 / 32.06712975122686 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -12736.0 / 14208.0 / -1.1682317259793586 / 400.9203608526663 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1294, 1294] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6934559838880356e+38 / 1.6947651885550825e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1294, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7032479281973387 / 0.9228089616333243 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1294, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09674495558532054 / 0.6740107274887593 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 1294] | torch.int64 → int64 | 0.0 / 1293.0 / 646.5 / 373.54551262195616 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -12736.0 / 14208.0 / -1.1682317259793586 / 400.9203608526663 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 1294, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.009902135838413643 / 1.7493553333506748 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 1294, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.009902135838413643 / 1.7493553333506748 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 1294, 1294] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6934559838880356e+38 / 1.6947651885550825e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 1294] | torch.int64 → int64 | 0.0 / 1293.0 / 646.5 / 373.54551262195616 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 1294, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7032479281973387 / 0.9228089616333243 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 1294, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.09674495558532054 / 0.6740107274887593 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.009902135838413643 / 1.7493553333506748 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 1294, 4096] | torch.bfloat16 → float32 | -20.0 / 26.625 / 0.03088691660328957 / 1.6440325181466422 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.009902135838413643 / 1.7493553333506748 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 1294, 512] | torch.bfloat16 → float32 | -90.0 / 69.0 / -0.05627633288167437 / 5.358767996749509 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.009902135838413643 / 1.7493553333506748 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 1294, 512] | torch.bfloat16 → float32 | -41.5 / 22.25 / -0.005642217110376086 / 3.415564555897427 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 1294, 4096] | torch.bfloat16 → float32 | -36.25 / 17.25 / -0.0005353292459160204 / 1.3358034449680871 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 1294, 2880] | torch.bfloat16 → float32 | -8000.0 / 8576.0 / 3.254140386717125 / 171.8653947684798 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -8000.0 / 8576.0 / 3.254140386717125 / 171.8653947684798 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 1294, 1294] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0004276714150936185 / 0.006367134738477308 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -11648.0 / 11520.0 / 2.086135397611687 / 404.2119005371625 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 1294, 2880] | torch.bfloat16 → float32 | -51.0 / 22.5 / -0.012120498882399662 / 1.2571791542431279 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -51.0 / 22.5 / -0.012120498882399662 / 1.2571791542431279 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [1294, 2880] | torch.bfloat16 → float32 | -51.0 / 22.5 / -0.012120498882399662 / 1.2571791542431279 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [1294, 2880] | torch.bfloat16 → float32 | -6976.0 / 7040.0 / -1.6624381169858469 / 167.14613850947936 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 1294, 2880] | torch.bfloat16 → float32 | -6976.0 / 7040.0 / -1.6624381169858469 / 167.14613850947936 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [1294, 32] | torch.bfloat16 → float32 | -8.4375 / 5.0 / 0.2284997410531022 / 2.4577222812377024 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 1294, 2880] | torch.bfloat16 → float32 | -11904.0 / 12160.0 / 0.4228759398764194 / 404.7429292871993 | [NPY](tensors/0000116.npy) |

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
