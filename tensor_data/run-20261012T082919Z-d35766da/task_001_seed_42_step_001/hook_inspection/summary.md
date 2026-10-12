# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012422795310475644 / 2.8933548557168467 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 180, 180] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8295100288651497e+38 / 1.6894006996774762e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 180, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8420290523105197 / 0.850588800043922 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 180, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12341726031380758 / 0.6013614230539578 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 180] | torch.int64 → int64 | 0.0 / 179.0 / 89.5 / 51.96072234550504 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012422795310475644 / 2.8933548557168467 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 180, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006546246988187187 / 0.7600179711066508 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 180, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006546246988187187 / 0.7600179711066508 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 180, 180] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8295100288651497e+38 / 1.6894006996774762e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 180] | torch.int64 → int64 | 0.0 / 179.0 / 89.5 / 51.96072234550504 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 180, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8420290523105197 / 0.850588800043922 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 180, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12341726031380758 / 0.6013614230539578 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006546246988187187 / 0.7600179711066508 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 180, 4096] | torch.bfloat16 → float32 | -9.5625 / 12.8125 / 0.022302993797630837 / 1.0213077216692643 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006546246988187187 / 0.7600179711066508 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 180, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.012822060618135664 / 5.828725257311382 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006546246988187187 / 0.7600179711066508 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 180, 512] | torch.bfloat16 → float32 | -7.375 / 7.71875 / -0.016750096281369527 / 1.1873084149930146 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 180, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / -0.006856022670448238 / 0.5428765443812966 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 180, 2880] | torch.bfloat16 → float32 | -34.5 / 53.0 / 0.02823490622053124 / 1.1654117085232998 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -34.5 / 53.0 / 0.02823490622053124 / 1.1654117085232998 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 180, 180] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.00224074462830848 / 0.03136074681852985 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -87.5 / 70.5 / 0.015810253291770264 / 3.017213420126163 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 180, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.00034571661418418824 / 0.3288594712064392 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.00034571661418418824 / 0.3288594712064392 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [180, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.00034571661418418824 / 0.3288594712064392 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [180, 2880] | torch.bfloat16 → float32 | -50.0 / 92.5 / 0.018832312666891532 / 0.9186545358309172 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -50.0 / 92.5 / 0.018832312666891532 / 0.9186545358309172 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [180, 32] | torch.bfloat16 → float32 | -4.9375 / 3.4375 / -0.10357949998643663 / 1.0356384873480906 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 180, 2880] | torch.bfloat16 → float32 | -89.5 / 106.0 / 0.0346348723364465 / 3.243664129701024 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.4910849526487751 / 61.76014102539872 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 180, 180] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6853503296556246e+38 / 1.6947395406323769e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 180, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8420290523105197 / 0.850588800043922 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 180, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12341726031380758 / 0.6013614230539578 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 180] | torch.int64 → int64 | 0.0 / 179.0 / 89.5 / 51.96072234550504 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.4910849526487751 / 61.76014102539872 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 180, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.0646406320779136 / 3.1965242121576285 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 180, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.0646406320779136 / 3.1965242121576285 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 180, 180] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6853503296556246e+38 / 1.6947395406323769e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 180] | torch.int64 → int64 | 0.0 / 179.0 / 89.5 / 51.96072234550504 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 180, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8420290523105197 / 0.850588800043922 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 180, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12341726031380758 / 0.6013614230539578 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.0646406320779136 / 3.1965242121576285 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 180, 4096] | torch.bfloat16 → float32 | -11.25 / 13.3125 / 0.036081254804351676 / 1.3302911435979232 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.0646406320779136 / 3.1965242121576285 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 180, 512] | torch.bfloat16 → float32 | -41.5 / 44.0 / 0.05755087577530907 / 3.5958499688282983 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.0646406320779136 / 3.1965242121576285 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 180, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.03923504004875819 / 2.472025382136268 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 180, 4096] | torch.bfloat16 → float32 | -11.75 / 11.25 / -0.03072821352116585 / 1.4060819611845221 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 180, 2880] | torch.bfloat16 → float32 | -466.0 / 500.0 / -0.061646914835214436 / 7.374006641641114 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -466.0 / 500.0 / -0.061646914835214436 / 7.374006641641114 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 180, 180] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004470211848405832 / 0.02412616618317913 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -41216.0 / 692.0 / 0.42949706265955795 / 60.84278170972988 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 180, 2880] | torch.bfloat16 → float32 | -78.5 / 6.0 / 0.009062058142857788 / 0.8002736967938144 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -78.5 / 6.0 / 0.009062058142857788 / 0.8002736967938144 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [180, 2880] | torch.bfloat16 → float32 | -78.5 / 6.0 / 0.009062058142857788 / 0.8002736967938144 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [180, 2880] | torch.bfloat16 → float32 | -508.0 / 406.0 / 0.1265130071581146 / 9.792350036680883 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -508.0 / 406.0 / 0.1265130071581146 / 9.792350036680883 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [180, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.16697910096910265 / 0.8186053474748173 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 180, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5561445207949038 / 63.01935734834799 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.6800020966706453 / 426.2169397163489 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 180, 180] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6853503296556246e+38 / 1.6947395406323769e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 180, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8420290523105197 / 0.850588800043922 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 180, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12341726031380758 / 0.6013614230539578 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 180] | torch.int64 → int64 | 0.0 / 179.0 / 89.5 / 51.96072234550504 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.6800020966706453 / 426.2169397163489 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 180, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.008965133351308328 / 1.7603151469072447 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 180, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.008965133351308328 / 1.7603151469072447 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 180, 180] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6853503296556246e+38 / 1.6947395406323769e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 180] | torch.int64 → int64 | 0.0 / 179.0 / 89.5 / 51.96072234550504 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 180, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8420290523105197 / 0.850588800043922 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 180, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12341726031380758 / 0.6013614230539578 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.008965133351308328 / 1.7603151469072447 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 180, 4096] | torch.bfloat16 → float32 | -18.0 / 24.0 / 0.032074018095570665 / 1.6127020275295056 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.008965133351308328 / 1.7603151469072447 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 180, 512] | torch.bfloat16 → float32 | -81.5 / 55.0 / -0.07700549374179294 / 4.844108972837185 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.008965133351308328 / 1.7603151469072447 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 180, 512] | torch.bfloat16 → float32 | -24.375 / 24.125 / 0.003684670395321316 / 3.118825930176184 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 180, 4096] | torch.bfloat16 → float32 | -22.625 / 12.9375 / -0.005164756160512399 / 1.122493482517871 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 180, 2880] | torch.bfloat16 → float32 | -6016.0 / 6240.0 / 2.8162521269779517 / 165.97387306485416 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -6016.0 / 6240.0 / 2.8162521269779517 / 165.97387306485416 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 180, 180] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.002508575124753757 / 0.01623855331416929 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -10496.0 / 11200.0 / 1.1353420700261623 / 374.9437966389996 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 180, 2880] | torch.bfloat16 → float32 | -47.0 / 20.0 / -0.014844848338836506 / 1.1830211832359352 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -47.0 / 20.0 / -0.014844848338836506 / 1.1830211832359352 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [180, 2880] | torch.bfloat16 → float32 | -47.0 / 20.0 / -0.014844848338836506 / 1.1830211832359352 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [180, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.4444619937001923 / 156.97219683239072 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 180, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.4444619937001923 / 156.97219683239072 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [180, 32] | torch.bfloat16 → float32 | -7.125 / 3.984375 / 0.24419949584537082 / 2.3385627790293535 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 180, 2880] | torch.bfloat16 → float32 | -10688.0 / 10880.0 / -0.3085437878267264 / 435.0461710568076 | [NPY](tensors/0000116.npy) |

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
