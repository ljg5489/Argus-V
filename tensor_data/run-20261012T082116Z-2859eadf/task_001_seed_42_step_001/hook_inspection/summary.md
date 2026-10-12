# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 731 full tensors; 950 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Outside Transformer blocks

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model` | 0 | `input.kwargs['input_ids']` | [1, 178] | torch.int64 → int64 | 11.0 / 191268.0 / 15487.140449438202 / 31299.690510862558 | [NPY](tensors/0000000.npy) |
| 1 | `model` | 0 | `input.kwargs['attention_mask']` | [1, 178] | torch.int64 → int64 | 1.0 / 1.0 / 1.0 / 0.0 | [NPY](tensors/0000001.npy) |
| 2 | `model` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 3 | `model` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 4 | `model` | 0 | `input.kwargs['return_dict']` | — | bool | True | — |
| 5 | `model.embed_tokens` | 0 | `input.args[0]` | [1, 178] | torch.int64 → int64 | 11.0 / 191268.0 / 15487.140449438202 / 31299.690510862558 | [NPY](tensors/0000005.npy) |
| 6 | `model.embed_tokens` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012427776665720371 / 2.9036417695607883 | [NPY](tensors/0000006.npy) |
| 7 | `model.rotary_emb` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012427776665720371 / 2.9036417695607883 | [NPY](tensors/0000007.npy) |
| 8 | `model.rotary_emb` | 0 | `input.args[1]` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000008.npy) |
| 9 | `model.rotary_emb` | 0 | `output[0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000009.npy) |
| 10 | `model.rotary_emb` | 0 | `output[1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000010.npy) |
| 947 | `model.norm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -10688.0 / 10880.0 / -0.18595643156625508 / 435.79241908750373 | [NPY](tensors/0000947.npy) |
| 948 | `model.norm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -334.0 / 188.0 / -0.01388053661130936 / 5.778989565763847 | [NPY](tensors/0000948.npy) |
| 949 | `model` | 0 | `output['last_hidden_state']` | [1, 178, 2880] | torch.bfloat16 → float32 | -334.0 / 188.0 / -0.01388053661130936 / 5.778989565763847 | [NPY](tensors/0000949.npy) |

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | `model.layers.0` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012427776665720371 / 2.9036417695607883 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000013.npy) |
| 14 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000014.npy) |
| 15 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 17 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 18 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 19 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012427776665720371 / 2.9036417695607883 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006481495284831173 / 0.7597855329591284 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006481495284831173 / 0.7597855329591284 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 25 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 26 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 29 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006481495284831173 / 0.7597855329591284 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -8.3125 / 12.8125 / 0.02196034138708793 / 1.0187042618512012 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006481495284831173 / 0.7597855329591284 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.014537226450577211 / 5.846561630499018 | [NPY](tensors/0000032.npy) |
| 33 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006481495284831173 / 0.7597855329591284 | [NPY](tensors/0000033.npy) |
| 34 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -7.375 / 7.71875 / -0.01590049836073029 / 1.185397127218064 | [NPY](tensors/0000034.npy) |
| 35 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / -0.0067246733135720525 / 0.5391182245120474 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -35.25 / 52.5 / 0.02801192100243393 / 1.1692208101828656 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -35.25 / 52.5 / 0.02801192100243393 / 1.1692208101828656 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0022595663984016482 / 0.03139782421317883 | [NPY](tensors/0000038.npy) |
| 39 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -87.5 / 70.5 / 0.015582338105724397 / 3.0280010721270774 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.00031469223251131444 / 0.3255851667606249 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.00031469223251131444 / 0.3255851667606249 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.00031469223251131444 / 0.3255851667606249 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 44 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 45 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 46 | `model.layers.0.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -50.0 / 92.5 / 0.01827109002237314 / 0.9103146566858126 | [NPY](tensors/0000046.npy) |
| 47 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -50.0 / 92.5 / 0.01827109002237314 / 0.9103146566858126 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.0.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -4.9375 / 3.4375 / -0.10429315888479854 / 1.040232740200142 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.0` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -89.5 / 106.0 / 0.033844796362589954 / 3.248864517670903 | [NPY](tensors/0000049.npy) |

## Layer 0001

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | `model.layers.1` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -89.5 / 106.0 / 0.033844796362589954 / 3.248864517670903 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.1` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.1` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000052.npy) |
| 53 | `model.layers.1` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000053.npy) |
| 54 | `model.layers.1` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.1` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 56 | `model.layers.1` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 57 | `model.layers.1` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 58 | `model.layers.1.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -89.5 / 106.0 / 0.033844796362589954 / 3.248864517670903 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.1.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.0070827932686506586 / 0.850946416355038 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.1.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.0070827932686506586 / 0.850946416355038 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.1.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.1.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 64 | `model.layers.1.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 65 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.1.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 68 | `model.layers.1.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.0070827932686506586 / 0.850946416355038 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.1.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -11.25 / 12.25 / -0.021680805011313302 / 1.103541995212041 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.1.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.0070827932686506586 / 0.850946416355038 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.1.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -109.0 / 39.5 / -0.7145060362775674 / 7.748947293455757 | [NPY](tensors/0000071.npy) |
| 72 | `model.layers.1.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.0070827932686506586 / 0.850946416355038 | [NPY](tensors/0000072.npy) |
| 73 | `model.layers.1.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -6.0 / 5.84375 / 0.015013363254204225 / 0.9830552430207073 | [NPY](tensors/0000073.npy) |
| 74 | `model.layers.1.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -5.8125 / 4.9375 / 0.0017971128329195432 / 0.4439522725650832 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.1.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -33.75 / 49.75 / 0.0029022545388931132 / 0.8408718484794229 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.1.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -33.75 / 49.75 / 0.0029022545388931132 / 0.8408718484794229 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.1.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003740084137698784 / 0.028625845407400975 | [NPY](tensors/0000077.npy) |
| 78 | `model.layers.1.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -76.5 / 78.5 / 0.03674586682432748 / 3.2291915543545797 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.1.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.40625 / -0.0003848509291552017 / 0.3548916945600512 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.1.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.40625 / -0.0003848509291552017 / 0.3548916945600512 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.1.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.40625 / -0.0003848509291552017 / 0.3548916945600512 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.1.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 83 | `model.layers.1.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 84 | `model.layers.1.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 85 | `model.layers.1.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -31.875 / 66.0 / 0.02353743861770064 / 1.0809875399104385 | [NPY](tensors/0000085.npy) |
| 86 | `model.layers.1.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -31.875 / 66.0 / 0.02353743861770064 / 1.0809875399104385 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.1.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -2.640625 / 2.59375 / -0.07244974173856585 / 0.7346347524650604 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.1` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -95.0 / 119.0 / 0.060295790709210983 / 3.765463537744747 | [NPY](tensors/0000088.npy) |

## Layer 0002

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 89 | `model.layers.2` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -95.0 / 119.0 / 0.060295790709210983 / 3.765463537744747 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.2` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.2` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000091.npy) |
| 92 | `model.layers.2` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000092.npy) |
| 93 | `model.layers.2` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.2` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 95 | `model.layers.2` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 96 | `model.layers.2` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 97 | `model.layers.2.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -95.0 / 119.0 / 0.060295790709210983 / 3.765463537744747 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.2.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -29.125 / 23.375 / 0.012324813385139431 / 0.8619326348302144 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.2.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -29.125 / 23.375 / 0.012324813385139431 / 0.8619326348302144 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.2.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.2.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 103 | `model.layers.2.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 104 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.2.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 107 | `model.layers.2.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -29.125 / 23.375 / 0.012324813385139431 / 0.8619326348302144 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.2.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -13.75 / 8.375 / 0.03940762477039121 / 0.8749436667715405 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.2.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -29.125 / 23.375 / 0.012324813385139431 / 0.8619326348302144 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.2.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -25.875 / 22.5 / -0.01855409358826916 / 2.5625214691562057 | [NPY](tensors/0000110.npy) |
| 111 | `model.layers.2.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -29.125 / 23.375 / 0.012324813385139431 / 0.8619326348302144 | [NPY](tensors/0000111.npy) |
| 112 | `model.layers.2.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -8.0625 / 5.84375 / 0.022868728286094882 / 1.1649787522120547 | [NPY](tensors/0000112.npy) |
| 113 | `model.layers.2.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -6.5 / 5.28125 / 0.01350501020149129 / 0.475227464490052 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.2.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41.5 / 52.0 / 0.0017041130763735537 / 0.9958793594505769 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.2.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41.5 / 52.0 / 0.0017041130763735537 / 0.9958793594505769 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.2.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0027347297842863385 / 0.02367255496227564 | [NPY](tensors/0000116.npy) |
| 117 | `model.layers.2.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -84.0 / 123.5 / 0.062009713875964635 / 3.720302881871745 | [NPY](tensors/0000117.npy) |
| 118 | `model.layers.2.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.21875 / 0.0015722589713803837 / 0.45427002725346766 | [NPY](tensors/0000118.npy) |
| 119 | `model.layers.2.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.21875 / 0.0015722589713803837 / 0.45427002725346766 | [NPY](tensors/0000119.npy) |
| 120 | `model.layers.2.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.21875 / 0.0015722589713803837 / 0.45427002725346766 | [NPY](tensors/0000120.npy) |
| 121 | `model.layers.2.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 122 | `model.layers.2.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 123 | `model.layers.2.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 124 | `model.layers.2.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -66.0 / 88.0 / 0.0323237972582845 / 1.3916783208715438 | [NPY](tensors/0000124.npy) |
| 125 | `model.layers.2.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -66.0 / 88.0 / 0.0323237972582845 / 1.3916783208715438 | [NPY](tensors/0000125.npy) |
| 126 | `model.layers.2.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -3.09375 / 2.21875 / -0.09099921215786023 / 0.6631636018247598 | [NPY](tensors/0000126.npy) |
| 127 | `model.layers.2` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -120.5 / 148.0 / 0.09433642859464876 / 4.49438629180344 | [NPY](tensors/0000127.npy) |

## Layer 0003

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | `model.layers.3` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -120.5 / 148.0 / 0.09433642859464876 / 4.49438629180344 | [NPY](tensors/0000128.npy) |
| 129 | `model.layers.3` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000129.npy) |
| 130 | `model.layers.3` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000130.npy) |
| 131 | `model.layers.3` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000131.npy) |
| 132 | `model.layers.3` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000132.npy) |
| 133 | `model.layers.3` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 134 | `model.layers.3` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 135 | `model.layers.3` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 136 | `model.layers.3.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -120.5 / 148.0 / 0.09433642859464876 / 4.49438629180344 | [NPY](tensors/0000136.npy) |
| 137 | `model.layers.3.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -59.75 / 56.75 / 0.03513888818596707 / 1.279258675498941 | [NPY](tensors/0000137.npy) |
| 138 | `model.layers.3.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -59.75 / 56.75 / 0.03513888818596707 / 1.279258675498941 | [NPY](tensors/0000138.npy) |
| 139 | `model.layers.3.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000139.npy) |
| 140 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000140.npy) |
| 141 | `model.layers.3.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 142 | `model.layers.3.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 143 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000143.npy) |
| 144 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000144.npy) |
| 145 | `model.layers.3.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 146 | `model.layers.3.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -59.75 / 56.75 / 0.03513888818596707 / 1.279258675498941 | [NPY](tensors/0000146.npy) |
| 147 | `model.layers.3.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -12.5625 / 9.0 / -0.024263414648108723 / 1.1043270524821902 | [NPY](tensors/0000147.npy) |
| 148 | `model.layers.3.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -59.75 / 56.75 / 0.03513888818596707 / 1.279258675498941 | [NPY](tensors/0000148.npy) |
| 149 | `model.layers.3.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -78.5 / 56.5 / -0.07232106338893429 / 4.831243552887683 | [NPY](tensors/0000149.npy) |
| 150 | `model.layers.3.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -59.75 / 56.75 / 0.03513888818596707 / 1.279258675498941 | [NPY](tensors/0000150.npy) |
| 151 | `model.layers.3.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -7.5 / 11.4375 / 0.018437433276283607 / 0.9646576644534357 | [NPY](tensors/0000151.npy) |
| 152 | `model.layers.3.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -3.671875 / 3.234375 / 0.008883367305607955 / 0.3141909265962711 | [NPY](tensors/0000152.npy) |
| 153 | `model.layers.3.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -62.75 / 40.5 / -0.0074426485492688575 / 1.0494741792538405 | [NPY](tensors/0000153.npy) |
| 154 | `model.layers.3.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -62.75 / 40.5 / -0.0074426485492688575 / 1.0494741792538405 | [NPY](tensors/0000154.npy) |
| 155 | `model.layers.3.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.9765625 / 0.002727582562831128 / 0.016432484886321437 | [NPY](tensors/0000155.npy) |
| 156 | `model.layers.3.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -103.0 / 133.0 / 0.08690255215105491 / 4.406667078545549 | [NPY](tensors/0000156.npy) |
| 157 | `model.layers.3.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -6.0 / 5.71875 / 0.004673459047170242 / 0.5169679310820312 | [NPY](tensors/0000157.npy) |
| 158 | `model.layers.3.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -6.0 / 5.71875 / 0.004673459047170242 / 0.5169679310820312 | [NPY](tensors/0000158.npy) |
| 159 | `model.layers.3.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -6.0 / 5.71875 / 0.004673459047170242 / 0.5169679310820312 | [NPY](tensors/0000159.npy) |
| 160 | `model.layers.3.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 161 | `model.layers.3.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 162 | `model.layers.3.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 163 | `model.layers.3.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -61.25 / 93.0 / 0.026017863241102217 / 1.5100906240810081 | [NPY](tensors/0000163.npy) |
| 164 | `model.layers.3.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -61.25 / 93.0 / 0.026017863241102217 / 1.5100906240810081 | [NPY](tensors/0000164.npy) |
| 165 | `model.layers.3.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -3.453125 / 1.828125 / -0.07172635967811841 / 0.5441132239502202 | [NPY](tensors/0000165.npy) |
| 166 | `model.layers.3` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -150.0 / 172.0 / 0.11290513629770457 / 5.292142197541945 | [NPY](tensors/0000166.npy) |

## Layer 0004

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 167 | `model.layers.4` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -150.0 / 172.0 / 0.11290513629770457 / 5.292142197541945 | [NPY](tensors/0000167.npy) |
| 168 | `model.layers.4` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000168.npy) |
| 169 | `model.layers.4` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000169.npy) |
| 170 | `model.layers.4` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000170.npy) |
| 171 | `model.layers.4` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000171.npy) |
| 172 | `model.layers.4` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 173 | `model.layers.4` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 174 | `model.layers.4` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 175 | `model.layers.4.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -150.0 / 172.0 / 0.11290513629770457 / 5.292142197541945 | [NPY](tensors/0000175.npy) |
| 176 | `model.layers.4.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.020551572195934446 / 1.144579976320253 | [NPY](tensors/0000176.npy) |
| 177 | `model.layers.4.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.020551572195934446 / 1.144579976320253 | [NPY](tensors/0000177.npy) |
| 178 | `model.layers.4.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000178.npy) |
| 179 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000179.npy) |
| 180 | `model.layers.4.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 181 | `model.layers.4.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 182 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000182.npy) |
| 183 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000183.npy) |
| 184 | `model.layers.4.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 185 | `model.layers.4.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.020551572195934446 / 1.144579976320253 | [NPY](tensors/0000185.npy) |
| 186 | `model.layers.4.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -16.75 / 7.59375 / -0.009666998929430286 / 1.0317831237452326 | [NPY](tensors/0000186.npy) |
| 187 | `model.layers.4.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.020551572195934446 / 1.144579976320253 | [NPY](tensors/0000187.npy) |
| 188 | `model.layers.4.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -13.5 / 99.0 / 0.23260505652327215 / 4.330122173558702 | [NPY](tensors/0000188.npy) |
| 189 | `model.layers.4.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.020551572195934446 / 1.144579976320253 | [NPY](tensors/0000189.npy) |
| 190 | `model.layers.4.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -10.8125 / 16.125 / 0.0016743008340342662 / 1.342643978329464 | [NPY](tensors/0000190.npy) |
| 191 | `model.layers.4.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -9.625 / 15.125 / -0.005901252356729242 / 0.5906568286379211 | [NPY](tensors/0000191.npy) |
| 192 | `model.layers.4.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -69.0 / 45.5 / -0.006555917669339373 / 1.2903826130599378 | [NPY](tensors/0000192.npy) |
| 193 | `model.layers.4.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -69.0 / 45.5 / -0.006555917669339373 / 1.2903826130599378 | [NPY](tensors/0000193.npy) |
| 194 | `model.layers.4.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.98046875 / 0.002823528321216681 / 0.02301419738837994 | [NPY](tensors/0000194.npy) |
| 195 | `model.layers.4.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -134.0 / 149.0 / 0.10636501633719113 / 5.214021888591354 | [NPY](tensors/0000195.npy) |
| 196 | `model.layers.4.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.90625 / 0.0067741332780314 / 0.580163575501398 | [NPY](tensors/0000196.npy) |
| 197 | `model.layers.4.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.90625 / 0.0067741332780314 / 0.580163575501398 | [NPY](tensors/0000197.npy) |
| 198 | `model.layers.4.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.90625 / 0.0067741332780314 / 0.580163575501398 | [NPY](tensors/0000198.npy) |
| 199 | `model.layers.4.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 200 | `model.layers.4.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 201 | `model.layers.4.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 202 | `model.layers.4.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -81.5 / 164.0 / 0.05461523706202724 / 2.550779277691965 | [NPY](tensors/0000202.npy) |
| 203 | `model.layers.4.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -81.5 / 164.0 / 0.05461523706202724 / 2.550779277691965 | [NPY](tensors/0000203.npy) |
| 204 | `model.layers.4.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -3.109375 / 2.171875 / -0.0812699178631386 / 0.6008676287396583 | [NPY](tensors/0000204.npy) |
| 205 | `model.layers.4` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -192.0 / 252.0 / 0.1609798386153508 / 6.845782809570116 | [NPY](tensors/0000205.npy) |

## Layer 0005

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 206 | `model.layers.5` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -192.0 / 252.0 / 0.1609798386153508 / 6.845782809570116 | [NPY](tensors/0000206.npy) |
| 207 | `model.layers.5` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000207.npy) |
| 208 | `model.layers.5` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000208.npy) |
| 209 | `model.layers.5` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000209.npy) |
| 210 | `model.layers.5` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000210.npy) |
| 211 | `model.layers.5` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 212 | `model.layers.5` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 213 | `model.layers.5` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 214 | `model.layers.5.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -192.0 / 252.0 / 0.1609798386153508 / 6.845782809570116 | [NPY](tensors/0000214.npy) |
| 215 | `model.layers.5.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -28.5 / 41.25 / 0.033671397949277086 / 1.186612726522485 | [NPY](tensors/0000215.npy) |
| 216 | `model.layers.5.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -28.5 / 41.25 / 0.033671397949277086 / 1.186612726522485 | [NPY](tensors/0000216.npy) |
| 217 | `model.layers.5.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000217.npy) |
| 218 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000218.npy) |
| 219 | `model.layers.5.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 220 | `model.layers.5.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 221 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000221.npy) |
| 222 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000222.npy) |
| 223 | `model.layers.5.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 224 | `model.layers.5.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -28.5 / 41.25 / 0.033671397949277086 / 1.186612726522485 | [NPY](tensors/0000224.npy) |
| 225 | `model.layers.5.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -18.75 / 14.9375 / -0.055950852755844334 / 1.4019087220162854 | [NPY](tensors/0000225.npy) |
| 226 | `model.layers.5.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -28.5 / 41.25 / 0.033671397949277086 / 1.186612726522485 | [NPY](tensors/0000226.npy) |
| 227 | `model.layers.5.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -35.25 / 39.5 / -0.03950954255846779 / 3.4271528852497513 | [NPY](tensors/0000227.npy) |
| 228 | `model.layers.5.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -28.5 / 41.25 / 0.033671397949277086 / 1.186612726522485 | [NPY](tensors/0000228.npy) |
| 229 | `model.layers.5.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -7.25 / 8.4375 / 0.00767735450455312 / 1.1980834744147453 | [NPY](tensors/0000229.npy) |
| 230 | `model.layers.5.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -4.34375 / 4.71875 / 0.01150081663639748 / 0.5130091610898291 | [NPY](tensors/0000230.npy) |
| 231 | `model.layers.5.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -70.0 / 72.5 / -0.008772406357162622 / 1.4756806397318676 | [NPY](tensors/0000231.npy) |
| 232 | `model.layers.5.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -70.0 / 72.5 / -0.008772406357162622 / 1.4756806397318676 | [NPY](tensors/0000232.npy) |
| 233 | `model.layers.5.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0029889963646942065 / 0.01858718525478953 | [NPY](tensors/0000233.npy) |
| 234 | `model.layers.5.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -130.0 / 207.0 / 0.15218084553505448 / 7.0429488409313015 | [NPY](tensors/0000234.npy) |
| 235 | `model.layers.5.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -5.59375 / 5.6875 / 0.006637942572397537 / 0.5665274512299792 | [NPY](tensors/0000235.npy) |
| 236 | `model.layers.5.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -5.59375 / 5.6875 / 0.006637942572397537 / 0.5665274512299792 | [NPY](tensors/0000236.npy) |
| 237 | `model.layers.5.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -5.59375 / 5.6875 / 0.006637942572397537 / 0.5665274512299792 | [NPY](tensors/0000237.npy) |
| 238 | `model.layers.5.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 239 | `model.layers.5.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 240 | `model.layers.5.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 241 | `model.layers.5.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -127.0 / 115.5 / 0.039791289719284396 / 2.673879327601038 | [NPY](tensors/0000241.npy) |
| 242 | `model.layers.5.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -127.0 / 115.5 / 0.039791289719284396 / 2.673879327601038 | [NPY](tensors/0000242.npy) |
| 243 | `model.layers.5.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -3.546875 / 2.265625 / -0.08999918016155115 / 0.5893171623405217 | [NPY](tensors/0000243.npy) |
| 244 | `model.layers.5` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -194.0 / 296.0 / 0.19198332023382483 / 8.682439203413367 | [NPY](tensors/0000244.npy) |

## Layer 0006

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 245 | `model.layers.6` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -194.0 / 296.0 / 0.19198332023382483 / 8.682439203413367 | [NPY](tensors/0000245.npy) |
| 246 | `model.layers.6` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000246.npy) |
| 247 | `model.layers.6` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000247.npy) |
| 248 | `model.layers.6` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000248.npy) |
| 249 | `model.layers.6` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000249.npy) |
| 250 | `model.layers.6` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 251 | `model.layers.6` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 252 | `model.layers.6` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 253 | `model.layers.6.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -194.0 / 296.0 / 0.19198332023382483 / 8.682439203413367 | [NPY](tensors/0000253.npy) |
| 254 | `model.layers.6.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -31.25 / 43.0 / 0.029515794424640106 / 1.313055966447363 | [NPY](tensors/0000254.npy) |
| 255 | `model.layers.6.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -31.25 / 43.0 / 0.029515794424640106 / 1.313055966447363 | [NPY](tensors/0000255.npy) |
| 256 | `model.layers.6.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000256.npy) |
| 257 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000257.npy) |
| 258 | `model.layers.6.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 259 | `model.layers.6.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 260 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000260.npy) |
| 261 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000261.npy) |
| 262 | `model.layers.6.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 263 | `model.layers.6.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -31.25 / 43.0 / 0.029515794424640106 / 1.313055966447363 | [NPY](tensors/0000263.npy) |
| 264 | `model.layers.6.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -29.25 / 16.625 / -0.026263677237223552 / 1.1612592717387988 | [NPY](tensors/0000264.npy) |
| 265 | `model.layers.6.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -31.25 / 43.0 / 0.029515794424640106 / 1.313055966447363 | [NPY](tensors/0000265.npy) |
| 266 | `model.layers.6.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -19.5 / 32.5 / 0.20832910317550885 / 2.3770652979394056 | [NPY](tensors/0000266.npy) |
| 267 | `model.layers.6.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -31.25 / 43.0 / 0.029515794424640106 / 1.313055966447363 | [NPY](tensors/0000267.npy) |
| 268 | `model.layers.6.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -7.59375 / 8.1875 / -0.05485714888304807 / 1.6479698899035053 | [NPY](tensors/0000268.npy) |
| 269 | `model.layers.6.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -6.84375 / 7.65625 / -0.03433042992266278 / 0.8253100076988303 | [NPY](tensors/0000269.npy) |
| 270 | `model.layers.6.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -90.5 / 81.5 / -0.003136949126228467 / 1.9556025424992673 | [NPY](tensors/0000270.npy) |
| 271 | `model.layers.6.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -90.5 / 81.5 / -0.003136949126228467 / 1.9556025424992673 | [NPY](tensors/0000271.npy) |
| 272 | `model.layers.6.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.00306585019949385 / 0.02638046756635082 | [NPY](tensors/0000272.npy) |
| 273 | `model.layers.6.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -179.0 / 247.0 / 0.18886731062340228 / 8.579615415311103 | [NPY](tensors/0000273.npy) |
| 274 | `model.layers.6.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -22.0 / 4.875 / 0.010368915222882852 / 0.6122288138930613 | [NPY](tensors/0000274.npy) |
| 275 | `model.layers.6.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -22.0 / 4.875 / 0.010368915222882852 / 0.6122288138930613 | [NPY](tensors/0000275.npy) |
| 276 | `model.layers.6.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -22.0 / 4.875 / 0.010368915222882852 / 0.6122288138930613 | [NPY](tensors/0000276.npy) |
| 277 | `model.layers.6.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 278 | `model.layers.6.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 279 | `model.layers.6.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 280 | `model.layers.6.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -41472.0 / 968.0 / -0.048671144373556796 / 58.10200928172614 | [NPY](tensors/0000280.npy) |
| 281 | `model.layers.6.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41472.0 / 968.0 / -0.048671144373556796 / 58.10200928172614 | [NPY](tensors/0000281.npy) |
| 282 | `model.layers.6.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -3.609375 / 5.0 / -0.10109779272186623 / 0.740394063452286 | [NPY](tensors/0000282.npy) |
| 283 | `model.layers.6` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.1403955950123838 / 58.990234889266226 | [NPY](tensors/0000283.npy) |

## Layer 0007

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 284 | `model.layers.7` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.1403955950123838 / 58.990234889266226 | [NPY](tensors/0000284.npy) |
| 285 | `model.layers.7` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000285.npy) |
| 286 | `model.layers.7` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000286.npy) |
| 287 | `model.layers.7` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000287.npy) |
| 288 | `model.layers.7` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000288.npy) |
| 289 | `model.layers.7` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 290 | `model.layers.7` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 291 | `model.layers.7` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 292 | `model.layers.7.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.1403955950123838 / 58.990234889266226 | [NPY](tensors/0000292.npy) |
| 293 | `model.layers.7.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03471701010293124 / 1.637982064934958 | [NPY](tensors/0000293.npy) |
| 294 | `model.layers.7.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03471701010293124 / 1.637982064934958 | [NPY](tensors/0000294.npy) |
| 295 | `model.layers.7.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000295.npy) |
| 296 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000296.npy) |
| 297 | `model.layers.7.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 298 | `model.layers.7.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 299 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000299.npy) |
| 300 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000300.npy) |
| 301 | `model.layers.7.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 302 | `model.layers.7.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03471701010293124 / 1.637982064934958 | [NPY](tensors/0000302.npy) |
| 303 | `model.layers.7.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -13.4375 / 13.1875 / -0.12110044808405598 / 1.4176135759498707 | [NPY](tensors/0000303.npy) |
| 304 | `model.layers.7.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03471701010293124 / 1.637982064934958 | [NPY](tensors/0000304.npy) |
| 305 | `model.layers.7.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -130.0 / 33.75 / -0.08194507901253326 / 5.389023313384873 | [NPY](tensors/0000305.npy) |
| 306 | `model.layers.7.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03471701010293124 / 1.637982064934958 | [NPY](tensors/0000306.npy) |
| 307 | `model.layers.7.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -17.0 / 10.75 / 0.014816035213095418 / 1.6624359998278138 | [NPY](tensors/0000307.npy) |
| 308 | `model.layers.7.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -7.6875 / 7.90625 / -0.0019298538298134404 / 0.888709284359181 | [NPY](tensors/0000308.npy) |
| 309 | `model.layers.7.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -120.5 / 122.5 / -0.005846251375663946 / 2.3511369730022564 | [NPY](tensors/0000309.npy) |
| 310 | `model.layers.7.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -120.5 / 122.5 / -0.005846251375663946 / 2.3511369730022564 | [NPY](tensors/0000310.npy) |
| 311 | `model.layers.7.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0042059815760508625 / 0.03031943653462259 | [NPY](tensors/0000311.npy) |
| 312 | `model.layers.7.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41472.0 / 1104.0 / 0.13455425083041933 / 58.97015905915831 | [NPY](tensors/0000312.npy) |
| 313 | `model.layers.7.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -77.0 / 5.375 / 0.008589989861029289 / 0.6341807899643829 | [NPY](tensors/0000313.npy) |
| 314 | `model.layers.7.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -77.0 / 5.375 / 0.008589989861029289 / 0.6341807899643829 | [NPY](tensors/0000314.npy) |
| 315 | `model.layers.7.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -77.0 / 5.375 / 0.008589989861029289 / 0.6341807899643829 | [NPY](tensors/0000315.npy) |
| 316 | `model.layers.7.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 317 | `model.layers.7.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 318 | `model.layers.7.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 319 | `model.layers.7.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -164.0 / 167.0 / 0.0321368825904439 / 3.5725011886501084 | [NPY](tensors/0000319.npy) |
| 320 | `model.layers.7.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -164.0 / 167.0 / 0.0321368825904439 / 3.5725011886501084 | [NPY](tensors/0000320.npy) |
| 321 | `model.layers.7.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -3.890625 / 3.828125 / -0.12229011634762367 / 0.8008035555175942 | [NPY](tensors/0000321.npy) |
| 322 | `model.layers.7` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.16668965873051522 / 59.39172756495323 | [NPY](tensors/0000322.npy) |

## Layer 0008

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 323 | `model.layers.8` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.16668965873051522 / 59.39172756495323 | [NPY](tensors/0000323.npy) |
| 324 | `model.layers.8` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000324.npy) |
| 325 | `model.layers.8` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000325.npy) |
| 326 | `model.layers.8` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000326.npy) |
| 327 | `model.layers.8` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000327.npy) |
| 328 | `model.layers.8` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 329 | `model.layers.8` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 330 | `model.layers.8` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 331 | `model.layers.8.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.16668965873051522 / 59.39172756495323 | [NPY](tensors/0000331.npy) |
| 332 | `model.layers.8.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.02579628284229954 / 1.3318378490231406 | [NPY](tensors/0000332.npy) |
| 333 | `model.layers.8.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.02579628284229954 / 1.3318378490231406 | [NPY](tensors/0000333.npy) |
| 334 | `model.layers.8.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000334.npy) |
| 335 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000335.npy) |
| 336 | `model.layers.8.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 337 | `model.layers.8.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 338 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000338.npy) |
| 339 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000339.npy) |
| 340 | `model.layers.8.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 341 | `model.layers.8.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.02579628284229954 / 1.3318378490231406 | [NPY](tensors/0000341.npy) |
| 342 | `model.layers.8.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -14.875 / 15.1875 / -0.009815485570174276 / 1.0572289012836893 | [NPY](tensors/0000342.npy) |
| 343 | `model.layers.8.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.02579628284229954 / 1.3318378490231406 | [NPY](tensors/0000343.npy) |
| 344 | `model.layers.8.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -22.375 / 28.75 / -0.0006607747126600883 / 2.22806353128652 | [NPY](tensors/0000344.npy) |
| 345 | `model.layers.8.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.02579628284229954 / 1.3318378490231406 | [NPY](tensors/0000345.npy) |
| 346 | `model.layers.8.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -9.375 / 9.6875 / 0.0004381500603107928 / 1.7305672872444005 | [NPY](tensors/0000346.npy) |
| 347 | `model.layers.8.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -6.75 / 7.03125 / 0.0009667686391632865 / 0.8649419472683606 | [NPY](tensors/0000347.npy) |
| 348 | `model.layers.8.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -198.0 / 212.0 / 0.0016822338011813413 / 3.0986404108267918 | [NPY](tensors/0000348.npy) |
| 349 | `model.layers.8.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -198.0 / 212.0 / 0.0016822338011813413 / 3.0986404108267918 | [NPY](tensors/0000349.npy) |
| 350 | `model.layers.8.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0034522087610635516 / 0.025138044795341447 | [NPY](tensors/0000350.npy) |
| 351 | `model.layers.8.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41472.0 / 1344.0 / 0.168414228894142 / 59.35534387981423 | [NPY](tensors/0000351.npy) |
| 352 | `model.layers.8.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -57.0 / 5.90625 / 0.006933353906648511 / 0.6688908085750285 | [NPY](tensors/0000352.npy) |
| 353 | `model.layers.8.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -57.0 / 5.90625 / 0.006933353906648511 / 0.6688908085750285 | [NPY](tensors/0000353.npy) |
| 354 | `model.layers.8.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -57.0 / 5.90625 / 0.006933353906648511 / 0.6688908085750285 | [NPY](tensors/0000354.npy) |
| 355 | `model.layers.8.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 356 | `model.layers.8.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 357 | `model.layers.8.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 358 | `model.layers.8.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -264.0 / 245.0 / 0.06991895275392783 / 5.237868269072445 | [NPY](tensors/0000358.npy) |
| 359 | `model.layers.8.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -264.0 / 245.0 / 0.06991895275392783 / 5.237868269072445 | [NPY](tensors/0000359.npy) |
| 360 | `model.layers.8.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -3.921875 / 3.53125 / -0.16193797079364905 / 0.7555846809673561 | [NPY](tensors/0000360.npy) |
| 361 | `model.layers.8` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.23819971215561236 / 60.45225200634762 | [NPY](tensors/0000361.npy) |

## Layer 0009

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 362 | `model.layers.9` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.23819971215561236 / 60.45225200634762 | [NPY](tensors/0000362.npy) |
| 363 | `model.layers.9` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000363.npy) |
| 364 | `model.layers.9` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000364.npy) |
| 365 | `model.layers.9` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000365.npy) |
| 366 | `model.layers.9` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000366.npy) |
| 367 | `model.layers.9` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 368 | `model.layers.9` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 369 | `model.layers.9` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 370 | `model.layers.9.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.23819971215561236 / 60.45225200634762 | [NPY](tensors/0000370.npy) |
| 371 | `model.layers.9.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -207.0 / 72.0 / 0.03742298364997393 / 1.800959929839125 | [NPY](tensors/0000371.npy) |
| 372 | `model.layers.9.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -207.0 / 72.0 / 0.03742298364997393 / 1.800959929839125 | [NPY](tensors/0000372.npy) |
| 373 | `model.layers.9.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000373.npy) |
| 374 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000374.npy) |
| 375 | `model.layers.9.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 376 | `model.layers.9.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 377 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000377.npy) |
| 378 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000378.npy) |
| 379 | `model.layers.9.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 380 | `model.layers.9.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -207.0 / 72.0 / 0.03742298364997393 / 1.800959929839125 | [NPY](tensors/0000380.npy) |
| 381 | `model.layers.9.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -10.125 / 20.25 / 0.06763714397960469 / 1.2622046045542712 | [NPY](tensors/0000381.npy) |
| 382 | `model.layers.9.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -207.0 / 72.0 / 0.03742298364997393 / 1.800959929839125 | [NPY](tensors/0000382.npy) |
| 383 | `model.layers.9.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -52.25 / 40.75 / 0.06738567576230911 / 3.8350192276420683 | [NPY](tensors/0000383.npy) |
| 384 | `model.layers.9.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -207.0 / 72.0 / 0.03742298364997393 / 1.800959929839125 | [NPY](tensors/0000384.npy) |
| 385 | `model.layers.9.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -27.75 / 12.375 / -0.013145852792129088 / 1.5094652933481034 | [NPY](tensors/0000385.npy) |
| 386 | `model.layers.9.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -11.0 / 8.8125 / -0.0037544710177769345 / 0.6477223297279192 | [NPY](tensors/0000386.npy) |
| 387 | `model.layers.9.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -348.0 / 344.0 / 0.01053072079265032 / 3.9901912672175506 | [NPY](tensors/0000387.npy) |
| 388 | `model.layers.9.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -348.0 / 344.0 / 0.01053072079265032 / 3.9901912672175506 | [NPY](tensors/0000388.npy) |
| 389 | `model.layers.9.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004186478498043049 / 0.026953350555193083 | [NPY](tensors/0000389.npy) |
| 390 | `model.layers.9.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41728.0 / 1480.0 / 0.24871382347206944 / 60.30979044877221 | [NPY](tensors/0000390.npy) |
| 391 | `model.layers.9.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -64.5 / 6.78125 / 0.007836444822422574 / 0.6889841474892067 | [NPY](tensors/0000391.npy) |
| 392 | `model.layers.9.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -64.5 / 6.78125 / 0.007836444822422574 / 0.6889841474892067 | [NPY](tensors/0000392.npy) |
| 393 | `model.layers.9.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -64.5 / 6.78125 / 0.007836444822422574 / 0.6889841474892067 | [NPY](tensors/0000393.npy) |
| 394 | `model.layers.9.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 395 | `model.layers.9.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 396 | `model.layers.9.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 397 | `model.layers.9.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -568.0 / 636.0 / 0.04729033382644368 / 5.8626769899444815 | [NPY](tensors/0000397.npy) |
| 398 | `model.layers.9.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -568.0 / 636.0 / 0.04729033382644368 / 5.8626769899444815 | [NPY](tensors/0000398.npy) |
| 399 | `model.layers.9.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -5.1875 / 6.40625 / -0.1310274467039644 / 0.6464913614585622 | [NPY](tensors/0000399.npy) |
| 400 | `model.layers.9` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.2961133787843321 / 60.513640944875824 | [NPY](tensors/0000400.npy) |

## Layer 0010

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 401 | `model.layers.10` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.2961133787843321 / 60.513640944875824 | [NPY](tensors/0000401.npy) |
| 402 | `model.layers.10` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000402.npy) |
| 403 | `model.layers.10` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000403.npy) |
| 404 | `model.layers.10` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000404.npy) |
| 405 | `model.layers.10` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000405.npy) |
| 406 | `model.layers.10` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 407 | `model.layers.10` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 408 | `model.layers.10` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 409 | `model.layers.10.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.2961133787843321 / 60.513640944875824 | [NPY](tensors/0000409.npy) |
| 410 | `model.layers.10.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.03098480228436983 / 1.5376131087399896 | [NPY](tensors/0000410.npy) |
| 411 | `model.layers.10.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.03098480228436983 / 1.5376131087399896 | [NPY](tensors/0000411.npy) |
| 412 | `model.layers.10.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000412.npy) |
| 413 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000413.npy) |
| 414 | `model.layers.10.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 415 | `model.layers.10.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 416 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000416.npy) |
| 417 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000417.npy) |
| 418 | `model.layers.10.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 419 | `model.layers.10.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.03098480228436983 / 1.5376131087399896 | [NPY](tensors/0000419.npy) |
| 420 | `model.layers.10.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -15.4375 / 16.125 / 0.03358911918646269 / 1.0978144325870443 | [NPY](tensors/0000420.npy) |
| 421 | `model.layers.10.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.03098480228436983 / 1.5376131087399896 | [NPY](tensors/0000421.npy) |
| 422 | `model.layers.10.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -56.5 / 17.125 / -0.06798342123543948 / 2.4185967910476056 | [NPY](tensors/0000422.npy) |
| 423 | `model.layers.10.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.03098480228436983 / 1.5376131087399896 | [NPY](tensors/0000423.npy) |
| 424 | `model.layers.10.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -9.6875 / 10.6875 / 0.06658004174071751 / 2.138958936578459 | [NPY](tensors/0000424.npy) |
| 425 | `model.layers.10.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -7.8125 / 8.3125 / 0.04361198547795293 / 1.0007583369222461 | [NPY](tensors/0000425.npy) |
| 426 | `model.layers.10.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -202.0 / 211.0 / 0.038541457522427956 / 4.3359855850267515 | [NPY](tensors/0000426.npy) |
| 427 | `model.layers.10.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -202.0 / 211.0 / 0.038541457522427956 / 4.3359855850267515 | [NPY](tensors/0000427.npy) |
| 428 | `model.layers.10.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.0033584778811743404 / 0.020024937151351754 | [NPY](tensors/0000428.npy) |
| 429 | `model.layers.10.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 924.0 / 0.33462893674138483 / 60.31248433497673 | [NPY](tensors/0000429.npy) |
| 430 | `model.layers.10.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -46.75 / 6.6875 / 0.010061008264351353 / 0.743932342412048 | [NPY](tensors/0000430.npy) |
| 431 | `model.layers.10.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -46.75 / 6.6875 / 0.010061008264351353 / 0.743932342412048 | [NPY](tensors/0000431.npy) |
| 432 | `model.layers.10.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -46.75 / 6.6875 / 0.010061008264351353 / 0.743932342412048 | [NPY](tensors/0000432.npy) |
| 433 | `model.layers.10.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 434 | `model.layers.10.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 435 | `model.layers.10.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 436 | `model.layers.10.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -712.0 / 896.0 / 0.14558536195278762 / 8.874732094649092 | [NPY](tensors/0000436.npy) |
| 437 | `model.layers.10.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -712.0 / 896.0 / 0.14558536195278762 / 8.874732094649092 | [NPY](tensors/0000437.npy) |
| 438 | `model.layers.10.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -5.3125 / 4.03125 / -0.12501177627049134 / 0.6778901403466615 | [NPY](tensors/0000438.npy) |
| 439 | `model.layers.10` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 820.0 / 0.48031127920162664 / 62.060164174334005 | [NPY](tensors/0000439.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 440 | `model.layers.11` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 820.0 / 0.48031127920162664 / 62.060164174334005 | [NPY](tensors/0000440.npy) |
| 441 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000441.npy) |
| 442 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000442.npy) |
| 443 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000443.npy) |
| 444 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000444.npy) |
| 445 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 446 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 447 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 448 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 820.0 / 0.48031127920162664 / 62.060164174334005 | [NPY](tensors/0000448.npy) |
| 449 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.0641431535188383 / 3.209579788984541 | [NPY](tensors/0000449.npy) |
| 450 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.0641431535188383 / 3.209579788984541 | [NPY](tensors/0000450.npy) |
| 451 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000451.npy) |
| 452 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000452.npy) |
| 453 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 454 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 455 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000455.npy) |
| 456 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000456.npy) |
| 457 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 458 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.0641431535188383 / 3.209579788984541 | [NPY](tensors/0000458.npy) |
| 459 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -11.25 / 13.3125 / 0.03535628786184124 / 1.3276271576525631 | [NPY](tensors/0000459.npy) |
| 460 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.0641431535188383 / 3.209579788984541 | [NPY](tensors/0000460.npy) |
| 461 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -38.25 / 45.0 / 0.053415084064132375 / 3.6017320136066373 | [NPY](tensors/0000461.npy) |
| 462 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -191.0 / 138.0 / 0.0641431535188383 / 3.209579788984541 | [NPY](tensors/0000462.npy) |
| 463 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.03749186152152801 / 2.469341125678701 | [NPY](tensors/0000463.npy) |
| 464 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -11.75 / 11.4375 / -0.029494838198807587 / 1.4069299633844594 | [NPY](tensors/0000464.npy) |
| 465 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -466.0 / 500.0 / -0.05944489844831709 / 7.374976750903982 | [NPY](tensors/0000465.npy) |
| 466 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -466.0 / 500.0 / -0.05944489844831709 / 7.374976750903982 | [NPY](tensors/0000466.npy) |
| 467 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004531528898781264 / 0.02422309002976874 | [NPY](tensors/0000467.npy) |
| 468 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 692.0 / 0.42086603037278153 / 61.14829184947875 | [NPY](tensors/0000468.npy) |
| 469 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -78.5 / 7.28125 / 0.008946720773491372 / 0.7991781585117789 | [NPY](tensors/0000469.npy) |
| 470 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -78.5 / 7.28125 / 0.008946720773491372 / 0.7991781585117789 | [NPY](tensors/0000470.npy) |
| 471 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -78.5 / 7.28125 / 0.008946720773491372 / 0.7991781585117789 | [NPY](tensors/0000471.npy) |
| 472 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 473 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 474 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 475 | `model.layers.11.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -508.0 / 400.0 / 0.12713429358940148 / 9.869124246669795 | [NPY](tensors/0000475.npy) |
| 476 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -508.0 / 400.0 / 0.12713429358940148 / 9.869124246669795 | [NPY](tensors/0000476.npy) |
| 477 | `model.layers.11.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.16606507676371027 / 0.8183653411796009 | [NPY](tensors/0000477.npy) |
| 478 | `model.layers.11` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5479130300838551 / 63.33543109727374 | [NPY](tensors/0000478.npy) |

## Layer 0012

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 479 | `model.layers.12` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5479130300838551 / 63.33543109727374 | [NPY](tensors/0000479.npy) |
| 480 | `model.layers.12` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000480.npy) |
| 481 | `model.layers.12` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000481.npy) |
| 482 | `model.layers.12` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000482.npy) |
| 483 | `model.layers.12` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000483.npy) |
| 484 | `model.layers.12` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 485 | `model.layers.12` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 486 | `model.layers.12` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 487 | `model.layers.12.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5479130300838551 / 63.33543109727374 | [NPY](tensors/0000487.npy) |
| 488 | `model.layers.12.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -136.0 / 43.25 / 0.038646563538437366 / 1.594579439388002 | [NPY](tensors/0000488.npy) |
| 489 | `model.layers.12.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -136.0 / 43.25 / 0.038646563538437366 / 1.594579439388002 | [NPY](tensors/0000489.npy) |
| 490 | `model.layers.12.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000490.npy) |
| 491 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000491.npy) |
| 492 | `model.layers.12.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 493 | `model.layers.12.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 494 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000494.npy) |
| 495 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000495.npy) |
| 496 | `model.layers.12.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 497 | `model.layers.12.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -136.0 / 43.25 / 0.038646563538437366 / 1.594579439388002 | [NPY](tensors/0000497.npy) |
| 498 | `model.layers.12.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -19.75 / 18.125 / -0.01606322802109297 / 1.361025401860938 | [NPY](tensors/0000498.npy) |
| 499 | `model.layers.12.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -136.0 / 43.25 / 0.038646563538437366 / 1.594579439388002 | [NPY](tensors/0000499.npy) |
| 500 | `model.layers.12.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -12.8125 / 13.1875 / -0.0008868913720832781 / 1.3319935030609948 | [NPY](tensors/0000500.npy) |
| 501 | `model.layers.12.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -136.0 / 43.25 / 0.038646563538437366 / 1.594579439388002 | [NPY](tensors/0000501.npy) |
| 502 | `model.layers.12.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -16.875 / 19.5 / -0.0019691100950991174 / 2.8304396907924527 | [NPY](tensors/0000502.npy) |
| 503 | `model.layers.12.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -11.375 / 10.5625 / -0.015227482069749904 / 1.4437697242696643 | [NPY](tensors/0000503.npy) |
| 504 | `model.layers.12.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -282.0 / 326.0 / -0.04610708841284302 / 6.072049096224019 | [NPY](tensors/0000504.npy) |
| 505 | `model.layers.12.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -282.0 / 326.0 / -0.04610708841284302 / 6.072049096224019 | [NPY](tensors/0000505.npy) |
| 506 | `model.layers.12.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.96875 / 0.003518246910140667 / 0.02053110946160686 | [NPY](tensors/0000506.npy) |
| 507 | `model.layers.12.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 700.0 / 0.5018777636553018 / 62.69291887800472 | [NPY](tensors/0000507.npy) |
| 508 | `model.layers.12.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -83.5 / 7.625 / 0.00862912250352505 / 0.8435630095256696 | [NPY](tensors/0000508.npy) |
| 509 | `model.layers.12.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -83.5 / 7.625 / 0.00862912250352505 / 0.8435630095256696 | [NPY](tensors/0000509.npy) |
| 510 | `model.layers.12.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -83.5 / 7.625 / 0.00862912250352505 / 0.8435630095256696 | [NPY](tensors/0000510.npy) |
| 511 | `model.layers.12.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 512 | `model.layers.12.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 513 | `model.layers.12.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 514 | `model.layers.12.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -1712.0 / 1520.0 / 0.162953216380692 / 13.365766634675431 | [NPY](tensors/0000514.npy) |
| 515 | `model.layers.12.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -1712.0 / 1520.0 / 0.162953216380692 / 13.365766634675431 | [NPY](tensors/0000515.npy) |
| 516 | `model.layers.12.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -6.9375 / 3.8125 / -0.15765468993883455 / 0.8254533937719983 | [NPY](tensors/0000516.npy) |
| 517 | `model.layers.12` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 1832.0 / 0.6646474569180187 / 66.40163887307963 | [NPY](tensors/0000517.npy) |

## Layer 0013

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 518 | `model.layers.13` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 1832.0 / 0.6646474569180187 / 66.40163887307963 | [NPY](tensors/0000518.npy) |
| 519 | `model.layers.13` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000519.npy) |
| 520 | `model.layers.13` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000520.npy) |
| 521 | `model.layers.13` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000521.npy) |
| 522 | `model.layers.13` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000522.npy) |
| 523 | `model.layers.13` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 524 | `model.layers.13` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 525 | `model.layers.13` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 526 | `model.layers.13.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 1832.0 / 0.6646474569180187 / 66.40163887307963 | [NPY](tensors/0000526.npy) |
| 527 | `model.layers.13.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -182.0 / 99.0 / 0.059725421291895765 / 2.9120727719161157 | [NPY](tensors/0000527.npy) |
| 528 | `model.layers.13.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -182.0 / 99.0 / 0.059725421291895765 / 2.9120727719161157 | [NPY](tensors/0000528.npy) |
| 529 | `model.layers.13.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000529.npy) |
| 530 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000530.npy) |
| 531 | `model.layers.13.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 532 | `model.layers.13.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 533 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000533.npy) |
| 534 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000534.npy) |
| 535 | `model.layers.13.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 536 | `model.layers.13.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -182.0 / 99.0 / 0.059725421291895765 / 2.9120727719161157 | [NPY](tensors/0000536.npy) |
| 537 | `model.layers.13.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -10.8125 / 12.4375 / 0.03930132067232969 / 1.3980726393296092 | [NPY](tensors/0000537.npy) |
| 538 | `model.layers.13.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -182.0 / 99.0 / 0.059725421291895765 / 2.9120727719161157 | [NPY](tensors/0000538.npy) |
| 539 | `model.layers.13.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -51.25 / 31.25 / -0.3251368781823791 / 3.9893153193098216 | [NPY](tensors/0000539.npy) |
| 540 | `model.layers.13.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -182.0 / 99.0 / 0.059725421291895765 / 2.9120727719161157 | [NPY](tensors/0000540.npy) |
| 541 | `model.layers.13.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -16.5 / 22.5 / 0.009812866536419043 / 2.808228008441496 | [NPY](tensors/0000541.npy) |
| 542 | `model.layers.13.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -11.0625 / 20.875 / -0.00046765846218589044 / 1.5941356472004635 | [NPY](tensors/0000542.npy) |
| 543 | `model.layers.13.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -564.0 / 1184.0 / -0.09135676194831134 / 9.659066545397561 | [NPY](tensors/0000543.npy) |
| 544 | `model.layers.13.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -564.0 / 1184.0 / -0.09135676194831134 / 9.659066545397561 | [NPY](tensors/0000544.npy) |
| 545 | `model.layers.13.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0049533840820915435 / 0.024569758199677296 | [NPY](tensors/0000545.npy) |
| 546 | `model.layers.13.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 1304.0 / 0.5732885155338473 / 64.77472645079406 | [NPY](tensors/0000546.npy) |
| 547 | `model.layers.13.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -86.0 / 6.46875 / 0.006586865098047048 / 0.9216737424005567 | [NPY](tensors/0000547.npy) |
| 548 | `model.layers.13.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -86.0 / 6.46875 / 0.006586865098047048 / 0.9216737424005567 | [NPY](tensors/0000548.npy) |
| 549 | `model.layers.13.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -86.0 / 6.46875 / 0.006586865098047048 / 0.9216737424005567 | [NPY](tensors/0000549.npy) |
| 550 | `model.layers.13.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 551 | `model.layers.13.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 552 | `model.layers.13.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 553 | `model.layers.13.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -476.0 / 592.0 / 0.07218052668220244 / 13.314391714087483 | [NPY](tensors/0000553.npy) |
| 554 | `model.layers.13.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -476.0 / 592.0 / 0.07218052668220244 / 13.314391714087483 | [NPY](tensors/0000554.npy) |
| 555 | `model.layers.13.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -5.46875 / 3.796875 / -0.18052455816376076 / 0.8687334161402915 | [NPY](tensors/0000555.npy) |
| 556 | `model.layers.13` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 1168.0 / 0.6454020325164224 / 68.7087725220101 | [NPY](tensors/0000556.npy) |

## Layer 0014

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 557 | `model.layers.14` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 1168.0 / 0.6454020325164224 / 68.7087725220101 | [NPY](tensors/0000557.npy) |
| 558 | `model.layers.14` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000558.npy) |
| 559 | `model.layers.14` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000559.npy) |
| 560 | `model.layers.14` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000560.npy) |
| 561 | `model.layers.14` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000561.npy) |
| 562 | `model.layers.14` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 563 | `model.layers.14` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 564 | `model.layers.14` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 565 | `model.layers.14.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 1168.0 / 0.6454020325164224 / 68.7087725220101 | [NPY](tensors/0000565.npy) |
| 566 | `model.layers.14.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -148.0 / 49.0 / 0.04398297492354252 / 1.9508360681193697 | [NPY](tensors/0000566.npy) |
| 567 | `model.layers.14.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -148.0 / 49.0 / 0.04398297492354252 / 1.9508360681193697 | [NPY](tensors/0000567.npy) |
| 568 | `model.layers.14.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000568.npy) |
| 569 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000569.npy) |
| 570 | `model.layers.14.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 571 | `model.layers.14.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 572 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000572.npy) |
| 573 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000573.npy) |
| 574 | `model.layers.14.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 575 | `model.layers.14.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -148.0 / 49.0 / 0.04398297492354252 / 1.9508360681193697 | [NPY](tensors/0000575.npy) |
| 576 | `model.layers.14.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -53.25 / 29.125 / -0.06173507293833916 / 2.1295402256605445 | [NPY](tensors/0000576.npy) |
| 577 | `model.layers.14.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -148.0 / 49.0 / 0.04398297492354252 / 1.9508360681193697 | [NPY](tensors/0000577.npy) |
| 578 | `model.layers.14.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -37.75 / 18.875 / 0.042868684809864235 / 1.638660652635687 | [NPY](tensors/0000578.npy) |
| 579 | `model.layers.14.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -148.0 / 49.0 / 0.04398297492354252 / 1.9508360681193697 | [NPY](tensors/0000579.npy) |
| 580 | `model.layers.14.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -22.625 / 21.5 / -0.03120714208383238 / 4.698179528848382 | [NPY](tensors/0000580.npy) |
| 581 | `model.layers.14.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -20.375 / 17.25 / -0.02823944558840336 / 2.5728949568758805 | [NPY](tensors/0000581.npy) |
| 582 | `model.layers.14.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -306.0 / 336.0 / -0.04743230007670252 / 8.911796085149032 | [NPY](tensors/0000582.npy) |
| 583 | `model.layers.14.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -306.0 / 336.0 / -0.04743230007670252 / 8.911796085149032 | [NPY](tensors/0000583.npy) |
| 584 | `model.layers.14.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.95703125 / 0.0034916613161054613 / 0.02446704860274592 | [NPY](tensors/0000584.npy) |
| 585 | `model.layers.14.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 944.0 / 0.5979264732008421 / 67.70968295717772 | [NPY](tensors/0000585.npy) |
| 586 | `model.layers.14.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -99.0 / 8.9375 / 0.006995788265191735 / 1.0019323103436932 | [NPY](tensors/0000586.npy) |
| 587 | `model.layers.14.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -99.0 / 8.9375 / 0.006995788265191735 / 1.0019323103436932 | [NPY](tensors/0000587.npy) |
| 588 | `model.layers.14.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -99.0 / 8.9375 / 0.006995788265191735 / 1.0019323103436932 | [NPY](tensors/0000588.npy) |
| 589 | `model.layers.14.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 590 | `model.layers.14.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 591 | `model.layers.14.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 592 | `model.layers.14.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -1280.0 / 1128.0 / 0.041038879294520464 / 19.19172803968782 | [NPY](tensors/0000592.npy) |
| 593 | `model.layers.14.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -1280.0 / 1128.0 / 0.041038879294520464 / 19.19172803968782 | [NPY](tensors/0000593.npy) |
| 594 | `model.layers.14.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -6.84375 / 6.53125 / -0.25154770492167955 / 0.8043898503435172 | [NPY](tensors/0000594.npy) |
| 595 | `model.layers.14` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 2032.0 / 0.6390620828121343 / 74.97636542090957 | [NPY](tensors/0000595.npy) |

## Layer 0015

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 596 | `model.layers.15` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 2032.0 / 0.6390620828121343 / 74.97636542090957 | [NPY](tensors/0000596.npy) |
| 597 | `model.layers.15` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000597.npy) |
| 598 | `model.layers.15` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000598.npy) |
| 599 | `model.layers.15` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000599.npy) |
| 600 | `model.layers.15` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000600.npy) |
| 601 | `model.layers.15` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 602 | `model.layers.15` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 603 | `model.layers.15` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 604 | `model.layers.15.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 2032.0 / 0.6390620828121343 / 74.97636542090957 | [NPY](tensors/0000604.npy) |
| 605 | `model.layers.15.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04443662672532669 / 2.1945886974664814 | [NPY](tensors/0000605.npy) |
| 606 | `model.layers.15.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04443662672532669 / 2.1945886974664814 | [NPY](tensors/0000606.npy) |
| 607 | `model.layers.15.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000607.npy) |
| 608 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000608.npy) |
| 609 | `model.layers.15.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 610 | `model.layers.15.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 611 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000611.npy) |
| 612 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000612.npy) |
| 613 | `model.layers.15.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 614 | `model.layers.15.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04443662672532669 / 2.1945886974664814 | [NPY](tensors/0000614.npy) |
| 615 | `model.layers.15.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -21.25 / 16.375 / 0.008798619227562678 / 1.4459312524456458 | [NPY](tensors/0000615.npy) |
| 616 | `model.layers.15.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04443662672532669 / 2.1945886974664814 | [NPY](tensors/0000616.npy) |
| 617 | `model.layers.15.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -37.0 / 51.5 / 0.034228647483533686 / 4.061879480604788 | [NPY](tensors/0000617.npy) |
| 618 | `model.layers.15.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04443662672532669 / 2.1945886974664814 | [NPY](tensors/0000618.npy) |
| 619 | `model.layers.15.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -61.5 / 38.5 / -0.13200999260618446 / 2.8359329037014533 | [NPY](tensors/0000619.npy) |
| 620 | `model.layers.15.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -11.625 / 20.5 / -0.08876292996749222 / 1.3722580171956538 | [NPY](tensors/0000620.npy) |
| 621 | `model.layers.15.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -1688.0 / 1720.0 / -0.029515669524399903 / 13.21264256246594 | [NPY](tensors/0000621.npy) |
| 622 | `model.layers.15.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -1688.0 / 1720.0 / -0.029515669524399903 / 13.21264256246594 | [NPY](tensors/0000622.npy) |
| 623 | `model.layers.15.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.00388873873390019 / 0.021838975816835676 | [NPY](tensors/0000623.npy) |
| 624 | `model.layers.15.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 1136.0 / 0.6096357205089706 / 72.90185832473945 | [NPY](tensors/0000624.npy) |
| 625 | `model.layers.15.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -106.0 / 9.375 / 0.00815841300731592 / 1.0067782808544306 | [NPY](tensors/0000625.npy) |
| 626 | `model.layers.15.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -106.0 / 9.375 / 0.00815841300731592 / 1.0067782808544306 | [NPY](tensors/0000626.npy) |
| 627 | `model.layers.15.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -106.0 / 9.375 / 0.00815841300731592 / 1.0067782808544306 | [NPY](tensors/0000627.npy) |
| 628 | `model.layers.15.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 629 | `model.layers.15.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 630 | `model.layers.15.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 631 | `model.layers.15.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -744.0 / 588.0 / -0.20061831896968846 / 20.763691060667472 | [NPY](tensors/0000631.npy) |
| 632 | `model.layers.15.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -744.0 / 588.0 / -0.20061831896968846 / 20.763691060667472 | [NPY](tensors/0000632.npy) |
| 633 | `model.layers.15.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -5.625 / 4.46875 / -0.2716347421153208 / 0.9531661746214 | [NPY](tensors/0000633.npy) |
| 634 | `model.layers.15` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 1416.0 / 0.4093402767300457 / 81.20857395387497 | [NPY](tensors/0000634.npy) |

## Layer 0016

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 635 | `model.layers.16` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 1416.0 / 0.4093402767300457 / 81.20857395387497 | [NPY](tensors/0000635.npy) |
| 636 | `model.layers.16` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000636.npy) |
| 637 | `model.layers.16` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000637.npy) |
| 638 | `model.layers.16` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000638.npy) |
| 639 | `model.layers.16` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000639.npy) |
| 640 | `model.layers.16` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 641 | `model.layers.16` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 642 | `model.layers.16` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 643 | `model.layers.16.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 1416.0 / 0.4093402767300457 / 81.20857395387497 | [NPY](tensors/0000643.npy) |
| 644 | `model.layers.16.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -131.0 / 50.0 / 0.03054664095400945 / 1.9117872107006213 | [NPY](tensors/0000644.npy) |
| 645 | `model.layers.16.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -131.0 / 50.0 / 0.03054664095400945 / 1.9117872107006213 | [NPY](tensors/0000645.npy) |
| 646 | `model.layers.16.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000646.npy) |
| 647 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000647.npy) |
| 648 | `model.layers.16.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 649 | `model.layers.16.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 650 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000650.npy) |
| 651 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000651.npy) |
| 652 | `model.layers.16.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 653 | `model.layers.16.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -131.0 / 50.0 / 0.03054664095400945 / 1.9117872107006213 | [NPY](tensors/0000653.npy) |
| 654 | `model.layers.16.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -25.625 / 28.5 / 0.028899657431251845 / 1.7054532573314316 | [NPY](tensors/0000654.npy) |
| 655 | `model.layers.16.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -131.0 / 50.0 / 0.03054664095400945 / 1.9117872107006213 | [NPY](tensors/0000655.npy) |
| 656 | `model.layers.16.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -14.9375 / 32.0 / 0.04271951974945122 / 1.6407602005499713 | [NPY](tensors/0000656.npy) |
| 657 | `model.layers.16.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -131.0 / 50.0 / 0.03054664095400945 / 1.9117872107006213 | [NPY](tensors/0000657.npy) |
| 658 | `model.layers.16.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -23.125 / 20.125 / 0.04108717568804709 / 4.317496320063013 | [NPY](tensors/0000658.npy) |
| 659 | `model.layers.16.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -21.375 / 18.0 / 0.008976390329743119 / 1.8971482945762408 | [NPY](tensors/0000659.npy) |
| 660 | `model.layers.16.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -548.0 / 548.0 / 0.02249142157144091 / 12.802004294752967 | [NPY](tensors/0000660.npy) |
| 661 | `model.layers.16.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -548.0 / 548.0 / 0.02249142157144091 / 12.802004294752967 | [NPY](tensors/0000661.npy) |
| 662 | `model.layers.16.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.94140625 / 0.0028210304463143895 / 0.020211172737366636 | [NPY](tensors/0000662.npy) |
| 663 | `model.layers.16.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 1328.0 / 0.4317916670095608 / 80.44330611556299 | [NPY](tensors/0000663.npy) |
| 664 | `model.layers.16.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -68.0 / 10.0 / 0.00793827949463856 / 0.9762992591343999 | [NPY](tensors/0000664.npy) |
| 665 | `model.layers.16.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -68.0 / 10.0 / 0.00793827949463856 / 0.9762992591343999 | [NPY](tensors/0000665.npy) |
| 666 | `model.layers.16.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -68.0 / 10.0 / 0.00793827949463856 / 0.9762992591343999 | [NPY](tensors/0000666.npy) |
| 667 | `model.layers.16.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 668 | `model.layers.16.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 669 | `model.layers.16.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 670 | `model.layers.16.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -2400.0 / 1736.0 / -0.19167555945642878 / 34.00437781247465 | [NPY](tensors/0000670.npy) |
| 671 | `model.layers.16.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -2400.0 / 1736.0 / -0.19167555945642878 / 34.00437781247465 | [NPY](tensors/0000671.npy) |
| 672 | `model.layers.16.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -6.375 / 4.46875 / -0.3127002742853058 / 1.2522917220828353 | [NPY](tensors/0000672.npy) |
| 673 | `model.layers.16` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 2688.0 / 0.24023862117238706 / 98.79023825539451 | [NPY](tensors/0000673.npy) |

## Layer 0017

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 674 | `model.layers.17` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 2688.0 / 0.24023862117238706 / 98.79023825539451 | [NPY](tensors/0000674.npy) |
| 675 | `model.layers.17` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000675.npy) |
| 676 | `model.layers.17` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000676.npy) |
| 677 | `model.layers.17` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000677.npy) |
| 678 | `model.layers.17` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000678.npy) |
| 679 | `model.layers.17` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 680 | `model.layers.17` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 681 | `model.layers.17` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 682 | `model.layers.17.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 2688.0 / 0.24023862117238706 / 98.79023825539451 | [NPY](tensors/0000682.npy) |
| 683 | `model.layers.17.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04004909422774142 / 2.741199631999932 | [NPY](tensors/0000683.npy) |
| 684 | `model.layers.17.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04004909422774142 / 2.741199631999932 | [NPY](tensors/0000684.npy) |
| 685 | `model.layers.17.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000685.npy) |
| 686 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000686.npy) |
| 687 | `model.layers.17.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 688 | `model.layers.17.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 689 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000689.npy) |
| 690 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000690.npy) |
| 691 | `model.layers.17.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 692 | `model.layers.17.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04004909422774142 / 2.741199631999932 | [NPY](tensors/0000692.npy) |
| 693 | `model.layers.17.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -16.75 / 19.375 / 0.01343433987313403 / 1.5764028090641462 | [NPY](tensors/0000693.npy) |
| 694 | `model.layers.17.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04004909422774142 / 2.741199631999932 | [NPY](tensors/0000694.npy) |
| 695 | `model.layers.17.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -68.0 / 40.0 / -0.051536247898102475 / 4.799077701943765 | [NPY](tensors/0000695.npy) |
| 696 | `model.layers.17.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04004909422774142 / 2.741199631999932 | [NPY](tensors/0000696.npy) |
| 697 | `model.layers.17.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -19.5 / 21.75 / 0.1196076741044441 / 3.03929344352167 | [NPY](tensors/0000697.npy) |
| 698 | `model.layers.17.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -10.0 / 10.9375 / 0.06204303669108596 / 1.226740390684028 | [NPY](tensors/0000698.npy) |
| 699 | `model.layers.17.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -1520.0 / 1552.0 / 0.2715273778700733 / 20.346453771466695 | [NPY](tensors/0000699.npy) |
| 700 | `model.layers.17.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -1520.0 / 1552.0 / 0.2715273778700733 / 20.346453771466695 | [NPY](tensors/0000700.npy) |
| 701 | `model.layers.17.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.0039895905911247935 / 0.027095504307057056 | [NPY](tensors/0000701.npy) |
| 702 | `model.layers.17.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41216.0 / 1824.0 / 0.5116301800874289 / 93.2463830719978 | [NPY](tensors/0000702.npy) |
| 703 | `model.layers.17.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41.75 / 9.0625 / 0.008311986819737487 / 0.9475925818764541 | [NPY](tensors/0000703.npy) |
| 704 | `model.layers.17.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41.75 / 9.0625 / 0.008311986819737487 / 0.9475925818764541 | [NPY](tensors/0000704.npy) |
| 705 | `model.layers.17.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -41.75 / 9.0625 / 0.008311986819737487 / 0.9475925818764541 | [NPY](tensors/0000705.npy) |
| 706 | `model.layers.17.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 707 | `model.layers.17.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 708 | `model.layers.17.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 709 | `model.layers.17.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -1184.0 / 40448.0 / -0.08737667889779577 / 67.88772509973272 | [NPY](tensors/0000709.npy) |
| 710 | `model.layers.17.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -1184.0 / 40448.0 / -0.08737667889779577 / 67.88772509973272 | [NPY](tensors/0000710.npy) |
| 711 | `model.layers.17.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -4.9375 / 3.015625 / -0.20484983385278938 / 0.9510912986671826 | [NPY](tensors/0000711.npy) |
| 712 | `model.layers.17` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -2416.0 / 2512.0 / 0.4244640021734916 / 98.65067863426052 | [NPY](tensors/0000712.npy) |

## Layer 0018

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 713 | `model.layers.18` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -2416.0 / 2512.0 / 0.4244640021734916 / 98.65067863426052 | [NPY](tensors/0000713.npy) |
| 714 | `model.layers.18` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000714.npy) |
| 715 | `model.layers.18` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000715.npy) |
| 716 | `model.layers.18` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000716.npy) |
| 717 | `model.layers.18` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000717.npy) |
| 718 | `model.layers.18` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 719 | `model.layers.18` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 720 | `model.layers.18` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 721 | `model.layers.18.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -2416.0 / 2512.0 / 0.4244640021734916 / 98.65067863426052 | [NPY](tensors/0000721.npy) |
| 722 | `model.layers.18.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.019004589548048456 / 1.6001645460511953 | [NPY](tensors/0000722.npy) |
| 723 | `model.layers.18.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.019004589548048456 / 1.6001645460511953 | [NPY](tensors/0000723.npy) |
| 724 | `model.layers.18.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000724.npy) |
| 725 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000725.npy) |
| 726 | `model.layers.18.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 727 | `model.layers.18.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 728 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000728.npy) |
| 729 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000729.npy) |
| 730 | `model.layers.18.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 731 | `model.layers.18.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.019004589548048456 / 1.6001645460511953 | [NPY](tensors/0000731.npy) |
| 732 | `model.layers.18.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -25.625 / 31.25 / 0.1216481300377453 / 1.843746715262029 | [NPY](tensors/0000732.npy) |
| 733 | `model.layers.18.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.019004589548048456 / 1.6001645460511953 | [NPY](tensors/0000733.npy) |
| 734 | `model.layers.18.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -17.25 / 48.0 / 0.1204698703387815 / 2.2517322888933786 | [NPY](tensors/0000734.npy) |
| 735 | `model.layers.18.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.019004589548048456 / 1.6001645460511953 | [NPY](tensors/0000735.npy) |
| 736 | `model.layers.18.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -24.875 / 23.375 / -0.274593033817377 / 4.279047317174327 | [NPY](tensors/0000736.npy) |
| 737 | `model.layers.18.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -18.625 / 20.375 / -0.14440065312872608 / 1.8354475315022736 | [NPY](tensors/0000737.npy) |
| 738 | `model.layers.18.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -456.0 / 632.0 / -0.4021333991746406 / 20.147438306909923 | [NPY](tensors/0000738.npy) |
| 739 | `model.layers.18.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -456.0 / 632.0 / -0.4021333991746406 / 20.147438306909923 | [NPY](tensors/0000739.npy) |
| 740 | `model.layers.18.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0025623533151128064 / 0.022181785368963758 | [NPY](tensors/0000740.npy) |
| 741 | `model.layers.18.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -2352.0 / 2464.0 / 0.022686698284934977 / 104.34057309208818 | [NPY](tensors/0000741.npy) |
| 742 | `model.layers.18.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -7.75 / 11.875 / 0.0013345840425415434 / 0.9114972627434695 | [NPY](tensors/0000742.npy) |
| 743 | `model.layers.18.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -7.75 / 11.875 / 0.0013345840425415434 / 0.9114972627434695 | [NPY](tensors/0000743.npy) |
| 744 | `model.layers.18.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -7.75 / 11.875 / 0.0013345840425415434 / 0.9114972627434695 | [NPY](tensors/0000744.npy) |
| 745 | `model.layers.18.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 746 | `model.layers.18.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 747 | `model.layers.18.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 748 | `model.layers.18.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -2112.0 / 2832.0 / 0.2726512704151549 / 57.24605295163493 | [NPY](tensors/0000748.npy) |
| 749 | `model.layers.18.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -2112.0 / 2832.0 / 0.2726512704151549 / 57.24605295163493 | [NPY](tensors/0000749.npy) |
| 750 | `model.layers.18.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -4.96875 / 2.3125 / -0.34023856045155043 / 1.0305307225162683 | [NPY](tensors/0000750.npy) |
| 751 | `model.layers.18` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.29523616128795305 / 146.77406656076093 | [NPY](tensors/0000751.npy) |

## Layer 0019

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 752 | `model.layers.19` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.29523616128795305 / 146.77406656076093 | [NPY](tensors/0000752.npy) |
| 753 | `model.layers.19` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000753.npy) |
| 754 | `model.layers.19` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000754.npy) |
| 755 | `model.layers.19` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000755.npy) |
| 756 | `model.layers.19` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000756.npy) |
| 757 | `model.layers.19` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 758 | `model.layers.19` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 759 | `model.layers.19` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 760 | `model.layers.19.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.29523616128795305 / 146.77406656076093 | [NPY](tensors/0000760.npy) |
| 761 | `model.layers.19.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.011511509469274277 / 1.8463677992593843 | [NPY](tensors/0000761.npy) |
| 762 | `model.layers.19.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.011511509469274277 / 1.8463677992593843 | [NPY](tensors/0000762.npy) |
| 763 | `model.layers.19.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000763.npy) |
| 764 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000764.npy) |
| 765 | `model.layers.19.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 766 | `model.layers.19.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 767 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000767.npy) |
| 768 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000768.npy) |
| 769 | `model.layers.19.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 770 | `model.layers.19.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.011511509469274277 / 1.8463677992593843 | [NPY](tensors/0000770.npy) |
| 771 | `model.layers.19.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -14.875 / 24.5 / -0.03900641329536474 / 1.3016615317956604 | [NPY](tensors/0000771.npy) |
| 772 | `model.layers.19.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.011511509469274277 / 1.8463677992593843 | [NPY](tensors/0000772.npy) |
| 773 | `model.layers.19.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -72.5 / 71.0 / -0.10866763490890519 / 6.83852400008913 | [NPY](tensors/0000773.npy) |
| 774 | `model.layers.19.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.011511509469274277 / 1.8463677992593843 | [NPY](tensors/0000774.npy) |
| 775 | `model.layers.19.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -15.9375 / 14.1875 / -0.030080962005291093 / 3.1587863298391867 | [NPY](tensors/0000775.npy) |
| 776 | `model.layers.19.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -10.625 / 11.875 / -0.013716233284708449 / 0.8823616156795006 | [NPY](tensors/0000776.npy) |
| 777 | `model.layers.19.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -2176.0 / 1944.0 / -0.6030850554524587 / 43.278757011720636 | [NPY](tensors/0000777.npy) |
| 778 | `model.layers.19.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -2176.0 / 1944.0 / -0.6030850554524587 / 43.278757011720636 | [NPY](tensors/0000778.npy) |
| 779 | `model.layers.19.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.9765625 / 0.001978487532818359 / 0.012400060308460645 | [NPY](tensors/0000779.npy) |
| 780 | `model.layers.19.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -3568.0 / 3344.0 / -0.30821981846765334 / 126.73121710123327 | [NPY](tensors/0000780.npy) |
| 781 | `model.layers.19.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -7.15625 / 16.75 / 0.0003261425238237547 / 0.9733752981749811 | [NPY](tensors/0000781.npy) |
| 782 | `model.layers.19.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -7.15625 / 16.75 / 0.0003261425238237547 / 0.9733752981749811 | [NPY](tensors/0000782.npy) |
| 783 | `model.layers.19.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -7.15625 / 16.75 / 0.0003261425238237547 / 0.9733752981749811 | [NPY](tensors/0000783.npy) |
| 784 | `model.layers.19.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 785 | `model.layers.19.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 786 | `model.layers.19.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 787 | `model.layers.19.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -2432.0 / 2512.0 / 0.306107875976372 / 84.65352306156133 | [NPY](tensors/0000787.npy) |
| 788 | `model.layers.19.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -2432.0 / 2512.0 / 0.306107875976372 / 84.65352306156133 | [NPY](tensors/0000788.npy) |
| 789 | `model.layers.19.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -6.21875 / 2.984375 / -0.2903549805116118 / 1.4147123142725615 | [NPY](tensors/0000789.npy) |
| 790 | `model.layers.19` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -4960.0 / 4608.0 / -0.002312086107727894 / 186.58471225778575 | [NPY](tensors/0000790.npy) |

## Layer 0020

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 791 | `model.layers.20` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -4960.0 / 4608.0 / -0.002312086107727894 / 186.58471225778575 | [NPY](tensors/0000791.npy) |
| 792 | `model.layers.20` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000792.npy) |
| 793 | `model.layers.20` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000793.npy) |
| 794 | `model.layers.20` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000794.npy) |
| 795 | `model.layers.20` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000795.npy) |
| 796 | `model.layers.20` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 797 | `model.layers.20` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 798 | `model.layers.20` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 799 | `model.layers.20.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -4960.0 / 4608.0 / -0.002312086107727894 / 186.58471225778575 | [NPY](tensors/0000799.npy) |
| 800 | `model.layers.20.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -41.5 / 39.0 / 0.008270260658622085 / 1.5333090407399759 | [NPY](tensors/0000800.npy) |
| 801 | `model.layers.20.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -41.5 / 39.0 / 0.008270260658622085 / 1.5333090407399759 | [NPY](tensors/0000801.npy) |
| 802 | `model.layers.20.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000802.npy) |
| 803 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000803.npy) |
| 804 | `model.layers.20.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 805 | `model.layers.20.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 806 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000806.npy) |
| 807 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000807.npy) |
| 808 | `model.layers.20.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 809 | `model.layers.20.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41.5 / 39.0 / 0.008270260658622085 / 1.5333090407399759 | [NPY](tensors/0000809.npy) |
| 810 | `model.layers.20.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -20.375 / 20.625 / 0.04469918587454211 / 1.2319135566766095 | [NPY](tensors/0000810.npy) |
| 811 | `model.layers.20.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41.5 / 39.0 / 0.008270260658622085 / 1.5333090407399759 | [NPY](tensors/0000811.npy) |
| 812 | `model.layers.20.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -27.0 / 37.0 / -0.10469701982448609 / 2.2229774148181036 | [NPY](tensors/0000812.npy) |
| 813 | `model.layers.20.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -41.5 / 39.0 / 0.008270260658622085 / 1.5333090407399759 | [NPY](tensors/0000813.npy) |
| 814 | `model.layers.20.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -23.0 / 20.375 / -0.00454975681358509 / 3.9188720201868295 | [NPY](tensors/0000814.npy) |
| 815 | `model.layers.20.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -17.5 / 17.75 / -0.01449984227362078 / 1.26803947953263 | [NPY](tensors/0000815.npy) |
| 816 | `model.layers.20.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -988.0 / 1072.0 / -0.19176360283898056 / 24.64372341546363 | [NPY](tensors/0000816.npy) |
| 817 | `model.layers.20.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -988.0 / 1072.0 / -0.19176360283898056 / 24.64372341546363 | [NPY](tensors/0000817.npy) |
| 818 | `model.layers.20.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.002196315386440987 / 0.01845218051350821 | [NPY](tensors/0000818.npy) |
| 819 | `model.layers.20.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -4960.0 / 4832.0 / -0.19414894887421758 / 191.37217672457228 | [NPY](tensors/0000819.npy) |
| 820 | `model.layers.20.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -6.96875 / 15.4375 / -0.0009542380170094387 / 0.9279126981356369 | [NPY](tensors/0000820.npy) |
| 821 | `model.layers.20.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -6.96875 / 15.4375 / -0.0009542380170094387 / 0.9279126981356369 | [NPY](tensors/0000821.npy) |
| 822 | `model.layers.20.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -6.96875 / 15.4375 / -0.0009542380170094387 / 0.9279126981356369 | [NPY](tensors/0000822.npy) |
| 823 | `model.layers.20.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 824 | `model.layers.20.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 825 | `model.layers.20.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 826 | `model.layers.20.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -5888.0 / 6848.0 / 0.4426708307754383 / 84.8902227818143 | [NPY](tensors/0000826.npy) |
| 827 | `model.layers.20.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -5888.0 / 6848.0 / 0.4426708307754383 / 84.8902227818143 | [NPY](tensors/0000827.npy) |
| 828 | `model.layers.20.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -5.3125 / 3.828125 / -0.17738475156634043 / 1.1842056007941217 | [NPY](tensors/0000828.npy) |
| 829 | `model.layers.20` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -9152.0 / 10368.0 / 0.24802953693899474 / 254.18760550591256 | [NPY](tensors/0000829.npy) |

## Layer 0021

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 830 | `model.layers.21` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -9152.0 / 10368.0 / 0.24802953693899474 / 254.18760550591256 | [NPY](tensors/0000830.npy) |
| 831 | `model.layers.21` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000831.npy) |
| 832 | `model.layers.21` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000832.npy) |
| 833 | `model.layers.21` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000833.npy) |
| 834 | `model.layers.21` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000834.npy) |
| 835 | `model.layers.21` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 836 | `model.layers.21` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 837 | `model.layers.21` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 838 | `model.layers.21.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -9152.0 / 10368.0 / 0.24802953693899474 / 254.18760550591256 | [NPY](tensors/0000838.npy) |
| 839 | `model.layers.21.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.004753493710180347 / 1.8135875745896664 | [NPY](tensors/0000839.npy) |
| 840 | `model.layers.21.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.004753493710180347 / 1.8135875745896664 | [NPY](tensors/0000840.npy) |
| 841 | `model.layers.21.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000841.npy) |
| 842 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000842.npy) |
| 843 | `model.layers.21.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 844 | `model.layers.21.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 845 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000845.npy) |
| 846 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000846.npy) |
| 847 | `model.layers.21.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 848 | `model.layers.21.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.004753493710180347 / 1.8135875745896664 | [NPY](tensors/0000848.npy) |
| 849 | `model.layers.21.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -19.625 / 33.25 / 0.023764481780704096 / 1.144395198500796 | [NPY](tensors/0000849.npy) |
| 850 | `model.layers.21.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.004753493710180347 / 1.8135875745896664 | [NPY](tensors/0000850.npy) |
| 851 | `model.layers.21.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -100.0 / 99.5 / -0.15424449846483348 / 7.853904777224912 | [NPY](tensors/0000851.npy) |
| 852 | `model.layers.21.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.004753493710180347 / 1.8135875745896664 | [NPY](tensors/0000852.npy) |
| 853 | `model.layers.21.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -21.625 / 20.625 / -0.009389372689000676 / 3.0933931849698957 | [NPY](tensors/0000853.npy) |
| 854 | `model.layers.21.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -11.375 / 13.3125 / 0.00382652854013072 / 0.6296484786842876 | [NPY](tensors/0000854.npy) |
| 855 | `model.layers.21.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -5184.0 / 4768.0 / -0.5630358408657502 / 83.91906101086404 | [NPY](tensors/0000855.npy) |
| 856 | `model.layers.21.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -5184.0 / 4768.0 / -0.5630358408657502 / 83.91906101086404 | [NPY](tensors/0000856.npy) |
| 857 | `model.layers.21.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.82421875 / 0.0019344355581742037 / 0.009362505753185858 | [NPY](tensors/0000857.npy) |
| 858 | `model.layers.21.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -5888.0 / 6048.0 / -0.31530678233552656 / 203.80767616144993 | [NPY](tensors/0000858.npy) |
| 859 | `model.layers.21.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -8.6875 / 22.75 / -0.0004848471313677775 / 1.05906267245171 | [NPY](tensors/0000859.npy) |
| 860 | `model.layers.21.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -8.6875 / 22.75 / -0.0004848471313677775 / 1.05906267245171 | [NPY](tensors/0000860.npy) |
| 861 | `model.layers.21.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -8.6875 / 22.75 / -0.0004848471313677775 / 1.05906267245171 | [NPY](tensors/0000861.npy) |
| 862 | `model.layers.21.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 863 | `model.layers.21.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 864 | `model.layers.21.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 865 | `model.layers.21.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -6144.0 / 5760.0 / -0.8934165977211332 / 158.8485987509191 | [NPY](tensors/0000865.npy) |
| 866 | `model.layers.21.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -6144.0 / 5760.0 / -0.8934165977211332 / 158.8485987509191 | [NPY](tensors/0000866.npy) |
| 867 | `model.layers.21.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -5.65625 / 4.40625 / -0.22128704156768456 / 1.526369972255158 | [NPY](tensors/0000867.npy) |
| 868 | `model.layers.21` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -9280.0 / 9664.0 / -1.2103585308708353 / 317.21201565636085 | [NPY](tensors/0000868.npy) |

## Layer 0022

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 869 | `model.layers.22` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -9280.0 / 9664.0 / -1.2103585308708353 / 317.21201565636085 | [NPY](tensors/0000869.npy) |
| 870 | `model.layers.22` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000870.npy) |
| 871 | `model.layers.22` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000871.npy) |
| 872 | `model.layers.22` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000872.npy) |
| 873 | `model.layers.22` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000873.npy) |
| 874 | `model.layers.22` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 875 | `model.layers.22` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 876 | `model.layers.22` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 877 | `model.layers.22.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -9280.0 / 9664.0 / -1.2103585308708353 / 317.21201565636085 | [NPY](tensors/0000877.npy) |
| 878 | `model.layers.22.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -43.0 / 49.0 / 6.900923640540488e-05 / 1.7217402333274934 | [NPY](tensors/0000878.npy) |
| 879 | `model.layers.22.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -43.0 / 49.0 / 6.900923640540488e-05 / 1.7217402333274934 | [NPY](tensors/0000879.npy) |
| 880 | `model.layers.22.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8216431162787256e+38 / 1.6900097276510153e+38 | [NPY](tensors/0000880.npy) |
| 881 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000881.npy) |
| 882 | `model.layers.22.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 883 | `model.layers.22.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 884 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000884.npy) |
| 885 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000885.npy) |
| 886 | `model.layers.22.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 887 | `model.layers.22.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -43.0 / 49.0 / 6.900923640540488e-05 / 1.7217402333274934 | [NPY](tensors/0000887.npy) |
| 888 | `model.layers.22.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -40.5 / 31.375 / -0.05220770927377764 / 2.4673575115676574 | [NPY](tensors/0000888.npy) |
| 889 | `model.layers.22.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -43.0 / 49.0 / 6.900923640540488e-05 / 1.7217402333274934 | [NPY](tensors/0000889.npy) |
| 890 | `model.layers.22.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -32.25 / 9.0 / -0.053254686944772686 / 1.366602762090833 | [NPY](tensors/0000890.npy) |
| 891 | `model.layers.22.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -43.0 / 49.0 / 6.900923640540488e-05 / 1.7217402333274934 | [NPY](tensors/0000891.npy) |
| 892 | `model.layers.22.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -26.625 / 27.25 / -0.044913673292050205 / 4.359484813757685 | [NPY](tensors/0000892.npy) |
| 893 | `model.layers.22.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -19.875 / 13.75 / -0.031165773890575878 / 1.4784717908238014 | [NPY](tensors/0000893.npy) |
| 894 | `model.layers.22.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -2128.0 / 1416.0 / -0.3996543095529675 / 40.31951719581782 | [NPY](tensors/0000894.npy) |
| 895 | `model.layers.22.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -2128.0 / 1416.0 / -0.3996543095529675 / 40.31951719581782 | [NPY](tensors/0000895.npy) |
| 896 | `model.layers.22.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.93359375 / 0.002232875521149112 / 0.019093614371516666 | [NPY](tensors/0000896.npy) |
| 897 | `model.layers.22.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -9920.0 / 10304.0 / -1.6114489469635351 / 330.58693124680195 | [NPY](tensors/0000897.npy) |
| 898 | `model.layers.22.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -14.125 / 17.75 / -0.008970255666783314 / 0.9502311402118198 | [NPY](tensors/0000898.npy) |
| 899 | `model.layers.22.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -14.125 / 17.75 / -0.008970255666783314 / 0.9502311402118198 | [NPY](tensors/0000899.npy) |
| 900 | `model.layers.22.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -14.125 / 17.75 / -0.008970255666783314 / 0.9502311402118198 | [NPY](tensors/0000900.npy) |
| 901 | `model.layers.22.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 902 | `model.layers.22.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 903 | `model.layers.22.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 904 | `model.layers.22.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -6656.0 / 6336.0 / 0.04186620526248298 / 155.8818100053836 | [NPY](tensors/0000904.npy) |
| 905 | `model.layers.22.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -6656.0 / 6336.0 / 0.04186620526248298 / 155.8818100053836 | [NPY](tensors/0000905.npy) |
| 906 | `model.layers.22.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -6.53125 / 4.78125 / -0.17246487971102253 / 1.3853981690509238 | [NPY](tensors/0000906.npy) |
| 907 | `model.layers.22` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -12864.0 / 14080.0 / -1.5692174570986097 / 425.41353603372715 | [NPY](tensors/0000907.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 908 | `model.layers.23` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -12864.0 / 14080.0 / -1.5692174570986097 / 425.41353603372715 | [NPY](tensors/0000908.npy) |
| 909 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000909.npy) |
| 910 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000910.npy) |
| 911 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000911.npy) |
| 912 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000912.npy) |
| 913 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 914 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 915 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 916 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -12864.0 / 14080.0 / -1.5692174570986097 / 425.41353603372715 | [NPY](tensors/0000916.npy) |
| 917 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009171789398791267 / 1.760154556252982 | [NPY](tensors/0000917.npy) |
| 918 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 178, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009171789398791267 / 1.760154556252982 | [NPY](tensors/0000918.npy) |
| 919 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 178, 178] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6852445390379825e+38 / 1.6947389495956697e+38 | [NPY](tensors/0000919.npy) |
| 920 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 178] | torch.int64 → int64 | 0.0 / 177.0 / 88.5 / 51.383363066268835 | [NPY](tensors/0000920.npy) |
| 921 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 922 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 923 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8445178149791246 / 0.8476422091611024 | [NPY](tensors/0000923.npy) |
| 924 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 178, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12217879084199196 / 0.6022798724808884 | [NPY](tensors/0000924.npy) |
| 925 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 926 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009171789398791267 / 1.760154556252982 | [NPY](tensors/0000926.npy) |
| 927 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 178, 4096] | torch.bfloat16 → float32 | -18.125 / 24.0 / 0.031751226399096645 / 1.6087443478973014 | [NPY](tensors/0000927.npy) |
| 928 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009171789398791267 / 1.760154556252982 | [NPY](tensors/0000928.npy) |
| 929 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -74.5 / 59.5 / -0.0783563160698526 / 4.8343120765175565 | [NPY](tensors/0000929.npy) |
| 930 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009171789398791267 / 1.760154556252982 | [NPY](tensors/0000930.npy) |
| 931 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 178, 512] | torch.bfloat16 → float32 | -24.5 / 24.5 / 0.003651185819272245 / 3.101093519503658 | [NPY](tensors/0000931.npy) |
| 932 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 178, 4096] | torch.bfloat16 → float32 | -23.0 / 12.9375 / -0.005585082746993169 / 1.1213102937237847 | [NPY](tensors/0000932.npy) |
| 933 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -6080.0 / 6272.0 / 2.841265727454952 / 166.57378346484526 | [NPY](tensors/0000933.npy) |
| 934 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -6080.0 / 6272.0 / 2.841265727454952 / 166.57378346484526 | [NPY](tensors/0000934.npy) |
| 935 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 178, 178] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0025403701367701266 / 0.016323577607343945 | [NPY](tensors/0000935.npy) |
| 936 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -10496.0 / 11200.0 / 1.271983352642083 / 375.4214288207207 | [NPY](tensors/0000936.npy) |
| 937 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -47.0 / 18.25 / -0.01470220929637235 / 1.1793443316936962 | [NPY](tensors/0000937.npy) |
| 938 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -47.0 / 18.25 / -0.01470220929637235 / 1.1793443316936962 | [NPY](tensors/0000938.npy) |
| 939 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [178, 2880] | torch.bfloat16 → float32 | -47.0 / 18.25 / -0.01470220929637235 / 1.1793443316936962 | [NPY](tensors/0000939.npy) |
| 940 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 941 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 942 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 943 | `model.layers.23.mlp.experts` | 0 | `output` | [178, 2880] | torch.bfloat16 → float32 | -4800.0 / 4736.0 / -1.4583127917124241 / 156.29758389080223 | [NPY](tensors/0000943.npy) |
| 944 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 178, 2880] | torch.bfloat16 → float32 | -4800.0 / 4736.0 / -1.4583127917124241 / 156.29758389080223 | [NPY](tensors/0000944.npy) |
| 945 | `model.layers.23.mlp` | 0 | `output[1]` | [178, 32] | torch.bfloat16 → float32 | -7.15625 / 3.96875 / 0.24876617313770766 / 2.3323978813475685 | [NPY](tensors/0000945.npy) |
| 946 | `model.layers.23` | 0 | `output` | [1, 178, 2880] | torch.bfloat16 → float32 | -10688.0 / 10880.0 / -0.18595643156625508 / 435.79241908750373 | [NPY](tensors/0000946.npy) |

## Registered modules that did not execute

- `<model>` (GptOssForCausalLM)
- `model.layers` (ModuleList)
- `model.layers.0.mlp.router` (GptOssTopKRouter)
- `model.layers.1.mlp.router` (GptOssTopKRouter)
- `model.layers.2.mlp.router` (GptOssTopKRouter)
- `model.layers.3.mlp.router` (GptOssTopKRouter)
- `model.layers.4.mlp.router` (GptOssTopKRouter)
- `model.layers.5.mlp.router` (GptOssTopKRouter)
- `model.layers.6.mlp.router` (GptOssTopKRouter)
- `model.layers.7.mlp.router` (GptOssTopKRouter)
- `model.layers.8.mlp.router` (GptOssTopKRouter)
- `model.layers.9.mlp.router` (GptOssTopKRouter)
- `model.layers.10.mlp.router` (GptOssTopKRouter)
- `model.layers.11.mlp.router` (GptOssTopKRouter)
- `model.layers.12.mlp.router` (GptOssTopKRouter)
- `model.layers.13.mlp.router` (GptOssTopKRouter)
- `model.layers.14.mlp.router` (GptOssTopKRouter)
- `model.layers.15.mlp.router` (GptOssTopKRouter)
- `model.layers.16.mlp.router` (GptOssTopKRouter)
- `model.layers.17.mlp.router` (GptOssTopKRouter)
- `model.layers.18.mlp.router` (GptOssTopKRouter)
- `model.layers.19.mlp.router` (GptOssTopKRouter)
- `model.layers.20.mlp.router` (GptOssTopKRouter)
- `model.layers.21.mlp.router` (GptOssTopKRouter)
- `model.layers.22.mlp.router` (GptOssTopKRouter)
- `model.layers.23.mlp.router` (GptOssTopKRouter)
- `lm_head` (Linear)

## Interpretation

- Block input: residual operand for the Attention addition.
- post_attention_layernorm input: Attention residual result / MLP residual operand.
- MLP first return tensor: MLP branch before residual addition.
- Block first return tensor: after both residual additions, before final model norm.
- Router tuple slots, attention weights and fused expert internals depend on the installed backend. Use records.jsonl for exact paths, dtypes, nonfinite counts and availability.
