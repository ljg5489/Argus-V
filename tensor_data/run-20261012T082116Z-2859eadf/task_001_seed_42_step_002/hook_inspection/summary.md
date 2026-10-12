# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 731 full tensors; 950 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Outside Transformer blocks

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model` | 0 | `input.kwargs['input_ids']` | [1, 215] | torch.int64 → int64 | 11.0 / 191268.0 / 16477.972093023254 / 32464.79928310422 | [NPY](tensors/0000000.npy) |
| 1 | `model` | 0 | `input.kwargs['attention_mask']` | [1, 215] | torch.int64 → int64 | 1.0 / 1.0 / 1.0 / 0.0 | [NPY](tensors/0000001.npy) |
| 2 | `model` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 3 | `model` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 4 | `model` | 0 | `input.kwargs['return_dict']` | — | bool | True | — |
| 5 | `model.embed_tokens` | 0 | `input.args[0]` | [1, 215] | torch.int64 → int64 | 11.0 / 191268.0 / 16477.972093023254 / 32464.79928310422 | [NPY](tensors/0000005.npy) |
| 6 | `model.embed_tokens` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.011612309428203842 / 2.8976011439963707 | [NPY](tensors/0000006.npy) |
| 7 | `model.rotary_emb` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.011612309428203842 / 2.8976011439963707 | [NPY](tensors/0000007.npy) |
| 8 | `model.rotary_emb` | 0 | `input.args[1]` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000008.npy) |
| 9 | `model.rotary_emb` | 0 | `output[0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000009.npy) |
| 10 | `model.rotary_emb` | 0 | `output[1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000010.npy) |
| 947 | `model.norm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -11328.0 / 10816.0 / -0.02829382292676034 / 425.5960353393399 | [NPY](tensors/0000947.npy) |
| 948 | `model.norm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -334.0 / 188.0 / -0.014269464250066791 / 6.050547059780885 | [NPY](tensors/0000948.npy) |
| 949 | `model` | 0 | `output['last_hidden_state']` | [1, 215, 2880] | torch.bfloat16 → float32 | -334.0 / 188.0 / -0.014269464250066791 / 6.050547059780885 | [NPY](tensors/0000949.npy) |

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | `model.layers.0` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.011612309428203842 / 2.8976011439963707 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000013.npy) |
| 14 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000014.npy) |
| 15 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 17 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 18 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 19 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.011612309428203842 / 2.8976011439963707 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006076278126983872 / 0.7556163966396938 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006076278126983872 / 0.7556163966396938 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 25 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 26 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 29 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006076278126983872 / 0.7556163966396938 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -8.25 / 12.8125 / 0.020193999117606817 / 1.0210535412722617 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006076278126983872 / 0.7556163966396938 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.013912592516389004 / 5.845839810982174 | [NPY](tensors/0000032.npy) |
| 33 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006076278126983872 / 0.7556163966396938 | [NPY](tensors/0000033.npy) |
| 34 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -7.375 / 7.71875 / -0.01747624517180199 / 1.1818009200455746 | [NPY](tensors/0000034.npy) |
| 35 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / -0.006839030312673675 / 0.5394749050485781 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -35.25 / 52.5 / 0.028112693631910848 / 1.1777480259230289 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -35.25 / 52.5 / 0.028112693631910848 / 1.1777480259230289 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0018956786414228287 / 0.028630450598864137 | [NPY](tensors/0000038.npy) |
| 39 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -87.5 / 71.0 / 0.016500549133895905 / 3.029741138601716 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0003366266747392733 / 0.3239246370436593 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0003366266747392733 / 0.3239246370436593 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.0003366266747392733 / 0.3239246370436593 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 44 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 45 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 46 | `model.layers.0.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -49.75 / 92.5 / 0.01753645134834664 / 0.8934769643055481 | [NPY](tensors/0000046.npy) |
| 47 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -49.75 / 92.5 / 0.01753645134834664 / 0.8934769643055481 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.0.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -5.03125 / 3.4375 / -0.102265282564385 / 1.041899248805532 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.0` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -89.0 / 106.0 / 0.03401941848971739 / 3.2383872949831694 | [NPY](tensors/0000049.npy) |

## Layer 0001

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | `model.layers.1` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -89.0 / 106.0 / 0.03401941848971739 / 3.2383872949831694 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.1` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.1` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000052.npy) |
| 53 | `model.layers.1` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000053.npy) |
| 54 | `model.layers.1` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.1` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 56 | `model.layers.1` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 57 | `model.layers.1` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 58 | `model.layers.1.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -89.0 / 106.0 / 0.03401941848971739 / 3.2383872949831694 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.1.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -28.125 / 25.75 / 0.0072750151523169925 / 0.8502526781504425 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.1.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -28.125 / 25.75 / 0.0072750151523169925 / 0.8502526781504425 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.1.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.1.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 64 | `model.layers.1.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 65 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.1.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 68 | `model.layers.1.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -28.125 / 25.75 / 0.0072750151523169925 / 0.8502526781504425 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.1.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -11.25 / 12.25 / -0.020808444688918824 / 1.1033010179871245 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.1.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -28.125 / 25.75 / 0.0072750151523169925 / 0.8502526781504425 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.1.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -109.5 / 39.75 / -0.7166177873001542 / 7.815775180258751 | [NPY](tensors/0000071.npy) |
| 72 | `model.layers.1.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -28.125 / 25.75 / 0.0072750151523169925 / 0.8502526781504425 | [NPY](tensors/0000072.npy) |
| 73 | `model.layers.1.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -6.03125 / 5.84375 / 0.01251652864522712 / 0.9747584634352896 | [NPY](tensors/0000073.npy) |
| 74 | `model.layers.1.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -5.84375 / 4.875 / 0.0007838171510197861 / 0.44187613530319503 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.1.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -33.75 / 50.0 / 0.002890179423315725 / 0.8362070034094962 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.1.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -33.75 / 50.0 / 0.002890179423315725 / 0.8362070034094962 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.1.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0031429728256318033 / 0.025849262552796962 | [NPY](tensors/0000077.npy) |
| 78 | `model.layers.1.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -89.0 / 79.5 / 0.03691069979692307 / 3.2081517794353944 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.1.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.40625 / 5.2134370002943756e-05 / 0.3546148856330154 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.1.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.40625 / 5.2134370002943756e-05 / 0.3546148856330154 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.1.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.40625 / 5.2134370002943756e-05 / 0.3546148856330154 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.1.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 83 | `model.layers.1.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 84 | `model.layers.1.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 85 | `model.layers.1.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -49.5 / 66.0 / 0.022571531995476367 / 1.064892790358218 | [NPY](tensors/0000085.npy) |
| 86 | `model.layers.1.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -49.5 / 66.0 / 0.022571531995476367 / 1.064892790358218 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.1.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -2.640625 / 2.609375 / -0.07905650915101517 / 0.7370413945151812 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.1` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -107.0 / 118.0 / 0.05948844782757821 / 3.729852980295783 | [NPY](tensors/0000088.npy) |

## Layer 0002

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 89 | `model.layers.2` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -107.0 / 118.0 / 0.05948844782757821 / 3.729852980295783 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.2` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.2` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000091.npy) |
| 92 | `model.layers.2` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000092.npy) |
| 93 | `model.layers.2` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.2` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 95 | `model.layers.2` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 96 | `model.layers.2` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 97 | `model.layers.2.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -107.0 / 118.0 / 0.05948844782757821 / 3.729852980295783 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.2.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -29.125 / 23.5 / 0.012796516013776916 / 0.8592008607485317 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.2.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -29.125 / 23.5 / 0.012796516013776916 / 0.8592008607485317 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.2.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.2.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 103 | `model.layers.2.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 104 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.2.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 107 | `model.layers.2.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -29.125 / 23.5 / 0.012796516013776916 / 0.8592008607485317 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.2.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -13.75 / 8.375 / 0.03882503964621634 / 0.8802184467794282 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.2.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -29.125 / 23.5 / 0.012796516013776916 / 0.8592008607485317 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.2.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -26.75 / 22.5 / -0.020804571031137954 / 2.5731545116688785 | [NPY](tensors/0000110.npy) |
| 111 | `model.layers.2.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -29.125 / 23.5 / 0.012796516013776916 / 0.8592008607485317 | [NPY](tensors/0000111.npy) |
| 112 | `model.layers.2.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -8.0 / 5.875 / 0.01891975291939669 / 1.1510040892675535 | [NPY](tensors/0000112.npy) |
| 113 | `model.layers.2.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -6.53125 / 5.28125 / 0.012155866144269376 / 0.4674794411680828 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.2.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41.5 / 51.0 / 0.001422299211471792 / 0.9698186177530009 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.2.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41.5 / 51.0 / 0.001422299211471792 / 0.9698186177530009 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.2.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002243296949434028 / 0.021501205228331252 | [NPY](tensors/0000116.npy) |
| 117 | `model.layers.2.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -83.0 / 123.0 / 0.06090638279606822 / 3.6826910789902825 | [NPY](tensors/0000117.npy) |
| 118 | `model.layers.2.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.28125 / 0.0022199201431770347 / 0.4516424465146531 | [NPY](tensors/0000118.npy) |
| 119 | `model.layers.2.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.28125 / 0.0022199201431770347 / 0.4516424465146531 | [NPY](tensors/0000119.npy) |
| 120 | `model.layers.2.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.28125 / 0.0022199201431770347 / 0.4516424465146531 | [NPY](tensors/0000120.npy) |
| 121 | `model.layers.2.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 122 | `model.layers.2.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 123 | `model.layers.2.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 124 | `model.layers.2.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -66.5 / 88.5 / 0.031228785495579395 / 1.3635098853371141 | [NPY](tensors/0000124.npy) |
| 125 | `model.layers.2.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -66.5 / 88.5 / 0.031228785495579395 / 1.3635098853371141 | [NPY](tensors/0000125.npy) |
| 126 | `model.layers.2.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -3.21875 / 2.21875 / -0.09632727157237918 / 0.6705139098824993 | [NPY](tensors/0000126.npy) |
| 127 | `model.layers.2` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -121.0 / 148.0 / 0.09213356197958461 / 4.442863620145314 | [NPY](tensors/0000127.npy) |

## Layer 0003

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | `model.layers.3` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -121.0 / 148.0 / 0.09213356197958461 / 4.442863620145314 | [NPY](tensors/0000128.npy) |
| 129 | `model.layers.3` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000129.npy) |
| 130 | `model.layers.3` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000130.npy) |
| 131 | `model.layers.3` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000131.npy) |
| 132 | `model.layers.3` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000132.npy) |
| 133 | `model.layers.3` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 134 | `model.layers.3` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 135 | `model.layers.3` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 136 | `model.layers.3.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -121.0 / 148.0 / 0.09213356197958461 / 4.442863620145314 | [NPY](tensors/0000136.npy) |
| 137 | `model.layers.3.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -60.0 / 56.5 / 0.03477945678571397 / 1.2832438752937327 | [NPY](tensors/0000137.npy) |
| 138 | `model.layers.3.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -60.0 / 56.5 / 0.03477945678571397 / 1.2832438752937327 | [NPY](tensors/0000138.npy) |
| 139 | `model.layers.3.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000139.npy) |
| 140 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000140.npy) |
| 141 | `model.layers.3.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 142 | `model.layers.3.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 143 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000143.npy) |
| 144 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000144.npy) |
| 145 | `model.layers.3.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 146 | `model.layers.3.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -60.0 / 56.5 / 0.03477945678571397 / 1.2832438752937327 | [NPY](tensors/0000146.npy) |
| 147 | `model.layers.3.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -12.5625 / 9.0 / -0.024902222651922615 / 1.1047972186518176 | [NPY](tensors/0000147.npy) |
| 148 | `model.layers.3.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -60.0 / 56.5 / 0.03477945678571397 / 1.2832438752937327 | [NPY](tensors/0000148.npy) |
| 149 | `model.layers.3.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -78.5 / 56.5 / -0.07918062192756076 / 4.837620814639027 | [NPY](tensors/0000149.npy) |
| 150 | `model.layers.3.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -60.0 / 56.5 / 0.03477945678571397 / 1.2832438752937327 | [NPY](tensors/0000150.npy) |
| 151 | `model.layers.3.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -7.4375 / 11.4375 / 0.016895596925602403 / 0.9496757426812235 | [NPY](tensors/0000151.npy) |
| 152 | `model.layers.3.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -3.65625 / 3.234375 / 0.008668288649377257 / 0.3116394935371107 | [NPY](tensors/0000152.npy) |
| 153 | `model.layers.3.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -63.5 / 41.25 / -0.008249027409737578 / 1.0339507477812113 | [NPY](tensors/0000153.npy) |
| 154 | `model.layers.3.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -63.5 / 41.25 / -0.008249027409737578 / 1.0339507477812113 | [NPY](tensors/0000154.npy) |
| 155 | `model.layers.3.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.9765625 / 0.0023213013904692776 / 0.014931744998767454 | [NPY](tensors/0000155.npy) |
| 156 | `model.layers.3.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -103.5 / 140.0 / 0.08389604642101653 / 4.356249525271341 | [NPY](tensors/0000156.npy) |
| 157 | `model.layers.3.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -6.0 / 5.6875 / 0.004946483754064378 / 0.5137427636765936 | [NPY](tensors/0000157.npy) |
| 158 | `model.layers.3.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -6.0 / 5.6875 / 0.004946483754064378 / 0.5137427636765936 | [NPY](tensors/0000158.npy) |
| 159 | `model.layers.3.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -6.0 / 5.6875 / 0.004946483754064378 / 0.5137427636765936 | [NPY](tensors/0000159.npy) |
| 160 | `model.layers.3.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 161 | `model.layers.3.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 162 | `model.layers.3.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 163 | `model.layers.3.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -61.5 / 93.0 / 0.026576954363544476 / 1.513183274794477 | [NPY](tensors/0000163.npy) |
| 164 | `model.layers.3.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -61.5 / 93.0 / 0.026576954363544476 / 1.513183274794477 | [NPY](tensors/0000164.npy) |
| 165 | `model.layers.3.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -3.453125 / 2.015625 / -0.07985771755839503 / 0.5508694622579415 | [NPY](tensors/0000165.npy) |
| 166 | `model.layers.3` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -149.0 / 171.0 / 0.11048447091450062 / 5.241915598104237 | [NPY](tensors/0000166.npy) |

## Layer 0004

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 167 | `model.layers.4` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -149.0 / 171.0 / 0.11048447091450062 / 5.241915598104237 | [NPY](tensors/0000167.npy) |
| 168 | `model.layers.4` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000168.npy) |
| 169 | `model.layers.4` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000169.npy) |
| 170 | `model.layers.4` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000170.npy) |
| 171 | `model.layers.4` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000171.npy) |
| 172 | `model.layers.4` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 173 | `model.layers.4` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 174 | `model.layers.4` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 175 | `model.layers.4.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -149.0 / 171.0 / 0.11048447091450062 / 5.241915598104237 | [NPY](tensors/0000175.npy) |
| 176 | `model.layers.4.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.020746969961842825 / 1.1423037979291069 | [NPY](tensors/0000176.npy) |
| 177 | `model.layers.4.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.020746969961842825 / 1.1423037979291069 | [NPY](tensors/0000177.npy) |
| 178 | `model.layers.4.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000178.npy) |
| 179 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000179.npy) |
| 180 | `model.layers.4.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 181 | `model.layers.4.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 182 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000182.npy) |
| 183 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000183.npy) |
| 184 | `model.layers.4.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 185 | `model.layers.4.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.020746969961842825 / 1.1423037979291069 | [NPY](tensors/0000185.npy) |
| 186 | `model.layers.4.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -17.0 / 8.125 / -0.011475950920836578 / 1.0329459699481052 | [NPY](tensors/0000186.npy) |
| 187 | `model.layers.4.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.020746969961842825 / 1.1423037979291069 | [NPY](tensors/0000187.npy) |
| 188 | `model.layers.4.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -14.3125 / 99.5 / 0.23373625631942305 / 4.325497213761819 | [NPY](tensors/0000188.npy) |
| 189 | `model.layers.4.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.020746969961842825 / 1.1423037979291069 | [NPY](tensors/0000189.npy) |
| 190 | `model.layers.4.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -10.875 / 16.0 / 0.0012678947559622835 / 1.3373184307639394 | [NPY](tensors/0000190.npy) |
| 191 | `model.layers.4.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -9.625 / 15.0 / -0.005657796024766063 / 0.5880714553302738 | [NPY](tensors/0000191.npy) |
| 192 | `model.layers.4.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -69.0 / 45.75 / -0.004669994289026588 / 1.2631939155565706 | [NPY](tensors/0000192.npy) |
| 193 | `model.layers.4.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -69.0 / 45.75 / -0.004669994289026588 / 1.2631939155565706 | [NPY](tensors/0000193.npy) |
| 194 | `model.layers.4.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0023481003545958016 / 0.021071153189283508 | [NPY](tensors/0000194.npy) |
| 195 | `model.layers.4.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -134.0 / 149.0 / 0.1058205052802113 / 5.1808858929657715 | [NPY](tensors/0000195.npy) |
| 196 | `model.layers.4.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.875 / 0.00762265652610658 / 0.5757525788177537 | [NPY](tensors/0000196.npy) |
| 197 | `model.layers.4.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.875 / 0.00762265652610658 / 0.5757525788177537 | [NPY](tensors/0000197.npy) |
| 198 | `model.layers.4.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.875 / 0.00762265652610658 / 0.5757525788177537 | [NPY](tensors/0000198.npy) |
| 199 | `model.layers.4.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 200 | `model.layers.4.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 201 | `model.layers.4.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 202 | `model.layers.4.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -82.5 / 165.0 / 0.05156177328923568 / 2.441113257814794 | [NPY](tensors/0000202.npy) |
| 203 | `model.layers.4.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -82.5 / 165.0 / 0.05156177328923568 / 2.441113257814794 | [NPY](tensors/0000203.npy) |
| 204 | `model.layers.4.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -3.125 / 2.171875 / -0.08776980555334757 / 0.6079346118944894 | [NPY](tensors/0000204.npy) |
| 205 | `model.layers.4` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -191.0 / 254.0 / 0.15738056173004233 / 6.728420211884033 | [NPY](tensors/0000205.npy) |

## Layer 0005

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 206 | `model.layers.5` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -191.0 / 254.0 / 0.15738056173004233 / 6.728420211884033 | [NPY](tensors/0000206.npy) |
| 207 | `model.layers.5` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000207.npy) |
| 208 | `model.layers.5` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000208.npy) |
| 209 | `model.layers.5` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000209.npy) |
| 210 | `model.layers.5` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000210.npy) |
| 211 | `model.layers.5` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 212 | `model.layers.5` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 213 | `model.layers.5` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 214 | `model.layers.5.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -191.0 / 254.0 / 0.15738056173004233 / 6.728420211884033 | [NPY](tensors/0000214.npy) |
| 215 | `model.layers.5.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -30.0 / 41.0 / 0.0338697977290905 / 1.1873658444291104 | [NPY](tensors/0000215.npy) |
| 216 | `model.layers.5.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -30.0 / 41.0 / 0.0338697977290905 / 1.1873658444291104 | [NPY](tensors/0000216.npy) |
| 217 | `model.layers.5.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000217.npy) |
| 218 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000218.npy) |
| 219 | `model.layers.5.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 220 | `model.layers.5.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 221 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000221.npy) |
| 222 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000222.npy) |
| 223 | `model.layers.5.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 224 | `model.layers.5.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -30.0 / 41.0 / 0.0338697977290905 / 1.1873658444291104 | [NPY](tensors/0000224.npy) |
| 225 | `model.layers.5.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -18.625 / 14.9375 / -0.057304844480998776 / 1.402405499100573 | [NPY](tensors/0000225.npy) |
| 226 | `model.layers.5.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -30.0 / 41.0 / 0.0338697977290905 / 1.1873658444291104 | [NPY](tensors/0000226.npy) |
| 227 | `model.layers.5.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -35.25 / 39.75 / -0.043741968066193335 / 3.4272795412567523 | [NPY](tensors/0000227.npy) |
| 228 | `model.layers.5.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -30.0 / 41.0 / 0.0338697977290905 / 1.1873658444291104 | [NPY](tensors/0000228.npy) |
| 229 | `model.layers.5.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -7.3125 / 8.375 / 0.006291747682316358 / 1.1900019577298853 | [NPY](tensors/0000229.npy) |
| 230 | `model.layers.5.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -4.375 / 4.71875 / 0.009625875734197271 / 0.5112347383672705 | [NPY](tensors/0000230.npy) |
| 231 | `model.layers.5.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -70.0 / 72.5 / -0.007602235210351934 / 1.4483999237542846 | [NPY](tensors/0000231.npy) |
| 232 | `model.layers.5.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -70.0 / 72.5 / -0.007602235210351934 / 1.4483999237542846 | [NPY](tensors/0000232.npy) |
| 233 | `model.layers.5.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002528852575230978 / 0.017019937769353333 | [NPY](tensors/0000233.npy) |
| 234 | `model.layers.5.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -140.0 / 208.0 / 0.14977160710080956 / 6.917297887665926 | [NPY](tensors/0000234.npy) |
| 235 | `model.layers.5.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -5.59375 / 5.6875 / 0.00813741530866894 / 0.5658988923088515 | [NPY](tensors/0000235.npy) |
| 236 | `model.layers.5.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -5.59375 / 5.6875 / 0.00813741530866894 / 0.5658988923088515 | [NPY](tensors/0000236.npy) |
| 237 | `model.layers.5.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -5.59375 / 5.6875 / 0.00813741530866894 / 0.5658988923088515 | [NPY](tensors/0000237.npy) |
| 238 | `model.layers.5.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 239 | `model.layers.5.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 240 | `model.layers.5.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 241 | `model.layers.5.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -124.0 / 116.5 / 0.04287144321495864 / 2.6332293571429894 | [NPY](tensors/0000241.npy) |
| 242 | `model.layers.5.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -124.0 / 116.5 / 0.04287144321495864 / 2.6332293571429894 | [NPY](tensors/0000242.npy) |
| 243 | `model.layers.5.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -3.5625 / 2.265625 / -0.09542632879212845 / 0.5995492071126381 | [NPY](tensors/0000243.npy) |
| 244 | `model.layers.5` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -195.0 / 296.0 / 0.19264481970814157 / 8.542782688430192 | [NPY](tensors/0000244.npy) |

## Layer 0006

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 245 | `model.layers.6` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -195.0 / 296.0 / 0.19264481970814157 / 8.542782688430192 | [NPY](tensors/0000245.npy) |
| 246 | `model.layers.6` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000246.npy) |
| 247 | `model.layers.6` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000247.npy) |
| 248 | `model.layers.6` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000248.npy) |
| 249 | `model.layers.6` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000249.npy) |
| 250 | `model.layers.6` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 251 | `model.layers.6` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 252 | `model.layers.6` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 253 | `model.layers.6.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -195.0 / 296.0 / 0.19264481970814157 / 8.542782688430192 | [NPY](tensors/0000253.npy) |
| 254 | `model.layers.6.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -34.5 / 43.0 / 0.03032510503356463 / 1.3133150751883318 | [NPY](tensors/0000254.npy) |
| 255 | `model.layers.6.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -34.5 / 43.0 / 0.03032510503356463 / 1.3133150751883318 | [NPY](tensors/0000255.npy) |
| 256 | `model.layers.6.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000256.npy) |
| 257 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000257.npy) |
| 258 | `model.layers.6.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 259 | `model.layers.6.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 260 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000260.npy) |
| 261 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000261.npy) |
| 262 | `model.layers.6.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 263 | `model.layers.6.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -34.5 / 43.0 / 0.03032510503356463 / 1.3133150751883318 | [NPY](tensors/0000263.npy) |
| 264 | `model.layers.6.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -29.0 / 16.625 / -0.025796958016482765 / 1.16252380794816 | [NPY](tensors/0000264.npy) |
| 265 | `model.layers.6.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -34.5 / 43.0 / 0.03032510503356463 / 1.3133150751883318 | [NPY](tensors/0000265.npy) |
| 266 | `model.layers.6.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -19.625 / 32.25 / 0.2074970408581024 / 2.359497331105415 | [NPY](tensors/0000266.npy) |
| 267 | `model.layers.6.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -34.5 / 43.0 / 0.03032510503356463 / 1.3133150751883318 | [NPY](tensors/0000267.npy) |
| 268 | `model.layers.6.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -8.0625 / 8.75 / -0.056523764410684275 / 1.630201198744171 | [NPY](tensors/0000268.npy) |
| 269 | `model.layers.6.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -7.03125 / 7.75 / -0.0357112780381549 / 0.8200611110061371 | [NPY](tensors/0000269.npy) |
| 270 | `model.layers.6.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -91.5 / 81.5 / -0.001513165895819895 / 1.9167707858278342 | [NPY](tensors/0000270.npy) |
| 271 | `model.layers.6.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -91.5 / 81.5 / -0.001513165895819895 / 1.9167707858278342 | [NPY](tensors/0000271.npy) |
| 272 | `model.layers.6.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002572725139398335 / 0.02405799069218703 | [NPY](tensors/0000272.npy) |
| 273 | `model.layers.6.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -180.0 / 246.0 / 0.19114406021990515 / 8.450264918109776 | [NPY](tensors/0000273.npy) |
| 274 | `model.layers.6.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -22.125 / 4.84375 / 0.011720217447679789 / 0.6075136453059307 | [NPY](tensors/0000274.npy) |
| 275 | `model.layers.6.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -22.125 / 4.84375 / 0.011720217447679789 / 0.6075136453059307 | [NPY](tensors/0000275.npy) |
| 276 | `model.layers.6.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -22.125 / 4.84375 / 0.011720217447679789 / 0.6075136453059307 | [NPY](tensors/0000276.npy) |
| 277 | `model.layers.6.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 278 | `model.layers.6.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 279 | `model.layers.6.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 280 | `model.layers.6.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -41472.0 / 968.0 / -0.033742877127896295 / 52.88163797765461 | [NPY](tensors/0000280.npy) |
| 281 | `model.layers.6.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41472.0 / 968.0 / -0.033742877127896295 / 52.88163797765461 | [NPY](tensors/0000281.npy) |
| 282 | `model.layers.6.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -3.59375 / 5.0 / -0.1092574629672738 / 0.7469257441675108 | [NPY](tensors/0000282.npy) |
| 283 | `model.layers.6` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.15758826135048878 / 53.829832685125346 | [NPY](tensors/0000283.npy) |

## Layer 0007

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 284 | `model.layers.7` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.15758826135048878 / 53.829832685125346 | [NPY](tensors/0000284.npy) |
| 285 | `model.layers.7` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000285.npy) |
| 286 | `model.layers.7` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000286.npy) |
| 287 | `model.layers.7` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000287.npy) |
| 288 | `model.layers.7` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000288.npy) |
| 289 | `model.layers.7` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 290 | `model.layers.7` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 291 | `model.layers.7` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 292 | `model.layers.7.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.15758826135048878 / 53.829832685125346 | [NPY](tensors/0000292.npy) |
| 293 | `model.layers.7.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03575848327078483 / 1.640116935345454 | [NPY](tensors/0000293.npy) |
| 294 | `model.layers.7.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03575848327078483 / 1.640116935345454 | [NPY](tensors/0000294.npy) |
| 295 | `model.layers.7.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000295.npy) |
| 296 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000296.npy) |
| 297 | `model.layers.7.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 298 | `model.layers.7.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 299 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000299.npy) |
| 300 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000300.npy) |
| 301 | `model.layers.7.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 302 | `model.layers.7.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03575848327078483 / 1.640116935345454 | [NPY](tensors/0000302.npy) |
| 303 | `model.layers.7.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -13.4375 / 13.1875 / -0.11981606544340626 / 1.4145670901186347 | [NPY](tensors/0000303.npy) |
| 304 | `model.layers.7.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03575848327078483 / 1.640116935345454 | [NPY](tensors/0000304.npy) |
| 305 | `model.layers.7.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -129.0 / 34.0 / -0.0780987550872703 / 5.391212648525713 | [NPY](tensors/0000305.npy) |
| 306 | `model.layers.7.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03575848327078483 / 1.640116935345454 | [NPY](tensors/0000306.npy) |
| 307 | `model.layers.7.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -17.0 / 10.75 / 0.01584037479966186 / 1.6386480885663015 | [NPY](tensors/0000307.npy) |
| 308 | `model.layers.7.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -7.6875 / 8.0 / -0.0004715089900242292 / 0.88298817035813 | [NPY](tensors/0000308.npy) |
| 309 | `model.layers.7.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -121.5 / 123.5 / -0.007078792386031312 / 2.3241778451876027 | [NPY](tensors/0000309.npy) |
| 310 | `model.layers.7.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -121.5 / 123.5 / -0.007078792386031312 / 2.3241778451876027 | [NPY](tensors/0000310.npy) |
| 311 | `model.layers.7.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0035147506278387585 / 0.0273413690226545 | [NPY](tensors/0000311.npy) |
| 312 | `model.layers.7.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41472.0 / 1104.0 / 0.1505303638172396 / 53.80533120104316 | [NPY](tensors/0000312.npy) |
| 313 | `model.layers.7.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -77.0 / 5.34375 / 0.009780974139866134 / 0.6279326272022842 | [NPY](tensors/0000313.npy) |
| 314 | `model.layers.7.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -77.0 / 5.34375 / 0.009780974139866134 / 0.6279326272022842 | [NPY](tensors/0000314.npy) |
| 315 | `model.layers.7.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -77.0 / 5.34375 / 0.009780974139866134 / 0.6279326272022842 | [NPY](tensors/0000315.npy) |
| 316 | `model.layers.7.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 317 | `model.layers.7.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 318 | `model.layers.7.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 319 | `model.layers.7.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -159.0 / 171.0 / 0.03374649719366424 / 3.5565522993606735 | [NPY](tensors/0000319.npy) |
| 320 | `model.layers.7.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -159.0 / 171.0 / 0.03374649719366424 / 3.5565522993606735 | [NPY](tensors/0000320.npy) |
| 321 | `model.layers.7.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -3.890625 / 3.828125 / -0.12741355507872826 / 0.8090130161865697 | [NPY](tensors/0000321.npy) |
| 322 | `model.layers.7` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.18426939557689107 / 54.266472112288334 | [NPY](tensors/0000322.npy) |

## Layer 0008

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 323 | `model.layers.8` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.18426939557689107 / 54.266472112288334 | [NPY](tensors/0000323.npy) |
| 324 | `model.layers.8` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000324.npy) |
| 325 | `model.layers.8` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000325.npy) |
| 326 | `model.layers.8` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000326.npy) |
| 327 | `model.layers.8` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000327.npy) |
| 328 | `model.layers.8` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 329 | `model.layers.8` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 330 | `model.layers.8` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 331 | `model.layers.8.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.18426939557689107 / 54.266472112288334 | [NPY](tensors/0000331.npy) |
| 332 | `model.layers.8.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.026639728790692967 / 1.3304596456879212 | [NPY](tensors/0000332.npy) |
| 333 | `model.layers.8.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.026639728790692967 / 1.3304596456879212 | [NPY](tensors/0000333.npy) |
| 334 | `model.layers.8.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000334.npy) |
| 335 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000335.npy) |
| 336 | `model.layers.8.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 337 | `model.layers.8.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 338 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000338.npy) |
| 339 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000339.npy) |
| 340 | `model.layers.8.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 341 | `model.layers.8.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.026639728790692967 / 1.3304596456879212 | [NPY](tensors/0000341.npy) |
| 342 | `model.layers.8.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -14.875 / 15.25 / -0.009843671515197858 / 1.0559330724398368 | [NPY](tensors/0000342.npy) |
| 343 | `model.layers.8.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.026639728790692967 / 1.3304596456879212 | [NPY](tensors/0000343.npy) |
| 344 | `model.layers.8.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -22.5 / 28.75 / -0.0011026375168977781 / 2.2190848684906013 | [NPY](tensors/0000344.npy) |
| 345 | `model.layers.8.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.026639728790692967 / 1.3304596456879212 | [NPY](tensors/0000345.npy) |
| 346 | `model.layers.8.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -9.3125 / 9.6875 / 0.002477202997651211 / 1.7122964736593382 | [NPY](tensors/0000346.npy) |
| 347 | `model.layers.8.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -7.25 / 7.0 / 0.0041670379850476695 / 0.8566144901226976 | [NPY](tensors/0000347.npy) |
| 348 | `model.layers.8.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -198.0 / 213.0 / 0.0028831499158488995 / 3.006228562419654 | [NPY](tensors/0000348.npy) |
| 349 | `model.layers.8.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -198.0 / 213.0 / 0.0028831499158488995 / 3.006228562419654 | [NPY](tensors/0000349.npy) |
| 350 | `model.layers.8.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0028689754724571417 / 0.02288888972328851 | [NPY](tensors/0000350.npy) |
| 351 | `model.layers.8.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41472.0 / 1344.0 / 0.18719738187330945 / 54.22779920674644 | [NPY](tensors/0000351.npy) |
| 352 | `model.layers.8.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -57.0 / 5.9375 / 0.008217965758932654 / 0.660278788081989 | [NPY](tensors/0000352.npy) |
| 353 | `model.layers.8.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -57.0 / 5.9375 / 0.008217965758932654 / 0.660278788081989 | [NPY](tensors/0000353.npy) |
| 354 | `model.layers.8.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -57.0 / 5.9375 / 0.008217965758932654 / 0.660278788081989 | [NPY](tensors/0000354.npy) |
| 355 | `model.layers.8.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 356 | `model.layers.8.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 357 | `model.layers.8.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 358 | `model.layers.8.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -266.0 / 251.0 / 0.07030190000931422 / 5.114633483955529 | [NPY](tensors/0000358.npy) |
| 359 | `model.layers.8.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -266.0 / 251.0 / 0.07030190000931422 / 5.114633483955529 | [NPY](tensors/0000359.npy) |
| 360 | `model.layers.8.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -3.921875 / 3.53125 / -0.16177538938300554 / 0.7516657355659867 | [NPY](tensors/0000360.npy) |
| 361 | `model.layers.8` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.2573079854881425 / 55.33891978788534 | [NPY](tensors/0000361.npy) |

## Layer 0009

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 362 | `model.layers.9` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.2573079854881425 / 55.33891978788534 | [NPY](tensors/0000362.npy) |
| 363 | `model.layers.9` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000363.npy) |
| 364 | `model.layers.9` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000364.npy) |
| 365 | `model.layers.9` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000365.npy) |
| 366 | `model.layers.9` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000366.npy) |
| 367 | `model.layers.9` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 368 | `model.layers.9` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 369 | `model.layers.9` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 370 | `model.layers.9.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.2573079854881425 / 55.33891978788534 | [NPY](tensors/0000370.npy) |
| 371 | `model.layers.9.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -207.0 / 72.0 / 0.03838316742263407 / 1.8042565723961388 | [NPY](tensors/0000371.npy) |
| 372 | `model.layers.9.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -207.0 / 72.0 / 0.03838316742263407 / 1.8042565723961388 | [NPY](tensors/0000372.npy) |
| 373 | `model.layers.9.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000373.npy) |
| 374 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000374.npy) |
| 375 | `model.layers.9.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 376 | `model.layers.9.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 377 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000377.npy) |
| 378 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000378.npy) |
| 379 | `model.layers.9.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 380 | `model.layers.9.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -207.0 / 72.0 / 0.03838316742263407 / 1.8042565723961388 | [NPY](tensors/0000380.npy) |
| 381 | `model.layers.9.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -10.1875 / 20.125 / 0.06669330355654765 / 1.2550698162511413 | [NPY](tensors/0000381.npy) |
| 382 | `model.layers.9.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -207.0 / 72.0 / 0.03838316742263407 / 1.8042565723961388 | [NPY](tensors/0000382.npy) |
| 383 | `model.layers.9.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -52.0 / 41.25 / 0.06636894260381543 / 3.881596873956582 | [NPY](tensors/0000383.npy) |
| 384 | `model.layers.9.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -207.0 / 72.0 / 0.03838316742263407 / 1.8042565723961388 | [NPY](tensors/0000384.npy) |
| 385 | `model.layers.9.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -27.75 / 12.375 / -0.0066600967285244984 / 1.4886276073210947 | [NPY](tensors/0000385.npy) |
| 386 | `model.layers.9.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -11.0 / 8.8125 / -0.0005434052548293343 / 0.6451479734694634 | [NPY](tensors/0000386.npy) |
| 387 | `model.layers.9.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -344.0 / 342.0 / 0.01755852152239676 / 3.91042559458723 | [NPY](tensors/0000387.npy) |
| 388 | `model.layers.9.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -344.0 / 342.0 / 0.01755852152239676 / 3.91042559458723 | [NPY](tensors/0000388.npy) |
| 389 | `model.layers.9.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0035111436196235304 / 0.023935296370199796 | [NPY](tensors/0000389.npy) |
| 390 | `model.layers.9.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41728.0 / 1480.0 / 0.2748553763988406 / 55.188923578751535 | [NPY](tensors/0000390.npy) |
| 391 | `model.layers.9.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -64.5 / 6.78125 / 0.009528036961567801 / 0.6806001526759494 | [NPY](tensors/0000391.npy) |
| 392 | `model.layers.9.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -64.5 / 6.78125 / 0.009528036961567801 / 0.6806001526759494 | [NPY](tensors/0000392.npy) |
| 393 | `model.layers.9.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -64.5 / 6.78125 / 0.009528036961567801 / 0.6806001526759494 | [NPY](tensors/0000393.npy) |
| 394 | `model.layers.9.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 395 | `model.layers.9.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 396 | `model.layers.9.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 397 | `model.layers.9.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -564.0 / 632.0 / 0.044838862616270396 / 5.77896799457478 | [NPY](tensors/0000397.npy) |
| 398 | `model.layers.9.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -564.0 / 632.0 / 0.044838862616270396 / 5.77896799457478 | [NPY](tensors/0000398.npy) |
| 399 | `model.layers.9.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -5.1875 / 6.40625 / -0.12946152576180392 / 0.6376976660001908 | [NPY](tensors/0000399.npy) |
| 400 | `model.layers.9` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 916.0 / 0.3197384610040551 / 55.5334686216512 | [NPY](tensors/0000400.npy) |

## Layer 0010

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 401 | `model.layers.10` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 916.0 / 0.3197384610040551 / 55.5334686216512 | [NPY](tensors/0000401.npy) |
| 402 | `model.layers.10` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000402.npy) |
| 403 | `model.layers.10` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000403.npy) |
| 404 | `model.layers.10` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000404.npy) |
| 405 | `model.layers.10` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000405.npy) |
| 406 | `model.layers.10` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 407 | `model.layers.10` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 408 | `model.layers.10` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 409 | `model.layers.10.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 916.0 / 0.3197384610040551 / 55.5334686216512 | [NPY](tensors/0000409.npy) |
| 410 | `model.layers.10.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.031873925425189256 / 1.5364734483661366 | [NPY](tensors/0000410.npy) |
| 411 | `model.layers.10.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.031873925425189256 / 1.5364734483661366 | [NPY](tensors/0000411.npy) |
| 412 | `model.layers.10.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000412.npy) |
| 413 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000413.npy) |
| 414 | `model.layers.10.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 415 | `model.layers.10.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 416 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000416.npy) |
| 417 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000417.npy) |
| 418 | `model.layers.10.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 419 | `model.layers.10.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.031873925425189256 / 1.5364734483661366 | [NPY](tensors/0000419.npy) |
| 420 | `model.layers.10.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -15.4375 / 16.125 / 0.03423796665152877 / 1.091741901133803 | [NPY](tensors/0000420.npy) |
| 421 | `model.layers.10.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.031873925425189256 / 1.5364734483661366 | [NPY](tensors/0000421.npy) |
| 422 | `model.layers.10.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -56.75 / 16.875 / -0.06606427687545155 / 2.393018575045724 | [NPY](tensors/0000422.npy) |
| 423 | `model.layers.10.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.031873925425189256 / 1.5364734483661366 | [NPY](tensors/0000423.npy) |
| 424 | `model.layers.10.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -9.6875 / 10.625 / 0.06156839714493863 / 2.1177366284551633 | [NPY](tensors/0000424.npy) |
| 425 | `model.layers.10.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -7.40625 / 8.4375 / 0.04128881320049153 / 0.9934973307044174 | [NPY](tensors/0000425.npy) |
| 426 | `model.layers.10.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -202.0 / 212.0 / 0.04661298200892386 / 4.255775839193346 | [NPY](tensors/0000426.npy) |
| 427 | `model.layers.10.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -202.0 / 212.0 / 0.04661298200892386 / 4.255775839193346 | [NPY](tensors/0000427.npy) |
| 428 | `model.layers.10.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.0028187293623494485 / 0.01834410157091913 | [NPY](tensors/0000428.npy) |
| 429 | `model.layers.10.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 928.0 / 0.3663507312705659 / 55.33029375945114 | [NPY](tensors/0000429.npy) |
| 430 | `model.layers.10.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -46.75 / 6.71875 / 0.011861697817726653 / 0.7347122879693411 | [NPY](tensors/0000430.npy) |
| 431 | `model.layers.10.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -46.75 / 6.71875 / 0.011861697817726653 / 0.7347122879693411 | [NPY](tensors/0000431.npy) |
| 432 | `model.layers.10.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -46.75 / 6.71875 / 0.011861697817726653 / 0.7347122879693411 | [NPY](tensors/0000432.npy) |
| 433 | `model.layers.10.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 434 | `model.layers.10.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 435 | `model.layers.10.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 436 | `model.layers.10.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -720.0 / 896.0 / 0.13929064482065442 / 8.496474114093761 | [NPY](tensors/0000436.npy) |
| 437 | `model.layers.10.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -720.0 / 896.0 / 0.13929064482065442 / 8.496474114093761 | [NPY](tensors/0000437.npy) |
| 438 | `model.layers.10.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -5.3125 / 4.03125 / -0.12135579087013422 / 0.6646341157232696 | [NPY](tensors/0000438.npy) |
| 439 | `model.layers.10` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 828.0 / 0.5056980288798802 / 57.12671988775315 | [NPY](tensors/0000439.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 440 | `model.layers.11` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 828.0 / 0.5056980288798802 / 57.12671988775315 | [NPY](tensors/0000440.npy) |
| 441 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000441.npy) |
| 442 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000442.npy) |
| 443 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000443.npy) |
| 444 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000444.npy) |
| 445 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 446 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 447 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 448 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 828.0 / 0.5056980288798802 / 57.12671988775315 | [NPY](tensors/0000448.npy) |
| 449 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -191.0 / 140.0 / 0.06575747820373037 / 3.213466082144965 | [NPY](tensors/0000449.npy) |
| 450 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -191.0 / 140.0 / 0.06575747820373037 / 3.213466082144965 | [NPY](tensors/0000450.npy) |
| 451 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000451.npy) |
| 452 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000452.npy) |
| 453 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 454 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 455 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000455.npy) |
| 456 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000456.npy) |
| 457 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 458 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -191.0 / 140.0 / 0.06575747820373037 / 3.213466082144965 | [NPY](tensors/0000458.npy) |
| 459 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -11.3125 / 13.3125 / 0.03629303991539589 / 1.3191158991910763 | [NPY](tensors/0000459.npy) |
| 460 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -191.0 / 140.0 / 0.06575747820373037 / 3.213466082144965 | [NPY](tensors/0000460.npy) |
| 461 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -38.25 / 50.25 / 0.06047573470792105 / 3.673049058614848 | [NPY](tensors/0000461.npy) |
| 462 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -191.0 / 140.0 / 0.06575747820373037 / 3.213466082144965 | [NPY](tensors/0000462.npy) |
| 463 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.03578767222027446 / 2.4637912654670373 | [NPY](tensors/0000463.npy) |
| 464 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -11.5625 / 11.3125 / -0.02717090005969726 / 1.410717137553858 | [NPY](tensors/0000464.npy) |
| 465 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -466.0 / 502.0 / -0.04810778886195302 / 7.097454748069535 | [NPY](tensors/0000465.npy) |
| 466 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -466.0 / 502.0 / -0.04810778886195302 / 7.097454748069535 | [NPY](tensors/0000466.npy) |
| 467 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0038338018969362956 / 0.02181525116643111 | [NPY](tensors/0000467.npy) |
| 468 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 696.0 / 0.4575768300729205 / 56.220142255061056 | [NPY](tensors/0000468.npy) |
| 469 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -78.5 / 7.28125 / 0.010668720663729718 / 0.7923244510207788 | [NPY](tensors/0000469.npy) |
| 470 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -78.5 / 7.28125 / 0.010668720663729718 / 0.7923244510207788 | [NPY](tensors/0000470.npy) |
| 471 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -78.5 / 7.28125 / 0.010668720663729718 / 0.7923244510207788 | [NPY](tensors/0000471.npy) |
| 472 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 473 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 474 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 475 | `model.layers.11.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -548.0 / 460.0 / 0.13274734314097913 / 9.786254596871176 | [NPY](tensors/0000475.npy) |
| 476 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -548.0 / 460.0 / 0.13274734314097913 / 9.786254596871176 | [NPY](tensors/0000476.npy) |
| 477 | `model.layers.11.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.16004395595816678 / 0.788096163500813 | [NPY](tensors/0000477.npy) |
| 478 | `model.layers.11` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.590309838189019 / 58.568828813877836 | [NPY](tensors/0000478.npy) |

## Layer 0012

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 479 | `model.layers.12` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.590309838189019 / 58.568828813877836 | [NPY](tensors/0000479.npy) |
| 480 | `model.layers.12` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000480.npy) |
| 481 | `model.layers.12` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000481.npy) |
| 482 | `model.layers.12` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000482.npy) |
| 483 | `model.layers.12` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000483.npy) |
| 484 | `model.layers.12` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 485 | `model.layers.12` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 486 | `model.layers.12` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 487 | `model.layers.12.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.590309838189019 / 58.568828813877836 | [NPY](tensors/0000487.npy) |
| 488 | `model.layers.12.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -136.0 / 43.25 / 0.040296143141673825 / 1.588154127563074 | [NPY](tensors/0000488.npy) |
| 489 | `model.layers.12.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -136.0 / 43.25 / 0.040296143141673825 / 1.588154127563074 | [NPY](tensors/0000489.npy) |
| 490 | `model.layers.12.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000490.npy) |
| 491 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000491.npy) |
| 492 | `model.layers.12.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 493 | `model.layers.12.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 494 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000494.npy) |
| 495 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000495.npy) |
| 496 | `model.layers.12.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 497 | `model.layers.12.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -136.0 / 43.25 / 0.040296143141673825 / 1.588154127563074 | [NPY](tensors/0000497.npy) |
| 498 | `model.layers.12.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -19.75 / 18.25 / -0.016075254925563904 / 1.3557645119703536 | [NPY](tensors/0000498.npy) |
| 499 | `model.layers.12.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -136.0 / 43.25 / 0.040296143141673825 / 1.588154127563074 | [NPY](tensors/0000499.npy) |
| 500 | `model.layers.12.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -12.75 / 13.0 / 0.003503983900990597 / 1.3339240740808538 | [NPY](tensors/0000500.npy) |
| 501 | `model.layers.12.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -136.0 / 43.25 / 0.040296143141673825 / 1.588154127563074 | [NPY](tensors/0000501.npy) |
| 502 | `model.layers.12.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -16.0 / 19.5 / 0.0010557648054389072 / 2.838563074538365 | [NPY](tensors/0000502.npy) |
| 503 | `model.layers.12.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -11.375 / 10.5625 / -0.012101290773178222 / 1.4593632365669984 | [NPY](tensors/0000503.npy) |
| 504 | `model.layers.12.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -282.0 / 344.0 / -0.03961364178039923 / 5.989672608759672 | [NPY](tensors/0000504.npy) |
| 505 | `model.layers.12.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -282.0 / 344.0 / -0.03961364178039923 / 5.989672608759672 | [NPY](tensors/0000505.npy) |
| 506 | `model.layers.12.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.97265625 / 0.0029609073489600115 / 0.019074554525240688 | [NPY](tensors/0000506.npy) |
| 507 | `model.layers.12.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 704.0 / 0.5507085790437013 / 57.9240984375913 | [NPY](tensors/0000507.npy) |
| 508 | `model.layers.12.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -83.5 / 8.0 / 0.010646552030353276 / 0.8380738334587191 | [NPY](tensors/0000508.npy) |
| 509 | `model.layers.12.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -83.5 / 8.0 / 0.010646552030353276 / 0.8380738334587191 | [NPY](tensors/0000509.npy) |
| 510 | `model.layers.12.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -83.5 / 8.0 / 0.010646552030353276 / 0.8380738334587191 | [NPY](tensors/0000510.npy) |
| 511 | `model.layers.12.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 512 | `model.layers.12.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 513 | `model.layers.12.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 514 | `model.layers.12.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -1688.0 / 1504.0 / 0.16181979785593906 / 12.773519766241717 | [NPY](tensors/0000514.npy) |
| 515 | `model.layers.12.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -1688.0 / 1504.0 / 0.16181979785593906 / 12.773519766241717 | [NPY](tensors/0000515.npy) |
| 516 | `model.layers.12.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -6.9375 / 3.8125 / -0.15083323412163313 / 0.7954103330067203 | [NPY](tensors/0000516.npy) |
| 517 | `model.layers.12` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 1816.0 / 0.7124901003184553 / 61.66439654285365 | [NPY](tensors/0000517.npy) |

## Layer 0013

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 518 | `model.layers.13` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 1816.0 / 0.7124901003184553 / 61.66439654285365 | [NPY](tensors/0000518.npy) |
| 519 | `model.layers.13` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000519.npy) |
| 520 | `model.layers.13` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000520.npy) |
| 521 | `model.layers.13` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000521.npy) |
| 522 | `model.layers.13` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000522.npy) |
| 523 | `model.layers.13` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 524 | `model.layers.13` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 525 | `model.layers.13` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 526 | `model.layers.13.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 1816.0 / 0.7124901003184553 / 61.66439654285365 | [NPY](tensors/0000526.npy) |
| 527 | `model.layers.13.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -182.0 / 105.0 / 0.06196580683538156 / 2.9054021936182144 | [NPY](tensors/0000527.npy) |
| 528 | `model.layers.13.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -182.0 / 105.0 / 0.06196580683538156 / 2.9054021936182144 | [NPY](tensors/0000528.npy) |
| 529 | `model.layers.13.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000529.npy) |
| 530 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000530.npy) |
| 531 | `model.layers.13.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 532 | `model.layers.13.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 533 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000533.npy) |
| 534 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000534.npy) |
| 535 | `model.layers.13.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 536 | `model.layers.13.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -182.0 / 105.0 / 0.06196580683538156 / 2.9054021936182144 | [NPY](tensors/0000536.npy) |
| 537 | `model.layers.13.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -10.8125 / 12.5625 / 0.03905051595058975 / 1.3918716205492112 | [NPY](tensors/0000537.npy) |
| 538 | `model.layers.13.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -182.0 / 105.0 / 0.06196580683538156 / 2.9054021936182144 | [NPY](tensors/0000538.npy) |
| 539 | `model.layers.13.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -59.5 / 31.25 / -0.33153571794892467 / 4.076801459955772 | [NPY](tensors/0000539.npy) |
| 540 | `model.layers.13.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -182.0 / 105.0 / 0.06196580683538156 / 2.9054021936182144 | [NPY](tensors/0000540.npy) |
| 541 | `model.layers.13.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -16.5 / 22.375 / 0.017953412061513855 / 2.8037981316275764 | [NPY](tensors/0000541.npy) |
| 542 | `model.layers.13.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -11.0 / 20.75 / 0.006880773076962474 / 1.5925248889395651 | [NPY](tensors/0000542.npy) |
| 543 | `model.layers.13.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -568.0 / 1176.0 / -0.07747515657728957 / 9.355563891415972 | [NPY](tensors/0000543.npy) |
| 544 | `model.layers.13.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -568.0 / 1176.0 / -0.07747515657728957 / 9.355563891415972 | [NPY](tensors/0000544.npy) |
| 545 | `model.layers.13.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004134052430475632 / 0.02218802129691248 | [NPY](tensors/0000545.npy) |
| 546 | `model.layers.13.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 1280.0 / 0.6350080926781785 / 60.09516485136014 | [NPY](tensors/0000546.npy) |
| 547 | `model.layers.13.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -86.0 / 6.96875 / 0.00931422770562406 / 0.9199956101096899 | [NPY](tensors/0000547.npy) |
| 548 | `model.layers.13.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -86.0 / 6.96875 / 0.00931422770562406 / 0.9199956101096899 | [NPY](tensors/0000548.npy) |
| 549 | `model.layers.13.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -86.0 / 6.96875 / 0.00931422770562406 / 0.9199956101096899 | [NPY](tensors/0000549.npy) |
| 550 | `model.layers.13.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 551 | `model.layers.13.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 552 | `model.layers.13.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 553 | `model.layers.13.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -472.0 / 616.0 / 0.08581854573823994 / 13.331196340415744 | [NPY](tensors/0000553.npy) |
| 554 | `model.layers.13.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -472.0 / 616.0 / 0.08581854573823994 / 13.331196340415744 | [NPY](tensors/0000554.npy) |
| 555 | `model.layers.13.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -5.46875 / 3.796875 / -0.17335890947386276 / 0.849721290889301 | [NPY](tensors/0000555.npy) |
| 556 | `model.layers.13` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 1144.0 / 0.7208485246998394 / 64.3072713947412 | [NPY](tensors/0000556.npy) |

## Layer 0014

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 557 | `model.layers.14` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 1144.0 / 0.7208485246998394 / 64.3072713947412 | [NPY](tensors/0000557.npy) |
| 558 | `model.layers.14` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000558.npy) |
| 559 | `model.layers.14` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000559.npy) |
| 560 | `model.layers.14` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000560.npy) |
| 561 | `model.layers.14` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000561.npy) |
| 562 | `model.layers.14` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 563 | `model.layers.14` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 564 | `model.layers.14` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 565 | `model.layers.14.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 1144.0 / 0.7208485246998394 / 64.3072713947412 | [NPY](tensors/0000565.npy) |
| 566 | `model.layers.14.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -148.0 / 49.5 / 0.046531633011207406 / 1.9433852328810213 | [NPY](tensors/0000566.npy) |
| 567 | `model.layers.14.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -148.0 / 49.5 / 0.046531633011207406 / 1.9433852328810213 | [NPY](tensors/0000567.npy) |
| 568 | `model.layers.14.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000568.npy) |
| 569 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000569.npy) |
| 570 | `model.layers.14.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 571 | `model.layers.14.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 572 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000572.npy) |
| 573 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000573.npy) |
| 574 | `model.layers.14.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 575 | `model.layers.14.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -148.0 / 49.5 / 0.046531633011207406 / 1.9433852328810213 | [NPY](tensors/0000575.npy) |
| 576 | `model.layers.14.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -53.0 / 29.25 / -0.06421617396031357 / 2.130880251353159 | [NPY](tensors/0000576.npy) |
| 577 | `model.layers.14.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -148.0 / 49.5 / 0.046531633011207406 / 1.9433852328810213 | [NPY](tensors/0000577.npy) |
| 578 | `model.layers.14.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -38.0 / 19.125 / 0.041801130702329235 / 1.6423925223627975 | [NPY](tensors/0000578.npy) |
| 579 | `model.layers.14.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -148.0 / 49.5 / 0.046531633011207406 / 1.9433852328810213 | [NPY](tensors/0000579.npy) |
| 580 | `model.layers.14.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -22.875 / 22.0 / -0.006088408204012144 / 4.710564524979899 | [NPY](tensors/0000580.npy) |
| 581 | `model.layers.14.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -20.125 / 18.375 / -0.012732332614723063 / 2.5979458592211926 | [NPY](tensors/0000581.npy) |
| 582 | `model.layers.14.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -300.0 / 334.0 / -0.040718023935356965 / 8.83912981884131 | [NPY](tensors/0000582.npy) |
| 583 | `model.layers.14.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -300.0 / 334.0 / -0.040718023935356965 / 8.83912981884131 | [NPY](tensors/0000583.npy) |
| 584 | `model.layers.14.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.9609375 / 0.0029375792279594136 / 0.02254937371620431 | [NPY](tensors/0000584.npy) |
| 585 | `model.layers.14.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 932.0 / 0.6800318281779918 / 63.29592657596603 | [NPY](tensors/0000585.npy) |
| 586 | `model.layers.14.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -99.0 / 8.9375 / 0.009927159010285864 / 0.998069946890606 | [NPY](tensors/0000586.npy) |
| 587 | `model.layers.14.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -99.0 / 8.9375 / 0.009927159010285864 / 0.998069946890606 | [NPY](tensors/0000587.npy) |
| 588 | `model.layers.14.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -99.0 / 8.9375 / 0.009927159010285864 / 0.998069946890606 | [NPY](tensors/0000588.npy) |
| 589 | `model.layers.14.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 590 | `model.layers.14.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 591 | `model.layers.14.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 592 | `model.layers.14.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -1280.0 / 1136.0 / 0.045908111823621645 / 18.807801931736467 | [NPY](tensors/0000592.npy) |
| 593 | `model.layers.14.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -1280.0 / 1136.0 / 0.045908111823621645 / 18.807801931736467 | [NPY](tensors/0000593.npy) |
| 594 | `model.layers.14.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -6.84375 / 6.53125 / -0.2416123811588731 / 0.7913569869149978 | [NPY](tensors/0000594.npy) |
| 595 | `model.layers.14` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 2016.0 / 0.726050024697947 / 70.79048728194817 | [NPY](tensors/0000595.npy) |

## Layer 0015

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 596 | `model.layers.15` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 2016.0 / 0.726050024697947 / 70.79048728194817 | [NPY](tensors/0000596.npy) |
| 597 | `model.layers.15` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000597.npy) |
| 598 | `model.layers.15` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000598.npy) |
| 599 | `model.layers.15` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000599.npy) |
| 600 | `model.layers.15` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000600.npy) |
| 601 | `model.layers.15` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 602 | `model.layers.15` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 603 | `model.layers.15` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 604 | `model.layers.15.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 2016.0 / 0.726050024697947 / 70.79048728194817 | [NPY](tensors/0000604.npy) |
| 605 | `model.layers.15.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04633016442817465 / 2.1811608850323267 | [NPY](tensors/0000605.npy) |
| 606 | `model.layers.15.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04633016442817465 / 2.1811608850323267 | [NPY](tensors/0000606.npy) |
| 607 | `model.layers.15.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000607.npy) |
| 608 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000608.npy) |
| 609 | `model.layers.15.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 610 | `model.layers.15.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 611 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000611.npy) |
| 612 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000612.npy) |
| 613 | `model.layers.15.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 614 | `model.layers.15.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04633016442817465 / 2.1811608850323267 | [NPY](tensors/0000614.npy) |
| 615 | `model.layers.15.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -21.25 / 17.75 / 0.009431607651302245 / 1.4462349366909097 | [NPY](tensors/0000615.npy) |
| 616 | `model.layers.15.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04633016442817465 / 2.1811608850323267 | [NPY](tensors/0000616.npy) |
| 617 | `model.layers.15.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -36.75 / 51.25 / 0.033359025098210156 / 4.108535584133033 | [NPY](tensors/0000617.npy) |
| 618 | `model.layers.15.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04633016442817465 / 2.1811608850323267 | [NPY](tensors/0000618.npy) |
| 619 | `model.layers.15.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -61.5 / 38.5 / -0.1334253311850304 / 2.8391125598970217 | [NPY](tensors/0000619.npy) |
| 620 | `model.layers.15.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -11.8125 / 20.375 / -0.08995729901430072 / 1.38709719335515 | [NPY](tensors/0000620.npy) |
| 621 | `model.layers.15.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -1680.0 / 1704.0 / -0.021071541521130294 / 13.048476952360614 | [NPY](tensors/0000621.npy) |
| 622 | `model.layers.15.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -1680.0 / 1704.0 / -0.021071541521130294 / 13.048476952360614 | [NPY](tensors/0000622.npy) |
| 623 | `model.layers.15.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0033044579083725805 / 0.02005612158496461 | [NPY](tensors/0000623.npy) |
| 624 | `model.layers.15.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 1144.0 / 0.7048916708776195 / 68.95381095458121 | [NPY](tensors/0000624.npy) |
| 625 | `model.layers.15.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -106.0 / 9.4375 / 0.010405768449839387 / 0.999718611895616 | [NPY](tensors/0000625.npy) |
| 626 | `model.layers.15.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -106.0 / 9.4375 / 0.010405768449839387 / 0.999718611895616 | [NPY](tensors/0000626.npy) |
| 627 | `model.layers.15.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -106.0 / 9.4375 / 0.010405768449839387 / 0.999718611895616 | [NPY](tensors/0000627.npy) |
| 628 | `model.layers.15.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 629 | `model.layers.15.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 630 | `model.layers.15.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 631 | `model.layers.15.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -784.0 / 600.0 / -0.18891531904846506 / 20.499614899557766 | [NPY](tensors/0000631.npy) |
| 632 | `model.layers.15.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -784.0 / 600.0 / -0.18891531904846506 / 20.499614899557766 | [NPY](tensors/0000632.npy) |
| 633 | `model.layers.15.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -5.5625 / 4.3125 / -0.25850411126779954 / 0.9236998409844317 | [NPY](tensors/0000633.npy) |
| 634 | `model.layers.15` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 1432.0 / 0.515902829034692 / 77.45801216355099 | [NPY](tensors/0000634.npy) |

## Layer 0016

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 635 | `model.layers.16` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 1432.0 / 0.515902829034692 / 77.45801216355099 | [NPY](tensors/0000635.npy) |
| 636 | `model.layers.16` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000636.npy) |
| 637 | `model.layers.16` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000637.npy) |
| 638 | `model.layers.16` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000638.npy) |
| 639 | `model.layers.16` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000639.npy) |
| 640 | `model.layers.16` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 641 | `model.layers.16` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 642 | `model.layers.16` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 643 | `model.layers.16.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 1432.0 / 0.515902829034692 / 77.45801216355099 | [NPY](tensors/0000643.npy) |
| 644 | `model.layers.16.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -131.0 / 52.25 / 0.03291964103104378 / 1.9063173199381387 | [NPY](tensors/0000644.npy) |
| 645 | `model.layers.16.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -131.0 / 52.25 / 0.03291964103104378 / 1.9063173199381387 | [NPY](tensors/0000645.npy) |
| 646 | `model.layers.16.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000646.npy) |
| 647 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000647.npy) |
| 648 | `model.layers.16.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 649 | `model.layers.16.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 650 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000650.npy) |
| 651 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000651.npy) |
| 652 | `model.layers.16.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 653 | `model.layers.16.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -131.0 / 52.25 / 0.03291964103104378 / 1.9063173199381387 | [NPY](tensors/0000653.npy) |
| 654 | `model.layers.16.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -25.375 / 26.0 / 0.032091881186047534 / 1.7116648287272076 | [NPY](tensors/0000654.npy) |
| 655 | `model.layers.16.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -131.0 / 52.25 / 0.03291964103104378 / 1.9063173199381387 | [NPY](tensors/0000655.npy) |
| 656 | `model.layers.16.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -14.875 / 32.25 / 0.041925182834614154 / 1.6469481227741423 | [NPY](tensors/0000656.npy) |
| 657 | `model.layers.16.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -131.0 / 52.25 / 0.03291964103104378 / 1.9063173199381387 | [NPY](tensors/0000657.npy) |
| 658 | `model.layers.16.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -22.75 / 19.625 / 0.041983874592670174 / 4.32957862602886 | [NPY](tensors/0000658.npy) |
| 659 | `model.layers.16.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -20.875 / 17.75 / 0.012489179303550235 / 1.9366503443368366 | [NPY](tensors/0000659.npy) |
| 660 | `model.layers.16.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -422.0 / 392.0 / 0.009862538469565474 / 12.8798366878034 | [NPY](tensors/0000660.npy) |
| 661 | `model.layers.16.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -422.0 / 392.0 / 0.009862538469565474 / 12.8798366878034 | [NPY](tensors/0000661.npy) |
| 662 | `model.layers.16.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.95703125 / 0.0023961629806348687 / 0.018914261163513767 | [NPY](tensors/0000662.npy) |
| 663 | `model.layers.16.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 1328.0 / 0.5255704436191293 / 76.99104641286058 | [NPY](tensors/0000663.npy) |
| 664 | `model.layers.16.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -68.0 / 9.9375 / 0.009600010063759117 / 0.9699120349690017 | [NPY](tensors/0000664.npy) |
| 665 | `model.layers.16.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -68.0 / 9.9375 / 0.009600010063759117 / 0.9699120349690017 | [NPY](tensors/0000665.npy) |
| 666 | `model.layers.16.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -68.0 / 9.9375 / 0.009600010063759117 / 0.9699120349690017 | [NPY](tensors/0000666.npy) |
| 667 | `model.layers.16.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 668 | `model.layers.16.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 669 | `model.layers.16.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 670 | `model.layers.16.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -2384.0 / 1728.0 / -0.20039640591742147 / 32.85771401549762 | [NPY](tensors/0000670.npy) |
| 671 | `model.layers.16.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -2384.0 / 1728.0 / -0.20039640591742147 / 32.85771401549762 | [NPY](tensors/0000671.npy) |
| 672 | `model.layers.16.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -4.90625 / 4.46875 / -0.3016052861546361 / 1.2206631584604468 | [NPY](tensors/0000672.npy) |
| 673 | `model.layers.16` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 2656.0 / 0.3253808794834817 / 95.21923858463387 | [NPY](tensors/0000673.npy) |

## Layer 0017

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 674 | `model.layers.17` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 2656.0 / 0.3253808794834817 / 95.21923858463387 | [NPY](tensors/0000674.npy) |
| 675 | `model.layers.17` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000675.npy) |
| 676 | `model.layers.17` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000676.npy) |
| 677 | `model.layers.17` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000677.npy) |
| 678 | `model.layers.17` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000678.npy) |
| 679 | `model.layers.17` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 680 | `model.layers.17` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 681 | `model.layers.17` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 682 | `model.layers.17.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 2656.0 / 0.3253808794834817 / 95.21923858463387 | [NPY](tensors/0000682.npy) |
| 683 | `model.layers.17.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04118395198839272 / 2.7346632933134103 | [NPY](tensors/0000683.npy) |
| 684 | `model.layers.17.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04118395198839272 / 2.7346632933134103 | [NPY](tensors/0000684.npy) |
| 685 | `model.layers.17.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000685.npy) |
| 686 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000686.npy) |
| 687 | `model.layers.17.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 688 | `model.layers.17.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 689 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000689.npy) |
| 690 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000690.npy) |
| 691 | `model.layers.17.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 692 | `model.layers.17.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04118395198839272 / 2.7346632933134103 | [NPY](tensors/0000692.npy) |
| 693 | `model.layers.17.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -17.0 / 19.25 / 0.015114332234106555 / 1.5745175368418352 | [NPY](tensors/0000693.npy) |
| 694 | `model.layers.17.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04118395198839272 / 2.7346632933134103 | [NPY](tensors/0000694.npy) |
| 695 | `model.layers.17.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -67.5 / 41.25 / -0.02347702385727749 / 4.917160073355956 | [NPY](tensors/0000695.npy) |
| 696 | `model.layers.17.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04118395198839272 / 2.7346632933134103 | [NPY](tensors/0000696.npy) |
| 697 | `model.layers.17.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -19.5 / 21.75 / 0.11067660201427548 / 3.0361123087014272 | [NPY](tensors/0000697.npy) |
| 698 | `model.layers.17.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -10.0625 / 10.9375 / 0.05771133689398317 / 1.2476823194926019 | [NPY](tensors/0000698.npy) |
| 699 | `model.layers.17.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -1520.0 / 1568.0 / 0.259078689168282 / 20.28631098282245 | [NPY](tensors/0000699.npy) |
| 700 | `model.layers.17.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -1520.0 / 1568.0 / 0.259078689168282 / 20.28631098282245 | [NPY](tensors/0000700.npy) |
| 701 | `model.layers.17.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.0033757027258279485 / 0.024072980691171253 | [NPY](tensors/0000701.npy) |
| 702 | `model.layers.17.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41216.0 / 1832.0 / 0.5845179025024099 / 89.9953889766796 | [NPY](tensors/0000702.npy) |
| 703 | `model.layers.17.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41.75 / 10.125 / 0.00890456953020983 / 0.9476396746023574 | [NPY](tensors/0000703.npy) |
| 704 | `model.layers.17.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41.75 / 10.125 / 0.00890456953020983 / 0.9476396746023574 | [NPY](tensors/0000704.npy) |
| 705 | `model.layers.17.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -41.75 / 10.125 / 0.00890456953020983 / 0.9476396746023574 | [NPY](tensors/0000705.npy) |
| 706 | `model.layers.17.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 707 | `model.layers.17.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 708 | `model.layers.17.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 709 | `model.layers.17.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -1176.0 / 40448.0 / -0.06680403820303983 / 63.79865915073898 | [NPY](tensors/0000709.npy) |
| 710 | `model.layers.17.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -1176.0 / 40448.0 / -0.06680403820303983 / 63.79865915073898 | [NPY](tensors/0000710.npy) |
| 711 | `model.layers.17.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -4.90625 / 2.59375 / -0.20113483584204386 / 0.94630651170074 | [NPY](tensors/0000711.npy) |
| 712 | `model.layers.17` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -2416.0 / 2512.0 / 0.5180220721735203 / 98.42854085893534 | [NPY](tensors/0000712.npy) |

## Layer 0018

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 713 | `model.layers.18` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -2416.0 / 2512.0 / 0.5180220721735203 / 98.42854085893534 | [NPY](tensors/0000713.npy) |
| 714 | `model.layers.18` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000714.npy) |
| 715 | `model.layers.18` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000715.npy) |
| 716 | `model.layers.18` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000716.npy) |
| 717 | `model.layers.18` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000717.npy) |
| 718 | `model.layers.18` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 719 | `model.layers.18` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 720 | `model.layers.18` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 721 | `model.layers.18.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -2416.0 / 2512.0 / 0.5180220721735203 / 98.42854085893534 | [NPY](tensors/0000721.npy) |
| 722 | `model.layers.18.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.019997320780458377 / 1.5966374583703236 | [NPY](tensors/0000722.npy) |
| 723 | `model.layers.18.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.019997320780458377 / 1.5966374583703236 | [NPY](tensors/0000723.npy) |
| 724 | `model.layers.18.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000724.npy) |
| 725 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000725.npy) |
| 726 | `model.layers.18.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 727 | `model.layers.18.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 728 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000728.npy) |
| 729 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000729.npy) |
| 730 | `model.layers.18.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 731 | `model.layers.18.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.019997320780458377 / 1.5966374583703236 | [NPY](tensors/0000731.npy) |
| 732 | `model.layers.18.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -26.625 / 31.5 / 0.12114130514214488 / 1.8498116345698046 | [NPY](tensors/0000732.npy) |
| 733 | `model.layers.18.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.019997320780458377 / 1.5966374583703236 | [NPY](tensors/0000733.npy) |
| 734 | `model.layers.18.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -18.5 / 47.75 / 0.1182677419899508 / 2.2512217998734356 | [NPY](tensors/0000734.npy) |
| 735 | `model.layers.18.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.019997320780458377 / 1.5966374583703236 | [NPY](tensors/0000735.npy) |
| 736 | `model.layers.18.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -24.75 / 23.25 / -0.26895648490550905 / 4.2908850282069055 | [NPY](tensors/0000736.npy) |
| 737 | `model.layers.18.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -18.0 / 20.5 / -0.14028738193319865 / 1.8747078609073875 | [NPY](tensors/0000737.npy) |
| 738 | `model.layers.18.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -484.0 / 660.0 / -0.3197123356808449 / 20.589563926581715 | [NPY](tensors/0000738.npy) |
| 739 | `model.layers.18.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -484.0 / 660.0 / -0.3197123356808449 / 20.589563926581715 | [NPY](tensors/0000739.npy) |
| 740 | `model.layers.18.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0021657402974222745 / 0.020544014677456847 | [NPY](tensors/0000740.npy) |
| 741 | `model.layers.18.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -2368.0 / 2464.0 / 0.19806592916641433 / 104.29908343955849 | [NPY](tensors/0000741.npy) |
| 742 | `model.layers.18.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -7.71875 / 13.625 / 0.0027473519769441864 / 0.9113563922722169 | [NPY](tensors/0000742.npy) |
| 743 | `model.layers.18.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -7.71875 / 13.625 / 0.0027473519769441864 / 0.9113563922722169 | [NPY](tensors/0000743.npy) |
| 744 | `model.layers.18.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -7.71875 / 13.625 / 0.0027473519769441864 / 0.9113563922722169 | [NPY](tensors/0000744.npy) |
| 745 | `model.layers.18.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 746 | `model.layers.18.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 747 | `model.layers.18.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 748 | `model.layers.18.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -2112.0 / 2816.0 / 0.2635081936222638 / 56.5122458687478 | [NPY](tensors/0000748.npy) |
| 749 | `model.layers.18.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -2112.0 / 2816.0 / 0.2635081936222638 / 56.5122458687478 | [NPY](tensors/0000749.npy) |
| 750 | `model.layers.18.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -4.65625 / 2.34375 / -0.330963762416396 / 1.0235583576293643 | [NPY](tensors/0000750.npy) |
| 751 | `model.layers.18` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.46187880247446306 / 146.0032181330326 | [NPY](tensors/0000751.npy) |

## Layer 0019

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 752 | `model.layers.19` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.46187880247446306 / 146.0032181330326 | [NPY](tensors/0000752.npy) |
| 753 | `model.layers.19` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000753.npy) |
| 754 | `model.layers.19` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000754.npy) |
| 755 | `model.layers.19` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000755.npy) |
| 756 | `model.layers.19` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000756.npy) |
| 757 | `model.layers.19` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 758 | `model.layers.19` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 759 | `model.layers.19` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 760 | `model.layers.19.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.46187880247446306 / 146.0032181330326 | [NPY](tensors/0000760.npy) |
| 761 | `model.layers.19.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -77.5 / 42.0 / 0.012910936509453973 / 1.8415622687235238 | [NPY](tensors/0000761.npy) |
| 762 | `model.layers.19.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -77.5 / 42.0 / 0.012910936509453973 / 1.8415622687235238 | [NPY](tensors/0000762.npy) |
| 763 | `model.layers.19.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000763.npy) |
| 764 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000764.npy) |
| 765 | `model.layers.19.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 766 | `model.layers.19.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 767 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000767.npy) |
| 768 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000768.npy) |
| 769 | `model.layers.19.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 770 | `model.layers.19.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -77.5 / 42.0 / 0.012910936509453973 / 1.8415622687235238 | [NPY](tensors/0000770.npy) |
| 771 | `model.layers.19.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -14.875 / 24.375 / -0.03815493755697643 / 1.3008386221946766 | [NPY](tensors/0000771.npy) |
| 772 | `model.layers.19.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -77.5 / 42.0 / 0.012910936509453973 / 1.8415622687235238 | [NPY](tensors/0000772.npy) |
| 773 | `model.layers.19.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -79.0 / 71.0 / -0.09752313442701517 / 6.993939826937983 | [NPY](tensors/0000773.npy) |
| 774 | `model.layers.19.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -77.5 / 42.0 / 0.012910936509453973 / 1.8415622687235238 | [NPY](tensors/0000774.npy) |
| 775 | `model.layers.19.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -16.0 / 14.125 / -0.02975946068763733 / 3.156218107991895 | [NPY](tensors/0000775.npy) |
| 776 | `model.layers.19.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -10.6875 / 11.75 / -0.011076929141382757 / 0.9213534405426105 | [NPY](tensors/0000776.npy) |
| 777 | `model.layers.19.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -2176.0 / 1936.0 / -0.5470515847945399 / 42.6885488319606 | [NPY](tensors/0000777.npy) |
| 778 | `model.layers.19.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -2176.0 / 1936.0 / -0.5470515847945399 / 42.6885488319606 | [NPY](tensors/0000778.npy) |
| 779 | `model.layers.19.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.98046875 / 0.0017377897770669633 / 0.011652390688994376 | [NPY](tensors/0000779.npy) |
| 780 | `model.layers.19.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -3584.0 / 3344.0 / -0.08510794311838864 / 127.29405163643031 | [NPY](tensors/0000780.npy) |
| 781 | `model.layers.19.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -7.15625 / 19.0 / 0.0019268111268525285 / 0.9717798083882135 | [NPY](tensors/0000781.npy) |
| 782 | `model.layers.19.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -7.15625 / 19.0 / 0.0019268111268525285 / 0.9717798083882135 | [NPY](tensors/0000782.npy) |
| 783 | `model.layers.19.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -7.15625 / 19.0 / 0.0019268111268525285 / 0.9717798083882135 | [NPY](tensors/0000783.npy) |
| 784 | `model.layers.19.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 785 | `model.layers.19.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 786 | `model.layers.19.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 787 | `model.layers.19.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -2400.0 / 2592.0 / 0.334909375730411 / 84.37832879846192 | [NPY](tensors/0000787.npy) |
| 788 | `model.layers.19.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -2400.0 / 2592.0 / 0.334909375730411 / 84.37832879846192 | [NPY](tensors/0000788.npy) |
| 789 | `model.layers.19.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -6.25 / 3.046875 / -0.28606499960256176 / 1.3978119965329796 | [NPY](tensors/0000789.npy) |
| 790 | `model.layers.19` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -4992.0 / 4608.0 / 0.24967452174933383 / 186.6266498815529 | [NPY](tensors/0000790.npy) |

## Layer 0020

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 791 | `model.layers.20` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -4992.0 / 4608.0 / 0.24967452174933383 / 186.6266498815529 | [NPY](tensors/0000791.npy) |
| 792 | `model.layers.20` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000792.npy) |
| 793 | `model.layers.20` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000793.npy) |
| 794 | `model.layers.20` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000794.npy) |
| 795 | `model.layers.20` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000795.npy) |
| 796 | `model.layers.20` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 797 | `model.layers.20` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 798 | `model.layers.20` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 799 | `model.layers.20.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -4992.0 / 4608.0 / 0.24967452174933383 / 186.6266498815529 | [NPY](tensors/0000799.npy) |
| 800 | `model.layers.20.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -41.75 / 39.0 / 0.010005185199800388 / 1.532425091962317 | [NPY](tensors/0000800.npy) |
| 801 | `model.layers.20.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -41.75 / 39.0 / 0.010005185199800388 / 1.532425091962317 | [NPY](tensors/0000801.npy) |
| 802 | `model.layers.20.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000802.npy) |
| 803 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000803.npy) |
| 804 | `model.layers.20.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 805 | `model.layers.20.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 806 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000806.npy) |
| 807 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000807.npy) |
| 808 | `model.layers.20.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 809 | `model.layers.20.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41.75 / 39.0 / 0.010005185199800388 / 1.532425091962317 | [NPY](tensors/0000809.npy) |
| 810 | `model.layers.20.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -21.125 / 20.5 / 0.0443113064131509 / 1.2364684945522502 | [NPY](tensors/0000810.npy) |
| 811 | `model.layers.20.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41.75 / 39.0 / 0.010005185199800388 / 1.532425091962317 | [NPY](tensors/0000811.npy) |
| 812 | `model.layers.20.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -27.125 / 37.0 / -0.10143377488089161 / 2.230970221821137 | [NPY](tensors/0000812.npy) |
| 813 | `model.layers.20.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -41.75 / 39.0 / 0.010005185199800388 / 1.532425091962317 | [NPY](tensors/0000813.npy) |
| 814 | `model.layers.20.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -22.5 / 20.375 / 0.009563315053318824 / 3.9220793945345997 | [NPY](tensors/0000814.npy) |
| 815 | `model.layers.20.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -17.375 / 15.3125 / -0.008988429535714014 / 1.2827200120776638 | [NPY](tensors/0000815.npy) |
| 816 | `model.layers.20.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -1032.0 / 1120.0 / -0.2183735694249163 / 25.3290880532737 | [NPY](tensors/0000816.npy) |
| 817 | `model.layers.20.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -1032.0 / 1120.0 / -0.2183735694249163 / 25.3290880532737 | [NPY](tensors/0000817.npy) |
| 818 | `model.layers.20.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0018170611574622856 / 0.01696118833748558 | [NPY](tensors/0000818.npy) |
| 819 | `model.layers.20.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -4864.0 / 4864.0 / 0.03161923036402817 / 190.59039763522216 | [NPY](tensors/0000819.npy) |
| 820 | `model.layers.20.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -7.0 / 16.625 / 0.0004576414769626095 / 0.9321744983235545 | [NPY](tensors/0000820.npy) |
| 821 | `model.layers.20.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -7.0 / 16.625 / 0.0004576414769626095 / 0.9321744983235545 | [NPY](tensors/0000821.npy) |
| 822 | `model.layers.20.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -7.0 / 16.625 / 0.0004576414769626095 / 0.9321744983235545 | [NPY](tensors/0000822.npy) |
| 823 | `model.layers.20.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 824 | `model.layers.20.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 825 | `model.layers.20.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 826 | `model.layers.20.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -5888.0 / 6816.0 / 0.39949625508113734 / 85.73002085833384 | [NPY](tensors/0000826.npy) |
| 827 | `model.layers.20.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -5888.0 / 6816.0 / 0.39949625508113734 / 85.73002085833384 | [NPY](tensors/0000827.npy) |
| 828 | `model.layers.20.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -5.28125 / 3.625 / -0.1814317403837692 / 1.175770736794363 | [NPY](tensors/0000828.npy) |
| 829 | `model.layers.20` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -9152.0 / 10304.0 / 0.43107439775491563 / 253.74787001696095 | [NPY](tensors/0000829.npy) |

## Layer 0021

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 830 | `model.layers.21` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -9152.0 / 10304.0 / 0.43107439775491563 / 253.74787001696095 | [NPY](tensors/0000830.npy) |
| 831 | `model.layers.21` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000831.npy) |
| 832 | `model.layers.21` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000832.npy) |
| 833 | `model.layers.21` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000833.npy) |
| 834 | `model.layers.21` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000834.npy) |
| 835 | `model.layers.21` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 836 | `model.layers.21` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 837 | `model.layers.21` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 838 | `model.layers.21.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -9152.0 / 10304.0 / 0.43107439775491563 / 253.74787001696095 | [NPY](tensors/0000838.npy) |
| 839 | `model.layers.21.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.005671861182503615 / 1.813616352278645 | [NPY](tensors/0000839.npy) |
| 840 | `model.layers.21.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.005671861182503615 / 1.813616352278645 | [NPY](tensors/0000840.npy) |
| 841 | `model.layers.21.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000841.npy) |
| 842 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000842.npy) |
| 843 | `model.layers.21.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 844 | `model.layers.21.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 845 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000845.npy) |
| 846 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000846.npy) |
| 847 | `model.layers.21.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 848 | `model.layers.21.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.005671861182503615 / 1.813616352278645 | [NPY](tensors/0000848.npy) |
| 849 | `model.layers.21.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -20.25 / 34.5 / 0.021411269189513065 / 1.1397270208976504 | [NPY](tensors/0000849.npy) |
| 850 | `model.layers.21.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.005671861182503615 / 1.813616352278645 | [NPY](tensors/0000850.npy) |
| 851 | `model.layers.21.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -100.0 / 100.5 / -0.16292465647985768 / 7.905008888608741 | [NPY](tensors/0000851.npy) |
| 852 | `model.layers.21.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.005671861182503615 / 1.813616352278645 | [NPY](tensors/0000852.npy) |
| 853 | `model.layers.21.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -21.5 / 20.5 / -0.014284749086513076 / 3.105394809858123 | [NPY](tensors/0000853.npy) |
| 854 | `model.layers.21.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -15.875 / 13.6875 / 0.0031451939340196226 / 0.675854000418622 | [NPY](tensors/0000854.npy) |
| 855 | `model.layers.21.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -5184.0 / 4736.0 / -0.5654632608827387 / 81.00740468279261 | [NPY](tensors/0000855.npy) |
| 856 | `model.layers.21.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -5184.0 / 4736.0 / -0.5654632608827387 / 81.00740468279261 | [NPY](tensors/0000856.npy) |
| 857 | `model.layers.21.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.90625 / 0.0016874808318112539 / 0.008806104837765866 | [NPY](tensors/0000857.npy) |
| 858 | `model.layers.21.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -5888.0 / 6080.0 / -0.13425543462275225 / 206.808061439138 | [NPY](tensors/0000858.npy) |
| 859 | `model.layers.21.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -8.75 / 22.625 / 0.0006882501050868391 / 1.0523811593694885 | [NPY](tensors/0000859.npy) |
| 860 | `model.layers.21.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -8.75 / 22.625 / 0.0006882501050868391 / 1.0523811593694885 | [NPY](tensors/0000860.npy) |
| 861 | `model.layers.21.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -8.75 / 22.625 / 0.0006882501050868391 / 1.0523811593694885 | [NPY](tensors/0000861.npy) |
| 862 | `model.layers.21.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 863 | `model.layers.21.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 864 | `model.layers.21.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 865 | `model.layers.21.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -6176.0 / 5664.0 / -0.8499840814753096 / 155.4764312776148 | [NPY](tensors/0000865.npy) |
| 866 | `model.layers.21.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -6176.0 / 5664.0 / -0.8499840814753096 / 155.4764312776148 | [NPY](tensors/0000866.npy) |
| 867 | `model.layers.21.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -5.71875 / 4.40625 / -0.22026855335679166 / 1.4824991018015994 | [NPY](tensors/0000867.npy) |
| 868 | `model.layers.21` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -9216.0 / 9664.0 / -0.9849227928930476 / 317.6843105193631 | [NPY](tensors/0000868.npy) |

## Layer 0022

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 869 | `model.layers.22` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -9216.0 / 9664.0 / -0.9849227928930476 / 317.6843105193631 | [NPY](tensors/0000869.npy) |
| 870 | `model.layers.22` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000870.npy) |
| 871 | `model.layers.22` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000871.npy) |
| 872 | `model.layers.22` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000872.npy) |
| 873 | `model.layers.22` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000873.npy) |
| 874 | `model.layers.22` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 875 | `model.layers.22` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 876 | `model.layers.22` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 877 | `model.layers.22.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -9216.0 / 9664.0 / -0.9849227928930476 / 317.6843105193631 | [NPY](tensors/0000877.npy) |
| 878 | `model.layers.22.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -43.25 / 49.0 / 0.001338566530890551 / 1.7227953851171462 | [NPY](tensors/0000878.npy) |
| 879 | `model.layers.22.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -43.25 / 49.0 / 0.001338566530890551 / 1.7227953851171462 | [NPY](tensors/0000879.npy) |
| 880 | `model.layers.22.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.967578058794731e+38 / 1.6726637957572052e+38 | [NPY](tensors/0000880.npy) |
| 881 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000881.npy) |
| 882 | `model.layers.22.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 883 | `model.layers.22.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 884 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000884.npy) |
| 885 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000885.npy) |
| 886 | `model.layers.22.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 887 | `model.layers.22.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -43.25 / 49.0 / 0.001338566530890551 / 1.7227953851171462 | [NPY](tensors/0000887.npy) |
| 888 | `model.layers.22.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -38.75 / 31.875 / -0.05203463842374541 / 2.470251255780102 | [NPY](tensors/0000888.npy) |
| 889 | `model.layers.22.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -43.25 / 49.0 / 0.001338566530890551 / 1.7227953851171462 | [NPY](tensors/0000889.npy) |
| 890 | `model.layers.22.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -32.5 / 8.9375 / -0.05285951439724412 / 1.3602053931915217 | [NPY](tensors/0000890.npy) |
| 891 | `model.layers.22.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -43.25 / 49.0 / 0.001338566530890551 / 1.7227953851171462 | [NPY](tensors/0000891.npy) |
| 892 | `model.layers.22.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -28.125 / 26.125 / -0.022010926590409388 / 4.366436787704987 | [NPY](tensors/0000892.npy) |
| 893 | `model.layers.22.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -19.75 / 14.9375 / -0.024081444326919485 / 1.483952430004267 | [NPY](tensors/0000893.npy) |
| 894 | `model.layers.22.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -2176.0 / 1880.0 / -0.36303501840555696 / 40.447116593205855 | [NPY](tensors/0000894.npy) |
| 895 | `model.layers.22.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -2176.0 / 1880.0 / -0.36303501840555696 / 40.447116593205855 | [NPY](tensors/0000895.npy) |
| 896 | `model.layers.22.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.93359375 / 0.0018411794416289095 / 0.01734741823890015 | [NPY](tensors/0000896.npy) |
| 897 | `model.layers.22.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -9920.0 / 10368.0 / -1.346942156020369 / 328.1797059152606 | [NPY](tensors/0000897.npy) |
| 898 | `model.layers.22.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -20.375 / 17.75 / -0.007350332671126654 / 0.9536636311183277 | [NPY](tensors/0000898.npy) |
| 899 | `model.layers.22.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -20.375 / 17.75 / -0.007350332671126654 / 0.9536636311183277 | [NPY](tensors/0000899.npy) |
| 900 | `model.layers.22.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -20.375 / 17.75 / -0.007350332671126654 / 0.9536636311183277 | [NPY](tensors/0000900.npy) |
| 901 | `model.layers.22.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 902 | `model.layers.22.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 903 | `model.layers.22.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 904 | `model.layers.22.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -6656.0 / 6336.0 / 0.009016681616928531 / 157.72097745727964 | [NPY](tensors/0000904.npy) |
| 905 | `model.layers.22.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -6656.0 / 6336.0 / 0.009016681616928531 / 157.72097745727964 | [NPY](tensors/0000905.npy) |
| 906 | `model.layers.22.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -6.46875 / 4.71875 / -0.1770589606706486 / 1.3560430700320718 | [NPY](tensors/0000906.npy) |
| 907 | `model.layers.22` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -1.3384880349802415 / 423.8727218828635 | [NPY](tensors/0000907.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 908 | `model.layers.23` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -1.3384880349802415 / 423.8727218828635 | [NPY](tensors/0000908.npy) |
| 909 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000909.npy) |
| 910 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000910.npy) |
| 911 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000911.npy) |
| 912 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000912.npy) |
| 913 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 914 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 915 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 916 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -1.3384880349802415 / 423.8727218828635 | [NPY](tensors/0000916.npy) |
| 917 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -52.5 / 71.5 / 0.00993265407742302 / 1.7610013456639688 | [NPY](tensors/0000917.npy) |
| 918 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 215, 2880] | torch.bfloat16 → float32 | -52.5 / 71.5 / 0.00993265407742302 / 1.7610013456639688 | [NPY](tensors/0000918.npy) |
| 919 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 215, 215] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6868830634879736e+38 / 1.6947473628263024e+38 | [NPY](tensors/0000919.npy) |
| 920 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 215] | torch.int64 → int64 | 0.0 / 214.0 / 107.0 / 62.0644825967316 | [NPY](tensors/0000920.npy) |
| 921 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 922 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 923 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8221578376237736 / 0.8676858161516383 | [NPY](tensors/0000923.npy) |
| 924 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 215, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.12216630666597941 / 0.6047353345644831 | [NPY](tensors/0000924.npy) |
| 925 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 926 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -52.5 / 71.5 / 0.00993265407742302 / 1.7610013456639688 | [NPY](tensors/0000926.npy) |
| 927 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 215, 4096] | torch.bfloat16 → float32 | -17.5 / 23.875 / 0.032511419265836936 / 1.6076731085596165 | [NPY](tensors/0000927.npy) |
| 928 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -52.5 / 71.5 / 0.00993265407742302 / 1.7610013456639688 | [NPY](tensors/0000928.npy) |
| 929 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -75.0 / 62.25 / -0.06799435182149674 / 4.91274908129472 | [NPY](tensors/0000929.npy) |
| 930 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -52.5 / 71.5 / 0.00993265407742302 / 1.7610013456639688 | [NPY](tensors/0000930.npy) |
| 931 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 215, 512] | torch.bfloat16 → float32 | -27.375 / 24.125 / 0.005171731183695238 / 3.1181495406018804 | [NPY](tensors/0000931.npy) |
| 932 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 215, 4096] | torch.bfloat16 → float32 | -22.625 / 12.9375 / -0.004583406968942104 / 1.125903327471834 | [NPY](tensors/0000932.npy) |
| 933 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -6112.0 / 6400.0 / 2.8439947979025133 / 169.06361473346794 | [NPY](tensors/0000933.npy) |
| 934 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -6112.0 / 6400.0 / 2.8439947979025133 / 169.06361473346794 | [NPY](tensors/0000934.npy) |
| 935 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 215, 215] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0021455185834268545 / 0.0147897499812375 | [NPY](tensors/0000935.npy) |
| 936 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -11008.0 / 11136.0 / 1.5056701849412546 / 378.82813109160406 | [NPY](tensors/0000936.npy) |
| 937 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -53.25 / 21.75 / -0.014055614976804385 / 1.1897174881041017 | [NPY](tensors/0000937.npy) |
| 938 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -53.25 / 21.75 / -0.014055614976804385 / 1.1897174881041017 | [NPY](tensors/0000938.npy) |
| 939 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [215, 2880] | torch.bfloat16 → float32 | -53.25 / 21.75 / -0.014055614976804385 / 1.1897174881041017 | [NPY](tensors/0000939.npy) |
| 940 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 941 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 942 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 943 | `model.layers.23.mlp.experts` | 0 | `output` | [215, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.5352844902649714 / 153.12021799200681 | [NPY](tensors/0000943.npy) |
| 944 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 215, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.5352844902649714 / 153.12021799200681 | [NPY](tensors/0000944.npy) |
| 945 | `model.layers.23.mlp` | 0 | `output[1]` | [215, 32] | torch.bfloat16 → float32 | -7.1875 / 3.984375 / 0.23163457914840344 / 2.2948858481720587 | [NPY](tensors/0000945.npy) |
| 946 | `model.layers.23` | 0 | `output` | [1, 215, 2880] | torch.bfloat16 → float32 | -11328.0 / 10816.0 / -0.02829382292676034 / 425.5960353393399 | [NPY](tensors/0000946.npy) |

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
