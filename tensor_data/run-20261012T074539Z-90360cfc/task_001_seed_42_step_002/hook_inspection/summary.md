# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 731 full tensors; 950 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Outside Transformer blocks

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model` | 0 | `input.kwargs['input_ids']` | [1, 281] | torch.int64 → int64 | 11.0 / 198835.0 / 25612.44839857651 / 41282.80277189102 | [NPY](tensors/0000000.npy) |
| 1 | `model` | 0 | `input.kwargs['attention_mask']` | [1, 281] | torch.int64 → int64 | 1.0 / 1.0 / 1.0 / 0.0 | [NPY](tensors/0000001.npy) |
| 2 | `model` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 3 | `model` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 4 | `model` | 0 | `input.kwargs['return_dict']` | — | bool | True | — |
| 5 | `model.embed_tokens` | 0 | `input.args[0]` | [1, 281] | torch.int64 → int64 | 11.0 / 198835.0 / 25612.44839857651 / 41282.80277189102 | [NPY](tensors/0000005.npy) |
| 6 | `model.embed_tokens` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.005187735238798202 / 2.8128906327218837 | [NPY](tensors/0000006.npy) |
| 7 | `model.rotary_emb` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.005187735238798202 / 2.8128906327218837 | [NPY](tensors/0000007.npy) |
| 8 | `model.rotary_emb` | 0 | `input.args[1]` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000008.npy) |
| 9 | `model.rotary_emb` | 0 | `output[0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000009.npy) |
| 10 | `model.rotary_emb` | 0 | `output[1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000010.npy) |
| 947 | `model.norm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -10944.0 / 10880.0 / -0.8688804400207591 / 413.1514180610229 | [NPY](tensors/0000947.npy) |
| 948 | `model.norm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -340.0 / 189.0 / -0.03672567316905082 / 6.331862538252157 | [NPY](tensors/0000948.npy) |
| 949 | `model` | 0 | `output['last_hidden_state']` | [1, 281, 2880] | torch.bfloat16 → float32 | -340.0 / 189.0 / -0.03672567316905082 / 6.331862538252157 | [NPY](tensors/0000949.npy) |

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | `model.layers.0` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.005187735238798202 / 2.8128906327218837 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000013.npy) |
| 14 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000014.npy) |
| 15 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 17 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 18 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 19 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.005187735238798202 / 2.8128906327218837 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.003860356925812521 / 0.7576518373019236 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.003860356925812521 / 0.7576518373019236 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 25 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 26 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 29 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.003860356925812521 / 0.7576518373019236 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -10.25 / 12.8125 / 0.021135465877734558 / 1.0411001343678539 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.003860356925812521 / 0.7576518373019236 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.023611766375680836 / 5.797660959104256 | [NPY](tensors/0000032.npy) |
| 33 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.003860356925812521 / 0.7576518373019236 | [NPY](tensors/0000033.npy) |
| 34 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -8.125 / 7.71875 / -0.01707450372044302 / 1.2134277540618192 | [NPY](tensors/0000034.npy) |
| 35 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -8.125 / 7.71875 / -0.00726052164820495 / 0.5489004398577653 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.028810523043528602 / 1.1748372917064498 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.028810523043528602 / 1.1748372917064498 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0013878806356226404 / 0.02451463610754445 | [NPY](tensors/0000038.npy) |
| 39 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -87.5 / 71.0 / 0.02362880636729851 / 2.9722634566981916 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -7.25 / 3.75 / 0.000893241947037328 / 0.34007502304022363 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -7.25 / 3.75 / 0.000893241947037328 / 0.34007502304022363 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -7.25 / 3.75 / 0.000893241947037328 / 0.34007502304022363 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 44 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 45 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 46 | `model.layers.0.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -50.0 / 93.0 / 0.018966990084151307 / 0.9172741757257287 | [NPY](tensors/0000046.npy) |
| 47 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -50.0 / 93.0 / 0.018966990084151307 / 0.9172741757257287 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.0.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -4.96875 / 3.4375 / -0.10461368764422542 / 1.0228367613154932 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.0` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -89.0 / 106.5 / 0.04258818286075193 / 3.228804075359364 | [NPY](tensors/0000049.npy) |

## Layer 0001

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | `model.layers.1` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -89.0 / 106.5 / 0.04258818286075193 / 3.228804075359364 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.1` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.1` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000052.npy) |
| 53 | `model.layers.1` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000053.npy) |
| 54 | `model.layers.1` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.1` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 56 | `model.layers.1` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 57 | `model.layers.1` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 58 | `model.layers.1.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -89.0 / 106.5 / 0.04258818286075193 / 3.228804075359364 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.1.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -28.125 / 25.75 / 0.009518592104981566 / 0.8533104487021493 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.1.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -28.125 / 25.75 / 0.009518592104981566 / 0.8533104487021493 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.1.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.1.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 64 | `model.layers.1.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 65 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.1.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 68 | `model.layers.1.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -28.125 / 25.75 / 0.009518592104981566 / 0.8533104487021493 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.1.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -11.375 / 12.25 / -0.01955021709211022 / 1.1079227423207842 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.1.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -28.125 / 25.75 / 0.009518592104981566 / 0.8533104487021493 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.1.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -110.0 / 40.5 / -0.7110644276668169 / 7.809424600964653 | [NPY](tensors/0000071.npy) |
| 72 | `model.layers.1.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -28.125 / 25.75 / 0.009518592104981566 / 0.8533104487021493 | [NPY](tensors/0000072.npy) |
| 73 | `model.layers.1.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -6.71875 / 8.0625 / 0.014785234375568472 / 1.0011960419994659 | [NPY](tensors/0000073.npy) |
| 74 | `model.layers.1.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -5.84375 / 5.96875 / 0.001999339624777352 / 0.44152092291492645 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.1.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -33.75 / 52.25 / 0.002496355771917162 / 0.837827913317659 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.1.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -33.75 / 52.25 / 0.002496355771917162 / 0.837827913317659 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.1.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0023749553858177517 / 0.022099840679434296 | [NPY](tensors/0000077.npy) |
| 78 | `model.layers.1.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -89.0 / 78.0 / 0.04508326979005652 / 3.1867977466079376 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.1.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.4375 / 0.000706577420635344 / 0.37073340010380057 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.1.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.4375 / 0.000706577420635344 / 0.37073340010380057 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.1.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.4375 / 0.000706577420635344 / 0.37073340010380057 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.1.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 83 | `model.layers.1.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 84 | `model.layers.1.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 85 | `model.layers.1.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -47.25 / 83.0 / 0.022879553428925087 / 1.1012518860713343 | [NPY](tensors/0000085.npy) |
| 86 | `model.layers.1.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -47.25 / 83.0 / 0.022879553428925087 / 1.1012518860713343 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.1.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -2.65625 / 2.75 / -0.08457319507395246 / 0.7297218236368176 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.1` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -109.5 / 130.0 / 0.06795254617210619 / 3.7451879507875065 | [NPY](tensors/0000088.npy) |

## Layer 0002

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 89 | `model.layers.2` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -109.5 / 130.0 / 0.06795254617210619 / 3.7451879507875065 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.2` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.2` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000091.npy) |
| 92 | `model.layers.2` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000092.npy) |
| 93 | `model.layers.2` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.2` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 95 | `model.layers.2` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 96 | `model.layers.2` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 97 | `model.layers.2.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -109.5 / 130.0 / 0.06795254617210619 / 3.7451879507875065 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.2.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -29.125 / 25.25 / 0.014465501155599674 / 0.8602838794218008 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.2.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -29.125 / 25.25 / 0.014465501155599674 / 0.8602838794218008 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.2.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.2.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 103 | `model.layers.2.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 104 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.2.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 107 | `model.layers.2.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -29.125 / 25.25 / 0.014465501155599674 / 0.8602838794218008 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.2.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -13.8125 / 8.375 / 0.04009183290015189 / 0.890595397872123 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.2.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -29.125 / 25.25 / 0.014465501155599674 / 0.8602838794218008 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.2.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -26.875 / 22.5 / -0.018257535596335063 / 2.568911000883953 | [NPY](tensors/0000110.npy) |
| 111 | `model.layers.2.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -29.125 / 25.25 / 0.014465501155599674 / 0.8602838794218008 | [NPY](tensors/0000111.npy) |
| 112 | `model.layers.2.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -8.0 / 5.875 / 0.02326528892398305 / 1.1619656533285163 | [NPY](tensors/0000112.npy) |
| 113 | `model.layers.2.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -6.5625 / 4.9375 / 0.013218381743982327 / 0.47360552090801106 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.2.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -48.0 / 51.0 / 0.0006065784470381097 / 0.9799297201684635 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.2.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -48.0 / 51.0 / 0.0006065784470381097 / 0.9799297201684635 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.2.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0017349353969667227 / 0.019115143794875437 | [NPY](tensors/0000116.npy) |
| 117 | `model.layers.2.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -83.5 / 123.5 / 0.06855946197817098 / 3.7016298529472578 | [NPY](tensors/0000117.npy) |
| 118 | `model.layers.2.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.28125 / 0.0025189644695742413 / 0.46387606455045954 | [NPY](tensors/0000118.npy) |
| 119 | `model.layers.2.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.28125 / 0.0025189644695742413 / 0.46387606455045954 | [NPY](tensors/0000119.npy) |
| 120 | `model.layers.2.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.28125 / 0.0025189644695742413 / 0.46387606455045954 | [NPY](tensors/0000120.npy) |
| 121 | `model.layers.2.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 122 | `model.layers.2.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 123 | `model.layers.2.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 124 | `model.layers.2.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -58.5 / 88.0 / 0.02924633300415774 / 1.346786651878854 | [NPY](tensors/0000124.npy) |
| 125 | `model.layers.2.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -58.5 / 88.0 / 0.02924633300415774 / 1.346786651878854 | [NPY](tensors/0000125.npy) |
| 126 | `model.layers.2.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -3.21875 / 2.21875 / -0.09775845945093556 / 0.6687917303193243 | [NPY](tensors/0000126.npy) |
| 127 | `model.layers.2` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -117.0 / 148.0 / 0.09779448037847034 / 4.442128109185962 | [NPY](tensors/0000127.npy) |

## Layer 0003

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | `model.layers.3` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -117.0 / 148.0 / 0.09779448037847034 / 4.442128109185962 | [NPY](tensors/0000128.npy) |
| 129 | `model.layers.3` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000129.npy) |
| 130 | `model.layers.3` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000130.npy) |
| 131 | `model.layers.3` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000131.npy) |
| 132 | `model.layers.3` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000132.npy) |
| 133 | `model.layers.3` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 134 | `model.layers.3` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 135 | `model.layers.3` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 136 | `model.layers.3.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -117.0 / 148.0 / 0.09779448037847034 / 4.442128109185962 | [NPY](tensors/0000136.npy) |
| 137 | `model.layers.3.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -57.25 / 56.5 / 0.035293923004189 / 1.2695684515754189 | [NPY](tensors/0000137.npy) |
| 138 | `model.layers.3.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -57.25 / 56.5 / 0.035293923004189 / 1.2695684515754189 | [NPY](tensors/0000138.npy) |
| 139 | `model.layers.3.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000139.npy) |
| 140 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000140.npy) |
| 141 | `model.layers.3.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 142 | `model.layers.3.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 143 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000143.npy) |
| 144 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000144.npy) |
| 145 | `model.layers.3.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 146 | `model.layers.3.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -57.25 / 56.5 / 0.035293923004189 / 1.2695684515754189 | [NPY](tensors/0000146.npy) |
| 147 | `model.layers.3.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -12.5625 / 9.0 / -0.024248936218925765 / 1.1101695916366032 | [NPY](tensors/0000147.npy) |
| 148 | `model.layers.3.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -57.25 / 56.5 / 0.035293923004189 / 1.2695684515754189 | [NPY](tensors/0000148.npy) |
| 149 | `model.layers.3.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -78.5 / 56.5 / -0.07893557666247425 / 4.8685024461870725 | [NPY](tensors/0000149.npy) |
| 150 | `model.layers.3.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -57.25 / 56.5 / 0.035293923004189 / 1.2695684515754189 | [NPY](tensors/0000150.npy) |
| 151 | `model.layers.3.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -7.625 / 11.375 / 0.01685018576946759 / 0.9740243512676655 | [NPY](tensors/0000151.npy) |
| 152 | `model.layers.3.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -4.15625 / 3.796875 / 0.009431081708882464 / 0.3220841888643693 | [NPY](tensors/0000152.npy) |
| 153 | `model.layers.3.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -63.0 / 36.25 / -0.005859414536061082 / 1.0174566768685844 | [NPY](tensors/0000153.npy) |
| 154 | `model.layers.3.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -63.0 / 36.25 / -0.005859414536061082 / 1.0174566768685844 | [NPY](tensors/0000154.npy) |
| 155 | `model.layers.3.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 0.9765625 / 0.0018852065131542781 / 0.013296702164507722 | [NPY](tensors/0000155.npy) |
| 156 | `model.layers.3.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -103.5 / 134.0 / 0.09195024938911447 / 4.4340218243182825 | [NPY](tensors/0000156.npy) |
| 157 | `model.layers.3.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -6.0 / 5.71875 / 0.004254201200108322 / 0.5207344913065116 | [NPY](tensors/0000157.npy) |
| 158 | `model.layers.3.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -6.0 / 5.71875 / 0.004254201200108322 / 0.5207344913065116 | [NPY](tensors/0000158.npy) |
| 159 | `model.layers.3.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -6.0 / 5.71875 / 0.004254201200108322 / 0.5207344913065116 | [NPY](tensors/0000159.npy) |
| 160 | `model.layers.3.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 161 | `model.layers.3.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 162 | `model.layers.3.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 163 | `model.layers.3.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -61.5 / 93.0 / 0.024724617920972084 / 1.4676821061505725 | [NPY](tensors/0000163.npy) |
| 164 | `model.layers.3.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -61.5 / 93.0 / 0.024724617920972084 / 1.4676821061505725 | [NPY](tensors/0000164.npy) |
| 165 | `model.layers.3.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -3.25 / 2.015625 / -0.07400821197075352 / 0.5414790762714151 | [NPY](tensors/0000165.npy) |
| 166 | `model.layers.3` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -150.0 / 172.0 / 0.11668390120947111 / 5.268796061782712 | [NPY](tensors/0000166.npy) |

## Layer 0004

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 167 | `model.layers.4` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -150.0 / 172.0 / 0.11668390120947111 / 5.268796061782712 | [NPY](tensors/0000167.npy) |
| 168 | `model.layers.4` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000168.npy) |
| 169 | `model.layers.4` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000169.npy) |
| 170 | `model.layers.4` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000170.npy) |
| 171 | `model.layers.4` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000171.npy) |
| 172 | `model.layers.4` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 173 | `model.layers.4` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 174 | `model.layers.4` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 175 | `model.layers.4.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -150.0 / 172.0 / 0.11668390120947111 / 5.268796061782712 | [NPY](tensors/0000175.npy) |
| 176 | `model.layers.4.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02186316388982141 / 1.1376952233108764 | [NPY](tensors/0000176.npy) |
| 177 | `model.layers.4.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02186316388982141 / 1.1376952233108764 | [NPY](tensors/0000177.npy) |
| 178 | `model.layers.4.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000178.npy) |
| 179 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000179.npy) |
| 180 | `model.layers.4.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 181 | `model.layers.4.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 182 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000182.npy) |
| 183 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000183.npy) |
| 184 | `model.layers.4.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 185 | `model.layers.4.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02186316388982141 / 1.1376952233108764 | [NPY](tensors/0000185.npy) |
| 186 | `model.layers.4.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -17.0 / 8.1875 / -0.010350024391759995 / 1.03468812670945 | [NPY](tensors/0000186.npy) |
| 187 | `model.layers.4.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02186316388982141 / 1.1376952233108764 | [NPY](tensors/0000187.npy) |
| 188 | `model.layers.4.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -14.25 / 99.0 / 0.23618517605939157 / 4.336859954744564 | [NPY](tensors/0000188.npy) |
| 189 | `model.layers.4.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02186316388982141 / 1.1376952233108764 | [NPY](tensors/0000189.npy) |
| 190 | `model.layers.4.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -10.8125 / 16.25 / 0.004077151788935543 / 1.3470136134439092 | [NPY](tensors/0000190.npy) |
| 191 | `model.layers.4.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -9.625 / 15.0625 / -0.0030354370400187346 / 0.5979343487374883 | [NPY](tensors/0000191.npy) |
| 192 | `model.layers.4.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -68.0 / 43.75 / -0.004600324788097309 / 1.2588600509100532 | [NPY](tensors/0000192.npy) |
| 193 | `model.layers.4.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -68.0 / 43.75 / -0.004600324788097309 / 1.2588600509100532 | [NPY](tensors/0000193.npy) |
| 194 | `model.layers.4.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.0018370913685422019 / 0.0185863159725161 | [NPY](tensors/0000194.npy) |
| 195 | `model.layers.4.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -134.0 / 150.0 / 0.11209265513587913 / 5.256122758719647 | [NPY](tensors/0000195.npy) |
| 196 | `model.layers.4.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -5.625 / 6.90625 / 0.00732244441338022 / 0.5796078922721035 | [NPY](tensors/0000196.npy) |
| 197 | `model.layers.4.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -5.625 / 6.90625 / 0.00732244441338022 / 0.5796078922721035 | [NPY](tensors/0000197.npy) |
| 198 | `model.layers.4.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -5.625 / 6.90625 / 0.00732244441338022 / 0.5796078922721035 | [NPY](tensors/0000198.npy) |
| 199 | `model.layers.4.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 200 | `model.layers.4.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 201 | `model.layers.4.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 202 | `model.layers.4.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -83.0 / 165.0 / 0.0486167390445986 / 2.316637583164471 | [NPY](tensors/0000202.npy) |
| 203 | `model.layers.4.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -83.0 / 165.0 / 0.0486167390445986 / 2.316637583164471 | [NPY](tensors/0000203.npy) |
| 204 | `model.layers.4.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -3.125 / 2.171875 / -0.08355731217462398 / 0.5996428591040432 | [NPY](tensors/0000204.npy) |
| 205 | `model.layers.4` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -192.0 / 253.0 / 0.1606950514398577 / 6.684694996865849 | [NPY](tensors/0000205.npy) |

## Layer 0005

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 206 | `model.layers.5` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -192.0 / 253.0 / 0.1606950514398577 / 6.684694996865849 | [NPY](tensors/0000206.npy) |
| 207 | `model.layers.5` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000207.npy) |
| 208 | `model.layers.5` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000208.npy) |
| 209 | `model.layers.5` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000209.npy) |
| 210 | `model.layers.5` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000210.npy) |
| 211 | `model.layers.5` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 212 | `model.layers.5` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 213 | `model.layers.5` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 214 | `model.layers.5.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -192.0 / 253.0 / 0.1606950514398577 / 6.684694996865849 | [NPY](tensors/0000214.npy) |
| 215 | `model.layers.5.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -29.875 / 41.25 / 0.03456342871620892 / 1.1821342492855338 | [NPY](tensors/0000215.npy) |
| 216 | `model.layers.5.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -29.875 / 41.25 / 0.03456342871620892 / 1.1821342492855338 | [NPY](tensors/0000216.npy) |
| 217 | `model.layers.5.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000217.npy) |
| 218 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000218.npy) |
| 219 | `model.layers.5.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 220 | `model.layers.5.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 221 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000221.npy) |
| 222 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000222.npy) |
| 223 | `model.layers.5.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 224 | `model.layers.5.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -29.875 / 41.25 / 0.03456342871620892 / 1.1821342492855338 | [NPY](tensors/0000224.npy) |
| 225 | `model.layers.5.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -19.5 / 15.0 / -0.05778200525868235 / 1.418812275277958 | [NPY](tensors/0000225.npy) |
| 226 | `model.layers.5.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -29.875 / 41.25 / 0.03456342871620892 / 1.1821342492855338 | [NPY](tensors/0000226.npy) |
| 227 | `model.layers.5.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -36.25 / 39.5 / -0.04537585048913107 / 3.4503720468286723 | [NPY](tensors/0000227.npy) |
| 228 | `model.layers.5.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -29.875 / 41.25 / 0.03456342871620892 / 1.1821342492855338 | [NPY](tensors/0000228.npy) |
| 229 | `model.layers.5.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -7.3125 / 8.4375 / 0.012091056201805847 / 1.204874392098176 | [NPY](tensors/0000229.npy) |
| 230 | `model.layers.5.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -4.5625 / 5.53125 / 0.011516194354687528 / 0.5267879604520179 | [NPY](tensors/0000230.npy) |
| 231 | `model.layers.5.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -71.5 / 78.5 / -0.004274809353811074 / 1.4842764836373226 | [NPY](tensors/0000231.npy) |
| 232 | `model.layers.5.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -71.5 / 78.5 / -0.004274809353811074 / 1.4842764836373226 | [NPY](tensors/0000232.npy) |
| 233 | `model.layers.5.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002036676194788862 / 0.014762272879922553 | [NPY](tensors/0000233.npy) |
| 234 | `model.layers.5.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -142.0 / 207.0 / 0.1563821279988453 / 6.984955397398798 | [NPY](tensors/0000234.npy) |
| 235 | `model.layers.5.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -5.59375 / 5.71875 / 0.008133089611473977 / 0.5665853851834393 | [NPY](tensors/0000235.npy) |
| 236 | `model.layers.5.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -5.59375 / 5.71875 / 0.008133089611473977 / 0.5665853851834393 | [NPY](tensors/0000236.npy) |
| 237 | `model.layers.5.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -5.59375 / 5.71875 / 0.008133089611473977 / 0.5665853851834393 | [NPY](tensors/0000237.npy) |
| 238 | `model.layers.5.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 239 | `model.layers.5.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 240 | `model.layers.5.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 241 | `model.layers.5.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -122.0 / 115.0 / 0.041567671268341704 / 2.497023372049312 | [NPY](tensors/0000241.npy) |
| 242 | `model.layers.5.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -122.0 / 115.0 / 0.041567671268341704 / 2.497023372049312 | [NPY](tensors/0000242.npy) |
| 243 | `model.layers.5.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -3.703125 / 2.265625 / -0.08869434506019239 / 0.5847722201869735 | [NPY](tensors/0000243.npy) |
| 244 | `model.layers.5` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -196.0 / 298.0 / 0.19791863985615976 / 8.4892370293047 | [NPY](tensors/0000244.npy) |

## Layer 0006

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 245 | `model.layers.6` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -196.0 / 298.0 / 0.19791863985615976 / 8.4892370293047 | [NPY](tensors/0000245.npy) |
| 246 | `model.layers.6` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000246.npy) |
| 247 | `model.layers.6` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000247.npy) |
| 248 | `model.layers.6` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000248.npy) |
| 249 | `model.layers.6` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000249.npy) |
| 250 | `model.layers.6` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 251 | `model.layers.6` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 252 | `model.layers.6` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 253 | `model.layers.6.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -196.0 / 298.0 / 0.19791863985615976 / 8.4892370293047 | [NPY](tensors/0000253.npy) |
| 254 | `model.layers.6.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -33.75 / 43.25 / 0.03115375072364988 / 1.3072268213346974 | [NPY](tensors/0000254.npy) |
| 255 | `model.layers.6.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -33.75 / 43.25 / 0.03115375072364988 / 1.3072268213346974 | [NPY](tensors/0000255.npy) |
| 256 | `model.layers.6.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000256.npy) |
| 257 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000257.npy) |
| 258 | `model.layers.6.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 259 | `model.layers.6.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 260 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000260.npy) |
| 261 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000261.npy) |
| 262 | `model.layers.6.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 263 | `model.layers.6.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -33.75 / 43.25 / 0.03115375072364988 / 1.3072268213346974 | [NPY](tensors/0000263.npy) |
| 264 | `model.layers.6.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -29.125 / 16.625 / -0.02629662034608978 / 1.1618724428244303 | [NPY](tensors/0000264.npy) |
| 265 | `model.layers.6.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -33.75 / 43.25 / 0.03115375072364988 / 1.3072268213346974 | [NPY](tensors/0000265.npy) |
| 266 | `model.layers.6.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -19.75 / 32.5 / 0.21271169471995263 / 2.380985308535273 | [NPY](tensors/0000266.npy) |
| 267 | `model.layers.6.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -33.75 / 43.25 / 0.03115375072364988 / 1.3072268213346974 | [NPY](tensors/0000267.npy) |
| 268 | `model.layers.6.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -10.9375 / 8.625 / -0.05875310885100178 / 1.6280907180080848 | [NPY](tensors/0000268.npy) |
| 269 | `model.layers.6.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -9.8125 / 7.71875 / -0.038777179807094914 / 0.8240879330022425 | [NPY](tensors/0000269.npy) |
| 270 | `model.layers.6.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -90.5 / 82.0 / -0.0011401231529742785 / 1.8664915496168117 | [NPY](tensors/0000270.npy) |
| 271 | `model.layers.6.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -90.5 / 82.0 / -0.0011401231529742785 / 1.8664915496168117 | [NPY](tensors/0000271.npy) |
| 272 | `model.layers.6.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0020159781324206576 / 0.021017154844411256 | [NPY](tensors/0000272.npy) |
| 273 | `model.layers.6.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -181.0 / 246.0 / 0.19678102792982718 / 8.432880588262067 | [NPY](tensors/0000273.npy) |
| 274 | `model.layers.6.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -22.0 / 4.875 / 0.011738841189679161 / 0.606213265740521 | [NPY](tensors/0000274.npy) |
| 275 | `model.layers.6.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -22.0 / 4.875 / 0.011738841189679161 / 0.606213265740521 | [NPY](tensors/0000275.npy) |
| 276 | `model.layers.6.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -22.0 / 4.875 / 0.011738841189679161 / 0.606213265740521 | [NPY](tensors/0000276.npy) |
| 277 | `model.layers.6.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 278 | `model.layers.6.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 279 | `model.layers.6.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 280 | `model.layers.6.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -41472.0 / 968.0 / -0.01871245910217282 / 46.26869906069415 | [NPY](tensors/0000280.npy) |
| 281 | `model.layers.6.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41472.0 / 968.0 / -0.01871245910217282 / 46.26869906069415 | [NPY](tensors/0000281.npy) |
| 282 | `model.layers.6.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -3.609375 / 5.0 / -0.11043788869185804 / 0.7409873040432837 | [NPY](tensors/0000282.npy) |
| 283 | `model.layers.6` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.17822402500267226 / 47.31493004946029 | [NPY](tensors/0000283.npy) |

## Layer 0007

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 284 | `model.layers.7` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.17822402500267226 / 47.31493004946029 | [NPY](tensors/0000284.npy) |
| 285 | `model.layers.7` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000285.npy) |
| 286 | `model.layers.7` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000286.npy) |
| 287 | `model.layers.7` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000287.npy) |
| 288 | `model.layers.7` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000288.npy) |
| 289 | `model.layers.7` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 290 | `model.layers.7` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 291 | `model.layers.7` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 292 | `model.layers.7.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.17822402500267226 / 47.31493004946029 | [NPY](tensors/0000292.npy) |
| 293 | `model.layers.7.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.037135782063054484 / 1.622003905241259 | [NPY](tensors/0000293.npy) |
| 294 | `model.layers.7.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.037135782063054484 / 1.622003905241259 | [NPY](tensors/0000294.npy) |
| 295 | `model.layers.7.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000295.npy) |
| 296 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000296.npy) |
| 297 | `model.layers.7.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 298 | `model.layers.7.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 299 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000299.npy) |
| 300 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000300.npy) |
| 301 | `model.layers.7.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 302 | `model.layers.7.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.037135782063054484 / 1.622003905241259 | [NPY](tensors/0000302.npy) |
| 303 | `model.layers.7.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -13.4375 / 13.25 / -0.12216116213408941 / 1.4282772809521325 | [NPY](tensors/0000303.npy) |
| 304 | `model.layers.7.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.037135782063054484 / 1.622003905241259 | [NPY](tensors/0000304.npy) |
| 305 | `model.layers.7.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -130.0 / 33.75 / -0.07502628580478163 / 5.422534363294424 | [NPY](tensors/0000305.npy) |
| 306 | `model.layers.7.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.037135782063054484 / 1.622003905241259 | [NPY](tensors/0000306.npy) |
| 307 | `model.layers.7.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -17.0 / 10.8125 / 0.008864239335484352 / 1.6491447134461545 | [NPY](tensors/0000307.npy) |
| 308 | `model.layers.7.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -7.71875 / 8.0 / 0.0011754098239397021 / 0.9085447347183702 | [NPY](tensors/0000308.npy) |
| 309 | `model.layers.7.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -121.5 / 129.0 / -0.0034344333351415536 / 2.2667792374143763 | [NPY](tensors/0000309.npy) |
| 310 | `model.layers.7.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -121.5 / 129.0 / -0.0034344333351415536 / 2.2667792374143763 | [NPY](tensors/0000310.npy) |
| 311 | `model.layers.7.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002760867514983917 / 0.02333991224209912 | [NPY](tensors/0000311.npy) |
| 312 | `model.layers.7.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41472.0 / 1104.0 / 0.17480605922229867 / 47.32646180646911 | [NPY](tensors/0000312.npy) |
| 313 | `model.layers.7.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -77.0 / 5.59375 / 0.010166449043656723 / 0.6255387528088014 | [NPY](tensors/0000313.npy) |
| 314 | `model.layers.7.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -77.0 / 5.59375 / 0.010166449043656723 / 0.6255387528088014 | [NPY](tensors/0000314.npy) |
| 315 | `model.layers.7.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -77.0 / 5.59375 / 0.010166449043656723 / 0.6255387528088014 | [NPY](tensors/0000315.npy) |
| 316 | `model.layers.7.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 317 | `model.layers.7.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 318 | `model.layers.7.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 319 | `model.layers.7.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -158.0 / 172.0 / 0.033456747161394615 / 3.4482704563247037 | [NPY](tensors/0000319.npy) |
| 320 | `model.layers.7.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -158.0 / 172.0 / 0.033456747161394615 / 3.4482704563247037 | [NPY](tensors/0000320.npy) |
| 321 | `model.layers.7.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -3.890625 / 3.828125 / -0.12790639799260584 / 0.7917085806986377 | [NPY](tensors/0000321.npy) |
| 322 | `model.layers.7` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.20825996625183033 / 47.81747694373386 | [NPY](tensors/0000322.npy) |

## Layer 0008

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 323 | `model.layers.8` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.20825996625183033 / 47.81747694373386 | [NPY](tensors/0000323.npy) |
| 324 | `model.layers.8` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000324.npy) |
| 325 | `model.layers.8` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000325.npy) |
| 326 | `model.layers.8` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000326.npy) |
| 327 | `model.layers.8` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000327.npy) |
| 328 | `model.layers.8` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 329 | `model.layers.8` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 330 | `model.layers.8` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 331 | `model.layers.8.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.20825996625183033 / 47.81747694373386 | [NPY](tensors/0000331.npy) |
| 332 | `model.layers.8.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.028220194717556144 / 1.3258872991337347 | [NPY](tensors/0000332.npy) |
| 333 | `model.layers.8.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.028220194717556144 / 1.3258872991337347 | [NPY](tensors/0000333.npy) |
| 334 | `model.layers.8.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000334.npy) |
| 335 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000335.npy) |
| 336 | `model.layers.8.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 337 | `model.layers.8.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 338 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000338.npy) |
| 339 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000339.npy) |
| 340 | `model.layers.8.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 341 | `model.layers.8.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.028220194717556144 / 1.3258872991337347 | [NPY](tensors/0000341.npy) |
| 342 | `model.layers.8.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -14.9375 / 15.25 / -0.00919101263569123 / 1.0647849122027888 | [NPY](tensors/0000342.npy) |
| 343 | `model.layers.8.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.028220194717556144 / 1.3258872991337347 | [NPY](tensors/0000343.npy) |
| 344 | `model.layers.8.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -22.375 / 30.75 / 0.0042220921490964515 / 2.2355614811971276 | [NPY](tensors/0000344.npy) |
| 345 | `model.layers.8.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -121.5 / 43.5 / 0.028220194717556144 / 1.3258872991337347 | [NPY](tensors/0000345.npy) |
| 346 | `model.layers.8.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -9.3125 / 9.6875 / 0.0014612638653385256 / 1.723557684228278 | [NPY](tensors/0000346.npy) |
| 347 | `model.layers.8.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -7.28125 / 7.03125 / 0.0033676317679448993 / 0.8673623484296349 | [NPY](tensors/0000347.npy) |
| 348 | `model.layers.8.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -199.0 / 213.0 / 0.008853502943817218 / 2.970630607758596 | [NPY](tensors/0000348.npy) |
| 349 | `model.layers.8.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -199.0 / 213.0 / 0.008853502943817218 / 2.970630607758596 | [NPY](tensors/0000349.npy) |
| 350 | `model.layers.8.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0022220267704557367 / 0.01999650193839787 | [NPY](tensors/0000350.npy) |
| 351 | `model.layers.8.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41472.0 / 1344.0 / 0.21712508842661335 / 47.78082655297875 | [NPY](tensors/0000351.npy) |
| 352 | `model.layers.8.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -57.0 / 6.375 / 0.00958369087691895 / 0.6619627569430703 | [NPY](tensors/0000352.npy) |
| 353 | `model.layers.8.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -57.0 / 6.375 / 0.00958369087691895 / 0.6619627569430703 | [NPY](tensors/0000353.npy) |
| 354 | `model.layers.8.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -57.0 / 6.375 / 0.00958369087691895 / 0.6619627569430703 | [NPY](tensors/0000354.npy) |
| 355 | `model.layers.8.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 356 | `model.layers.8.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 357 | `model.layers.8.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 358 | `model.layers.8.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -294.0 / 252.0 / 0.06503359255181701 / 4.911391083693216 | [NPY](tensors/0000358.npy) |
| 359 | `model.layers.8.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -294.0 / 252.0 / 0.06503359255181701 / 4.911391083693216 | [NPY](tensors/0000359.npy) |
| 360 | `model.layers.8.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -3.9375 / 3.515625 / -0.1618343290485097 / 0.7436136117527451 | [NPY](tensors/0000360.npy) |
| 361 | `model.layers.8` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.2820602468277165 / 48.8933758670483 | [NPY](tensors/0000361.npy) |

## Layer 0009

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 362 | `model.layers.9` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.2820602468277165 / 48.8933758670483 | [NPY](tensors/0000362.npy) |
| 363 | `model.layers.9` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000363.npy) |
| 364 | `model.layers.9` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000364.npy) |
| 365 | `model.layers.9` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000365.npy) |
| 366 | `model.layers.9` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000366.npy) |
| 367 | `model.layers.9` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 368 | `model.layers.9` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 369 | `model.layers.9` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 370 | `model.layers.9.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.2820602468277165 / 48.8933758670483 | [NPY](tensors/0000370.npy) |
| 371 | `model.layers.9.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.040178915512622475 / 1.7835437871270647 | [NPY](tensors/0000371.npy) |
| 372 | `model.layers.9.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.040178915512622475 / 1.7835437871270647 | [NPY](tensors/0000372.npy) |
| 373 | `model.layers.9.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000373.npy) |
| 374 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000374.npy) |
| 375 | `model.layers.9.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 376 | `model.layers.9.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 377 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000377.npy) |
| 378 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000378.npy) |
| 379 | `model.layers.9.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 380 | `model.layers.9.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.040178915512622475 / 1.7835437871270647 | [NPY](tensors/0000380.npy) |
| 381 | `model.layers.9.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -10.1875 / 20.125 / 0.06424159047263633 / 1.2800380909120548 | [NPY](tensors/0000381.npy) |
| 382 | `model.layers.9.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.040178915512622475 / 1.7835437871270647 | [NPY](tensors/0000382.npy) |
| 383 | `model.layers.9.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -51.25 / 41.0 / 0.056777810737543684 / 3.9207601731596204 | [NPY](tensors/0000383.npy) |
| 384 | `model.layers.9.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.040178915512622475 / 1.7835437871270647 | [NPY](tensors/0000384.npy) |
| 385 | `model.layers.9.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -27.75 / 12.375 / -0.0063216038233869015 / 1.5088184212777802 | [NPY](tensors/0000385.npy) |
| 386 | `model.layers.9.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -11.0 / 8.875 / 0.0011719854616155313 / 0.6660335821164195 | [NPY](tensors/0000386.npy) |
| 387 | `model.layers.9.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -348.0 / 344.0 / 0.020668768094193015 / 3.71356512553787 | [NPY](tensors/0000387.npy) |
| 388 | `model.layers.9.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -348.0 / 344.0 / 0.020668768094193015 / 3.71356512553787 | [NPY](tensors/0000388.npy) |
| 389 | `model.layers.9.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.002761717360092232 / 0.020174076828445412 | [NPY](tensors/0000389.npy) |
| 390 | `model.layers.9.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41728.0 / 1480.0 / 0.30281035685878627 / 48.83151359725118 | [NPY](tensors/0000390.npy) |
| 391 | `model.layers.9.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -64.5 / 6.75 / 0.010495273389891467 / 0.6773078983094418 | [NPY](tensors/0000391.npy) |
| 392 | `model.layers.9.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -64.5 / 6.75 / 0.010495273389891467 / 0.6773078983094418 | [NPY](tensors/0000392.npy) |
| 393 | `model.layers.9.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -64.5 / 6.75 / 0.010495273389891467 / 0.6773078983094418 | [NPY](tensors/0000393.npy) |
| 394 | `model.layers.9.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 395 | `model.layers.9.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 396 | `model.layers.9.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 397 | `model.layers.9.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -572.0 / 640.0 / 0.04254911796713875 / 5.4412263377928 | [NPY](tensors/0000397.npy) |
| 398 | `model.layers.9.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -572.0 / 640.0 / 0.04254911796713875 / 5.4412263377928 | [NPY](tensors/0000398.npy) |
| 399 | `model.layers.9.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -5.21875 / 6.40625 / -0.1280342319257743 / 0.6171871041322221 | [NPY](tensors/0000399.npy) |
| 400 | `model.layers.9` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 908.0 / 0.3454988874056067 / 49.298123514486306 | [NPY](tensors/0000400.npy) |

## Layer 0010

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 401 | `model.layers.10` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 908.0 / 0.3454988874056067 / 49.298123514486306 | [NPY](tensors/0000401.npy) |
| 402 | `model.layers.10` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000402.npy) |
| 403 | `model.layers.10` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000403.npy) |
| 404 | `model.layers.10` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000404.npy) |
| 405 | `model.layers.10` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000405.npy) |
| 406 | `model.layers.10` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 407 | `model.layers.10` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 408 | `model.layers.10` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 409 | `model.layers.10.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 908.0 / 0.3454988874056067 / 49.298123514486306 | [NPY](tensors/0000409.npy) |
| 410 | `model.layers.10.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.03339468562108648 / 1.5344851009976903 | [NPY](tensors/0000410.npy) |
| 411 | `model.layers.10.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.03339468562108648 / 1.5344851009976903 | [NPY](tensors/0000411.npy) |
| 412 | `model.layers.10.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000412.npy) |
| 413 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000413.npy) |
| 414 | `model.layers.10.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 415 | `model.layers.10.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 416 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000416.npy) |
| 417 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000417.npy) |
| 418 | `model.layers.10.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 419 | `model.layers.10.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.03339468562108648 / 1.5344851009976903 | [NPY](tensors/0000419.npy) |
| 420 | `model.layers.10.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -15.4375 / 16.25 / 0.035975509019971666 / 1.0996257532264149 | [NPY](tensors/0000420.npy) |
| 421 | `model.layers.10.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.03339468562108648 / 1.5344851009976903 | [NPY](tensors/0000421.npy) |
| 422 | `model.layers.10.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -56.5 / 17.0 / -0.0627367765878019 / 2.3913561713180207 | [NPY](tensors/0000422.npy) |
| 423 | `model.layers.10.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.03339468562108648 / 1.5344851009976903 | [NPY](tensors/0000423.npy) |
| 424 | `model.layers.10.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -10.5625 / 10.6875 / 0.06746418599132117 / 2.1319323093169835 | [NPY](tensors/0000424.npy) |
| 425 | `model.layers.10.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -7.75 / 8.4375 / 0.04570020822037549 / 1.0186830102327296 | [NPY](tensors/0000425.npy) |
| 426 | `model.layers.10.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -203.0 / 211.0 / 0.04765055700827253 / 4.18888981077133 | [NPY](tensors/0000426.npy) |
| 427 | `model.layers.10.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -203.0 / 211.0 / 0.04765055700827253 / 4.18888981077133 | [NPY](tensors/0000427.npy) |
| 428 | `model.layers.10.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.0022435416688268302 / 0.016102620186340826 | [NPY](tensors/0000428.npy) |
| 429 | `model.layers.10.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 920.0 / 0.39318454954736354 / 49.12966875990449 | [NPY](tensors/0000429.npy) |
| 430 | `model.layers.10.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -46.75 / 7.34375 / 0.012593223649335265 / 0.7328343875098091 | [NPY](tensors/0000430.npy) |
| 431 | `model.layers.10.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -46.75 / 7.34375 / 0.012593223649335265 / 0.7328343875098091 | [NPY](tensors/0000431.npy) |
| 432 | `model.layers.10.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -46.75 / 7.34375 / 0.012593223649335265 / 0.7328343875098091 | [NPY](tensors/0000432.npy) |
| 433 | `model.layers.10.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 434 | `model.layers.10.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 435 | `model.layers.10.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 436 | `model.layers.10.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -708.0 / 908.0 / 0.13023969149426914 / 7.926122285719806 | [NPY](tensors/0000436.npy) |
| 437 | `model.layers.10.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -708.0 / 908.0 / 0.13023969149426914 / 7.926122285719806 | [NPY](tensors/0000437.npy) |
| 438 | `model.layers.10.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -5.3125 / 4.03125 / -0.1166142153146004 / 0.6445168255905396 | [NPY](tensors/0000438.npy) |
| 439 | `model.layers.10` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.5235395466965523 / 50.9394114485589 | [NPY](tensors/0000439.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 440 | `model.layers.11` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.5235395466965523 / 50.9394114485589 | [NPY](tensors/0000440.npy) |
| 441 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000441.npy) |
| 442 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000442.npy) |
| 443 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000443.npy) |
| 444 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000444.npy) |
| 445 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 446 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 447 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 448 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.5235395466965523 / 50.9394114485589 | [NPY](tensors/0000448.npy) |
| 449 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -191.0 / 134.0 / 0.0679452244715287 / 3.1617651675123817 | [NPY](tensors/0000449.npy) |
| 450 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -191.0 / 134.0 / 0.0679452244715287 / 3.1617651675123817 | [NPY](tensors/0000450.npy) |
| 451 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000451.npy) |
| 452 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000452.npy) |
| 453 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 454 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 455 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000455.npy) |
| 456 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000456.npy) |
| 457 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 458 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -191.0 / 134.0 / 0.0679452244715287 / 3.1617651675123817 | [NPY](tensors/0000458.npy) |
| 459 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -12.0625 / 13.3125 / 0.03684885428152626 / 1.3412053122667167 | [NPY](tensors/0000459.npy) |
| 460 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -191.0 / 134.0 / 0.0679452244715287 / 3.1617651675123817 | [NPY](tensors/0000460.npy) |
| 461 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -38.25 / 48.25 / 0.06573239212782782 / 3.722043372158821 | [NPY](tensors/0000461.npy) |
| 462 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -191.0 / 134.0 / 0.0679452244715287 / 3.1617651675123817 | [NPY](tensors/0000462.npy) |
| 463 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.04044878493424412 / 2.5059310243135915 | [NPY](tensors/0000463.npy) |
| 464 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -11.6875 / 11.375 / -0.030547146341538607 / 1.463387680001409 | [NPY](tensors/0000464.npy) |
| 465 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -466.0 / 502.0 / -0.02721769352568355 / 6.55173096006312 | [NPY](tensors/0000465.npy) |
| 466 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -466.0 / 502.0 / -0.02721769352568355 / 6.55173096006312 | [NPY](tensors/0000466.npy) |
| 467 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003009450335703101 / 0.018245565585833647 | [NPY](tensors/0000467.npy) |
| 468 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 720.0 / 0.4963566048902313 / 50.208176528910165 | [NPY](tensors/0000468.npy) |
| 469 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -78.5 / 7.5625 / 0.011758664005353883 / 0.7849539773956085 | [NPY](tensors/0000469.npy) |
| 470 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -78.5 / 7.5625 / 0.011758664005353883 / 0.7849539773956085 | [NPY](tensors/0000470.npy) |
| 471 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -78.5 / 7.5625 / 0.011758664005353883 / 0.7849539773956085 | [NPY](tensors/0000471.npy) |
| 472 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 473 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 474 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 475 | `model.layers.11.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -540.0 / 450.0 / 0.11722387808403416 / 9.252880013290795 | [NPY](tensors/0000475.npy) |
| 476 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -540.0 / 450.0 / 0.11722387808403416 / 9.252880013290795 | [NPY](tensors/0000476.npy) |
| 477 | `model.layers.11.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -10.6875 / 2.859375 / -0.15139965654692192 / 0.7439421514323076 | [NPY](tensors/0000477.npy) |
| 478 | `model.layers.11` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.6135696261803026 / 52.63925534022176 | [NPY](tensors/0000478.npy) |

## Layer 0012

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 479 | `model.layers.12` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.6135696261803026 / 52.63925534022176 | [NPY](tensors/0000479.npy) |
| 480 | `model.layers.12` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000480.npy) |
| 481 | `model.layers.12` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000481.npy) |
| 482 | `model.layers.12` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000482.npy) |
| 483 | `model.layers.12` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000483.npy) |
| 484 | `model.layers.12` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 485 | `model.layers.12` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 486 | `model.layers.12` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 487 | `model.layers.12.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.6135696261803026 / 52.63925534022176 | [NPY](tensors/0000487.npy) |
| 488 | `model.layers.12.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -136.0 / 44.25 / 0.04192760136256863 / 1.5918620443496447 | [NPY](tensors/0000488.npy) |
| 489 | `model.layers.12.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -136.0 / 44.25 / 0.04192760136256863 / 1.5918620443496447 | [NPY](tensors/0000489.npy) |
| 490 | `model.layers.12.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000490.npy) |
| 491 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000491.npy) |
| 492 | `model.layers.12.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 493 | `model.layers.12.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 494 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000494.npy) |
| 495 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000495.npy) |
| 496 | `model.layers.12.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 497 | `model.layers.12.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -136.0 / 44.25 / 0.04192760136256863 / 1.5918620443496447 | [NPY](tensors/0000497.npy) |
| 498 | `model.layers.12.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -19.75 / 18.375 / -0.018090810349274893 / 1.3649999498081076 | [NPY](tensors/0000498.npy) |
| 499 | `model.layers.12.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -136.0 / 44.25 / 0.04192760136256863 / 1.5918620443496447 | [NPY](tensors/0000499.npy) |
| 500 | `model.layers.12.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -12.8125 / 13.125 / 0.0063668488660741105 / 1.3419208782806027 | [NPY](tensors/0000500.npy) |
| 501 | `model.layers.12.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -136.0 / 44.25 / 0.04192760136256863 / 1.5918620443496447 | [NPY](tensors/0000501.npy) |
| 502 | `model.layers.12.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -16.0 / 19.5 / 0.011131060916227802 / 2.8750077778800884 | [NPY](tensors/0000502.npy) |
| 503 | `model.layers.12.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -10.75 / 10.75 / -0.003634241125922974 / 1.5098172611599314 | [NPY](tensors/0000503.npy) |
| 504 | `model.layers.12.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -272.0 / 338.0 / -0.026450799916200293 / 5.856265870283301 | [NPY](tensors/0000504.npy) |
| 505 | `model.layers.12.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -272.0 / 338.0 / -0.026450799916200293 / 5.856265870283301 | [NPY](tensors/0000505.npy) |
| 506 | `model.layers.12.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 0.96875 / 0.002353330025196414 / 0.016778580228991886 | [NPY](tensors/0000506.npy) |
| 507 | `model.layers.12.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 728.0 / 0.5871642822614062 / 52.06594670630317 | [NPY](tensors/0000507.npy) |
| 508 | `model.layers.12.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -83.5 / 8.25 / 0.01173341529773082 / 0.8352139695237925 | [NPY](tensors/0000508.npy) |
| 509 | `model.layers.12.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -83.5 / 8.25 / 0.01173341529773082 / 0.8352139695237925 | [NPY](tensors/0000509.npy) |
| 510 | `model.layers.12.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -83.5 / 8.25 / 0.01173341529773082 / 0.8352139695237925 | [NPY](tensors/0000510.npy) |
| 511 | `model.layers.12.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 512 | `model.layers.12.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 513 | `model.layers.12.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 514 | `model.layers.12.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -1704.0 / 1512.0 / 0.14894657094707695 / 11.919495945535079 | [NPY](tensors/0000514.npy) |
| 515 | `model.layers.12.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -1704.0 / 1512.0 / 0.14894657094707695 / 11.919495945535079 | [NPY](tensors/0000515.npy) |
| 516 | `model.layers.12.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -6.9375 / 3.8125 / -0.14907477165032113 / 0.7693165147072295 | [NPY](tensors/0000516.npy) |
| 517 | `model.layers.12` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 1824.0 / 0.7361332306234013 / 55.74501755958564 | [NPY](tensors/0000517.npy) |

## Layer 0013

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 518 | `model.layers.13` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 1824.0 / 0.7361332306234013 / 55.74501755958564 | [NPY](tensors/0000518.npy) |
| 519 | `model.layers.13` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000519.npy) |
| 520 | `model.layers.13` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000520.npy) |
| 521 | `model.layers.13` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000521.npy) |
| 522 | `model.layers.13` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000522.npy) |
| 523 | `model.layers.13` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 524 | `model.layers.13` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 525 | `model.layers.13` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 526 | `model.layers.13.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 1824.0 / 0.7361332306234013 / 55.74501755958564 | [NPY](tensors/0000526.npy) |
| 527 | `model.layers.13.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -182.0 / 103.5 / 0.06520176273444724 / 2.8746480751932197 | [NPY](tensors/0000527.npy) |
| 528 | `model.layers.13.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -182.0 / 103.5 / 0.06520176273444724 / 2.8746480751932197 | [NPY](tensors/0000528.npy) |
| 529 | `model.layers.13.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000529.npy) |
| 530 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000530.npy) |
| 531 | `model.layers.13.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 532 | `model.layers.13.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 533 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000533.npy) |
| 534 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000534.npy) |
| 535 | `model.layers.13.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 536 | `model.layers.13.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -182.0 / 103.5 / 0.06520176273444724 / 2.8746480751932197 | [NPY](tensors/0000536.npy) |
| 537 | `model.layers.13.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -10.8125 / 12.6875 / 0.04246706495602579 / 1.412303509179438 | [NPY](tensors/0000537.npy) |
| 538 | `model.layers.13.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -182.0 / 103.5 / 0.06520176273444724 / 2.8746480751932197 | [NPY](tensors/0000538.npy) |
| 539 | `model.layers.13.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -65.0 / 31.25 / -0.3329939641376619 / 4.141396699497056 | [NPY](tensors/0000539.npy) |
| 540 | `model.layers.13.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -182.0 / 103.5 / 0.06520176273444724 / 2.8746480751932197 | [NPY](tensors/0000540.npy) |
| 541 | `model.layers.13.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -16.375 / 22.5 / 0.01353319864256102 / 2.8642636362109806 | [NPY](tensors/0000541.npy) |
| 542 | `model.layers.13.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -13.9375 / 20.875 / 0.006745168008082905 / 1.6426385257944645 | [NPY](tensors/0000542.npy) |
| 543 | `model.layers.13.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -560.0 / 1184.0 / -0.053269430923840184 / 8.81566484716767 | [NPY](tensors/0000543.npy) |
| 544 | `model.layers.13.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -560.0 / 1184.0 / -0.053269430923840184 / 8.81566484716767 | [NPY](tensors/0000544.npy) |
| 545 | `model.layers.13.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0032114328426054383 / 0.018323071603062572 | [NPY](tensors/0000545.npy) |
| 546 | `model.layers.13.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 1296.0 / 0.6829473678751773 / 54.501904150765256 | [NPY](tensors/0000546.npy) |
| 547 | `model.layers.13.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -86.0 / 6.875 / 0.011327882568300736 / 0.9172175902111699 | [NPY](tensors/0000547.npy) |
| 548 | `model.layers.13.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -86.0 / 6.875 / 0.011327882568300736 / 0.9172175902111699 | [NPY](tensors/0000548.npy) |
| 549 | `model.layers.13.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -86.0 / 6.875 / 0.011327882568300736 / 0.9172175902111699 | [NPY](tensors/0000549.npy) |
| 550 | `model.layers.13.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 551 | `model.layers.13.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 552 | `model.layers.13.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 553 | `model.layers.13.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -478.0 / 624.0 / 0.07657963351894151 / 12.793771729052695 | [NPY](tensors/0000553.npy) |
| 554 | `model.layers.13.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -478.0 / 624.0 / 0.07657963351894151 / 12.793771729052695 | [NPY](tensors/0000554.npy) |
| 555 | `model.layers.13.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -5.46875 / 3.796875 / -0.17449863313355904 / 0.8210326494219211 | [NPY](tensors/0000555.npy) |
| 556 | `model.layers.13` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 1160.0 / 0.759644304956547 / 58.82096151153353 | [NPY](tensors/0000556.npy) |

## Layer 0014

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 557 | `model.layers.14` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 1160.0 / 0.759644304956547 / 58.82096151153353 | [NPY](tensors/0000557.npy) |
| 558 | `model.layers.14` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000558.npy) |
| 559 | `model.layers.14` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000559.npy) |
| 560 | `model.layers.14` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000560.npy) |
| 561 | `model.layers.14` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000561.npy) |
| 562 | `model.layers.14` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 563 | `model.layers.14` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 564 | `model.layers.14` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 565 | `model.layers.14.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 1160.0 / 0.759644304956547 / 58.82096151153353 | [NPY](tensors/0000565.npy) |
| 566 | `model.layers.14.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -148.0 / 50.0 / 0.04897085417632106 / 1.950344499677016 | [NPY](tensors/0000566.npy) |
| 567 | `model.layers.14.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -148.0 / 50.0 / 0.04897085417632106 / 1.950344499677016 | [NPY](tensors/0000567.npy) |
| 568 | `model.layers.14.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000568.npy) |
| 569 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000569.npy) |
| 570 | `model.layers.14.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 571 | `model.layers.14.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 572 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000572.npy) |
| 573 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000573.npy) |
| 574 | `model.layers.14.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 575 | `model.layers.14.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -148.0 / 50.0 / 0.04897085417632106 / 1.950344499677016 | [NPY](tensors/0000575.npy) |
| 576 | `model.layers.14.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -53.25 / 29.25 / -0.06266819563769596 / 2.1311406284259253 | [NPY](tensors/0000576.npy) |
| 577 | `model.layers.14.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -148.0 / 50.0 / 0.04897085417632106 / 1.950344499677016 | [NPY](tensors/0000577.npy) |
| 578 | `model.layers.14.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -37.5 / 19.25 / 0.04056914015490814 / 1.6547292418269652 | [NPY](tensors/0000578.npy) |
| 579 | `model.layers.14.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -148.0 / 50.0 / 0.04897085417632106 / 1.950344499677016 | [NPY](tensors/0000579.npy) |
| 580 | `model.layers.14.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -23.0 / 23.0 / -0.02180534728481252 / 4.749184510013031 | [NPY](tensors/0000580.npy) |
| 581 | `model.layers.14.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -19.5 / 18.5 / -0.019502526275573757 / 2.648626254786815 | [NPY](tensors/0000581.npy) |
| 582 | `model.layers.14.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -306.0 / 334.0 / -0.026957346879449607 / 8.744818483319637 | [NPY](tensors/0000582.npy) |
| 583 | `model.layers.14.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -306.0 / 334.0 / -0.026957346879449607 / 8.744818483319637 | [NPY](tensors/0000583.npy) |
| 584 | `model.layers.14.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 0.9609375 / 0.0022960350770896746 / 0.019706016695222196 | [NPY](tensors/0000584.npy) |
| 585 | `model.layers.14.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 940.0 / 0.7327194726716958 / 57.93545243616031 | [NPY](tensors/0000585.npy) |
| 586 | `model.layers.14.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -99.0 / 9.4375 / 0.012532865386876063 / 0.9959096812258114 | [NPY](tensors/0000586.npy) |
| 587 | `model.layers.14.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -99.0 / 9.4375 / 0.012532865386876063 / 0.9959096812258114 | [NPY](tensors/0000587.npy) |
| 588 | `model.layers.14.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -99.0 / 9.4375 / 0.012532865386876063 / 0.9959096812258114 | [NPY](tensors/0000588.npy) |
| 589 | `model.layers.14.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 590 | `model.layers.14.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 591 | `model.layers.14.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 592 | `model.layers.14.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -1280.0 / 1128.0 / 0.023299909231925778 / 17.900862336605783 | [NPY](tensors/0000592.npy) |
| 593 | `model.layers.14.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -1280.0 / 1128.0 / 0.023299909231925778 / 17.900862336605783 | [NPY](tensors/0000593.npy) |
| 594 | `model.layers.14.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -6.84375 / 6.53125 / -0.24250661605617754 / 0.7642607139046002 | [NPY](tensors/0000594.npy) |
| 595 | `model.layers.14` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 2024.0 / 0.7559782632305105 / 65.39367848010545 | [NPY](tensors/0000595.npy) |

## Layer 0015

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 596 | `model.layers.15` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 2024.0 / 0.7559782632305105 / 65.39367848010545 | [NPY](tensors/0000596.npy) |
| 597 | `model.layers.15` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000597.npy) |
| 598 | `model.layers.15` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000598.npy) |
| 599 | `model.layers.15` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000599.npy) |
| 600 | `model.layers.15` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000600.npy) |
| 601 | `model.layers.15` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 602 | `model.layers.15` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 603 | `model.layers.15` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 604 | `model.layers.15.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 2024.0 / 0.7559782632305105 / 65.39367848010545 | [NPY](tensors/0000604.npy) |
| 605 | `model.layers.15.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04838628834352846 / 2.1861561793148714 | [NPY](tensors/0000605.npy) |
| 606 | `model.layers.15.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04838628834352846 / 2.1861561793148714 | [NPY](tensors/0000606.npy) |
| 607 | `model.layers.15.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000607.npy) |
| 608 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000608.npy) |
| 609 | `model.layers.15.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 610 | `model.layers.15.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 611 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000611.npy) |
| 612 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000612.npy) |
| 613 | `model.layers.15.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 614 | `model.layers.15.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04838628834352846 / 2.1861561793148714 | [NPY](tensors/0000614.npy) |
| 615 | `model.layers.15.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -21.25 / 17.875 / 0.009881157648971916 / 1.4641828991317716 | [NPY](tensors/0000615.npy) |
| 616 | `model.layers.15.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04838628834352846 / 2.1861561793148714 | [NPY](tensors/0000616.npy) |
| 617 | `model.layers.15.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -41.0 / 51.0 / 0.03270534597572562 / 4.165045554957253 | [NPY](tensors/0000617.npy) |
| 618 | `model.layers.15.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.04838628834352846 / 2.1861561793148714 | [NPY](tensors/0000618.npy) |
| 619 | `model.layers.15.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -61.5 / 38.5 / -0.13617969076298309 / 2.890695118769594 | [NPY](tensors/0000619.npy) |
| 620 | `model.layers.15.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -12.6875 / 20.75 / -0.10351759293686379 / 1.4637205012870276 | [NPY](tensors/0000620.npy) |
| 621 | `model.layers.15.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -1704.0 / 1736.0 / 0.019073719855364064 / 12.886400144173225 | [NPY](tensors/0000621.npy) |
| 622 | `model.layers.15.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -1704.0 / 1736.0 / 0.019073719855364064 / 12.886400144173225 | [NPY](tensors/0000622.npy) |
| 623 | `model.layers.15.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0026168533104091083 / 0.017337549315636715 | [NPY](tensors/0000623.npy) |
| 624 | `model.layers.15.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 1144.0 / 0.7750101901741073 / 63.92840520789068 | [NPY](tensors/0000624.npy) |
| 625 | `model.layers.15.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -106.0 / 10.1875 / 0.013699209364922844 / 1.007522644846197 | [NPY](tensors/0000625.npy) |
| 626 | `model.layers.15.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -106.0 / 10.1875 / 0.013699209364922844 / 1.007522644846197 | [NPY](tensors/0000626.npy) |
| 627 | `model.layers.15.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -106.0 / 10.1875 / 0.013699209364922844 / 1.007522644846197 | [NPY](tensors/0000627.npy) |
| 628 | `model.layers.15.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 629 | `model.layers.15.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 630 | `model.layers.15.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 631 | `model.layers.15.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -732.0 / 600.0 / -0.1898261428303566 / 20.66037515395136 | [NPY](tensors/0000631.npy) |
| 632 | `model.layers.15.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -732.0 / 600.0 / -0.1898261428303566 / 20.66037515395136 | [NPY](tensors/0000632.npy) |
| 633 | `model.layers.15.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -5.625 / 4.5 / -0.26127816434432605 / 0.916734677929029 | [NPY](tensors/0000633.npy) |
| 634 | `model.layers.15` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 1424.0 / 0.5853478790319404 / 72.98157189656015 | [NPY](tensors/0000634.npy) |

## Layer 0016

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 635 | `model.layers.16` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 1424.0 / 0.5853478790319404 / 72.98157189656015 | [NPY](tensors/0000635.npy) |
| 636 | `model.layers.16` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000636.npy) |
| 637 | `model.layers.16` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000637.npy) |
| 638 | `model.layers.16` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000638.npy) |
| 639 | `model.layers.16` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000639.npy) |
| 640 | `model.layers.16` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 641 | `model.layers.16` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 642 | `model.layers.16` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 643 | `model.layers.16.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 1424.0 / 0.5853478790319404 / 72.98157189656015 | [NPY](tensors/0000643.npy) |
| 644 | `model.layers.16.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -131.0 / 51.5 / 0.03549869986992667 / 1.9095661801793764 | [NPY](tensors/0000644.npy) |
| 645 | `model.layers.16.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -131.0 / 51.5 / 0.03549869986992667 / 1.9095661801793764 | [NPY](tensors/0000645.npy) |
| 646 | `model.layers.16.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000646.npy) |
| 647 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000647.npy) |
| 648 | `model.layers.16.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 649 | `model.layers.16.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 650 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000650.npy) |
| 651 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000651.npy) |
| 652 | `model.layers.16.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 653 | `model.layers.16.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -131.0 / 51.5 / 0.03549869986992667 / 1.9095661801793764 | [NPY](tensors/0000653.npy) |
| 654 | `model.layers.16.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -25.375 / 25.25 / 0.028294473618522303 / 1.721313806073371 | [NPY](tensors/0000654.npy) |
| 655 | `model.layers.16.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -131.0 / 51.5 / 0.03549869986992667 / 1.9095661801793764 | [NPY](tensors/0000655.npy) |
| 656 | `model.layers.16.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -14.875 / 32.0 / 0.040507451057752254 / 1.6522435534941047 | [NPY](tensors/0000656.npy) |
| 657 | `model.layers.16.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -131.0 / 51.5 / 0.03549869986992667 / 1.9095661801793764 | [NPY](tensors/0000657.npy) |
| 658 | `model.layers.16.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -22.625 / 21.75 / 0.01779189822512589 / 4.384581320373926 | [NPY](tensors/0000658.npy) |
| 659 | `model.layers.16.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -20.75 / 19.125 / 0.0011901805566356624 / 1.9732870767324018 | [NPY](tensors/0000659.npy) |
| 660 | `model.layers.16.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -548.0 / 544.0 / 0.044887679204206284 / 12.944432154035894 | [NPY](tensors/0000660.npy) |
| 661 | `model.layers.16.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -548.0 / 544.0 / 0.044887679204206284 / 12.944432154035894 | [NPY](tensors/0000661.npy) |
| 662 | `model.layers.16.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 0.953125 / 0.001871749701614307 / 0.016469020391314027 | [NPY](tensors/0000662.npy) |
| 663 | `model.layers.16.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 1464.0 / 0.6302199630173547 / 72.71917959397703 | [NPY](tensors/0000663.npy) |
| 664 | `model.layers.16.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -68.0 / 9.8125 / 0.012894632221417212 / 0.9756474386568615 | [NPY](tensors/0000664.npy) |
| 665 | `model.layers.16.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -68.0 / 9.8125 / 0.012894632221417212 / 0.9756474386568615 | [NPY](tensors/0000665.npy) |
| 666 | `model.layers.16.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -68.0 / 9.8125 / 0.012894632221417212 / 0.9756474386568615 | [NPY](tensors/0000666.npy) |
| 667 | `model.layers.16.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 668 | `model.layers.16.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 669 | `model.layers.16.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 670 | `model.layers.16.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -2400.0 / 1744.0 / -0.2355709239775694 / 31.72213309420455 | [NPY](tensors/0000670.npy) |
| 671 | `model.layers.16.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -2400.0 / 1744.0 / -0.2355709239775694 / 31.72213309420455 | [NPY](tensors/0000671.npy) |
| 672 | `model.layers.16.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -6.375 / 4.46875 / -0.30094537701046764 / 1.2053907412929028 | [NPY](tensors/0000672.npy) |
| 673 | `model.layers.16` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 2672.0 / 0.3947345599396609 / 90.72405722341578 | [NPY](tensors/0000673.npy) |

## Layer 0017

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 674 | `model.layers.17` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 2672.0 / 0.3947345599396609 / 90.72405722341578 | [NPY](tensors/0000674.npy) |
| 675 | `model.layers.17` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000675.npy) |
| 676 | `model.layers.17` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000676.npy) |
| 677 | `model.layers.17` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000677.npy) |
| 678 | `model.layers.17` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000678.npy) |
| 679 | `model.layers.17` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 680 | `model.layers.17` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 681 | `model.layers.17` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 682 | `model.layers.17.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 2672.0 / 0.3947345599396609 / 90.72405722341578 | [NPY](tensors/0000682.npy) |
| 683 | `model.layers.17.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -124.5 / 86.5 / 0.04354027877475208 / 2.720013042292766 | [NPY](tensors/0000683.npy) |
| 684 | `model.layers.17.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -124.5 / 86.5 / 0.04354027877475208 / 2.720013042292766 | [NPY](tensors/0000684.npy) |
| 685 | `model.layers.17.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000685.npy) |
| 686 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000686.npy) |
| 687 | `model.layers.17.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 688 | `model.layers.17.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 689 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000689.npy) |
| 690 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000690.npy) |
| 691 | `model.layers.17.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 692 | `model.layers.17.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -124.5 / 86.5 / 0.04354027877475208 / 2.720013042292766 | [NPY](tensors/0000692.npy) |
| 693 | `model.layers.17.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -20.125 / 20.875 / 0.011597107306106313 / 1.6016377942620295 | [NPY](tensors/0000693.npy) |
| 694 | `model.layers.17.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -124.5 / 86.5 / 0.04354027877475208 / 2.720013042292766 | [NPY](tensors/0000694.npy) |
| 695 | `model.layers.17.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -67.5 / 43.5 / -0.029119273249948154 / 5.0752174052347305 | [NPY](tensors/0000695.npy) |
| 696 | `model.layers.17.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -124.5 / 86.5 / 0.04354027877475208 / 2.720013042292766 | [NPY](tensors/0000696.npy) |
| 697 | `model.layers.17.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -19.625 / 21.75 / 0.13230445281042322 / 3.0805117292843707 | [NPY](tensors/0000697.npy) |
| 698 | `model.layers.17.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -10.125 / 11.625 / 0.07804609555875372 / 1.301363335995416 | [NPY](tensors/0000698.npy) |
| 699 | `model.layers.17.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -1512.0 / 1552.0 / 0.2897424545030623 / 20.20882338605003 | [NPY](tensors/0000699.npy) |
| 700 | `model.layers.17.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -1512.0 / 1552.0 / 0.2897424545030623 / 20.20882338605003 | [NPY](tensors/0000700.npy) |
| 701 | `model.layers.17.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 0.98828125 / 0.0026999038051678656 / 0.021010290418980025 | [NPY](tensors/0000701.npy) |
| 702 | `model.layers.17.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41216.0 / 1880.0 / 0.6843210491091425 / 86.79690298530674 | [NPY](tensors/0000702.npy) |
| 703 | `model.layers.17.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -41.75 / 10.5 / 0.011315530023735327 / 0.949959348890048 | [NPY](tensors/0000703.npy) |
| 704 | `model.layers.17.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41.75 / 10.5 / 0.011315530023735327 / 0.949959348890048 | [NPY](tensors/0000704.npy) |
| 705 | `model.layers.17.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -41.75 / 10.5 / 0.011315530023735327 / 0.949959348890048 | [NPY](tensors/0000705.npy) |
| 706 | `model.layers.17.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 707 | `model.layers.17.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 708 | `model.layers.17.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 709 | `model.layers.17.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -1176.0 / 40192.0 / -0.11607571731399952 / 58.00685222580546 | [NPY](tensors/0000709.npy) |
| 710 | `model.layers.17.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -1176.0 / 40192.0 / -0.11607571731399952 / 58.00685222580546 | [NPY](tensors/0000710.npy) |
| 711 | `model.layers.17.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -4.9375 / 2.609375 / -0.20023741246966706 / 0.9243221891414344 | [NPY](tensors/0000711.npy) |
| 712 | `model.layers.17` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -2416.0 / 2496.0 / 0.568349751223213 / 98.00905456808476 | [NPY](tensors/0000712.npy) |

## Layer 0018

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 713 | `model.layers.18` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -2416.0 / 2496.0 / 0.568349751223213 / 98.00905456808476 | [NPY](tensors/0000713.npy) |
| 714 | `model.layers.18` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000714.npy) |
| 715 | `model.layers.18` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000715.npy) |
| 716 | `model.layers.18` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000716.npy) |
| 717 | `model.layers.18` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000717.npy) |
| 718 | `model.layers.18` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 719 | `model.layers.18` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 720 | `model.layers.18` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 721 | `model.layers.18.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -2416.0 / 2496.0 / 0.568349751223213 / 98.00905456808476 | [NPY](tensors/0000721.npy) |
| 722 | `model.layers.18.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -45.25 / 39.25 / 0.021638823779923683 / 1.6005260395271566 | [NPY](tensors/0000722.npy) |
| 723 | `model.layers.18.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -45.25 / 39.25 / 0.021638823779923683 / 1.6005260395271566 | [NPY](tensors/0000723.npy) |
| 724 | `model.layers.18.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000724.npy) |
| 725 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000725.npy) |
| 726 | `model.layers.18.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 727 | `model.layers.18.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 728 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000728.npy) |
| 729 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000729.npy) |
| 730 | `model.layers.18.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 731 | `model.layers.18.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -45.25 / 39.25 / 0.021638823779923683 / 1.6005260395271566 | [NPY](tensors/0000731.npy) |
| 732 | `model.layers.18.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -26.0 / 31.875 / 0.12250027415246617 / 1.860623684366958 | [NPY](tensors/0000732.npy) |
| 733 | `model.layers.18.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -45.25 / 39.25 / 0.021638823779923683 / 1.6005260395271566 | [NPY](tensors/0000733.npy) |
| 734 | `model.layers.18.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -18.5 / 50.0 / 0.12238025766038385 / 2.2671073819635477 | [NPY](tensors/0000734.npy) |
| 735 | `model.layers.18.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -45.25 / 39.25 / 0.021638823779923683 / 1.6005260395271566 | [NPY](tensors/0000735.npy) |
| 736 | `model.layers.18.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -24.0 / 23.375 / -0.24901756718489623 / 4.332912981509934 | [NPY](tensors/0000736.npy) |
| 737 | `model.layers.18.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -18.125 / 20.625 / -0.12862192280204082 / 1.9036831606357936 | [NPY](tensors/0000737.npy) |
| 738 | `model.layers.18.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -596.0 / 740.0 / -0.2880534911773489 / 21.122204493939584 | [NPY](tensors/0000738.npy) |
| 739 | `model.layers.18.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -596.0 / 740.0 / -0.2880534911773489 / 21.122204493939584 | [NPY](tensors/0000739.npy) |
| 740 | `model.layers.18.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.001676572632365299 / 0.017839599827510936 | [NPY](tensors/0000740.npy) |
| 741 | `model.layers.18.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -2400.0 / 2464.0 / 0.2804356846143814 / 104.6733172859639 | [NPY](tensors/0000741.npy) |
| 742 | `model.layers.18.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -8.1875 / 13.125 / 0.004870022245903362 / 0.9133835759012822 | [NPY](tensors/0000742.npy) |
| 743 | `model.layers.18.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -8.1875 / 13.125 / 0.004870022245903362 / 0.9133835759012822 | [NPY](tensors/0000743.npy) |
| 744 | `model.layers.18.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -8.1875 / 13.125 / 0.004870022245903362 / 0.9133835759012822 | [NPY](tensors/0000744.npy) |
| 745 | `model.layers.18.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 746 | `model.layers.18.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 747 | `model.layers.18.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 748 | `model.layers.18.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -2112.0 / 2832.0 / 0.16205252929844371 / 54.232844665853754 | [NPY](tensors/0000748.npy) |
| 749 | `model.layers.18.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -2112.0 / 2832.0 / 0.16205252929844371 / 54.232844665853754 | [NPY](tensors/0000749.npy) |
| 750 | `model.layers.18.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -4.9375 / 2.640625 / -0.325795341641029 / 1.0116997844440327 | [NPY](tensors/0000750.npy) |
| 751 | `model.layers.18` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.44220463521587083 / 143.48067458856588 | [NPY](tensors/0000751.npy) |

## Layer 0019

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 752 | `model.layers.19` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.44220463521587083 / 143.48067458856588 | [NPY](tensors/0000752.npy) |
| 753 | `model.layers.19` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000753.npy) |
| 754 | `model.layers.19` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000754.npy) |
| 755 | `model.layers.19` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000755.npy) |
| 756 | `model.layers.19` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000756.npy) |
| 757 | `model.layers.19` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 758 | `model.layers.19` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 759 | `model.layers.19` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 760 | `model.layers.19.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -4160.0 / 4352.0 / 0.44220463521587083 / 143.48067458856588 | [NPY](tensors/0000760.npy) |
| 761 | `model.layers.19.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -78.0 / 41.75 / 0.01376926938845924 / 1.836016455996056 | [NPY](tensors/0000761.npy) |
| 762 | `model.layers.19.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -78.0 / 41.75 / 0.01376926938845924 / 1.836016455996056 | [NPY](tensors/0000762.npy) |
| 763 | `model.layers.19.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000763.npy) |
| 764 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000764.npy) |
| 765 | `model.layers.19.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 766 | `model.layers.19.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 767 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000767.npy) |
| 768 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000768.npy) |
| 769 | `model.layers.19.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 770 | `model.layers.19.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -78.0 / 41.75 / 0.01376926938845924 / 1.836016455996056 | [NPY](tensors/0000770.npy) |
| 771 | `model.layers.19.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -16.25 / 24.5 / -0.03767411982474856 / 1.3113854837453593 | [NPY](tensors/0000771.npy) |
| 772 | `model.layers.19.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -78.0 / 41.75 / 0.01376926938845924 / 1.836016455996056 | [NPY](tensors/0000772.npy) |
| 773 | `model.layers.19.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -82.0 / 71.0 / -0.09810243877731396 / 7.1106891791920175 | [NPY](tensors/0000773.npy) |
| 774 | `model.layers.19.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -78.0 / 41.75 / 0.01376926938845924 / 1.836016455996056 | [NPY](tensors/0000774.npy) |
| 775 | `model.layers.19.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -16.125 / 15.625 / -0.02733677707851145 / 3.1878306017260365 | [NPY](tensors/0000775.npy) |
| 776 | `model.layers.19.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -11.375 / 11.25 / -0.011878023123393183 / 0.9709118464286557 | [NPY](tensors/0000776.npy) |
| 777 | `model.layers.19.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -2176.0 / 1928.0 / -0.6042687912465332 / 42.694143758911274 | [NPY](tensors/0000777.npy) |
| 778 | `model.layers.19.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -2176.0 / 1928.0 / -0.6042687912465332 / 42.694143758911274 | [NPY](tensors/0000778.npy) |
| 779 | `model.layers.19.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 0.98046875 / 0.0014323097285122211 / 0.01032618245376766 | [NPY](tensors/0000779.npy) |
| 780 | `model.layers.19.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -3616.0 / 3312.0 / -0.16203150298577518 / 125.7277381971097 | [NPY](tensors/0000780.npy) |
| 781 | `model.layers.19.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -7.15625 / 18.75 / 0.0028226204502247876 / 0.9921160121886847 | [NPY](tensors/0000781.npy) |
| 782 | `model.layers.19.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -7.15625 / 18.75 / 0.0028226204502247876 / 0.9921160121886847 | [NPY](tensors/0000782.npy) |
| 783 | `model.layers.19.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -7.15625 / 18.75 / 0.0028226204502247876 / 0.9921160121886847 | [NPY](tensors/0000783.npy) |
| 784 | `model.layers.19.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 785 | `model.layers.19.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 786 | `model.layers.19.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 787 | `model.layers.19.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -2640.0 / 2688.0 / 0.2661263621244661 / 86.49721758832311 | [NPY](tensors/0000787.npy) |
| 788 | `model.layers.19.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -2640.0 / 2688.0 / 0.2661263621244661 / 86.49721758832311 | [NPY](tensors/0000788.npy) |
| 789 | `model.layers.19.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -6.21875 / 3.046875 / -0.2874046271381853 / 1.441322272893593 | [NPY](tensors/0000789.npy) |
| 790 | `model.layers.19` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -5024.0 / 4672.0 / 0.10413473633826131 / 186.27826611811167 | [NPY](tensors/0000790.npy) |

## Layer 0020

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 791 | `model.layers.20` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -5024.0 / 4672.0 / 0.10413473633826131 / 186.27826611811167 | [NPY](tensors/0000791.npy) |
| 792 | `model.layers.20` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000792.npy) |
| 793 | `model.layers.20` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000793.npy) |
| 794 | `model.layers.20` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000794.npy) |
| 795 | `model.layers.20` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000795.npy) |
| 796 | `model.layers.20` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 797 | `model.layers.20` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 798 | `model.layers.20` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 799 | `model.layers.20.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -5024.0 / 4672.0 / 0.10413473633826131 / 186.27826611811167 | [NPY](tensors/0000799.npy) |
| 800 | `model.layers.20.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.009331219648951925 / 1.5371317629574877 | [NPY](tensors/0000800.npy) |
| 801 | `model.layers.20.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.009331219648951925 / 1.5371317629574877 | [NPY](tensors/0000801.npy) |
| 802 | `model.layers.20.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000802.npy) |
| 803 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000803.npy) |
| 804 | `model.layers.20.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 805 | `model.layers.20.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 806 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000806.npy) |
| 807 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000807.npy) |
| 808 | `model.layers.20.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 809 | `model.layers.20.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.009331219648951925 / 1.5371317629574877 | [NPY](tensors/0000809.npy) |
| 810 | `model.layers.20.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -21.25 / 20.625 / 0.044822830933752104 / 1.2429888018185284 | [NPY](tensors/0000810.npy) |
| 811 | `model.layers.20.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.009331219648951925 / 1.5371317629574877 | [NPY](tensors/0000811.npy) |
| 812 | `model.layers.20.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -29.25 / 37.0 / -0.09848684714145932 / 2.2553528885475966 | [NPY](tensors/0000812.npy) |
| 813 | `model.layers.20.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -41.75 / 38.75 / 0.009331219648951925 / 1.5371317629574877 | [NPY](tensors/0000813.npy) |
| 814 | `model.layers.20.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -22.125 / 21.5 / 0.0221817815523873 / 3.9633930380634697 | [NPY](tensors/0000814.npy) |
| 815 | `model.layers.20.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -17.5 / 17.25 / -0.002786859728891429 / 1.3088868479859972 | [NPY](tensors/0000815.npy) |
| 816 | `model.layers.20.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -1012.0 / 1096.0 / -0.25971007489931824 / 25.752730720481857 | [NPY](tensors/0000816.npy) |
| 817 | `model.layers.20.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -1012.0 / 1096.0 / -0.25971007489931824 / 25.752730720481857 | [NPY](tensors/0000817.npy) |
| 818 | `model.layers.20.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0013985135882117006 / 0.014886137037170247 | [NPY](tensors/0000818.npy) |
| 819 | `model.layers.20.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -4928.0 / 4864.0 / -0.15605905557536662 / 189.8242408524477 | [NPY](tensors/0000819.npy) |
| 820 | `model.layers.20.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -6.96875 / 19.125 / 0.00034662794016858444 / 0.9475214945925691 | [NPY](tensors/0000820.npy) |
| 821 | `model.layers.20.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -6.96875 / 19.125 / 0.00034662794016858444 / 0.9475214945925691 | [NPY](tensors/0000821.npy) |
| 822 | `model.layers.20.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -6.96875 / 19.125 / 0.00034662794016858444 / 0.9475214945925691 | [NPY](tensors/0000822.npy) |
| 823 | `model.layers.20.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 824 | `model.layers.20.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 825 | `model.layers.20.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 826 | `model.layers.20.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -5888.0 / 6816.0 / 0.3755452022575116 / 83.17961448952619 | [NPY](tensors/0000826.npy) |
| 827 | `model.layers.20.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -5888.0 / 6816.0 / 0.3755452022575116 / 83.17961448952619 | [NPY](tensors/0000827.npy) |
| 828 | `model.layers.20.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -5.3125 / 3.578125 / -0.185098195839607 / 1.1856852864902139 | [NPY](tensors/0000828.npy) |
| 829 | `model.layers.20` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -9152.0 / 10368.0 / 0.21979196713629706 / 249.96287265756595 | [NPY](tensors/0000829.npy) |

## Layer 0021

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 830 | `model.layers.21` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -9152.0 / 10368.0 / 0.21979196713629706 / 249.96287265756595 | [NPY](tensors/0000830.npy) |
| 831 | `model.layers.21` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000831.npy) |
| 832 | `model.layers.21` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000832.npy) |
| 833 | `model.layers.21` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000833.npy) |
| 834 | `model.layers.21` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000834.npy) |
| 835 | `model.layers.21` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 836 | `model.layers.21` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 837 | `model.layers.21` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 838 | `model.layers.21.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -9152.0 / 10368.0 / 0.21979196713629706 / 249.96287265756595 | [NPY](tensors/0000838.npy) |
| 839 | `model.layers.21.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.00512025589797279 / 1.8108818367286552 | [NPY](tensors/0000839.npy) |
| 840 | `model.layers.21.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.00512025589797279 / 1.8108818367286552 | [NPY](tensors/0000840.npy) |
| 841 | `model.layers.21.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000841.npy) |
| 842 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000842.npy) |
| 843 | `model.layers.21.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 844 | `model.layers.21.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 845 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000845.npy) |
| 846 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000846.npy) |
| 847 | `model.layers.21.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 848 | `model.layers.21.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.00512025589797279 / 1.8108818367286552 | [NPY](tensors/0000848.npy) |
| 849 | `model.layers.21.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -20.125 / 36.5 / 0.022310547188933542 / 1.1599538667417806 | [NPY](tensors/0000849.npy) |
| 850 | `model.layers.21.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.00512025589797279 / 1.8108818367286552 | [NPY](tensors/0000850.npy) |
| 851 | `model.layers.21.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -100.0 / 99.5 / -0.15984803818007168 / 8.019973691176126 | [NPY](tensors/0000851.npy) |
| 852 | `model.layers.21.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.00512025589797279 / 1.8108818367286552 | [NPY](tensors/0000852.npy) |
| 853 | `model.layers.21.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -21.875 / 23.0 / -0.009628491681665713 / 3.165529499696907 | [NPY](tensors/0000853.npy) |
| 854 | `model.layers.21.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -16.625 / 13.5625 / 0.0033161587938467353 / 0.7275236470009667 | [NPY](tensors/0000854.npy) |
| 855 | `model.layers.21.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -5152.0 / 4704.0 / -0.650096559777308 / 80.73109484701921 | [NPY](tensors/0000855.npy) |
| 856 | `model.layers.21.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -5152.0 / 4704.0 / -0.650096559777308 / 80.73109484701921 | [NPY](tensors/0000856.npy) |
| 857 | `model.layers.21.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 0.9375 / 0.0013950582453213217 / 0.007845755694968348 | [NPY](tensors/0000857.npy) |
| 858 | `model.layers.21.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -5856.0 / 6112.0 / -0.4312966412732421 / 205.14575650122353 | [NPY](tensors/0000858.npy) |
| 859 | `model.layers.21.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -8.8125 / 26.75 / 8.181213283783932e-05 / 1.073018703765474 | [NPY](tensors/0000859.npy) |
| 860 | `model.layers.21.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -8.8125 / 26.75 / 8.181213283783932e-05 / 1.073018703765474 | [NPY](tensors/0000860.npy) |
| 861 | `model.layers.21.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -8.8125 / 26.75 / 8.181213283783932e-05 / 1.073018703765474 | [NPY](tensors/0000861.npy) |
| 862 | `model.layers.21.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 863 | `model.layers.21.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 864 | `model.layers.21.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 865 | `model.layers.21.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -6208.0 / 5664.0 / -0.9590526408477942 / 156.28347283825366 | [NPY](tensors/0000865.npy) |
| 866 | `model.layers.21.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -6208.0 / 5664.0 / -0.9590526408477942 / 156.28347283825366 | [NPY](tensors/0000866.npy) |
| 867 | `model.layers.21.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -5.8125 / 4.40625 / -0.23075414297843744 / 1.5290326619876635 | [NPY](tensors/0000867.npy) |
| 868 | `model.layers.21` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -9216.0 / 9792.0 / -1.3906032231920271 / 315.85470120094425 | [NPY](tensors/0000868.npy) |

## Layer 0022

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 869 | `model.layers.22` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -9216.0 / 9792.0 / -1.3906032231920271 / 315.85470120094425 | [NPY](tensors/0000869.npy) |
| 870 | `model.layers.22` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000870.npy) |
| 871 | `model.layers.22` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000871.npy) |
| 872 | `model.layers.22` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000872.npy) |
| 873 | `model.layers.22` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000873.npy) |
| 874 | `model.layers.22` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 875 | `model.layers.22` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 876 | `model.layers.22` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 877 | `model.layers.22.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -9216.0 / 9792.0 / -1.3906032231920271 / 315.85470120094425 | [NPY](tensors/0000877.npy) |
| 878 | `model.layers.22.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -43.25 / 48.75 / -0.0006167952656250972 / 1.727256971964591 | [NPY](tensors/0000878.npy) |
| 879 | `model.layers.22.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -43.25 / 48.75 / -0.0006167952656250972 / 1.727256971964591 | [NPY](tensors/0000879.npy) |
| 880 | `model.layers.22.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.194453390280363e+38 / 1.619426740081737e+38 | [NPY](tensors/0000880.npy) |
| 881 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000881.npy) |
| 882 | `model.layers.22.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 883 | `model.layers.22.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 884 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000884.npy) |
| 885 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000885.npy) |
| 886 | `model.layers.22.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 887 | `model.layers.22.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -43.25 / 48.75 / -0.0006167952656250972 / 1.727256971964591 | [NPY](tensors/0000887.npy) |
| 888 | `model.layers.22.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -39.75 / 31.625 / -0.051864399378301174 / 2.474712312237656 | [NPY](tensors/0000888.npy) |
| 889 | `model.layers.22.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -43.25 / 48.75 / -0.0006167952656250972 / 1.727256971964591 | [NPY](tensors/0000889.npy) |
| 890 | `model.layers.22.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -32.75 / 9.125 / -0.054860488175218956 / 1.382685372447965 | [NPY](tensors/0000890.npy) |
| 891 | `model.layers.22.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -43.25 / 48.75 / -0.0006167952656250972 / 1.727256971964591 | [NPY](tensors/0000891.npy) |
| 892 | `model.layers.22.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -27.875 / 27.5 / -0.014537163794677028 / 4.4017754353894185 | [NPY](tensors/0000892.npy) |
| 893 | `model.layers.22.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -19.875 / 14.625 / -0.02145313910783229 / 1.4697566582247108 | [NPY](tensors/0000893.npy) |
| 894 | `model.layers.22.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -2144.0 / 1840.0 / -0.44016219228859615 / 39.81703985284256 | [NPY](tensors/0000894.npy) |
| 895 | `model.layers.22.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -2144.0 / 1840.0 / -0.44016219228859615 / 39.81703985284256 | [NPY](tensors/0000895.npy) |
| 896 | `model.layers.22.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 0.9375 / 0.0013884764792257557 / 0.01486095118718588 | [NPY](tensors/0000896.npy) |
| 897 | `model.layers.22.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -9920.0 / 10432.0 / -1.8316025697369498 / 324.82853879233505 | [NPY](tensors/0000897.npy) |
| 898 | `model.layers.22.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -20.25 / 21.625 / -0.008788262111141823 / 0.9780795885940361 | [NPY](tensors/0000898.npy) |
| 899 | `model.layers.22.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -20.25 / 21.625 / -0.008788262111141823 / 0.9780795885940361 | [NPY](tensors/0000899.npy) |
| 900 | `model.layers.22.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -20.25 / 21.625 / -0.008788262111141823 / 0.9780795885940361 | [NPY](tensors/0000900.npy) |
| 901 | `model.layers.22.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 902 | `model.layers.22.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 903 | `model.layers.22.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 904 | `model.layers.22.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -6656.0 / 6368.0 / -0.012548856680550658 / 155.424255161132 | [NPY](tensors/0000904.npy) |
| 905 | `model.layers.22.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -6656.0 / 6368.0 / -0.012548856680550658 / 155.424255161132 | [NPY](tensors/0000905.npy) |
| 906 | `model.layers.22.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -7.40625 / 4.8125 / -0.18473260767519262 / 1.4424333629584971 | [NPY](tensors/0000906.npy) |
| 907 | `model.layers.22` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -1.8433740587939667 / 417.2148157457952 | [NPY](tensors/0000907.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 908 | `model.layers.23` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -1.8433740587939667 / 417.2148157457952 | [NPY](tensors/0000908.npy) |
| 909 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000909.npy) |
| 910 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000910.npy) |
| 911 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000911.npy) |
| 912 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000912.npy) |
| 913 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 914 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 915 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 916 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -12928.0 / 14016.0 / -1.8433740587939667 / 417.2148157457952 | [NPY](tensors/0000916.npy) |
| 917 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.008153073052765589 / 1.7564214492961185 | [NPY](tensors/0000917.npy) |
| 918 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 281, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.008153073052765589 / 1.7564214492961185 | [NPY](tensors/0000918.npy) |
| 919 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 281, 281] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6887344999829714e+38 / 1.6947549629287244e+38 | [NPY](tensors/0000919.npy) |
| 920 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 281] | torch.int64 → int64 | 0.0 / 280.0 / 140.0 / 81.11719916269298 | [NPY](tensors/0000920.npy) |
| 921 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 922 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 923 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8072647361144476 / 0.8697748884974921 | [NPY](tensors/0000923.npy) |
| 924 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 281, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11802216233611869 / 0.6223520199620735 | [NPY](tensors/0000924.npy) |
| 925 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 926 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.008153073052765589 / 1.7564214492961185 | [NPY](tensors/0000926.npy) |
| 927 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 281, 4096] | torch.bfloat16 → float32 | -18.5 / 24.25 / 0.032352424562246546 / 1.6361111527342054 | [NPY](tensors/0000927.npy) |
| 928 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.008153073052765589 / 1.7564214492961185 | [NPY](tensors/0000928.npy) |
| 929 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -83.0 / 59.5 / -0.07505329643969434 / 5.048101783417991 | [NPY](tensors/0000929.npy) |
| 930 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -53.0 / 72.0 / 0.008153073052765589 / 1.7564214492961185 | [NPY](tensors/0000930.npy) |
| 931 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 281, 512] | torch.bfloat16 → float32 | -28.375 / 24.25 / 0.02288577883269015 / 3.19808560464058 | [NPY](tensors/0000931.npy) |
| 932 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 281, 4096] | torch.bfloat16 → float32 | -27.125 / 12.9375 / -0.0007809507453293593 / 1.151134266795639 | [NPY](tensors/0000932.npy) |
| 933 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -6528.0 / 6816.0 / 2.5821173260031887 / 170.6067466990671 | [NPY](tensors/0000933.npy) |
| 934 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -6528.0 / 6816.0 / 2.5821173260031887 / 170.6067466990671 | [NPY](tensors/0000934.npy) |
| 935 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 281, 281] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.001744389633977013 / 0.013023545922247071 | [NPY](tensors/0000935.npy) |
| 936 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -11328.0 / 11200.0 / 0.7372392373105764 / 371.6161138772754 | [NPY](tensors/0000936.npy) |
| 937 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -52.5 / 23.0 / -0.016779625413445156 / 1.2327399979565035 | [NPY](tensors/0000937.npy) |
| 938 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -52.5 / 23.0 / -0.016779625413445156 / 1.2327399979565035 | [NPY](tensors/0000938.npy) |
| 939 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [281, 2880] | torch.bfloat16 → float32 | -52.5 / 23.0 / -0.016779625413445156 / 1.2327399979565035 | [NPY](tensors/0000939.npy) |
| 940 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 941 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 942 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 943 | `model.layers.23.mlp.experts` | 0 | `output` | [281, 2880] | torch.bfloat16 → float32 | -4832.0 / 4704.0 / -1.6059714248313317 / 151.38017120207215 | [NPY](tensors/0000943.npy) |
| 944 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 281, 2880] | torch.bfloat16 → float32 | -4832.0 / 4704.0 / -1.6059714248313317 / 151.38017120207215 | [NPY](tensors/0000944.npy) |
| 945 | `model.layers.23.mlp` | 0 | `output[1]` | [281, 32] | torch.bfloat16 → float32 | -8.125 / 4.4375 / 0.23861856392694114 / 2.5061858627777927 | [NPY](tensors/0000945.npy) |
| 946 | `model.layers.23` | 0 | `output` | [1, 281, 2880] | torch.bfloat16 → float32 | -10944.0 / 10880.0 / -0.8688804400207591 / 413.1514180610229 | [NPY](tensors/0000946.npy) |

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
