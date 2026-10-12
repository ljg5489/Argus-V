# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -95.0 / 72.0 / -0.014616249807942143 / 2.771657515200314 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 416, 416] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.5057963191988977e+38 / 1.4881062077973063e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 416, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7805841172543856 / 0.8848249184897391 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 416, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10879501749751888 / 0.6367559954185894 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 416] | torch.int64 → int64 | 0.0 / 415.0 / 207.5 / 120.08850902563492 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -95.0 / 72.0 / -0.014616249807942143 / 2.771657515200314 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 416, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007725746308340947 / 0.7706710684872734 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 416, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007725746308340947 / 0.7706710684872734 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 416, 416] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.5057963191988977e+38 / 1.4881062077973063e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 416] | torch.int64 → int64 | 0.0 / 415.0 / 207.5 / 120.08850902563492 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 416, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7805841172543856 / 0.8848249184897391 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 416, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10879501749751888 / 0.6367559954185894 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007725746308340947 / 0.7706710684872734 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 416, 4096] | torch.bfloat16 → float32 | -9.0625 / 11.8125 / 0.02349520568350272 / 1.0148219307299207 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007725746308340947 / 0.7706710684872734 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 416, 512] | torch.bfloat16 → float32 | -63.5 / 65.5 / 0.02615722078861346 / 5.768792444075628 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -30.75 / 15.0 / -0.007725746308340947 / 0.7706710684872734 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 416, 512] | torch.bfloat16 → float32 | -7.375 / 7.25 / -0.00959187262910396 / 1.2036116919143538 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 416, 4096] | torch.bfloat16 → float32 | -6.8125 / 6.40625 / -0.004702672475558562 / 0.5441093082921535 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 416, 2880] | torch.bfloat16 → float32 | -38.5 / 52.25 / 0.02709381563631762 / 1.190887383795915 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -38.5 / 52.25 / 0.02709381563631762 / 1.190887383795915 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 416, 416] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0009591302711556809 / 0.019758882210620665 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -87.5 / 64.5 / 0.012473893224492544 / 2.9859297745696898 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 416, 2880] | torch.bfloat16 → float32 | -6.59375 / 3.0625 / 0.0004735950519366619 / 0.33497461856031635 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -6.59375 / 3.0625 / 0.0004735950519366619 / 0.33497461856031635 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [416, 2880] | torch.bfloat16 → float32 | -6.59375 / 3.0625 / 0.0004735950519366619 / 0.33497461856031635 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [416, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.0161163856023644 / 0.8328115095339921 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.0161163856023644 / 0.8328115095339921 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [416, 32] | torch.bfloat16 → float32 | -5.1875 / 3.40625 / -0.11156867559139545 / 0.9921942724648087 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 416, 2880] | torch.bfloat16 → float32 | -91.0 / 156.0 / 0.02858087685054693 / 3.240967771457284 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -41728.0 / 1088.0 / 0.45869515471988254 / 43.84249287183163 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 416, 416] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6906917386290712e+38 / 1.6947607980369672e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 416, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7805841172543856 / 0.8848249184897391 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 416, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10879501749751888 / 0.6367559954185894 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 416] | torch.int64 → int64 | 0.0 / 415.0 / 207.5 / 120.08850902563492 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -41728.0 / 1088.0 / 0.45869515471988254 / 43.84249287183163 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 416, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.061159528727428275 / 3.0537104172303993 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 416, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.061159528727428275 / 3.0537104172303993 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 416, 416] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6906917386290712e+38 / 1.6947607980369672e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 416] | torch.int64 → int64 | 0.0 / 415.0 / 207.5 / 120.08850902563492 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 416, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7805841172543856 / 0.8848249184897391 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 416, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10879501749751888 / 0.6367559954185894 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.061159528727428275 / 3.0537104172303993 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 416, 4096] | torch.bfloat16 → float32 | -12.375 / 14.625 / 0.038474023360733474 / 1.3889259363740336 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.061159528727428275 / 3.0537104172303993 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 416, 512] | torch.bfloat16 → float32 | -42.5 / 43.5 / 0.054839982240642154 / 3.5445297418334074 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.061159528727428275 / 3.0537104172303993 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 416, 512] | torch.bfloat16 → float32 | -16.0 / 22.0 / -0.01619760860306157 / 2.568131677640758 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 416, 4096] | torch.bfloat16 → float32 | -11.3125 / 12.9375 / -0.015594527731708968 / 1.4882764695328246 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 416, 2880] | torch.bfloat16 → float32 | -486.0 / 440.0 / -0.01706529995904137 / 5.644069466306636 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -486.0 / 440.0 / -0.01706529995904137 / 5.644069466306636 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 416, 416] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002028747189027194 / 0.01451650491339905 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -41728.0 / 636.0 / 0.44161926505402627 / 43.443582564536854 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 416, 2880] | torch.bfloat16 → float32 | -78.5 / 6.40625 / 0.009623775574125939 / 0.7713852528462147 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -78.5 / 6.40625 / 0.009623775574125939 / 0.7713852528462147 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [416, 2880] | torch.bfloat16 → float32 | -78.5 / 6.40625 / 0.009623775574125939 / 0.7713852528462147 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [416, 2880] | torch.bfloat16 → float32 | -410.0 / 342.0 / 0.08368837151867457 / 7.5969705506657235 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -410.0 / 342.0 / 0.08368837151867457 / 7.5969705506657235 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [416, 32] | torch.bfloat16 → float32 | -10.75 / 3.46875 / -0.15664285879868728 / 0.7473450734119147 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 416, 2880] | torch.bfloat16 → float32 | -41728.0 / 776.0 / 0.5252839444030044 / 45.61192853257442 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -12672.0 / 14080.0 / -1.078143936344701 / 414.716948343653 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 416, 416] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6906917386290712e+38 / 1.6947607980369672e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 416, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7805841172543856 / 0.8848249184897391 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 416, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10879501749751888 / 0.6367559954185894 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 416] | torch.int64 → int64 | 0.0 / 415.0 / 207.5 / 120.08850902563492 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -12672.0 / 14080.0 / -1.078143936344701 / 414.716948343653 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 416, 2880] | torch.bfloat16 → float32 | -57.25 / 70.0 / 0.010352600588558766 / 1.7663036120724516 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 416, 2880] | torch.bfloat16 → float32 | -57.25 / 70.0 / 0.010352600588558766 / 1.7663036120724516 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 416, 416] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6906917386290712e+38 / 1.6947607980369672e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 416] | torch.int64 → int64 | 0.0 / 415.0 / 207.5 / 120.08850902563492 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 416, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7805841172543856 / 0.8848249184897391 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 416, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10879501749751888 / 0.6367559954185894 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -57.25 / 70.0 / 0.010352600588558766 / 1.7663036120724516 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 416, 4096] | torch.bfloat16 → float32 | -19.625 / 25.0 / 0.03472414630558573 / 1.6739693528270974 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -57.25 / 70.0 / 0.010352600588558766 / 1.7663036120724516 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 416, 512] | torch.bfloat16 → float32 | -87.0 / 60.25 / -0.10794457317811415 / 4.9065357250316 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -57.25 / 70.0 / 0.010352600588558766 / 1.7663036120724516 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 416, 512] | torch.bfloat16 → float32 | -21.875 / 18.125 / -0.02159478481973145 / 3.2568008051004087 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 416, 4096] | torch.bfloat16 → float32 | -19.75 / 14.625 / -0.006088242716141568 / 1.1277215231320707 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 416, 2880] | torch.bfloat16 → float32 | -4480.0 / 4800.0 / 2.2899124568352143 / 137.81627374527338 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -4480.0 / 4800.0 / 2.2899124568352143 / 137.81627374527338 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 416, 416] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0012583199044700873 / 0.010898241534549654 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -11200.0 / 11328.0 / 1.2113627246302416 / 358.55130065130555 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 416, 2880] | torch.bfloat16 → float32 | -49.0 / 26.125 / -0.01476686036365473 / 1.2236351108898578 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -49.0 / 26.125 / -0.01476686036365473 / 1.2236351108898578 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [416, 2880] | torch.bfloat16 → float32 | -49.0 / 26.125 / -0.01476686036365473 / 1.2236351108898578 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [416, 2880] | torch.bfloat16 → float32 | -6624.0 / 6592.0 / -1.1788047301208868 / 151.50708976354377 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 416, 2880] | torch.bfloat16 → float32 | -6624.0 / 6592.0 / -1.1788047301208868 / 151.50708976354377 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [416, 32] | torch.bfloat16 → float32 | -7.40625 / 4.125 / 0.25645414224037755 / 2.5334119343544725 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 416, 2880] | torch.bfloat16 → float32 | -11776.0 / 11968.0 / 0.032151347755366946 / 399.9826704804703 | [NPY](tensors/0000116.npy) |

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
