# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.013169299475159808 / 2.914082082900395 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 172, 172] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.7983398014363203e+38 / 1.6915978139258627e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 172, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8441919836887094 / 0.8480342676753228 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 172, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11758776786865742 / 0.6030870541716191 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 172] | torch.int64 → int64 | 0.0 / 171.0 / 85.5 / 49.65128397131337 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.013169299475159808 / 2.914082082900395 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 172, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006751385078860509 / 0.7602758702136114 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 172, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006751385078860509 / 0.7602758702136114 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 172, 172] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.7983398014363203e+38 / 1.6915978139258627e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 172] | torch.int64 → int64 | 0.0 / 171.0 / 85.5 / 49.65128397131337 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 172, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8441919836887094 / 0.8480342676753228 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 172, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11758776786865742 / 0.6030870541716191 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006751385078860509 / 0.7602758702136114 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 172, 4096] | torch.bfloat16 → float32 | -8.3125 / 12.8125 / 0.022467410454293377 / 1.017527438594557 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006751385078860509 / 0.7602758702136114 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 172, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.013672488893187323 / 5.844791493963608 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006751385078860509 / 0.7602758702136114 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 172, 512] | torch.bfloat16 → float32 | -7.375 / 7.71875 / -0.015074363628099132 / 1.1784495598839035 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 172, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / -0.006499787744513781 / 0.5398969978479191 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 172, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.02796577607546674 / 1.1610292150666779 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.02796577607546674 / 1.1610292150666779 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 172, 172] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002354370527506603 / 0.032077613395472326 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -87.5 / 70.5 / 0.014791505589349633 / 3.02813776074249 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 172, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0002655479351891258 / 0.3253713568309265 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0002655479351891258 / 0.3253713568309265 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [172, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0002655479351891258 / 0.3253713568309265 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [172, 2880] | torch.bfloat16 → float32 | -50.0 / 92.5 / 0.01854802265532257 / 0.9186318117082953 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -50.0 / 92.5 / 0.01854802265532257 / 0.9186318117082953 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [172, 32] | torch.bfloat16 → float32 | -4.9375 / 3.4375 / -0.10334751217864281 / 1.0471729392904792 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 172, 2880] | torch.bfloat16 → float32 | -89.5 / 106.0 / 0.03332774338026072 / 3.2459222206560363 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.4772781754032894 / 62.97596004297848 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 172, 172] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6849124057035249e+38 / 1.6947370511019625e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 172, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8441919836887094 / 0.8480342676753228 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 172, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11758776786865742 / 0.6030870541716191 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 172] | torch.int64 → int64 | 0.0 / 171.0 / 85.5 / 49.65128397131337 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.4772781754032894 / 62.97596004297848 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 172, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06480003658763929 / 3.1962334608644447 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 172, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06480003658763929 / 3.1962334608644447 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 172, 172] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6849124057035249e+38 / 1.6947370511019625e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 172] | torch.int64 → int64 | 0.0 / 171.0 / 85.5 / 49.65128397131337 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 172, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8441919836887094 / 0.8480342676753228 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 172, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11758776786865742 / 0.6030870541716191 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06480003658763929 / 3.1962334608644447 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 172, 4096] | torch.bfloat16 → float32 | -11.25 / 13.3125 / 0.035040477763898306 / 1.3292376058312425 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06480003658763929 / 3.1962334608644447 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 172, 512] | torch.bfloat16 → float32 | -38.25 / 45.25 / 0.05456242520297162 / 3.5868096420322884 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06480003658763929 / 3.1962334608644447 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 172, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.0379764917631482 / 2.476574468998607 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 172, 4096] | torch.bfloat16 → float32 | -11.8125 / 11.25 / -0.029750870924603035 / 1.4144292238443383 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 172, 2880] | torch.bfloat16 → float32 | -466.0 / 500.0 / -0.06019533261613444 / 7.333206378752886 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -466.0 / 500.0 / -0.06019533261613444 / 7.333206378752886 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 172, 172] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0046722930050579065 / 0.024312250661749843 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -41216.0 / 692.0 / 0.417071469748051 / 62.09339826979432 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 172, 2880] | torch.bfloat16 → float32 | -78.5 / 6.03125 / 0.008693153698969565 / 0.8006644275203059 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -78.5 / 6.03125 / 0.008693153698969565 / 0.8006644275203059 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [172, 2880] | torch.bfloat16 → float32 | -78.5 / 6.03125 / 0.008693153698969565 / 0.8006644275203059 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [172, 2880] | torch.bfloat16 → float32 | -504.0 / 402.0 / 0.12428145744387802 / 9.812723798668666 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -504.0 / 402.0 / 0.12428145744387802 / 9.812723798668666 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [172, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.16622194717096728 / 0.8210954936188499 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 172, 2880] | torch.bfloat16 → float32 | -41216.0 / 836.0 / 0.5413103709849276 / 64.23175170682775 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.6198003961134326 / 424.91424135524727 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 172, 172] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6849124057035249e+38 / 1.6947370511019625e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 172, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8441919836887094 / 0.8480342676753228 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 172, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11758776786865742 / 0.6030870541716191 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 172] | torch.int64 → int64 | 0.0 / 171.0 / 85.5 / 49.65128397131337 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.6198003961134326 / 424.91424135524727 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 172, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009109947666314068 / 1.7599899818664202 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 172, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009109947666314068 / 1.7599899818664202 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 172, 172] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6849124057035249e+38 / 1.6947370511019625e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 172] | torch.int64 → int64 | 0.0 / 171.0 / 85.5 / 49.65128397131337 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 172, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8441919836887094 / 0.8480342676753228 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 172, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11758776786865742 / 0.6030870541716191 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009109947666314068 / 1.7599899818664202 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 172, 4096] | torch.bfloat16 → float32 | -18.0 / 24.0 / 0.031372500122500264 / 1.6037915030468615 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009109947666314068 / 1.7599899818664202 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 172, 512] | torch.bfloat16 → float32 | -74.5 / 53.25 / -0.07951873196234796 / 4.815737144069469 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009109947666314068 / 1.7599899818664202 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 172, 512] | torch.bfloat16 → float32 | -24.75 / 24.125 / 0.0037412201595860856 / 3.095940340416259 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 172, 4096] | torch.bfloat16 → float32 | -22.875 / 12.9375 / -0.005420188028512162 / 1.1259233367122436 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 172, 2880] | torch.bfloat16 → float32 | -6016.0 / 6240.0 / 2.8568462840923967 / 166.8412638741477 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -6016.0 / 6240.0 / 2.8568462840923967 / 166.8412638741477 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 172, 172] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.002649945123430102 / 0.016662175764344766 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -10496.0 / 11200.0 / 1.2364586975531369 / 376.4933777459721 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 172, 2880] | torch.bfloat16 → float32 | -47.25 / 18.125 / -0.015020598434585626 / 1.1786301132119361 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -47.25 / 18.125 / -0.015020598434585626 / 1.1786301132119361 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [172, 2880] | torch.bfloat16 → float32 | -47.25 / 18.125 / -0.015020598434585626 / 1.1786301132119361 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [172, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.4790757304938265 / 157.61275822818155 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 172, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.4790757304938265 / 157.61275822818155 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [172, 32] | torch.bfloat16 → float32 | -7.1875 / 3.96875 / 0.24833036855209706 / 2.318279399619115 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 172, 2880] | torch.bfloat16 → float32 | -10688.0 / 10880.0 / -0.24058871010477223 / 437.81121177823735 | [NPY](tensors/0000116.npy) |

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
