# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012043011286164248 / 2.898192910993545 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 275, 275] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.1761575873365923e+38 / 1.6249592626624985e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 275, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8087255521254106 / 0.8694707101685584 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 275, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11789227544054896 / 0.6208978682508439 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 275] | torch.int64 → int64 | 0.0 / 274.0 / 137.0 / 79.38513714795737 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012043011286164248 / 2.898192910993545 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 275, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0060584400454442005 / 0.7536744215060942 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 275, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0060584400454442005 / 0.7536744215060942 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 275, 275] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.1761575873365923e+38 / 1.6249592626624985e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 275] | torch.int64 → int64 | 0.0 / 274.0 / 137.0 / 79.38513714795737 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 275, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8087255521254106 / 0.8694707101685584 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 275, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11789227544054896 / 0.6208978682508439 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0060584400454442005 / 0.7536744215060942 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 275, 4096] | torch.bfloat16 → float32 | -9.5 / 12.8125 / 0.019823491849304195 / 1.0220396821343591 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0060584400454442005 / 0.7536744215060942 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 275, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.020917673381892116 / 5.813821907782106 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0060584400454442005 / 0.7536744215060942 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 275, 512] | torch.bfloat16 → float32 | -7.375 / 7.71875 / -0.016018522435968574 / 1.173565544442528 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 275, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / -0.005993012926243531 / 0.5422840245293317 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 275, 2880] | torch.bfloat16 → float32 | -38.25 / 56.25 / 0.028064116317576566 / 1.1827096209028711 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -38.25 / 56.25 / 0.028064116317576566 / 1.1827096209028711 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 275, 275] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0015037308566995295 / 0.025322068487532448 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -87.5 / 71.0 / 0.016029815993525764 / 3.029554582700477 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 275, 2880] | torch.bfloat16 → float32 | -7.25 / 3.8125 / 0.0003516659388186956 / 0.3247133552868594 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -7.25 / 3.8125 / 0.0003516659388186956 / 0.3247133552868594 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [275, 2880] | torch.bfloat16 → float32 | -7.25 / 3.8125 / 0.0003516659388186956 / 0.3247133552868594 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [275, 2880] | torch.bfloat16 → float32 | -50.0 / 93.0 / 0.017821974749516956 / 0.8834303054942675 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -50.0 / 93.0 / 0.017821974749516956 / 0.8834303054942675 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [275, 32] | torch.bfloat16 → float32 | -5.0625 / 3.4375 / -0.10082599986683238 / 1.0568637067187043 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 275, 2880] | torch.bfloat16 → float32 | -89.0 / 106.5 / 0.03384557496176826 / 3.2231230090359992 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.5056059493247909 / 51.2403587016383 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 275, 275] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.688602910281674e+38 / 1.6947544895262821e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 275, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8087255521254106 / 0.8694707101685584 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 275, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11789227544054896 / 0.6208978682508439 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 275] | torch.int64 → int64 | 0.0 / 274.0 / 137.0 / 79.38513714795737 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.5056059493247909 / 51.2403587016383 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 275, 2880] | torch.bfloat16 → float32 | -191.0 / 136.0 / 0.06691005570840353 / 3.1799535107433443 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 275, 2880] | torch.bfloat16 → float32 | -191.0 / 136.0 / 0.06691005570840353 / 3.1799535107433443 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 275, 275] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.688602910281674e+38 / 1.6947544895262821e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 275] | torch.int64 → int64 | 0.0 / 274.0 / 137.0 / 79.38513714795737 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 275, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8087255521254106 / 0.8694707101685584 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 275, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11789227544054896 / 0.6208978682508439 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -191.0 / 136.0 / 0.06691005570840353 / 3.1799535107433443 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 275, 4096] | torch.bfloat16 → float32 | -11.375 / 13.3125 / 0.03609575405109684 / 1.3319925053174728 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -191.0 / 136.0 / 0.06691005570840353 / 3.1799535107433443 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 275, 512] | torch.bfloat16 → float32 | -38.5 / 49.5 / 0.07472077310085297 / 3.7445762776458684 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -191.0 / 136.0 / 0.06691005570840353 / 3.1799535107433443 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 275, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.02672270043329759 / 2.506210345953699 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 275, 4096] | torch.bfloat16 → float32 | -11.6875 / 12.0625 / -0.025062273720862074 / 1.4427737183272609 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 275, 2880] | torch.bfloat16 → float32 | -466.0 / 502.0 / -0.03028827526804173 / 6.602319361859073 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -466.0 / 502.0 / -0.03028827526804173 / 6.602319361859073 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 275, 275] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0030674911593380197 / 0.0182578313485453 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -41216.0 / 720.0 / 0.475350935271292 / 50.463915838450575 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 275, 2880] | torch.bfloat16 → float32 | -78.5 / 6.03125 / 0.010712563181107845 / 0.7867405777420912 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -78.5 / 6.03125 / 0.010712563181107845 / 0.7867405777420912 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [275, 2880] | torch.bfloat16 → float32 | -78.5 / 6.03125 / 0.010712563181107845 / 0.7867405777420912 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [275, 2880] | torch.bfloat16 → float32 | -540.0 / 452.0 / 0.13341148414455278 / 9.33104162130408 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -540.0 / 452.0 / 0.13341148414455278 / 9.33104162130408 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [275, 32] | torch.bfloat16 → float32 | -10.6875 / 2.859375 / -0.15270284219221636 / 0.7580505417260784 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 275, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.6087224863996409 / 52.88053992456215 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -1.5014842553957548 / 411.3118833259886 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 275, 275] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.688602910281674e+38 / 1.6947544895262821e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 275, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8087255521254106 / 0.8694707101685584 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 275, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11789227544054896 / 0.6208978682508439 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 275] | torch.int64 → int64 | 0.0 / 274.0 / 137.0 / 79.38513714795737 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -1.5014842553957548 / 411.3118833259886 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 275, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.009581495929848066 / 1.7565028830744167 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 275, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.009581495929848066 / 1.7565028830744167 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 275, 275] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.688602910281674e+38 / 1.6947544895262821e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 275] | torch.int64 → int64 | 0.0 / 274.0 / 137.0 / 79.38513714795737 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 275, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8087255521254106 / 0.8694707101685584 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 275, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11789227544054896 / 0.6208978682508439 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.009581495929848066 / 1.7565028830744167 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 275, 4096] | torch.bfloat16 → float32 | -20.375 / 23.75 / 0.030396013659694954 / 1.6266071654309957 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.009581495929848066 / 1.7565028830744167 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 275, 512] | torch.bfloat16 → float32 | -88.5 / 66.5 / -0.08013486260717566 / 5.102797804887125 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -53.25 / 72.0 / 0.009581495929848066 / 1.7565028830744167 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 275, 512] | torch.bfloat16 → float32 | -26.125 / 24.5 / 0.0053776273944161155 / 3.1257162952185107 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 275, 4096] | torch.bfloat16 → float32 | -22.875 / 12.9375 / -0.005203936218924809 / 1.1485133393011107 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 275, 2880] | torch.bfloat16 → float32 | -6336.0 / 6688.0 / 2.824836888222983 / 170.2748987339941 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -6336.0 / 6688.0 / 2.824836888222983 / 170.2748987339941 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 275, 275] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.0018189565387544495 / 0.012829351463815768 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -11328.0 / 11392.0 / 1.3208138917865173 / 380.4581185215055 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 275, 2880] | torch.bfloat16 → float32 | -48.5 / 20.75 / -0.01517145305465568 / 1.1892829051437892 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -48.5 / 20.75 / -0.01517145305465568 / 1.1892829051437892 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [275, 2880] | torch.bfloat16 → float32 | -48.5 / 20.75 / -0.01517145305465568 / 1.1892829051437892 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [275, 2880] | torch.bfloat16 → float32 | -4832.0 / 4736.0 / -1.5974329407046541 / 147.31935061702663 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 275, 2880] | torch.bfloat16 → float32 | -4832.0 / 4736.0 / -1.5974329407046541 / 147.31935061702663 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [275, 32] | torch.bfloat16 → float32 | -7.21875 / 4.03125 / 0.22943378621881658 / 2.3069557936312988 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 275, 2880] | torch.bfloat16 → float32 | -10816.0 / 10880.0 / -0.2768861762152778 / 424.45114886997715 | [NPY](tensors/0000116.npy) |

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
