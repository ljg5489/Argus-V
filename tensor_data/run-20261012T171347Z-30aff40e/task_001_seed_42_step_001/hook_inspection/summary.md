# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012934244355427647 / 2.7989374462784387 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 461, 461] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.5780381387722036e+38 / 1.4463957097184514e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 461, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7688620568873308 / 0.8910067305431617 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 461, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11423660487574454 / 0.6414496856756625 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 461] | torch.int64 → int64 | 0.0 / 460.0 / 230.0 / 133.07892395116517 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012934244355427647 / 2.7989374462784387 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 461, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.0073277740830209985 / 0.767417667106853 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 461, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.0073277740830209985 / 0.767417667106853 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 461, 461] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.5780381387722036e+38 / 1.4463957097184514e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 461] | torch.int64 → int64 | 0.0 / 460.0 / 230.0 / 133.07892395116517 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 461, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7688620568873308 / 0.8910067305431617 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 461, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11423660487574454 / 0.6414496856756625 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.0073277740830209985 / 0.767417667106853 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 461, 4096] | torch.bfloat16 → float32 | -9.0625 / 11.6875 / 0.0238593964414397 / 1.0127149401042872 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.0073277740830209985 / 0.767417667106853 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 461, 512] | torch.bfloat16 → float32 | -63.5 / 65.5 / 0.027607730073135127 / 5.769662606020432 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -30.5 / 15.0 / -0.0073277740830209985 / 0.767417667106853 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 461, 512] | torch.bfloat16 → float32 | -7.375 / 7.25 / -0.01147121275470081 / 1.1805541569891274 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 461, 4096] | torch.bfloat16 → float32 | -6.84375 / 6.46875 / -0.005928524591439193 / 0.5301891317024213 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 461, 2880] | torch.bfloat16 → float32 | -39.25 / 53.75 / 0.028174701999249402 / 1.1918827415432949 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -39.25 / 53.75 / 0.028174701999249402 / 1.1918827415432949 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 461, 461] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0008656076143323169 / 0.018724378822181493 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -87.5 / 71.0 / 0.01524194378749696 / 2.9954870520597146 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 461, 2880] | torch.bfloat16 → float32 | -6.625 / 3.0625 / 0.0007304579388573819 / 0.3287606438946176 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -6.625 / 3.0625 / 0.0007304579388573819 / 0.3287606438946176 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [461, 2880] | torch.bfloat16 → float32 | -6.625 / 3.0625 / 0.0007304579388573819 / 0.3287606438946176 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [461, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.01654789382086788 / 0.8258834848236096 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -49.25 / 135.0 / 0.01654789382086788 / 0.8258834848236096 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [461, 32] | torch.bfloat16 → float32 | -5.125 / 3.8125 / -0.10991265716883727 / 1.0189937731705183 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 461, 2880] | torch.bfloat16 → float32 | -85.0 / 156.0 / 0.031791317359665325 / 3.2448461665954422 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -41728.0 / 1088.0 / 0.40812688245058454 / 42.21743099707858 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 461, 461] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.691089413292523e+38 / 1.694761707331128e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 461, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7688620568873308 / 0.8910067305431617 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 461, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11423660487574454 / 0.6414496856756625 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 461] | torch.int64 → int64 | 0.0 / 460.0 / 230.0 / 133.07892395116517 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -41728.0 / 1088.0 / 0.40812688245058454 / 42.21743099707858 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 461, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05539116184430313 / 3.096948647965096 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 461, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05539116184430313 / 3.096948647965096 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 461, 461] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.691089413292523e+38 / 1.694761707331128e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 461] | torch.int64 → int64 | 0.0 / 460.0 / 230.0 / 133.07892395116517 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 461, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7688620568873308 / 0.8910067305431617 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 461, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11423660487574454 / 0.6414496856756625 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05539116184430313 / 3.096948647965096 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 461, 4096] | torch.bfloat16 → float32 | -12.9375 / 14.6875 / 0.04075645653825955 / 1.3744372154175215 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05539116184430313 / 3.096948647965096 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 461, 512] | torch.bfloat16 → float32 | -39.0 / 42.5 / 0.06398798672443483 / 3.364533062522158 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.05539116184430313 / 3.096948647965096 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 461, 512] | torch.bfloat16 → float32 | -16.0 / 22.0 / -0.01359208900513786 / 2.551073372883743 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 461, 4096] | torch.bfloat16 → float32 | -11.625 / 13.0 / -0.01430640598853765 / 1.4116379700083577 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 461, 2880] | torch.bfloat16 → float32 | -470.0 / 394.0 / -0.03214222273016499 / 5.542843296604102 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -470.0 / 394.0 / -0.03214222273016499 / 5.542843296604102 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 461, 461] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0018038335830993747 / 0.013617212974158572 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -41728.0 / 640.0 / 0.3760133733632163 / 41.774039376942206 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 461, 2880] | torch.bfloat16 → float32 | -78.5 / 6.4375 / 0.007246306901099552 / 0.7684680643688706 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -78.5 / 6.4375 / 0.007246306901099552 / 0.7684680643688706 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [461, 2880] | torch.bfloat16 → float32 | -78.5 / 6.4375 / 0.007246306901099552 / 0.7684680643688706 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [461, 2880] | torch.bfloat16 → float32 | -418.0 / 374.0 / 0.08702582755873767 / 7.945033869331079 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -418.0 / 374.0 / 0.08702582755873767 / 7.945033869331079 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [461, 32] | torch.bfloat16 → float32 | -10.75 / 3.078125 / -0.158266371087759 / 0.7471069892127172 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 461, 2880] | torch.bfloat16 → float32 | -41728.0 / 876.0 / 0.4630501525319895 / 44.19218654908591 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -12672.0 / 14208.0 / -0.9047086747418429 / 414.6722187041845 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 461, 461] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.691089413292523e+38 / 1.694761707331128e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 461, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7688620568873308 / 0.8910067305431617 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 461, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11423660487574454 / 0.6414496856756625 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 461] | torch.int64 → int64 | 0.0 / 460.0 / 230.0 / 133.07892395116517 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -12672.0 / 14208.0 / -0.9047086747418429 / 414.6722187041845 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 461, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010111434353844578 / 1.7636912204405486 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 461, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010111434353844578 / 1.7636912204405486 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 461, 461] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.691089413292523e+38 / 1.694761707331128e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 461] | torch.int64 → int64 | 0.0 / 460.0 / 230.0 / 133.07892395116517 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 461, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7688620568873308 / 0.8910067305431617 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 461, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11423660487574454 / 0.6414496856756625 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010111434353844578 / 1.7636912204405486 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 461, 4096] | torch.bfloat16 → float32 | -19.375 / 24.625 / 0.03549242044690664 / 1.6672380586252267 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010111434353844578 / 1.7636912204405486 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 461, 512] | torch.bfloat16 → float32 | -76.0 / 54.5 / -0.08817543365225931 / 4.642274029932995 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -57.25 / 71.0 / 0.010111434353844578 / 1.7636912204405486 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 461, 512] | torch.bfloat16 → float32 | -22.5 / 19.0 / -0.012817242552491951 / 3.2536659668368784 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 461, 4096] | torch.bfloat16 → float32 | -20.625 / 14.3125 / -0.006923847614276372 / 1.1033968120427575 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 461, 2880] | torch.bfloat16 → float32 | -4480.0 / 4800.0 / 2.318420399666896 / 139.07895934491964 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -4480.0 / 4800.0 / 2.318420399666896 / 139.07895934491964 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 461, 461] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0011012756398041943 / 0.009965351062069602 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -11200.0 / 11392.0 / 1.4135949205392584 / 358.4636007013932 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 461, 2880] | torch.bfloat16 → float32 | -50.25 / 20.125 / -0.013724883866650595 / 1.2156384322214377 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -50.25 / 20.125 / -0.013724883866650595 / 1.2156384322214377 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [461, 2880] | torch.bfloat16 → float32 | -50.25 / 20.125 / -0.013724883866650595 / 1.2156384322214377 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [461, 2880] | torch.bfloat16 → float32 | -6528.0 / 6496.0 / -1.2641042612810887 / 163.9935756316169 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 461, 2880] | torch.bfloat16 → float32 | -6528.0 / 6496.0 / -1.2641042612810887 / 163.9935756316169 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [461, 32] | torch.bfloat16 → float32 | -7.5625 / 4.21875 / 0.2643362074249996 / 2.5733986803342153 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 461, 2880] | torch.bfloat16 → float32 | -11840.0 / 12032.0 / 0.14955668234486097 / 416.3756389668168 | [NPY](tensors/0000116.npy) |

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
