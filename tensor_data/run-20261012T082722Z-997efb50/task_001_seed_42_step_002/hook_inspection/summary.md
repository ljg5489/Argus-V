# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.0008221837833594088 / 2.748425150286653 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 356, 356] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.3882053633900797e+38 / 1.5464062161878432e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 356, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.783499295122168 / 0.8885162457583061 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 356, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10629118793873571 / 0.6283728546274333 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 356] | torch.int64 → int64 | 0.0 / 355.0 / 177.5 / 102.76794247234884 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.0008221837833594088 / 2.748425150286653 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 356, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0023536972579320707 / 0.760080975774781 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 356, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0023536972579320707 / 0.760080975774781 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 356, 356] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.3882053633900797e+38 / 1.5464062161878432e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 356] | torch.int64 → int64 | 0.0 / 355.0 / 177.5 / 102.76794247234884 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 356, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.783499295122168 / 0.8885162457583061 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 356, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10629118793873571 / 0.6283728546274333 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0023536972579320707 / 0.760080975774781 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 356, 4096] | torch.bfloat16 → float32 | -10.25 / 12.8125 / 0.02226560165703877 / 1.0542472325050622 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0023536972579320707 / 0.760080975774781 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 356, 512] | torch.bfloat16 → float32 | -65.5 / 69.0 / 0.03340282734860195 / 5.7561392478104425 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0023536972579320707 / 0.760080975774781 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 356, 512] | torch.bfloat16 → float32 | -8.125 / 7.75 / -0.01687372067754858 / 1.2380615131415724 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 356, 4096] | torch.bfloat16 → float32 | -8.125 / 7.75 / -0.007687529522608015 / 0.5582742254683607 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 356, 2880] | torch.bfloat16 → float32 | -39.25 / 58.0 / 0.030157419939168408 / 1.1898106658030674 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -39.25 / 58.0 / 0.030157419939168408 / 1.1898106658030674 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 356, 356] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0010605694086006125 / 0.021479280715733576 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -87.5 / 71.0 / 0.029336080627374063 / 2.937674544493378 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 356, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 0.0014522084040792841 / 0.35140311329690116 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 0.0014522084040792841 / 0.35140311329690116 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [356, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 0.0014522084040792841 / 0.35140311329690116 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [356, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.019986327264816053 / 0.9280854833908586 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.019986327264816053 / 0.9280854833908586 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [356, 32] | torch.bfloat16 → float32 | -5.03125 / 3.421875 / -0.10750788249326555 / 1.0087803015373875 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 356, 2880] | torch.bfloat16 → float32 | -93.0 / 105.5 / 0.049315939707851295 / 3.2321986070342223 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -41216.0 / 896.0 / 0.5223155578870451 / 46.08564364140641 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 356, 356] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6900051168318751e+38 / 1.6947590084078117e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 356, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.783499295122168 / 0.8885162457583061 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 356, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10629118793873571 / 0.6283728546274333 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 356] | torch.int64 → int64 | 0.0 / 355.0 / 177.5 / 102.76794247234884 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -41216.0 / 896.0 / 0.5223155578870451 / 46.08564364140641 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 356, 2880] | torch.bfloat16 → float32 | -191.0 / 140.0 / 0.0689518092014128 / 3.1297457510201174 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 356, 2880] | torch.bfloat16 → float32 | -191.0 / 140.0 / 0.0689518092014128 / 3.1297457510201174 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 356, 356] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6900051168318751e+38 / 1.6947590084078117e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 356] | torch.int64 → int64 | 0.0 / 355.0 / 177.5 / 102.76794247234884 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 356, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.783499295122168 / 0.8885162457583061 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 356, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10629118793873571 / 0.6283728546274333 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -191.0 / 140.0 / 0.0689518092014128 / 3.1297457510201174 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 356, 4096] | torch.bfloat16 → float32 | -12.0625 / 13.3125 / 0.03526597566760143 / 1.3580156397069543 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -191.0 / 140.0 / 0.0689518092014128 / 3.1297457510201174 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 356, 512] | torch.bfloat16 → float32 | -42.25 / 49.0 / 0.07338930398560642 / 3.759490110097033 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -191.0 / 140.0 / 0.0689518092014128 / 3.1297457510201174 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 356, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.04546598587813002 / 2.5166411127051997 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 356, 4096] | torch.bfloat16 → float32 | -11.75 / 11.4375 / -0.03771943100591517 / 1.5018634424333557 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 356, 2880] | torch.bfloat16 → float32 | -466.0 / 500.0 / -0.026332035198570518 / 6.312522661282687 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -466.0 / 500.0 / -0.026332035198570518 / 6.312522661282687 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 356, 356] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0024121001331464846 / 0.01582206446963953 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -41216.0 / 700.0 / 0.4959397311216585 / 45.42637106485177 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 356, 2880] | torch.bfloat16 → float32 | -78.5 / 7.3125 / 0.011366659871473462 / 0.7856859608059995 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -78.5 / 7.3125 / 0.011366659871473462 / 0.7856859608059995 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [356, 2880] | torch.bfloat16 → float32 | -78.5 / 7.3125 / 0.011366659871473462 / 0.7856859608059995 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [356, 2880] | torch.bfloat16 → float32 | -504.0 / 404.0 / 0.1178299662734983 / 9.05149193746318 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -504.0 / 404.0 / 0.1178299662734983 / 9.05149193746318 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [356, 32] | torch.bfloat16 → float32 | -10.75 / 3.21875 / -0.1517863635266765 / 0.7590370214619316 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 356, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.613846431213074 / 47.960481928610946 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -2.081844232204404 / 405.6846570555369 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 356, 356] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6900051168318751e+38 / 1.6947590084078117e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 356, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.783499295122168 / 0.8885162457583061 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 356, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10629118793873571 / 0.6283728546274333 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 356] | torch.int64 → int64 | 0.0 / 355.0 / 177.5 / 102.76794247234884 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -2.081844232204404 / 405.6846570555369 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 356, 2880] | torch.bfloat16 → float32 | -52.75 / 72.0 / 0.0075309789945347035 / 1.7505462488421042 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 356, 2880] | torch.bfloat16 → float32 | -52.75 / 72.0 / 0.0075309789945347035 / 1.7505462488421042 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 356, 356] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6900051168318751e+38 / 1.6947590084078117e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 356] | torch.int64 → int64 | 0.0 / 355.0 / 177.5 / 102.76794247234884 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 356, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.783499295122168 / 0.8885162457583061 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 356, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10629118793873571 / 0.6283728546274333 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -52.75 / 72.0 / 0.0075309789945347035 / 1.7505462488421042 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 356, 4096] | torch.bfloat16 → float32 | -19.0 / 24.25 / 0.030955261246229424 / 1.6678567771740294 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -52.75 / 72.0 / 0.0075309789945347035 / 1.7505462488421042 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 356, 512] | torch.bfloat16 → float32 | -86.0 / 60.75 / -0.07745715024556671 / 5.1038270704436375 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -52.75 / 72.0 / 0.0075309789945347035 / 1.7505462488421042 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 356, 512] | torch.bfloat16 → float32 | -27.625 / 24.375 / 0.017393538037712652 / 3.258104110685844 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 356, 4096] | torch.bfloat16 → float32 | -26.25 / 13.0625 / 0.0029188024584719348 / 1.1617958020784098 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 356, 2880] | torch.bfloat16 → float32 | -6336.0 / 6496.0 / 2.203554165606083 / 165.0247777398658 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -6336.0 / 6496.0 / 2.203554165606083 / 165.0247777398658 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 356, 356] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.001434296618508012 / 0.01155161292511418 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -10496.0 / 11264.0 / 0.12147766475225064 / 355.5865847383251 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 356, 2880] | torch.bfloat16 → float32 | -51.0 / 31.625 / -0.01868382271369931 / 1.2909067099193958 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -51.0 / 31.625 / -0.01868382271369931 / 1.2909067099193958 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [356, 2880] | torch.bfloat16 → float32 | -51.0 / 31.625 / -0.01868382271369931 / 1.2909067099193958 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [356, 2880] | torch.bfloat16 → float32 | -4832.0 / 4704.0 / -1.6647899158587318 / 149.88984894545308 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 356, 2880] | torch.bfloat16 → float32 | -4832.0 / 4704.0 / -1.6647899158587318 / 149.88984894545308 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [356, 32] | torch.bfloat16 → float32 | -8.9375 / 5.15625 / 0.25271604837996237 / 2.7190173362273833 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 356, 2880] | torch.bfloat16 → float32 | -10752.0 / 10944.0 / -1.5424302366640088 / 391.0493253496145 | [NPY](tensors/0000116.npy) |

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
