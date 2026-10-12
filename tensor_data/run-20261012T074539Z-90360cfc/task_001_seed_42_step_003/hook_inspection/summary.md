# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 731 full tensors; 950 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Outside Transformer blocks

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model` | 0 | `input.kwargs['input_ids']` | [1, 395] | torch.int64 → int64 | 6.0 / 198835.0 / 29478.7164556962 / 44045.70868058883 | [NPY](tensors/0000000.npy) |
| 1 | `model` | 0 | `input.kwargs['attention_mask']` | [1, 395] | torch.int64 → int64 | 1.0 / 1.0 / 1.0 / 0.0 | [NPY](tensors/0000001.npy) |
| 2 | `model` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 3 | `model` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 4 | `model` | 0 | `input.kwargs['return_dict']` | — | bool | True | — |
| 5 | `model.embed_tokens` | 0 | `input.args[0]` | [1, 395] | torch.int64 → int64 | 6.0 / 198835.0 / 29478.7164556962 / 44045.70868058883 | [NPY](tensors/0000005.npy) |
| 6 | `model.embed_tokens` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.002628051764593734 / 2.769474062899876 | [NPY](tensors/0000006.npy) |
| 7 | `model.rotary_emb` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.002628051764593734 / 2.769474062899876 | [NPY](tensors/0000007.npy) |
| 8 | `model.rotary_emb` | 0 | `input.args[1]` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000008.npy) |
| 9 | `model.rotary_emb` | 0 | `output[0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000009.npy) |
| 10 | `model.rotary_emb` | 0 | `output[1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000010.npy) |
| 947 | `model.norm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -10880.0 / 10944.0 / -0.8523356772206839 / 390.0506987858363 | [NPY](tensors/0000947.npy) |
| 948 | `model.norm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -336.0 / 188.0 / -0.03905946120598816 / 6.873981137598574 | [NPY](tensors/0000948.npy) |
| 949 | `model` | 0 | `output['last_hidden_state']` | [1, 395, 2880] | torch.bfloat16 → float32 | -336.0 / 188.0 / -0.03905946120598816 / 6.873981137598574 | [NPY](tensors/0000949.npy) |

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | `model.layers.0` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.002628051764593734 / 2.769474062899876 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000013.npy) |
| 14 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000014.npy) |
| 15 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 17 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 18 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 19 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.002628051764593734 / 2.769474062899876 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0027924119715569693 / 0.7556595694574754 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0027924119715569693 / 0.7556595694574754 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 25 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 26 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 29 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0027924119715569693 / 0.7556595694574754 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -10.25 / 12.8125 / 0.0207215434167596 / 1.0497737176238222 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0027924119715569693 / 0.7556595694574754 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.026153782273265473 / 5.774759753009887 | [NPY](tensors/0000032.npy) |
| 33 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0027924119715569693 / 0.7556595694574754 | [NPY](tensors/0000033.npy) |
| 34 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -8.125 / 7.75 / -0.016498922722714752 / 1.2239569128211745 | [NPY](tensors/0000034.npy) |
| 35 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -8.125 / 7.75 / -0.007376189915939115 / 0.5567681976087566 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.02956279255777896 / 1.1848310392121721 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.02956279255777896 / 1.1848310392121721 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0009748929629927732 / 0.020573716331691583 | [NPY](tensors/0000038.npy) |
| 39 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -87.5 / 71.0 / 0.026935443735030467 / 2.950022914735606 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0013452232257055666 / 0.3450454479800405 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0013452232257055666 / 0.3450454479800405 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0013452232257055666 / 0.3450454479800405 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 44 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 45 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 46 | `model.layers.0.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.01930305899027866 / 0.914158145133216 | [NPY](tensors/0000046.npy) |
| 47 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.01930305899027866 / 0.914158145133216 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.0.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -5.0625 / 3.4375 / -0.10593767769729034 / 1.0148342856563717 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.0` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -92.0 / 105.5 / 0.04623313374031445 / 3.221196441191203 | [NPY](tensors/0000049.npy) |

## Layer 0001

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | `model.layers.1` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -92.0 / 105.5 / 0.04623313374031445 / 3.221196441191203 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.1` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.1` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000052.npy) |
| 53 | `model.layers.1` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000053.npy) |
| 54 | `model.layers.1` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.1` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 56 | `model.layers.1` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 57 | `model.layers.1` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 58 | `model.layers.1.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -92.0 / 105.5 / 0.04623313374031445 / 3.221196441191203 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.1.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.010668067179473559 / 0.8549110624962999 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.1.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.010668067179473559 / 0.8549110624962999 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.1.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.1.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 64 | `model.layers.1.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 65 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.1.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 68 | `model.layers.1.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.010668067179473559 / 0.8549110624962999 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.1.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -11.4375 / 12.25 / -0.018104773835495764 / 1.1115156087097016 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.1.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.010668067179473559 / 0.8549110624962999 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.1.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -111.0 / 44.25 / -0.7128951722081298 / 7.893883401025472 | [NPY](tensors/0000071.npy) |
| 72 | `model.layers.1.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.010668067179473559 / 0.8549110624962999 | [NPY](tensors/0000072.npy) |
| 73 | `model.layers.1.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -6.6875 / 8.0625 / 0.01683348575945873 / 1.0080316817160737 | [NPY](tensors/0000073.npy) |
| 74 | `model.layers.1.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -5.8125 / 5.9375 / 0.0034308640146695586 / 0.44684673617399445 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.1.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -33.75 / 53.0 / 0.003496479723539004 / 0.8414043179102841 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.1.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -33.75 / 53.0 / 0.003496479723539004 / 0.8414043179102841 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.1.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0017067079554025477 / 0.018398614180632038 | [NPY](tensors/0000077.npy) |
| 78 | `model.layers.1.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -90.0 / 82.0 / 0.04972993831258954 / 3.1765687294497353 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.1.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.421875 / 0.001552108968129976 / 0.37522020466397416 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.1.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.421875 / 0.001552108968129976 / 0.37522020466397416 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.1.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.421875 / 0.001552108968129976 / 0.37522020466397416 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.1.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 83 | `model.layers.1.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 84 | `model.layers.1.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 85 | `model.layers.1.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -47.25 / 82.5 / 0.02148761510366964 / 1.082084661649194 | [NPY](tensors/0000085.npy) |
| 86 | `model.layers.1.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -47.25 / 82.5 / 0.02148761510366964 / 1.082084661649194 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.1.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -2.890625 / 2.71875 / -0.09147443348848366 / 0.7314502298101111 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.1` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -109.5 / 131.0 / 0.07121269741809486 / 3.7156955674214682 | [NPY](tensors/0000088.npy) |

## Layer 0002

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 89 | `model.layers.2` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -109.5 / 131.0 / 0.07121269741809486 / 3.7156955674214682 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.2` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.2` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000091.npy) |
| 92 | `model.layers.2` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000092.npy) |
| 93 | `model.layers.2` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.2` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 95 | `model.layers.2` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 96 | `model.layers.2` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 97 | `model.layers.2.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -109.5 / 131.0 / 0.07121269741809486 / 3.7156955674214682 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.2.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -29.125 / 25.375 / 0.015631900807075022 / 0.8595413574659627 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.2.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -29.125 / 25.375 / 0.015631900807075022 / 0.8595413574659627 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.2.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.2.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 103 | `model.layers.2.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 104 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.2.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 107 | `model.layers.2.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -29.125 / 25.375 / 0.015631900807075022 / 0.8595413574659627 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.2.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -13.875 / 8.375 / 0.040221561822444185 / 0.8973857317005479 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.2.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -29.125 / 25.375 / 0.015631900807075022 / 0.8595413574659627 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.2.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -28.375 / 22.75 / -0.016818485495890784 / 2.612030044699422 | [NPY](tensors/0000110.npy) |
| 111 | `model.layers.2.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -29.125 / 25.375 / 0.015631900807075022 / 0.8595413574659627 | [NPY](tensors/0000111.npy) |
| 112 | `model.layers.2.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -8.0 / 6.0 / 0.02358396352899461 / 1.1604064109782728 | [NPY](tensors/0000112.npy) |
| 113 | `model.layers.2.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -6.53125 / 5.28125 / 0.012931550367235289 / 0.48136638061606435 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.2.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -47.5 / 55.0 / -0.0017119467928258993 / 0.9730035622197314 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.2.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -47.5 / 55.0 / -0.0017119467928258993 / 0.9730035622197314 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.2.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.001248829282556392 / 0.016432589431020595 | [NPY](tensors/0000116.npy) |
| 117 | `model.layers.2.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -83.0 / 123.0 / 0.06949616088142878 / 3.683862694675334 | [NPY](tensors/0000117.npy) |
| 118 | `model.layers.2.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.28125 / 0.00278870832232651 / 0.46587266001657557 | [NPY](tensors/0000118.npy) |
| 119 | `model.layers.2.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.28125 / 0.00278870832232651 / 0.46587266001657557 | [NPY](tensors/0000119.npy) |
| 120 | `model.layers.2.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.28125 / 0.00278870832232651 / 0.46587266001657557 | [NPY](tensors/0000120.npy) |
| 121 | `model.layers.2.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 122 | `model.layers.2.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 123 | `model.layers.2.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 124 | `model.layers.2.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -58.5 / 88.0 / 0.024470340249910634 / 1.2716094938859792 | [NPY](tensors/0000124.npy) |
| 125 | `model.layers.2.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -58.5 / 88.0 / 0.024470340249910634 / 1.2716094938859792 | [NPY](tensors/0000125.npy) |
| 126 | `model.layers.2.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -3.3125 / 2.203125 / -0.10330698520322389 / 0.678196441976568 | [NPY](tensors/0000126.npy) |
| 127 | `model.layers.2` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -117.0 / 148.0 / 0.09397565452023061 / 4.3414021693691005 | [NPY](tensors/0000127.npy) |

## Layer 0003

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | `model.layers.3` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -117.0 / 148.0 / 0.09397565452023061 / 4.3414021693691005 | [NPY](tensors/0000128.npy) |
| 129 | `model.layers.3` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000129.npy) |
| 130 | `model.layers.3` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000130.npy) |
| 131 | `model.layers.3` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000131.npy) |
| 132 | `model.layers.3` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000132.npy) |
| 133 | `model.layers.3` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 134 | `model.layers.3` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 135 | `model.layers.3` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 136 | `model.layers.3.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -117.0 / 148.0 / 0.09397565452023061 / 4.3414021693691005 | [NPY](tensors/0000136.npy) |
| 137 | `model.layers.3.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -57.0 / 56.5 / 0.03443962308781223 / 1.2501564049149827 | [NPY](tensors/0000137.npy) |
| 138 | `model.layers.3.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -57.0 / 56.5 / 0.03443962308781223 / 1.2501564049149827 | [NPY](tensors/0000138.npy) |
| 139 | `model.layers.3.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000139.npy) |
| 140 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000140.npy) |
| 141 | `model.layers.3.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 142 | `model.layers.3.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 143 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000143.npy) |
| 144 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000144.npy) |
| 145 | `model.layers.3.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 146 | `model.layers.3.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -57.0 / 56.5 / 0.03443962308781223 / 1.2501564049149827 | [NPY](tensors/0000146.npy) |
| 147 | `model.layers.3.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -13.0625 / 9.0 / -0.02293728152228509 / 1.1320711557996173 | [NPY](tensors/0000147.npy) |
| 148 | `model.layers.3.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -57.0 / 56.5 / 0.03443962308781223 / 1.2501564049149827 | [NPY](tensors/0000148.npy) |
| 149 | `model.layers.3.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -80.0 / 56.5 / -0.07015256299519369 / 4.968831158150308 | [NPY](tensors/0000149.npy) |
| 150 | `model.layers.3.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -57.0 / 56.5 / 0.03443962308781223 / 1.2501564049149827 | [NPY](tensors/0000150.npy) |
| 151 | `model.layers.3.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -7.65625 / 11.375 / 0.01535073769620702 / 0.9826132166856496 | [NPY](tensors/0000151.npy) |
| 152 | `model.layers.3.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -4.75 / 4.0625 / 0.010215359393000249 / 0.3449414587943074 | [NPY](tensors/0000152.npy) |
| 153 | `model.layers.3.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -63.25 / 52.0 / -0.0036877052527596933 / 1.0412775380339254 | [NPY](tensors/0000153.npy) |
| 154 | `model.layers.3.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -63.25 / 52.0 / -0.0036877052527596933 / 1.0412775380339254 | [NPY](tensors/0000154.npy) |
| 155 | `model.layers.3.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0014403366896041537 / 0.01198254733928024 | [NPY](tensors/0000155.npy) |
| 156 | `model.layers.3.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -103.0 / 134.0 / 0.09030030091100605 / 4.421170021584859 | [NPY](tensors/0000156.npy) |
| 157 | `model.layers.3.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -6.0 / 5.71875 / 0.0036258804968934185 / 0.5205473018155161 | [NPY](tensors/0000157.npy) |
| 158 | `model.layers.3.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -6.0 / 5.71875 / 0.0036258804968934185 / 0.5205473018155161 | [NPY](tensors/0000158.npy) |
| 159 | `model.layers.3.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -6.0 / 5.71875 / 0.0036258804968934185 / 0.5205473018155161 | [NPY](tensors/0000159.npy) |
| 160 | `model.layers.3.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 161 | `model.layers.3.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 162 | `model.layers.3.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 163 | `model.layers.3.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -61.25 / 94.0 / 0.021329806255891853 / 1.405382865120141 | [NPY](tensors/0000163.npy) |
| 164 | `model.layers.3.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -61.25 / 94.0 / 0.021329806255891853 / 1.405382865120141 | [NPY](tensors/0000164.npy) |
| 165 | `model.layers.3.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -3.265625 / 2.015625 / -0.07685475530503671 / 0.5437618018488399 | [NPY](tensors/0000165.npy) |
| 166 | `model.layers.3` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -150.0 / 171.0 / 0.11162540397563564 / 5.189479090712796 | [NPY](tensors/0000166.npy) |

## Layer 0004

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 167 | `model.layers.4` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -150.0 / 171.0 / 0.11162540397563564 / 5.189479090712796 | [NPY](tensors/0000167.npy) |
| 168 | `model.layers.4` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000168.npy) |
| 169 | `model.layers.4` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000169.npy) |
| 170 | `model.layers.4` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000170.npy) |
| 171 | `model.layers.4` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000171.npy) |
| 172 | `model.layers.4` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 173 | `model.layers.4` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 174 | `model.layers.4` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 175 | `model.layers.4.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -150.0 / 171.0 / 0.11162540397563564 / 5.189479090712796 | [NPY](tensors/0000175.npy) |
| 176 | `model.layers.4.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02135610625336442 / 1.1345366701825166 | [NPY](tensors/0000176.npy) |
| 177 | `model.layers.4.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02135610625336442 / 1.1345366701825166 | [NPY](tensors/0000177.npy) |
| 178 | `model.layers.4.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000178.npy) |
| 179 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000179.npy) |
| 180 | `model.layers.4.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 181 | `model.layers.4.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 182 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000182.npy) |
| 183 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000183.npy) |
| 184 | `model.layers.4.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 185 | `model.layers.4.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02135610625336442 / 1.1345366701825166 | [NPY](tensors/0000185.npy) |
| 186 | `model.layers.4.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -16.875 / 8.1875 / -0.010282992511991646 / 1.0384383003869329 | [NPY](tensors/0000186.npy) |
| 187 | `model.layers.4.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02135610625336442 / 1.1345366701825166 | [NPY](tensors/0000187.npy) |
| 188 | `model.layers.4.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -14.25 / 99.0 / 0.24484106964207714 / 4.399768505915969 | [NPY](tensors/0000188.npy) |
| 189 | `model.layers.4.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02135610625336442 / 1.1345366701825166 | [NPY](tensors/0000189.npy) |
| 190 | `model.layers.4.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -10.8125 / 16.25 / 0.005358910816132173 / 1.3562073413329792 | [NPY](tensors/0000190.npy) |
| 191 | `model.layers.4.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -9.625 / 15.0 / -0.002434349544743863 / 0.6059467418159422 | [NPY](tensors/0000191.npy) |
| 192 | `model.layers.4.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -69.0 / 44.5 / -0.0015715764774174626 / 1.2455433051031932 | [NPY](tensors/0000192.npy) |
| 193 | `model.layers.4.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -69.0 / 44.5 / -0.0015715764774174626 / 1.2455433051031932 | [NPY](tensors/0000193.npy) |
| 194 | `model.layers.4.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0013194637497923156 / 0.01581043006627574 | [NPY](tensors/0000194.npy) |
| 195 | `model.layers.4.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -134.0 / 150.0 / 0.11004530169792821 / 5.214802454885411 | [NPY](tensors/0000195.npy) |
| 196 | `model.layers.4.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -5.84375 / 6.90625 / 0.0070710255408924175 / 0.5763435889425902 | [NPY](tensors/0000196.npy) |
| 197 | `model.layers.4.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -5.84375 / 6.90625 / 0.0070710255408924175 / 0.5763435889425902 | [NPY](tensors/0000197.npy) |
| 198 | `model.layers.4.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -5.84375 / 6.90625 / 0.0070710255408924175 / 0.5763435889425902 | [NPY](tensors/0000198.npy) |
| 199 | `model.layers.4.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 200 | `model.layers.4.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 201 | `model.layers.4.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 202 | `model.layers.4.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -81.0 / 165.0 / 0.040169553361235795 / 2.11642617062194 | [NPY](tensors/0000202.npy) |
| 203 | `model.layers.4.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -81.0 / 165.0 / 0.040169553361235795 / 2.11642617062194 | [NPY](tensors/0000203.npy) |
| 204 | `model.layers.4.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -3.46875 / 2.171875 / -0.09029446372502967 / 0.6067763924088967 | [NPY](tensors/0000204.npy) |
| 205 | `model.layers.4` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -192.0 / 254.0 / 0.15021830519878746 / 6.448259782264532 | [NPY](tensors/0000205.npy) |

## Layer 0005

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 206 | `model.layers.5` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -192.0 / 254.0 / 0.15021830519878746 / 6.448259782264532 | [NPY](tensors/0000206.npy) |
| 207 | `model.layers.5` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000207.npy) |
| 208 | `model.layers.5` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000208.npy) |
| 209 | `model.layers.5` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000209.npy) |
| 210 | `model.layers.5` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000210.npy) |
| 211 | `model.layers.5` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 212 | `model.layers.5` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 213 | `model.layers.5` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 214 | `model.layers.5.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -192.0 / 254.0 / 0.15021830519878746 / 6.448259782264532 | [NPY](tensors/0000214.npy) |
| 215 | `model.layers.5.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -30.625 / 41.0 / 0.03395827375425736 / 1.182038366819465 | [NPY](tensors/0000215.npy) |
| 216 | `model.layers.5.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -30.625 / 41.0 / 0.03395827375425736 / 1.182038366819465 | [NPY](tensors/0000216.npy) |
| 217 | `model.layers.5.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000217.npy) |
| 218 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000218.npy) |
| 219 | `model.layers.5.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 220 | `model.layers.5.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 221 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000221.npy) |
| 222 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000222.npy) |
| 223 | `model.layers.5.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 224 | `model.layers.5.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -30.625 / 41.0 / 0.03395827375425736 / 1.182038366819465 | [NPY](tensors/0000224.npy) |
| 225 | `model.layers.5.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -19.875 / 16.25 / -0.058720020471690386 / 1.444463431658084 | [NPY](tensors/0000225.npy) |
| 226 | `model.layers.5.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -30.625 / 41.0 / 0.03395827375425736 / 1.182038366819465 | [NPY](tensors/0000226.npy) |
| 227 | `model.layers.5.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -35.25 / 39.5 / -0.04706409997520438 / 3.4875821904226623 | [NPY](tensors/0000227.npy) |
| 228 | `model.layers.5.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -30.625 / 41.0 / 0.03395827375425736 / 1.182038366819465 | [NPY](tensors/0000228.npy) |
| 229 | `model.layers.5.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -7.25 / 8.3125 / 0.013926912166024971 / 1.2024838998772127 | [NPY](tensors/0000229.npy) |
| 230 | `model.layers.5.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -5.25 / 5.46875 / 0.009415332908892501 / 0.5475330484039848 | [NPY](tensors/0000230.npy) |
| 231 | `model.layers.5.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -92.0 / 79.0 / -0.0020752536641818952 / 1.5716537614518196 | [NPY](tensors/0000231.npy) |
| 232 | `model.layers.5.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -92.0 / 79.0 / -0.0020752536641818952 / 1.5716537614518196 | [NPY](tensors/0000232.npy) |
| 233 | `model.layers.5.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0015352506707429548 / 0.012742380215025748 | [NPY](tensors/0000233.npy) |
| 234 | `model.layers.5.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -143.0 / 208.0 / 0.1481413903775849 / 6.847836841403382 | [NPY](tensors/0000234.npy) |
| 235 | `model.layers.5.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.125 / 0.007273911381174408 / 0.5640095528600431 | [NPY](tensors/0000235.npy) |
| 236 | `model.layers.5.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.125 / 0.007273911381174408 / 0.5640095528600431 | [NPY](tensors/0000236.npy) |
| 237 | `model.layers.5.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.125 / 0.007273911381174408 / 0.5640095528600431 | [NPY](tensors/0000237.npy) |
| 238 | `model.layers.5.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 239 | `model.layers.5.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 240 | `model.layers.5.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 241 | `model.layers.5.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -126.5 / 117.0 / 0.03986083561944895 / 2.3796805158333756 | [NPY](tensors/0000241.npy) |
| 242 | `model.layers.5.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -126.5 / 117.0 / 0.03986083561944895 / 2.3796805158333756 | [NPY](tensors/0000242.npy) |
| 243 | `model.layers.5.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -4.375 / 2.265625 / -0.09111435322821895 / 0.5990145780928405 | [NPY](tensors/0000243.npy) |
| 244 | `model.layers.5` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -196.0 / 296.0 / 0.18799289070268893 / 8.257263363189514 | [NPY](tensors/0000244.npy) |

## Layer 0006

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 245 | `model.layers.6` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -196.0 / 296.0 / 0.18799289070268893 / 8.257263363189514 | [NPY](tensors/0000245.npy) |
| 246 | `model.layers.6` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000246.npy) |
| 247 | `model.layers.6` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000247.npy) |
| 248 | `model.layers.6` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000248.npy) |
| 249 | `model.layers.6` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000249.npy) |
| 250 | `model.layers.6` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 251 | `model.layers.6` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 252 | `model.layers.6` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 253 | `model.layers.6.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -196.0 / 296.0 / 0.18799289070268893 / 8.257263363189514 | [NPY](tensors/0000253.npy) |
| 254 | `model.layers.6.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -34.25 / 43.0 / 0.030284706938660762 / 1.307823795361067 | [NPY](tensors/0000254.npy) |
| 255 | `model.layers.6.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -34.25 / 43.0 / 0.030284706938660762 / 1.307823795361067 | [NPY](tensors/0000255.npy) |
| 256 | `model.layers.6.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000256.npy) |
| 257 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000257.npy) |
| 258 | `model.layers.6.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 259 | `model.layers.6.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 260 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000260.npy) |
| 261 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000261.npy) |
| 262 | `model.layers.6.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 263 | `model.layers.6.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -34.25 / 43.0 / 0.030284706938660762 / 1.307823795361067 | [NPY](tensors/0000263.npy) |
| 264 | `model.layers.6.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -29.125 / 16.875 / -0.025835078559777937 / 1.1532952690247638 | [NPY](tensors/0000264.npy) |
| 265 | `model.layers.6.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -34.25 / 43.0 / 0.030284706938660762 / 1.307823795361067 | [NPY](tensors/0000265.npy) |
| 266 | `model.layers.6.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -20.375 / 33.0 / 0.2160372369290518 / 2.3933394414500757 | [NPY](tensors/0000266.npy) |
| 267 | `model.layers.6.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -34.25 / 43.0 / 0.030284706938660762 / 1.307823795361067 | [NPY](tensors/0000267.npy) |
| 268 | `model.layers.6.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -10.5625 / 8.6875 / -0.04883602484161789 / 1.6186864341451825 | [NPY](tensors/0000268.npy) |
| 269 | `model.layers.6.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -9.625 / 7.6875 / -0.03403096960801122 / 0.8111027314666747 | [NPY](tensors/0000269.npy) |
| 270 | `model.layers.6.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -90.5 / 82.0 / -0.00012044042703838404 / 1.8062437550624375 | [NPY](tensors/0000270.npy) |
| 271 | `model.layers.6.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -90.5 / 82.0 / -0.00012044042703838404 / 1.8062437550624375 | [NPY](tensors/0000271.npy) |
| 272 | `model.layers.6.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0014331254105736935 / 0.01733323201517607 | [NPY](tensors/0000272.npy) |
| 273 | `model.layers.6.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -180.0 / 247.0 / 0.18787287676552344 / 8.189647390929618 | [NPY](tensors/0000273.npy) |
| 274 | `model.layers.6.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -22.0 / 5.25 / 0.01052745935513668 / 0.6005158980490907 | [NPY](tensors/0000274.npy) |
| 275 | `model.layers.6.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -22.0 / 5.25 / 0.01052745935513668 / 0.6005158980490907 | [NPY](tensors/0000275.npy) |
| 276 | `model.layers.6.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -22.0 / 5.25 / 0.01052745935513668 / 0.6005158980490907 | [NPY](tensors/0000276.npy) |
| 277 | `model.layers.6.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 278 | `model.layers.6.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 279 | `model.layers.6.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 280 | `model.layers.6.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -41472.0 / 968.0 / -0.004693533697711762 / 39.044505393702046 | [NPY](tensors/0000280.npy) |
| 281 | `model.layers.6.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41472.0 / 968.0 / -0.004693533697711762 / 39.044505393702046 | [NPY](tensors/0000281.npy) |
| 282 | `model.layers.6.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -4.375 / 5.0 / -0.12327794425095184 / 0.7660153659898757 | [NPY](tensors/0000282.npy) |
| 283 | `model.layers.6` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.1832757282927737 / 40.18833210917254 | [NPY](tensors/0000283.npy) |

## Layer 0007

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 284 | `model.layers.7` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.1832757282927737 / 40.18833210917254 | [NPY](tensors/0000284.npy) |
| 285 | `model.layers.7` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000285.npy) |
| 286 | `model.layers.7` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000286.npy) |
| 287 | `model.layers.7` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000287.npy) |
| 288 | `model.layers.7` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000288.npy) |
| 289 | `model.layers.7` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 290 | `model.layers.7` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 291 | `model.layers.7` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 292 | `model.layers.7.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.1832757282927737 / 40.18833210917254 | [NPY](tensors/0000292.npy) |
| 293 | `model.layers.7.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.037073947269831035 / 1.6206094704940472 | [NPY](tensors/0000293.npy) |
| 294 | `model.layers.7.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.037073947269831035 / 1.6206094704940472 | [NPY](tensors/0000294.npy) |
| 295 | `model.layers.7.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000295.npy) |
| 296 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000296.npy) |
| 297 | `model.layers.7.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 298 | `model.layers.7.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 299 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000299.npy) |
| 300 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000300.npy) |
| 301 | `model.layers.7.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 302 | `model.layers.7.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.037073947269831035 / 1.6206094704940472 | [NPY](tensors/0000302.npy) |
| 303 | `model.layers.7.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -13.5625 / 13.25 / -0.11971835129955288 / 1.4385689150702863 | [NPY](tensors/0000303.npy) |
| 304 | `model.layers.7.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.037073947269831035 / 1.6206094704940472 | [NPY](tensors/0000304.npy) |
| 305 | `model.layers.7.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -132.0 / 34.0 / -0.06840579138797578 / 5.485153242774677 | [NPY](tensors/0000305.npy) |
| 306 | `model.layers.7.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.037073947269831035 / 1.6206094704940472 | [NPY](tensors/0000306.npy) |
| 307 | `model.layers.7.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -17.0 / 10.8125 / 0.0064090935030032565 / 1.6407334747247013 | [NPY](tensors/0000307.npy) |
| 308 | `model.layers.7.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -7.65625 / 8.0625 / 0.001988339611563178 / 0.9341604223375618 | [NPY](tensors/0000308.npy) |
| 309 | `model.layers.7.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -121.0 / 129.0 / 0.0009889396392961667 / 2.272980506742802 | [NPY](tensors/0000309.npy) |
| 310 | `model.layers.7.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -121.0 / 129.0 / 0.0009889396392961667 / 2.272980506742802 | [NPY](tensors/0000310.npy) |
| 311 | `model.layers.7.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0020160144243749115 / 0.01975131275087058 | [NPY](tensors/0000311.npy) |
| 312 | `model.layers.7.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41472.0 / 1104.0 / 0.18424870161064566 / 40.22608332146835 | [NPY](tensors/0000312.npy) |
| 313 | `model.layers.7.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -77.0 / 6.25 / 0.009871058736452321 / 0.6201838009346644 | [NPY](tensors/0000313.npy) |
| 314 | `model.layers.7.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -77.0 / 6.25 / 0.009871058736452321 / 0.6201838009346644 | [NPY](tensors/0000314.npy) |
| 315 | `model.layers.7.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -77.0 / 6.25 / 0.009871058736452321 / 0.6201838009346644 | [NPY](tensors/0000315.npy) |
| 316 | `model.layers.7.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 317 | `model.layers.7.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 318 | `model.layers.7.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 319 | `model.layers.7.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -159.0 / 168.0 / 0.03661435275976501 / 3.413382724205878 | [NPY](tensors/0000319.npy) |
| 320 | `model.layers.7.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -159.0 / 168.0 / 0.03661435275976501 / 3.413382724205878 | [NPY](tensors/0000320.npy) |
| 321 | `model.layers.7.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -3.890625 / 3.828125 / -0.14247866431369058 / 0.8142596321217258 | [NPY](tensors/0000321.npy) |
| 322 | `model.layers.7` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.2208863842638233 / 40.7628704262114 | [NPY](tensors/0000322.npy) |

## Layer 0008

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 323 | `model.layers.8` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.2208863842638233 / 40.7628704262114 | [NPY](tensors/0000323.npy) |
| 324 | `model.layers.8` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000324.npy) |
| 325 | `model.layers.8` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000325.npy) |
| 326 | `model.layers.8` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000326.npy) |
| 327 | `model.layers.8` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000327.npy) |
| 328 | `model.layers.8` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 329 | `model.layers.8` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 330 | `model.layers.8` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 331 | `model.layers.8.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.2208863842638233 / 40.7628704262114 | [NPY](tensors/0000331.npy) |
| 332 | `model.layers.8.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -121.5 / 43.75 / 0.02877291919155316 / 1.32442218648229 | [NPY](tensors/0000332.npy) |
| 333 | `model.layers.8.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -121.5 / 43.75 / 0.02877291919155316 / 1.32442218648229 | [NPY](tensors/0000333.npy) |
| 334 | `model.layers.8.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000334.npy) |
| 335 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000335.npy) |
| 336 | `model.layers.8.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 337 | `model.layers.8.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 338 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000338.npy) |
| 339 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000339.npy) |
| 340 | `model.layers.8.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 341 | `model.layers.8.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -121.5 / 43.75 / 0.02877291919155316 / 1.32442218648229 | [NPY](tensors/0000341.npy) |
| 342 | `model.layers.8.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -14.9375 / 15.25 / -0.010449629610211328 / 1.0648538342273883 | [NPY](tensors/0000342.npy) |
| 343 | `model.layers.8.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -121.5 / 43.75 / 0.02877291919155316 / 1.32442218648229 | [NPY](tensors/0000343.npy) |
| 344 | `model.layers.8.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -22.5 / 31.5 / 0.004775852876232017 / 2.242088980767959 | [NPY](tensors/0000344.npy) |
| 345 | `model.layers.8.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -121.5 / 43.75 / 0.02877291919155316 / 1.32442218648229 | [NPY](tensors/0000345.npy) |
| 346 | `model.layers.8.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -9.3125 / 9.625 / -0.0008919135321084929 / 1.7151175984171303 | [NPY](tensors/0000346.npy) |
| 347 | `model.layers.8.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -7.21875 / 7.21875 / 0.003278088131730927 / 0.8609788152540709 | [NPY](tensors/0000347.npy) |
| 348 | `model.layers.8.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -199.0 / 212.0 / 0.013147853441934629 / 2.8595326089082893 | [NPY](tensors/0000348.npy) |
| 349 | `model.layers.8.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -199.0 / 212.0 / 0.013147853441934629 / 2.8595326089082893 | [NPY](tensors/0000349.npy) |
| 350 | `model.layers.8.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0015841226211304718 / 0.01665480132095744 | [NPY](tensors/0000350.npy) |
| 351 | `model.layers.8.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41472.0 / 1344.0 / 0.234018755918146 / 40.72313036506251 | [NPY](tensors/0000351.npy) |
| 352 | `model.layers.8.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -57.0 / 6.40625 / 0.010154502745036627 / 0.6559209408837222 | [NPY](tensors/0000352.npy) |
| 353 | `model.layers.8.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -57.0 / 6.40625 / 0.010154502745036627 / 0.6559209408837222 | [NPY](tensors/0000353.npy) |
| 354 | `model.layers.8.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -57.0 / 6.40625 / 0.010154502745036627 / 0.6559209408837222 | [NPY](tensors/0000354.npy) |
| 355 | `model.layers.8.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 356 | `model.layers.8.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 357 | `model.layers.8.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 358 | `model.layers.8.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -294.0 / 250.0 / 0.055514193312192935 / 4.676031717619744 | [NPY](tensors/0000358.npy) |
| 359 | `model.layers.8.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -294.0 / 250.0 / 0.055514193312192935 / 4.676031717619744 | [NPY](tensors/0000359.npy) |
| 360 | `model.layers.8.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -3.921875 / 3.53125 / -0.17847835293299036 / 0.7664903200064368 | [NPY](tensors/0000360.npy) |
| 361 | `model.layers.8` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.2894694681610237 / 41.83405437119064 | [NPY](tensors/0000361.npy) |

## Layer 0009

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 362 | `model.layers.9` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.2894694681610237 / 41.83405437119064 | [NPY](tensors/0000362.npy) |
| 363 | `model.layers.9` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000363.npy) |
| 364 | `model.layers.9` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000364.npy) |
| 365 | `model.layers.9` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000365.npy) |
| 366 | `model.layers.9` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000366.npy) |
| 367 | `model.layers.9` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 368 | `model.layers.9` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 369 | `model.layers.9` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 370 | `model.layers.9.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.2894694681610237 / 41.83405437119064 | [NPY](tensors/0000370.npy) |
| 371 | `model.layers.9.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.0407173355500071 / 1.7818909323470606 | [NPY](tensors/0000371.npy) |
| 372 | `model.layers.9.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.0407173355500071 / 1.7818909323470606 | [NPY](tensors/0000372.npy) |
| 373 | `model.layers.9.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000373.npy) |
| 374 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000374.npy) |
| 375 | `model.layers.9.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 376 | `model.layers.9.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 377 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000377.npy) |
| 378 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000378.npy) |
| 379 | `model.layers.9.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 380 | `model.layers.9.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.0407173355500071 / 1.7818909323470606 | [NPY](tensors/0000380.npy) |
| 381 | `model.layers.9.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -10.5 / 20.25 / 0.06330340089375165 / 1.296798176528403 | [NPY](tensors/0000381.npy) |
| 382 | `model.layers.9.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.0407173355500071 / 1.7818909323470606 | [NPY](tensors/0000382.npy) |
| 383 | `model.layers.9.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -51.25 / 43.75 / 0.04364952336631338 / 3.963047967084513 | [NPY](tensors/0000383.npy) |
| 384 | `model.layers.9.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.0407173355500071 / 1.7818909323470606 | [NPY](tensors/0000384.npy) |
| 385 | `model.layers.9.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -27.75 / 12.4375 / -0.005891744293201762 / 1.478750199982903 | [NPY](tensors/0000385.npy) |
| 386 | `model.layers.9.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -11.0 / 8.8125 / 0.0021706652873943514 / 0.6736351073715147 | [NPY](tensors/0000386.npy) |
| 387 | `model.layers.9.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -348.0 / 344.0 / 0.028911551661192116 / 3.6484120934094637 | [NPY](tensors/0000387.npy) |
| 388 | `model.layers.9.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -348.0 / 344.0 / 0.028911551661192116 / 3.6484120934094637 | [NPY](tensors/0000388.npy) |
| 389 | `model.layers.9.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0019993581162735126 / 0.016396006005395158 | [NPY](tensors/0000389.npy) |
| 390 | `model.layers.9.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41728.0 / 1480.0 / 0.31840722623253676 / 41.7969739593481 | [NPY](tensors/0000390.npy) |
| 391 | `model.layers.9.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -64.5 / 6.75 / 0.010861530325856223 / 0.6736443254995211 | [NPY](tensors/0000391.npy) |
| 392 | `model.layers.9.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -64.5 / 6.75 / 0.010861530325856223 / 0.6736443254995211 | [NPY](tensors/0000392.npy) |
| 393 | `model.layers.9.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -64.5 / 6.75 / 0.010861530325856223 / 0.6736443254995211 | [NPY](tensors/0000393.npy) |
| 394 | `model.layers.9.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 395 | `model.layers.9.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 396 | `model.layers.9.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 397 | `model.layers.9.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -568.0 / 636.0 / 0.04127647848571906 / 5.334348111047046 | [NPY](tensors/0000397.npy) |
| 398 | `model.layers.9.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -568.0 / 636.0 / 0.04127647848571906 / 5.334348111047046 | [NPY](tensors/0000398.npy) |
| 399 | `model.layers.9.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -5.1875 / 6.40625 / -0.13452827357038666 / 0.6258706955026557 | [NPY](tensors/0000399.npy) |
| 400 | `model.layers.9` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.3597210164345099 / 42.46205492629778 | [NPY](tensors/0000400.npy) |

## Layer 0010

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 401 | `model.layers.10` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.3597210164345099 / 42.46205492629778 | [NPY](tensors/0000401.npy) |
| 402 | `model.layers.10` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000402.npy) |
| 403 | `model.layers.10` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000403.npy) |
| 404 | `model.layers.10` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000404.npy) |
| 405 | `model.layers.10` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000405.npy) |
| 406 | `model.layers.10` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 407 | `model.layers.10` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 408 | `model.layers.10` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 409 | `model.layers.10.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.3597210164345099 / 42.46205492629778 | [NPY](tensors/0000409.npy) |
| 410 | `model.layers.10.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.034254180210656925 / 1.533619164800205 | [NPY](tensors/0000410.npy) |
| 411 | `model.layers.10.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.034254180210656925 / 1.533619164800205 | [NPY](tensors/0000411.npy) |
| 412 | `model.layers.10.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000412.npy) |
| 413 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000413.npy) |
| 414 | `model.layers.10.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 415 | `model.layers.10.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 416 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000416.npy) |
| 417 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000417.npy) |
| 418 | `model.layers.10.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 419 | `model.layers.10.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.034254180210656925 / 1.533619164800205 | [NPY](tensors/0000419.npy) |
| 420 | `model.layers.10.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -15.875 / 18.125 / 0.03304313918488333 / 1.1061370297152744 | [NPY](tensors/0000420.npy) |
| 421 | `model.layers.10.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.034254180210656925 / 1.533619164800205 | [NPY](tensors/0000421.npy) |
| 422 | `model.layers.10.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -56.25 / 16.875 / -0.06189624674948333 / 2.3406644469913336 | [NPY](tensors/0000422.npy) |
| 423 | `model.layers.10.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.034254180210656925 / 1.533619164800205 | [NPY](tensors/0000423.npy) |
| 424 | `model.layers.10.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -10.4375 / 10.6875 / 0.061955108972195576 / 2.116890300603444 | [NPY](tensors/0000424.npy) |
| 425 | `model.layers.10.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -8.0 / 8.6875 / 0.04343734423703297 / 1.0266176346325135 | [NPY](tensors/0000425.npy) |
| 426 | `model.layers.10.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -203.0 / 233.0 / 0.054196459038756827 / 4.188501537828805 | [NPY](tensors/0000426.npy) |
| 427 | `model.layers.10.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -203.0 / 233.0 / 0.054196459038756827 / 4.188501537828805 | [NPY](tensors/0000427.npy) |
| 428 | `model.layers.10.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.0016347138681068693 / 0.013628219441951975 | [NPY](tensors/0000428.npy) |
| 429 | `model.layers.10.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 924.0 / 0.41393540903150444 / 42.29390138225055 | [NPY](tensors/0000429.npy) |
| 430 | `model.layers.10.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -46.75 / 7.34375 / 0.01284430834762071 / 0.7281619891330294 | [NPY](tensors/0000430.npy) |
| 431 | `model.layers.10.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -46.75 / 7.34375 / 0.01284430834762071 / 0.7281619891330294 | [NPY](tensors/0000431.npy) |
| 432 | `model.layers.10.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -46.75 / 7.34375 / 0.01284430834762071 / 0.7281619891330294 | [NPY](tensors/0000432.npy) |
| 433 | `model.layers.10.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 434 | `model.layers.10.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 435 | `model.layers.10.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 436 | `model.layers.10.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -700.0 / 896.0 / 0.12645497721458787 / 7.513194659104535 | [NPY](tensors/0000436.npy) |
| 437 | `model.layers.10.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -700.0 / 896.0 / 0.12645497721458787 / 7.513194659104535 | [NPY](tensors/0000437.npy) |
| 438 | `model.layers.10.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -5.3125 / 4.03125 / -0.11951755571968947 / 0.628473919128153 | [NPY](tensors/0000438.npy) |
| 439 | `model.layers.10` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.5404284779566082 / 44.20855577845985 | [NPY](tensors/0000439.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 440 | `model.layers.11` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.5404284779566082 / 44.20855577845985 | [NPY](tensors/0000440.npy) |
| 441 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000441.npy) |
| 442 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000442.npy) |
| 443 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000443.npy) |
| 444 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000444.npy) |
| 445 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 446 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 447 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 448 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.5404284779566082 / 44.20855577845985 | [NPY](tensors/0000448.npy) |
| 449 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.07029564310918375 / 3.1532855729947262 | [NPY](tensors/0000449.npy) |
| 450 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.07029564310918375 / 3.1532855729947262 | [NPY](tensors/0000450.npy) |
| 451 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000451.npy) |
| 452 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000452.npy) |
| 453 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 454 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 455 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000455.npy) |
| 456 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000456.npy) |
| 457 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 458 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.07029564310918375 / 3.1532855729947262 | [NPY](tensors/0000458.npy) |
| 459 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -11.875 / 13.3125 / 0.038101462194045095 / 1.3505143861277518 | [NPY](tensors/0000459.npy) |
| 460 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.07029564310918375 / 3.1532855729947262 | [NPY](tensors/0000460.npy) |
| 461 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -41.25 / 48.25 / 0.08283494939641509 / 3.7776485677275375 | [NPY](tensors/0000461.npy) |
| 462 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -191.0 / 139.0 / 0.07029564310918375 / 3.1532855729947262 | [NPY](tensors/0000462.npy) |
| 463 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -15.875 / 22.125 / -0.04114642629364529 / 2.511548081288343 | [NPY](tensors/0000463.npy) |
| 464 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -11.625 / 11.8125 / -0.033705145542064455 / 1.4785003281223057 | [NPY](tensors/0000464.npy) |
| 465 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -464.0 / 502.0 / -0.01916254390340231 / 6.238415493771649 | [NPY](tensors/0000465.npy) |
| 466 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -464.0 / 502.0 / -0.01916254390340231 / 6.238415493771649 | [NPY](tensors/0000466.npy) |
| 467 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002196809979999701 / 0.015126778908783972 | [NPY](tensors/0000467.npy) |
| 468 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 700.0 / 0.5212365949606593 / 43.55837538700344 | [NPY](tensors/0000468.npy) |
| 469 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -78.5 / 7.59375 / 0.011946588771577539 / 0.7803379505095241 | [NPY](tensors/0000469.npy) |
| 470 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -78.5 / 7.59375 / 0.011946588771577539 / 0.7803379505095241 | [NPY](tensors/0000470.npy) |
| 471 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -78.5 / 7.59375 / 0.011946588771577539 / 0.7803379505095241 | [NPY](tensors/0000471.npy) |
| 472 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 473 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 474 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 475 | `model.layers.11.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -568.0 / 410.0 / 0.11424909021448651 / 9.124349729175528 | [NPY](tensors/0000475.npy) |
| 476 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -568.0 / 410.0 / 0.11424909021448651 / 9.124349729175528 | [NPY](tensors/0000476.npy) |
| 477 | `model.layers.11.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.1500065634522257 / 0.723030253039005 | [NPY](tensors/0000477.npy) |
| 478 | `model.layers.11` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.6354374901386588 / 46.257923135836926 | [NPY](tensors/0000478.npy) |

## Layer 0012

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 479 | `model.layers.12` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.6354374901386588 / 46.257923135836926 | [NPY](tensors/0000479.npy) |
| 480 | `model.layers.12` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000480.npy) |
| 481 | `model.layers.12` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000481.npy) |
| 482 | `model.layers.12` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000482.npy) |
| 483 | `model.layers.12` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000483.npy) |
| 484 | `model.layers.12` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 485 | `model.layers.12` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 486 | `model.layers.12` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 487 | `model.layers.12.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.6354374901386588 / 46.257923135836926 | [NPY](tensors/0000487.npy) |
| 488 | `model.layers.12.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -136.0 / 46.5 / 0.04288172237386432 / 1.5856207761658976 | [NPY](tensors/0000488.npy) |
| 489 | `model.layers.12.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -136.0 / 46.5 / 0.04288172237386432 / 1.5856207761658976 | [NPY](tensors/0000489.npy) |
| 490 | `model.layers.12.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000490.npy) |
| 491 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000491.npy) |
| 492 | `model.layers.12.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 493 | `model.layers.12.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 494 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000494.npy) |
| 495 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000495.npy) |
| 496 | `model.layers.12.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 497 | `model.layers.12.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -136.0 / 46.5 / 0.04288172237386432 / 1.5856207761658976 | [NPY](tensors/0000497.npy) |
| 498 | `model.layers.12.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -19.75 / 18.375 / -0.019249630265145656 / 1.359462975117725 | [NPY](tensors/0000498.npy) |
| 499 | `model.layers.12.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -136.0 / 46.5 / 0.04288172237386432 / 1.5856207761658976 | [NPY](tensors/0000499.npy) |
| 500 | `model.layers.12.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -12.75 / 13.0 / 0.010315823150633634 / 1.3292162286738995 | [NPY](tensors/0000500.npy) |
| 501 | `model.layers.12.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -136.0 / 46.5 / 0.04288172237386432 / 1.5856207761658976 | [NPY](tensors/0000501.npy) |
| 502 | `model.layers.12.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -17.125 / 19.375 / 0.015796705964316107 / 2.887293235874922 | [NPY](tensors/0000502.npy) |
| 503 | `model.layers.12.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -10.625 / 11.0 / 0.0020606800556234196 / 1.5300862569222349 | [NPY](tensors/0000503.npy) |
| 504 | `model.layers.12.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -284.0 / 326.0 / -0.016755327672452656 / 5.8535300083699715 | [NPY](tensors/0000504.npy) |
| 505 | `model.layers.12.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -284.0 / 326.0 / -0.016755327672452656 / 5.8535300083699715 | [NPY](tensors/0000505.npy) |
| 506 | `model.layers.12.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 0.96875 / 0.0017020425548751113 / 0.014076199409873105 | [NPY](tensors/0000506.npy) |
| 507 | `model.layers.12.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 708.0 / 0.6187420470000319 / 45.60897977787882 | [NPY](tensors/0000507.npy) |
| 508 | `model.layers.12.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -83.5 / 8.25 / 0.012307285760776908 / 0.8316406384547604 | [NPY](tensors/0000508.npy) |
| 509 | `model.layers.12.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -83.5 / 8.25 / 0.012307285760776908 / 0.8316406384547604 | [NPY](tensors/0000509.npy) |
| 510 | `model.layers.12.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -83.5 / 8.25 / 0.012307285760776908 / 0.8316406384547604 | [NPY](tensors/0000510.npy) |
| 511 | `model.layers.12.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 512 | `model.layers.12.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 513 | `model.layers.12.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 514 | `model.layers.12.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -1696.0 / 1496.0 / 0.13336131610950838 / 11.071983390069262 | [NPY](tensors/0000514.npy) |
| 515 | `model.layers.12.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -1696.0 / 1496.0 / 0.13336131610950838 / 11.071983390069262 | [NPY](tensors/0000515.npy) |
| 516 | `model.layers.12.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -6.9375 / 3.8125 / -0.14804669875132886 / 0.7452245616496069 | [NPY](tensors/0000516.npy) |
| 517 | `model.layers.12` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 1808.0 / 0.7520248083659198 / 49.28237278616648 | [NPY](tensors/0000517.npy) |

## Layer 0013

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 518 | `model.layers.13` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 1808.0 / 0.7520248083659198 / 49.28237278616648 | [NPY](tensors/0000518.npy) |
| 519 | `model.layers.13` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000519.npy) |
| 520 | `model.layers.13` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000520.npy) |
| 521 | `model.layers.13` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000521.npy) |
| 522 | `model.layers.13` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000522.npy) |
| 523 | `model.layers.13` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 524 | `model.layers.13` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 525 | `model.layers.13` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 526 | `model.layers.13.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 1808.0 / 0.7520248083659198 / 49.28237278616648 | [NPY](tensors/0000526.npy) |
| 527 | `model.layers.13.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -182.0 / 103.0 / 0.06793503082471307 / 2.8546075311537558 | [NPY](tensors/0000527.npy) |
| 528 | `model.layers.13.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -182.0 / 103.0 / 0.06793503082471307 / 2.8546075311537558 | [NPY](tensors/0000528.npy) |
| 529 | `model.layers.13.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000529.npy) |
| 530 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000530.npy) |
| 531 | `model.layers.13.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 532 | `model.layers.13.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 533 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000533.npy) |
| 534 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000534.npy) |
| 535 | `model.layers.13.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 536 | `model.layers.13.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -182.0 / 103.0 / 0.06793503082471307 / 2.8546075311537558 | [NPY](tensors/0000536.npy) |
| 537 | `model.layers.13.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -10.6875 / 12.5625 / 0.04078632363875668 / 1.4236574722838111 | [NPY](tensors/0000537.npy) |
| 538 | `model.layers.13.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -182.0 / 103.0 / 0.06793503082471307 / 2.8546075311537558 | [NPY](tensors/0000538.npy) |
| 539 | `model.layers.13.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -57.5 / 35.25 / -0.3397070337909191 / 4.184148458586774 | [NPY](tensors/0000539.npy) |
| 540 | `model.layers.13.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -182.0 / 103.0 / 0.06793503082471307 / 2.8546075311537558 | [NPY](tensors/0000540.npy) |
| 541 | `model.layers.13.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -16.5 / 22.5 / 0.00566111328139241 / 2.893164414972583 | [NPY](tensors/0000541.npy) |
| 542 | `model.layers.13.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -14.0625 / 20.875 / 0.00751742183262097 / 1.6529770715141854 | [NPY](tensors/0000542.npy) |
| 543 | `model.layers.13.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -564.0 / 1176.0 / -0.04478959280208969 / 8.442504395166427 | [NPY](tensors/0000543.npy) |
| 544 | `model.layers.13.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -564.0 / 1176.0 / -0.04478959280208969 / 8.442504395166427 | [NPY](tensors/0000544.npy) |
| 545 | `model.layers.13.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0023119870227080504 / 0.015068323763301831 | [NPY](tensors/0000545.npy) |
| 546 | `model.layers.13.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 1296.0 / 0.7072523184935924 / 48.206555901967086 | [NPY](tensors/0000546.npy) |
| 547 | `model.layers.13.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -86.0 / 6.875 / 0.012130357193041449 / 0.9200912718082915 | [NPY](tensors/0000547.npy) |
| 548 | `model.layers.13.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -86.0 / 6.875 / 0.012130357193041449 / 0.9200912718082915 | [NPY](tensors/0000548.npy) |
| 549 | `model.layers.13.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -86.0 / 6.875 / 0.012130357193041449 / 0.9200912718082915 | [NPY](tensors/0000549.npy) |
| 550 | `model.layers.13.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 551 | `model.layers.13.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 552 | `model.layers.13.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 553 | `model.layers.13.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -476.0 / 588.0 / 0.07852212162963448 / 12.639877212702459 | [NPY](tensors/0000553.npy) |
| 554 | `model.layers.13.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -476.0 / 588.0 / 0.07852212162963448 / 12.639877212702459 | [NPY](tensors/0000554.npy) |
| 555 | `model.layers.13.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -5.46875 / 3.796875 / -0.17692070218581188 / 0.8073919388120773 | [NPY](tensors/0000555.npy) |
| 556 | `model.layers.13` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 1160.0 / 0.7857418497034602 / 52.888795635317265 | [NPY](tensors/0000556.npy) |

## Layer 0014

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 557 | `model.layers.14` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 1160.0 / 0.7857418497034602 / 52.888795635317265 | [NPY](tensors/0000557.npy) |
| 558 | `model.layers.14` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000558.npy) |
| 559 | `model.layers.14` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000559.npy) |
| 560 | `model.layers.14` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000560.npy) |
| 561 | `model.layers.14` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000561.npy) |
| 562 | `model.layers.14` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 563 | `model.layers.14` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 564 | `model.layers.14` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 565 | `model.layers.14.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 1160.0 / 0.7857418497034602 / 52.888795635317265 | [NPY](tensors/0000565.npy) |
| 566 | `model.layers.14.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -148.0 / 50.5 / 0.05064129942999275 / 1.9409084244500503 | [NPY](tensors/0000566.npy) |
| 567 | `model.layers.14.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -148.0 / 50.5 / 0.05064129942999275 / 1.9409084244500503 | [NPY](tensors/0000567.npy) |
| 568 | `model.layers.14.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000568.npy) |
| 569 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000569.npy) |
| 570 | `model.layers.14.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 571 | `model.layers.14.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 572 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000572.npy) |
| 573 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000573.npy) |
| 574 | `model.layers.14.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 575 | `model.layers.14.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -148.0 / 50.5 / 0.05064129942999275 / 1.9409084244500503 | [NPY](tensors/0000575.npy) |
| 576 | `model.layers.14.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -53.25 / 29.25 / -0.06537452793642921 / 2.120604148919869 | [NPY](tensors/0000576.npy) |
| 577 | `model.layers.14.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -148.0 / 50.5 / 0.05064129942999275 / 1.9409084244500503 | [NPY](tensors/0000577.npy) |
| 578 | `model.layers.14.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -37.75 / 19.625 / 0.03799571601454393 / 1.6204893696967388 | [NPY](tensors/0000578.npy) |
| 579 | `model.layers.14.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -148.0 / 50.5 / 0.05064129942999275 / 1.9409084244500503 | [NPY](tensors/0000579.npy) |
| 580 | `model.layers.14.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -23.875 / 22.625 / -0.011671837867249416 / 4.757347310428832 | [NPY](tensors/0000580.npy) |
| 581 | `model.layers.14.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -21.875 / 18.625 / -0.011835194842915883 / 2.666623413785962 | [NPY](tensors/0000581.npy) |
| 582 | `model.layers.14.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -304.0 / 334.0 / -0.018637445904052544 / 8.561313329043495 | [NPY](tensors/0000582.npy) |
| 583 | `model.layers.14.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -304.0 / 334.0 / -0.018637445904052544 / 8.561313329043495 | [NPY](tensors/0000583.npy) |
| 584 | `model.layers.14.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 0.97265625 / 0.0016558864195825402 / 0.016462170613366855 | [NPY](tensors/0000584.npy) |
| 585 | `model.layers.14.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.7670320225969145 / 52.05887756396968 | [NPY](tensors/0000585.npy) |
| 586 | `model.layers.14.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -99.0 / 9.75 / 0.013601284892037616 / 0.9925455692409837 | [NPY](tensors/0000586.npy) |
| 587 | `model.layers.14.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -99.0 / 9.75 / 0.013601284892037616 / 0.9925455692409837 | [NPY](tensors/0000587.npy) |
| 588 | `model.layers.14.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -99.0 / 9.75 / 0.013601284892037616 / 0.9925455692409837 | [NPY](tensors/0000588.npy) |
| 589 | `model.layers.14.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 590 | `model.layers.14.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 591 | `model.layers.14.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 592 | `model.layers.14.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -1296.0 / 1136.0 / 0.05521967383544321 / 17.140648717130507 | [NPY](tensors/0000592.npy) |
| 593 | `model.layers.14.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -1296.0 / 1136.0 / 0.05521967383544321 / 17.140648717130507 | [NPY](tensors/0000593.npy) |
| 594 | `model.layers.14.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -6.84375 / 6.53125 / -0.24323210776606694 / 0.7603045265459399 | [NPY](tensors/0000594.npy) |
| 595 | `model.layers.14` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 2032.0 / 0.8222344466369028 / 59.58937365582044 | [NPY](tensors/0000595.npy) |

## Layer 0015

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 596 | `model.layers.15` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 2032.0 / 0.8222344466369028 / 59.58937365582044 | [NPY](tensors/0000596.npy) |
| 597 | `model.layers.15` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000597.npy) |
| 598 | `model.layers.15` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000598.npy) |
| 599 | `model.layers.15` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000599.npy) |
| 600 | `model.layers.15` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000600.npy) |
| 601 | `model.layers.15` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 602 | `model.layers.15` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 603 | `model.layers.15` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 604 | `model.layers.15.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 2032.0 / 0.8222344466369028 / 59.58937365582044 | [NPY](tensors/0000604.npy) |
| 605 | `model.layers.15.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -164.0 / 66.5 / 0.05150262949021557 / 2.1700836776872072 | [NPY](tensors/0000605.npy) |
| 606 | `model.layers.15.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -164.0 / 66.5 / 0.05150262949021557 / 2.1700836776872072 | [NPY](tensors/0000606.npy) |
| 607 | `model.layers.15.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000607.npy) |
| 608 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000608.npy) |
| 609 | `model.layers.15.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 610 | `model.layers.15.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 611 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000611.npy) |
| 612 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000612.npy) |
| 613 | `model.layers.15.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 614 | `model.layers.15.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -164.0 / 66.5 / 0.05150262949021557 / 2.1700836776872072 | [NPY](tensors/0000614.npy) |
| 615 | `model.layers.15.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -21.25 / 19.875 / 0.012128062947563712 / 1.4711013444776313 | [NPY](tensors/0000615.npy) |
| 616 | `model.layers.15.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -164.0 / 66.5 / 0.05150262949021557 / 2.1700836776872072 | [NPY](tensors/0000616.npy) |
| 617 | `model.layers.15.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -40.5 / 52.25 / 0.03516541584571706 / 4.192359388883793 | [NPY](tensors/0000617.npy) |
| 618 | `model.layers.15.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -164.0 / 66.5 / 0.05150262949021557 / 2.1700836776872072 | [NPY](tensors/0000618.npy) |
| 619 | `model.layers.15.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -61.5 / 38.5 / -0.1303704369873622 / 2.89670904396506 | [NPY](tensors/0000619.npy) |
| 620 | `model.layers.15.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -14.3125 / 20.5 / -0.10236736782976359 / 1.504850359540351 | [NPY](tensors/0000620.npy) |
| 621 | `model.layers.15.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -1696.0 / 1720.0 / 0.044020619968531335 / 12.738789764581115 | [NPY](tensors/0000621.npy) |
| 622 | `model.layers.15.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -1696.0 / 1720.0 / 0.044020619968531335 / 12.738789764581115 | [NPY](tensors/0000622.npy) |
| 623 | `model.layers.15.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0019350173184236282 / 0.014735340152713758 | [NPY](tensors/0000623.npy) |
| 624 | `model.layers.15.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 1160.0 / 0.8663601616431558 / 58.45775223725204 | [NPY](tensors/0000624.npy) |
| 625 | `model.layers.15.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -106.0 / 10.375 / 0.01579051232727771 / 1.0093866877013036 | [NPY](tensors/0000625.npy) |
| 626 | `model.layers.15.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -106.0 / 10.375 / 0.01579051232727771 / 1.0093866877013036 | [NPY](tensors/0000626.npy) |
| 627 | `model.layers.15.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -106.0 / 10.375 / 0.01579051232727771 / 1.0093866877013036 | [NPY](tensors/0000627.npy) |
| 628 | `model.layers.15.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 629 | `model.layers.15.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 630 | `model.layers.15.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 631 | `model.layers.15.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -788.0 / 728.0 / -0.1732085916865224 / 20.443579803236062 | [NPY](tensors/0000631.npy) |
| 632 | `model.layers.15.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -788.0 / 728.0 / -0.1732085916865224 / 20.443579803236062 | [NPY](tensors/0000632.npy) |
| 633 | `model.layers.15.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -5.5625 / 4.34375 / -0.2638685190224949 / 0.9379371799605316 | [NPY](tensors/0000633.npy) |
| 634 | `model.layers.15` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 1456.0 / 0.6930219707676798 / 67.79494900181935 | [NPY](tensors/0000634.npy) |

## Layer 0016

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 635 | `model.layers.16` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 1456.0 / 0.6930219707676798 / 67.79494900181935 | [NPY](tensors/0000635.npy) |
| 636 | `model.layers.16` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000636.npy) |
| 637 | `model.layers.16` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000637.npy) |
| 638 | `model.layers.16` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000638.npy) |
| 639 | `model.layers.16` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000639.npy) |
| 640 | `model.layers.16` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 641 | `model.layers.16` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 642 | `model.layers.16` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 643 | `model.layers.16.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 1456.0 / 0.6930219707676798 / 67.79494900181935 | [NPY](tensors/0000643.npy) |
| 644 | `model.layers.16.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -131.0 / 51.5 / 0.038611401834023486 / 1.9046662242007428 | [NPY](tensors/0000644.npy) |
| 645 | `model.layers.16.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -131.0 / 51.5 / 0.038611401834023486 / 1.9046662242007428 | [NPY](tensors/0000645.npy) |
| 646 | `model.layers.16.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000646.npy) |
| 647 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000647.npy) |
| 648 | `model.layers.16.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 649 | `model.layers.16.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 650 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000650.npy) |
| 651 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000651.npy) |
| 652 | `model.layers.16.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 653 | `model.layers.16.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -131.0 / 51.5 / 0.038611401834023486 / 1.9046662242007428 | [NPY](tensors/0000653.npy) |
| 654 | `model.layers.16.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -25.375 / 25.875 / 0.030034717199620756 / 1.7199612903170107 | [NPY](tensors/0000654.npy) |
| 655 | `model.layers.16.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -131.0 / 51.5 / 0.038611401834023486 / 1.9046662242007428 | [NPY](tensors/0000655.npy) |
| 656 | `model.layers.16.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -14.875 / 32.25 / 0.04334254397515538 / 1.6189847337782322 | [NPY](tensors/0000656.npy) |
| 657 | `model.layers.16.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -131.0 / 51.5 / 0.038611401834023486 / 1.9046662242007428 | [NPY](tensors/0000657.npy) |
| 658 | `model.layers.16.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -22.875 / 26.625 / 0.002535394567383242 / 4.4154504821625284 | [NPY](tensors/0000658.npy) |
| 659 | `model.layers.16.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -21.125 / 20.375 / -0.007436407584340418 / 1.988900731774343 | [NPY](tensors/0000659.npy) |
| 660 | `model.layers.16.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -548.0 / 552.0 / 0.037194534390536035 / 13.074054007280928 | [NPY](tensors/0000660.npy) |
| 661 | `model.layers.16.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -548.0 / 552.0 / 0.037194534390536035 / 13.074054007280928 | [NPY](tensors/0000661.npy) |
| 662 | `model.layers.16.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 0.953125 / 0.0013595422734625773 / 0.013724072995923884 | [NPY](tensors/0000662.npy) |
| 663 | `model.layers.16.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 1528.0 / 0.7302746621734145 / 67.9523639205745 | [NPY](tensors/0000663.npy) |
| 664 | `model.layers.16.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -68.0 / 10.0 / 0.014758865633761999 / 0.9742588952771137 | [NPY](tensors/0000664.npy) |
| 665 | `model.layers.16.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -68.0 / 10.0 / 0.014758865633761999 / 0.9742588952771137 | [NPY](tensors/0000665.npy) |
| 666 | `model.layers.16.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -68.0 / 10.0 / 0.014758865633761999 / 0.9742588952771137 | [NPY](tensors/0000666.npy) |
| 667 | `model.layers.16.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 668 | `model.layers.16.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 669 | `model.layers.16.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 670 | `model.layers.16.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -2400.0 / 1736.0 / -0.18590659217995428 / 29.837231609138406 | [NPY](tensors/0000670.npy) |
| 671 | `model.layers.16.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -2400.0 / 1736.0 / -0.18590659217995428 / 29.837231609138406 | [NPY](tensors/0000671.npy) |
| 672 | `model.layers.16.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -6.375 / 4.46875 / -0.29721438703657704 / 1.2366264644886296 | [NPY](tensors/0000672.npy) |
| 673 | `model.layers.16` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 2656.0 / 0.5443155577883607 / 85.16619178180643 | [NPY](tensors/0000673.npy) |

## Layer 0017

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 674 | `model.layers.17` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 2656.0 / 0.5443155577883607 / 85.16619178180643 | [NPY](tensors/0000674.npy) |
| 675 | `model.layers.17` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000675.npy) |
| 676 | `model.layers.17` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000676.npy) |
| 677 | `model.layers.17` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000677.npy) |
| 678 | `model.layers.17` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000678.npy) |
| 679 | `model.layers.17` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 680 | `model.layers.17` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 681 | `model.layers.17` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 682 | `model.layers.17.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 2656.0 / 0.5443155577883607 / 85.16619178180643 | [NPY](tensors/0000682.npy) |
| 683 | `model.layers.17.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04710952492412468 / 2.695214917359122 | [NPY](tensors/0000683.npy) |
| 684 | `model.layers.17.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04710952492412468 / 2.695214917359122 | [NPY](tensors/0000684.npy) |
| 685 | `model.layers.17.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000685.npy) |
| 686 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000686.npy) |
| 687 | `model.layers.17.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 688 | `model.layers.17.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 689 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000689.npy) |
| 690 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000690.npy) |
| 691 | `model.layers.17.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 692 | `model.layers.17.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04710952492412468 / 2.695214917359122 | [NPY](tensors/0000692.npy) |
| 693 | `model.layers.17.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -23.0 / 29.375 / 0.01370669405127668 / 1.6295978238397015 | [NPY](tensors/0000693.npy) |
| 694 | `model.layers.17.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04710952492412468 / 2.695214917359122 | [NPY](tensors/0000694.npy) |
| 695 | `model.layers.17.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -68.0 / 44.0 / -0.003835414847008342 / 5.138490430132717 | [NPY](tensors/0000695.npy) |
| 696 | `model.layers.17.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04710952492412468 / 2.695214917359122 | [NPY](tensors/0000696.npy) |
| 697 | `model.layers.17.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -19.5 / 21.875 / 0.12708984541152663 / 3.0967441982649437 | [NPY](tensors/0000697.npy) |
| 698 | `model.layers.17.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -11.375 / 11.75 / 0.07712623156973528 / 1.3419187722551682 | [NPY](tensors/0000698.npy) |
| 699 | `model.layers.17.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -1520.0 / 1568.0 / 0.25082663427006174 / 20.10987828881472 | [NPY](tensors/0000699.npy) |
| 700 | `model.layers.17.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -1520.0 / 1568.0 / 0.25082663427006174 / 20.10987828881472 | [NPY](tensors/0000700.npy) |
| 701 | `model.layers.17.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.001969555699716421 / 0.017146871804120258 | [NPY](tensors/0000701.npy) |
| 702 | `model.layers.17.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41216.0 / 1872.0 / 0.7952516453309737 / 82.29211666186967 | [NPY](tensors/0000702.npy) |
| 703 | `model.layers.17.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41.75 / 10.3125 / 0.01230003355235993 / 0.9570471081392659 | [NPY](tensors/0000703.npy) |
| 704 | `model.layers.17.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41.75 / 10.3125 / 0.01230003355235993 / 0.9570471081392659 | [NPY](tensors/0000704.npy) |
| 705 | `model.layers.17.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -41.75 / 10.3125 / 0.01230003355235993 / 0.9570471081392659 | [NPY](tensors/0000705.npy) |
| 706 | `model.layers.17.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 707 | `model.layers.17.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 708 | `model.layers.17.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 709 | `model.layers.17.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -1176.0 / 40448.0 / -0.08595012504172558 / 52.17947335099123 | [NPY](tensors/0000709.npy) |
| 710 | `model.layers.17.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -1176.0 / 40448.0 / -0.08595012504172558 / 52.17947335099123 | [NPY](tensors/0000710.npy) |
| 711 | `model.layers.17.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -4.90625 / 2.96875 / -0.19869317887704582 / 0.952289981803211 | [NPY](tensors/0000711.npy) |
| 712 | `model.layers.17` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -2432.0 / 2512.0 / 0.7094342139736343 / 95.91860474857401 | [NPY](tensors/0000712.npy) |

## Layer 0018

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 713 | `model.layers.18` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -2432.0 / 2512.0 / 0.7094342139736343 / 95.91860474857401 | [NPY](tensors/0000713.npy) |
| 714 | `model.layers.18` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000714.npy) |
| 715 | `model.layers.18` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000715.npy) |
| 716 | `model.layers.18` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000716.npy) |
| 717 | `model.layers.18` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000717.npy) |
| 718 | `model.layers.18` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 719 | `model.layers.18` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 720 | `model.layers.18` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 721 | `model.layers.18.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -2432.0 / 2512.0 / 0.7094342139736343 / 95.91860474857401 | [NPY](tensors/0000721.npy) |
| 722 | `model.layers.18.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -45.5 / 39.25 / 0.024120118637292864 / 1.6006757564245755 | [NPY](tensors/0000722.npy) |
| 723 | `model.layers.18.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -45.5 / 39.25 / 0.024120118637292864 / 1.6006757564245755 | [NPY](tensors/0000723.npy) |
| 724 | `model.layers.18.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000724.npy) |
| 725 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000725.npy) |
| 726 | `model.layers.18.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 727 | `model.layers.18.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 728 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000728.npy) |
| 729 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000729.npy) |
| 730 | `model.layers.18.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 731 | `model.layers.18.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -45.5 / 39.25 / 0.024120118637292864 / 1.6006757564245755 | [NPY](tensors/0000731.npy) |
| 732 | `model.layers.18.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -27.0 / 32.0 / 0.11986659993886815 / 1.8712106641170754 | [NPY](tensors/0000732.npy) |
| 733 | `model.layers.18.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -45.5 / 39.25 / 0.024120118637292864 / 1.6006757564245755 | [NPY](tensors/0000733.npy) |
| 734 | `model.layers.18.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -19.375 / 49.5 / 0.12114933682870874 / 2.269849460150903 | [NPY](tensors/0000734.npy) |
| 735 | `model.layers.18.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -45.5 / 39.25 / 0.024120118637292864 / 1.6006757564245755 | [NPY](tensors/0000735.npy) |
| 736 | `model.layers.18.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -26.125 / 23.75 / -0.2337241945151664 / 4.364223689399658 | [NPY](tensors/0000736.npy) |
| 737 | `model.layers.18.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -21.0 / 20.125 / -0.11789590006916988 / 1.9469897119126862 | [NPY](tensors/0000737.npy) |
| 738 | `model.layers.18.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -588.0 / 736.0 / -0.2580700252416286 / 21.759671702954034 | [NPY](tensors/0000738.npy) |
| 739 | `model.layers.18.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -588.0 / 736.0 / -0.2580700252416286 / 21.759671702954034 | [NPY](tensors/0000739.npy) |
| 740 | `model.layers.18.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.001210595339340499 / 0.015196406310725281 | [NPY](tensors/0000740.npy) |
| 741 | `model.layers.18.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -2400.0 / 2464.0 / 0.451611631315846 / 102.73616308032865 | [NPY](tensors/0000741.npy) |
| 742 | `model.layers.18.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -7.78125 / 13.25 / 0.006373305774798951 / 0.9200123659139687 | [NPY](tensors/0000742.npy) |
| 743 | `model.layers.18.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -7.78125 / 13.25 / 0.006373305774798951 / 0.9200123659139687 | [NPY](tensors/0000743.npy) |
| 744 | `model.layers.18.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -7.78125 / 13.25 / 0.006373305774798951 / 0.9200123659139687 | [NPY](tensors/0000744.npy) |
| 745 | `model.layers.18.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 746 | `model.layers.18.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 747 | `model.layers.18.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 748 | `model.layers.18.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -2112.0 / 2832.0 / 0.12018053746256979 / 52.69644662263415 | [NPY](tensors/0000748.npy) |
| 749 | `model.layers.18.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -2112.0 / 2832.0 / 0.12018053746256979 / 52.69644662263415 | [NPY](tensors/0000749.npy) |
| 750 | `model.layers.18.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -4.96875 / 2.65625 / -0.32591670193249667 / 1.055342530708743 | [NPY](tensors/0000750.npy) |
| 751 | `model.layers.18` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.5716031214288855 / 138.80714910353 | [NPY](tensors/0000751.npy) |

## Layer 0019

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 752 | `model.layers.19` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.5716031214288855 / 138.80714910353 | [NPY](tensors/0000752.npy) |
| 753 | `model.layers.19` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000753.npy) |
| 754 | `model.layers.19` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000754.npy) |
| 755 | `model.layers.19` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000755.npy) |
| 756 | `model.layers.19` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000756.npy) |
| 757 | `model.layers.19` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 758 | `model.layers.19` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 759 | `model.layers.19` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 760 | `model.layers.19.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.5716031214288855 / 138.80714910353 | [NPY](tensors/0000760.npy) |
| 761 | `model.layers.19.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.015754999603693663 / 1.8243434828899199 | [NPY](tensors/0000761.npy) |
| 762 | `model.layers.19.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.015754999603693663 / 1.8243434828899199 | [NPY](tensors/0000762.npy) |
| 763 | `model.layers.19.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000763.npy) |
| 764 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000764.npy) |
| 765 | `model.layers.19.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 766 | `model.layers.19.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 767 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000767.npy) |
| 768 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000768.npy) |
| 769 | `model.layers.19.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 770 | `model.layers.19.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.015754999603693663 / 1.8243434828899199 | [NPY](tensors/0000770.npy) |
| 771 | `model.layers.19.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -15.875 / 24.5 / -0.03343474545353148 / 1.3233811051864866 | [NPY](tensors/0000771.npy) |
| 772 | `model.layers.19.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.015754999603693663 / 1.8243434828899199 | [NPY](tensors/0000772.npy) |
| 773 | `model.layers.19.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -84.5 / 72.0 / -0.09950869631085213 / 7.28790515515961 | [NPY](tensors/0000773.npy) |
| 774 | `model.layers.19.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.015754999603693663 / 1.8243434828899199 | [NPY](tensors/0000774.npy) |
| 775 | `model.layers.19.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -15.875 / 18.875 / -0.02625565858722865 / 3.198552758307961 | [NPY](tensors/0000775.npy) |
| 776 | `model.layers.19.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -12.25 / 11.9375 / -0.009800866173863937 / 1.0386168957740658 | [NPY](tensors/0000776.npy) |
| 777 | `model.layers.19.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -2144.0 / 1912.0 / -0.5072888960513259 / 42.774762402742226 | [NPY](tensors/0000777.npy) |
| 778 | `model.layers.19.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -2144.0 / 1912.0 / -0.5072888960513259 / 42.774762402742226 | [NPY](tensors/0000778.npy) |
| 779 | `model.layers.19.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.0010937214557322319 / 0.0092354387413844 | [NPY](tensors/0000779.npy) |
| 780 | `model.layers.19.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -3616.0 / 3344.0 / 0.06403315043818263 / 123.34212001364244 | [NPY](tensors/0000780.npy) |
| 781 | `model.layers.19.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -7.0625 / 18.625 / 0.004794881918929968 / 1.0171559498425526 | [NPY](tensors/0000781.npy) |
| 782 | `model.layers.19.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -7.0625 / 18.625 / 0.004794881918929968 / 1.0171559498425526 | [NPY](tensors/0000782.npy) |
| 783 | `model.layers.19.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -7.0625 / 18.625 / 0.004794881918929968 / 1.0171559498425526 | [NPY](tensors/0000783.npy) |
| 784 | `model.layers.19.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 785 | `model.layers.19.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 786 | `model.layers.19.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 787 | `model.layers.19.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -2640.0 / 3008.0 / 0.2681506966136176 / 85.68447856484956 | [NPY](tensors/0000787.npy) |
| 788 | `model.layers.19.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -2640.0 / 3008.0 / 0.2681506966136176 / 85.68447856484956 | [NPY](tensors/0000788.npy) |
| 789 | `model.layers.19.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -7.875 / 3.046875 / -0.2893501619749431 / 1.5532655070722026 | [NPY](tensors/0000789.npy) |
| 790 | `model.layers.19` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -4992.0 / 4704.0 / 0.3319784900005357 / 182.27755279937583 | [NPY](tensors/0000790.npy) |

## Layer 0020

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 791 | `model.layers.20` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -4992.0 / 4704.0 / 0.3319784900005357 / 182.27755279937583 | [NPY](tensors/0000791.npy) |
| 792 | `model.layers.20` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000792.npy) |
| 793 | `model.layers.20` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000793.npy) |
| 794 | `model.layers.20` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000794.npy) |
| 795 | `model.layers.20` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000795.npy) |
| 796 | `model.layers.20` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 797 | `model.layers.20` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 798 | `model.layers.20` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 799 | `model.layers.20.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -4992.0 / 4704.0 / 0.3319784900005357 / 182.27755279937583 | [NPY](tensors/0000799.npy) |
| 800 | `model.layers.20.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.011561122597437537 / 1.5416300610589755 | [NPY](tensors/0000800.npy) |
| 801 | `model.layers.20.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.011561122597437537 / 1.5416300610589755 | [NPY](tensors/0000801.npy) |
| 802 | `model.layers.20.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000802.npy) |
| 803 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000803.npy) |
| 804 | `model.layers.20.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 805 | `model.layers.20.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 806 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000806.npy) |
| 807 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000807.npy) |
| 808 | `model.layers.20.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 809 | `model.layers.20.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.011561122597437537 / 1.5416300610589755 | [NPY](tensors/0000809.npy) |
| 810 | `model.layers.20.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -23.0 / 21.125 / 0.04293437379838688 / 1.2599687616048318 | [NPY](tensors/0000810.npy) |
| 811 | `model.layers.20.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.011561122597437537 / 1.5416300610589755 | [NPY](tensors/0000811.npy) |
| 812 | `model.layers.20.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -30.625 / 37.0 / -0.09564683835944633 / 2.2404398154002365 | [NPY](tensors/0000812.npy) |
| 813 | `model.layers.20.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.011561122597437537 / 1.5416300610589755 | [NPY](tensors/0000813.npy) |
| 814 | `model.layers.20.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -22.375 / 22.25 / 0.021219964066072353 / 3.936257012950663 | [NPY](tensors/0000814.npy) |
| 815 | `model.layers.20.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -17.75 / 16.375 / -0.004034760330301373 / 1.3034452894566448 | [NPY](tensors/0000815.npy) |
| 816 | `model.layers.20.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -1056.0 / 1080.0 / -0.2248714400386718 / 26.200253065821514 | [NPY](tensors/0000816.npy) |
| 817 | `model.layers.20.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -1056.0 / 1080.0 / -0.2248714400386718 / 26.200253065821514 | [NPY](tensors/0000817.npy) |
| 818 | `model.layers.20.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0009836471854621086 / 0.012456286028736814 | [NPY](tensors/0000818.npy) |
| 819 | `model.layers.20.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -4864.0 / 4864.0 / 0.10711944204510179 / 184.48070379387977 | [NPY](tensors/0000819.npy) |
| 820 | `model.layers.20.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -7.0 / 20.375 / 0.002596640843169766 / 0.9760962424437155 | [NPY](tensors/0000820.npy) |
| 821 | `model.layers.20.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -7.0 / 20.375 / 0.002596640843169766 / 0.9760962424437155 | [NPY](tensors/0000821.npy) |
| 822 | `model.layers.20.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -7.0 / 20.375 / 0.002596640843169766 / 0.9760962424437155 | [NPY](tensors/0000822.npy) |
| 823 | `model.layers.20.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 824 | `model.layers.20.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 825 | `model.layers.20.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 826 | `model.layers.20.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -5888.0 / 6816.0 / 0.32926151384951874 / 80.97468870618177 | [NPY](tensors/0000826.npy) |
| 827 | `model.layers.20.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -5888.0 / 6816.0 / 0.32926151384951874 / 80.97468870618177 | [NPY](tensors/0000827.npy) |
| 828 | `model.layers.20.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -6.0 / 4.25 / -0.19000228145454504 / 1.2804424934376264 | [NPY](tensors/0000828.npy) |
| 829 | `model.layers.20` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -9216.0 / 10368.0 / 0.4365672933200241 / 241.9774240960144 | [NPY](tensors/0000829.npy) |

## Layer 0021

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 830 | `model.layers.21` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -9216.0 / 10368.0 / 0.4365672933200241 / 241.9774240960144 | [NPY](tensors/0000830.npy) |
| 831 | `model.layers.21` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000831.npy) |
| 832 | `model.layers.21` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000832.npy) |
| 833 | `model.layers.21` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000833.npy) |
| 834 | `model.layers.21` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000834.npy) |
| 835 | `model.layers.21` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 836 | `model.layers.21` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 837 | `model.layers.21` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 838 | `model.layers.21.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -9216.0 / 10368.0 / 0.4365672933200241 / 241.9774240960144 | [NPY](tensors/0000838.npy) |
| 839 | `model.layers.21.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.006907834836534642 / 1.8018382100867925 | [NPY](tensors/0000839.npy) |
| 840 | `model.layers.21.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.006907834836534642 / 1.8018382100867925 | [NPY](tensors/0000840.npy) |
| 841 | `model.layers.21.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000841.npy) |
| 842 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000842.npy) |
| 843 | `model.layers.21.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 844 | `model.layers.21.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 845 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000845.npy) |
| 846 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000846.npy) |
| 847 | `model.layers.21.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 848 | `model.layers.21.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.006907834836534642 / 1.8018382100867925 | [NPY](tensors/0000848.npy) |
| 849 | `model.layers.21.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -20.25 / 38.75 / 0.02346182012350923 / 1.1834446289483773 | [NPY](tensors/0000849.npy) |
| 850 | `model.layers.21.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.006907834836534642 / 1.8018382100867925 | [NPY](tensors/0000850.npy) |
| 851 | `model.layers.21.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -101.0 / 99.5 / -0.1886695326697538 / 8.106356516366539 | [NPY](tensors/0000851.npy) |
| 852 | `model.layers.21.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.006907834836534642 / 1.8018382100867925 | [NPY](tensors/0000852.npy) |
| 853 | `model.layers.21.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -21.375 / 23.75 / -0.0021938577730538722 / 3.15551884652908 | [NPY](tensors/0000853.npy) |
| 854 | `model.layers.21.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -17.0 / 13.5625 / 0.004135989978896783 / 0.7728854432129734 | [NPY](tensors/0000854.npy) |
| 855 | `model.layers.21.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -5152.0 / 4672.0 / -0.6675179074075906 / 79.23188517127635 | [NPY](tensors/0000855.npy) |
| 856 | `model.layers.21.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -5152.0 / 4672.0 / -0.6675179074075906 / 79.23188517127635 | [NPY](tensors/0000856.npy) |
| 857 | `model.layers.21.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 0.98046875 / 0.0010416093675492597 / 0.006723210739551992 | [NPY](tensors/0000857.npy) |
| 858 | `model.layers.21.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -5920.0 / 6080.0 / -0.2312852870764108 / 201.51101796184352 | [NPY](tensors/0000858.npy) |
| 859 | `model.layers.21.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -8.6875 / 27.125 / 0.0018024049278573984 / 1.0990484808607903 | [NPY](tensors/0000859.npy) |
| 860 | `model.layers.21.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -8.6875 / 27.125 / 0.0018024049278573984 / 1.0990484808607903 | [NPY](tensors/0000860.npy) |
| 861 | `model.layers.21.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -8.6875 / 27.125 / 0.0018024049278573984 / 1.0990484808607903 | [NPY](tensors/0000861.npy) |
| 862 | `model.layers.21.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 863 | `model.layers.21.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 864 | `model.layers.21.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 865 | `model.layers.21.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -6144.0 / 5696.0 / -0.982480970414882 / 152.79009503468694 | [NPY](tensors/0000865.npy) |
| 866 | `model.layers.21.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -6144.0 / 5696.0 / -0.982480970414882 / 152.79009503468694 | [NPY](tensors/0000866.npy) |
| 867 | `model.layers.21.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -6.625 / 4.5 / -0.23490441237823873 / 1.6179691557052527 | [NPY](tensors/0000867.npy) |
| 868 | `model.layers.21` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -9216.0 / 9600.0 / -1.2138581352394846 / 307.96444914115733 | [NPY](tensors/0000868.npy) |

## Layer 0022

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 869 | `model.layers.22` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -9216.0 / 9600.0 / -1.2138581352394846 / 307.96444914115733 | [NPY](tensors/0000869.npy) |
| 870 | `model.layers.22` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000870.npy) |
| 871 | `model.layers.22` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000871.npy) |
| 872 | `model.layers.22` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000872.npy) |
| 873 | `model.layers.22` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000873.npy) |
| 874 | `model.layers.22` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 875 | `model.layers.22` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 876 | `model.layers.22` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 877 | `model.layers.22.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -9216.0 / 9600.0 / -1.2138581352394846 / 307.96444914115733 | [NPY](tensors/0000877.npy) |
| 878 | `model.layers.22.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -44.25 / 49.0 / 0.0006310985592598656 / 1.7329980371193514 | [NPY](tensors/0000878.npy) |
| 879 | `model.layers.22.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -44.25 / 49.0 / 0.0006310985592598656 / 1.7329980371193514 | [NPY](tensors/0000879.npy) |
| 880 | `model.layers.22.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.4677265765053658e+38 / 1.5082314924322046e+38 | [NPY](tensors/0000880.npy) |
| 881 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000881.npy) |
| 882 | `model.layers.22.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 883 | `model.layers.22.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 884 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000884.npy) |
| 885 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000885.npy) |
| 886 | `model.layers.22.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 887 | `model.layers.22.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -44.25 / 49.0 / 0.0006310985592598656 / 1.7329980371193514 | [NPY](tensors/0000887.npy) |
| 888 | `model.layers.22.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -40.25 / 33.75 / -0.05206882282597424 / 2.483917032484536 | [NPY](tensors/0000888.npy) |
| 889 | `model.layers.22.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -44.25 / 49.0 / 0.0006310985592598656 / 1.7329980371193514 | [NPY](tensors/0000889.npy) |
| 890 | `model.layers.22.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -32.25 / 9.0 / -0.05265918667192418 / 1.359846836307511 | [NPY](tensors/0000890.npy) |
| 891 | `model.layers.22.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -44.25 / 49.0 / 0.0006310985592598656 / 1.7329980371193514 | [NPY](tensors/0000891.npy) |
| 892 | `model.layers.22.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -27.875 / 26.5 / 0.015044863896939573 / 4.414111162328451 | [NPY](tensors/0000892.npy) |
| 893 | `model.layers.22.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -19.875 / 16.375 / -0.007213527109934725 / 1.485300145500992 | [NPY](tensors/0000893.npy) |
| 894 | `model.layers.22.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -2112.0 / 1840.0 / -0.4191996581878634 / 40.890478062709626 | [NPY](tensors/0000894.npy) |
| 895 | `model.layers.22.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -2112.0 / 1840.0 / -0.4191996581878634 / 40.890478062709626 | [NPY](tensors/0000895.npy) |
| 896 | `model.layers.22.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 0.93359375 / 0.0009941895952927876 / 0.012411819712041935 | [NPY](tensors/0000896.npy) |
| 897 | `model.layers.22.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -9920.0 / 10304.0 / -1.6317961973681228 / 316.20217418902735 | [NPY](tensors/0000897.npy) |
| 898 | `model.layers.22.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -20.375 / 21.875 / -0.007089702878383141 / 1.0015040657665724 | [NPY](tensors/0000898.npy) |
| 899 | `model.layers.22.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -20.375 / 21.875 / -0.007089702878383141 / 1.0015040657665724 | [NPY](tensors/0000899.npy) |
| 900 | `model.layers.22.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -20.375 / 21.875 / -0.007089702878383141 / 1.0015040657665724 | [NPY](tensors/0000900.npy) |
| 901 | `model.layers.22.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 902 | `model.layers.22.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 903 | `model.layers.22.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 904 | `model.layers.22.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -6656.0 / 6368.0 / 0.08565073026718806 / 151.4230966488201 | [NPY](tensors/0000904.npy) |
| 905 | `model.layers.22.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -6656.0 / 6368.0 / 0.08565073026718806 / 151.4230966488201 | [NPY](tensors/0000905.npy) |
| 906 | `model.layers.22.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -7.84375 / 4.84375 / -0.19327376160440565 / 1.5050692129807965 | [NPY](tensors/0000906.npy) |
| 907 | `model.layers.22` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.545753577295403 / 404.3806294727644 | [NPY](tensors/0000907.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 908 | `model.layers.23` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.545753577295403 / 404.3806294727644 | [NPY](tensors/0000908.npy) |
| 909 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000909.npy) |
| 910 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000910.npy) |
| 911 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000911.npy) |
| 912 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000912.npy) |
| 913 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 914 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 915 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 916 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.545753577295403 / 404.3806294727644 | [NPY](tensors/0000916.npy) |
| 917 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009308927643588321 / 1.753129264202018 | [NPY](tensors/0000917.npy) |
| 918 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009308927643588321 / 1.753129264202018 | [NPY](tensors/0000918.npy) |
| 919 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 395, 395] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.690475148563424e+38 / 1.6947602635461005e+38 | [NPY](tensors/0000919.npy) |
| 920 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 395] | torch.int64 → int64 | 0.0 / 394.0 / 197.0 / 114.02631275280281 | [NPY](tensors/0000920.npy) |
| 921 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 922 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 923 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7807881976984724 / 0.8878127519086231 | [NPY](tensors/0000923.npy) |
| 924 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 395, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10842773332540535 / 0.6324022670486465 | [NPY](tensors/0000924.npy) |
| 925 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 926 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009308927643588321 / 1.753129264202018 | [NPY](tensors/0000926.npy) |
| 927 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 395, 4096] | torch.bfloat16 → float32 | -19.375 / 24.25 / 0.03135063183347287 / 1.6601312742499292 | [NPY](tensors/0000927.npy) |
| 928 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009308927643588321 / 1.753129264202018 | [NPY](tensors/0000928.npy) |
| 929 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -86.0 / 68.0 / -0.0651675080460175 / 5.080973450559657 | [NPY](tensors/0000929.npy) |
| 930 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009308927643588321 / 1.753129264202018 | [NPY](tensors/0000930.npy) |
| 931 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 395, 512] | torch.bfloat16 → float32 | -29.5 / 24.125 / 0.016662668289404502 / 3.1997368854507284 | [NPY](tensors/0000931.npy) |
| 932 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 395, 4096] | torch.bfloat16 → float32 | -26.875 / 12.9375 / -0.00020483954713775352 / 1.163268657591452 | [NPY](tensors/0000932.npy) |
| 933 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -6528.0 / 6848.0 / 2.4030536954563875 / 164.23759957494255 | [NPY](tensors/0000933.npy) |
| 934 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -6528.0 / 6848.0 / 2.4030536954563875 / 164.23759957494255 | [NPY](tensors/0000934.npy) |
| 935 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 395, 395] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.001295724518179001 / 0.010849903095015502 | [NPY](tensors/0000935.npy) |
| 936 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -11264.0 / 11264.0 / 0.857043704691483 / 362.93568929139826 | [NPY](tensors/0000936.npy) |
| 937 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.0 / 25.125 / -0.01595853261492423 / 1.2678399353854628 | [NPY](tensors/0000937.npy) |
| 938 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -52.0 / 25.125 / -0.01595853261492423 / 1.2678399353854628 | [NPY](tensors/0000938.npy) |
| 939 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [395, 2880] | torch.bfloat16 → float32 | -52.0 / 25.125 / -0.01595853261492423 / 1.2678399353854628 | [NPY](tensors/0000939.npy) |
| 940 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 941 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 942 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 943 | `model.layers.23.mlp.experts` | 0 | `output` | [395, 2880] | torch.bfloat16 → float32 | -6144.0 / 5568.0 / -1.709581885143339 / 147.9636142472134 | [NPY](tensors/0000943.npy) |
| 944 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 395, 2880] | torch.bfloat16 → float32 | -6144.0 / 5568.0 / -1.709581885143339 / 147.9636142472134 | [NPY](tensors/0000944.npy) |
| 945 | `model.layers.23.mlp` | 0 | `output[1]` | [395, 32] | torch.bfloat16 → float32 | -8.625 / 4.78125 / 0.2541901503937154 / 2.6644883771196293 | [NPY](tensors/0000945.npy) |
| 946 | `model.layers.23` | 0 | `output` | [1, 395, 2880] | torch.bfloat16 → float32 | -10880.0 / 10944.0 / -0.8523356772206839 / 390.0506987858363 | [NPY](tensors/0000946.npy) |

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
