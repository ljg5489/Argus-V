# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 731 full tensors; 950 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Outside Transformer blocks

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model` | 0 | `input.kwargs['input_ids']` | [1, 443] | torch.int64 → int64 | 6.0 / 198835.0 / 28364.801354401807 / 43134.63141591889 | [NPY](tensors/0000000.npy) |
| 1 | `model` | 0 | `input.kwargs['attention_mask']` | [1, 443] | torch.int64 → int64 | 1.0 / 1.0 / 1.0 / 0.0 | [NPY](tensors/0000001.npy) |
| 2 | `model` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 3 | `model` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 4 | `model` | 0 | `input.kwargs['return_dict']` | — | bool | True | — |
| 5 | `model.embed_tokens` | 0 | `input.args[0]` | [1, 443] | torch.int64 → int64 | 6.0 / 198835.0 / 28364.801354401807 / 43134.63141591889 | [NPY](tensors/0000005.npy) |
| 6 | `model.embed_tokens` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.0030488124808973048 / 2.774230889968154 | [NPY](tensors/0000006.npy) |
| 7 | `model.rotary_emb` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.0030488124808973048 / 2.774230889968154 | [NPY](tensors/0000007.npy) |
| 8 | `model.rotary_emb` | 0 | `input.args[1]` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000008.npy) |
| 9 | `model.rotary_emb` | 0 | `output[0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000009.npy) |
| 10 | `model.rotary_emb` | 0 | `output[1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000010.npy) |
| 947 | `model.norm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -10880.0 / 10944.0 / -0.8261206908904134 / 391.3105693416343 | [NPY](tensors/0000947.npy) |
| 948 | `model.norm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -334.0 / 188.0 / -0.03604938812593125 / 6.842689993771995 | [NPY](tensors/0000948.npy) |
| 949 | `model` | 0 | `output['last_hidden_state']` | [1, 443, 2880] | torch.bfloat16 → float32 | -334.0 / 188.0 / -0.03604938812593125 / 6.842689993771995 | [NPY](tensors/0000949.npy) |

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | `model.layers.0` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.0030488124808973048 / 2.774230889968154 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000013.npy) |
| 14 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000014.npy) |
| 15 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 17 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 18 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 19 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.0030488124808973048 / 2.774230889968154 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0028506270508768454 / 0.7534349141179518 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0028506270508768454 / 0.7534349141179518 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 25 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 26 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 29 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0028506270508768454 / 0.7534349141179518 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -10.25 / 12.8125 / 0.019710622075703704 / 1.0475856407650541 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0028506270508768454 / 0.7534349141179518 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.023559566834493714 / 5.773861820546159 | [NPY](tensors/0000032.npy) |
| 33 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.0028506270508768454 / 0.7534349141179518 | [NPY](tensors/0000033.npy) |
| 34 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -8.125 / 7.75 / -0.016734164762000594 / 1.2197421225312854 | [NPY](tensors/0000034.npy) |
| 35 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -8.125 / 7.75 / -0.007152764195554387 / 0.5572880466327884 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -34.75 / 52.5 / 0.029263173286051027 / 1.1897568900549644 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -34.75 / 52.5 / 0.029263173286051027 / 1.1897568900549644 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.000881004987214381 / 0.01952653813479402 | [NPY](tensors/0000038.npy) |
| 39 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -87.5 / 71.0 / 0.0262169376348295 / 2.9579278227909027 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 0.0013839374697908052 / 0.3423912876989626 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 0.0013839374697908052 / 0.3423912876989626 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.78125 / 0.0013839374697908052 / 0.3423912876989626 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 44 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 45 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 46 | `model.layers.0.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.018912295382708152 / 0.9062353190480502 | [NPY](tensors/0000046.npy) |
| 47 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -50.0 / 92.0 / 0.018912295382708152 / 0.9062353190480502 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.0.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -5.15625 / 3.4375 / -0.10482937918290597 / 1.0144097814325919 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.0` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -92.0 / 105.5 / 0.045123762963094415 / 3.222613247441156 | [NPY](tensors/0000049.npy) |

## Layer 0001

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | `model.layers.1` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -92.0 / 105.5 / 0.045123762963094415 / 3.222613247441156 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.1` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.1` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000052.npy) |
| 53 | `model.layers.1` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000053.npy) |
| 54 | `model.layers.1` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.1` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 56 | `model.layers.1` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 57 | `model.layers.1` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 58 | `model.layers.1.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -92.0 / 105.5 / 0.045123762963094415 / 3.222613247441156 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.1.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -29.5 / 25.625 / 0.010478558295700957 / 0.8543258195630264 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.1.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -29.5 / 25.625 / 0.010478558295700957 / 0.8543258195630264 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.1.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.1.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 64 | `model.layers.1.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 65 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.1.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 68 | `model.layers.1.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -29.5 / 25.625 / 0.010478558295700957 / 0.8543258195630264 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.1.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -11.4375 / 12.25 / -0.01781678742074299 / 1.1097968908265907 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.1.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -29.5 / 25.625 / 0.010478558295700957 / 0.8543258195630264 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.1.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -111.5 / 44.0 / -0.714345850672749 / 7.916504666678713 | [NPY](tensors/0000071.npy) |
| 72 | `model.layers.1.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -29.5 / 25.625 / 0.010478558295700957 / 0.8543258195630264 | [NPY](tensors/0000072.npy) |
| 73 | `model.layers.1.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -6.5625 / 7.96875 / 0.01639475193756063 / 1.0030151084586405 | [NPY](tensors/0000073.npy) |
| 74 | `model.layers.1.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -5.8125 / 5.90625 / 0.003363354166722201 / 0.4480967295026675 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.1.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -33.75 / 52.75 / 0.0037357084513985274 / 0.8374624805786047 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.1.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -33.75 / 52.75 / 0.0037357084513985274 / 0.8374624805786047 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.1.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0015313905828168081 / 0.01727889604808424 | [NPY](tensors/0000077.npy) |
| 78 | `model.layers.1.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -96.0 / 83.0 / 0.048855055697077286 / 3.1802212485219163 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.1.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.421875 / 0.001705882675826161 / 0.37235657769097397 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.1.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.421875 / 0.001705882675826161 / 0.37235657769097397 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.1.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.421875 / 0.001705882675826161 / 0.37235657769097397 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.1.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 83 | `model.layers.1.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 84 | `model.layers.1.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 85 | `model.layers.1.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -47.25 / 82.0 / 0.020990779432499652 / 1.0663699092042966 | [NPY](tensors/0000085.npy) |
| 86 | `model.layers.1.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -47.25 / 82.0 / 0.020990779432499652 / 1.0663699092042966 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.1.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -2.890625 / 2.75 / -0.09429091632231633 / 0.7324932628833465 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.1` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -109.5 / 130.0 / 0.06983834924571101 / 3.7019276946095045 | [NPY](tensors/0000088.npy) |

## Layer 0002

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 89 | `model.layers.2` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -109.5 / 130.0 / 0.06983834924571101 / 3.7019276946095045 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.2` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.2` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000091.npy) |
| 92 | `model.layers.2` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000092.npy) |
| 93 | `model.layers.2` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.2` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 95 | `model.layers.2` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 96 | `model.layers.2` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 97 | `model.layers.2.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -109.5 / 130.0 / 0.06983834924571101 / 3.7019276946095045 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.2.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -29.125 / 24.875 / 0.015608719236969364 / 0.8585429382604763 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.2.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -29.125 / 24.875 / 0.015608719236969364 / 0.8585429382604763 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.2.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.2.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 103 | `model.layers.2.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 104 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.2.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 107 | `model.layers.2.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -29.125 / 24.875 / 0.015608719236969364 / 0.8585429382604763 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.2.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -13.8125 / 8.375 / 0.039926925815362536 / 0.8993411387434825 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.2.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -29.125 / 24.875 / 0.015608719236969364 / 0.8585429382604763 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.2.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -28.875 / 22.875 / -0.01828767584059198 / 2.628461423452129 | [NPY](tensors/0000110.npy) |
| 111 | `model.layers.2.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -29.125 / 24.875 / 0.015608719236969364 / 0.8585429382604763 | [NPY](tensors/0000111.npy) |
| 112 | `model.layers.2.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -8.0 / 6.5 / 0.021768848076946276 / 1.1555262652852416 | [NPY](tensors/0000112.npy) |
| 113 | `model.layers.2.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -6.53125 / 6.21875 / 0.011334908324910013 / 0.4791493341065191 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.2.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -48.75 / 54.75 / -0.0015442690928379019 / 0.9648289832120475 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.2.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -48.75 / 54.75 / -0.0015442690928379019 / 0.9648289832120475 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.2.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0011076513632047968 / 0.015494459457864826 | [NPY](tensors/0000116.npy) |
| 117 | `model.layers.2.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -83.0 / 123.0 / 0.06829279827793529 / 3.673775021482484 | [NPY](tensors/0000117.npy) |
| 118 | `model.layers.2.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.28125 / 0.002939348246464013 / 0.46186562178210167 | [NPY](tensors/0000118.npy) |
| 119 | `model.layers.2.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.28125 / 0.002939348246464013 / 0.46186562178210167 | [NPY](tensors/0000119.npy) |
| 120 | `model.layers.2.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.28125 / 0.002939348246464013 / 0.46186562178210167 | [NPY](tensors/0000120.npy) |
| 121 | `model.layers.2.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 122 | `model.layers.2.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 123 | `model.layers.2.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 124 | `model.layers.2.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -57.0 / 88.5 / 0.023425733588649005 / 1.2401452578245171 | [NPY](tensors/0000124.npy) |
| 125 | `model.layers.2.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -57.0 / 88.5 / 0.023425733588649005 / 1.2401452578245171 | [NPY](tensors/0000125.npy) |
| 126 | `model.layers.2.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -3.3125 / 2.21875 / -0.10571639101876631 / 0.6810322793045065 | [NPY](tensors/0000126.npy) |
| 127 | `model.layers.2` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -117.5 / 148.0 / 0.09171894911031005 / 4.309489681966444 | [NPY](tensors/0000127.npy) |

## Layer 0003

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | `model.layers.3` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -117.5 / 148.0 / 0.09171894911031005 / 4.309489681966444 | [NPY](tensors/0000128.npy) |
| 129 | `model.layers.3` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000129.npy) |
| 130 | `model.layers.3` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000130.npy) |
| 131 | `model.layers.3` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000131.npy) |
| 132 | `model.layers.3` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000132.npy) |
| 133 | `model.layers.3` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 134 | `model.layers.3` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 135 | `model.layers.3` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 136 | `model.layers.3.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -117.5 / 148.0 / 0.09171894911031005 / 4.309489681966444 | [NPY](tensors/0000136.npy) |
| 137 | `model.layers.3.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -59.25 / 56.25 / 0.03394199030743391 / 1.252339774165749 | [NPY](tensors/0000137.npy) |
| 138 | `model.layers.3.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -59.25 / 56.25 / 0.03394199030743391 / 1.252339774165749 | [NPY](tensors/0000138.npy) |
| 139 | `model.layers.3.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000139.npy) |
| 140 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000140.npy) |
| 141 | `model.layers.3.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 142 | `model.layers.3.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 143 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000143.npy) |
| 144 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000144.npy) |
| 145 | `model.layers.3.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 146 | `model.layers.3.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -59.25 / 56.25 / 0.03394199030743391 / 1.252339774165749 | [NPY](tensors/0000146.npy) |
| 147 | `model.layers.3.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -13.3125 / 9.0 / -0.02281875526652264 / 1.1355107404178035 | [NPY](tensors/0000147.npy) |
| 148 | `model.layers.3.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -59.25 / 56.25 / 0.03394199030743391 / 1.252339774165749 | [NPY](tensors/0000148.npy) |
| 149 | `model.layers.3.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -79.5 / 56.5 / -0.06964901693083311 / 4.976778933846337 | [NPY](tensors/0000149.npy) |
| 150 | `model.layers.3.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -59.25 / 56.25 / 0.03394199030743391 / 1.252339774165749 | [NPY](tensors/0000150.npy) |
| 151 | `model.layers.3.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -7.5 / 11.375 / 0.014864398659791368 / 0.9703813876636518 | [NPY](tensors/0000151.npy) |
| 152 | `model.layers.3.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -4.75 / 4.0625 / 0.010317040877029221 / 0.34516238258918663 | [NPY](tensors/0000152.npy) |
| 153 | `model.layers.3.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -63.25 / 48.75 / -0.0042101046117933635 / 1.0281483722404856 | [NPY](tensors/0000153.npy) |
| 154 | `model.layers.3.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -63.25 / 48.75 / -0.0042101046117933635 / 1.0281483722404856 | [NPY](tensors/0000154.npy) |
| 155 | `model.layers.3.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0012988229291544917 / 0.011406038013531402 | [NPY](tensors/0000155.npy) |
| 156 | `model.layers.3.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -103.0 / 134.0 / 0.08751926482442542 / 4.391524007834444 | [NPY](tensors/0000156.npy) |
| 157 | `model.layers.3.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -6.0 / 5.71875 / 0.0036910639404932866 / 0.5166380338052227 | [NPY](tensors/0000157.npy) |
| 158 | `model.layers.3.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -6.0 / 5.71875 / 0.0036910639404932866 / 0.5166380338052227 | [NPY](tensors/0000158.npy) |
| 159 | `model.layers.3.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -6.0 / 5.71875 / 0.0036910639404932866 / 0.5166380338052227 | [NPY](tensors/0000159.npy) |
| 160 | `model.layers.3.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 161 | `model.layers.3.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 162 | `model.layers.3.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 163 | `model.layers.3.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -61.25 / 94.0 / 0.02145169215234324 / 1.3953819125123046 | [NPY](tensors/0000163.npy) |
| 164 | `model.layers.3.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -61.25 / 94.0 / 0.02145169215234324 / 1.3953819125123046 | [NPY](tensors/0000164.npy) |
| 165 | `model.layers.3.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -3.625 / 2.015625 / -0.08243264893645896 / 0.5508298334685787 | [NPY](tensors/0000165.npy) |
| 166 | `model.layers.3` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -150.0 / 171.0 / 0.10898044459168582 / 5.156663216043971 | [NPY](tensors/0000166.npy) |

## Layer 0004

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 167 | `model.layers.4` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -150.0 / 171.0 / 0.10898044459168582 / 5.156663216043971 | [NPY](tensors/0000167.npy) |
| 168 | `model.layers.4` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000168.npy) |
| 169 | `model.layers.4` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000169.npy) |
| 170 | `model.layers.4` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000170.npy) |
| 171 | `model.layers.4` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000171.npy) |
| 172 | `model.layers.4` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 173 | `model.layers.4` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 174 | `model.layers.4` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 175 | `model.layers.4.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -150.0 / 171.0 / 0.10898044459168582 / 5.156663216043971 | [NPY](tensors/0000175.npy) |
| 176 | `model.layers.4.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.021118758166041147 / 1.1341226999055276 | [NPY](tensors/0000176.npy) |
| 177 | `model.layers.4.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.021118758166041147 / 1.1341226999055276 | [NPY](tensors/0000177.npy) |
| 178 | `model.layers.4.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000178.npy) |
| 179 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000179.npy) |
| 180 | `model.layers.4.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 181 | `model.layers.4.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 182 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000182.npy) |
| 183 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000183.npy) |
| 184 | `model.layers.4.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 185 | `model.layers.4.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.021118758166041147 / 1.1341226999055276 | [NPY](tensors/0000185.npy) |
| 186 | `model.layers.4.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -16.875 / 8.1875 / -0.010793312802819172 / 1.0388402040670495 | [NPY](tensors/0000186.npy) |
| 187 | `model.layers.4.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.021118758166041147 / 1.1341226999055276 | [NPY](tensors/0000187.npy) |
| 188 | `model.layers.4.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -16.5 / 99.5 / 0.24867310222045416 / 4.408318672238968 | [NPY](tensors/0000188.npy) |
| 189 | `model.layers.4.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.021118758166041147 / 1.1341226999055276 | [NPY](tensors/0000189.npy) |
| 190 | `model.layers.4.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -10.8125 / 17.25 / 0.0036244010229534037 / 1.3528575561697138 | [NPY](tensors/0000190.npy) |
| 191 | `model.layers.4.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -9.625 / 15.125 / -0.0032183304784137 / 0.6069786481746176 | [NPY](tensors/0000191.npy) |
| 192 | `model.layers.4.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -69.0 / 44.5 / -0.0016245284269942033 / 1.234418957254239 | [NPY](tensors/0000192.npy) |
| 193 | `model.layers.4.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -69.0 / 44.5 / -0.0016245284269942033 / 1.234418957254239 | [NPY](tensors/0000193.npy) |
| 194 | `model.layers.4.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0011827526942809127 / 0.01503257961367548 | [NPY](tensors/0000194.npy) |
| 195 | `model.layers.4.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -141.0 / 158.0 / 0.10734516748187234 / 5.1909333163343785 | [NPY](tensors/0000195.npy) |
| 196 | `model.layers.4.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -5.875 / 6.90625 / 0.007177475494327237 / 0.5716976447305895 | [NPY](tensors/0000196.npy) |
| 197 | `model.layers.4.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -5.875 / 6.90625 / 0.007177475494327237 / 0.5716976447305895 | [NPY](tensors/0000197.npy) |
| 198 | `model.layers.4.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -5.875 / 6.90625 / 0.007177475494327237 / 0.5716976447305895 | [NPY](tensors/0000198.npy) |
| 199 | `model.layers.4.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 200 | `model.layers.4.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 201 | `model.layers.4.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 202 | `model.layers.4.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -81.5 / 164.0 / 0.03848305441680218 / 2.0636648568467977 | [NPY](tensors/0000202.npy) |
| 203 | `model.layers.4.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -81.5 / 164.0 / 0.03848305441680218 / 2.0636648568467977 | [NPY](tensors/0000203.npy) |
| 204 | `model.layers.4.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -3.828125 / 2.171875 / -0.09509286815910253 / 0.6138989168290042 | [NPY](tensors/0000204.npy) |
| 205 | `model.layers.4` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -192.0 / 252.0 / 0.14582552982805846 / 6.379607770449355 | [NPY](tensors/0000205.npy) |

## Layer 0005

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 206 | `model.layers.5` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -192.0 / 252.0 / 0.14582552982805846 / 6.379607770449355 | [NPY](tensors/0000206.npy) |
| 207 | `model.layers.5` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000207.npy) |
| 208 | `model.layers.5` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000208.npy) |
| 209 | `model.layers.5` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000209.npy) |
| 210 | `model.layers.5` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000210.npy) |
| 211 | `model.layers.5` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 212 | `model.layers.5` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 213 | `model.layers.5` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 214 | `model.layers.5.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -192.0 / 252.0 / 0.14582552982805846 / 6.379607770449355 | [NPY](tensors/0000214.npy) |
| 215 | `model.layers.5.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -32.0 / 41.0 / 0.033574627085507354 / 1.1831732333100224 | [NPY](tensors/0000215.npy) |
| 216 | `model.layers.5.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -32.0 / 41.0 / 0.033574627085507354 / 1.1831732333100224 | [NPY](tensors/0000216.npy) |
| 217 | `model.layers.5.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000217.npy) |
| 218 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000218.npy) |
| 219 | `model.layers.5.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 220 | `model.layers.5.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 221 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000221.npy) |
| 222 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000222.npy) |
| 223 | `model.layers.5.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 224 | `model.layers.5.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -32.0 / 41.0 / 0.033574627085507354 / 1.1831732333100224 | [NPY](tensors/0000224.npy) |
| 225 | `model.layers.5.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -20.0 / 16.125 / -0.058282460153329725 / 1.445603340474706 | [NPY](tensors/0000225.npy) |
| 226 | `model.layers.5.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -32.0 / 41.0 / 0.033574627085507354 / 1.1831732333100224 | [NPY](tensors/0000226.npy) |
| 227 | `model.layers.5.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -35.75 / 40.75 / -0.04710169161594227 / 3.4896262343819395 | [NPY](tensors/0000227.npy) |
| 228 | `model.layers.5.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -32.0 / 41.0 / 0.033574627085507354 / 1.1831732333100224 | [NPY](tensors/0000228.npy) |
| 229 | `model.layers.5.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -7.25 / 8.4375 / 0.011109146646131461 / 1.193146544615679 | [NPY](tensors/0000229.npy) |
| 230 | `model.layers.5.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -5.21875 / 5.59375 / 0.007500409817545532 / 0.5483524079283342 | [NPY](tensors/0000230.npy) |
| 231 | `model.layers.5.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -92.0 / 78.5 / -0.0020470258729134794 / 1.5626839397347896 | [NPY](tensors/0000231.npy) |
| 232 | `model.layers.5.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -92.0 / 78.5 / -0.0020470258729134794 / 1.5626839397347896 | [NPY](tensors/0000232.npy) |
| 233 | `model.layers.5.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.001385271339532258 / 0.012138079828370623 | [NPY](tensors/0000233.npy) |
| 234 | `model.layers.5.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -142.0 / 206.0 / 0.1437671395151843 / 6.774811071285366 | [NPY](tensors/0000234.npy) |
| 235 | `model.layers.5.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.125 / 0.007307437201856759 / 0.5614410732632601 | [NPY](tensors/0000235.npy) |
| 236 | `model.layers.5.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.125 / 0.007307437201856759 / 0.5614410732632601 | [NPY](tensors/0000236.npy) |
| 237 | `model.layers.5.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.125 / 0.007307437201856759 / 0.5614410732632601 | [NPY](tensors/0000237.npy) |
| 238 | `model.layers.5.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 239 | `model.layers.5.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 240 | `model.layers.5.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 241 | `model.layers.5.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -122.0 / 117.5 / 0.040735591092533066 / 2.354234227762147 | [NPY](tensors/0000241.npy) |
| 242 | `model.layers.5.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -122.0 / 117.5 / 0.040735591092533066 / 2.354234227762147 | [NPY](tensors/0000242.npy) |
| 243 | `model.layers.5.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -4.375 / 2.265625 / -0.09439167642701023 / 0.6096490322303235 | [NPY](tensors/0000243.npy) |
| 244 | `model.layers.5` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -196.0 / 296.0 / 0.18450977707196214 / 8.178659598925538 | [NPY](tensors/0000244.npy) |

## Layer 0006

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 245 | `model.layers.6` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -196.0 / 296.0 / 0.18450977707196214 / 8.178659598925538 | [NPY](tensors/0000245.npy) |
| 246 | `model.layers.6` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000246.npy) |
| 247 | `model.layers.6` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000247.npy) |
| 248 | `model.layers.6` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000248.npy) |
| 249 | `model.layers.6` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000249.npy) |
| 250 | `model.layers.6` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 251 | `model.layers.6` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 252 | `model.layers.6` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 253 | `model.layers.6.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -196.0 / 296.0 / 0.18450977707196214 / 8.178659598925538 | [NPY](tensors/0000253.npy) |
| 254 | `model.layers.6.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -35.0 / 43.0 / 0.029943735904735615 / 1.3086874680023084 | [NPY](tensors/0000254.npy) |
| 255 | `model.layers.6.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -35.0 / 43.0 / 0.029943735904735615 / 1.3086874680023084 | [NPY](tensors/0000255.npy) |
| 256 | `model.layers.6.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000256.npy) |
| 257 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000257.npy) |
| 258 | `model.layers.6.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 259 | `model.layers.6.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 260 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000260.npy) |
| 261 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000261.npy) |
| 262 | `model.layers.6.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 263 | `model.layers.6.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -35.0 / 43.0 / 0.029943735904735615 / 1.3086874680023084 | [NPY](tensors/0000263.npy) |
| 264 | `model.layers.6.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -29.125 / 17.375 / -0.025606600783008512 / 1.151242887127042 | [NPY](tensors/0000264.npy) |
| 265 | `model.layers.6.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -35.0 / 43.0 / 0.029943735904735615 / 1.3086874680023084 | [NPY](tensors/0000265.npy) |
| 266 | `model.layers.6.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -20.625 / 32.75 / 0.21572963546742904 / 2.3867420794954826 | [NPY](tensors/0000266.npy) |
| 267 | `model.layers.6.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -35.0 / 43.0 / 0.029943735904735615 / 1.3086874680023084 | [NPY](tensors/0000267.npy) |
| 268 | `model.layers.6.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -10.5625 / 8.6875 / -0.046399094171335385 / 1.609596363447922 | [NPY](tensors/0000268.npy) |
| 269 | `model.layers.6.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -9.5 / 7.65625 / -0.03237957098655864 / 0.8082342880293681 | [NPY](tensors/0000269.npy) |
| 270 | `model.layers.6.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -91.0 / 81.0 / -0.00025082920706691455 / 1.7838336774476398 | [NPY](tensors/0000270.npy) |
| 271 | `model.layers.6.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -91.0 / 81.0 / -0.00025082920706691455 / 1.7838336774476398 | [NPY](tensors/0000271.npy) |
| 272 | `model.layers.6.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0012827957717500577 / 0.016394052465863687 | [NPY](tensors/0000272.npy) |
| 273 | `model.layers.6.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -181.0 / 247.0 / 0.18425848570747844 / 8.122893534149869 | [NPY](tensors/0000273.npy) |
| 274 | `model.layers.6.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -22.0 / 6.0625 / 0.01043391061359505 / 0.5955751380641131 | [NPY](tensors/0000274.npy) |
| 275 | `model.layers.6.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -22.0 / 6.0625 / 0.01043391061359505 / 0.5955751380641131 | [NPY](tensors/0000275.npy) |
| 276 | `model.layers.6.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -22.0 / 6.0625 / 0.01043391061359505 / 0.5955751380641131 | [NPY](tensors/0000276.npy) |
| 277 | `model.layers.6.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 278 | `model.layers.6.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 279 | `model.layers.6.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 280 | `model.layers.6.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -41472.0 / 968.0 / 0.00024071175031361344 / 36.87655039373794 | [NPY](tensors/0000280.npy) |
| 281 | `model.layers.6.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41472.0 / 968.0 / 0.00024071175031361344 / 36.87655039373794 | [NPY](tensors/0000281.npy) |
| 282 | `model.layers.6.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -4.4375 / 5.0 / -0.1271913455248417 / 0.7723356997840274 | [NPY](tensors/0000282.npy) |
| 283 | `model.layers.6` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.1845605145787607 / 38.06465453218721 | [NPY](tensors/0000283.npy) |

## Layer 0007

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 284 | `model.layers.7` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.1845605145787607 / 38.06465453218721 | [NPY](tensors/0000284.npy) |
| 285 | `model.layers.7` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000285.npy) |
| 286 | `model.layers.7` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000286.npy) |
| 287 | `model.layers.7` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000287.npy) |
| 288 | `model.layers.7` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000288.npy) |
| 289 | `model.layers.7` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 290 | `model.layers.7` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 291 | `model.layers.7` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 292 | `model.layers.7.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.1845605145787607 / 38.06465453218721 | [NPY](tensors/0000292.npy) |
| 293 | `model.layers.7.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03685721965912652 / 1.6226568324038337 | [NPY](tensors/0000293.npy) |
| 294 | `model.layers.7.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03685721965912652 / 1.6226568324038337 | [NPY](tensors/0000294.npy) |
| 295 | `model.layers.7.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000295.npy) |
| 296 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000296.npy) |
| 297 | `model.layers.7.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 298 | `model.layers.7.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 299 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000299.npy) |
| 300 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000300.npy) |
| 301 | `model.layers.7.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 302 | `model.layers.7.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03685721965912652 / 1.6226568324038337 | [NPY](tensors/0000302.npy) |
| 303 | `model.layers.7.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -13.625 / 13.25 / -0.11811191941602171 / 1.4352407575483441 | [NPY](tensors/0000303.npy) |
| 304 | `model.layers.7.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03685721965912652 / 1.6226568324038337 | [NPY](tensors/0000304.npy) |
| 305 | `model.layers.7.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -133.0 / 34.0 / -0.0665894085507862 / 5.489680368447153 | [NPY](tensors/0000305.npy) |
| 306 | `model.layers.7.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03685721965912652 / 1.6226568324038337 | [NPY](tensors/0000306.npy) |
| 307 | `model.layers.7.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -17.0 / 10.8125 / 0.006922232645141218 / 1.6328318945569287 | [NPY](tensors/0000307.npy) |
| 308 | `model.layers.7.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -7.6875 / 7.84375 / 0.004158282606443857 / 0.935603936174789 | [NPY](tensors/0000308.npy) |
| 309 | `model.layers.7.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -120.0 / 129.0 / 0.0011305019968397899 / 2.2473692482357204 | [NPY](tensors/0000309.npy) |
| 310 | `model.layers.7.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -120.0 / 129.0 / 0.0011305019968397899 / 2.2473692482357204 | [NPY](tensors/0000310.npy) |
| 311 | `model.layers.7.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0018121671670559393 / 0.018587091109829125 | [NPY](tensors/0000311.npy) |
| 312 | `model.layers.7.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41472.0 / 1104.0 / 0.18569860714612704 / 38.10314570907125 | [NPY](tensors/0000312.npy) |
| 313 | `model.layers.7.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -77.0 / 6.84375 / 0.009975269734102636 / 0.6165428658185405 | [NPY](tensors/0000313.npy) |
| 314 | `model.layers.7.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -77.0 / 6.84375 / 0.009975269734102636 / 0.6165428658185405 | [NPY](tensors/0000314.npy) |
| 315 | `model.layers.7.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -77.0 / 6.84375 / 0.009975269734102636 / 0.6165428658185405 | [NPY](tensors/0000315.npy) |
| 316 | `model.layers.7.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 317 | `model.layers.7.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 318 | `model.layers.7.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 319 | `model.layers.7.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -200.0 / 188.0 / 0.03693791268790967 / 3.4232916067997703 | [NPY](tensors/0000319.npy) |
| 320 | `model.layers.7.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -200.0 / 188.0 / 0.03693791268790967 / 3.4232916067997703 | [NPY](tensors/0000320.npy) |
| 321 | `model.layers.7.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -3.890625 / 3.828125 / -0.14487418740920505 / 0.8243249800222101 | [NPY](tensors/0000321.npy) |
| 322 | `model.layers.7` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.22263895330914646 / 38.670150576284904 | [NPY](tensors/0000322.npy) |

## Layer 0008

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 323 | `model.layers.8` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.22263895330914646 / 38.670150576284904 | [NPY](tensors/0000323.npy) |
| 324 | `model.layers.8` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000324.npy) |
| 325 | `model.layers.8` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000325.npy) |
| 326 | `model.layers.8` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000326.npy) |
| 327 | `model.layers.8` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000327.npy) |
| 328 | `model.layers.8` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 329 | `model.layers.8` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 330 | `model.layers.8` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 331 | `model.layers.8.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.22263895330914646 / 38.670150576284904 | [NPY](tensors/0000331.npy) |
| 332 | `model.layers.8.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -121.5 / 46.75 / 0.02869493639646021 / 1.325122061041983 | [NPY](tensors/0000332.npy) |
| 333 | `model.layers.8.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -121.5 / 46.75 / 0.02869493639646021 / 1.325122061041983 | [NPY](tensors/0000333.npy) |
| 334 | `model.layers.8.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000334.npy) |
| 335 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000335.npy) |
| 336 | `model.layers.8.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 337 | `model.layers.8.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 338 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000338.npy) |
| 339 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000339.npy) |
| 340 | `model.layers.8.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 341 | `model.layers.8.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -121.5 / 46.75 / 0.02869493639646021 / 1.325122061041983 | [NPY](tensors/0000341.npy) |
| 342 | `model.layers.8.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -14.9375 / 15.25 / -0.01123910074178306 / 1.0639906569920958 | [NPY](tensors/0000342.npy) |
| 343 | `model.layers.8.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -121.5 / 46.75 / 0.02869493639646021 / 1.325122061041983 | [NPY](tensors/0000343.npy) |
| 344 | `model.layers.8.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -22.375 / 31.625 / 0.004137836931731644 / 2.234889103740958 | [NPY](tensors/0000344.npy) |
| 345 | `model.layers.8.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -121.5 / 46.75 / 0.02869493639646021 / 1.325122061041983 | [NPY](tensors/0000345.npy) |
| 346 | `model.layers.8.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -9.3125 / 9.625 / 0.001841229175082902 / 1.707017671464863 | [NPY](tensors/0000346.npy) |
| 347 | `model.layers.8.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -7.21875 / 7.78125 / 0.004677941650196963 / 0.8591279335965634 | [NPY](tensors/0000347.npy) |
| 348 | `model.layers.8.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -199.0 / 212.0 / 0.012902990822379666 / 2.825814487696099 | [NPY](tensors/0000348.npy) |
| 349 | `model.layers.8.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -199.0 / 212.0 / 0.012902990822379666 / 2.825814487696099 | [NPY](tensors/0000349.npy) |
| 350 | `model.layers.8.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.001418725822429788 / 0.015751260282181736 | [NPY](tensors/0000350.npy) |
| 351 | `model.layers.8.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41472.0 / 1344.0 / 0.23553503069747264 / 38.630370843320605 | [NPY](tensors/0000351.npy) |
| 352 | `model.layers.8.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -57.0 / 6.375 / 0.01034612737216218 / 0.6513777514523382 | [NPY](tensors/0000352.npy) |
| 353 | `model.layers.8.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -57.0 / 6.375 / 0.01034612737216218 / 0.6513777514523382 | [NPY](tensors/0000353.npy) |
| 354 | `model.layers.8.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -57.0 / 6.375 / 0.01034612737216218 / 0.6513777514523382 | [NPY](tensors/0000354.npy) |
| 355 | `model.layers.8.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 356 | `model.layers.8.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 357 | `model.layers.8.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 358 | `model.layers.8.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -294.0 / 251.0 / 0.05289065709591269 / 4.56370424661639 | [NPY](tensors/0000358.npy) |
| 359 | `model.layers.8.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -294.0 / 251.0 / 0.05289065709591269 / 4.56370424661639 | [NPY](tensors/0000359.npy) |
| 360 | `model.layers.8.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -3.921875 / 3.53125 / -0.17981545596843918 / 0.7700658939247699 | [NPY](tensors/0000360.npy) |
| 361 | `model.layers.8` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.28838439369249497 / 39.73857337763997 | [NPY](tensors/0000361.npy) |

## Layer 0009

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 362 | `model.layers.9` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.28838439369249497 / 39.73857337763997 | [NPY](tensors/0000362.npy) |
| 363 | `model.layers.9` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000363.npy) |
| 364 | `model.layers.9` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000364.npy) |
| 365 | `model.layers.9` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000365.npy) |
| 366 | `model.layers.9` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000366.npy) |
| 367 | `model.layers.9` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 368 | `model.layers.9` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 369 | `model.layers.9` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 370 | `model.layers.9.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.28838439369249497 / 39.73857337763997 | [NPY](tensors/0000370.npy) |
| 371 | `model.layers.9.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -207.0 / 73.5 / 0.040635398788139855 / 1.7816613148406075 | [NPY](tensors/0000371.npy) |
| 372 | `model.layers.9.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -207.0 / 73.5 / 0.040635398788139855 / 1.7816613148406075 | [NPY](tensors/0000372.npy) |
| 373 | `model.layers.9.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000373.npy) |
| 374 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000374.npy) |
| 375 | `model.layers.9.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 376 | `model.layers.9.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 377 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000377.npy) |
| 378 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000378.npy) |
| 379 | `model.layers.9.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 380 | `model.layers.9.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -207.0 / 73.5 / 0.040635398788139855 / 1.7816613148406075 | [NPY](tensors/0000380.npy) |
| 381 | `model.layers.9.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -10.1875 / 20.125 / 0.061873313412659926 / 1.2984304079180657 | [NPY](tensors/0000381.npy) |
| 382 | `model.layers.9.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -207.0 / 73.5 / 0.040635398788139855 / 1.7816613148406075 | [NPY](tensors/0000382.npy) |
| 383 | `model.layers.9.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -52.25 / 44.25 / 0.04116711155950296 / 3.994317813644415 | [NPY](tensors/0000383.npy) |
| 384 | `model.layers.9.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -207.0 / 73.5 / 0.040635398788139855 / 1.7816613148406075 | [NPY](tensors/0000384.npy) |
| 385 | `model.layers.9.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -27.75 / 12.4375 / -0.005071671381876562 / 1.4696786018050507 | [NPY](tensors/0000385.npy) |
| 386 | `model.layers.9.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -11.0 / 8.8125 / 0.0038318988486475995 / 0.6738888573718321 | [NPY](tensors/0000386.npy) |
| 387 | `model.layers.9.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -348.0 / 344.0 / 0.027374318790962398 / 3.595868461757488 | [NPY](tensors/0000387.npy) |
| 388 | `model.layers.9.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -348.0 / 344.0 / 0.027374318790962398 / 3.595868461757488 | [NPY](tensors/0000388.npy) |
| 389 | `model.layers.9.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.00179839747083938 / 0.015284134208692427 | [NPY](tensors/0000389.npy) |
| 390 | `model.layers.9.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41728.0 / 1480.0 / 0.3157983894482095 / 39.70989319665051 | [NPY](tensors/0000390.npy) |
| 391 | `model.layers.9.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -64.5 / 6.75 / 0.010613746987714156 / 0.6701720792960258 | [NPY](tensors/0000391.npy) |
| 392 | `model.layers.9.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -64.5 / 6.75 / 0.010613746987714156 / 0.6701720792960258 | [NPY](tensors/0000392.npy) |
| 393 | `model.layers.9.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -64.5 / 6.75 / 0.010613746987714156 / 0.6701720792960258 | [NPY](tensors/0000393.npy) |
| 394 | `model.layers.9.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 395 | `model.layers.9.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 396 | `model.layers.9.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 397 | `model.layers.9.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -568.0 / 636.0 / 0.04085481177005429 / 5.256393928250777 | [NPY](tensors/0000397.npy) |
| 398 | `model.layers.9.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -568.0 / 636.0 / 0.04085481177005429 / 5.256393928250777 | [NPY](tensors/0000398.npy) |
| 399 | `model.layers.9.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -5.1875 / 6.40625 / -0.1339463154295497 / 0.6245472753070608 | [NPY](tensors/0000399.npy) |
| 400 | `model.layers.9` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.3566904976937834 / 40.431057087788865 | [NPY](tensors/0000400.npy) |

## Layer 0010

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 401 | `model.layers.10` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.3566904976937834 / 40.431057087788865 | [NPY](tensors/0000401.npy) |
| 402 | `model.layers.10` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000402.npy) |
| 403 | `model.layers.10` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000403.npy) |
| 404 | `model.layers.10` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000404.npy) |
| 405 | `model.layers.10` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000405.npy) |
| 406 | `model.layers.10` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 407 | `model.layers.10` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 408 | `model.layers.10` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 409 | `model.layers.10.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.3566904976937834 / 40.431057087788865 | [NPY](tensors/0000409.npy) |
| 410 | `model.layers.10.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.033882182509600296 / 1.533545828956611 | [NPY](tensors/0000410.npy) |
| 411 | `model.layers.10.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.033882182509600296 / 1.533545828956611 | [NPY](tensors/0000411.npy) |
| 412 | `model.layers.10.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000412.npy) |
| 413 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000413.npy) |
| 414 | `model.layers.10.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 415 | `model.layers.10.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 416 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000416.npy) |
| 417 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000417.npy) |
| 418 | `model.layers.10.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 419 | `model.layers.10.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.033882182509600296 / 1.533545828956611 | [NPY](tensors/0000419.npy) |
| 420 | `model.layers.10.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -16.625 / 18.5 / 0.032709312348020304 / 1.1072014104938233 | [NPY](tensors/0000420.npy) |
| 421 | `model.layers.10.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.033882182509600296 / 1.533545828956611 | [NPY](tensors/0000421.npy) |
| 422 | `model.layers.10.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -56.5 / 16.875 / -0.06076268056427543 / 2.333805933918748 | [NPY](tensors/0000422.npy) |
| 423 | `model.layers.10.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -109.0 / 50.0 / 0.033882182509600296 / 1.533545828956611 | [NPY](tensors/0000423.npy) |
| 424 | `model.layers.10.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -10.625 / 10.75 / 0.06160971011785669 / 2.1015450769882156 | [NPY](tensors/0000424.npy) |
| 425 | `model.layers.10.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -7.96875 / 8.9375 / 0.04359970999349892 / 1.0235079324221976 | [NPY](tensors/0000425.npy) |
| 426 | `model.layers.10.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -202.0 / 221.0 / 0.054305425463494254 / 4.130539516683743 | [NPY](tensors/0000426.npy) |
| 427 | `model.layers.10.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -202.0 / 221.0 / 0.054305425463494254 / 4.130539516683743 | [NPY](tensors/0000427.npy) |
| 428 | `model.layers.10.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.0014668776548563218 / 0.012892452367504055 | [NPY](tensors/0000428.npy) |
| 429 | `model.layers.10.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 924.0 / 0.4109890459174048 / 40.281689286209584 | [NPY](tensors/0000429.npy) |
| 430 | `model.layers.10.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -46.75 / 7.3125 / 0.012870174435212376 / 0.7244840472732683 | [NPY](tensors/0000430.npy) |
| 431 | `model.layers.10.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -46.75 / 7.3125 / 0.012870174435212376 / 0.7244840472732683 | [NPY](tensors/0000431.npy) |
| 432 | `model.layers.10.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -46.75 / 7.3125 / 0.012870174435212376 / 0.7244840472732683 | [NPY](tensors/0000432.npy) |
| 433 | `model.layers.10.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 434 | `model.layers.10.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 435 | `model.layers.10.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 436 | `model.layers.10.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -844.0 / 896.0 / 0.1215783447827018 / 7.438990799934559 | [NPY](tensors/0000436.npy) |
| 437 | `model.layers.10.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -844.0 / 896.0 / 0.1215783447827018 / 7.438990799934559 | [NPY](tensors/0000437.npy) |
| 438 | `model.layers.10.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -5.3125 / 4.03125 / -0.11806813427341711 / 0.628592890854775 | [NPY](tensors/0000438.npy) |
| 439 | `model.layers.10` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1048.0 / 0.532587874082207 / 42.2405651256576 | [NPY](tensors/0000439.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 440 | `model.layers.11` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1048.0 / 0.532587874082207 / 42.2405651256576 | [NPY](tensors/0000440.npy) |
| 441 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000441.npy) |
| 442 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000442.npy) |
| 443 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000443.npy) |
| 444 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000444.npy) |
| 445 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 446 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 447 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 448 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1048.0 / 0.532587874082207 / 42.2405651256576 | [NPY](tensors/0000448.npy) |
| 449 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.06970079270709362 / 3.1606605248267017 | [NPY](tensors/0000449.npy) |
| 450 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.06970079270709362 / 3.1606605248267017 | [NPY](tensors/0000450.npy) |
| 451 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000451.npy) |
| 452 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000452.npy) |
| 453 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 454 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 455 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000455.npy) |
| 456 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000456.npy) |
| 457 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 458 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.06970079270709362 / 3.1606605248267017 | [NPY](tensors/0000458.npy) |
| 459 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -13.625 / 13.3125 / 0.03898752342505405 / 1.3480858945343135 | [NPY](tensors/0000459.npy) |
| 460 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.06970079270709362 / 3.1606605248267017 | [NPY](tensors/0000460.npy) |
| 461 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -40.25 / 48.25 / 0.08576100683848858 / 3.813684490829798 | [NPY](tensors/0000461.npy) |
| 462 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -191.0 / 141.0 / 0.06970079270709362 / 3.1606605248267017 | [NPY](tensors/0000462.npy) |
| 463 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -15.875 / 22.125 / -0.03820328803459165 / 2.5026941818314445 | [NPY](tensors/0000463.npy) |
| 464 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -11.625 / 11.8125 / -0.030120355844697293 / 1.4735531900516243 | [NPY](tensors/0000464.npy) |
| 465 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -480.0 / 502.0 / -0.015752975332006678 / 6.162516630300338 | [NPY](tensors/0000465.npy) |
| 466 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -480.0 / 502.0 / -0.015752975332006678 / 6.162516630300338 | [NPY](tensors/0000466.npy) |
| 467 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.001969039656780573 / 0.014170175736758165 | [NPY](tensors/0000467.npy) |
| 468 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 700.0 / 0.5168519015535843 / 41.59487333824097 | [NPY](tensors/0000468.npy) |
| 469 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -78.5 / 7.59375 / 0.011902216545291895 / 0.777599295208428 | [NPY](tensors/0000469.npy) |
| 470 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -78.5 / 7.59375 / 0.011902216545291895 / 0.777599295208428 | [NPY](tensors/0000470.npy) |
| 471 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -78.5 / 7.59375 / 0.011902216545291895 / 0.777599295208428 | [NPY](tensors/0000471.npy) |
| 472 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 473 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 474 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 475 | `model.layers.11.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -572.0 / 460.0 / 0.11466934618149778 / 9.02865367238753 | [NPY](tensors/0000475.npy) |
| 476 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -572.0 / 460.0 / 0.11466934618149778 / 9.02865367238753 | [NPY](tensors/0000476.npy) |
| 477 | `model.layers.11.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -10.75 / 3.375 / -0.14904070277246342 / 0.7293372196085178 | [NPY](tensors/0000477.npy) |
| 478 | `model.layers.11` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 840.0 / 0.6315684565153522 / 44.359503379673356 | [NPY](tensors/0000478.npy) |

## Layer 0012

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 479 | `model.layers.12` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 840.0 / 0.6315684565153522 / 44.359503379673356 | [NPY](tensors/0000479.npy) |
| 480 | `model.layers.12` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000480.npy) |
| 481 | `model.layers.12` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000481.npy) |
| 482 | `model.layers.12` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000482.npy) |
| 483 | `model.layers.12` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000483.npy) |
| 484 | `model.layers.12` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 485 | `model.layers.12` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 486 | `model.layers.12` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 487 | `model.layers.12.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 840.0 / 0.6315684565153522 / 44.359503379673356 | [NPY](tensors/0000487.npy) |
| 488 | `model.layers.12.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -136.0 / 49.0 / 0.04252548080039541 / 1.5837621991663007 | [NPY](tensors/0000488.npy) |
| 489 | `model.layers.12.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -136.0 / 49.0 / 0.04252548080039541 / 1.5837621991663007 | [NPY](tensors/0000489.npy) |
| 490 | `model.layers.12.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000490.npy) |
| 491 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000491.npy) |
| 492 | `model.layers.12.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 493 | `model.layers.12.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 494 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000494.npy) |
| 495 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000495.npy) |
| 496 | `model.layers.12.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 497 | `model.layers.12.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -136.0 / 49.0 / 0.04252548080039541 / 1.5837621991663007 | [NPY](tensors/0000497.npy) |
| 498 | `model.layers.12.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -19.75 / 18.375 / -0.020091521435530692 / 1.3575292930327765 | [NPY](tensors/0000498.npy) |
| 499 | `model.layers.12.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -136.0 / 49.0 / 0.04252548080039541 / 1.5837621991663007 | [NPY](tensors/0000499.npy) |
| 500 | `model.layers.12.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -12.75 / 13.625 / 0.011244172893444067 / 1.32790490597433 | [NPY](tensors/0000500.npy) |
| 501 | `model.layers.12.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -136.0 / 49.0 / 0.04252548080039541 / 1.5837621991663007 | [NPY](tensors/0000501.npy) |
| 502 | `model.layers.12.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -16.0 / 19.375 / 0.02282184383618534 / 2.8842684752419374 | [NPY](tensors/0000502.npy) |
| 503 | `model.layers.12.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -10.5625 / 11.25 / 0.007414917714126585 / 1.5321710496158527 | [NPY](tensors/0000503.npy) |
| 504 | `model.layers.12.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -284.0 / 344.0 / -0.014702943267297462 / 5.776267722111166 | [NPY](tensors/0000504.npy) |
| 505 | `model.layers.12.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -284.0 / 344.0 / -0.014702943267297462 / 5.776267722111166 | [NPY](tensors/0000505.npy) |
| 506 | `model.layers.12.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 0.96875 / 0.001525639675497854 / 0.013360757120255409 | [NPY](tensors/0000506.npy) |
| 507 | `model.layers.12.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 708.0 / 0.6168615407503606 / 43.71749165907596 | [NPY](tensors/0000507.npy) |
| 508 | `model.layers.12.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -83.5 / 8.25 / 0.012585851082595587 / 0.8281579759906184 | [NPY](tensors/0000508.npy) |
| 509 | `model.layers.12.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -83.5 / 8.25 / 0.012585851082595587 / 0.8281579759906184 | [NPY](tensors/0000509.npy) |
| 510 | `model.layers.12.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -83.5 / 8.25 / 0.012585851082595587 / 0.8281579759906184 | [NPY](tensors/0000510.npy) |
| 511 | `model.layers.12.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 512 | `model.layers.12.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 513 | `model.layers.12.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 514 | `model.layers.12.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -1696.0 / 1496.0 / 0.13157872645395094 / 11.02344323564773 | [NPY](tensors/0000514.npy) |
| 515 | `model.layers.12.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -1696.0 / 1496.0 / 0.13157872645395094 / 11.02344323564773 | [NPY](tensors/0000515.npy) |
| 516 | `model.layers.12.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -6.9375 / 3.8125 / -0.1470223732511292 / 0.7476636932458235 | [NPY](tensors/0000516.npy) |
| 517 | `model.layers.12` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1808.0 / 0.748323816472138 / 47.45645084762428 | [NPY](tensors/0000517.npy) |

## Layer 0013

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 518 | `model.layers.13` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1808.0 / 0.748323816472138 / 47.45645084762428 | [NPY](tensors/0000518.npy) |
| 519 | `model.layers.13` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000519.npy) |
| 520 | `model.layers.13` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000520.npy) |
| 521 | `model.layers.13` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000521.npy) |
| 522 | `model.layers.13` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000522.npy) |
| 523 | `model.layers.13` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 524 | `model.layers.13` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 525 | `model.layers.13` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 526 | `model.layers.13.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1808.0 / 0.748323816472138 / 47.45645084762428 | [NPY](tensors/0000526.npy) |
| 527 | `model.layers.13.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -182.0 / 103.5 / 0.06736181161789434 / 2.8585114464847217 | [NPY](tensors/0000527.npy) |
| 528 | `model.layers.13.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -182.0 / 103.5 / 0.06736181161789434 / 2.8585114464847217 | [NPY](tensors/0000528.npy) |
| 529 | `model.layers.13.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000529.npy) |
| 530 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000530.npy) |
| 531 | `model.layers.13.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 532 | `model.layers.13.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 533 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000533.npy) |
| 534 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000534.npy) |
| 535 | `model.layers.13.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 536 | `model.layers.13.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -182.0 / 103.5 / 0.06736181161789434 / 2.8585114464847217 | [NPY](tensors/0000536.npy) |
| 537 | `model.layers.13.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -10.9375 / 12.5625 / 0.041098567594793245 / 1.4179838647298322 | [NPY](tensors/0000537.npy) |
| 538 | `model.layers.13.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -182.0 / 103.5 / 0.06736181161789434 / 2.8585114464847217 | [NPY](tensors/0000538.npy) |
| 539 | `model.layers.13.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -62.5 / 33.25 / -0.3347857617996486 / 4.237690923515536 | [NPY](tensors/0000539.npy) |
| 540 | `model.layers.13.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -182.0 / 103.5 / 0.06736181161789434 / 2.8585114464847217 | [NPY](tensors/0000540.npy) |
| 541 | `model.layers.13.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -16.5 / 22.5 / 0.00586032381167732 / 2.8848186387752666 | [NPY](tensors/0000541.npy) |
| 542 | `model.layers.13.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -14.3125 / 20.875 / 0.009293505822312207 / 1.6419656765086104 | [NPY](tensors/0000542.npy) |
| 543 | `model.layers.13.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -564.0 / 1176.0 / -0.04062429960244337 / 8.498843591017094 | [NPY](tensors/0000543.npy) |
| 544 | `model.layers.13.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -564.0 / 1176.0 / -0.04062429960244337 / 8.498843591017094 | [NPY](tensors/0000544.npy) |
| 545 | `model.layers.13.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002065907421192052 / 0.014039287439481324 | [NPY](tensors/0000545.npy) |
| 546 | `model.layers.13.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1296.0 / 0.7076784097074955 / 46.37074283979512 | [NPY](tensors/0000546.npy) |
| 547 | `model.layers.13.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -86.0 / 6.8125 / 0.012492301823173757 / 0.9177401013481267 | [NPY](tensors/0000547.npy) |
| 548 | `model.layers.13.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -86.0 / 6.8125 / 0.012492301823173757 / 0.9177401013481267 | [NPY](tensors/0000548.npy) |
| 549 | `model.layers.13.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -86.0 / 6.8125 / 0.012492301823173757 / 0.9177401013481267 | [NPY](tensors/0000549.npy) |
| 550 | `model.layers.13.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 551 | `model.layers.13.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 552 | `model.layers.13.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 553 | `model.layers.13.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -476.0 / 612.0 / 0.08105362292845388 / 12.634431277835532 | [NPY](tensors/0000553.npy) |
| 554 | `model.layers.13.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -476.0 / 612.0 / 0.08105362292845388 / 12.634431277835532 | [NPY](tensors/0000554.npy) |
| 555 | `model.layers.13.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -5.46875 / 3.796875 / -0.17520793458409017 / 0.8100424390059273 | [NPY](tensors/0000555.npy) |
| 556 | `model.layers.13` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1160.0 / 0.788713291494476 / 51.18721107865904 | [NPY](tensors/0000556.npy) |

## Layer 0014

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 557 | `model.layers.14` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1160.0 / 0.788713291494476 / 51.18721107865904 | [NPY](tensors/0000557.npy) |
| 558 | `model.layers.14` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000558.npy) |
| 559 | `model.layers.14` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000559.npy) |
| 560 | `model.layers.14` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000560.npy) |
| 561 | `model.layers.14` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000561.npy) |
| 562 | `model.layers.14` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 563 | `model.layers.14` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 564 | `model.layers.14` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 565 | `model.layers.14.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1160.0 / 0.788713291494476 / 51.18721107865904 | [NPY](tensors/0000565.npy) |
| 566 | `model.layers.14.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -148.0 / 51.25 / 0.05039683097091899 / 1.9379269190969288 | [NPY](tensors/0000566.npy) |
| 567 | `model.layers.14.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -148.0 / 51.25 / 0.05039683097091899 / 1.9379269190969288 | [NPY](tensors/0000567.npy) |
| 568 | `model.layers.14.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000568.npy) |
| 569 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000569.npy) |
| 570 | `model.layers.14.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 571 | `model.layers.14.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 572 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000572.npy) |
| 573 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000573.npy) |
| 574 | `model.layers.14.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 575 | `model.layers.14.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -148.0 / 51.25 / 0.05039683097091899 / 1.9379269190969288 | [NPY](tensors/0000575.npy) |
| 576 | `model.layers.14.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -53.25 / 29.25 / -0.0657657122148981 / 2.111097166023823 | [NPY](tensors/0000576.npy) |
| 577 | `model.layers.14.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -148.0 / 51.25 / 0.05039683097091899 / 1.9379269190969288 | [NPY](tensors/0000577.npy) |
| 578 | `model.layers.14.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -37.75 / 19.25 / 0.03821630256224747 / 1.6143467842552468 | [NPY](tensors/0000578.npy) |
| 579 | `model.layers.14.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -148.0 / 51.25 / 0.05039683097091899 / 1.9379269190969288 | [NPY](tensors/0000579.npy) |
| 580 | `model.layers.14.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -24.625 / 22.75 / -0.01136946782330997 / 4.753523822775004 | [NPY](tensors/0000580.npy) |
| 581 | `model.layers.14.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -22.375 / 18.875 / -0.010915142747541667 / 2.6692671083394015 | [NPY](tensors/0000581.npy) |
| 582 | `model.layers.14.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -302.0 / 334.0 / -0.023170291533698813 / 8.51466868892756 | [NPY](tensors/0000582.npy) |
| 583 | `model.layers.14.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -302.0 / 334.0 / -0.023170291533698813 / 8.51466868892756 | [NPY](tensors/0000583.npy) |
| 584 | `model.layers.14.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 0.9765625 / 0.0014816707015915082 / 0.015546933088547552 | [NPY](tensors/0000584.npy) |
| 585 | `model.layers.14.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.765548015950406 / 50.34351097028135 | [NPY](tensors/0000585.npy) |
| 586 | `model.layers.14.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -99.0 / 9.6875 / 0.013698311762639925 / 0.9906028705104487 | [NPY](tensors/0000586.npy) |
| 587 | `model.layers.14.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -99.0 / 9.6875 / 0.013698311762639925 / 0.9906028705104487 | [NPY](tensors/0000587.npy) |
| 588 | `model.layers.14.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -99.0 / 9.6875 / 0.013698311762639925 / 0.9906028705104487 | [NPY](tensors/0000588.npy) |
| 589 | `model.layers.14.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 590 | `model.layers.14.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 591 | `model.layers.14.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 592 | `model.layers.14.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -1296.0 / 1136.0 / 0.0553553968137268 / 17.0930004023721 | [NPY](tensors/0000592.npy) |
| 593 | `model.layers.14.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -1296.0 / 1136.0 / 0.0553553968137268 / 17.0930004023721 | [NPY](tensors/0000593.npy) |
| 594 | `model.layers.14.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -6.84375 / 6.53125 / -0.24219687636226886 / 0.7779168944104947 | [NPY](tensors/0000594.npy) |
| 595 | `model.layers.14` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 2032.0 / 0.8209114162731146 / 58.031576514035855 | [NPY](tensors/0000595.npy) |

## Layer 0015

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 596 | `model.layers.15` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 2032.0 / 0.8209114162731146 / 58.031576514035855 | [NPY](tensors/0000596.npy) |
| 597 | `model.layers.15` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000597.npy) |
| 598 | `model.layers.15` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000598.npy) |
| 599 | `model.layers.15` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000599.npy) |
| 600 | `model.layers.15` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000600.npy) |
| 601 | `model.layers.15` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 602 | `model.layers.15` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 603 | `model.layers.15` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 604 | `model.layers.15.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 2032.0 / 0.8209114162731146 / 58.031576514035855 | [NPY](tensors/0000604.npy) |
| 605 | `model.layers.15.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -164.0 / 67.5 / 0.050850745834875505 / 2.1689007414602877 | [NPY](tensors/0000605.npy) |
| 606 | `model.layers.15.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -164.0 / 67.5 / 0.050850745834875505 / 2.1689007414602877 | [NPY](tensors/0000606.npy) |
| 607 | `model.layers.15.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000607.npy) |
| 608 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000608.npy) |
| 609 | `model.layers.15.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 610 | `model.layers.15.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 611 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000611.npy) |
| 612 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000612.npy) |
| 613 | `model.layers.15.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 614 | `model.layers.15.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -164.0 / 67.5 / 0.050850745834875505 / 2.1689007414602877 | [NPY](tensors/0000614.npy) |
| 615 | `model.layers.15.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -21.25 / 19.875 / 0.013250044343787303 / 1.4678223491812743 | [NPY](tensors/0000615.npy) |
| 616 | `model.layers.15.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -164.0 / 67.5 / 0.050850745834875505 / 2.1689007414602877 | [NPY](tensors/0000616.npy) |
| 617 | `model.layers.15.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -41.25 / 52.25 / 0.04106381991842675 / 4.210615351908948 | [NPY](tensors/0000617.npy) |
| 618 | `model.layers.15.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -164.0 / 67.5 / 0.050850745834875505 / 2.1689007414602877 | [NPY](tensors/0000618.npy) |
| 619 | `model.layers.15.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -61.5 / 38.5 / -0.13120634066801345 / 2.8883368748629747 | [NPY](tensors/0000619.npy) |
| 620 | `model.layers.15.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -14.6875 / 20.5 / -0.1056914833237137 / 1.5077700582391647 | [NPY](tensors/0000620.npy) |
| 621 | `model.layers.15.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -1696.0 / 1720.0 / 0.05072701621475037 / 13.128948457062595 | [NPY](tensors/0000621.npy) |
| 622 | `model.layers.15.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -1696.0 / 1720.0 / 0.05072701621475037 / 13.128948457062595 | [NPY](tensors/0000622.npy) |
| 623 | `model.layers.15.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0017466871921614404 / 0.013893810250744432 | [NPY](tensors/0000623.npy) |
| 624 | `model.layers.15.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1160.0 / 0.8715607841420899 / 56.94557259364381 | [NPY](tensors/0000624.npy) |
| 625 | `model.layers.15.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -106.0 / 9.6875 / 0.016098438613518513 / 1.0081181432698858 | [NPY](tensors/0000625.npy) |
| 626 | `model.layers.15.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -106.0 / 9.6875 / 0.016098438613518513 / 1.0081181432698858 | [NPY](tensors/0000626.npy) |
| 627 | `model.layers.15.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -106.0 / 9.6875 / 0.016098438613518513 / 1.0081181432698858 | [NPY](tensors/0000627.npy) |
| 628 | `model.layers.15.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 629 | `model.layers.15.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 630 | `model.layers.15.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 631 | `model.layers.15.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -780.0 / 724.0 / -0.17004958454875502 / 20.45610033849015 | [NPY](tensors/0000631.npy) |
| 632 | `model.layers.15.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -780.0 / 724.0 / -0.17004958454875502 / 20.45610033849015 | [NPY](tensors/0000632.npy) |
| 633 | `model.layers.15.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -6.1875 / 5.09375 / -0.2624664155947166 / 0.9520558779342397 | [NPY](tensors/0000633.npy) |
| 634 | `model.layers.15` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1456.0 / 0.7015618231710946 / 66.439420520902 | [NPY](tensors/0000634.npy) |

## Layer 0016

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 635 | `model.layers.16` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1456.0 / 0.7015618231710946 / 66.439420520902 | [NPY](tensors/0000635.npy) |
| 636 | `model.layers.16` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000636.npy) |
| 637 | `model.layers.16` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000637.npy) |
| 638 | `model.layers.16` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000638.npy) |
| 639 | `model.layers.16` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000639.npy) |
| 640 | `model.layers.16` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 641 | `model.layers.16` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 642 | `model.layers.16` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 643 | `model.layers.16.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1456.0 / 0.7015618231710946 / 66.439420520902 | [NPY](tensors/0000643.npy) |
| 644 | `model.layers.16.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -131.0 / 51.25 / 0.0384496695856074 / 1.9025410601531645 | [NPY](tensors/0000644.npy) |
| 645 | `model.layers.16.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -131.0 / 51.25 / 0.0384496695856074 / 1.9025410601531645 | [NPY](tensors/0000645.npy) |
| 646 | `model.layers.16.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000646.npy) |
| 647 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000647.npy) |
| 648 | `model.layers.16.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 649 | `model.layers.16.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 650 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000650.npy) |
| 651 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000651.npy) |
| 652 | `model.layers.16.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 653 | `model.layers.16.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -131.0 / 51.25 / 0.0384496695856074 / 1.9025410601531645 | [NPY](tensors/0000653.npy) |
| 654 | `model.layers.16.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -25.25 / 26.0 / 0.030661356711417675 / 1.718751353394043 | [NPY](tensors/0000654.npy) |
| 655 | `model.layers.16.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -131.0 / 51.25 / 0.0384496695856074 / 1.9025410601531645 | [NPY](tensors/0000655.npy) |
| 656 | `model.layers.16.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -14.875 / 32.25 / 0.0434081809250383 / 1.6204751186362858 | [NPY](tensors/0000656.npy) |
| 657 | `model.layers.16.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -131.0 / 51.25 / 0.0384496695856074 / 1.9025410601531645 | [NPY](tensors/0000657.npy) |
| 658 | `model.layers.16.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -22.625 / 22.625 / -0.004306191849705192 / 4.412229090150769 | [NPY](tensors/0000658.npy) |
| 659 | `model.layers.16.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -20.75 / 20.125 / -0.011034710851179165 / 2.0102874643790933 | [NPY](tensors/0000659.npy) |
| 660 | `model.layers.16.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -544.0 / 548.0 / 0.022561565843689464 / 13.360447417629093 | [NPY](tensors/0000660.npy) |
| 661 | `model.layers.16.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -544.0 / 548.0 / 0.022561565843689464 / 13.360447417629093 | [NPY](tensors/0000661.npy) |
| 662 | `model.layers.16.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 0.94921875 / 0.001223169749566641 / 0.013065472835060103 | [NPY](tensors/0000662.npy) |
| 663 | `model.layers.16.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1536.0 / 0.724151850237056 / 66.7389756910608 | [NPY](tensors/0000663.npy) |
| 664 | `model.layers.16.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -68.0 / 10.0 / 0.014567837556195732 / 0.9734644764961841 | [NPY](tensors/0000664.npy) |
| 665 | `model.layers.16.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -68.0 / 10.0 / 0.014567837556195732 / 0.9734644764961841 | [NPY](tensors/0000665.npy) |
| 666 | `model.layers.16.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -68.0 / 10.0 / 0.014567837556195732 / 0.9734644764961841 | [NPY](tensors/0000666.npy) |
| 667 | `model.layers.16.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 668 | `model.layers.16.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 669 | `model.layers.16.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 670 | `model.layers.16.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -2400.0 / 1736.0 / -0.16644864143630392 / 29.346240372732964 | [NPY](tensors/0000670.npy) |
| 671 | `model.layers.16.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -2400.0 / 1736.0 / -0.16644864143630392 / 29.346240372732964 | [NPY](tensors/0000671.npy) |
| 672 | `model.layers.16.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -6.34375 / 4.46875 / -0.2957208312661061 / 1.2513116765720185 | [NPY](tensors/0000672.npy) |
| 673 | `model.layers.16` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 2656.0 / 0.5578811951678649 / 83.73973248637934 | [NPY](tensors/0000673.npy) |

## Layer 0017

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 674 | `model.layers.17` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 2656.0 / 0.5578811951678649 / 83.73973248637934 | [NPY](tensors/0000674.npy) |
| 675 | `model.layers.17` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000675.npy) |
| 676 | `model.layers.17` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000676.npy) |
| 677 | `model.layers.17` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000677.npy) |
| 678 | `model.layers.17` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000678.npy) |
| 679 | `model.layers.17` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 680 | `model.layers.17` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 681 | `model.layers.17` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 682 | `model.layers.17.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 2656.0 / 0.5578811951678649 / 83.73973248637934 | [NPY](tensors/0000682.npy) |
| 683 | `model.layers.17.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04679745418653322 / 2.696366308534823 | [NPY](tensors/0000683.npy) |
| 684 | `model.layers.17.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04679745418653322 / 2.696366308534823 | [NPY](tensors/0000684.npy) |
| 685 | `model.layers.17.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000685.npy) |
| 686 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000686.npy) |
| 687 | `model.layers.17.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 688 | `model.layers.17.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 689 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000689.npy) |
| 690 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000690.npy) |
| 691 | `model.layers.17.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 692 | `model.layers.17.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04679745418653322 / 2.696366308534823 | [NPY](tensors/0000692.npy) |
| 693 | `model.layers.17.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -22.5 / 28.0 / 0.01391911015720526 / 1.6298761636406538 | [NPY](tensors/0000693.npy) |
| 694 | `model.layers.17.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04679745418653322 / 2.696366308534823 | [NPY](tensors/0000694.npy) |
| 695 | `model.layers.17.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -67.5 / 44.75 / 0.0116198664497212 / 5.207528284860493 | [NPY](tensors/0000695.npy) |
| 696 | `model.layers.17.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04679745418653322 / 2.696366308534823 | [NPY](tensors/0000696.npy) |
| 697 | `model.layers.17.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -19.5 / 21.875 / 0.12155740385198162 / 3.0898657157300033 | [NPY](tensors/0000697.npy) |
| 698 | `model.layers.17.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -10.0625 / 11.0 / 0.0751397651548969 / 1.348567736551878 | [NPY](tensors/0000698.npy) |
| 699 | `model.layers.17.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -1520.0 / 1568.0 / 0.24085245877410913 / 20.16751662497077 | [NPY](tensors/0000699.npy) |
| 700 | `model.layers.17.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -1520.0 / 1568.0 / 0.24085245877410913 / 20.16751662497077 | [NPY](tensors/0000700.npy) |
| 701 | `model.layers.17.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.0017697161996288974 / 0.01592243390000583 | [NPY](tensors/0000701.npy) |
| 702 | `model.layers.17.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41216.0 / 1872.0 / 0.7987638919611217 / 81.11903268359038 | [NPY](tensors/0000702.npy) |
| 703 | `model.layers.17.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -41.75 / 10.5 / 0.012200735853847134 / 0.955834824345864 | [NPY](tensors/0000703.npy) |
| 704 | `model.layers.17.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41.75 / 10.5 / 0.012200735853847134 / 0.955834824345864 | [NPY](tensors/0000704.npy) |
| 705 | `model.layers.17.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -41.75 / 10.5 / 0.012200735853847134 / 0.955834824345864 | [NPY](tensors/0000705.npy) |
| 706 | `model.layers.17.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 707 | `model.layers.17.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 708 | `model.layers.17.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 709 | `model.layers.17.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -1160.0 / 40448.0 / -0.07084934850189958 / 50.55192621303958 | [NPY](tensors/0000709.npy) |
| 710 | `model.layers.17.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -1160.0 / 40448.0 / -0.07084934850189958 / 50.55192621303958 | [NPY](tensors/0000710.npy) |
| 711 | `model.layers.17.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -4.9375 / 2.953125 / -0.19627300665017983 / 0.9663348018962046 | [NPY](tensors/0000711.npy) |
| 712 | `model.layers.17` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -2432.0 / 2496.0 / 0.7279583996269736 / 95.55839302969488 | [NPY](tensors/0000712.npy) |

## Layer 0018

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 713 | `model.layers.18` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -2432.0 / 2496.0 / 0.7279583996269736 / 95.55839302969488 | [NPY](tensors/0000713.npy) |
| 714 | `model.layers.18` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000714.npy) |
| 715 | `model.layers.18` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000715.npy) |
| 716 | `model.layers.18` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000716.npy) |
| 717 | `model.layers.18` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000717.npy) |
| 718 | `model.layers.18` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 719 | `model.layers.18` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 720 | `model.layers.18` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 721 | `model.layers.18.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -2432.0 / 2496.0 / 0.7279583996269736 / 95.55839302969488 | [NPY](tensors/0000721.npy) |
| 722 | `model.layers.18.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -45.5 / 39.25 / 0.02421393085926106 / 1.6003866790697665 | [NPY](tensors/0000722.npy) |
| 723 | `model.layers.18.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -45.5 / 39.25 / 0.02421393085926106 / 1.6003866790697665 | [NPY](tensors/0000723.npy) |
| 724 | `model.layers.18.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000724.npy) |
| 725 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000725.npy) |
| 726 | `model.layers.18.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 727 | `model.layers.18.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 728 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000728.npy) |
| 729 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000729.npy) |
| 730 | `model.layers.18.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 731 | `model.layers.18.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -45.5 / 39.25 / 0.02421393085926106 / 1.6003866790697665 | [NPY](tensors/0000731.npy) |
| 732 | `model.layers.18.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -26.625 / 32.75 / 0.11962756854330725 / 1.8716789777859864 | [NPY](tensors/0000732.npy) |
| 733 | `model.layers.18.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -45.5 / 39.25 / 0.02421393085926106 / 1.6003866790697665 | [NPY](tensors/0000733.npy) |
| 734 | `model.layers.18.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -18.75 / 51.5 / 0.11910963206970196 / 2.2675206959816046 | [NPY](tensors/0000734.npy) |
| 735 | `model.layers.18.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -45.5 / 39.25 / 0.02421393085926106 / 1.6003866790697665 | [NPY](tensors/0000735.npy) |
| 736 | `model.layers.18.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -26.125 / 23.375 / -0.22695257980980896 / 4.354369053022281 | [NPY](tensors/0000736.npy) |
| 737 | `model.layers.18.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -20.875 / 20.125 / -0.11465701276892501 / 1.9568149495676197 | [NPY](tensors/0000737.npy) |
| 738 | `model.layers.18.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -604.0 / 748.0 / -0.2448075731206664 / 21.760898599243344 | [NPY](tensors/0000738.npy) |
| 739 | `model.layers.18.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -604.0 / 748.0 / -0.2448075731206664 / 21.760898599243344 | [NPY](tensors/0000739.npy) |
| 740 | `model.layers.18.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.001086823308944367 / 0.01440482018352155 | [NPY](tensors/0000740.npy) |
| 741 | `model.layers.18.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -2400.0 / 2448.0 / 0.4831376630230778 / 102.27085323608706 | [NPY](tensors/0000741.npy) |
| 742 | `model.layers.18.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -7.78125 / 14.0625 / 0.006494656433768294 / 0.9195462786340175 | [NPY](tensors/0000742.npy) |
| 743 | `model.layers.18.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -7.78125 / 14.0625 / 0.006494656433768294 / 0.9195462786340175 | [NPY](tensors/0000743.npy) |
| 744 | `model.layers.18.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -7.78125 / 14.0625 / 0.006494656433768294 / 0.9195462786340175 | [NPY](tensors/0000744.npy) |
| 745 | `model.layers.18.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 746 | `model.layers.18.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 747 | `model.layers.18.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 748 | `model.layers.18.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -2112.0 / 2832.0 / 0.12744459997061833 / 52.251707039817155 | [NPY](tensors/0000748.npy) |
| 749 | `model.layers.18.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -2112.0 / 2832.0 / 0.12744459997061833 / 52.251707039817155 | [NPY](tensors/0000749.npy) |
| 750 | `model.layers.18.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -5.1875 / 2.640625 / -0.32562031326121726 / 1.0659914965941644 | [NPY](tensors/0000750.npy) |
| 751 | `model.layers.18` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.6109825315109494 / 137.9260215928651 | [NPY](tensors/0000751.npy) |

## Layer 0019

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 752 | `model.layers.19` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.6109825315109494 / 137.9260215928651 | [NPY](tensors/0000752.npy) |
| 753 | `model.layers.19` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000753.npy) |
| 754 | `model.layers.19` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000754.npy) |
| 755 | `model.layers.19` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000755.npy) |
| 756 | `model.layers.19` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000756.npy) |
| 757 | `model.layers.19` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 758 | `model.layers.19` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 759 | `model.layers.19` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 760 | `model.layers.19.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.6109825315109494 / 137.9260215928651 | [NPY](tensors/0000760.npy) |
| 761 | `model.layers.19.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.015902661495349867 / 1.8256218947155192 | [NPY](tensors/0000761.npy) |
| 762 | `model.layers.19.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.015902661495349867 / 1.8256218947155192 | [NPY](tensors/0000762.npy) |
| 763 | `model.layers.19.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000763.npy) |
| 764 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000764.npy) |
| 765 | `model.layers.19.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 766 | `model.layers.19.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 767 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000767.npy) |
| 768 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000768.npy) |
| 769 | `model.layers.19.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 770 | `model.layers.19.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.015902661495349867 / 1.8256218947155192 | [NPY](tensors/0000770.npy) |
| 771 | `model.layers.19.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -16.25 / 24.5 / -0.03301115865221576 / 1.3223823932821788 | [NPY](tensors/0000771.npy) |
| 772 | `model.layers.19.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.015902661495349867 / 1.8256218947155192 | [NPY](tensors/0000772.npy) |
| 773 | `model.layers.19.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -85.0 / 71.0 / -0.08730227901780574 / 7.391859247786513 | [NPY](tensors/0000773.npy) |
| 774 | `model.layers.19.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.015902661495349867 / 1.8256218947155192 | [NPY](tensors/0000774.npy) |
| 775 | `model.layers.19.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -16.0 / 20.125 / -0.025174469384575016 / 3.190961232843655 | [NPY](tensors/0000775.npy) |
| 776 | `model.layers.19.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -12.1875 / 11.375 / -0.008930310213556909 / 1.0630916075261605 | [NPY](tensors/0000776.npy) |
| 777 | `model.layers.19.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -2144.0 / 1912.0 / -0.510504212332663 / 42.96440816054006 | [NPY](tensors/0000777.npy) |
| 778 | `model.layers.19.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -2144.0 / 1912.0 / -0.510504212332663 / 42.96440816054006 | [NPY](tensors/0000778.npy) |
| 779 | `model.layers.19.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.0010113462848010926 / 0.00885024183455766 | [NPY](tensors/0000779.npy) |
| 780 | `model.layers.19.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -3616.0 / 3344.0 / 0.10057480823793355 / 122.81988441855736 | [NPY](tensors/0000780.npy) |
| 781 | `model.layers.19.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -7.09375 / 20.625 / 0.004957680716075364 / 1.0189987097656614 | [NPY](tensors/0000781.npy) |
| 782 | `model.layers.19.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -7.09375 / 20.625 / 0.004957680716075364 / 1.0189987097656614 | [NPY](tensors/0000782.npy) |
| 783 | `model.layers.19.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -7.09375 / 20.625 / 0.004957680716075364 / 1.0189987097656614 | [NPY](tensors/0000783.npy) |
| 784 | `model.layers.19.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 785 | `model.layers.19.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 786 | `model.layers.19.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 787 | `model.layers.19.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -2560.0 / 2832.0 / 0.2885912959807972 / 85.71047045332782 | [NPY](tensors/0000787.npy) |
| 788 | `model.layers.19.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -2560.0 / 2832.0 / 0.2885912959807972 / 85.71047045332782 | [NPY](tensors/0000788.npy) |
| 789 | `model.layers.19.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -8.8125 / 3.09375 / -0.2889397838583918 / 1.5729405923136877 | [NPY](tensors/0000789.npy) |
| 790 | `model.layers.19` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -4992.0 / 4800.0 / 0.3889156506119559 / 181.6466568610634 | [NPY](tensors/0000790.npy) |

## Layer 0020

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 791 | `model.layers.20` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -4992.0 / 4800.0 / 0.3889156506119559 / 181.6466568610634 | [NPY](tensors/0000791.npy) |
| 792 | `model.layers.20` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000792.npy) |
| 793 | `model.layers.20` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000793.npy) |
| 794 | `model.layers.20` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000794.npy) |
| 795 | `model.layers.20` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000795.npy) |
| 796 | `model.layers.20` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 797 | `model.layers.20` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 798 | `model.layers.20` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 799 | `model.layers.20.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -4992.0 / 4800.0 / 0.3889156506119559 / 181.6466568610634 | [NPY](tensors/0000799.npy) |
| 800 | `model.layers.20.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.011795070963991832 / 1.541926256195269 | [NPY](tensors/0000800.npy) |
| 801 | `model.layers.20.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.011795070963991832 / 1.541926256195269 | [NPY](tensors/0000801.npy) |
| 802 | `model.layers.20.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000802.npy) |
| 803 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000803.npy) |
| 804 | `model.layers.20.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 805 | `model.layers.20.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 806 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000806.npy) |
| 807 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000807.npy) |
| 808 | `model.layers.20.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 809 | `model.layers.20.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.011795070963991832 / 1.541926256195269 | [NPY](tensors/0000809.npy) |
| 810 | `model.layers.20.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -23.0 / 20.625 / 0.042735870626704024 / 1.2601064085628744 | [NPY](tensors/0000810.npy) |
| 811 | `model.layers.20.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.011795070963991832 / 1.541926256195269 | [NPY](tensors/0000811.npy) |
| 812 | `model.layers.20.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -29.625 / 37.0 / -0.09421299528498749 / 2.2419028024206873 | [NPY](tensors/0000812.npy) |
| 813 | `model.layers.20.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.011795070963991832 / 1.541926256195269 | [NPY](tensors/0000813.npy) |
| 814 | `model.layers.20.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -22.375 / 21.25 / 0.02344111977597072 / 3.933185452993307 | [NPY](tensors/0000814.npy) |
| 815 | `model.layers.20.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -17.375 / 16.875 / -0.002024035409189541 / 1.3138323103238858 | [NPY](tensors/0000815.npy) |
| 816 | `model.layers.20.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -1160.0 / 1104.0 / -0.25174838487261636 / 26.60161790036449 | [NPY](tensors/0000816.npy) |
| 817 | `model.layers.20.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -1160.0 / 1104.0 / -0.25174838487261636 / 26.60161790036449 | [NPY](tensors/0000817.npy) |
| 818 | `model.layers.20.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0008842880867589379 / 0.011882638407915178 | [NPY](tensors/0000818.npy) |
| 819 | `model.layers.20.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -4864.0 / 4928.0 / 0.13690732234039193 / 183.31420245501462 | [NPY](tensors/0000819.npy) |
| 820 | `model.layers.20.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -6.96875 / 20.125 / 0.0026327618681116754 / 0.979490246806011 | [NPY](tensors/0000820.npy) |
| 821 | `model.layers.20.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -6.96875 / 20.125 / 0.0026327618681116754 / 0.979490246806011 | [NPY](tensors/0000821.npy) |
| 822 | `model.layers.20.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -6.96875 / 20.125 / 0.0026327618681116754 / 0.979490246806011 | [NPY](tensors/0000822.npy) |
| 823 | `model.layers.20.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 824 | `model.layers.20.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 825 | `model.layers.20.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 826 | `model.layers.20.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -5888.0 / 6848.0 / 0.34650745083282913 / 80.82954807167903 | [NPY](tensors/0000826.npy) |
| 827 | `model.layers.20.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -5888.0 / 6848.0 / 0.34650745083282913 / 80.82954807167903 | [NPY](tensors/0000827.npy) |
| 828 | `model.layers.20.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -6.0 / 4.09375 / -0.19057496944883875 / 1.299861432966489 | [NPY](tensors/0000828.npy) |
| 829 | `model.layers.20` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -9216.0 / 10368.0 / 0.4838798071347234 / 240.66985434410427 | [NPY](tensors/0000829.npy) |

## Layer 0021

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 830 | `model.layers.21` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -9216.0 / 10368.0 / 0.4838798071347234 / 240.66985434410427 | [NPY](tensors/0000830.npy) |
| 831 | `model.layers.21` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000831.npy) |
| 832 | `model.layers.21` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000832.npy) |
| 833 | `model.layers.21` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000833.npy) |
| 834 | `model.layers.21` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000834.npy) |
| 835 | `model.layers.21` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 836 | `model.layers.21` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 837 | `model.layers.21` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 838 | `model.layers.21.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -9216.0 / 10368.0 / 0.4838798071347234 / 240.66985434410427 | [NPY](tensors/0000838.npy) |
| 839 | `model.layers.21.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.00706486035823254 / 1.8017968018243984 | [NPY](tensors/0000839.npy) |
| 840 | `model.layers.21.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.00706486035823254 / 1.8017968018243984 | [NPY](tensors/0000840.npy) |
| 841 | `model.layers.21.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000841.npy) |
| 842 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000842.npy) |
| 843 | `model.layers.21.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 844 | `model.layers.21.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 845 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000845.npy) |
| 846 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000846.npy) |
| 847 | `model.layers.21.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 848 | `model.layers.21.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.00706486035823254 / 1.8017968018243984 | [NPY](tensors/0000848.npy) |
| 849 | `model.layers.21.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -20.25 / 39.5 / 0.023010540727829175 / 1.1818940177366746 | [NPY](tensors/0000849.npy) |
| 850 | `model.layers.21.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.00706486035823254 / 1.8017968018243984 | [NPY](tensors/0000850.npy) |
| 851 | `model.layers.21.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -101.0 / 100.0 / -0.18742688874995656 / 8.217481097921974 | [NPY](tensors/0000851.npy) |
| 852 | `model.layers.21.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -75.0 / 63.5 / 0.00706486035823254 / 1.8017968018243984 | [NPY](tensors/0000852.npy) |
| 853 | `model.layers.21.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -21.375 / 24.0 / -0.009635815257495628 / 3.1602315623688364 | [NPY](tensors/0000853.npy) |
| 854 | `model.layers.21.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -16.875 / 13.5625 / 0.0028280461221633396 / 0.7825556891817419 | [NPY](tensors/0000854.npy) |
| 855 | `model.layers.21.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -5152.0 / 4672.0 / -0.654180498857351 / 78.24894779440736 | [NPY](tensors/0000855.npy) |
| 856 | `model.layers.21.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -5152.0 / 4672.0 / -0.654180498857351 / 78.24894779440736 | [NPY](tensors/0000856.npy) |
| 857 | `model.layers.21.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 0.94921875 / 0.0009395434635386482 / 0.006346026162843808 | [NPY](tensors/0000857.npy) |
| 858 | `model.layers.21.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -5920.0 / 6112.0 / -0.1702693599550713 / 200.82428625709463 | [NPY](tensors/0000858.npy) |
| 859 | `model.layers.21.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -8.8125 / 28.25 / 0.00217735079395792 / 1.1002922797749783 | [NPY](tensors/0000859.npy) |
| 860 | `model.layers.21.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -8.8125 / 28.25 / 0.00217735079395792 / 1.1002922797749783 | [NPY](tensors/0000860.npy) |
| 861 | `model.layers.21.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -8.8125 / 28.25 / 0.00217735079395792 / 1.1002922797749783 | [NPY](tensors/0000861.npy) |
| 862 | `model.layers.21.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 863 | `model.layers.21.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 864 | `model.layers.21.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 865 | `model.layers.21.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -5792.0 / 5696.0 / -0.9735383857902142 / 151.8754569424404 | [NPY](tensors/0000865.npy) |
| 866 | `model.layers.21.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -5792.0 / 5696.0 / -0.9735383857902142 / 151.8754569424404 | [NPY](tensors/0000866.npy) |
| 867 | `model.layers.21.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -6.5625 / 4.375 / -0.23527525563810534 / 1.6338262548321527 | [NPY](tensors/0000867.npy) |
| 868 | `model.layers.21` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -9216.0 / 9728.0 / -1.1440024615829083 / 306.9373655660351 | [NPY](tensors/0000868.npy) |

## Layer 0022

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 869 | `model.layers.22` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -9216.0 / 9728.0 / -1.1440024615829083 / 306.9373655660351 | [NPY](tensors/0000869.npy) |
| 870 | `model.layers.22` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000870.npy) |
| 871 | `model.layers.22` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000871.npy) |
| 872 | `model.layers.22` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000872.npy) |
| 873 | `model.layers.22` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000873.npy) |
| 874 | `model.layers.22` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 875 | `model.layers.22` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 876 | `model.layers.22` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 877 | `model.layers.22.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -9216.0 / 9728.0 / -1.1440024615829083 / 306.9373655660351 | [NPY](tensors/0000877.npy) |
| 878 | `model.layers.22.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -44.5 / 49.0 / 0.0009954867106662646 / 1.7341869711558358 | [NPY](tensors/0000878.npy) |
| 879 | `model.layers.22.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -44.5 / 49.0 / 0.0009954867106662646 / 1.7341869711558358 | [NPY](tensors/0000879.npy) |
| 880 | `model.layers.22.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.550546850404038e+38 / 1.4628292357945166e+38 | [NPY](tensors/0000880.npy) |
| 881 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000881.npy) |
| 882 | `model.layers.22.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 883 | `model.layers.22.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 884 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000884.npy) |
| 885 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000885.npy) |
| 886 | `model.layers.22.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 887 | `model.layers.22.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -44.5 / 49.0 / 0.0009954867106662646 / 1.7341869711558358 | [NPY](tensors/0000887.npy) |
| 888 | `model.layers.22.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -40.0 / 34.0 / -0.05197595554631043 / 2.4830758115767817 | [NPY](tensors/0000888.npy) |
| 889 | `model.layers.22.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -44.5 / 49.0 / 0.0009954867106662646 / 1.7341869711558358 | [NPY](tensors/0000889.npy) |
| 890 | `model.layers.22.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -32.5 / 8.9375 / -0.05248195915628786 / 1.3620975028529638 | [NPY](tensors/0000890.npy) |
| 891 | `model.layers.22.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -44.5 / 49.0 / 0.0009954867106662646 / 1.7341869711558358 | [NPY](tensors/0000891.npy) |
| 892 | `model.layers.22.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -28.25 / 29.375 / 0.02159268783014394 / 4.417008315053411 | [NPY](tensors/0000892.npy) |
| 893 | `model.layers.22.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -19.875 / 16.0 / -0.006090121593397414 / 1.4920202298982108 | [NPY](tensors/0000893.npy) |
| 894 | `model.layers.22.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -2272.0 / 2016.0 / -0.39793703970206185 / 40.987709515223195 | [NPY](tensors/0000894.npy) |
| 895 | `model.layers.22.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -2272.0 / 2016.0 / -0.39793703970206185 / 40.987709515223195 | [NPY](tensors/0000895.npy) |
| 896 | `model.layers.22.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 0.93359375 / 0.000886571047908439 / 0.011756056994010784 | [NPY](tensors/0000896.npy) |
| 897 | `model.layers.22.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -9920.0 / 10368.0 / -1.542623881466083 / 314.2105726361964 | [NPY](tensors/0000897.npy) |
| 898 | `model.layers.22.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -20.25 / 21.5 / -0.0065344158489026305 / 1.0039170055825963 | [NPY](tensors/0000898.npy) |
| 899 | `model.layers.22.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -20.25 / 21.5 / -0.0065344158489026305 / 1.0039170055825963 | [NPY](tensors/0000899.npy) |
| 900 | `model.layers.22.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -20.25 / 21.5 / -0.0065344158489026305 / 1.0039170055825963 | [NPY](tensors/0000900.npy) |
| 901 | `model.layers.22.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 902 | `model.layers.22.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 903 | `model.layers.22.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 904 | `model.layers.22.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -6656.0 / 6368.0 / 0.04473868800728488 / 150.2546564119732 | [NPY](tensors/0000904.npy) |
| 905 | `model.layers.22.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -6656.0 / 6368.0 / 0.04473868800728488 / 150.2546564119732 | [NPY](tensors/0000905.npy) |
| 906 | `model.layers.22.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -7.75 / 4.75 / -0.1938450363365845 / 1.5152966340971228 | [NPY](tensors/0000906.npy) |
| 907 | `model.layers.22` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.49686315348491 / 401.5666770010688 | [NPY](tensors/0000907.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 908 | `model.layers.23` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.49686315348491 / 401.5666770010688 | [NPY](tensors/0000908.npy) |
| 909 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000909.npy) |
| 910 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000910.npy) |
| 911 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000911.npy) |
| 912 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000912.npy) |
| 913 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 914 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 915 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 916 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.49686315348491 / 401.5666770010688 | [NPY](tensors/0000916.npy) |
| 917 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009455468299127565 / 1.7547421892438961 | [NPY](tensors/0000917.npy) |
| 918 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 443, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009455468299127565 / 1.7547421892438961 | [NPY](tensors/0000918.npy) |
| 919 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 443, 443] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6909400384302243e+38 / 1.694761376723884e+38 | [NPY](tensors/0000919.npy) |
| 920 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 443] | torch.int64 → int64 | 0.0 / 442.0 / 221.0 / 127.88275880665071 | [NPY](tensors/0000920.npy) |
| 921 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 922 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 923 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7744658824821627 / 0.8882062578587617 | [NPY](tensors/0000923.npy) |
| 924 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 443, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11284811299545985 / 0.6388208477044731 | [NPY](tensors/0000924.npy) |
| 925 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 926 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009455468299127565 / 1.7547421892438961 | [NPY](tensors/0000926.npy) |
| 927 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 443, 4096] | torch.bfloat16 → float32 | -20.75 / 25.125 / 0.03176870780108293 / 1.6615154090640434 | [NPY](tensors/0000927.npy) |
| 928 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009455468299127565 / 1.7547421892438961 | [NPY](tensors/0000928.npy) |
| 929 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -87.0 / 69.5 / -0.06675139695145012 / 5.183015483483847 | [NPY](tensors/0000929.npy) |
| 930 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -52.5 / 72.0 / 0.009455468299127565 / 1.7547421892438961 | [NPY](tensors/0000930.npy) |
| 931 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 443, 512] | torch.bfloat16 → float32 | -28.875 / 24.125 / 0.015922203177531537 / 3.1920096800019215 | [NPY](tensors/0000931.npy) |
| 932 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 443, 4096] | torch.bfloat16 → float32 | -26.625 / 13.875 / -0.0007060900984110928 / 1.1617462775683813 | [NPY](tensors/0000932.npy) |
| 933 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -6496.0 / 6944.0 / 2.382711439672227 / 163.15614481244916 | [NPY](tensors/0000933.npy) |
| 934 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -6496.0 / 6944.0 / 2.382711439672227 / 163.15614481244916 | [NPY](tensors/0000934.npy) |
| 935 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 443, 443] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0011705050453951415 / 0.01015843775113095 | [NPY](tensors/0000935.npy) |
| 936 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -11328.0 / 11264.0 / 0.8862935254470372 / 361.2847556792391 | [NPY](tensors/0000936.npy) |
| 937 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -52.5 / 24.875 / -0.015501749463583073 / 1.275053132745384 | [NPY](tensors/0000937.npy) |
| 938 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -52.5 / 24.875 / -0.015501749463583073 / 1.275053132745384 | [NPY](tensors/0000938.npy) |
| 939 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [443, 2880] | torch.bfloat16 → float32 | -52.5 / 24.875 / -0.015501749463583073 / 1.275053132745384 | [NPY](tensors/0000939.npy) |
| 940 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 941 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 942 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 943 | `model.layers.23.mlp.experts` | 0 | `output` | [443, 2880] | torch.bfloat16 → float32 | -5856.0 / 5280.0 / -1.712614278910541 / 148.83484295664582 | [NPY](tensors/0000943.npy) |
| 944 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 443, 2880] | torch.bfloat16 → float32 | -5856.0 / 5280.0 / -1.712614278910541 / 148.83484295664582 | [NPY](tensors/0000944.npy) |
| 945 | `model.layers.23.mlp` | 0 | `output[1]` | [443, 32] | torch.bfloat16 → float32 | -8.25 / 4.9375 / 0.2550579742707194 / 2.668002353172342 | [NPY](tensors/0000945.npy) |
| 946 | `model.layers.23` | 0 | `output` | [1, 443, 2880] | torch.bfloat16 → float32 | -10880.0 / 10944.0 / -0.8261206908904134 / 391.3105693416343 | [NPY](tensors/0000946.npy) |

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
