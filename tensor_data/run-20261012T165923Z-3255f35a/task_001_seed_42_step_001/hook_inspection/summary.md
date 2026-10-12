# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -95.0 / 72.0 / -0.01244045304118966 / 2.780906577979641 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 350, 350] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.374830204707598e+38 / 1.5523347003167586e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 350, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7840756014415196 / 0.8888353925731802 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 350, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10827774247004916 / 0.6268626933647311 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 350] | torch.int64 → int64 | 0.0 / 349.0 / 174.5 / 101.03588471429346 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -95.0 / 72.0 / -0.01244045304118966 / 2.780906577979641 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 350, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007235826396087688 / 0.7706083626337484 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 350, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007235826396087688 / 0.7706083626337484 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 350, 350] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.374830204707598e+38 / 1.5523347003167586e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 350] | torch.int64 → int64 | 0.0 / 349.0 / 174.5 / 101.03588471429346 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 350, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7840756014415196 / 0.8888353925731802 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 350, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10827774247004916 / 0.6268626933647311 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007235826396087688 / 0.7706083626337484 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 350, 4096] | torch.bfloat16 → float32 | -9.3125 / 12.25 / 0.023257981356816473 / 1.014535387561695 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007235826396087688 / 0.7706083626337484 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 350, 512] | torch.bfloat16 → float32 | -63.5 / 65.5 / 0.026162814583097185 / 5.768999372530391 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007235826396087688 / 0.7706083626337484 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 350, 512] | torch.bfloat16 → float32 | -7.375 / 7.53125 / -0.010942844258887427 / 1.1958117085405584 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 350, 4096] | torch.bfloat16 → float32 | -6.84375 / 6.125 / -0.005065183831131728 / 0.5374272992668077 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 350, 2880] | torch.bfloat16 → float32 | -38.75 / 52.25 / 0.026707853594197084 / 1.1814602102717606 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -38.75 / 52.25 / 0.026707853594197084 / 1.1814602102717606 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 350, 350] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0011404563186363367 / 0.021610373552200947 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -87.5 / 64.5 / 0.014259460788870613 / 2.982985288279333 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 350, 2880] | torch.bfloat16 → float32 | -6.5 / 3.0625 / 0.0006439090148797111 / 0.3338843963741363 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -6.5 / 3.0625 / 0.0006439090148797111 / 0.3338843963741363 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [350, 2880] | torch.bfloat16 → float32 | -6.5 / 3.0625 / 0.0006439090148797111 / 0.3338843963741363 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [350, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.016604820017303734 / 0.8444789788893302 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.016604820017303734 / 0.8444789788893302 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [350, 32] | torch.bfloat16 → float32 | -5.1875 / 3.21875 / -0.11151949746268136 / 1.003708529229792 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 350, 2880] | torch.bfloat16 → float32 | -91.0 / 156.0 / 0.030866667564899208 / 3.2388006877184825 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -41728.0 / 1088.0 / 0.45865435215783495 / 47.10259146423061 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 350, 350] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.689923506926837e+38 / 1.694758777200652e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 350, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7840756014415196 / 0.8888353925731802 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 350, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10827774247004916 / 0.6268626933647311 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 350] | torch.int64 → int64 | 0.0 / 349.0 / 174.5 / 101.03588471429346 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -41728.0 / 1088.0 / 0.45865435215783495 / 47.10259146423061 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 350, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.05953917131490179 / 3.0744496662674394 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 350, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.05953917131490179 / 3.0744496662674394 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 350, 350] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.689923506926837e+38 / 1.694758777200652e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 350] | torch.int64 → int64 | 0.0 / 349.0 / 174.5 / 101.03588471429346 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 350, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7840756014415196 / 0.8888353925731802 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 350, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10827774247004916 / 0.6268626933647311 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.05953917131490179 / 3.0744496662674394 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 350, 4096] | torch.bfloat16 → float32 | -12.5 / 14.6875 / 0.037134977869812125 / 1.382297783694288 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.05953917131490179 / 3.0744496662674394 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 350, 512] | torch.bfloat16 → float32 | -40.0 / 42.25 / 0.04809650410498892 / 3.472047354655263 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -191.0 / 144.0 / 0.05953917131490179 / 3.0744496662674394 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 350, 512] | torch.bfloat16 → float32 | -16.0 / 22.0 / -0.011609296713556563 / 2.5619954393546314 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 350, 4096] | torch.bfloat16 → float32 | -10.9375 / 12.875 / -0.013670524867287506 / 1.4569577237636862 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 350, 2880] | torch.bfloat16 → float32 | -480.0 / 438.0 / -0.0247458390517249 / 5.747403702361548 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -480.0 / 438.0 / -0.0247458390517249 / 5.747403702361548 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 350, 350] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002362265595177198 / 0.0162025578650778 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -41728.0 / 640.0 / 0.4339242356921 / 46.601972414709465 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 350, 2880] | torch.bfloat16 → float32 | -78.5 / 6.40625 / 0.009850431665896425 / 0.773488209963104 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -78.5 / 6.40625 / 0.009850431665896425 / 0.773488209963104 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [350, 2880] | torch.bfloat16 → float32 | -78.5 / 6.40625 / 0.009850431665896425 / 0.773488209963104 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [350, 2880] | torch.bfloat16 → float32 | -406.0 / 344.0 / 0.08500904859436881 / 7.749498493536357 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -406.0 / 344.0 / 0.08500904859436881 / 7.749498493536357 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [350, 32] | torch.bfloat16 → float32 | -10.75 / 2.953125 / -0.15960067067827496 / 0.7576412607686829 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 350, 2880] | torch.bfloat16 → float32 | -41728.0 / 772.0 / 0.5189327439807709 / 48.70440570875039 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -12672.0 / 14080.0 / -0.9634440380278089 / 421.9734128800355 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 350, 350] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.689923506926837e+38 / 1.694758777200652e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 350, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7840756014415196 / 0.8888353925731802 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 350, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10827774247004916 / 0.6268626933647311 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 350] | torch.int64 → int64 | 0.0 / 349.0 / 174.5 / 101.03588471429346 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -12672.0 / 14080.0 / -0.9634440380278089 / 421.9734128800355 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 350, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.010460601913550544 / 1.770045738338761 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 350, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.010460601913550544 / 1.770045738338761 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 350, 350] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.689923506926837e+38 / 1.694758777200652e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 350] | torch.int64 → int64 | 0.0 / 349.0 / 174.5 / 101.03588471429346 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 350, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7840756014415196 / 0.8888353925731802 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 350, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10827774247004916 / 0.6268626933647311 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.010460601913550544 / 1.770045738338761 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 350, 4096] | torch.bfloat16 → float32 | -20.375 / 25.125 / 0.03574005550766223 / 1.6607322565032818 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.010460601913550544 / 1.770045738338761 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 350, 512] | torch.bfloat16 → float32 | -78.0 / 57.25 / -0.10862952504307032 / 4.801356238631801 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -57.5 / 70.5 / 0.010460601913550544 / 1.770045738338761 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 350, 512] | torch.bfloat16 → float32 | -22.125 / 18.25 / -0.024697262729917253 / 3.270058105380325 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 350, 4096] | torch.bfloat16 → float32 | -19.125 / 14.75 / -0.008191121823180894 / 1.120369520898817 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 350, 2880] | torch.bfloat16 → float32 | -4480.0 / 4800.0 / 2.228843997882472 / 139.88326371668182 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -4480.0 / 4800.0 / 2.228843997882472 / 139.88326371668182 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 350, 350] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.001427865375764073 / 0.012048786859053489 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -11264.0 / 11392.0 / 1.2645137636699375 / 361.7581891081058 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 350, 2880] | torch.bfloat16 → float32 | -49.0 / 18.5 / -0.014549670328223518 / 1.2101643042325756 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -49.0 / 18.5 / -0.014549670328223518 / 1.2101643042325756 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [350, 2880] | torch.bfloat16 → float32 | -49.0 / 18.5 / -0.014549670328223518 / 1.2101643042325756 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [350, 2880] | torch.bfloat16 → float32 | -6528.0 / 6496.0 / -1.1482296971517896 / 155.8208815737602 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 350, 2880] | torch.bfloat16 → float32 | -6528.0 / 6496.0 / -1.1482296971517896 / 155.8208815737602 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [350, 32] | torch.bfloat16 → float32 | -6.625 / 3.859375 / 0.24825777326311385 / 2.46210892415992 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 350, 2880] | torch.bfloat16 → float32 | -11840.0 / 12032.0 / 0.11679534524584573 / 408.8008380701775 | [NPY](tensors/0000116.npy) |

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
